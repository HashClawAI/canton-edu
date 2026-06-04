---
title: "DA.Math"
slug: "appdev-reference-daml-standard-library-da-math"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-math.md"
source_title: "DA.Math"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-math
---

# DA.Math

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Math

> Reference documentation for Daml module DA.Math.

<span id="module-da-math-30023" />

# DA.Math

Math - Utility Math functions for `Decimal`

The this library is designed to give good precision, typically giving 9 correct decimal places.

The numerical algorithms run with many iterations to achieve that precision and are interpreted

by the Daml runtime so they are not performant. Their use is not advised in performance critical

contexts.

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

<span id="function-da-math-starstar-89123" />

### `**`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
** : Decimal -> Decimal -> Decimal
```

Take a power of a number Example: `2.0 ** 3.0 == 8.0`.

<span id="function-da-math-sqrt-24467" />

### `sqrt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sqrt : Decimal -> Decimal
```

Calculate the square root of a Decimal.

```
>>> sqrt 1.44
1.2
```

<span id="function-da-math-exp-84235" />

### `exp`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exp : Decimal -> Decimal
```

The exponential function. Example: `exp 0.0 == 1.0`

<span id="function-da-math-log-52192" />

### `log`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
log : Decimal -> Decimal
```

The natural logarithm. Example: `log 10.0 == 2.30258509299`

<span id="function-da-math-logbase-64267" />

### `logBase`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
logBase : Decimal -> Decimal -> Decimal
```

The logarithm of a number to a given base. Example: `log 10.0 100.0 == 2.0`

<span id="function-da-math-sin-61636" />

### `sin`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sin : Decimal -> Decimal
```

`sin` is the sine function

<span id="function-da-math-cos-82859" />

### `cos`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
cos : Decimal -> Decimal
```

`cos` is the cosine function

<span id="function-da-math-tan-54959" />

### `tan`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tan : Decimal -> Decimal
```

`tan` is the tangent function

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
