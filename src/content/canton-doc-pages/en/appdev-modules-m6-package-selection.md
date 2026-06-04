---
title: "Package Selection"
slug: "appdev-modules-m6-package-selection"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-package-selection.md"
source_title: "Package Selection"
tags:
  - appdev
  - modules
  - m6-package-selection
---

# Package Selection

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Package Selection

> How the Canton ledger resolves which package version to use when multiple versions coexist

When multiple versions of a package are uploaded to a validator, the validator needs rules for deciding which version to execute. Package selection determines this — it governs how the Daml runtime resolves templates and choices when both v1 and v2 packages are available.

## How Version Resolution Works

Every contract on the ledger is associated with the package version that created it. When you fetch or exercise a contract, the runtime uses the package version referenced in your code, not necessarily the version that created the contract.

The resolution follows these rules:

* **Creating contracts** — The runtime uses the package version your code references. If your backend imports v2, new contracts are created with v2.
* **Fetching contracts** — The runtime evaluates the contract's data against the version your code references. SCU and vetting rules determine whether the fetch succeeds (see [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility)).
* **Exercising choices** — The choice body from the version your code references is executed, not the version that created the contract. This means bug fixes in v2 choices apply to v1 contracts.

## Symbolic Package References

Do not hardcode a specific package version in your backend. Use symbolic package references in your Ledger API queries. Instead of specifying a particular package ID, you reference a package by name:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
#com-example-licensing:Main:License
```

This tells the Ledger API to match contracts from any version of the `com-example-licensing` package that contains a `Main.License` template. Your backend receives contracts from both v1 and v2 without needing separate query logic for each version.

Without symbolic references, you'd need to update your backend's query filters every time you upload a new package version — defeating the purpose of seamless upgrades.

## Multi-Version Coexistence

Both v1 and v2 packages remain active on the ledger after uploading v2. This means:

* Contracts created with v1 continue to exist and can be fetched, exercised, and archived
* New contracts can be created with either v1 or v2 (depending on which version your code references)
* Different organizations can use different versions simultaneously during the rollout period

The ledger doesn't automatically migrate v1 contracts to v2. A v1 contract stays a v1 contract until it's archived. If you need contracts to gain v2 data (like a newly added `Optional` field with a non-`None` value), you must archive the v1 contract and create a new v2 contract — either through normal business operations or through an explicit upgrade choice.

## Package Vetting

Vetting a package allows other participant nodes to determine which workflows the parties on the participant can engage in. A package cannot be used until it is vetted, providing an additional verification step in the deployment process. By default, when a Daml package is uploaded, the participant node automatically marks it as vetted and publishes its vetting status on the synchronizer.

Packages can also be unvetted. For example, after uploading and vetting v2, unvetting v1 signals that the participant node can no longer participate in v1 workflows, finalizing the upgrade process.

A participant node must fully upgrade all its v1 contracts before unvetting v1 to avoid potential issues.
A contract created with V1 of a template can be used/upgraded with/to V2, even though V1 was unvetted provided that V2 is vetted.

## Cross-Version Fetch Behavior

The runtime uses whatever package version your code references. There is no automatic "preference" for newer versions — the version used depends on which package your code was compiled against. The cross-version behavior follows these rules:

* If you fetch a `License` using v2 code, and the contract was created with v1, the runtime applies v2 logic (filling new `Optional` fields with `None`)
* If you fetch a `License` using v1 code, and the contract was created with v2 where new fields are `None`, the runtime applies v1 logic (ignoring unknown fields)
* If you fetch a `License` using v1 code, and the contract was created with v2 where new fields have non-`None` values, the fetch fails to prevent data loss

The system fails safely when versions are incompatible rather than silently dropping data.

## Next Steps

* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — Verify that version resolution works correctly for your upgrade
* [Deploying Upgrades](/appdev/modules/m6-deployment) — Coordinate package uploads across validators

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
