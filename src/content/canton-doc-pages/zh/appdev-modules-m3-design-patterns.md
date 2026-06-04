---
title: "组合与设计模式"
slug: "appdev-modules-m3-design-patterns"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-design-patterns.md"
source_title: "Composition and Design Patterns"
tags:
  - appdev
  - modules
  - m3-design-patterns
---

# 组合与设计模式

> 组合多步交易，理解 Daml 执行模型与隐私，并应用常见多方工作流模式

# 组合 choice

现在将把目前所学整合为完整、安全的资产发行、管理、转移与交易 Daml 模型。本应用能力类似 [CN Quickstart](/sdks-tools/reference-projects/cn-quickstart)。过程中还将学习：

* Daml 项目、包与模块
* 交易组合
* 观察方与 stakeholder
* Daml 执行模型
* 隐私

本节模型不是单个 Daml 文件，而是由多个相互依赖的文件组成的 Daml 项目。

<Tip>
  可运行 `dpm new intro-compose  --template daml-intro-compose` 将本节全部代码加载到 `intro-compose` 文件夹。
</Tip>

## Daml 项目

Daml 按项目、包与模块组织。Daml 项目用单个 `daml.yaml` 指定，编译为 Daml 中间语言（或字节码等价物）Daml-LF 中的包。项目内每个 `.daml` 文件成为一个 Daml 模块，类似命名空间。项目在 `daml.yaml` 的 `source` 参数指定源根目录，包包含该源目录下所有 `*.daml` 中的模块。

可在终端用 `dpm new project-name` 创建骨架项目。最小项目仅含 `daml.yaml` 与空的源文件目录。

> 查看本章项目的 `daml.yaml`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: __VERSION__
name: __PROJECT_NAME__
source: daml
version: 1.0.0
dependencies:
  - daml-prim
  - daml-stdlib
  - daml-script
```

`name` 与 `version` 一般可自由设置以描述项目。`dependencies` 即依赖列表，应始终包含 `daml-prim` 与 `daml-stdlib`：前者含编译器与 Daml Runtime 内部，后者提供标准库。`daml-script` 含 Daml Script 的类型与函数。

在项目根目录运行 `dpm build` 编译，生成 `.daml/dist/dist/${project_name}-${project_version}.dar`。DAR 类似 Java 的 JAR，是部署到账本以加载包及其依赖的产物。`dar` 文件自包含主包的全部依赖。更多见 [构建与打包](/appdev/modules/m3-building-packaging)。

## 项目结构

本项目包含可转让、可拆分（fungible）资产的持仓模型，以及独立的交易工作流。模板分布在三个模块：`Intro.Asset`、`Intro.Asset.Role`、`Intro.Asset.Trade`。

测试位于 `Test.Intro.Asset`、`Test.Intro.Asset.Role`、`Test.Intro.Asset.Trade`。

模块名中除最后一段 `.` 分隔符外，各段对应项目源目录下的路径，最后一段为文件名。目录结构如下：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
.
├── daml
│   ├── Intro
│   │   ├── Asset
│   │   │   ├── Role.daml
│   │   │   └── Trade.daml
│   │   └── Asset.daml
│   └── Test
│       └── Intro
│           ├── Asset
│           │   ├── Role.daml
│           │   └── Trade.daml
│           └── Asset.daml
└── daml.yaml
```

每个文件有模块头，例如 `daml/Intro/Asset/Role.daml`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Intro.Asset.Role where
```

可用 `import` 导入模块。`LibraryModules` 导入全部六个模块：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Intro.Asset
```

import 须紧接模块声明之后。可在 import 后列出名称以仅导入选定符号：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import DA.List (sortOn, groupOn)
```

若模块含 Daml Script，须导入对应功能：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Daml.Script
```

## 项目概览

本项目在 [授权](/appdev/modules/m3-authorization) 中的 `Iou` 模型上做了修改与扩展：

* 资产可通过 `Merge`、`Split` choice 由 `owner` 管理持仓，具有可合并、可拆分（fungible）特性。

