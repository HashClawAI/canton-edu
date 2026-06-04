> 通过 Admin API 或 Ledger API 入网外部 Party 并签署拓扑交易。

本教程演示如何使用 **Admin API** 入网 **外部 Party**。外部 Party 可用自管密钥签署 Daml 交易而无需信任网络节点。建议先阅读外部签名概述；拓扑概念见拓扑教程 an **external party** using the Admin API. External parties can authorize Daml transactions without the need to trust any node

教程以名为 `Alice` 的 Party 为例，可重复该流程入网更多 Party of a party named `Alice`. The process can be repeated any number of times to onboard new parties.

<Warning>
  本教程仅供演示，代码片段请勿直接用于生产环境
</Warning> purposes. The code snippets should not be used directly in a production environment.
</Warning>

## 前提条件
为简化起见，假设最小 Canton 部署：一个 participant 连接一个 synchronizer（含 sequencer 与 mediator） a minimal Canton setup consisting of one participant node connected to one synchronizer (which includes both a sequencer node and a mediator node).

<Tip>
  若已有此类实例，可直接进入 Setup 节
</Tip> such an instance running, proceed to the Setup section.
</Tip>

该配置并非入网外部 Party 的硬性要求，但在提交外部签名交易时会需要 to onboard external parties per se, but will be when submitting externally signed transactions.

### 启动 Canton
获取 Canton 制品见 getting started。在制品目录执行： refer to the getting started section. From the artifact directory, start Canton using the command:

```
./bin/canton -c examples/08-interactive-submission/interactive-submission.conf --bootstrap examples/08-interactive-submission/bootstrap.canton
```

出现 “Welcome to Canton” 后即可继续 message appears, you are ready to proceed.

### 配置
进入 Canton 发行包中 `examples/08-interactive-submission` 目录 example folder located at `examples/08-interactive-submission` in the Canton release artifact.

在 Canton 控制台运行下列命令收集： information by running the commands below in the Canton console:

* Participant Id
* Admin API 端点```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.id.filterString
    res1: String = "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.adminApi.address
    res2: String = "127.0.0.1"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.adminApi.port.unwrap
    res3: Int = 30014
```

下文示例值请替换为你自己的： we'll use the following values, but make sure to replace them with your own:

* Participant Id: `participant1::122083aecbe5b3ca3c95c7584d2e0202891f8051d39754802a156521cd1677c8e759`
* Admin API endpoint: `localhost:4002`

### API
本教程使用 participant **Admin API** 上的 gRPC 服务 `TopologyManagerWriteService`，定义见外部签名拓扑交易教程 `TopologyManagerWriteService`, a gRPC service available on the **Admin API**

使用 Python 演示入网流程 the onboarding of an external party.

建议使用独立 Python 虚拟环境，避免依赖冲突，可使用 [venv](https://docs.python.org/3/library/venv.html) python environment to avoid conflicting dependencies. Considering using [venv](https://docs.python.org/3/library/venv.html).

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

然后运行 setup 脚本生成与 Canton gRPC 交互所需的 Python 文件： to generate the necessary python files to interact with Canton's gRPC interface:

```
./setup.sh
```

<Warning>
  The tutorial builds up on the externally signed topology transactions tutorial by re-using some if its code and concepts. For convenience, here are the topology utility functions used in the tutorial:

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
  # SPDX-License-Identifier: Apache-2.0

  # [Imports start]
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

  # [Imports end]
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

  # Computes a canton compatible hash using sha256
  # purpose: Canton prefixes content with a hash purpose
  # https://github.com/digital-asset/canton/blob/main/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala
  # content: payload to be hashed
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

  # Computes the fingerprint of a public key by hashing it and adding some Canton specific data
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

  def compute_multi_transaction_hash(hashes: [bytes]) -> bytes:
      """
      Computes a combined hash for multiple topology transactions.

      This function sorts the given hashes, concatenates them with length encoding,
      and computes a Canton-specific SHA-256 hash with a predefined purpose.

      Args:
          hashes (list[bytes]): A list of hashes representing individual topology transactions.

      Returns:
          bytes: The computed multi-transaction hash.
      """
      # Sort the hashes by their hex representation
      sorted_hashes = sorted(hashes, key=lambda h: h.hex())

      # Start with the number of hashes encoded as a 4 bytes integer in big endian
      combined_hashes = len(sorted_hashes).to_bytes(4, byteorder="big")

      # Concatenate each hash, prefixing them with their size as a 4 bytes integer in big endian
      for h in sorted_hashes:
          combined_hashes += len(h).to_bytes(4, byteorder="big") + h

      # 55 is the hash purpose for multi topology transaction hashes
      return compute_sha256_canton_hash(55, combined_hashes)

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

  def build_add_transaction_request(
      signed_transactions: [topology_pb2.SignedTopologyTransaction],
      synchronizer_id: str,
  ):
      """
      Builds an AddTransactionsRequest for the topology API.

      Args:
          signed_transactions (list[topology_pb2.SignedTopologyTransaction]): List of signed transactions.
          synchronizer_id (str): The synchronizer ID for the transaction.

      Returns:
          topology_manager_write_service_pb2.AddTransactionsRequest: The request object.
      """
      return topology_manager_write_service_pb2.AddTransactionsRequest(
          transactions=signed_transactions,
          store=common_pb2.StoreId(
              synchronizer=common_pb2.Synchronizer(
                  id=synchronizer_id,
              )
          ),
      )

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

  @handle_grpc_error
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

  @handle_grpc_error
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
</Warning>

Additionally, the following imports and variables are required for the rest of the tutorial:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
import time

import grpc
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from grpc import Channel

import google.protobuf.empty_pb2
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2_grpc,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_read_service_pb2_grpc,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_read_service_pb2,
    common_pb2,
)
from com.digitalasset.canton.protocol.v30 import topology_pb2
from com.digitalasset.canton.crypto.v30 import crypto_pb2
from google.protobuf import empty_pb2
from interactive_topology_util import (
    compute_fingerprint,
    compute_sha256_canton_hash,
    serialize_topology_transaction,
    compute_multi_transaction_hash,
    sign_hash,
    compute_topology_transaction_hash,
)
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
admin_port="4002"
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
admin_channel = grpc.insecure_channel(f"localhost:{admin_port}")
```

## 拓扑映射
入网外部 Party 需要三种拓扑映射： topology mappings:

* `NamespaceDelegation`: Defines a root namespace for the party and registers the **namespace signing** key, which is used to authorize topology changes involving the party's identity.

* `PartyToKeyMapping`:

  > * The **protocol signing** key responsible for authenticating the submission of Daml transactions to the ledger on behalf of the party.
  > * A threshold (number) of keys, at least equal to the number of keys registered. At least threshold-many signatures must be obtained for a transaction submission to be authorized.

* `PartyToParticipantMapping`:

  > * Associates the party with one or more participant nodes, granting them **confirmation** rights. These rights allow participant nodes to validate Daml transactions involving the party and authorize their commitment to the ledger on behalf of the party.
  > * A threshold (number) of participant node, at least equal to the number of hosting participants. At least threshold-many confirmations must be obtained from the hosting participants for a valid transaction to be authorized and committed to the ledger.

<Note>
  Hosting a party on more than one participant nodes for confirmation allows the party to reduce the trust put in any single node, as well as increase their overall availability on the network (e.g if a confirmation node becomes unavailable). See the Trust model for more details.
</Note>

## 签名密钥
Canton 用数字签名做认证。上一节中 `NamespaceDelegation` 与 `PartyToKeyMapping` 用于注册相应公钥。最佳实践是为不同用途使用不同密钥；本教程为简化使用同一密钥对 for authentication. As shown in the previous section, two of the three required topology mappings, `NamespaceDelegation` and `PartyToKeyMapping`, are

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
# For the sake of simplicity in the demo, we use a single signing key pair for the party namespace (used to manage the party itself on the network),
# and for the signing of transactions via the interactive submission service. We however recommend to use different keys in real world deployment for better security.
private_key = ec.generate_private_key(curve=ec.SECP256R1())
public_key = private_key.public_key()

# Extract the public key in the DER format
public_key_bytes: bytes = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
# Wrap the public key in a Canton protobuf message
signing_public_key = crypto_pb2.SigningPublicKey(
    # Must match the format to which the key was exported to above
    format=crypto_pb2.CryptoKeyFormat.CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO,
    public_key=public_key_bytes,
    # Must match the scheme of the key
    scheme=crypto_pb2.SigningKeyScheme.SIGNING_KEY_SCHEME_EC_DSA_P256,
    # Because we have only one key, we specify both NAMESPACE and PROTOCOL usage for it
    # When using different keys, ensure to use only the correct usage for each
    usage=[
        crypto_pb2.SigningKeyUsage.SIGNING_KEY_USAGE_NAMESPACE,
        crypto_pb2.SigningKeyUsage.SIGNING_KEY_USAGE_PROTOCOL,
    ],
    # This field is deprecated in favor of scheme but python requires us to set it
    key_spec=crypto_pb2.SIGNING_KEY_SPEC_EC_P256,
)
```

