---
title: "外部签名：拓扑交易"
slug: "appdev-deep-dives-external-signing-topology"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/external-signing-topology.md"
source_title: "External Signing: Topology Transactions"
tags:
  - appdev
  - deep-dives
  - external-signing-topology
---

# 外部签名：拓扑交易

> 使用外部密钥构建、签署并提交 Canton 拓扑交易。

Canton [拓扑](/zh/docs/canton/overview-reference-topology) 形式化 synchronizer 上的共享状态，并提供安全的分布式变更机制(/overview/reference/topology) formalizes a shared state on a synchronizer and provides a secure, distributed mechanism for modifying this state.

本教程演示如何构建、签署并提交拓扑交易，适用于签名密钥在网外的场景，例如外部 Party 入网或 participant 根命名空间初始化。流程以导入根命名空间委托为例，可推广到任意拓扑映射, sign, and submit topology transactions. It is particularly useful for cases where the signature is provided by a key held externally to the network, such as in the case of external party onboarding, or initialization

<Warning>
  本教程仅供演示，代码片段请勿直接用于生产
</Warning> purposes. The code snippets should not be used directly in a production environment.
</Warning>

## 前提条件
为简化起见，假设一个 participant 连接一个 synchronizer a minimal Canton setup consisting of one participant node connected to one synchronizer (which includes both a sequencer node and a mediator node).

### 启动 Canton
获取 Canton 制品见 getting started，执行： refer to the getting started section. From the artifact directory, start Canton using the command:

```
./bin/canton -c examples/01-simple-topology/simple-topology.conf --bootstrap examples/01-simple-topology/simple-ping.canton
```

出现 “Welcome to Canton” 后继续 message appears, you are ready to proceed.

### 配置
进入发行包 `examples/08-interactive-submission` example folder located at `examples/08-interactive-submission` in the Canton release artifact.

<Tip>
  本教程代码摘自该目录脚本
</Tip> in this tutorial are extracted from scripts located in that folder.
</Tip>

在 Canton 控制台收集： information by running the commands below in the Canton console:

* Admin API 端点
* Synchronizer ID```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.adminApi.address
    res1: String = "127.0.0.1"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.adminApi.port.unwrap
    res2: Int = 30044
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.synchronizer_id.toProtoPrimitive
    res3: String = "da::1220a82692abc55c0367abefc4bdbc23df25688230430ddfeef5759845f26d5cc29c"
```

下文示例值请替换为你自己的： the following values, but make sure to replace them with your own:

* Admin API endpoint: `localhost:4002`
* Synchronizer ID: `da::12207a94aca813c822c6ae10a1b5478c2ba1077447b468cc66dbd255f60f8fa333e1`

### API
本教程使用 participant **Admin API** 的 `TopologyManagerWriteService` gRPC 服务，假设 Admin API 未启用客户端证书认证 `TopologyManagerWriteService`, a gRPC service available on the **Admin API**

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

syntax = "proto3";

package com.digitalasset.canton.topology.admin.v30;

import "com/digitalasset/canton/protocol/v30/topology.proto";
import "com/digitalasset/canton/topology/admin/v30/common.proto";
import "google/protobuf/duration.proto";

/**
 * Write operations on the local topology manager.
 *
 * Participants, mediators, and sequencers run a local topology manager exposing the same write interface.
 */
service TopologyManagerWriteService {
  rpc Authorize(AuthorizeRequest) returns (AuthorizeResponse);

  rpc AddTransactions(AddTransactionsRequest) returns (AddTransactionsResponse);

  rpc ImportTopologySnapshot(stream ImportTopologySnapshotRequest) returns (ImportTopologySnapshotResponse);
  rpc ImportTopologySnapshotV2(stream ImportTopologySnapshotV2Request) returns (ImportTopologySnapshotV2Response);

  rpc SignTransactions(SignTransactionsRequest) returns (SignTransactionsResponse);

  /** RPC to generate topology transactions that can be signed */
  rpc GenerateTransactions(GenerateTransactionsRequest) returns (GenerateTransactionsResponse);

  /** Creates a temporary topology store.
   * Trying to create a store with the same name results in an error.
   */
  rpc CreateTemporaryTopologyStore(CreateTemporaryTopologyStoreRequest) returns (CreateTemporaryTopologyStoreResponse);

  /** Drops a temporary topology store.
   * Trying to drop a temporary store that does not exist results in an error.
   */
  rpc DropTemporaryTopologyStore(DropTemporaryTopologyStoreRequest) returns (DropTemporaryTopologyStoreResponse);
}

message GenerateTransactionsRequest {
  message Proposal {
    /** Replace / Remove */
    com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp operation = 1;

    /** Optionally, the serial number of this request (auto-determined if omitted)
     * NOTE: omitting the serial MAY end up overwriting previous mappings processed concurrently.
     * To avoid such cases, First read the state using the TopologyManagerReadService and update the mappings
     * accordingly, incrementing the serial by one and setting it here explicitly.
     */
    uint32 serial = 2;

    /** The mapping to be authorized */
    com.digitalasset.canton.protocol.v30.TopologyMapping mapping = 3;

    // Target store
    StoreId store = 4;
  }
  // transaction proposals for which to generate topology transactions
  repeated Proposal proposals = 1;
}

message GenerateTransactionsResponse {
  message GeneratedTransaction {
    // Serialized com.digitalasset.canton.protocol.v30.TopologyTransaction
    bytes serialized_transaction = 1;
    // Hash of the transaction - this should be signed by the submitter to authorize the transaction
    bytes transaction_hash = 2;
  }
  // Generated transactions, in the same order as the mappings provided in the request
  repeated GeneratedTransaction generated_transactions = 1;
}

message AuthorizeRequest {
  message Proposal {
    /** Replace / Remove */
    com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp change = 1;

    /** Optionally, the serial number of this request (auto-determined if omitted) */
    uint32 serial = 2;

    /** The mapping to be authorized */
    com.digitalasset.canton.protocol.v30.TopologyMapping mapping = 3;
  }

  oneof type {
    /**
     * Propose a transaction and distribute it.
     * If authorize if the node has enough signing keys
     */
    Proposal proposal = 1;
    /**
     * Authorize a transaction, meaning the node needs to be able to fully sign it locally.
     * Hash is in hexadecimal format.
     */
    string transaction_hash = 2;
  }

  /**
   * If true: the transaction is only signed if the new signatures will result in the transaction being fully
   * authorized. Otherwise returns as an error.
   * If false: the transaction is signed and the signature distributed. The transaction may still not be fully
   * authorized and remain as a proposal.
   */
  bool must_fully_authorize = 3;

  /** Force specific changes even if dangerous */
  repeated ForceFlag force_changes = 4;

  /**
   * Fingerprint of the keys signing the authorization
   *
   * The signing key is used to identify a particular `NamespaceDelegation` certificate,
   * which is used to justify the given authorization.
   * Optional, if empty, suitable signing keys available known to the node are automatically selected.
   */
  repeated string signed_by = 5;

  /**
   * The store that is used as the underlying source for executing this request.
   * If `store` is a synchronizer store, the resulting topology transaction will only be available on the respective synchronizer.
   * If `store` is the authorized store, the resulting topology transaction may or may not be synchronized automatically
   * to all synchronizers that the node is currently connected to or will be connected to in the future.
   *
   * Selecting a specific synchronizers store might be necessary, if the transaction to authorize by hash or the previous
   * generation of the submitted proposal is only available on the synchronizers store and not in the authorized store.
   */
  StoreId store = 6;

  /** Optional timeout to wait for the transaction to become effective in the store. */
  google.protobuf.Duration wait_to_become_effective = 7;
}

message AuthorizeResponse {
  /** the generated signed topology transaction */
  com.digitalasset.canton.protocol.v30.SignedTopologyTransaction transaction = 1;
}

message AddTransactionsRequest {
  /**
   * The transactions that should be added to the target store as indicated by the parameter `store`.
   */
  repeated com.digitalasset.canton.protocol.v30.SignedTopologyTransaction transactions = 1;

  /** Force specific changes even if dangerous */
  repeated ForceFlag force_changes = 2;

  /**
   * The store that is used as the underlying source for executing this request.
   * If `store` is a synchronizers store, the resulting topology transaction will only be available on the respective synchronizers.
   * If `store` is the authorized store, the resulting topology transaction may or may not be synchronized automatically
   * to all synchronizers that the node is currently connected to or will be connected to in the future.
   *
   * Selecting a specific synchronizers store might be necessary, if the transaction to authorize by hash or the previous
   * generation of the submitted proposal is only available on the synchronizers store and not in the authorized store.
   */
  StoreId store = 3;

  /** Optional timeout to wait for the transaction to become effective in the store. */
  google.protobuf.Duration wait_to_become_effective = 7;
}
message AddTransactionsResponse {}

