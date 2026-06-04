---
title: "合约键"
slug: "appdev-modules-m3-contract-keys"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-contract-keys.md"
source_title: "Contract Keys"
tags:
  - appdev
  - modules
  - m3-contract-keys
---

# 合约键

> 使用合约键获得稳定合约引用并按键查找

# 参考：合约键

合约键是模板的可选扩展，可用模板参数指定识别合约的方式——类似数据库主键。

合约键不变，即使合约 ID 因更新而改变，仍可通过键引用当前活跃合约。合约经归档与创建更新时，可用键轻松引用当前活跃合约。

<Note>
  在 Canton 3.x 中，同一模板的多个活跃合约可共享同一键。

  一般用法是在 Daml 引擎外保证键唯一——例如在 Daml 业务逻辑或后端客户端（唯一账号、发票号等）。因此主键 API（`lookupByKey`、`fetchByKey`、`exerciseByKey`）针对「至多一个合约对应一个键」的常见情况做了优化。
</Note>

下面为银行账户设置合约键作为账户 ID 的示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AccountKey = (Party, Text)

template Account with
    bank : Party
    number : Text
    owner : Party
    balance : Decimal
    observers : [Party]
  where
    signatory [bank, owner]
    observer observers

    key (bank, number) : AccountKey
    maintainer key._1
