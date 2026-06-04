---
title: "DA.Logic"
slug: "appdev-reference-daml-standard-library-da-logic"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-logic.md"
source_title: "DA.Logic"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-logic
---

# DA.Logic

> Daml 模块 DA.Logic 参考文档。

<span id="module-da-logic-59184" />

# DA.Logic

Logic — 命题演算。

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

<span id="type-da-logic-types-formula-34794" />

### `data Formula t`

`Formula t` 表示命题类型为 `t` 的命题演算公式。

构造子：

<span id="constr-da-logic-types-proposition-6173" />

* `Proposition t`
  `Proposition p` 即命题 `p`

<span id="constr-da-logic-types-negation-48969" />

* `Negation (Formula t)`
  对公式 `f`，`Negation f` 表示 ¬f

<span id="constr-da-logic-types-conjunction-51637" />

* `Conjunction [Formula t]`
  对公式 f1, …, fn，`Conjunction [f1, ..., fn]` 表示 f1 ∧ … ∧ fn

<span id="constr-da-logic-types-disjunction-65549" />

* `Disjunction [Formula t]`
  对公式 f1, …, fn，`Disjunction [f1, ..., fn]` 表示 f1 ∨ … ∨ fn

实例：

* `instance Action Formula`
* `instance Applicative Formula`
* `instance Functor Formula`
* `instance Eq t => Eq (Formula t)`
* `instance Ord t => Ord (Formula t)`
* `instance Show t => Show (Formula t)`

## 函数

<span id="function-da-logic-ampampamp-55265" />

### `&&&`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
&&& : Formula t -> Formula t -> Formula t
```

`&&&` 为公式布尔代数中的 ∧ 运算，读作「与」。

<span id="function-da-logic-pipepipepipe-30747" />

### `|||`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
||| : Formula t -> Formula t -> Formula t
```

`|||` 为公式布尔代数中的 ∨ 运算，读作「或」。

<span id="function-da-logic-true-31438" />

### `true`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
true : Formula t
```

`true` 为公式布尔代数的单位元 1，表示为空合取。

<span id="function-da-logic-false-99028" />

### `false`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
false : Formula t
```

`false` 为公式布尔代数的零元 0，表示为空析取。

<span id="function-da-logic-neg-1597" />

### `neg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
neg : Formula t -> Formula t
```

`neg` 为公式布尔代数中的 ¬（否定）运算。

<span id="function-da-logic-conj-82504" />

### `conj`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conj : [Formula t] -> Formula t
```

`conj` 是 `&&&` 的列表版本，利用 ∧ 的结合律。

<span id="function-da-logic-disj-92448" />

### `disj`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
disj : [Formula t] -> Formula t
```

`disj` 是 `|||` 的列表版本，利用 ∨ 的结合律。

<span id="function-da-logic-frombool-36630" />

### `fromBool`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromBool : Bool -> Formula t
```

`fromBool` 将 `True` 转为 `true`，`False` 转为 `false`。

<span id="function-da-logic-tonnf-87354" />

### `toNNF`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toNNF : Formula t -> Formula t
```

`toNNF` 将公式化为否定范式（参见 [否定范式](https://en.wikipedia.org/wiki/Negation_normal_form)）。

<span id="function-da-logic-todnf-90852" />

### `toDNF`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toDNF : Formula t -> Formula t
```

`toDNF` 将公式化为析取范式（参见 [析取范式](https://en.wikipedia.org/wiki/Disjunctive_normal_form)）。

<span id="function-da-logic-traverse-17816" />

### `traverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traverse : Applicative f => (t -> f s) -> Formula t -> f (Formula s)
```

通常意义上的 `traverse` 实现。

<span id="function-da-logic-zipformulas-28999" />

### `zipFormulas`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipFormulas : Formula t -> Formula s -> Formula (t, s)
```

`zipFormulas` 对两个结构相同（仅命题不同）的公式进行 zip。

<span id="function-da-logic-substitute-65872" />

### `substitute`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substitute : (t -> Optional Bool) -> Formula t -> Formula t
```

`substitute` 根据真值赋值将 `True` 或 `False` 代入公式相应位置。

<span id="function-da-logic-reduce-40218" />

### `reduce`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reduce : Formula t -> Formula t
```

`reduce` 尽可能化简公式：

1. 移除所有 `true` 与 `false` 出现；
2. 移除直接嵌套的 Conjunction 与 Disjunction；
3. 化为否定范式。

<span id="function-da-logic-isbool-80820" />

### `isBool`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isBool : Formula t -> Optional Bool
```

`isBool` 尝试将公式转为 `Bool`。满足 `isBool true == Some True` 且 `isBool false == Some False`，否则返回 `None`。

<span id="function-da-logic-interpret-88386" />

### `interpret`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interpret : (t -> Optional Bool) -> Formula t -> Either (Formula t) Bool
```

`interpret` 是 `toBool` 的变体：先用真值函数代入，再尽可能化简。

<span id="function-da-logic-substitutea-61566" />

### `substituteA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substituteA : Applicative f => (t -> f (Optional Bool)) -> Formula t -> f (Formula t)
```

`substituteA` 是 `substitute` 的变体，允许通过 action 获取真值。

<span id="function-da-logic-interpreta-14928" />

### `interpretA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interpretA : Applicative f => (t -> f (Optional Bool)) -> Formula t -> f (Either (Formula t) Bool)
```

`interpretA` 是 `interpret` 的变体，允许通过 action 获取真值。

## 孤儿类型类实例

* `instance Eq t => Eq (Formula t)`

* `instance Ord t => Ord (Formula t)`

* `instance Show t => Show (Formula t)`

* `instance Functor Formula`

* `instance Applicative Formula`

* `instance Action Formula`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
