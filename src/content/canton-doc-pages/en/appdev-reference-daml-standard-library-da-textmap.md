---
title: "DA.TextMap"
slug: "appdev-reference-daml-standard-library-da-textmap"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-textmap.md"
source_title: "DA.TextMap"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-textmap
---

# DA.TextMap

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.TextMap

> Reference documentation for Daml module DA.TextMap.

<span id="module-da-textmap-81719" />

# DA.TextMap

TextMap - A map is an associative array data type composed of a

collection of key/value pairs such that, each possible key appears

at most once in the collection.

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

<span id="function-da-textmap-fromlist-19033" />

### `fromList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromList : [(Text, a)] -> TextMap a
```

Create a map from a list of key/value pairs.

<span id="function-da-textmap-fromlistwithl-22912" />

### `fromListWithL`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithL : (a -> a -> a) -> [(Text, a)] -> TextMap a
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
>>> fromListWithL (++) [] == (empty : TextMap [Int])
True
```

<span id="function-da-textmap-fromlistwithr-69626" />

### `fromListWithR`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWithR : (a -> a -> a) -> [(Text, a)] -> TextMap a
```

Create a map from a list of key/value pairs like `fromListWithL`
with the combining function flipped. Examples:

```
>>> fromListWithR (++) [("A", [1]), ("A", [2]), ("B", [2]), ("B", [1]), ("A", [3])]
fromList [("A", [1, 2, 3]), ("B", [2, 1])]
>>> fromListWithR (++) [] == (empty : TextMap [Int])
True
```

<span id="function-da-textmap-fromlistwith-41741" />

### `fromListWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromListWith : (a -> a -> a) -> [(Text, a)] -> TextMap a
```

<span id="function-da-textmap-tolist-95168" />

### `toList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toList : TextMap a -> [(Text, a)]
```

Convert the map to a list of key/value pairs where the keys are
in ascending order.

<span id="function-da-textmap-empty-66187" />

### `empty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
empty : TextMap a
```

The empty map.

<span id="function-da-textmap-size-46150" />

### `size`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
size : TextMap a -> Int
```

Number of elements in the map.

<span id="function-da-textmap-null-64690" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : TextMap v -> Bool
```

Is the map empty?

<span id="function-da-textmap-lookup-87021" />

### `lookup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookup : Text -> TextMap a -> Optional a
```

Lookup the value at a key in the map.

<span id="function-da-textmap-member-14417" />

### `member`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
member : Text -> TextMap v -> Bool
```

Is the key a member of the map?

<span id="function-da-textmap-filter-317" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : (v -> Bool) -> TextMap v -> TextMap v
```

Filter the `TextMap` using a predicate: keep only the entries where the
value satisfies the predicate.

<span id="function-da-textmap-filterwithkey-64027" />

### `filterWithKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filterWithKey : (Text -> v -> Bool) -> TextMap v -> TextMap v
```

Filter the `TextMap` using a predicate: keep only the entries which
satisfy the predicate.

<span id="function-da-textmap-delete-54270" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Text -> TextMap a -> TextMap a
```

Delete a key and its value from the map. When the key is not a
member of the map, the original map is returned.

<span id="function-da-textmap-singleton-39431" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : Text -> a -> TextMap a
```

Create a singleton map.

<span id="function-da-textmap-insert-41312" />

### `insert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insert : Text -> a -> TextMap a -> TextMap a
```

Insert a new key/value pair in the map. If the key is already
present in the map, the associated value is replaced with the
supplied value.

<span id="function-da-textmap-insertwith-45464" />

### `insertWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
insertWith : (v -> v -> v) -> Text -> v -> TextMap v -> TextMap v
```

Insert a new key/value pair in the map. If the key is already
present in the map, it is combined with the previous value using the given function
`f new_value old_value`.

<span id="function-da-textmap-union-13945" />

### `union`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
union : TextMap a -> TextMap a -> TextMap a
```

The union of two maps, preferring the first map when equal
keys are encountered.

<span id="function-da-textmap-merge-26784" />

### `merge`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
merge : (Text -> a -> Optional c) -> (Text -> b -> Optional c) -> (Text -> a -> b -> Optional c) -> TextMap a -> TextMap b -> TextMap c
```

Merge two maps. `merge f g h x y` applies `f` to all key/value pairs
whose key only appears in `x`, `g` to all pairs whose key only appears
in `y` and `h` to all pairs whose key appears in both `x` and `y`.
In the end, all pairs yielding `Some` are collected as the result.

## Orphan Typeclass Instances

* `instance Show a => Show (TextMap a)`

* `instance Eq a => Eq (TextMap a)`

* `instance Ord a => Ord (TextMap a)`

* `instance Semigroup (TextMap b)`

* `instance Monoid (TextMap b)`

* `instance Functor TextMap`

* `instance Foldable TextMap`

* `instance Traversable TextMap`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
