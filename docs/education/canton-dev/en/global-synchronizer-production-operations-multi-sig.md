---
title: "Multi-Sig in Canton"
slug: "global-synchronizer-production-operations-multi-sig"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/multi-sig.md"
source_title: "Multi-Sig in Canton"
tags:
  - global-synchronizer
  - production-operations
  - multi-sig
---

# Multi-Sig in Canton

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Sig in Canton

> Decentralized namespaces, decentralized party hosting, and decentralized signing of submissions in Canton.

## Introduction

In the Canton protocol, at the high level, there are three types of transactions that need to be signed: submissions, confirmations, and topology transactions. Submissions are a request to change on-ledger state, submitted by one or more parties. Confirmations are approvals by counter-parties to a submitted transaction that certify the transaction is valid and can be committed. Finally, topology transactions modify the shared global topology state of the network: they determine which Validators host a party, what rights that party grants to the Validator (submission, confirmation, or observation), and which public-private keypair the party will use to authorize transactions.

The idea of multi-sig, or decentralization, where multiple signatures are required on an action, can be applied to each of these types of transactions. This document walks you through the options for setting up:

1. A decentralized namespace (to apply decentralized control over topology transactions)
2. Decentralized party hosting (for decentralizing transaction validation & confirmation)
3. Decentralized signing of transaction submissions for a given party, including Daml models for achieving multi-sig workflows for Daml transactions, and multi-signature submissions using external parties.

## 1: Decentralizing Control Over Topology Changes

The root of trust in Canton is the private transaction signing key (or keys), which generate a signature for a transaction, proving that a given party has authorized that transaction. The transactions that *associate signing keys with parties* are an example of *topology* transactions. The transactions that give a Validator node permission to create and store data on behalf of a party (confirmation and observation rights) are *also* examples of topology transactions.

So the first level of decentralization in Canton is whether or not to decentralize control over topology transactions for a given party. If a single private-public keypair controls this association, then a signature from the private key in that keypair can change the signing keys for that party.

If the association of keys to a party requires signatures from more than one set of keys, then control over the party itself is decentralized. We refer to decentralization of control over the signing keys for a party as a "decentralized namespace": that is, a decentralized namespace maps partyIDs to keys without relying on a single authority.

### Creating A Decentralized Namespace

To create a party where control over the key to party mapping is controlled by a decentralized namespace, you construct, authorize and submit a specific set of topology transactions:

1. Namespace Delegation transactions

Create N `NamespaceDelegation` transactions, each registering a public key that will act as a foundation for the decentralized namespace. To be authorized, each of these transactions must be signed by their respective key (acting similarly to a self-signed root certificate).

2. Decentralized Namespace formation

Create a `DecentralizedNamespaceDefinition` transaction. This refers to the N keys established in the prior step, and it defines a validity threshold T which is less than or equal to N. To be authorized, this `DecentralizedNamespaceDefinition` transaction must be signed by all of the N namespace owner keys.

### Creating and Hosting a party in (controlled by) the Decentralized Namespace

Create a `PartyToParticipant transaction`, stating where the party will be hosted. This transaction serves three distinct purposes in Canton 3.4:

* Authorizes party hosting: The `PartyToParticipant` transaction states where the party will be hosted and with what rights (submission, confirmation, observation)
  * This must be signed by at least T out of the N namespace owners
* Registers keys: In Canton 3.4, the party's protocol signing key (or keys) can and should be registered in the `PartyToParticipant` transaction as well.
* Proves possession: This transaction must also be signed by the protocol keys it registers, to prove ownership of the corresponding private keys.

With the above transactions in hand and the corresponding signatures, these topology transactions may be submitted to the allocateExternalParty endpoint on the Ledger API, which creates the decentralized party. All of the hosting nodes specified in the transaction must approve the transaction before it will take effect.

In this setup, the party is secured at two distinct threshold layers:

1. Identity Control: The party's namespace is governed by the namespace owners via the `DecentralizedNamespaceDefinition` (requiring T signatures)
2. Operational control: Authorization of Daml transactions is governed by the protocol keys defined in the `PartyToParticipant` transaction.

*For further details on setting up decentralized namespaces or distributing a party across multiple confirming nodes, please refer to the Canton documentation.*

