---
title: "App Rewards"
slug: "appdev-app-rewards"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/app-rewards.md"
source_title: "App Rewards"
tags:
  - appdev
  - app-rewards
---

# App Rewards

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# App Rewards

> How applications earn Canton Coin rewards on the Canton Network through featured app activity and reward coupons

The Canton Network incentivizes application providers through a reward system tied to network activity. Applications that generate value on the network can earn Canton Coin (CC) as rewards. This page explains the reward types, how to earn them, and the process for getting your application featured.

## Reward Types

{/* COPIED_END */}

These coupons are collected over each reward round and converted into CC during the minting process.

## How Apps Earn Rewards

The primary mechanism for application rewards is the **FeaturedAppActivityMarker**. When your application creates activity on the network, your backend (or automation) writes a `FeaturedAppActivityMarker` contract that records the activity. SV automation detects these markers and converts them into `AppRewardCoupon` contracts, which are then included in the next minting round.

The flow:

1. Your application creates transactions on the Global Synchronizer (e.g., users exercise choices, create contracts)
2. Your app's automation creates a `FeaturedAppActivityMarker` referencing that activity
3. SV automation validates the marker and creates an `AppRewardCoupon`
4. At the end of the reward round, the coupon is included in the CC minting calculation
5. Your application provider party receives CC proportional to the activity

`FeaturedAppActivityMarker` is the preferred method because it ties rewards directly to demonstrable network usage rather than requiring manual reporting or opaque metrics.

## Getting Featured

After [CIP-0078](https://github.com/canton-foundation/cips/blob/main/cip-0078/cip-0078.md), only **featured applications** are eligible for app rewards. An unfeatured application's activity markers will not be converted into reward coupons.

To get your application featured:

1. Deploy your application on the Canton Network (DevNet, TestNet, or MainNet)
2. Submit a request to the Global Synchronizer Foundation through the [application process](https://sync.global/)
3. The tokenomics committee reviews the submission, evaluating the application's contribution to the network
4. Upon approval, an SV governance vote registers your application as featured

Once featured, your `FeaturedAppActivityMarker` contracts are eligible for conversion into `AppRewardCoupon` contracts.

## Self-Featuring on DevNet

On DevNet, you can register your application as self-featured for testing purposes. This lets you verify that your reward-earning logic works correctly before going through the formal featuring process on TestNet or MainNet.

Self-featuring on DevNet does not require GSF approval. It is intended purely for development and integration testing of the reward flow.

## Minting Delegation

If your application generates activity on behalf of external parties (e.g., end users interacting through your platform), you can delegate minting rights. Minting delegation allows a validator to mint rewards on behalf of another party, which is useful when your application's transaction-submitting validator differs from the party that should receive the reward.

## Fee Structure

Canton Network does not charge fees on CC transfers between parties. The only cost associated with network usage is traffic -- the transaction fee paid by the submitting validator. Application rewards are a separate mechanism that compensates app providers for generating network activity, independent of traffic costs.

## Further Reading

* [Canton Coin and Traffic](/docs/canton/appdev-modules-m4-canton-coin) -- How traffic credits and CC work for application developers
* [Getting Your App Featured](/docs/canton/overview-understand-getting-app-featured) -- Promotional opportunities on Canton Network
* [Canton Coin overview](/docs/canton/overview-understand-canton-coin) -- Tokenomics, validator rewards, and governance

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
