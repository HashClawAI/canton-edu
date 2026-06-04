---
title: "Wallet Integration Guide"
slug: "integrations-wallet-guidance"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet/guidance.md"
source_title: "Wallet Integration Guide"
tags:
  - integrations
  - wallet
  - guidance
---

# Wallet Integration Guide

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallet Integration Guide

> Integrate with the Canton Network as a wallet: onboard external parties, read data, sign transactions, and support Canton Coin and USDCx.

# Canton Network Overview

## High-level Overview

Canton Network is a public layer 1 blockchain network with privacy. It is designed for financial institutions and DeFi alike to facilitate secure, interoperable, and privacy-preserving transactions and drive the confluence of TradFi and DeFi.

Key Features:

* It uniquely balances the decentralization of public blockchains with the privacy and controls required for financial markets.
* It enables real-time, secure synchronization and settlement across multiple asset classes on a shared, interoperable infrastructure.
* It allows assets and data to move across applications with real-time synchronization and guaranteed privacy.

**Technology:** The Canton Network is designed as a "network of networks," where each participating institution maintains its own sub-ledger while connecting with others via a shared synchronization layer. **Governance:** The Global Synchronizer Foundation (GSF), an independent, non-profit body under the Linux Foundation, governs the global synchronizer. **Participants:** Canton Network was launched in May 2023 by a group of major institutions, and continues to be backed by the world's largest financial and crypto institutions alike. Participants include Goldman Sachs, HSBC and BNP Paribas, market infrastructure providers like DTCC and Deutsche Börse, and (crypto) trading firms like DRW and QCP.

## Canton's High-level architecture

### Nodes and Consensus

The Canton network is composed of nodes known as **validators** that achieve consensus through **synchronizers**. Validator nodes are responsible for storing contract data and executing smart contract code. The synchronizers, in turn, distribute encrypted messages and facilitate transaction coordination. Transaction data is only distributed on a **need-to-know basis** to maintain confidentiality. This is the key delta to other chains:

* In most other chains, all state and transactions get replicated to all nodes/validators.
* In Canton, state and transactions get distributed only to nodes/validators that are specified in the smart contracts.

### Parties

In Canton, **parties** are the core on-ledger identities, and are the wallet addresses, similar to an address or Externally Owned Account (EOA) on other blockchains. They are central to how **permissions** and **privacy** are managed within the network.

**Party Permissions and Roles**

Smart contracts specify permissions for different parties, dictating what they can and can't do. Depending on their role, parties:

* **Validate** specific transactions, such as a transfer of assets.
* **Control** certain actions, like initiating transfers.
* **See** specific state and transactions, such as a record of their holdings.

Privacy is maintained at the party level, meaning transaction and state data is only shared with the parties who need to see it, ensuring a high degree of confidentiality.

**Local parties vs External parties**

Parties come in two forms, internal and external. An internal party is created on the validator node, it gives a validator node submission rights and therefore holds its key on the validator node. Transactions are signed using the Validators own internal keys for signing (and thereby the validator operator has full control of everything that happens on the party).

External parties are similar to how node interactions happens on other networks and therefore Externally Owned Accounts. In this case the signing key can be held externally and a signature is required alongside the transaction to authorize the action. For external parties the base flow follows three steps: Prepare a transaction, sign the transaction and submit the transaction. In this guide, when a party is referenced, it is referring to an external party unless otherwise specified.

To read more about the differences between internal and external parties, see the [Local and external parties documentation section here](/overview/reference/external-party).

**Onboarding and Format**

Parties are formatted as `name::fingerprint`. The party name or hint is freely chosen at time of creation - there's a maximum limit of 185 characters from \[a-zA-Z0-9:-\_ ], it must not use two consecutive colons, and must be unique in the namespace. The **fingerprint** is a unique identifier and a sha256 hash of the public key prefixed with '12' (as indicated by the [hash purpose](https://github.com/digital-asset/canton/blob/8ee65155e7f866e1f420703c376c867336b75088/community/base/src/main/scala/com/digitalasset/canton/crypto/HashPurpose.scala#L63)).

If you want to be able to derive your Party IDs from the public key, you can either use a static Party Name, and therefore derive the key from the fingerprint, or derive Party Name from the public key, too.

To use a party, you must **onboard** it by submitting a topology transaction that authorizes a node to host it. The designated node must then submit a matching transaction to officially accept the hosting request. Instructions on how to do that can be found here.

**Party Hosting**

Since not every user wants to host a node, parties are associated with validator nodes. These validators "host" parties by: \* Storing the party's private data and making it available through an RPC (Remote Procedure Call) interface. \* Participating in consensus on the party's behalf.

Crucially, even though a validator hosts a party, the party retains ultimate control by holding its own independent **signing keys** externally to the participant.

To participate in the network, a party must designate one or more validator nodes to host their data. This relationship, known as **Party Hosting**, is established through a **topology transaction**.

**Advice on using Parties for wallet providers**

Unlike Ethereum or Bitcoin addresses, creating parties has a cost associated to them and they create state on the validator node which means that they're not as ephemeral as on other chains. Therefore, it's suggested to avoid using parties for use cases such as “deposit addresses”.

* For wallets, it's suggested to aim for one Party per key pair to represent the wallet.
* For custodians, it's suggested aiming for one Party per account/wallet.
* For exchanges, it's suggested aiming for one, or few parties for the exchange vault and using memo tags for tracking deposits. See here for more information.

### Consequences & Implications

**Reading Data and Validator State**

A key implication of Canton's architecture for providing privacy, is how you read data. Unlike other blockchains where nodes are often ephemeral and interchangeable, in Canton, **validators have state**. This means that to access a party's or user's data, you must specifically connect to the **validator that hosts that party**. There is no single, all-encompassing blockchain RPC endpoint you can call to retrieve all data. Instead, you'll need to use your node's RPC for private data ("Ledger API") and potentially an app provider's API for their data (e.g., a "Scan API").

**Advantages and Consequences**

The design of the Canton Network leads to several significant advantages:

* **Privacy:** It enables true confidentiality at the smart contract level, as data is only distributed to the parties who have a legitimate need to see it.
* **Light Node Footprint:** Nodes only process their own transactions, not the entire network's, which keeps them lightweight and efficient.
* **Scalability:** The network can be scaled by simply adding more nodes.

However, this architecture has the consequence of decentralized data access, as previously mentioned.

<div id="implications-for-wallet-providers">
  **Implications for Wallet Providers**
</div>

To offer services on the Canton Network, you will need a **validator node to host your parties and your customers' parties**. You have two options for this: you can **self-host** a node or use a [node-as-a-service provider](https://sync.global/current-validators-offering-nodes/).

For **wallets and custodians**, this means your role extends beyond just safekeeping assets; you are also responsible for **safekeeping your customers' data** and preserving their privacy.

The Canton Network is designed to be agile and undergoes frequent upgrades. Node operators are asked to run nodes in three different environments: **DevNet, TestNet, and MainNet** to ensure that applications and integrations can be tested with new network upgrades. If you choose to self-host, be prepared to spin up and maintain nodes for all three environments. To stay informed and get support, it's highly recommended that self-hosting node operators join the validator node operator community on Slack.

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/integrating-with-canton-network/index.rst" hash="241a9637" */}

# Integrating with the Canton Network

When integrating with the Canton Network, we recommend that wallet providers support the necessary features outlined below to optimal user experience. Additionally, there are optional features that can further enhance the integration and provide additional value to users.

## Necessary Features

The following features are required for wallet providers to integrate with the Canton Network:

* Support the [CIP-0056 token standard](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md) to enable the holding and transferring of assets on the Canton Network. Documentation and guidance on how to implement this with the Wallet SDK is in the Token Standard section of this guide.
* Provide support specifically for Canton Coin and USDCx. The Canton Coin package of Amulet is preinstalled with all validators and USDCx is issued with the Digital Asset Registry and that dars for that application can be found in the DAR Package Versions of the Utilities documentation.
* [Memo tag support](#sending-deposits-to-exchanges) to allow deposits to be sent to exchanges
* [UTXO management](#utxo-management-and-locked-funds) to reduce the number of UTXOs

## Optional Features

While optional for wallet providers, the following features are strongly recommended to ensure full support for the Canton Network and maximize user adoption:

* [Canton Coin pre-approvals](/appdev/modules/m7-canton-coin-preapprovals). Documentation on how to implement pre-approvals with the Wallet SDK are in the [2-step transfer vs 1-step transfer section of this guide](#2-step-transfer-vs-1-step-transfer).
* dApp support by conforming to [CIP-0103](https://github.com/canton-foundation/cips/blob/main/cip-0103/cip-0103.md), the standard for wallet and dApp integration.
* The requirement to hold and transfer USDCx is included in the Necessary Features section above, however there are additional levels of support for USDCx for wallet providers to support such as supporting xReserves deposits and withdrawals and integrating the xReserve UI into the wallet directly. The options and instructions are laid out in the [USDCx Support for Wallets section of this guide](#usdcx-support-for-wallets).
* Pre-approvals for DA Registry issued assets.

## How to install the Wallet SDK

The Wallet SDK is available as a package on the NPM registry. You can install it using your preferred package manager.

<div className="tabs">
  .. group-tab:: npm .. code:: shell

  npm install @canton-network/wallet-sdk .. group-tab:: yarn .. code:: shell

  yarn add @canton-network/wallet-sdk .. group-tab:: pnpm .. code:: shell

  pnpm add @canton-network/wallet-sdk
</div>

Alternatively, to do dApp development only, the dApp SDK can be used which has a smaller bundle size and is optimized for browser usage. The dApp SDK can be installed with:

<div className="tabs">
  .. group-tab:: npm .. code:: shell

  npm install @canton-network/dapp-sdk .. group-tab:: yarn .. code:: shell

  yarn add @canton-network/dapp-sdk .. group-tab:: pnpm .. code:: shell

  pnpm add @canton-network/dapp-sdk
</div>

Both SDKs use the same underlying core packages and where only partial code is needed (like for transaction visualization or hash verification) those packages can be used independently.

## Hosting a Validator

As stated in the Implications for Wallet Providers section here, it's important for wallet providers to have a validator to host their users' parties. It's also strongly advised to operate a node in all three network environments so that you can test and verify your applications and integration as the Canton Network evolves.

Links to the node deployment docs are below depending on the deployment choice and environment. The guidance differs very little based on the environment - different URLs and arguments etc.:

* [MainNet docs](/global-synchronizer/deployment/onboarding-process)
  * [Docker Compose MainNet docs](/global-synchronizer/deployment/validator-docker-compose)
  * [Kubernetes MainNet docs](/global-synchronizer/deployment/validator-kubernetes)

* [TestNet docs](/global-synchronizer/deployment/onboarding-process)
  * [Docker Compose TestNet docs](/global-synchronizer/deployment/validator-docker-compose)
  * [Kubernetes TestNet docs](/global-synchronizer/deployment/validator-kubernetes)

* [DevNet](/global-synchronizer/deployment/onboarding-process)
  * [Docker Compose DevNet docs](/global-synchronizer/deployment/validator-docker-compose)
  * [Kubernetes DevNet docs](/global-synchronizer/deployment/validator-kubernetes)

The Wallet integration guide is tailored to work with a LocalNet setup ([/sdks-tools/development-tools/localnet](/sdks-tools/development-tools/localnet)) to make testing and verification easy.

## Connecting to a Synchronizer

For onboarding a validator with the global synchronizer it is recommended to read the Splice documentation here: [/global-synchronizer/deployment/onboarding-process](/global-synchronizer/deployment/onboarding-process)

## Supporting Tokens and Applications

To integrate and support tokens, it is recommended to use the Splice documentation here: [/global-synchronizer/deployment/onboarding-process](/global-synchronizer/deployment/onboarding-process)

If you are interested in building your own application, a good first place would be to utilize the CN quickstart: [https://github.com/digital-asset/cn-quickstart](https://github.com/digital-asset/cn-quickstart)

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/party-management/index.rst" hash="4a434174" */}

# Create an External Party (Wallet)

## Overview

Parties represent acting entities in the network and all transaction happens between one or more parties. To understand more about parties see the Parties in the Overview.

A detailed tutorial of the steps below can be seen in the External Signing Tutorial [here](/appdev/deep-dives/external-signing-onboarding) using python example scripts.

*This document focuses on the steps required to create an external party using the Wallet SDK.*

## How do I quickly allocate a party?

Using the wallet SDK you can quickly allocate a party using the following code snippet:

<div className="tabs">
  <div className="tab">
    Quick using Splice LocalNet

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import {
        SDK,
        TokenProviderConfig,
        localNetStaticConfig,
    } from '@canton-network/wallet-sdk'

    export default async function () {
        const auth: TokenProviderConfig = {
            method: 'self_signed',
            issuer: 'unsafe-auth',
            credentials: {
                clientId: 'ledger-api-user',
                clientSecret: 'unsafe',
                audience: 'https://canton.network.global',
                scope: '',
            },
        }

        /*
        if using OAuth, provide a different auth config when initializing the SDK such as:
            const auth = {
            method: 'client_credentials',
            configUrl: 'https://my-oauth-url',
            credentials: {
                clientId: 'your-client-id',
                clientSecret: 'your-client-secret',
                audience: `https://daml.com/jwt/aud/participant/${participantId}`,
                scope: 'openid daml_ledger_api offline_access',
            },
        }
        */

        const sdk = await SDK.create({
            auth,
            ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        })

        const key = sdk.keys.generate()

        // partyHint is optional but recommended to make it easier to identify the party
        const partyHint = 'my-wallet-1'

        await sdk.party.external
            .create(key.publicKey, { partyHint })
            .sign(key.privateKey)
            .execute()
    }
    ```
  </div>

  <div className="tab">
    Comprehensive using Splice LocalNet

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import {
        localNetStaticConfig,
        SDK,
        signTransactionHash,
    } from '@canton-network/wallet-sdk'
    import { pino } from 'pino'
    import { v4 } from 'uuid'
    import {
        TOKEN_NAMESPACE_CONFIG,
        TOKEN_PROVIDER_CONFIG_DEFAULT,
        AMULET_NAMESPACE_CONFIG,
    } from './utils/index.js'

    const logger = pino({ name: 'v1-01-ping-localnet', level: 'info' })

    const sdk = await SDK.create({
        auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: TOKEN_NAMESPACE_CONFIG,
        amulet: AMULET_NAMESPACE_CONFIG,
    })

    const senderKeys = sdk.keys.generate()

    const sender = await sdk.party.external
        .create(senderKeys.publicKey, {
            partyHint: 'v1-01-alice',
        })
        .sign(senderKeys.privateKey)
        .execute()

    const senderFingerprint = await sdk.keys.fingerprint(senderKeys.publicKey)

    logger.info({ sender, senderFingerprint }, 'Sender party representation:')

    if (sender.publicKeyFingerprint !== senderFingerprint)
        throw Error('Inconsistent fingerprints')

    const receiverKeys = sdk.keys.generate()

    const receiverPartyCreation = sdk.party.external.create(
        receiverKeys.publicKey,
        {
            partyHint: 'v1-01-bob',
        }
    )

    const unsignedReceiver = await receiverPartyCreation.topology()

    // external signing simulation
    const receiverPartySignature = signTransactionHash(
        unsignedReceiver.multiHash,
        receiverKeys.privateKey
    )

    const signedReceiverParty = await receiverPartyCreation.execute(
        receiverPartySignature
    )

    logger.info({ signedReceiverParty }, 'Receiver party representation:')

    const pingCommand = [
        {
            CreateCommand: {
                templateId:
                    '#canton-builtin-admin-workflow-ping:Canton.Internal.Ping:Ping',
                createArguments: {
                    id: v4(),
                    initiator: sender.partyId,
                    responder: sender.partyId,
                },
            },
        },
    ]

    logger.info({ pingCommand }, 'Ping command to be submitted:')

    await sdk.ledger
        .prepare({
            partyId: sender.partyId,
            commands: pingCommand,
            disclosedContracts: [],
        })
        .sign(senderKeys.privateKey)
        .execute({ partyId: sender.partyId })

    logger.info('Ping command submitted with online signing')

    /*
    offline signing example
    */

    const preparedPingCommand = sdk.ledger.prepare({
        partyId: sender.partyId,
        commands: pingCommand,
        disclosedContracts: [],
    })

    const { response: preparedPingCommandResponse } =
        await preparedPingCommand.toJSON()

    logger.info({ preparedPingCommand }, 'Prepared ping command:')

    /*
    Note: The following code uses the @canton-network/core-signing-lib as the 'custodian' of the private key to sign the prepared transaction hash,
    but in a real scenario, the signing could be done using any compatible signing mechanism, such as a hardware wallet or an external signing service.
    */
    const signature = signTransactionHash(
        preparedPingCommandResponse.preparedTransactionHash,
        senderKeys.privateKey
    )

    const signed = sdk.ledger.fromSignature(preparedPingCommandResponse, signature)

    await sdk.ledger.execute(signed, { partyId: sender.partyId })

    logger.info('Ping command submitted with offline signing')

    const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
        sender.partyId,
        '10000'
    )

    const result = await sdk.ledger
        .prepare({
            partyId: sender.partyId,
            commands: amuletTapCommand,
            disclosedContracts: amuletTapDisclosedContracts,
        })
        .sign(senderKeys.privateKey)
        .execute({ partyId: sender.partyId })

    const senderUtxos = await sdk.token.utxos.list({ partyId: sender.partyId })

    const tapTransaction = await sdk.token.transactionsById({
        updateId: result.updateId,
        partyId: sender.partyId,
    })

    const mintEvent = tapTransaction.events.find(
        (tokenStandardEvent) =>
            tokenStandardEvent.label.type === 'Mint' &&
            tokenStandardEvent.unlockedHoldingsChange.creates.find(
                (h) => h.amount === '10000.0000000000'
            )
    )

    if (mintEvent) {
        logger.info('Found token standard event with type Mint')
    } else {
        throw new Error(`Couldn't find tap transaction by updateId`)
    }
    const senderAmuletUtxos = senderUtxos.filter((utxo) => {
        return (
            utxo.interfaceViewValue.amount === '10000.0000000000' &&
            utxo.interfaceViewValue.instrumentId.id === 'Amulet'
        )
    })

    if (senderAmuletUtxos.length === 0) {
        throw new Error('No UTXOs found for Sender')
    }

    logger.info('Tap command for Amulet for Sender submitted and UTXO received')
    ```
  </div>
</div>

## Create a key pair

The process for creating a key using standard encryption practices is similar that in other blockchains. The full details of supported cryptographic algorithms can be found [Here](/overview/learn/cryptographic-keys). By default an **Ed25519** encryption is used. There exists many libraries that can be used to generate such a key pair, you can do it simply with the WalletSDK using:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    sdk.keys.generate()
}
```

### Generating Keys from a Mnemonic Phrase (BIP-0039)

The Canton Network supports the generation of cryptographic keys using a mnemonic code or mnemonic sentence, following the [BIP-0039 standard](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki).

Using a mnemonic phrase allows for deterministic key generation, which simplifies the backup and recovery process. Instead of managing individual private key files, you can recreate your keys across different environments using a human-readable sequence of words.

A typescript example of generating an Ed25519 key pair with a BIP-0039 mnemonic phrase using the libraries bip39 and ed25519 as dependencies is shown below:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { getPublicKeyFromPrivate } from '@canton-network/wallet-sdk'
import naclUtil from 'tweetnacl-util'
import * as bip39 from 'bip39'
import * as fs from 'fs'

export default async function createCantonKeyFromMnemonic() {
    try {
        // 1. Generate a new 24-word BIP-0039 mnemonic
        const mnemonic = bip39.generateMnemonic(256)
        console.log('Generated Mnemonic:', mnemonic)

        // 2. Convert mnemonic to a seed
        const seed = await bip39.mnemonicToSeed(mnemonic)

        // 3. Derive a 32-byte Private Key (first 32 bytes of the seed)
        const privateKey = naclUtil.encodeBase64(seed.slice(0, 32))
        const publicKey = getPublicKeyFromPrivate(privateKey)

        console.log('Private Key (bas64):', privateKey)
        console.log('Public Key (bas64):', publicKey)

        // 4. Save to a file for Canton Import
        fs.writeFileSync('canton_private_key.base64', privateKey)

        console.log(
            "\nSuccess: Private key saved to 'canton_private_key.base64'"
        )
        console.log('Keep your mnemonic phrase safe!')
    } catch (error) {
        console.error('An error occurred:', error)
    }
}
```

## Choosing a party hint

The unique party id is defined as **\${partyHint}::\${fingerprint}**. The partyHint is a user friendly name and can be anything that is unique for the fingerprint, e.g. "alice", "bob" or "my-wallet-1". It is recommended to include a hint when setting up the party (see `quick-party-allocation` for an example).

## Generate the fingerprint

The wallet SDK has a built in function to generate the fingerprint:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    const keys = EXISTING_PARTY_1_KEYS

    await sdk.keys.fingerprint(keys.publicKey)
}
```

this can be used to determine the unique party id beforehand or recompute the fingerprint based on the public key.

## Generating the topology transactions

When onboarding using external signing, multiple topology transactions are required to be generated and signed. This is because both the keyHolder (the party) and the node (the validator) need to agree on the hosting relationship. The three transactions that needs to be generated are:

* \`PartyToParticipant\`: This transaction indicates that the party agrees to be hosted by the participant (validator).
* \`ParticipantToParty\`: This transaction indicates that the participant (validator) agrees to host the party.
* \`KeyToParty\`: This transaction indicates that the key (public key) is associated with the party.

Once all the transactions are built they can be combined into a single hash and submitted as part of a single signature. The wallet SDK has helper functions to generate these transactions:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    const key = sdk.keys.generate()

    // partyHint is optional but recommended to make it easier to identify the party
    const partyHint = 'my-wallet-1'

    const prepared = sdk.party.external.create(key.publicKey, {
        partyHint,
    })

    await prepared.topology()
}
```

## Decoding the topology transactions

Sometimes converting the topology transactions to human readable json might be needed, for this you can use the `.decode()` function:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        amulet: AMULET_NAMESPACE_CONFIG,
    })

    const sender = global.EXISTING_PARTY_1

    const [tapCommand, disclosedContracts] = await sdk.amulet.tap(
        sender,
        '2000'
    )

    const preparedTransaction = sdk.ledger.prepare({
        commands: tapCommand,
        disclosedContracts,
        partyId: sender,
    })

    await preparedTransaction.decode()
}
```

## Sign multi-hash

Since the topology transactions need to be submitted together the combined hash needs to be signed. The wallet SDK has a helper function to sign the combined hash:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    SDK,
    localNetStaticConfig,
    signTransactionHash,
} from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    const keys = sdk.keys.generate()

    const preparedParty = EXISTING_TOPOLOGY

    //This signing function works for a party topology hash or a transaction hash
    signTransactionHash(preparedParty.multiHash, keys.privateKey)
}
```

## Submit the topology transactions

Once the signature is generated, the topology transactions can be submitted to the validator. The wallet SDK has a helper function to submit the transactions:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    SDK,
    localNetStaticConfig,
    signTransactionHash,
} from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    //Online signing
    const keys = sdk.keys.generate()

    await sdk.party.external
        .create(keys.publicKey, {
            partyHint: 'snippet-party-hint',
        })
        .sign(keys.privateKey)
        .execute()

    //offline signing where the keys are held externally
    const offlineSigningKeys = sdk.keys.generate()

    const receiverPartyCreation = sdk.party.external.create(
        offlineSigningKeys.publicKey,
        {
            partyHint: 'offline-signing-party',
        }
    )

    const unsignedReceiver = await receiverPartyCreation.topology()

    // offline signing simulation - in most cases a signing provider would sign the multihash
    const receiverPartySignature = signTransactionHash(
        unsignedReceiver.multiHash,
        offlineSigningKeys.privateKey
    )

    await receiverPartyCreation.execute(receiverPartySignature)
}
```

## Multi-hosting a party

Since only relevant data is shared between validator nodes, and nodes don't contain all data, backup and recovery are important. Another important aspect is to prevent having a validator being a single source of failure, this can be handled on a party basis by doing multi hosting. Multi hosting of a party means replication of all the information related to that party onto multiple validators, this can either be multiple validators run by the same entity (most common case for wallets) or even validators run by different entities in case of malicious actors.

To facilitate multi-hosting we simply need to extend `partyToParticipant` and `ParticipantToParty` to include new validators. This requires sourcing signed transaction from the validators the client is interested in being hosted on.

The below script allows you (by using the SDK) to host a single party on both `app-user` and `app-provider` validators.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import pino from 'pino'
import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
import {
    TOKEN_PROVIDER_CONFIG_DEFAULT,
    AMULET_NAMESPACE_CONFIG,
} from './utils/index.js'

const logger = pino({ name: 'v1-03-parties', level: 'info' })

const userId = localNetStaticConfig.LOCALNET_USER_ID

const sdk = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    amulet: AMULET_NAMESPACE_CONFIG,
})

const allocatedParties = await Promise.all(
    ['v1-03-alice', 'v1-03-bob'].map((partyHint) => {
        const partyKeys = sdk.keys.generate()
        return sdk.party.external
            .create(partyKeys.publicKey, {
                partyHint,
            })
            .sign(partyKeys.privateKey)
            .execute()
    })
)

logger.info(allocatedParties, 'Allocated parties')

const listedParties = await sdk.party.list()

logger.info(listedParties, `Obtained parties for ${userId}`)

const allocatedPartiesIds = new Set(
    allocatedParties.map((party) => party.partyId)
)

if (!allocatedPartiesIds.isSubsetOf(new Set(listedParties))) {
    throw new Error(
        "At least some of the allocated parties haven't been listed."
    )
}

const featuredAppRights = await sdk.amulet.featuredApp.grant()

if (!featuredAppRights) {
    throw new Error(
        'Failed to obtain featured app rights for validator operator party'
    )
} else {
    logger.info(
        featuredAppRights,
        'Featured app rights for validator operator party'
    )
}

logger.info('Preparing multi hosted party...')

const participantEndpoints = [
    {
        url: new URL('http://127.0.0.1:3975'),
        tokenProviderConfig: TOKEN_PROVIDER_CONFIG_DEFAULT,
    },
]

const charlieKeys = sdk.keys.generate()
const charlie = await sdk.party.external
    .create(charlieKeys.publicKey, {
        partyHint: 'v1-03-charlie',
        confirmingParticipantEndpoints: participantEndpoints,
    })
    .sign(charlieKeys.privateKey)
    .execute()

logger.info(charlie, 'Multi hosted party allocated successfully')

const charliePingCommand = sdk.utils.ping.create([
    { initiator: charlie.partyId, responder: charlie.partyId },
])

const pingResult = await sdk.ledger
    .prepare({
        partyId: charlie.partyId,
        commands: charliePingCommand,
    })
    .sign(charlieKeys.privateKey)
    .execute({
        partyId: charlie.partyId,
    })

logger.info(
    pingResult,
    'Successfully validated party allocation via Canton.Internal.Ping'
)

logger.info('Preparing multi hosted party with observing participant...')

const observingCharlieKeys = sdk.keys.generate()
const observingCharlie = await sdk.party.external
    .create(observingCharlieKeys.publicKey, {
        partyHint: 'v1-03-observingCharlie',
        observingParticipantEndpoints: participantEndpoints,
    })
    .sign(observingCharlieKeys.privateKey)
    .execute()

logger.info(
    observingCharlie,
    'Multi hosted party with observing participant allocated successfully'
)

const observingConradPingCommand = sdk.utils.ping.create([
    {
        initiator: observingCharlie.partyId,
        responder: observingCharlie.partyId,
    },
])

const observingPingResult = await sdk.ledger
    .prepare({
        partyId: observingCharlie.partyId,
        commands: observingConradPingCommand,
    })
    .sign(observingCharlieKeys.privateKey)
    .execute({
        partyId: observingCharlie.partyId,
    })

logger.info(
    observingPingResult,
    'Successfully validated observing party allocation via Canton.Internal.Ping'
)
```

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/finding-and-reading-data/index.rst" hash="20fe15cb" */}

