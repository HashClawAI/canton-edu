---
title: "SV Governance Reference"
slug: "overview-reference-sv-governance-reference"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/sv-governance-reference.md"
source_title: "SV Governance Reference"
tags:
  - overview
  - reference
  - sv-governance-reference
---

# SV Governance Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SV Governance Reference

> Governance model, voting mechanics, and governance actions for the Decentralized Synchronizer Operator (DSO)

The Global Synchronizer is governed by its Super Validators (SVs) acting collectively as the Decentralized Synchronizer Operator (DSO). Governance decisions are made through on-chain voting using Daml contracts defined in the `splice-dso-governance` package.

## DSO Governance Model

CC, CNS, and Global Synchronizer governance are implemented in a decentralized fashion to tolerate up to `f` faulty or dishonest SV nodes for `f = numSvNodes - t` and confirmation threshold `t = ceiling (numSvNodes * 2.0 / 3.0)`.

The implementation uses three key techniques to achieves this Byzantine fault tolerance:

* **DSO party**: it sets up a decentralized Daml party, called the DSO party, with confirmation threshold `t` and hosted on all SV nodes.
* **on-ledger confirmations**: it requires explicit on-ledger confirmations from `t` SV nodes for exercising choices with off-ledger input in the name of the DSO party.
* **decentralized automation**: all SV nodes run automation code that attempts to exercise choices required to be executed by the DSO party. The choices are either executed directly if they do not require off-ledger input, or they are exercised indirectly by creating the corresponding confirmation if they require off-ledger input. The automation exercises choices in a timely fashion, so that the skew between the target time and the actual time is bounded on average.
* **median-based voting**: agreement on conversion rates and like configuration parameters is achieved using median-based voting, where every SV operator publishes their desired value on-ledger and the DSO party uses the median of these values.

Thus CC and CNS users that are willing to assume that no more than `f` SV nodes are dishonest can rely on the following guarantees:

* **valid transactions**: every transaction that requires confirmation from the DSO party is [valid](/docs/canton/overview-learn-ledger-model).
* **timely automation**: actions required to be taken by the DSO party are taken in a timely fashion.
* **predictable fees and configuration values**: fees and configuration values are reasonably predictable as they represent the *aggregate preferences* of \~2/3 of SV operators, which can be assumed to be acting in their own best interest.

The guarantee of valid transactions is particularly important for CC and CNS users, as it is used to decouple the concerns of implementing decentralized automation and governance from the concern of implementing the tokenomics and business logic of CC and CNS.

All code other than `splice-dso-governance` and `splice-validator-lifecycle` is written under the assumption that the DSO party behaves as an honest provider of the CC and CNS applications. We define what this means in the sections below.

This approach of factoring out decentralization concerns using a decentralized party greatly simplifies the code, and enables factoring the code as shown in the package dependency graph:

<img src="https://mintcdn.com/cantonfoundation/805bfL5zagaL0yiJ/overview/reference/images/daml-package-dependencies.png?fit=max&auto=format&n=805bfL5zagaL0yiJ&q=85&s=f3dd07a1160b603f0771882b48e0ea5a" class="align-center" alt="Daml package dependency graph" width="1712" height="1133" data-path="overview/reference/images/daml-package-dependencies.png" />

###

The DSO is a decentralized party hosted across all SV nodes. It uses a Byzantine Fault Tolerant (BFT) confirmation model where actions require approval from a supermajority of SVs. The system tolerates up to `f` faulty or dishonest nodes, where `f = floor((n - 1) / 3)` and `n` is the total number of SVs.

The required number of votes for any governance action is:

```
requiredNumVotes = ceiling((numSVs + f + 1) / 2)
```

This threshold ensures two properties: **integrity** (a dishonest minority cannot push through an action) and **availability** (up to `f` abstaining SVs cannot block progress).

## Governance Roles

Any SV can propose a governance action by creating a `VoteRequest` on-chain. All other SVs can then cast votes (accept or reject) on that request. Once the vote threshold is met, the DSO delegate executes the action.

There are two execution paths for actions that require confirmation:

* **Voted actions** -- Any SV creates a vote request; other SVs respond with accept/reject votes. The action executes when `requiredNumVotes` accept votes are collected.
* **Automated confirmations** -- For routine operational actions (like advancing mining rounds), each SV node automatically creates a confirmation when its preconditions are met. Once enough confirmations accumulate, execution proceeds without manual voting.

## Voting Mechanics

Vote requests are represented as `VoteRequest` Daml contracts on the DSO ledger. Each request specifies the proposed `ActionRequiringConfirmation`, a `voteBefore` deadline, and an optional `targetEffectiveAt` timestamp for scheduled actions.

A vote resolves as:

* **Accepted** -- At least `requiredNumVotes` SVs vote to accept. The action executes on-chain.
* **Rejected** -- At least `requiredNumVotes` SVs vote to reject. The request is archived.
* **Expired** -- The `voteBefore` deadline passes without enough votes in either direction.

For vote requests with a `targetEffectiveAt` date, the action executes only after both the threshold is reached and the effective time has passed. This allows SVs to schedule changes in advance, such as parameter updates or upgrade activations.

SV operators manage votes through the **Governance tab** in the SV web UI, where they can create new vote requests, review pending proposals, cast their votes, and track outcomes. The UI groups vote requests into categories such as "Action Needed", "In Progress", "Planned", "Executed", and "Rejected" for easier tracking.

## Types of Governance Actions

Governance actions fall into three categories based on the Daml data types that represent them: `ARC_DsoRules`, `ARC_AmuletRules`, and `ARC_AnsEntryContext`.

