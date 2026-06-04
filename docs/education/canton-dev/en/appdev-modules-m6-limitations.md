---
title: "Upgrade Limitations"
slug: "appdev-modules-m6-limitations"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-limitations.md"
source_title: "Upgrade Limitations"
tags:
  - appdev
  - modules
  - m6-limitations
---

# Upgrade Limitations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Limitations

> Known limitations and constraints of Daml smart contract upgrades

Smart contract upgrades (SCU) in Daml are powerful but have firm boundaries. Understanding these limitations upfront prevents surprises during development and production rollouts.

## Packages Cannot Be Removed

Once you upload a DAR (Daml Archive) package to a validator, it stays there permanently. There is no mechanism to delete or unregister a package. This means:

* Every version of your package that was ever uploaded remains available
* The validator's package store grows over time
* You cannot revert a package upload

Plan your package uploads carefully, especially on MainNet where every uploaded package persists indefinitely.

## Template Removal Is Not Possible

You cannot remove a template from a package in a later version. If version 1 defines templates `Asset` and `LegacyAsset`, version 2 must still include both.

### Deprecating a Template

### Adding and Deprecating Templates

New templates can be added. Existing templates cannot be removed but can be deprecated by:

* Removing references to them from other Daml code.
* Adding `ensure False` to make them non-operational. This prevents new contract creation using the template and choice exercises, including the implicit <span class="title-ref">Archive</span> choice, on existing contracts created using the template.

Note that the latter approach may result in a large number of active contracts stored on the ledger without a way to archive them, unless another update is deployed to evaluate the
`ensure` clause to `True`. To deprecate a template without leaving contracts on the ledger that cannot be archived,
add `ensure False` to the template only after all active contracts created from it have been archived through automation or other means.

#

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template LegacyAsset
  with
    owner : Party
    value : Decimal
  where
    signatory owner
    ensure False  -- No new contracts can be created
```

## Removing Fields, Choices, or Variant Constructors Is Not Allowed

SCU compatibility rules prohibit removing:

* **Fields from a template** -- You can add optional fields (with defaults) but cannot remove existing ones
* **Choices from a template** -- Once a choice exists, it must remain in all future versions
* **Constructors from a variant type** -- Variant types can gain new constructors but not lose existing ones

These rules ensure that contracts created under an older package version remain valid and exercisable under the new version. If a validator still holds contracts from version 1,
those contracts must be interpretable by the version 2 package.

## Changing Field Types Is Restricted

You cannot change the type of an existing field. If `amount` is a `Decimal` in version 1, it must remain a `Decimal` in version 2. Type changes are breaking modifications that would make existing contracts unreadable.

## What You Can Do

For contrast, these modifications are allowed across package versions:

* Add new templates
* Add new optional fields to existing templates (with default values)
* Add new choices to existing templates
* Add new variant constructors
* Add new interface implementations (on new templates only)
* Change choice bodies (the implementation logic)

## Planning Around Limitations

### Manage Backward-Incompatible Changes

Not all changes can maintain backward compatibility. The strategy for updating Daml models follows principles similar to how APIs evolve in a service-based architecture.

Only backward-compatible changes are allowed for existing APIs, that is for the current Daml code. Introduce backward-incompatible changes by creating changing APIs, such as removing a parameter in a choice. To implement backwards-incompatible upgrades:

* Introduce the new templates with the backwards incompatible change with a consuming `Upgrade` choice to existing templates. This choice archives the old contract and creates an instance of the new template, ensuring a backwards-compatible upgrade.
* Where necessary, provide reference data, such as default values, for `Upgrade` choices via additional choice arguments.
* Use backend automation to migrate old contracts to new ones. The process may incur downtime on workflows until the contracts are converted by the automation.

This approach is explicit and requires active cooperation from contract stakeholders, which is a feature -- stakeholders always consent to changes that affect their contracts.

## Further Reading

* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) -- Full compatibility rules for SCU
* [Package Naming](/appdev/modules/m6-package-naming) -- Naming conventions that account for breaking changes
* [Smart Contract Upgrades in Production](/appdev/modules/m7-smart-contract-upgrades) -- Operational considerations for rollouts

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
