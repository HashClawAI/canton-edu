---
title: "开发基金"
slug: "global-synchronizer-splice-fundamentals-validator-development-fund"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/splice-fundamentals/validator-development-fund.md"
source_title: "Development Fund"
tags:
  - global-synchronizer
  - splice-fundamentals
  - validator-development-fund
---

# 开发基金

> 验证者运营方访问与使用 Splice 开发基金。

> 验证者运营商如何获取和使用 Splice 开发基金

## 概述

发展基金是[CIP-0082](https://github.com/canton-foundation/cips/blob/main/cip-0082/cip-0082.md)引入的协议级机制。从激活开始，每轮发行中所有未来铸币排放量的可配置百分比将分配给发展基金，如 `IssuanceConfig.optDevelopmentFundPercentage` 所定义（默认值：5%）。

对于每轮发行：

* 发展基金份额（默认值：5%）作为本轮可铸造 CC 的一部分进行计算。
* 相应金额记录为合同下无人认领的权利`Splice.Amulet.UnclaimedDevelopmentFundCoupon`。
* 剩余的铸币部分按比例减少。

随着时间的推移，可能会积累多个`Splice.Amulet.UnclaimedDevelopmentFundCoupon`合约。 SV 应用程序中的自动化功能会定期合并小型无人认领的优惠券，以限制活跃合约的数量。

当无人认领的优惠券数量至少达到`2 × unclaimedDevelopmentFundCouponsThreshold`（根据 SV 配置中的定义）时，会触发合并。当满足这个条件时：

* 选择`threshold`最小的优惠券（按金额）。
* 所选优惠券已存档。
* 为它们的金额之和创建一个新的`Splice.Amulet.UnclaimedDevelopmentFundCoupon`。

较大的优惠券有意保持不变，以减少与可能引用其合约 ID 的外部准备交易的争用。

可用的发展基金由 DSO 方跟踪。有关发展基金分配的治理决策按照 [CIP-0100](https://github.com/canton-foundation/cips/blob/main/cip-0100/cip-0100.md) 中的定义在账外做出。指定的账本方（发展基金经理）通过将部分累积权利分配给特定受益人来执行这些决定。分配会导致为受益人创建`Splice.Amulet.DevelopmentFundCoupon`合同。

一旦分配：

* 受益人（本地或外部方）可以通过钱包应用程序自动化收取分配。这行使`Splice.Amulet.DevelopmentFundCoupon`中嵌入的铸造权，并向受益人铸造相应数量的Canton币。
* 发展基金管理人可以在收取之前撤回分配。这将归档相应的`Splice.Amulet.DevelopmentFundCoupon`并创建一个新的`Splice.Amulet.UnclaimedDevelopmentFundCoupon`，将金额返还给发展基金权利。
* 如果受益人未在有效期内领取分配，则分配可能会通过 SV 应用程序自动化自动过期。到期将 `Splice.Amulet.DevelopmentFundCoupon` 存档，并创建相同金额的新 `Splice.Amulet.UnclaimedDevelopmentFundCoupon`。

发展基金经理负责根据 [CIP-0100](https://github.com/canton-foundation/cips/blob/main/cip-0100/cip-0100.md) 中定义的治理决策管理分配。

## 管理发展基金分配

发展基金分配通过钱包 UI 中的 **发展基金** 选项卡进行管理，该选项卡用于实现根据 [CIP-0100](https://github.com/canton-foundation/cips/blob/main/cip-0100/cip-0100.md) 决定的分配。

此选项卡提供当前发展基金余额的可见性，并允许发展基金经理分配和管理优惠券。它还允许受益人查看其所在方是受益人的有效和历史优惠券。

<Warning>
  **发展基金**选项卡主要针对 CF 基金会指定的现任发展基金经理。

  如果您所在的一方不是指定的发展基金经理，您将无法创建拨款。

  如果您的政党以前是发展基金经理，您可以使用此页面来管理您的有效发展基金分配并查看您过去分配的历史记录。

  如果您的一方是分配的受益人，您将能够查看这些分配的历史记录。

  否则，可以安全地忽略此页面。
</Warning>

### 发展基金总额

**发展基金总额**指标显示发展基金当前可用的总额。

该值对应于所有活跃 `Splice.Amulet.UnclaimedDevelopmentFundCoupon` 合约的总和。所有用户都可以看到此信息。

### 发展资金分配

**发展基金分配**部分允许现任发展基金经理将资金分配给受益人。

此部分仅对当前经理启用。

要创建分配，经理必须提供：

* **金额**
* **受益人**
* **到期于**
* **原因**

提交分配将为指定受益人创建`Splice.Amulet.DevelopmentFundCoupon`合同。

### 无人认领的发展基金分配

**无人认领的发展基金分配**部分列出了所有有效的 `Splice.Amulet.DevelopmentFundCoupon` 合同：

* 由现任或前任经理分配，并且
* 尚未被收集、过期、撤回或拒绝。

此列表对以下人员可见：

* 现任或前任发展基金经理（针对他们分配的优惠券），以及
* 受益人（分配给其政党的优惠券）。

只有特定息票的发展基金经理才可以通过提供撤回原因来撤回该分配。

撤回分配：

* 存档对应的`Splice.Amulet.DevelopmentFundCoupon`。
* 创建一个新的`Splice.Amulet.UnclaimedDevelopmentFundCoupon`，将金额返还给发展基金权利。

### 优惠券历史记录

**优惠券历史**部分允许现任或前任发展基金经理查看历史分配，受益人可以查看其所在方作为受益人的分配情况。

这包括由于以下原因而被存档的`Splice.Amulet.DevelopmentFundCoupon`合同：

* 托收（由受益人领取）
* 过期（SV 自动化过期）
* 撤回（由发展基金管理人撤回）
* 拒绝（受益人通过 Ledger API 拒绝）

对于每个条目，UI 都会显示导致优惠券被存档的事件。

### 拒绝分配

如果受益人希望拒绝分配，则必须通过 Ledger API 完成。

钱包 UI 不为受益人提供拒绝操作。

## 改变发展基金配置

发展基金配置在`AmuletConfig`和`IssuanceConfig`类型中定义。

两个可选字段控制发展基金的行为：

* `IssuanceConfig.optDevelopmentFundPercentage` 定义每轮发行分配给发展基金的百分比。

  如果未设置该字段（`null`），Daml 发行逻辑默认为 **5%**。

* `AmuletConfig.optDevelopmentFundManager` 指定有权分配发展基金权利的一方。

发展基金百分比或发展基金经理的变更必须通过标准治理流程进行。

具体来说，这些参数是通过**“设置Amulet规则配置”**投票来更新的。

本次投票由SV按照网络正常治理规则提交并批准。

一旦投票获得批准并且更新的配置生效：

* 更新后的发展基金百分比适用于后续发行轮次。
* 指定的发展基金经理有权分配发展基金权利。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
