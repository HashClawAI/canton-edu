---
title: "DA.Assert"
slug: "appdev-reference-daml-standard-library-da-assert"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-assert.md"
source_title: "DA.Assert"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-assert
---

# DA.Assert

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Assert

> Reference documentation for Daml module DA.Assert.

<span id="module-da-assert-92761" />

# DA.Assert

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

<span id="function-da-assert-asserteq-7135" />

### `assertEq`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertEq : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

Check two values for equality. If they're not equal,
fail with a message.

<span id="function-da-assert-eqeqeq-18699" />

### `===`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=== : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

Infix version of `assertEq`.

<span id="function-da-assert-assertnoteq-28771" />

### `assertNotEq`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertNotEq : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

Check two values for inequality. If they're equal,
fail with a message.

<span id="function-da-assert-eqslasheq-37517" />

### `=/=`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=/= : (CanAssert m, Show a, Eq a) => a -> a -> m ()
```

Infix version of `assertNotEq`.

<span id="function-da-assert-assertaftermsg-14090" />

### `assertAfterMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertAfterMsg : (CanAssert m, HasTime m) => Text -> Time -> m ()
```

Check whether the given time is in the future. If it's not,
abort with a message.

<span id="function-da-assert-assertbeforemsg-56514" />

### `assertBeforeMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertBeforeMsg : (CanAssert m, HasTime m) => Text -> Time -> m ()
```

Check whether the given time is in the past. If it's not,
abort with a message.

<span id="function-da-assert-assertwithindeadline-85580" />

### `assertWithinDeadline`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertWithinDeadline : Text -> Time -> Update ()
```

Check whether the ledger time of the transaction is strictly before the given deadline.
If it's not, abort with a message.

<span id="function-da-assert-assertdeadlineexceeded-21600" />

### `assertDeadlineExceeded`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertDeadlineExceeded : Text -> Time -> Update ()
```

Check whether the ledger time of the transaction is at or after the given deadline.
If it's not, abort with a message.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