* 转移提案现需 `issuer` 与 `newOwner` 双方授权才能接受，从发行方角度看 `Asset` 比 `Iou` 更安全。

  在 `Iou` 模型中，转移仅由 `owner` 与 `newOwner` 授权，发行方可能对任何人负债。本项目中只有持有 `AssetHolder` 合约的参与方才能成为资产持有人，发行方可控制谁可持有其资产。

* `Trade` 模板在模型中加入两种资产的互换。

## 组合 choice 与 script

本项目展示如何将 [授权](/appdev/modules/m3-authorization) 中学到的 `Update` 与 `Script` action 付诸实践。例如 `Merge`、`Split` choice 的后果中各执行多个动作。

* `Split` 时两个 create 动作
* `Merge` 时一个 create 与一个 archive 动作

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Split
      : SplitResult
      with
        splitQuantity : Decimal
      controller owner
      do
        splitAsset <- create this with
          quantity = splitQuantity
        remainder <- create this with
          quantity = quantity - splitQuantity
        return SplitResult with
          splitAsset
          remainder

    choice Merge
      : ContractId Asset
      with
        otherCid : ContractId Asset
      controller owner
      do
        other <- fetch otherCid
        assertMsg
          "Merge failed: issuer does not match"
          (issuer == other.issuer)
        assertMsg
          "Merge failed: owner does not match"
          (owner == other.owner)
        assertMsg
          "Merge failed: symbol does not match"
          (symbol == other.symbol)
        archive otherCid
        create this with
          quantity = quantity + other.quantity
```

`Split` 中使用的 `return` 在任何 `Action` 上下文中可用。`return x` 的结果是不产生副作用、但携带值 `x` 的动作。别名 `pure` 表示纯值而非带副作用的值。当 `return` 作为 `do` 块最后一条语句时，其参数即为该 `do` 块的「返回值」。

进一步组合交易时，`Trade` 上的 `Trade_Settle` choice 组合两个 `exercise` 动作：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Trade_Settle
      : (ContractId Asset, ContractId Asset)
      with
        quoteAssetCid : ContractId Asset
        baseApprovalCid : ContractId TransferApproval
      controller quoteAsset.owner
      do
        fetchedBaseAsset <- fetch baseAssetCid
        assertMsg
          "Base asset mismatch"
          (baseAsset == fetchedBaseAsset with
            observers = baseAsset.observers)

        fetchedQuoteAsset <- fetch quoteAssetCid
        assertMsg
          "Quote asset mismatch"
          (quoteAsset == fetchedQuoteAsset with
            observers = quoteAsset.observers)

        transferredBaseCid <- exercise
          baseApprovalCid TransferApproval_Transfer with
            assetCid = baseAssetCid

        transferredQuoteCid <- exercise
          quoteApprovalCid TransferApproval_Transfer with
            assetCid = quoteAssetCid

        return (transferredBaseCid, transferredQuoteCid)
```

两层嵌套后果的交易可在 `Test.Intro.Asset.Trade` 的 `test_trade` script 中查看：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
TX 14 1970-01-01T00:00:00Z (Test.Intro.Asset.Trade:79:23)
#14:0
│   disclosed to (since): 'Alice' (14), 'Bob' (14)
└─> 'Bob' exercises Trade_Settle on #12:0 (Intro.Asset.Trade:Trade)
          with
            quoteAssetCid = #9:1; baseApprovalCid = #13:1
    children:
    #14:1
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
    └─> 'Alice' and 'USD_Bank' fetch #10:1 (Intro.Asset:Asset)

    #14:2
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
    └─> 'Bob' and 'EUR_Bank' fetch #9:1 (Intro.Asset:Asset)

    #14:3
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
    └─> 'Alice' and 'Bob' exercise TransferApproval_Transfer on #13:1 (Intro.Asset:TransferApproval)
                          with
                            assetCid = #10:1
        children:
        #14:4
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Alice' and 'USD_Bank' fetch #10:1 (Intro.Asset:Asset)

        #14:5
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Alice' and 'USD_Bank' exercise Archive on #10:1 (Intro.Asset:Asset)

        #14:6
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Bob' and 'USD_Bank' create Intro.Asset:Asset
                                 with
                                   issuer = 'USD_Bank';
                                   owner = 'Bob';
                                   symbol = "USD";
                                   quantity = 100.0000000000;
                                   observers = []

    #14:7
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
    └─> 'Alice',
        'Bob' exercises TransferApproval_Transfer on #11:1 (Intro.Asset:TransferApproval)
              with
                assetCid = #9:1
        children:
        #14:8
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Bob' and 'EUR_Bank' fetch #9:1 (Intro.Asset:Asset)

        #14:9
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Bob' and 'EUR_Bank' exercise Archive on #9:1 (Intro.Asset:Asset)

        #14:10
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Alice' and 'EUR_Bank' create Intro.Asset:Asset
                                   with
                                     issuer = 'EUR_Bank';
                                     owner = 'Alice';
                                     symbol = "EUR";
                                     quantity = 90.0000000000;
                                     observers = []
