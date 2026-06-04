---
title: "DA.NonEmpty"
slug: "appdev-reference-daml-standard-library-da-nonempty"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-nonempty.md"
source_title: "DA.NonEmpty"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-nonempty
---

# DA.NonEmpty

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.NonEmpty

> Reference documentation for Daml module DA.NonEmpty.

<span id="module-da-nonempty-15701" />

# DA.NonEmpty

Type and functions for non-empty lists. This module re-exports many functions with

the same name as prelude list functions, so it is expected to import the module qualified.

For example, with the following import list you will have access to the `NonEmpty` type

and any functions on non-empty lists will be qualified, for example as `NE.append, NE.map, NE.foldl`:

```

import DA.NonEmpty (NonEmpty)

import qualified DA.NonEmpty as NE

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

## Functions

<span id="function-da-nonempty-cons-63704" />

### `cons`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
cons : a -> NonEmpty a -> NonEmpty a
```

Prepend an element to a non-empty list.

<span id="function-da-nonempty-append-34337" />

### `append`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
append : NonEmpty a -> NonEmpty a -> NonEmpty a
```

Append or concatenate two non-empty lists.

<span id="function-da-nonempty-map-69362" />

### `map`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
map : (a -> b) -> NonEmpty a -> NonEmpty b
```

Apply a function over each element in the non-empty list.

<span id="function-da-nonempty-nonempty-24939" />

### `nonEmpty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonEmpty : [a] -> Optional (NonEmpty a)
```

Turn a list into a non-empty list, if possible. Returns
`None` if the input list is empty, and `Some` otherwise.

<span id="function-da-nonempty-singleton-99101" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : a -> NonEmpty a
```

A non-empty list with a single element.

<span id="function-da-nonempty-tolist-15474" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : NonEmpty a -> [a]
```

Turn a non-empty list into a list (by forgetting that it is not empty).

<span id="function-da-nonempty-reverse-64050" />

### `reverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverse : NonEmpty a -> NonEmpty a
```

Reverse a non-empty list.

<span id="function-da-nonempty-find-73910" />

### `find`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
find : (a -> Bool) -> NonEmpty a -> Optional a
```

Find an element in a non-empty list.

<span id="function-da-nonempty-deleteby-6333" />

### `deleteBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
deleteBy : (a -> a -> Bool) -> a -> NonEmpty a -> [a]
```

The 'deleteBy' function behaves like 'delete', but takes a
user-supplied equality predicate.

<span id="function-da-nonempty-delete-59160" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Eq a => a -> NonEmpty a -> [a]
```

Remove the first occurence of x from the non-empty list, potentially
removing all elements.

<span id="function-da-nonempty-foldl1-17561" />

### `foldl1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1 : (a -> a -> a) -> NonEmpty a -> a
```

Apply a function repeatedly to pairs of elements from a non-empty list,
from the left. For example, `foldl1 (+) (NonEmpty 1 [2,3,4]) = ((1 + 2) + 3) + 4`.

<span id="function-da-nonempty-foldr1-43627" />

### `foldr1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1 : (a -> a -> a) -> NonEmpty a -> a
```

Apply a function repeatedly to pairs of elements from a non-empty list,
from the right. For example, `foldr1 (+) (NonEmpty 1 [2,3,4]) = 1 + (2 + (3 + 4))`.

<span id="function-da-nonempty-foldr-65043" />

### `foldr`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr : (a -> b -> b) -> b -> NonEmpty a -> b
```

Apply a function repeatedly to pairs of elements from a non-empty list,
from the right, with a given initial value. For example,
`foldr (+) 0 (NonEmpty 1 [2,3,4]) = 1 + (2 + (3 + (4 + 0)))`.

<span id="function-da-nonempty-foldra-91227" />

### `foldrA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldrA : Action m => (a -> b -> m b) -> b -> NonEmpty a -> m b
```

The same as `foldr` but running an action each time.

<span id="function-da-nonempty-foldr1a-13463" />

### `foldr1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1A : Action m => (a -> a -> m a) -> NonEmpty a -> m a
```

The same as `foldr1` but running an action each time.

<span id="function-da-nonempty-foldl-91113" />

### `foldl`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl : (b -> a -> b) -> b -> NonEmpty a -> b
```

Apply a function repeatedly to pairs of elements from a non-empty list,
from the left, with a given initial value. For example,
`foldl (+) 0 (NonEmpty 1 [2,3,4]) = (((0 + 1) + 2) + 3) + 4`.

<span id="function-da-nonempty-foldla-69961" />

### `foldlA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldlA : Action m => (b -> a -> m b) -> b -> NonEmpty a -> m b
```

The same as `foldl` but running an action each time.

<span id="function-da-nonempty-foldl1a-63665" />

### `foldl1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1A : Action m => (a -> a -> m a) -> NonEmpty a -> m a
```

The same as `foldl1` but running an action each time.

## Orphan Typeclass Instances

* `instance Eq a => Eq (NonEmpty a)`

* `instance Show a => Show (NonEmpty a)`

* `instance Ord a => Ord (NonEmpty a)`

* `instance GetField hd (NonEmpty a) a`

* `instance SetField hd (NonEmpty a) a`

* `instance GetField tl (NonEmpty a) [a]`

* `instance SetField tl (NonEmpty a) [a]`

* `instance Semigroup (NonEmpty a)`

* `instance Functor NonEmpty`

* `instance Applicative NonEmpty`

* `instance Action NonEmpty`

* `instance Foldable NonEmpty`

* `instance Traversable NonEmpty`

* `instance IsParties (NonEmpty Party)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
