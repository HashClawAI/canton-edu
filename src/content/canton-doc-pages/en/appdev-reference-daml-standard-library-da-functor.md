---
title: "DA.Functor"
slug: "appdev-reference-daml-standard-library-da-functor"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-functor.md"
source_title: "DA.Functor"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-functor
---

# DA.Functor

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Functor

> Reference documentation for Daml module DA.Functor.

<span id="module-da-functor-63823" />

# DA.Functor

The `Functor` class is used for types that can be mapped over.

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

## Functions

<span id="function-da-functor-dollargt-48161" />

### `$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
$> : Functor f => f a -> b -> f b
```

Replace all locations in the input (on the left) with the given
value (on the right).

<span id="function-da-functor-ltampgt-91298" />

### `<&>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<&> : Functor f => f a -> (a -> b) -> f b
```

Map a function over a functor. Given a value `as` and a function
`f`, `as <&> f` is `f <$> as`. That is, `<&>` is like `<$>` but the
arguments are in reverse order.

<span id="function-da-functor-ltdollardollargt-89503" />

### `<$$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<$$> : (Functor f, Functor g) => (a -> b) -> g (f a) -> g (f b)
```

Nested `<$>`.

<span id="function-da-functor-void-91123" />

### `void`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
void : Functor f => f a -> f ()
```

Replace all the locations in the input with `()`.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
