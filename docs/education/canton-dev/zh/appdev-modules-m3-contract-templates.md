---
title: "合约模板"
slug: "appdev-modules-m3-contract-templates"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-contract-templates.md"
source_title: "Contract Templates"
tags:
  - appdev
  - modules
  - m3-contract-templates
---

# 合约模板

> 学习如何定义 Daml 合约模板——Canton 智能合约的核心构建块

## 简介

首先编写一个非常小的 Daml 模板，表示一种自行发行、不可转让的代币。作为最小模板，它本身并不实用——稍后你会让它更有用——但足以展示最基本概念：

* 交易
* Daml 模块与文件
* 模板
* 合约
* 签署方

<Tip>
  可运行 `dpm new intro-contracts --template daml-intro-contracts` 加载本节代码。
</Tip>

## Daml 账本基础

与多数称为「账本」的结构一样，Daml 账本就是一系列*提交*。所谓*提交*，指*参与方*成功向账本*提交*一笔*交易*后的最终结果。

*交易* 是本章将逐步细化的概念。最基本例子是*合约*的创建与归档。

合约从存在已提交的创建交易起为*活跃*，直至存在已提交的*归档*交易。

单个合约是*不可变*的：活跃合约不能被修改。你只能通过对*活跃合约集*创建新合约或归档旧合约来变更它。

Daml 规定 Daml 账本上哪些交易合法；Daml 代码中的规则统称为 *Daml 模型* 或 *合约模型*。

## Daml 模块与文件

每个 `.daml` 文件在顶部定义一个 *Daml 模块*：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Token where
```

Daml 注释以 `--` 引入：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- A Daml file defines a module.
module Token where
```

## 模板

`template` 定义可创建的合约类型及谁有权创建。*合约* 是*模板*的实例。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Token
  with
    owner : Party
  where
    signatory owner
```

以 `template` 关键字声明模板，后接名称。

Daml 对空白敏感，用缩进组织*块*。首行以下缩进的内容属于模板体。

*合约* 包含数据，称为*创建参数*或简称*参数*。`with` 块通过列出字段名与类型定义创建参数的数据类型。单冒号 `:` 表示「类型为」，可读作「模板 `Token` 带有类型为 `Party` 的字段 `owner`」。

`Token` 合约有一个类型为 `Party` 的字段 `owner`。模板 `with` 块中声明的字段在模板其余部分（`where` 块内）处于作用域。

## 签署方

`signatory` 关键字指定合约的*签署方*。这些是创建或归档合约所需*权限*的参与方——如同真实合同。每个合约至少有一个签署方。

此外，Daml 账本*保证*参与方能看到使用其权限的所有交易。即合约签署方保证能看到该合约的创建与归档。

## 下一步

在 [Choices](/appdev/modules/m3-choices) 中，你将学习如何用 choice 为合约添加行为。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