# Finding and Reading Data

The wallet SDK primarily focus on an on-party basis interaction, therefore it is almost always required to define the party you are using fo each command/

## Reading Available Parties

Reading all available parties to you can easily be done using the wallet SDK as shown in the example below, and the result is paginated. It's worth noting that the call to read all available parties doesn't use the the party and synchronizer fields therefore changing them has no effect on the result.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    await sdk.party.list()
}
```

## Reading Ledger End

A lot of different requests will take a ledger offset to ensure the requested time correlates with ledger time. A Validator does not have a block height since there is no total state replication. There are two values that correlate:

* ledger time - this is the time the ledger chooses when computing a transaction prior to commit.
* record time - this is the time assigned by the sequencer when registering the confirmation request.

Ledger time should be used for all operations in your local environment (that does not affect partners). When doing reconciliation for transactions with partners or other members of a synchronizer it is better to use record time.

Ledger end is used as a default for wallet SDK operations.

## Reading Active Contracts

Using the above ledger time we can figure out what the current state of all active contracts are. Contracts can be in two states - active and archived - which correlates to the UTXO mode of unspent and spent. Active contracts are contracts that are unspent and thereby can be used in new transactions or to exercise choices.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    const myParty = global.EXISTING_PARTY_1
    //we use holdings as an example here
    const myTemplateId = '#splice-amulet:Splice.Amulet:Amulet'

    await sdk.ledger.acsReader.read({
        parties: [myParty],
        templateIds: [myTemplateId], //this is optional for if you want to filter by template id
        filterByParty: true,
    })
}
```

## Visualizing a Transaction

