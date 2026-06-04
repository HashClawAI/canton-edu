---
title: "SV 治理参考"
slug: "overview-reference-sv-governance-reference"
locale: "zh"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/sv-governance-reference.md"
source_title: "SV Governance Reference"
tags:
  - overview
  - reference
  - sv-governance-reference
---

# SV 治理参考

> Global Synchronizer 超级验证者治理机制参考。

> 去中心化同步器运营商 (DSO) 的治理模型、投票机制和治理行动

全局同步器由其超级验证器（SV）管理，这些超级验证器共同充当去中心化同步器操作员（DSO）。治理决策是使用`splice-dso-governance`包中定义的Daml合约通过链上投票做出的。

## DSO 治理模型

CC、CNS 和全局同步器治理以去中心化方式实现，以容忍最多 `f` 故障或不诚实的 SV 节点，实现`f = numSvNodes - t` 和确认阈值`t = ceiling (numSvNodes * 2.0 / 3.0)`。

该实现使用三种关键技术来实现这种拜占庭容错：

* **DSO方**：它建立了一个去中心化的Daml方，称为DSO方，确认阈值`t`并托管在所有SV节点上。
* **账本确认**：它需要来自 `t` SV 节点的明确账本确认，以便以 DSO 方的名义使用账外输入进行选择。
* **去中心化自动化**：所有 SV 节点都运行自动化代码，尝试执行 DSO 方所需执行的选择。如果不需要账外输入，则选择直接执行；如果需要账外输入，则通过创建相应的确认来间接执行。自动化会及时执行选择，以便目标时间和实际时间之间的偏差平均而言是有限的。
* **基于中值的投票**：使用基于中值的投票来实现转换率和类似配置参数的一致，其中每个 SV 运营商在账本上发布其所需的值，而 DSO 方使用这些值的中值。

因此，愿意假设不超过 `f` 个 SV 节点不诚实的 CC 和 CNS 用户可以依赖以下保证：

* **有效交易**：每笔需要DSO方确认的交易都是[有效](/zh/docs/canton/overview-learn-ledger-model)。
* **及时自动化**：DSO 方需要采取的行动及时采取。
* **可预测的费用和配置值**：费用和配置值是可以合理预测的，因为它们代表了 SV 运营商约 2/3 的“总偏好”，可以假设这些运营商是按照自己的最佳利益行事的。

有效交易的保证对于 CC 和 CNS 用户来说尤其重要，因为它用于将实现去中心化自动化和治理的关注点与实现 CC 和 CNS 的代币经济和业务逻辑的关注点脱钩。

除 `splice-dso-governance` 和 `splice-validator-lifecycle` 之外的所有代码都是在 DSO 方充当 CC 和 CNS 应用程序的诚实提供商的假设下编写的。我们在下面的部分中定义了这意味着什么。

这种使用去中心化方分解去中心化问题的方法极大地简化了代码，并且能够分解代码，如包依赖关系图所示：

<img src="https://mintcdn.com/cantonfoundation/805bfL5zagaL0yiJ/overview/reference/images/daml-package-dependency.png?fit=max&auto=format&n=805bfL5zagaL0yiJ&q=85&s=f3dd07a1160b603f0771882b48e0ea5a" class="align-center" alt="Daml 包依赖关系图" width="1712" height="1133" data-path="overview/reference/images/daml-package-dependency.png" />

###

DSO 是一个跨所有 SV 节点托管的去中心化团体。它使用拜占庭容错（BFT）确认模型，其中的操作需要得到绝大多数 SV 的批准。系统最多可容忍`f`个故障或不诚实节点，其中`f = floor((n - 1) / 3)`和`n`是SV的总数。

任何治理行动所需的票数为：

```
requiredNumVotes = ceiling((numSVs + f + 1) / 2)
```

这个阈值确保了两个属性：**完整性**（不诚实的少数人无法推动某项行动）和**可用性**（最多 `f` 弃权 SV 不能阻止进展）。

