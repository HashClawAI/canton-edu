---
title: "应用开发者隐私模型"
slug: "appdev-deep-dives-privacy-model"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/privacy-model.md"
source_title: "Privacy Model for App Developers"
tags:
  - appdev
  - deep-dives
  - privacy-model
---

# 应用开发者隐私模型

> Canton 的标志性架构能力是子交易级隐私：单笔原子交易中，各方仅看到与自己相关的部分。本文说明其原理及在应用中的隐私友好模式。

## 交易树分解

当你提交涉及多方的交易时，Canton 不会把完整交易发给每个验证者，而是将交易树分解为**视图（views）**，每个利益相关方一组。

每个视图只包含该组有利益关系的动作（创建、执行、获取）。视图加密后，仅托管对应 Party 的验证者可解密。

Bob 不会知道 Charlie 的手续费，Charlie 也不会知道 Bob 的资产；Alice 作为提交者与签字方，能看到自己动作及其后果的完整范围。

## 利益相关方共识与隐私

验证者只确认自己能解密的视图。托管 Alice 的验证者确认 Alice 的视图；托管 Bob 的确认 Bob 的。同步器汇总确认并决定交易结果。

各方可见范围：

* **验证者** 仅看到其托管 Party 的视图；未参与交易的验证者收不到任何相关信息。
* **同步器** 看到加密载荷、路由元数据（发给哪些验证者）与确认结果；无法读取交易内容、合约数据、视图内 Party 关系或金额条款。
* **非利益相关方** 对交易载荷与元数据一无所知，甚至不知道交易发生过。

## 隐私保证

协议层保证：

* 交易内容仅对利益相关方可见（签字方、观察方、相关动作的控制方）
* 每个验证者只存其托管 Party 的数据——没有全局状态复制
* 同步器无法读取任何交易载荷
* 无权查看某视图的 Party 对该视图一无所知（包括涉及哪些 Party）

你的验证者节点是少数能看到你全部 Party 数据的实体，选择验证者应像选择托管方或云厂商一样谨慎。

## 隐私模式

### 双边协议

合约有两个签字方且无观察方时，仅这两方可见，同验证者上的其他 Party 也看不到。

```haskell
template NDA
  with
    partyA : Party
    partyB : Party
    terms : Text
  where
    signatory partyA, partyB
    -- 无 observer：最大隐私
```

适用于无需第三方可见的保密双方合约。

### 观察方披露

将额外 Party 声明为 `observer` 可授予读权限。观察方可见合约，但不能执行 Choice（除非另设为 controller）。

```haskell
template RegulatedLoan
  with
    lender : Party
    borrower : Party
    regulator : Party
    principal : Decimal
  where
    signatory lender, borrower
    observer regulator
```

监管方可见贷款及生命周期事件但不能修改。适用于合规/审计需要第三方可见的场景。

### 泄露（Divulgence）

当合约在另一方的交易中被 fetch 或 exercise 时，该方自动获得对该合约的可见性，称为 divulgence。

```haskell
choice SettleTrade : ()
  controller buyer
  do
    asset <- fetch sellerAssetId
    archive sellerAssetId
    create Asset with owner = buyer, issuer = asset.issuer, value = asset.value
```

Divulgence 由交易结构自动产生。谨慎设计 fetch，因为每次 fetch 都可能扩大可见范围。

### 显式合约披露

Canton 还支持显式披露：一方在常规利益相关方模型之外把合约引用分享给另一方，接收方可在自己的交易中使用该合约，无需改 observer 列表。

## 隐私与可审计性

隐私不等于无法审计：

* **PQS** 用 PostgreSQL 同步你验证者上的账本状态，可 SQL 查询自己的交易历史与合约状态；可见范围与 Party 权限一致。
* **Scan** 是 Global Synchronizer 的公开服务，提供轮次、CC 铸造与聚合统计，不暴露私有合约数据。
* **审计方作为 observer** 是常见 Daml 模式：把审计 Party 加为 observer，其可见生命周期但不能擅自操作。

原则：各方只能审计自己有权看到的内容，不能更多。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
