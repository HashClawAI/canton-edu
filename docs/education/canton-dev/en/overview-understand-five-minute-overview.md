---
title: "Canton Network in 5 Minutes"
slug: "overview-understand-five-minute-overview"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/five-minute-overview.md"
source_title: "Canton Network in 5 Minutes"
tags:
  - overview
  - understand
  - five-minute-overview
---

# Canton Network in 5 Minutes

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Network in 5 Minutes

> A rapid introduction to Canton Network's approach to privacy-preserving blockchain

Canton Network is a public blockchain that solves a fundamental problem: how do you get the benefits of blockchain (shared truth, automation, auditability) without exposing sensitive data to everyone?

## The Core Insight

Traditional blockchains replicate all data to all nodes. This provides strong integrity guarantees but prevents privacy without additional layers.

Canton inverts this model: **data goes only where it needs to go**. Parties see only what they're entitled to see, yet the system maintains the same integrity guarantees as a fully replicated blockchain.

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph Traditional[Traditional Blockchain]
        TX1[Transaction] --> ALL[All Nodes]
        ALL --> N1[Node 1: sees everything]
        ALL --> N2[Node 2: sees everything]
        ALL --> N3[Node N: sees everything]
    end
```

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph Canton[Canton Network]
        TX2[Transaction] --> VIEWS[Split into Views]
        VIEWS --> VA[Alice's validator: sees Alice's view]
        VIEWS --> VB[Bob's validator: sees Bob's view]
        VIEWS --> VC[Charlie's validator: sees Charlie's view]
    end
```

## How It Achieves This

Canton achieves this through three key innovations:

### 1. Sub-Transaction Privacy

Transactions are decomposed into **views**. Each party receives only the views they're entitled to see based on their role (signatory, observer, controller).

If Alice pays Bob, and Bob pays Charlie in a single atomic transaction:

* Alice sees her payment to Bob
* Bob sees both payments (he's involved in both)
* Charlie sees only his receipt from Bob
* Nobody else sees anything

### 2. Synchronizers Only Synchronize, Don't Store Transaction State

The **Global Synchronizer** orders transactions and facilitates consensus but never sees transaction content. It handles encrypted messages and confirmation results only.

This separation means:

* No central point that can read all data
* Synchronization without visibility
* Validators store data for their hosted parties

### 3. Smart Contracts Define Privacy

Privacy isn't a bolt-on feature. Daml smart contracts explicitly declare:

* **Signatories**: Who must authorize and always see the contract
* **Observers**: Who can see but not act
* **Controllers**: Who can execute specific actions

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Asset
  with
    owner : Party
    issuer : Party
    regulator : Party
  where
    signatory issuer      -- Must authorize; always sees
    observer owner, regulator  -- Can see

    choice Transfer : ContractId Asset
      with newOwner : Party
      controller owner    -- Only owner can execute the Transfer choice
      do create this with owner = newOwner
```

## The Network

Canton Network consists of:

| Component               | Role                                                      |
| ----------------------- | --------------------------------------------------------- |
| **Global Synchronizer** | Public synchronization layer operated by Super Validators |
| **Validators**          | Nodes that host parties and store their contract data     |
| **Canton Coin (CC)**    | Native token for transaction fees                         |
| **Applications**        | What you build on top                                     |

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph GS[Global Synchronizer]
        SV1[Super Validator 1]
        SV2[Super Validator 2]
        SV3[Super Validator N]
    end

    V1[Validator A<br>+ App A] <--> GS
    V2[Validator B<br>+ App B] <--> GS
    V3[Validator C<br>+ App C] <--> GS
```

Each validator typically runs one or more applications. Applications can also compose with other applications—using their published Daml packages to build on top of existing functionality while preserving privacy.

## Why This Matters

Canton enables use cases that are not feasible on traditional blockchains:

| Use Case                    | Why Canton Works                                              |
| --------------------------- | ------------------------------------------------------------- |
| **Regulated finance**       | Data stays with entitled parties; compliance becomes possible |
| **Multi-party workflows**   | Shared truth without shared visibility                        |
| **Confidential agreements** | Terms visible only to signatories                             |
| **Position privacy**        | Trading strategies protected                                  |

## What's Different

If you're coming from other blockchains:

| Traditional Blockchain     | Canton                                  |
| -------------------------- | --------------------------------------- |
| Everyone sees everything   | Parties see only their views            |
| Global state replication   | Distributed state per party             |
| Privacy = additional layer | Privacy = core protocol                 |
| Gas fees                   | Traffic fees                            |
| EOA/Address                | Party                                   |
| Mutable contracts          | Immutable; changes create new contracts |

## Next Steps

<CardGroup cols={2}>
  <Card title="Why Canton?" icon="question" href="/docs/canton/overview-understand-the-problem">
    Understand the problem Canton solves in depth.
  </Card>

  <Card title="Core Concepts" icon="book" href="/docs/canton/overview-understand-core-concepts">
    Learn about parties, validators, synchronizers, and smart contracts.
  </Card>

  <Card title="For Ethereum Devs" icon="ethereum" href="/docs/canton/appdev-modules-m2-canton-for-ethereum-devs">
    Translate your blockchain knowledge to Canton.
  </Card>

  <Card title="Architecture" icon="diagram-project" href="/docs/canton/overview-learn-architecture">
    See how components work together.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