The Wallet SDK uses a transaction parsing transform a fully fledged transaction tree into human recognizable transaction view. The full code for the transaction parsing can be found at [parser typescript class](https://github.com/canton-network/wallet/blob/main/core/ledger-client/src/txparse/parser.ts).

The Wallet SDK uses this parser to transform all transaction tree interacted with into PrettyTransactions.

for instance on the `getTransactionById` or `listHoldingTransactions` (Detailed here).

The Transactions will have format:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export interface Transaction {
    updateId: string // unique updateId
    offset: number // the ledger offset (local validator)
    recordTime: string // time recorded on the synchronizer (use this if needed to compare with another ledger)
    synchronizerId: string // the synchronizer the transaction happened on
    events: TokenStandardEvent[] // event representing all the changes caused by the transaction
}
```

A single transaction can contain multiple events (deposits and withdrawals are considered events). In order to figure out the on chain transaction it is required to iterate over all the events. The events have the format:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export interface TokenStandardEvent {
    label: Label // used to identify the type of transaction
    lockedHoldingsChange: HoldingsChange // all the changes to locked holdings
    lockedHoldingsChangeSummary: HoldingsChangeSummary // summary of above changes
    unlockedHoldingsChange: HoldingsChange // all the changes to unlocked holdings
    unlockedHoldingsChangeSummary: HoldingsChangeSummary // summary of above changes
    transferInstruction: TransferInstructionView | null // any pending transfer instructions
}
```

below you can have a look at different event types and how to potentially visualize the transaction for a client

<div className="tabs">
  <div className="tab">
    Tap operation

    Here is an example on how a "tap" event looks like (Performing tap):

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
        "updateId": "1220a8d78d06461abd045813491f9997a1bcf2f29d4c2a9afadeb89616998201b40a",
        "offset": 1313,
        "recordTime": "2025-10-14T02:11:45.485840Z",
        "synchronizerId": "global-domain::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
        "events": [
            {
                "label": {
                    "burnAmount": "0",
                    "mintAmount": "2000000",
                    "type": "Mint",
                    "tokenStandardChoice": null,
                    "reason": "tapped faucet",
                    "meta": {
                        "values": {}
                    }
                },
                "unlockedHoldingsChange": {
                    "creates": [
                        {
                            "amount": "2000000.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305",
                            "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": null
                        }
                    ]
                },
                "unlockedHoldingsChangeSummary": {
                    "numOutputs": 1,
                    "outputAmount": "2000000",
                    "amountChange": "2000000"
                },
                "transferInstruction": null
            }
        ]
    }
    ```

    The tap gives a nice and simple view some key values to look at. Using the `label` we can quickly gage what is happening:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "label": {
        "burnAmount": "0", // how much was burned
        "mintAmount": "2000000", // how much was minted
        "type": "Mint", // event type
        "tokenStandardChoice": null, // no token standard choice
        "reason": "tapped faucet", // reason
        "meta": {
            "values": {} // any other meta data value
        }
    }
    ```

    For a "tap" event we don't have any locked holding changes, however we do have an unlocked create event:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "unlockedHoldingsChange": {
        // we have one create event
        // if utxos what spend this would be an archive instead
        "creates": [
            {
                // amount on the utxo
                "amount": "2000000.0000000000",
                // instrument information
                "instrumentId": {
                    "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                    "id": "Amulet"
                },
                // the contract id of the new utxo
                "contractId": "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305",
                // owner of the utxo
                "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                // any meta data
                "meta": {
                    "values": {
                        "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                        "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                    }
                },
                // lock if applicable
                "lock": null
            }
        ]
    }
    ```
  </div>

  <div className="tab">
    Merge Split

    A Merge or split is usually done by performing a transfer to yourself, by selecting several input utxos they can be consolidated into one and likewise a transfer to yourself of one big utxo can be used to split it into two. Below is the usual merge split that you would see if you use an utxo that is bigger than the transferred amount when performing a 2-step transfer:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
        "updateId": "1220f5c5a8403d830babd0b25124701ec59c0540d3f75377fe48df34c89a955f7bfc",
        "offset": 1316,
        "recordTime": "2025-10-14T02:11:47.509312Z",
        "synchronizerId": "global-domain::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
        "events": [
            {
                "label": {
                    "burnAmount": "0",
                    "mintAmount": "0",
                    "type": "MergeSplit",
                    "tokenStandardChoice": {
                        "name": "TransferFactory_Transfer",
                        "choiceArgument": {
                            "expectedAdmin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                            "transfer": {
                                "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                                "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                                "amount": "100.0000000000",
                                "instrumentId": {
                                    "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                    "id": "Amulet"
                                },
                                "requestedAt": "2025-10-14T02:10:47.406Z",
                                "executeBefore": "2025-10-15T02:11:47.406Z",
                                "inputHoldingCids": [
                                    "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305"
                                ],
                                "meta": {
                                    "values": {
                                        "splice.lfdecentralizedtrust.org/reason": "memo-ref"
                                    }
                                }
                            },
                            "extraArgs": {
                                "context": {
                                    "values": {
                                        "amulet-rules": {
                                            "tag": "AV_ContractId",
                                            "value": "00ccd166b3b91e776fc1d2270d3ffdff551bd43117c679a145281d4c4545fa8bc7ca1112204f1604f06e4c616656c39678e173f68a2ae3a96af984b71120a6da57ca34d66c"
                                        },
                                        "open-round": {
                                            "tag": "AV_ContractId",
                                            "value": "003a5299317dd50dc84c2a645f2b233f69dfd16286ddf9dd2996c764ff93e591cbca11122008b6e9f88a00262449d8e6bf4de2edf50b85a160c068744b53091653fb107b9f"
                                        }
                                    }
                                },
                                "meta": {
                                    "values": {}
                                }
                            }
                        },
                        "exerciseResult": {
                            "output": {
                                "tag": "TransferInstructionResult_Pending",
                                "value": {
                                    "transferInstructionCid": "002e296168aeabe02e40c04874c794a5855f918b8acf950f56b2b941c09305fd4bca1112201bda3ae677b8a26e682f6869c97afeea9136852ee31e638045f6be87d6c0e953"
                                }
                            },
                            "senderChangeCids": [
                                "00ba31e046f04908e6bf6fe5eeb725f0e2054f37353e85c7ef99a0924df8c1b891ca11122046dee24aeae91d4a5fc0570458cad8ccc94002645b6a6e2c82cc5f07ca897fe9"
                            ],
                            "meta": {
                                "values": {}
                            }
                        }
                    },
                    "reason": "memo-ref",
                    "meta": {
                        "values": {}
                    }
                },
                "lockedHoldingsChange": {
                    "creates": [
                        {
                            "amount": "100.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b",
                            "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": {
                                "holders": [
                                    "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36"
                                ],
                                "expiresAt": "2025-10-15T02:11:47.406Z",
                                "expiresAfter": null,
                                "context": "transfer to 'bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783'"
                            }
                        }
                    ]
                },
                "lockedHoldingsChangeSummary": {
                    "numOutputs": 1,
                    "outputAmount": "100",
                    "amountChange": "100"
                },
                "unlockedHoldingsChange": {
                    "creates": [
                        {
                            "amount": "1999900.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "00ba31e046f04908e6bf6fe5eeb725f0e2054f37353e85c7ef99a0924df8c1b891ca11122046dee24aeae91d4a5fc0570458cad8ccc94002645b6a6e2c82cc5f07ca897fe9",
                            "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": null
                        }
                    ],
                    "archives": [
                        {
                            "amount": "2000000.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305",
                            "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": null
                        }
                    ]
                },
                "unlockedHoldingsChangeSummary": {
                    "numInputs": 1,
                    "inputAmount": "2000000",
                    "numOutputs": 1,
                    "outputAmount": "1999900",
                    "amountChange": "-100"
                },
                "transferInstruction": {
                    "originalInstructionCid": null,
                    "transfer": {
                        "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                        "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                        "amount": "100.0000000000",
                        "instrumentId": {
                            "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                            "id": "Amulet"
                        },
                        "requestedAt": "2025-10-14T02:10:47.406Z",
                        "executeBefore": "2025-10-15T02:11:47.406Z",
                        "inputHoldingCids": [
                            "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305"
                        ],
                        "meta": {
                            "values": {
                                "splice.lfdecentralizedtrust.org/reason": "memo-ref"
                            }
                        }
                    },
                    "status": {
                        "before": null
                    },
                    "meta": null
                }
            }
        ]
    }
    ```

    The label gives us the quick information

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "label": {
            "burnAmount": "0",  // how much was burned
            "mintAmount": "0",  // how much was minted
            "type": "MergeSplit", // event type
            "tokenStandardChoice": { // the entire token standard choice

            },
            "reason": "memo-ref", // memo tag
            "meta": { // any other relevant meta data
              "values": {}
            }
          }
    ```

    The locked holding change shows one new utxo equivalent to the amount send to Bob. Once Bob accepts the transfer this locked utxo would be archived.information.

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "lockedHoldingsChange": {
           // we have 1 new locked holding of the transfer amount (100)
           "creates": [
             {
               "amount": "100.0000000000",
               "instrumentId": {
                 "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                 "id": "Amulet"
               },
               "contractId": "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b",
               // alice is still the owner since this a locked utxo, until bob accepts
               "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
               "meta": {
                 "values": {
                   "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                   "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                 }
               },
               "lock": {
               // the DSO (instrument Admin) is holder of the lock
                 "holders": [
                   "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36"
                 ],
                 "expiresAt": "2025-10-15T02:11:47.406Z",
                 "expiresAfter": null,
                 "context": "transfer to 'bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783'"
               }
             }
           ]
         },
         //overview of how holdings have changed
         "lockedHoldingsChangeSummary": {
           "numOutputs": 1,
           "outputAmount": "100",
           "amountChange": "100"
         },
    ```

    There is also an unlocked holding change, consist of one create and one archive. Since alice had one transaction of 2000000.0000000000, and only send 100, then she gets the remaining 1999900.0000000000 back:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "unlockedHoldingsChange": {
            // creates the new utxo for alice with the unspent amount
            "creates": [
              {
                "amount": "1999900.0000000000",
                "instrumentId": {
                  "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                  "id": "Amulet"
                },
                "contractId": "00ba31e046f04908e6bf6fe5eeb725f0e2054f37353e85c7ef99a0924df8c1b891ca11122046dee24aeae91d4a5fc0570458cad8ccc94002645b6a6e2c82cc5f07ca897fe9",
                "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                "meta": {
                  "values": {
                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                  }
                },
                "lock": null
              }
            ],
            // archives the old spend utxo
            "archives": [
              {
                "amount": "2000000.0000000000",
                "instrumentId": {
                  "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                  "id": "Amulet"
                },
                "contractId": "00cee8d2659d5966962fbda321aae358092eafbb162d46f2639a8da0688ef3ee8aca11122096aeb27e0fa9c03a3209fda9db88e4e67a2ba1509f094bdd82a38d844ca65305",
                "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                "meta": {
                  "values": {
                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                  }
                },
                "lock": null
              }
            ]
          },
          // overview of how this has changed alices utxos
          "unlockedHoldingsChangeSummary": {
            "numInputs": 1,
            "inputAmount": "2000000",
            "numOutputs": 1,
            "outputAmount": "1999900",
            "amountChange": "-100"
          }
    ```
  </div>

  <div className="tab">
    Transfer Out

    When Bob accepts the transfer we see the actual transfer out event. This is seen from Alice point of view

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
        "updateId": "122064654ed225797ea8161eb0730d38beff917201cecb00079666192cda648bb182",
        "offset": 1319,
        "recordTime": "2025-10-14T02:11:48.989233Z",
        "synchronizerId": "global-domain::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
        "events": [
            {
                "label": {
                    "burnAmount": "0",
                    "mintAmount": "0",
                    "type": "TransferOut",
                    "receiverAmounts": [
                        {
                            "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                            "amount": "100"
                        }
                    ],
                    "tokenStandardChoice": {
                        "name": "TransferInstruction_Accept",
                        "choiceArgument": {
                            "extraArgs": {
                                "context": {
                                    "values": {
                                        "amulet-rules": {
                                            "tag": "AV_ContractId",
                                            "value": "00ccd166b3b91e776fc1d2270d3ffdff551bd43117c679a145281d4c4545fa8bc7ca1112204f1604f06e4c616656c39678e173f68a2ae3a96af984b71120a6da57ca34d66c"
                                        },
                                        "expire-lock": {
                                            "tag": "AV_Bool",
                                            "value": true
                                        },
                                        "open-round": {
                                            "tag": "AV_ContractId",
                                            "value": "003a5299317dd50dc84c2a645f2b233f69dfd16286ddf9dd2996c764ff93e591cbca11122008b6e9f88a00262449d8e6bf4de2edf50b85a160c068744b53091653fb107b9f"
                                        }
                                    }
                                },
                                "meta": {
                                    "values": {}
                                }
                            }
                        },
                        "exerciseResult": {
                            "output": {
                                "tag": "TransferInstructionResult_Completed",
                                "value": {
                                    "receiverHoldingCids": [
                                        "002e360f78cf28a40c742839572bbf7a683ba59c3db906757b284a2edf433700edca1112209685da5d5a5c531b51504601c175cbbeaba8956e7a7fc2926fa8909d8b81a95a"
                                    ]
                                }
                            },
                            "senderChangeCids": [],
                            "meta": {
                                "values": {}
                            }
                        }
                    },
                    "reason": "memo-ref",
                    "meta": {
                        "values": {}
                    }
                },
                "lockedHoldingsChange": {
                    "archives": [
                        {
                            "amount": "100.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b",
                            "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": {
                                "holders": [
                                    "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36"
                                ],
                                "expiresAt": "2025-10-15T02:11:47.406Z",
                                "expiresAfter": null,
                                "context": "transfer to 'bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783'"
                            }
                        }
                    ]
                },
                "lockedHoldingsChangeSummary": {
                    "numInputs": 1,
                    "inputAmount": "100",
                    "amountChange": "-100"
                },
                "transferInstruction": {
                    "originalInstructionCid": null,
                    "transfer": {
                        "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                        "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                        "amount": "100.0000000000",
                        "instrumentId": {
                            "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                            "id": "Amulet"
                        },
                        "requestedAt": "2025-10-14T02:10:47.406Z",
                        "executeBefore": "2025-10-15T02:11:47.406Z",
                        "inputHoldingCids": [
                            "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b"
                        ],
                        "meta": {
                            "values": {
                                "splice.lfdecentralizedtrust.org/reason": "memo-ref"
                            }
                        }
                    },
                    "meta": {
                        "values": {}
                    },
                    "status": {
                        "before": {
                            "tag": "TransferPendingReceiverAcceptance",
                            "value": {}
                        }
                    }
                }
            }
        ]
    }
    ```

    The label gives us the quick information.

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "label": {
            "burnAmount": "0", // how much was burned
            "mintAmount": "0",  // how much was minted
            "type": "TransferOut", // event type
            "receiverAmounts": [ // the list of receivers and how much
              {
                "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                "amount": "100"
              }
            ],
            "tokenStandardChoice": { // the entire token standard choice

            },
            "reason": "memo-ref", // memo tag
            "meta": { // any other meta data
              "values": {}
            }
          }
    ```

    We can see that the locked 100 transfer is now archived, on Bobs side he will see a Transfer In that creates an unlocked holding of 100.

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "lockedHoldingsChange": {
            // The locked utxo is archived
            "archives": [
              {
                "amount": "100.0000000000",
                "instrumentId": {
                  "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                  "id": "Amulet"
                },
                "contractId": "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b",
                "owner": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                "meta": {
                  "values": {
                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                  }
                },
                "lock": {
                  "holders": [
                    "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36"
                  ],
                  "expiresAt": "2025-10-15T02:11:47.406Z",
                  "expiresAfter": null,
                  "context": "transfer to 'bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783'"
                }
              }
            ]
          }
    ```
  </div>

  <div className="tab">
    Transfer In

    Bob will see a transfer in once he has accepted the transferInstruction from Alice. If Bob had set up transfer pre-approval, then he would only see the below transfer:

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
        "updateId": "122064654ed225797ea8161eb0730d38beff917201cecb00079666192cda648bb182",
        "offset": 1319,
        "recordTime": "2025-10-14T02:11:48.989233Z",
        "synchronizerId": "global-domain::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
        "events": [
            {
                "label": {
                    "type": "TransferIn",
                    "burnAmount": "0",
                    "mintAmount": "0",
                    "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                    "tokenStandardChoice": {
                        "name": "TransferInstruction_Accept",
                        "choiceArgument": {
                            "extraArgs": {
                                "context": {
                                    "values": {
                                        "amulet-rules": {
                                            "tag": "AV_ContractId",
                                            "value": "00ccd166b3b91e776fc1d2270d3ffdff551bd43117c679a145281d4c4545fa8bc7ca1112204f1604f06e4c616656c39678e173f68a2ae3a96af984b71120a6da57ca34d66c"
                                        },
                                        "expire-lock": {
                                            "tag": "AV_Bool",
                                            "value": true
                                        },
                                        "open-round": {
                                            "tag": "AV_ContractId",
                                            "value": "003a5299317dd50dc84c2a645f2b233f69dfd16286ddf9dd2996c764ff93e591cbca11122008b6e9f88a00262449d8e6bf4de2edf50b85a160c068744b53091653fb107b9f"
                                        }
                                    }
                                },
                                "meta": {
                                    "values": {}
                                }
                            }
                        },
                        "exerciseResult": {
                            "output": {
                                "tag": "TransferInstructionResult_Completed",
                                "value": {
                                    "receiverHoldingCids": [
                                        "002e360f78cf28a40c742839572bbf7a683ba59c3db906757b284a2edf433700edca1112209685da5d5a5c531b51504601c175cbbeaba8956e7a7fc2926fa8909d8b81a95a"
                                    ]
                                }
                            },
                            "senderChangeCids": [],
                            "meta": {
                                "values": {}
                            }
                        }
                    },
                    "reason": "memo-ref",
                    "meta": {
                        "values": {}
                    }
                },
                "unlockedHoldingsChange": {
                    "creates": [
                        {
                            "amount": "100.0000000000",
                            "instrumentId": {
                                "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                                "id": "Amulet"
                            },
                            "contractId": "002e360f78cf28a40c742839572bbf7a683ba59c3db906757b284a2edf433700edca1112209685da5d5a5c531b51504601c175cbbeaba8956e7a7fc2926fa8909d8b81a95a",
                            "owner": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                            "meta": {
                                "values": {
                                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                                }
                            },
                            "lock": null
                        }
                    ]
                },
                "unlockedHoldingsChangeSummary": {
                    "numOutputs": 1,
                    "outputAmount": "100",
                    "amountChange": "100"
                },
                "transferInstruction": {
                    "originalInstructionCid": null,
                    "transfer": {
                        "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
                        "receiver": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                        "amount": "100.0000000000",
                        "instrumentId": {
                            "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                            "id": "Amulet"
                        },
                        "requestedAt": "2025-10-14T02:10:47.406Z",
                        "executeBefore": "2025-10-15T02:11:47.406Z",
                        "inputHoldingCids": [
                            "00b0af2ac89701b35d60b52fa239a66a993b383f963a9230f3f04e6510290dbe95ca1112200df1866e4ed7b50d6f9ac02b348a47a47b70c4d74f8d9575a1453ee9fe175f1b"
                        ],
                        "meta": {
                            "values": {
                                "splice.lfdecentralizedtrust.org/reason": "memo-ref"
                            }
                        }
                    },
                    "meta": {
                        "values": {}
                    },
                    "status": {
                        "before": {
                            "tag": "TransferPendingReceiverAcceptance",
                            "value": {}
                        }
                    }
                }
            }
        ]
    }
    ```

    The label gives us the quick information.

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "label": {
            "type": "TransferIn", // event type
            "burnAmount": "0",  // how much was burned
            "mintAmount": "0", // how much was minted
            // the original sender of the amount
            "sender": "alice::12201acb807c49aceaeb68b1d89bb3bea95fe740b4b0a6cca428e6a351c2450540f4",
            "tokenStandardChoice": {

            },
            "reason": "memo-ref", // memo tag
            "meta": { // any other meta fields
              "values": {}
            }
          }
    ```

    Bob then also sees one new unlocked utxo for the 100.

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    "unlockedHoldingsChange": {
            // the new money available for Bob
            "creates": [
              {
                "amount": "100.0000000000",
                "instrumentId": {
                  "admin": "DSO::1220294d264ccf205000d72d9f0106e3a0e8ce8d34982d7f134c42d42d18750ccd36",
                  "id": "Amulet"
                },
                "contractId": "002e360f78cf28a40c742839572bbf7a683ba59c3db906757b284a2edf433700edca1112209685da5d5a5c531b51504601c175cbbeaba8956e7a7fc2926fa8909d8b81a95a",
                "owner": "bob::1220447e99360f4e11caf7be818b96ead2a23c593eb927f792ae5f0a0bc15b264783",
                "meta": {
                  "values": {
                    "amulet.splice.lfdecentralizedtrust.org/created-in-round": "32",
                    "amulet.splice.lfdecentralizedtrust.org/rate-per-round": "0.00380518"
                  }
                },
                "lock": null
              }
            ]
          }
    ```
  </div>
</div>

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/preparing-and-signing-transactions/index.rst" hash="39205f15" */}

# Preparing and Signing Transactions Using External Party

## High-level Signing Process

The basic steps of preparing and signing a transaction using an external party are as follows:

1. **Creating a command** - You start by simply creating a command.
2. **Preparing the transaction** - You send the command to the blockchain RPC, offered by your node, to prepare the transaction.
3. **Validating the transaction** - You inspect the transaction and decide whether to sign it.
4. **Signing the transaction** - Once validated, you sign the transaction hash using your private key (typically with ECDSA/EdDSA).
5. **Submitting the transaction** - You submit the signed transaction to be executed.
6. **Observing the transaction** - You observe the blockchain until the transaction is committed.

In the examples below, the SDK examples use the Ping app which comes pre-installed with the validator and the cURL examples show the underlying HTTP requests using Canton Coin following a token standard transfer.

## How do I quickly execute a Ping?

Below shows how to quickly execute a ping command against yourself on a running Splice LocalNet:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    localNetStaticConfig,
    SDK,
    signTransactionHash,
} from '@canton-network/wallet-sdk'
import { pino } from 'pino'
import { v4 } from 'uuid'
import {
    TOKEN_NAMESPACE_CONFIG,
    TOKEN_PROVIDER_CONFIG_DEFAULT,
    AMULET_NAMESPACE_CONFIG,
} from './utils/index.js'

const logger = pino({ name: 'v1-01-ping-localnet', level: 'info' })

const sdk = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    token: TOKEN_NAMESPACE_CONFIG,
    amulet: AMULET_NAMESPACE_CONFIG,
})

const senderKeys = sdk.keys.generate()

const sender = await sdk.party.external
    .create(senderKeys.publicKey, {
        partyHint: 'v1-01-alice',
    })
    .sign(senderKeys.privateKey)
    .execute()

const senderFingerprint = await sdk.keys.fingerprint(senderKeys.publicKey)

logger.info({ sender, senderFingerprint }, 'Sender party representation:')

if (sender.publicKeyFingerprint !== senderFingerprint)
    throw Error('Inconsistent fingerprints')

const receiverKeys = sdk.keys.generate()

const receiverPartyCreation = sdk.party.external.create(
    receiverKeys.publicKey,
    {
        partyHint: 'v1-01-bob',
    }
)

const unsignedReceiver = await receiverPartyCreation.topology()

// external signing simulation
const receiverPartySignature = signTransactionHash(
    unsignedReceiver.multiHash,
    receiverKeys.privateKey
)

const signedReceiverParty = await receiverPartyCreation.execute(
    receiverPartySignature
)

logger.info({ signedReceiverParty }, 'Receiver party representation:')

const pingCommand = [
    {
        CreateCommand: {
            templateId:
                '#canton-builtin-admin-workflow-ping:Canton.Internal.Ping:Ping',
            createArguments: {
                id: v4(),
                initiator: sender.partyId,
                responder: sender.partyId,
            },
        },
    },
]

logger.info({ pingCommand }, 'Ping command to be submitted:')

await sdk.ledger
    .prepare({
        partyId: sender.partyId,
        commands: pingCommand,
        disclosedContracts: [],
    })
    .sign(senderKeys.privateKey)
    .execute({ partyId: sender.partyId })

logger.info('Ping command submitted with online signing')

/*
offline signing example
*/

const preparedPingCommand = sdk.ledger.prepare({
    partyId: sender.partyId,
    commands: pingCommand,
    disclosedContracts: [],
})

const { response: preparedPingCommandResponse } =
    await preparedPingCommand.toJSON()

logger.info({ preparedPingCommand }, 'Prepared ping command:')

/*
Note: The following code uses the @canton-network/core-signing-lib as the 'custodian' of the private key to sign the prepared transaction hash,
but in a real scenario, the signing could be done using any compatible signing mechanism, such as a hardware wallet or an external signing service.
*/
const signature = signTransactionHash(
    preparedPingCommandResponse.preparedTransactionHash,
    senderKeys.privateKey
)

const signed = sdk.ledger.fromSignature(preparedPingCommandResponse, signature)

await sdk.ledger.execute(signed, { partyId: sender.partyId })

logger.info('Ping command submitted with offline signing')

const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
    sender.partyId,
    '10000'
)

const result = await sdk.ledger
    .prepare({
        partyId: sender.partyId,
        commands: amuletTapCommand,
        disclosedContracts: amuletTapDisclosedContracts,
    })
    .sign(senderKeys.privateKey)
    .execute({ partyId: sender.partyId })

const senderUtxos = await sdk.token.utxos.list({ partyId: sender.partyId })

const tapTransaction = await sdk.token.transactionsById({
    updateId: result.updateId,
    partyId: sender.partyId,
})

const mintEvent = tapTransaction.events.find(
    (tokenStandardEvent) =>
        tokenStandardEvent.label.type === 'Mint' &&
        tokenStandardEvent.unlockedHoldingsChange.creates.find(
            (h) => h.amount === '10000.0000000000'
        )
)

if (mintEvent) {
    logger.info('Found token standard event with type Mint')
} else {
    throw new Error(`Couldn't find tap transaction by updateId`)
}
const senderAmuletUtxos = senderUtxos.filter((utxo) => {
    return (
        utxo.interfaceViewValue.amount === '10000.0000000000' &&
        utxo.interfaceViewValue.instrumentId.id === 'Amulet'
    )
})

