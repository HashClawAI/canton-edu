---
title: "DA.Numeric"
slug: "appdev-reference-daml-standard-library-da-numeric"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-numeric.md"
source_title: "DA.Numeric"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-numeric
---

# DA.Numeric

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Numeric

> Reference documentation for Daml module DA.Numeric.

<span id="module-da-numeric-17471" />

# DA.Numeric

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

<span id="type-da-numeric-roundingmode-53864" />

### `data RoundingMode`

Rounding modes.

Constructors:

<span id="constr-da-numeric-roundingup-99831" />

* `RoundingUp`
  Round away from zero.

<span id="constr-da-numeric-roundingdown-63242" />

* `RoundingDown`
  Round towards zero.

<span id="constr-da-numeric-roundingceiling-67218" />

* `RoundingCeiling`
  Round towards positive infinity.

<span id="constr-da-numeric-roundingfloor-71675" />

* `RoundingFloor`
  Round towards negative infinity.

<span id="constr-da-numeric-roundinghalfup-22532" />

* `RoundingHalfUp`
  Round towards the nearest neighbor unless both neighbors
  are equidistant, in which case round away from zero.

<span id="constr-da-numeric-roundinghalfdown-91305" />

* `RoundingHalfDown`
  Round towards the nearest neighbor unless both neighbors
  are equidistant, in which case round towards zero.

<span id="constr-da-numeric-roundinghalfeven-70729" />

* `RoundingHalfEven`
  Round towards the nearest neighbor unless both neighbors
  are equidistant, in which case round towards the even neighbor.

<span id="constr-da-numeric-roundingunnecessary-42017" />

* `RoundingUnnecessary`
  Do not round. Raises an error if the result cannot
  be represented without rounding at the targeted scale.

## Functions

<span id="function-da-numeric-mul-81896" />

### `mul`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mul : NumericScale n3 => Numeric n1 -> Numeric n2 -> Numeric n3
```

Multiply two numerics. Both inputs and the output may have
different scales, unlike `(*)` which forces all numeric scales
to be the same. Raises an error on overflow, rounds to chosen
scale otherwise.

<span id="function-da-numeric-div-56407" />

### `div`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
div : NumericScale n3 => Numeric n1 -> Numeric n2 -> Numeric n3
```

Divide two numerics. Both inputs and the output may have
different scales, unlike `(/)` which forces all numeric scales
to be the same. Raises an error on overflow, rounds to chosen
scale otherwise.

<span id="function-da-numeric-cast-54256" />

### `cast`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
cast : NumericScale n2 => Numeric n1 -> Numeric n2
```

Cast a Numeric. Raises an error on overflow or loss of precision.

<span id="function-da-numeric-castandround-59941" />

### `castAndRound`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
castAndRound : NumericScale n2 => Numeric n1 -> Numeric n2
```

Cast a Numeric. Raises an error on overflow, rounds to chosen
scale otherwise.

<span id="function-da-numeric-shift-13796" />

### `shift`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
shift : NumericScale n2 => Numeric n1 -> Numeric n2
```

Move the decimal point left or right by multiplying the numeric
value by 10^(n1 - n2). Does not overflow or underflow.

<span id="function-da-numeric-pi-88702" />

### `pi`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
pi : NumericScale n => Numeric n
```

The number pi.

<span id="function-da-numeric-epsilon-3092" />

### `epsilon`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
epsilon : NumericScale n => Numeric n
```

The minimum strictly positive value that can be represented by a numeric of scale `n`.

<span id="function-da-numeric-roundnumeric-41344" />

### `roundNumeric`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
roundNumeric : NumericScale n => Int -> RoundingMode -> Numeric n -> Numeric n
```

Round a `Numeric` number. The value of `round n r a` is the value
of `a` rounded to `n` decimal places (i.e. scale), according to the rounding
mode `r`.

This will fail when using the `RoundingUnnecessary` mode for a number that cannot
be represented exactly with at most `n` decimal places.

## Orphan Typeclass Instances

* `instance NumericScale n => Bounded (Numeric n)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
