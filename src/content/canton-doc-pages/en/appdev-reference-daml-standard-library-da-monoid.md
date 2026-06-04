---
title: "DA.Monoid"
slug: "appdev-reference-daml-standard-library-da-monoid"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-monoid.md"
source_title: "DA.Monoid"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-monoid
---

# DA.Monoid

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Monoid

> Reference documentation for Daml module DA.Monoid.

<span id="module-da-monoid-95505" />

# DA.Monoid

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

<span id="type-da-monoid-types-all-38142" />

### `data All`

Boolean monoid under conjunction (&&)

Constructors:

<span id="constr-da-monoid-types-all-18981" />

* `All`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAll | Bool |  |

Instances:

* `instance Monoid All`
* `instance Semigroup All`
* `instance GetField getAll All Bool`
* `instance SetField getAll All Bool`
* `instance Eq All`
* `instance Ord All`
* `instance Show All`

<span id="type-da-monoid-types-any-3989" />

### `data Any`

Boolean Monoid under disjunction (||)

Constructors:

<span id="constr-da-monoid-types-any-54474" />

* `Any`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAny | Bool |  |

Instances:

* `instance Monoid Any`
* `instance Semigroup Any`
* `instance GetField getAny Any Bool`
* `instance SetField getAny Any Bool`
* `instance Eq Any`
* `instance Ord Any`
* `instance Show Any`

<span id="type-da-monoid-types-endo-95420" />

### `data Endo a`

The monoid of endomorphisms under composition.

Constructors:

<span id="constr-da-monoid-types-endo-7873" />

* `Endo`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| appEndo | a -> a |  |

Instances:

* `instance Monoid (Endo a)`
* `instance Semigroup (Endo a)`
* `instance GetField appEndo (Endo a) (a -> a)`
* `instance SetField appEndo (Endo a) (a -> a)`

<span id="type-da-monoid-types-product-66754" />

### `data Product a`

Monoid under (\*)

```
> Product 2 <> Product 3
Product 6
```

Constructors:

<span id="constr-da-monoid-types-product-4241" />

* `Product a`

Instances:

* `instance Multiplicative a => Monoid (Product a)`
* `instance Multiplicative a => Semigroup (Product a)`
* `instance Eq a => Eq (Product a)`
* `instance Ord a => Ord (Product a)`
* `instance Additive a => Additive (Product a)`
* `instance Multiplicative a => Multiplicative (Product a)`
* `instance Show a => Show (Product a)`

<span id="type-da-monoid-types-sum-76394" />

### `data Sum a`

Monoid under (+)

```
> Sum 1 <> Sum 2
Sum 3
```

Constructors:

<span id="constr-da-monoid-types-sum-82289" />

* `Sum a`

Instances:

* `instance Additive a => Monoid (Sum a)`
* `instance Additive a => Semigroup (Sum a)`
* `instance Eq a => Eq (Sum a)`
* `instance Ord a => Ord (Sum a)`
* `instance Additive a => Additive (Sum a)`
* `instance Multiplicative a => Multiplicative (Sum a)`
* `instance Show a => Show (Sum a)`

## Orphan Typeclass Instances

* `instance Eq All`

* `instance Ord All`

* `instance Show All`

* `instance Eq Any`

* `instance Ord Any`

* `instance Show Any`

* `instance Eq a => Eq (Sum a)`

* `instance Ord a => Ord (Sum a)`

* `instance Show a => Show (Sum a)`

* `instance Additive a => Additive (Sum a)`

* `instance Multiplicative a => Multiplicative (Sum a)`

* `instance Eq a => Eq (Product a)`

* `instance Ord a => Ord (Product a)`

* `instance Show a => Show (Product a)`

* `instance Additive a => Additive (Product a)`

* `instance Multiplicative a => Multiplicative (Product a)`

* `instance Semigroup All`

* `instance Monoid All`

* `instance Semigroup Any`

* `instance Monoid Any`

* `instance Semigroup (Endo a)`

* `instance Monoid (Endo a)`

* `instance Additive a => Semigroup (Sum a)`

* `instance Additive a => Monoid (Sum a)`

* `instance Multiplicative a => Semigroup (Product a)`

* `instance Multiplicative a => Monoid (Product a)`

* `instance GetField getAll All Bool`

* `instance SetField getAll All Bool`

* `instance GetField getAny Any Bool`

* `instance SetField getAny Any Bool`

* `instance GetField appEndo (Endo a) (a -> a)`

* `instance SetField appEndo (Endo a) (a -> a)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
