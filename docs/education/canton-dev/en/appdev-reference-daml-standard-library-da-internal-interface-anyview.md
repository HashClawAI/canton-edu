---
title: "DA.Internal.Interface.AnyView"
slug: "appdev-reference-daml-standard-library-da-internal-interface-anyview"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-internal-interface-anyview.md"
source_title: "DA.Internal.Interface.AnyView"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-internal-interface-anyview
---

# DA.Internal.Interface.AnyView

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Internal.Interface.AnyView

> Reference documentation for Daml module DA.Internal.Interface.AnyView.

<span id="module-da-internal-interface-anyview-80474" />

# DA.Internal.Interface.AnyView

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

<span id="class-da-internal-interface-anyview-hasfromanyview-30108" />

### `class HasFromAnyView i v`

## Functions

<span id="function-da-internal-interface-anyview-fromanyview-10400" />

### `fromAnyView`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyView : (HasTemplateTypeRep i, HasFromAnyView i v) => AnyView -> Optional v
```

## Orphan Typeclass Instances

* `instance Eq InterfaceTypeRep`

* `instance Ord InterfaceTypeRep`

* `instance GetField getAnyView AnyView Any`

* `instance SetField getAnyView AnyView Any`

* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