if (senderAmuletUtxos.length === 0) {
    throw new Error('No UTXOs found for Sender')
}

logger.info('Tap command for Amulet for Sender submitted and UTXO received')
```

## Creating a Command

Commands are the intents of an user on the validator, there are two kinds of commands: `CreateCommand` and `ExerciseCommand`.

The `CreateCommand` is used to create a new implementation of a template with the given arguments and can result in one or more new contracts being created. The `ExerciseCommand` takes an existing contract and exercises a choice on it, which also can result in new contracts being created.

In the Canton Network, it is often necessary to need to include input data when creating commands which needs to be read from the ledger. For example, which UTXOs to include in a transfer. This is private data which you read from your own node. It's also often necessary to include contextual information in a transfer. For example, information about a particular asset which you don't get from your own node - you get from an API provided by the asset issuer. See [here](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md) for more information.

The general process for forming a transaction is:

1. Call your own node's RPC to get the current ledger end (think “latest block”)
2. Call your own node's RPC to get relevant private data at ledger end (e.g. wallet's holdings)
3. Call app/token specific APIs to get context information (e.g. mining round contracts)
4. Assemble the data into the full command using the OpenAPI/JSON or gRPC schemas.

In the examples below, the SDK example uses the Token Standards inside the a validator to create a simple transfer command. The transfer command is sent to a recipient party who can then exercise `accept` or `reject` on the created contract (thereby archiving it). In the cURL example, we show the steps above gaining information from a validator and context information from the Canton Coin scan API.

The Wallet SDK allow us to build such a command easily:

<div className="tabs">
  <div className="tab">
    SDK

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

    export default async function () {
        // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
        const sdk = await SDK.create({
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
            ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
            token: global.TOKEN_NAMESPACE_CONFIG,
        })

        const sender = global.EXISTING_PARTY_1
        const receiver = global.EXISTING_PARTY_2

        const utxos = await sdk.token.utxos.list({ partyId: sender })

        const utxosToUse = utxos.filter((t) => t.interfaceViewValue.amount != '50') //we filter out the 50, since we want to send 125

        await sdk.token.transfer.create({
            sender,
            recipient: receiver,
            amount: '2000',
            instrumentId: 'Amulet',
            registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            inputUtxos: utxosToUse.map((t) => t.contractId),
        })
    }
    ```
  </div>

  <div className="tab">
    cURL

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # In the examples below, replace the following with your own values: "YOUR_NODE_JSON_API", "OFFSET_FROM_1", "WALLET_ID", "YOUR_CHOICE_OF_INPUT_CIDs",
    # "SENDER_PARTY_ID", "RECEIVER_PARTY_ID"

    # 1. Call your own node’s RPC to get the latest offset / ledger end
    curl -X GET http://YOUR_NODE_JSON_API/v2/state/ledger-end

    # 2. Get the contract ID of an active Amulet contract via
    curl -X POST http://YOUR_NODE_JSON_API/v2/state/active-contracts -d 
    '{  "verbose" : true, 
        "activeAtOffset": OFFSET_FROM_1, 
        "filter" : {
            "filtersByParty" : {
                "WALLET_ID" : {
                    "cumulative":  
                        [{"identifierFilter": {
                            "InterfaceFilter": {
                                "value": {
                                    "includeInterfaceView":true,
                                    "includeCreatedEventBlob": false, 
                                    "interfaceId": "#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding"}}}}]}}}}'

    # 3. Get context information for Canton Coin
        #3. a) the Registry admin party id:
    curl -X GET https://scan.sv-1.global.canton.network.sync.global/registry/metadata/v1/info
    # Example output:
    # {"adminId":"DSO::1220b143…","supportedApis":{"splice-api-token-metadata-v1":1}}

        # 3. b) the instrument ID:
    curl -X GET https://scan.sv-1.global.canton.network.sync.global/registry/metadata/v1/instruments
    # Example output:
    # "instrumentId" : {
    #   "admin" : "DSO::1220b1431ef217342db44d516bb9befde802be7d8899637d290895fa58880f19accc",
    #   "id" : "Amulet"}

        # 3. c) Get the TransferFactory and context from the asset admin:
    curl -X POST -H "Content-Type: application/json" https://scan.sv-1.dev.global.canton.network.sync.global/registry/transfer-instruction/v1/transfer-factory -d '{
    "choiceArguments" : {
      "expectedAdmin" : "DSO::1220be58c29e65de40bf273be1dc2b266d43a9a002ea5b18955aeef7aac881bb471a",
      "transfer" : {
        "sender" : "SENDER_PARTY_ID",
        "receiver" : "RECEIVER_PARTY_ID",
        "amount" : "1000.0",
        "instrumentId" : {
          "admin" : "DSO::1220be58c29e65de40bf273be1dc2b266d43a9a002ea5b18955aeef7aac881bb471a",
          "id" : "Amulet"
        },
        "requestedAt" : "2025-07-11T12:45:00Z",
        "executeBefore" : "2025-07-12T12:45:00Z",
        "inputHoldingCids" : [
          "YOUR_CHOICE_OF_INPUT_CIDs"
        ],
        "meta" : { "values" : {} }
      },
      "extraArgs" : {
        "context": { "values" : {} },
        "meta" : { "values" : {} }
      }
        }
      }'
    # Example output:
    # {
    #   "factoryId": "009f00e5bf0…", – ContractId of the transferfactory to use
    #   "transferKind": "direct", – type of transfer - see pre-approvals for more information
    #   "choiceContext": { … }, – data to stick in the extra arguments
    #   "disclosedContracts": [ … ] – any admin-private contracts on chain needed for preparation
    # }

    # 4. The information obtained can be used to construct the transfer and transaction in the prepare step:
    #
    # Transfer:
    #   "transfer" : {
    #     "sender" : "SENDER_PARTY_ID",
    #     "receiver" : "RECEIVER_PARTY_ID",
    #     "amount" : "1000.0",
    #     "instrumentId" : {
    #       "admin" : "DSO::1220b1431ef217342db44d516bb9befde802be7d8899637d290895fa58880f19accc",
    #       "id" : "Amulet"
    #     },
    #     "requestedAt" : "2025-08-11T12:45:00Z",
    #     "executeBefore" : "2025-08-12T12:45:00Z",
    #     "inputHoldingCids" : [
    #   "YOUR_CHOICE_OF_INPUT_CIDs"
    #     ],
    #     "meta" : { "values" : {} }
    #   }
    ```
  </div>
</div>

## Preparing the Transaction

Now that we have a command we need to prepare the transaction by calling a node's RPC API which will return an unsigned transaction. It must be a validator which hosts the party initiating the transaction as private information is needed to construct the transaction. This is unlike other chains where you construct the transaction fully offline using an SDK. A transaction is a collection of commands that are atomic, meaning that either all commands succeed or none of them do.

Note: contractId's are pinned as part of prepare step, the execution of the transfer will only go succeed if the contractId's haven't been archived between preparation and execution steps.

To prepare a transaction we need to send the commands to the ledger.

<div className="tabs">
  <div className="tab">
    SDK

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

    export default async function () {
        const sdk = await SDK.create({
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
            ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
            token: global.TOKEN_NAMESPACE_CONFIG,
        })

        const sender = global.EXISTING_PARTY_1
        const receiver = global.EXISTING_PARTY_2

        const [transferCommand, disclosedContracts] =
            await sdk.token.transfer.create({
                sender,
                recipient: receiver,
                amount: '2000',
                instrumentId: 'Amulet',
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        sdk.ledger.prepare({
            partyId: sender,
            commands: transferCommand,
            disclosedContracts,
        })
    }
    ```
  </div>

  <div className="tab">
    cURL

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # In the example below, replace the values with your own

    # PrepareTransaction call with all the inputs gathered.
     curl -X POST http://YOUR_NODE_JSON_API/v2/interactive-submission/prepare -d {
        "userId" : "USER_ID",
        "commandId" : "curl-transfer-test",
        "actAs" : ["SENDER_PARTY_ID"],
        "readAs" : [],
        "synchronizerId": "global-domain::1220be58c29e65de40bf273be1dc2b266d43a9a002ea5b18955aeef7aac881bb471a",
        "verboseHashing": false,
        "packageIdSelectionPreference" : [],
        "commands" : [ {
          "ExerciseCommand" : {
            "templateId" : "#splice-api-token-transfer-instruction-v1:Splice.Api.Token.TransferInstructionV1:TransferFactory",
            "contractId" : "009f00e5bf0…",
            "choice" : "TransferFactory_Transfer",
            "choiceArgument" : { 
              ... ,
              "extraArgs" : {
                "context": { ... },
                ...
              }
            }
          }
        } ],
        "disclosedContracts" : [ … ]
      }
    ```
  </div>
</div>

The return type is an unsigned transaction if the combination of the commands are possible, otherwise an error is returned. The transaction can then be visualised and signed by the party.

## Validating the Transaction

The result from the prepare step is an encoded protobuf message and easily decoded and inspected to go through a policy engine, for example. The transaction is returned alongside with the hash that needs to be signed. If the validator is not controlled by you, then it might be a good idea to validate that the transaction is what you expect it to be. You can use the Wallet SDK to visualize the transaction as described in the Visualizing a transaction section.

On top of visualizing the transaction, it's also important to compute the transaction hash yourself and confirm that it matches the hash of the transaction provided by the validator from the prepare step.

The hash can be computed using the Wallet SDK:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    const transaction = global.PREPARED_TRANSACTION
    if (!transaction.preparedTransaction) {
        throw Error('Prepared tx not found')
    }

    const calculatedTxHash = await sdk.utils.hash.preparedTransacation(
        transaction.preparedTransaction
    )
    const hex = calculatedTxHash.toHex()
    const base64 = calculatedTxHash.toBase64()

    if (base64 !== transaction.preparedTransactionHash)
        throw Error('Incorrect hash calculated')
}
```

You can then compare the `hash` with the `transaction.preparedTransactionHash` to ensure they match.

## Signing the Transaction

Once the transaction is validated, the hash retrieved from the prepare step can be signed using the private key of the party.

Below shows an example in the Wallet SDK and using cURL commands:

<div className="tabs">
  <div className="tab">
    SDK

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import {
        SDK,
        localNetStaticConfig,
        signTransactionHash,
    } from '@canton-network/wallet-sdk'

    export default async function () {
        const sdk = await SDK.create({
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
            ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        })
        const keys = sdk.keys.generate()

        const preparedParty = EXISTING_TOPOLOGY

        //This signing function works for a party topology hash or a transaction hash
        signTransactionHash(preparedParty.multiHash, keys.privateKey)
    }
    ```
  </div>

  <div className="tab">
    cURL

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # In this example the hash is signed using openssl and "PREPARE_TRANSACTION_RESPONSE.json" is the JSON output from the prepare 
    # transaction step is here. "PRIVATE_KEY_FILE" should be the private key of the namespace of the external party. For more information
    # on the openssl commands to generate the key see here:

    TRANSACTION_HASH=$(cat create_ping_prepare_response.json | jq -r .prepared_transaction_hash)
    PREPARED_TRANSACTION=$(cat create_ping_prepare_response.json | jq -r .prepared_transaction)
    SIGNATURE=$(echo -n "$TRANSACTION_HASH" | base64 --decode | openssl pkeyutl -rawin -inkey "PRIVATE_KEY_FILE" -keyform DER -sign | openssl base64 -e -A)
    ```
  </div>
</div>

## Submitting the Transaction

Once the transaction is signed, it can be executed on the validator. You can observe completions by seeing the committed transactions. If they don't appear on your ledger, you are guaranteed some response, and you can keep retrying; signed transactions are idempotent. Finality usually takes 3-10s.

<div className="tabs">
  <div className="tab">
    SDK

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import {
        SDK,
        localNetStaticConfig,
        signTransactionHash,
    } from '@canton-network/wallet-sdk'
    import { v4 } from 'uuid'

    export default async function () {
        const sdk = await SDK.create({
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
            ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        })
        const myParty = global.EXISTING_PARTY_1
        const keys = global.EXISTING_PARTY_1_KEYS

        const pingCommand = [
            {
                CreateCommand: {
                    templateId:
                        '#canton-builtin-admin-workflow-ping:Canton.Internal.Ping:Ping',
                    createArguments: {
                        id: v4(),
                        initiator: myParty,
                        responder: myParty,
                    },
                },
            },
        ]

        const preparedPingCommand = sdk.ledger.prepare({
            partyId: myParty,
            commands: pingCommand,
            disclosedContracts: [],
        })

        const { response: preparedPingCommandResponse } =
            await preparedPingCommand.toJSON()

        const signature = signTransactionHash(
            preparedPingCommandResponse.preparedTransactionHash,
            keys.privateKey
        )

        const signed = sdk.ledger.fromSignature(
            preparedPingCommandResponse,
            signature
        )
        await sdk.ledger.execute(signed, { partyId: myParty })
    }
    ```
  </div>

  <div className="tab">
    cURL

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl http://localhost:7575/v2/interactive-submission/execute -d {
        "preparedTransaction": "$PREPARED_TRANSACTION",
        "hashingSchemeVersion": "HASHING_SCHEME_VERSION_V2",
        "userId": "USER_ID",
        "submissionId": "51dd5a0e-2ab6-4ca4-aa9d-9333fb603eb0",
        "deduplicationPeriod": {
            "Empty": {}
        },
        "partySignatures": {
            "signatures": [
                {
                    "party": "PARTY_ID",
                    "signatures": [
                    {
                        "format": "SIGNATURE_FORMAT_CONCAT",
                        "signature": "$SIGNATURE",
                        "signingAlgorithmSpec": "SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256",
                        "signedBy": "FINGERPRINT"
                    }
                    ]
                }
            ]
        }
    }
    ```
  </div>
</div>

## Observing the Transaction

