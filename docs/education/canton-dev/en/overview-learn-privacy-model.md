---
title: "Privacy Model Explained"
slug: "overview-learn-privacy-model"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/learn/privacy-model.md"
source_title: "Privacy Model Explained"
tags:
  - overview
  - learn
  - privacy-model
---

# Privacy Model Explained

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Privacy Model Explained

> Deep understanding of Canton's unique sub-transaction privacy capabilities

Canton's privacy model is its defining feature. This section explains how sub-transaction privacy works, what guarantees it provides, and common patterns for privacy-aware development.

## The Privacy Problem in Blockchain

On most blockchains, achieving transaction integrity requires global visibility. Every validator sees every transaction to verify no double-spends occur and all rules are followed.

This creates an inherent tension:

| Requirement      | Traditional Approach               | Problem                 |
| ---------------- | ---------------------------------- | ----------------------- |
| **Integrity**    | Validators verify all transactions | Requires visibility     |
| **Verification** | See transaction content            | Reveals private data    |
| **Privacy**      | Hide transaction content           | Undermines verification |

Traditional blockchains make a choice: integrity over privacy. Everyone sees everything.

### Why This Blocks Enterprise Adoption

For regulated industries, global visibility is a non-starter:

* **Position visibility**: Competitors can see your trading strategies
* **Front-running risk**: Observers can exploit transaction information
* **Regulatory compliance**: Data may not be shared with unauthorized parties
* **Confidential agreements**: Business terms should remain between parties

## Canton's Approach: Sub-Transaction Privacy

Canton resolves the integrity-privacy tension through **sub-transaction privacy**: decomposing transactions into views where each party sees only what they need to verify their portion.

### How It Works

When a transaction involves multiple parties, Canton doesn't send the full transaction to everyone. Instead:

