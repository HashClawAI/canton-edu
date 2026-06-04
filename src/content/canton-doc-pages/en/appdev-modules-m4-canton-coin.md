---
title: "Canton Coin and Traffic"
slug: "appdev-modules-m4-canton-coin"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-canton-coin.md"
source_title: "Canton Coin and Traffic"
tags:
  - appdev
  - modules
  - m4-canton-coin
---

# Canton Coin and Traffic

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Coin and Traffic

> How Canton Coin buys traffic credits and what application developers need to know about transaction costs

Every transaction on the Global Synchronizer costs traffic. Canton Coin (CC) is the native currency you use to purchase traffic credits. As an application developer, you need to understand this relationship so your users' transactions go through without interruption.

## Canton Coin

Canton Coin is the native utility token of the Global Synchronizer. It is implemented through [Splice](https://github.com/canton-network/splice), the open-source infrastructure layer for decentralized Canton synchronizers.

CC has several primary purposes on the network:

* **Buying traffic** -- Convert CC into traffic credits so your validator can submit transactions
* **Validator rewards** -- Validators earn CC for operating infrastructure and processing transactions
* **Application rewards** -- Application providers earn CC based on the use of their application (adding value) to the Canton Network
* **Governance** -- Super Validators stake CC to participate in synchronizer governance

Unlike most blockchain tokens, CC balances are private. Only you and explicitly entitled parties can see your holdings. There is no public ledger of balances or transfers.

## Traffic: How Transaction Fees Work

Traffic is Canton's term for transaction fees. You do not pay CC directly when submitting a transaction. Instead, your validator maintains a **traffic budget** measured in traffic credits. Each transaction deducts credits from this budget based on the transaction's size and complexity.

The two-step process:

1. **Top up** -- Convert CC into traffic credits, adding them to your validator's traffic budget
2. **Consume** -- When your validator submits a transaction, traffic credits are deducted from the budget

Traffic credits are non-transferable. Once CC is converted to traffic, those credits can only be consumed by transaction fees on that validator.

### What Affects Traffic Cost

Traffic cost for a given transaction depends on:

* **Transaction size** -- Larger payloads (more contract data, more parties) cost more credits
* **Network conditions** -- Costs may vary with network load

## The Auto-Top-Up Feature

Validators can enable **auto-top-up** to automatically purchase traffic credits when the budget drops below a configured threshold. When auto-top-up is active, the validator converts CC to traffic credits without manual intervention.

This is the recommended approach for App Providers. Without auto-top-up, you would need to monitor your traffic budget and manually trigger top-ups before it runs out. If the budget is exhausted, your validator's transactions will fail until more credits are added.

<Note>
  Auto-top-up requires that the validator's wallet holds sufficient CC. If the wallet balance is too low to purchase traffic, auto-top-up cannot proceed and transactions will start failing.
</Note>

## Managing Traffic as an App Provider

As an App Provider, your validator submits transactions on behalf of your application's parties. You are responsible for ensuring your validator has enough traffic credits to handle the transaction volume your application generates.

Practical considerations:

* **Estimate traffic usage** -- Understand how many transactions your application generates per day and how large they are. Use DevNet or TestNet to measure actual traffic consumption.  When a transaction is prepared for an external party, an estimate of the traffic used for that transaction can be provided.
* **Enable auto-top-up** -- Configure your validator to automatically replenish traffic credits. Set the threshold high enough to absorb traffic spikes.
* **Monitor your wallet balance** -- Auto-top-up draws from your wallet's CC balance. Keep it funded.
* **Handle insufficient-traffic errors** -- If a transaction fails because of insufficient traffic, your backend should surface a clear error rather than silently retrying. The fix is to top up the traffic budget, not to retry the command.

## Obtaining Canton Coin

How you get CC depends on the environment:

* **LocalNet** -- Test CC is available automatically. No action needed.
* **DevNet** -- Use the faucet (tap) to receive free test CC. Rate-limited, no real value.
* **TestNet** -- Same faucet mechanism as DevNet. Test CC only.
* **MainNet** -- Purchase CC from supported exchanges, earn it through validator operations, or receive it via direct transfer from another party.

## Wallet Integration for Applications

If your application involves CC payments between parties (e.g., a user paying for a license), you integrate with the Splice wallet system. In cn-quickstart, the license renewal flow demonstrates this:

1. The [`License_Renew`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml) choice creates a `LicenseRenewalRequest` contract that implements the Splice `AllocationRequest` interface
2. The Splice wallet detects the allocation request, creates an `AppPaymentRequest`, and transfers CC from the user to the provider
3. Once payment settles, the provider exercises [`LicenseRenewalRequest_CompleteRenewal`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml) to create the renewed license

See [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java) for the backend implementation of this flow.

The wallet handles CC transfers, balance lookups, and payment confirmations. Your Daml model defines payment request contracts that the wallet system understands.

## Traffic vs. CC: A Summary

* **Canton Coin (CC)** is the currency. You hold it in a wallet, transfer it between parties, and use it to buy traffic.
* **Traffic credits** are what your validator spends when submitting transactions. They live in the validator's traffic budget, not in a wallet.
* You convert CC to traffic credits via top-up (manually or automatically). The reverse is not possible -- traffic credits cannot be converted back to CC.

## Further Reading

* [Canton Coin overview](/overview/understand/canton-coin) -- Deeper background on CC tokenomics, validator rewards, and governance
* [Backend Development](/appdev/modules/m4-backend-dev) -- Handling transaction errors, including insufficient-traffic failures
* [cn-quickstart](https://github.com/digital-asset/cn-quickstart) -- Working example of wallet integration in a Canton application

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