The `execute` method in the `ledger`` namespace will execute the submission and wait for a response. THs returns an \`updateId`and`completionOffset\`. Additionally, you can continuously monitor holdings changes using token standard history parser.

## How to use the SDK to Offline sign a Transaction

The SDK exposes functionality that can be used in an offline environment to sign and validate transactions the below script shows an entire interaction between `Alice` and `Bob` with signing happening in an offline environment and online environment that performs the prepare and submit.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    localNetStaticConfig,
    SDK,
    signTransactionHash,
} from '@canton-network/wallet-sdk'
import { pino } from 'pino'
import {
    TOKEN_NAMESPACE_CONFIG,
    TOKEN_PROVIDER_CONFIG_DEFAULT,
    AMULET_NAMESPACE_CONFIG,
} from './utils/index.js'

const onlineLogger = pino({ name: '14-online-localnet', level: 'info' })
const offlineLogger = pino({ name: '14-oggline-localnet', level: 'info' })

const onlineSDK = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    amulet: AMULET_NAMESPACE_CONFIG,
    token: TOKEN_NAMESPACE_CONFIG,
})

onlineLogger.info(`Online sdk initialized.`)

const offlineSdk = SDK.createOffline()

offlineLogger.info(`Offline sdk initialized.`)

offlineLogger.info(
    '===================== OFFLINE CREATED KEYS SENDER ====================='
)

const keyPairSender = offlineSdk.keys.generate()

onlineLogger.info(
    '===================== ONLINE CREATED TOPOLOGY TRANSACTIONS SENDER ====================='
)

const senderPartyPrepared = onlineSDK.party.external.create(
    keyPairSender.publicKey,
    {
        partyHint: 'v1-14-alice',
    }
)

const senderPartyTopology = await senderPartyPrepared.topology()

onlineLogger.info(
    `Prepared sender onboarding with multi hash: ${senderPartyTopology.multiHash}`
)

offlineLogger.info(
    '===================== OFFLINE TOPOLOGY TX HASHING SENDER ====================='
)

const senderTopologyTxCalculated =
    await offlineSdk.utils.hash.topologyTransaction(
        senderPartyTopology.topologyTransactions
    )

if (senderTopologyTxCalculated !== senderPartyTopology.multiHash)
    throw Error(
        'Recomputed sender topology hash does not match received sender multihash'
    )

const senderSignedTopologyTx = signTransactionHash(
    senderPartyTopology.multiHash,
    keyPairSender.privateKey
)

offlineLogger.info(`Sender signed onboarding hash`)

onlineLogger.info(
    '===================== ONLINE EXECUTE TOPOLOGY TX SENDER ====================='
)

const senderParty = await senderPartyPrepared.execute(senderSignedTopologyTx)

onlineLogger.info(`Created sender party: ${senderParty}`)

offlineLogger.info(
    '===================== OFFLINE GENERATE KEYS RECEIVER ====================='
)

const keyPairReceiver = offlineSdk.keys.generate()

offlineLogger.info('Created sender keyPair')

onlineLogger.info(
    '===================== ONLINE CREATED TOPOLOGY TRANSACTIONS RECEIVER ====================='
)

const receiverPartyPrepared = onlineSDK.party.external.create(
    keyPairReceiver.publicKey,
    {
        partyHint: 'v1-14-bob',
    }
)

const receiverPartyTopology = await receiverPartyPrepared.topology()

onlineLogger.info(
    `Prepared sender onboarding with multi hash: ${receiverPartyTopology.multiHash}`
)

offlineLogger.info(
    '===================== OFFLINE COMPUTE MULTIHASH FROM TOPOLOGY TX RECEIVER ====================='
)

const receiverTopologyHashCalculated =
    await offlineSdk.utils.hash.topologyTransaction(
        receiverPartyTopology.topologyTransactions
    )

if (receiverTopologyHashCalculated !== receiverPartyTopology.multiHash)
    throw Error(
        'Recomputed receiver topology hash does not match received multihash'
    )

const receiverSignedTopologyTx = signTransactionHash(
    receiverPartyTopology.multiHash,
    keyPairReceiver.privateKey
)

offlineLogger.info(`Receiver signed onboarding hash`)

onlineLogger.info(
    '===================== ONLINE EXECUTE TOPOLOGY TX FOR RECEIVER ====================='
)

const receiverParty = await receiverPartyPrepared.execute(
    receiverSignedTopologyTx
)

onlineLogger.info(`Created receiver party: ${receiverParty}`)

// Configure amulet namespace for online sdk

onlineLogger.info(
    '===================== ONLINE SENDER TAP (PREPARE) ====================='
)

const [amuletTapCommand, amuletTapDisclosedContracts] =
    await onlineSDK.amulet.tap(senderParty.partyId, '10000')

const { response: preparedTapCommandResponse } = await onlineSDK.ledger
    .prepare({
        partyId: senderParty.partyId,
        commands: amuletTapCommand,
        disclosedContracts: amuletTapDisclosedContracts,
    })
    .toJSON()

onlineLogger.info(
    `Prepared tap with hash: ${preparedTapCommandResponse.preparedTransactionHash}`
)

offlineLogger.info(
    '===================== OFFLINE TAP SIGNING AND HASH RECOMPUTATION ====================='
)
const calculatedTxHash = await offlineSdk.utils.hash.preparedTransacation(
    preparedTapCommandResponse.preparedTransaction
)

if (
    calculatedTxHash.toBase64() !==
    preparedTapCommandResponse.preparedTransactionHash
)
    throw Error('Recomputed tap hash does not match prepared tap hash')

const signatureTapCommand = signTransactionHash(
    preparedTapCommandResponse.preparedTransactionHash,
    keyPairSender.privateKey
)
offlineLogger.info('Signed tap transaction hash')

const signed = onlineSDK.ledger.fromSignature(
    preparedTapCommandResponse,
    signatureTapCommand
)

onlineLogger.info(
    '===================== ONLINE EXECUTE TAP COMMAND SENDER ====================='
)

await onlineSDK.ledger.execute(signed, { partyId: senderParty.partyId })

onlineLogger.info('Tap completed')

//creating a transfer
onlineLogger.info(
    '===================== ONLINE SENDER TRANSFER (PREPARE) ====================='
)

const [transferCommand, transferDisclosedContracts] =
    await onlineSDK.token.transfer.create({
        sender: senderParty.partyId,
        recipient: receiverParty.partyId,
        instrumentId: 'Amulet',
        registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
        amount: '100',
    })

const { response: preparedTransferResponse } = await onlineSDK.ledger
    .prepare({
        partyId: senderParty.partyId,
        commands: transferCommand,
        disclosedContracts: transferDisclosedContracts,
    })
    .toJSON()

offlineLogger.info(
    '===================== OFFLINE TRANSFER SIGNING AND HASH RECOMPUTATION ====================='
)

onlineLogger.info(
    `Prepared create transfer with hash: ${preparedTransferResponse.preparedTransactionHash}`
)

const calculatedCreateTransferHash =
    await offlineSdk.utils.hash.preparedTransacation(
        preparedTransferResponse.preparedTransaction
    )

if (
    calculatedCreateTransferHash.toBase64() !==
    preparedTransferResponse.preparedTransactionHash
)
    throw Error(
        'Recomputed create transfer hash does not match prepared create transfer hash'
    )

const signatureTransferCommand = signTransactionHash(
    preparedTransferResponse.preparedTransactionHash,
    keyPairSender.privateKey
)
offlineLogger.info('Signed create transfer transaction hash')

const signedTransferHash = onlineSDK.ledger.fromSignature(
    preparedTransferResponse,
    signatureTransferCommand
)

onlineLogger.info(
    '====================== SUBMITTING TRANSFER ====================='
)

await onlineSDK.ledger.execute(signedTransferHash, {
    partyId: senderParty.partyId,
})

onlineLogger.info(
    `Created a transfer from ${senderParty.partyId} to ${receiverParty.partyId}`
)

onlineLogger.info(
    '===================== ONLINE ACCEPT TRANSFER (PREPARE) ====================='
)

const pendingOffers = await onlineSDK.token.transfer.pending(
    receiverParty.partyId
)

if (pendingOffers?.length !== 1) {
    throw new Error(
        `Expected exactly one pending transfer instruction, but found ${pendingOffers?.length}`
    )
}

onlineLogger.info(`Found pending offer: ${pendingOffers[0].contractId}`)

const pendingOffer = pendingOffers[0]

const [acceptTransferCommand, transferDisclosedContractsAccept] =
    await onlineSDK.token.transfer.accept({
        transferInstructionCid: pendingOffer.contractId,
        registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
    })

const { response: preparedTransferAcceptResponse } = await onlineSDK.ledger
    .prepare({
        partyId: receiverParty.partyId,
        commands: acceptTransferCommand,
        disclosedContracts: transferDisclosedContractsAccept,
    })
    .toJSON()

onlineLogger.info(
    `Prepared create transfer with hash: ${preparedTransferAcceptResponse.preparedTransactionHash}`
)

offlineLogger.info(
    '===================== OFFLINE CALCULATE TX HASH AND SIGNING FOR ACCEPT TRANSFER ====================='
)

const calculatedAcceptTransferHash =
    await offlineSdk.utils.hash.preparedTransacation(
        preparedTransferAcceptResponse.preparedTransaction
    )

if (
    calculatedAcceptTransferHash.toBase64() !==
    preparedTransferAcceptResponse.preparedTransactionHash
)
    throw Error(
        'Recomputed accept transfer hash does not match prepared accept transfer hash'
    )

const signatureAcceptTransfer = signTransactionHash(
    preparedTransferAcceptResponse.preparedTransactionHash,
    keyPairReceiver.privateKey
)
offlineLogger.info('Signed accept transfer transaction hash')

const signedAcceptTransferHash = onlineSDK.ledger.fromSignature(
    preparedTransferAcceptResponse,
    signatureAcceptTransfer
)

onlineLogger.info(
    '===================== ONLINE SUBMITTING ACCEPT ====================='
)

await onlineSDK.ledger.execute(signedAcceptTransferHash, {
    partyId: receiverParty.partyId,
})

onlineLogger.info('Accepted transfer instruction')
```

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/signing-transactions-from-dapps/index.rst" hash="6593e378" */}

# Signing Transactions from third party dApps

A normal flow on blockchain applications is to have dApps that interact with the blockchain on the clients behalf, these flows usually require the user to sign transactions that the dApp prepares and submit it. To faciliate this in Canton it is required that the prepared transaction is sent to the wallet for signing. An easy way of supporting this is to expose a dApp API (OpenRPC spec can be found here: [https://github.com/canton-network/wallet/blob/main/api-specs/openrpc-dapp-api.json](https://github.com/canton-network/wallet/blob/main/api-specs/openrpc-dapp-api.json) ).

*The specs are in OpenRPC to conform with traditional standards like for ethereum.*

A client can provide access to a Wallet Providers dApp API by either embedding a wallet provider in the dApp or by connecting to an external wallet provider via a browser extension or other means. Then the dApp is able to funnel transactions through to the wallet provider for signing.

## Receiving a Transaction

A dApp would usually call the `prepareExecute` endpoint or the `prepareExecuteAndWait` endpoint. In both cases the Wallet Provider would prepare, sign and submit the transaction to the ledger.

You can prepare the incoming transaction using the Wallet SDK:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    const preparedCommand = global.PREPARED_COMMAND

    const myParty = global.EXISTING_PARTY_2

    sdk.ledger.prepare({
        partyId: myParty,
        commands: preparedCommand,
    })
}
```

## Reading and Visualising the Transaction

It is important when integrating with third party dApps to showcase the User exactly what is being signed. Once the signature is applied the transaction can be considered valid (and executed). The easiest would be to create a visualizer that takes a JSON representation of the transaction. The Json for a prepared transaction (before signature is applied) can be obtained using the Wallet SDK:

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/token-standard/index.rst" hash="3c8d8496" */}

# Token Standard

The Wallet SDK support performing basic token standard operations, these are exposed through the `sdk.tokenStandard` a complete overview of the underlying integration can be found [here](/appdev/deep-dives/token-standard) and the CIP is defined [here](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md).

## How do i quickly perform a transfer between two parties?

The below performs a 2-step transfer between Alice and Bob and expose their holdings:

<div className="tabs">
  <div className="tab">
    Creating a transfer

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
    import { pino } from 'pino'
    import _accept from './_accept.js'
    import { TransferTestScriptParameters } from './types.js'
    import _reject from './_reject.js'
    import _withdraw from './_withdraw.js'
    import _expire from './_expire.js'
    import {
        TOKEN_NAMESPACE_CONFIG,
        TOKEN_PROVIDER_CONFIG_DEFAULT,
        AMULET_NAMESPACE_CONFIG,
    } from '../utils/index.js'

    const logger = pino({ name: 'v1-02-two-step-transfer', level: 'info' })

    const sdk = await SDK.create({
        auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: TOKEN_NAMESPACE_CONFIG,
        amulet: AMULET_NAMESPACE_CONFIG,
    })

    const senderKeys = sdk.keys.generate()

    const sender = await sdk.party.external
        .create(senderKeys.publicKey, {
            partyHint: 'v1-02-alice',
        })
        .sign(senderKeys.privateKey)
        .execute()

    const receiverKeys = sdk.keys.generate()

    const receiver = await sdk.party.external
        .create(receiverKeys.publicKey, {
            partyHint: 'v1-02-bob',
        })
        .sign(receiverKeys.privateKey)
        .execute()

    const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
        sender.partyId,
        '10000'
    )

    await sdk.ledger
        .prepare({
            partyId: sender.partyId,
            commands: amuletTapCommand,
            disclosedContracts: amuletTapDisclosedContracts,
        })
        .sign(senderKeys.privateKey)
        .execute({ partyId: sender.partyId })

    const senderUtxos = await sdk.token.utxos.list({ partyId: sender.partyId })

    const senderAmuletUtxos = senderUtxos.filter((utxo) => {
        return (
            utxo.interfaceViewValue.amount === '10000.0000000000' &&
            utxo.interfaceViewValue.instrumentId.id === 'Amulet'
        )
    })

    if (senderAmuletUtxos.length === 0) {
        throw new Error('No UTXOs found for Sender')
    }

    const transferTestScriptParameters: TransferTestScriptParameters = {
        sdk,
        sender,
        senderKeys,
        receiver,
        receiverKeys,
        logger,
    }

    await _accept(transferTestScriptParameters)

    await _reject(transferTestScriptParameters)

    await _withdraw(transferTestScriptParameters)

    await _expire(transferTestScriptParameters)
    ```
  </div>

  <div className="tab">
    Accepting a transfer

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { localNetStaticConfig } from '@canton-network/wallet-sdk'
    import { TransferTestScriptParameters } from './types.js'

    export default async (args: TransferTestScriptParameters) => {
        const { sdk, sender, receiver, senderKeys, receiverKeys, logger } = args

        const [transferCommand, transferDisclosedContracts] =
            await sdk.token.transfer.create({
                sender: sender.partyId,
                recipient: receiver.partyId,
                instrumentId: 'Amulet',
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
                amount: '2000',
            })

        logger.info('Transfer command created, ready for signing and execution')

        await sdk.ledger
            .prepare({
                partyId: sender.partyId,
                commands: transferCommand,
                disclosedContracts: transferDisclosedContracts,
            })
            .sign(senderKeys.privateKey)
            .execute({ partyId: sender.partyId })

        logger.info(
            { sender, receiver },
            'Submitted transfer command from Sender to Receiver'
        )
        const receiverPendingTransfers = await sdk.token.transfer.pending(
            receiver.partyId
        )
        logger.info(
            receiverPendingTransfers,
            'Receiver pending transfer instructions'
        )

        const [acceptCommand, acceptDisclosedContracts] =
            await sdk.token.transfer.accept({
                transferInstructionCid: receiverPendingTransfers[0].contractId,
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        await sdk.ledger
            .prepare({
                partyId: receiver.partyId,
                commands: acceptCommand,
                disclosedContracts: acceptDisclosedContracts,
            })
            .sign(receiverKeys.privateKey)
            .execute({ partyId: receiver.partyId })
        logger.info('Receiver accepted the transfer instruction')

        const receiverUtxos = await sdk.token.utxos.list({
            partyId: receiver.partyId,
        })
        logger.info(
            receiverUtxos,
            'Receiver UTXOs after accepting transfer instruction'
        )

        const receiverAmuletUtxos = receiverUtxos.filter((utxo) => {
            return (
                utxo.interfaceViewValue.amount === '2000.0000000000' &&
                utxo.interfaceViewValue.instrumentId.id === 'Amulet'
            )
        })

        if (receiverAmuletUtxos.length === 0) {
            throw new Error(
                'No Amulet UTXOs found for Receiver after accepting transfer instruction'
            )
        }

        logger.info('Two step transfer process completed successfully')
    }
    ```
  </div>

  <div className="tab">
    Rejecting a transfer

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { localNetStaticConfig } from '@canton-network/wallet-sdk'
    import { TransferTestScriptParameters } from './types.js'

    export default async (args: TransferTestScriptParameters) => {
        const { sdk, receiver, sender, senderKeys, receiverKeys, logger } = args

        const [transferCommand, transferDisclosedContracts] =
            await sdk.token.transfer.create({
                sender: sender.partyId,
                recipient: receiver.partyId,
                instrumentId: 'Amulet',
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
                amount: '2000',
            })

        logger.info('Transfer command created, ready for signing and execution')

        await sdk.ledger
            .prepare({
                partyId: sender.partyId,
                commands: transferCommand,
                disclosedContracts: transferDisclosedContracts,
            })
            .sign(senderKeys.privateKey)
            .execute({ partyId: sender.partyId })

        logger.info(
            { sender, receiver },
            'Submitted transfer command from Sender to Receiver'
        )

        const pendingTransfer = await sdk.token.transfer.pending(receiver.partyId)

        if (!pendingTransfer.length) throw Error('pendingTransfer is empty')

        const [rejectCommand, rejectDisclosedContracts] =
            await sdk.token.transfer.reject({
                transferInstructionCid: pendingTransfer[0].contractId,
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        await sdk.ledger
            .prepare({
                partyId: receiver.partyId,
                commands: rejectCommand,
                disclosedContracts: rejectDisclosedContracts,
            })
            .sign(receiverKeys.privateKey)
            .execute({
                partyId: receiver.partyId,
            })

        const pendingTransferAfterReject = await sdk.token.transfer.pending(
            receiver.partyId
        )
        if (pendingTransferAfterReject.length)
            throw Error('pendingTransferAfterReject is not empty')

        logger.info('Successfully rejected the submitted transfer')
    }
    ```
  </div>

  <div className="tab">
    Withdrawing a transfer

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    import { localNetStaticConfig } from '@canton-network/wallet-sdk'
    import { TransferTestScriptParameters } from './types.js'

    export default async (args: TransferTestScriptParameters) => {
        const { sdk, receiver, sender, senderKeys, logger } = args

        const [transferCommand, transferDisclosedContracts] =
            await sdk.token.transfer.create({
                sender: sender.partyId,
                recipient: receiver.partyId,
                instrumentId: 'Amulet',
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
                amount: '2000',
            })

        logger.info('Transfer command created, ready for signing and execution')

        await sdk.ledger
            .prepare({
                partyId: sender.partyId,
                commands: transferCommand,
                disclosedContracts: transferDisclosedContracts,
            })
            .sign(senderKeys.privateKey)
            .execute({ partyId: sender.partyId })

        logger.info(
            { sender, receiver },
            'Submitted transfer command from Sender to Receiver'
        )

        const pendingTransfer = await sdk.token.transfer.pending(receiver.partyId)

        if (!pendingTransfer.length) throw Error('pendingTransfer is empty')

        const [withdrawCommand, withdrawDisclosedContracts] =
            await sdk.token.transfer.withdraw({
                transferInstructionCid: pendingTransfer[0].contractId,
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        await sdk.ledger
            .prepare({
                partyId: sender.partyId,
                commands: withdrawCommand,
                disclosedContracts: withdrawDisclosedContracts,
            })
            .sign(senderKeys.privateKey)
            .execute({
                partyId: sender.partyId,
            })

        const pendingTransferAfterWithdraw = await sdk.token.transfer.pending(
            receiver.partyId
        )
        if (pendingTransferAfterWithdraw.length)
            throw Error('pendingTransferAfterWithdraw is not empty')

        logger.info('Successfully withdrawn the submitted transfer')
    }
    ```
  </div>
</div>

## Listing holdings (UTXO's)

Canton uses created and archived events to determine the state of the ledger. This correlates to how UTXO's are handled on other blockchains like Bitcoin. This means that at any point in time you can retrieve all your active contracts with the interface 'Holding' to see all assets you posses across different instruments.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const myParty = global.EXISTING_PARTY_1

    await sdk.token.utxos.list({ partyId: myParty })
}
```

the above script can safely be used to determine used in a transfer, if you provide no boolean value or true then you need to filter out the locked ones manually.

## Listing holding transactions

In order to stream transaction events as they happen on ledger the `listHoldingTransactions` endpoint can be used. This takes two ledger offset and gives an overview of all token standard transactions that have happened between. It also returns a `nextOffset` that can be used when calling the endpoint again. This will allow you to easily ensure you do not receive any transaction twice and you are only querying the transactions that have happened after.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })
    const myParty = global.EXISTING_PARTY_1

    await sdk.token.holdings({ partyId: myParty })
}
```

to quickly convert the stream into deposit and withdrawal you can use this function:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function convertToTransaction(pt: Transaction, associatedParty: string): object[] {
    return pt.events.flatMap((event) => {
        if (event.label.type === 'TransferIn') {
            return [{
                updateId: pt.updateId,
                recordTime: pt.recordTime,
                from: event.label.sender,
                to: associatedParty,
                amount: Number(event.unlockedHoldingsChangeSummary.amountChange),
                instrumentId: 'Amulet', //hardcoded instrumentId from local net
                fee: Number(event.label.burnAmount),
                memo: event.label.reason,
            }];
        } else if (event.label.type === 'TransferOut') {
            const label = event.label
            return event.label.receiverAmounts.map((receiverAmount: any) => ({
                updateId: pt.updateId,
                recordTime: pt.recordTime,
                from: associatedParty,
                to: receiverAmount.receiver,
                amount: Number(receiverAmount.amount),
                instrumentId: 'Amulet', //hardcoded instrumentId from local net
                fee: Number(label.burnAmount),
                memo: label.meta.reason,
            }));
        } else {
            return [];
        }
    });
}
```

## Performing a Tap on DevNet or LocalNet

When writing scripts and setup it is important to have funds present, this can be very tedious on blockchains. Therefor most blockchains support some form of a faucet (that allows to receive a small amount of funds to play with). On canton we allow the `tap` method that is only present on DevNet (or LocalNet), by using this you can stock funds to easily attempt some of the CC transfer flows:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        amulet: global.AMULET_NAMESPACE_CONFIG,
    })

    const myParty = global.EXISTING_PARTY_1

    await sdk.amulet.tap(myParty, '2000')
}
```

this is an important pre-requisite for the creating of transfer in your script.

## Creating a transfer

In order to create a simple transfer you can use the `createTransfer` on the token standard. Then like any other operation you can use the `prepareSubmission` endpoint, sign the returned hash and finally `executeSubmission`.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const sender = global.EXISTING_PARTY_1
    const receiver = global.EXISTING_PARTY_2

    const utxos = await sdk.token.utxos.list({ partyId: sender })

    const utxosToUse = utxos.filter((t) => t.interfaceViewValue.amount != '50') //we filter out the 50, since we want to send 125

    await sdk.token.transfer.create({
        sender,
        recipient: receiver,
        amount: '2000',
        instrumentId: 'Amulet',
        registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
        inputUtxos: utxosToUse.map((t) => t.contractId),
    })
}
```

