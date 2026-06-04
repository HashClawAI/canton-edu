---
title: "Smart Contract Upgrades in Production"
slug: "appdev-modules-m7-smart-contract-upgrades"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-smart-contract-upgrades.md"
source_title: "Smart Contract Upgrades in Production"
tags:
  - appdev
  - modules
  - m7-smart-contract-upgrades
---

# Smart Contract Upgrades in Production

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Contract Upgrades in Production

> Operational considerations for rolling out smart contract upgrades in production

Upgrading smart contracts in a running production environment is different from upgrading during development. Contracts are shared between parties, often across organizational boundaries, and an upgrade that works on your validator may behave differently when counterparties are running mixed versions. This page covers the operational side of production SCU rollouts.

## Before You Upgrade

### Pre-Upgrade Checklist

Before uploading a new package version to production:

* Verify the upgrade passes `dpm build` and `dpm test` in your CI pipeline
* Confirm the new package is SCU-compatible with the current version (run compatibility checks locally or in CI)
* Review the list of changes against the [upgrade limitations](/appdev/modules/m6-limitations) to ensure no breaking modifications
* Test the upgrade on DevNet or TestNet with realistic data volumes
* Communicate with counterparties who hold contracts affected by the upgrade (see below)
* Document the rollback procedure before starting

### Communicating with Counterparties

On Canton Network, your contracts may have signatories or observers hosted on other validators. When you upload a new package version, those validators also need the new package to interpret upgraded contracts correctly.

Steps:

1. **Notify counterparties** in advance. Share the new DAR file and a summary of changes.
2. **Agree on a rollout window**. All validators that host parties on affected contracts should upload the new package within a defined time period.
3. **Verify package availability**. After uploading, confirm that the new package ID is recognized by all relevant validators.

If a counterparty has not yet uploaded the new package and your application creates a contract under the new version, their validator will not be able to process it. The transaction will fail for that counterparty.

## During the Upgrade

### Uploading the Package

Upload the new DAR to your validator using the Admin API or your deployment tooling:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm deploy --target <validator-url> <dar-file>
```

The upload is non-destructive. The old package version remains available, and existing contracts under the old version continue to work. No downtime is required.

### Mixed-Version Deployments

After you upload a new package, the system enters a **mixed-version state**: some active contracts were created under the old version, and new contracts will be created under the new version.

How Canton handles this:

* **Existing contracts** remain associated with the package version under which they were created
* **New contracts** are created under the latest uploaded version
* **Exercising choices** on old-version contracts uses the new package's choice body if the contract template is SCU-compatible. The contract payload is interpreted against the new version's type definition.
* **Added optional fields** in the new version receive their default values when old contracts are read

This mixed state persists until all old-version contracts are archived (consumed or explicitly migrated). There is no automatic bulk migration.

### Monitoring the Rollout

Track these indicators during and after the upgrade:

* **Command error rates** -- Watch for spikes in `FAILED_PRECONDITION` or `INVALID_ARGUMENT` errors that might indicate compatibility issues
* **Contract version distribution** -- Query PQS to see how many active contracts remain on the old version vs. the new version
* **Counterparty readiness** -- Monitor whether transactions involving counterparties succeed or fail due to missing packages

A PQS query to check contract version distribution:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT package_id, count(*) AS active_count
FROM active('your-module:YourTemplate')
GROUP BY package_id;
```

## Rollback Procedures

SCU does not have a built-in rollback mechanism. Because packages cannot be removed once uploaded, "rolling back" means managing the situation rather than undoing the upload.

If the new version causes problems:

1. **Stop creating new contracts** under the problematic version. Update your backend to explicitly reference the old package version when creating contracts, if your tooling supports it.
2. **Investigate and fix** the issue in the new package, then upload a corrected version (version 3, effectively).
3. **Communicate with counterparties** so they are aware of the issue and can adjust their systems.

Because the old package version is still present, contracts created under it continue to function. The risk is primarily with new contracts or choices that exercise new-version-specific logic.

### When Rollback Is Not Enough

If the new version introduced a breaking change that was not caught in testing (this should be prevented by compatibility checks, but mistakes happen), you may need to:

* Upload a corrected package version
* Migrate affected contracts using explicit migration choices
* Align the migration with all counterparties who hold affected contracts

This is the most disruptive scenario and underscores the importance of thorough testing on DevNet/TestNet before production deployment.

## Operational Checklist

Use this checklist for each production upgrade:

* [ ] New DAR passes `dpm build` and `dpm test`
* [ ] Compatibility checks pass against the current production package
* [ ] Upgrade tested on DevNet or TestNet with realistic data
* [ ] Counterparties notified and rollout window agreed
* [ ] Rollback procedure documented
* [ ] Monitoring dashboards updated to track version-specific metrics
* [ ] DAR uploaded to production validator
* [ ] Counterparties confirmed their upload
* [ ] Error rates monitored for 24-48 hours post-upgrade
* [ ] Old-version contract migration plan in place (if applicable)

## Further Reading

* [Upgrade Limitations](/appdev/modules/m6-limitations) -- Constraints that affect production rollouts
* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) -- Testing strategies before going to production
* [Error Handling](/appdev/modules/m7-error-handling) -- Handling errors that may arise during mixed-version deployments
* [Deployment Progression](/appdev/modules/m5-deployment-progression) -- The DevNet to TestNet to MainNet path
* [Smart Contract Upgrading Reference](/appdev/deep-dives/smart-contract-upgrading-reference) — Detailed package validation and runtime upgrade rules.
* [Values in the Ledger API](/appdev/deep-dives/values-in-the-ledger-api) — How the Ledger API validates and normalizes values during command submission and query.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
