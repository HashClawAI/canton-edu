---
title: "Writing Your First Upgrade"
slug: "appdev-modules-m6-writing-first-upgrade"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-writing-first-upgrade.md"
source_title: "Writing Your First Upgrade"
tags:
  - appdev
  - modules
  - m6-writing-first-upgrade
---

# Writing Your First Upgrade

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Writing Your First Upgrade

> Step-by-step tutorial for creating a v2 Daml package with backward-compatible changes

This tutorial walks you through creating a v2 version of a Daml package. You'll start with a simple template, add an optional field and a new choice, then verify that the upgrade compiles and that existing contracts work with the new code.

## Prerequisites

* A working `dpm` installation with the Daml SDK
* Familiarity with Daml templates and choices ([Module 3](/appdev/modules/m3-contract-templates))
* A text editor or Daml Studio

## Step 1: Create the v1 Package

Start by scaffolding a new project. The `dpm new` command creates the directory structure and a `daml.yaml` file:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm new com-example-licensing
```

For this tutorial, set up the directory structure manually to keep things explicit:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
mkdir -p daml/v1/daml
```

Create `daml/v1/daml.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v1/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 1.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
```

Create `daml/v1/daml/Main.daml`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v1/daml/Main.daml
module Main where

data LicenseInfo = LicenseInfo
  with
    holder : Party
    issuer : Party
    product : Text
  deriving (Eq, Show)

template License
  with
    info : LicenseInfo
  where
    signatory info.issuer
    observer info.holder

    choice Revoke : ()
      controller info.issuer
      do pure ()
```

Build and verify:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v1
dpm build
```

<Note>
  The SDK also provides a built-in upgrades example template you can generate with `dpm new upgrade-demo --template upgrades-example`. See [the example source](https://github.com/digital-asset/daml/tree/main/sdk/docs/source/sdk/sdlc-howtos/smart-contracts/upgrade/example) for details.
</Note>

## Step 2: Create the v2 Package

Copy the package — `cp -r v1 v2` — and bump the version. The package name must stay the same — this is how Daml knows it's an upgrade:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v2/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 2.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
upgrades: ../v1/.daml/dist/com-example-licensing-1.0.0.dar
```

The `upgrades` field points to the v1 DAR. This is what tells `dpm build` to validate that v2 is a compatible upgrade of v1.

Now make backward-compatible changes. Add an `Optional` field to the record and a new choice to the template:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v2/daml/Main.daml
module Main where

data LicenseInfo = LicenseInfo
  with
    holder : Party
    issuer : Party
    product : Text
    expiryDate : Optional Time  -- NEW: optional expiry date
  deriving (Eq, Show)

template License
  with
    info : LicenseInfo
  where
    signatory info.issuer
    observer info.holder

    choice Revoke : ()
      controller info.issuer
      do pure ()

    -- NEW: choice to renew the license with an expiry date
    choice Renew : ContractId License
      with
        newExpiry : Time
      controller info.issuer
      do create this with
           info = info with expiryDate = Some newExpiry
```

The changes follow SCU compatibility rules:

* `expiryDate` is an `Optional` field with implicit `None` default for v1 contracts
* `Renew` is a new choice (doesn't exist in v1, so no backward-compatibility issue)

## Step 3: Verify Compatibility

Build the v2 package:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v2
dpm build
```

If the build succeeds, the compiler has verified that v2 is a valid upgrade of v1. The `upgrades` field in `daml.yaml` triggers this check — without it, `dpm build` compiles v2 in isolation and performs no cross-version validation. The compiler checks all the SCU rules: no removed fields, no type changes, new fields are `Optional`, etc.

If you've introduced a breaking change, the compiler will report an error telling you what rule was violated.

## Step 4: Test Approximated Cross-Version Behavior

To verify the upgrade path, add a test script to the v2 package. First, add the `daml-script` dependency to `daml/v2/daml.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v2/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 2.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
  - daml-script
upgrades: ../v1/.daml/dist/com-example-licensing-1.0.0.dar
```

Then create a test script that simulates a v1 contract (with `expiryDate = None`) and exercises the new v2 `Renew` choice:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v2/daml/UpgradeTest.daml
module UpgradeTest where

import Main
import Daml.Script
import DA.Date (Month(..), datetime)

testUpgradePath : Script ()
testUpgradePath = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  -- Create a contract with no expiryDate (simulating a v1 contract)
  licenseCid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder
        issuer
        product = "Widget Pro"
        expiryDate = None

  -- Exercise the new v2 Renew choice
  newLicenseCid <- submit issuer do
    exerciseCmd licenseCid Renew with
      newExpiry = datetime 2026 Dec 31 0 0 0

  -- Verify the renewed license has the expiry set
  Some renewed <- queryContractId holder newLicenseCid
  assertMsg "Should have expiry"
    (renewed.info.expiryDate == Some (datetime 2026 Dec 31 0 0 0))
```

Run the test from the v2 package directory:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v2
dpm test
```

<Note>
  This test runs within a single package version, so it approximates rather than fully reproduces cross-version behavior. On a real ledger with both v1 and v2 DARs uploaded, the runtime handles the version resolution between actual v1 contracts and v2 code. See [Testing Upgrades](/appdev/modules/m6-testing-upgrades) for strategies to test real cross-version scenarios.
</Note>

## Step 5: Deploy Both Versions

In a real deployment, you may have both DAR files uploaded to your validator. The order matters: upload v1 first (if not already uploaded), then v2.  For new validators, they only need to upload v2 provided that it is SCU compatible with v1.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Upload v1 (if not already on the ledger)
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @daml/v1/.daml/dist/com-example-licensing-1.0.0.dar

# Upload v2
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @daml/v2/.daml/dist/com-example-licensing-2.0.0.dar
```

Once v2 is uploaded and vetted on all stakeholders' validators, the new choice becomes available on existing v1 contracts.

## What Happens Under the Hood

When a validator receives a v2 DAR:

1. If automatic vetting is enabled, the validator node vets the new package alongside v1.  Otherwise, vetting must be manually done.
2. Both packages remain active — v1 contracts aren't affected
3. When v2 code fetches a v1 contract, the runtime fills `Optional` fields with `None`
4. When v1 code fetches a v2 contract where `Optional` fields are `None`, the fetch succeeds (the fields are simply ignored)
5. When v1 code fetches a v2 contract where an `Optional` field has a non-`None` value, the fetch fails to prevent data loss

This design ensures that mixed-version operation is safe: no data is silently lost, and incompatible interactions fail explicitly rather than corrupting state.

See [Package Selection](/appdev/modules/m6-package-selection) to learn how different versions are resolved at runtime.

## Next Steps

* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — Full reference of allowed and disallowed changes
* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — Comprehensive upgrade testing strategies
* [Deploying Upgrades](/appdev/modules/m6-deployment) — Rolling out upgrades across environments

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