## 治理角色

任何 SV 都可以通过在链上创建`VoteRequest`来提出治理行动。然后，所有其他 SV 都可以对该请求进行投票（接受或拒绝）。一旦达到投票阈值，DSO 代表就会执行操作。

需要确认的操作有两种执行路径：* **投票行动** -- 任何 SV 创建投票请求；其他 SV 以接受/拒绝投票来响应。当`requiredNumVotes`接受投票被收集时执行该操作。
* **自动确认** -- 对于日常操作操作（例如推进挖矿轮数），每个 SV 节点在满足其先决条件时会自动创建确认。一旦积累了足够的确认，执行就会继续，无需手动投票。

## 投票机制

投票请求在 DSO 账本上表示为 `VoteRequest` Daml 合约。每个请求指定建议的 `ActionRequiringConfirmation`、`voteBefore` 截止日期以及用于计划操作的可选 `targetEffectiveAt` 时间戳。

投票结果如下：

* **接受** -- 至少 `requiredNumVotes` SV 投票接受。该操作在链上执行。
* **拒绝** -- 至少 `requiredNumVotes` SV 投票拒绝。该请求已存档。
* **已过期** -- `voteBefore` 截止日期已过，但双方都没有足够的票数。

对于日期为`targetEffectiveAt`的投票请求，仅在达到阈值且已过有效时间后才会执行操作。这允许 SV 提前安排更改，例如参数更新或升级激活。

SV 操作员通过 SV Web UI 中的 **治理选项卡** 管理投票，他们可以在其中创建新的投票请求、审查待决提案、投票并跟踪结果。 UI 将投票请求分为“需要采取行动”、“进行中”、“计划”、“已执行”和“已拒绝”等类别，以便于跟踪。

## 治理行动的类型

治理操作根据表示它们的 Daml 数据类型分为三类：`ARC_DsoRules`、`ARC_AmuletRules` 和 `ARC_AnsEntryContext`。

### DSO 规则操作 (`ARC_DsoRules`)

* **添加 SV** (`SRARC_AddSv`) -- 将新的超级验证器添加到 DSO
* **Offboard SV** (`SRARC_OffboardSv`) -- 从 DSO 中删除超级验证器
* **授予特色应用权利** (`SRARC_GrantFeaturedAppRight`) -- 批准应用程序提供商获得特色应用奖励
* **撤销推荐应用程序权限** (`SRARC_RevokeFeaturedAppRight`) -- 从提供商处删除推荐应用程序状态
* **更新SV奖励权重** (`SRARC_UpdateSvRewardWeight`) -- 更改分配给SV的奖励权重
* **Set DSO config** (`SRARC_SetConfig`) -- 修改`DsoRulesConfig`，控制网络级参数

### 护身符规则动作 (`ARC_AmuletRules`)

* **设置护身符配置** (`CRARC_SetConfig`) -- 更改`AmuletConfig`，它控制 Canton Coin 经济，包括费用表、发行曲线和流量定价

### Canton名称服务行动 (`ARC_AnsEntryContext`)

* **收取初始入境付款** (`ANSRARC_CollectInitialEntryPayment`) -- 自动收取新 CNS 入境付款
* **拒绝入场付款** (`ANSRARC_RejectEntryInitialPayment`) -- 自动拒绝无效的 CNS 入场付款

### 自动操作

有些行动不需要手动投票。满足先决条件时，SV 节点会自动创建确认：

* **开始发行轮次** (`CRARC_MiningRound_StartIssuing`) -- 一旦计算出奖励摘要，将挖矿轮次转换为发行轮次
* **存档封闭挖矿轮次** (`CRARC_MiningRound_Archive`) -- 清理完全过期的挖矿轮次
* **确认SV加入** (`SRARC_ConfirmSvOnboarding`) -- 确认一方经过身份验证后可以成为SV

## 参数治理

