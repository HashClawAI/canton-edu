---
title: "Featured App Activity Markers"
slug: "appdev-modules-m4-featured-app-activity-marker"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-featured-app-activity-marker.md"
source_title: "Featured App Activity Markers"
tags:
  - appdev
  - modules
  - m4-featured-app-activity-marker
---

# Featured App Activity Markers

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Featured App Activity Markers

> How to create FeaturedAppActivityMarker contracts to record app activity and earn rewards

When your application runs on Canton Network, economically meaningful events can be recorded as **app activity**. The preferred mechanism for this is the `FeaturedAppActivityMarker` contract. SV (Super Validator) automation converts these markers into `AppRewardCoupon` contracts, which translate to Canton Coin (CC) rewards for your application.

## What is a FeaturedAppActivityMarker?

{/* COPIED_END */}

A `FeaturedAppActivityMarker` records a specific activity event in your application. It signals to the network that something economically relevant happened -- for example, a real-world asset was locked, a token was minted, or a license was renewed.

After [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md), only **featured** apps receive rewards. Unfeatured apps can still create markers, but they will not generate reward coupons.

## When to Create Markers

{/* COPIED_END */}

Beyond the basics above, other examples of appropriate markers include settling a payment or trade, and renewing or issuing a license. Do not create markers for routine housekeeping operations (cache refreshes, health checks, internal bookkeeping) that do not represent user-facing economic value.

## How to Create Markers

The `FeaturedAppActivityMarker` contract is specified in [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md). Your Daml code creates the marker as part of the transaction that performs the economically meaningful action.

{/* COPIED_END */}

The marker contract includes fields that identify your application, the type of activity, and metadata about the event. Refer to [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) for the exact contract interface and required fields.

The *featured application activity marker* is specified in [CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md). A summary follows.

Featured application activity markers (FeaturedAppActivityMarker) can be created for a transaction that adds value but does not involve a CC Transfer (e.g., a stable coin transfer or the settlement of a trade). [CIP 47](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) says:

> Featured application providers are expected to create featured application activity markers only for transactions that correspond to a transfer of an asset, or an equivalent transaction, which was enabled by the application provider. The detailed fair usage policy and enforcement thereof is left up to the Tokenomics Committee of the Global Synchronizer Foundation (GSF).

Generally the guidance is to create a `FeaturedAppActivityMarker` for any economically important event, such as:

* Lock or unlock a Real World Asset (RWA).
* Transfer a RWA.
* Mint or burn tokens.

However, it should not be created for any intermediate steps or a propose step.

A `FeaturedAppActivityMarker` is immediately converted into an AppRewardCoupon by the automation run by the Super Validators. The AppRewardCoupon is created with the DSO as the `signatory` and the `provider` field as an observer. By default, the `provider` can mint CC in the minting step. The `featured` field is set to `true` to indicate eligibility to receive featured application rewards, based on a FeaturedAppRight contract.

There can be several `FeaturedAppActivityMarkers` per transaction tree which increases the total reward. However, this is only allowed for composed transactions (e.g. a settlement transaction) where trading venue and all the registries of the transferred assets would get featured app rewards. It is also possible for a single Canton transaction tree to include ValidatorRewardCoupon, an AppRewardCoupon and a FeaturedAppActivityMarker(s) if there are sub-transcations that create each separately.

A non-featured app cannot accrue a `FeaturedAppActivityMarker`.

### Creating a Featured Application Activity Marker

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

### Markers in cn-quickstart

In [cn-quickstart](https://github.com/digital-asset/cn-quickstart), the license renewal flow creates a `FeaturedAppActivityMarker` when a license is renewed. The marker is created inside the Daml choice that performs the renewal, so it is part of the same transaction and recorded atomically.

## Getting Your App Featured

To receive rewards from your markers, your application must be **featured** on the network.

### On DevNet

You can self-feature your application on DevNet for testing purposes. This lets you verify that your markers are created correctly and that the SV automation converts them into reward coupons, without going through the formal review process.

### On TestNet and MainNet

For TestNet and MainNet, the process is:

1. **Submit your application** via the GSF (Global Synchronizer Foundation) form. You provide details about your application, the types of activities you record, and why they represent genuine economic value.
2. **Tokenomics committee review** -- The GSF tokenomics committee evaluates your submission. They assess whether the recorded activities reflect real economic value and whether the marker creation is appropriate.
3. **Approval and featuring** -- If approved, your application is added to the featured apps list. From that point, your markers generate reward coupons.

## Reward Mechanics

The reward calculation depends on the number and type of activity markers your application creates, relative to other featured apps on the network. The exact formula is governed by the tokenomics rules defined by the GSF.

Key points:

* Rewards are paid in CC to the app provider party
* More activity markers (representing genuine economic events) generally means more rewards
* The reward pool is shared across all featured apps, so your share depends on your relative activity
* Gaming the system (creating markers for non-economic events) risks losing featured status

## Testing Markers Locally

On LocalNet (via cn-quickstart), the SV automation that converts markers to coupons is part of the local Splice infrastructure. You can:

1. Trigger an action in your application that creates a marker
2. Query PQS for active `FeaturedAppActivityMarker` contracts to verify they were created
3. Wait for the SV automation cycle, then query for `AppRewardCoupon` contracts to confirm conversion

This local testing loop lets you validate your marker creation logic before deploying to DevNet.

## Further Reading

* [Canton Coin and Traffic](/docs/canton/appdev-modules-m4-canton-coin) -- How CC rewards relate to traffic and transaction costs
* [CIP-0047](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0047/cip-0047.md) -- The specification for FeaturedAppActivityMarker
* [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) -- The change restricting rewards to featured apps
* [Deployment Progression](/docs/canton/appdev-modules-m5-deployment-progression) -- Moving from LocalNet to DevNet to MainNet

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