## UTXO management and locked funds

The default script for creating a transfer above uses automated utxo selection, the automatic being to simply select all utxo's. In a more professional way, you would want to carefully pick which utxo's you would like to use as input for your transfers, alongside you might also want to define a custom expiration time for when the transaction should automatically expire.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const sender = global.EXISTING_PARTY_1
    const receiver = global.EXISTING_PARTY_2

    await sdk.token.transfer.create({
        sender,
        recipient: receiver,
        amount: '2000',
        instrumentId: 'Amulet',
        registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
    })
}
```

if we call `sdk.token.utxos.list({partyId})` or `sdk.token.utxos.list({partyId, includeLocked: false})` then it will show 1 utxo of 50 (then one we excluded). This defaults to filtering out the locked utxos.

if we call `sdk.token.utxos.list({partyId, includeLocked: true})` then it will show all 3 utxos (100 and 25 both will have a lock).

## 2-step transfer vs 1-step transfer

The default behavior for all tokens are a 2-step transfer, this matches how funds are usually transferred in TradFi, however this is counter-intuitive in the blockchain world. Canton Coin supports setting up a "Transfer Pre-approval", this allows a party to designate that he wants to auto-accept all incoming transfer, giving a similar behavior of the blockchain world.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        amulet: global.AMULET_NAMESPACE_CONFIG,
    })

    const myParty = global.EXISTING_PARTY_1
    const myPrivateKey = global.EXISTING_PARTY_1_KEYS.privateKey

    const createPreapprovalCommand =
        await sdk.amulet.preapproval.command.create({
            parties: {
                receiver: myParty,
            },
        })

    await sdk.ledger
        .prepare({
            partyId: myParty,
            commands: createPreapprovalCommand,
        })
        .sign(myPrivateKey)
        .execute({
            partyId: myParty,
        })
}
```

## Accepting or rejecting a 2-step transfer

If no Transfer pre-approval have been set up, then it is required to fetch incoming transfer instructions and consume either the `Accept` or `Reject` choice, this can be done easily using the Wallet SDK.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })
    const myParty = global.EXISTING_PARTY_1

    //this returns a list of all transfer instructions, you can then accept or reject them
    await sdk.token.transfer.pending(myParty)
}
```

the above give a list of pending transfer instructions, you can then exercise the accept or reject choice on them:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })
    const myParty = global.EXISTING_PARTY_2
    const myPrivateKey = global.EXISTING_PARTY_2_KEYS.privateKey
    const Reject = true

    const myPendingTransaction = await sdk.token.transfer.pending(myParty)

    const myPendingTransactionCid = myPendingTransaction[0].contractId
    if (Reject) {
        //reject the transaction
        const [rejectTransferCommand, disclosedContracts] =
            await sdk.token.transfer.reject({
                transferInstructionCid: myPendingTransactionCid,
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        await sdk.ledger
            .prepare({
                partyId: myParty,
                commands: rejectTransferCommand,
                disclosedContracts: disclosedContracts,
            })
            .sign(myPrivateKey)
            .execute({ partyId: myParty })
    } else {
        //accept the transaction
        const [acceptTransferCommand, disclosedContracts] =
            await sdk.token.transfer.accept({
                transferInstructionCid: myPendingTransactionCid,
                registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
            })

        await sdk.ledger
            .prepare({
                partyId: myParty,
                commands: acceptTransferCommand,
                disclosedContracts: disclosedContracts,
            })
            .sign(myPrivateKey)
            .execute({ partyId: myParty })
    }
}
```

## Withdrawing a 2-step transfer before it gets accepted

Apart from accepting or rejecting a transfer instruction, it is also possible for the sender to `withdraw` the offer, thereby retrieving the locked funds.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })
    const myParty = global.EXISTING_PARTY_1
    const myPrivateKey = global.EXISTING_PARTY_1_KEYS.privateKey

    const myPendingTransaction = await sdk.token.transfer.pending(myParty)

    const myPendingTransactionCid = myPendingTransaction[0].contractId

    const [withdrawTransferCommand, disclosedContracts] =
        await sdk.token.transfer.withdraw({
            transferInstructionCid: myPendingTransactionCid,
            registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
        })

    await sdk.ledger
        .prepare({
            partyId: myParty,
            commands: withdrawTransferCommand,
            disclosedContracts: disclosedContracts,
        })
        .sign(myPrivateKey)
        .execute({ partyId: myParty })
}
```

## How do i quickly setup transfer preapproval?

It is worth nothing that using the validator operator party as the providing party causes the transfer pre-approval to auto-renew. The below script setup transfer preapproval for Bob and performs a 1-step transfer from Alice to Bob:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { Holding, PrettyContract } from '@canton-network/core-tx-parser'
import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
import { pino } from 'pino'
import {
    TOKEN_NAMESPACE_CONFIG,
    TOKEN_PROVIDER_CONFIG_DEFAULT,
    AMULET_NAMESPACE_CONFIG,
} from './utils/index.js'

const logger = pino({ name: 'v1-05-preapproval', level: 'info' })

const sdk = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    token: TOKEN_NAMESPACE_CONFIG,
    amulet: AMULET_NAMESPACE_CONFIG,
})

await sdk.amulet.tapInternal('1000')

const aliceKeys = sdk.keys.generate()

const alice = await sdk.party.external
    .create(aliceKeys.publicKey, {
        partyHint: 'v1-05-alice',
    })
    .sign(aliceKeys.privateKey)
    .execute()

const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
    alice.partyId,
    '10000'
)

await sdk.ledger
    .prepare({
        partyId: alice.partyId,
        commands: amuletTapCommand,
        disclosedContracts: amuletTapDisclosedContracts,
    })
    .sign(aliceKeys.privateKey)
    .execute({ partyId: alice.partyId })

const bobKeys = sdk.keys.generate()

const bob = await sdk.party.external
    .create(bobKeys.publicKey, {
        partyHint: 'v1-05-bob',
    })
    .sign(bobKeys.privateKey)
    .execute()

// --- TEST CREATE COMMAND

const createPreapprovalCommand = await sdk.amulet.preapproval.command.create({
    parties: {
        receiver: bob.partyId,
    },
})

logger.info(
    { createPreapprovalCommand },
    'Successfully created a preapproval command'
)

await sdk.ledger
    .prepare({
        partyId: bob.partyId,
        commands: createPreapprovalCommand,
    })
    .sign(bobKeys.privateKey)
    .execute({
        partyId: bob.partyId,
    })

logger.info('Successfully registered the preapproval.')

// --- TEST FETCH

const start = performance.now()
const fetchOnceStatus = await sdk.amulet.preapproval.fetchQuick(bob.partyId)
const end = performance.now()

const duration = end - start
if (duration < 1000) {
    logger.info(
        `Success! The operation was fast (${duration.toFixed(2)} ms) and fetchOnce status is ${fetchOnceStatus}.`
    )
} else {
    logger.warn(
        `Warning: Operation took longer than 1 second (${(duration / 1000).toFixed(2)} s).`
    )
}

logger.info('Fetching for preapproval status with retry')

const fetchedPreapprovalStatus = await sdk.amulet.preapproval.fetchStatus(
    bob.partyId
)

logger.info({ fetchedPreapprovalStatus }, 'Fetched preapproval status')

const sentValue = 2000

const [transferCommand, transferDisclosedContracts] =
    await sdk.token.transfer.create({
        sender: alice.partyId,
        recipient: bob.partyId,
        amount: sentValue.toString(),
        instrumentId: 'Amulet',
        registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
    })

await sdk.ledger
    .prepare({
        partyId: alice.partyId,
        commands: transferCommand,
        disclosedContracts: transferDisclosedContracts,
    })
    .sign(aliceKeys.privateKey)
    .execute({ partyId: alice.partyId })

logger.info({ sentValue }, 'Executed transfer from Alice to Bob with value:')

const aliceUtxos = await sdk.token.utxos.list({ partyId: alice.partyId })
const bobUtxos = await sdk.token.utxos.list({ partyId: bob.partyId })

const partyAmuletValue = (utxos: PrettyContract<Holding>[]) =>
    utxos.reduce(
        (acc, utxo) => acc + parseFloat(utxo.interfaceViewValue.amount),
        0
    )
const aliceAmuletValue = partyAmuletValue(aliceUtxos)
const bobAmuletValue = partyAmuletValue(bobUtxos)

if (aliceAmuletValue !== 8000 || bobAmuletValue !== 2000)
    throw Error(
        `Wrong end results for utxos: ${JSON.stringify({ aliceAmuletValue, bobAmuletValue })}`
    )

logger.info({ aliceAmuletValue, bobAmuletValue }, 'Result:')

// --- TEST RENEW COMMAND

logger.info('Renewing preapproval...')

const start2 = performance.now()
const fetchOnceStatusWithPreapproval = await sdk.amulet.preapproval.fetchQuick(
    bob.partyId
)
const end2 = performance.now()

const duration2 = end2 - start2
if (duration < 1000) {
    logger.info(
        `Success! The operation was fast (${duration2.toFixed(2)} ms) and fetchOnce status is ${fetchOnceStatusWithPreapproval}.`
    )
} else {
    logger.warn(
        `Warning: Operation took longer than 1 second (${duration2.toFixed(2)} s).`
    )
}

const newExpiresAt = new Date(fetchedPreapprovalStatus!.expiresAt)
newExpiresAt.setDate(newExpiresAt.getDate() + 2)

await sdk.amulet.preapproval.renew({
    parties: {
        receiver: bob.partyId,
    },
    expiresAt: newExpiresAt,
})

const fetchedStatusAfterRenew = await sdk.amulet.preapproval.fetchStatus(
    bob.partyId,
    {
        oldCid: fetchedPreapprovalStatus!.contractId,
    }
)

const before = fetchedPreapprovalStatus!.expiresAt
const after = fetchedStatusAfterRenew!.expiresAt

if (!(after.getTime() > before.getTime())) {
    throw new Error(
        `Expected expiresAt to increase after renewal. before=${fetchedPreapprovalStatus!.expiresAt.toISOString()} after=${fetchedStatusAfterRenew!.expiresAt.toISOString()}`
    )
}

logger.info(
    {
        before: before.toISOString(),
        after: after.toISOString(),
        extendedSeconds: Math.round(
            (after.getTime() - before.getTime()) / 1000
        ),
    },
    'TransferPreapproval expiry extended, managed to renew preapproval'
)

// --- TEST CANCEL COMMAND
logger.info('Testing out cancel command')

if (!fetchedStatusAfterRenew?.templateId) {
    throw new Error('No preapproval found - fetchedPreapprovalStatus is null')
}
const [cancelPreapprovalCommand, cancelDisclosedContracts] =
    await sdk.amulet.preapproval.command.cancel({
        parties: {
            receiver: bob.partyId,
        },
    })

if (!cancelPreapprovalCommand) {
    throw Error(
        'Cancel preapproval command is null even though one has been created before'
    )
}

await sdk.ledger
    .prepare({
        partyId: bob.partyId,
        commands: cancelPreapprovalCommand,
        disclosedContracts: cancelDisclosedContracts,
    })
    .sign(bobKeys.privateKey)
    .execute({
        partyId: bob.partyId,
    })

logger.info('Submitted cancel command; now polling')
const cancelled = await sdk.amulet.preapproval.fetchStatus(bob.partyId, {
    cancelled: true,
})

const preapprovalACS = await sdk.ledger.acsReader.readJsContracts({
    parties: [bob.partyId],
    filterByParty: true,
})

const renewedPreapprovalStillActive = preapprovalACS.some(
    (contract) => contract.contractId === fetchedStatusAfterRenew?.contractId
)

if (cancelled === null && !renewedPreapprovalStillActive) {
    logger.info(`Successfully cancelled`)
}
```

## How to renew or cancel a transfer preapproval

If you have used the validator operator party as the provider, then it will automatically renew the transfer preapproval approximately 20 days before expiry, however there are cases where you would like to perform the preapproval renewal manually:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await amulet.preapproval.renew({
    parties: {
        receiver: myPartyId,
    },
    expiresAt: newExpiresAt,
})
```

You can also deploy a secondary transfer preapproval, however this means that there are simply two preapprovals instead of it replacing the existing.

If you have accidentally created a transfer preapproval that you dont want to keep you can perform a cancel instead:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const [cancelPreapprovalCommand, cancelDisclosedContracts] =
await amulet.preapproval.command.cancel({
    parties: {
        receiver: myPartyId,
    },
})
await sdk.ledger
    .prepare({
        partyId: myPartyId,
        commands: cancelPreapprovalCommand,
        disclosedContracts: cancelDisclosedContracts,
    })
    .sign(myPrivateKey)
    .execute({
        partyId: myPartyId,
    })
```

## How do I fetch transaction by updateId?

Given an update Id, the token namespace has a method for getting a transaction based on the updateId. This will print out the transaction in the same format as `sdk.token.holdings`

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        amulet: global.AMULET_NAMESPACE_CONFIG,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const myParty = global.EXISTING_PARTY_1

    const [amuletTapCommand, amuletTapDisclosedContracts] =
        await sdk.amulet.tap(myParty, '2000')

    const result = await sdk.ledger
        .prepare({
            partyId: myParty,
            commands: amuletTapCommand,
            disclosedContracts: amuletTapDisclosedContracts,
        })
        .sign(global.EXISTING_PARTY_1_KEYS.privateKey)
        .execute({ partyId: myParty })

    await sdk.token.transactionsById({
        updateId: result.updateId,
        partyId: myParty,
    })
}
```

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/wallet-sdk-configuration/index.rst" hash="75ca5982" */}

# Wallet SDK Configuration

If you have already played around with the wallet SDK you might have come across snippets like:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    localNetStaticConfig,
    SDK,
    signTransactionHash,
} from '@canton-network/wallet-sdk'
import { pino } from 'pino'
import { v4 } from 'uuid'
import {
    TOKEN_NAMESPACE_CONFIG,
    TOKEN_PROVIDER_CONFIG_DEFAULT,
    AMULET_NAMESPACE_CONFIG,
} from './utils/index.js'

const logger = pino({ name: 'v1-01-ping-localnet', level: 'info' })

const sdk = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    token: TOKEN_NAMESPACE_CONFIG,
    amulet: AMULET_NAMESPACE_CONFIG,
})

const senderKeys = sdk.keys.generate()

const sender = await sdk.party.external
    .create(senderKeys.publicKey, {
        partyHint: 'v1-01-alice',
    })
    .sign(senderKeys.privateKey)
    .execute()

const senderFingerprint = await sdk.keys.fingerprint(senderKeys.publicKey)

logger.info({ sender, senderFingerprint }, 'Sender party representation:')

if (sender.publicKeyFingerprint !== senderFingerprint)
    throw Error('Inconsistent fingerprints')

const receiverKeys = sdk.keys.generate()

const receiverPartyCreation = sdk.party.external.create(
    receiverKeys.publicKey,
    {
        partyHint: 'v1-01-bob',
    }
)

const unsignedReceiver = await receiverPartyCreation.topology()

// external signing simulation
const receiverPartySignature = signTransactionHash(
    unsignedReceiver.multiHash,
    receiverKeys.privateKey
)

const signedReceiverParty = await receiverPartyCreation.execute(
    receiverPartySignature
)

logger.info({ signedReceiverParty }, 'Receiver party representation:')

const pingCommand = [
    {
        CreateCommand: {
            templateId:
                '#canton-builtin-admin-workflow-ping:Canton.Internal.Ping:Ping',
            createArguments: {
                id: v4(),
                initiator: sender.partyId,
                responder: sender.partyId,
            },
        },
    },
]

logger.info({ pingCommand }, 'Ping command to be submitted:')

await sdk.ledger
    .prepare({
        partyId: sender.partyId,
        commands: pingCommand,
        disclosedContracts: [],
    })
    .sign(senderKeys.privateKey)
    .execute({ partyId: sender.partyId })

logger.info('Ping command submitted with online signing')

/*
offline signing example
*/

const preparedPingCommand = sdk.ledger.prepare({
    partyId: sender.partyId,
    commands: pingCommand,
    disclosedContracts: [],
})

const { response: preparedPingCommandResponse } =
    await preparedPingCommand.toJSON()

logger.info({ preparedPingCommand }, 'Prepared ping command:')

/*
Note: The following code uses the @canton-network/core-signing-lib as the 'custodian' of the private key to sign the prepared transaction hash,
but in a real scenario, the signing could be done using any compatible signing mechanism, such as a hardware wallet or an external signing service.
*/
const signature = signTransactionHash(
    preparedPingCommandResponse.preparedTransactionHash,
    senderKeys.privateKey
)

const signed = sdk.ledger.fromSignature(preparedPingCommandResponse, signature)

await sdk.ledger.execute(signed, { partyId: sender.partyId })

logger.info('Ping command submitted with offline signing')

const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
    sender.partyId,
    '10000'
)

const result = await sdk.ledger
    .prepare({
        partyId: sender.partyId,
        commands: amuletTapCommand,
        disclosedContracts: amuletTapDisclosedContracts,
    })
    .sign(senderKeys.privateKey)
    .execute({ partyId: sender.partyId })

const senderUtxos = await sdk.token.utxos.list({ partyId: sender.partyId })

const tapTransaction = await sdk.token.transactionsById({
    updateId: result.updateId,
    partyId: sender.partyId,
})

const mintEvent = tapTransaction.events.find(
    (tokenStandardEvent) =>
        tokenStandardEvent.label.type === 'Mint' &&
        tokenStandardEvent.unlockedHoldingsChange.creates.find(
            (h) => h.amount === '10000.0000000000'
        )
)

if (mintEvent) {
    logger.info('Found token standard event with type Mint')
} else {
    throw new Error(`Couldn't find tap transaction by updateId`)
}
const senderAmuletUtxos = senderUtxos.filter((utxo) => {
    return (
        utxo.interfaceViewValue.amount === '10000.0000000000' &&
        utxo.interfaceViewValue.instrumentId.id === 'Amulet'
    )
})

