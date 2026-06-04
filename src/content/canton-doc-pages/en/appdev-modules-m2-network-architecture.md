---
title: "Network Architecture Comparison"
slug: "appdev-modules-m2-network-architecture"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-network-architecture.md"
source_title: "Network Architecture Comparison"
tags:
  - appdev
  - modules
  - m2-network-architecture
---

# Network Architecture Comparison

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Network Architecture Comparison

> Understanding how Canton's network architecture differs from Ethereum

Canton's network architecture is fundamentally different from Ethereum. This page compares the architectures to help you understand the implications for your applications.

## High-Level Architecture

### Ethereum Architecture

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Ethereum[Ethereum Network]
        N1[Node 1<br>Full state]
        N2[Node 2<br>Full state]
        N3[Node 3<br>Full state]
        NN[Node N<br>Full state]

        N1 <--> N2
        N2 <--> N3
        N3 <--> NN
        N1 <--> N3
    end

    User1[User A] --> N1
    User2[User B] --> N2
    User3[User C] --> N3
```

**Key characteristics:**

* All nodes store all state
* Any node can answer any query
* Consensus requires all validators
* Horizontal scaling limited

### Canton Architecture

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Canton[Canton Network]
        SYNC[Synchronizer<br>Coordination only]

        V1[Validator A<br>Alice's data]
        V2[Validator B<br>Bob's data]
        V3[Validator C<br>Charlie's data]

        V1 <--> SYNC
        V2 <--> SYNC
        V3 <--> SYNC
    end

    UserA[Alice] --> V1
    UserB[Bob] --> V2
    UserC[Charlie] --> V3
```

**Key characteristics:**

* Validators store only their parties' data
* Synchronizer coordinates without storing
* Consensus involves only affected parties
* A party can be hosted on multiple validators (multihosting)

## Canton Components

### Validators

Validators store only their parties' data and answer queries only for hosted parties. In consensus, they validate only transactions affecting their parties.

### Synchronizers

Synchronizers coordinate transaction ordering without storing state. They ensure all affected parties see consistent ordering.

### Key Differences from Traditional Blockchains

In Canton:

* There is no global state—each party has their own view
* State visibility is private to stakeholders
* Only hosting validators can answer queries for their parties
* Finality is deterministic after confirmation

## Data Flow Comparison

### Ethereum Transaction Flow

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequenceDiagram
    participant User
    participant Mempool
    participant Validators
    participant Network

    User->>Mempool: Submit transaction
    Note over Mempool: Visible to all
    Validators->>Mempool: Select transactions
    Validators->>Validators: Execute transaction
    Validators->>Network: Broadcast block
    Network->>Network: All nodes update state
```

### Canton Transaction Flow

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequenceDiagram
    participant User
    participant ValidatorA as Validator A (Alice)
    participant Sync as Synchronizer
    participant ValidatorB as Validator B (Bob)

    User->>ValidatorA: Submit command
    ValidatorA->>ValidatorA: Execute Daml, create views
    ValidatorA->>Sync: Submit encrypted
    Sync->>Sync: Order, distribute
    Sync->>ValidatorA: Alice's view
    Sync->>ValidatorB: Bob's view
    ValidatorA->>Sync: Confirm
    ValidatorB->>Sync: Confirm
    Sync->>ValidatorA: Commit
    Sync->>ValidatorB: Commit
```

## Query Architecture

### Ethereum: Global Queries

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Any node can answer any query
const totalSupply = await token.totalSupply();
const aliceBalance = await token.balanceOf(aliceAddress);
const bobBalance = await token.balanceOf(bobAddress);
const allTransfers = await getTransferEvents();
```

### Canton: Party-Scoped Queries

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Query only your party's data via your validator
const myContracts = await ledgerApi.getActiveContracts({
  party: myParty,
  templateId: "Token"
});

// Can't query other parties' balances
// Must be added as observer to see their data
```

| Query Type              | Ethereum       | Canton                     |
| ----------------------- | -------------- | -------------------------- |
| **My balance**          | Query any node | Query my validator         |
| **Other's balance**     | Query any node | Must be observer           |
| **Total supply**        | Query any node | Only if designed to expose |
| **Transaction history** | Query any node | Only my transactions       |

## Implications for Application Design

### Data Availability

| Consideration     | Ethereum             | Canton                     |
| ----------------- | -------------------- | -------------------------- |
| **Read replicas** | Any node             | Only your validator        |
| **Caching**       | Cache any data       | Cache only entitled data   |
| **Analytics**     | On-chain data public | Need explicit data sharing |

### User Experience

| Aspect                  | Ethereum              | Canton                    |
| ----------------------- | --------------------- | ------------------------- |
| **Wallet connection**   | Any RPC endpoint      | Your validator's API      |
| **Balance display**     | Query public state    | Query your contracts      |
| **Transaction history** | Public block explorer | Personal transaction view |

### Scaling

Canton's architecture naturally distributes load because validators only process transactions affecting their hosted parties. Additional capacity can be achieved by distributing parties across more validators.

## Network Topology

### Ethereum: Flat P2P

All nodes are peers, all store the same data.

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    N1((Node 1)) <--> N2((Node 2))
    N2 <--> N3((Node 3))
    N3 <--> N4((Node 4))
    N4 <--> N1
    N1 <--> N3
    N2 <--> N4
```

### Canton: Hierarchical

Synchronizer coordinates, validators serve parties.

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph SyncLayer[Coordination Layer]
        SV1[Super Validator 1]
        SV2[Super Validator 2]
        SV3[Super Validator 3]
    end

    subgraph ValidatorLayer[Validator Layer]
        V1[Validator A]
        V2[Validator B]
        V3[Validator C]
    end

    subgraph UserLayer[Application Layer]
        App1[App 1]
        App2[App 2]
    end

    SV1 <--> SV2
    SV2 <--> SV3
    SV3 <--> SV1

    V1 <--> SyncLayer
    V2 <--> SyncLayer
    V3 <--> SyncLayer

    App1 --> V1
    App2 --> V2
```

## Trust Model Comparison

| Entity                | Ethereum Trust                 | Canton Trust                         |
| --------------------- | ------------------------------ | ------------------------------------ |
| **Validators**        | See all, validate all          | See only relevant, validate relevant |
| **Network operators** | Block producers see everything | Synchronizer sees nothing            |
| **Your node**         | You trust your node            | You trust your validator             |
| **Other users**       | Compete for block space        | Independent transactions             |

## Migration Considerations

When migrating from Ethereum to Canton:

| Aspect                       | Action Required                        |
| ---------------------------- | -------------------------------------- |
| **State queries**            | Redesign for party-scoped queries      |
| **Analytics**                | Build explicit data sharing if needed  |
| **Node infrastructure**      | Set up validator, not full node        |
| **User onboarding**          | Connect users to your validator        |
| **Third-party integrations** | Access Ledger API via gRPC or JSON API |

## Next Steps

<CardGroup cols={2}>
  <Card title="Architecture Deep Dive" icon="diagram-project" href="/docs/canton/overview-learn-architecture">
    Detailed Canton architecture documentation.
  </Card>

  <Card title="Start Building" icon="code" href="/docs/canton/appdev-modules-m3-dev-environment">
    Begin writing Daml smart contracts.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
