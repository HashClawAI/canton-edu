---
title: "DA.Record"
slug: "appdev-reference-daml-standard-library-da-record"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-record.md"
source_title: "DA.Record"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-record
---

# DA.Record

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Record

> Reference documentation for Daml module DA.Record.

<span id="module-da-record-78710" />

# DA.Record

Exports the record machinery necessary to allow one to annotate

code that is polymorphic in the underlying record type.

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

<span id="type-da-internal-record-hasfield-59910" />

### `type HasField = (GetField x r a, SetField x r a)`

`HasField` is a class synonym for `GetField` and `SetField`, which
respectively give you getter and setter functions for each record field
automatically.

**In the vast majority of use-cases, plain Record syntax should be
preferred**:

```
daml> let a = MyRecord 1 "hello"
daml> a.foo
1
daml> a.bar
"hello"
daml> a { bar = "bye" }
MyRecord {foo = 1, bar = "bye"}
daml> a with foo = 3
MyRecord {foo = 3, bar = "hello"}
daml>
```

For more on Record syntax, see [DA.Record](/docs/canton/appdev-reference-daml-standard-library-da-record).

`GetField x r a` and `SetField x r a` are typeclasses taking three parameters. The first
parameter `x` is the field name, the second parameter `r` is the record type,
and the last parameter `a` is the type of the field in this record. For
example, if we define a type:

```
data MyRecord = MyRecord with
    foo : Int
    bar : Text
```

Then we get, for free, the following GetField and SetField instances:

```
GetField "foo" MyRecord Int
SetField "foo" MyRecord Int
GetField "bar" MyRecord Text
SetField "bar" MyRecord Text
```

If we want to get a value, we can use the `getField` method of class `GetField`:

```
getFoo : MyRecord -> Int
getFoo r = getField @"foo" r

getBar : MyRecord -> Text
getBar r = getField @"bar" r
```

Note that this uses the “type application” syntax ( `f @t` ) to specify the
field name.

Likewise, if we want to set the value in the field, we can use the `setField` method of class `SetField`:

```
setFoo : Int -> MyRecord -> MyRecord
setFoo a r = setField @"foo" a r

setBar : Text -> MyRecord -> MyRecord
setBar a r = setField @"bar" a r
```

## Typeclasses

<span id="class-da-internal-record-getfield-53979" />

### `class GetField x r a`

`GetField x r a` provides the getter part of `HasField`

Methods:

* `getField : r -> a`

Instances:

* `instance GetField _1 (a, b) a`
* `instance GetField _1 (a, b, c) a`
* `instance GetField _1 (a, b, c, d) a`
* `instance GetField _1 (a, b, c, d, e) a`
* `instance GetField _2 (a, b) b`
* `instance GetField _2 (a, b, c) b`
* `instance GetField _2 (a, b, c, d) b`
* `instance GetField _2 (a, b, c, d, e) b`
* `instance GetField _3 (a, b, c) c`
* `instance GetField _3 (a, b, c, d) c`
* `instance GetField _3 (a, b, c, d, e) c`
* `instance GetField _4 (a, b, c, d) d`
* `instance GetField _4 (a, b, c, d, e) d`
* `instance GetField _5 (a, b, c, d, e) e`
* `instance GetField appEndo (Endo a) (a -> a)`
* `instance GetField category FailureStatus FailureCategory`
* `instance GetField errorId FailureStatus Text`
* `instance GetField getAll All Bool`
* `instance GetField getAny Any Bool`
* `instance GetField getAnyView AnyView Any`
* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance GetField hd (NonEmpty a) a`
* `instance GetField map (Set k) (Map k ())`
* `instance GetField message FailureStatus Text`
* `instance GetField message ArithmeticError Text`
* `instance GetField message AssertionFailed Text`
* `instance GetField message GeneralError Text`
* `instance GetField message PreconditionFailed Text`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance GetField runState (State s a) (s -> (a, s))`
* `instance GetField srcLocEndCol SrcLoc Int`
* `instance GetField srcLocEndLine SrcLoc Int`
* `instance GetField srcLocFile SrcLoc Text`
* `instance GetField srcLocModule SrcLoc Text`
* `instance GetField srcLocPackage SrcLoc Text`
* `instance GetField srcLocStartCol SrcLoc Int`
* `instance GetField srcLocStartLine SrcLoc Int`
* `instance GetField tl (NonEmpty a) [a]`

<span id="class-da-internal-record-setfield-4311" />

### `class SetField x r a`

`SetField x r a` provides the setter part of `HasField`

Methods:

* `setField : a -> r -> r`

Instances:

* `instance SetField _1 (a, b) a`
* `instance SetField _1 (a, b, c) a`
* `instance SetField _1 (a, b, c, d) a`
* `instance SetField _1 (a, b, c, d, e) a`
* `instance SetField _2 (a, b) b`
* `instance SetField _2 (a, b, c) b`
* `instance SetField _2 (a, b, c, d) b`
* `instance SetField _2 (a, b, c, d, e) b`
* `instance SetField _3 (a, b, c) c`
* `instance SetField _3 (a, b, c, d) c`
* `instance SetField _3 (a, b, c, d, e) c`
* `instance SetField _4 (a, b, c, d) d`
* `instance SetField _4 (a, b, c, d, e) d`
* `instance SetField _5 (a, b, c, d, e) e`
* `instance SetField appEndo (Endo a) (a -> a)`
* `instance SetField category FailureStatus FailureCategory`
* `instance SetField errorId FailureStatus Text`
* `instance SetField getAll All Bool`
* `instance SetField getAny Any Bool`
* `instance SetField getAnyView AnyView Any`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField hd (NonEmpty a) a`
* `instance SetField map (Set k) (Map k ())`
* `instance SetField message FailureStatus Text`
* `instance SetField message ArithmeticError Text`
* `instance SetField message AssertionFailed Text`
* `instance SetField message GeneralError Text`
* `instance SetField message PreconditionFailed Text`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance SetField runState (State s a) (s -> (a, s))`
* `instance SetField srcLocEndCol SrcLoc Int`
* `instance SetField srcLocEndLine SrcLoc Int`
* `instance SetField srcLocFile SrcLoc Text`
* `instance SetField srcLocModule SrcLoc Text`
* `instance SetField srcLocPackage SrcLoc Text`
* `instance SetField srcLocStartCol SrcLoc Int`
* `instance SetField srcLocStartLine SrcLoc Int`
* `instance SetField tl (NonEmpty a) [a]`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