```

与 choice 类似，本项目 script 也彼此组合：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
test_issuance = do
  setupResult@(alice, bob, bank, aha, ahb) <- setupRoles

  assetCid <- submit bank do
    exerciseCmd aha Issue_Asset
      with
        symbol = "USD"
        quantity = 100.0

  Some asset <- queryContractId bank assetCid
  assert (asset == Asset with
      issuer = bank
      owner = alice
      symbol = "USD"
      quantity = 100.0
      observers = []
        )

  return (setupResult, assetCid)
```

上例中 `Test.Intro.Asset.Role` 的 `test_issuance` script 使用同模块 `setupRoles` script 的输出。

同一行展示新的模式匹配：不必写 `setupResult <- setupRoles` 再用 `_1`、`_2` 访问分量，可直接命名。等价于：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
setupResult <- setupRoles
case setupResult of
  (alice, bob, bank, aha, ahb) -> ...
```

仅写 `(alice, bob, bank, aha, ahb) <- setupRoles` 也合法，但 `test_issuance` 返回值用到 `setupResult`，故同时命名整体与分量。`@` 记号可一次为整体与分量命名。

## Daml 执行模型

Daml 执行模型较易理解，但有重要后果。可想象交易生命周期如下：

命令提交
用户通过参与方节点的 Ledger API 以托管在该节点的 `Party` 身份提交命令列表，该方称为 requester。

解释
每个命令对应一个或多个动作。此步骤在账本上下文中求值各动作对应的 `Update`，计算全部后果（含传递性后果），得到完整交易。交易与其 requester 合称 commit。

脱敏
在强隐私账本上，为所有相关方创建投影（见 [隐私模型](/overview/learn/privacy-model)），亦称 *projecting*。

交易提交
将交易/commit 提交到网络。

验证
网络验证交易/commit；具体验证者因实现而异。验证还包括调度与冲突检测，保证交易在 commit 的（偏）序中有明确位置且无双花。

承诺
按账本的 commit 或共识协议实际提交 commit。

确认
网络向所有相关参与方节点发回承诺确认。

完成
用户通过提交参与方节点的 Ledger API 收到确认。

首要后果：所有交易原子提交——要么全体参与方整体提交，要么失败。

这对上文 `Trade_Settle` choice 很重要：choice 将 `baseAsset` 与 `quoteAsset` 各向一方转移，交易原子性保证任一方不会只出不进。

第二后果：交易 requester 知晓其提交交易的全部后果——Daml 中无「意外」。但也意味着 requester 须具备解释交易的全部信息，下文亦称原则 2。

这对 `Trade` 也很重要：为使 Bob 能解释将 Alice 资金转给 Bob 的交易，Bob 须知晓 Alice 的 `Asset` 合约，以及 Alice 接受转移的方式——本例中接受转移需要 `issuer` 权限。

## 观察方

*观察方* 是 Daml 向其他参与方披露合约的机制。声明方式与 signatory 类似，但用 `observer` 关键字，见 `Asset` 模板：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Asset
  with
    issuer : Party
    owner : Party
    symbol : Text
    quantity : Decimal
    observers : [Party]
  where
    signatory issuer, owner
    ensure quantity > 0.0

    observer observers
```

`Asset` 模板还给 `owner` 设置观察方的 choice；可见 Alice 在提议交易前用其向 Bob 展示 `Asset`。可尝试删除该交易观察后果：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
usdCid <- submit alice do
    exerciseCmd usdCid SetObservers with
      newObservers = [bob]
