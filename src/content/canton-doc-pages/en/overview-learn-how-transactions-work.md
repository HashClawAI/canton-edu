---
title: "How Transactions Work"
slug: "overview-learn-how-transactions-work"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/learn/how-transactions-work.md"
source_title: "How Transactions Work"
tags:
  - overview
  - learn
  - how-transactions-work
---

# How Transactions Work

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# How Transactions Work

> The four-step transaction lifecycle in Canton

Every transaction on Canton follows a four-step lifecycle: submit, order and distribute, validate and confirm, and commit. Understanding this flow explains why Canton can provide both privacy and integrity without requiring every validator to see every transaction.

## The Four Steps

### Step 1: Submit

Your application sends a **command** to its validator through the Ledger API. A command describes what should happen -- "create this contract" or "exercise this choice on that contract." The validator interprets the Daml code locally, executing the smart contract logic to produce a **transaction tree**: the full set of contract creates, archives, and sub-transactions that result from the command.

The submitting validator then encrypts the transaction tree into **views**. Each view contains only the portion of the transaction relevant to a specific set of stakeholders. The encrypted views are sent to the synchronizer.

At this point, only the submitting validator has seen the full transaction. No other party or infrastructure component has access to the plaintext.

### Step 2: Order and Distribute

The synchronizer's **sequencer** receives the encrypted views, assigns them a global timestamp, and delivers each view to the validators that host the relevant parties. The sequencer provides a total ordering guarantee: all validators receive messages in the same order, which prevents conflicting transactions from being processed inconsistently.

The sequencer and the rest of the synchronizer infrastructure see only encrypted data. They know which validators should receive which messages (based on routing information), but they cannot read the transaction content.

Each validator receives only the views it needs. A validator that does not host any party involved in a particular sub-transaction receives nothing about it.

### Step 3: Validate and Confirm

Each validator that received a view now decrypts it and performs validation:

* **Re-execute the Daml logic** for their portion of the transaction to verify the result matches what the submitting validator claimed
* **Check authorization** -- are the required signatories present? Does the exercising party have the right to exercise this choice?
* **Verify contract status** -- are the consumed contracts still active?

If validation passes, the validator sends a **confirmation** to the synchronizer's **mediator**. If validation fails (for example, a contract was already archived by a concurrent transaction), the validator sends a rejection.

Validators confirm or reject based solely on their own view. They do not need to see the full transaction to verify their portion.

### Step 4: Commit

The mediator collects confirmations from all validators that received views. Once it has enough positive confirmations (the required threshold depends on the stakeholders involved), it declares the transaction **committed** and sends the result back to all participating validators through the sequencer.

Each validator then applies the transaction to its local ledger: creating new contracts, archiving consumed contracts, and recording the transaction in its history. The application that submitted the original command receives a completion notification through the Ledger API.

If the mediator receives a rejection from any required validator, the transaction is **rejected**. No state changes are applied, and the submitting application receives an error.

## Why This Design Matters

The four-step flow is what makes Canton different from traditional blockchains:

**Privacy without sacrifice.** Because the synchronizer handles only encrypted data and validators see only their own views, no single party has a global view of all transactions. Privacy is enforced by the protocol, not by application-level access controls.

**Integrity without global replication.** Each validator independently verifies its portion of the transaction. The mediator aggregates these independent checks. The result is the same integrity guarantee as a system where everyone validates everything -- but without exposing the data.

**Horizontal scaling.** Since validators only process transactions involving their hosted parties, adding more validators to the network does not increase the validation load on existing validators. Each validator's work scales with its own transaction volume, not the network's total volume.

## A Concrete Example

Alice (on Validator A) transfers an asset to Bob (on Validator B):

1. **Submit** -- Alice's application sends a `Transfer` command to Validator A. Validator A executes the Daml logic, producing a transaction that archives Alice's asset contract and creates a new one with Bob as owner. Validator A encrypts two views: one for itself (the archival) and one for Validator B (the creation).

2. **Order and Distribute** -- The sequencer timestamps the views and delivers Alice's view to Validator A and Bob's view to Validator B. No other validators receive anything.

3. **Validate and Confirm** -- Validator A verifies Alice authorized the transfer and the asset contract is still active. Validator B verifies the new contract is well-formed and Bob is a valid stakeholder. Both send confirmations to the mediator.

4. **Commit** -- The mediator sees two confirmations, declares the transaction committed, and notifies both validators. Validator A archives the old contract. Validator B stores the new contract. Alice's application receives a success response.

Throughout this process, the synchronizer never saw the asset details, the transfer amount, or even that Alice and Bob were the parties involved (beyond the encrypted routing information).

## Further Reading

* [Architecture Overview](/docs/canton/overview-learn-architecture) -- How validators, synchronizers, and applications fit together
* [Privacy Model Explained](/docs/canton/overview-learn-privacy-model) -- Detailed explanation of sub-transaction privacy and view decomposition
* [Two-Layer Consensus](/docs/canton/overview-learn-two-layer-consensus) -- The consensus protocol in more technical detail

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
