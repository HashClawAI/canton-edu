---
title: "Tokenomics"
slug: "appdev-deep-dives-tokenomics"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/tokenomics.md"
source_title: "Tokenomics"
tags:
  - appdev
  - deep-dives
  - tokenomics
---

# Tokenomics

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Tokenomics

> Canton Network tokenomics: rounds, activity records, transfers, traffic, and reward distribution

Following is an overview of the Canton Network tokenomics for application developers and validator operators. It builds on the [Canton Coin whitepaper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf) and assumes you have read it.

Canton Network tokenomics is based on an *Activity Record* which identifies a party that performed an action which provides value to the network. An activity record has a *weight* which is the relative share of CC minting associated with this activity record.

Creating an activity record and minting the associated Canton Coin (CC) are two distinct steps. The creation and minting steps are performed in a cycle that is called a *round* which has five phases. In the first phase, any fee values for that round are written to the ledger (the fees can be obtained from the Scan State API). The second phase is called the *activity recording* and it is when activity records are created; records created in this phase belong to that round. The next phase calculates a [CC-issuance-per-activity-weight](https://github.com/canton-network/splice/blob/332e06a7ae9e13fde5bba0bf7dcb059aa36f979e/daml/splice-amulet/daml/Splice/Issuance.daml#L67) for each kind of activity record which is the share of total CC that can be minted for this type of activity record. This is followed by a *minting phase* where the owners of an activity record can mint CC proportional to its minting weight.

There are several rounds active concurrently with each round being in a different phase. A round starts every 10 minutes, which is a configuration parameter that the Super Validators may change in the future via a governance vote. See the CC whitepaper for the details.

There is no difference in activity record creation for an [external party](/appdev/deep-dives/external-signing-onboarding) or a local party, but there is a difference in the automation support used in the minting phase. For local parties onboarded to a validator, the validator application runs background automation to mint all activity records automatically. An external party signs transactions using a key they control. As a consequence, the validator automation is not able to perform minting for external parties directly. For external parties, there are two options:

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

### How to become a featured application

To become a featured application you need an *application provider's party ID* which is an input to the application. That process starts by filling in [this form](https://sync.global/featured-app-request/). The request goes to the tokenomics committee who reviews the application and responds to it. This [webpage](https://lists.sync.global/g/tokenomics/topics) lists the tokenomics committees topics for tracking. Here’s an [example of a successful submission](https://lists.sync.global/g/tokenomics/topic/new_featured_app_request/112787885). Note that, for testing purposes, you can self-feature your application on DevNet.

For some of the templates, the attribution of activity can be shared with multiple beneficiary parties. For example, a featured application reward can be shared between the application provider and application user, based on a given `weight` for each. The general pattern for this is:

* A list of beneficiaries, each with a `weight`, is provided. The weights sum up to `1.0`.
* Later processing creates a separate contract for each beneficiary and weight pair, setting the contract's `beneficiary` and `weight` fields accordingly.

Beneficiaries are discussed further in the following sections.

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) eliminated almost all fees for Canton Coin transfers and locks so unfeatured applications no longer receive any reward. The holding fee remains but its behavior changed so that no holding fees are charged when using a coin as an input to a transfer.

The holding fees is a fixed fee, per separate coin contract (UTXO) per unit of time, that is independent of the coin amount. It promotes merging of CC to reduce network storage use by incentivizing merging or removal of dust coins. Holding fees are not charged when transferring coins but only explicitly on expired coin contracts via the `Amulet_Expire` choice. A coin contract (UTXO) may be expired by the Super Validators once its accrued holding fees are greater than its coin value. This makes accounting for holding fees simple as the value of the coin contract is constant and independent of the holding fee.

{/* COPIED_START source="splice:docs/src/background/tokenomics/feat_app_act_marker_tokenomics.rst" hash="f4ed8911" */}

## Featured Application Activity Marker

The *featured application activity marker* is specified in [CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md). A summary follows.

Featured application activity markers (FeaturedAppActivityMarker) can be created for a transaction that adds value but does not involve a CC Transfer (e.g., a stable coin transfer or the settlement of a trade). [CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) says:

> Featured application providers are expected to create featured application activity markers only for transactions that correspond to a transfer of an asset, or an equivalent transaction, which was enabled by the application provider. The detailed fair usage policy and enforcement thereof is left up to the Tokenomics Committee of the Global Synchronizer Foundation (GSF).

Generally the guidance is to create a `FeaturedAppActivityMarker` for any economically important event, such as:

