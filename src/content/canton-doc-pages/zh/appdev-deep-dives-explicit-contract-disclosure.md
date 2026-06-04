---
title: "显式合约披露"
slug: "appdev-deep-dives-explicit-contract-disclosure"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/explicit-contract-disclosure.md"
source_title: "Explicit Contract Disclosure"
tags:
  - appdev
  - deep-dives
  - explicit-contract-disclosure
---

# 显式合约披露

> 向非利益相关方披露合约，使其可作为输入使用而无需加入为利益相关方。

在 Daml 中须用模板中的利益相关方标注指定谁可查看数据；要变更可见性通常需用计算不同利益相关方 Party 的模板重新创建合约。

显式合约披露允许通过链下数据分发将合约读权限委托给非利益相关方，从而在账本上高效、可扩展地共享数据。

<Note>
  显式披露默认启用。要关闭请配置 `participants.participant.ledger-api.enable-explicit-disclosure = false`。
</Note>

以下用例说明如何受益：

* 为股票交易提供价格数据证明：不必订阅每分钟数千条价格更新，可通过传统 Web 2.0 API 提供价格，仅在用时写回账本，仍获相同校验与安全，传输量可大幅降低。
* 在账本上运行开放市场：不必让所有买卖双方通过 observer 机制显式可见，可通过 Web 2.0 API 提供行情，在交易时点将可用买卖盘写回交易，获得与链上共享相同的活跃性与正确性保证。

## 合约读权限委托

合约读权限委托允许某 Party 在命令提交期间获得对其既非利益相关方亦非先前期 informee 的合约的读权限。

示例：简化双方交易。**Seller** 持有由 **StockExchange** 发行的 `Stock`，发行方还以 `PriceQuotation` 公开发布市价。**Seller** 创建可被愿按市价支付 `IOU` 的任何人 exercise 的 `Offer`。

**Buyer** 持有 10 单位 `IOU`，欲购入 **Seller** 的股票。

建模模板如下（节选）：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module StockExchange where

import Daml.Script
import DA.Assert
import DA.Action

template IOU
  with
    issuer: Party
    owner: Party
    value: Int
  where
    signatory issuer
    observer owner

    choice IOU_Transfer: ()
      with
        target: Party
        amount: Int
      controller owner
      do
        -- Check that the transferred amount is not higher than the current IOU value
        assert (value >= amount)
        create this with issuer = issuer, owner = target, value = amount
        -- No need to create a new IOU for owner if the full value is transferred
        if value == amount then pure ()
        else void $ create this with issuer = issuer, owner = owner, value = value - amount
        pure ()

template Stock
  with
    issuer: Party
    owner: Party
    stockName: Text
  where
    signatory issuer
    observer owner

    choice Stock_Transfer: ()
      with
        newOwner: Party
      controller owner
      do
        create this with owner = newOwner
        pure ()