```

观察方在 Daml 中有保证：尤其保证能看到其作为 observer 的合约上的创建与归档动作。

因观察方由合约参数计算，他们彼此知晓。因此 Alice 不在 `AssetHolder` 上加 Bob 为 observer 并在 `Trade_Settle` 中用其授权转移，而是创建一次性的 `TransferAuthorization`。若 Alice 有许多对手方，否则他们会彼此泄露。

Choice controller 不会自动成为 observer，因其仅在 choice 参数已知时才能计算。

## 隐私

Daml 隐私模型基于两条原则：

原则 1. 参与方看到与其有利害关系的动作。原则 2. 看到某动作的参与方看到其（传递）后果。

原则 2 保证各方能独立验证所见每笔交易的有效性。

参与方对动作有利害关系若：

* 是该动作的必需授权方
* 是被执行动作合约的 signatory
* 是该合约的 observer，且动作为创建或归档

对 `test_trade` 中 `exercise tradeCid Trade_Settle` 意味着什么？

Alice 是 `tradeCid` 的 signatory，Bob 是 `Trade_Settle` 动作的必需授权方，故二者均可见。按原则 2，他们看到交易内一切。

后果中除若干 `fetch` 外，有两个 `TransferApproval_Transfer` choice 的 `exercise` 动作。

两个 `TransferApproval` 合约由不同 `issuer` 签署，各自看到「自己」合约上的动作。故 EUR_Bank 看到 EUR `Asset` 的 `TransferApproval_Transfer`，USD_Bank 看到 USD `Asset` 的对应动作。

部分 Daml 账本（如 script runner 与 Sandbox）遵循「数据最小化」，仅分发上述信息。即分发给 EUR_Bank 的整体交易「投影」（`execution_model` 第 4 步）仅含 `TransferApproval_Transfer` 及其后果。

其他实现（尤其公链）隐私约束可能更弱。

### 泄露（Divulgence）

隐私模型原则 2 意味着参与方有时能看到并非 signatory 或 observer 的合约。例如 `test_trade` script 最终账本状态中，Alice 与 Bob 均看到两种资产（各自列中的 X）：

| Alice | Bob | EUR\_Bank | USD\_Bank | id     | status | issuer    | owner | symbol | quantity |
| ----- | --- | --------- | --------- | ------ | ------ | --------- | ----- | ------ | -------- |
| X     | X   | -         | X         | #15:6  | active | USD\_Bank | Bob   | USD    | 100.0    |
| X     | X   | X         | -         | #15:10 | active | EUR\_Bank | Alice | EUR    | 90.0     |

因这些合约的 `create` 动作在双方有利害关系的 `Trade_Settle` 的传递后果中。此类披露常称「divulgence」，设计隐私敏感应用时须考虑。

## 常见 Daml 设计模式

除上文组合模式外，本节介绍 Daml 中常见的多方工作流模式。以下示例均用 `Coin` 资产模型说明。

### 提议-接受（Propose-Accept）

多方就共享合约达成一致的最常见方式：一方创建提案合约，另一方接受、拒绝或任其过期。[授权模块](/appdev/modules/m3-authorization#use-propose-accept-workflow-for-one-off-authorization) 中的 `IouProposal` 也是此模式。

发行方创建 `CoinMaster`，再邀请持有人。邀请为提案合约，发行方为 signatory，持有人为 observer：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template CoinMaster
  with
    issuer: Party
  where
    signatory issuer

    nonconsuming choice Invite : ContractId CoinIssueProposal
      with owner: Party
      controller issuer
      do create CoinIssueProposal
            with coinAgreement = CoinIssueAgreement with issuer; owner
```

提案给持有人接受 choice。完整模型还可含 `Reject`、`Counter`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template CoinIssueProposal
  with
    coinAgreement: CoinIssueAgreement
  where
    signatory coinAgreement.issuer
    observer coinAgreement.owner

    choice AcceptCoinProposal
      : ContractId CoinIssueAgreement
      controller coinAgreement.owner
      do create coinAgreement
