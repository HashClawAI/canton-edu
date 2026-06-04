---
title: "DA.TextMap"
slug: "appdev-reference-daml-standard-library-da-textmap"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-textmap.md"
source_title: "DA.TextMap"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-textmap
---

# DA.TextMap

> Daml 模块 DA.TextMap 参考文档

# DA.TextMap

<span id="module-da-textmap-81719" />

# DA.TextMap

TextMap——键值对关联数组，每个键最多出现一次。

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

## 函数

<span id="function-da-textmap-fromlist-19033" />

### `fromList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromList : [(Text, a)] -> TextMap a
```

由键值对列表创建映射。

<span id="function-da-textmap-fromlistwithl-22912" />

### `fromListWithL`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithL : (a -> a -> a) -> [(Text, a)] -> TextMap a
```

由键值对列表创建映射，并用合并函数处理重复键。
合并函数仅在键多次出现时调用，
参数为新插入值与该键已累积值。

示例：

```
>>> fromListWithL (++) [("A", [1]), ("A", [2]), ("B", [2]), ("B", [1]), ("A", [3])]
fromList [("A", [3, 2, 1]), ("B", [1, 2])]
>>> fromListWithL (++) [] == (empty : TextMap [Int])
True
```

<span id="function-da-textmap-fromlistwithr-69626" />

### `fromListWithR`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithR : (a -> a -> a) -> [(Text, a)] -> TextMap a
```

类似 `fromListWithL`，但合并函数参数顺序相反。
示例：

```
>>> fromListWithR (++) [("A", [1]), ("A", [2]), ("B", [2]), ("B", [1]), ("A", [3])]
fromList [("A", [1, 2, 3]), ("B", [2, 1])]
>>> fromListWithR (++) [] == (empty : TextMap [Int])
True
```

<span id="function-da-textmap-fromlistwith-41741" />

### `fromListWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWith : (a -> a -> a) -> [(Text, a)] -> TextMap a
```

<span id="function-da-textmap-tolist-95168" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : TextMap a -> [(Text, a)]
```

将映射转为键值对列表，键按升序排列。

<span id="function-da-textmap-empty-66187" />

### `empty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
empty : TextMap a
```

空映射。

<span id="function-da-textmap-size-46150" />

### `size`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
size : TextMap a -> Int
```

映射中元素个数。

<span id="function-da-textmap-null-64690" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : TextMap v -> Bool
```

映射是否为空？

<span id="function-da-textmap-lookup-87021" />

### `lookup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookup : Text -> TextMap a -> Optional a
```

按键查找值。

<span id="function-da-textmap-member-14417" />

### `member`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
member : Text -> TextMap v -> Bool
```

键是否在映射中？

<span id="function-da-textmap-filter-317" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : (v -> Bool) -> TextMap v -> TextMap v
```

用谓词过滤 `TextMap`：仅保留值满足谓词的条目。

<span id="function-da-textmap-filterwithkey-64027" />

### `filterWithKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filterWithKey : (Text -> v -> Bool) -> TextMap v -> TextMap v
```

用谓词过滤 `TextMap`：仅保留满足谓词的条目。

<span id="function-da-textmap-delete-54270" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Text -> TextMap a -> TextMap a
```

删除键及其值；键不存在时返回原映射。

<span id="function-da-textmap-singleton-39431" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : Text -> a -> TextMap a
```

创建单键映射。

<span id="function-da-textmap-insert-41312" />

### `insert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insert : Text -> a -> TextMap a -> TextMap a
```

插入键值对；键已存在时用 `f new_value old_value` 合并。

<span id="function-da-textmap-insertwith-45464" />

### `insertWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insertWith : (v -> v -> v) -> Text -> v -> TextMap v -> TextMap v
```

插入键值对；键已存在时用 `f new_value old_value` 合并。

<span id="function-da-textmap-union-13945" />

### `union`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
union : TextMap a -> TextMap a -> TextMap a
```

两映射的并集；键冲突时优先取第一个映射的值。

<span id="function-da-textmap-merge-26784" />

### `merge`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
merge : (Text -> a -> Optional c) -> (Text -> b -> Optional c) -> (Text -> a -> b -> Optional c) -> TextMap a -> TextMap b -> TextMap c
```

合并两映射。`merge f g h x y` 对仅出现在 `x` 的键用 `f`，
仅出现在 `y` 的键用 `g`，
两映射都有的键用 `h`；保留结果为 `Some` 的条目。

## 孤立类型类实例

* `instance Show a => Show (TextMap a)`

* `instance Eq a => Eq (TextMap a)`

* `instance Ord a => Ord (TextMap a)`

* `instance Semigroup (TextMap b)`

* `instance Monoid (TextMap b)`

* `instance Functor TextMap`

* `instance Foldable TextMap`

* `instance Traversable TextMap`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
