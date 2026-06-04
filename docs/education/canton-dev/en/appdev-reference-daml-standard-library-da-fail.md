---
title: "DA.Fail"
slug: "appdev-reference-daml-standard-library-da-fail"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-fail.md"
source_title: "DA.Fail"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-fail
---

# DA.Fail

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Fail

> Reference documentation for Daml module DA.Fail.

<span id="module-da-fail-58029" />

# DA.Fail

Fail, for FailureStatus

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

<span id="type-da-internal-fail-types-failurecategory-97811" />

### `data FailureCategory`

The category of the failure, which determines the status code and log
level of the failure. Maps 1-1 to the Canton error categories documented
here: [Error categories inventory](/global-synchronizer/reference/error-codes#error-categories-inventory)

If you are more familiar with gRPC error codes, you can use the synonyms referenced in the
comments.

Constructors:

<span id="constr-da-internal-fail-types-invalidindependentofsystemstate-84432" />

* `InvalidIndependentOfSystemState`
  Use this to report errors that are independent of the current state of the ledger,
  and should thus not be retried.

Corresponds to the gRPC status code `INVALID_ARGUMENT`.

See [Error categories inventory](/global-synchronizer/reference/error-codes#error-categories-inventory)
for more information.

<span id="constr-da-internal-fail-types-invalidgivencurrentsystemstateother-6547" />

* `InvalidGivenCurrentSystemStateOther`
  Use this to report errors that are due to the current state of the ledger,
  but might disappear if the ledger state changes. Clients should retry these
  requests after reading updated state from the ledger.

Corresponds to the gRPC status code `FAILED_PRECONDITION`.

See [Error categories inventory](/global-synchronizer/reference/error-codes#error-categories-inventory)
for more information.

Instances:

* `instance GetField category FailureStatus FailureCategory`
* `instance SetField category FailureStatus FailureCategory`
* `instance Eq FailureCategory`
* `instance Ord FailureCategory`
* `instance Show FailureCategory`

<span id="type-da-internal-fail-types-failurestatus-69615" />

### `data FailureStatus`

Constructors:

<span id="constr-da-internal-fail-types-failurestatus-61878" />

* `FailureStatus`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| errorId | Text | Unambiguous identifier of the error.<br /><br />SHOULD be prefixed with the DNS name identifying the app provider<br /><br />or the API standard defining the error. For example,<br /><br />`splice.lfdecentralizedtrust.org/insufficient-funds` could be used for<br /><br />reporting an out of funds error in the context of the CN token standards. |
  \| category | FailureCategory | Category of the failure, which determines how clients are expected to handle the error. |
  \| message | Text | Developer-facing error message, which should be in English. |
  \| meta | TextMap Text | Machine-readable metadata about the error in a key-value format.<br /><br />Use this to provide extra context to clients for errors.<br /><br />SHOULD be less than \< 512 characters as it MAY be truncated otherwise. |

Instances:

* `instance GetField category FailureStatus FailureCategory`
* `instance GetField errorId FailureStatus Text`
* `instance GetField message FailureStatus Text`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance SetField category FailureStatus FailureCategory`
* `instance SetField errorId FailureStatus Text`
* `instance SetField message FailureStatus Text`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance Eq FailureStatus`
* `instance Ord FailureStatus`
* `instance Show FailureStatus`

## Typeclasses

<span id="class-da-internal-fail-actionfailwithstatus-58664" />

### `class Action m => ActionFailWithStatus m`

Methods:

* `failWithStatus : FailureStatus -> m a`
  Fail with a failure status

Instances:

* `instance ActionFailWithStatus Update`

## Functions

<span id="function-da-fail-invalidargument-67588" />

### `invalidArgument`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
invalidArgument : FailureCategory
```

Alternative name for `InvalidIndependentOfSystemState`.

<span id="function-da-fail-failedprecondition-95960" />

### `failedPrecondition`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
failedPrecondition : FailureCategory
```

Alternative name for `InvalidGivenCurrentSystemStateOther`.

<span id="function-da-internal-fail-failwithstatuspure-20043" />

### `failWithStatusPure`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
failWithStatusPure : FailureStatus -> a
```

Fail with a failure status in a pure context

## Orphan Typeclass Instances

* `instance Eq FailureStatus`

* `instance Ord FailureStatus`

* `instance Show FailureStatus`

* `instance Eq FailureCategory`

* `instance Ord FailureCategory`

* `instance Show FailureCategory`

* `instance GetField errorId FailureStatus Text`

* `instance SetField errorId FailureStatus Text`

* `instance GetField category FailureStatus FailureCategory`

* `instance SetField category FailureStatus FailureCategory`

* `instance GetField message FailureStatus Text`

* `instance SetField message FailureStatus Text`

* `instance GetField meta FailureStatus (TextMap Text)`

* `instance SetField meta FailureStatus (TextMap Text)`

* `instance ActionFail Update`

* `instance CanAbort Update`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
