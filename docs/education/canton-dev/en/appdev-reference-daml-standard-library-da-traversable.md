---
title: "DA.Traversable"
slug: "appdev-reference-daml-standard-library-da-traversable"
locale: "en"
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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Traversable

> Reference documentation for Daml module DA.Traversable.

<span id="module-da-traversable-75075" />

# DA.Traversable

Class of data structures that can be traversed from left to right, performing an action on each element.

You typically would want to import this module qualified to avoid clashes with

functions defined in `Prelude`. Ie.:

```

import DA.Traversable   qualified as F

```

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

<span id="class-da-traversable-traversable-18144" />

### `class (Functor t, Foldable t) => Traversable t`

Functors representing data structures that can be traversed from left to right.

Methods:

* `mapA : Applicative f => (a -> f b) -> t a -> f (t b)`
  Map each element of a structure to an action, evaluate these actions
  from left to right, and collect the results.
* `sequence : Applicative f => t (f a) -> f (t a)`
  Evaluate each action in the structure from left to right, and
  collect the results.

Instances:

* `instance Ord k => Traversable (Map k)`
* `instance Traversable TextMap`
* `instance Traversable Optional`
* `instance Traversable NonEmpty`
* `instance Traversable (Validation err)`
* `instance Traversable (Either a)`
* `instance Traversable []`
* `instance Traversable a`

## Functions

<span id="function-da-traversable-fora-19271" />

### `forA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA : (Traversable t, Applicative f) => t a -> (a -> f b) -> f (t b)
```

`forA` is `mapA` with its arguments flipped.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
