---
title: "DA.List.Total"
slug: "appdev-reference-daml-standard-library-da-list-total"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-list-total.md"
source_title: "DA.List.Total"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-list-total
---

# DA.List.Total

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.List.Total

> Daml 模块 DA.List.Total 的参考文档。

<span id="module-da-list-total-99663" />

# DA.List.Total

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

<span id="function-da-list-total-head-26095" />

### `head`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
head : [a] -> Optional a
```

返回列表首元素。列表为空时返回 `None`。

<span id="function-da-list-total-tail-49055" />

### `tail`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tail : [a] -> Optional [a]
```

返回除首元素外的列表。列表为空时返回 `None`。

<span id="function-da-list-total-last-22829" />

### `last`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
last : [a] -> Optional a
```

提取列表末元素。列表为空时返回 `None`。

<span id="function-da-list-total-init-12739" />

### `init`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
init : [a] -> Optional [a]
```

返回除末元素外的所有元素。列表为空时返回 `None`。

<span id="function-da-list-total-bangbang-57917" />

### `!!`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
!! : [a] -> Int -> Optional a
```

返回列表第 n 个元素。索引越界时返回 `None`。

<span id="function-da-list-total-foldl1-27683" />

### `foldl1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1 : (a -> a -> a) -> [a] -> Optional a
```

从列表头部开始做左 fold。
例如 `foldl1 f [a,b,c] = f (f a b) c`。
列表为空时返回 `None`。

<span id="function-da-list-total-foldr1-3777" />

### `foldr1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1 : (a -> a -> a) -> [a] -> Optional a
```

从列表末元素开始做右 fold。
例如 `foldr1 f [a,b,c] = f a (f b c)`

<span id="function-da-list-total-foldbalanced1-85298" />

### `foldBalanced1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldBalanced1 : (a -> a -> a) -> [a] -> Optional a
```

以平衡方式 fold 非空列表。平衡指运算符树中各元素深度大致相同（最大与最小深度差至多为 1）。累加运算须结合且可交换，才能得到与 `foldl1` 或 `foldr1` 相同的结果。

列表为空时返回 `None`。

<span id="function-da-list-total-minimumby-50223" />

### `minimumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumBy : (a -> a -> Ordering) -> [a] -> Optional a
```

按给定比较函数返回列表最小元素。列表为空时返回 `None`。

<span id="function-da-list-total-maximumby-35485" />

### `maximumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumBy : (a -> a -> Ordering) -> [a] -> Optional a
```

按给定比较函数返回列表最大元素。列表为空时返回 `None`。

<span id="function-da-list-total-minimumon-58803" />

### `minimumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumOn : Ord k => (a -> k) -> [a] -> Optional a
```

按键函数比较时返回列表最小元素。
例如 `minimumOn (\(x,y) -> x + y) [(1,2), (2,0)] == Some (2,0)`。
列表为空时返回 `None`。

<span id="function-da-list-total-maximumon-82285" />

### `maximumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumOn : Ord k => (a -> k) -> [a] -> Optional a
```

按键函数比较时返回列表最大元素。
例如 `maximumOn (\(x,y) -> x + y) [(1,2), (2,0)] == Some (1,2)`。
列表为空时返回 `None`。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
