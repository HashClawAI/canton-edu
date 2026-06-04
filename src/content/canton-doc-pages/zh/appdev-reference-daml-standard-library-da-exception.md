---
title: "DA.Exception"
slug: "appdev-reference-daml-standard-library-da-exception"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-exception.md"
source_title: "DA.Exception"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-exception
---

# DA.Exception

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.Exception

> Daml 模块 DA.Exception 的参考文档。

<span id="module-da-exception-55791" />

# DA.Exception

Daml 中的异常处理。

已弃用：请使用 `failWithStatus` 与 `FailureStatus`，而非 Daml Exception。

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    已弃用。
  </Card>

  <Card title="说明">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `2`
    Deprecated since: `3.4.9`
  </Card>
</CardGroup>

<Warning>
  异常已弃用，请优先使用 `failWithStatus`，并避免使用 catch。
</Warning>

<AccordionGroup>
  <Accordion title="全部弃用项 (2)">
    * 异常已弃用，请优先使用 `failWithStatus`，并避免使用 catch。
    * 使用 `-Wno-deprecated-exceptions` 可关闭该警告。
  </Accordion>
</AccordionGroup>

## 数据类型

<span id="type-da-internal-exception-exception-4133" />

### `type Exception = (HasThrow e, HasMessage e, HasToAnyException e, HasFromAnyException e)`

异常类型类。不应直接实现，请使用 `exception` 语法。

## 类型类

<span id="class-da-internal-exception-hasthrow-30284" />

### `class HasThrow e`

`Exception` 约束的一部分。

方法：

* `throwPure : e -> t`
  在纯上下文中抛出异常。

实例：

* `instance HasThrow ArithmeticError`
* `instance HasThrow AssertionFailed`
* `instance HasThrow GeneralError`
* `instance HasThrow PreconditionFailed`

<span id="class-da-internal-exception-hasmessage-3179" />

### `class HasMessage e`

`Exception` 约束的一部分。

方法：

* `message : e -> Text`
  获取异常关联的错误消息。

实例：

* `instance HasMessage AnyException`
* `instance HasMessage ArithmeticError`
* `instance HasMessage AssertionFailed`
* `instance HasMessage GeneralError`
* `instance HasMessage PreconditionFailed`

<span id="class-da-internal-exception-hastoanyexception-55973" />

### `class HasToAnyException e`

`Exception` 约束的一部分。

方法：

* `toAnyException : e -> AnyException`
  将异常类型转换为 AnyException。

实例：

* `instance HasToAnyException AnyException`
* `instance HasToAnyException ArithmeticError`
* `instance HasToAnyException AssertionFailed`
* `instance HasToAnyException GeneralError`
* `instance HasToAnyException PreconditionFailed`

<span id="class-da-internal-exception-hasfromanyexception-16788" />

### `class HasFromAnyException e`

`Exception` 约束的一部分。

方法：

* `fromAnyException : AnyException -> Optional e`
  若可能，将 AnyException 转回底层异常类型。

实例：

* `instance HasFromAnyException AnyException`
* `instance HasFromAnyException ArithmeticError`
* `instance HasFromAnyException AssertionFailed`
* `instance HasFromAnyException GeneralError`
* `instance HasFromAnyException PreconditionFailed`

<span id="class-da-internal-exception-actionthrow-37623" />

### `class Action m => ActionThrow m`

支持 `throw` 的 Action 类型。

方法：

* `throw : Exception e => e -> m t`

实例：

* `instance ActionThrow Update`

<span id="class-da-internal-exception-actioncatch-69238" />

### `class ActionThrow m => ActionCatch m`

支持 `try ... catch ...` 的 Action 类型。
已弃用：避免在 Daml 代码中使用 catch，优先在客户端处理错误，并用 `failWithStatus` 抛出。

方法：

* `_tryCatch : (() -> m t) -> (AnyException -> Optional (m t)) -> m t`
  处理异常。请使用 `try ... catch ...` 语法，而非直接调用本方法。

实例：

* `instance ActionCatch Update`

## 孤儿类型类实例

* `instance GetField message GeneralError Text`

* `instance SetField message GeneralError Text`

* `instance GetField message ArithmeticError Text`

* `instance SetField message ArithmeticError Text`

* `instance GetField message PreconditionFailed Text`

* `instance SetField message PreconditionFailed Text`

* `instance GetField message AssertionFailed Text`

* `instance SetField message AssertionFailed Text`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
