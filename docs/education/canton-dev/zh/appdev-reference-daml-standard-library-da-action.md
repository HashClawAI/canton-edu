---
title: "DA.Action"
slug: "appdev-reference-daml-standard-library-da-action"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action.md"
source_title: "DA.Action"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action
---

# DA.Action

> Daml 标准库模块 DA.Action 参考文档。

<span id="module-da-action-7169" />

# DA.Action

Action

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Stable.
  </Card>

  <Card title="Notices">
    状态：`active`
    引入于：`3.4.9`
    删除于：`-`
    Warnings: `0`
    弃用：`0`
    已弃用自：`-`
  </Card>
</CardGroup>

## 函数

<span id="function-da-action-when-35467" />

### `when`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
when : Applicative f => Bool -> f () -> f ()
```

`Action` 表达式的条件执行。例如，

```
  when final (archive contractId)
```

如果布尔值`final`为，则将归档合约`contractId`
；否则无操作。

该函数具有短路语义，即，当两个参数都是
存在且第一个参数的计算结果为 `False`，第二个参数
根本不会求值。

<span id="function-da-action-unless-8539" />

### `unless`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unless : Applicative f => Bool -> f () -> f ()
```

与`when`相反。

该函数具有短路语义，即，当两个参数都是
存在且第一个参数的计算结果为 `True`，第二个参数
根本不会求值。

<span id="function-da-action-foldra-2803" />

### `foldrA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldrA : Action m => (a -> b -> m b) -> b -> [a] -> m b
```

`foldrA` 与 `foldr` 类似，只不过它的结果是
封装在一个动作中。请注意，`foldrA` 从右到左工作
超过列表参数。

<span id="function-da-action-foldr1a-55935" />

### `foldr1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1A : Action m => (a -> a -> m a) -> [a] -> m a
```

`foldr1A` 类似于 `foldrA` 但在呈现时会引发错误
带有空列表参数。

<span id="function-da-action-foldla-78897" />

### `foldlA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldlA : Action m => (b -> a -> m b) -> b -> [a] -> m b
```

`foldlA` 与 `foldl` 类似，只不过它的结果是
封装在一个动作中。请注意，`foldlA`适用于
从左到右遍历列表参数。

<span id="function-da-action-foldl1a-65193" />

### `foldl1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1A : Action m => (a -> a -> m a) -> [a] -> m a
```

`foldl1A` 类似于 `foldlA` 但在以下情况下会引发错误
呈现一个空列表参数。

<span id="function-da-action-filtera-13011" />

### `filterA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filterA : Applicative m => (a -> m Bool) -> [a] -> m [a]
```

使用 applicative 函数过滤列表：仅保留谓词所在的元素。
示例：给定一组 Iou 合约 ID，人们只能找到 GBP。

```
filterA (fmap (\iou -> iou.currency == "GBP") . fetch) iouCids
```

<span id="function-da-action-replicatea-98867" />

### `replicateA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicateA : Applicative m => Int -> m a -> m [a]
```

`replicateA n act` 执行动作 `n` 次，收集
结果。

<span id="function-da-action-replicatea-83733" />

### `replicateA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicateA_ : Applicative m => Int -> m a -> m ()
```

与`replicateA`类似，但丢弃结果。

<span id="function-da-action-gteqgt-60955" />

### `>=>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
>=> : Action m => (a -> m b) -> (b -> m c) -> a -> m c
```

Kleisli 箭头从左到右的组合。

<span id="function-da-action-lteqlt-31871" />

### `<=<`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<=< : Action m => (b -> m c) -> (a -> m b) -> a -> m c
```

Kleisli 箭头从右到左的组合。 @('>=>')@，带有参数
翻转了。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
