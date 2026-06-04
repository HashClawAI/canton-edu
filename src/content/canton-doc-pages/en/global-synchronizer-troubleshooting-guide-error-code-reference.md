---
title: "Common Error Codes"
slug: "global-synchronizer-troubleshooting-guide-error-code-reference"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/error-code-reference.md"
source_title: "Common Error Codes"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - error-code-reference
---

# Common Error Codes

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Error Codes

> Common Canton and Splice error codes with causes and resolution steps

Canton and Splice error codes follow a structured format: `CATEGORY_ERROR_NAME(severity, retryability)`. The severity ranges from 0 (informational) to 9 (critical). A retryability of `0` means the error is not retriable; other values indicate the error category for retry logic.

This page lists the error codes most frequently encountered by validator operators.

## Participant Errors

### PARTICIPANT\_TOPOLOGY\_UNKNOWN\_PARTIES

* **Message:** `Parties not known on synchronizer`
* **Cause:** The party referenced in a command has not been registered on the synchronizer. This happens when a party is created locally but the topology transaction has not yet propagated.
* **Resolution:** Wait a few seconds for topology propagation. If the error persists, verify the party is enabled on your validator with `participant.parties.list()` in Canton Console.

### PARTICIPANT\_PRUNING\_NOT\_SUPPORTED\_IN\_COMMUNITY

* **Message:** `Pruning is not supported in the community edition`
* **Cause:** You are running Canton Community Edition, which does not support pruning.
* **Resolution:** Upgrade to Canton Enterprise, which is required for Global Synchronizer validators.

### PARTICIPANT\_TRAFFIC\_BELOW\_LIMIT

* **Message:** `Insufficient traffic for submission`
* **Cause:** Your validator's traffic balance is too low to submit the transaction to the sequencer.
* **Resolution:** Purchase additional traffic via the validator API or enable auto-top-up. See [Transaction Failures](/global-synchronizer/troubleshooting-guide/transaction-failures) for details.

## Sequencer Errors

### SEQUENCER\_REQUEST\_REFUSED

* **Message:** `The sequencer refused to sequence the send request`
* **Cause:** The sequencer rejected the message. Common reasons: the sender is not registered, the message exceeds the maximum size, or the sender's traffic balance is insufficient.
* **Resolution:** Check that your validator is properly onboarded and has sufficient traffic. If the message is large, consider splitting it into smaller transactions.

### SEQUENCER\_SUBSCRIPTION\_LOST

* **Message:** `Lost subscription to sequencer`
* **Cause:** The gRPC stream to the sequencer was interrupted. Network instability, sequencer restarts, or load balancer timeouts can cause this.
* **Resolution:** The validator reconnects automatically. If it does not, check network connectivity to the sequencer and restart the validator.

### SEQUENCER\_TOMBSTONED\_MEMBER

* **Message:** `Member has been tombstoned`
* **Cause:** Your validator was evicted from the synchronizer, typically due to prolonged inactivity or a governance decision.
* **Resolution:** Contact your SV sponsor to understand why the eviction occurred and whether re-onboarding is possible.

## Mediator Errors

### MEDIATOR\_SAYS\_TX\_TIMED\_OUT

* **Message:** `Rejected transaction as the mediator did not receive sufficient confirmations within the expected timeframe`
* **Cause:** One or more parties failed to confirm the transaction in time. The `unresponsiveParties` field in the error context identifies which parties did not respond.
* **Resolution:** If the unresponsive party is yours, check your validator's health, traffic balance, and database performance. If it is a counterparty, contact their operator.

### MEDIATOR\_INVALID\_MESSAGE

* **Message:** `The mediator received an invalid message`
* **Cause:** A protocol-level error, usually caused by a version mismatch between the sender and the mediator.
* **Resolution:** Verify your validator is running the same protocol version as the network. Upgrade if you are behind.

## ACS Commitment Errors

### ACS\_COMMITMENT\_MISMATCH

* **Message:** `ACS commitment mismatch detected`
* **Cause:** Your validator's Active Contract Set (ACS) state does not match the expected commitment. This is a serious consistency issue.
* **Resolution:** This error requires investigation. Check for database corruption or incomplete synchronizer migration. Capture full logs and contact [da-support@digitalasset.com](mailto:da-support@digitalasset.com) with the details.

### ACS\_COMMITMENT\_DEGRADATION

* **Message:** `ACS commitment computation is degraded`
* **Cause:** The commitment computation could not complete in time, usually because the database is overloaded.
* **Resolution:** Check database performance. Ensure pruning is enabled and running. Increase database IOPS if necessary.

## General Errors

### GENERIC\_CONFIG\_ERROR

* **Message:** `Cannot convert configuration`
* **Cause:** A configuration value is missing, empty, or of the wrong type. The error message includes the specific configuration path.
* **Resolution:** Check the path mentioned in the error against your configuration files and environment variables. See [Configuration Problems](/global-synchronizer/troubleshooting-guide/configuration-problems).

### DB\_STORAGE\_DEGRADATION

* **Message:** `Database storage is degraded`
* **Cause:** Database queries are taking longer than expected. The connection pool may be saturated.
* **Resolution:** Check database disk space, IOPS, and active query count. Enable pruning if table sizes are large.

### PACKAGE\_SELECTION\_FAILED

* **Message:** `No package found for module`
* **Cause:** The required Daml package is not uploaded or not vetted on one of the involved validators.
* **Resolution:** Upload and vet the DAR file on your validator. Coordinate with counterparties to do the same on theirs.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
