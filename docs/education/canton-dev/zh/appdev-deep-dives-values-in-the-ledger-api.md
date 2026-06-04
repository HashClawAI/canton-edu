---
title: "Ledger API 中的值"
slug: "appdev-deep-dives-values-in-the-ledger-api"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/values-in-the-ledger-api.md"
source_title: "Values in the Ledger API"
tags:
  - appdev
  - deep-dives
  - values-in-the-ledger-api
---

# Ledger API 中的值

> 经 Ledger API 交换的值的校验、规范化与动态包解析规则

命令与查询对摄入的值采用宽松校验；返回的值须规范化。

### 命令中的值校验

*目标模板*指命令经动态包解析后 `template_id` 所标识的模板或接口。命令中的值（如 `create_arguments`）若须按类型 `T` 通过类型检查，则称其*期望类型*为 `T`（子值同理）。

记录值中，若自某字段起至末尾均为 `None`，则该字段为*尾部 None*。

提交命令时规则放宽：

> * `record_id`、`variant_id`、`enum_id` 若存在，仅校验模块名与类型名，**忽略** package ID。
> * 提供全部字段名时，可省略任意 `None` 字段。
> * 未提供全部字段名时，须按类型定义顺序提供字段，可省略尾部 `None`。

**示例 1**

包 `example1-1.0.0` 与 `other-1.0.0` 均在 `Main` 定义模板 `T`（字段不同）。Ledger API 仍接受针对 `example1-1.0.0:Main.T` 的 Create，即使 `create_arguments` 错误标注为 `other-1.0.0:Main.T`，因模块名与类型名与期望类型一致：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Main where

template T
  with
    p : Party
  where
    signatory p
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd))
```

**示例 2**

模板含前导与尾部 `Optional` 时，仅按名提供 `p` 可成功；无 `p` 标签失败；按序提供除尾部 optional 外字段（可无标签）可成功。

### Ledger API 响应中的值规范化

值处于**规范形**当且仅当自身及子值均无尾部 None。自 Daml 3.3.0 起，非 verbose 响应会规范化（含子值）。查询时尾部 optional（如 `j`、`rk`）可省略；非尾部的 `None` 字段（如 `i`、`ri`）仍会返回。


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
