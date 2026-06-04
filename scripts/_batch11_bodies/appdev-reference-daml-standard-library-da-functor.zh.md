# DA.Functor

> Daml 模块 DA.Functor 的参考文档。

<span id="module-da-functor-63823" />

# DA.Functor

`Functor` 类用于可映射（map）的类型。

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

<span id="function-da-functor-dollargt-48161" />

### `$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
$> : Functor f => f a -> b -> f b
```

将输入（左侧）中所有位置替换为给定值（右侧）。

<span id="function-da-functor-ltampgt-91298" />

### `<&>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<&> : Functor f => f a -> (a -> b) -> f b
```

对 functor 应用函数。给定 `as` 与 `f`，`as <&> f` 即 `f <$> as`。即 `<&>` 与 `<$>` 参数顺序相反。

<span id="function-da-functor-ltdollardollargt-89503" />

### `<$$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<$$> : (Functor f, Functor g) => (a -> b) -> g (f a) -> g (f b)
```

嵌套 `<$>`。

<span id="function-da-functor-void-91123" />

### `void`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
void : Functor f => f a -> f ()
```

将输入中所有位置替换为 `()`。