Whether or not you decentralize control over topology transactions via a decentralized namespace, you then have the option to use one or more signing keys to sign submissions by a given party. We'll cover this in section 3.

## 2: Decentralizing Confirmations

Due to the privacy model in Canton, every transaction needs to be confirmed by the participants hosting the parties that are stakeholders on the transaction. The `partyToParticipant` mapping in the topology state defines which participant(s) host every party in the network, and thus should sign confirmations for said parties. A party with more than one Validator in the `partyToParticipant` mapping is called a *multi-hosted party.* When combined with a threshold higher than 1 for confirmations, a multi-hosted party may be referred to as a *decentralized party*. The threshold defines how many of those Validator nodes need to sign the confirmation before it's considered signed by the party. Every transaction requiring confirmation from this party is sent to all participants listed in its `partyToParticipant` mapping, and once the number of confirmations from different participants crosses the threshold, the transaction is considered confirmed by the party.

## 3: Decentralizing Control over Command Submission

Canton ledger state is changed by submitting commands through a participant, which expands the commands into Daml transactions. Each command submission is signed by the party (or parties) that authorize and submit this command. For a standard (non-decentralized) party in Canton, this is simple: that party is hosted on a participant node, and submits the command via that node. For a decentralized party, this becomes more complicated, as one needs to figure out who (i.e. which user, via which participant) performs the actual submission, and how do they prove authority from a threshold of users to act on behalf of the decentralized party.

There are three main possible approaches for submissions on behalf of a decentralized party, each with its own pros and cons:

1. Collecting authority via delegation, using Daml workflows
2. In-Daml signature verification
3. External signing with multi-signatures

### Collecting Authority via Delegation Daml Workflows

A common pattern in Daml is delegating authority to execute actions on behalf of other parties. For example, a propose-accept workflow could consist of multiple steps that collect the delegation from the sender and receiver of an asset to perform a certain transaction. Depending on the exact workflow, either party can then submit a transaction for the transfer with the authority of the other party.

This pattern can be leveraged for delegating authority to "simple", i.e. non-decentralized parties to submit transactions that the decentralized party will then confirm. In this case, you will typically have one "rules" contract with the decentralized party as its signatory, and choices in that contract that define actions that different actors can perform. The "rules" will then typically include a list of parties that can take the actual actions, and under which conditions.

In the case of the Canton Coin app, for example, the `dsoParty` is a decentralized party that is the signatory on the [dsoRules contract](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L441)). The contract has a list of Super Validators (the `svs` [field](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L444) in the contract) that participate in the application.

Certain actions can then be taken by any SV, assuming certain conditions hold. These conditions are enforced via assertions in the Daml workflows themselves. For example, any SV can execute the [DsoRules\_Amulet\_Expire choice](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L1095C34-L1095C43) to archive an Amulet contract for which the expiration date has already passed.

