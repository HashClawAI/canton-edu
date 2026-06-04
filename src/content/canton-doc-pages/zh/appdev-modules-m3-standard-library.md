---
title: "Daml 标准库"
slug: "appdev-modules-m3-standard-library"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-standard-library.md"
source_title: "The Daml Standard Library"
tags:
  - appdev
  - modules
  - m3-standard-library
---

# Daml 标准库

> 浏览 Daml 标准库：Prelude、重要类型与类型类，以及如何查阅与搜索库函数。

在 `data` 与 `functional-101` 中你已学会定义自己的数据类型与函数，但不必从零实现一切。Daml 附带标准库，涵盖大量用例的类型、函数与类型类。

本章概览要点并说明如何浏览与搜索库以查找函数。熟练运用标准库可显著提高 Daml 开发效率。具体包括：

* Prelude
* 标准库重要类型及其函数与类型类
* 类型类
* `Functor`、`Foldable`、`Traversable` 等重要类型类
* 如何搜索标准库

若要深入，可参考 `haskell-connection` 中的资料。标准库类型类如 `Applicative`、`Foldable`、`Traversable`、`Action`（Haskell 中称 `Monad`）等是 Haskell 程序员的日常工具。

<Note>
  本章有项目模板 `daml-intro-11`，但仅含嵌入本节代码片段的单个源文件。
</Note>

## Prelude

你已在不 import 的情况下使用大量函数、类型与类型类：如 `create`、`exercise`、`(==)`，类型 `[]`、`(,)`、`Optional`，类型类 `Eq`、`Show`、`Ord`。它们来自 Prelude。Prelude 被隐式导入每个 Daml 模块，既含 Daml 专用机制，也含操作内建类型与类型类所需的基础。

## Prelude 中的重要类型

除 `native-types` 外，Prelude 还定义多种常见类型：

### 列表

你已见过列表。列表有两个构造子 `[]` 与 `x :: xs`，后者为「前置」：`1 :: [2] == [1, 2]`。事实上 `[1,2]` 是 `1 :: 2 :: []` 的语法糖。

### 元组

除已见的二元组外，Prelude 定义至多 15 元组。元组以临时方式存储混合数据。常见用例是函数返回多个部分，或在 fold 中传递数据（如 `folds`）。较宽元组示例见 `exceptions` 项目的测试模块：`Test.Intro.Asset.TradeSetup.tradeSetup` 以长元组返回分配的参与方与活跃合约；`Test.Intro.Asset.MultiTrade.testMultiTrade` 用模式匹配将它们放回作用域：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Test/Intro/Asset/TradeSetup.daml
-- [Include actual code example here]
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Test/Intro/Asset/MultiTrade.daml
-- [Include actual code example here]
```

元组与列表一样有语法糖：类型与构造子均为 `(,,,)`，逗号数量决定元数。类型与数据构造子可在括号内或外应用，且可部分应用：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

<Note>
  虽支持很长元组，复杂结构或长期存活的值宜定义带命名字段的自定义记录。过度使用元组会损害可读性。
</Note>

### Optional

`Optional` 表示可能缺失的值，最接近 Daml 的「可空」类型。两个构造子：`Some` 带值，`None` 不带值。许多语言会写：

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookupResult = lookupByKey(k);

if( lookupResult == null) {
  // Do something
} else {
  // Do something else
}
```

在 Daml 中可表达为：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

### Either

`Either` 用于值须为两种类型之一。构造子 `Left`、`Right` 各带一种类型的值。典型用法是作为扩展的 `Optional`：`Right` 类似 `Some`，`Left` 类似 `None`，但 `Left` 可存错误值。例如 `Either Text` 行为类似 `Optional`，但 `Left` 构造子的值附带文本。

<Note>
  与元组一样，过度使用 `Either` 会损害可读性。可考虑定义更明确的自定义类型。例如若返回 `South a` 与 `North b`，用自有类型比 `Either` 更清晰。
</Note>

## 类型类

从 `data` 起你已在用类型类，现深入其机制。

类型类用 `class` 关键字声明：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

这类似带 getter/setter 的接口声明。要*实现*该接口，须定义该类型类的实例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

类型类可有约束，如函数：`class Eq a => Ord a` 表示「可排序的类型也可比较相等」。大致如此。

## Prelude 中的重要类型类

### Eq

`Eq` 允许比较（不）相等，提供 `==`、`/=`。多数标准库数据类型有 `Eq` 实例。如 `data` 中所学，可用 `deriving` 让编译器自动生成 `Eq` 实例。

模板总有 `Eq` 实例，模板上存储的所有类型也须有。

### Ord

`Ord` 允许比较顺序，提供 `<`、`>`、`<=`、`>=`。多数内建类型有 `Ord`；`List`、`Optional` 等在元素类型有 `Ord` 时也有实例。可用 `deriving` 自动生成。

### Show

`Show` 表示类型可序列化为 `Text`，即在 shell 中「显示」。关键函数 `show` 将值转为 `Text`。所有内建类型有 `Show`；`List`、`Optional` 在元素有 `Show` 时也有。支持 `deriving`。

### Functor

Functor 是 Daml 中最接近「容器」的概念。见单类型参数的类型，多半是 `Functor`：`[a]`、`Optional a`、`Either Text a`、`Update a`。Functor 可被 map，`Functor` 的关键函数 `fmap` 对列表的 `map` 做泛化。

