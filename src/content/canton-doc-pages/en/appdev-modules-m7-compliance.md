---
title: "Compliance Considerations"
slug: "appdev-modules-m7-compliance"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-compliance.md"
source_title: "Compliance Considerations"
tags:
  - appdev
  - modules
  - m7-compliance
---

# Compliance Considerations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Compliance Considerations

> Privacy, audit, and regulatory considerations for Canton applications

Canton's architecture provides built-in privacy and audit properties that differ substantially from public blockchains. This page summarizes the compliance-relevant characteristics you should understand when building applications on Canton Network.

<Warning>
  This page provides technical facts about Canton's capabilities. It is not legal advice. Consult qualified legal counsel for regulatory compliance in your jurisdiction.
</Warning>

## Privacy Properties

### Sub-Transaction Privacy

Canton does not broadcast transactions to all validators. Each transaction is decomposed into **views**, and each validator receives only the views relevant to its hosted parties. A validator that is not a stakeholder in a particular part of a transaction sees nothing about that part -- not the payload, not the parties involved, not even the fact that it exists.

This means:

* Contract data is visible only to signatories, observers, and controllers defined in the Daml template
* The synchronizer (sequencer and mediator) processes encrypted messages and never sees plaintext transaction data
* Validators store only the contracts and transactions that involve their hosted parties

For a detailed explanation of visibility rules, see [Privacy Model Explained](/docs/canton/overview-learn-privacy-model).

### No Global State Visibility

Unlike public blockchains where any participant can read the full ledger, Canton validators maintain private, local ledger shards. There is no shared database of all contracts. A party cannot query contracts it is not entitled to see, and a validator cannot access data belonging to parties it does not host.

## Audit Capabilities

### Ledger API Transaction History

Each validator maintains a complete, append-only history of transactions involving its hosted parties. Applications can read this history through the Ledger API's update stream, which provides a chronological record of every contract creation, choice exercise, and archival visible to the querying party.

### PQS for Historical Queries

The Participant Query Store (PQS) maintains a PostgreSQL database that mirrors the ledger state. PQS stores both the current active contract set and the full history of contract events. This makes it suitable for audit queries:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find all archived contracts of a given template, with timestamps
SELECT contract_id, payload, created_at, archived_at
FROM contracts('your-module:YourTemplate')
WHERE archived_at IS NOT NULL
ORDER BY archived_at DESC;
```

PQS retains data for as long as the underlying PostgreSQL database is maintained. You control the retention policy.

### Auditor Patterns in Daml

You can grant audit access at the smart contract level by adding an auditor party as an observer. The auditor sees the contract and all events that affect it, without being able to modify it. See the [Privacy Model](/docs/canton/overview-learn-privacy-model) page for code examples of auditor patterns.

## Data Residency

### Private Synchronizers

If your regulatory environment requires data to stay within a specific geographic region, you can operate a **private synchronizer** that runs in your chosen jurisdiction. Validators connected to a private synchronizer communicate only through that synchronizer's infrastructure, which you control.

A validator can be connected to both the Global Synchronizer (for cross-network interoperability) and one or more private synchronizers (for jurisdiction-specific workflows). The multi-synchronizer architecture lets you separate regulated workflows from public ones without running separate infrastructure for each.

### Validator-Level Data Control

Since validators store only data for their hosted parties, your organization's data resides on your validator infrastructure. You choose where that infrastructure runs -- on-premises, in a specific cloud region, or across multiple locations. No other validator holds a copy of your data unless the other validator hosts a party that is a stakeholder on a shared contract.

## Immutable Ledger and Data Modification Requests

Canton's ledger is append-only. Contracts are never modified in place; they are archived and replaced. Transaction history cannot be rewritten.

For regulations that require data modification or deletion (such as GDPR's right to erasure), consider:

* **Contract design** -- Store personally identifiable information (PII) off-ledger, referenced by an opaque identifier on-ledger. Deleting the off-ledger data makes the on-ledger reference meaningless.
* **PQS data management** -- PQS is a projection that you control. You can purge or anonymize records in the PQS database without affecting the ledger itself.
* **Pruning** -- Canton supports ledger pruning, which removes old transaction data from the validator's local store after a configurable retention period. Pruned data is no longer accessible through the Ledger API.

These are technical mechanisms. Whether they satisfy specific regulatory requirements depends on the regulation and your legal counsel's interpretation.

## Application Design Guidelines

* Use Daml's signatory/observer model to enforce data visibility rules at the contract level, not just at the application layer
* Add auditor parties as observers on contracts that require audit trails
* Store sensitive PII off-ledger and reference it by ID on-ledger
* Use private synchronizers for workflows with strict data residency requirements
* Configure ledger pruning retention periods according to your regulatory obligations

## Further Reading

* [Privacy Model Explained](/docs/canton/overview-learn-privacy-model) -- Full details on sub-transaction privacy
* [Security Best Practices](/docs/canton/appdev-modules-m7-security) -- Securing your Canton application
* [Architecture Overview](/docs/canton/overview-learn-architecture) -- How validators and synchronizers relate

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