/**
 * Same message as AddTransactionsRequest, except that transactions are encoded in a byte string
 */
message ImportTopologySnapshotRequest {
  bytes topology_snapshot = 1;
  StoreId store = 2;
  /** Optional timeout to wait for the transaction to become effective in the store. */
  google.protobuf.Duration wait_to_become_effective = 3;
}
message ImportTopologySnapshotResponse {}

/**
 * Same message as AddTransactionsRequest, except that transactions are encoded in a byte string
 */
message ImportTopologySnapshotV2Request {
  bytes topology_snapshot = 1;
  StoreId store = 2;
  /** Optional timeout to wait for the transaction to become effective in the store. */
  google.protobuf.Duration wait_to_become_effective = 3;
}
message ImportTopologySnapshotV2Response {}

message SignTransactionsRequest {
  /** The transactions to be signed, but will not be stored in the authorized store */
  repeated com.digitalasset.canton.protocol.v30.SignedTopologyTransaction transactions = 1;
  /**
   * Fingerprint of the keys signing the authorization
   *
   * The signing key is used to identify a particular `NamespaceDelegation` certificate,
   * which is used to justify the given authorization.
   * Optional, if empty, suitable signing keys available known to the node are automatically selected.
   */
  repeated string signed_by = 2;

  // Target store
  StoreId store = 3;

  /** Force specific changes even if dangerous */
  repeated ForceFlag force_flags = 4;
}

message SignTransactionsResponse {
  /** The transactions with the additional signatures from this node. */
  repeated com.digitalasset.canton.protocol.v30.SignedTopologyTransaction transactions = 1;
}

message CreateTemporaryTopologyStoreRequest {
  /** The name of the topology store */
  string name = 1;
  /** The protocol version that should be used by the store */
  uint32 protocol_version = 2;
}

message CreateTemporaryTopologyStoreResponse {
  /** The identifier of the topology store that should be used as a store filter string */
  StoreId.Temporary store_id = 1;
}

message DropTemporaryTopologyStoreRequest {
  /** The identifier of the topology store that should be dropped */
  StoreId.Temporary store_id = 1;
}

message DropTemporaryTopologyStoreResponse {}

enum ForceFlag {
  FORCE_FLAG_UNSPECIFIED = 0;
  /** Required when authorizing adding a topology transaction on behalf of another node. */
  FORCE_FLAG_ALIEN_MEMBER = 1;
  /* Deprecated, increasing ledger time record time tolerance does not require a force flag for PV >= 32 */
  FORCE_FLAG_LEDGER_TIME_RECORD_TIME_TOLERANCE_INCREASE = 2;
  // Previously FORCE_FLAG_ALLOW_UNVET_PACKAGE, now always enabled as it is not dangerous anymore
  reserved 3;
  reserved "FORCE_FLAG_ALLOW_UNVET_PACKAGE";
  /** Required when vetting unknown packages (not uploaded). */
  FORCE_FLAG_ALLOW_UNKNOWN_PACKAGE = 4;
  /** Required when vetting a package with unvetted dependencies */
  FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES = 5;
  /** Required when disabling a party with active contracts */
  FORCE_FLAG_DISABLE_PARTY_WITH_ACTIVE_CONTRACTS = 6;
  /**
   * Required when using a key that is not suitable to sign a topology transaction.
   * Using this force flag likely causes the transaction to be rejected at a later stage of the processing.
   */
  FORCE_FLAG_ALLOW_UNVALIDATED_SIGNING_KEYS = 7;
  // Previously FORCE_FLAG_ALLOW_UNVET_PACKAGE_WITH_ACTIVE_CONTRACTS, now allowed without flag as it is not a dangerous operation anymore.
  reserved 8;
  reserved "FORCE_FLAG_ALLOW_UNVET_PACKAGE_WITH_ACTIVE_CONTRACTS";
  /** Required when increasing the submission time record time tolerance */
  FORCE_FLAG_PREPARATION_TIME_RECORD_TIME_TOLERANCE_INCREASE = 9;
  /** Required when we want to change all participants' permissions to observation while the party is still a signatory of a contract. */
  FORCE_FLAG_ALLOW_INSUFFICIENT_PARTICIPANT_PERMISSION_FOR_SIGNATORY_PARTY = 10;
  /** Required when changing the party-to-participant mapping, that would result in insufficient
   * signatory-assigning participants and thus the assignment would be stuck.
   */
  FORCE_FLAG_ALLOW_INSUFFICIENT_SIGNATORY_ASSIGNING_PARTICIPANTS_FOR_PARTY = 11;
  /** Required when vetting a package that fails upgrade checking */
  FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES = 12;
  /** Required when submitting dynamic synchronizer parameters that have out-of-bounds values */
  FORCE_FLAG_ALLOW_OUT_OF_BOUNDS_VALUE = 13;
  /** Required when changing the confirming threshold to a value higher than the number of confirming participants */
  FORCE_FLAG_ALLOW_CONFIRMING_THRESHOLD_CANNOT_BE_MET = 14;
}
```

### Python
建议使用独立 Python 虚拟环境，见 [venv](https://docs.python.org/3/library/venv.html) python environment to avoid conflicting dependencies. Considering using [venv](https://docs.python.org/3/library/venv.html).

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

运行 setup 脚本生成 Python gRPC 绑定： to generate the necessary python files to interact with Canton's gRPC interface:

```
./setup.sh
```

最后需要以下 import： will be needed:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from grpc import Channel

from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2_grpc,
    topology_manager_read_service_pb2_grpc,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2,
    topology_manager_read_service_pb2,
    common_pb2,
)
from com.digitalasset.canton.protocol.v30 import topology_pb2
from com.digitalasset.canton.version.v1 import untyped_versioned_message_pb2
from com.digitalasset.canton.crypto.v30 import crypto_pb2
from google.rpc import status_pb2, error_details_pb2
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToJson
import hashlib
import grpc
```

### Shell
终端方式请安装：, install the following tools:

