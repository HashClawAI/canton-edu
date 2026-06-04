---
title: "Package Naming"
slug: "appdev-modules-m6-package-naming"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-package-naming.md"
source_title: "Package Naming"
tags:
  - appdev
  - modules
  - m6-package-naming
---

# Package Naming

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Package Naming

> Naming conventions and package structure for Daml smart contract upgrades

Good package naming prevents confusion as your application evolves through multiple versions. A clear naming scheme communicates ownership, purpose, and version at a glance.

## Reverse DNS Convention

Avoid package name conflicts, particularly between packages published by different app providers. Follow the Java ecosystem’s convention of prefixing package names with the reverse Domain Name System (DNS) name of the app provider. For example, for the issuance workflows of the money market fund app provided by Acme Inc., the recommended <span class="title-ref">daml.yaml</span> configuration would be: <span class="title-ref">name: com-acme-money-market-fund-issuance</span>.

Daml package names use hyphens as separators (not dots). The reverse DNS prefix establishes organizational ownership, and the remaining segments describe the package's purpose.

```
com-acme-money-market-fund-issuance
com-acme-money-market-fund-trading
org-example-token-registry
```

## Version Markers in Package Names

Include a version marker in the package name when you anticipate breaking changes over the application's lifecycle. This makes it unambiguous which major version of a contract model a package represents:

```
com-acme-asset-main-v1
com-acme-asset-main-v2
com-acme-asset-interfaces-v1
```

The version marker refers to the **contract model version**, not the build version. Increment it only when you make breaking changes that require a new package (as described in
[Upgrade Limitations](/docs/canton/appdev-modules-m6-limitations)). Non-breaking upgrades (adding optional fields, new choices) happen within the same package name -- SCU handles those transparently.

Do not include version numbers in template names.

## Separating Interfaces from Templates

Split your Daml code into at least two packages:

* **Interface package** -- Contains interface definitions that form your public API. Other applications depend on this package to interact with your contracts.
* **Template package** -- Contains template definitions that implement the interfaces. This is your private implementation.

```
com-acme-asset-interfaces-v1    -- interfaces only
com-acme-asset-main-v1          -- templates implementing those interfaces
```

Why this separation matters:

* Interfaces are not upgradeable. Putting them in their own package means the template package can evolve independently (adding fields, choices, new templates) without touching the interface package.
* Other applications that depend on your interfaces only need to import the interface package. They do not take a dependency on your implementation details.
* When a breaking interface change is unavoidable, you publish `com-acme-asset-interfaces-v2` alongside `v1`. Consumers can migrate at their own pace.

## Breaking Changes via New Package Names

When SCU compatibility rules prevent an in-place upgrade (for example, you need to change a field type or remove a template), create a new package with an incremented version marker:

```
com-acme-asset-main-v1   -- original version
com-acme-asset-main-v2   -- breaking changes
```

Both packages coexist on the validator. Existing contracts under `v1` remain valid. You provide a migration path -- typically a choice on the `v1` template that archives the old contract and creates a `v2` replacement. Stakeholders exercise this choice to migrate their contracts.

This approach keeps the upgrade explicit. Stakeholders must consent to the migration because exercising the choice requires their authorization as signatories.

## Naming Checklist

When naming a new package, verify:

* The name starts with your organization's reverse DNS prefix
* The name includes a clear functional description (not just "main" or "core")
* Interface packages are named separately from template packages
* A version marker is present if breaking changes are foreseeable
* The name is consistent with your existing packages (same prefix style, same separator conventions)

## Example: Multi-Package Application

A real-world application might have:

```
com-acme-lending-interfaces-v1       -- public interfaces for loan contracts
com-acme-lending-main-v1             -- loan templates, choices, workflows
com-acme-lending-reporting-v1        -- reporting-specific templates
com-acme-lending-test-fixtures-v1    -- test data generators (not deployed to production)
```

Each package can be versioned independently. The interface package changes rarely. The main package changes with each feature release (non-breaking changes via SCU). The reporting package might lag behind. Test fixtures never leave the development environment.

## Further Reading

* [Upgrade Limitations](/docs/canton/appdev-modules-m6-limitations) -- Constraints that drive package naming decisions
* [Upgrade Compatibility](/docs/canton/appdev-modules-m6-upgrade-compatibility) -- Rules for what constitutes a breaking vs. non-breaking change
* [Building and Packaging](/docs/canton/appdev-modules-m3-building-packaging) -- How to compile and package Daml code with `dpm build`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
