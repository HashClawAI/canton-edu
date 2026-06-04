---
title: "Architecture Overview"
slug: "overview-learn-architecture"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/learn/architecture.md"
source_title: "Architecture Overview"
tags:
  - overview
  - learn
  - architecture
---

# Architecture Overview

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Architecture Overview

> Visual understanding of how Canton Network components work together

Canton's architecture differs fundamentally from traditional blockchains. Understanding these components is essential for designing and debugging Canton applications.

## The Big Picture

Canton separates **coordination** from **storage**. Synchronizers coordinate transaction ordering; participant nodes (validators) store data for their hosted parties.

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph CN[Canton Network]
        subgraph GS[Global Synchronizer]
            SEQ[Sequencer] <--> MED[Mediator]
        end

        subgraph VA[Validator A]
            PNA[Participant Node]
            LSA[(Ledger Shard)]
            PAA[Party: Alice]
        end

        subgraph VB[Validator B]
            PNB[Participant Node]
            LSB[(Ledger Shard)]
            PBB[Party: Bob]
            PCB[Party: Charlie]
        end

        PNA <--> SEQ
        PNB <--> SEQ
    end

    AppA[Application A] --> PNA
    AppB[Application B] --> PNB
```

Unlike Ethereum where every node stores all state, Canton nodes store only their parties' data. The synchronizer coordinates but never stores transaction content.

## Core Components

### Validators

Validators are the workhorses of Canton. They:

| Function                  | Description                                                    |
| ------------------------- | -------------------------------------------------------------- |
| **Host parties**          | Store contract data for their hosted parties                   |
| **Execute Daml logic**    | Run smart contract code when transactions affect their parties |
| **Validate transactions** | Verify authorization and correctness for their shard           |
| **Expose the Ledger API** | Provide gRPC/JSON APIs for applications                        |

A validator is the Canton Network role that operates a participant node. The participant node, often shortened to "participant", is the private, self-sovereign computational and storage unit for an entity within Canton Network.

**Key characteristics:**

* Each participant node maintains a **localized, private view** of the ledger
* Participant nodes only store contracts where their hosted parties are stakeholders
* Multiple parties can be hosted on a single participant node
* Participant nodes can connect to multiple synchronizers

### Synchronizers

Synchronizers coordinate transaction ordering and consensus **without seeing transaction content**. They consist of two components:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph Sync[Synchronizer]
        subgraph SEQs[Sequencers]
            SEQ1[Sequencer 1]
            SEQ2[Sequencer 2]
            SEQ3[Sequencer N]
        end
        subgraph MEDs[Mediators]
            MED1[Mediator 1]
            MED2[Mediator 2]
            MED3[Mediator N]
        end
        SEQs <--> MEDs
    end

    P1[Participant 1] <--> SEQs
    P2[Participant 2] <--> SEQs
    P3[Participant N] <--> SEQs
```

**Sequencer**

* Orders and distributes encrypted messages between participants
* Provides total ordering for transactions for that synchronizer
* **Does not see** decrypted transaction content
* Ensures all participants receive messages from that synchronizer in the same order

**Mediator**

* Facilitates the consensus protocol
* Collects confirmation verdicts from participants
* Declares transaction verdicts (committed or rejected)
* **Does not see** decrypted transaction content

<Note>
  The synchronizer is a coordination layer, not a state storage layer. It never stores or has access to transaction data, only encrypted messages and confirmation results.
</Note>

### Parties

Parties are Canton's on-ledger identities, analogous to addresses or externally owned accounts (EOAs) on other blockchains.

```
alice::1220f2fe29866fd6a0009ecc8a64ccdc09f1958bd0f801166baaee469d1251b2eb72
└┬┘  └─────────────────────────────────────────┘
 name                              fingerprint (hash of public key)
```

**Party Capabilities:**

| Capability   | Description                                    |
| ------------ | ---------------------------------------------- |
| **Validate** | Confirm transactions affecting their contracts |
| **Control**  | Initiate specific actions (choices)            |
| **Observe**  | See specific state and transactions            |

**Local vs External Parties:**

| Type               | Key Storage       | Control                      | Use Case                             |
| ------------------ | ----------------- | ---------------------------- | ------------------------------------ |
| **Local Party**    | Held by validator | Validator signs on behalf    | Simpler; validator has full control  |
| **External Party** | Held externally   | Requires explicit signatures | More control; wallet-like experience |

<Warning>
  Unlike Ethereum addresses, parties have costs associated with creation and create state on validators. They're not ephemeral, design your party structure deliberately.
</Warning>

## How Transactions Work

### Transaction Flow

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequenceDiagram
    participant App as Application
    participant P1 as Participant 1<br>(hosts Alice)
    participant Sync as Synchronizer
    participant P2 as Participant 2<br>(hosts Bob)

    App->>P1: 1. Submit command<br>(Alice transfers to Bob)
    P1->>P1: 2. Interpret Daml,<br>create transaction views
    P1->>Sync: 3. Submit encrypted views
    Sync->>Sync: 4. Sequence & order
    Sync->>P1: 5. Deliver view for Alice
    Sync->>P2: 5. Deliver view for Bob
    P1->>P1: 6. Validate Alice's view
    P2->>P2: 6. Validate Bob's view
    P1->>Sync: 7. Confirmation
    P2->>Sync: 7. Confirmation
    Sync->>Sync: 8. Mediator collects confirmations
    Sync->>P1: 9. Commit notification
    Sync->>P2: 9. Commit notification
