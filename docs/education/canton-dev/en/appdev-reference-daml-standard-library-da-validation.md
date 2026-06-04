---
title: "DA.Validation"
slug: "appdev-reference-daml-standard-library-da-validation"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-validation.md"
source_title: "DA.Validation"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-validation
---

# DA.Validation

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Validation

> Reference documentation for Daml module DA.Validation.

<span id="module-da-validation-69700" />

# DA.Validation

`Validation` type and associated functions.

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

<span id="type-da-validation-types-validation-39644" />

### `data Validation err a`

A `Validation` represents eithor a non-empty list of errors, or a successful value.
This generalizes `Either` to allow more than one error to be collected.

Constructors:

<span id="constr-da-validation-types-errors-73825" />

* `Errors (NonEmpty err)`

<span id="constr-da-validation-types-success-12286" />

* `Success a`

Instances:

* `instance Foldable (Validation err)`
* `instance Applicative (Validation err)`
* `instance Semigroup (Validation err a)`
* `instance Traversable (Validation err)`
* `instance Functor (Validation err)`
* `instance (Eq err, Eq a) => Eq (Validation err a)`
* `instance (Show err, Show a) => Show (Validation err a)`

## Functions

<span id="function-da-validation-invalid-71114" />

### `invalid`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
invalid : err -> Validation err a
```

Fail for the given reason.

<span id="function-da-validation-ok-57346" />

### `ok`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ok : a -> Validation err a
```

Succeed with the given value.

<span id="function-da-validation-validate-15676" />

### `validate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
validate : Either err a -> Validation err a
```

Turn an `Either` into a `Validation`.

<span id="function-da-validation-run-73024" />

### `run`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
run : Validation err a -> Either (NonEmpty err) a
```

Convert a `Validation err a` value into an `Either`,
taking the non-empty list of errors as the left value.

<span id="function-da-validation-run1-16566" />

### `run1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
run1 : Validation err a -> Either err a
```

Convert a `Validation err a` value into an `Either`,
taking just the first error as the left value.

<span id="function-da-validation-runwithdefault-81974" />

### `runWithDefault`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
runWithDefault : a -> Validation err a -> a
```

Run a `Validation err a` with a default value in case of errors.

<span id="function-da-validation-ltwhatgt-24976" />

### `<?>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<?> : Optional b -> err -> Validation err b
```

Convert an `Optional t` into a `Validation err t`, or
more generally into an `m t` for any `ActionFail` type `m`.

## Orphan Typeclass Instances

* `instance (Eq err, Eq a) => Eq (Validation err a)`

* `instance (Show err, Show a) => Show (Validation err a)`

* `instance Functor (Validation err)`

* `instance Applicative (Validation err)`

* `instance Semigroup (Validation err a)`

* `instance Foldable (Validation err)`

* `instance Traversable (Validation err)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
