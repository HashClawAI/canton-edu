---
title: "Splice Wallet Reference"
slug: "overview-reference-splice-wallet-reference"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/splice-wallet-reference.md"
source_title: "Splice Wallet Reference"
tags:
  - overview
  - reference
  - splice-wallet-reference
---

# Splice Wallet Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Splice Wallet Reference

> Reference documentation for the built-in Splice wallet, covering Canton Coin operations, automation, transfer workflows, APIs, and UTXO management

The Splice Wallet is the built-in wallet component of every validator node on the Canton Network. It provides Canton Coin (CC) management for parties hosted on that validator, including a web UI, background automation, and programmatic APIs.

## Wallet UI

The wallet UI ships with every validator node and gives users a browser-based interface for CC operations. After logging in and onboarding (which allocates a fresh party), users can:

* View their CC balance and individual Holding contracts (UTXOs)
* Send CC to other parties via transfer offers or one-step preapproved transfers
* Accept, reject, or withdraw incoming transfer offers
* Review transaction history
* Buy traffic for any validator on the network
* Manage minting delegations (accept, reject, or withdraw proposals from external parties)

The validator operator's party is automatically created during validator initialization and associated with the configured `validatorWalletUser`. Other users onboard through the UI or via the `/v0/admin/users` API endpoint.

## Wallet Automation

The validator app runs several background automations on behalf of wallet users. These handle recurring CC operations without manual intervention.

**Reward collection.** The wallet automation periodically collects and mints reward coupons (validator rewards, app rewards, liveness activity records) for each onboarded party. This converts earned coupons into CC holdings.

**Traffic top-ups.** When configured, the validator automatically purchases traffic credits using CC from the operator's wallet whenever the extra traffic balance drops below a threshold. Operators set a `targetThroughput` and `minTopupInterval`, and the automation buys enough traffic to sustain that throughput. On DevNet, the validator taps enough coin automatically if the wallet lacks funds.

**Sweeps.** Operators can configure automatic sweeping, where CC is transferred from one party to another when the sender's balance exceeds a `maxBalanceUSD` threshold. The automation creates transfer offers that move funds down to a configured `minBalanceUSD`. Sweep configuration maps sender party IDs to receiver party IDs and balance thresholds. Sweeps can use transfer preapprovals for one-step delivery.

**Auto-accept.** Operators can configure automatic acceptance of incoming transfer offers from specific sender parties. This is configured per sender-receiver party ID pair in the validator's Helm chart or Docker Compose configuration.

Contrary to other assets like Eth or Bitcoin, Canton Coin requires a party to explicitly agree to hold Canton Coin. This includes explicitly agreeing to any incoming transfers.

Parties that are ok with accepting incoming Canton Coin transfers from any sender, can setup a `TransferPreapproval`. This allows any party to send Canton Coin to the party that setup the `TransferPreapproval`. Note that this only applies to transfers of Canton Coin but not to other assets. Other assets may provide their own variant of a preapproval which needs to be setup separately or they may require approval of each incoming transfer individually.

To ensure that the super validators don't have to store and serve `TransferPreapprovals` contracts for parties that are no longer active or malicious parties cannot spam them, a preapproval has a limited lifetime until it expires and a fee must be burned proportional to the lifetime when creating the preapproval. The fee is controlled by the super validators through the `transferPreapprovalFee` parameter. The current value can be observed in CC Scan at [https://scan.sv-1.unknown\_cluster.global.canton.network.sync.global/dso](https://scan.sv-1.unknown_cluster.global.canton.network.sync.global/dso) and defaults to \$1/year.

Each preapproval has two parties: The `receiver` party that approves incoming transfers and the `provider` party. The provider party is responsible for paying the fee and renewing the preapproval when it gets close to its expiry date. In return, the `provider` party will be the app provider on all incoming transfers that use this preapproval and get the app rewards for it. The `provider` party must not necessarily be hosted on the same node as the `receiver` party although that is the most common setup in practice.

## Setting up Preapprovals

For parties not using external signing, the preapproval can be created by the user in the in their splice wallet UI through the button next to the logout button:

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/preapproval_button.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=feabdf575485595c7c0aa26911e133dd" width="600" alt="Button to create preapproval" data-path="images/splice/preapproval_button.png" />

For parties using external signing, the most common way of doing so is for the validator operator to create a `ExternalPartySetupProposal` contract. The external party then signs a transaction that exercises `ExternalPartySetupProposal_Accept`. This creates both the `ValidatorRight` contract required for validator reward minting for the external party and the `TransferPreapproval` contract with the provider set to the validator operator party. The validator exposes the endpoints `/v0/admin/external-party/setup-proposal` to create the proposal and then `/v0/admin/external-party/setup-proposal/prepare-accept` and `/v0/admin/external-party/setup-proposal/submit-accept` to prepare and submit the signed acceptance from the external party. Refer to the API docs for details. If you want a different setup in terms of who should be the provider, you may need to build your own setup Daml contracts and create them through the ledger API instead of using the validator APIs.

Note the limit on the number of parties when setting up preapprovals with the provider set as the validator operator.

The validator APIs always create a preapproval with an expiry date of 90 days in the future.

## Expiry and Renewal of Preapprovals

As explained above, preapprovals always have an expiry date. If that date is reached and the preapproval has not been renewed, it can no longer be used for transfers and automation run by the super validators will eventually archive the contract.

Preapprovals that have the validator operator party as a provider, will automatically be renewed for another 90 days through automation in the validator app when expiry is less than 30 days away.

If you have set up a preapproval with a different party as the provider, you need to setup your own renewal automation that periodically exercises the `TransferPreapproval_Renew` choice.