## 指纹
Canton 用指纹高效标识签名密钥，详见拓扑教程指纹一节 identify and reference signing keys. Refer to the Fingerprint section

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
public_key_fingerprint = compute_fingerprint(public_key_bytes)
```

## Party ID
`Party ID` 由两部分组成： of two parts:

* A human readable name, in this case: `alice`
* The fingerprint of the namespace signing key, also simply called `namespace`

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
# The party id is constructed with party_name :: fingerprint
# This must be the fingerprint of the _namespace signing key_
party_id = party_name + "::" + public_key_fingerprint
```

## 外部 Party 入网交易
生成入网 `Alice` 所需的三笔拓扑交易 necessary for the onboarding of `Alice`.

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_serialized_transaction_and_hash(
    mapping: topology_pb2.TopologyMapping,
) -> (bytes, bytes):
    """
    Generates a serialized topology transaction and its corresponding hash.

    Args:
        mapping (topology_pb2.TopologyMapping): The topology mapping to be serialized.

    Returns:
        tuple: A tuple containing:
            - bytes: The serialized transaction.
            - bytes: The SHA-256 hash of the serialized transaction.
    """
    transaction = serialize_topology_transaction(mapping)
    transaction_hash = compute_sha256_canton_hash(11, transaction)
    return transaction, transaction_hash
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_party_to_key_transaction(
    channel: grpc.Channel,
    party_id: str,
    new_signing_key: crypto_pb2.SigningPublicKey,
    synchronizer_id: str,
) -> bytes:
    """
    Constructs a topology transaction that updates the party-to-key mapping.

    Args:
        channel (grpc.Channel): gRPC channel for communication with the topology manager.
        party_id (str): Identifier of the party whose key mapping is being updated.
        new_signing_key (crypto_pb2.SigningPublicKey): The new signing key to be added.
        synchronizer_id (str): ID of the synchronizer to query the topology state.

    Returns:
        bytes: Serialized topology transaction containing the updated mapping.
    """
    # Retrieve the current party to key mapping
    list_party_to_key_request = (
        topology_manager_read_service_pb2.ListPartyToKeyMappingRequest(
            base_query=topology_manager_read_service_pb2.BaseQuery(
                store=common_pb2.StoreId(
                    synchronizer=common_pb2.Synchronizer(id=synchronizer_id)
                ),
                head_state=empty_pb2.Empty(),
            ),
            filter_party=party_id,
        )
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )
    party_to_key_response: (
        topology_manager_read_service_pb2.ListPartyToKeyMappingResponse
    ) = topology_read_client.ListPartyToKeyMapping(list_party_to_key_request)
    if len(party_to_key_response.results) == 0:
        current_serial = 0
        current_keys_list = []
    else:
        # Sort the results by serial in descending order and take the first one
        sorted_results = sorted(
            party_to_key_response.results,
            key=lambda result: result.context.serial,
            reverse=True,
        )
        # Get the mapping with the highest serial and its list of hosting participants
        current_serial = sorted_results[0].context.serial
        current_keys_list: [crypto_pb2.SigningPublicKey] = sorted_results[
            0
        ].item.signing_keys

    # Create a new mapping adding the new participant to the list and incrementing the serial
    updated_mapping = topology_pb2.TopologyMapping(
        party_to_key_mapping=topology_pb2.PartyToKeyMapping(
            party=party_id,
            threshold=1,
            signing_keys=current_keys_list + [new_signing_key],
        )
    )
    # Build the serialized transaction
    return serialize_topology_transaction(updated_mapping, serial=current_serial + 1)
```

<Note>
  The `build_party_to_key_transaction` function is an example of how to safely build a topology transaction by first obtaining the highest serial for it unique mapping, updating the mapping's content and incrementing the serial by 1. This ensures concurrent updates would be rejected. During onboarding of external parties however it is expected that there are no existing mappings and the serial will therefore bet set to 1.
</Note>

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Namespace delegation: registers a root namespace with the public key of the party to the network
# effectively creating the party.
namespace_delegation_mapping = topology_pb2.TopologyMapping(
    namespace_delegation=topology_pb2.NamespaceDelegation(
        namespace=public_key_fingerprint,
        target_key=signing_public_key,
        is_root_delegation=True,
    )
)
(namespace_delegation_transaction, namespace_transaction_hash) = (
    build_serialized_transaction_and_hash(namespace_delegation_mapping)
)

# Party to key: registers the public key as the one that will be used to sign and authorize Daml transactions submitted
# to the ledger via the interactive submission service
party_to_key_transaction = build_party_to_key_transaction(
    channel, party_id, signing_public_key, synchronizer_id
)
party_to_key_transaction_hash = compute_topology_transaction_hash(
    party_to_key_transaction
)

# Party to participant: records the fact that the party wants to be hosted on the participants with confirmation rights
# This means those participants are not allowed to submit transactions on behalf of this party but will validate transactions
# on behalf of the party by confirming or rejecting them according to the ledger model. They also records transaction for that party on the ledger.
confirming_participants_hosting = []
for confirming_participant_id in confirming_participant_ids:
    confirming_participants_hosting.append(
        topology_pb2.PartyToParticipant.HostingParticipant(
            participant_uid=confirming_participant_id,
            permission=topology_pb2.Enums.ParticipantPermission.PARTICIPANT_PERMISSION_CONFIRMATION,
        )
    )
party_to_participant_mapping = topology_pb2.TopologyMapping(
    party_to_participant=topology_pb2.PartyToParticipant(
        party=party_id,
        threshold=confirming_threshold,
        participants=confirming_participants_hosting,
    )
)
(party_to_participant_transaction, party_to_participant_transaction_hash) = (
    build_serialized_transaction_and_hash(party_to_participant_mapping)
)
```

