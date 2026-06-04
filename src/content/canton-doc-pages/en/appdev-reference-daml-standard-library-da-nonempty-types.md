---
title: "DA.NonEmpty.Types"
slug: "appdev-reference-daml-standard-library-da-nonempty-types"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-nonempty-types.md"
source_title: "DA.NonEmpty.Types"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-nonempty-types
---

# DA.NonEmpty.Types

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.NonEmpty.Types

> Reference documentation for Daml module DA.NonEmpty.Types.

<span id="module-da-nonempty-types-38464" />

# DA.NonEmpty.Types

This module contains the type for non-empty lists so we can give it a stable package id.

This is reexported from DA.NonEmpty so you should never need to import this module.

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

<span id="type-da-nonempty-types-nonempty-16010" />

### `data NonEmpty a`

`NonEmpty` is the type of non-empty lists. In other words, it is the type of lists
that always contain at least one element. If `x` is a non-empty list, you can obtain
the first element with `x.hd` and the rest of the list with `x.tl`.

Constructors:

<span id="constr-da-nonempty-types-nonempty-68983" />

* `NonEmpty`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| hd | a |  |
  \| tl | \[a] |  |

Instances:

* `instance Foldable NonEmpty`
* `instance Action NonEmpty`
* `instance Applicative NonEmpty`
* `instance Semigroup (NonEmpty a)`
* `instance GetField hd (NonEmpty a) a`
* `instance GetField tl (NonEmpty a) [a]`
* `instance SetField hd (NonEmpty a) a`
* `instance SetField tl (NonEmpty a) [a]`
* `instance IsParties (NonEmpty Party)`
* `instance Traversable NonEmpty`
* `instance Functor NonEmpty`
* `instance Eq a => Eq (NonEmpty a)`
* `instance Ord a => Ord (NonEmpty a)`
* `instance Show a => Show (NonEmpty a)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