* Lock or unlock a Real World Asset (RWA).
* Transfer a RWA.
* Mint or burn tokens.

However, it should not be created for any intermediate steps or a [propose step](/appdev/modules/m3-authorization#use-propose-accept-workflow-for-one-off-authorization).

A `FeaturedAppActivityMarker` is immediately converted into an AppRewardCoupon by the automation run by the Super Validators. The AppRewardCoupon is created with the DSO as the `signatory` and the `provider` field as an observer. By default, the `provider` can mint CC in the minting step. The `featured` field is set to `true` to indicate eligibility to receive featured application rewards, based on a FeaturedAppRight contract.

There can be several `FeaturedAppActivityMarkers` per transaction tree which increases the total reward. However, this is only allowed for composed transactions (e.g. a settlement transaction) where trading venue and all the registries of the transferred assets would get featured app rewards. It is also possible for a single Canton transaction tree to include ValidatorRewardCoupon, an AppRewardCoupon and a FeaturedAppActivityMarker(s) if there are sub-transcations that create each separately.

A non-featured app cannot accrue a `FeaturedAppActivityMarker`.

## Creating a Featured Application Activity Marker

There are two prerequisites for an application to create a `FeaturedAppActivityMarker`. The first is to become an approved featured application which was described in the `types_of_activity_records` section. The second is to update the application code:

> 1\. Find the fully qualified package-id of the interface definition for the FeaturedAppRight interface which is `7804375fe5e4c6d5afe067bd314c42fe0b7d005a1300019c73154dd939da4dda:Splice.Api.FeaturedAppRightV1:FeaturedAppRight` for `Splice.Api.FeaturedAppRightV1`. The command `daml damlc inspect-dar` can be used to find this.
>
> 2\. Query the ledger using this ID to retrieve contracts from the Daml ledger that implement the FeaturedAppRight interface. The `curl` example below illustrates this approach.
>
> ````bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
> curl "http://$lapiParticipant/v2/state/active-contracts" \
> "$jwtToken" "application/json" \
>    --data-raw '{
>    "filter": {
>    "filtersByParty": {
>          "'$holderPartyId'": {
>          "cumulative":
>          [
>             {
>                "identifierFilter": {
>                "InterfaceFilter": {
>                   "value": {
>                      "interfaceId": "'7804375fe5e4c6d5afe067bd314c42fe0b7d005a1300019c73154dd939da4dda:Splice.Api.FeaturedAppRightV1:FeaturedAppRight'",
>                      "includeInterfaceView": true,
>                      "includeCreatedEventBlob": false
>                   }
>                }
>                }
>             }
>          ]}
>    }
>    },
>    "verbose": false,
>    "activeAtOffset":"'$latestOffset'"
> }'
> ```text
>
> 3\. The application's Daml code will have to depend on the `splice-api-featured-app-v1.dar` and take an argument of type `ContractId FeaturedAppRight` on the choice whose execution should be featured, which allows that choice's body to call the `FeaturedAppRight_CreateActivityMarker` in the next step.
>
> 3\. In the application's Daml code, using the `FeaturedAppRight` interface, exercise the `FeaturedAppRight_CreateActivityMarker` choice. Set the `templateId` to the fully qualified interface ID above.
>
> 4\. For testing examples, please review the example DamlScript test [here](https://github.com/canton-network/splice/blob/a32995a0df2d447b9e76d81b770a06c296295ab5/daml/splice-dso-governance-test/daml/Splice/Scripts/TestFeaturedAppActivityMarkers.daml#L4).
> ````

Consider a single, simple transaction of a RWA which creates a single `FeaturedAppActivityMarker` activity record for one `provider` and the `beneficiary` is the `provider`:

> 1\. A FeaturedAppActivityMarker contract is created in the business transaction. The `provider` is set to the featured application provider's party. The `beneficiary` must be set (unlike an AppRewardCoupon) to the party that should be eligible to mint the CC for that activity. The `provider` field of the FeaturedAppActivityMarker is set by calling the interface choice FeaturedAppRight\_CreateActivityMarker.
>
> 2. No `ValidatorRewardCoupon` is created.

It is possible to share the attribution of activity for the `FeaturedAppActivityMarker`. The `FeaturedAppRight_CreateActivityMarker` choice accepts a list of AppRewardBeneficiary contracts. Then a `FeaturedAppActivityMarker` is created for each `beneficiary` with the `weight` field set appropriately.

{/* COPIED_START source="splice:docs/src/background/tokenomics/cc_transfer_splice_wallet_tokenomics.rst" hash="d0136d43" */}

## A CC Transfer using the Splice Wallet UI

A manual CC transfer using the UI of the Splice wallet (the wallet UI built into every validator) is an example of an AmuletRules\_Transfer. There are three types of manual transfers possible with the Splice Wallet UI:

> * *Amulet legacy transfer* offer where the receiver has to accept the transfer offer and then automation on the sender’s side completes the transfer. The `sender` is assigned to the ValidatorRewardCoupon user field.
>
>   These transfers are never featured. Since [CIP-0078 CC Fee Removal](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) was implemented, no fees are charged and thus no activity records are created.
>
> * A two-step, *CN token standard based* Transfer offer first locks the desired CC amount; on acceptance, it is unlocked and the transfer is completed. This does not rely on automation and works well for external parties. Note that there the two steps show up in the wallet:
>
>   > 1. The first step locks the CC as part of creating the transfer offer.
>   > 2. When the `receiver` accepts the transfer, the CC is unlocked and the CC amount is transferred to the `receiver`.
>
>   Since [CIP-0078 CC Fee Removal](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) was implemented, these steps neither charge any fees nor do they generate any activity records.
>
> * *One-step transfer* to a `receiver` that has preapproved incoming CC transfers set up via a TransferPreapproval contract. The validator operator of the `receiver` is the `provider` party on the `TransferPreapproval`. The `TransferPreapproval` contract is only visible to: the `receiver`, the receiver's validator operator party, and SuperValidators.
>
>   The transfer is featured if the `provider` party is a featured application provider. The reason for this being a featured transfer, is that this `provider` party enabled the receipt of the CC for the external party by creating the `TransferPreapproval` and taking care of its regular renewal. The legacy or token standard based one-step transfers work the same.
>
>   As for the other two transfers, no fees are charged. If the transfer is featured, then an `AppRewardCoupon` is created for the `provider` with the amount set to `AmuletConfig.transferConfig.extraFeaturedAppRewardAmount / conversionRate` where the `USD / CC` `conversionRate` is read from the `OpenMiningRound` contract referenced in the transfer.

When comparing the `Amulet` legacy and token standard two-step transfers, a difference is that the token standard transfer has additional coupons for the CC locking fees.

{/* COPIED_START source="splice:docs/src/background/tokenomics/traffic_tokenomics.rst" hash="f063357a" */}

Traffic credits are used for all submissions to the Global Synchronizer. Traffic costs are charged for sending all data based on the size of the messages and its delivery cost. However only the sending validator node is charged. Please refer to `traffic` for more details.

A validator increases its traffic credit balance by burning CC at the current USD-to-Canton-Coin conversion rate (a USD/MB price). When needed, the operator of a validator (or a third-party service provider) burns CC in exchange for traffic credits. The CC burned creates a ValidatorRewardCoupon with the amount of CC burnt and where the `user` is the validator operator of the validator hosting the purchasing party. There is no application involved so no AppRewardCoupon is created.

To avoid running out of traffic credits, the ability to perform automatic traffic purchases is provided and recommended. Please see `helm_validator_topup` for Kubernetes or `compose_validator_topup` for Docker-compose. Alternatively, Daml application code can use AmuletRules\_BuyMemberTraffic to increase the traffic credit balance.

Note that traffic credits are used whenever a confirmation request for a Daml transaction is sent to the Global Synchronizer. The traffic is consumed even if the confirmation request fails due to contention on consuming contracts. For example, when submitting two `Transfer` operations that consume the same `Amulet` contracts.

{/* COPIED_START source="splice:docs/src/background/tokenomics/val_live_tokenomics.rst" hash="48ad8bfc" */}

In each round, each live validator records its liveness activity with a ValidatorLivenessActivityRecord. This rewards a validator for being available to validate and confirm transactions. It also provides them with initial funds to purchase extra traffic for higher throughput, after onboarding.

{/* COPIED_START source="splice:docs/src/background/tokenomics/sv_live_tokenomics.rst" hash="a7bf1890" */}

Each Super Validator, in each round, creates an SvRewardCoupon.

These SV minting rights are granted by the tokenomics committee in exchange for operating an SV node or contributing key infrastructure or activity to the network. The tokenomics committee uses the CIP process to record the SV rights. The current list of SV rights is thus available from the [CIP repo](https://github.com/global-synchronizer-foundation/cips).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
