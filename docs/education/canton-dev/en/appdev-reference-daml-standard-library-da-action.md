---
title: "DA.Action"
slug: "appdev-reference-daml-standard-library-da-action"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action.md"
source_title: "DA.Action"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action
---

# DA.Action

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Action

> Reference documentation for Daml module DA.Action.

<span id="module-da-action-7169" />

# DA.Action

Action

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

<span id="function-da-action-when-35467" />

### `when`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
when : Applicative f => Bool -> f () -> f ()
```

Conditional execution of `Action` expressions. For example,

```
  when final (archive contractId)
```

will archive the contract `contractId` if the Boolean value `final` is
`True`, and otherwise do nothing.

This function has short-circuiting semantics, i.e., when both arguments are
present and the first arguments evaluates to `False`, the second argument
is not evaluated at all.

<span id="function-da-action-unless-8539" />

### `unless`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unless : Applicative f => Bool -> f () -> f ()
```

The reverse of `when`.

This function has short-circuiting semantics, i.e., when both arguments are
present and the first arguments evaluates to `True`, the second argument
is not evaluated at all.

<span id="function-da-action-foldra-2803" />

### `foldrA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldrA : Action m => (a -> b -> m b) -> b -> [a] -> m b
```

The `foldrA` is analogous to `foldr`, except that its result is
encapsulated in an action. Note that `foldrA` works from right-to-left
over the list arguments.

<span id="function-da-action-foldr1a-55935" />

### `foldr1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1A : Action m => (a -> a -> m a) -> [a] -> m a
```

`foldr1A` is like `foldrA` but raises an error when presented
with an empty list argument.

<span id="function-da-action-foldla-78897" />

### `foldlA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldlA : Action m => (b -> a -> m b) -> b -> [a] -> m b
```

`foldlA` is analogous to `foldl`, except that its result is
encapsulated in an action. Note that `foldlA` works from
left-to-right over the list arguments.

<span id="function-da-action-foldl1a-65193" />

### `foldl1A`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1A : Action m => (a -> a -> m a) -> [a] -> m a
```

The `foldl1A` is like `foldlA` but raises an errors when
presented with an empty list argument.

<span id="function-da-action-filtera-13011" />

### `filterA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filterA : Applicative m => (a -> m Bool) -> [a] -> m [a]
```

Filters the list using the applicative function: keeps only the elements where the predicate holds.
Example: given a collection of Iou contract IDs one can find only the GBPs.

```
filterA (fmap (\iou -> iou.currency == "GBP") . fetch) iouCids
```

<span id="function-da-action-replicatea-98867" />

### `replicateA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicateA : Applicative m => Int -> m a -> m [a]
```

`replicateA n act` performs the action `n` times, gathering the
results.

<span id="function-da-action-replicatea-83733" />

### `replicateA_`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicateA_ : Applicative m => Int -> m a -> m ()
```

Like `replicateA`, but discards the result.

<span id="function-da-action-gteqgt-60955" />

### `>=>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
>=> : Action m => (a -> m b) -> (b -> m c) -> a -> m c
```

Left-to-right composition of Kleisli arrows.

<span id="function-da-action-lteqlt-31871" />

### `<=<`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<=< : Action m => (b -> m c) -> (a -> m b) -> a -> m c
```

Right-to-left composition of Kleisli arrows. @('>=>')@, with the arguments
flipped.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