Set、Map、Tree 等也是经典 Functor。

### Applicative Functor

Applicative Functor 有点像 `constraints` 中的 Action，但不能把一个 action 的结果作为下一个 action 的输入。Daml 中唯一重要且非 action 的 Applicative Functor 是 Daml Script `submit` 块中提交的 `Commands`。因此在 Daml Script 中使用 `do` 记号须启用 `ApplicativeDo` 语言扩展。

### Action

Action 已在 `constraints` 中介绍。可将其视为某值的「配方」，须「执行」才能得到该值。Action 恒为 Functor（也是 Applicative Functor）。直觉上 `fmap f x` 是在 `x` 的配方上增加「对结果应用纯函数 `f`」的指令。

Daml 中最重要的 Action 是 `Update` 与 `Script`，还有许多如 `[]`、`Optional`、`Either a`。

### Semigroup 与 Monoid

Semigroup 与 Monoid 关于二元运算，实践中对 `Text` 与 `[]` 很重要，可用 `{<>}` 拼接。

### Additive 与 Multiplicative

Additive 与 Multiplicative 抽象算术运算，使 `(+)`、`(-)`、`(*)` 等可在 `Decimal` 与 `Int` 间统一使用。

## 标准库中的重要模块

对上述多数类型与类型类，标准库有对应模块：

* [DA.List](/zh/docs/canton/appdev-reference-daml-standard-library-da-list) — 列表
* [DA.Optional](/zh/docs/canton/appdev-reference-daml-standard-library-da-optional) — `Optional`
* [DA.Tuple](/zh/docs/canton/appdev-reference-daml-standard-library-da-tuple) — 元组
* [DA.Either](/zh/docs/canton/appdev-reference-daml-standard-library-da-either) — `Either`
* [DA.Functor](/zh/docs/canton/appdev-reference-daml-standard-library-da-functor) — Functor
* [DA.Action](/zh/docs/canton/appdev-reference-daml-standard-library-da-action) — Action
* [DA.Functor](/zh/docs/canton/appdev-reference-daml-standard-library-da-functor) 与 [DA.Semigroup](/zh/docs/canton/appdev-reference-daml-standard-library-da-semigroup) — Monoid 与 Semigroup
* [DA.Text](/zh/docs/canton/appdev-reference-daml-standard-library-da-text) — `Text`
* [DA.Time](/zh/docs/canton/appdev-reference-daml-standard-library-da-time) — `Time`
* [DA.Date](/zh/docs/canton/appdev-reference-daml-standard-library-da-date) — `Date`

命名相当直观。

除 Prelude 中的类型类外，还有两个值得了解的模块，泛化你已学的概念：`Foldable` 与 `Traversable`。本章较早示例基于列表，但还有许多迭代器，由两个额外类型类表达：[DA.Traversable](/zh/docs/canton/appdev-reference-daml-standard-library-da-traversable) 与 [DA.Foldable](/zh/docs/canton/appdev-reference-daml-standard-library-da-foldable)。更多细节见 [Haskell wiki 上的 Foldable and Traversable](https://wiki.haskell.org/Foldable_and_Traversable)。

## 搜索标准库

从 [Daml 标准库参考](/zh/docs/canton/appdev-reference-daml-standard-library-index) 浏览是起点，模块命名也有帮助，但要查陌生函数含义、或找「做某事」的函数仍不够高效。

Daml 有自有 [Hoogle](https://hoogle.haskell.org/)：[Daml Hoogle](https://hoogle.daml.com)，支持按名称与签名搜索标准库。

### 按名称搜索函数

若遇到陌生函数，如 `MultiTrade` 的 `ensure` 子句中的：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Intro/Asset/MultiTrade.daml
-- [Include actual code example here]
```

或可猜 `not`、`null` 的作用，也可在文档搜索中查这些名称。标准库结果会排在前面。例如 `not`：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
not

 : Bool -> Bool

 Boolean “not”
```

签名（含类型约束）与描述通常能清楚说明函数作用。

### 按签名搜索函数

另一常见场景：已有若干值要做某操作，但不知标准库函数。在 `MultiTrade` 模板上有列表 `baseAssets`，且 ensure 子句保证非空。原 `Trade` 用 `baseAsset.owner` 作 signatory。如何在不写完整 `case` 模式匹配的情况下取列表首元以提取 `owner`？

技巧是思考所需函数签名再搜索。此处要从列表取一个 distinguished 元素，签名应为 `[a] -> a`。搜索该签名会得到多种结果，标准库仍排在前面。

浏览描述，`head` 是明显选择，如 `MultiTrade` 模板的 `let` 中所用。

可能注意到部分结果未显式出现 `[]`，例如：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
fold

  : (Foldable t, Monoid m) => t m -> m

  Combine the elements of a structure using a monoid.
```

因存在 `Foldable [a]` 的实例。

再试一次搜索。若不要首元而要索引 `n` 处的元素，记得 `functional-101` 的 `(!!)` 运算符。可搜 `[a] -> Int -> a` 或 `Int -> [a] -> a`，两种都会返回 `(!!)`，不必纠结参数顺序。

## 下一步

下一节介绍测试与交互 Daml 代码的更多选项，并讨论部分关键字的操作语义、常见失败，以及 Daml 测试中的覆盖率报告。

{/* Mintlify preview rebuild marker. */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
