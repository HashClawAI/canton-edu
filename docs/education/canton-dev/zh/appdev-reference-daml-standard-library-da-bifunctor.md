---
title: "DA.Bifunctor"
slug: "appdev-reference-daml-standard-library-da-bifunctor"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-bifunctor.md"
source_title: "DA.Bifunctor"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-bifunctor
---

# DA.Bifunctor

> Daml 标准库模块 DA.Bifunctor 参考文档。

<span id="module-da-bifunctor-44306" />

# DA.Bifunctor

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Stable.
  </Card>

  <Card title="Notices">
    状态：`active`
    引入于：`3.4.9`
    删除于：`-`
    警告：`0`
    弃用：`0`
    已弃用自：`-`
  </Card>
</CardGroup>

## 类型类

<span id="class-da-bifunctor-bifunctor-68312" />

### `class Bifunctor p`

双函子是一种类型构造函数，它采用
两个类型参数，并且是 *两个* 参数中的函子。那
与 `Functor` 不同，它是一个类型构造函数，例如 `Either`
不需要部分申请`Bifunctor`
实例，并且该类中的方法允许映射
对 Left 值或 `Right` 值起作用，
或同时两者。

它是一个双函子，其中第一个和第二个
参数是协变的。

您可以通过定义 bimap 或通过定义 `Bifunctor`
定义第一和第二。

如果您提供 bimap，您应该确保：

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
`bimap identity identity` ≡ `identity`
```

如果您提供第一个和第二个，请确保：

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
first identity ≡ identity
second identity ≡ identity

```

如果您同时提供两者，您还应该确保：

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
bimap f g ≡ first f . second g
```

通过参数化，这些将确保：

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}

bimap  (f . g) (h . i) ≡ bimap f h . bimap g i
first  (f . g) ≡ first  f . first  g
second (f . g) ≡ second f . second g

```

方法：

* `bimap : (a -> b) -> (c -> d) -> p a c -> p b d`
  同时映射两个参数。

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  bimap f g ≡ first f . second g
  ```

  示例：

  ```
  >>> bimap not (+1) (True, 3)
  (False,4)

  >>> bimap not (+1) (Left True)
  Left False

  >>> bimap not (+1) (Right 3)
  Right 4
  ```
* `first : (a -> b) -> p a c -> p b c`
  对第一个参数进行协变映射。

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  first f ≡ bimap f identity
  ```

  示例：

  ```
  >>> first not (True, 3)
  (False,3)

  >>> first not (Left True : Either Bool Int)
  Left False
  ```
* `second : (b -> c) -> p a b -> p a c`
  对第二个参数进行协变映射。

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  second ≡ bimap identity
  ```

  示例：

  ```
  >>> second (+1) (True, 3)
  (True,4)

  >>> second (+1) (Right 3 : Either Bool Int)
  Right 4
  ```

实例：

* `instance Bifunctor Either`
* `instance Bifunctor ()`
* `instance Bifunctor x1`
* `instance Bifunctor (x1, x2)`
* `instance Bifunctor (x1, x2, x3)`
* `instance Bifunctor (x1, x2, x3, x4)`
* `instance Bifunctor (x1, x2, x3, x4, x5)`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