本教程使用单一签名密钥，故除 `PartyToParticipant` 需托管 participant 签署外，各交易均仅用该密钥签名。生产环境使用多密钥时，每笔交易须用对应密钥签署：, therefore all transactions are signed exclusively with that key (with the exception

* `Namespace Signing Key`: All transactions must be signed by this key, as it authorizes any topology state changes involving the party.
* `PartyToKeyMapping` Transaction: In addition to the namespace signing key, this transaction must be signed by all protocol signing keys it registers. This ensures the network can verify that the party has control over those keys.
* `PartyToParticipantMapping` Transaction: Along with the namespace signing key, this transaction must be authorized by all hosting participants it registers.

<Note>
  Any change to these topology transactions requires a signature from the namespace key. No node can alter the topology state of the external party without an explicit signature from its namespace key.
</Note>

## 多交易哈希
为减少签名次数，可合并三笔交易的哈希一次性签名；教程开头工具函数已提供 `compute_multi_transaction_hash` of signing operations required, compute a multi-transaction hash of all three transactions combined. Signing this hash allows authenticating all three transactions at once. A function to that effect is already available in the utility functions provided at the beginning

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Combine the hashes of all three transactions, so we can perform a single signature
multi_hash = compute_multi_transaction_hash(
    [
        namespace_transaction_hash,
        party_to_key_transaction_hash,
        party_to_participant_transaction_hash,
    ]
)
```

## 签名
先用命名空间密钥签署 multi hash： with the namespace key:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
signature = sign_hash(private_key, multi_hash)
```

再构建 Topology API 所需的 `SignedTopologyTransaction` 消息： messages expected by the Topology API:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def build_signed_topology_transaction(
    transaction: bytes,
    hashes: [bytes],
    signature: bytes,
    signed_by: str,
    proposal: bool = False,
):
    """
    Builds a signed topology transaction, optionally including multi-transaction signatures.

    Args:
        transaction (bytes): The raw bytes representing the transaction to be signed.
        hashes (list[bytes]): A list of transaction hashes for the multi-transaction signature.
        signature (bytes): The signature for the transaction.
        signed_by (str): The identifier of the entity signing the transaction.
        proposal (bool, optional): A flag indicating if this transaction is part of a proposal. Defaults to False.

    Returns:
        topology_pb2.SignedTopologyTransaction
    """
    return topology_pb2.SignedTopologyTransaction(
        transaction=transaction,
        # Not set because we use the multi transactions signature
        signatures=[],
        multi_transaction_signatures=[
            topology_pb2.MultiTransactionSignatures(
                transaction_hashes=hashes,
                signatures=[
                    crypto_pb2.Signature(
                        format=crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
                        signature=signature,
                        signed_by=signed_by,
                        signing_algorithm_spec=crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
                    )
                ],
            )
        ],
        proposal=proposal,
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
hash_list = [
    namespace_transaction_hash,
    party_to_key_transaction_hash,
    party_to_participant_transaction_hash,
]
signed_namespace_transaction = build_signed_topology_transaction(
    namespace_delegation_transaction, hash_list, signature, public_key_fingerprint
)
signed_party_to_key_transaction = build_signed_topology_transaction(
    party_to_key_transaction, hash_list, signature, public_key_fingerprint
)
signed_party_to_participant_transaction = build_signed_topology_transaction(
    party_to_participant_transaction,
    hash_list,
    signature,
    public_key_fingerprint,
    True,
)
```

## 提交
提交已由外部 Party 密钥签名的交易： with the external party's key:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
add_transactions_request = (
    topology_manager_write_service_pb2.AddTransactionsRequest(
        transactions=[
            signed_namespace_transaction,
            signed_party_to_key_transaction,
            signed_party_to_participant_transaction,
        ],
        store=common_pb2.StoreId(
            synchronizer=common_pb2.Synchronizer(
                id=synchronizer_id,
            )
        ),
    )
)
topology_write_client.AddTransactions(add_transactions_request)
```

## 授权 PartyToParticipant 映射
托管 participant 须显式授权 PartyToParticipant 交易。本教程仅一个托管 participant，其授权即可完成入网。若有多个托管方，各方须分别授权，详见 party replication the PartyToParticipant transaction explicitly. In this tutorial there's only one hosting participant, so its authorization is sufficient to complete the onboarding. If there were multiple hosting participants for the marty, each would have to authorize the transaction individually. See party replication for more details.

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
topology_write_client.Authorize(
    topology_manager_write_service_pb2.AuthorizeRequest(
        proposal=topology_manager_write_service_pb2.AuthorizeRequest.Proposal(
            change=topology_pb2.Enums.TopologyChangeOp.TOPOLOGY_CHANGE_OP_ADD_REPLACE,
            serial=1,
            mapping=party_to_participant_mapping,
        ),
        # False because the authorization from the participant is not enough:
        # - it requires the signatures from the party (already submitted above)
        # - as well as signatures from any other hosting participant
        must_fully_authorize=False,
        store=common_pb2.StoreId(
            synchronizer=common_pb2.Synchronizer(
                id=synchronizer_id,
            ),
        ),
    )
)
```

## 观察已入网 Party
最后在拓扑中等待观察到该 Party，确认创建成功： in the topology, confirming it was created successfully:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def wait_to_observe_party_to_participant(
    topology_read_client: topology_manager_read_service_pb2_grpc,
    synchronizer_id: str,
    party_id,
):
    party_in_topology = False
    while not party_in_topology:
        party_to_participant_response: (
            topology_manager_read_service_pb2.ListPartyToParticipantResponse
        ) = topology_read_client.ListPartyToParticipant(
            topology_manager_read_service_pb2.ListPartyToParticipantRequest(
                base_query=topology_manager_read_service_pb2.BaseQuery(
                    store=common_pb2.StoreId(
                        synchronizer=common_pb2.Synchronizer(
                            id=synchronizer_id,
                        )
                    ),
                    head_state=google.protobuf.empty_pb2.Empty(),
                ),
                filter_party=party_id,
            )
        )
        if len(party_to_participant_response.results) > 0:
            break
        else:
            time.sleep(0.5)
            continue
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
# If there's only one confirming participant, onboarding should be complete already
if len(confirming_participant_ids) == 1:
    wait_to_observe_party_to_participant(
        topology_read_client, synchronizer_id, party_id
    )
```

`Alice` 已成功入网，可继续学习如何提交外部签名交易 and ready to interact with the ledger. Move to the next tutorial to learn how to submit externally signed transactions.

## 工具
本教程脚本可用于测试与开发 can be used as tools for testing and development purposes

### 入网外部 party
在账本创建外部 Party 并将公私钥写入本地 `der` 文件。默认从本目录 canton bootstrap 写入的文件读取 synchronizer ID 与 participant ID，可用 `--synchronizer-id` 与 `--participant-id` 覆盖 and write their private and public keys to local `der` files. By default the `synchronizer ID` and `participant ID` will be picked up from the files written by the canton bootstrap script in this directory. They can be overridden with ` --synchronizer-id synchronizer_id` and `--participant-id participant_id`.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./setup.sh
python interactive_submission.py create-party --name alice
```

输出：```
Onboarding alice
Waiting for alice to appear in topology
Party ID: alice::122076f2a757c1ea944f52fc1fa854aa78077672efa32d7903e97cbf92646331876d
Written private key to: alice::122076f2a757c1ea944f52fc1fa854aa78077672efa32d7903e97cbf92646331876d-private-key.der
Written public key to: alice::122076f2a757c1ea944f52fc1fa854aa78077672efa32d7903e97cbf92646331876d-public-key.der
```

## 高级入网主题
### 多方托管 Party
多方托管 Party 托管在多个 Participant 节点上。本教程为单 participant 简化环境，外部 Party 亦可多方托管 hosted on more than one Participant Node. This tutorial uses a simplified setup

创建多方托管外部 Party 时，在以上流程基础上做两处调整：, follow the tutorial above with the following two adjustments:

* Update the `PartyToParticipant` topology mapping:

  > * List all hosting participants (along with their permission) instead of just one
  > * Adjust the confirming threshold to strike the desired tradeoff between security and availability

* On each hosting participants, approve the `PartyToParticipant` transaction.

The following python function illustrates this process:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def authorize_external_party_hosting(
    participant_id: str,
    party_id: str,
    synchronizer_id: str,
    channel: Channel,
    auto_accept: bool,
) -> bool:
    """
    Authorizes the hosting of a multi-hosted external party on the current node.
    Expects the PartyToParticipant proposal to have already been published to the synchronizer.

    Args:
        party_id (str): ID of the party.
        synchronizer_id (str): ID of the synchronizer on which the party will be registered.
        channel (grpc.Channel): gRPC channel to the confirming participant Admin API.
        auto_accept (bool): Will not ask for confirmation when true.
    """
    print(f"Authorizing hosting of {party_id} on target participant {participant_id}")

    topology_write_client = (
        topology_manager_write_service_pb2_grpc.TopologyManagerWriteServiceStub(channel)
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )

    # Retrieve the pending proposal
    transaction_in_store = False
    party_to_participant_proposals: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse
    )
    while not transaction_in_store:
        party_to_participant_proposals: (
            topology_manager_read_service_pb2.ListPartyToParticipantResponse
        ) = topology_read_client.ListPartyToParticipant(
            topology_manager_read_service_pb2.ListPartyToParticipantRequest(
                base_query=topology_manager_read_service_pb2.BaseQuery(
                    store=common_pb2.StoreId(
                        synchronizer=common_pb2.Synchronizer(
                            id=synchronizer_id,
                        ),
                    ),
                    proposals=True,
                    head_state=empty_pb2.Empty(),
                ),
                filter_party=party_id,
            )
        )
        if len(party_to_participant_proposals.results) > 0:
            break
        else:
            time.sleep(0.5)
            continue
    # Expecting a single pending proposal for the party
    party_to_participant_proposal: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse.Result
    ) = party_to_participant_proposals.results[0]

    if not auto_accept:
        print(MessageToJson(party_to_participant_proposal))
        user_input = input("Authorize party hosting? (y/n): ")
        if user_input.lower() != "y":
            print("Transaction rejected.")
            sys.exit(0)

    # Authorize the hosting
    topology_write_client.Authorize(
        topology_manager_write_service_pb2.AuthorizeRequest(
            transaction_hash=party_to_participant_proposal.context.transaction_hash.hex(),
            must_fully_authorize=False,
            store=common_pb2.StoreId(
                synchronizer=common_pb2.Synchronizer(
                    id=synchronizer_id,
                ),
            ),
        )
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def multi_host_party(
    party_name: str,
    synchronizer_id: str,
    confirming_threshold: int,
    participant_endpoints: [str],
    auto_accept: bool,
) -> (EllipticCurvePrivateKey, str):
    """
    Onboard a multi hosted party.

    Args:
        party_name (str): Name of the party.
        synchronizer_id (str): ID of the synchronizer on which the party will be registered.
        confirming_threshold (int): Minimum number of confirmations that must be received from the confirming participants to authorize a transaction.
        participant_endpoints ([str]]): List of endpoints to the respective hosting participant Admin APIs.
        auto_accept (bool): Will not ask for confirmation when true.
    """
    print(f"Authorizing hosting of {party_name}")
    channels = []
    participant_ids = []
    for participant_endpoint in participant_endpoints:
        channel = grpc.insecure_channel(participant_endpoint)
        channels = channels + [channel]
        # Get the participant id from each participant
        participant_ids = participant_ids + [get_participant_id(channel)]

    (party_private_key, party_namespace) = onboard_external_party(
        party_name,
        participant_ids,
        confirming_threshold,
        synchronizer_id,
        # Pick one of the participants to do the initial external party onboarding
        channels[0],
    )
    party_id = party_name + "::" + party_namespace

    # Authorize hosting for each additional confirming participant
    # In reality this wouldn't be done from a central place like here but every hosting participant validator
    # would run this on their own node
    for index, additional_participant_channel in enumerate(channels[1:]):
        authorize_external_party_hosting(
            participant_ids[index],
            party_id,
            synchronizer_id,
            additional_participant_channel,
            auto_accept,
        )

    # Wait for the party to appear in topology for all participants
    for participant_channel in channels:
        with participant_channel:
            topology_read_client = (
                topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(
                    participant_channel
                )
            )
            wait_to_observe_party_to_participant(
                topology_read_client, synchronizer_id, party_id
            )

    print(f"Multi-Hosted party {party_id} fully onboarded")
    return party_private_key, party_namespace
```

示例用法：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python external_party_onboarding_multi_hosting.py --admin-endpoint localhost:4012 localhost:4022 --synchronizer-id da::12204457ac942c4d839331d402f82ecc941c6232de06a88097ade653350a2d6fc9c5 --party-name charlie --threshold 1 onboard
```

### 离线 Party 复制
<Warning>
  This section only illustrates how to authorize changes to the `PartyToParticipant` mapping of an external party. It is NOT sufficient to fully replicate an existing party to new nodes. Follow the procedure described in the offline party replication documentation.
</Warning>

离线 Party 复制是将已有 Party 复制到额外托管节点的复杂流程，详见离线 party replication 文档。本地与外部 Party 流程类似，但外部 Party 拓扑变更须用拓扑交易签名显式授权 of replicating an existing party to additional hosting nodes. This is a complex process described in detail in the offline party replication documentation. The procedure is similar for local and external parties, with the exception that, as established in this tutorial, changes to the topology

The following code demonstrates how to update the `PartyToParticipant` mapping for an external party via the Canton Admin API:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def update_party_to_participant_transaction(
    channel: grpc.Channel,
    party_id: str,
    additional_participants: [topology_pb2.PartyToParticipant.HostingParticipant],
    synchronizer_id: str,
    confirming_threshold: Optional[int],
) -> (bytes, list[str]):
    """
    Constructs a topology transaction that updates the party-to-participant mapping with additional hosting nodes.

    Args:
        channel (grpc.Channel): gRPC channel for communication with the topology manager.
        party_id (str): Identifier of the party whose key mapping is being updated.
        additional_participants ([topology_pb2.PartyToParticipant.HostingParticipant]): A list of additional hosting participants and their hosting permission.
        synchronizer_id (str): ID of the synchronizer to query the topology state.
        confirming_threshold (int): Updated confirming threshold

    Returns:
        bytes: Serialized topology transaction containing the updated mapping. None if the provided nodes already host the party with those permissions
        [str]: list of participant_ids added to the party hosting and requiring approval
    """
    # Retrieve the current party to participant mapping
    list_party_to_participant_request = (
        topology_manager_read_service_pb2.ListPartyToParticipantRequest(
            base_query=topology_manager_read_service_pb2.BaseQuery(
                store=common_pb2.StoreId(
                    synchronizer=common_pb2.Synchronizer(
                        id=synchronizer_id,
                    ),
                ),
                head_state=empty_pb2.Empty(),
            ),
            filter_party=party_id,
        )
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )
    party_to_participant_response: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse
    ) = topology_read_client.ListPartyToParticipant(list_party_to_participant_request)
    if len(party_to_participant_response.results) == 0:
        current_serial = 0
        current_participants_list = []
    else:
        # Sort the results by serial in descending order and take the first one
        sorted_results = sorted(
            party_to_participant_response.results,
            key=lambda result: result.context.serial,
            reverse=True,
        )
        # Get the mapping with the highest serial and its list of hosting participants
        current_serial = sorted_results[0].context.serial
        current_participants_list: topology_pb2.PartyToParticipant = sorted_results[
            0
        ].item

    # Map of existing participant_uid -> hosting
    participant_id_to_hosting = {
        participant.participant_uid: participant
        for participant in current_participants_list.participants
    }
    # Keep track of the new hosting nodes, as we'll need to approve the hosting on each of them as well
    new_hosting_nodes = []
    # Update map with new participants
    for new_hosting in additional_participants:
        if new_hosting.participant_uid not in participant_id_to_hosting:
            new_hosting_nodes = new_hosting_nodes + [new_hosting.participant_uid]
        participant_id_to_hosting[new_hosting.participant_uid] = new_hosting

    if confirming_threshold is not None:
        updated_threshold = confirming_threshold
    else:
        updated_threshold = current_participants_list.threshold

    # Create a new mapping with the updated hosting relationships and increment the serial
    updated_mapping = topology_pb2.TopologyMapping(
        party_to_participant=topology_pb2.PartyToParticipant(
            party=party_id,
            threshold=updated_threshold,
            participants=list(participant_id_to_hosting.values()),
        )
    )

    # Build the serialized transaction
    return (
        serialize_topology_transaction(updated_mapping, serial=current_serial + 1),
        new_hosting_nodes,
    )
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def update_external_party_hosting(
    party_id: str,
    synchronizer_id: str,
    confirming_threshold: Optional[int],
    additional_hosting_participants: [
        topology_pb2.PartyToParticipant.HostingParticipant
    ],
    namespace_private_key: EllipticCurvePrivateKey,
    admin_api_channel: Channel,
) -> [str]:
    """
    Authorize replication of an external party to additional hosting nodes.

    Args:
        party_id (str): Identifier of the party whose key mapping is being updated.
        synchronizer_id (str): ID of the synchronizer to query the topology state.
        confirming_threshold (Optional[int]): Updated confirming threshold. Optional, if None the threshold stays unchanged.
        admin_api_channel (grpc.Channel): gRPC channel to the .
        additional_hosting_participants ([topology_pb2.PartyToParticipant.HostingParticipant]): A list of additional hosting participants and their hosting permission.
        namespace_private_key (EllipticCurvePrivateKey): private namespace key of the external party

    Returns:
        [str]: list of participant_ids added to the party hosting and requiring approval
    """
    updated_party_to_participant_transaction, nodes_requiring_auth = (
        update_party_to_participant_transaction(
            admin_api_channel,
            party_id,
            additional_hosting_participants,
            synchronizer_id,
            confirming_threshold,
        )
    )

    party_to_participant_transaction_hash = compute_topology_transaction_hash(
        updated_party_to_participant_transaction
    )
    signature = sign_hash(namespace_private_key, party_to_participant_transaction_hash)
    fingerprint = party_id.split("::")[1]
    signed_topology_transaction = topology_pb2.SignedTopologyTransaction(
        transaction=updated_party_to_participant_transaction,
        signatures=[
            crypto_pb2.Signature(
                format=crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
                signature=signature,
                signed_by=fingerprint,
                signing_algorithm_spec=crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
            )
        ],
        multi_transaction_signatures=[],
        proposal=True,
    )

    topology_write_client = (
        topology_manager_write_service_pb2_grpc.TopologyManagerWriteServiceStub(
            admin_api_channel
        )
    )

    add_transactions_request = (
        topology_manager_write_service_pb2.AddTransactionsRequest(
            transactions=[signed_topology_transaction],
            store=common_pb2.StoreId(
                synchronizer=common_pb2.Synchronizer(
                    id=synchronizer_id,
                ),
            ),
        )
    )
    topology_write_client.AddTransactions(add_transactions_request)
    return nodes_requiring_auth
```

示例用法：```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
python external_party_onboarding_multi_hosting.py --admin-endpoint localhost:4002 --synchronizer-id da::12204457ac942c4d839331d402f82ecc941c6232de06a88097ade653350a2d6fc9c5 --threshold 1 --private-key-file charlie::1220a844fb05224ef180032eb41c6ec9283f662beb1167ccb2d2fd9a4f67c0cc1529-private-key.der update --party-id charlie::1220a844fb05224ef180032eb41c6ec9283f662beb1167ccb2d2fd9a4f67c0cc1529 --participant-permission observation
```

完整多方托管外部 Party 示例见： external party multi-hosting, check out this file:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import argparse

from typing import Optional
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from interactive_topology_util import (
    serialize_topology_transaction,
    compute_topology_transaction_hash,
    sign_hash,
)
from cryptography.hazmat.primitives.serialization import load_der_private_key
from cryptography.hazmat.backends import default_backend
from grpc import Channel
from google.protobuf.json_format import MessageToJson
import grpc
from google.protobuf import empty_pb2
from com.digitalasset.canton.protocol.v30 import topology_pb2
from com.digitalasset.canton.crypto.v30 import crypto_pb2
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2_grpc,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_write_service_pb2,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_read_service_pb2_grpc,
)
from com.digitalasset.canton.topology.admin.v30 import (
    topology_manager_read_service_pb2,
    common_pb2,
)
from com.digitalasset.canton.admin.participant.v30 import (
    participant_status_service_pb2,
    participant_status_service_pb2_grpc,
)
from external_party_onboarding_admin_api import (
    onboard_external_party,
    wait_to_observe_party_to_participant,
)

# Authorize an external party hosting on a participant node
def authorize_external_party_hosting(
    participant_id: str,
    party_id: str,
    synchronizer_id: str,
    channel: Channel,
    auto_accept: bool,
) -> bool:
    """
    Authorizes the hosting of a multi-hosted external party on the current node.
    Expects the PartyToParticipant proposal to have already been published to the synchronizer.

    Args:
        party_id (str): ID of the party.
        synchronizer_id (str): ID of the synchronizer on which the party will be registered.
        channel (grpc.Channel): gRPC channel to the confirming participant Admin API.
        auto_accept (bool): Will not ask for confirmation when true.
    """
    print(f"Authorizing hosting of {party_id} on target participant {participant_id}")

    topology_write_client = (
        topology_manager_write_service_pb2_grpc.TopologyManagerWriteServiceStub(channel)
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )

    # Retrieve the pending proposal
    transaction_in_store = False
    party_to_participant_proposals: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse
    )
    while not transaction_in_store:
        party_to_participant_proposals: (
            topology_manager_read_service_pb2.ListPartyToParticipantResponse
        ) = topology_read_client.ListPartyToParticipant(
            topology_manager_read_service_pb2.ListPartyToParticipantRequest(
                base_query=topology_manager_read_service_pb2.BaseQuery(
                    store=common_pb2.StoreId(
                        synchronizer=common_pb2.Synchronizer(
                            id=synchronizer_id,
                        ),
                    ),
                    proposals=True,
                    head_state=empty_pb2.Empty(),
                ),
                filter_party=party_id,
            )
        )
        if len(party_to_participant_proposals.results) > 0:
            break
        else:
            time.sleep(0.5)
            continue
    # Expecting a single pending proposal for the party
    party_to_participant_proposal: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse.Result
    ) = party_to_participant_proposals.results[0]

    if not auto_accept:
        print(MessageToJson(party_to_participant_proposal))
        user_input = input("Authorize party hosting? (y/n): ")
        if user_input.lower() != "y":
            print("Transaction rejected.")
            sys.exit(0)

    # Authorize the hosting
    topology_write_client.Authorize(
        topology_manager_write_service_pb2.AuthorizeRequest(
            transaction_hash=party_to_participant_proposal.context.transaction_hash.hex(),
            must_fully_authorize=False,
            store=common_pb2.StoreId(
                synchronizer=common_pb2.Synchronizer(
                    id=synchronizer_id,
                ),
            ),
        )
    )

