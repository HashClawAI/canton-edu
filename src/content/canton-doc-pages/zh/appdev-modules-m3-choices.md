---
title: "Choice"
slug: "appdev-modules-m3-choices"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-choices.md"
source_title: "Choices"
tags:
  - appdev
  - modules
  - m3-choices
---

# Choice

> 学习如何使用 choice 为 Daml 合约添加行为——转换合约状态的方法

## 简介

上一节你已通过归档并重新创建合约来变更数据。若希望允许其他参与方做特定修改，或提供便捷的数据变换方式呢？

本节将学习如何用 *choice* 定义简单数据变换，以及如何将 *exercise* 这些 choice 的权利委托给其他参与方。

<Tip>
  可运行 `dpm new intro-choices --template daml-intro-choices` 加载本节代码。
</Tip>

## Choice 即方法

若把模板比作类、合约比作对象，方法在哪里？

例如 `Contact` 合约：联系人所有方希望能改电话号码。与其像 [合约模板](/appdev/modules/m3-contract-templates) 中那样手动查找合约、归档旧合约再创建新合约，可在 `Contact` 上提供便捷方法：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Contact
  with
    owner : Party
    party : Party
    address : Text
    telephone : Text
  where
    signatory owner
    observer party

    choice UpdateTelephone
      : ContractId Contact
      with
        newTelephone : Text
      controller owner
      do
        create this with
          telephone = newTelephone
```

上例定义了名为 `UpdateTelephone` 的 *choice*。Choice 属于合约模板，是有权限的函数，结果为 `Update`。通过 choice 可传递权限，构建复杂交易。

拆解上述片段：

* 首行 `choice UpdateTelephone` 表示 choice 定义，`UpdateTelephone` 为名称，并开启该 choice 的定义块。

* `: ContractId Contact` 为 choice 的返回类型。

  本 choice 会归档当前 `Contact` 并创建新合约，返回新合约引用，即 `ContractId Contact`。

* 随后的 `with` 块是记录。与模板类似，背后会声明新记录类型：`data UpdateTelephone = UpdateTelephone with`。

* `controller owner` 表示该 choice 由 `owner` *控制*，即只有 `owner` 可 *exercise*。

* `do` 开始定义 exercise 时执行的动作。此处创建新 `Contact`。

* 新 `Contact` 用 `this with` 创建。`this` 是模板 `where` 块中的特殊值，为当前合约参数。

未显式说明要归档当前 `Contact`，因为 choice 默认是 *consuming*（消耗型）：在上述 choice 被 exercise 时，该合约会被归档。

如 `data` 中所述，choice 内用 `create` 而非 `createCmd`。`createCmd` 在客户端构建提交到账本的命令列表；`create` 构建由账本直接执行的更灵活的 `Update`。`create` 返回 `Update (ContractId Contact)`，而非 `ContractId Contact`。因 `do` 块返回其中最后一条语句的值，整个 `do` 返回 `Update`，但 choice 声明的返回类型仅为 `ContractId Contact`，这是可读性便利：choice *总是* 返回 `Update`，类型声明中省略 `Update`。

在 script 中 exercise 新 choice：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice_test = do
  owner <- allocateParty "Alice"
  party <- allocateParty "Bob"

  contactCid <- submit owner do
     createCmd Contact with
      owner
      party
      address = "1 Bobstreet"
      telephone = "012 345 6789"

  -- Bob can't change his own telephone number as Alice controls
  -- that choice.
  submitMustFail party do
    exerciseCmd contactCid UpdateTelephone with
      newTelephone = "098 7654 321"

  newContactCid <- submit owner do
    exerciseCmd contactCid UpdateTelephone with
      newTelephone = "098 7654 321"
```

用 `exercise` exercise choice，接受 `ContractId a` 与类型 `c` 的值，其中 `c` 是模板 `a` 上的 choice。因 `c` 只是记录，也可用熟悉的 `with` 语法填写 choice 参数。

`exerciseCmd` 返回 `Commands r`，`r` 为 choice 上声明的返回类型，从而可将新 `ContractId Contact` 存入 `newContactCid`。与 `createCmd`/`create` 类似，还有 `exerciseCmd` 与 `exercise`：带 `cmd` 后缀的在客户端构建命令列表；无后缀的在 choice 内由服务端直接执行。

还有 `createAndExerciseCmd` 与 `createAndExercise`（上一节已见），可用给定参数创建合约并立即 exercise 其上 choice。对 consuming choice，合约会在同一交易内被创建并归档。

## Choice 即委托

此前合约多只涉及一方。`party` 虽作为 `Party` 字段存储，暗示其为账本参与者，但无法看到合约或以任何方式修改。被存 `Contact` 的一方理应能更新自己的地址与电话，即 `Contact` 的 `owner` 应能将某类数据变换权 *委托* 给 `party`。

