---
title: "DA.Map"
slug: "appdev-reference-daml-standard-library-da-map"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-map.md"
source_title: "DA.Map"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-map
---

# DA.Map

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Map

> Reference documentation for Daml module DA.Map.

<span id="module-da-map-69618" />

# DA.Map

Note: This is only supported in Daml-LF 1.11 or later.

This module exports the generic map type `Map k v` and associated

functions. This module should be imported qualified, for example:

```

import DA.Map (Map)

import DA.Map qualified as M

```

This will give access to the `Map` type, and the various operations

as `M.lookup`, `M.insert`, `M.fromList`, etc.

`Map k v` internally uses the built-in order for the type `k`.

This means that keys that contain functions are not comparable

and will result in runtime errors. To prevent this, the `Ord k`

instance is required for most map operations. It is recommended to

only use `Map k v` for key types that have an `Ord k` instance

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

## Functions

<span id="function-da-map-fromlist-23400" />

### `fromList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromList : Ord k => [(k, v)] -> Map k v
```

Create a map from a list of key/value pairs.

<span id="function-da-map-fromlistwithl-71603" />

### `fromListWithL`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithL : Ord k => (v -> v -> v) -> [(k, v)] -> Map k v
```

Create a map from a list of key/value pairs with a combining
function. The combining function is only used when a key appears multiple
times in the list and it takes two arguments: the first one is the new value
being inserted at that key and the second one is the value accumulated so
far at that key.
Examples:

```
>>> fromListWithL (++) [("A", [1]), ("A", [2]), ("B", [2]), ("B", [1]), ("A", [3])]
fromList [("A", [3, 2, 1]), ("B", [1, 2])]
>>> fromListWithL (++) [] == (empty : Map Text [Int])
True
```

<span id="function-da-map-fromlistwithr-67193" />

### `fromListWithR`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithR : Ord k => (v -> v -> v) -> [(k, v)] -> Map k v
```

Create a map from a list of key/value pairs like `fromListWithL`
with the combining function flipped. Examples:

```
>>> fromListWithR (++) [("A", [1]), ("A", [2]), ("B", [2]), ("B", [1]), ("A", [3])]
fromList [("A", [1, 2, 3]), ("B", [2, 1])]
>>> fromListWithR (++) [] == (empty : Map Text [Int])
True
```

<span id="function-da-map-fromlistwith-28620" />

### `fromListWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWith : Ord k => (v -> v -> v) -> [(k, v)] -> Map k v
```

<span id="function-da-map-keys-97544" />

### `keys`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
keys : Map k v -> [k]
```

Get the list of keys in the map. Keys are sorted according to the
built-in order for the type `k`, which matches the `Ord k` instance
when using `deriving Ord`.

```
>>> keys (fromList [("A", 1), ("C", 3), ("B", 2)])
["A", "B", "C"]
```

<span id="function-da-map-values-1656" />

### `values`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
values : Map k v -> [v]
```

Get the list of values in the map. These will be in the same order as
their respective keys from `M.keys`.

```
>>> values (fromList [("A", 1), ("B", 2)])
[1, 2]
```

<span id="function-da-map-tolist-88193" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : Map k v -> [(k, v)]
```

Convert the map to a list of key/value pairs. These will be ordered
by key, as in `M.keys`.

<span id="function-da-map-empty-15540" />

### `empty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
empty : Map k v
```

The empty map.

<span id="function-da-map-size-29495" />

### `size`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
size : Map k v -> Int
```

Number of elements in the map.

<span id="function-da-map-null-81379" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : Map k v -> Bool
```

Is the map empty?

<span id="function-da-map-lookup-19256" />

### `lookup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookup : Ord k => k -> Map k v -> Optional v
```

Lookup the value at a key in the map.

<span id="function-da-map-member-48452" />

### `member`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
member : Ord k => k -> Map k v -> Bool
```

Is the key a member of the map?

<span id="function-da-map-filter-60004" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : Ord k => (v -> Bool) -> Map k v -> Map k v
```

Filter the `Map` using a predicate: keep only the entries where the
value satisfies the predicate.

<span id="function-da-map-filterwithkey-3168" />

### `filterWithKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filterWithKey : Ord k => (k -> v -> Bool) -> Map k v -> Map k v
```

Filter the `Map` using a predicate: keep only the entries which
satisfy the predicate.

<span id="function-da-map-delete-97567" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Ord k => k -> Map k v -> Map k v
```

Delete a key and its value from the map. When the key is not a
member of the map, the original map is returned.

<span id="function-da-map-singleton-98784" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : Ord k => k -> v -> Map k v
```

Create a singleton map.

<span id="function-da-map-insert-53601" />

### `insert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insert : Ord k => k -> v -> Map k v -> Map k v
```

Insert a new key/value pair in the map. If the key is already
present in the map, the associated value is replaced with the
supplied value.

<span id="function-da-map-insertwith-32465" />

### `insertWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insertWith : Ord k => (v -> v -> v) -> k -> v -> Map k v -> Map k v
```

Insert a new key/value pair in the map. If the key is already
present in the map, it is combined with the previous value using the given function
`f new_value old_value`.

<span id="function-da-map-alter-84047" />

### `alter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
alter : Ord k => (Optional v -> Optional v) -> k -> Map k v -> Map k v
```

Update the value in `m` at `k` with `f`, inserting or deleting as
required.  `f` will be called with either the value at `k`, or `None`
if absent; `f` can return `Some` with a new value to be inserted in
`m` (replacing the old value if there was one), or `None` to remove
any `k` association `m` may have.

Some implications of this behavior:

alter identity k = identity
alter g k . alter f k = alter (g . f) k
alter (\_ -> Some v) k = insert k v
alter (\_ -> None) = delete

<span id="function-da-map-union-90078" />

### `union`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
union : Ord k => Map k v -> Map k v -> Map k v
```

The union of two maps, preferring the first map when equal
keys are encountered.

<span id="function-da-map-unionwith-55674" />

### `unionWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unionWith : Ord k => (v -> v -> v) -> Map k v -> Map k v -> Map k v
```

The union of two maps using the combining function to merge values that
exist in both maps.

<span id="function-da-map-merge-46179" />

### `merge`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
merge : Ord k => (k -> a -> Optional c) -> (k -> b -> Optional c) -> (k -> a -> b -> Optional c) -> Map k a -> Map k b -> Map k c
```

Combine two maps, using separate functions based on whether
a key appears only in the first map, only in the second map,
or appears in both maps.

## Orphan Typeclass Instances

* `instance (Show k, Show v) => Show (Map k v)`

* `instance (Ord k, Eq v) => Eq (Map k v)`

* `instance (Ord k, Ord v) => Ord (Map k v)`

* `instance Ord k => Semigroup (Map k v)`

* `instance Ord k => Monoid (Map k v)`

* `instance Ord k => Functor (Map k)`

* `instance Ord k => Foldable (Map k)`

* `instance Ord k => Traversable (Map k)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
