---
title: "铸造委托"
slug: "global-synchronizer-splice-fundamentals-rewards-minting"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/splice-fundamentals/rewards-minting.md"
source_title: "Minting Delegations"
tags:
  - global-synchronizer
  - splice-fundamentals
  - rewards-minting
---

# 铸造委托

> 验证者为外部 Party 委托铸造权限的说明。

> 验证者运营商如何向其节点上托管的外部各方授予铸币权

铸造委托允许委托人指示其验证者节点代表同一验证者节点上托管的外部方（受益人）自动铸造奖励。委托人可以是验证者节点钱包中加入的任何一方（例如，验证者运营方，但其他内部方也是可能的）。这对于自动化外部各方的奖励收集很有用。

## 概述

**铸币委托**授予委托方以下权力：

* 代表受益方铸造奖励券
* 为受益人自动合并Amulet（最多达到配置的限制）

以下奖励优惠券类型可以通过委托铸造：

* 验证者奖励优惠券
* 无人认领的活动记录
* 发展基金优惠券
* 应用奖励优惠券
* 验证者活跃度ActivityRecord

<Note>
  要铸造 验证者RewardCoupon，受益人必须首先创建 验证者Right。
</Note>

该委托具有以下关键属性：

|物业 |描述 |
| ------------------ | ----------------------------------------------------------- |
|受益人|代表其进行铸币的外部方 |
|代表|内部人士获授权进行铸币业务 |
|到期 |授权不再有效的时间 |
|Amulet合并限制 |自动合并后保留的Amulet数量 |

## 自动化

当铸币委托处于活动状态时，验证者节点为受益方运行自动化 (`铸造DelegationCollectRewardsTrigger`)，定期：

1. 检查受益人拥有的符合铸造资格的奖励券
2. 代表受益人收集并铸造这些奖励
3. 当计数超过配置的合并限制的两倍时，合并受益人的Amulet

为了使自动化成功运行，必须满足以下条件：

* 委托人必须是验证者节点钱包的加入方（例如，验证者运营方或拥有自己用户帐户的其他内部方）
* 委托不得过期
* 受益人必须至少以观察者模式托管在验证者节点上
* 受益人不应加入钱包应用程序，否则委托自动化会与钱包应用程序的内置自动化发生冲突
* 受益人必须有需要处理的奖励券或Amulet

请注意，铸造委托计入最大 200 个 Splice 钱包方限制。

自动化作为委托方提交交易。交易费用从验证者节点的流量余额中支付。

<Note>
  Amulet合并限制控制受益人Amulet的自动合并：当Amulet数量超过限制的两倍时，最小的Amulet将被合并以准确保持配置的数量。
</Note>

## 管理铸币代表团

铸币委托工作流程包括以下步骤：

1. **提案创建**：受益人创建一个`铸造DelegationProposal`，指定委托人、到期日期和Amulet合并限制。这通常是通过 Ledger API 完成的。
2. **提案接受**：委托人通过钱包 UI 审核并接受（或拒绝）提案。接受后，将创建一个有效的`铸造Delegation`合约。
3. **提现**：当不再需要委托时，委托人可以通过钱包UI进行提现。这将终止委托并停止自动化为受益人铸造奖励。

### 使用“委托”选项卡

委托人可以通过钱包 UI 中的“委托”选项卡管理铸币委托。此选项卡显示两个部分：

#### 拟议代表团

**提议**部分显示当前用户是指定委托人的所有待处理的`铸造DelegationProposal`合约。

对于每项提案，代表可以：

* **接受**：批准授权请求。这将创建一个活跃的铸币委托。如果同一受益人已存在授权，则接受新提案将取代现有授权。
* **拒绝**：拒绝委托请求。这会将提案归档。<Note>
  如果受益人尚未托管在验证者节点上，则“接受”按钮将被禁用。在接受委托之前，必须接待受益人。
</Note>

#### 活跃代表团

**Active** 部分显示当前用户作为委托人的所有当前 `铸造Delegation` 合约。

对于每个活跃的委托，委托人可以：

* **撤回**：终止委托。这会将委托合同存档并阻止自动化为受益人铸造奖励。

### 更换代表团

当代理人接受已拥有有效委托的受益人的提案时，将出现一个确认对话框，其中显示：

* 当前委托的合并阈值和过期值
* 新提案的合并阈值和过期值

接受该提案将自动用新的代表团取代现有代表团。这允许受益人更新其委托参数（例如延长到期日期），而委托人无需先手动撤回旧委托。

<提示>
  要更改委托的到期或Amulet合并限制，受益人应使用更新的值创建新提案。当受托人接受后，现有的受托人将被替换。
</提示>

### 通过 Ledger API 创建提案

希望将铸币委托给委托方的外部各方（受益人）必须创建一份`铸造DelegationProposal`合同。由于受益人通常无法访问钱包 UI，因此他们可以使用 Canton Ledger API 以编程方式创建提案。

#### 先决条件

在创建提案之前，受益人必须：

1. **托管在验证者节点上**：受益方必须托管在他们想要委托铸币的验证者节点上。
2. **Ledger API 访问**：对验证者的 Ledger API 端点进行身份验证的访问，包括：
   * Ledger API URL（例如，`https://<验证者-host>:<port>`）
   * 有效的身份验证凭据（OAuth2 令牌或其他配置的身份验证方法）
   * 受益人的当事人ID