```

## 什么可作为合约键

键可以是任意可序列化表达式，但**不得**包含合约 ID。不过**必须**包含你希望作为 `maintainer` 的每个参与方（见下文 [指定 Maintainer](#specify-maintainers)）。

键宜使用 `Text`、`Int` 等简单类型，而非列表或更复杂类型。

## 指定 Maintainer

若模板指定合约键，还须指定 `maintainer`（可多个），方式类似 signatory 或 observer。Maintainer「拥有」键，如同 signatory「拥有」合约。与 signatory 防止双花或虚假合约数据类似，键的 maintainer 保证键查找一致。键是合约的一部分，maintainer **必须**是合约 signatory，但由 `key` 而非模板参数计算。上例中 `bank` 即为键的 maintainer。

多个模板可能共用同一键类型，部分键相关函数须用 `@ContractType` 注解，如下文示例。

编写 Daml 模型时 maintainer 影响授权——与 signatory、observer 类似。无需额外「维护」键；交易中涉及键的 maintainer 的验证节点会确认对该键的合约按一致顺序检索。

## 合约查找

合约键的主要用途是在 Daml 中提供稳定、可能有业务含义的标识以 fetch 合约。主要按键查找函数为默认提供的 `fetchByKey`、`lookupByKey`、`exerciseByKey`。

多个合约共享同一键时，这些函数按下列查找顺序返回**第一个**合约：

1. 当前交易内创建的合约，从最近开始。
2. 显式披露的合约，按命令中提供的顺序。
3. 参与方已知的合约，任意顺序。（当前实现常按新近顺序返回，但不保证，不应依赖。）

若预期每键多合约，可使用 `DA.ContractKeys` 的 `lookupNByKey`、`lookupAllByKey`（见下文 [多合约键查找](#multi-contract-key-lookups)）。

因披露合约优先于已知合约，可在提交命令时用披露控制特定检索顺序。

### fetchByKey

`(fetchedContractId, fetchedContract) <- fetchByKey @ContractType contractKey`

用 `fetchByKey` 获取指定键的第一个合约（按上序）的 ID 与数据，是 `fetch` 的替代，行为在多数情况下相同。

返回 ID 与合约对象（含全部数据）的元组。

与 `fetch` 类似，`fetchByKey` 须至少一名 stakeholder 授权。

若无给定键的合约对提交方可见，`fetchByKey` 失败并以 [`CONTRACT_KEY_NOT_FOUND`](/appdev/reference/error-codes#contracts-and-transactions) 中止交易。

### lookupByKey

`optionalContractId <- lookupByKey @ContractType contractKey`

用 `lookupByKey` 检查是否存在指定键的合约。存在则返回 `Some contractId`（第一个匹配键的合约 ID，按上序）；否则 `None`。

`lookupByKey` 需要键的**全部** maintainer 授权，以便托管 maintainer 的确认参与方验证交易内对该键的检索顺序一致。

更精确地说：

* 存在给定键的合约且提交方为该合约 stakeholder，并有全部 maintainer 授权时，`lookupByKey` 返回 `Some contractId`。
* 不存在给定键的合约（或对提交方不可见），并有全部 maintainer 授权时，返回 `None`。
* 缺少任一 maintainer 授权时，`lookupByKey` 中止交易。

## exerciseByKey

`exerciseByKey @ContractType contractKey`

对给定键的第一个合约（按上序）exercise choice。与 `exercise` 一样，运行 `exerciseByKey` 需要合约可见性及 choice controller 的授权。

## 多合约键查找

若预期多个合约可共享同一键，`DA.ContractKeys` 提供：

* **`lookupNByKey @ContractType n key`** — 查找至多 `n` 个同键合约，按上文查找顺序返回。
* **`lookupAllByKey @ContractType key`** — 查找同键全部合约。

默认不导入，使用须在模块中添加 `import DA.ContractKeys`。

<Note>
  性能针对每键零或一个合约的常见情况优化。多合约函数（`lookupNByKey`、`lookupAllByKey`）在许多合约共享键时可能较慢。
</Note>

## Daml Script 函数

除上述在交易内运行的 Daml 语言原语外，还有在交易外按键查询的 Daml Script 函数：

* **`queryByKey @ContractType party key`** — 按键查找合约，返回 ID 与数据。作为顶层 `Script` 动作运行。
* **`queryNByKey @ContractType party n key`** — 按键查找至多 `n` 个合约，返回 ID 与数据。作为顶层 `Script` 动作运行。
* **`exerciseByKeyCmd @ContractType key choiceArg`** — 对给定键的第一个合约 exercise choice。为 `Commands` 动作，须在 `submit` 块内使用，可与其他命令组合。

## 示例

演示按键查找与 exercise 的示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

module Test where

import Daml.Script
import DA.Assert
import DA.ContractKeys
import DA.Optional

template WithKey
  with
    p : Party
    payload : Text
  where
    signatory p
    key p : Party
    maintainer key
    nonconsuming choice GetText : Text
      with
        party : Party
      controller party
      do pure payload

template Helper
  with
    p : Party
  where
    signatory p

    choice PerformLookupByKey : Optional (ContractId WithKey)
      controller p
      do lookupByKey @WithKey p
    
    choice PerformFetchByKey : (ContractId WithKey, WithKey)
      controller p
      do fetchByKey @WithKey p
    
    choice PerformExerciseByKey : Text
      controller p
      do exerciseByKey @WithKey p GetText with party = p
    
    choice PerformLookupNByKey : [(ContractId WithKey, WithKey)]
      with n : Int
      controller p
      do lookupNByKey @WithKey n p
    
    choice CreateThenPerformLookupNByKey : [(ContractId WithKey, WithKey)]
      with 
        payload : Text
        n : Int
      controller p
      do create (WithKey p payload)
         lookupNByKey @WithKey n p

-- Demonstrates basic key operations: lookupByKey, fetchByKey, exerciseByKey
useKeyOperations : Script ()
useKeyOperations = script do
  alice <- allocateParty "alice"

  -- Create a contract with a key
  cid <- alice `submit` createCmd (WithKey alice "hello")

  -- lookupByKey returns Some if a contract with the key exists
  mcid <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformLookupByKey
  assert (isSome mcid)

  -- fetchByKey returns the contract ID and data
  (kcid, contract) <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformFetchByKey
  kcid === cid
  contract.payload === "hello"

  -- exerciseByKey exercises a choice on the contract with the key
  result <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformExerciseByKey
  result === "hello"

-- Demonstrates non-unique keys: multiple contracts can share a key.
-- lookupByKey and fetchByKey return the first contract per lookup order;
-- lookupNByKey (from DA.ContractKeys) returns up to n contracts.
multipleContractsPerKey : Script ()
multipleContractsPerKey = script do
  alice <- allocateParty "alice"

  -- Create multiple contracts with the same key
  cid1 <- alice `submit` createCmd (WithKey alice "first")
  cid2 <- alice `submit` createCmd (WithKey alice "second")
  cid3 <- alice `submit` createCmd (WithKey alice "third")

  let contracts = [(cid1, "first"), (cid2, "second"), (cid3, "third")]

  -- fetchByKey returns one of the created contracts
  (kcid, contract) <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformFetchByKey
  assert ((kcid, contract.payload) `elem` contracts)

  -- lookupNByKey returns up to n contracts (any 2 of 3, in any order)
  result <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformLookupNByKey with n = 2
  let results = [(cid, c.payload) | (cid, c) <- result]
  length results === 2
  let [r1, r2] = results
  assert (r1 `elem` contracts)
  assert (r2 `elem` contracts)
  r1 =/= r2

  -- lookupNByKey returns:
  --   - local contracts in recency order
  --   - then disclosures in command-specified order
  --   - then contracts known to the participant in any order
  Some disclosure <- alice `queryDisclosure` cid1
  result <- submit (actAs alice <> disclose disclosure) do
    createAndExerciseCmd (Helper alice) CreateThenPerformLookupNByKey with
      payload = "fourth"
      n = 3
  let results = [(cid, c.payload) | (cid, c) <- result]
  length results === 3
  let [r1, r2, r3] = results
  r1._2 === "fourth"
  r2 === (cid1, "first")
  r3._1 =/= cid1
  r3._2 =/= "fourth"
  assert (r3 `elem` contracts)

-- Demonstrates exerciseByKeyCmd in a submit block
exerciseByKeyCmdExample : Script ()
exerciseByKeyCmdExample = script do
  alice <- allocateParty "alice"

  alice `submit` createCmd (WithKey alice "payload")

  -- exerciseByKeyCmd is a Commands action used inside submit
  result <- alice `submit` do
    exerciseByKeyCmd @WithKey alice GetText with party = alice
  result === "payload"
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
