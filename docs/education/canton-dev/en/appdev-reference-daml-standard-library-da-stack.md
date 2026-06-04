---
title: "DA.Stack"
slug: "appdev-reference-daml-standard-library-da-stack"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-stack.md"
source_title: "DA.Stack"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-stack
---

# DA.Stack

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Stack

> Reference documentation for Daml module DA.Stack.

<span id="module-da-stack-24914" />

# DA.Stack

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

<span id="type-da-stack-types-srcloc-15887" />

### `data SrcLoc`

Location in the source code.

Line and column are 0-based.

Constructors:

<span id="constr-da-stack-types-srcloc-29880" />

* `SrcLoc`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| srcLocPackage | Text |  |
  \| srcLocModule | Text |  |
  \| srcLocFile | Text |  |
  \| srcLocStartLine | Int |  |
  \| srcLocStartCol | Int |  |
  \| srcLocEndLine | Int |  |
  \| srcLocEndCol | Int |  |

Instances:

* `instance GetField srcLocEndCol SrcLoc Int`
* `instance GetField srcLocEndLine SrcLoc Int`
* `instance GetField srcLocFile SrcLoc Text`
* `instance GetField srcLocModule SrcLoc Text`
* `instance GetField srcLocPackage SrcLoc Text`
* `instance GetField srcLocStartCol SrcLoc Int`
* `instance GetField srcLocStartLine SrcLoc Int`
* `instance SetField srcLocEndCol SrcLoc Int`
* `instance SetField srcLocEndLine SrcLoc Int`
* `instance SetField srcLocFile SrcLoc Text`
* `instance SetField srcLocModule SrcLoc Text`
* `instance SetField srcLocPackage SrcLoc Text`
* `instance SetField srcLocStartCol SrcLoc Int`
* `instance SetField srcLocStartLine SrcLoc Int`

## Functions

<span id="function-da-stack-prettycallstack-78669" />

### `prettyCallStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
prettyCallStack : CallStack -> Text
```

Pretty-print a `CallStack`.

<span id="function-da-stack-getcallstack-34576" />

### `getCallStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
getCallStack : CallStack -> [(Text, SrcLoc)]
```

Extract the list of call sites from the `CallStack`.

The most recent call comes first.

<span id="function-da-stack-callstack-89067" />

### `callStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
callStack : HasCallStack => CallStack
```

Access to the current `CallStack`.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