```

持有人接受后，结果合约双方均为 signatory——未经同意任何一方不会被强制进入协议：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template CoinIssueAgreement
  with
    issuer: Party
    owner: Party
  where
    signatory issuer, owner

    nonconsuming choice Issue : ContractId Coin
      with amount: Decimal
      controller issuer
      do create Coin with issuer; owner; amount; delegates = []
```

需要两方以上签名时此模式可能冗长——见下文多方协议。

### 委托（Delegation）

一方有权代表另一方 exercise choice。Principal 创建委托合约，授权 agent 代为行动，principal 不必逐笔授权。这对应银行托管证券并代客户结算等关系。

委托合约（`CoinPoA` — 授权书）以 principal 为 signatory。Attorney 控制 `TransferCoin` choice，在 principal 的 coin 上 exercise `Transfer`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template CoinPoA
  with
    attorney: Party
    principal: Party
  where
    signatory principal
    observer attorney

    choice WithdrawPoA
      : ()
      controller principal
      do return ()

    -- Attorney has the delegated right to Transfer
    nonconsuming choice TransferCoin
      : ContractId TransferProposal
      with
        coinId: ContractId Coin
        newOwner: Party
      controller attorney
      do
        exercise coinId Transfer with newOwner
```

Attorney exercise 委托 choice 前须披露 coin，可通过 `Coin` 上 `Disclose` choice 将其加为 observer：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Disclose : ContractId Coin
      with p : Party
      controller owner
      do create this with delegates = p :: delegates
```

### 授权（Authorization）

在采取某些动作前验证控制方具备权限。授权合约作为证明——choice 体检查其存在与有效性。

例如发行方只希望经认可的参与方接收 coin 转移。发行方为获准 owner 创建授权 token：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template CoinOwnerAuthorization
  with
    owner: Party
    issuer: Party
  where
    signatory issuer
    observer owner

    choice WithdrawAuthorization
      : ()
      controller issuer
      do return ()
```

`TransferProposal` 的 `AcceptTransfer` 要求新 owner 提供授权 token，`assert` 验证 token 的 issuer 与 new owner：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice AcceptTransfer
      : ContractId Coin
      with token: ContractId CoinOwnerAuthorization
      controller newOwner
      do
        t <- fetch token
        assert (coin.issuer == t.issuer)
        assert (newOwner == t.owner)
        create coin with owner = newOwner
```

若发行方在转移被接受前撤回授权，转移失败。

### 锁定（Locking）

合约处于锁定状态时阻止 exercise choice。适用于清算期间冻结资产等场景。

一种做法是**通过状态变更锁定**——合约带 `locker` 字段。`owner == locker` 时未锁定可转移；否则由第三方 locker 控制解锁：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template LockableCoin
  with
    owner: Party
    issuer: Party
    amount: Decimal
    locker: Party
  where
    signatory issuer, owner
    observer locker

    ensure amount > 0.0

    -- Transfer can only happen if not locked
    choice Transfer : ContractId TransferProposal
      with newOwner: Party
      controller owner
      do
        assert (locker == owner)
        create TransferProposal with coin=this; newOwner

    -- Lock by bringing a locker on board
    choice Lock : ContractId LockableCoin
      with newLocker: Party
      controller owner
      do
        assert (newLocker /= owner)
        create this with locker = newLocker

    -- Unlock restores owner control
    choice Unlock
      : ContractId LockableCoin
      controller locker
      do
        assert (locker /= owner)
        create this with locker = owner
```

另有**通过归档锁定**（归档原合约并创建带 `Unlock`、`Clawback` 的 `LockedCoin` 包装）与**通过托管锁定**（将托管交给可信第三方由其控制解锁）。

### 多方协议（Multiple party agreement）

收集两方以上签名。`Pending` 合约包装最终 `Agreement` 并跟踪已签方。各方通过 `Sign` choice 签署，全部签署后任一方可 `Finalize` 创建协议。

最终协议合约有多名 signatory：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Agreement
  with
    signatories: [Party]
  where
    signatory signatories
    ensure unique signatories
```

`Pending` 合约逐个收集签名。所有必需 signatory 可观察，故各方可知何时轮到自己：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toSign : Pending -> [Party]
toSign Pending { alreadySigned, finalContract } =
  filter (`notElem` alreadySigned) finalContract.signatories

