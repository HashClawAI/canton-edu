---
title: "在 Quickstart 中接入外部 Party"
slug: "appdev-quickstart-external-parties"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/external-parties.md"
source_title: "Onboard External Parties in Quickstart"
tags:
  - appdev
  - quickstart
  - external-parties
---

# 在 Quickstart 中接入外部 Party

> 在 Canton Network Quickstart 中接入并使用外部 Party 的分步指南，含 OpenSSL 密钥、拓扑 API 与签名流程。

# 在 Quickstart 中接入外部 Party

## 简介

External parties control their cryptographic signing keys, which removes
the need to trust any participant node with transaction authorization.
External parties provide full control over transaction signing, ensure
regulatory compliance for transaction authorization, and are independent
of participant node operators.

## 前置条件

* 可访问 participant 节点并具备 Admin API 凭证
* OpenSSL 或等效工具生成密钥
* curl 调用 API（或 grpcurl 用于 gRPC）

## Quickstart LocalNet 设置

If you haven't installed the Canton Network Quickstart application,
refer to `quickstart-cnqs-installation`.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 进入 Quickstart 目录并运行 setup
  cd cn-quickstart
  make setup
 
  # 提示时选择：
  # - 启用 Observability？否
  # - 启用 OAUTH2？否
  # - Party hint：默认
  # - 启用 Test mode：否
 
  # 启动 LocalNet
  make start

```

`.env.local` 应类似：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  OBSERVABILITY_ENABLED=false
  AUTH_MODE=shared-secret
  PARTY_HINT=quickstart-USERNAME-1
  TEST_MODE=off

```

**获取 Admin 令牌**

The external party topology APIs require authentication. In
shared-secret mode, you generate a JWT token using the
`splice-onboarding` container with `app-user` as the subject:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ADMIN_TOKEN=$(docker exec splice-onboarding \
    jwt-cli encode hs256 --s unsafe --p '{"sub": "app-user", "aud": "https://canton.network.global"}')
 
  echo $ADMIN_TOKEN

```

## 生成加密密钥

为外部 Party 创建 Ed25519 密钥对。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 生成 PEM 格式 Ed25519 私钥
  openssl genpkey -algorithm ed25519 -out external_party_private.pem

  # 提取 32 字节公钥并转 hex 供 API 使用
  HEX_PUBLIC_KEY=$(openssl pkey -in external_party_private.pem -pubout -outform DER | tail -c 32 | xxd -p -c 32)
  echo "Hex public key: $HEX_PUBLIC_KEY"

```

## 接入外部 Party

### 生成拓扑交易

Update the `party_hint` value below to match your `.env.local`
configuration.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 从 .env.local 提取 party hint
  PARTY_HINT=$(grep '^PARTY_HINT=' .env.local | cut -d= -f2)

```

Use the validator API to generate the three required topology
transactions:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  GENERATE_RESPONSE=$(curl -sS -X POST http://localhost:2903/api/validator/v0/admin/external-party/topology/generate \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "party_hint": "'"$PARTY_HINT"'",
    "public_key": "'"$HEX_PUBLIC_KEY"'"
  }')

  echo "$GENERATE_RESPONSE" | jq .

```

**示例响应：**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "party_id": "quickstart-USERNAME-1::1220abc123...",
    "topology_txs": [
      {
        "topology_tx": "CowBCAEQAR...",
        "hash": "122032fd29c1..."
      },
      {
        "topology_tx": "Cr4BCAEQAb...",
        "hash": "122088b08d96..."
      },
      {
        "topology_tx": "CqIBCAEQAZ...",
        "hash": "12209ac948be..."
      }
    ]
  }

