---
title: "Tokenomics of the Global Synchronizer"
slug: "overview-reference-tokenomics-of-gs"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/tokenomics-of-gs.md"
source_title: "Tokenomics of the Global Synchronizer"
tags:
  - overview
  - reference
  - tokenomics-of-gs
---

# Tokenomics of the Global Synchronizer

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Tokenomics of the Global Synchronizer

> Economic model sustaining the Global Synchronizer: traffic fees, reward distribution, issuance, and the CC-USD conversion rate

Canton Coin (CC) is the economic engine of the Global Synchronizer. Validators, Super Validators, and application providers earn CC by contributing infrastructure and activity to the network. Users spend CC (by burning it) to purchase synchronizer traffic. The resulting burn-mint equilibrium ties the token's value to actual network utility.

## Burn-Mint Equilibrium

The Canton Coin application employs a burn-mint equilibrium mechanism, aiming to stabilize the conversion rate of Canton Coin around the intrinsic value it provides to network users:

* **Fee burning** -- Users pay fees (denominated in USD but paid by burning Canton Coin) when they purchase synchronizer traffic. The burned coins are permanently removed from circulation.
* **Minting rewards** -- Validators, Super Validators, and application providers mint new CC in return for their contributions to the network (infrastructure operation, application services, usage, and liveness).
* **Dynamic equilibrium** -- Over the long term, the total CC burned (reflecting actual network utility) roughly balances the CC minted (subject to a predetermined maximum minting curve). When usage is high, more coins are burned, which tends to increase the token's conversion rate; when usage is lower, supply increases until balance is restored.

## Traffic Economics

Every message submitted to the Global Synchronizer consumes traffic. The sending validator is charged; recipients are not.

### Base-Rate Allocation (Free Tier)

Each validator receives a free, regenerating traffic allowance defined by two parameters on the `AmuletRules` contract:

* `burstAmount` -- the maximum number of bytes a validator can use within one burst window without incurring fees.
* `burstWindow` -- the time window over which the burst amount regenerates. After a full window of inactivity, the free balance is fully restored.

Base-rate traffic is always consumed first. Only when it is exhausted does extra (paid) traffic get drawn down.

### Extra Traffic (Purchased by Burning CC)

A validator increases its traffic credit balance by burning CC at the current USD-to-CC conversion rate (a USD/MB price). When needed, the operator of a validator (or a third-party service provider) burns CC in exchange for traffic credits. The CC burned creates a `ValidatorRewardCoupon` recording the amount of CC burnt, where the `user` is the validator operator hosting the purchasing party. No `AppRewardCoupon` is created for traffic purchases.

Automatic top-up automation is available so validators do not run out of traffic unexpectedly. A `minTopupAmount` parameter ensures each purchase is large enough to amortize the processing cost for Super Validators.

Traffic accounting is per-validator -- all parties hosted on the same validator share one traffic balance. When a validator hosts external parties, it purchases traffic on their behalf. The Scan API provides traffic pricing parameters that validators can use to estimate costs for transactions submitted by external parties.

### Cost Factors

The actual traffic drawn from a validator's balance for a given message depends on:

* **Payload size** -- the byte size of the sequenced message.
* **Number of recipients** -- each recipient adds a delivery surcharge controlled by `readVsWriteScalingFactor` (specified in basis points). For example, at a factor of 4, a 1 MB message with 10 recipients costs `1,000,000 * (1 + 10 * 0.004) = 1,040,000` bytes.
* **Extra traffic price** -- the `extraTrafficPrice` in USD per MB, charged in CC at the prevailing conversion rate.

All of these parameters live on the `AmuletRules` contract and can be queried through the Scan API.

## Reward Distribution

Network activity is tracked through **activity records**, each carrying a weight that determines the party's share of CC minting for a given round. Five key contract templates drive the accounting:

* **`SvRewardCoupon`** -- one per Super Validator per round. SV minting rights are granted by the tokenomics committee through the [CIP process](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0000/cip-0000.md) in exchange for operating SV infrastructure or contributing key resources.
* **`ValidatorRewardCoupon`** -- created whenever CC is burned (traffic purchase) or an `AmuletRules_Transfer` executes. The coupon's weight reflects the amount of CC the validator burned.
* **`ValidatorLivenessActivityRecord`** -- one per live validator per round. Rewards a validator for being available to validate and confirm transactions and provides initial funds for purchasing extra traffic after onboarding.
* **`AppRewardCoupon`** -- created when a featured application's transaction succeeds or when a `FeaturedAppActivityMarker` is converted by SV automation. Only featured applications receive rewards (per [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md)).
* **`FeaturedAppActivityMarker`** -- created in the business transaction for economically meaningful events (asset transfers, token mints/burns). SV automation converts these into `AppRewardCoupon` contracts.

