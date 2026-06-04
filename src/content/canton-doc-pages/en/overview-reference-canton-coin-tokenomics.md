---
title: "Canton Coin Tokenomics"
slug: "overview-reference-canton-coin-tokenomics"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/canton-coin-tokenomics.md"
source_title: "Canton Coin Tokenomics"
tags:
  - overview
  - reference
  - canton-coin-tokenomics
---

# Canton Coin Tokenomics

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Coin Tokenomics

> Technical reference for Canton Coin fees, minting rounds, activity records, and burn-mint equilibrium

Canton Coin (CC) is the native utility token of the Global Synchronizer. It is implemented through the [Splice](https://github.com/canton-network/splice) open-source infrastructure, where it is referred to as "Amulet" at the Daml contract level. CC serves three functions: paying for network usage (traffic), rewarding infrastructure operators and application providers, and governing the network through Super Validator participation.

For background on CC's role in the network and how to obtain it, see [Canton Coin and the Global Synchronizer](/docs/canton/overview-understand-canton-coin). The [Canton Coin white paper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf) provides the full formal specification.

## Fee Structure

CC has three fee types. Following [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md), transfer fees and lock fees were eliminated, leaving traffic fees and holding fees as the two active mechanisms.

### Traffic Fees

Traffic credits are non-transferable. Once CC is converted to traffic, it can only pay for transaction submissions. If a validator's traffic budget is exhausted, transactions will fail. Auto-top-up automation is available and recommended.

<Note>
  Traffic credits are consumed even if a confirmation request fails due to contention on consuming contracts -- for example, when two transfers attempt to consume the same coin contract.
</Note>

### Holding Fees

Canton Network tokenomics is based on an *Activity Record* which identifies a party that performed an action which provides value to the network. An activity record has a *weight* which is the relative share of CC minting associated with this activity record.

Creating an activity record and minting the associated Canton Coin (CC) are two distinct steps. The creation and minting steps are performed in a cycle that is called a *round* which has five phases. In the first phase, any fee values for that round are written to the ledger (the fees can be obtained from the Scan State API). The second phase is called the *activity recording* and it is when activity records are created; records created in this phase belong to that round. The next phase calculates a [CC-issuance-per-activity-weight](https://github.com/canton-network/splice/blob/332e06a7ae9e13fde5bba0bf7dcb059aa36f979e/daml/splice-amulet/daml/Splice/Issuance.daml#L67) for each kind of activity record which is the share of total CC that can be minted for this type of activity record. This is followed by a *minting phase* where the owners of an activity record can mint CC proportional to its minting weight.

There are several rounds active concurrently with each round being in a different phase. A round starts every 10 minutes, which is a configuration parameter that the Super Validators may change in the future via a governance vote. See the CC whitepaper for the details.

There is no difference in activity record creation for an external party or a local party, but there is a difference in the automation support used in the minting phase. For local parties onboarded to a validator, the validator application runs background automation to mint all activity records automatically. An external party signs transactions using a key they control. As a consequence, the validator automation is not able to perform minting for external parties directly. For external parties, there are two options:

1. Use a minting delegation to delegate reward collection to a validator, avoiding the need to build custom automation.
2. Develop custom automation to call AmuletRules\_Transfer at least once per round with all activity records as inputs.

An approved CIP called [Weighted Validator Liveness Rewards for SV-Determined Parties](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) describes providing this support.

As an aside, some interesting templates are important to the tokenomics are:

* AmuletRules which stores the fees schedules;
* OpenMiningRound which stores the price and fees as of opening the round;
* IssuingMiningRound which stores the amount-to-mint-per-activity-weight.

## Types of Activity Records

There are five key templates involved in the accounting for network activity:

* Two templates are application related:

  > * FeaturedAppActivityMarker
  > * AppRewardCoupon

* Three templates relate to providing the infrastructure for the applications:

  > * ValidatorRewardCoupon
  > * ValidatorLivenessActivityRecord
  > * SvRewardCoupon

The last four are activity records while a `FeaturedAppActivityMarker` is not considered an activity record. As discussed later, a `FeaturedAppActivityMarker` is converted into an `AppRewardCoupon` via automation run by the Super Validators. The featured CC transfer and `FeaturedAppActivityMarker`` both generate the same reward. The ``FeaturedAppActivityMarker`\` is the preferred way to generate app activity records.

The `FeaturedAppActivityMarker`, `AppRewardCoupon`, and `ValidatorRewardCoupon` contracts are created when an application's transaction succeeds. In general, an application receives rewards when its Daml code directly creates `FeaturedAppActivityMarker` contracts or interacts with Daml models that feature the application provider's party. A `ValidatorRewardCoupon` is created for every call to `AmuletRules_Transfer` (e.g., a CC Transfer using the Splice Wallet UI) or when CC is burned.

Aside from the minting weight, an application's reward also depends on whether it is designated as *featured* or *unfeatured* (the default state). After CIP-0078 was implemented, only featured applications get a reward. A featured application receives a minting weight with a total equivalent value of about \$1 US (the SuperValidators may adjust this in the future).

## How to become a featured application

To become a featured application you need an *application provider's party ID* which is an input to the application. That process starts by filling in [this form](https://sync.global/featured-app-request/). The request goes to the tokenomics committee who reviews the application and responds to it. This [webpage](https://lists.sync.global/g/tokenomics/topics) lists the tokenomics committees topics for tracking. Here’s an [example of a successful submission](https://lists.sync.global/g/tokenomics/topic/new_featured_app_request/112787885). Note that, for testing purposes, you can self-feature your application on DevNet.

For some of the templates, the attribution of activity can be shared with multiple beneficiary parties. For example, a featured application reward can be shared between the application provider and application user, based on a given `weight` for each. The general pattern for this is:

* A list of beneficiaries, each with a `weight`, is provided. The weights sum up to `1.0`.
* Later processing creates a separate contract for each beneficiary and weight pair, setting the contract's `beneficiary` and `weight` fields accordingly.

Beneficiaries are discussed further in the following sections.

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) eliminated almost all fees for Canton Coin transfers and locks so unfeatured applications no longer receive any reward. The holding fee remains but its behavior changed so that no holding fees are charged when using a coin as an input to a transfer.

The holding fees is a fixed fee, per separate coin contract (UTXO) per unit of time, that is independent of the coin amount. It promotes merging of CC to reduce network storage use by incentivizing merging or removal of dust coins. Holding fees are not charged when transferring coins but only explicitly on expired coin contracts via the `Amulet_Expire` choice. A coin contract (UTXO) may be expired by the Super Validators once its accrued holding fees are greater than its coin value. This makes accounting for holding fees simple as the value of the coin contract is constant and independent of the holding fee.

Because the holding fee is per-UTXO rather than per-CC-amount, small "dust" coins accrue fees faster relative to their value. Once the accrued holding fee exceeds the coin's value, Super Validators can expire the contract, removing it from the ledger. This makes accounting straightforward: the face value of a coin contract stays constant and does not decrease with accumulated fees.

### Transfer and Lock Fees (Post CIP-0078)

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) eliminated almost all fees for CC transfers and locks. Neither legacy Amulet transfers, CN Token Standard two-step transfers, nor one-step `TransferPreapproval` transfers charge fees. The only exception is that featured one-step transfers still generate an `AppRewardCoupon` for the provider party who maintains the `TransferPreapproval` contract.

## Burn-Mint Equilibrium

The supply of CC is therefore dynamic rather than fixed. The maximum minting curve constrains how fast new coins can enter circulation, while burn events from traffic purchases remove coins.

Minting rewards are distributed across four categories of contributors:

* **Super Validators** earn minting rights by operating synchronizer nodes (sequencers, mediators, and governance infrastructure).
* **Application providers** earn rewards when they facilitate transactions through featured applications.
* **Validators** earn minting rights proportional to the fees they burn, which the network treats as a proxy for the activity generated by that node.
* **Liveness incentives** reward validators for uptime and readiness. If a validator does not use all its minting allowance via direct activity, a portion is allocated as a liveness bonus.

## Minting Rounds

Three Daml templates drive the round lifecycle:

* **`AmuletRules`** stores the fee schedules
* **`OpenMiningRound`** stores the price and fees as of the round's opening
* **`IssuingMiningRound`** stores the computed CC-issuance-per-activity-weight

### Minting for External Parties

For local parties, the validator application runs background automation that mints all activity records automatically. External parties sign transactions with keys they control, so the validator automation cannot mint on their behalf directly. External parties have two options:

* **Minting delegation** -- Delegate reward collection to a validator, avoiding custom automation.
* **Custom automation** -- Call `AmuletRules_Transfer` at least once per round with all activity records as inputs.

[CIP-0073 (Weighted Validator Liveness Rewards for SV-Determined Parties)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) describes additional support for this workflow.

## Activity Records

Activity record attribution can be shared among multiple beneficiaries. Each beneficiary receives a `weight` (summing to 1.0), and the system creates a separate contract per beneficiary/weight pair during minting.

## Featured vs. Unfeatured Applications

An application's reward depends on whether it is designated as *featured* or *unfeatured* (the default). After CIP-0078, only featured applications receive a reward. A featured application gets a minting weight with a total equivalent value of approximately \$1 USD per qualifying activity (the Super Validators may adjust this amount).

The `FeaturedAppActivityMarker` is the preferred mechanism for generating application activity records. Featured one-step transfers via `TransferPreapproval` also generate an `AppRewardCoupon` for the provider party.

To become a featured application, submit a request through the [GSF featured app request form](https://sync.global/featured-app-request/). The tokenomics committee reviews submissions; progress is tracked on the [tokenomics committee topics page](https://lists.sync.global/g/tokenomics/topics). On DevNet, you can self-feature your application for testing purposes.

## UTXO Model and Dust Expiry

CC holdings use a UTXO (unspent transaction output) model. Each coin is represented as an individual `Amulet` contract on the ledger with a specific face value. Transfers consume input UTXOs and create new output UTXOs, similar to Bitcoin's transaction model but with privacy -- balances are visible only to entitled parties, and there is no public ledger of all holdings.

When a transfer produces change (the input exceeds the amount being sent), a new UTXO is created for the remainder. Over time, this can result in a wallet holding many small-value UTXOs.

### Dust Expiry

The per-UTXO holding fee creates a natural cleanup mechanism for dust. Because the fee is fixed per contract regardless of the coin's face value, a 0.001 CC coin and a 1000 CC coin accrue the same holding fee per unit of time. Small coins therefore become uneconomical faster.

Once the accrued holding fee on a UTXO exceeds its face value, Super Validators can expire the contract by exercising the `Amulet_Expire` choice. This removes the contract from the ledger entirely. Users are incentivized to merge small coins into larger ones to minimize the number of UTXOs and reduce holding fee exposure. The Splice wallet automation handles this merging automatically when possible.

## CN Token Standard (CIP-0056)

[CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) defines the Canton Network Token Standard, a set of Daml interfaces for token operations including transfers, locks, and metadata queries. The Splice wallet implements CIP-0056 for CC, and applications that handle CC programmatically interact through these standard interfaces.

CIP-0056-based two-step transfers work as follows:

1. The sender locks the desired CC amount, creating a transfer offer.
2. The receiver accepts the offer, which unlocks the CC and completes the transfer.

This two-step flow does not rely on sender-side automation and works well for external parties. Since CIP-0078, these operations incur no fees and generate no activity records.

For API details, see the [CIP-0056 text](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) and the [token standard source code](https://github.com/canton-network/splice/tree/main/token-standard#readme).

## Related Resources

* [Canton Coin and the Global Synchronizer](/docs/canton/overview-understand-canton-coin) -- conceptual overview and how to obtain CC
* [CIP-0078 (CC Fee Removal)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) -- the proposal that eliminated transfer and lock fees
* [CIP-0056 (CN Token Standard)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) -- standard interfaces for token operations
* [CIP-0073 (Weighted Validator Liveness Rewards)](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) -- liveness reward support for SV-determined parties
* [Canton Coin white paper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf) -- full formal specification

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