```

响应包含：

* `party_id`: The allocated party identifier (party hint + key
  fingerprint)
* `topology_txs`: Array of three topology transactions with their
  hashes:
  1. **Root namespace transaction** - Creates the party and sets the
     public key controlling the namespace
  2. **Party to participant mapping** - Hosts the party on the
     participant with Confirmation rights
  3. **Party to key mapping** - Sets the key to authorize Daml
     transactions

### 签署拓扑交易哈希

Each topology transaction returned by the generate API has a `hash`
field that must be signed with your private key. The hash is
hex-encoded.

**提取响应值：**

The `GENERATE_RESPONSE` variable was set by the curl command above. Now
extract the party ID, topology transactions, and hashes:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 提取 party_id 供后续使用
  PARTY_ID=$(echo "$GENERATE_RESPONSE" | jq -r '.party_id')
  echo "Party ID: $PARTY_ID"
 
  # 从 party_id 提取密钥指纹（:: 之后）
  # 第 3 部分签署交易需要
  KEY_FINGERPRINT=${PARTY_ID##*::}
  echo "Key fingerprint: $KEY_FINGERPRINT"
 
  # 提取拓扑交易与哈希
  TOPOLOGY_TX_1=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[0].topology_tx')
  HASH_1=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[0].hash')
 
  TOPOLOGY_TX_2=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[1].topology_tx')
  HASH_2=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[1].hash')
 
  TOPOLOGY_TX_3=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[2].topology_tx')
  HASH_3=$(echo "$GENERATE_RESPONSE" | jq -r '.topology_txs[2].hash')
 
  echo "Hash 1: $HASH_1"
  echo "Hash 2: $HASH_2"
  echo "Hash 3: $HASH_3"

```

**用 Ed25519 私钥签署各哈希：**

The signing commands use temporary files for cross-platform
compatibility:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 签署哈希 1
  printf '%s' "$HASH_1" | xxd -r -p > /tmp/hash1.bin
  SIG_1=$(openssl pkeyutl -sign -inkey external_party_private.pem -rawin -in /tmp/hash1.bin | xxd -p | tr -d '\n')
  echo "Signature 1: $SIG_1"
 
  # 签署哈希 2
  printf '%s' "$HASH_2" | xxd -r -p > /tmp/hash2.bin
  SIG_2=$(openssl pkeyutl -sign -inkey external_party_private.pem -rawin -in /tmp/hash2.bin | xxd -p | tr -d '\n')
  echo "Signature 2: $SIG_2"
 
  # 签署哈希 3
  printf '%s' "$HASH_3" | xxd -r -p > /tmp/hash3.bin
  SIG_3=$(openssl pkeyutl -sign -inkey external_party_private.pem -rawin -in /tmp/hash3.bin | xxd -p | tr -d '\n')
  echo "Signature 3: $SIG_3"

```

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  The hashes and signatures are hex-encoded strings. The submit API
  expects:

  * `topology_tx`: Base64-encoded topology transaction (as returned by
    generate)
  * `signed_hash`：交易哈希的 Ed25519 签名（hex）
</div>

### 提交已签拓扑交易

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  curl -X POST http://localhost:2903/api/validator/v0/admin/external-party/topology/submit \
    -H "Authorization: Bearer $ADMIN_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "public_key": "'"$HEX_PUBLIC_KEY"'",
      "signed_topology_txs": [
        {
          "topology_tx": "'"$TOPOLOGY_TX_1"'",
          "signed_hash": "'"$SIG_1"'"
        },
        {
          "topology_tx": "'"$TOPOLOGY_TX_2"'",
          "signed_hash": "'"$SIG_2"'"
        },
        {
          "topology_tx": "'"$TOPOLOGY_TX_3"'",
          "signed_hash": "'"$SIG_3"'"
        }
      ]
    }'

```

**成功响应：**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "party_id": "quickstart-USERNAME-1::1220abc123..."
  }

```

### 验证 Party 创建

After submitting the signed topology transactions, verify the external
party was created successfully.

为 `ledger-api-user` 生成 Ledger API 令牌。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  LEDGER_TOKEN=$(docker exec splice-onboarding \
    jwt-cli encode hs256 --s unsafe --p '{"sub": "ledger-api-user", "aud": "https://canton.network.global"}')

```

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 查询 parties 端点验证 party 存在
  curl -f -sS "http://localhost:2975/v2/parties?parties=$PARTY_ID" \
    -H "Authorization: Bearer $LEDGER_TOKEN"

```

**发现 Synchronizer ID**

The synchronizer ID identifies the network your participant is connected
to and is required for topology validation and transaction submission.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 从已连接 synchronizer 获取 ID
  SYNCHRONIZER_ID=$(curl -f -sS -L http://localhost:2975/v2/state/connected-synchronizers \
    -H "Authorization: Bearer $LEDGER_TOKEN" | jq -r ".connectedSynchronizers[0].synchronizerId")
 
  echo "Synchronizer ID: $SYNCHRONIZER_ID"

```

