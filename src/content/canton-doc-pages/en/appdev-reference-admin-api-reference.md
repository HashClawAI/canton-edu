---
title: "Admin API Reference"
slug: "appdev-reference-admin-api-reference"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/admin-api-reference.md"
source_title: "Admin API Reference"
tags:
  - appdev
  - reference
  - admin-api-reference
---

# Admin API Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Admin API Reference

> Reference documentation for the Canton Admin API used for node administration

The Admin API provides administrative access to Canton participant, sequencer, and mediator nodes. It is used for node configuration, topology management, key management, and operational tasks that are not exposed through the Ledger API.

<Warning>
  Never expose the Admin API to the public internet. Restrict access to VPN or private networks only. The Admin API provides full administrative control over the node.
</Warning>

## Access

The Admin API uses gRPC and is available on the participant's Admin API port (default: 5002). It is also accessible through the Canton Console, which wraps Admin API calls in a Scala REPL.

## Core Service Groups

### Health and Status

* **StatusService** — Check node health, readiness, and connected synchronizers

### Topology Management

Topology commands manage the distributed topology state that controls party-to-participant mappings, package vetting, and synchronizer parameters.

* **TopologyManagerReadService** — Read current topology state (party mappings, vetted packages, namespace delegations)
* **TopologyManagerWriteService** — Propose topology changes (requires appropriate authorization)

### Synchronizer Connection

* **SynchronizerConnectivityService** — Connect, disconnect, and reconnect to synchronizers. List connected and registered synchronizers.

### Package Management

* **PackageService** — Upload DAR packages, list packages, manage package vetting
* **DarService** — Upload and manage DAR files

### Key Management

* **VaultService** — Manage cryptographic keys. Generate new keys, list existing keys, rotate keys. Supports external KMS integration.

### Pruning

* **PruningService** — Prune old ledger data to manage storage growth. Configure automatic pruning schedules.

### Repair

* **RepairService** — Low-level repair operations for disaster recovery. Import/export ACS snapshots, purge contracts.

<Warning>
  Repair operations can cause data inconsistencies if used incorrectly. Only use them when instructed by operational documentation or Digital Asset support.
</Warning>

## Canton Console Access

The Canton Console provides a more ergonomic interface to Admin API operations. See [Essential Commands](/docs/canton/global-synchronizer-canton-console-essential-commands) for commonly used console commands.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Example: list connected synchronizers via Canton Console
participant.synchronizers.list_connected

// Example: upload a DAR package
participant.participant1.dars.upload("dars/CantonExamples.dar")

// Example: check node health
participant.health.status
```

## Next Steps

* [API Reference](/docs/canton/api-reference) — Central hub for all generated API documentation, including the Ledger API
* [Canton Console](/docs/canton/global-synchronizer-canton-console-console-overview) — Interactive console access

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