-- Expresses the current market value of a stock issued by the issuer.
-- Not modelled in this example: the issuer ensures that only one `PriceQuotation`
-- is active at a time for a specific `stockName`.
template PriceQuotation
  with
    issuer: Party
    stockName: Text
    value: Int
  where
    signatory issuer

    -- Helper choice to allow the controller to fetch this contract without being a stakeholder.
    -- By fetching this contract, the controller (i.e. `fetcher) proves
    -- that this contract is active and represents the current market value for this stock.
    nonconsuming choice PriceQuotation_Fetch: PriceQuotation
      with fetcher: Party
      controller fetcher
      do pure this

template Offer
  with
    seller: Party
    quotationProducer: Party
    offeredAssetCid: ContractId Stock
  where
    signatory seller

    choice Offer_Accept: ()
      with
        priceQuotationCid: ContractId PriceQuotation
        buyer: Party
        buyerIou: ContractId IOU
      controller buyer
      do
        priceQuotation <- fetch priceQuotationCid
        asset <- fetch offeredAssetCid
        assert (priceQuotation.issuer == quotationProducer)
        assert (priceQuotation.stockName == asset.stockName)
        -- priceQuotation models the setup of the trade between the parties.
        pure ()
```

在链上结算交易意味着 **Buyer** 对 `offerCid` exercise `Offer_Accept`。但 **Buyer** 既非该合约利益相关方亦非先前期 informee，如何 exercise？对 `stockCid` 与 `priceQuotationCid` 的可见性同理。

若 **Buyer** 直接提交如下命令，将因对相关合约缺少可见性而失败：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- 若未附带披露合约，Buyer 将因缺少可见性而失败
submit buyer do
  exerciseCmd offerCid Offer_Accept with ...
```

**StockExchange**、**Seller** 等利益相关方可通过链下（HTTPS、SFTP、邮件等）将合约详情分享给希望成交的 Party。**Buyer** 可在 exercise **Seller** `offerCid` 上 `Offer_Accept` 的命令提交中附带披露合约，从而绕过对这些合约的可见性限制。

<Note>
  Ledger API 使用命令提交附带的披露合约在解释阶段解析合约与 key 的活跃性查找。使用披露合约可绕过提交方对该合约的可见性限制，但 Daml 模型的授权限制仍适用：提交的命令须充分授权，执行方须有权执行该动作。
</Note>

## 利益相关方如何向提交方披露合约？

披露合约详情可由利益相关方从合约关联的 `CreatedEvent` 经 Ledger API 状态与更新查询获取。

利益相关方随后通过链下常规方式将详情分享给提交方。`DisclosedContract` 可由原合约 `CreatedEvent` 中同名字段构造。

<Note>
  `CreatedEvent` 中的 `created_event_blob`（用于构造 `DisclosedContract`）**仅**在按需请求 `GetUpdates`、`GetUpdateTrees`、`GetActiveContracts` 流时填充。详见 configuring event format。
</Note>

## 将披露合约附到命令提交

披露合约可作为 `Command` 的 `disclosed_contracts` 一部分附加，须从原 `CreatedEvent` 填充（见 DisclosedContract）：

* **template_id** — 合约模板 id
* **contract_id** — 合约 id
* **created_event_blob** — 合约的不透明 blob 编码

<Note>
  仅 Canton 2.8 及之后创建的合约可作为披露合约共享；更早版本 `CreatedEvent` 无所需 `created_event_blob`。
</Note>

## 用显式披露完成股票交易

上例中 **Buyer** 对 `stockCid`、`priceQuotationCid`、`offerCid` 不可见，须在 exercise `Offer_Accept` 的提交中作为披露合约提供。利益相关方须从账本取出并交给 **Buyer**。

**Buyer** 再将披露合约载荷附到接受报价的命令提交。

后两步可用支持显式披露的 Daml Script 函数 `queryDisclosure` 与 `submitWithDisclosures`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
disclosedStock <- fromSome <$> queryDisclosure stockExchange stockCid
disclosedOffer <- fromSome <$> queryDisclosure seller offerCid
disclosedPriceQuotation <- fromSome <$> queryDisclosure stockExchange priceQuotationCid

_ <- submitWithDisclosures buyer [disclosedStock, disclosedOffer, disclosedPriceQuotation] do
  exerciseCmd offerCid Offer_Accept with priceQuotationCid = priceQuotationCid, buyer = buyer, buyerIou = buyerIouCid
```

<Note>
  Java 客户端示例见 [Java Bindings StockExchange 示例项目](https://github.com/digital-asset/ex-java-bindings/blob/f474ae83976b0ad197e2fabfce9842fb9b3de907/StockExchange/README.rst)。
</Note>

## 防护措施

若恶意 **Buyer** 篡改从 **StockExchange** 收到的 `disclosedPriceQuotation`（调低价格）再作为披露合约提交呢？

### 合约认证

显式披露引入 Daml 合约认证：合约参数、template-id、签字方、key 等纳入 contract-id 的哈希，任何篡改会导致与提交 id 不一致，诚实 participant 会发现不一致。

诚实 **Buyer** participant 会拒绝并返回 `DISCLOSED_CONTRACT_AUTHENTICATION_FAILED`；若 participant 亦恶意提交畸形载荷，其他 participant 会拒绝确认请求。

### 业务逻辑防护

良好实践是工作流应有业务前置条件防滥用。`Offer_Accept` 的 controller（`buyer`）由参数提供，任何 Party 可在提交时提供 `disclosedOffer`，故 choice 体内应有 Daml assert，例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
        assert (priceQuotation.issuer == quotationProducer)
        assert (priceQuotation.stockName == asset.stockName)
```

使用披露合约建模时，此类防护保证：

* 披露合约使用者：内容经预期条件校验。
* 披露合约所有者：合约在预期协议范围内被使用。

本例中 `Offer_Accept` 的 assert 确保报价来自 **Seller** 信任的 **Issuer**，且与 **Seller** 拟出售的股票一致。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
