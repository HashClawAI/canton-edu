---
title: "DA.Action.State.Class"
slug: "appdev-reference-daml-standard-library-da-action-state-class"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action-state-class.md"
source_title: "DA.Action.State.Class"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action-state-class
---

# DA.Action.State.Class

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Action.State.Class

> Reference documentation for Daml module DA.Action.State.Class.

<span id="module-da-action-state-class-12696" />

# DA.Action.State.Class

DA.Action.State.Class

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

## Typeclasses

<span id="class-da-action-state-class-actionstate-80467" />

### `class ActionState s m`

Action `m` has a state variable of type `s`.

Rules:

* `get *> ma  =  ma`
* `ma <* get  =  ma`
* `put a >>= get   =  put a $> a`
* `put a *> put b  =  put b`
* `(,) <$> get <*> get  =  get <&> \a -> (a, a)`

Informally, these rules mean it behaves like an ordinary assignable variable:
it doesn't magically change value by looking at it, if you put a value there
that's always the value you'll get if you read it, assigning a value but
never reading that value has no effect, and so on.

Methods:

* `get : m s`
  Fetch the current value of the state variable.
* `put : s -> m ()`
  Set the value of the state variable.
* `modify : (s -> s) -> m ()`
  Modify the state variable with the given function.
* `modify : Action m => (s -> s) -> m ()`

Instances:

* `instance ActionState s (State s)`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