def get_participant_id(channel: grpc.Channel) -> str:
    status_service_client = (
        participant_status_service_pb2_grpc.ParticipantStatusServiceStub(channel)
    )
    status_response: participant_status_service_pb2.ParticipantStatusResponse = (
        status_service_client.ParticipantStatus(
            participant_status_service_pb2.ParticipantStatusRequest()
        )
    )
    return status_response.status.common_status.uid

def update_party_to_participant_transaction(
    channel: grpc.Channel,
    party_id: str,
    additional_participants: [topology_pb2.PartyToParticipant.HostingParticipant],
    synchronizer_id: str,
    confirming_threshold: Optional[int],
) -> (bytes, list[str]):
    """
    Constructs a topology transaction that updates the party-to-participant mapping with additional hosting nodes.

    Args:
        channel (grpc.Channel): gRPC channel for communication with the topology manager.
        party_id (str): Identifier of the party whose key mapping is being updated.
        additional_participants ([topology_pb2.PartyToParticipant.HostingParticipant]): A list of additional hosting participants and their hosting permission.
        synchronizer_id (str): ID of the synchronizer to query the topology state.
        confirming_threshold (int): Updated confirming threshold

    Returns:
        bytes: Serialized topology transaction containing the updated mapping. None if the provided nodes already host the party with those permissions
        [str]: list of participant_ids added to the party hosting and requiring approval
    """
    # Retrieve the current party to participant mapping
    list_party_to_participant_request = (
        topology_manager_read_service_pb2.ListPartyToParticipantRequest(
            base_query=topology_manager_read_service_pb2.BaseQuery(
                store=common_pb2.StoreId(
                    synchronizer=common_pb2.Synchronizer(
                        id=synchronizer_id,
                    ),
                ),
                head_state=empty_pb2.Empty(),
            ),
            filter_party=party_id,
        )
    )
    topology_read_client = (
        topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(channel)
    )
    party_to_participant_response: (
        topology_manager_read_service_pb2.ListPartyToParticipantResponse
    ) = topology_read_client.ListPartyToParticipant(list_party_to_participant_request)
    if len(party_to_participant_response.results) == 0:
        current_serial = 0
        current_participants_list = []
    else:
        # Sort the results by serial in descending order and take the first one
        sorted_results = sorted(
            party_to_participant_response.results,
            key=lambda result: result.context.serial,
            reverse=True,
        )
        # Get the mapping with the highest serial and its list of hosting participants
        current_serial = sorted_results[0].context.serial
        current_participants_list: topology_pb2.PartyToParticipant = sorted_results[
            0
        ].item

    # Map of existing participant_uid -> hosting
    participant_id_to_hosting = {
        participant.participant_uid: participant
        for participant in current_participants_list.participants
    }
    # Keep track of the new hosting nodes, as we'll need to approve the hosting on each of them as well
    new_hosting_nodes = []
    # Update map with new participants
    for new_hosting in additional_participants:
        if new_hosting.participant_uid not in participant_id_to_hosting:
            new_hosting_nodes = new_hosting_nodes + [new_hosting.participant_uid]
        participant_id_to_hosting[new_hosting.participant_uid] = new_hosting

    if confirming_threshold is not None:
        updated_threshold = confirming_threshold
    else:
        updated_threshold = current_participants_list.threshold

    # Create a new mapping with the updated hosting relationships and increment the serial
    updated_mapping = topology_pb2.TopologyMapping(
        party_to_participant=topology_pb2.PartyToParticipant(
            party=party_id,
            threshold=updated_threshold,
            participants=list(participant_id_to_hosting.values()),
        )
    )

    # Build the serialized transaction
    return (
        serialize_topology_transaction(updated_mapping, serial=current_serial + 1),
        new_hosting_nodes,
    )