if (senderAmuletUtxos.length === 0) {
    throw new Error('No UTXOs found for Sender')
}

logger.info('Tap command for Amulet for Sender submitted and UTXO received')
```

This is the default config that can be used in combination with a non-altered [Localnet](https://docs.global.canton.network.sync.global/app_dev/testing/localnet.html) running instance.

However as soon as you need to migrate your script, code and deployment to a different environment these default configurations are no longer viable to use. In those cases creating custom factories for each controller is needed. Here is a template that you can use when setting up your own custom connectivity configuration:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: {
            method: 'self_signed',
            issuer: 'unsafe-auth',
            credentials: {
                clientId: 'ledger-api-user',
                clientSecret: 'unsafe',
                audience: 'https://canton.network.global',
                scope: '',
            },
        },
        ledgerClientUrl: new URL('http://localhost:2975'),
        token: {
            validatorUrl: new URL('http://localhost:2000/api/validator'),
            registries: [
                new URL('http://localhost:2000/api/validator/v0/scan-proxy'),
            ],
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        },
        amulet: {
            validatorUrl: localNetStaticConfig.LOCALNET_APP_VALIDATOR_URL,
            scanApiUrl: localNetStaticConfig.LOCALNET_SCAN_API_URL,
            auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
            registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
        },
        asset: {
            registries: [localNetStaticConfig.LOCALNET_REGISTRY_API_URL],
            auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
        },
    })

    const myParty = global.EXISTING_PARTY_1

    await sdk.token.utxos.list({ partyId: myParty })

    await sdk.amulet.traffic.status()

    // OR, you can defer loading config by calling .extend()

    const basicSDK = await SDK.create({
        auth: {
            method: 'self_signed',
            issuer: 'unsafe-auth',
            credentials: {
                clientId: 'ledger-api-user',
                clientSecret: 'unsafe',
                audience: 'https://canton.network.global',
                scope: '',
            },
        },
        ledgerClientUrl: new URL('http://localhost:2975'),
    })

    // Extend with token namespace
    const tokenExtendedSDK = await basicSDK.extend({
        token: {
            validatorUrl: new URL('http://localhost:2000/api/validator'),
            registries: [
                new URL('http://localhost:2000/api/validator/v0/scan-proxy'),
            ],
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        },
    })

    // Now token namespace is available
    await tokenExtendedSDK.token.utxos.list({ partyId: myParty })

    // Can extend further with more namespaces
    const fullyExtendedSDK = await tokenExtendedSDK.extend({
        amulet: {
            validatorUrl: localNetStaticConfig.LOCALNET_APP_VALIDATOR_URL,
            scanApiUrl: localNetStaticConfig.LOCALNET_SCAN_API_URL,
            auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
            registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
        },
    })

    // Now both token and amulet are available
    await fullyExtendedSDK.token.utxos.list({ partyId: myParty })
    await fullyExtendedSDK.amulet.traffic.status()
}
```

## How do I validate my configurations?

Knowing if you are using the correct url and port can be daunting, here is a few curl and gcurl commands you can use to validate against an expected output

**my-json-ledger-api** can be identified with `curl http://${my-json-ledger-api}/v2/version` it should produce a json that looks like

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
"version": "3.4.12-SNAPSHOT",
"features": {
   "experimental": {
         "staticTime": {
            "supported": false
         },
         "commandInspectionService": {
            "supported": true
         }
   },
   "userManagement": {
         "supported": true,
         "maxRightsPerUser": 1000,
         "maxUsersPageSize": 1000
   },
   "partyManagement": {
         "maxPartiesPageSize": 10000
   },
   "offsetCheckpoint": {
         "maxOffsetCheckpointEmissionDelay": {
            "seconds": 75,
            "nanos": 0,
            "unknownFields": {
               "fields": {}
            }
         }
   },
   "packageFeature": {
         "maxVettedPackagesPageSize": 100
   }
}
}
```

the fields may vary based on your configuration.

**my-validator-app-api** can be identified with `curl ${api}/version` it should produce an output like

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{"version":"0.4.15","commit_ts":"2025-09-05T11:38:13Z"}
```

**my-scan-proxy-api** is an api inside the validator api and can be defined as `${my-validator-app-api}/v0/scan-proxy`.

**my-registry-api** is the registry for the token you want to use, for Canton Coin you can use **my-scan-proxy-api**, however for any other token standard token it is required to source the api from a reputable source.

## Configuring auth

The wallet-sdk can either take in a Provider (which will have auth bundled into it) or a LedgerClientUrl + TokenProviderConfig. In our examples, we have provided a default TokenProviderConfig for connecting to localnet, which uses a self-signed token.

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
method: 'self_signed',
issuer: 'unsafe-auth',
credentials: {
   clientId: 'ledger-api-user',
   clientSecret: 'unsafe',
   audience: 'https://canton.network.global',
   scope: '',
},
}
```

The value for some of the audiences in localnet would have to be adjusted to match "[https://canton.network.global](https://canton.network.global)". This is specifically the `LEDGER_API_AUTH_AUDIENCE` & `VALIDATOR_AUTH_AUDIENCE`.

When upgrading your setup from a localnet setup to a production or client facing environment then it might make more sense to add proper authentication to the ledger api and other services. The community contributions include okta and keycloak [OIDC](/global-synchronizer/deployment/oidc-providers). These can easily be configured for the SDK using a different TokenProviderConfig. The following programmatic methods of token fetching are supported:

> 1. \`static\`: a fixed, in-memory token. Only used for compatibility, it will totally break for expired tokens.
> 2. \`self\_signed\`: only for development purposes, used for Canton setups that accept HMAC256 self signed tokens.
> 3. \`client\_credentials\`: used to programmatically acquire tokens via oauth2, a.k.a "machine-to-machine" tokens

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export type TokenProviderConfig =
   | {
         method: 'static'
         token: string
      }
   | {
         method: 'self_signed'
         issuer: string
         credentials: ClientCredentials
      }
   | {
         method: 'client_credentials'
         configUrl: string
         credentials: ClientCredentials
      }

export interface ClientCredentials {
 clientId: string
 clientSecret: string
 scope: string | undefined
 audience: string | undefined
}
```

## Registering Plugins

The Wallet SDK supports extending its functionality through a plugin system. Plugins allow you to add custom methods and functionality to the SDK instance while maintaining access to the SDK context and logger.

### Creating and Registering a Plugin

To create a plugin, extend the `SDKPlugin` class and implement your custom functionality. Plugins are registered using the `registerPlugins` method, which accepts a record of plugin constructors keyed by their desired property names.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, SDKContext, SDKPlugin } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = (
        await SDK.create({
            auth: {
                method: 'self_signed',
                issuer: 'unsafe-auth',
                credentials: {
                    clientId: 'ledger-api-user',
                    clientSecret: 'unsafe',
                    audience: 'https://canton.network.global',
                    scope: '',
                },
            },
            ledgerClientUrl: 'http://localhost:2975',
        })
    ).registerPlugins({
        myPlugin: class extends SDKPlugin {
            // wallet-sdk plugin should always accept SDKContext
            constructor(protected readonly ctx: SDKContext) {
                super('myPlugin', ctx)
            }

            myMethod() {
                // do some logic
                return
            }
        },
    })

    sdk.myPlugin.myMethod()
}
```

### Key Points

* **Plugin Constructor**: Plugin classes must accept `SDKContext` as a constructor parameter and pass it to the `super()` call along with the plugin name.
* **Type Safety**: The `registerPlugins` method provides full type safety, ensuring that registered plugins are accessible with proper autocompletion and type checking.
* **Access to SDK Context**: Plugins have access to the SDK's context, logger, and other internal utilities through the `ctx` property.
* **Multiple Plugins**: You can register multiple plugins at once by passing them in a single object to `registerPlugins`.

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/traffic/index.rst" hash="bc045f4b" */}

# Traffic

Below is a high-level summary of the [Synchronizer Traffic Fees page](/global-synchronizer/deployment/synchronizer-traffic) in the Splice Validator documentation. For more detail on point, it's advised to read that documentation.

## Traffic

* Traffic fees are paid at the validator node level, not the party level.

* Every validator has a traffic balance at the global synchronizer level.
  * Traffic is measured in bytes.
  * A trickle rate of free traffic is provided to validator nodes every 10 minutes (each mining round).

* Traffic is deducted from your validator node's traffic balance every time your node sends a message to the synchronizer. Traffic is charged for:
  * Broadcasting a transaction - this is where the bulk of the traffic fees will be paid.
  * Sending consensus messages for transactions a validator is involved in.

* If your node runs out of traffic it is unable to transact. It'll recover by itself thanks to the free trickle rate. However, you can buy more traffic. See the next section.

## Getting more traffic

* Traffic is obtained by burning Canton Coin and it is always pre-purchased.

* The conversion Canton Coin \<> Bytes can be derived from on-chain parameters.
  * Super Validators publish an on-chain conversion CC \<> USD.
  * Super Validators publish a traffic cost USD \<> Bytes.

* Anyone can burn Canton Coin to get traffic for any node.
  * You can buy your own traffic.
  * You can sign up with a service like the [Denex Gas Station](https://denex.io/gasstation) to buy your traffic.

* The validator node has automation to keep traffic topped up. As long as you keep CC in your validator party, it'll stay available. See [here](/global-synchronizer/deployment/validator-kubernetes#configuring-automatic-traffic-purchases) for how to configure automatic traffic purchases.

## How to determine the traffic cost of a transaction?

Follow this [FAQ entry in the Splice documentation](/global-synchronizer/deployment/synchronizer-traffic).

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/tokenomics-and-rewards/index.rst" hash="08ff71a4" */}

# Tokenomics and Rewards

## CC Rewards

* The tokenomics operate on 10m “mining rounds”.
* Every 10 minutes, different stakeholders of the network are rewarded with coupons which can be used to mint Canton Coin according to how much value they've brought to the network.
* Coupons are rewarded to the Validator admin party.
* All rewards awarded to a node's local parties will be auto-minted by the node administrator party.
* The validators automation is not able to mint the rewards for an external parties - the external party needs to delegate the ability for the validator admin party to mint their rewards on their behalf or manually mint the rewards themselves each round they receive rewards.
* All rewards and coupons are mintable the follow mining round
* If rewards are not redeemed then they are lost\*

You can find more information about the tokenomics of Canton Coin [here](/overview/reference/canton-coin-tokenomics).

## Ways of Obtaining Canton Coin Rewards

The tokenomics of the network give you options for obtaining Canton Coin:

### Validator & Super Validator Liveness Rewards

Just for being online and growing the network, Canton Coin tokenomics enable validator operators to mint CC. Validators and Super Validators generate reward coupons that can be used to mint Canton Coins. The coupons are paid out to the validator adminstration party. For local parties onboarded to a validator, the validator application runs background automation to mint all activity records automatically. An external party signs transactions using a key they control. As a consequence, the validator automation is not able to perform minting for external parties.

For external parties, automation needs to be developed to call `AmuletRules_Transfer` at least once per round with all activity records as inputs.

You can find more information about the tokenomics of Canton Coin at [/overview/reference/canton-coin-tokenomics](/overview/reference/canton-coin-tokenomics).

*All rewards and coupons are mintable the follow mining round, if rewards are not redemed then they are lost*

### Validator Activeness Rewards

If you self-purchase traffic, you get a discount via these rewards.

### Application Rewards and Featured Activity Markers

**Application Rewards**

* Transactions which include Canton Coin and featured application transactions earn application rewards.
* The percentage of Canton Coin awarded to applications is significant and will grow over time.
* The current amount of CC awarded to applications can be seen in the 'Canton Coin Reward Split By Role Over Time' chart [here](https://canton.thetie.io/).

**Featured application activity markers**

* Applications which generate valuable activity for the canton network, and have 'featured application' status can earn more application rewards.
* By qualifying as a Featured Application (apply [here](https://sync.global/featured-app-request/)) and applying a `FeaturedAppActivityMarker` to a transaction it is marked and converted to reward coupons that can be redeemed.
* A weighting is applied to each transaction in that Canton Coin minting round.
* More weightings in a round equate to more application rewards.
* Currently, featured apps receive many more rewards in Canton Coin than the average transaction costs in traffic fees.

## Gaining Application Rewards as a Wallet/Custodian/Exchange

* Request featured application status. Apply [here](https://sync.global/featured-app-request/).
  * On DevNet you can self-feature through the wallet UI.

**Enabling Pre-approval / 1-step Transfers**

* One way that wallets can earn app rewards is by enabling direct / 1 step / pre-approval transfers
* Setting up pre-approvals costs around \$1 per 90 days per party
* By enabling 1-step transfers your party is added as the operator party to incoming deposits
* Therefore, when users deposit funds into your account you'll receive rewards.
* You can also mark transactions out of your wallet (that don't go to parties which have 1-step transfers enabled) with your party as the operator part for that transaction
* It's anticipated that you will receive far more Canton Coin through rewards for pre-approval deposits and transfers than you pay in traffic fees, setting up pre-approvals and for creating parties.
* Therefore:
  * You may not want to charge your users for traffic in the near term.
  * In the mid-to-long term the tokenomics may not support this model, so you may want to think about a charging strategy.
  * We still advise monitoring or even controlling the number of parties that a user can create so that you don't end up with users creating too many parties and therefore cost.

## Redeming Reward Coupons with External Party

To accept rewards with an external party you need to call `AmuletRules_Transfer` with the activity records as inputs.

## Sharing Featured Application Reward between multiple parties

Featured Application rewards can be shared between multiple parties, this can be done by defining a list of benificiaries and give them a weighted amount of the total reward. The sum of all beneficiaries weight must be equal to 1.0. This results in separate coupons being generated for each beneficiary.

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/user-management/index.rst" hash="35355c49" */}

# User Management

The Wallet SDK has functionality for creating and managing user rights, by default when you are connecting it uses whichever user is defined in your auth-controller. If the user is an admin user on the ledger api they can be used to create other users and grant them rights.

## How do I quickly setup canReadAsAnyParty and canExecuteAsAnyParty?

This script sets up three users `alice`, `bob` and `master`. `master` is given canReadAsAnyParty and canExecuteAsAnyParty and it shows proper access control by creating parties and ensuring that `alice` and `bob` can not see each others parties.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
import { pino } from 'pino'
import { TOKEN_PROVIDER_CONFIG_DEFAULT } from './utils/index.js'
const logger = pino({ name: 'v1-multi-user-setup', level: 'info' })

logger.info('Operator sets up users and primary parties')

const operatorSdk = await SDK.create({
    auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
})

const aliceInternal = await operatorSdk.party.internal.allocate({
    partyHint: 'v1-09-alice',
})

const bobInternal = await operatorSdk.party.internal.allocate({
    partyHint: 'v1-09-bob',
})

const masterPartyInternal = await operatorSdk.party.internal.allocate({
    partyHint: 'v1-09-master',
})

logger.info('Created the internal parties')

const aliceUser = await operatorSdk.user.create({
    userId: 'alice-user',
    primaryParty: aliceInternal,
    userRights: {
        participantAdmin: true,
    },
})

const bobUser = await operatorSdk.user.create({
    userId: 'bob-user',
    primaryParty: bobInternal,
    userRights: {
        participantAdmin: true,
    },
})

const masterUser = await operatorSdk.user.create({
    userId: 'master-user',
    primaryParty: masterPartyInternal,
    userRights: {
        participantAdmin: true,
    },
})

logger.info('created the users')

if (!(aliceUser || bobUser || masterUser)) {
    throw new Error(`One of the users was not created correctly`)
}

await operatorSdk.user.rights.grant({
    userId: masterUser.id!,
    userRights: {
        canExecuteAsAnyParty: true,
        canReadAsAnyParty: true,
    },
})

logger.info(
    `Created alice user: ${aliceUser.id} with primary party (internal) ${aliceUser.primaryParty}`
)
logger.info(
    `Created bob user: ${bobUser.id} with primary party (internal) ${bobUser.primaryParty}`
)
logger.info(
    `Created master user: ${masterUser.id} with primary party (internal) ${masterUser.primaryParty}, with read as and execute as rights`
)

const aliceSdk = await SDK.create({
    auth: {
        method: 'self_signed',
        issuer: 'unsafe-auth',
        credentials: {
            clientId: aliceUser.id,
            clientSecret: 'unsafe',
            audience: 'https://canton.network.global',
            scope: '',
        },
    },
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
})

const aliceKeyPair = aliceSdk.keys.generate()
const aliceExternal = await aliceSdk.party.external
    .create(aliceKeyPair.publicKey, {
        partyHint: 'v1-09-alice',
    })
    .sign(aliceKeyPair.privateKey)
    .execute()

logger.info(`alice created external party`)

const bobSdk = await SDK.create({
    auth: {
        method: 'self_signed',
        issuer: 'unsafe-auth',
        credentials: {
            clientId: bobUser.id,
            clientSecret: 'unsafe',
            audience: 'https://canton.network.global',
            scope: '',
        },
    },
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
})

const bobKeyPair = bobSdk.keys.generate()
const bobExternal = await bobSdk.party.external
    .create(bobKeyPair.publicKey, {
        partyHint: 'v1-09-bob',
    })
    .sign(bobKeyPair.privateKey)
    .execute()
logger.info(`bob created external party`)

const masterUserSdk = await SDK.create({
    auth: {
        method: 'self_signed',
        issuer: 'unsafe-auth',
        credentials: {
            clientId: masterUser.id,
            clientSecret: 'unsafe',
            audience: 'https://canton.network.global',
            scope: '',
        },
    },
    ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
})

const masterWalletView = await masterUserSdk.party.list()

if (!masterWalletView?.find((p) => p === aliceExternal.partyId)) {
    throw new Error('master user cannot see alice party')
}
if (!masterWalletView?.find((p) => p === bobExternal.partyId)) {
    throw new Error('master user cannot see bob party')
}

const aliceWalletView = await aliceSdk.party.list()
logger.info(aliceWalletView)

if (aliceWalletView?.find((p) => p === bobExternal.partyId)) {
    throw new Error('alice user can see bob party')
}

const bobWalletView = await bobSdk.party.list()

if (bobWalletView?.find((p) => p === aliceExternal.partyId)) {
    throw new Error('bob user can see alice party')
}

logger.info(
    'alice and bob have proper isolation and cannot see each others external parties'
)

//user management test
await bobSdk.user.rights.grant({
    userRights: {
        readAs: [aliceExternal.partyId],
    },
})

const bobWalletViewAfterGrantRights = await bobSdk.party.list()

if (!bobWalletViewAfterGrantRights?.find((p) => p === aliceExternal.partyId)) {
    throw new Error('bob user cannot see alice party even with ReadAs rights')
}

const bobRightsAfterGrantRights = await bobSdk.user.rights.list()

logger.info(bobRightsAfterGrantRights, 'Bob user rights')

await bobSdk.user.rights.revoke({
    userRights: {
        readAs: [aliceExternal.partyId],
    },
})

const bobWalletViewAfterRevokeRights = await bobSdk.party.list()

if (bobWalletViewAfterRevokeRights?.find((p) => p === aliceExternal.partyId)) {
    throw new Error('bob user can see alice party even after revoking rights')
}
```