* [openssl](https://www.openssl.org/)
* [buf](https://buf.build/docs/cli/installation/)
* [jq](https://jqlang.org/)
* [xxd](https://linux.die.net/man/1/xxd)

教程使用 buf proto 镜像（反）序列化 proto 消息 to (de)serialize proto messages.

> ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
> CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)
> BUF_PROTO_IMAGE="$CURRENT_DIR/interactive_topology_buf_image.json.gz"
> ```
>
> ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
> ROOT_PATH="../../protobuf"
> ```

教程将使用以下 shell 函数： throughout the tutorial:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Encode bytes read from stdin to base64
encode_to_base64() {
  openssl base64 -e -A
}

# Decode base64 string to bytes
decode_from_base64() {
  openssl base64 -d
}

# Encode bytes read from stdin to hexadecimal
encode_to_hex() {
  xxd -ps -c 0
}
```

### 错误处理
遇到 RPC 错误时可能需要额外反序列化以获取可操作信息。RPC 错误示例：, it may be necessary to perform additional deserialization to get actionable information on the cause

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "code": "invalid_argument",
   "message": "PROTO_DESERIALIZATION_FAILURE(8,0): Deserialization of protobuf message failed",
   "details": [
      {
         "type": "google.rpc.ErrorInfo",
         "value": "Ch1QUk9UT19ERVNFUklBTElaQVRJT05fRkFJTFVSRRobCgtwYXJ0aWNpcGFudBIMcGFydGljaXBhbnQxGlQKBnJlYXNvbhJKVmFsdWVDb252ZXJzaW9uRXJyb3Ioc3RvcmUsRW1wdHkgc3RyaW5nIGlzIG5vdCBhIHZhbGlkIHVuaXF1ZSBpZGVudGlmaWVyLikaDQoIY2F0ZWdvcnkSATg"
      }
   ]
}
```

`type` 指明错误 protobuf 类型。下列工具代码可提取有用信息 the protobuf type in which the error is encoded. In this case, it is a `google.rpc.ErrorInfo` message. The following utility code can be

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Make an RPC call with the given request.
# Arguments:
#   $1 - JSON request string
#   $2 - RPC endpoint URL
make_rpc_call() {
  local request=$1
  local rpc=$2
  echo -n "$request" | buf curl --protocol grpc --http2-prior-knowledge -d @- "$rpc" 2>&1
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
handle_rpc_error() {
  local response="$1"
  local details
  local type

  echo "Request failed"
  # Extract the first element from the details field using jq
  details=$(echo "$response" | jq -r '.details[0].value // empty')
  type=$(echo "$response" | jq -r '.details[0].type // empty')

  if [ -n "$details" ] && [ "$type" = "google.rpc.ErrorInfo" ]; then
    # Decode the base64 value and save it to a file
    echo "$details" | base64 -d > error_info.bin

    # Download the error info proto if it doesn't exist
    if [ ! -f "google/rpc/error_details.proto" ]; then
      mkdir -p "google/rpc"
      curl -s "https://raw.githubusercontent.com/googleapis/googleapis/9415ba048aa587b1b2df2b96fc00aa009c831597/google/rpc/error_details.proto" -o "google/rpc/error_details.proto"
    fi

    # Deserialize the protobuf message using buf convert
    buf convert google/rpc/error_details.proto --from error_info.bin --to - --type google.rpc.ErrorInfo | jq .
  else
    echo "No details available in the response or type is not google.rpc.ErrorInfo."
  fi
}
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def handle_grpc_error(func):
    """
    Decorator to handle gRPC errors and print detailed error information.

    Args:
        func (function): The gRPC function to be wrapped.

    Returns:
        function: Wrapped function with error handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except grpc.RpcError as e:
            print("gRPC error occurred:")
            grpc_metadata: grpc.aio.Metadata = grpc.aio.Metadata.from_tuple(
                e.trailing_metadata()
            )
            metadata = grpc_metadata.get("grpc-status-details-bin")
            if metadata is None:
                raise
            status: status_pb2.Status = status_pb2.Status.FromString(metadata)
            for detail in status.details:
                if detail.type_url == "type.googleapis.com/google.rpc.ErrorInfo":
                    error: error_details_pb2.ErrorInfo = (
                        error_details_pb2.ErrorInfo.FromString(detail.value)
                    )
                    print(MessageToJson(error))
                else:
                    print(MessageToJson(detail))
            raise

    return wrapper
```

## 1. 签名密钥
首先生成外部签名密钥对供本教程使用 pair to use in the rest of this tutorial.

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate an ECDSA private key and extract its public key
openssl ecparam -name prime256v1 -genkey -noout -outform DER -out namespace_private_key.der
openssl ec -inform der -in namespace_private_key.der -pubout -outform der -out namespace_public_key.der 2> /dev/null
```

Python```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
private_key = ec.generate_private_key(curve=ec.SECP256R1())
public_key = private_key.public_key()
```

## 2. 哈希
若干步骤需对字节序列哈希。过程使用底层算法，并在输入与最终哈希上加特定前缀： to compute a hash over a sequence of bytes. The process uses an underlying algorithm, with specific prefixes added to both the input bytes and the final hash:

1. 在字节序列前加 hash purpose（4 字节整数），取值定义于 Canton 代码库 integer) is prefixed to the byte sequence. Hash purpose values are defined directly in the Canton codebase.

   > >
   >
   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > // Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   > // SPDX-License-Identifier: Apache-2.0
   >
   > package com.digitalasset.canton.crypto
   >
   > import scala.collection.mutable
   >
   > /** The purpose of a hash serves to avoid hash collisions due to equal encodings for different
   >   * objects. It is in general not possible to derive the purpose of the hash from the hash alone.
   >   *
   >   * Whenever a hash is computed using [[HashOps]], a [[HashPurpose]] must be specified that gets
   >   * included in the hash. To reliably prevent hash collisions, every [[HashPurpose]] object should
   >   * be used only in a single place.
   >   *
   >   * All [[HashPurpose]] objects must be created through the [[HashPurpose$.apply]] method, which
   >   * checks that the id is fresh.
   >   *
   >   * @param id
   >   *   The identifier for the [[HashPurpose]]. Every [[HashPurpose]] object must have a unique
   >   *   [[id]].
   >   */
   > class HashPurpose private (val id: Int) extends AnyVal
   >
   > object HashPurpose {
   >   private val ids: mutable.Map[Int, String] = mutable.TreeMap.empty[Int, String]
   >
   >   /** Creates a new [[HashPurpose]] with a given description */
   >   def apply(id: Int, description: String): HashPurpose = {
   >     ids.put(id, description).foreach { oldDescription =>
   >       throw new IllegalArgumentException(
   >         s"requirement failed: HashPurpose with id=$id already exists for $oldDescription"
   >       )
   >     }
   >
   >     new HashPurpose(id)
   >   }
   >
   >   /** Returns the description that was given when the hash purpose was created. */
   >   def description(hashPurpose: HashPurpose): String =
   >     ids.getOrElse(
   >       hashPurpose.id,
   >       throw new IllegalStateException(
   >         s"Hash purpose with id ${hashPurpose.id} has been created without going through apply"
   >       ),
   >     )
   >
   >   /* HashPurposes are listed as `val` rather than `case object`s such that they are initialized eagerly.
   >    * This ensures that HashPurpose id clashes are detected eagerly. Otherwise, it may be there are two hash purposes
   >    * with the same id, but they are never used in the same Java process and therefore the clash is not detected.
   >    * NOTE: We're keeping around the old hash purposes (no longer used) to prevent accidental reuse.
   >    */
   >   val SequencedEventSignature = HashPurpose(1, "SequencedEventSignature")
   >   val _Hmac = HashPurpose(2, "Hmac")
   >   val MerkleTreeInnerNode = HashPurpose(3, "MerkleTreeInnerNode")
   >   val _Discriminator = HashPurpose(4, "Discriminator")
   >   val SubmitterMetadata = HashPurpose(5, "SubmitterMetadata")
   >   val CommonMetadata = HashPurpose(6, "CommonMetadata")
   >   val ParticipantMetadata = HashPurpose(7, "ParticipantMetadata")
   >   val ViewCommonData = HashPurpose(8, "ViewCommonData")
   >   val ViewParticipantData = HashPurpose(9, "ViewParticipantData")
   >   val _MalformedMediatorRequestResult = HashPurpose(10, "MalformedMediatorRequestResult")
   >   val TopologyTransactionSignature = HashPurpose(11, "TopologyTransactionSignature")
   >   val PublicKeyFingerprint = HashPurpose(12, "PublicKeyFingerprint")
   >   val _DarIdentifier = HashPurpose(13, "DarIdentifier")
   >   val AuthenticationToken = HashPurpose(14, "AuthenticationToken")
   >   val _AgreementId = HashPurpose(15, "AgreementId")
   >   val _MediatorResponseSignature = HashPurpose(16, "MediatorResponseSignature")
   >   val _TransactionResultSignature = HashPurpose(17, "TransactionResultSignature")
   >   val _TransferResultSignature = HashPurpose(19, "TransferResultSignature")
   >   val _ParticipantStateSignature = HashPurpose(20, "ParticipantStateSignature")
   >   val _SynchronizerTopologyTransactionMessageSignature =
   >     HashPurpose(21, "SynchronizerTopologyTransactionMessageSignature")
   >   val _AcsCommitment = HashPurpose(22, "AcsCommitment")
   >   val Stakeholders = HashPurpose(23, "Stakeholders")
   >   val UnassignmentCommonData = HashPurpose(24, "UnassignmentCommonData")
   >   val UnassignmentView = HashPurpose(25, "UnassignmentView")
   >   val AssignmentCommonData = HashPurpose(26, "AssignmentCommonData")
   >   val AssignmentView = HashPurpose(27, "AssignmentView")
   >   val _TransferViewTreeMessageSeed = HashPurpose(28, "TransferViewTreeMessageSeed")
   >   val Unicum = HashPurpose(29, "Unicum")
   >   val RepairUpdateId = HashPurpose(30, "RepairUpdateId")
   >   val _MediatorLeadershipEvent = HashPurpose(31, "MediatorLeadershipEvent")
   >   val _LegalIdentityClaim = HashPurpose(32, "LegalIdentityClaim")
   >   val DbLockId = HashPurpose(33, "DbLockId")
   >   val HashedAcsCommitment = HashPurpose(34, "HashedAcsCommitment")
   >   val SubmissionRequestSignature = HashPurpose(35, "SubmissionRequestSignature")
   >   val AcknowledgementSignature = HashPurpose(36, "AcknowledgementSignature")
   >   val DecentralizedNamespaceNamespace = HashPurpose(37, "DecentralizedNamespace")
   >   val SignedProtocolMessageSignature = HashPurpose(38, "SignedProtocolMessageSignature")
   >   val AggregationId = HashPurpose(39, "AggregationId")
   >   val BftOrderingPbftBlock = HashPurpose(40, "BftOrderingPbftBlock")
   >   val _SetTrafficPurchased = HashPurpose(41, "SetTrafficPurchased")
   >   val OrderingRequestSignature = HashPurpose(42, "OrderingRequestSignature")
   >   val TopologyMappingUniqueKey = HashPurpose(43, "TopologyMappingUniqueKey")
   >   val CantonScript = HashPurpose(44, "CantonScriptHash")
   >   val BftAvailabilityAck = HashPurpose(45, "BftAvailabilityAck")
   >   val BftBatchId = HashPurpose(46, "BftBatchId")
   >   val BftSignedAvailabilityMessage = HashPurpose(47, "BftSignedAvailabilityMessage")
   >   val PreparedSubmission = HashPurpose(48, "PreparedSubmission")
   >   val TopologyUpdateId = HashPurpose(49, "TopologyUpdateId")
   >   val OnlinePartyReplicationId = HashPurpose(50, "OnlinePartyReplication")
   >   val PartyUpdateId = HashPurpose(51, "PartyUpdateId")
   >   val BftSignedConsensusMessage = HashPurpose(52, "BftSignedConsensusMessage")
   >   val BftSignedStateTransferMessage = HashPurpose(53, "BftSignedStateTransferMessage")
   >   val BftSignedRetransmissionMessage = HashPurpose(54, "BftSignedRetransmissionMessage")
   >   val MultiTopologyTransaction = HashPurpose(55, "MultiTopologyTransaction")
   >   val SessionKeyDelegation = HashPurpose(56, "SessionKeyDelegation")
   >   val ReassignmentId = HashPurpose(57, "ReassignmentId")
   >   val EncryptedSessionKey = HashPurpose(58, "EncryptedSessionKey")
   >   val ContractIdAbsolutization = HashPurpose(59, "ContractIdAbsolutization")
   >   val InitialTopologyStateConsistency = HashPurpose(60, "InitialTopologyStateConsistency")
   >
   >   // Do not use for anything other than testing or "mock" hashes
   >   // Is not in a testing-only module because it used in traffic cost estimation that requires mock hashes
   >   val TestHashPurpose: HashPurpose = HashPurpose(-1, "testing")
   > }
   > ```

2. 对结果数据用底层算法哈希 using the underlying algorithm.

3. 最终 multihash 再按 [multi-codec](https://github.com/multiformats/multicodec) 加两字节前缀： again with two bytes, following the [multi-codec](https://github.com/multiformats/multicodec) specification:

   > * The identifier for the hash algorithm used.
   > * The length of the hash.

<Tip>
  多数场景可用 SHA-256 作为底层算法，本教程亦如此
</Tip> usages, SHA-256 can be used as the underlying algorithm, and is used in this tutorial as well.
</Tip>

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
compute_canton_hash() {
  # The hash purpose integer must be prefixed to the content to be hashed as a 4 bytes big endian
  (printf "\\x00\\x00\\x00\\x$(printf '%02X' "$1")"; cat - <(cat)) | \
  # Then hash with sha256
  openssl dgst -sha256 -binary | \
  # And finally prefix with 0x12 (The multicodec code for SHA256 https://github.com/multiformats/multicodec/blob/master/table.csv#L9)
  # and 0x20, the length of the hash (32 bytes)
  ( printf '\x12\x20'; cat - )
}
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def compute_sha256_canton_hash(purpose: int, content: bytes):
    hash_purpose = purpose.to_bytes(4, byteorder="big")
    # Hashed content
    hashed_content = hashlib.sha256(hash_purpose + content).digest()

    # Multi-hash encoding
    # Canton uses an implementation of multihash (https://github.com/multiformats/multihash)
    # Since we use sha256 always here, we can just hardcode the prefixes
    # This may be improved and simplified in subsequent versions
    sha256_algorithm_prefix = bytes([0x12])
    sha256_length_prefix = bytes([0x20])
    return sha256_algorithm_prefix + sha256_length_prefix + hashed_content
```

## 3. 指纹
Canton 用指纹标识签名密钥；指纹为公钥哈希。用前述算法计算，指纹的 hash purpose 为 `12` identify and reference signing keys. A fingerprint is a hash

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
compute_canton_fingerprint() {
  # 12 is the hash purpose for public key fingerprints
  # https://github.com/digital-asset/canton/blob/main/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala
  compute_canton_hash 12 | encode_to_hex
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Compute the fingerprint of the public key
fingerprint=$(compute_canton_fingerprint < namespace_public_key.der)
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def compute_fingerprint(public_key_bytes: bytes) -> str:
    """
    Computes the fingerprint of a public signing key.

    Args:
        public_key_bytes (bytes): The serialized transaction data.

    Returns:
        str: The computed fingerprint in hexadecimal format.
    """
    # 12 is the hash purpose for public key fingerprints
    # https://github.com/digital-asset/canton/blob/main/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala
    return compute_sha256_canton_hash(12, public_key_bytes).hex()
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
public_key_bytes: bytes = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
public_key_fingerprint = compute_fingerprint(public_key_bytes)
```

<Tip>
  本教程脚本可快速验证第三方哈希/签名实现，例如对 base64 公钥输出有效指纹
</Tip> can provide a quick way to verify third party implementations of the hashing and signing logic. For instance, the following script outputs the valid fingerprint of a signing public key passed in a base64 format:

  ```
  > . ./interactive_topology_util.sh && compute_canton_fingerprint_from_base64 "2RwUiIHVUVdulxzD8NKtPmIaaBqMer1A90rDjoklJPY="
  1220205057e331cc8929dd217e2f8e63f503b7081773de60d01fb46839700bc5caaa
  ```
</Tip>

## 4. 命名空间委托映射
有多种拓扑映射，各建模拓扑状态的一部分 available, each modeling a part

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
message TopologyMapping {
  oneof mapping {
    NamespaceDelegation namespace_delegation = 1;
    DecentralizedNamespaceDefinition decentralized_namespace_definition = 3;

    OwnerToKeyMapping owner_to_key_mapping = 4;

    SynchronizerTrustCertificate synchronizer_trust_certificate = 5;
    ParticipantSynchronizerPermission participant_permission = 6;
    PartyHostingLimits party_hosting_limits = 7;
    VettedPackages vetted_packages = 8;

    PartyToParticipant party_to_participant = 9;

    SynchronizerParametersState synchronizer_parameters_state = 11;
    MediatorSynchronizerState mediator_synchronizer_state = 12;
    SequencerSynchronizerState sequencer_synchronizer_state = 13;
    DynamicSequencingParametersState sequencing_dynamic_parameters_state = 15;

    PartyToKeyMapping party_to_key_mapping = 16;

    SynchronizerUpgradeAnnouncement synchronizer_upgrade_announcement = 17;
    SequencerConnectionSuccessor sequencer_connection_successor = 18;
  }
  reserved 2; // was identifier_delegation
  reserved 10; // was authority_of
  reserved 14; // was purge_topology_txs
}
```

本教程以导入根 `NamespaceDelegation` 为例，流程可推广到任意映射 of importing a root namespace delegation, represented by the `NamespaceDelegation` mapping, but the same procedure can be applied for any topology mapping.

Namespace Delegation 映射需要三个值： three values:

1. `namespace`：根密钥指纹

2. `target_key`：委托使用的公钥。根命名空间委托为自签 to be used by delegation. Root namespace delegations are self-signed.

   > * The format (`DER`) and specification (`EC256`) of the key must match those of the key generated in step 1.

3. `is_root_delegation`：根委托为 `true` `true` for root namespace delegations

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_namespace_mapping() {
  local namespace="$1"
  local format="$2"
  local public_key="$3"
  local spec="$4"
  local restrictions="$5"
    cat <<EOF
{
  "namespace_delegation": {
    "namespace": "$namespace",
    "target_key": {
      "format": "$format",
      "public_key": "$public_key",
      "usage": ["SIGNING_KEY_USAGE_NAMESPACE"],
      "key_spec": "$spec"
    },
    $restrictions
  }
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Base64 encoded public key: grpcurl expects protobuf bytes value to be Base64 encoded in the JSON representation
public_key_base64=$(openssl enc -base64 -A -in namespace_public_key.der)
# This is a root delegation and therefore can sign all mappings
mapping=$(build_namespace_mapping "$fingerprint" "CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO" "$public_key_base64" "SIGNING_KEY_SPEC_EC_P256" '"can_sign_all_mappings": {}')
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_namespace_mapping(
    public_key_fingerprint: str,
    public_key_bytes: bytes,
    key_format: crypto_pb2.CryptoKeyFormat,
    key_scheme: crypto_pb2.SigningKeyScheme,
):
    """
    Constructs a topology mapping for namespace delegation.

    Args:
        public_key_fingerprint (str): The fingerprint of the public key.
        public_key_bytes (bytes): The raw bytes of the public key.
        key_format (crypto_pb2.CryptoKeyFormat): The format of the public key.
        key_scheme (crypto_pb2.SigningKeyScheme): The signing scheme of the key.

    Returns:
        topology_pb2.TopologyMapping: A topology mapping for namespace delegation.
    """
    return topology_pb2.TopologyMapping(
        namespace_delegation=topology_pb2.NamespaceDelegation(
            namespace=public_key_fingerprint,
            target_key=crypto_pb2.SigningPublicKey(
                # Must match the format to which the key was exported
                format=key_format,
                public_key=public_key_bytes,
                # Must match the scheme of the key
                scheme=key_scheme,
                # Keys in NamespaceDelegation are used only for namespace operations
                usage=[
                    crypto_pb2.SigningKeyUsage.SIGNING_KEY_USAGE_NAMESPACE,
                ],
            ),
            is_root_delegation=True,
        )
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapping = build_namespace_mapping(
    public_key_fingerprint,
    public_key_bytes,
    crypto_pb2.CryptoKeyFormat.CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO,
    crypto_pb2.SigningKeyScheme.SIGNING_KEY_SCHEME_EC_DSA_P256,
)
```

## 5. 拓扑交易
拓扑状态作用于 synchronizer。各 synchronizer 支持特定 Canton 协议版本（Protocol Version），使用拓扑 API 时须选择目标 synchronizer. Each synchronizer supports a specific version

选定 synchronizer 后，可通过 sequencer API 的 `SequencerConnectService#GetSynchronizerParameters` 获取其 `ProtocolVersion`, its `ProtocolVersion` can be retrieved via the `SequencerConnectService#GetSynchronizerParameters` RPC

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

syntax = "proto3";

package com.digitalasset.canton.sequencer.api.v30;

import "com/digitalasset/canton/protocol/v30/sequencing.proto";
import "com/digitalasset/canton/protocol/v30/topology.proto";

service SequencerConnectService {
  rpc Handshake(SequencerConnect.HandshakeRequest) returns (SequencerConnect.HandshakeResponse);
  rpc GetSynchronizerId(SequencerConnect.GetSynchronizerIdRequest) returns (SequencerConnect.GetSynchronizerIdResponse);
  rpc GetSynchronizerParameters(SequencerConnect.GetSynchronizerParametersRequest) returns (SequencerConnect.GetSynchronizerParametersResponse);
  rpc VerifyActive(SequencerConnect.VerifyActiveRequest) returns (SequencerConnect.VerifyActiveResponse);
  rpc RegisterOnboardingTopologyTransactions(SequencerConnect.RegisterOnboardingTopologyTransactionsRequest) returns (SequencerConnect.RegisterOnboardingTopologyTransactionsResponse);
}

message SequencerConnect {
  // Messages for performing a version handshake with a sequencer service
  // Reused between sequencer services
  // IMPORTANT: changing the version handshakes can lead to issues with upgrading synchronizers - be very careful
  // when changing the handshake message format
  message HandshakeRequest {
    repeated int32 client_protocol_versions = 1;
    optional int32 minimum_protocol_version = 2;
  }

  message HandshakeResponse {
    int32 server_protocol_version = 1;
    oneof value {
      Success success = 2;
      Failure failure = 3;
    }

    message Success {}

    message Failure {
      string reason = 1;
    }
  }

  message GetSynchronizerIdRequest {}

  message GetSynchronizerIdResponse {
    string physical_synchronizer_id = 1;
    string sequencer_uid = 2;
  }

  message GetSynchronizerParametersRequest {}

  message GetSynchronizerParametersResponse {
    oneof parameters {
      com.digitalasset.canton.protocol.v30.StaticSynchronizerParameters parameters_v1 = 2;
    }
  }

  message VerifyActiveRequest {}

  message VerifyActiveResponse {
    message Success {
      bool is_active = 1;
    }

    message Failure {
      string reason = 1;
    }
    oneof value {
      Success success = 1;
      Failure failure = 2;
    }
  }

  message RegisterOnboardingTopologyTransactionsRequest {
    repeated com.digitalasset.canton.protocol.v30.SignedTopologyTransaction topology_transactions = 1;
  }

  message RegisterOnboardingTopologyTransactionsResponse {}
}
```

在目标 synchronizer 的 sequencer 节点上，Canton 控制台也可查询： node

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.synchronizer_parameters.static.get.protocolVersion
    res4: ProtocolVersion = 34
```

各 `Protocol Version` 对应 Canton 协议涉及 protobuf 的 `Protobuf Version`，包括 `TopologyTransaction` `Protobuf Version` for protobuf messages involved in the Canton protocol. That includes the `TopologyTransaction` message.

| 协议版本 | 拓扑交易 Protobuf 版本 | Transaction Protobuf Version |
| ---------------- | ------------------------------------- |
| 34               | 30                                    |

The protobuf version becomes relevant in the Version Wrapper section.

<Note>
  protobuf 消息版本相对稳定，下文假设 protobuf 版本为 `30`
</Note> messages is relatively stable and is not expected to change often. The rest of the tutorial assumes the protobuf version used is `30`.
</Note>

拓扑交易由三部分组成： parts:

### 拓扑映射
见命名空间委托映射一节 section

### Serial
`serial` 为从 1 起单调递增的序号。创建、替换或删除唯一拓扑映射的交易须将 serial 设为该映射上一笔已接受交易 serial 加 1。唯一性因映射而异，见各映射 protobuf。这可避免并发更新同一映射时相互覆盖。查询现有 serial 请用 `TopologyManagerReadService` 列出相关映射 increasing number, starting from 1. Each transaction creating, replacing, or deleting a unique topology mapping must specify a serial incrementing the serial

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

syntax = "proto3";

package com.digitalasset.canton.topology.admin.v30;

import "com/digitalasset/canton/protocol/v30/synchronizer_parameters.proto";
import "com/digitalasset/canton/protocol/v30/topology.proto";
import "com/digitalasset/canton/topology/admin/v30/common.proto";
import "google/protobuf/empty.proto";
import "google/protobuf/timestamp.proto";

service TopologyManagerReadService {
  rpc ListNamespaceDelegation(ListNamespaceDelegationRequest) returns (ListNamespaceDelegationResponse);
  rpc ListDecentralizedNamespaceDefinition(ListDecentralizedNamespaceDefinitionRequest) returns (ListDecentralizedNamespaceDefinitionResponse);

  rpc ListOwnerToKeyMapping(ListOwnerToKeyMappingRequest) returns (ListOwnerToKeyMappingResponse);
  rpc ListPartyToKeyMapping(ListPartyToKeyMappingRequest) returns (ListPartyToKeyMappingResponse);

  rpc ListSynchronizerTrustCertificate(ListSynchronizerTrustCertificateRequest) returns (ListSynchronizerTrustCertificateResponse);
  rpc ListParticipantSynchronizerPermission(ListParticipantSynchronizerPermissionRequest) returns (ListParticipantSynchronizerPermissionResponse);
  rpc ListPartyHostingLimits(ListPartyHostingLimitsRequest) returns (ListPartyHostingLimitsResponse);
  rpc ListVettedPackages(ListVettedPackagesRequest) returns (ListVettedPackagesResponse);

  rpc ListPartyToParticipant(ListPartyToParticipantRequest) returns (ListPartyToParticipantResponse);

  rpc ListSynchronizerParametersState(ListSynchronizerParametersStateRequest) returns (ListSynchronizerParametersStateResponse);
  rpc ListMediatorSynchronizerState(ListMediatorSynchronizerStateRequest) returns (ListMediatorSynchronizerStateResponse);
  rpc ListSequencerSynchronizerState(ListSequencerSynchronizerStateRequest) returns (ListSequencerSynchronizerStateResponse);

  rpc ListSynchronizerUpgradeAnnouncement(ListSynchronizerUpgradeAnnouncementRequest) returns (ListSynchronizerUpgradeAnnouncementResponse);
  rpc ListSequencerConnectionSuccessor(ListSequencerConnectionSuccessorRequest) returns (ListSequencerConnectionSuccessorResponse);

  rpc ListAvailableStores(ListAvailableStoresRequest) returns (ListAvailableStoresResponse);
  rpc ListAll(ListAllRequest) returns (ListAllResponse);
  rpc ExportTopologySnapshot(ExportTopologySnapshotRequest) returns (stream ExportTopologySnapshotResponse);
  rpc ExportTopologySnapshotV2(ExportTopologySnapshotV2Request) returns (stream ExportTopologySnapshotV2Response);

  // Fetch the genesis topology state.
  // The returned bytestring can be used directly to initialize a sequencer.
  rpc GenesisState(GenesisStateRequest) returns (stream GenesisStateResponse);
  rpc GenesisStateV2(GenesisStateV2Request) returns (stream GenesisStateV2Response);

  // Fetch the topology state
  // The returned bytestring can be used directly to initialize a successor sequencer
  rpc LogicalUpgradeState(LogicalUpgradeStateRequest) returns (stream LogicalUpgradeStateResponse);
}

message BaseQuery {
  StoreId store = 1;

  // whether to query only for proposals instead of approved topology mappings
  bool proposals = 2;

  com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp operation = 3;

  reserved 4;

  message TimeRange {
    google.protobuf.Timestamp from = 1;
    google.protobuf.Timestamp until = 2;
  }

  oneof time_query {
    google.protobuf.Timestamp snapshot = 5;
    google.protobuf.Empty head_state = 6;
    TimeRange range = 7;
  }
  string filter_signed_key = 8;
  optional int32 protocol_version = 9;
}

message BaseResult {
  StoreId store = 1;
  google.protobuf.Timestamp sequenced = 2;
  google.protobuf.Timestamp valid_from = 3;
  google.protobuf.Timestamp valid_until = 4;
  com.digitalasset.canton.protocol.v30.Enums.TopologyChangeOp operation = 5;
  bytes transaction_hash = 6;
  int32 serial = 7;
  repeated string signed_by_fingerprints = 8;
}

message ListNamespaceDelegationRequest {
  BaseQuery base_query = 1;
  string filter_namespace = 2;
  string filter_target_key_fingerprint = 3;
}

message ListNamespaceDelegationResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.NamespaceDelegation item = 2;
  }
  repeated Result results = 1;
}

message ListDecentralizedNamespaceDefinitionRequest {
  BaseQuery base_query = 1;
  string filter_namespace = 2;
}

message ListDecentralizedNamespaceDefinitionResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.DecentralizedNamespaceDefinition item = 2;
  }
  repeated Result results = 1;
}

message ListOwnerToKeyMappingRequest {
  BaseQuery base_query = 1;
  string filter_key_owner_type = 2;
  string filter_key_owner_uid = 3;
}

message ListOwnerToKeyMappingResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.OwnerToKeyMapping item = 2;
  }
  repeated Result results = 1;
}

message ListPartyToKeyMappingRequest {
  BaseQuery base_query = 1;
  string filter_party = 2;
}

message ListPartyToKeyMappingResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.PartyToKeyMapping item = 2;
  }
  repeated Result results = 1;
}

message ListSynchronizerTrustCertificateRequest {
  BaseQuery base_query = 1;
  string filter_uid = 2;
}

message ListSynchronizerTrustCertificateResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.SynchronizerTrustCertificate item = 2;
  }
  repeated Result results = 1;
}

message ListParticipantSynchronizerPermissionRequest {
  BaseQuery base_query = 1;
  string filter_uid = 2;
}

message ListParticipantSynchronizerPermissionResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.ParticipantSynchronizerPermission item = 2;
  }
  repeated Result results = 1;
}

message ListPartyHostingLimitsRequest {
  BaseQuery base_query = 1;
  string filter_uid = 2;
}

message ListPartyHostingLimitsResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.PartyHostingLimits item = 2;
  }
  repeated Result results = 1;
}

message ListVettedPackagesRequest {
  BaseQuery base_query = 1;
  string filter_participant = 2;
}

message ListVettedPackagesResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.VettedPackages item = 2;
  }
  repeated Result results = 1;
}
message ListPartyToParticipantRequest {
  BaseQuery base_query = 1;
  string filter_party = 2;
  string filter_participant = 3;
}

message ListPartyToParticipantResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.PartyToParticipant item = 2;
  }
  repeated Result results = 2;
}

message ListSynchronizerParametersStateRequest {
  BaseQuery base_query = 1;
  string filter_synchronizer_id = 2;
}

message ListSynchronizerParametersStateResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.DynamicSynchronizerParameters item = 2;
  }
  repeated Result results = 1;
}

message ListMediatorSynchronizerStateRequest {
  BaseQuery base_query = 1;
  string filter_synchronizer_id = 2;
}

message ListMediatorSynchronizerStateResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.MediatorSynchronizerState item = 2;
  }
  repeated Result results = 1;
}

message ListSequencerSynchronizerStateRequest {
  BaseQuery base_query = 1;
  string filter_synchronizer_id = 2;
}

message ListSequencerSynchronizerStateResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.SequencerSynchronizerState item = 2;
  }
  repeated Result results = 1;
}

message ListSynchronizerUpgradeAnnouncementRequest {
  BaseQuery base_query = 1;
  string filter_synchronizer_id = 2;
}

message ListSynchronizerUpgradeAnnouncementResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.SynchronizerUpgradeAnnouncement item = 2;
  }
  repeated Result results = 1;
}

message ListSequencerConnectionSuccessorRequest {
  BaseQuery base_query = 1;
  string filter_sequencer_id = 2;
}

message ListSequencerConnectionSuccessorResponse {
  message Result {
    BaseResult context = 1;
    com.digitalasset.canton.protocol.v30.SequencerConnectionSuccessor item = 2;
  }
  repeated Result results = 1;
}

message ListAvailableStoresRequest {}

message ListAvailableStoresResponse {
  repeated StoreId store_ids = 1;
}

message ListAllRequest {
  BaseQuery base_query = 1;
  /** The list of topology mappings to exclude from the result.*/
  repeated string exclude_mappings = 2;
  string filter_namespace = 3;
}

message ListAllResponse {
  com.digitalasset.canton.topology.admin.v30.TopologyTransactions result = 1;
}

message ExportTopologySnapshotRequest {
  BaseQuery base_query = 1;
  repeated string exclude_mappings = 2;
  string filter_namespace = 3;
}

message ExportTopologySnapshotResponse {
  bytes chunk = 1;
}

message ExportTopologySnapshotV2Request {
  BaseQuery base_query = 1;
  repeated string exclude_mappings = 2;
  string filter_namespace = 3;
}

message ExportTopologySnapshotV2Response {
  bytes chunk = 1;
}

message GenesisStateRequest {
  // Must be specified if the genesis state is requested from a participant node.
  optional StoreId synchronizer_store = 1;
  // Optional - the effective time used to fetch the topology transactions. If not provided the effective time of the last topology transaction is used.
  google.protobuf.Timestamp timestamp = 2;
}

message GenesisStateResponse {
  // versioned stored topology transactions
  bytes chunk = 1;
}

message GenesisStateV2Request {
  // Must be specified if the genesis state is requested from a participant node.
  optional StoreId synchronizer_store = 1;
  // Optional - the effective time used to fetch the topology transactions. If not provided the effective time of the last topology transaction is used.
  google.protobuf.Timestamp timestamp = 2;
}

message GenesisStateV2Response {
  // versioned stored topology transactions
  bytes chunk = 1;
}

message LogicalUpgradeStateRequest {}

message LogicalUpgradeStateResponse {
  // versioned stored topology transactions
  bytes chunk = 1;
}
```

本教程假设新建的 `NamespaceDelegation` 尚无既有根委托，故 serial 设为 1 that the `NamespaceDelegation` created is new, in particular there is no pre-existing root namespace delegation with the key created in step 1. The serial is therefore set to 1.

<Tip>
  读取并递增 serial 的示例见外部 Party 入网教程
</Tip> and increment the serial, see the external party onboarding tutorial
</Tip>

### 操作
两种操作：

* `ADD_REPLACE`：新增或替换映射 Adds a new mapping or replaces an existing one.
* `REMOVE`：删除既有映射 Remove an existing mapping

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_topology_transaction() {
    local mapping="$1"
    local serial="$2"
    local operation="${3:-TOPOLOGY_CHANGE_OP_ADD_REPLACE}"
    cat <<EOF
{
  "operation": "$operation",
  "serial": $serial,
  "mapping": $mapping
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Serial = 1 as the expectation is that there is no existing root namespace with this key already
serial=1
transaction=$(build_topology_transaction "$mapping" "$serial")
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_topology_transaction(
    mapping: topology_pb2.TopologyMapping,
    serial: int = 1,
):
    """
    Builds a topology transaction.

    Args:
        mapping (topology_pb2.TopologyMapping): The topology mapping to include in the transaction.
        serial (int): The serial of the topology transaction. Defaults to 1.

    Returns:
        topology_pb2.TopologyTransaction: The topology transaction object.
    """
    return topology_pb2.TopologyTransaction(
        mapping=mapping,
        operation=topology_pb2.Enums.TopologyChangeOp.TOPOLOGY_CHANGE_OP_ADD_REPLACE,
        serial=serial,
    )
```

## 6. 版本包装
为保证 protobuf 变更时的向后兼容，Canton 用包装消息包含与消息绑定的 protobuf 版本 while supporting changes to the protobuf messages involved in the protocol, Canton wraps serialized messages

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
message UntypedVersionedMessage {
  oneof wrapper {
    bytes data = 1;
  }
  int32 version = 2;
}
```

* `data`：序列化的拓扑交易 topology transaction
* `version`：拓扑交易的 protobuf 版本

将序列化交易包入 `UntypedVersionedMessage` 并序列化结果： in an `UntypedVersionedMessage`, and serialize the result:

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_versioned_transaction() {
  local data="$1"
    cat <<EOF
{
  "data": "$data",
  "version": "30"
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
json_to_serialized_versioned_message() {
  local json=$1
  local proto=$2
  local message_type=$3
  # Serialize it to binary
  SERIALIZED_JSON_BASE64=$(echo "$json" | convert_json_to_bin "$proto"  "$message_type" | encode_to_base64)
  versioned_transaction=$(build_versioned_transaction "$SERIALIZED_JSON_BASE64")
  echo "$versioned_transaction" | convert_json_to_bin \
        "$BUF_PROTO_IMAGE" \
        "com.digitalasset.canton.version.v1.UntypedVersionedMessage"
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
serialize_topology_transaction() {
  local transaction="$1"
  json_to_serialized_versioned_message "$transaction" "$BUF_PROTO_IMAGE" "com.digitalasset.canton.protocol.v30.TopologyTransaction"
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
serialized_versioned_transaction_file="versioned_topology_transaction.binpb"
serialize_topology_transaction "$transaction" > "$serialized_versioned_transaction_file"
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_versioned_transaction(
    data: bytes,
):
    """
    Builds a versioned transaction wrapper for the given data.

    Args:
        data (bytes): Serialized transaction data.

    Returns:
        untyped_versioned_message_pb2.UntypedVersionedMessage: The versioned transaction object.
    """
    return untyped_versioned_message_pb2.UntypedVersionedMessage(
        data=data,
        version=30,
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def serialize_topology_transaction(
    mapping: topology_pb2.TopologyMapping,
    serial: int = 1,
):
    """
    Serializes a topology transaction.

    Args:
        mapping (topology_pb2.TopologyMapping): The topology mapping to serialize.
        serial (int): The serial of the topology transaction. Defaults to 1.

    Returns:
        bytes: The serialized topology transaction.
    """
    topology_transaction = build_topology_transaction(mapping, serial)
    versioned_topology_transaction = build_versioned_transaction(
        topology_transaction.SerializeToString()
    )
    return versioned_topology_transaction.SerializeToString()
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
serialized_versioned_topology_transaction = serialize_topology_transaction(mapping)
```

## 7. 交易哈希
下一步计算交易哈希：对版本化交易的序列化 protobuf 使用前文哈希函数，此次 hash purpose 为 `11`

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
compute_topology_transaction_hash() {
  # 11 is the hash purpose for topology transaction signatures
  # https://github.com/digital-asset/canton/blob/main/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala
  compute_canton_hash 11
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
topology_transaction_hash_file="topology_transaction_hash.bin"
compute_topology_transaction_hash < $serialized_versioned_transaction_file > $topology_transaction_hash_file
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def compute_topology_transaction_hash(serialized_versioned_transaction: bytes) -> bytes:
    """
    Computes the hash of a serialized topology transaction.

    Args:
        serialized_versioned_transaction (bytes): The serialized transaction data.

    Returns:
        bytes: The computed hash.
    """
    # 11 is the hash purpose for topology transaction signatures
    # https://github.com/digital-asset/canton/blob/main/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala
    return compute_sha256_canton_hash(11, serialized_versioned_transaction)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
transaction_hash = compute_topology_transaction_hash(
    serialized_versioned_topology_transaction
)
```

<Tip>
  步骤 5–7 可用拓扑 API 的 `GenerateTransactions` RPC 生成序列化版本化交易及其哈希；使用时强烈建议反序列化返回交易、校验内容并**重新计算哈希**，以防生成方误用或恶意行为
</Tip> `5` to `7`, the topology API offers a `GenerateTransactions` RPC to generate the serialized versioned transaction and its hash. When using the `GenerateTransactions` API, it is strongly recommended to deserialize the returned transaction, validate its content and re-compute its hash, to prevent any accidental misuse or adversarial behavior of the participant generating the transaction.
</Tip>

## 8. 签名
哈希现可签署。根命名空间交易仅涉及一个密钥；其他映射可能需额外签名（如 `OwnerToKeyMapping` 中的密钥，或 `PartyToParticipant` 的多方授权规则）。所有交易均须由目标命名空间的根密钥或经 `NamespaceDelegation` 注册的委托密钥签署；各映射授权规则见 protobuf，超出本教程范围. For root namespace transactions, there is only one key involved, and it therefore needs only one signature. Other topology mappings may require additional signatures, either because the mappings themselves contain additional public keys (e.g `OwnerToKeyMapping`), or because the authorization rules

<Tip>
  拓扑 API 可用单一哈希认证多笔交易，见外部签名入网教程
</Tip> authenticating several transactions with a single hash. This is illustrated in the external signing onboarding tutorial.
</Tip>

用私钥签署哈希：

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sign_hash() {
  local private_key_file="$1"
  local transaction_hash_file="$2"
  openssl pkeyutl -rawin -inkey "$private_key_file" -keyform DER -sign < "$transaction_hash_file" | encode_to_base64
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
signature=$(sign_hash namespace_private_key.der $topology_transaction_hash_file)
canton_signature=$(build_canton_signature "SIGNATURE_FORMAT_DER" "$signature" "$fingerprint" "SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256")
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def sign_hash(
    private_key: EllipticCurvePrivateKey,
    data: bytes,
):
    """
    Signs the given data using an elliptic curve private key.

    Args:
        private_key (EllipticCurvePrivateKey): The private key used for signing.
        data (bytes): The data to be signed.

    Returns:
        bytes: The generated signature.
    """
    return private_key.sign(
        data=data,
        signature_algorithm=ec.ECDSA(hashes.SHA256()),
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
signature = sign_hash(private_key, transaction_hash)
```

## 9. 提交交易
通过 `TopologyManagerWriteService` 的 `AddTransactions` RPC 提交交易与签名：. This is done via the `AddTransactions` RPC

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_canton_signature() {
  local format="$1"
  local signature="$2"
  local signed_by="$3"
  local spec="$4"
    cat <<EOF
{
  "format": "$format",
  "signature": "$signature",
  "signed_by": "$signed_by",
  "signing_algorithm_spec": "$spec"
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_signed_transaction() {
    local proposal="$1"
    local transaction="$2"
    shift 2
    local signatures=("$@")
    local signatures_json=""

    for signature in "${signatures[@]}"; do
        signatures_json+="$signature,"
    done

    signatures_json="[${signatures_json%,}]"

    cat <<EOF
{
  "transaction": "$transaction",
  "signatures": $signatures_json,
  "proposal": $proposal
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_add_transactions_request() {
    local synchronizer_id="$1"
    shift
    local transactions=("$@")
    local transactions_json=""

    # Construct JSON array properly
    for transaction in "${transactions[@]}"; do
        transactions_json+="$transaction,"
    done

    # Remove the trailing comma and wrap in brackets
    transactions_json="[${transactions_json%,}]"

    cat <<EOF
{
  "transactions": $transactions_json,
  "store": {
    "synchronizer": {
      "id": "$synchronizer_id"
    }
  }
}
EOF
}
```

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
GRPC_HOST:localhost
GRPC_PORT:4002
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
versioned_transaction_base64=$(openssl enc -base64 -A -in $serialized_versioned_transaction_file)
canton_signatures=("$canton_signature")

signed_transaction=$(build_signed_transaction "false" "$versioned_transaction_base64" "${canton_signatures[@]}")
signed_transactions=("$signed_transaction")
add_transactions_request=$(build_add_transactions_request "$SYNCHRONIZER_ID" "${signed_transactions[@]}")

rpc_status=0
response=$(make_rpc_call "$add_transactions_request" "http://$GRPC_ENDPOINT/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/AddTransactions") || rpc_status=$?
echo $response
if [ $rpc_status -eq 0 ]; then
  echo "Transaction submitted successfully"
else
  echo "Transaction submission failed"
  handle_rpc_error "$response"
  exit $rpc_status
fi
```

成功时应显示 `Transaction submitted successfully`, `Transaction submitted successfully` should be displayed.

Python```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
admin_channel = grpc.insecure_channel(f"localhost:{admin_port}")
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_canton_signature(
    signature: bytes,
    signed_by: str,
    format: crypto_pb2.SignatureFormat,
    spec: crypto_pb2.SigningAlgorithmSpec,
):
    """
    Builds a Canton-compatible digital signature.

    Args:
        signature (bytes): The cryptographic signature bytes.
        signed_by (str): The identifier of the entity that signed the data.
        format (crypto_pb2.SignatureFormat): The format of the signature.
        spec (crypto_pb2.SigningAlgorithmSpec): The signing algorithm specification.

    Returns:
        crypto_pb2.Signature: A protocol buffer representation of the Canton signature.
    """
    return crypto_pb2.Signature(
        format=format,
        signature=signature,
        signed_by=signed_by,
        signing_algorithm_spec=spec,
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_signed_transaction(
    serialized_versioned_transaction: bytes,
    signatures: [crypto_pb2.Signature],
):
    """
    Builds a signed topology transaction.

    Args:
        serialized_versioned_transaction (bytes): Serialized topology transaction.
        signatures (list[crypto_pb2.Signature]): List of cryptographic signatures.

    Returns:
        topology_pb2.SignedTopologyTransaction: The signed transaction.
    """
    return topology_pb2.SignedTopologyTransaction(
        transaction=serialized_versioned_transaction,
        signatures=signatures,
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def submit_signed_transactions(
    channel: Channel,
    signed_transactions: [topology_pb2.SignedTopologyTransaction],
    synchronizer_id: str,
) -> (EllipticCurvePrivateKey, str):
    """
    Submits signed topology transactions to the Canton topology API.

    Args:
        channel (Channel): The gRPC channel used to communicate with the topology service.
        signed_transactions (list[topology_pb2.SignedTopologyTransaction]):
            A list of signed topology transactions to be submitted.
        synchronizer_id (str): The identifier of the synchronizer to target.

    Raises:
        grpc.RpcError: If there is an issue communicating with the topology API.
    """
    add_transactions_request = build_add_transaction_request(
        signed_transactions,
        synchronizer_id,
    )
    topology_write_client = (
        topology_manager_write_service_pb2_grpc.TopologyManagerWriteServiceStub(channel)
    )
    topology_write_client.AddTransactions(add_transactions_request)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton_signature = build_canton_signature(
    signature,
    public_key_fingerprint,
    crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
    crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
)
signed_transaction = build_signed_transaction(
    serialized_versioned_topology_transaction,
    [canton_signature],
)
submit_signed_transactions(channel, [signed_transaction], synchronizer_id)
print(f"Transaction submitted successfully")
```

### Proposal
`SignedTopologyTransaction` 含布尔字段 `proposal`：为 true 时可提交尚未集齐全部所需签名的拓扑交易，便于需多方签名的场景 a boolean `proposal` field. When set to true, it allows submitting topology transactions without attaching all the signatures required for the transaction to be fully authorized. This is especially useful in cases where signatures from multiple entities

## 10. 观察交易
最后一步是在 synchronizer 拓扑状态中观察 `NamespaceDelegation`。提交是异步的，可能需要等待 the `NamespaceDelegation` on the topology state

Bash```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
build_list_namespace_delegations_request() {
  local synchronizer_id="$1"
  local namespace="$2"
    cat <<EOF
{
  "base_query": {
    "store": {
      "synchronizer": {
        "id": "$synchronizer_id"
      }
    },
    "head_state": {}
  },
  "filter_namespace": "$namespace"
}
EOF
}
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
list_namespace_delegations_request=$(build_list_namespace_delegations_request "$SYNCHRONIZER_ID" "$fingerprint")

# Topology transaction submission is asynchronous, so we may need to wait a bit before observing the delegation in the topology state
while true; do
  rpc_status=0
  response=$(make_rpc_call "$list_namespace_delegations_request" "http://$GRPC_ENDPOINT/com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/ListNamespaceDelegation") || rpc_status=$?
  if [ $rpc_status -ne 0 ]; then
    handle_rpc_error "$response"
    exit $rpc_status
  elif [ "$response" != "{}" ]; then
      echo "Namespace delegation is now active"
      break
  fi
  sleep 1
done
```

Python```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def list_namespace_delegation(
    channel: Channel,
    synchronizer_id: str,
    fingerprint: str,
):
    """
    Retrieves namespace delegations from the topology API.

    Args:
        channel (Channel): The gRPC channel used to communicate with the topology service.
        synchronizer_id (str): The identifier of the synchronizer managing the namespace.
        fingerprint (str): The fingerprint of the public key associated with the namespace.

    Returns:
        topology_manager_read_service_pb2.ListNamespaceDelegationResponse:
            The response containing the list of namespace delegations.

    Raises:
        grpc.RpcError: If there is an issue communicating with the topology API.
    """
    list_namespace_delegation_request = (
        topology_manager_read_service_pb2.ListNamespaceDelegationRequest(
            base_query=topology_manager_read_service_pb2.BaseQuery(
                store=common_pb2.StoreId(
                    synchronizer=common_pb2.Synchronizer(id=synchronizer_id)
                ),
                head_state=empty_pb2.Empty(),
            ),
            filter_namespace=fingerprint,
        )
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )
    return topology_read_client.ListNamespaceDelegation(
        list_namespace_delegation_request
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Topology transaction submission is asynchronous, so we may need to wait a bit before observing the delegation in the topology state
namespace_delegation_response = None
while True:
    namespace_delegation_response = list_namespace_delegation(
        channel, synchronizer_id, public_key_fingerprint
    )
    if namespace_delegation_response.results:
        print("Namespace delegation is now active")
        break
    time.sleep(1)  # Wait for 1 second before retrying
```

教程结束，交易已在 synchronizer 拓扑状态中生效。代码位于 `examples/08-interactive-submission`，可运行：. The transaction is now active on the topology state

Bash```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./interactive_topology_example.sh localhost:4002
```

Python```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python interactive_topology_example.py --synchronizer-id da::12207a94aca813c822c6ae10a1b5478c2ba1077447b468cc66dbd255f60f8fa333e1 run-demo
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
