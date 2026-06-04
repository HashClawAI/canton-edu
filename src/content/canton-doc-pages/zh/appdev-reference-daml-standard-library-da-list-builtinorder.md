---
title: "DA.List.BuiltinOrder"
slug: "appdev-reference-daml-standard-library-da-list-builtinorder"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-list-builtinorder.md"
source_title: "DA.List.BuiltinOrder"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-list-builtinorder
---

# DA.List.BuiltinOrder

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.List.BuiltinOrder

> Daml 模块 DA.List.BuiltinOrder 的参考文档。

<span id="module-da-list-builtinorder-49213" />

# DA.List.BuiltinOrder

说明：仅支持 Daml-LF 1.11 及更高版本。

本模块提供基于 Daml-LF 内建序（而非用户自定义序）的标准库函数变体，与 `DA.Map` 所用顺序相同。

这些函数通常比基于 `Ord` 的对应函数高效得多。

注意：本模块函数仍要求 `Ord` 约束，仅为防止传入不可比较的值（如函数）；其实现并不使用这些实例。

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

<span id="function-da-list-builtinorder-dedup-38418" />

### `dedup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedup : Ord a => [a] -> [a]
```

`dedup l` 从列表中移除重复元素，仅保留每个元素的首次出现。

`dedup` 是稳定的，输出元素按其在输入中首次出现的顺序排列。若不需要稳定性，可考虑更高效的 `dedupSort`。

```
>>> dedup [3, 1, 1, 3]
[3, 1]
```

<span id="function-da-list-builtinorder-dedupon-23739" />

### `dedupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOn : Ord k => (v -> k) -> [v] -> [v]
```

在应用给定函数后再去重的 `dedup` 版本。示例：`dedupOn (.employeeNo) employees`。

`dedupOn` 是稳定的。若不需要稳定性，可考虑更高效的 `dedupOnSort`。

```
>>> dedupOn fst [(3, "a"), (1, "b"), (1, "c"), (3, "d")]
[(3, "a"), (1, "b")]
```

<span id="function-da-list-builtinorder-dedupsort-5846" />

### `dedupSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSort : Ord a => [a] -> [a]
```

`dedupSort` 是 `dedup` 的更高效变体，不保留输入元素顺序；
输出按 Daml-LF 内建序排序。

```
>>> dedupSort [3, 1, 1, 3]
[1, 3]
```

<span id="function-da-list-builtinorder-deduponsort-69087" />

### `dedupOnSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOnSort : Ord k => (v -> k) -> [v] -> [v]
```

`dedupOnSort` 是 `dedupOn` 的更高效变体，不保留输入元素顺序；
输出按函数返回值排序。

对重复项，输出包含列表中第一个元素。

```
>>> dedupOnSort fst [(3, "a"), (1, "b"), (1, "c"), (3, "d")]
[(1, "b"), (3, "a")]
```

<span id="function-da-list-builtinorder-sort-65819" />

### `sort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sort : Ord a => [a] -> [a]
```

按 Daml-LF 序排序列表。

在内建 Daml-LF 序下相同的值不可区分，因此此处稳定性无关。

```
>>> sort [3,1,2]
[1,2,3]
```

<span id="function-da-list-builtinorder-sorton-7978" />

### `sortOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortOn : Ord b => (a -> b) -> [a] -> [a]
```

`sortOn f` 是 `sort` 的变体，允许按给定函数的返回值排序。

`sortOn` 是稳定的：映射到相同排序键的元素按输入位置排序。

```
>>> sortOn fst [(3, "a"), (1, "b"), (3, "c"), (2, "d")]
[(1, "b"), (2, "d"), (3, "a"), (3, "c")]
```

<span id="function-da-list-builtinorder-unique-2492" />

### `unique`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unique : Ord a => [a] -> Bool
```

当且仅当给定列表无重复元素时返回 True。

```
>>> unique [1, 2, 3]
True
```

<span id="function-da-list-builtinorder-uniqueon-93017" />

### `uniqueOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueOn : Ord k => (a -> k) -> [a] -> Bool
```

在应用函数后，当且仅当列表无重复元素时返回 True。

```
>>> uniqueOn fst [(1, 2), (2, 42), (1, 3)]
False
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