## Cancellation of Preapprovals

Preapprovals can be revoked by both the receiver and the provider through the `TransferPreapproval_Cancel` choice.

There is currently no support for this in the splice wallet UI but for preapprovals with the validator operator as the provider, a `DELETE` request to `/v0/admin/transfer-preapprovals/by-party/{receiver-party}` can be used by the validator operator. Refer to the API docs for details.

## Transferring through a Preapproval

The splice wallet UI will automatically default to using a preapproval for a transfer if the receiver has one setup.

If you are working through APIs instead, in particular for external parties, the preferred way of exercising a Canton Coin transfer is through the Token Standard APIs which will also use a preapproval where possible. Refer to the [CIP](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) and the [token standard reference CLI](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/transfer.ts) for examples of how to use it.

Lastly, the legacy external signing APIs for non-standard Canton Coin transfers on the validator `/v0/admin/external-party/transfer-preapproval/prepare-send` and `/v0/admin/external-party/transfer-preapproval/submit-send` can also be used. Refer to the API docs for details.

## Transfer Workflows

CC transfers between parties follow one of three patterns.

**Two-step token standard transfer.** The sender locks CC into a `TransferInstruction` contract. The receiver then accepts (unlocking and completing the transfer), rejects, or lets it expire. The sender can also withdraw the offer before acceptance, reclaiming the locked funds. Since [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md), no fees are charged on these transfers.

**One-step preapproved transfer.** If the receiver has set up a `TransferPreapproval` contract, the sender can transfer CC in a single step without the receiver needing to accept. The receiver's validator operator acts as the `provider` party on the preapproval and handles its periodic renewal. If the provider is a featured application provider, the transfer generates an `AppRewardCoupon`.

## Wallet API Endpoints

The validator app exposes wallet APIs under the `/v0/wallet/*` path. These fall into two categories.

**External API** (`wallet-external.yaml`) -- intended for programmatic wallet interaction with backwards compatibility guarantees. Requires a JWT where the subject claim identifies the wallet user. Endpoints include:

* `POST /v0/wallet/transfer-offers` -- create a transfer offer
* `POST /v0/wallet/transfer-offers/{tracking_id}/status` -- check transfer offer status
* `GET /v0/wallet/transfer-offers` -- list transfer offers
* `POST /v0/wallet/buy-traffic-requests` -- request a traffic purchase
* `POST /v0/wallet/buy-traffic-requests/{tracking_id}/status` -- check traffic purchase status

**Internal API** (`wallet-internal.yaml`) -- used by the wallet UI frontend. No backwards compatibility guarantees. Endpoints include:

* `GET /v0/wallet/balance` -- query wallet balance
* `GET /v0/wallet/amulets` -- list UTXOs
* `POST /v0/wallet/transactions` -- transaction history
* `POST /v0/wallet/transfer-offers/accept` -- accept a transfer offer
* `POST /v0/wallet/transfer-offers/reject` -- reject a transfer offer
* `POST /v0/wallet/transfer-offers/withdraw` -- withdraw a transfer offer
* `GET /v0/wallet/user-status` -- user onboarding and wallet status

For the full OpenAPI specifications, see the [wallet-external.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/wallet/src/main/openapi/wallet-external.yaml) and [wallet-internal.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/wallet/src/main/openapi/wallet-internal.yaml) files.

## UTXO Management

Canton Coin uses a UTXO model inherited from the underlying Amulet contract structure in Splice. Each active `Holding` contract on the ledger represents a single UTXO with a specific CC amount. Unlike account-balance models, a party's total balance is the sum of all their individual Holding UTXOs. UTXO management matters for wallet providers because active Holding contracts consume storage and compute on the hosting validators, and each UTXO input to a transfer incurs extra traffic cost.

Canton Coin enforces a limit of 100 input contracts per transfer and expires dust UTXOs whose initial amount is smaller than the accrued holding fee. Wallet providers should aim for roughly 10 or fewer UTXOs per user on average.

**MergeDelegation contracts** allow a wallet provider to merge small Holding UTXOs on behalf of users. The workflow:

1. The user signs the creation of a `MergeDelegationProposal` during onboarding.
2. The wallet provider accepts the proposal, creating an active `MergeDelegation`.
3. A background process identifies users with more than 10 UTXOs, constructs merge operations via the registry API, and executes them in batches of \~100 using the `BatchMergeUtility_MergeHoldings` choice.

MergeDelegation contracts also allow wallet providers to combine airdrop campaigns with the auto-merging of holdings in a single batched call. Featured wallet providers earn featured app rewards for performing merges.

## External Party Wallet Support

The validator provides APIs for managing CC for external parties -- parties whose transaction signing keys are held outside the participant node. The external signing workflow uses Canton's interactive submission feature, where transactions are prepared on the participant, signed externally, and then submitted back.

The high-level flow for an external party:

1. Set up the external party's topology using `/v0/admin/external-party/topology/*`
2. Create a `TransferPreapproval` via `/v0/admin/external-party/setup-proposal` to enable sending and receiving CC
3. Send CC using `/v0/admin/external-party/transfer-preapproval/*`
4. Query balances with `GET /v0/admin/external-party/balance`

For each transfer, the caller must prepare the transaction (obtaining a hash), sign the hash with the external party's private key, and submit the signed transaction back to the participant. See the [validator-internal.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/validator/src/main/openapi/validator-internal.yaml) OpenAPI spec for the full endpoint list.

For building custom wallet integrations using the TypeScript Wallet SDK, see the [Wallet SDK documentation](/integrations/wallet/sdk-download).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