def update_external_party_hosting(
    party_id: str,
    synchronizer_id: str,
    confirming_threshold: Optional[int],
    additional_hosting_participants: [
        topology_pb2.PartyToParticipant.HostingParticipant
    ],
    namespace_private_key: EllipticCurvePrivateKey,
    admin_api_channel: Channel,
) -> [str]:
    """
    Authorize replication of an external party to additional hosting nodes.

    Args:
        party_id (str): Identifier of the party whose key mapping is being updated.
        synchronizer_id (str): ID of the synchronizer to query the topology state.
        confirming_threshold (Optional[int]): Updated confirming threshold. Optional, if None the threshold stays unchanged.
        admin_api_channel (grpc.Channel): gRPC channel to the .
        additional_hosting_participants ([topology_pb2.PartyToParticipant.HostingParticipant]): A list of additional hosting participants and their hosting permission.
        namespace_private_key (EllipticCurvePrivateKey): private namespace key of the external party

    Returns:
        [str]: list of participant_ids added to the party hosting and requiring approval
    """
    updated_party_to_participant_transaction, nodes_requiring_auth = (
        update_party_to_participant_transaction(
            admin_api_channel,
            party_id,
            additional_hosting_participants,
            synchronizer_id,
            confirming_threshold,
        )
    )

    party_to_participant_transaction_hash = compute_topology_transaction_hash(
        updated_party_to_participant_transaction
    )
    signature = sign_hash(namespace_private_key, party_to_participant_transaction_hash)
    fingerprint = party_id.split("::")[1]
    signed_topology_transaction = topology_pb2.SignedTopologyTransaction(
        transaction=updated_party_to_participant_transaction,
        signatures=[
            crypto_pb2.Signature(
                format=crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
                signature=signature,
                signed_by=fingerprint,
                signing_algorithm_spec=crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
            )
        ],
        multi_transaction_signatures=[],
        proposal=True,
    )

    topology_write_client = (
        topology_manager_write_service_pb2_grpc.TopologyManagerWriteServiceStub(
            admin_api_channel
        )
    )

    add_transactions_request = (
        topology_manager_write_service_pb2.AddTransactionsRequest(
            transactions=[signed_topology_transaction],
            store=common_pb2.StoreId(
                synchronizer=common_pb2.Synchronizer(
                    id=synchronizer_id,
                ),
            ),
        )
    )
    topology_write_client.AddTransactions(add_transactions_request)
    return nodes_requiring_auth

