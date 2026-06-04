---
title: "在 Daml 中组合多方工作流"
slug: "appdev-deep-dives-composition-multi-party"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/composition-multi-party.md"
source_title: "Composing Multi-Party Workflows in Daml"
tags:
  - appdev
  - deep-dives
  - composition-multi-party
---

# 在 Daml 中组合多方工作流

> 高级 Daml 模式：提议-接受、委托、授权链与原子多方组合。

真实世界的 Daml 应用涉及角色、权限与信任关系各不相同的多个参与方。本深度文章涵盖使复杂多方工作流得以运行的 Daml 设计模式——从简单的双方协议到跨多个组织的多步授权链。

## 提议-接受模式

提议-接受的规范讲解见 [模块 2：多方工作流](/zh/docs/canton/appdev-modules-m2-multi-party-workflows#the-propose-accept-pattern)。本文侧重在该基础上的其他组合模式。

## 委托

委托允许一方在限定范围内授予另一方代表其行事的权限。与提议-接受（创建共享协议）不同，委托建立的是单向信任关系。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template OperatorLicense
  with
    owner : Party
    operator : Party
    allowedOperations : [Text]
  where
    signatory owner
    observer operator

    choice Operate : ContractId OperationResult
      with
        operation : Text
      controller operator
      do assertMsg "Operation not allowed"
           (operation `elem` allowedOperations)
         create OperationResult with
           performer = operator
           onBehalfOf = owner
           operation
```

所有者将特定操作授予运营方。运营方可行使 `Operate` choice，但仅限允许的操作。所有者可通过归档 `OperatorLicense` 撤销委托。

## 多步工作流

许多业务流程需要不同参与方按序执行动作。将其建模为合约链，每一步的输出成为下一步的输入：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template TradeRequest
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer
    observer seller

    choice ConfirmTrade : ContractId TradeSettlement
      controller seller
      do create TradeSettlement with
           buyer
           seller
           asset
           price

template TradeSettlement
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer, seller

    choice Settle : ()
      controller seller
      do pure ()
```

工作流每一步对应独立模板，使状态可见、可审计——可查询账本以查看任意交易处于哪一步。

## 原子组合

Daml 交易是原子的：交易中所有创建与归档要么全部成功，要么全部失败。利用该性质实现必须同时发生的复杂操作：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice SwapAssets : (ContractId Asset, ContractId Asset)
  controller partyA
  do -- Both transfers happen atomically
     newAssetForB <- exercise assetFromA Transfer with newOwner = partyB
     newAssetForA <- exercise assetFromB Transfer with newOwner = partyA
     pure (newAssetForA, newAssetForB)
```

若任一转移失败（controller 错误、合约已归档、断言失败），则两者都不会发生。这是 DvP（券款对付）等结算模式的基础。

## 通过接口授权

接口定义模板可实现的抽象能力，用于构建可组合的授权模式：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface Transferable where
  viewtype TransferView
  getOwner : Party
  transfer : Party -> Update (ContractId Transferable)

  choice TransferTo : ContractId Transferable
    with newOwner : Party
    controller getOwner this
    do transfer this newOwner
```

任何实现 `Transferable` 的模板都获得 `TransferTo` choice。后端可针对接口编写通用转移逻辑，而无需知道具体模板类型。

<Note>
  将接口定义放在仅含接口、不含模板的独立包中。接口结构（方法与 view 类型）部署后不可修改；若需变更，应在新包中引入新版本接口。
</Note>

## 多方可见性模式

Canton 隐私模型下，各方仅能看到自己作为利益相关方（签字方或观察方）的合约。若工作流需要更广可见性但不授予操作权，可使用观察方模式：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuditableTransaction
  with
    executor : Party
    counterparty : Party
    auditor : Party
    details : Text
  where
    signatory executor, counterparty
    observer auditor  -- auditor can see but not act
```

监管或合规场景下，第三方需可见交易但非参与方时，将其加为 observer。其可通过 Ledger API 读取合约数据，但不能对其行使 choice。

## 设计考量

组合多方工作流时：

* 尽量保持签字方集合最小——每增加一名签字方都会增加协调开销
* 只读访问用 observer，而非将各方都设为签字方
* 设计模板使各方 choice 在声明中一目了然
* 避免过深的交易树（大量嵌套 exercise），以免增大交易体积与延迟
* 评估某步是否必须上链，或可链下完成

## 下一步

* [去中心化](/zh/docs/canton/appdev-deep-dives-decentralization) — 各层去中心化策略
* [多方托管](/zh/docs/canton/appdev-deep-dives-multi-hosting) — 跨验证者分布 Party 以提高韧性


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