template Pending
  with
    finalContract: Agreement
    alreadySigned: [Party]
  where
    signatory alreadySigned
    observer finalContract.signatories
    ensure unique alreadySigned

    choice Sign : ContractId Pending with
        signer : Party
      controller signer
        do
          assert (signer `elem` toSign this)
          create this with alreadySigned = signer :: alreadySigned

    choice Finalize : ContractId Agreement with
        signer : Party
      controller signer
        do
          assert (sort alreadySigned == sort finalContract.signatories)
          create finalContract
```

一方通过创建仅将自己列为已签的 `Pending` 启动工作流。其他人任意顺序签署，完成后任一 signatory 可 finalize：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Any party can kick off by creating a Pending listing only themselves
pending <- person1 `submit` do
  createCmd Pending with finalContract; alreadySigned = [person1]

-- Each party signs
pending <- person2 `submit` do exerciseCmd pending Sign with signer = person2
pending <- person3 `submit` do exerciseCmd pending Sign with signer = person3
pending <- person4 `submit` do exerciseCmd pending Sign with signer = person4

-- Once all have signed, any signatory can finalize
person1 `submit` do exerciseCmd pending Finalize with signer = person1
```

# 组合 choice

现在将把目前所学整合为完整、安全的资产发行、管理、转移与交易 Daml 模型。本应用能力类似 [CN Quickstart](/sdks-tools/reference-projects/cn-quickstart)。过程中还将学习：

* Daml 项目、包与模块
* 交易组合
* 观察方与 stakeholder
* Daml 执行模型
* 隐私

本节模型不是单个 Daml 文件，而是由多个相互依赖的文件组成的 Daml 项目。

<Tip>
  可运行 `dpm new intro-compose  --template daml-intro-compose` 将本节全部代码加载到 `intro-compose` 文件夹。
</Tip>

## Daml 项目

Daml 按项目、包与模块组织。Daml 项目用单个 `daml.yaml` 指定，编译为 Daml-LF 包。项目内每个 `.daml` 文件成为一个模块。源根由 `daml.yaml` 的 `source` 指定。

可在终端用 `dpm new project-name` 创建骨架。最小项目仅含 `daml.yaml` 与空源目录。

> 查看本章项目的 `daml.yaml`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml.yaml.template
-- [Include actual code example here]
```

`name` 与 `version` 可自由设置。`dependencies` 须包含 `daml-prim`、`daml-stdlib` 与 `daml-script`。

在项目根运行 `dpm build` 生成 DAR。更多见 [构建与打包](/appdev/modules/m3-building-packaging)。

## 项目结构

本项目含可转让 fungible 资产持仓模型与独立交易工作流。模板在 `Intro.Asset`、`Intro.Asset.Role`、`Intro.Asset.Trade`；测试在对应 `Test.Intro.*` 模块。目录结构：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
.
├── daml
│   ├── Intro
│   │   ├── Asset
│   │   │   ├── Role.daml
│   │   │   └── Trade.daml
│   │   └── Asset.daml
│   └── Test
│       └── Intro
│           ├── Asset
│           │   ├── Role.daml
│           │   └── Trade.daml
│           └── Asset.daml
└── daml.yaml
```

每个文件含模块头，例如 `daml/Intro/Asset/Role.daml`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Intro/Asset/Role.daml
-- [Include actual code example here]
```

可用 `import` 导入模块：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Intro/Asset/Role.daml
-- [Include actual code example here]
```

import 须紧接模块声明。可 selective import：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import DA.List (sortOn, groupOn)
```

含 Daml Script 时须：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Daml.Script
```

## 项目概览

本项目扩展 [授权](/appdev/modules/m3-authorization) 中的 `Iou` 模型：`Merge`/`Split`、双方授权的转移、以及 `Trade` 互换两种资产。

## 组合 choice 与 script

展示 [授权](/appdev/modules/m3-authorization) 中 `Update` 与 `Script` 的用法。`Merge`、`Split` 后果含多个动作。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Intro/Asset.daml
-- [Include actual code example here]
```

`return`/`pure` 在 `Action` 中用法同上。

`Trade_Settle` 组合两个 `exercise`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Intro/Asset/Trade.daml
-- [Include actual code example here]
```

