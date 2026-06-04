---
title: "DA.Action.State"
slug: "appdev-reference-daml-standard-library-da-action-state"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action-state.md"
source_title: "DA.Action.State"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action-state
---

# DA.Action.State

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Action.State

> Reference documentation for Daml module DA.Action.State.

<span id="module-da-action-state-50232" />

# DA.Action.State

DA.Action.State

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

<span id="type-da-action-state-type-state-76783" />

### `data State s a`

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
A value of type `State s a` represents a computation that has access to a state variable
of type `s` and produces a value of type `a`.

>>> runState (modify (+1)) 0
((), 1)

>>> evalState (modify (+1)) 0
()

>>> execState (modify (+1)) 0
1

>>> runState (do x <- get; modify (+1); pure x) 0
(0, 1)

>>> runState (put 1) 0
((), 1)

>>> runState (modify (+1)) 0
((), 1)

Note that values of type `State s a` are not serializable.
```

Constructors:

<span id="constr-da-action-state-type-state-26" />

* `State`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| runState | s -> (a, s) |  |

Instances:

* `instance ActionState s (State s)`
* `instance Action (State s)`
* `instance Applicative (State s)`
* `instance GetField runState (State s a) (s -> (a, s))`
* `instance SetField runState (State s a) (s -> (a, s))`
* `instance Functor (State s)`

## Functions

<span id="function-da-action-state-evalstate-95640" />

### `evalState`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
evalState : State s a -> s -> a
```

Special case of `runState` that does not return the final state.

<span id="function-da-action-state-execstate-48251" />

### `execState`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
execState : State s a -> s -> s
```

Special case of `runState` that does only retun the final state.

## Orphan Typeclass Instances

* `instance Functor (State s)`

* `instance Applicative (State s)`

* `instance Action (State s)`

* `instance ActionState s (State s)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