Other actions require collecting enough confirmations from other SVs. This is also implemented in Daml. For example, any SV can invoke the [DsoRules\_RequestVote choice](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L674C34-L674C43). Any SV can then cast a vote on it via invoking the [DsoRules\_CastVote choice](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L712). Any SV can then also invoke the [DsoRules\_CloseVoteRequest choice](https://github.com/hyperledger-labs/splice/blob/0f194d4e5b55722cfd14b82a74e4b0db47f0f251/daml/splice-dso-governance/daml/Splice/DsoRules.daml#L761) to complete the process. Under the conditions encoded in Daml (e.g. enough "Yay" votes, and a certain time has been reached), the action voted on may be taken by the `dsoParty`. Note that all submissions in the process were performed by "simple", non-decentralized, parties, the SV parties in the example of Canton Coin.

We will return to the bootstrapping problem of how to create the "rules" contract owned by the decentralized party in the first place toward the end of the document.

**Pros of this approach:**

* All actions (specifically, votes and action submissions) are visible as separate on-ledger transactions.
* It does not require any off-ledger communication between the operators of the individual nodes hosting the decentralized party. They observe each other's actions on-ledger and have all the information required to act accordingly on-ledger.

**Cons of this approach:**

* Since every step (e.g. every vote) is an on-ledger transaction, it is relatively expensive in traffic on the synchronizer. Depending on the frequency of operations, this may be impractical.

### In-Daml Signature Verification

In this approach, as in the previous approach, a single party (which is *not* the decentralized party) submits a command on behalf of the decentralized party. However, the process of collecting signatures is carried out off-ledger. The collected signatures are submitted as arguments to a Daml choice, and signature verification is implemented as Daml assertions.

An example for a Daml choice asserting validity of a signature can be found in the [Daml test code](https://github.com/digital-asset/daml/blob/main/sdk/daml-script/test/daml/crypto/AttestationTests.daml). This can then be extended to a choice that asserts existence and validity of a threshold of signatures. It will still be a choice on a "rules" contract owned by the decentralized party, where the controller of the choice is another party, but the process of collecting the signatures (or "votes") is no longer implemented in this contract.

The process for collecting signatures and submitting a transaction via such a choice will then be:

* Each member (controller of a signing key) signs some agreed upon "encoded command" off-ledger. This could be, for example, some agreed upon JSON struct that encodes the details of the command to execute.
* The signatures are collected via some off-ledger channel to one node that will submit the transaction.
* The submitting node constructs a single Daml transaction via the choice described above, including the collected signatures as arguments.
* The assertions in the Daml code confirm validity, and the action is executed.

**Pros of this approach:**

* Auditability is still high, similar to the first approach, as the submitted transaction documents on-ledger which signatures have been collected.
* The Daml workflows are simpler, as signature collection (e.g. "voting") is off-ledger.
* Cheaper on on-ledger traffic
* No time-out between the time an attestation was signed and when it gets verified on-ledger. Enables workflows where the authorizing signature may be given long before submission time, e.g., air-gapped offline signing

**Cons of this approach:**

* Requires an additional off-ledger channel for collecting signatures, ensuring they are not lost, etc.
* Slightly lower auditability, as a signature that was not submitted is not recorded on-ledger

### External multi-sig signing of Daml transaction submissions

You can configure an external party to require a threshold of signatures (multi-sig) to submit Daml transactions. This setup moves the coordination of signatures off-ledger while keeping the on-ledger Daml code simpler.

Start by associating multiple protocol signing keys to the Party, via a the PartyToParticipant topology transaction. This configuration dictates:

* **Hosting:** Which nodes host the party.
* **Submission Rights:** A list of public keys (Protocol Signing Keys) and a required threshold (e.g., 3 of 5) to authorize submissions.

The process for preparing and submitting a transaction requiring multiple external signatures:

* **Prepare:** A participant node prepares the transaction payload (subject to a global timeout, typically 24h).
* **Distribute:** The payload is sent off-band to the required signers.
* **Sign:** Each member validates and signs the payload locally.
* **Collect & Submit:** A submitting node collects the signatures. Once the threshold defined in PartyToParticipant is met, it constructs the final envelope and submits it to the ledger.

<Note>
  A prepared transaction is subject to a timeout, after which submissions will fail. This is a global timeout on the synchronizer, currently configured to 24 hours on the Global Synchronizer.
</Note>

Note also that external multi-sig signing protects keys from being stolen, but it does not protect against a malicious hosting node ignoring the signature requirement. To protect against a malicious node, the party must be **Multi-Hosted** (as described in Section 2) with a confirmation threshold > 1. This forces multiple nodes to independently verify the external signatures.

**Pros of this approach:**

* Simpler Daml – No changes to Daml models are required; the party acts like any other entity in the code.
* Standard Identity – The decentralized nature is abstracted away from the application logic.

**Cons of this approach:**

* Complex Coordination – Requires robust off-ledger infrastructure to distribute payloads and collect signatures.
* Complex Validation – Signers must decode and inspect raw transaction binaries before signing.
* Limited Auditability – Individual signatures are validated by the protocol but are not visible within the Daml model history.

### Guidelines for choosing an approach for command submission

The pros and cons described above will guide your preferred choice of implementation, to summarize:

* If you expect relatively infrequent submissions for the decentralized party, and are comfortable writing more complex Daml coordination logic, you might want to choose "Collecting Authority via Delegation Daml Workflows". You will benefit from not having to establish an off-ledger channel, and full visibility on-ledger.
* If you still want on-ledger visibility, but less complex Daml workflows, and can establish (or already have) an off-ledger channel between the nodes, then "In-Daml Signature Verification" may be a good choice.
* Finally, if on-ledger visibility of the signatures is not a requirement, and you are comfortable with more complex off-ledger processes and communication between nodes, you may want to consider "External multi-sig signing".

## Additional Topics

### Bootstrapping Multi-sig Daml Workflows

The first two approaches both require the existence of a "rules" contract owned by the decentralized party, which raises the question of bootstrapping, or in simpler words, how does one get to the point where this contract exists in the first place?

There are two possible answers to this question:

* Bootstrap the decentralized party as a centralized party initially, and create this contract before decentralizing the party. This is the simpler approach, as the submission of the bootstrapping transaction is a simple non-decentralized submission, but in certain cases could lead to concerns regarding trust and liability of the bootstrapping node.
* Use multi-sig external signing for creating the "rules" contract. This basically utilizes the third approach, External multi-sig signing, to sign a single transaction that only bootstraps the process by creating the initial contract. The following workflows can follow either of the other options to derive authority from that contract.

If you start centralized, the single key holder has absolute power. To transition to decentralized, that single key holder must sign the `DecentralizedNamespaceDefinition`. This is a "trusted setup" approach.

## Key Management

Depending on your setup, there are between four sets of keys that might be used in the above. Any given setup will use either two or three of these sets of keys.

* The participant-internal keys, which the participants use to sign confirmations
* Namespace member keys, which are used to sign topology transactions. It is highly recommended to make these separate keys, as [demonstrated in the docs](https://docs.digitalasset-staging.com/operate/3.3/howtos/operate/parties/decentralized_parties.html#setup-a-decentralized-party).
* If external signing is in use, then keys for external signing are also required. It is typically acceptable for these to reuse the same keys as the namespace keys, but they can also be made different for extra security.
* Similarly, if in-Daml signature verification is used, then keys for this signing are required. In-Daml signatures may reuse the same keys as the namespace keys, but they can also be different keys, for added security.

## Risks Related to Topology Changes

### Hosting a party on an additional node with confirmation rights (Onboarding to an additional node)

Changing the set of participants hosting the decentralized namespace and party, and the corresponding thresholds, can be performed through a process called [Offline Party Replication](https://docs.digitalasset-staging.com/operate/3.3/howtos/operate/parties/party_replication.html#offline-party-replication).

Note that the current Offline Party Replication process incurs some risk on the node that is newly hosting the party, and certain mistakes in the process currently might lead to an error state on the node.

Specifically, the new node could confirm a new transaction that should not be approved, and it could also create duplicate contracts under certain conditions during party replication. Both of these known issues will be resolved in future Canton releases.

Until these issues are resolved, you should always use a fresh node when expanding the pool of nodes hosting in the decentralized party. If the onboarding process produces one of the error conditions described above, making the node unusable, you can easily replace the new node.

Once the decentralized party is onboarded to the new node, it is safe to use that node for other purposes, as offboarding the decentralized party from a node is considered a safe process in Canton 3.3 and Canton 3.4.

### Removing / offboarding a party from a node that hosts it

As of Canton 3.4 it is safe to remove a party from a Validator node, provided the following hold true:

1. The Validator has only ever connected to a single synchronizer, and no multi-synchronizer apps have been installed on that node.
2. The party will never be re-onboarded to that Validator node.

### Shutting down a node that hosts a party with (submission, confirmation, observation?) rights

It is safe to completely shut down ("offboard" or "decomission") a Validator node that hosts one or more participating in a decentralized confirmation pool.

It is also safe to bring this node onto the network within the sequencer pruning window, which is, for example, 30 days on the Global Synchronizer. After the sequencer pruning window, a number of failures could occur which currently have no known resolutions.

### Impact on Malicious Hosting Participants

Malicious or faulty nodes hosting the multi-sig party will neither impact integrity nor availability of transaction processing, as long as sufficiently valid participants are available to reach quorum.

However, a malicious or faulty node may send invalid ACS commitments. These commitments are regular checkpoints exchanged between the participant nodes to reassure each other over the current state. These commitments don't impact transaction processing, but they would alert the node operator if two participant nodes start to diverge and block pruning of the node until the disagreement is resolved or explicitly ignored.

For further reading, refer to Decentralization.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
