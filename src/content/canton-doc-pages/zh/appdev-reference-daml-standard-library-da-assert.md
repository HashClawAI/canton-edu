---
title: "DA.Assert"
slug: "appdev-reference-daml-standard-library-da-assert"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-assert.md"
source_title: "DA.Assert"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-assert
---

# DA.Assert

> Daml 标准库模块 DA.Assert 参考文档。

<span id="module-da-assert-92761" />

# DA.断言

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Stable.
  </Card>

  <Card title="Notices">
    状态：`active`
    引入于：`3.4.9`
    删除于：`-`
    警告：`0`
    弃用：`0`
    已弃用自：`-`
  </Card>
</CardGroup>

## 函数

<span id="function-da-assert-asserteq-7135" />

### `assertEq`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertEq : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

检查两个值是否相等。如果它们不相等，
失败并显示一条消息。

<span id="function-da-assert-eqeqeq-18699" />

### `===`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=== : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

`assertEq` 的中缀版本。

<span id="function-da-assert-assertnoteq-28771" />

### `assertNotEq`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertNotEq : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

检查两个值是否不相等。如果它们相等的话
失败并显示一条消息。

<span id="function-da-assert-eqslasheq-37517" />

### `=/=`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=/= : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

`assertNotEq` 的中缀版本。

<span id="function-da-assert-assertaftermsg-14090" />

### `assertAfterMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertAfterMsg : (CanAssert m, HasTime m) => Text -> Time -> m ()
```

检查给定时间是否是将来的时间。如果不是，
通过消息中止。

<span id="function-da-assert-assertbeforemsg-56514" />

### `assertBeforeMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertBeforeMsg : (CanAssert m, HasTime m) => Text -> Time -> m ()
```

检查给定时间是否是过去的时间。如果不是，
通过消息中止。

<span id="function-da-assert-assertwithindeadline-85580" />

### `assertWithinDeadline`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertWithinDeadline : Text -> Time -> Update ()
```

检查交易的账本时间是否严格在给定的截止日期之前。
如果不是，则通过消息中止。

<span id="function-da-assert-assertdeadlineexceeded-21600" />

### `assertDeadlineExceeded`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertDeadlineExceeded : Text -> Time -> Update ()
```

检查交易的分类时间是否等于或晚于给定的截止日期。
如果不是，则通过消息中止。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
