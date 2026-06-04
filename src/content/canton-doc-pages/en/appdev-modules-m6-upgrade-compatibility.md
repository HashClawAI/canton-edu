---
title: "Upgrade Compatibility"
slug: "appdev-modules-m6-upgrade-compatibility"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-upgrade-compatibility.md"
source_title: "Upgrade Compatibility"
tags:
  - appdev
  - modules
  - m6-upgrade-compatibility
---

# Upgrade Compatibility

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Compatibility

> Allowed changes, breaking changes, and compatibility rules for Daml smart contract upgrades

SCU defines strict rules about which changes to Daml models are backward-compatible. The Daml compiler enforces these rules at build time — if your v2 package introduces a breaking change relative to v1, `dpm build` will reject it.

## Backward-Compatible Changes

### Adding Optional fields

`Optional` fields can be added to contracts, choice arguments, and choice return types.

When a component fetches a contract created from an older version, the newly introduced `Optional` fields default to `None`. This ensures older contracts remain readable after a template evolves.

When Daml code referencing an older version fetches a contract from a newer version, the fetch succeeds only if all unknown fields have the value `None`. If any unknown field contains a value other than `None`, the fetch fails. This prevents unintended data loss in workflows like archive-and-recreate.

<Note>
  When adding `Optional` fields to choice return types, the return type must be a Daml record (not a scalar, tuple, list, set, or map). It is to your advantage to design choices so that they are ready to gain return fields in the future, by using Daml-record return types right from the start of your design process.
</Note>

### Adding new constructors to variants

New constructors can be added to variant types, including enums. Using a new constructor value with code that expects the older version will fail, just as setting a new `Optional` field to a non-`None` value fails with older code.

### Adding new choices

For a new choice in v2 to be available on a given active v1 contract, all the validators of the stakeholders of that contract must have uploaded and vetted the v2 DAR files. The new choice must pass the mediator consensus layer, which requires all stakeholder validators to recognize the v2 package. Whether validators that are not stakeholders have uploaded the v2 DAR files has no influence on the availability of the new choice for that contract's stakeholders.

### Modifying existing choices

Controllers, observers, and the choice body can be updated for bug fixes or to handle new arguments. Existing choices cannot be removed — the compiler rejects this as a breaking change because existing code may reference these choices. To deprecate a choice, replace its body with `abort "Deprecated."`.

### Updating signatories, observers, and ensure clauses

The code for determining signatories, observers, and `ensure` clauses can be updated, but with restrictions. For existing contracts, the computed signatories and observers must remain unchanged. When a contract is fetched or exercised, Daml recomputes these values using the latest code and compares them to the original values. If they don't match, the transaction aborts.

The `ensure` clause is also recomputed and re-evaluated for existing contracts when they are fetched or exercised.

### Adding interface definitions and instances

New interface instances can be added to templates, but existing instances cannot be removed. Interface definitions themselves cannot be changed once deployed — always place interface definitions in a standalone package containing only interfaces and no templates.

Interface choices can be made inoperable by having them evaluate to `error "No longer implemented."`.

### Adding and deprecating templates

New templates can be added freely. Existing templates cannot be removed but can be deprecated by:

* Removing references to them from other Daml code
* Adding `ensure False` to make them non-operational (prevents new contract creation and choice exercises, including the implicit `Archive` choice)

<Warning>
  Adding `ensure False` leaves existing contracts on the ledger with no way to archive them. Only add `ensure False` after all active contracts created from the template have been archived through automation or normal business operations.
</Warning>

## Breaking Changes

These changes are **not** backward-compatible and will be rejected by the compiler:

* Removing fields from templates or choices
* Changing the type of an existing field
* Removing choices from templates
* Removing templates entirely
* Removing constructors from variant types
* Removing interface instances from templates
* Changing interface definitions

If you need to make a breaking change, create new templates with the desired structure and add `Upgrade` choices to the old templates that archive old contracts and create new ones. See [SCU compatibility rules](/docs/canton/appdev-modules-m6-writing-first-upgrade#step-3-verify-compatibility) for details on what the compiler checks.

## Backend Compatibility

You must use symbolic package references and not package IDs. These references take the form of `#package-name:module-name:template-id` for ledger reads to retrieve data from all contracts that are instances of the template with `module-name` and `template-id` of any version of the `package-name`.

Since newer versions of a template may introduce `Optional` fields that did not exist in earlier versions, the backend must handle cases where these fields are missing. The Daml SDK's codegens automatically set missing `Optional` fields to `None`.

## Package Naming

Avoid package name conflicts, particularly between packages published by different app providers. Follow the Java ecosystem's convention of prefixing package names with the reverse DNS name of the app provider. For example, for the issuance workflows of the money market fund app provided by Acme Inc., the recommended `daml.yaml` configuration would be: `name: com-acme-money-market-fund-issuance`.

## Compiler Version Considerations

The Daml compiler validates upgrade compatibility between v1 and v2 at build time. If the compiler version changes between when you built v1 and when you create v2, be aware that the compiler needs access to the compiled v1 DAR to perform its compatibility checks. The v2 package references v1 through the `upgrades` field in `daml.yaml`, which points to the v1 DAR file. As long as the v1 DAR is available, the newer compiler can validate the upgrade even if the v1 source code can no longer be compiled by the current compiler version.

## Next Steps

* [Writing Your First Upgrade](/docs/canton/appdev-modules-m6-writing-first-upgrade) — Step-by-step tutorial for creating a v2 package
* [Package Selection](/docs/canton/appdev-modules-m6-package-selection) — How the ledger resolves package versions

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
