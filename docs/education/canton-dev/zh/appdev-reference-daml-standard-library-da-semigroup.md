---
title: "DA.Semigroup"
slug: "appdev-reference-daml-standard-library-da-semigroup"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-semigroup.md"
source_title: "DA.Semigroup"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-semigroup
---

# DA.Semigroup

> Daml 模块 DA.Semigroup 参考文档。

<span id="module-da-semigroup-27147" />

# DA.Semigroup

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定（Stable）。
  </Card>

  <Card title="说明">
    状态：`active`
    引入版本：`3.4.9`
    移除版本：`-`
    警告：`0`
    弃用：`0`
    弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-semigroup-types-max-52699" />

### `data Max a`

在 `max` 下的 Semigroup。

```
> Max 23 <> Max 42
Max 42
```

构造子：

<span id="constr-da-semigroup-types-max-20326" />

* `Max a`

实例：

* `instance Ord a => Semigroup (Max a)`
* `instance Eq a => Eq (Max a)`
* `instance Ord a => Ord (Max a)`
* `instance Show a => Show (Max a)`

<span id="type-da-semigroup-types-min-78217" />

### `data Min a`

在 `min` 下的 Semigroup。

```
> Min 23 <> Min 42
Min 23
```

构造子：

<span id="constr-da-semigroup-types-min-6532" />

* `Min a`

实例：

* `instance Ord a => Semigroup (Min a)`
* `instance Eq a => Eq (Min a)`
* `instance Ord a => Ord (Min a)`
* `instance Show a => Show (Min a)`

## 孤儿类型类实例

* `instance Eq a => Eq (Min a)`

* `instance Ord a => Ord (Min a)`

* `instance Show a => Show (Min a)`

* `instance Eq a => Eq (Max a)`

* `instance Ord a => Ord (Max a)`

* `instance Show a => Show (Max a)`

* `instance Ord a => Semigroup (Min a)`

* `instance Ord a => Semigroup (Max a)`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
