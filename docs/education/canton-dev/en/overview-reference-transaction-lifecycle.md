---
title: "Transaction Lifecycle"
slug: "overview-reference-transaction-lifecycle"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/transaction-lifecycle.md"
source_title: "Transaction Lifecycle"
tags:
  - overview
  - reference
  - transaction-lifecycle
---

# Transaction Lifecycle

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Transaction Lifecycle

> Complete five-phase lifecycle of a Canton transaction — from preparation through sequencing, validation, and final commit

A Canton transaction passes through five distinct phases before it commits (or is rejected). Each phase involves specific node roles — participant nodes, sequencer nodes, and mediator nodes — communicating through encrypted, sequenced messages. No single node ever sees the full transaction in the clear.

The phases are:

1. **Preparation** — the submitting participant interprets the command and constructs encrypted transaction views
2. **Submission** — the participant sends a confirmation request batch to the sequencer
3. **Sequencing and Distribution** — the sequencer orders and delivers messages to recipients
4. **Validation and Confirmation** — each confirming participant validates its views and responds to the mediator
5. **Aggregation and Commit** — the mediator collects responses, renders a verdict, and participants apply (or discard) the result based on the verdict

## Phase 1: Preparation

The lifecycle begins when the submitting participant node receives a command from an application through the Ledger API (gRPC). The participant then:

* **Interprets the command** by executing the Daml smart contract code locally in the Daml engine. The engine evaluates the command against the participant's current Active Contract Set (ACS) and produces a full transaction tree — a structure containing every action (creates, exercises, fetches), the consequences of each action, and all associated metadata.

* **Determines informees** for each action node in the tree. Informees are the parties who are entitled to see a given action — signatories, observers, and actors (executing the choice), as defined by the Daml template. The informee set for each action governs who receives which parts of the transaction.

* **Decomposes the transaction into views.** Each action node in the transaction tree becomes a separate view. A view contains the action, its consequences, and enough context for validation — but nothing more. Each view is encrypted so that only its informees (and the participants hosting those informees) can decrypt it. Non-informees learn nothing about the action: not the payload, not the parties, not even that the action exists.

* **Computes a root hash** that cryptographically commits to the entire transaction tree. The root hash binds all views together: every confirming participant can verify that the view it received belongs to the same transaction that every other participant is validating. The mediator uses the root hash to correlate confirmation responses.

If the transaction touches contracts on multiple synchronizers, the participant may need to reassign those contracts to a common synchronizer before submission. This is handled by the [Reassignment Protocol](/docs/canton/overview-reference-reassignment-protocol).

## Phase 2: Submission (Confirmation Request)

The submitting participant sends a **confirmation request batch** to the sequencer. The batch contains three categories of message:

* **Encrypted views** — one per action node. Each view is encrypted for the participants that host its informees. A participant that does not host any informee of a particular view cannot decrypt it and never receives it.

* **Root hash messages** — one per recipient participant. Each root hash message carries the transaction's root hash, allowing the recipient to correlate the views it receives to a single transaction.

* **Informee messages** — sent to the mediator. These list the informees and the confirmation policy for each view. The confirmation policy specifies which signatories need to confirm, and the threshold of hosting participants that must approve for each signatory. The mediator uses this information to determine when enough confirmations have arrived.

The submitting participant sends all of these messages in a single batch to the sequencer.

## Phase 3: Sequencing and Distribution

The sequencer processes the confirmation request batch:

1. **Assigns a timestamp.** This is the sequencing time for the transaction. The sequencer performs a BFT-write: the ordering nodes reach agreement on the position and timestamp of this batch in the global message sequence. The timestamp becomes the reference point for all subsequent deadlines.

2. **Delivers each message to its designated recipients only.** Participants receive the encrypted views where they host an informee party, plus their root hash message. The mediator receives the informee messages. A participant that hosts no informees for any view in the transaction receives nothing and learns nothing about the transaction.

The mediator, upon receiving the informee messages:

* Records the confirmation request metadata (root hash, informee lists, confirmation policies)
* Starts a **confirmation deadline timer** based on the sequencing time and the synchronizer's configured decision time parameter
* Awaits confirmation responses from participants

## Phase 4: Validation and Confirmation

Each participant that received views independently validates them. The validation checks are:

* **Conformance** — the participant re-executes the Daml contract logic for each action in the view it received. The re-execution must produce the same consequences (created contracts, archived contracts) as claimed in the view. If the results diverge, the view is malformed or the submitter is dishonest.

* **Authorization** — the participant checks that every action is properly authorized. For each action, the required parties (signatories, controllers) must have authorized it. Authorization is verified through the party-to-participant topology and the Daml authorization rules.

