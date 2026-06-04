---
title: "Privacy Model Differences"
slug: "appdev-modules-m2-privacy-differences"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-privacy-differences.md"
source_title: "Privacy Model Differences"
tags:
  - appdev
  - modules
  - m2-privacy-differences
---

# Privacy Model Differences

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Privacy Model Differences

> Understanding how Canton's privacy model differs fundamentally from Ethereum

Privacy is the most significant architectural difference between Canton and Ethereum. This page explains the differences in depth and provides guidance for adapting your thinking.

## The Fundamental Difference

| Aspect                 | Ethereum                      | Canton                                    |
| ---------------------- | ----------------------------- | ----------------------------------------- |
| **Default visibility** | Public                        | Private                                   |
| **Approach**           | Add privacy on top            | Build privacy in                          |
| **Data location**      | All nodes store all data      | Nodes store only relevant data            |
| **Opt-in model**       | Opt-in to privacy (difficult) | Opt-in to visibility (explicit observers) |

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Ethereum[Ethereum Default]
        TX1[Transaction] --> ALL[All Validators]
        ALL --> PUBLIC[Public State<br>Everyone sees everything]
    end

    subgraph Canton[Canton Default]
        TX2[Transaction] --> VIEWS[Split by stakeholder]
        VIEWS --> A[Party A's view<br>A sees only their data]
        VIEWS --> B[Party B's view<br>B sees only their data]
    end
```

## Default Visibility Comparison

### Ethereum: Public by Default

On Ethereum, when you deploy a contract or send a transaction:

1. **Transaction data** is visible in the mempool before execution
2. **State changes** are recorded on every node
3. **Historical data** is queryable by anyone forever
4. **Contract code** is readable by anyone
5. **All interactions** are visible to all observers

Even "private" variables in Solidity are not private—they're just not exposed via the ABI. Anyone can read storage slots directly.

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Solidity: "private" is misleading
contract NotReallyPrivate {
    uint256 private secretValue;  // Anyone can read this from storage
}
```

### Canton: Private by Default

On Canton, data is visible only to entitled parties:

1. **Transaction content** is encrypted during submission
2. **Views** are delivered only to relevant validators
3. **State** is stored only on validators hosting stakeholders
4. **Contract data** is visible only to signatories and observers
5. **Third parties** see nothing unless explicitly declared

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Daml: Visibility is explicit
template TrulyPrivate
  with
    owner : Party
    secretValue : Decimal
  where
    signatory owner
    -- No observers: only owner sees this contract
```

## Sub-Transaction Privacy

Canton's key innovation is **sub-transaction privacy**: different parts of the same transaction are visible to different parties.

### Example: Atomic Three-Party Transfer

Consider: Alice pays Bob with Canton Coin, and Bob simultaneously pays Charlie.

**On Ethereum:**

* Everyone sees: Alice paid Bob, Bob paid Charlie
* Everyone knows: amounts, parties, timing
* Carol (unrelated) can see all details

**On Canton:**

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph TX[Single Atomic Transaction]
        L1[Leg 1: Alice → Bob]
        L2[Leg 2: Bob → Charlie]
    end

    subgraph Views[Views by Party]
        VA["Alice sees:<br>- Leg 1 (her payment)<br>- Not Leg 2 or Charlie"]
        VB["Bob sees:<br>- Leg 1<br>- Leg 2<br>- (both, he's involved)"]
        VC["Charlie sees:<br>- Leg 2 (his receipt)<br>- Not Leg 1 or Alice"]
        VD["Carol sees:<br>Nothing"]
    end

    TX --> Views
```

### Why This Matters

| Use Case         | Ethereum Problem                     | Canton Solution                  |
| ---------------- | ------------------------------------ | -------------------------------- |
| **Trading**      | Competitors see your trades          | Only counterparty sees trade     |
| **Lending**      | Loan terms are public                | Only borrower/lender see terms   |
| **Supply chain** | All parties see all prices           | Each party sees their portion    |
| **Compliance**   | Data visible to unauthorized parties | Regulator added as observer only |

## Comparison to Ethereum Privacy Solutions

### Layer 2 Solutions

**Approach:** Move transactions off MainNet; settle on-chain.

| Aspect                  | L2 Solutions                      | Canton                    |
| ----------------------- | --------------------------------- | ------------------------- |
| **Operator visibility** | L2 operator sees all transactions | Synchronizer sees nothing |
| **Data availability**   | Must be available somewhere       | Only to entitled parties  |
| **Settlement**          | Requires L1 confirmation          | Immediate finality        |
| **Trust model**         | Trust L2 operator                 | Cryptographic privacy     |

### Zero-Knowledge Solutions

**Approach:** Prove validity without revealing data.

Canton does not use zero-knowledge proofs. Instead, privacy is achieved through selective data distribution—parties only receive the transaction views they're entitled to see. This provides a simpler programming model without ZK circuit complexity or proof generation overhead.

### Private Channels (Hyperledger Fabric)

**Approach:** Separate channels for private transactions.

| Aspect            | Private Channels               | Canton                     |
| ----------------- | ------------------------------ | -------------------------- |
| **Granularity**   | Channel-level                  | Sub-transaction level      |
| **Cross-channel** | Complex to implement           | Native atomic transactions |
| **Membership**    | Must manage channel membership | Declared in contracts      |
| **Flexibility**   | Rigid channel structure        | Dynamic per-transaction    |

### Encryption at Rest

**Approach:** Encrypt data stored on-chain.

| Aspect             | Encryption                      | Canton                    |
| ------------------ | ------------------------------- | ------------------------- |
| **Key management** | Complex key distribution        | No shared keys needed     |
| **Metadata**       | Transaction patterns visible    | Encrypted entirely        |
| **Future risk**    | May be decrypted later          | Not stored to decrypt     |
| **Computation**    | Can't compute on encrypted data | Full computation on views |

## Private Ledger View

In Canton, each party has their own **private ledger view**—the collection of all contracts where they're a stakeholder.

### What This Means

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Network[Canton Network State]
        C1[Contract 1<br>Signatories: A, B]
        C2[Contract 2<br>Signatories: B, C]
        C3[Contract 3<br>Signatories: A, C]
        C4[Contract 4<br>Signatories: C, D]
    end

    subgraph PartyViews[Each Party's Ledger View]
        VA["Alice sees:<br>Contract 1, Contract 3"]
        VB["Bob sees:<br>Contract 1, Contract 2"]
        VC["Charlie sees:<br>Contract 2, Contract 3, Contract 4"]
    end

    Network --> PartyViews
```

**Key implications:**

| On Ethereum                        | On Canton                                                       |
| ---------------------------------- | --------------------------------------------------------------- |
| Query all tokens: `getAllTokens()` | Query *your* tokens: `getMyContracts()`                         |
| Global state exists                | No global state concept                                         |
| Total supply is known              | Total supply visible only if explicitly designed for visibility |
| Any node answers any query         | Only your validator answers your queries                        |

### Querying Data

**Ethereum approach:**

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Anyone can query any data
const totalSupply = await token.totalSupply();
const aliceBalance = await token.balanceOf(alice);
const bobBalance = await token.balanceOf(bob);
```

**Canton approach:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// You can only query your own data
const myContracts = await ledgerApi.getActiveContracts({
  templateId: "Token",
  party: myParty  // Only your party
});

// Can't query Bob's balance unless you're an observer
```

## What the Synchronizer Can and Cannot See

The synchronizer (sequencer + mediator) coordinates transactions but never sees content.

### Synchronizer Can See

* Encrypted message blobs (must deliver them)
* Message sizes (network routing)
* Timestamps (ordering)
* Confirmation results, such as committed or rejected (finality)
* Validator identifiers (routing)
* Party identifiers (for routing, but not end-user identity)

### Synchronizer Cannot See

* Transaction content (encrypted)
* Contract data (never transmitted to synchronizer)
* Choice being exercised (encrypted)
* Amounts, prices, terms (encrypted)

### Trust Implications

Canton's trust model differs fundamentally from traditional blockchains:

**What you trust the synchronizer for:**

* Ordering transactions fairly (not reordering to favor certain parties)
* Delivering messages to all entitled participants
* Availability (being online when you need to transact)

**What you don't need to trust the synchronizer for:**

* Your data privacy—it only sees encrypted blobs
* Transaction validation—your validator does this
* Correct execution—the protocol enforces this cryptographically

**What you trust your validator for:**

* Storing your contract data securely
* Executing transactions correctly on your behalf
* Not revealing your data to unauthorized parties

<Warning>
  Your hosting validator sees all your party's data. Choose your validator carefully—this is a trust relationship similar to choosing a bank or custodian.
</Warning>

| Ethereum                                     | Canton                                               |
| -------------------------------------------- | ---------------------------------------------------- |
| Trust all validators not to censor           | Trust synchronizer not to censor                     |
| All validators see everything                | Synchronizer sees only encrypted views               |
| MEV is possible (validators see pending txs) | MEV is significantly harder (transactions encrypted) |
| Front-running is structural                  | Front-running is much harder                         |
| Trust any node for queries                   | Trust only your validator for your data              |

## Design Implications for Developers

### Rethinking State Queries

**Ethereum mindset:** "How do I query global state?"

**Canton mindset:** "What can my party see, and who else needs visibility?"

### Observer Pattern

When designing contracts, explicitly consider:

1. **Who are signatories?** They must authorize and always see.
2. **Who are observers?** They can see but not act.
3. **Who can exercise choices?** Controllers for each choice.
4. **What gets divulged?** Fetching contracts in transactions reveals them.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template DesignedForPrivacy
  with
    primaryParty : Party
    counterparty : Party
    auditor : Party  -- Only if audit is required
    details : SensitiveData
  where
    signatory primaryParty
    observer counterparty  -- Needs to see, but not auditor

    -- Add auditor only when they need to see
    choice AddAuditObserver : ContractId DesignedForPrivacy
      with newAuditor : Party
      controller primaryParty
      do create this with auditor = newAuditor
```

### Privacy Checklist

When designing Canton applications:

| Question                                 | Design Impact                      |
| ---------------------------------------- | ---------------------------------- |
| Who needs to see this contract?          | Signatory + observer declarations  |
| Who can act on this contract?            | Controller declarations per choice |
| What happens when contracts are fetched? | Divulgence considerations          |
| Do third parties need visibility?        | Add observers explicitly           |
| Should validators see everything?        | Consider party hosting choices     |

## Next Steps

<CardGroup cols={2}>
  <Card title="Smart Contract Paradigm" icon="code" href="/appdev/modules/m2-smart-contract-paradigm">
    Understand Daml's immutable contract model vs. Solidity.
  </Card>

  <Card title="Privacy Model Deep Dive" icon="lock" href="/overview/learn/privacy-model">
    Technical details of sub-transaction privacy.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
