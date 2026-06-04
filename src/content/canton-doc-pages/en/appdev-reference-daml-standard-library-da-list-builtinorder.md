---
title: "DA.List.BuiltinOrder"
slug: "appdev-reference-daml-standard-library-da-list-builtinorder"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-list-builtinorder.md"
source_title: "DA.List.BuiltinOrder"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-list-builtinorder
---

# DA.List.BuiltinOrder

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.List.BuiltinOrder

> Reference documentation for Daml module DA.List.BuiltinOrder.

<span id="module-da-list-builtinorder-49213" />

# DA.List.BuiltinOrder

Note: This is only supported in Daml-LF 1.11 or later.

This module provides variants of other standard library

functions that are based on the builtin Daml-LF ordering rather

than user-defined ordering. This is the same order also used

by `DA.Map`.

These functions are usually much more efficient than their

`Ord`-based counterparts.

Note that the functions in this module still require `Ord`

constraints. This is purely to enforce that you don’t

pass in values that cannot be compared, e.g., functions. The

implementation of those instances is not used.

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

<span id="function-da-list-builtinorder-dedup-38418" />

### `dedup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedup : Ord a => [a] -> [a]
```

`dedup l` removes duplicate elements from a list. In particular,
it keeps only the first occurrence of each element.

`dedup` is stable so the elements in the output are ordered
by their first occurrence in the input. If you do not need
stability, consider using `dedupSort` which is more efficient.

```
>>> dedup [3, 1, 1, 3]
[3, 1]
```

<span id="function-da-list-builtinorder-dedupon-23739" />

### `dedupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOn : Ord k => (v -> k) -> [v] -> [v]
```

A version of `dedup` where deduplication is done
after applying the given function. Example use: `dedupOn (.employeeNo) employees`.

`dedupOn` is stable so the elements in the output are ordered
by their first occurrence in the input. If you do not need
stability, consider using `dedupOnSort` which is more efficient.

```
>>> dedupOn fst [(3, "a"), (1, "b"), (1, "c"), (3, "d")]
[(3, "a"), (1, "b")]
```

<span id="function-da-list-builtinorder-dedupsort-5846" />

### `dedupSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSort : Ord a => [a] -> [a]
```

`dedupSort` is a more efficient variant of `dedup`
that does not preserve the order of the input elements.
Instead the output will be sorted acoording to the builtin Daml-LF
ordering.

```
>>> dedupSort [3, 1, 1, 3]
[1, 3]
```

<span id="function-da-list-builtinorder-deduponsort-69087" />

### `dedupOnSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOnSort : Ord k => (v -> k) -> [v] -> [v]
```

`dedupOnSort` is a more efficient variant of `dedupOn`
that does not preserve the order of the input elements.
Instead the output will be sorted on the values returned by the function.

For duplicates, the first element in the list will be included in the output.

```
>>> dedupOnSort fst [(3, "a"), (1, "b"), (1, "c"), (3, "d")]
[(1, "b"), (3, "a")]
```

<span id="function-da-list-builtinorder-sort-65819" />

### `sort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sort : Ord a => [a] -> [a]
```

Sort the list according to the Daml-LF ordering.

Values that are identical according to the builtin Daml-LF ordering
are indistinguishable so stability is not relevant here.

```
>>> sort [3,1,2]
[1,2,3]
```

<span id="function-da-list-builtinorder-sorton-7978" />

### `sortOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortOn : Ord b => (a -> b) -> [a] -> [a]
```

`sortOn f` is a version of sort that allows sorting
on the result of the given function.

`sortOn` is stable so elements that map to the same sort key
will be ordered by their position in the input.

```
>>> sortOn fst [(3, "a"), (1, "b"), (3, "c"), (2, "d")]
[(1, "b"), (2, "d"), (3, "a"), (3, "c")]
```

<span id="function-da-list-builtinorder-unique-2492" />

### `unique`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unique : Ord a => [a] -> Bool
```

Returns True if and only if there are no duplicate elements in the given list.

```
>>> unique [1, 2, 3]
True
```

<span id="function-da-list-builtinorder-uniqueon-93017" />

### `uniqueOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueOn : Ord k => (a -> k) -> [a] -> Bool
```

Returns True if and only if there are no duplicate elements in the given list
after applyng function.

```
>>> uniqueOn fst [(1, 2), (2, 42), (1, 3)]
False
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
