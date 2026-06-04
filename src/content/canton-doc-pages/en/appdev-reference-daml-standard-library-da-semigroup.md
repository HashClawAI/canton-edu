---
title: "DA.Semigroup"
slug: "appdev-reference-daml-standard-library-da-semigroup"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-semigroup.md"
source_title: "DA.Semigroup"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-semigroup
---

# DA.Semigroup

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Semigroup

> Reference documentation for Daml module DA.Semigroup.

<span id="module-da-semigroup-27147" />

# DA.Semigroup

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

<span id="type-da-semigroup-types-max-52699" />

### `data Max a`

Semigroup under `max`

```
> Max 23 <> Max 42
Max 42
```

Constructors:

<span id="constr-da-semigroup-types-max-20326" />

* `Max a`

Instances:

* `instance Ord a => Semigroup (Max a)`
* `instance Eq a => Eq (Max a)`
* `instance Ord a => Ord (Max a)`
* `instance Show a => Show (Max a)`

<span id="type-da-semigroup-types-min-78217" />

### `data Min a`

Semigroup under `min`

```
> Min 23 <> Min 42
Min 23
```

Constructors:

<span id="constr-da-semigroup-types-min-6532" />

* `Min a`

Instances:

* `instance Ord a => Semigroup (Min a)`
* `instance Eq a => Eq (Min a)`
* `instance Ord a => Ord (Min a)`
* `instance Show a => Show (Min a)`

## Orphan Typeclass Instances

* `instance Eq a => Eq (Min a)`

* `instance Ord a => Ord (Min a)`

* `instance Show a => Show (Min a)`

* `instance Eq a => Eq (Max a)`

* `instance Ord a => Ord (Max a)`

* `instance Show a => Show (Max a)`

* `instance Ord a => Semigroup (Min a)`

* `instance Ord a => Semigroup (Max a)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
