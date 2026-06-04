---
title: "SV Upgrades"
slug: "global-synchronizer-production-operations-sv-upgrades"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/sv-upgrades.md"
source_title: "SV Upgrades"
tags:
  - global-synchronizer
  - production-operations
  - sv-upgrades
---

# SV Upgrades

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SV Upgrades

> Minor upgrade procedures for Super Validator nodes

There are two types of upgrades:

Version upgrades (this corresponds to an upgrade from `0.A.X` to `0.B.Y`) and protocol upgrades (the actual version can remain the same, only the protocol is upgraded).

Version upgrades can be done by each node independently and only require a `helm upgrade`. Make sure to read the `release_notes` to learn about changes you may need to make as part of the upgrade.

Protocol upgrades are performed through logical synchronizer upgrades, which allow upgrading the protocol version with very limited network downtime.

<Card title="Logical Synchronizer Upgrades" icon="shuffle" href="/docs/canton/global-synchronizer-production-operations-logical-synchronizer-upgrade">
  Review the operational flow for scheduling and performing logical synchronizer upgrades.
</Card>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
