# DA.Foldable

> Daml 模块 DA.Foldable 的参考文档。

<span id="module-da-foldable-94882" />

# DA.Foldable

可折叠为汇总值的数据结构类型类。

建议 qualified 导入本模块以免与 `Prelude` 中函数冲突，例如：

```

import DA.Foldable qualified as F

```

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

## 类型类

<span id="class-da-foldable-foldable-25994" />

### `class Foldable t`

可折叠为汇总值的数据结构类型类。

方法：

* `fold : Monoid m => t m -> m`
  用 monoid 合并结构中的元素。
* `foldMap : Monoid m => (a -> m) -> t a -> m`
  用 monoid 合并结构中的元素。
* `foldr : (a -> b -> b) -> b -> t a -> b`
  对结构做右结合 fold。
* `foldl : (b -> a -> b) -> b -> t a -> b`
  对结构做左结合 fold。
* `foldr1 : (a -> a -> a) -> t a -> a`
  无基情形的 `foldr` 变体，仅应用于非空结构。
* `foldl1 : (a -> a -> a) -> t a -> a`
  无基情形的 `foldl` 变体，仅应用于非空结构。
* `toList : t a -> [a]`
  结构的元素列表，从左到右。
* `null : t a -> Bool`
  判断结构是否为空。默认实现对类似 cons 列表的结构做了优化，因一般无法做得更好。
* `length : t a -> Int`
  以 `Int` 返回有限结构的大小/长度。默认实现对类似 cons 列表的结构做了优化。
* `elem : Eq a => a -> t a -> Bool`
  元素是否出现在结构中？
* `sum : Additive a => t a -> a`
  计算结构中数值的和。
* `product : Multiplicative a => t a -> a`
  计算结构中数值的积。
* `minimum : Ord a => t a -> a`
  非空结构的最小元素。
* `maximum : Ord a => t a -> a`
  非空结构的最大元素。

实例：

* `instance Ord k => Foldable (Map k)`
* `instance Foldable TextMap`
* `instance Foldable Optional`
* `instance Foldable NonEmpty`
* `instance Foldable Set`
* `instance Foldable (Validation err)`
* `instance Foldable (Either a)`
* `instance Foldable []`
* `instance Foldable a`

## 函数

<span id="function-da-foldable-mapa-78745" />

### `mapA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA_ : (Foldable t, Applicative f) => (a -> f b) -> t a -> f ()
```

将结构中每个元素映射为 action，从左到右求值并忽略结果。需要保留结果时请见 `DA.Traversable.mapA`。

<span id="function-da-foldable-fora-54422" />

### `forA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA_ : (Foldable t, Applicative f) => t a -> (a -> f b) -> f ()
```

`forA_` 是参数翻转的 `mapA_`。需要保留结果时请见 `DA.Traversable.forA`。

<span id="function-da-foldable-form-34370" />

### `forM_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forM_ : (Foldable t, Applicative f) => t a -> (a -> f b) -> f ()
```

<span id="function-da-foldable-sequence-26917" />

### `sequence_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequence_ : (Foldable t, Action m) => t (m a) -> m ()
```

从左到右求值结构中每个 action 并忽略结果。需要保留结果时请见 `DA.Traversable.sequence`。

<span id="function-da-foldable-concat-71538" />

### `concat`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concat : Foldable t => t [a] -> [a]
```

拼接容器中所有列表元素。

<span id="function-da-foldable-and-52214" />

### `and`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
and : Foldable t => t Bool -> Bool
```

`and` 返回 Bool 容器的合取。结果为 `True` 时容器须为有限；`False` 可由距左端有限距离处的 `False` 得出。

<span id="function-da-foldable-or-15333" />

### `or`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
or : Foldable t => t Bool -> Bool
```

`or` 返回 Bool 容器的析取。结果为 `False` 时容器须为有限；`True` 可由距左端有限距离处的 `True` 得出。

<span id="function-da-foldable-any-93587" />

### `any`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
any : Foldable t => (a -> Bool) -> t a -> Bool
```

判断结构中是否存在满足谓词的元素。

<span id="function-da-foldable-all-59560" />

### `all`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
all : Foldable t => (a -> Bool) -> t a -> Bool
```

判断结构中是否所有元素都满足谓词。