```

### Step-by-Step Explanation

| Step              | Component              | Action                                             |
| ----------------- | ---------------------- | -------------------------------------------------- |
| **1. Submit**     | Application            | Sends command to participant via Ledger API        |
| **2. Interpret**  | Submitting Participant | Executes Daml code, creates transaction with views |
| **3. Submit**     | Submitting Participant | Sends encrypted views to synchronizer              |
| **4. Sequence**   | Sequencer              | Orders transaction, assigns timestamp              |
| **5. Distribute** | Sequencer              | Sends each view only to entitled participants      |
| **6. Validate**   | All Participants       | Each validates their view independently            |
| **7. Confirm**    | All Participants       | Send confirmation/rejection verdict to mediator    |
| **8. Collect**    | Mediator               | Aggregates verdicts, determines outcome            |
| **9. Commit**     | All Participants       | Apply transaction to local ledger shard            |

**Key points:**

* Transaction is decomposed into **views**, each party sees only their view
* Synchronizer sequences but **never decrypts** content
* Confirmation requires **threshold agreement** from relevant participants
* Each participant stores only their committed view

## Network Topology Options

Canton supports multiple topology configurations:

### Single Synchronizer (Simple)

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    SYNC[Synchronizer]
    P1[Participant 1]
    P2[Participant 2]
    P3[Participant 3]

    P1 <--> SYNC
    P2 <--> SYNC
    P3 <--> SYNC
```

Use case: Simple deployments, testing, single-organization applications.

### Multiple Synchronizers (Enterprise)

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    SYNC1[Synchronizer A<br>Private]
    SYNC2[Synchronizer B<br>Consortium]

    P1[Participant 1]
    P2[Participant 2]
    P3[Participant 3]

    P1 <--> SYNC1
    P1 <--> SYNC2
    P2 <--> SYNC1
    P3 <--> SYNC2
```

Use case: Different synchronizers for different workflows; regulatory separation; consortium governance.

### Global Synchronizer (Canton Network)

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph GSD[Global Synchronizer]
        subgraph SVs[Super Validators]
            SV1[SV 1]
            SV2[SV 2]
            SV3[SV N]
        end
        subgraph SEQs[Distributed Sequencer]
            SEQ1[Sequencer Node 1]
            SEQ2[Sequencer Node 2]
            SEQ3[Sequencer Node N]
        end
        subgraph MEDs[Distributed Mediator]
            MED1[Mediator Node 1]
            MED2[Mediator Node 2]
            MED3[Mediator Node N]
        end
    end

    V1[Validator A]
    V2[Validator B]
    V3[Validator C]

    V1 <--> GSD
    V2 <--> GSD
    V3 <--> GSD
```

Use case: Public Canton Network; decentralized applications; cross-organization workflows.

## Where Your Code Runs

| Component                       | Location                        | Technology                              | Responsibility                               |
| ------------------------------- | ------------------------------- | --------------------------------------- | -------------------------------------------- |
| **Smart Contracts (Templates)** | Participant nodes               | Daml                                    | Business logic, authorization, privacy rules |
| **Backend Services**            | Your infrastructure             | Any language (TypeScript, Java, Python) | Off-ledger automation, integrations          |
| **Frontend**                    | Browser/mobile                  | Any framework                           | User interface                               |
| **Queries**                     | Participant (Ledger API) or PQS | gRPC, JSON, SQL                         | Reading ledger state                         |

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph YA[Your Application]
        FE[Frontend<br>React, etc.] --> BE[Backend<br>TypeScript, Java]
    end

    subgraph CI[Canton Infrastructure]
        PART[Participant Node<br>Daml execution] <--> SYNC[Synchronizer]
        PART --> PQS[PQS<br>SQL queries]
    end

    BE --> PART
    BE --> PQS
```

### Application Architecture Decisions

| Decision                      | On-Ledger (Daml)  | Off-Ledger (Backend) |
| ----------------------------- | ----------------- | -------------------- |
| **Multi-party agreements**    | ✓ Required        |                      |
| **Authorization enforcement** | ✓ Recommended     | Possible but weaker  |
| **Complex business logic**    | Possible          | ✓ Often easier       |
| **External API calls**        | Not possible      | ✓ Required           |
| **High-frequency operations** | Consider batching | ✓ Better suited      |
| **Audit trail requirements**  | ✓ Built-in        | Must implement       |

## Component Communication

### APIs Overview

| API                   | Protocol      | Use Case                              |
| --------------------- | ------------- | ------------------------------------- |
| **Ledger API (gRPC)** | gRPC/Protobuf | High-performance backend integration  |
| **Ledger API (JSON)** | HTTP/JSON     | Simpler integration, browser-friendly |
| **Admin API**         | gRPC/Protobuf | Node administration, party management |
| **PQS SQL API**       | PostgreSQL    | Complex queries, reporting            |

### Ledger API Operations

| Operation               | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| **Command Submission**  | Submit Daml commands (create contracts, exercise choices) |
| **Transaction Stream**  | Subscribe to transaction events for your parties          |
| **Active Contract Set** | Query currently active contracts                          |
| **Completions**         | Track command completion status                           |

## Next Steps

* **[Privacy Model Explained](/overview/learn/privacy-model)** - Deep dive into sub-transaction privacy
* **[The Global Synchronizer](/overview/understand/global-synchronizer)** - Understand the public network infrastructure
* **[Validator Operations](/global-synchronizer/understand/introduction)** - For those deploying and operating validators

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
