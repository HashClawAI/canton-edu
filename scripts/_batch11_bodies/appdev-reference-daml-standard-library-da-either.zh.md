# DA.Either

> Daml 模块 DA.Either 的参考文档。

<span id="module-da-either-91022" />

# DA.Either

`Either` 类型表示具有两种可能性的值。

有时用于表示值要么正确、要么为错误。按惯例，`Left` 构造子存放错误值，`Right` 存放正确值（助记：「right」也有「正确」之意）。

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

## 函数

<span id="function-da-either-lefts-59601" />

### `lefts`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lefts : [Either a b] -> [a]
```

从列表中提取所有 `Left` 元素。

<span id="function-da-either-rights-20455" />

### `rights`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
rights : [Either a b] -> [b]
```

从列表中提取所有 `Right` 元素。

<span id="function-da-either-partitioneithers-19904" />

### `partitionEithers`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partitionEithers : [Either a b] -> ([a], [b])
```

将 `Either` 列表划分为两个列表，分别为 `Left` 与 `Right` 元素，并保持顺序。

<span id="function-da-either-isleft-96021" />

### `isLeft`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLeft : Either a b -> Bool
```

若给定值为 `Left`，返回 `True`，否则返回 `False`。

<span id="function-da-either-isright-36975" />

### `isRight`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isRight : Either a b -> Bool
```

若给定值为 `Right`，返回 `True`，否则返回 `False`。

<span id="function-da-either-fromleft-63875" />

### `fromLeft`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromLeft : a -> Either a b -> a
```

返回 `Left` 值的内容；若为 `Right` 则返回默认值。

<span id="function-da-either-fromright-27657" />

### `fromRight`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromRight : b -> Either a b -> b
```

返回 `Right` 值的内容；若为 `Left` 则返回默认值。

<span id="function-da-either-optionaltoeither-21876" />

### `optionalToEither`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
optionalToEither : a -> Optional b -> Either a b
```

将 `Optional` 转为 `Either`；若 `Optional` 为 `None`，则使用所供参数作为 `Left` 值。

<span id="function-da-either-eithertooptional-89140" />

### `eitherToOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
eitherToOptional : Either a b -> Optional b
```

将 `Either` 转为 `Optional`，丢弃 `Left` 中的值。

<span id="function-da-either-maybetoeither-6635" />

### `maybeToEither`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maybeToEither : a -> Optional b -> Either a b
```

<span id="function-da-either-eithertomaybe-94811" />

### `eitherToMaybe`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
eitherToMaybe : Either a b -> Optional b
```
