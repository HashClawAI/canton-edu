---
title: "DA.Set"
slug: "appdev-reference-daml-standard-library-da-set"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-set.md"
source_title: "DA.Set"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-set
---

# DA.Set

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Set

> Reference documentation for Daml module DA.Set.

<span id="module-da-set-6124" />

# DA.Set

Note: This is only supported in Daml-LF 1.11 or later.

This module exports the generic set type `Set k` and associated

functions. This module should be imported qualified, for example:

```

import DA.Set (Set)

import DA.Set qualified as S

```

This will give access to the `Set` type, and the various operations

as `S.lookup`, `S.insert`, `S.fromList`, etc.

`Set k` internally uses the built-in order for the type `k`.

This means that keys that contain functions are not comparable

and will result in runtime errors. To prevent this, the `Ord k`

instance is required for most set operations. It is recommended to

only use `Set k` for key types that have an `Ord k` instance

that is derived automatically using `deriving`:

```

data K = ...

deriving (Eq, Ord)

```

This includes all built-in types that aren't function types, such as

`Int`, `Text`, `Bool`, `(a, b)` assuming `a` and `b` have default

`Ord` instances, `Optional t` and `[t]` assuming `t` has a

default `Ord` instance, `Map k v` assuming `k` and `v` have

default `Ord` instances, and `Set k` assuming `k` has a

default `Ord` instance.

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

## Data Types

<span id="type-da-set-types-set-90436" />

### `data Set k`

The type of a set. This is a wrapper over the `Map` type.

Constructors:

<span id="constr-da-set-types-set-78105" />

* `Set`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| map | Map k () |  |

Instances:

* `instance Foldable Set`
* `instance Ord k => Monoid (Set k)`
* `instance Ord k => Semigroup (Set k)`
* `instance GetField map (Set k) (Map k ())`
* `instance SetField map (Set k) (Map k ())`
* `instance IsParties (Set Party)`
* `instance Ord k => Eq (Set k)`
* `instance Ord k => Ord (Set k)`
* `instance (Ord k, Show k) => Show (Set k)`

## Functions

<span id="function-da-set-empty-19742" />

### `empty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
empty : Set k
```

The empty set.

<span id="function-da-set-size-6437" />

### `size`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
size : Set k -> Int
```

The number of elements in the set.

<span id="function-da-set-tolist-26355" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : Set k -> [k]
```

Convert the set to a list of elements.

<span id="function-da-set-fromlist-9190" />

### `fromList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromList : Ord k => [k] -> Set k
```

Create a set from a list of elements.

<span id="function-da-set-tomap-37614" />

### `toMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toMap : Set k -> Map k ()
```

Convert a `Set` into a `Map`.

<span id="function-da-set-frommap-15501" />

### `fromMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromMap : Map k () -> Set k
```

Create a `Set` from a `Map`.

<span id="function-da-set-member-75542" />

### `member`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
member : Ord k => k -> Set k -> Bool
```

Is the element in the set?

<span id="function-da-set-notmember-79044" />

### `notMember`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
notMember : Ord k => k -> Set k -> Bool
```

Is the element not in the set?
`notMember k s` is equivalent to `not (member k s)`.

<span id="function-da-set-null-99389" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : Set k -> Bool
```

Is this the empty set?

<span id="function-da-set-insert-58479" />

### `insert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insert : Ord k => k -> Set k -> Set k
```

Insert an element in a set. If the set already contains the
element, this returns the set unchanged.

<span id="function-da-set-filter-76182" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : Ord k => (k -> Bool) -> Set k -> Set k
```

Filter all elements that satisfy the predicate.

<span id="function-da-set-delete-52281" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Ord k => k -> Set k -> Set k
```

Delete an element from a set.

<span id="function-da-set-singleton-15574" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : Ord k => k -> Set k
```

Create a singleton set.

<span id="function-da-set-union-79876" />

### `union`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
union : Ord k => Set k -> Set k -> Set k
```

The union of two sets.

<span id="function-da-set-intersection-70017" />

### `intersection`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intersection : Ord k => Set k -> Set k -> Set k
```

The intersection of two sets.

<span id="function-da-set-difference-68545" />

### `difference`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
difference : Ord k => Set k -> Set k -> Set k
```

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
`difference x y` returns the set consisting of all
elements in `x` that are not in `y`.

>>> fromList [1, 2, 3] `difference` fromList [1, 4]
fromList [2, 3]
```

<span id="function-da-set-issubsetof-34493" />

### `isSubsetOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSubsetOf : Ord k => Set k -> Set k -> Bool
```

`isSubsetOf a b` returns true if `a` is a subset of `b`,
that is, if every element of `a` is in `b`.

<span id="function-da-set-ispropersubsetof-90093" />

### `isProperSubsetOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isProperSubsetOf : Ord k => Set k -> Set k -> Bool
```

`isProperSubsetOf a b` returns true if `a` is a proper subset of `b`.
That is, if `a` is a subset of `b` but not equal to `b`.

## Orphan Typeclass Instances

* `instance Ord k => Eq (Set k)`

* `instance Ord k => Ord (Set k)`

* `instance (Ord k, Show k) => Show (Set k)`

* `instance IsParties (Set Party)`

* `instance Ord k => Semigroup (Set k)`

* `instance Ord k => Monoid (Set k)`

* `instance GetField map (Set k) (Map k ())`

* `instance SetField map (Set k) (Map k ())`

* `instance Foldable Set`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