下面用 `UpdateAddress` choice 及 script 扩展演示：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice UpdateAddress
      : ContractId Contact
      with
        newAddress : Text
      controller party
      do
        create this with
          address = newAddress
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
newContactCid <- submit party do
    exerciseCmd newContactCid UpdateAddress with
      newAddress = "1-10 Bobstreet"

  Some newContact <- queryContractId owner newContactCid

  assert (newContact.address == "1-10 Bobstreet")
```

在 IDE 中打开 script 视图可见 Bob 能看到 `Contact`，因模板将 `party` 指定为 `observer`，此处 Bob 即 `party`。更多 *observer* 内容后述；简言之，他们能看到合约的一切变更。

## Choice 与账本模型

在 [合约模板](/appdev/modules/m3-contract-templates#daml-ledger-basics) 中你已了解 Daml 账本的高层结构。结合 choice 与 `exercise`，你具备理解账本与交易结构的下一要素。

*交易* 是 *动作* 列表，动作有三类：`create`、`exercise` 与 `fetch`。

* `create` 用给定参数创建新合约并设为 *active*。
* `fetch` 检查合约存在且为 active。
* `exercise` 在合约上 exercise choice，产生称为 *后果* 的交易（子动作列表）。Exercise 分 `consuming` 与 `nonconsuming`，默认 `consuming`，将合约从 *active* 变为 *archived*。

每个动作可可视化为树：动作为根，子节点为其后果；每个后果可有进一步后果。`fetch`、`create` 无后果，恒为叶节点。可在上述 script 的交易视图中看到动作与后果：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Transactions:
  TX 0 1970-01-01T00:00:00Z (Contact:46:17)
  #0:0
  │   consumed by: #2:0
  │   referenced by #2:0
  │   disclosed to (since): 'Alice' (0), 'Bob' (0)
  └─> 'Alice' creates Contact:Contact
              with
                owner = 'Alice'; party = 'Bob'; address = "1 Bobstreet"; telephone = "012 345 6789"

  TX 1 1970-01-01T00:00:00Z
    mustFailAt actAs: {'Bob'} readAs: {} (Contact:55:3)

  TX 2 1970-01-01T00:00:00Z (Contact:59:20)
  #2:0
  │   disclosed to (since): 'Alice' (2), 'Bob' (2)
  └─> 'Alice' exercises UpdateTelephone on #0:0 (Contact:Contact)
              with
                newTelephone = "098 7654 321"
      children:
      #2:1
      │   consumed by: #3:0
      │   referenced by #3:0
      │   disclosed to (since): 'Alice' (2), 'Bob' (2)
      └─> 'Alice' creates Contact:Contact
                  with
                    owner = 'Alice'; party = 'Bob'; address = "1 Bobstreet"; telephone = "098 7654 321"

  TX 3 1970-01-01T00:00:00Z (Contact:69:20)
  #3:0
  │   disclosed to (since): 'Alice' (3), 'Bob' (3)
  └─> 'Bob' exercises UpdateAddress on #2:1 (Contact:Contact)
            with
              newAddress = "1-10 Bobstreet"
      children:
      #3:1
      │   disclosed to (since): 'Alice' (3), 'Bob' (3)
      └─> 'Alice' creates Contact:Contact
                  with
                    owner = 'Alice';
                    party = 'Bob';
                    address = "1-10 Bobstreet";
                    telephone = "098 7654 321"

Active contracts:  #3:1

Return value: {}
```

四个 commit 对应 script 中四次 `submit`。每个 commit 内，动作 ID 形如 `#commit_number:action_number`。合约 ID 即其 `create` 动作的 ID。

故 commit `#2`、`#3` 含 ID 为 `#2:0`、`#3:0` 的 `exercise` 动作。更新后 `Contact` 的 `create` 动作 `#2:1`、`#3:1` 缩进在 `children:` 下，树结构清晰。

### Archive choice

没有单独的 archive 动作，因 `archive cid` 只是 `exercise cid Archive` 的简写；`Archive` 是每个模板隐式添加的 choice，controller 为签署方。

## 简单现金模型

借助 choice，可构建第一个有趣模型：现金 IOU（我欠你）发行。此处模型比 [语言基础](/appdev/modules/m3-language-fundamentals) 更简单，不关心实物现金位置，只关心负债：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Cash = Cash with
  currency : Text
  amount : Decimal
    deriving (Eq, Show)

template SimpleIou
  with
    issuer : Party
    owner : Party
    cash : Cash
  where
    signatory issuer
    observer owner

    choice Transfer
      : ContractId SimpleIou
      with
        newOwner : Party
      controller owner
      do
        create this with owner = newOwner
```

只要各方信任 Dora，上述模型可行。Dora 可随时通过归档撤销 `SimpleIou`；但所有交易溯源在账本上，持有人可 *证明* Dora 不诚信地取消了债务。

## 下一步

你现已能在账本上存储与变换数据，甚至通过 choice 授予其他参与方特定写权限。

在 [授权模型](/appdev/modules/m3-authorization) 中，将进一步了解谁可创建、exercise 与归档合约的授权规则。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
