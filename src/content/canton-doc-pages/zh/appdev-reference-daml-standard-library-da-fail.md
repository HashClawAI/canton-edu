---
title: "DA.Fail"
slug: "appdev-reference-daml-standard-library-da-fail"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-fail.md"
source_title: "DA.Fail"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-fail
---

# DA.Fail

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.Fail

> Daml 模块 DA.Fail 的参考文档。

<span id="module-da-fail-58029" />

# DA.Fail

Fail，用于 FailureStatus。

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="说明">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-internal-fail-types-failurecategory-97811" />

### `data FailureCategory`

失败类别，决定失败的状态码与日志级别。与 Canton 文档中的错误类别一一对应：
[错误类别清单](/global-synchronizer/reference/error-codes#error-categories-inventory)

若更熟悉 gRPC 错误码，可使用注释中的同义词。

构造子：

<span id="constr-da-internal-fail-types-invalidindependentofsystemstate-84432" />

* `InvalidIndependentOfSystemState`
  用于报告与账本当前状态无关的错误，因此不应重试。

对应 gRPC 状态码 `INVALID_ARGUMENT`。

详见 [错误类别清单](/global-synchronizer/reference/error-codes#error-categories-inventory)。

<span id="constr-da-internal-fail-types-invalidgivencurrentsystemstateother-6547" />

* `InvalidGivenCurrentSystemStateOther`
  用于报告由账本当前状态导致的错误；若账本状态变化，错误可能消失。客户端应在从账本读取更新状态后重试。

对应 gRPC 状态码 `FAILED_PRECONDITION`。

详见 [错误类别清单](/global-synchronizer/reference/error-codes#error-categories-inventory)。

实例：

* `instance GetField category FailureStatus FailureCategory`
* `instance SetField category FailureStatus FailureCategory`
* `instance Eq FailureCategory`
* `instance Ord FailureCategory`
* `instance Show FailureCategory`

<span id="type-da-internal-fail-types-failurestatus-69615" />

### `data FailureStatus`

构造子：

<span id="constr-da-internal-fail-types-failurestatus-61878" />

* `FailureStatus`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| errorId | Text | 错误的明确标识符。<br /><br />SHOULD 以标识应用提供方或定义该错误的 API 标准的 DNS 名为前缀。例如<br /><br />在 CN 代币标准场景下，资金不足可报告为 `splice.lfdecentralizedtrust.org/insufficient-funds`。 |
  \| category | FailureCategory | 失败类别，决定客户端应如何处理该错误。 |
  \| message | Text | 面向开发者的错误消息，应为英文。 |
  \| meta | TextMap Text | 键值形式的机器可读错误元数据。<br /><br />用于向客户端提供额外上下文。<br /><br />SHOULD 少于 512 字符，否则可能被截断。 |

实例：

* `instance GetField category FailureStatus FailureCategory`
* `instance GetField errorId FailureStatus Text`
* `instance GetField message FailureStatus Text`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance SetField category FailureStatus FailureCategory`
* `instance SetField errorId FailureStatus Text`
* `instance SetField message FailureStatus Text`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance Eq FailureStatus`
* `instance Ord FailureStatus`
* `instance Show FailureStatus`

## 类型类

<span id="class-da-internal-fail-actionfailwithstatus-58664" />

### `class Action m => ActionFailWithStatus m`

方法：

* `failWithStatus : FailureStatus -> m a`
  以 failure status 失败

实例：

* `instance ActionFailWithStatus Update`

## 函数

<span id="function-da-fail-invalidargument-67588" />

### `invalidArgument`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
invalidArgument : FailureCategory
```

`InvalidIndependentOfSystemState` 的别名。

<span id="function-da-fail-failedprecondition-95960" />

### `failedPrecondition`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
failedPrecondition : FailureCategory
```

`InvalidGivenCurrentSystemStateOther` 的别名。

<span id="function-da-internal-fail-failwithstatuspure-20043" />

### `failWithStatusPure`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
failWithStatusPure : FailureStatus -> a
```

在纯上下文中以 failure status 失败

## 孤儿类型类实例

* `instance Eq FailureStatus`

* `instance Ord FailureStatus`

* `instance Show FailureStatus`

* `instance Eq FailureCategory`

* `instance Ord FailureCategory`

* `instance Show FailureCategory`

* `instance GetField errorId FailureStatus Text`

* `instance SetField errorId FailureStatus Text`

* `instance GetField category FailureStatus FailureCategory`

* `instance SetField category FailureStatus FailureCategory`

* `instance GetField message FailureStatus Text`

* `instance SetField message FailureStatus Text`

* `instance GetField meta FailureStatus (TextMap Text)`

* `instance SetField meta FailureStatus (TextMap Text)`

* `instance ActionFail Update`

* `instance CanAbort Update`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
