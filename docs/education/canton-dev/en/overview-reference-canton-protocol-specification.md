---
title: "Canton Protocol Specification"
slug: "overview-reference-canton-protocol-specification"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/canton-protocol-specification.md"
source_title: "Canton Protocol Specification"
tags:
  - overview
  - reference
  - canton-protocol-specification
---

# Canton Protocol Specification

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Protocol Specification

> Technical specification of the Canton protocol architecture, covering consensus layers, transaction processing, and topology management

This section provides the full technical specification of the Canton protocol. Where the [Learn](/docs/canton/overview-learn-architecture) pages introduce concepts at a high level, these reference pages describe the protocol mechanics in detail — the data structures, trust assumptions, message flows, and formal properties that underpin Canton Network.

## Protocol Architecture

Canton's protocol separates two concerns that most blockchains conflate: **smart contract validation** and **transaction ordering**. The result is a two-layer consensus architecture where each layer can be optimized independently.

| Layer                        | Responsibility                             | Mechanism                           | Trust Boundary         |
| ---------------------------- | ------------------------------------------ | ----------------------------------- | ---------------------- |
| **Smart contract consensus** | Validate transaction correctness           | Proof of Stakeholder (peer-to-peer) | Only affected parties  |
| **Ordering consensus**       | Establish consistent synchronizer ordering | BFT ordering via sequencers         | Synchronizer operators |

The protocol operates across three node types:

* **Participant nodes** host parties, maintain their Active Contract Set (ACS), execute the smart contract consensus protocol on their behalf, and make the LAPI available for use.
* **Sequencer nodes** provide authenticated, event ordering multicast with sender privacy
* **Mediator nodes** mediate the two-phase commit protocol that binds validation results into final transaction decisions

Participants and mediators never communicate directly. All messages flow through sequencers, which global ordering. Payloads are encrypted so that sequencers see only metadata — recipient lists and message sizes — not transaction content.

## Reference Pages

<CardGroup cols={2}>
  <Card title="Ledger Model (Detailed)" icon="layer-group" href="/docs/canton/overview-reference-ledger-model-detailed">
    The extended UTXO model: templates, stakeholders, choices, transaction structure, views, and witnesses.
  </Card>

  <Card title="Smart Contract Consensus" icon="handshake" href="/docs/canton/overview-reference-smart-contract-consensus">
    Proof of Stakeholder validation, privacy-preserving consensus, and trust domain comparisons.
  </Card>

  <Card title="Ordering Consensus" icon="arrow-down-1-9" href="/docs/canton/overview-reference-ordering-consensus">
    Sequencer and mediator architecture, BFT ordering service, and the ISS-inspired consensus protocol.
  </Card>

  <Card title="Transaction Lifecycle" icon="rotate" href="/docs/canton/overview-reference-transaction-lifecycle">
    The complete five-phase lifecycle from preparation through commit.
  </Card>

  <Card title="Topology" icon="diagram-project" href="/docs/canton/overview-reference-topology">
    Namespace management, cryptographic keys, party-to-participant mappings, and topology transactions.
  </Card>
</CardGroup>

## Key Properties

Canton's protocol provides the following guarantees:

* **Sub-transaction privacy**: Each party sees only the portions of a transaction relevant to them. Sequencers and mediators cannot read transaction payloads.
* **Integrity**: A transaction commits only if all required stakeholders confirm it, and only if the smart contract logic passes validation for every signatory.
* **Consistency**: The ordering layer helps to prevent double-spends by ensuring a single global ordering of all state changes on a given synchronizer.
* **Finality**: Once a mediator issues a commit verdict and it is sequenced, the transaction result is final. There are no forks or reorganizations.
* **Liveness**: Under the BFT fault tolerance threshold (fewer than one-third of ordering nodes faulty), the protocol makes progress.

## How the Layers Interact

A Daml transaction moves through both consensus layers during its lifecycle:

1. The submitting participant prepares the transaction locally (smart contract layer)
2. The participant sends encrypted views to the sequencer (ordering layer)
3. The sequencer distributes views to affected participants and an informee message to the mediator
4. Each confirming participant validates its views and sends a confirmation or rejection to the mediator (smart contract layer, via ordering layer)
5. The mediator aggregates confirmations and issues a verdict, within the required time window, which the sequencer distributes to all participants (ordering layer)

The [Transaction Lifecycle](/docs/canton/overview-reference-transaction-lifecycle) page covers each phase in full detail.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