通常返回如 `global-domain::12209d604bfb...`。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 列出 party-participant 映射验证拓扑
  grpcurl -plaintext -d '{
    "base_query": {
      "store": {
        "synchronizer": {"id": "'"$SYNCHRONIZER_ID"'"}
      },
      "head_state": {}
    },
    "filter_party": "'"$PARTY_ID"'"
  }' localhost:2902 com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/ListPartyToParticipant

```

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  Topology transaction submission is asynchronous. The party may take a
  few seconds to appear in the topology state after successful submission.
  Implement a retry loop with a short delay if immediate verification is
  required.
</div>

## 以外部 Party 提交交易

### 概览

Unlike internal parties (1-step submission), external parties use a
3-step interactive submission process:

1. **Prepare** - Request transaction preparation from a participant
   node
2. **Sign** — 用外部密钥签署交易哈希
3. **Execute** — 提交已签交易

### 步骤 1：准备交易

Use the `InteractiveSubmissionService/PrepareSubmission` gRPC endpoint
to prepare your transaction.

The `Canton.Internal.Ping` template is available on all Canton
participants without deploying any DAR files. The Ping template requires
an `initiator` (your external party) and a `responder` (any other known
party).

Retrieve the `app_user` party from your Quickstart LocalNet to use as
responder:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  RESPONDER_PARTY=$(grpcurl -plaintext -H "Authorization: Bearer $LEDGER_TOKEN" localhost:2901 \
    com.daml.ledger.api.v2.admin.PartyManagementService/ListKnownParties | \
    jq -r '.party_details[] | select(.party | startswith("app_user")) | .party' | head -1)

  echo "Responder party: $RESPONDER_PARTY"

```

提交 `Ping` 合约：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  grpcurl -emit-defaults -plaintext \
    -H "Authorization: Bearer $LEDGER_TOKEN" \
    -d '{
      "user_id": "ledger-api-user",
      "command_id": "'"$(uuidgen)"'",
      "act_as": ["'"$PARTY_ID"'"],
      "synchronizer_id": "'"$SYNCHRONIZER_ID"'",
      "commands": [
        {
          "create": {
            "template_id": {
              "package_id": "#canton-builtin-admin-workflow-ping",
              "module_name": "Canton.Internal.Ping",
              "entity_name": "Ping"
            },
            "create_arguments": {
              "fields": [
                { "label": "id", "value": { "text": "external-party-ping-test" } },
                { "label": "initiator", "value": { "party": "'"$PARTY_ID"'" } },
                { "label": "responder", "value": { "party": "'"$RESPONDER_PARTY"'" } }
              ]
            }
          }
        }
      ]
    }' localhost:2901 \
    com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/PrepareSubmission \
    > prepare_response.json

```

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  The `user_id` must be `ledger-api-user` to match the JWT subject used
  for the `LEDGER_TOKEN`.
</div>

<div class="tip" markdown="1">
  <div class="title" markdown="1">
    Tip
  </div>

  To use your own Daml templates instead of the built-in Ping, replace the
  `template_id` fields with your package ID, module name, and template
  name. Discover deployed packages using:

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       grpcurl -plaintext -H "Authorization: Bearer $LEDGER_TOKEN" localhost:2901 \
         com.daml.ledger.api.v2.PackageService/ListPackages

  ```
</div>

**响应字段：**

* `prepared_transaction`: The full transaction and metadata to be
  signed
* `prepared_transaction_hash`: Pre-computed hash (recompute
  client-side for security)
* `hashing_scheme_version`: Version of the hashing algorithm
  (typically `HASHING_SCHEME_VERSION_V2`)

提取 prepared transaction 与哈希以供签署：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  PREPARED_TRANSACTION=$(cat prepare_response.json | jq .prepared_transaction)
  TRANSACTION_HASH=$(cat prepare_response.json | jq -r .prepared_transaction_hash)

```

### 步骤 2：验证并签署

**1. 验证交易**

Before signing, inspect the prepared transaction to verify it matches
your intent:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  cat prepare_response.json | jq .prepared_transaction

```

**2. 签署哈希**

