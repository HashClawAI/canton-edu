---
title: "DA.Exception"
slug: "appdev-reference-daml-standard-library-da-exception"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-exception.md"
source_title: "DA.Exception"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-exception
---

# DA.Exception

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Exception

> Reference documentation for Daml module DA.Exception.

<span id="module-da-exception-55791" />

# DA.Exception

Exception handling in Daml.

DEPRECATED: Use `failWithStatus` and `FailureStatus` over Daml Exceptions

## Module Snapshot

<CardGroup cols={2}>
  <Card title="Lifecycle">
    Deprecated.
  </Card>

  <Card title="Notices">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `2`
    Deprecated since: `3.4.9`
  </Card>
</CardGroup>

<Warning>
  Exceptions are deprecated, prefer `failWithStatus`, and avoid using catch.
</Warning>

<AccordionGroup>
  <Accordion title="All deprecations (2)">
    * Exceptions are deprecated, prefer `failWithStatus`, and avoid using catch.
    * Use `-Wno-deprecated-exceptions` to disable this warning.
  </Accordion>
</AccordionGroup>

## Data Types

<span id="type-da-internal-exception-exception-4133" />

### `type Exception = (HasThrow e, HasMessage e, HasToAnyException e, HasFromAnyException e)`

Exception typeclass. This should not be implemented directly,
instead, use the `exception` syntax.

## Typeclasses

<span id="class-da-internal-exception-hasthrow-30284" />

### `class HasThrow e`

Part of the `Exception` constraint.

Methods:

* `throwPure : e -> t`
  Throw exception in a pure context.

Instances:

* `instance HasThrow ArithmeticError`
* `instance HasThrow AssertionFailed`
* `instance HasThrow GeneralError`
* `instance HasThrow PreconditionFailed`

<span id="class-da-internal-exception-hasmessage-3179" />

### `class HasMessage e`

Part of the `Exception` constraint.

Methods:

* `message : e -> Text`
  Get the error message associated with an exception.

Instances:

* `instance HasMessage AnyException`
* `instance HasMessage ArithmeticError`
* `instance HasMessage AssertionFailed`
* `instance HasMessage GeneralError`
* `instance HasMessage PreconditionFailed`

<span id="class-da-internal-exception-hastoanyexception-55973" />

### `class HasToAnyException e`

Part of the `Exception` constraint.

Methods:

* `toAnyException : e -> AnyException`
  Convert an exception type to AnyException.

Instances:

* `instance HasToAnyException AnyException`
* `instance HasToAnyException ArithmeticError`
* `instance HasToAnyException AssertionFailed`
* `instance HasToAnyException GeneralError`
* `instance HasToAnyException PreconditionFailed`

<span id="class-da-internal-exception-hasfromanyexception-16788" />

### `class HasFromAnyException e`

Part of the `Exception` constraint.

Methods:

* `fromAnyException : AnyException -> Optional e`
  Convert an AnyException back to the underlying exception type, if possible.

Instances:

* `instance HasFromAnyException AnyException`
* `instance HasFromAnyException ArithmeticError`
* `instance HasFromAnyException AssertionFailed`
* `instance HasFromAnyException GeneralError`
* `instance HasFromAnyException PreconditionFailed`

<span id="class-da-internal-exception-actionthrow-37623" />

### `class Action m => ActionThrow m`

Action type in which `throw` is supported.

Methods:

* `throw : Exception e => e -> m t`

Instances:

* `instance ActionThrow Update`

<span id="class-da-internal-exception-actioncatch-69238" />

### `class ActionThrow m => ActionCatch m`

Action type in which `try ... catch ...` is supported.
DEPRECATED: Avoid the use of catch in daml code, prefer error handling on client, and throwing using `failWithStatus`

Methods:

* `_tryCatch : (() -> m t) -> (AnyException -> Optional (m t)) -> m t`
  Handle an exception. Use the `try ... catch ...` syntax
  instead of calling this method directly.

Instances:

* `instance ActionCatch Update`

## Orphan Typeclass Instances

* `instance GetField message GeneralError Text`

* `instance SetField message GeneralError Text`

* `instance GetField message ArithmeticError Text`

* `instance SetField message ArithmeticError Text`

* `instance GetField message PreconditionFailed Text`

* `instance SetField message PreconditionFailed Text`

* `instance GetField message AssertionFailed Text`

* `instance SetField message AssertionFailed Text`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