* **Consistency** — the participant checks that all input contracts referenced by the view are still active in its local ACS. A contract that has already been consumed (archived) cannot be used again. This check is what prevents double-spends within a single synchronizer.

* **Time bounds** — the participant verifies that the ledger time claimed for the transaction falls within the acceptable bounds relative to the sequencing time (record time). The tolerance window is a synchronizer parameter.

* **Root hash** — the participant verifies that the view it received is consistent with the root hash from the root hash message. This ensures all participants are validating views from the same transaction tree, preventing a malicious submitter from sending different views to different participants.

After validation, the participant constructs a **mediator response (MR)** message:

* **Approve** if all checks pass for all views the participant received
* **Reject** if any check fails, with a rejection reason

The mediator response is sent to the sequencer, which performs another BFT-write to timestamp the message, then delivers it to the mediator. The confirming participant does not send its response directly to the mediator — all communication flows through the sequencer.

## Phase 5: Aggregation and Commit

The mediator collects mediator response messages and evaluates them against the confirmation policy:

1. **Aggregation.** For each view, the confirmation policy specifies which signatory parties must confirm. A signatory party may be hosted on multiple participants; the policy defines a confirmation threshold — how many hosting participants must approve for that signatory to count as confirmed. The mediator tracks approvals per signatory, per view. This includes the case where the submitting party is multi-hosted.

2. **Verdict determination.** Two outcomes are possible:
   * **Approve**: all signatory thresholds for all views are met before the confirmation deadline. Every required signatory has enough hosting participants that approved.
   * **Reject**: any required participant explicitly rejects, or the confirmation deadline expires without sufficient approvals. A single signatory failing its threshold is enough to reject the entire transaction.

3. **Transaction result distribution.** The mediator sends a **transaction result (TR)** message to the sequencer. The sequencer delivers this verdict to all informee participants. When a participant reads the verdict from the sequencer, it performs a BFT-read — verifying the sequencer's signature on the delivered message to confirm authenticity.

4. **Local commit or discard.** Each participant processes the verdict:
   * **On approve**: the participant commits the transaction. It archives consumed contracts, creates new contracts, and updates the ACS. The transaction and its effects become part of the participant's local ledger projection.
   * **On reject**: the participant discards the transaction. No state changes are applied. The ACS remains unchanged.

Once the verdict is sequenced and delivered, the transaction result is **final**. There are no forks, reorganizations, or rollbacks. A committed transaction stays committed; a rejected transaction stays rejected.

## Message Summary

The following table summarizes the messages exchanged during the protocol, their senders, recipients, and contents.

| Message                     | Sender                 | Recipient(s)                               | Content                                        |
| --------------------------- | ---------------------- | ------------------------------------------ | ---------------------------------------------- |
| **Command**                 | Application            | Submitting participant                     | Daml command (create, exercise) via Ledger API |
| **Encrypted views**         | Submitting participant | Sequencer, then informee participants      | One per action node; encrypted per-informee    |
| **Root hash messages**      | Submitting participant | Sequencer, then each recipient participant | Root hash of the full transaction tree         |
| **Informee messages**       | Submitting participant | Sequencer, then mediator                   | Informee list and confirmation policy per view |
| **Mediator response (MR)**  | Confirming participant | Sequencer, then mediator                   | Approve or reject (with reason)                |
| **Transaction result (TR)** | Mediator               | Sequencer, then all informee participants  | Final verdict: approve or reject               |

## Timing and Deadlines

Two time parameters govern the protocol's liveness:

* **Sequencing time** — assigned by the sequencer when the confirmation request batch is ordered. This is the transaction's reference timestamp.
* **Decision time** — computed as the sequencing time plus the synchronizer's `decisionTimeout` parameter. If the mediator has not received sufficient confirmations by the decision time, the transaction is rejected by timeout.

Participants also enforce a **participant response deadline**: they must send their mediator response before a configured cutoff derived from the sequencing time. A participant that fails to respond in time is treated as non-confirming for that transaction.

## Failure Modes

Transactions can fail at several points in the lifecycle:

* **Preparation failure**: the Daml engine rejects the command (e.g., contract not found, authorization failure, assertion violation). The command is rejected synchronously before any messages are sent. No other nodes are involved.

* **Validation rejection**: a confirming participant finds a conformance, authorization, consistency, or time-bounds violation. It sends a reject MR. Depending on the confirmation policy, a single rejection may be sufficient to reject the entire transaction.

* **Timeout**: not enough participants respond before the decision time. The mediator rejects the transaction. This can happen if participants are offline, overloaded, or unreachable.

* **Equivocation detection**: if the submitter sends inconsistent views to different participants (views that do not match the root hash), honest participants detect the inconsistency during root hash validation and reject.

In all failure cases, no state is changed. The ACS on every participant remains as it was before the transaction was submitted.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
