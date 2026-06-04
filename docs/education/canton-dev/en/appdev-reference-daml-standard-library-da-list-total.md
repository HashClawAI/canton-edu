---
title: "DA.List.Total"
slug: "appdev-reference-daml-standard-library-da-list-total"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-list-total.md"
source_title: "DA.List.Total"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-list-total
---

# DA.List.Total

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.List.Total

> Reference documentation for Daml module DA.List.Total.

<span id="module-da-list-total-99663" />

# DA.List.Total

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

<span id="function-da-list-total-head-26095" />

### `head`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
head : [a] -> Optional a
```

Return the first element of a list. Return `None` if list is empty.

<span id="function-da-list-total-tail-49055" />

### `tail`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tail : [a] -> Optional [a]
```

Return all but the first element of a list. Return `None` if list is empty.

<span id="function-da-list-total-last-22829" />

### `last`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
last : [a] -> Optional a
```

Extract the last element of a list. Returns `None` if list is empty.

<span id="function-da-list-total-init-12739" />

### `init`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
init : [a] -> Optional [a]
```

Return all the elements of a list except the last one. Returns `None` if list is empty.

<span id="function-da-list-total-bangbang-57917" />

### `!!`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
!! : [a] -> Int -> Optional a
```

Return the nth element of a list. Return `None` if index is out of bounds.

<span id="function-da-list-total-foldl1-27683" />

### `foldl1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1 : (a -> a -> a) -> [a] -> Optional a
```

Fold left starting with the head of the list.
For example, `foldl1 f [a,b,c] = f (f a b) c`.
Return `None` if list is empty.

<span id="function-da-list-total-foldr1-3777" />

### `foldr1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1 : (a -> a -> a) -> [a] -> Optional a
```

Fold right starting with the last element of the list.
For example, `foldr1 f [a,b,c] = f a (f b c)`

<span id="function-da-list-total-foldbalanced1-85298" />

### `foldBalanced1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldBalanced1 : (a -> a -> a) -> [a] -> Optional a
```

Fold a non-empty list in a balanced way. Balanced means that each
element has approximately the same depth in the operator
tree. Approximately the same depth means that the difference
between maximum and minimum depth is at most 1. The accumulation
operation must be associative and commutative in order to get the
same result as `foldl1` or `foldr1`.

Return `None` if list is empty.

<span id="function-da-list-total-minimumby-50223" />

### `minimumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumBy : (a -> a -> Ordering) -> [a] -> Optional a
```

Return the least element of a list according to the given comparison function.
Return `None` if list  is empty.

<span id="function-da-list-total-maximumby-35485" />

### `maximumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumBy : (a -> a -> Ordering) -> [a] -> Optional a
```

Return the greatest element of a list according to the given comparison function.
Return `None` if list is empty.

<span id="function-da-list-total-minimumon-58803" />

### `minimumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumOn : Ord k => (a -> k) -> [a] -> Optional a
```

Return the least element of a list when comparing by a key function.
For example `minimumOn (\(x,y) -> x + y) [(1,2), (2,0)] == Some (2,0)`.
Return `None` if list is empty.

<span id="function-da-list-total-maximumon-82285" />

### `maximumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumOn : Ord k => (a -> k) -> [a] -> Optional a
```

Return the greatest element of a list when comparing by a key function.
For example `maximumOn (\(x,y) -> x + y) [(1,2), (2,0)] == Some (1,2)`.
Return `None` if list is empty.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
