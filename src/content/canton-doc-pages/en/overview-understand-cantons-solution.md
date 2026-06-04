---
title: "Canton's Solution: Three Pillars"
slug: "overview-understand-cantons-solution"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/cantons-solution.md"
source_title: "Canton's Solution: Three Pillars"
tags:
  - overview
  - understand
  - cantons-solution
---

# Canton's Solution: Three Pillars

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton's Solution: Three Pillars

> How Canton achieves privacy without sacrificing integrity

Canton resolves the privacy-integrity tradeoff through three architectural pillars that work together to provide both strong privacy guarantees and blockchain-grade integrity.

## Pillar 1: Sub-Transaction Privacy

Canton's core innovation is **sub-transaction privacy**. This works at two levels:

1. **Transaction isolation**: Different transactions are kept completely separate—unrelated parties don't even know other transactions exist
2. **View decomposition**: Within a single transaction, different parties see only their relevant portions

### How Views Work

When a transaction involves multiple parties, Canton doesn't send the entire transaction to everyone. Instead:

1. **Decomposition**: The transaction is split into views based on stakeholder relationships
2. **Encryption**: Each view is encrypted for its specific recipients
3. **Distribution**: The synchronizer delivers only entitled views to each participant
4. **Validation**: Each participant validates their view independently
5. **Confirmation**: Participants confirm based on their view alone

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph TX[Transaction]
        direction TB
        A1[Alice → Bob]
        A2[Bob → Charlie]
    end

    TX --> DECOMP[Decompose]

    DECOMP --> VA[Alice's View<br>Sees: Alice → Bob]
    DECOMP --> VB[Bob's View<br>Sees: Both]
    DECOMP --> VC[Charlie's View<br>Sees: Bob → Charlie]
```

In this example, a single atomic transaction moves value from Alice to Bob to Charlie. But Alice never learns about Charlie, and Charlie never learns about Alice.

### What Each Party Sees

| Party            | Sees                             | Doesn't See                                  |
| ---------------- | -------------------------------- | -------------------------------------------- |
| **Alice**        | Her payment to Bob               | Bob's payment to Charlie; Charlie's identity |
| **Bob**          | Both payments (involved in both) | Nothing hidden                               |
| **Charlie**      | His receipt from Bob             | Alice's involvement; original source         |
| **Synchronizer** | Encrypted messages only          | Any transaction content                      |

This isn't just hiding data—it's providing mathematically enforced boundaries on information flow.

## Pillar 2: Proof of Stakeholder Consensus

Traditional blockchains require all validators to verify all transactions. Canton uses a different approach: **only the stakeholders in a transaction need to confirm it**.

### Why This Works

Consider: why does a validator need to verify a transaction they're not part of?

In traditional blockchains, validators verify everything to prevent double-spends and ensure rules are followed. But if only Alice and Bob are affected by a transaction, only Alice and Bob need to verify it. As long as:

* Alice's validator confirms Alice authorized the transaction
* Bob's validator confirms Bob is receiving what he's supposed to
* Both agree the transaction is valid

Then the transaction is valid. Charlie's validator doesn't need to see it, verify it, or even know it exists.

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequenceDiagram
    participant Alice as Alice's Validator
    participant Sync as Synchronizer
    participant Bob as Bob's Validator

    Alice->>Sync: Submit encrypted transaction
    Sync->>Sync: Order and timestamp
    Sync->>Alice: Deliver Alice's view
    Sync->>Bob: Deliver Bob's view
    Alice->>Sync: Confirmation
    Bob->>Sync: Confirmation
    Sync->>Alice: Commit
    Sync->>Bob: Commit

    Note over Alice,Bob: Only involved parties<br/>participate in consensus
```

### Integrity Without Global Visibility

This approach maintains integrity because:

* **Double-spend prevention**: Alice's validator tracks Alice's contracts; can't spend what doesn't exist; and in the example case of reputable tokens, the issuer's approval is required for issuance.
* **Authorization enforcement**: Only parties declared as controllers can exercise choices
* **Consistency**: The synchronizer ensures all parties see a consistent order of events
* **Atomicity**: Either all involved parties confirm, or the transaction is rejected

## Pillar 3: Synchronization Without Visibility

The **synchronizer** (sequencer + mediator nodes) synchronizes transaction ordering and confirmation without seeing transaction content.

### What the Synchronizer Does

| Function         | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| **Ordering**     | Assigns timestamps and total order to transactions and events |
| **Distribution** | Routes encrypted views to entitled participants               |
| **Mediation**    | Collects confirmations and declares outcomes                  |
| **Consistency**  | Ensures all participants see the same ordering                |

### What the Synchronizer Cannot Do

| Limitation              | Guarantee                                                         |
| ----------------------- | ----------------------------------------------------------------- |
| **Read content**        | Only sees encrypted views                                         |
| **Identify end users**  | Knows parties for routing, but not the humans/systems behind them |
| **Modify transactions** | Can only pass through or reject                                   |
| **Store state**         | No persistent transaction data                                    |

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Participants
        PA[Participant A<br>Stores contracts for parties A hosts]
        PB[Participant B<br>Stores contracts for parties B hosts]
    end

    subgraph Synchronizer
        SEQ[Sequencer<br>Orders encrypted messages]
        MED[Mediator<br>Collects confirmations]
    end

    PA <--> SEQ
    PB <--> SEQ
    SEQ <--> MED

    Note1[Synchronizer sees:<br>- Encrypted blobs<br>- Timestamps<br>- Confirmation results]
    Note2[Participants store:<br>- Decrypted contract data<br>- Only for their parties]
```

### The Trust Model

The synchronizer's limited capability is a feature, not a limitation:

* **You don't need to trust the synchronizer** with your data—it can't read it
* **You do trust the synchronizer** for ordering and availability
* **The synchronizer can't cheat** because it can't see what it's synchronizing

This separation of concerns means:

* Privacy is enforced cryptographically, not by policy
* Synchronizer operators cannot extract transaction intelligence
* Adding more synchronizer operators doesn't expand data exposure

## How the Pillars Work Together

The three pillars are interdependent:

| Pillar                                 | Enables                                   |
| -------------------------------------- | ----------------------------------------- |
| **Sub-transaction privacy**            | Views that can be validated independently |
| **Proof of stakeholder**               | Consensus without global visibility       |
| **Synchronization without visibility** | Ordering without data exposure            |

Together, they create a system where:

1. Each party receives only their view
2. Each party validates only their view
3. The synchronizer never sees any views
4. The transaction commits atomically if all stakeholders confirm

## Real-World Impact

This architecture enables use cases not feasible on traditional blockchains:

### Confidential Multi-Party Workflows

Multiple organizations can share a workflow where each sees only their part:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    Bank[Bank] --> |sees loan terms| Workflow
    Borrower[Borrower] --> |sees their obligations| Workflow
    Auditor[Auditor] --> |sees compliance data| Workflow

    Workflow[Loan Agreement]

    Note[Each party sees different<br/>aspects of the same contract]
```

### Privacy-Preserving Settlement

Trading parties settle without observers seeing prices:

* Buyer sees: asset received, payment made
* Seller sees: asset transferred, payment received
* Market: cannot see price or parties

### Regulatory Compliance

Meet data protection requirements while maintaining shared truth:

* Data stays with entitled parties
* Audit trails exist for those with audit rights
* Cross-border data flows are minimized

## Next Steps

<CardGroup cols={2}>
  <Card title="Use Cases" icon="building" href="/overview/understand/use-cases">
    See concrete examples of Canton in action.
  </Card>

  <Card title="Core Concepts" icon="book" href="/overview/understand/core-concepts">
    Learn about parties, validators, and synchronizers.
  </Card>

  <Card title="Architecture Deep Dive" icon="diagram-project" href="/overview/learn/architecture">
    Understand how components work together technically.
  </Card>

  <Card title="Privacy Model" icon="lock" href="/overview/learn/privacy-model">
    Explore the privacy guarantees in detail.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
