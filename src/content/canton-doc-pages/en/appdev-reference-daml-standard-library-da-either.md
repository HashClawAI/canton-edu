---
title: "DA.Either"
slug: "appdev-reference-daml-standard-library-da-either"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-either.md"
source_title: "DA.Either"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-either
---

# DA.Either

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Either

> Reference documentation for Daml module DA.Either.

<span id="module-da-either-91022" />

# DA.Either

The `Either` type represents values with two possibilities.

It is sometimes used to represent a value which is either correct

or an error. By convention, the `Left` constructor is used to hold

an error value and the `Right` constructor is used to hold a correct

value (mnemonic: "right" also means correct).

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

<span id="function-da-either-lefts-59601" />

### `lefts`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lefts : [Either a b] -> [a]
```

Extracts all the `Left` elements from a list.

<span id="function-da-either-rights-20455" />

### `rights`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
rights : [Either a b] -> [b]
```

Extracts all the `Right` elements from a list.

<span id="function-da-either-partitioneithers-19904" />

### `partitionEithers`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partitionEithers : [Either a b] -> ([a], [b])
```

Partitions a list of `Either` into two lists, the `Left` and
`Right` elements respectively. Order is maintained.

<span id="function-da-either-isleft-96021" />

### `isLeft`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLeft : Either a b -> Bool
```

Return `True` if the given value is a `Left`-value, `False`
otherwise.

<span id="function-da-either-isright-36975" />

### `isRight`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isRight : Either a b -> Bool
```

Return `True` if the given value is a `Right`-value, `False`
otherwise.

<span id="function-da-either-fromleft-63875" />

### `fromLeft`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromLeft : a -> Either a b -> a
```

Return the contents of a `Left`-value, or a default value
in case of a `Right`-value.

<span id="function-da-either-fromright-27657" />

### `fromRight`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromRight : b -> Either a b -> b
```

Return the contents of a `Right`-value, or a default value
in case of a `Left`-value.

<span id="function-da-either-optionaltoeither-21876" />

### `optionalToEither`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
optionalToEither : a -> Optional b -> Either a b
```

Convert a `Optional` value to an `Either` value, using the supplied
parameter as the `Left` value if the `Optional` is `None`.

<span id="function-da-either-eithertooptional-89140" />

### `eitherToOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
eitherToOptional : Either a b -> Optional b
```

Convert an `Either` value to a `Optional`, dropping any value in
`Left`.

<span id="function-da-either-maybetoeither-6635" />

### `maybeToEither`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maybeToEither : a -> Optional b -> Either a b
```

<span id="function-da-either-eithertomaybe-94811" />

### `eitherToMaybe`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
eitherToMaybe : Either a b -> Optional b
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
