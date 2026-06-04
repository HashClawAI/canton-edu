---
title: "全局同步器代币经济学"
slug: "overview-reference-tokenomics-of-gs"
locale: "zh"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/tokenomics-of-gs.md"
source_title: "Tokenomics of the Global Synchronizer"
tags:
  - overview
  - reference
  - tokenomics-of-gs
---

# 全局同步器代币经济学

> Global Synchronizer 代币经济学（Canton Coin / Traffic）参考。

> 支撑全球同步器的经济模型：流量费、奖励分配、发行、CC-USD 兑换率

Canton Coin（CC）是全球同步器的经济引擎。验证者、超级验证者和应用程序提供商通过为网络贡献基础设施和活动来赚取 CC。用户花费 CC（通过燃烧它）来购买同步器流量。由此产生的销毁薄荷均衡将代币的价值与实际网络效用联系起来。

## 烧薄荷平衡

Canton Coin应用采用销毁薄荷币均衡机制，旨在围绕其为网络用户提供的内在价值稳定Canton Coin的兑换率：

* **费用燃烧** -- 用户在购买同步器流量时需要支付费用（以美元计价，通过燃烧Canton Coin支付）。烧毁的硬币将永久退出流通。
* **铸造奖励** - 验证者、超级验证者和应用程序提供商铸造新的 CC，以换取他们对网络的贡献（基础设施运营、应用程序服务、使用和活跃度）。
* **动态平衡** - 从长远来看，销毁的总 CC（反映实际网络效用）大致平衡铸造的 CC（受预定的最大铸造曲线影响）。当使用量较高时，会燃烧更多代币，这往往会提高代币的转化率；当使用量较低时，供应量会增加，直到恢复平衡。

## 流量经济学

每条提交到全局同步器的消息都会消耗流量。发送验证器被收费；收件人则不然。

### 基本费率分配（免费套餐）

每个验证者都会收到免费的、可再生的流量限额，该限额由 `AmuletRules` 合约上的两个参数定义：

* `burstAmount`——验证器在一个突发窗口内可以使用且不产生费用的最大字节数。
* `burstWindow` -- 突发量重新生成的时间窗口。经过一整段时间的不活动后，自由平衡将完全恢复。

基本速率流量始终首先被消耗。只有当它耗尽时，额外的（付费）流量才会被消耗。

### 额外流量（由 Burning CC 购买）

验证者通过以当前的美元到 CC 的汇率（美元/MB 价格）销毁 CC 来增加其流量信用余额。当需要时，验证者的运营者（或第三方服务提供商）会销毁 CC以换取流量积分。销毁的 CC 会创建一个`ValidatorRewardCoupon`，记录销毁的 CC 数量，其中`user` 是托管购买方的验证人运营商。不创建`AppRewardCoupon`用于购买流量。

可以使用自动充值自动化，因此验证器不会意外耗尽流量。 `minTopupAmount` 参数可确保每次购买足够大，以分摊超级验证者的处理成本。

流量统计是按验证器进行的——同一验证器上托管的所有各方共享一个流量平衡。当验证者托管外部各方时，它会代表他们购买流量。 Scan API 提供了流量定价参数，验证者可以使用这些参数来估算外部各方提交的交易的成本。

### 成本因素

对于给定消息，从验证者余额中提取的实际流量取决于：

* **有效负载大小** -- 排序消息的字节大小。
* **收件人数量** -- 每个收件人都会增加由`readVsWriteScalingFactor`（以基点指定）控制的递送附加费。例如，按 4 倍计算，有 10 个收件人的 1 MB 消息的成本为 `1,000,000 * (1 + 10 * 0.004) = 1,040,000` 字节。
* **额外流量价格** -- `extraTrafficPrice`，以美元/MB 为单位，按现行兑换率以 CC 收费。

所有这些参数都存在于`AmuletRules`合约中，可以通过Scan API进行查询。

## 奖励分配

网络活动通过**活动记录**进行跟踪，每个活动记录都有一个权重，决定了该方在给定轮次中所占的 CC 铸造份额。五个关键合同模板驱动会计：* **`SvRewardCoupon`** -- 每轮每个超级验证者一个。 SV 铸币权由代币经济委员会通过 [CIP 流程](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0000/cip-0000.md) 授予，以换取运营 SV 基础设施或贡献关键资源。
* **`ValidatorRewardCoupon`** -- 每当 CC 被烧毁（流量购买）或 `AmuletRules_Transfer` 执行时创建。优惠券的权重反映了验证者燃烧的 CC 数量。
* **`ValidatorLivenessActivityRecord`** -- 每轮每个实时验证者一个。奖励验证者验证和确认交易，并提供初始资金用于在入职后购买额外流量。
* **`AppRewardCoupon`** -- 当特色应用程序的交易成功或当 SV 自动化转换 `FeaturedAppActivityMarker` 时创建。只有特色应用程序才会获得奖励（根据 [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md)）。
* **`FeaturedAppActivityMarker`** -- 在业务交易中创建，用于具有经济意义的事件（资产转移、代币铸造/销毁）。 SV 自动化将这些转换为 `AppRewardCoupon` 合约。

