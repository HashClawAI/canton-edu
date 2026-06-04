---
title: "Smart Contract Consensus"
slug: "overview-reference-smart-contract-consensus"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/smart-contract-consensus.md"
source_title: "Smart Contract Consensus"
tags:
  - overview
  - reference
  - smart-contract-consensus
---

# Smart Contract Consensus

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Contract Consensus

> Proof of Stakeholder consensus in Canton — peer-to-peer validation, privacy-preserving consensus, and trust domain analysis

Canton's smart contract consensus layer determines *who validates a transaction* and *how their confirmations produce a binding result*. The mechanism is called **Proof of Stakeholder**: only the participant nodes hosting parties with a stake in the affected contracts participate in validation and confirmation. No global replication of state or computation is required.

This page specifies the validation logic, confirmation policies, and security properties of the smart contract consensus layer. For transaction ordering and sequencer mechanics, see [Ordering Consensus](/overview/reference/ordering-consensus). For the end-to-end message flow, see [Transaction Lifecycle](/overview/reference/transaction-lifecycle).

## Proof of Stakeholder

In a fully replicated blockchain, every node validates every transaction. Canton takes a different approach. A transaction's **stakeholders** — the signatories and observers of the contracts it creates, consumes, or references — are the only parties whose participant nodes validate and confirm the transaction. This is Proof of Stakeholder.

The principle is straightforward: if a contract exists between Alice and Bob, only Alice's and Bob's participant nodes need to confirm that a state change to that contract is valid. Charlie's participant node has no reason to see the transaction, validate it, or even know it happened.

Stakeholder-scoped validation produces two properties simultaneously:

* **Privacy**: non-stakeholders receive no information about the transaction — the payload content remains private.
* **Scalability**: the validation workload for any given transaction is bounded by the number of stakeholders, not by the total number of nodes in the network.

The ordering layer (sequencer and mediator) handles global consistency — preventing double-spends and establishing a total order of state changes. The smart contract consensus layer handles correctness — ensuring the Daml logic was executed faithfully and authorization rules were satisfied. This separation is what the [Canton Protocol Specification](/overview/reference/canton-protocol-specification) calls two-layer consensus.

## Peer-to-Peer Validation

When a submitting participant prepares a transaction, it constructs **transaction views** — subsets of the full transaction tree, each encrypted to the parties entitled to see that subset. The sequencer distributes these encrypted views to the appropriate participant nodes. Each recipient then validates independently.

### What Each Confirming Participant Does

A confirming participant node that receives one or more views for a transaction performs the following checks:

1. **Decryption and deserialization** — The participant decrypts the views addressed to it and reconstructs the portion of the transaction tree visible to its hosted parties.

2. **Daml interpretation** — The participant re-executes the Daml smart contract logic for the actions in its views. The computed consequences (created contracts, archived contracts, choice results) must match what the submitting participant claimed.

3. **Authorization verification** — The participant checks that the correct signatories authorized contract creation, that the correct controllers exercised choices, and that all required signatures are present.

