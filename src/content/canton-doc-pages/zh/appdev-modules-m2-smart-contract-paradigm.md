---
title: "智能合约范式转变"
slug: "appdev-modules-m2-smart-contract-paradigm"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-smart-contract-paradigm.md"
source_title: "Smart Contract Paradigm Shift"
tags:
  - appdev
  - modules
  - m2-smart-contract-paradigm
---

# 智能合约范式转变

> 理解 Solidity 与 Daml 编程模型的根本差异

从 Solidity 迁到 Daml 需要显著心智转变。本节说明范式差异与适应方式。

## 编程模型对比

| 方面 | Solidity | Daml |
| ---------------- | --------------------------- | ----------------------- |
| **范式** | 命令式、面向对象 | 函数式、声明式 |
| **状态** | 可变存储 | 不可变合约 |
| **执行** | 顺序操作 | 交易树 |
| **类型** | 静态 + 动态调用 | 强类型、ADT |
| **副作用** | 不受限 | 通过 monad 控制 |

## 状态模型：可变 vs 不可变

Solidity：合约是可修改状态的持久对象。

Daml：合约是不可变事实；变更归档旧合约并创建新合约。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Token
  with
    owner : Party
    issuer : Party
    amount : Decimal
  where
    signatory issuer
    observer owner
    choice Transfer : ContractId Token
      with newOwner : Party; transferAmount : Decimal
      controller owner
      do
        create Token with owner = newOwner, issuer, amount = transferAmount
        create this with amount = amount - transferAmount
```

**心智模型**：合约是事实；exercise 归档事实并创建新事实。

## UTXO vs 账户模型

以太坊：全局账户余额 mapping，易查总余额，热门账户有争用。

Canton：扩展 UTXO——状态是合约集合，转账归档并新建，余额为所持 Token 合约之和，并行更好、数据流显式。

## 语言对比

Daml 用 ADT、`Optional` 显式空值、完整参数多态；控制流用 `forA`、`assertMsg` 等于 `Update` monad 内。

## 授权模型

Solidity：`onlyOwner` 等运行时 `require`，易遗漏、任何人可尝试调用。

Daml：`signatory`/`controller` 声明，编译器与协议强制，未授权方无法到达 Choice 体。

## 多方协调

Solidity 手动多签 mapping；Daml 原生 `signatory partyA, partyB` 与 Proposal → Accept 模式。

## 常见模式对照

| Solidity 模式 | Daml 等价 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Ownable** | Signatory |
| **Pausable** | 归档 + 重建 |
| **ERC-20** | CIP-0056 Token Standard |
| **Proxy/Upgradeable** | SCU |
| **Pull payment** | Propose/accept |
| **Factory** | Template + create |
| **Registry** | Contract keys |

## 需要调整的习惯

| Solidity 习惯 | Daml 现实 |
| -------------------------------- | ---------------------------------------------------- |
| 原地改状态 | 归档 + 新建 |
| 运行时 msg.sender | 编译期 controller |
| 公开函数人人可调 | 仅 controller 可 exercise |
| 固定合约地址 | Contract ID 每次更新都变 |
| 循环迭代 | `forA`、`mapA`、fold |
| 到处 try/catch | 用 assert；异常已弃用 |

## 下一步

<CardGroup cols={2}>
  <Card title="网络架构" icon="network-wired" href="/appdev/modules/m2-network-architecture">
    网络架构与拓扑对比。
  </Card>

  <Card title="模块 3：Daml" icon="code" href="/appdev/modules/m3-dev-environment">
    开始编写 Daml 智能合约。
  </Card>
</CardGroup>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