3. **委托方 ID**：委托通常是验证者运营方，但也可以是验证者节点上的另一个内部方。
4. **DSO 方 ID**：网络的 DSO 方 ID。

#### 示例：创建提案

`铸造DelegationProposal` 合约包含一个 `delegation` 字段，其属性与上面概述部分中描述的相同（受益人、委托人、到期日和Amulet合并限制），以及 DSO 方 ID。

所有交互均通过 JSON Ledger API 进行（请参阅其 [OpenAPI 定义](https://github.com/digital-asset/canton/blob/main/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml)）。查看[身份验证文档](/global-synchronizer/reference/security-configuration#configure-api-authentication-and-authorization-with-jwt)，了解有关如何对请求进行身份验证的更多信息。

要创建提案，请通过 Ledger API [命令提交端点](https://github.com/digital-asset/canton/blob/main/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L173)提交 `create` 命令。

首先，设置所需的环境变量：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export LEDGER_API_URL="https://验证者.example.com:5003"
export TOKEN="your-auth-token"
export BENEFICIARY_PARTY="beneficiary::1220abcd..."
export DELEGATE_PARTY="验证者_operator::1220efgh..."
export DSO_PARTY="DSO::1220ijkl..."
export EXPIRES_AT="2025-12-31T23:59:59Z"
# This could be created by
# export EXPIRES_AT="$(date -u -d '+1 year' '+%Y-%m-%dT%H:%M:%SZ')"
export AMULET_MERGE_LIMIT=10
```

然后使用curl创建提案：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
--data-raw '{
  "commands": [
    {
      "CreateCommand": {
        "templateId": "#splice-钱包:Splice.钱包.铸造Delegation:铸造DelegationProposal",
        "createArguments": {
          "delegation": {
            "beneficiary": "'"$BENEFICIARY_PARTY"'",
            "delegate": "'"$DELEGATE_PARTY"'",
            "dso": "'"$DSO_PARTY"'",
            "expiresAt": "'"$EXPIRES_AT"'",
            "amuletMergeLimit": '"$AMULET_MERGE_LIMIT"'
          }
        }
      }
    }
  ]
}' \
"$LEDGER_API_URL/v2/commands"
```有关完整的 Daml 定义，请参阅 [铸造DelegationProposal 模板源代码](https://github.com/canton-network/splice/blob/main/daml/splice-钱包/daml/Splice/钱包/铸造Delegation.daml)。

#### 监控提案状态

受益人可以通过 Ledger API 的[活动合约端点](https://github.com/digital-asset/canton/blob/main/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L620)查询活动的`铸造DelegationProposal`合约来监控其提案状态。

要查询待处理的提案：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
--data-raw '{
  "filter": {
    "filtersByParty": {
      "'"$BENEFICIARY_PARTY"'": {
        "filters": [
          {
            "inclusive": {
              "templateFilters": [
                {"templateId": "#splice-钱包:Splice.钱包.铸造Delegation:铸造DelegationProposal"}
              ]
            }
          }
        ]
      }
    }
  }
}' \
"$LEDGER_API_URL/v2/state/active-contracts"
```

接受后，查询活动的 `铸造Delegation` 合约以确认委托处于活动状态：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
--data-raw '{
  "filter": {
    "filtersByParty": {
      "'"$BENEFICIARY_PARTY"'": {
        "filters": [
          {
            "inclusive": {
              "templateFilters": [
                {"templateId": "#splice-钱包:Splice.钱包.铸造Delegation:铸造Delegation"}
              ]
            }
          }
        ]
      }
    }
  }
}' \
"$LEDGER_API_URL/v2/state/active-contracts"
```

#### 撤回提案

如果受益人想在提案被接受或拒绝之前撤回提案，他们可以通过 Ledger API 的[行使端点](https://github.com/digital-asset/canton/blob/main/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L173)在其提案合同上行使`铸造DelegationProposal_Withdraw`选择权。

首先，从上面的活跃合约查询中获取提案的合约ID，然后执行提现选择：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export PROPOSAL_CONTRACT_ID="00abcd1234..."

curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
--data-raw '{
  "commands": [
    {
      "ExerciseCommand": {
        "templateId": "#splice-钱包:Splice.钱包.铸造Delegation:铸造DelegationProposal",
        "contractId": "'"$PROPOSAL_CONTRACT_ID"'",
        "choice": "铸造DelegationProposal_Withdraw",
        "choiceArgument": {}
      }
    }
  ]
}' \
"$LEDGER_API_URL/v2/commands"
```

### 安全考虑

在管理铸币代表团时，代表们应考虑：

1. **验证受益人**：在接受委托之前，请确保您认可并信任受益人。参与方 ID 应与预期参与方匹配。
2. **流量成本**：验证验证人运营商是否愿意从验证人节点的流量余额中支付铸造交易的成本。
3. **主办状态**：仅接受主办方的委托。 UI 通过禁用非托管受益人的“接受”按钮来强制执行此操作。
4. **监控活跃授权**：定期审查活跃授权并撤回不再需要或授权的任何授权。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
