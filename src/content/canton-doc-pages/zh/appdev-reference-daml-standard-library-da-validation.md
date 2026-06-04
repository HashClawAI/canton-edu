---
title: "DA.Validation"
slug: "appdev-reference-daml-standard-library-da-validation"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-validation.md"
source_title: "DA.Validation"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-validation
---

# DA.Validation

> Daml 模块 DA.Validation 参考文档

# DA.Validation

<span id="module-da-validation-69700" />

# DA.Validation

`Validation` 类型及相关函数。

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

<span id="type-da-validation-types-validation-39644" />

### `data Validation err a`

`Validation` 表示非空错误列表或成功值。
相比 `Either`，可累积多条错误。

构造子：

<span id="constr-da-validation-types-errors-73825" />

* `Errors (NonEmpty err)`

<span id="constr-da-validation-types-success-12286" />

* `Success a`

实例：

* `instance Foldable (Validation err)`
* `instance Applicative (Validation err)`
* `instance Semigroup (Validation err a)`
* `instance Traversable (Validation err)`
* `instance Functor (Validation err)`
* `instance (Eq err, Eq a) => Eq (Validation err a)`
* `instance (Show err, Show a) => Show (Validation err a)`

## 函数

<span id="function-da-validation-invalid-71114" />

### `invalid`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
invalid : err -> Validation err a
```

因给定原因失败。

<span id="function-da-validation-ok-57346" />

### `ok`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ok : a -> Validation err a
```

以给定值成功。

<span id="function-da-validation-validate-15676" />

### `validate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
validate : Either err a -> Validation err a
```

将 `Either` 转为 `Validation`。

<span id="function-da-validation-run-73024" />

### `run`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
run : Validation err a -> Either (NonEmpty err) a
```

将 `Validation err a` 转为 `Either`，
左值为非空错误列表。

<span id="function-da-validation-run1-16566" />

### `run1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
run1 : Validation err a -> Either err a
```

将 `Validation err a` 转为 `Either`，
左值仅取第一个错误。

<span id="function-da-validation-runwithdefault-81974" />

### `runWithDefault`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
runWithDefault : a -> Validation err a -> a
```

运行 `Validation err a`，出错时返回默认值。

<span id="function-da-validation-ltwhatgt-24976" />

### `<?>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<?> : Optional b -> err -> Validation err b
```

将 `Optional t` 转为 `Validation err t`（或更一般地转为任意 `ActionFail` 类型 `m` 的 `m t`）。

## 孤立类型类实例

* `instance (Eq err, Eq a) => Eq (Validation err a)`

* `instance (Show err, Show a) => Show (Validation err a)`

* `instance Functor (Validation err)`

* `instance Applicative (Validation err)`

* `instance Semigroup (Validation err a)`

* `instance Foldable (Validation err)`

* `instance Traversable (Validation err)`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
