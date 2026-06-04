---
title: "Error Handling"
slug: "appdev-modules-m7-error-handling"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-error-handling.md"
source_title: "Error Handling"
tags:
  - appdev
  - modules
  - m7-error-handling
---

# Error Handling

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Handling

> Error handling and recovery patterns for Canton applications

Canton applications deal with a distributed, multi-party ledger. Errors fall into distinct categories, and each category calls for a different recovery strategy. This page covers the error types you will encounter and how to handle them in your backend.

## Error Categories

### Command Rejection

A command is rejected when the Ledger API refuses it before the transaction reaches the synchronizer. Common causes:

* **INVALID\_ARGUMENT** -- The command payload does not match the template or choice signature (wrong field types, missing required fields)
* **NOT\_FOUND** -- The referenced contract ID does not exist or is not visible to the submitting party
* **PERMISSION\_DENIED** -- The authenticated party does not have authorization to perform the action

These errors indicate a bug in your application logic or stale data. Retrying the same command will produce the same result. Fix the root cause: correct the payload, re-query for a valid contract ID, or check party authorization.

### Contention

Contention occurs when two or more commands try to consume the same contract simultaneously. Only one succeeds; the others receive a **FAILED\_PRECONDITION** (or `ABORTED`) error indicating the contract was already archived.

This is normal in multi-party applications. Two users might try to exercise the same choice on the same contract at nearly the same time. Canton's consistency model ensures only one succeeds.

### Timeout

A command may time out if the synchronizer does not process it within the configured deadline. The `StatusRuntimeException` will have a `DEADLINE_EXCEEDED` code. Timeouts can occur during network congestion or when a counterparty's validator is slow to respond.

A timeout does **not** mean the command failed. It may have succeeded but the response did not arrive in time. Before retrying, check the completion stream or query PQS to determine whether the command was applied.

### Insufficient Traffic

If your validator's traffic budget is exhausted, command submissions fail with an error indicating insufficient traffic. This is not a transient error -- retrying will not help until the traffic budget is replenished (either manually or via auto-top-up).

See [Canton Coin and Traffic](/appdev/modules/m4-canton-coin) for how to manage traffic credits.

## Handling Contention

Contention on consuming contracts is the most common error pattern in Canton applications. The standard approach:

1. **Catch the error** -- Detect `FAILED_PRECONDITION` or `ABORTED` in the gRPC response
2. **Re-read the contract** -- Query PQS for the current state. The contract you targeted may have been archived, and a new contract (from the competing transaction) may now be active.
3. **Resubmit with a new command ID** -- Build a new command targeting the current contract and submit it with a fresh command ID

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
int maxRetries = 3;
for (int attempt = 0; attempt < maxRetries; attempt++) {
    try {
        var contract = damlRepository.findActiveAsset(assetId).join();
        if (contract.isEmpty()) {
            throw new NotFoundException("Asset no longer active");
        }
        ledger.exerciseAndGetResult(
            contract.get().contractId, choice, UUID.randomUUID().toString()
        ).join();
        return; // success
    } catch (CompletionException e) {
        if (isContention(e) && attempt < maxRetries - 1) {
            Thread.sleep((long) Math.pow(2, attempt) * 100); // exponential backoff
            continue;
        }
        throw e;
    }
}
```

Use exponential backoff between retries. Without backoff, competing commands will keep colliding.

### When Not to Retry

Do not retry on:

* **INVALID\_ARGUMENT** -- The command itself is wrong
* **PERMISSION\_DENIED** -- Authorization will not change between retries
* **Insufficient traffic** -- The issue is the traffic budget, not the command

## Idempotent Command Submission

The Ledger API deduplicates commands by their command ID. If you submit two commands with the same ID, the second is treated as a duplicate and returns the result of the first.

Use this to make your backend idempotent:

* Generate a deterministic command ID from the operation's inputs (e.g., hash of the user ID, action type, and a nonce from the frontend)
* If a network failure prevents you from receiving the response, resubmit with the same command ID
* The Ledger API returns the original result instead of executing the command twice

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
String commandId = "renew-license-" + licenseNum + "-" + requestNonce;
ledger.exerciseAndGetResult(contractId, renewChoice, commandId).join();
// Safe to retry with the same commandId if the response is lost
```

The deduplication window is configurable. The default is sufficient for most applications, but if your operations span long time periods, verify the window covers your retry horizon.

## Completion Stream Monitoring

The Ledger API's completion stream reports the final status of every submitted command. Subscribe to it for reliable outcome tracking:

* **Successful completions** confirm the transaction was committed
* **Failed completions** include the error code and details
* **Missing completions** (within the expected window) suggest the command was lost before reaching the synchronizer

In cn-quickstart, the synchronous `CommandService` (rather than `CommandSubmissionService`) waits for the completion internally and returns the result in a single round-trip. If you use the asynchronous `CommandSubmissionService` instead, you need to monitor completions yourself.

## Backend Recovery Patterns

### Startup Recovery

When your backend restarts, it may have in-flight commands whose outcomes are unknown. On startup:

1. Read the completion stream from the last known offset
2. Reconcile in-flight commands with their completion status
3. Retry any commands that were never submitted (no completion found and no matching contract in PQS)

### Circuit Breaker

If the Ledger API becomes unavailable (validator restart, network partition), wrap your submission logic in a circuit breaker. After a configurable number of consecutive failures, stop submitting and surface a service-unavailable error to callers. Periodically probe the Ledger API to detect recovery.

### Dead Letter Handling

Commands that fail after all retries should be logged with full context (command ID, template, choice, arguments, error) and sent to a dead letter queue or table. This provides an audit trail and enables manual intervention for edge cases.

## Further Reading

* [Backend Development](/appdev/modules/m4-backend-dev) -- Ledger API client setup, including error handling examples
* [Canton Coin and Traffic](/appdev/modules/m4-canton-coin) -- Managing traffic to avoid submission failures
* [Observability](/appdev/modules/m4-observability) -- Logging and metrics for error tracking

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
