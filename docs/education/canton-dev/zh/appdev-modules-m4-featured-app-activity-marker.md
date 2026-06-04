---
title: "Featured App 活动标记"
slug: "appdev-modules-m4-featured-app-activity-marker"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-featured-app-activity-marker.md"
source_title: "Featured App Activity Markers"
tags:
  - appdev
  - modules
  - m4-featured-app-activity-marker
---

# Featured App 活动标记

> 如何创建 FeaturedAppActivityMarker 合约以记录应用活动并赚取奖励

应用在 Canton Network 上运行时，具有经济意义的事件可记录为 **应用活动**。首选机制是 `FeaturedAppActivityMarker` 合约。SV（Super Validator）自动化将这些标记转换为 `AppRewardCoupon` 合约，进而转化为 Canton Coin（CC）奖励。

## 什么是 FeaturedAppActivityMarker？

`FeaturedAppActivityMarker` 记录应用中的特定活动事件，向网络表明发生了具有经济相关性的事件——例如锁定真实世界资产（RWA）、铸造代币或许可证续期。

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) 之后，仅 **featured** 应用获得奖励。未 featured 的应用仍可创建标记，但不会生成奖励券。

## 何时创建标记

除上述示例外，适合创建标记的场景还包括结算支付或交易、续期或签发许可证。不要为不产生用户-facing 经济价值的例行运维（缓存刷新、健康检查、内部记账）创建标记。

## 如何创建标记

`FeaturedAppActivityMarker` 合约规范见 [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md)。Daml 代码在执行具有经济意义动作的交易中创建标记。

标记合约包含标识应用、活动类型与事件元数据的字段。精确合约接口与必填字段见 [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md)。

*featured application activity marker* 规范见 [CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md)。摘要如下。

Featured application activity markers（FeaturedAppActivityMarker）可为增加价值但不涉及 CC 转账的交易创建（如稳定币转账或交易结算）。[CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) 规定：

> Featured application providers are expected to create featured application activity markers only for transactions that correspond to a transfer of an asset, or an equivalent transaction, which was enabled by the application provider. The detailed fair usage policy and enforcement thereof is left up to the Tokenomics Committee of the Global Synchronizer Foundation (GSF).

一般指导：为任何具有经济重要性的事件创建 `FeaturedAppActivityMarker`，例如：

* 锁定或解锁 RWA
* 转移 RWA
* 铸造或销毁代币

但不应为中间步骤或 propose 步骤创建。

`FeaturedAppActivityMarker` 会立即被 Super Validator 运行的自动化转换为 AppRewardCoupon。AppRewardCoupon 以 DSO 为 `signatory`，`provider` 字段为 observer。默认 `provider` 可在 minting 步骤铸造 CC。`featured` 字段设为 `true` 表示基于 FeaturedAppRight 合约有资格获得 featured 应用奖励。

单个交易树可含多个 `FeaturedAppActivityMarker`，从而增加总奖励，但仅允许用于组合交易（如结算交易），交易场所与各资产 registry 均可获得 featured 应用奖励。单个 Canton 交易树也可同时包含 ValidatorRewardCoupon、AppRewardCoupon 与 FeaturedAppActivityMarker（若子交易分别创建）。

非 featured 应用无法累积 `FeaturedAppActivityMarker`。

### 创建 Featured Application Activity Marker

应用创建 `FeaturedAppActivityMarker` 有两个前提。首先是成为获批的 featured 应用（见 `types_of_activity_records` 一节）。其次是更新应用代码：