## Issuance Curve and Minting Schedule

The `IssuanceConfig` on the `AmuletRules` contract defines the maximum CC that can be minted. Its key fields are:

* `amuletToIssuePerYear` -- the annual ceiling on new CC issuance. Per-round issuance is derived by dividing this number by the number of rounds per year (rounds start every 10 minutes by default, so roughly 52,560 rounds per year).
* `validatorRewardPercentage` -- the fraction of per-round issuance allocated to validator activity rewards (burn-proportional coupons and liveness faucets).
* `appRewardPercentage` -- the fraction allocated to application rewards.
* The remainder after validator and app tranches goes to Super Validator rewards, distributed proportionally to each SV's weight.

Within each tranche, per-coupon issuance is capped (`validatorRewardCap`, `featuredAppRewardCap`, `unfeaturedAppRewardCap`, `validatorFaucetCap`). If total coupon demand in a tranche is below the cap, the surplus flows to the next tranche -- for example, unclaimed validator activity rewards flow to the validator liveness faucet, and unclaimed unfeatured app rewards flow to featured app rewards. Unclaimed rewards beyond all tranches go to SV rewards.

A `developmentFundPercentage` (default 5%) is set aside from each round's issuance for the development fund under [CIP-0082](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0082/cip-0082.md), before the remainder is split across the tranches above.

## Fee Schedules and Round Snapshots

Fee parameters are stored on the **`AmuletRules`** contract, which the DSO governs through on-ledger voting. When a new mining round opens, the current fee values and conversion rate are snapshotted into an **`OpenMiningRound`** contract so that all transactions within that round use consistent pricing. As the round progresses through its phases, an **`IssuingMiningRound`** contract records the computed amount-to-mint-per-activity-weight for each reward type.

[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) eliminated nearly all fees for CC transfers and locks. The holding fee remains -- a fixed fee per separate coin contract (UTXO) per unit of time, independent of coin amount. Holding fees incentivize merging small coins to reduce on-ledger storage. They are charged only on expired coin contracts via `Amulet_Expire`, not during transfers.

## CC-USD Conversion Rate

Each Super Validator publishes the CC conversion rate they consider appropriate. The rate used for each mining round is the **median** of all published SV rates. This median-based approach prevents any single SV from unilaterally shifting the price.

The resulting `amuletPrice` (USD per CC) is recorded on each `OpenMiningRound` contract and can be queried through the Scan API or Scan UI. All USD-denominated fees (traffic costs, reward caps) are converted to CC at this rate when applied.

## How Validators Earn

Validators earn CC through two mechanisms that run every round:

* **Liveness rewards** -- each live validator creates a `ValidatorLivenessActivityRecord`, earning a share of the validator faucet tranche. The per-validator faucet cap defaults to \$2.85 USD equivalent per round. Liveness rewards give new validators initial CC to fund traffic purchases.
* **Activity rewards** -- when a validator's users burn CC (traffic purchases or transfers), the resulting `ValidatorRewardCoupon` entitles the validator to mint CC proportional to the amount burned. Validators that drive more network usage earn more.

For validators hosting external parties (parties that sign with their own keys rather than through the validator), minting can be handled either through a **minting delegation** to the validator or through custom automation calling `AmuletRules_Transfer` each round. [CIP-0073](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md) describes weighted validator liveness rewards for SV-determined parties.

## Further Reading

* [Canton Coin white paper](https://www.digitalasset.com/hubfs/Canton%20Network%20Files/Documents%20\(whitepapers%2c%20etc...\)/Canton%20Coin_%20A%20Canton-Network-native%20payment%20application.pdf) -- full technical specification of the burn-mint mechanism
* [Canton Network white paper](https://www.digitalasset.com/hubfs/Canton/Canton%20Network%20-%20White%20Paper.pdf) -- broader network architecture and design
* [CIP repository](https://github.com/global-synchronizer-foundation/cips) -- governance proposals including fee and reward changes

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
