---
title: "DA.Optional"
slug: "appdev-reference-daml-standard-library-da-optional"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-optional.md"
source_title: "DA.Optional"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-optional
---

# DA.Optional

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Optional

> Reference documentation for Daml module DA.Optional.

<span id="module-da-optional-38505" />

# DA.Optional

The `Optional` type encapsulates an optional value. A value of type

`Optional a` either contains a value of type `a` (represented as `Some a`),

or it is empty (represented as `None`). Using `Optional` is a good way

to deal with errors or exceptional cases without resorting to

drastic measures such as error.

The Optional type is also an action. It is a simple kind of error

action, where all errors are represented by `None`. A richer

error action can be built using the `Either` type.

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

<span id="function-da-optional-fromsome-59859" />

### `fromSome`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromSome : Optional a -> a
```

The `fromSome` function extracts the element out of a `Some` and
throws an error if its argument is `None`.

Note that in most cases you should prefer using `fromSomeNote`
to get a better error on failures.

<span id="function-da-optional-fromsomenote-25463" />

### `fromSomeNote`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromSomeNote : Text -> Optional a -> a
```

Like `fromSome` but with a custom error message.

<span id="function-da-optional-catoptionals-11568" />

### `catOptionals`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
catOptionals : [Optional a] -> [a]
```

The `catOptionals` function takes a list of `Optionals` and returns a
list of all the `Some` values.

<span id="function-da-optional-listtooptional-83598" />

### `listToOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
listToOptional : [a] -> Optional a
```

The `listToOptional` function returns `None` on an empty list or
`Some` a where a is the first element of the list.

<span id="function-da-optional-optionaltolist-83426" />

### `optionalToList`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
optionalToList : Optional a -> [a]
```

The `optionalToList` function returns an empty list when given
`None` or a singleton list when not given `None`.

<span id="function-da-optional-fromoptional-77879" />

### `fromOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromOptional : a -> Optional a -> a
```

The `fromOptional` function takes a default value and a `Optional`
value. If the `Optional` is `None`, it returns the default values
otherwise, it returns the value contained in the `Optional`.

<span id="function-da-optional-issome-25261" />

### `isSome`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSome : Optional a -> Bool
```

The `isSome` function returns `True` iff its argument is of the
form `Some _`.

<span id="function-da-optional-isnone-84783" />

### `isNone`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isNone : Optional a -> Bool
```

The `isNone` function returns `True` iff its argument is
`None`.

<span id="function-da-optional-mapoptional-4330" />

### `mapOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapOptional : (a -> Optional b) -> [a] -> [b]
```

The `mapOptional` function is a version of `map` which can throw out
elements. In particular, the functional argument returns something
of type `Optional b`. If this is `None`, no element is added on to
the result list. If it is `Some b`, then `b` is included in the
result list.

<span id="function-da-optional-whensome-82167" />

### `whenSome`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
whenSome : Applicative m => Optional a -> (a -> m ()) -> m ()
```

Perform some operation on `Some`, given the field inside the
`Some`.

<span id="function-da-optional-findoptional-83634" />

### `findOptional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
findOptional : (a -> Optional b) -> [a] -> Optional b
```

The `findOptional` returns the value of the predicate at the first
element where it returns `Some`. `findOptional` is similar to `find` but it
allows you to return a value from the predicate. This is useful both as a more
type safe version if the predicate corresponds to a pattern match
and for performance to avoid duplicating work performed in the predicate.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
