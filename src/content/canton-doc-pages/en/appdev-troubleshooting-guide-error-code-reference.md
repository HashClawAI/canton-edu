---
title: "Daml Error Codes"
slug: "appdev-troubleshooting-guide-error-code-reference"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/error-code-reference.md"
source_title: "Daml Error Codes"
tags:
  - appdev
  - troubleshooting-guide
  - error-code-reference
---

# Daml Error Codes

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Daml Error Codes

> Reference for common error codes in Daml compilation, Canton runtime, and the Ledger API

This page lists error codes you are most likely to encounter during Canton Network application development, grouped by where they originate. Each entry includes the error message, its typical cause, and how to resolve it.

## Daml Compilation Errors

These errors appear when you run `dpm build` or compile Daml sources.

### Type mismatch

```
Couldn't match expected type 'X' with actual type 'Y'
```

**Cause:** A function argument or binding has the wrong type. Common cases include passing a `ContractId T` where `T` is expected (use `fetch`), or passing `Text` where `Party` is expected.

**Fix:** Check the type signatures of the function you are calling. Use `fetch` to convert a `ContractId` to its payload, or `getParty` to convert a `Text` to a `Party` in Daml Script.

### Missing field in record

```
Fields not initialised: 'fieldName'
```

**Cause:** You created a record or template instance without supplying all required fields.

**Fix:** Add the missing field to your record construction. If you recently added a field to a template, update all call sites.

### SCU compatibility violation

```
Upgrade check failed: field 'X' has changed type from 'A' to 'B'
```

**Cause:** A Smart Contract Upgrade compatibility check failed. SCU requires that new package versions are wire-compatible with previous versions. You cannot remove fields, change field types, or reorder fields.

**Fix:** Add new optional fields (with defaults) instead of modifying existing ones. If you need a fundamentally different structure, create a new template and migrate contracts explicitly.

### Deprecated exceptions warning

```
warning: Daml exceptions are deprecated
```

**Cause:** Your code uses `exception` declarations or `try/catch` blocks.

**Fix:** Replace exception-based error handling with `Either`, `Optional`, or explicit error contract patterns. Daml exceptions are deprecated and will be removed in a future release.

## Runtime Errors

These errors occur when transactions are submitted to a running Canton validator.

### INVALID\_ARGUMENT

```
INVALID_ARGUMENT: <detail>
```

**Cause:** The submitted command is malformed or violates a precondition. Sub-causes include:

* Missing required fields in a create or exercise command
* Invalid party identifier format
* Referencing a template that does not exist in the uploaded packages

**Fix:** Check the command payload against the Ledger API specification. Verify the template name, party identifiers, and all required fields are present and correctly typed.

### NOT\_FOUND

```
NOT_FOUND: CONTRACT_NOT_FOUND - Contract could not be found with id <contract-id>
```

**Cause:** The contract has already been archived (consumed by a previous exercise), or it was never visible to the submitting party.

**Fix:** Query the active contract set (ACS) to confirm the contract still exists before exercising. Implement a fetch-then-exercise pattern or handle this error with a retry that re-fetches the current contract ID.

### ALREADY\_EXISTS

```
ALREADY_EXISTS: CONTRACT_KEY_ALREADY_EXISTS - Contract key already exists
```

**Cause:** You attempted to create a contract whose key matches an already-active contract. Daml enforces key uniqueness per template within a party's visibility.

**Fix:** Check for existing contracts with the same key before creating. Use `lookupByKey` in Daml or query the ACS via the Ledger API. If you want to replace the existing contract, archive it first.

### ABORTED (contention)

```
ABORTED: Interpretation error: ... contract not active
```

**Cause:** A concurrent transaction consumed the contract between your read and your exercise. This is normal in concurrent environments.

**Fix:** Retry the operation with exponential backoff. See [Development Issues](/appdev/troubleshooting-guide/development-issues) for a retry pattern.

## Ledger API errors

Ledger API runtime error codes (AUTH\_INVALID\_TOKEN, PACKAGE\_NOT\_FOUND, PARTY\_NOT\_KNOWN, PERMISSION\_DENIED, etc.) live on their own page: [Ledger API Errors](/appdev/troubleshooting-guide/ledger-api-errors).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