## 发行曲线和铸币时间表

`AmuletRules`合约上的`IssuanceConfig`定义了可以铸造的最大CC。其关键字段是：

* `amuletToIssuePerYear`——年度新CC发行上限。每轮发行量的计算方法是将该数字除以每年的轮数（默认情况下，轮次每 10 分钟开始一次，因此每年大约 52,560 轮）。
* `validatorRewardPercentage`——分配给验证者活动奖励的每轮发行的比例（按比例销毁的优惠券和活跃水龙头）。
* `appRewardPercentage`——分配给申请奖励的分数。
* 验证者和应用程序部分后的剩余部分将用于超级验证者奖励，按每个 SV 的权重按比例分配。

在每个批次中，每张优惠券的发行量都有上限（`validatorRewardCap`、`featuredAppRewardCap`、`unfeaturedAppRewardCap`、`validatorFaucetCap`）。如果某个批次中的优惠券总需求低于上限，则盈余流向下一个批次——例如，无人认领的验证者活动奖励将流向验证者活跃水龙头，而无人认领的非特色应用程序奖励将流向特色应用程序奖励。所有级别之外无人认领的奖励将转为 SV 奖励。

根据 [CIP-0082](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0082/cip-0082.md)，从每轮发行的发展基金中预留 `developmentFundPercentage`（默认 5%），然后将剩余部分分配到上述部分。

## 费用表和回合快照

费用参数存储在 **`AmuletRules`** 合约中，DSO 通过账本投票对其进行管理。当新一轮挖矿开始时，当前费用值和兑换率将被快照到 **`OpenMiningRound`** 合约中，以便该轮中的所有交易都使用一致的定价。随着该轮各阶段的进展，**`IssuingMiningRound`** 合约会记录计算出的每种奖励类型的每个活动权重的铸币金额。

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) 消除了几乎所有 CC 传输和锁定费用。持有费仍然存在——每单位时间每个单独的代币合约（UTXO）的固定费用，与代币数量无关。持有费激励合并小币以减少账本存储。仅通过`Amulet_Expire`对过期的代币合约收取费用，而不是在转账过程中收取费用。

## CC-USD 兑换率

每个超级验证者都会发布他们认为合适的 CC 转化率。每轮挖矿使用的费率是所有已发布的 SV 费率的**中位数**。这种基于中值的方法可以防止任何单个SV单方面改变价格。

生成的`amuletPrice`（每CC美元）记录在每个`OpenMiningRound`合约上，可以通过Scan API或Scan UI进行查询。所有以美元计价的费用（流量费用、奖励上限）在应用时均按此汇率转换为 CC。

## 验证者如何赚钱

验证者通过每轮运行的两种机制获得 CC：* **活跃度奖励**——每个活跃验证者都会创建一个`ValidatorLivenessActivityRecord`，赚取验证者水龙头部分的份额。每个验证者的水龙头上限默认为每轮 2.85 美元等值。活跃度奖励为新验证者提供初始 CC 来资助流量购买。
* **活动奖励** -- 当验证者的用户燃烧 CC（流量购买或转移）时，由此产生的 `ValidatorRewardCoupon` 使验证者有权根据燃烧的数量按比例铸造 CC。推动更多网络使用的验证者赚得更多。

对于托管外部方的验证器（使用自己的密钥而不是通过验证器签名的各方），可以通过验证器的**铸币委托**或通过每轮调用`AmuletRules_Transfer`的自定义自动化来处理铸币。 [CIP-0073](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) 描述了 SV 确定方的加权验证者活跃度奖励。

## 进一步阅读

* [Canton Coin白皮书](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20 payment%20application.pdf) -- 销毁铸币机制的完整技术规范
* [Canton Network白皮书](https://www.digitalasset.com/hubfs/Canton/Canton%20Network%20-%20White%20Paper.pdf) -- 更广泛的网络架构和设计
* [CIP 存储库](https://github.com/global-synchronizer-foundation/cips) -- 治理提案，包括费用和奖励变更

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
