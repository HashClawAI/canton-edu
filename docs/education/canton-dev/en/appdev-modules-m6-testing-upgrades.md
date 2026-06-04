---
title: "Testing Upgrades"
slug: "appdev-modules-m6-testing-upgrades"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-testing-upgrades.md"
source_title: "Testing Upgrades"
tags:
  - appdev
  - modules
  - m6-testing-upgrades
---

# Testing Upgrades

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Upgrades

> Verifying upgrade compatibility, testing cross-version workflows, and regression testing strategies

Upgrading Daml packages across a distributed network leaves no room for guesswork. You need to verify both that the compiler accepts the upgrade and that workflows continue to function with mixed package versions.

## Type-Level Compatibility Tests

A type-level compatibility test checks whether the old and new versions of a package with the same name can coexist without breaking. The easiest way to test this during development is to use the `dpm upgrade-check` command.

It is also recommended to do this as part of CI by uploading both old and new versions to a fresh
participant node using the DAR files that will be in production. Ideally, these should be stored in a dedicated artifact repository, but given their small sizes (typically under 1 MB), they may also be checked into source control.

In practice, this means your CI pipeline should:

1. Build the v2 DAR with `dpm build`
2. Start a sandbox with `dpm sandbox`
3. Upload the production v1 DAR
4. Upload the v2 DAR
5. If both uploads succeed without errors, type-level compatibility is confirmed

## Workflow-Level Compatibility Tests

A workflow-level compatibility test verifies that core business processes continue to function correctly after an upgrade. A basic integration test should follow these steps:

1. Start the application with v2 software, but upload only the v1 DAR file to test backward compatibility.
2. Initialize the application and start one instance of every core workflow.
3. Upload the v2 DAR.
4. Update the configuration to instruct the backends to start using the v2 DAR.
5. Verify that the workflows remain in the correct state and can continue without issues.

For more complex upgrades, additional tests may be needed.

## Daml Script Upgrade Tests

Write Daml Script tests that explicitly test cross-version scenarios. The key patterns to cover:

### Creating v1 contracts, reading with v2

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testV1ContractWithV2Code : Script ()
testV1ContractWithV2Code = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  -- Create with v1 fields only
  cid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder; issuer
        product = "Widget"
        expiryDate = None  -- v2 field, set to None

  -- Fetch and verify v2 fields default correctly
  Some license <- queryContractId issuer cid
  assertMsg "expiryDate should be None" (license.info.expiryDate == None)
```

### Exercising v2 choices on existing contracts

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testNewChoiceOnExistingContract : Script ()
testNewChoiceOnExistingContract = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  cid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder; issuer
        product = "Widget"
        expiryDate = None

  -- Exercise the new v2 choice
  newCid <- submit issuer do
    exerciseCmd cid Renew with
      newExpiry = datetime 2026 Dec 31 0 0 0

  -- Verify result
  Some renewed <- queryContractId issuer newCid
  assertMsg "Should have expiry set"
    (renewed.info.expiryDate == Some (datetime 2026 Dec 31 0 0 0))
```

### Testing incompatible downgrades

True cross-version downgrade testing requires uploading both v1 and v2 DARs to a sandbox and exercising contracts across version boundaries. This cannot be done in a single Daml Script test because Daml Script runs within a single package version. Use the workflow-level testing approach described above: upload both DARs to a sandbox, create contracts with v2 data (non-`None` optional fields), then verify that v1 code fails to fetch them as expected.

## Regression Testing

Every upgrade should run your full existing test suite against the new package version. Your v1 tests should pass unchanged when run against v2 — if they don't, you have a backward-compatibility issue.

Structure your test packages so that regression tests are separate from upgrade-specific tests:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml/
├── v1/              # Production v1
├── v2/              # Production v2
└── test/
    ├── regression/  # Existing tests, run against v2
    └── upgrade/     # New tests for cross-version scenarios
```

## CI Integration

Add upgrade testing to your CI pipeline as a separate stage that runs after the standard build and test:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Standard build and test
dpm build
dpm test

# Upgrade compatibility
dpm sandbox &
SANDBOX_PID=$!

# Wait for sandbox to be ready (use a health check loop in production CI)
sleep 30

# Upload production v1 DAR
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @artifacts/v1.dar

# Upload v2 DAR — if this succeeds, type-level compatibility is confirmed
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @artifacts/v2.dar

# Run your project's upgrade test suite here

kill $SANDBOX_PID
```

## Next Steps

* [Deploying Upgrades](/appdev/modules/m6-deployment) — Rolling out tested upgrades across environments
* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — Reference for what changes are allowed

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
