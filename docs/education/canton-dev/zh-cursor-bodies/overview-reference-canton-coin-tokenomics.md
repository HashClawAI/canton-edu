> Canton Coin 费用、铸造轮次、活动记录与销毁-铸造均衡的技术参考

Canton Coin (CC) 是 Global Synchronizer 的原生效用代币，通过 [Splice](https://github.com/canton-network/splice) 开源基础设施实现，Daml 合约层称为「Amulet」。CC 三项功能：支付网络使用（流量）、奖励基础设施运营方与应用提供方、通过 Super Validator 参与治理网络。

CC 在网络中的角色与获取方式见 [Canton Coin and the Global Synchronizer](/overview/understand/canton-coin)。正式规范见 [Canton Coin white paper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf)。

## 费用结构

CC 有三类费用。依 [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md)，转账费与锁定费已取消，现仅**流量费**与**持有费**生效。

### 流量费

流量额度不可转让。CC 兑换为流量后仅可用于支付交易提交。验证者流量预算耗尽则交易失败。建议启用自动充值。

<Note>
  即使确认请求因 consuming 合约争用失败（例如两笔转账试图消费同一 coin 合约），流量额度仍会被消耗。
</Note>

### 持有费

Canton Network 代币经济学基于 **Activity Record**（活动记录），标识为网络提供价值的 Party 及其操作。活动记录有 **weight**（权重），表示与该记录关联的 CC 铸造份额。

创建活动记录与铸造对应 CC 是两步，在称为 **round**（轮次）的周期中执行，共五阶段。第一阶段将该轮费用写入账本（费用可从 Scan State API 获取）。第二阶段为 **activity recording**，创建的活动记录属于该轮。下一阶段计算各类型活动记录的 [CC-issuance-per-activity-weight](https://github.com/canton-network/splice/blob/332e06a7ae9e13fde5bba0bf7dcb059aa36f979e/daml/splice-amulet/daml/Splice/Issuance.daml#L67)，即可为该类型铸造的 CC 总份额。随后 **minting phase**，活动记录所有者可按铸造权重比例铸造 CC。

多轮并发，每轮处于不同阶段。每 10 分钟开启一轮（Super Validator 未来可通过治理投票调整）。详见 CC 白皮书。

外部 Party 与本地 Party 创建活动记录无差别，但铸造阶段自动化支持不同。本地 Party 入驻验证者时，验证者应用后台自动铸造全部活动记录。外部 Party 用自管密钥签署交易，验证者自动化无法直接代其铸造。外部 Party 可选：

1. 使用 minting delegation 将奖励收集委托给验证者，无需自建自动化。
2. 开发自定义自动化，每轮至少一次以全部活动记录为输入调用 `AmuletRules_Transfer`。

已批准 CIP [Weighted Validator Liveness Rewards for SV-Determined Parties](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) 描述对此的支持。

代币经济学相关重要 template：

* AmuletRules — 存储费用表；
* OpenMiningRound — 轮次开启时的价格与费用；
* IssuingMiningRound — 存储 amount-to-mint-per-activity-weight。

## 活动记录类型

网络活动核算涉及五类关键 template：

* 两类与应用相关：
  > * FeaturedAppActivityMarker
  > * AppRewardCoupon
* 三类与为应用提供的基础设施相关：
  > * ValidatorRewardCoupon
  > * ValidatorLivenessActivityRecord
  > * SvRewardCoupon

后四类为活动记录；`FeaturedAppActivityMarker` 不算活动记录。后文述及，`FeaturedAppActivityMarker` 经 Super Validator 自动化转为 `AppRewardCoupon`。特色 CC 转账与 `FeaturedAppActivityMarker` 产生相同奖励；**首选**用 `FeaturedAppActivityMarker` 生成应用活动记录。

`FeaturedAppActivityMarker`、`AppRewardCoupon`、`ValidatorRewardCoupon` 在应用交易成功时创建。一般而言，应用在其 Daml 代码直接创建 `FeaturedAppActivityMarker` 或与突出应用提供方 Party 的 Daml 模型交互时获奖励。每次调用 `AmuletRules_Transfer`（如 Splice Wallet UI 的 CC 转账）或 CC 被销毁时创建 `ValidatorRewardCoupon`。

除铸造权重外，应用奖励还取决于是否 designated 为 **featured** 或 **unfeatured**（默认）。CIP-0078 后仅 featured 应用获奖励。featured 应用获得的铸造权重总价值约 \$1 US（Super Validator 未来可调整）。

## 如何成为 featured 应用

需 **application provider's party ID** 作为应用输入。流程始于填写 [this form](https://sync.global/featured-app-request/)。请求交 tokenomics committee 审查。进展见 [webpage](https://lists.sync.global/g/tokenomics/topics)。[成功提交示例](https://lists.sync.global/g/tokenomics/topic/new_featured_app_request/112787885)。DevNet 可自 feature 应用做测试。

部分 template 的活动归因可分给多个受益 Party。例如 featured 应用奖励可在应用提供方与用户间按 `weight` 分配。通用模式：

* 提供受益人列表，各带 `weight`，总和为 `1.0`。
* 后续处理为每对受益人与 weight 创建独立合约，设置 `beneficiary` 与 `weight`。

受益人详见下文各节。

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) 取消几乎所有 CC 转账与锁定费，unfeatured 应用不再获奖励。持有费保留但行为变更：将 coin 用作转账输入时不收持有费。

持有费为每个独立 coin 合约（UTXO）每单位时间的固定费用，与金额无关，激励合并 CC 以减少网络存储，或清理粉尘 coin。持有费不在转账时收取，仅通过 `Amulet_Expire` choice 对过期 coin 合约显式收取。当累计持有费超过 coin 面值时，Super Validator 可过期该合约并从账本移除。因此 coin 合约面值恒定，不随费用递减。

因持有费按 UTXO 而非按 CC 数量，小额「粉尘」coin 相对面值更快累积费用；费用超过面值后 Super Validator 可过期合约。会计简单：coin 合约面值不变。

### 转账与锁定费（CIP-0078 之后）

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) 取消几乎所有 CC 转账与锁定费。遗留 Amulet 转账、CN Token Standard 两步转账与一步 `TransferPreapproval` 转账均不收费。例外：featured 一步转账仍为维护 `TransferPreapproval` 合约的提供方 Party 生成 `AppRewardCoupon`。

