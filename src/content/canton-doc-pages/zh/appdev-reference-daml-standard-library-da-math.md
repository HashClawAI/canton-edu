---
title: "DA.Math"
slug: "appdev-reference-daml-standard-library-da-math"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-math.md"
source_title: "DA.Math"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-math
---

# DA.Math

> Daml 模块 DA.Math 参考文档。

<span id="module-da-math-30023" />

# DA.Math

Math — `Decimal` 实用数学函数。

本库侧重高精度，通常可提供约 9 位正确小数。数值算法经多次迭代达到该精度，由 Daml 运行时解释执行，**性能不高**。在性能敏感场景不建议使用。

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

## 函数

<span id="function-da-math-starstar-89123" />

### `**`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
** : Decimal -> Decimal -> Decimal
```

幂运算。示例：`2.0 ** 3.0 == 8.0`。

<span id="function-da-math-sqrt-24467" />

### `sqrt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sqrt : Decimal -> Decimal
```

计算 `Decimal` 的平方根。

```
>>> sqrt 1.44
1.2
```

<span id="function-da-math-exp-84235" />

### `exp`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exp : Decimal -> Decimal
```

指数函数。示例：`exp 0.0 == 1.0`

<span id="function-da-math-log-52192" />

### `log`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
log : Decimal -> Decimal
```

自然对数。示例：`log 10.0 == 2.30258509299`

<span id="function-da-math-logbase-64267" />

### `logBase`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
logBase : Decimal -> Decimal -> Decimal
```

以给定底数的对数。示例：`log 10.0 100.0 == 2.0`

<span id="function-da-math-sin-61636" />

### `sin`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sin : Decimal -> Decimal
```

`sin` 为正弦函数。

<span id="function-da-math-cos-82859" />

### `cos`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
cos : Decimal -> Decimal
```

`cos` 为余弦函数。

<span id="function-da-math-tan-54959" />

### `tan`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tan : Decimal -> Decimal
```

`tan` 为正切函数。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