## Creating a new user

Creating a new user can be done using the adminLedger, this new user can then be granted rights or can create new parties as needed.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    await sdk.user.create({
        userId: 'alice-user',
        primaryParty: global.EXISTING_PARTY_1,
    })
}
```

## ReadAs and ActAs limitations

Currently when allocating a new party we also grant ReadAs and ActAs rights for that party for the submitting user. This allows the user to do the normal flows involved like preparing transactions and executing those. There are performance issues if too many of these rights are assigned to the same user, in the case of a `master` user that is interacting on behalf of a client, then it might be more convenient to use `CanReadAsAnyParty` and `CanExecuteAsAnyParty` as described below.

Here is how the method changes if you need to allocate a party without granting rights:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })
    const key = sdk.keys.generate()

    const party = await sdk.party.external
        .create(key.publicKey, { partyHint: 'my-party-without-rights' })
        .sign(key.privateKey)
        .execute({ grantUserRights: false }) //do not grant user actAs and readAs for the party
}
```

## CanReadAsAnyParty

CanReadAsAnyParty gives a user full information about any party on the ledger, if a user is set up with this they will see: 1. All parties hosted on the ledger (multi-hosted and single hosted) 2. All transaction happening involving a party on the ledger 3. Prepare transactions on behalf of any party

This will not grant information about parties hosted on other ledgers or their transactions.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    await sdk.user.rights.grant({
        userRights: { canReadAsAnyParty: true },
    })
}
```

The SDK automatically leverages this elevated permission for certain endpoints like `listWallets`.

## CanExecuteAsAnyParty

CanExecuteAsAnyParty gives full execution rights for a party, this means that a user with these rights can submit transaction on behalf of a party hosted on the ledger.

**This does not give the user rights to move funds without a valid signature!**

The setup is similar to the \`CanReadAsAnyParty\`:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // it is important to configure the SDK correctly else you might run into connectivity or authentication issues
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    //optional arguments are idp and userId; if not provided, will use the default idp and extract the userId from the auth token
    await sdk.user.rights.grant({
        userRights: { canExecuteAsAnyParty: true },
    })
}
```

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/canton-coin-specific-considerations/index.rst" hash="45961707" */}

# Canton Coin Specific Considerations

## Handling Time-Bound Signatures (Canton Coin)

If your wallet infrastructure relies on offline signing, cold storage, or multi-party approval flows that take longer than **10–20 minutes**, then this guide is for you.

### The 10-Minute Signing Window

Canton Coin transactions operate on a strict **10-minute minting cycle**. Unlike standard Daml transactions, **Canton Coin** transfers and acceptances must reference a specific OpenMiningRound contract to calculate network fees and rewards.

* A new `OpenMiningRound` is created every **10 minutes**.
* The contract remains active for approximately **20 minutes** (the current round + overlap).
* **The Problem:** If you prepare a transaction referencing *Round A*, but you do not sign and submit it before *Round A* expires, the network will reject it.

**Common Error:** If your transaction exceeds this window, the API will return a `409 Conflict` with the following error:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
LOCAL_VERDICT_INACTIVE_CONTRACTS
```

There is one way of handle incoming transfers and another way to handle outgoing transfers, listed below.

### Solution 1: Implement Pre-approvals for Incoming Transfers / Receiving Funds

**Use Case:** Your users need to receive Canton Coin, but you cannot sign a transaction within 10 minutes (e.g., due to cold storage of the receiver's keys).

**The Fix:** Enable **1-Step Transfers** using [Pre-approvals](#2-step-transfer-vs-1-step-transfer).

Instead of signing every incoming transfer, the receiver signs a single, long-living `TransferPreapproval` contract. This authorizes the sending party (or a specific provider) to deposit funds immediately without requiring an interactive acceptance signature for every transaction.

To do this, create a `Splice.Wallet.TransferPreapproval` contract. The guide on how to create the pre-approval contract in the [Wallet SDK is here](#2-step-transfer-vs-1-step-transfer) and the general information about [Canton Coin Preapprovals is here](/appdev/modules/m7-canton-coin-preapprovals). By implementing a preapproval contract the receiver doesn't need to accept Canton Coin transfers sent to them as they are automatically accepted.

### Solution 2: Use Command Delegation for Outgoing Transfers / Sending Funds

<Note>
  Using `TransferCommand` only works where the receiver has enabled pre-approvals for Canton Coin and the sending external party has been onboarded to the splice wallet using the Validator APIs. Parties set up using the validator APIs and not using these workarounds are subject to the 200 party limit described here.
</Note>

**Use Case:** Your users need to send Canton Coin, but the signing process (e.g., institutional custody approval) takes hours.

**The Fix:** Use **Command Delegation** - TransferCommand.

Instead of signing the transfer transaction directly (which pins a short-lived Mining Round), the user signs a long-living instruction to transfer funds.

#### How it works

1. **User Signs Instruction:** The user signs a transaction to create a `Splice.ExternalPartyAmuletRules.TransferCommand` contract.
   * This contract **does not** reference a mining round.
   * It can remain valid for up to 24 hours (or as defined by `expiresAt`).
2. **Delegated Execution:** Once this command is on the ledger, a Super Validator (SV) or a delegate picks it up.
3. **Execution:** The delegate executes the actual transfer. The *delegate* selects the current `OpenMiningRound` at the moment of execution, ensuring the transaction succeeds regardless of how long ago the user signed the instruction.

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/deposits-into-exchanges/index.rst" hash="8d2784fe" */}

# Sending Deposits to Exchanges

To enable deposits to be sent to specific user accounts at exchanges, an account identifier needs to be sent to the exchange along with the transfer information. In Canton, the [“memo tag” pattern](https://support.ledger.com/article/4409603715217-zd) is implemented as follows.

## Canton Coin Wallet

In the Canton Coin wallet, the “Description” field in the screenshot below must be used to communicate this account identifier in the format required by the exchange. For example: “AcmeExchange account: \<exchangeInternalAccountId>”.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/cantonfoundation/integrations/images/splice-wallet.png" alt="Splice wallet UI" />

## CN Token Standard Wallets

The token standard defines the `splice.lfdecentralizedtrust.org/reason` metadata key for the purpose of communicating a human-readable description for the transfer (see [CIP-0056](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md#generic-metadata)).

Token standard wallets must provide a “Description” or “Reason” field analogous to the Canton Coin wallet, and store its value in the metadata field of the `Transfer` specification ([code](https://github.com/hyperledger-labs/splice/blob/332e06a7ae9e13fde5bba0bf7dcb059aa36f979e/token-standard/splice-api-token-transfer-instruction-v1/daml/Splice/Api/Token/TransferInstructionV1.daml#L12-L43)) when initiating a transfer. This is actually what the Canton Coin wallet does behind the scenes when initiating a Canton Coin transfer.

Likewise when displaying an incoming transfer or the tx history for a transfer the content of `splice.lfdecentralizedtrust.org/reason` metadata key should be parsed and displayed, as done for example by the transaction history parser in the token standard CLI ([docs](/appdev/deep-dives/token-standard)). This allows exchanges to communicate a correlation-id for a redemption.

Code sample for setting the right metadata field: see this [change to the experimental token standard CLI](https://github.com/hyperledger-labs/splice/pull/2003/files) to take the “reason” as command line argument and store it in the metadata field.

## CN Token Registries

Token standard compliant registries must ensure that they pass the `Transfer` specification unchanged along when implementing multi-step transfers using the `TransferInstruction` interface ([code](https://github.com/hyperledger-labs/splice/blob/332e06a7ae9e13fde5bba0bf7dcb059aa36f979e/token-standard/splice-api-token-transfer-instruction-v1/daml/Splice/Api/Token/TransferInstructionV1.daml#L108-L115)).

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/usdcx-support/index.rst" hash="852eb3cf" */}

# USDCx Support for Wallets

## Overview

Circle and Digital Asset have partnered to develop and implement a USDC token on Canton Network. This implementation requires users to send USDC on L1 chains (starting with Ethereum) to Circle’s xReserve contract which is then created as a USDC token on Canton Network. Conversely a withdrawal request for a USDC token on the Canton Network will result in the release of the asset on another chain. During the existence of the USDC token on Canton Network, it is available for use in financial transactions.

USDC on Canton Network represents USDC locked by Circle on the original L1 chain. And this token on Canton Network, is in the form of a Canton Network Standard Token ([CIP-56](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md)) as defined through the Canton Network Utilities service.

Wallet providers and exchanges have three options for supporting USDCx on the Canton Network:

1. Transfer & hold USDCx - Since USDCx is a token standard ([CIP-56](https://github.com/canton-foundation/cips/blob/main/cip-0056/cip-0056.md)) compliant asset then as such any wallet that supports the token standard will have built in support for transfers and holding.

2. Support xReserves deposits and withdrawals - Custom API integration is required for wallet providers and exchanges to support xReserve deposits and withdrawals to the utility-bridge daml models to / from their parties using the [xReserves UI](https://digital-asset.github.io/xreserve-deposits/). Instructions for doing this are included in the section “Supporting xReserve Deposits and Withdrawals” below.

3. Integrating the xReserve UI (Ethereum) into the wallet - To enable a full end-to-end experience for the user, a wallet can integrate against Ethereum directly for deposits on top of integrating point 2. To provide an example for doing this, the [xReserves UI](https://digital-asset.github.io/xreserve-deposits/) as well as [open-sourced example scripts](https://github.com/digital-asset/xreserve-deposits) are available for reference. This demonstrates the 2 ethereum transactions that must be submitted to an ethereum node:
   * approve a USDC spending allowance.
   * depositToRemote to deposit USDC into the xReserve contract.

## Supporting xReserve Deposits and Withdrawals

The required dar file can be found here

There are 3 choices (API calls) a wallet will need to implement in order to fully support the xReserve:

### Onboarding

To use the xReserve a party will first need to onboard to the bridge using the below: Example API call:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "CreateCommand": {
       "templateId": "#utility-bridge-v0:Utility.Bridge.V0.Agreement.User:BridgeUserAgreementRequest",
       "createArguments": {
           "crossChainRepresentative": "${ADMIN_PARTY_ID}",
           "operator": "${UTILITY_OPERATOR_PARTY_ID}",
           "bridgeOperator": "${BRIDGE_OPERATOR_PARTY_ID}",
           "user": "${USER_PARTY_ID}",
           "instrumentId": {
               "admin": "${ADMIN_PARTY_ID}",
               "id": "USDCx"
           },
           "preApproval": false
       }
   }
}
```

### Mint

Once a user deposits USDC into ethereum a DepositAttestation is created on the Canton network. In order for the recipient party to claim those funds they will need to call a choice to mint from the DepositAttestation:

`\#utility-bridge-v0:Utility.Bridge.V0.Attestation.Deposit:DepositAttestation`

Example API call:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "commands": [
        {
            "ExerciseCommand": {
                "templateId": "#utility-bridge-v0:Utility.Bridge.V0.Agreement.User:BridgeUserAgreement",
                "contractId": "${BRIDGE_USER_AGREEMENT_CONTRACT_ID}",
                "choice": "BridgeUserAgreement_Mint",
                "choiceArgument": {
                    "depositAttestationCid": "${DEPOSIT_ATTESTATION_CID}",
                    "factoryCid": "${FACTORY_CID}",
                    "contextContractIds": "${CONTEXT_CONTRACT_IDS}"
                }
            }
        }
    ],
    "disclosedContracts": "${DISCLOSED_CONTRACTS}",
}
```

### Withdraw

To withdraw from the Canton Network to Ethereum a user must burn the USDC on Canton. Specifying the:

* destination domain id: Currently only Ethereum is supported (domain id of 0).
* Amount: In Decimal to a max 6 decimal precision.
* Destination recipient: a valid Ethereum address.
* An optional reference. Empty Text field if not provided.

In addition the wallet will need to provide:

* The available Holding contract Ids
* A UUID as the requestId

Example API call:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "commands": [
        {
            "ExerciseCommand": {
                "templateId": "#utility-bridge-v0:Utility.Bridge.V0.Agreement.User:BridgeUserAgreement",
                "contractId": "${BRIDGE_USER_AGREEMENT_CONTRACT_ID}",
                "choice": "BridgeUserAgreement_Burn",
                "choiceArgument": {
                "amount": "${AMOUNT_IN_DECIMAL}",
                "destinationDomain": "0",
                "destinationRecipient": "${ETHEREUM_ADDRESS}",
                    "holdingCids": "${HOLDING_CONTRACT_IDS}",
                "requestId": "${UUID_REQUEST_ID}",
                "reference": "",
                "factoryCid": "${FACTORY_CID}",
                    "contextContractIds": "${CONTEXT_CONTRACT_IDS}"
                }
            }
        }
    ],
    "disclosedContracts": "${DISCLOSED_CONTRACTS}",
}
```

### Extracting Contract IDs and Disclosed Contracts

The utilities backend provides a Burn Mint Factory API Endpoint

Endpoint:

> \${UTILITY_BACKEND_URL}/api/utilities/v0/registry/burn-mint-instruction/v0/burn-mint-factory

Example request body:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "instrumentId": {
        "admin": "${ADMIN_PARTY_ID}",
        "id": "USDCx"
    },
    "inputHoldingCids": "${HOLDING_CONTRACT_IDS_IF_WITHDRAWING}",
    "outputs": [
        {
            "owner": "${ADMIN_PARTY_ID}",
            "amount": "${AMOUNT_IN_DECIMAL}" // For minting, this is the amount to mint. For burning, this is the change amount.
        }
    ]
}
```

***

When you call the Burn Mint factory endpoint, the response contains the contract IDs and disclosed contracts you need for both minting and withdrawing.

Note that these values can be cached to reduce api calls as these values change infrequently.

As an example for extracting the required contexts and contracts from the response:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Assume `response` is the parsed JSON from the API call
const choiceContext = response.httpResponse.body.choiceContext;

// Extract CONTEXT_CONTRACT_IDS
const values = choiceContext.choiceContextData.values;
const contextContractIds = {
    instrumentConfigurationCid: values["utility.digitalasset.com/instrument-configuration"].value,
    appRewardConfigurationCid: values["utility.digitalasset.com/app-reward-configuration"].value,
    featuredAppRightCid: values["utility.digitalasset.com/featured-app-right"].value,
};

// Extract FACTORY_CID
const factoryCid = response.httpResponse.body.factoryId;

// Extract DISCLOSED_CONTRACTS
const disclosedContracts = choiceContext.disclosedContracts;
```

### MainNet Environment Variables

| Variable                     | Value                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- |
| UTILITY\_BACKEND\_URL        | [https://api.utilities.digitalasset.com](https://api.utilities.digitalasset.com)                          |
| ADMIN\_PARTY\_ID             | decentralized-usdc-interchain-rep::12208115f1e168dd7e792320be9c4ca720c751a02a3053c7606e1c1cd3dad9bf60ef   |
| UTILITY\_OPERATOR\_PARTY\_ID | auth0\_007c6643538f2eadd3e573dd05b9::12205bcc106efa0eaa7f18dc491e5c6f5fb9b0cc68dc110ae66f4ed6467475d7c78e |
| BRIDGE\_OPERATOR\_PARTY\_ID  | Bridge-Operator::1220c8448890a70e65f6906bd48d797ee6551f094e9e6a53e329fd5b2b549334f13f                     |

### TestNet Environment Variables

| Variable                     | Value                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| UTILITY\_BACKEND\_URL        | [https://api.utilities.digitalasset-staging.com](https://api.utilities.digitalasset-staging.com)        |
| ADMIN\_PARTY\_ID             | decentralized-usdc-interchain-rep::122049e2af8a725bd19759320fc83c638e7718973eac189d8f201309c512d1ffec61 |
| UTILITY\_OPERATOR\_PARTY\_ID | DigitalAsset-UtilityOperator::12202679f2bbe57d8cba9ef3cee847ac8239df0877105ab1f01a77d47477fdce1204      |
| BRIDGE\_OPERATOR\_PARTY\_ID  | Bridge-Operator::12209d011ce250de439fefc35d16d1ab9d56fb99ccb24c18d798efb22352d533bcdb                   |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