### DSO Rules Actions (`ARC_DsoRules`)

* **Add SV** (`SRARC_AddSv`) -- Onboard a new Super Validator to the DSO
* **Offboard SV** (`SRARC_OffboardSv`) -- Remove a Super Validator from the DSO
* **Grant featured app right** (`SRARC_GrantFeaturedAppRight`) -- Approve an application provider for featured app rewards
* **Revoke featured app right** (`SRARC_RevokeFeaturedAppRight`) -- Remove featured app status from a provider
* **Update SV reward weight** (`SRARC_UpdateSvRewardWeight`) -- Change the reward weight assigned to an SV
* **Set DSO config** (`SRARC_SetConfig`) -- Modify the `DsoRulesConfig`, which controls network-level parameters

### Amulet Rules Actions (`ARC_AmuletRules`)

* **Set amulet config** (`CRARC_SetConfig`) -- Change the `AmuletConfig`, which governs Canton Coin economics including fee schedules, issuance curves, and traffic pricing

### Canton Name Service Actions (`ARC_AnsEntryContext`)

* **Collect initial entry payment** (`ANSRARC_CollectInitialEntryPayment`) -- Automated collection of payment for a new CNS entry
* **Reject entry payment** (`ANSRARC_RejectEntryInitialPayment`) -- Automated rejection of an invalid CNS entry payment

### Automated Actions

Some actions do not require manual voting. SV nodes create confirmations automatically when preconditions are met:

* **Start issuing round** (`CRARC_MiningRound_StartIssuing`) -- Transition a mining round to issuing once reward summaries are computed
* **Archive closed mining round** (`CRARC_MiningRound_Archive`) -- Clean up fully expired mining rounds
* **Confirm SV onboarding** (`SRARC_ConfirmSvOnboarding`) -- Confirm that a party can become an SV after identity verification

## Parameter Governance

SVs govern network parameters through voted config changes. Key configurable parameters include:

* **Traffic pricing** (`extraTrafficPrice`) -- The USD cost per MB of synchronizer traffic. Per [CIP-0042](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0042/cip-0042.md), this should be calibrated so a standard Canton Coin transfer costs 1 USD.
* **Read vs. write scaling factor** (`readVsWriteScalingFactor`) -- The ratio of read traffic cost relative to write traffic cost, reflecting the lower infrastructure cost of message delivery compared to ordering and persistence.
* **CC-USD conversion rate** -- Each SV publishes their desired dollar-to-CC rate on-chain. The DSO uses the **median** of all published values, making the rate resistant to manipulation by any single SV.
* **Round duration** -- The length of mining rounds (default: 10 minutes), which determines how frequently rewards are calculated and issued.
* **SV reward weights** -- Each SV has a configurable reward weight that determines their share of SV reward distributions. Changes require a governance vote and should also be reflected in the [GSF configs repository](https://github.com/global-synchronizer-foundation/configs).

The median-based approach for the CC-USD rate means that every SV operator publishes their preferred value, and the system automatically selects the median. This produces predictable, aggregate-preference pricing that represents roughly two-thirds of SV operators' positions.

Traffic parameters require periodic recalibration. Actual traffic costs change depending on factors like the number of SVs in the DSO and the Canton protocol version, so SVs are expected to measure current costs and adjust parameters through governance votes accordingly.

## CIP Process

Formal changes to Canton Network standards and protocols go through the Canton Improvement Proposal (CIP) process. CIPs cover technical specifications, governance procedures, and informational guidelines. SVs vote on CIP adoption through the same on-chain governance mechanism described above.

For a full overview of the CIP lifecycle and how to participate, see [What Are CIPs?](/docs/canton/overview-reference-what-are-cips). The CIP repository is maintained at [github.com/global-synchronizer-foundation/cips](https://github.com/global-synchronizer-foundation/cips).

## Global Synchronizer Foundation

The [Global Synchronizer Foundation (GSF)](https://sync.global) is an independent, non-profit body under the Linux Foundation created to support the governance and growth of the Global Synchronizer. The GSF:

* Operates its own SV node and participates in governance votes on behalf of its members
* Provides transparency into Super Validator governance decisions and network operations
* Coordinates upgrade schedules and maintenance across the SV operator group
* Manages the Splice codebase governance and oversees featured application review

The GSF does not have unilateral control over the network. Its SV node carries the same voting weight as any other SV, and all governance actions still require the standard BFT vote threshold to pass. The current list of Super Validators is maintained by the GSF.

## On-Chain Governance Architecture

All governance state lives on-chain as Daml contracts. The `DsoRules` contract holds the authoritative record of DSO membership (`svs` map), the DSO delegate, and the current configuration. The `AmuletRules` contract holds the Canton Coin configuration schedule. Vote requests, confirmations, and SV state contracts are all ledger-visible, making governance auditable by any party with access to the Scan app.

The decentralized party model means that the DSO party itself has a confirmation threshold of `ceiling(numSVs * 2.0 / 3.0)`. Every transaction signed by the DSO party must be confirmed by at least that many SV participant nodes, enforcing BFT at the Canton protocol layer independent of the application-level voting logic.

## BFT Guarantees

The combination of on-chain voting and decentralized automation provides three guarantees for network participants who trust that no more than `f` SVs are dishonest:

* **Valid transactions** -- Every DSO-confirmed transaction satisfies Daml's [ledger validity model](/docs/canton/overview-learn-ledger-model)
* **Timely automation** -- Routine operational actions (round advancement, reward issuance) execute without delay
* **Predictable parameters** -- Fees and configuration values reflect the aggregate preferences of at least two-thirds of SV operators

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