1. **Decomposition**: Transaction is split into **views** based on stakeholder relationships
2. **Encryption**: Each view is encrypted to its respective recipients
3. **Distribution**: Synchronizer delivers only entitled views to each participant
4. **Validation**: Each participant validates their view independently
5. **Confirmation**: Participants confirm based on their view alone

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph FT[Full Transaction]
        TX[Transaction:<br>Alice pays Bob,<br>Bob pays Charlie]
    end

    TX --> DECOMPOSE[Decompose into Views]

    DECOMPOSE --> VA[Alice's View<br>- Alice pays Bob<br>- encrypted rest]
    DECOMPOSE --> VB[Bob's View<br>- Alice pays Bob<br>- Bob pays Charlie]
    DECOMPOSE --> VC[Charlie's View<br>- encrypted context<br>- Bob pays Charlie]
```

In other words, participants see only those parts of a transaction they are entitled to according to the privacy model. For the other parts of a transaction they are not entitled to, participants see neither any transaction payload nor metadata like involved participants or parties.

The synchronizer sees **none of this**—only encrypted messages and confirmation results.

### What Each Party Sees

| Party       | Sees                                  | Doesn't See                                   |
| ----------- | ------------------------------------- | --------------------------------------------- |
| **Alice**   | Her payment to Bob                    | Bob's payment to Charlie; Charlie's identity  |
| **Bob**     | Both payments (he's involved in both) | -                                             |
| **Charlie** | His receipt from Bob                  | Alice's involvement; original source of funds |

The synchronizer sees **none of this** - only encrypted messages and confirmation results.

## Stakeholder Visibility Rules

Visibility in Canton follows two core principles:

### Principle 1: Parties See Actions They Have a Stake In

| Role           | Visibility                                  |
| -------------- | ------------------------------------------- |
| **Signatory**  | Always sees the contract and all its events |
| **Observer**   | Sees the contract by explicit declaration   |
| **Controller** | Sees choices they can exercise              |

### Principle 2: Parties Who See an Action See Its Consequences

If you see an action, you see the creates/archives it produces. This enables independent verification - you can confirm the action was executed correctly based on the outcomes you observe.

### Visibility Example

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Payment
  with
    sender : Party
    receiver : Party
    amount : Decimal
  where
    signatory sender
    observer receiver
    
    choice Accept : ContractId Receipt
      controller receiver
      do
        create Receipt with payer = sender, payee = receiver, amount
```

| Party           | Contract Visibility | Choice Visibility     |
| --------------- | ------------------- | --------------------- |
| **sender**      | ✓ (signatory)       | ✓ (sees consequences) |
| **receiver**    | ✓ (observer)        | ✓ (controller)        |
| **anyone else** | ✗                   | ✗                     |

## Privacy Guarantees

### What Canton Guarantees

<Check>
  **Transaction content** is only visible to authorized parties (signatories, observers, controllers).
</Check>

<Check>
  **Synchronizer operators** cannot read transaction data - they see only encrypted messages.
</Check>

<Check>
  **No metadata leakage** about parties not entitled to see an action - other participants and parties are invisible.
</Check>

<Check>
  **Validators only store** data for their hosted parties - no global state replication.
</Check>

## Privacy Patterns

### Pattern 1: Bilateral Agreement

Only the two signatories see the contract. Maximum privacy for two-party agreements.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template BilateralContract
  with
    partyA : Party
    partyB : Party
    terms : Text
  where
    signatory partyA, partyB
    -- No observers: only signatories see this contract
```

**Use when**: Two parties need a private agreement with no third-party visibility.

**Visibility**: Only `partyA` and `partyB`.

### Pattern 2: Selective Disclosure via Observers

Add specific parties as observers when they need visibility but not control.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template RegulatedAsset
  with
    owner : Party
    issuer : Party
    regulator : Party
    value : Decimal
  where
    signatory issuer
    observer owner, regulator

    choice Transfer : ContractId RegulatedAsset
      with
        newOwner : Party
      controller owner  -- owner can transfer unilaterally
      do
        create this with owner = newOwner
```

**Use when**: Third parties need visibility for compliance, audit, or information purposes.

**Visibility**: `issuer` (signatory), `owner` and `regulator` (observers). Note that `owner` is also the controller for `Transfer`, so they can execute that choice unilaterally.

### Pattern 3: Divulgence

When contracts are used in transactions, parties to that transaction may learn about them. This "divulgence" is automatic.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Contract held by Alice
template Asset with owner : Party where
  signatory owner

-- Alice uses her Asset in a transaction with Bob
template Trade
  with
    seller : Party  -- Alice
    buyer : Party   -- Bob
    assetId : ContractId Asset
  where
    signatory seller, buyer
    
    choice Execute : ()
      controller buyer
      do
        -- Bob sees the Asset contract through divulgence
        asset <- fetch assetId
        archive assetId
        -- ... transfer logic
```

**What happens**: When `Execute` runs, Bob (as a party to the Trade) sees the Asset contract that Alice owns, even though he wasn't originally an observer.

**Use carefully**: Divulgence can inadvertently reveal information. Design transactions with awareness of what gets divulged.

## Privacy vs. Auditability

Canton enables privacy without sacrificing auditability. Common patterns:

### Auditor as Observer

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuditableTransaction
  with
    partyA : Party
    partyB : Party
    auditor : Party
    details : TransactionDetails
  where
    signatory partyA, partyB
    observer auditor  -- Auditor sees everything but cannot act
```

### Selective Audit Rights

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template SelectivelyAuditable
  with
    owner : Party
    data : SensitiveData
    auditor : Party
  where
    signatory owner
    
    -- Non-consuming choice: reveals data without changing state
    nonconsuming choice Audit : AuditReport
      controller auditor
      do
        -- Auditor can request audit, seeing only what's returned
        return AuditReport with 
          timestamp = now
          summary = summarize data  -- Controlled disclosure
```

### Best Practices for Auditability

| Practice                     | Description                                                              |
| ---------------------------- | ------------------------------------------------------------------------ |
| **Explicit auditor parties** | Add auditors as observers where audit trail is required                  |
| **Audit choices**            | Create non-consuming choices that return audit information               |
| **Separate audit contracts** | Create dedicated audit trail contracts when full visibility isn't needed |
| **Time-bounded access**      | Use workflow patterns to grant temporary audit access                    |

## Common Privacy Mistakes

### Mistake 1: Over-Sharing via Observers

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- BAD: Adding unnecessary observers
template OverShared
  with
    owner : Party
    counterparty : Party
    allUsers : [Party]  -- Why do all users need to see this?
  where
    signatory owner
    observer counterparty, allUsers  -- Privacy leak!
```

**Problem**: Every party in `allUsers` sees this contract, even if they don't need to.

**Fix**: Only add observers who genuinely need visibility.

### Mistake 2: Ignoring Divulgence

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Transaction reveals more than intended
choice RevealingChoice : ()
  controller buyer
  do
    -- Fetching this contract divulges it to all transaction stakeholders
    sensitiveAsset <- fetch sensitiveAssetId
    -- buyer now knows about sensitiveAsset, even if not originally an observer
```

**Problem**: Composing contracts in transactions can reveal information to parties who weren't original stakeholders.

**Fix**: Understand which contracts get fetched and who sees the transaction.

### Mistake 3: Timing Attacks

**Problem**: Even without seeing content, observers might infer information from:

* When transactions occur
* Transaction sizes
* Patterns of activity

**Fix**:

* Consider batching sensitive operations
* Add noise or randomization where appropriate
* Design workflows to minimize timing information leakage

## Privacy Design Checklist

When designing Canton applications, ask:

| Question                          | Consideration                                  |
| --------------------------------- | ---------------------------------------------- |
| **Who are the signatories?**      | They will always see everything                |
| **Who needs to observe?**         | Add observers deliberately, not by default     |
| **What gets divulged?**           | Trace through transaction composition          |
| **What do contract keys reveal?** | Keys should not encode sensitive relationships |
| **What can timing reveal?**       | Consider patterns, not just content            |
| **Who is my validator?**          | They see all your data - choose carefully      |

## Next Steps

* **[The Global Synchronizer](/overview/understand/global-synchronizer)** - Understand the public network infrastructure
* **[Developer Track Module 3: Daml Development](/appdev/modules/m3-dev-environment)** - Apply privacy patterns in code
* **[Glossary](/overview/understand/glossary)** - Terminology reference including privacy-related terms

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