Sign the `$TRANSACTION_HASH` returned by `PrepareSubmission` with your
Ed25519 private key:

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  For production deployments, you may want to recompute the transaction
  hash client-side rather than trusting the pre-computed hash. A Python
  implementation is available in the Canton release artifact at
  `examples/08-interactive-submission/daml_transaction_hashing_v2.py`.
</div>

**用私钥签署哈希：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # 将 base64 哈希解码到临时文件
  printf '%s' "$TRANSACTION_HASH" | base64 --decode > /tmp/tx_hash.bin
 
  # 签署并 base64 编码
  SIGNATURE=$(openssl pkeyutl -sign -inkey external_party_private.pem -rawin -in /tmp/tx_hash.bin | base64 | tr -d '\n')

```

保存签名供 execute 步骤使用。

### 步骤 3：执行提交

Submit the signed transaction using
`InteractiveSubmissionService/ExecuteSubmission`:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  SUBMISSION_ID=$(uuidgen)
 
  grpcurl -emit-defaults -plaintext \
    -H "Authorization: Bearer $LEDGER_TOKEN" \
    -d '{
      "prepared_transaction": '"$PREPARED_TRANSACTION"',
      "hashing_scheme_version": "HASHING_SCHEME_VERSION_V2",
      "user_id": "ledger-api-user",
      "submission_id": "'"$SUBMISSION_ID"'",
      "party_signatures": {
        "signatures": [
          {
            "party": "'"$PARTY_ID"'",
            "signatures": [
              {
                "format": "SIGNATURE_FORMAT_CONCAT",
                "signature": "'"$SIGNATURE"'",
                "signing_algorithm_spec": "SIGNING_ALGORITHM_SPEC_ED25519",
                "signed_by": "'"$KEY_FINGERPRINT"'"
              }
            ]
          }
        ]
      }
    }' localhost:2901 \
    com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/ExecuteSubmission

```

**关键字段：**

* `submission_id`: A new UUID for this submission attempt (can retry
  with a new ID without re-signing)
* `party_signatures`: Contains the signature with format, algorithm
  spec, and the signing key fingerprint

### 观察交易结果

Verify the transaction was processed using the `CompletionStream`
endpoint.

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  `CompletionStream` is a blocking endpoint that waits for new
  completions. Open a **second terminal** and run this command **before**
  executing Step 3, or re-generate `LEDGER_TOKEN` and `PARTY_ID` in the
  new terminal first.
</div>

在第二个终端：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  grpcurl -emit-defaults -plaintext -H "Authorization: Bearer $LEDGER_TOKEN" -d '{
    "user_id": "ledger-api-user",
    "parties": ["'"$PARTY_ID"'"]
  }' localhost:2901 \
    com.daml.ledger.api.v2.CommandCompletionService/CompletionStream \
    > completion_response.json

```

The stream captures the completion after executing Step 3 in your
original terminal. Stop the stream, then inspect the result:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  cat completion_response.json | jq .

  ``status.code`` 为 ``0`` 表示成功：

```

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  {
    "completion": {
      "command_id": "your-command-id",
      "status": { "code": 0, "message": "" },
      "update_id": "1220...",
      "offset": "24"
    }
  }

```

**查询交易详情（可选）**

Extract the `offset` from the completion and use `GetUpdates` to
retrieve full transaction details:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  COMPLETION_OFFSET=$(cat completion_response.json | jq -r '.completion.offset')

  grpcurl -emit-defaults -plaintext -H "Authorization: Bearer $LEDGER_TOKEN" -d '{
    "begin_exclusive": '"$((COMPLETION_OFFSET - 1))"',
    "end_inclusive": '"$COMPLETION_OFFSET"',
    "update_format": {
      "include_transactions": {
        "transaction_shape": "TRANSACTION_SHAPE_ACS_DELTA",
        "event_format": {
          "filters_by_party": {
            "'"$PARTY_ID"'": {
              "cumulative": [{ "wildcard_filter": {} }]
            }
          }
        }
      }
    }
  }' localhost:2901 \
    com.daml.ledger.api.v2.UpdateService/GetUpdates

```

<div class="note" markdown="1">
  <div class="title" markdown="1">
    Note
  </div>

  External parties authenticate via cryptographic signatures rather than
  ledger user rights. This means `GetUpdateById` (which requires
  `can_read_as` rights) won't work for external party transactions. Use
  `GetUpdates` with the offset range instead.
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
