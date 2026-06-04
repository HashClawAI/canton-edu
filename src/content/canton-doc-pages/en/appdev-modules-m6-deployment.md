---
title: "Upgrade Deployment"
slug: "appdev-modules-m6-deployment"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-deployment.md"
source_title: "Upgrade Deployment"
tags:
  - appdev
  - modules
  - m6-deployment
---

# Upgrade Deployment

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Deployment

> Deploying Daml package upgrades across environments with coordination, rollback, and migration strategies

Deploying an upgrade means getting newer version packages onto all relevant validators and transitioning workflows from the current version to the new version. The distributed nature of Canton means you can't just flip a switch — you need to coordinate across organizations while keeping existing workflows running.

In the following discussion, the current version is `v1` and the new version is `v2`.

## Deployment Sequence

The deployment follows the asynchronous rollout model described in the [Overview](/docs/canton/appdev-modules-m6-overview):

1. **Upload v2 DAR to your own validator** — Upload the v2 package on your participant node. This doesn't affect other organizations yet.

2. **Distribute v2 DAR to counterparties** — Share the v2 DAR file with app users and other organizations. They need to upload it to their validators before v2 workflows can span multiple parties.

3. **Update backends to use v2** — Point your backend's Ledger API client at the v2 package. New contracts are now created with v2. Existing v1 contracts remain usable.  Note that the backend may need to work with both the v1 and v2 packages to minimize any downtime.

4. **Migrate existing contracts (if needed)** — For contracts that need v2 data, run migration automation that exercises upgrade choices to archive v1 contracts and create v2 replacements.

5. **Set a switch-over date** — Publish a target date for all parties to complete the transition. After this date, v1 workflows may be decommissioned by unvetting the v1 packages.

6. **Vet the new package** — AT the target date, all parties complete the transition by vetting the v2 package. After this date, v1 workflows may be decommissioned by unvetting the v1 packages.

7. **Unvet v1 (optional)** — Once all v1 contracts have been archived or migrated, unvet the v1 package to finalize the upgrade.

## Coordinating with Counterparties

Uncoordinated transitions to v2 workflows can cause command submission failures, resulting in workflows getting stuck. Common scenarios include:

* **Daml model version mismatch** — A command referencing v2 workflows fails if a stakeholder's participant node lacks the required v2 package or the v2 package is not vetted.  In this situation, the v1 version will be used if it remains vetted.
* **Explicit disclosure** — When a v2 contract is used in explicit disclosure, a command referencing it fails if the submitting party's participant node lacks the required v2 package.
  This occurs even if all stakeholders of the disclosed contract have uploaded v2.

To avoid these issues, communicate the upgrade timeline clearly:

* Distribute the v2 DAR file well before the switch-over date
* Provide instructions for uploading and vetting the DAR
* Give organizations enough time to test their own backends against v2
* Confirm readiness before exercising v2-only workflows

## Contract Migration Strategies

Not all contracts need explicit migration. Contract archival in Daml can happen through several paths:

* **Natural end of lifecycle** — The contract represents a business entity whose lifecycle has naturally ended (e.g., a loan fully repaid).
* **State no longer holds** — The contract attested to a state that is no longer valid.
* **Modification of the underlying entity** — The business entity is still relevant, but because Daml contracts are immutable, the update requires archiving the old contract. If the updated contract is created using v2, this results in organic, incremental migration away from v1.
* **Explicit upgrade** — The contract is archived as part of an upgrade process, ideally by an upgrade runner to automate the task.

The preferred approach is to handle versioning and upgrades directly in Daml rather than relying on external automation. However, in some cases a valid v2 can only be generated from a v1 in consultation with off-ledger systems or Active Contract Set (ACS) / PQS queries.

For backward-incompatible changes that require old v1 contracts to upgrade to v2 templates:

1. Add a consuming `Upgrade` choice to the v1 template that archives the old contract and creates an instance of the new template
2. Where necessary, provide reference data (such as default values) for the `Upgrade` choice via additional choice arguments
3. Use backend automation to iterate through the ACS and exercise the `Upgrade` choice on each contract

## Rollback Strategies

### Rollback by unvetting

For upgrades that do not modify the types of existing templates and choices, roll back by unvetting the v2 DAR package.  Use this approach if no contracts have been created with v2.

### Rollback by roll-forward

Rollback is more complex for upgrades that add new fields to existing templates. If at least one contract has been created using the new fields, those contracts cannot be read with the previous version of the Daml code. Instead:

1. Publish a new version of the DARs that disregards the newly added fields.
2. Introduce a `Downgrade` choice that resets the newly added fields to `None`.
3. Use backend automation to iterate through the ACS and invoke the `Downgrade` choice.

To avoid complex roll-forward rollbacks, consider splitting an upgrade into two steps:

1. An upgrade that adds new fields but does not use them. Since no changes are made to choices, this upgrade doesn't need rollback.
2. A separate upgrade that modifies choice implementations to use the new fields. If an issue arises, this upgrade can be rolled back by unvetting.

## Environment-by-Environment Rollout

Apply the standard promotion path from [Deployment Progression](/docs/canton/appdev-modules-m5-deployment-progression):

* **LocalNet** — Test the full upgrade cycle locally: upload v1, create contracts, upload v2, verify cross-version behavior, run migration automation.
* **DevNet** — Deploy the upgrade with a real counterparty. Verify that DAR distribution and mixed-version operation work across validators.
* **TestNet** — Run through the complete upgrade process including the coordinated switch-over date. This rehearsal catches coordination issues before MainNet.
* **MainNet** — Execute the upgrade plan with real counterparties and real contracts.

## Next Steps

* [Smart Contract Upgrades Overview](/docs/canton/appdev-modules-m6-overview) — Return to the module overview
* [Testing Upgrades](/docs/canton/appdev-modules-m6-testing-upgrades) — Verify upgrade paths before deployment
* [Deployment Progression](/docs/canton/appdev-modules-m5-deployment-progression) — General environment promotion strategy

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