4. **Consistency against the local ACS** — The participant checks that input contracts referenced in the transaction are active in its local Active Contract Set. A contract that has already been archived or consumed represents a conflict (a potential double-spend from this participant's perspective).

5. **Confirmation or rejection** — Based on the outcome of these checks, the participant sends a cryptographically signed confirmation (approve) or rejection (reject) response to the mediator, routed through the sequencer.

No single participant needs to see the entire transaction. Each validates only the views it received. A participant hosting Alice validates Alice's view; a participant hosting Bob validates Bob's view. If the transaction spans both, each confirms independently and the mediator aggregates the results.

### The Mediator's Role

The mediator receives the informee list for the transaction (which parties must confirm) along with the signed confirmation or rejection responses from confirming participants. It does not receive decrypted transaction content — it sees only:

* Which parties are informees (signatories and observers) for each view
* Whether each confirming participant approved or rejected
* The confirmation policy that applies

Once sufficient confirmations arrive (see [Confirmation Policies](#confirmation-policies) below), the mediator issues a **verdict**: commit or abort. The sequencer distributes this verdict to all involved participants, who then atomically apply (or discard) the transaction against their local ledger state.

The mediator enforces the protocol but cannot independently verify Daml logic — it relies on confirming participants for that. Its authority is limited to tallying confirmations against the required policy and declaring the outcome.

## How Consensus Enables Privacy

Proof of Stakeholder and sub-transaction privacy are mutually reinforcing. Because validation is distributed across only the affected stakeholders rather than replicated globally, Canton achieves privacy as a structural property of the protocol, not as an add-on.

**Each party sees only its views.** A transaction involving Alice, Bob, and Charlie is decomposed into views. Alice's view contains the actions where Alice is a stakeholder. Charlie's view contains only Charlie's portion. Alice and Charlie may not even be aware of each other's involvement in the same atomic transaction.

**The sequencer sees encrypted payloads only.** The sequencer routes messages based on recipient metadata (which participant nodes should receive which encrypted blobs). It cannot decrypt the payloads and therefore learns nothing about contract content, party relationships within a transaction, or business logic.

**The mediator sees informee lists and confirmation outcomes, not contract data.** The mediator knows that certain parties need to confirm a certain transaction, and it receives their approve/reject responses. It does not see the Daml code, contract payloads, or choice arguments.

**No global state replication means no global visibility.** Each participant node stores only the contracts where its hosted parties are stakeholders. There is no shared global state that could be queried or leaked.

The net effect: the set of entities that learn anything about a transaction is bounded by its stakeholder set, and even within that set, each party's visibility is scoped to the views it is entitled to.

## Confirmation Policies

The confirmation policy defines how many confirmations the mediator needs before it can issue a commit verdict. Canton uses a **signatory-based confirmation policy**: for each signatory of a contract involved in the transaction, the mediator requires confirmation from the participant nodes hosting that signatory.

### Single-Hosted Parties

In the simplest case, a signatory is hosted on exactly one participant node. The mediator needs that single participant to confirm. If the transaction involves contracts with signatories Alice and Bob, the mediator waits for confirmation from Alice's participant and Bob's participant. Both must approve for the transaction to commit.

### Multi-Hosted Parties and Thresholds

A party can be hosted on multiple participant nodes simultaneously — a configuration called multi-hosting or party replication. When a party is multi-hosted, the party-to-participant topology mapping specifies:

* Which participant nodes are **confirming participant nodes (CPNs)** for that party
* A **confirmation threshold**: the minimum number of those CPNs that must confirm

For example, if Alice is hosted on three participant nodes with a confirmation threshold of 2, the mediator requires at least 2 of those 3 CPNs to approve the transaction on Alice's behalf. This is an m-of-n scheme where m is the threshold and n is the number of CPNs.

The threshold creates a tradeoff between security and availability:

* **Higher threshold** (e.g., 3-of-3): stronger security, since more nodes must be compromised to forge a confirmation, but any single node's unavailability blocks confirmation.
* **Lower threshold** (e.g., 1-of-3): higher availability, since the party can confirm as long as any one CPN is online, but a single compromised CPN can approve on the party's behalf.

### Aggregation Rule

The mediator applies the confirmation policy independently for each signatory involved in the transaction. The transaction commits only if **all** signatories' confirmation thresholds are met. A single signatory whose threshold is not met — whether due to rejection or timeout — causes the entire transaction to abort.

Observers receive the transaction views for informational purposes and may validate them locally, but their confirmation is not required for the transaction to commit. The commit decision rests entirely on signatory confirmations.

## Trust Domain Comparison

The following table compares Canton's Proof of Stakeholder approach against two other architectures across six dimensions relevant to protocol designers and security auditors.

| Trust Domain            | Canton (Proof of Stakeholder)   | Fully Replicated (e.g., Ethereum)                 | UTXO with Notaries (e.g., Corda) |
| ----------------------- | ------------------------------- | ------------------------------------------------- | -------------------------------- |
| Transaction validation  | Only stakeholder participants   | All nodes                                         | Notary + transacting parties     |
| State storage           | Only hosting participants       | All nodes                                         | Only transacting parties         |
| Finality                | Mediator verdict (immediate)    | Block confirmation (probabilistic or epoch-based) | Notary signature                 |
| Double-spend prevention | Sequencer ordering + mediator   | Global ordering                                   | Notary                           |
| Transaction ordering    | Synchronizer sequencer          | Block proposer / miners                           | Notary                           |
| Message distribution    | Sequencer multicast (encrypted) | Gossip (public)                                   | Point-to-point                   |

Canton's design concentrates trust for *data correctness* within the stakeholder set while delegating trust for *ordering and availability* to the synchronizer infrastructure. Ethereum concentrates all trust dimensions in the global validator set. Corda places significant trust in the notary for ordering, finality, and double-spend prevention, with transacting parties responsible for validation.

A key distinction: Canton's sequencer and mediator never see decrypted transaction content, so the ordering layer cannot extract business intelligence from the transactions it orders. In Ethereum, every validator has full visibility into every transaction. In Corda, the notary sees transaction hashes but not content (in the non-validating notary model) or full transactions (in the validating notary model).

## Security Properties

Proof of Stakeholder provides the following guarantees, assuming the underlying cryptographic primitives and the ordering layer are sound:

**Confirmation integrity.** A transaction commits only if all required signatories' participant nodes confirm it. The mediator cannot forge confirmations — each confirmation is cryptographically signed by the confirming participant.

**Participant isolation.** A malicious participant cannot forge confirmations for parties it does not host. The topology state (party-to-participant mappings) is authenticated and distributed through the sequencer, so the mediator knows which participants are authorized CPNs for each party.

**Privacy preservation.** Non-stakeholders learn nothing about the transaction. The sequencer sees only encrypted payloads and routing metadata. The mediator sees informee lists and confirmation outcomes but not contract data. Participants that do not host any stakeholder party receive no views.

**Authorization enforcement.** Confirming participants independently verify that the Daml authorization rules were satisfied — correct signatories, correct controllers, valid choice exercise. A submitting participant that constructs a transaction violating these rules will be rejected during confirmation.

**Atomicity.** The mediator's verdict is all-or-nothing. Either every action in the transaction commits, or none does. There is no partial commit state.

**Liveness.** Transaction progress depends on the availability of the sequencer (for message ordering and distribution), the mediator (for verdict aggregation), and sufficiently many confirming participants (to meet each signatory's confirmation threshold). If any of these components are unavailable beyond the protocol's timeout, the transaction aborts. Liveness of the ordering layer is analyzed in [Ordering Consensus](/overview/reference/ordering-consensus).

**Consistency.** Double-spend protection operates at two levels. Each confirming participant checks consumed contracts against its local ACS. The sequencer's total ordering ensures that conflicting transactions are sequenced, so participants observe a consistent history. If two transactions attempt to consume the same contract, the one sequenced second will find the contract already archived and reject.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