def multi_host_party(
    party_name: str,
    synchronizer_id: str,
    confirming_threshold: int,
    participant_endpoints: [str],
    auto_accept: bool,
) -> (EllipticCurvePrivateKey, str):
    """
    Onboard a multi hosted party.

    Args:
        party_name (str): Name of the party.
        synchronizer_id (str): ID of the synchronizer on which the party will be registered.
        confirming_threshold (int): Minimum number of confirmations that must be received from the confirming participants to authorize a transaction.
        participant_endpoints ([str]]): List of endpoints to the respective hosting participant Admin APIs.
        auto_accept (bool): Will not ask for confirmation when true.
    """
    print(f"Authorizing hosting of {party_name}")
    channels = []
    participant_ids = []
    for participant_endpoint in participant_endpoints:
        channel = grpc.insecure_channel(participant_endpoint)
        channels = channels + [channel]
        # Get the participant id from each participant
        participant_ids = participant_ids + [get_participant_id(channel)]

    (party_private_key, party_namespace) = onboard_external_party(
        party_name,
        participant_ids,
        confirming_threshold,
        synchronizer_id,
        # Pick one of the participants to do the initial external party onboarding
        channels[0],
    )
    party_id = party_name + "::" + party_namespace

    # Authorize hosting for each additional confirming participant
    # In reality this wouldn't be done from a central place like here but every hosting participant validator
    # would run this on their own node
    for index, additional_participant_channel in enumerate(channels[1:]):
        authorize_external_party_hosting(
            participant_ids[index],
            party_id,
            synchronizer_id,
            additional_participant_channel,
            auto_accept,
        )

    # Wait for the party to appear in topology for all participants
    for participant_channel in channels:
        with participant_channel:
            topology_read_client = (
                topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(
                    participant_channel
                )
            )
            wait_to_observe_party_to_participant(
                topology_read_client, synchronizer_id, party_id
            )

    print(f"Multi-Hosted party {party_id} fully onboarded")
    return party_private_key, party_namespace

def read_id_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

