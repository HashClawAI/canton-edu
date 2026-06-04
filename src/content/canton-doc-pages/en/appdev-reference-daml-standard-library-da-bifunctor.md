---
title: "DA.Bifunctor"
slug: "appdev-reference-daml-standard-library-da-bifunctor"
locale: "en"
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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Bifunctor

> Reference documentation for Daml module DA.Bifunctor.

<span id="module-da-bifunctor-44306" />

# DA.Bifunctor

## Module Snapshot

<CardGroup cols={2}>
  <Card title="Lifecycle">
    Stable.
  </Card>

  <Card title="Notices">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

## Typeclasses

<span id="class-da-bifunctor-bifunctor-68312" />

### `class Bifunctor p`

A bifunctor is a type constructor that takes
two type arguments and is a functor in *both* arguments. That
is, unlike with `Functor`, a type constructor such as `Either`
does not need to be partially applied for a `Bifunctor`
instance, and the methods in this class permit mapping
functions over the Left value or the `Right` value,
or both at the same time.

It is a bifunctor where both the first and second
arguments are covariant.

You can define a `Bifunctor` by either defining bimap or by
defining both first and second.

If you supply bimap, you should ensure that:

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
`bimap identity identity` ≡ `identity`
```

If you supply first and second, ensure:

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
first identity ≡ identity
second identity ≡ identity

```

If you supply both, you should also ensure:

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
bimap f g ≡ first f . second g
```

By parametricity, these will ensure that:

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}

bimap  (f . g) (h . i) ≡ bimap f h . bimap g i
first  (f . g) ≡ first  f . first  g
second (f . g) ≡ second f . second g

```

Methods:

* `bimap : (a -> b) -> (c -> d) -> p a c -> p b d`
  Map over both arguments at the same time.

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  bimap f g ≡ first f . second g
  ```

  Examples:

  ```
  >>> bimap not (+1) (True, 3)
  (False,4)

  >>> bimap not (+1) (Left True)
  Left False

  >>> bimap not (+1) (Right 3)
  Right 4
  ```
* `first : (a -> b) -> p a c -> p b c`
  Map covariantly over the first argument.

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  first f ≡ bimap f identity
  ```

  Examples:

  ```
  >>> first not (True, 3)
  (False,3)

  >>> first not (Left True : Either Bool Int)
  Left False
  ```
* `second : (b -> c) -> p a b -> p a c`
  Map covariantly over the second argument.

  ```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
  second ≡ bimap identity
  ```

  Examples:

  ```
  >>> second (+1) (True, 3)
  (True,4)

  >>> second (+1) (Right 3 : Either Bool Int)
  Right 4
  ```

Instances:

* `instance Bifunctor Either`
* `instance Bifunctor ()`
* `instance Bifunctor x1`
* `instance Bifunctor (x1, x2)`
* `instance Bifunctor (x1, x2, x3)`
* `instance Bifunctor (x1, x2, x3, x4)`
* `instance Bifunctor (x1, x2, x3, x4, x5)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
