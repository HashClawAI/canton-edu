---
title: "DA.Time"
slug: "appdev-reference-daml-standard-library-da-time"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-time.md"
source_title: "DA.Time"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-time
---

# DA.Time

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Time

> Reference documentation for Daml module DA.Time.

<span id="module-da-time-32716" />

# DA.Time

This module provides a set of functions to manipulate Time values.

The `Time` type represents a specific datetime in UTC,

for example `time (date 2007 Apr 5) 14 30 05`.

The bounds for Time are 0001-01-01T00:00:00.000000Z and

9999-12-31T23:59:59.999999Z.

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

<span id="type-da-time-types-reltime-23082" />

### `data RelTime`

The `RelTime` type describes a time offset, i.e. relative time.

Instances:

* `instance Eq RelTime`
* `instance Ord RelTime`
* `instance Bounded RelTime`
* `instance Additive RelTime`
* `instance Signed RelTime`
* `instance Show RelTime`

## Functions

<span id="function-da-internal-time-time-34667" />

### `time`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
time : Date -> Int -> Int -> Int -> Time
```

`time d h m s` turns given UTC date `d` and the UTC time (given in hours, minutes, seconds)
into a UTC timestamp (`Time`). Does not handle leap seconds.

<span id="function-da-time-addreltime-70617" />

### `addRelTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
addRelTime : Time -> RelTime -> Time
```

Adjusts `Time` with given time offset.

<span id="function-da-time-subtime-47226" />

### `subTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subTime : Time -> Time -> RelTime
```

Returns time offset between two given instants.

<span id="function-da-time-wholedays-91725" />

### `wholeDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wholeDays : RelTime -> Int
```

Returns the number of whole days in a time offset. Fraction of time is rounded towards zero.

<span id="function-da-time-days-58759" />

### `days`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
days : Int -> RelTime
```

A number of days in relative time.

<span id="function-da-time-hours-54068" />

### `hours`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
hours : Int -> RelTime
```

A number of hours in relative time.

<span id="function-da-time-minutes-72520" />

### `minutes`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minutes : Int -> RelTime
```

A number of minutes in relative time.

<span id="function-da-time-seconds-68512" />

### `seconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
seconds : Int -> RelTime
```

A number of seconds in relative time.

<span id="function-da-time-milliseconds-28552" />

### `milliseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
milliseconds : Int -> RelTime
```

A number of milliseconds in relative time.

<span id="function-da-time-microseconds-56941" />

### `microseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
microseconds : Int -> RelTime
```

A number of microseconds in relative time.

<span id="function-da-time-convertreltimetomicroseconds-23127" />

### `convertRelTimeToMicroseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
convertRelTimeToMicroseconds : RelTime -> Int
```

Convert RelTime to microseconds
Use higher level functions instead of the internal microseconds

<span id="function-da-time-convertmicrosecondstoreltime-73643" />

### `convertMicrosecondsToRelTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
convertMicrosecondsToRelTime : Int -> RelTime
```

Convert microseconds to RelTime
Use higher level functions instead of the internal microseconds

<span id="function-da-time-isledgertimelt-78120" />

### `isLedgerTimeLT`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeLT : Time -> Update Bool
```

True iff the ledger time of the transaction is less than the given time.

<span id="function-da-time-isledgertimele-50101" />

### `isLedgerTimeLE`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeLE : Time -> Update Bool
```

True iff the ledger time of the transaction is less than or equal to the given time.

<span id="function-da-time-isledgertimegt-6233" />

### `isLedgerTimeGT`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeGT : Time -> Update Bool
```

True iff the ledger time of the transaction is greater than the given time.

<span id="function-da-time-isledgertimege-95212" />

### `isLedgerTimeGE`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeGE : Time -> Update Bool
```

True iff the ledger time of the transaction is greater than or equal to the given time.

## Orphan Typeclass Instances

* `instance Eq RelTime`

* `instance Ord RelTime`

* `instance Show RelTime`

* `instance Additive RelTime`

* `instance Signed RelTime`

* `instance Bounded RelTime`

* `instance Bounded Time`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
