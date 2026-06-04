---
title: "Wallets for Users"
slug: "integrations-wallets-for-users"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallets/for-users.md"
source_title: "Wallets for Users"
tags:
  - integrations
  - wallets
  - for-users
---

# Wallets for Users

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallets for Users

> Finding and using Canton Network wallets

A wallet is your gateway to Canton Network—it lets you manage Canton Coin, interact with applications, and track your activity.

## What is a Canton Wallet?

A Canton wallet allows you to:

| Function               | Description                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hold Canton Coin**   | Store and manage your CC balance                                                                                                                      |
| **Hold other tokens**  | Hold any [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) compliant token (support varies by wallet) |
| **Transfer value**     | Send CC to other parties                                                                                                                              |
| **Interact with apps** | Connect to Canton Network applications                                                                                                                |
| **View activity**      | See your transaction history                                                                                                                          |

## Finding a Wallet

### Splice Wallet (Reference Implementation)

The Splice project provides a reference wallet implementation:

* **Type**: Web-based wallet
* **Access**: Through validator or application interfaces
* **Features**: Core wallet functionality

<Note>
  The Splice reference wallet is not yet [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) compliant. Support for the token standard is planned for a future release.
</Note>

### Validator-Provided Wallets

Some validators offer wallet interfaces as part of their services. Check with your validator or application provider.

### Application-Integrated Wallets

Many Canton applications include wallet functionality:

* Built into the application interface
* Seamless experience within the app
* May have application-specific features

## Wallet Basics

### Your Balance

Your wallet shows your Canton Coin balance. Wallets may also display other tokens that follow the [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) token standard—check your specific wallet for supported assets. Unlike other cryptocurrencies:

* Only you can see your balance
* Others cannot query your holdings
* Your transactions are private

### Transfers

To send CC to another party:

1. Enter the recipient's party identifier
2. Specify the amount
3. Confirm the transfer
4. Transaction completes (typically within seconds)

### Transaction History

View your past transactions:

* Transfers sent and received
* Traffic fees paid
* Application interactions

<Note>
  You can only see transactions where you were a participant. There's no public ledger of all transactions.
</Note>

## Security

### Protecting Your Wallet

| Practice               | Description                                  |
| ---------------------- | -------------------------------------------- |
| **Secure access**      | Use strong authentication                    |
| **Verify parties**     | Confirm recipient identifiers before sending |
| **Trusted validators** | Use wallets from reputable sources           |

### Understanding the Trust Model

Your wallet connects to a validator that:

* Hosts your party
* Stores your contract data
* Processes your transactions

Choose your validator carefully—they have visibility into your operations.

## Differences from Other Crypto Wallets

| Aspect                  | Traditional Crypto     | Canton                       |
| ----------------------- | ---------------------- | ---------------------------- |
| **Balance visibility**  | Public                 | Private                      |
| **Transaction history** | Public                 | Private                      |
| **Address format**      | Hex address            | Party identifier             |
| **Network explorer**    | Shows all transactions | Shows only your transactions |

## Getting Started

### On DevNet/TestNet

1. Access a wallet interface (through your validator or application)
2. Create or import your party
3. Use the faucet ("tap") to receive test CC
4. Start transacting

### On MainNet

1. Connect to a wallet through your validator or application
2. Obtain CC through:
   * Exchange purchase
   * Transfer from another party
   * Network activity rewards

## Common Tasks

### Checking Your Balance

Open your wallet interface to see your current CC balance.

### Sending CC

1. Navigate to "Send" or "Transfer"
2. Enter the recipient party
3. Enter the amount
4. Review and confirm

### Receiving CC

1. Share your party identifier with the sender
2. CC appears in your balance after confirmation

### Topping Up Traffic

If you're running an application that needs traffic:

1. Navigate to traffic management
2. Initiate a top-up
3. CC is converted to traffic credits

## Troubleshooting

| Issue             | Solution                                                |
| ----------------- | ------------------------------------------------------- |
| Balance shows 0   | Ensure wallet is connected to correct validator         |
| Transfer failed   | Check recipient party format; ensure sufficient balance |
| Slow confirmation | Network may be busy; wait a few moments                 |
| Can't connect     | Check network connectivity; verify validator status     |

## Next Steps

<CardGroup cols={2}>
  <Card title="How Canton Wallets Differ" icon="code-compare" href="/integrations/wallets/canton-vs-web3">
    Understand the technical differences.
  </Card>

  <Card title="Find Apps" icon="grid-2" href="/integrations/apps/finding-apps">
    Discover Canton Network applications.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
