---
title: "DA.Internal.Interface.AnyView.Types"
slug: "appdev-reference-daml-standard-library-da-internal-interface-anyview-types"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-internal-interface-anyview-types.md"
source_title: "DA.Internal.Interface.AnyView.Types"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-internal-interface-anyview-types
---

# DA.Internal.Interface.AnyView.Types

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Internal.Interface.AnyView.Types

> Reference documentation for Daml module DA.Internal.Interface.AnyView.Types.

<span id="module-da-internal-interface-anyview-types-13315" />

# DA.Internal.Interface.AnyView\.Types

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

<span id="type-da-internal-interface-anyview-types-anyview-16883" />

### `data AnyView`

Existential contract key type that can wrap an arbitrary contract key.

Constructors:

<span id="constr-da-internal-interface-anyview-types-anyview-58868" />

* `AnyView`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyView | Any |  |
  \| getAnyViewInterfaceTypeRep | InterfaceTypeRep |  |

Instances:

* `instance GetField getAnyView AnyView Any`
* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField getAnyView AnyView Any`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

<span id="type-da-internal-interface-anyview-types-interfacetyperep-5047" />

### `data InterfaceTypeRep`

Constructors:

<span id="constr-da-internal-interface-anyview-types-interfacetyperep-24802" />

* `InterfaceTypeRep`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getInterfaceTypeRep | TypeRep |  |

Instances:

* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance Eq InterfaceTypeRep`
* `instance Ord InterfaceTypeRep`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
