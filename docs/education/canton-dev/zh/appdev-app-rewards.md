---
title: "应用奖励"
slug: "appdev-app-rewards"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/app-rewards.md"
source_title: "App Rewards"
tags:
  - appdev
  - app-rewards
---

# 应用奖励

> 应用如何通过 Featured 应用活动与奖励券在 Canton Network 上获得 Canton Coin 奖励

Canton Network 通过与应用活动挂钩的奖励机制激励应用提供方。在网络上产生价值的应用可获得 Canton Coin（CC）作为奖励。本页说明奖励类型、如何获得，以及如何让应用成为 Featured 应用。

## 奖励类型

这些券在每个奖励轮次中累积，并在铸币过程中转换为 CC。

## 应用如何获得奖励

应用奖励的主要机制是 **FeaturedAppActivityMarker**。当你的应用在网络上产生活动时，你的后端（或自动化）会写入 `FeaturedAppActivityMarker` 合约以记录该活动。SV 自动化检测这些标记并将其转换为 `AppRewardCoupon` 合约，随后在下一轮铸币中纳入。

流程如下：

1. 你的应用在 Global Synchronizer 上创建交易（例如用户行使 choice、创建合约）
2. 应用自动化创建引用该活动的 `FeaturedAppActivityMarker`
3. SV 自动化校验标记并创建 `AppRewardCoupon`
4. 奖励轮次结束时，该券纳入 CC 铸币计算
5. 你的应用提供方 Party 按活动比例获得 CC

`FeaturedAppActivityMarker` 是首选方式，因为它将奖励与可证实的网络使用直接关联，而不依赖人工上报或不透明指标。

## 成为 Featured 应用

[CIP-0078](https://github.com/canton-foundation/cips/blob/main/cip-0078/cip-0078.md) 之后，只有 **Featured 应用** 才有资格获得应用奖励。未 Featured 应用的活动标记不会转换为奖励券。

要让应用成为 Featured：

1. 在 Canton Network（DevNet、TestNet 或 MainNet）上部署应用
2. 通过 [申请流程](https://sync.global/) 向 Global Synchronizer Foundation 提交请求
3. 代币经济委员会评审提交，评估应用对网络的贡献
4. 批准后，经 SV 治理投票将你的应用注册为 Featured

成为 Featured 后，你的 `FeaturedAppActivityMarker` 合约才有资格转换为 `AppRewardCoupon`。

## DevNet 自 Featured

在 DevNet 上，可为测试目的将应用注册为自 Featured。这样可在 TestNet 或 MainNet 走正式 Featured 流程之前，验证奖励逻辑是否正确。

DevNet 自 Featured 不需要 GSF 批准，仅用于开发与奖励流程的集成测试。

## 铸币委托

若你的应用代表外部 Party 产生活动（例如终端用户通过你的平台交互），可委托铸币权利。铸币委托允许验证者为另一 Party 铸币奖励，适用于提交交易的验证者与应获得奖励的 Party 不是同一方的情况。

## 费用结构

Canton Network 不对 Party 之间的 CC 转账收费。网络使用的唯一成本是 **traffic**——由提交交易的验证者支付的交易费。应用奖励是独立机制，用于补偿产生网络活动的应用提供方，与 traffic 成本无关。

## 延伸阅读

* [Canton Coin 与 Traffic](/appdev/modules/m4-canton-coin) — 应用开发者视角下的 traffic 额度与 CC
* [如何让应用 Featured](/overview/understand/getting-app-featured) — Canton Network 上的推广机会
* [Canton Coin 概览](/overview/understand/canton-coin) — 代币经济、验证者奖励与治理

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
