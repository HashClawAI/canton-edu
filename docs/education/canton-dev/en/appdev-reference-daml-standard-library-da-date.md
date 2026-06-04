---
title: "DA.Date"
slug: "appdev-reference-daml-standard-library-da-date"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-date.md"
source_title: "DA.Date"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-date
---

# DA.Date

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Date

> Reference documentation for Daml module DA.Date.

<span id="module-da-date-80009" />

# DA.Date

This module provides a set of functions to manipulate Date values.

The bounds for Date are 0001-01-01T00:00:00.000000Z and

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

<span id="type-da-date-types-dayofweek-18120" />

### `data DayOfWeek`

Constructors:

<span id="constr-da-date-types-monday-43349" />

* `Monday`

<span id="constr-da-date-types-tuesday-5501" />

* `Tuesday`

<span id="constr-da-date-types-wednesday-18786" />

* `Wednesday`

<span id="constr-da-date-types-thursday-55301" />

* `Thursday`

<span id="constr-da-date-types-friday-14884" />

* `Friday`

<span id="constr-da-date-types-saturday-99714" />

* `Saturday`

<span id="constr-da-date-types-sunday-48181" />

* `Sunday`

Instances:

* `instance Eq DayOfWeek`
* `instance Ord DayOfWeek`
* `instance Bounded DayOfWeek`
* `instance Enum DayOfWeek`
* `instance Show DayOfWeek`

<span id="type-da-date-types-month-22803" />

### `data Month`

The `Month` type represents a month in the Gregorian calendar.

Note that, while `Month` has an `Enum` instance, the `toEnum` and `fromEnum`
functions start counting at 0, i.e. `toEnum 1 :: Month` is `Feb`.

Constructors:

<span id="constr-da-date-types-jan-1103" />

* `Jan`

<span id="constr-da-date-types-feb-88523" />

* `Feb`

<span id="constr-da-date-types-mar-5472" />

* `Mar`

<span id="constr-da-date-types-apr-12091" />

* `Apr`

<span id="constr-da-date-types-may-50999" />

* `May`

<span id="constr-da-date-types-jun-17739" />

* `Jun`

<span id="constr-da-date-types-jul-21893" />

* `Jul`

<span id="constr-da-date-types-aug-18125" />

* `Aug`

<span id="constr-da-date-types-sep-63548" />

* `Sep`

<span id="constr-da-date-types-oct-96134" />

* `Oct`

<span id="constr-da-date-types-nov-72317" />

* `Nov`

<span id="constr-da-date-types-dec-74760" />

* `Dec`

Instances:

* `instance Eq Month`
* `instance Ord Month`
* `instance Bounded Month`
* `instance Enum Month`
* `instance Show Month`

## Functions

<span id="function-da-date-adddays-7836" />

### `addDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
addDays : Date -> Int -> Date
```

Add the given number of days to a date.

<span id="function-da-date-subtractdays-16626" />

### `subtractDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subtractDays : Date -> Int -> Date
```

Subtract the given number of days from a date.

`subtractDays d r` is equivalent to `addDays d (- r)`.

<span id="function-da-date-subdate-25598" />

### `subDate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subDate : Date -> Date -> Int
```

Returns the number of days between the two given dates.

<span id="function-da-date-dayofweek-99931" />

### `dayOfWeek`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dayOfWeek : Date -> DayOfWeek
```

Returns the day of week for the given date.

<span id="function-da-date-fromgregorian-85346" />

### `fromGregorian`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromGregorian : (Int, Month, Int) -> Date
```

Constructs a `Date` from the triplet `(year, month, days)`.

<span id="function-da-date-togregorian-84541" />

### `toGregorian`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toGregorian : Date -> (Int, Month, Int)
```

Turn `Date` value into a `(year, month, day)` triple, according
to the Gregorian calendar.

<span id="function-da-date-date-21355" />

### `date`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
date : Int -> Month -> Int -> Date
```

Given the three values (year, month, day), constructs a `Date` value.
`date y m d` turns the year `y`, month `m`, and day `d` into a `Date` value.
Raises an error if `d` is outside the range `1 .. monthDayCount y m`.

<span id="function-da-date-isleapyear-61920" />

### `isLeapYear`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLeapYear : Int -> Bool
```

Returns `True` if the given year is a leap year.

<span id="function-da-date-frommonth-90328" />

### `fromMonth`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromMonth : Month -> Int
```

Get the number corresponding to given month. For example, `Jan` corresponds
to `1`, `Feb` corresponds to `2`, and so on.

<span id="function-da-date-monthdaycount-59295" />

### `monthDayCount`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
monthDayCount : Int -> Month -> Int
```

Get number of days in the given month in the given year, according to Gregorian calendar.
This does not take historical calendar changes into account (for example, the
moves from Julian to Gregorian calendar), but does count leap years.

<span id="function-da-date-datetime-90284" />

### `datetime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
datetime : Int -> Month -> Int -> Int -> Int -> Int -> Time
```

Constructs an instant using `year`, `month`, `day`, `hours`, `minutes`, `seconds`.

<span id="function-da-date-todateutc-87953" />

### `toDateUTC`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toDateUTC : Time -> Date
```

Extracts UTC date from UTC time.

This function will truncate Time to Date, but in many cases it will not return the date you really want.
The reason for this is that usually the source of Time would be getTime, and getTime returns UTC, and most likely
the date you want is something local to a location or an exchange. Consequently the date retrieved this way would be
yesterday if retrieved when the market opens in say Singapore.

## Orphan Typeclass Instances

* `instance Eq DayOfWeek`

* `instance Ord DayOfWeek`

* `instance Show DayOfWeek`

* `instance Enum DayOfWeek`

* `instance Bounded DayOfWeek`

* `instance Eq Month`

* `instance Ord Month`

* `instance Show Month`

* `instance Enum Month`

* `instance Bounded Month`

* `instance Enum Date`

* `instance Bounded Date`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
