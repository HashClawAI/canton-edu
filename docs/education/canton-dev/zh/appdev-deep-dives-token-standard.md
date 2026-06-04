---
title: "代币标准"
slug: "appdev-deep-dives-token-standard"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/token-standard.md"
source_title: "Token Standard"
tags:
  - appdev
  - deep-dives
  - token-standard
---

# 代币标准

> Canton Network 代币标准 API 与 Daml 接口

## 概览

* 参阅 [CIP-0056 全文](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 了解 Canton Network 代币标准所含 API。
* 参阅[源码 README](https://github.com/canton-network/splice/tree/main/token-standard#readme) 了解如何使用这些 API。

## Holding UTXO 管理

与比特币类似，Canton 使用 UTXO 模型，其中 UTXO 为所有实现 `Holding` 接口的活跃合约。

活跃的 `Holding` 合约会在托管用户的验证者节点以及托管代币管理员的验证者节点上产生存储与计算成本。为高效利用网络资源，我们建议钱包提供方尽量保持每用户 UTXO 数量较低，即平均每用户约 **10 个以下** UTXO。

这也能优化 traffic 成本，因为转账的每个 UTXO 输入都会增加额外 traffic。该建议也与 Canton Coin 等代币的激励一致，其会：

* 单笔转账最多允许 100 个输入合约，从而抑制过度拆分持仓
* 对初始金额低于累计持有费的 coin UTXO 做过期处理，从而抑制「尘埃」UTXO

我们建议钱包提供方实施 UTXO 管理策略：

* 优先选择金额较小的 `Holding` UTXO 作为转账输入
* 在钱包 onboarding 时让用户配置 `MergeDelegation` 合约（见文档），使钱包提供方可代表用户自动合并小额 `Holding` UTXO

<Note>
  `MergeDelegation` 合约还允许钱包提供方通过单次批量调用，对多用户、多工具执行空投并与持仓自动合并。Featured 钱包提供方为用户执行合并还可获得 featured 应用奖励。
</Note>

### 配置 MergeDelegation

<Tabs>
  <Tab title="DevNet (0.6.4)">
    若你是为用户运行验证者节点的钱包提供方，可按以下步骤为用户配置 `MergeDelegation` 合约。

    1. 从发布包中提取最新版 `splice-util-token-standard-wallet.dar`（<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">下载包（DevNet 0.6.4）</a>）。
    2. 将 `.dar` 上传到你的验证者节点。
    3. 调整用户 onboarding 流程，使用户签署创建 `MergeDelegationProposal` 合约（见文档）。
    4. 以钱包提供方 Party 对 `MergeDelegationProposal` 行使 `Accept` choice 予以接受。
  </Tab>

  <Tab title="TestNet (0.6.3)">
    若你是为用户运行验证者节点的钱包提供方，可按以下步骤为用户配置 `MergeDelegation` 合约。

    1. 从发布包中提取最新版 `splice-util-token-standard-wallet.dar`（<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">下载包（TestNet 0.6.3）</a>）。
    2. 将 `.dar` 上传到你的验证者节点。
    3. 调整用户 onboarding 流程，使用户签署创建 `MergeDelegationProposal` 合约（见文档）。
    4. 以钱包提供方 Party 对 `MergeDelegationProposal` 行使 `Accept` choice 予以接受。
  </Tab>

  <Tab title="MainNet (0.6.2)">
    若你是为用户运行验证者节点的钱包提供方，可按以下步骤为用户配置 `MergeDelegation` 合约。

    1. 从发布包中提取最新版 `splice-util-token-standard-wallet.dar`（<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">下载包（MainNet 0.6.2）</a>）。
    2. 将 `.dar` 上传到你的验证者节点。
    3. 调整用户 onboarding 流程，使用户签署创建 `MergeDelegationProposal` 合约（见文档）。
    4. 以钱包提供方 Party 对 `MergeDelegationProposal` 行使 `Accept` choice 予以接受。
  </Tab>
</Tabs>

### 使用 MergeDelegation

建议以批量方式使用 `MergeDelegation` 合约：

1. 在验证者节点 setup 时为钱包提供方 Party 创建单个 `BatchMergeUtility` 合约（见文档）。

2. 在验证者节点上为钱包提供方用户授予 `CanReadAsAnyParty` 权限，以便读取所有用户的 `Holding` UTXO。

3. 运行定期执行以下步骤的后台进程：

   > 1. 找出拥有超过 10 个 `Holding` UTXO 的用户。例如通过 [Participant Query Store](/zh/docs/canton/appdev-modules-m4-query-with-pqs) 提供的数据库；或直接从验证者 Ledger API 读取 Holding 合约（前者更可扩展）。
   >
   > 2. 按 `token_standard_usage_executing_factory_choice` 中的说明查询 registry API，构造合并多余 `Holding` 合约的转账 choice。
   >
   > 3. 查找每位用户的 `MergeDelegation` 合约，构造相应的 `MergeDelegation_Merge` choice 调用。
   >
   > 4. 将约 100 个 merge delegation choice 组装为对 `BatchMergeUtility_MergeHoldings` choice 的单次调用。
   >
   > 5. 查找上文创建的 `BatchMergeUtility` 合约 ID。
   >
   > 6. 在验证者节点上以钱包提供方用户行使 `BatchMergeUtility_MergeHoldings` choice 执行批量合并。使用 Ledger API 行使 choice，并确保在单次调用中加入前述步骤获得的全部 disclosed contracts。
   >
   >    可为提高吞吐并行执行多批。

可选：在合并调用中加入从运营方 Party 发起的转账，以批量方式实现空投活动。

### 从自定义 MergeDelegation 升级

部分钱包提供方已有自定义 merge delegation 合约，可与 Splice 提供的 `MergeDelegation` 并存，**不强制**升级到 Splice 合约。

若希望升级（例如使用额外功能），可：

1. 在 `CustomMergeDelegation` 模板上添加 `CustomMergeDelegation_Upgrade` choice，为用户创建 `MergeDelegation` 合约；将 choice 设为 `consuming`，以便升级时归档旧 `CustomMergeDelegation`。
2. 提升自定义 merge delegation `.dar` 版本并构建新发布。
3. 将新 `custom-merge-delegation.dar` 上传到验证者节点。
4. 对现有全部 `CustomMergeDelegation` 调用 `CustomMergeDelegation_Upgrade`，升级为 Splice 提供的 `MergeDelegation`

## 钱包与代币标准资产集成

本节为钱包开发者提供与代币标准资产集成的指引。集成通过向托管钱包用户 Party 的验证者 Ledger API 发送正确的读写请求完成。共有五类集成模式：

> * `token_standard_usage_reading_contracts`
> * `token_standard_usage_reading_tx_history`
> * `token_standard_usage_executing_factory_choice`
> * `token_standard_usage_executing_nonfactory_choice`
> * `token_standard_usage_custom_daml_code`

这些模式已封装在 `canton-network/wallet-gateway` 仓库的 [Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk) 中，并[在此文档](/zh/docs/canton/integrations-wallet-guidance)说明。

上述模式在 [代币标准 CLI 实验命令行](https://github.com/canton-network/splice/tree/main/token-standard#cli) 中也有可执行示例。下文各节先链接代码，再补充实现背景。

所有交互均通过 JSON Ledger API（[OpenAPI 定义](https://docs.canton.network/sdks-tools/api-reference/json-api)）。该定义也可在 `http(s)://${YOUR_PARTICIPANT}/docs/openapi` 访问。建议使用 OpenAPI 代码生成工具，而非手写 HTTP 请求。

认证请参阅[认证文档](/zh/docs/canton/global-synchronizer-reference-security-configuration#configure-api-authentication-and-authorization-with-jwt)。

### 读取实现代币标准接口的合约

参考代码：[Token Standard CLI 按接口列出合约](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/listContractsByInterface.ts)

代币标准包含多个由 Daml 模板实现的接口。要列出实现某接口的全部合约，需查询 participant 的[活跃合约端点](https://docs.canton.network/sdks-tools/api-reference/json-api)。

`activeAtOffset` 可设为 participant [ledger-end 端点](https://docs.canton.network/sdks-tools/api-reference/json-api#ledger-end) 的结果以获取最新 ACS，或使用更早（未修剪）的 offset 获取该时刻 ACS。

按 Party 与接口过滤时，`filtersByParty` 应包含 `InterfaceFilter`：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "filtersByParty": {
    "$A_PARTY": {
      "cumulative": [
        {
          "identifierFilter": {
            "InterfaceFilter": {
              "value": {
                "interfaceId": "$AN_INTERFACE_ID",
                "includeInterfaceView": true,
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    }
  }
}
```

例如：

* `"$A_PARTY"` 可能形如 `test::1220a0db3761b3fc919b55e7ff80ad740824336010bfde8829611c0e64477ab7bee5`。
* `"$AN_INTERFACE_ID"` 可能为 `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding`。

还可设置三个标志：

* `includeInterfaceView`：在响应中包含合约的接口视图。
* `includeCreatedEventBlob`：包含 [显式披露](/zh/docs/canton/appdev-deep-dives-explicit-contract-disclosure) 所需的二进制 blob。
* `verbose`：在响应中包含更多信息。

此类查询的响应包含合约的 `createdEvent`（含所请求的接口视图）。其中的 `viewValue` 为 JSON 序列化的 Daml 接口视图。若请求多个接口，可通过 `interfaceId` 区分。[Holding 示例响应](https://github.com/canton-network/splice/blob/main/token-standard/cli/__tests__/mocks/data/holdings.json)。

### 读取并解析涉及代币标准合约的交易历史

示例代码：[Token Standard CLI 列出交易](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/listHoldingTransactions.ts)

participant 提供[列出交易端点](https://docs.canton.network/sdks-tools/api-reference/json-api)，包含所提供 Party 与接口相关的全部交易。

过滤方式与上节相同，`filtersByParty` 含 `InterfaceFilter`：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "filtersByParty": {
    "$A_PARTY": {
      "cumulative": [
        {
          "identifierFilter": {
            "InterfaceFilter": {
              "value": {
                "interfaceId": "$AN_INTERFACE_ID",
                "includeInterfaceView": true,
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    }
  }
}
```

例如：

* `"$A_PARTY"` 同上。
* `"$AN_INTERFACE_ID"` 可为 `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding`，以读取指定 Party 的全部 `Holding` 合约。

要包含不直接涉及接口的其他交易节点（例如非接口特定的子节点），可在 `cumulative` 过滤数组中加入 `WildcardFilter`：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "identifierFilter": {
    "WildcardFilter": {
      "value": {
        "includeCreatedEventBlob": true
      }
    }
  }
}
```

`beginExclusive` 为开始读取交易的 offset。分页时，可从 `GET ${PARTICIPANT_URL}/v2/state/latest-pruned-offsets` 的 `participantPrunedUpToInclusive` 开始，后续传入上一响应最后一笔交易的 offset。

#### 解析历史

示例代码：[解析器](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/txparse/parser.ts)。它通过解析涉及 `Holding` 与 `TransferInstruction` 接口的交易，提取用户可读的钱包历史。

端点返回交易树数组，交易按账本顺序排列。给定 `nodeId=X` 且 `lastDescendantNodeId=Y` 的 `ExercisedEvent`，其子节点为 `nodeId` 在 `[X+1, Y]` 范围内的节点。`CreatedEvent` 与 `ArchivedEvent`（或 `consuming=true` 的 `ExercisedEvent`）无子节点。

据此可对交易节点做树形遍历。代币标准解析器通常关注代币标准 choice 的行使及实现代币标准接口的合约创建。需要进一步定制时，也可关注标准外的内部/特定 choice。

每个代币标准 exercise 节点中可找到：

* 正在执行的 choice，用于区分操作类型。
* 通过子节点的归档/创建可发现其他相关操作，例如 `Holding` 的创建或归档。
* 元数据键值，标准部分包括：
  * `splice.lfdecentralizedtrust.org/tx-kind`：节点操作类型，可比 exercised choice 更具体，取值包括：
    * `transfer`
    * `merge-split`
    * `burn`
    * `mint`
    * `unlock`
    * `expire-dust`
  * `splice.lfdecentralizedtrust.org/sender`：节点中的发送方 Party。
  * `splice.lfdecentralizedtrust.org/reason`：说明操作原因的文本。
  * `splice.lfdecentralizedtrust.org/burned`：节点中销毁的持仓数量。

<Warning>
  元数据键值可出现在多个可选字段中。对转账，应按以下顺序以「后写覆盖」合并各字段中的值：

  * event.choiceArgument.transfer.meta,
  * event.choiceArgument.extraArgs.meta,
  * event.choiceArgument.meta,
  * event.exerciseResult.meta,
</Warning>

### 执行 factory choice

示例代码：[Token Standard CLI 通过 TransferFactory 创建转账](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/transfer.ts)

通过代币标准 factory 执行 choice 时，需先从对应 registry 获取 factory。

<Note>
  工具 `admin` Party ID 到 registry URL 的映射目前需由钱包自行维护，直至基于 CNS 等的通用方案（见 [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#off-ledger-api-discovery-and-access)）落地。
</Note>

registry 在对应端点返回相关 factory：

* TransferFactory
* AllocationFactory

响应 payload 包含三个关键字段：

* `factoryId`：factory 合约 ID
* `disclosedContracts`：行使 factory choice 时必须提供
* `choiceContextData`：作为 `choiceArgument` 中的 `context` 传入

据此可在 factory 上执行 choice。对外部 Party 须调用 participant 的 [prepare](https://docs.canton.network/sdks-tools/api-reference/json-api#interactive-submission) 与 [execute](https://docs.canton.network/sdks-tools/api-reference/json-api#interactive-submission) 端点；非外部 Party 可使用 [submit-and-wait](https://docs.canton.network/sdks-tools/api-reference/json-api#command-submission)。

两种情况下 payload 均须包含 `ExerciseCommand`，字段包括：

* `templateId`：要行使 choice 的 factory 接口 ID，例如 `#splice-api-token-transfer-instruction-v1:Splice.Api.Token.TransferInstructionV1:TransferFactory`。
* `contractId`：registry 返回的 `factoryId`。
* `choice`：要执行的 choice 名称，例如 `TransferFactory_Transfer`。
* `choiceArgument`：传入 Daml choice 的参数（由 JSON 解码），`TransferFactory_Transfer` 包括发送方、接收方、金额等。

### 执行非 factory choice

示例代码：[Token Standard CLI 接受转账指令](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/acceptTransferInstruction.ts)

对实现代币标准接口的合约执行 choice 时，外部 Party 须使用 prepare/execute；非外部 Party 使用 submit-and-wait。`ExerciseCommand` 字段：

* `templateId`：合约接口 ID，例如 `#splice-api-token-transfer-instruction-v1:Splice.Api.Token.TransferInstructionV1:TransferInstruction`。
* `contractId`：要行使 choice 的合约 ID，通常来自 Party 当前 ACS。
* `choice`：例如 `TransferInstruction_Accept`。
* `choiceArgument`：由 JSON 解码的 Daml 参数。

当 `choiceArgument` 需要 `context` 时，可从对应 registry 获取：

* 接受 TransferInstruction
* 拒绝 TransferInstruction
* 撤回 TransferInstruction
* 撤回 Allocation
* 取消 Allocation

这些端点响应包含：

* `choiceContextData`：作为 `choiceArgument` 的 `context`
* `disclosedContracts`：在 submit 或 prepare 请求中传入

<Warning>
  `AllocationRequest_Reject` 与 `AllocationRequest_Withdraw` 应使用空 choice context 调用。保留 `ChoiceContext` 是为未来扩展这些 choice 的实现行为。
</Warning>

### 在自定义 Daml 代码中调用代币标准 choice

在自定义 Daml 中调用代币标准 choice 有助于将自有应用流程与代币标准集成。对钱包提供方，相关流程包括合并用户持仓以控制 ACS 规模、批量转账，或将用户操作标记为钱包应用活动。

Splice 发布可选的 `splice-util-token-standard-wallet.dar`，封装常见钱包运维流程。见 [splice-util-token-standard-wallet](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-util-token-standard-wallet) 各模板参考。

## API 参考

更多背景见 [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#details)。

### 代币元数据

* Daml 参考：[splice-api-token-metadata-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-metadata-v1)
* OpenAPI：[Token Metadata Service](https://docs.canton.network/reference/splice-token-metadata-service/get-registry-metadata-v1-info)

### Holding

用于实现 [Portfolio View](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#wallet-client--portfolio-view)。

* Daml 参考：[splice-api-token-holding-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-holding-v1)

### Transfer Instruction

用于实现 [点对点直接 / 货银对付（FOP）转账](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#direct-peer-to-peer--free-of-payment-fop-transfer-workflow)。

* Daml 参考：[splice-api-token-transfer-instruction-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-transfer-instruction-v1)
* OpenAPI：[Transfer Instruction API](https://docs.canton.network/reference/splice-transfer-instruction-api/post-registry-transfer-instruction-v1-transfer-factory)

### Allocation

与下文 Allocation Instruction、Allocation Request API 共同实现 [券款对付（DVP）工作流](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#delivery-versus-payment-dvp-transfer-workflows)。

* Daml 参考：[splice-api-token-allocation-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-v1)
* OpenAPI：[Allocation API](https://docs.canton.network/reference/splice-allocation-api/post-registry-allocations-v1-allocationid-choice-contexts-execute-transfer)

### Allocation Instruction

* Daml 参考：[splice-api-token-allocation-instruction-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-instruction-v1)
* OpenAPI：[Allocation Instruction API](https://docs.canton.network/reference/splice-allocation-instruction-api/post-registry-allocation-instruction-v1-allocation-factory)

### Allocation Request

* Daml 参考：[splice-api-token-allocation-request-v1](https://docs.canton.network/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-request-v1)

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