SV 通过投票的配置更改来管理网络参数。关键可配置参数包括：* **流量定价** (`extraTrafficPrice`) -- 每 MB 同步器流量的美元成本。根据 [CIP-0042](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0042/cip-0042.md)，应对此进行校准，以便标准 Canton Coin 转账费用为 1 美元。
* **读取与写入比例因子** (`readVsWriteScalingFactor`) ​​-- 读取流量成本相对于写入流量成本的比率，反映了与排序和持久性相比，消息传递的基础设施成本较低。
* **CC-USD 汇率** -- 每个 SV 在链上发布其所需的美元对 CC 的汇率。 DSO 使用所有已发布值的**中位数**，使速率能够抵抗任何单个 SV 的操纵。
* **轮次持续时间** -- 挖矿轮次的长度（默认：10 分钟），决定了计算和发放奖励的频率。
* **SV 奖励权重** -- 每个 SV 都有一个可配置的奖励权重，决定了它们在 SV 奖励分配中的份额。更改需要治理投票，并且还应反映在 [GSF 配置存储库](https://github.com/global-synchronizer-foundation/configs) 中。

CC-USD 汇率基于中位数的方法意味着每个 SV 运营商都会发布他们的首选值，系统会自动选择中位数。这产生了可预测的总体偏好定价，约占 SV 运营商头寸的三分之二。

流量参数需要定期重新校准。实际流量成本会根据 DSO 中 SV 的数量和 Canton 协议版本等因素而变化，因此 SV 需要衡量当前成本并通过治理投票相应地调整参数。

## CIP 流程

对 Canton 网络标准和协议的正式变更要经过 Canton 改进提案 (CIP) 流程。 CIP 涵盖技术规范、治理程序和信息指南。 SV 通过上述相同的链上治理机制对 CIP 的采用进行投票。

有关 CIP 生命周期以及如何参与的完整概述，请参阅[什么是 CIP？](/zh/docs/canton/overview-reference-what-are-cips)。 CIP 存储库维护在 [github.com/global-synchronizer-foundation/cips](https://github.com/global-synchronizer-foundation/cips)。

## 全球同步器基金会

[Global Synchronizer Foundation (GSF)](https://sync.global) 是 Linux 基金会旗下的一个独立的非营利机构，旨在支持 全局同步器 的治理和发展。 GSF：

* 运营自己的SV节点并代表成员参与治理投票
* 提供超级验证者治理决策和网络运营的透明度
* 协调整个 SV 运营商团队的升级计划和维护
* 管理 Splice 代码库治理并监督特色应用程序审查

GSF 对网络没有单方面控制权。其 SV 节点与任何其他 SV 具有相同的投票权重，所有治理行动仍需要标准 BFT 投票阈值才能通过。当前的超级验证者列表由 GSF 维护。

## 链上治理架构

所有治理状态都以 Daml 合约的形式存在于链上。 `DsoRules`合约保存了DSO成员资格（`svs`映射）、DSO委托和当前配置的权威记录。 `AmuletRules`合约保存了Canton Coin的配置时间表。投票请求、确认和 SV 状态合约都是账本可见的，使得有权访问 Scan 应用程序的任何一方都可以审核治理。

去中心化的政党模型意味着DSO政党本身有`ceiling(numSVs * 2.0 / 3.0)`的确认门槛。 DSO 方签署的每笔交易都必须得到至少多个 SV 参与节点的确认，从而在独立于应用程序级投票逻辑的 Canton 协议层上执行 BFT。

## BFT 保证

链上投票和去中心化自动化的结合为网络参与者提供了三项保证，他们相信不超过 `f` SV 是不诚实的：

* **有效交易** -- 每个 DSO 确认的交易都满足 Daml 的[账本有效性模型](/zh/docs/canton/overview-learn-ledger-model)
* **及时自动化** -- 例行操作动作（回合晋级、奖励发放）立即执行
* **可预测的参数** -- 费用和配置值反映了至少三分之二的 SV 运营商的总体偏好

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