"""
   Exemple script demonstrating how to onboard a multi hosted external party, and update the hosting relationships of an existing party.
   ATTENTION: Replicating an existing party to additional hosting nodes requires following a specific procedure.
   Check the offline party replication documentation for more details. This script simply demonstrates how to authorize changes
   to the PartyToParticipant mapping for an external party.
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Hosted external party")
    parser.add_argument(
        "--admin-endpoint",
        type=str,
        nargs="+",
        help="address:port of the admin API of hosting nodes",
    )
    parser.add_argument(
        "--synchronizer-id",
        type=str,
        help="Synchronizer ID",
        default=read_id_from_file("synchronizer_id"),
    )
    parser.add_argument(
        "--party-name",
        type=str,
        help="Party name",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        help="Confirmation threshold",
    )
    parser.add_argument(
        "--auto-accept",
        "-a",
        help="Authorize party hosting without explicit confirmation",
        action="store_true",
    )
    parser.add_argument(
        "--private-key-file",
        type=str,
        help="Path of the file holding the external party's private key",
    )

    subparsers = parser.add_subparsers(required=True, dest="subcommand")
    parser_onboard = subparsers.add_parser(
        "onboard", help="Onboard a multi-hosted external party"
    )
    parser_replicate = subparsers.add_parser(
        "update",
        help="Update the permissions or add new hosting nodes to the party-to-participant mapping of an existing external party",
    )
    parser_replicate.add_argument(
        "--party-id",
        type=str,
        help="External party ID",
    )
    parser_replicate.add_argument(
        "--participant-id",
        type=str,
        help="Participant ID of the new hosting participant",
    )
    parser_replicate.add_argument(
        "--participant-permission",
        type=str,
        choices=["confirmation", "observation"],
        nargs="+",
        help="Permission of the new hosting participants (confirmation or observation). One per new hosting participant.",
    )

    args = parser.parse_args()

    if args.subcommand == "onboard":
        party_private_key, party_fingerprint = multi_host_party(
            args.party_name,
            args.synchronizer_id,
            args.threshold,
            args.admin_endpoint,
            args.auto_accept,
        )

        private_key_file = (
            args.private_key_file
            or f"{args.party_name}::{party_fingerprint}-private-key.der"
        )
        with open(private_key_file, "wb") as key_file:
            key_file.write(
                party_private_key.private_bytes(
                    encoding=serialization.Encoding.DER,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        print(f"Party ID: {args.party_name}::{party_fingerprint}")
        print(f"Written private key to: {private_key_file}")

    elif args.subcommand == "update":
        with open(args.private_key_file, "rb") as key_file:
            private_key = load_der_private_key(
                key_file.read(),
                password=None,  # Use this if the key is not encrypted
                backend=default_backend(),
            )
            channels = {}
            # New hosting relationships
            hosting = []
            for index, endpoint in enumerate(args.admin_endpoint):
                channel = grpc.insecure_channel(endpoint)
                participant_id = get_participant_id(channel)
                channels[participant_id] = grpc.insecure_channel(endpoint)
                permission_str = args.participant_permission[index]
                if permission_str == "confirmation":
                    permission = (
                        topology_pb2.Enums.ParticipantPermission.PARTICIPANT_PERMISSION_CONFIRMATION
                    )
                else:
                    permission = (
                        topology_pb2.Enums.ParticipantPermission.PARTICIPANT_PERMISSION_OBSERVATION
                    )

                hosting = hosting + [
                    topology_pb2.PartyToParticipant.HostingParticipant(
                        participant_uid=participant_id, permission=permission
                    )
                ]

            nodes_requiring_auth = update_external_party_hosting(
                args.party_id,
                args.synchronizer_id,
                args.threshold,
                hosting,
                private_key,
                # Pick one of the participants to load the updated hosting mapping signed by the party.
                # It doesn't matter which one here, we just use the node's admin API to load the externally signed
                # updated topology transaction onto the synchronizer
                list(channels.values())[0],
            )
            # Then authorize the hosting on each new hosting node
            for participant_id, channel in channels.items():
                # If new nodes are hosting the party, approve the hosting on the nodes
                if participant_id in nodes_requiring_auth:
                    authorize_external_party_hosting(
                        participant_id,
                        args.party_id,
                        args.synchronizer_id,
                        channel,
                        args.auto_accept,
                    )

                # Observe the party on the participants
                # TODO(i27030): check the permission matches
                topology_read_client = topology_manager_read_service_pb2_grpc.TopologyManagerReadServiceStub(
                    channel
                )
                wait_to_observe_party_to_participant(
                    topology_read_client, args.synchronizer_id, args.party_id
                )
            print("Hosting updated ")
    else:
        parser.print_help()
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/tutorials/app-dev/external_signing_onboarding_lapi.rst" hash="51422925" */}

# 使用 Ledger API 入网外部 Party
本教程演示如何使用 **Admin API** 入网 **外部 Party**。外部 Party 可用自管密钥签署 Daml 交易而无需信任网络节点。建议先阅读外部签名概述；拓扑概念见拓扑教程 an **external party** using the Ledger API.

## 前提条件
This tutorial uses a script which is included as an example in the Canton artifact. Please note that the script uses openssl to create keys on the file system, which is not secure for production use.

获取 Canton 制品见 getting started。在制品目录执行： refer to the getting started section. From the artifact directory, start Canton using the command:

```
./bin/canton -c examples/08-interactive-submission/interactive-submission.conf --bootstrap examples/08-interactive-submission/bootstrap.canton
```

## 运行脚本
本教程步骤包含在制品 `examples/08-interactive-submission/external_party_onboarding.sh` 中，涵盖： in the script `external_party_onboarding.sh` located in the `examples/08-interactive-submission` directory

* 用 openssl 为外部 Party 创建私钥 using openssl for the external party.
* 确定可用 synchronizer-id available.
* 创建定义新外部 Party 的拓扑交易集 transactions to define a new external party.
* 签署拓扑交易.
* 将已签拓扑交易上传到 Ledger API transactions to the Ledger API.

请在启动 Canton 的同一目录运行脚本以便读取 `canton_ports.json`，或用 `-p1 <host>:<port>` 指定 Ledger API 地址 from the same directory where you started Canton such that the script can find the `canton_ports.json` file which contains the port configuration

启动后示例输出：, you will see:

```
./examples/08-interactive-submission/external_party_onboarding.sh
Fetching localhost:7374/v2/state/connected-synchronizers
Detected synchronizer-id "da::1220682ef8618b4425e8b1c5d7104260d5340eb4140509e99050a6bc9c5e8898d7b4"
Requesting generate topology transactions
Signing hash EiAfdSBLNQswwxUq9LyAYqHj8C5FzeZNLVvUJSgyrtORWg== for MyParty::1220ad82d8863893d65f10e2275a2f7b7af5c26cca97a761cb7cdc77d68e1ba20dc5 using ED25519
Submitting onboarding transaction to participant1
Onboarded party "MyParty::1220ad82d8863893d65f10e2275a2f7b7af5c26cca97a761cb7cdc77d68e1ba20dc5"
```

脚本支持若干命令行参数，见源码 a few command line arguments, which you can see by inspecting the code.

## 脚本细节
脚本先用 `v2/connected-synchronizers` 获取 synchronizer-id（假设仅一个）。Party 须在欲托管的每个 synchronizer 上重复分配 synchronizer-ids using the `v2/connected-synchronizers` endpoint, assuming that there is exactly one. The party allocation must be repeated for each synchronizer-id the party should be hosted on.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
SYNCHRONIZER_ID=$(curl -f -s -L ${PARTICIPANT1}/v2/state/connected-synchronizers | jq .connectedSynchronizers.[0].synchronizerId)
```

接着用 openssl 创建外部 Party 的 Ed25519 私钥（亦支持其他密钥类型），导出 DER 公钥并转 base64 a private Ed25519 key for the external party (other types of keys are supported as well). The public key is then extracted in DER format and convert the binary DER format to base64.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate an ed25519 private key and extract its public key
openssl genpkey -algorithm ed25519 -outform DER -out $PRIVATE_KEY_FILE
# Extract the public key from the private key
openssl pkey -in private_key.der -pubout -outform DER -out public_key.der 2> /dev/null
# Convert public key to base64
PUBLIC_KEY_BASE64=$(base64 -w 0 -i public_key.der)
```

脚本使用便捷端点 `/v2/parties/external/generate-topology` 生成拓扑交易（节点可信时可用；否则应手工构建或签署前检查并自行重算哈希） `/v2/parties/external/generate-topology` to generate the topology transactions required to onboard the external party. This is fine if the node is trusted. In other scenarios, the transactions should be built manually or inspected before signing, including recomputing the hash.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Create the JSON payload to generate the onboarding transaction
# Note: otherConfirmingParticipantUids is optional but can be used to add other participants
# as confirming nodes. confirmationThreshold allows to configure the number of required confirmations.
# If not set, all confirming nodes must confirm.
GENERATE=$(cat << EOF
{
  "synchronizer" : $SYNCHRONIZER_ID,
  "partyHint" : "$PARTY_NAME",
  "publicKey" : {
    "format" : "CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO",
    "keyData": "$PUBLIC_KEY_BASE64",
    "keySpec" : "SIGNING_KEY_SPEC_EC_CURVE25519"
  },
  "otherConfirmingParticipantUids" : [$OTHER_PARTICIPANT_UIDS]
}
EOF
)

# Submit it to the JSON API
ONBOARDING_TX=$(curl -f -s -d "$GENERATE" -H "Content-Type: application/json" \
  -X POST ${PARTICIPANT1}/v2/parties/external/generate-topology)
```

便捷端点返回拓扑交易、新 Party 的 party-id、公钥指纹及 multi-hash（对整个交易集的承诺） the generated topology transactions together with the computed party-id for the new party and the fingerprint

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
PARTY_ID=$(echo $ONBOARDING_TX | jq -r .partyId)
TRANSACTIONS=$(echo $ONBOARDING_TX | jq '.topologyTransactions | map({ transaction : .})')
PUBLIC_KEY_FINGERPRINT=$(echo $ONBOARDING_TX | jq -r .publicKeyFingerprint)
MULTI_HASH=$(echo -n $ONBOARDING_TX | jq -r .multiHash)
```

该哈希须由新 Party 私钥签署；脚本用 openssl 签名并转 base64 by the private key

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
echo "Signing hash ${MULTI_HASH} for ${PARTY_ID} using ED25519"
echo -n $MULTI_HASH | base64 --decode > hash_binary.bin
openssl pkeyutl -sign -inkey $PRIVATE_KEY_FILE -rawin -in hash_binary.bin -out signature.bin -keyform DER
SIGNATURE=$(base64 -w 0 < signature.bin)
```

用签名与前述数据向 Ledger API 提交以完成入网： from the previous step, the script submits the topology transactions and the signature to the ledger API to complete the onboarding

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
ALLOCATE=$(cat << EOF
{
  "synchronizer" : $SYNCHRONIZER_ID,
  "onboardingTransactions": $TRANSACTIONS,
  "multiHashSignatures": [{
     "format" : "SIGNATURE_FORMAT_CONCAT",
     "signature": "$SIGNATURE",
     "signedBy" : "$PUBLIC_KEY_FINGERPRINT",
     "signingAlgorithmSpec" : "SIGNING_ALGORITHM_SPEC_ED25519"
  }]
}
EOF
)

RESULT=$(curl -f -s -d "$ALLOCATE" -H "Content-Type: application/json" \
  -X POST ${PARTICIPANT1}/v2/parties/external/allocate)
```

交易可逐笔签署，也可像脚本中一样对合并哈希一次性签署, or together as one hash, as done in the script.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/tutorials/app-dev/external_signing_onboarding_multihosted.rst" hash="83333f88" */}

# 入网多方托管外部 Party
本教程演示如何使用 **Admin API** 入网 **外部 Party**。外部 Party 可用自管密钥签署 Daml 交易而无需信任网络节点。建议先阅读外部签名概述；拓扑概念见拓扑教程 an **external party** using the Ledger API which is hosted on multiple validators. It is a simple extension to the onboard external party tutorial.

## 前提条件
请先完成「入网外部 Party」教程并保留运行中的 Canton 示例。

## 运行脚本
上一教程脚本亦支持多方托管；加 `--multi-hosted` 时默认在两个节点入网。

```
./examples/08-interactive-submission/external_party_onboarding.sh --multi-hosted
```

## 脚本细节

标志 `--multi-hosted` 会在 `generate-topology` 请求中通过下列字段传入第二个 participant id：

```
`"otherConfirmingParticipantUids" : [$OTHER_PARTICIPANT_ID]`
```

该字段使生成的拓扑交易在托管关系中包含额外 participant id。亦可配置 `observingParticipantUids`、`confirmationThreshold` 等；未配置时确认阈值默认为确认节点数。

生成的拓扑交易还须上传到第二个 participant 的 Ledger API：

（将 `ALLOCATE` 请求提交到第二个 participant 的 Ledger API，步骤同上一教程。）

若两个 participant 连接同一 synchronizer，可在 Canton 控制台试验：用 participant1 为内部 Party 创建托管提议（无需外部签署拓扑），由 participant2 批准。

先用 participant1 创建托管提议：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.propose(
        com.digitalasset.canton.topology.PartyId.tryCreate("Alice", participant1.id.uid.namespace),
        newParticipants = Seq(
            (participant1.id, ParticipantPermission.Confirmation),
            (participant2.id, ParticipantPermission.Confirmation),
        ),
    )
    res1: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          Alice::12201ff69b1d...,
          PositiveNumeric(1),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:483ecaff7581...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

在 participant2 列出提议，新提议会很快出现：. The new proposal should appear shortly:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.party_to_participant_mappings.list_hosting_proposals(sequencer1.synchronizer_id, participant2.id)
    res2: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMultiHostingProposal] = Vector(
      ListMultiHostingProposal(
        txHash = SHA-256:483ecaff7581...,
        party = Alice::12201ff69b1d...,
        permission = Confirmation$,
        others = PAR::participant1::12201ff69b1d... -> Confirmation$,
        threshold = 1
      )
    )
```

显示待批准提议，等待第二 participant 签名；可从上一命令输出取得 `txHash`：, awaiting the signature

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val txHash = participant2.topology.party_to_participant_mappings.list_hosting_proposals(sequencer1.synchronizer_id, participant2.id).head.txHash
    txHash : TopologyTransaction.TxHash = TxHash(hash = SHA-256:483ecaff7581...)
```

用 `topology.transactions.authorize` 授权： command topology.transactions.authorize:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.transactions.authorize(sequencer1.synchronizer_id, txHash)
    res4: SignedTopologyTransaction[TopologyChangeOp, TopologyMapping] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          Alice::12201ff69b1d...,
          PositiveNumeric(1),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:483ecaff7581...
      ),
      signatures = Seq(12201ff69b1d..., 1220a4d7463b...),
      proposal
    )
```

为提议加上 participant2 签名；完全签署后 Party 会出现在两节点： to the proposal. Because the proposal is now fully signed, the party will appear as being hosted on both nodes:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.hosted("Alice")
    res5: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        party = Alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = local::122032922613..., permission = Confirmation)
            )
          ),
          ParticipantSynchronizers(
            participant = PAR::participant2::1220a4d7463b...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = local::122032922613..., permission = Confirmation)
            )
          )
        )
      )
    )
```
