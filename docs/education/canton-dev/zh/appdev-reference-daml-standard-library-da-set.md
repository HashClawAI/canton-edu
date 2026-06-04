---
title: "DA.Set"
slug: "appdev-reference-daml-standard-library-da-set"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-set.md"
source_title: "DA.Set"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-set
---

# DA.Set

> Daml 模块 DA.Set 参考文档

# DA.Set

<span id="module-da-set-6124" />

# DA.Set

注意：仅支持 Daml-LF 1.11 或更高版本。

本模块导出泛型集合类型 `Set k` 及相关

函数。应使用限定导入，例如：

```

import DA.Set (Set)

import DA.Set qualified as S

```

这样可访问 `Set` 类型，并以

`S.lookup`、`S.insert`、`S.fromList` 等形式使用各操作。

`Set k` 内部使用类型 `k` 的内建序。

这意味着含函数的键不可比较，

会导致运行时错误。为避免此问题，多数集合操作要求 `Ord k`

实例。建议仅对具有自动

`deriving` 的 `Ord k` 实例的键类型使用 `Set k`：

```

data K = ...

deriving (Eq, Ord)

```

包括所有非函数类型的内建类型，例如

`Int`、`Text`、`Bool`、在 `a` 与 `b` 有默认

`Ord` 实例时的 `(a, b)`、在 `t` 有默认 `Ord` 时的 `Optional t` 与 `[t]`、

在 `k` 与 `v` 有默认 `Ord` 时的 `Map k v`，

以及 `k` 有默认 `Ord` 时的 `Set k`。

## 模块快照

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="通知">
    状态：`active`
    引入版本：`3.4.9`
    移除版本：`-`
    警告数：`0`
    弃用数：`0`
    弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-set-types-set-90436" />

### `data Set k`

集合类型，是对 `Map` 类型的封装。

构造子：

<span id="constr-da-set-types-set-78105" />

* `Set`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| map | Map k () |  |

实例：

* `instance Foldable Set`
* `instance Ord k => Monoid (Set k)`
* `instance Ord k => Semigroup (Set k)`
* `instance GetField map (Set k) (Map k ())`
* `instance SetField map (Set k) (Map k ())`
* `instance IsParties (Set Party)`
* `instance Ord k => Eq (Set k)`
* `instance Ord k => Ord (Set k)`
* `instance (Ord k, Show k) => Show (Set k)`

## 函数

<span id="function-da-set-empty-19742" />

### `empty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
empty : Set k
```

空集。

<span id="function-da-set-size-6437" />

### `size`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
size : Set k -> Int
```

集合中元素个数。

<span id="function-da-set-tolist-26355" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : Set k -> [k]
```

将集合转为元素列表。

<span id="function-da-set-fromlist-9190" />

### `fromList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromList : Ord k => [k] -> Set k
```

由元素列表创建集合。

<span id="function-da-set-tomap-37614" />

### `toMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toMap : Set k -> Map k ()
```

将 `Set` 转为 `Map`。

<span id="function-da-set-frommap-15501" />

### `fromMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromMap : Map k () -> Set k
```

由 `Map` 创建 `Set`。

<span id="function-da-set-member-75542" />

### `member`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
member : Ord k => k -> Set k -> Bool
```

元素是否在集合中？

<span id="function-da-set-notmember-79044" />

### `notMember`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
notMember : Ord k => k -> Set k -> Bool
```

元素是否不在集合中？
`notMember k s` 等价于 `not (member k s)`。

<span id="function-da-set-null-99389" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : Set k -> Bool
```

是否为空集？

<span id="function-da-set-insert-58479" />

### `insert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insert : Ord k => k -> Set k -> Set k
```

向集合插入元素；若已存在则返回原集合。

<span id="function-da-set-filter-76182" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : Ord k => (k -> Bool) -> Set k -> Set k
```

保留满足谓词的所有元素。

<span id="function-da-set-delete-52281" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Ord k => k -> Set k -> Set k
```

从集合删除元素。

<span id="function-da-set-singleton-15574" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : Ord k => k -> Set k
```

创建单元素集合。

<span id="function-da-set-union-79876" />

### `union`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
union : Ord k => Set k -> Set k -> Set k
```

两集合的并集。

<span id="function-da-set-intersection-70017" />

### `intersection`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intersection : Ord k => Set k -> Set k -> Set k
```

两集合的交集。

<span id="function-da-set-difference-68545" />

### `difference`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
difference : Ord k => Set k -> Set k -> Set k
```

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
`difference x y` returns the set consisting of all
elements in `x` that are not in `y`.

>>> fromList [1, 2, 3] `difference` fromList [1, 4]
fromList [2, 3]
```

<span id="function-da-set-issubsetof-34493" />

### `isSubsetOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSubsetOf : Ord k => Set k -> Set k -> Bool
```

`isSubsetOf a b` 在 `a` 是 `b` 的子集时返回 true，
即 `a` 的每个元素都在 `b` 中。

<span id="function-da-set-ispropersubsetof-90093" />

### `isProperSubsetOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isProperSubsetOf : Ord k => Set k -> Set k -> Bool
```

`isProperSubsetOf a b` 在 `a` 是 `b` 的真子集时返回 true。
即 `a` 是 `b` 的子集但不等于 `b`。

## 孤立类型类实例

* `instance Ord k => Eq (Set k)`

* `instance Ord k => Ord (Set k)`

* `instance (Ord k, Show k) => Show (Set k)`

* `instance IsParties (Set Party)`

* `instance Ord k => Semigroup (Set k)`

* `instance Ord k => Monoid (Set k)`

* `instance GetField map (Set k) (Map k ())`

* `instance SetField map (Set k) (Map k ())`

* `instance Foldable Set`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