> 1. 找到 FeaturedAppRight 接口定义的完全限定 package-id：`7804375fe5e4c6d5afe067bd314c42fe0b7d005a1300019c73154dd939da4dda:Splice.Api.FeaturedAppRightV1:FeaturedAppRight`（对应 `Splice.Api.FeaturedAppRightV1`）。可用 `daml damlc inspect-dar` 查找。
>
> 2. 用该 ID 查询账本，获取实现 FeaturedAppRight 接口的合约。下方 `curl` 示例演示此方法。
>
> ````bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
> curl "http://$lapiParticipant/v2/state/active-contracts" \
> "$jwtToken" "application/json" \
>    --data-raw '{
>    "filter": {
>    "filtersByParty": {
>          "'$holderPartyId'": {
>          "cumulative":
>          [
>             {
>                "identifierFilter": {
>                "InterfaceFilter": {
>                   "value": {
>                      "interfaceId": "'7804375fe5e4c6d5afe067bd314c42fe0b7d005a1300019c73154dd939da4dda:Splice.Api.FeaturedAppRightV1:FeaturedAppRight'",
>                      "includeInterfaceView": true,
>                      "includeCreatedEventBlob": false
>                   }
>                }
>                }
>             }
>          ]}
>    }
>    },
>    "verbose": false,
>    "activeAtOffset":"'$latestOffset'"
> }'
> ```text
>
> 3. 应用 Daml 代码需依赖 `splice-api-featured-app-v1.dar`，并在应被 featured 的 choice 上接受 `ContractId FeaturedAppRight` 参数，以便 choice 体调用下一步的 `FeaturedAppRight_CreateActivityMarker`。
>
> 3. 在应用 Daml 代码中，通过 `FeaturedAppRight` 接口行使 `FeaturedAppRight_CreateActivityMarker` choice，将 `templateId` 设为上述完全限定接口 ID。
>
> 4. 测试示例见 [此处 DamlScript 测试](https://github.com/canton-network/splice/blob/a32995a0df2d447b9e76d81b770a06c296295ab5/daml/splice-dso-governance-test/daml/Splice/Scripts/TestFeaturedAppActivityMarkers.daml#L4)。
> ````

考虑单笔简单 RWA 交易，为单个 `provider` 创建一条 `FeaturedAppActivityMarker` 活动记录，`beneficiary` 为 `provider`：

> 1. 在业务交易中创建 FeaturedAppActivityMarker 合约。`provider` 设为 featured 应用提供方的 party。`beneficiary` 必须设置（与 AppRewardCoupon 不同）为应有资格铸造该活动 CC 的 party。FeaturedAppActivityMarker 的 `provider` 字段通过调用接口 choice FeaturedAppRight_CreateActivityMarker 设置。
>
> 2. 不创建 `ValidatorRewardCoupon`。

可通过 `FeaturedAppRight_CreateActivityMarker` choice 接受 AppRewardBeneficiary 合约列表来共享 `FeaturedAppActivityMarker` 的活动归因，为每个 `beneficiary` 创建 FeaturedAppActivityMarker 并适当设置 `weight` 字段。

### cn-quickstart 中的标记

在 [cn-quickstart](https://github.com/digital-asset/cn-quickstart) 中，许可证续期流程在续期时创建 `FeaturedAppActivityMarker`。标记在执行业务续期的 Daml choice 内创建，属于同一交易并原子记录。

## 让应用成为 Featured

要从标记获得奖励，应用必须在网络上被 **featured**。

### DevNet 上

可在 DevNet 自行 featured 应用以作测试，验证标记创建正确且 SV 自动化将其转换为奖励券，无需正式审查流程。

### TestNet 与 MainNet 上

TestNet 与 MainNet 流程：

1. **提交应用** — 通过 GSF（Global Synchronizer Foundation）表单提供应用详情、记录的活动类型及为何代表真实经济价值。
2. **Tokenomics 委员会审查** — GSF tokenomics 委员会评估提交，判断记录的活动是否反映真实经济价值及标记创建是否恰当。
3. **批准与 featuring** — 批准后应用加入 featured 应用列表，此后标记生成奖励券。

## 奖励机制

奖励计算取决于应用创建的标记数量与类型，相对于网络上其他 featured 应用。精确公式由 GSF 定义的 tokenomics 规则管辖。

要点：

* 奖励以 CC 支付给应用提供方 party
* 更多标记（代表真实经济事件）通常意味着更多奖励
* 奖励池在所有 featured 应用间共享，份额取决于相对活动量
* 刷量（为非经济事件创建标记）可能导致失去 featured 地位

## 本地测试标记

LocalNet（通过 cn-quickstart）中，将标记转换为券的 SV 自动化是本地 Splice 基础设施的一部分。你可以：

1. 触发应用中创建标记的动作
2. 查询 PQS 中活跃的 `FeaturedAppActivityMarker` 合约以验证创建
3. 等待 SV 自动化周期，再查询 `AppRewardCoupon` 合约确认转换

此本地测试循环可在部署到 DevNet 前验证标记创建逻辑。

## 延伸阅读

* [Canton Coin 与 Traffic](/appdev/modules/m4-canton-coin) — CC 奖励与 traffic 及交易成本的关系
* [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) — FeaturedAppActivityMarker 规范
* [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) — 将奖励限制于 featured 应用的变更
* [部署进阶](/appdev/modules/m5-deployment-progression) — 从 LocalNet 到 DevNet 再到 MainNet

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