## 销毁-铸造均衡

CC 供应量因此动态而非固定。最大铸造曲线约束新币进入流通速度，流量购买等销毁事件移除 coin。

铸造奖励分给四类贡献者：

* **Super Validator** — 运营 synchronizer 节点（Sequencer、Mediator、治理基础设施）获得铸造权。
* **应用提供方** — 通过 featured 应用促成交易获奖励。
* **Validator** — 铸造权与其销毁的费用成正比，网络将其视为该节点产生活动的代理指标。
* **Liveness 激励** — 奖励验证者在线与就绪；若验证者未通过直接活动用尽铸造配额，部分作为 liveness 奖金分配。

## 铸造轮次

三个 Daml template 驱动轮次生命周期：

* **`AmuletRules`** — 费用表
* **`OpenMiningRound`** — 轮次开启时的价格与费用
* **`IssuingMiningRound`** — 计算后的 CC-issuance-per-activity-weight

### 外部 Party 铸造

本地 Party 由验证者应用后台自动铸造全部活动记录。外部 Party 用自管密钥签署，验证者无法代铸造。选项：

* **Minting delegation** — 将奖励收集委托给验证者。
* **Custom automation** — 每轮至少一次以全部活动记录为输入调用 `AmuletRules_Transfer`。

[CIP-0073 (Weighted Validator Liveness Rewards for SV-Determined Parties)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) 描述额外工作流支持。

## 活动记录

活动记录归因可在多个受益人之间分配。各受益人获 `weight`（总和 1.0），铸造时为每对受益人/weight 创建独立合约。

## Featured 与 Unfeatured 应用

应用奖励取决于 **featured** 或 **unfeatured**（默认）。CIP-0078 后仅 featured 应用获奖励。featured 应用每次合格活动获得的铸造权重总价值约 \$1 USD（Super Validator 可调整）。

`FeaturedAppActivityMarker` 是生成应用活动记录的首选机制。经 `TransferPreapproval` 的 featured 一步转账亦为提供方 Party 生成 `AppRewardCoupon`。

成为 featured 应用请通过 [GSF featured app request form](https://sync.global/featured-app-request/) 提交。tokenomics committee 审查；进展见 [tokenomics committee topics page](https://lists.sync.global/g/tokenomics/topics)。DevNet 可自 feature 做测试。

## UTXO 模型与粉尘过期

CC 持仓使用 UTXO 模型。每枚 coin 为账本上具面值的独立 `Amulet` 合约。转账消费输入 UTXO 并创建输出 UTXO，类似 Bitcoin 但具隐私——余额仅对有权 Party 可见，无公开全体持仓账本。

转账找零时为新 UTXO 创建余额，钱包可能持有许多小额 UTXO。

### 粉尘过期（Dust Expiry）

按 UTXO 的持有费形成粉尘自然清理：费用与面值无关，0.001 CC 与 1000 CC  coin 单位时间费用相同，小额 coin 更快变得不经济。累计持有费超过面值后，Super Validator 可 exercise `Amulet_Expire` 从账本移除。用户有激励合并小额 coin 以减少 UTXO 数量与持有费暴露。Splice 钱包在可能时自动合并。

## CN Token Standard (CIP-0056)

[CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 定义 Canton Network Token Standard——用于转账、锁定与元数据查询的 Daml 接口集。Splice 钱包为 CC 实现 CIP-0056，以编程方式处理 CC 的应用通过这些标准接口交互。

CIP-0056 两步转账：

1. 发送方锁定所需 CC 金额，创建 transfer offer。
2. 接收方接受 offer，解锁 CC 并完成转账。

两步流程不依赖发送方自动化，适合用自管密钥签署的外部 Party。CIP-0078 后这些操作无费用且不产生活动记录。

API 详情见 [CIP-0056 text](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 与 [token standard source code](https://github.com/canton-network/splice/tree/main/token-standard#readme)。

## 相关资源

* [Canton Coin and the Global Synchronizer](/overview/understand/canton-coin) — 概念概览与获取 CC
* [CIP-0078 (CC Fee Removal)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) — 取消转账与锁定费的提案
* [CIP-0056 (CN Token Standard)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) — 代币操作标准接口
* [CIP-0073 (Weighted Validator Liveness Rewards)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) — SV 确定 Party 的 liveness 奖励支持
* [Canton Coin white paper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf) — 完整正式规范
