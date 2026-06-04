---
title: "Smart Contract Upgrades Overview"
slug: "appdev-modules-m6-overview"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-overview.md"
source_title: "Smart Contract Upgrades Overview"
tags:
  - appdev
  - modules
  - m6-overview
---

# Smart Contract Upgrades Overview

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Contract Upgrades Overview

> Why smart contract upgrades matter and how Canton's upgrade model works

Canton applications evolve. Templates gain new fields, choices change behavior, and entirely new workflows get introduced. Smart Contract Upgrade (SCU) is the mechanism that makes this possible without breaking existing contracts or requiring coordinated downtime across organizations.  NOTE:  SCU has rules that need to be followed.

## Why Upgrades Are Different on Canton

On a traditional database, you run a migration script and the schema changes. On Canton, contracts are immutable and distributed across multiple organizations' validators. Changing a template's structure means every validator hosting parties that use that template needs to be aware of the change.

This creates a challenge: you can't force all organizations to upgrade simultaneously. SCU solves this by allowing multiple versions of a package to coexist on the ledger, with controlled rules for cross-version interaction.

## The Upgrade Model

The recommended approach combines an asynchronous rollout with a synchronous switch-over:

**Asynchronous rollout:**

1. The app provider implements and tests v2 app components.
2. The app provider makes the v2 components available to app users.
3. The app provider and users asynchronously roll out upgraded backends, frontends, audit the upgraded DAR packages, and then vet the packages.

The frontends and backends should support both v1 and v2 workflows, allowing the app provider and app users to deploy their updates independently on their own schedules. Mixed-version deployments are expected until all users switch to v2 workflows.

**Synchronous switch-over:**

1. The app provider publishes a target date for app users to complete the upgrade and decommission v1.
2. Shortly before the target upgrade date, the app provider and users coordinate to upload the v2 package (DAR) files to their validators.
3. At the predetermined time, they all vet the newly uploaded package(s) to make that version active.

## Package Versioning

Every Daml package has a name and version, defined in `daml.yaml`. When you upload a new version of a package (same name, higher version number), both versions exist on the ledger simultaneously. Existing contracts remain associated with the version that created them, but the ledger can resolve them against newer versions under SCU's compatibility rules.

This multi-version coexistence is the foundation of zero-downtime upgrades. Old contracts don't need to be migrated before the new version becomes active — they can be read and exercised through the newer version's code when compatibility permits.

## When to Use Upgrades vs. New Templates

Not every change requires the upgrade mechanism. Consider the trade-offs:

**Use SCU when:**

* You're adding optional fields to existing templates
* You're adding new choices to existing templates
* You need existing contracts to work with new code without migration
* You want zero-downtime deployment

**Use new templates when:**

* The change is fundamentally incompatible (removing fields, changing types)
* The new workflow is logically distinct from the old one
* You want a clean separation between old and new behavior

## Key Challenges

* **Asynchronous rollouts** — App providers and app users often cannot upgrade simultaneously. Upgrades must allow independent deployment schedules.
* **Mixed-version deployments** — Due to asynchronous rollouts, the application must temporarily support mixed-version deployments across organizations. Backends and frontends must remain compatible with both v1 and v2 DAR workflows.
* **Zero-downtime upgrades** — Certain workflows may need to progress 24/7 without interruption. SCU and the asynchronous rollout approach enable workflows to continue uninterrupted during the upgrade process.

## Module Structure

This module walks you through the upgrade process step by step:

<CardGroup cols={2}>
  <Card title="Upgrade Compatibility" icon="code-compare" href="/appdev/modules/m6-upgrade-compatibility">
    What changes are allowed and what breaks compatibility.
  </Card>

  <Card title="Writing Your First Upgrade" icon="pen" href="/appdev/modules/m6-writing-first-upgrade">
    Step-by-step tutorial for creating a v2 package.
  </Card>

  <Card title="Package Selection" icon="list-check" href="/appdev/modules/m6-package-selection">
    How the ledger resolves which package version to use.
  </Card>

  <Card title="Testing Upgrades" icon="vial" href="/appdev/modules/m6-testing-upgrades">
    Verifying upgrade paths before deployment.
  </Card>

  <Card title="Deploying Upgrades" icon="rocket" href="/appdev/modules/m6-deployment">
    Rolling out upgrades across environments and organizations.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