交易树见 `Test.Intro.Asset.Trade` 的 `test_trade`：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
TX 14 1970-01-01T00:00:00Z (Test.Intro.Asset.Trade:79:23)
#14:0
│   disclosed to (since): 'Alice' (14), 'Bob' (14)
└─> 'Bob' exercises Trade_Settle on #12:0 (Intro.Asset.Trade:Trade)
          with
            quoteAssetCid = #9:1; baseApprovalCid = #13:1
    children:
    #14:1
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
    └─> 'Alice' and 'USD_Bank' fetch #10:1 (Intro.Asset:Asset)

    #14:2
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
    └─> 'Bob' and 'EUR_Bank' fetch #9:1 (Intro.Asset:Asset)

    #14:3
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
    └─> 'Alice' and 'Bob' exercise TransferApproval_Transfer on #13:1 (Intro.Asset:TransferApproval)
                          with
                            assetCid = #10:1
        children:
        #14:4
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Alice' and 'USD_Bank' fetch #10:1 (Intro.Asset:Asset)

        #14:5
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Alice' and 'USD_Bank' exercise Archive on #10:1 (Intro.Asset:Asset)

        #14:6
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'USD_Bank' (14)
        └─> 'Bob' and 'USD_Bank' create Intro.Asset:Asset
                                 with
                                   issuer = 'USD_Bank';
                                   owner = 'Bob';
                                   symbol = "USD";
                                   quantity = 100.0000000000;
                                   observers = []

    #14:7
    │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
    └─> 'Alice',
        'Bob' exercises TransferApproval_Transfer on #11:1 (Intro.Asset:TransferApproval)
              with
                assetCid = #9:1
        children:
        #14:8
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Bob' and 'EUR_Bank' fetch #9:1 (Intro.Asset:Asset)

        #14:9
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Bob' and 'EUR_Bank' exercise Archive on #9:1 (Intro.Asset:Asset)

        #14:10
        │   disclosed to (since): 'Alice' (14), 'Bob' (14), 'EUR_Bank' (14)
        └─> 'Alice' and 'EUR_Bank' create Intro.Asset:Asset
                                   with
                                     issuer = 'EUR_Bank';
                                     owner = 'Alice';
                                     symbol = "EUR";
                                     quantity = 90.0000000000;
                                     observers = []
```

script 亦彼此组合：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Test/Intro/Asset/Role.daml
-- [Include actual code example here]
```

`test_issuance` 使用 `setupRoles` 输出；`@` 记号同时命名元组整体与分量。

## Daml 执行模型

交易生命周期：命令提交 → 解释（计算 `Update` 后果）→ 脱敏（强隐私账本）→ 提交 → 验证 → 承诺 → 确认 → 完成。原子性与 requester 知晓全部后果（原则 2）对 `Trade_Settle`、`Trade` 中 Bob 须知晓 Alice 资产与转移授权尤为关键。

## 观察方

用 `observer` 披露合约；`SetObservers` 示例同上。观察方保证见创建/归档；不宜用 `AssetHolder` observer 授权 `Trade_Settle`，宜用一次性 `TransferAuthorization`。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Intro/Asset.daml
-- [Include actual code example here]
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-compose/daml/Test/Intro/Asset/Trade.daml
-- [Include actual code example here]
```

## 隐私

原则 1：见有利害关系的动作。原则 2：见动作则见其传递后果。对 `Trade_Settle`，Alice/Bob 见全交易；各银行只见各自 `TransferApproval_Transfer`。Sandbox 等遵循数据最小化投影。

### 泄露（Divulgence）

原则 2 下参与方有时可见非 signatory/observer 合约。`test_trade` 最终状态示例：

<figure>
  <img src="https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/appdev/modules/images/compose/divulgence.png?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=a920641ce4bd1220282f433482af589b" alt="images/compose/divulgence.png" width="480" height="163" data-path="appdev/modules/images/compose/divulgence.png" />
</figure>

因 `create` 在双方有利害关系的 `Trade_Settle` 传递后果中。设计隐私敏感模型时须考虑 divulgence。

## 下一步

在异常处理章节将学习如何在 Daml 中处理模型错误。


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
