---
title: "DA.Traversable"
slug: "appdev-reference-daml-standard-library-da-traversable"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-traversable.md"
source_title: "DA.Traversable"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-traversable
---

# DA.Traversable

> Daml 模块 DA.Traversable 参考文档

# DA.Traversable

<span id="module-da-traversable-75075" />

# DA.Traversable

可从左到右遍历并对每个元素执行动作的数据结构类型类。

通常应限定导入以避免与

`Prelude` 中函数冲突，例如：

```

import DA.Traversable   qualified as F

```

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

## 类型类

<span id="class-da-traversable-traversable-18144" />

### `class (Functor t, Foldable t) => Traversable t`

表示可从左到右遍历的数据结构的 Functor。

方法：

* `mapA : Applicative f => (a -> f b) -> t a -> f (t b)`
  将结构中每个元素映射为动作，从左到右求值并收集结果。
  
* `sequence : Applicative f => t (f a) -> f (t a)`
  从左到右求值结构中的每个动作并收集结果。
  

实例：

* `instance Ord k => Traversable (Map k)`
* `instance Traversable TextMap`
* `instance Traversable Optional`
* `instance Traversable NonEmpty`
* `instance Traversable (Validation err)`
* `instance Traversable (Either a)`
* `instance Traversable []`
* `instance Traversable a`

## 函数

<span id="function-da-traversable-fora-19271" />

### `forA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA : (Traversable t, Applicative f) => t a -> (a -> f b) -> f (t b)
```

`forA` 是参数翻转的 `mapA`。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
