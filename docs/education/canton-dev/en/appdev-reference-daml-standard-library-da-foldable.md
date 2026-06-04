---
title: "DA.Foldable"
slug: "appdev-reference-daml-standard-library-da-foldable"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-foldable.md"
source_title: "DA.Foldable"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-foldable
---

# DA.Foldable

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Foldable

> Reference documentation for Daml module DA.Foldable.

<span id="module-da-foldable-94882" />

# DA.Foldable

Class of data structures that can be folded to a summary value.

It's a good idea to import this module qualified to avoid clashes with

functions defined in `Prelude`. Ie.:

```

import DA.Foldable qualified as F

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

<span id="class-da-foldable-foldable-25994" />

### `class Foldable t`

Class of data structures that can be folded to a summary value.

Methods:

* `fold : Monoid m => t m -> m`
  Combine the elements of a structure using a monoid.
* `foldMap : Monoid m => (a -> m) -> t a -> m`
  Combine the elements of a structure using a monoid.
* `foldr : (a -> b -> b) -> b -> t a -> b`
  Right-associative fold of a structure.
* `foldl : (b -> a -> b) -> b -> t a -> b`
  Left-associative fold of a structure.
* `foldr1 : (a -> a -> a) -> t a -> a`
  A variant of foldr that has no base case, and thus should only be applied to non-empty structures.
* `foldl1 : (a -> a -> a) -> t a -> a`
  A variant of foldl that has no base case, and thus should only be applied to non-empty structures.
* `toList : t a -> [a]`
  List of elements of a structure, from left to right.
* `null : t a -> Bool`
  Test whether the structure is empty. The default implementation is optimized for structures that are similar to cons-lists, because there is no general way to do better.
* `length : t a -> Int`
  Returns the size/length of a finite structure as an `Int`. The default implementation is optimized for structures that are similar to cons-lists, because there is no general way to do better.
* `elem : Eq a => a -> t a -> Bool`
  Does the element occur in the structure?
* `sum : Additive a => t a -> a`
  The sum function computes the sum of the numbers of a structure.
* `product : Multiplicative a => t a -> a`
  The product function computes the product of the numbers of a structure.
* `minimum : Ord a => t a -> a`
  The least element of a non-empty structure.
* `maximum : Ord a => t a -> a`
  The largest element of a non-empty structure.

Instances:

* `instance Ord k => Foldable (Map k)`
* `instance Foldable TextMap`
* `instance Foldable Optional`
* `instance Foldable NonEmpty`
* `instance Foldable Set`
* `instance Foldable (Validation err)`
* `instance Foldable (Either a)`
* `instance Foldable []`
* `instance Foldable a`

## Functions

<span id="function-da-foldable-mapa-78745" />

### `mapA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA_ : (Foldable t, Applicative f) => (a -> f b) -> t a -> f ()
```

Map each element of a structure to an action, evaluate these
actions from left to right, and ignore the results. For a version
that doesn't ignore the results see 'DA.Traversable.mapA'.

<span id="function-da-foldable-fora-54422" />

### `forA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA_ : (Foldable t, Applicative f) => t a -> (a -> f b) -> f ()
```

'for\_' is 'mapA\_' with its arguments flipped. For a version
that doesn't ignore the results see 'DA.Traversable.forA'.

<span id="function-da-foldable-form-34370" />

### `forM_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forM_ : (Foldable t, Applicative f) => t a -> (a -> f b) -> f ()
```

<span id="function-da-foldable-sequence-26917" />

### `sequence_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequence_ : (Foldable t, Action m) => t (m a) -> m ()
```

Evaluate each action in the structure from left to right,
and ignore the results. For a version that doesn't ignore the
results see 'DA.Traversable.sequence'.

<span id="function-da-foldable-concat-71538" />

### `concat`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concat : Foldable t => t [a] -> [a]
```

The concatenation of all the elements of a container of lists.

<span id="function-da-foldable-and-52214" />

### `and`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
and : Foldable t => t Bool -> Bool
```

`and` returns the conjunction of a container of Bools. For the result to be `True`, the container must be finite; `False`, however, results from a `False` value finitely far from the left end.

<span id="function-da-foldable-or-15333" />

### `or`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
or : Foldable t => t Bool -> Bool
```

`or` returns the disjunction of a container of Bools. For the result to be `False`, the container must be finite; `True`, however, results from a `True` value finitely far from the left end.

<span id="function-da-foldable-any-93587" />

### `any`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
any : Foldable t => (a -> Bool) -> t a -> Bool
```

Determines whether any element of the structure satisfies the predicate.

<span id="function-da-foldable-all-59560" />

### `all`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
all : Foldable t => (a -> Bool) -> t a -> Bool
```

Determines whether all elements of the structure satisfy the predicate.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
