> Migrate 钱包 SDK 集成 from v0 to v1: 配置, namespaces, and per-namespace changes.

# 钱包 SDK v1 Migration Guide

钱包 SDK v1 is not backwards compatible with v0.

**Quick links**

* `钱包-sdk-config` - Detailed 配置 guide
* `preparing-and-signing-交易` - Preparing and signing 交易

We have removed the configure() and connect() pattern in favor of passing in a static 配置 or a 提供方 with ledger api capabilities.

Static 配置 initialization where we supply an auth config and a ledgerClientUrl:

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

提供方 intialization: The 提供方 is an abstraction that ultimately interacts with the Ledger (JSON LAPI). This can be implemented for either a dApp consumer, direct ledger 用户, or alternative transport channels such as 钱包 连接.

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Notice that `auth` and `ledgerClientUrl` are no longer needed
// when supplying sdk with custom provider
const sdk = await SDK.create(config, provider)
```

## Namespace changes

We have removed the controllers and replaced them with namespaces to appropriately segregate the 服务 layer in terms of business context. When the sdk is initialized, it has access to the 用户, keys, ledger, and party namespaces. The amulet, token, asset, and 事件 namespace can initialized with a separate config via `.extend()` 方法.

* [Party Namespace](#party-namespace)
* [Token Namespace](#token-namespace)
* [用户 Namespace](#用户-namespace)
* [Amulet Namespace](#amulet-namespace)
* [Ledger Namespace](#ledger-namespace)
* [Asset Namespace](#asset-namespace)

## Removed functionality

以下 方法 have been removed:

`sdk.connect()` No longer needed, SDK is connected on creation `sdk.connectAdmin()` No longer needed, admin operations are available in the ledger namespace and rights are extracted from the token. `sdk.connectTopology()` No longer needed, the grpc 端点 have been removed and replaced with ledger api 端点. `sdk.setPartyId()` Pass `partyId` explicitly to each operation

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  sdk.setPartyId(myPartyId)
  const holdingTransactionsmyPartyId = await sdk.tokenStandard?.listHoldingTransactions()
  sdk.setPartyId(myPartyId2)
  const holdingTransactionsmyPartyId2 = await sdk.tokenStandard?.listHoldingTransactions()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const holdingTransactionsmyPartyId = await token.holdings(myPartyId)
  const holdingTransactionsmyPartyId2 = await token.holdings(myPartyId2)
  ```
</div>

In v0, the controllers and sdk were stateful. In v1, party information should be passed explicitly to each function. This enables acting as multiple Party and allows for thread safety in concurrent use.

## Migration reference table

| v0 controller + 方法                                               | v1 namespace + 方法                                                                           |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `createKeyPair()`                                                    | `sdk.keys.generate()`                                                                           |
| `sdk.userLedger.signAndAllocateExternalParty(privateKey, partyHint)` | `sdk.party.external.create(publicKey, {partyHint}).sign(privateKey).execute()`                  |
| `sdk.userLedger.listWallets()`                                       | `sdk.party.list()`                                                                              |
| `sdk.userLedger.prepareSignExecuteAndWaitFor`                        | `sdk.ledger.prepare({partyId, 命令, disclosedContracts}).sign(privateKey).execute(partyId)` |
| `sdk.userLedger.activeContracts`                                     | `sdk.ledger.acs.read`                                                                           |
| `sdk.adminLedger.uploadDar`                                          | `sdk.ledger.dar.upload`                                                                         |
| `sdk.userLedger.isPackageUploaded`                                   | `sdk.ledger.dar.check`                                                                          |
| `sdk.adminLedger.createUser`                                         | `sdk.用户.create`                                                                               |
| `sdk.userLedger.grantRights`                                         | `sdk.用户.rights.grant`                                                                         |
| `sdk.tokenStandard.createTransfer`                                   | `sdk.token.transfer.create`                                                                     |
| `sdk.tokenStandard.exerciseTransferInstructionChoice`                | `sdk.token.transfer.accept` / `sdk.token.transfer.reject` / `sdk.token.transfer.withdraw`       |
| `sdk.tokenStandard.fetchPendingTransferInstructionView`              | `sdk.token.transfer.pending`                                                                    |
| `sdk.tokenStandard.listHoldingTransactions({partyId})`               | `sdk.token.持仓`                                                                            |
| `sdk.tokenStandard.listHoldingUtxos()`                               | `sdk.token.utxos.list({partyId})`                                                               |
| `sdk.tokenStandard.mergeHoldingUtxos`                                | `sdk.token.utxos.merge`                                                                         |
| `sdk.tokenStandard.fetchPendingAllocationRequestView`                | `sdk.token.allocation.pending(partyId, ALLOCATION_REQUEST_INTERFACE_ID)`                        |
| `sdk.tokenStandard.fetchPendingAllocationInstructionView`            | `sdk.token.allocation.pending(partyId, ALLOCATION_INSTRUCTION_INTERFACE_ID)`                    |
| `sdk.tokenStandard.fetchPendingAllocationView`                       | `sdk.token.allocation.pending(partyId)`                                                         |
| `sdk.tokenStandard.getAllocationExecuteTransferChoiceContext(cId)`   | `sdk.token.allocation.context.execute`                                                          |
| `sdk.tokenStandard.getAllocationWithdrawChoiceContext(cId)`          | `sdk.token.allocation.context.withdraw`                                                         |
| `sdk.tokenStandard.getAllocationCancelChoiceContext(cId)`            | `sdk.token.allocation.context.cancel`                                                           |
| `sdk.tokenStandard.getMemberTrafficStatus`                           | `sdk.amulet.流量.status`                                                                     |
| `sdk.tokenStandard.buyMemberTraffic`                                 | `sdk.amulet.流量.buy`                                                                        |
| `sdk.userLedger.createTransferPreapprovalCommand`                    | `sdk.amulet.preapproval.命令.create`                                                         |
| `sdk.tokenStandard.getTransferPreApprovalByParty`                    | `sdk.amulet.preapproval.fetchStatus`                                                            |
| `sdk.tokenStandard.createRenewTransferPreapproval`                   | `sdk.amulet.preapproval.renew`                                                                  |
| `sdk.tokenStandard.createCancelTransferPreapproval`                  | `sdk.amulet.preapproval.命令.cancel`                                                         |
| `sdk.tokenStandard.createTap`                                        | `sdk.amulet.tap`                                                                                |
| `sdk.tokenStandard.lookupFeaturedApps`                               | `sdk.amulet.featuredApp.rights`                                                                 |
| `sdk.tokenStandard.selfGrantFeatureAppRights`                        | `sdk.amulet.featuredApp.grant`                                                                  |
| `sdk.tokenStandard.getInstrumentById`                                | `sdk.asset.find`                                                                                |
| `sdk.tokenStandard.listInstruments`                                  | `sdk.asset.list`                                                                                |
| `sdk.userLedger.subscribeToUpdates`                                  | `sdk.事件.updates`                                                                            |
| `sdk.userLedger.subscribeToCompletions`                              | `sdk.事件.completions`                                                                        |

Migration reference table

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/party.rst" hash="bc376f31" */}

# Party Namespace

The party namespace provides 方法 to manage 钱包 Party on the Canton Network. In v1, the party namespace replaces the stateful party management from v0.

## Availability

The party namespace is always available as part of the basic SDK interface. It's initialized automatically when you create an SDK instance and doesn't require additional 配置 via `extend()`.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    // party namespace is immediately available
    await sdk.party.list()
}
```

## Key changes from v0 to v1

v0 used a stateful approach where you set a party context once with `sdk.setPartyId()`. All subsequent operations acted on that party.

v1 uses an explicit approach where you pass the party ID to each operation. This enables:

* Thread-safe concurrent operations
* Multi-party 交易 within the same 应用
* Clearer code intent

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  sdk.setPartyId(myPartyId)
  const result = await sdk.userLedger.doSomething()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const result = await sdk.ledger
      .prepare({ partyId: myPartyId, ... })
      .sign(privateKey)
      .execute({ partyId: myPartyId })
  ```
</div>

Refer to `preparing-and-signing-交易` for more information.

## Party types

**Internal Party**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const internalParty =
  await sdk.adminLedger!.allocateInternalParty(partyHint)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // v1 - no state, explicit party ID
  const internalParty = await sdk.party.internal.allocate({
      partyHint: 'my-service',
      synchronizerId: 'my-synchronizer-id'
  })
  ```
</div>

The below example demonstrates the full usage of the feature:

<div className="dropdown">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
</div>

**External Party**

An external party uses an external key pair for signing. You provide the public key, and the SDK generates the topology. You then sign the topology 交易 with your private key and execute it on the ledger.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const party = await sdk.userLedger?.signAndAllocateExternalParty(
          privateKey,
          partyHint
      )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const party = await sdk.party.external
      .create(publicKey, { partyHint: 'my-party' })
      .sign(privateKey)
      .execute()
  ```
</div>

<Note>
  我们建议 always providing a `partyHint` when creating a party. Refer to `party-hint` for more details.
</Note>

## Listing Party

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const wallets = await sdk.userLedger?.listWallets()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const partyIds = await sdk.party.list()
  ```
</div>

This 方法 returns all Party where the 用户 has `CanActAs`, `CanReadAs`, or `CanExecuteAs` rights. 若 用户 has admin rights, all local Party are returned.

## Offline signing 工作流

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const preparedParty = await sdk.userLedger?.generateExternalParty(
      keyPair.publicKey, partyHint
  )
  const allocatedParty = await sdk.userLedger?.allocateExternalParty(
      signature,
      preparedParty
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const party = await sdk.party.external
      .create(publicKey, options)
      .execute(signature, executeOptions)
  ```
</div>

## Migration reference

| v0 方法                                                            | v1 方法                                                                      |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `sdk.setPartyId(partyId)`                                            | Pass `partyId` explicitly to each operation                                    |
| `sdk.userLedger.listWallets()`                                       | `sdk.party.list()`                                                             |
| `sdk.userLedger.signAndAllocateExternalParty(privateKey, partyHint)` | `sdk.party.external.create(publicKey, {partyHint}).sign(privateKey).execute()` |
| `sdk.topology?.prepareExternalPartyTopology()`                       | `sdk.party.external.create().prepare()` (implicit on create)                   |
| `sdk.topology?.submitExternalPartyTopology()`                        | `sdk.party.external.create().sign().execute()`                                 |

Party-related 方法 migration

## See also

* `钱包-sdk-config` - SDK 配置
* `preparing-and-signing-交易` - 交易 lifecycle

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/token.rst" hash="7742b4ca" */}

# Token Namespace

The token namespace provides 方法 to manage token operations including transfers, 持仓, UTXOs, and allocations on the Canton Network. In v1, the token namespace replaces the `tokenStandard` controller from v0.

## Availability and extensibility

The token namespace is an extended namespace that requires 配置. 你可以 initialize it either during SDK creation or later using the `extend()` 方法.

**选项 1: Initialize during SDK creation**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const partyId = EXISTING_PARTY_1

    // token namespace is now available
    await sdk.token.utxos.list({ partyId })
}
```

**选项 2: 添加 token namespace later using extend()**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { SDK, localNetStaticConfig } from '@canton-network/wallet-sdk'

export default async function () {
    // Create basic SDK first
    const basicSDK = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    // Extend with token namespace when needed
    const extendedSDK = await basicSDK.extend({
        token: global.TOKEN_NAMESPACE_CONFIG,
    })

    const partyId = EXISTING_PARTY_1

    // Now token namespace is available
    await extendedSDK.token.utxos.list({ partyId })
}
```

## Key changes from v0 to v1

v0 used the `tokenStandard` controller with implicit party context set via `sdk.setPartyId()`.

v1 uses the `token` namespace where you:

* Pass `partyId` explicitly to each operation
* Initialize the namespace with 配置
* Access operations through logical groupings (`transfer`, `utxos`, `allocation`)

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  sdk.setPartyId(myPartyId)
  const holdings = await sdk.tokenStandard?.listHoldingTransactions()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const holdings = await sdk.token.holdings({ partyId: myPartyId })
  ```
</div>

This enables thread-safe concurrent operations and clearer code organization.

## Transfers

**Creating transfers**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const transfer = await sdk.tokenStandard.createTransfer(
      senderPartyId,
      recipientPartyId,
      amount.toString(),
      {
        instrumentId: 'Amulet',
        instrumentAdmin: instrumentAdminPartyId
      },
      registryUrl,
      memo
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const [command, disclosedContracts] = await sdk.token.transfer.create({
      sender: senderPartyId,
      recipient: recipientPartyId,
      amount: amount.toString(),
      instrumentId: 'Amulet',
      registryUrl,
      inputUtxos: ['utxo-1', 'utxo-2'],
      memo: 'Payment for services',
  })
  ```
</div>

**Accepting, rejecting, or withdrawing transfers**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.tokenStandard.exerciseTransferInstructionChoice(transferCid, choiceType /* 'Accept' | 'Withdraw' | 'Reject' */)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // Accept transfer
  const [acceptCommand, disclosed1] = await sdk.token.transfer.accept({
      transferInstructionCid,
      registryUrl,
  })

  // Reject transfer
  const [rejectCommand, disclosed2] = await sdk.token.transfer.reject({
      transferInstructionCid,
      registryUrl,
  })

  // Withdraw transfer
  const [withdrawCommand, disclosed3] = await sdk.token.transfer.withdraw({
      transferInstructionCid,
      registryUrl,
  })
  ```
</div>

**Listing pending transfers**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  const pending = await sdk.tokenStandard
      .fetchPendingTransferInstructionView()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const pending = await sdk.token.transfer.pending(myPartyId)
  ```
</div>

## 持仓

持仓 represent the 交易 history of token ownership for a party.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  const holdings = await sdk.tokenStandard
      .listHoldingTransactions()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const holdings = await sdk.token.holdings({ partyId })
  ```
</div>

你可以 also specify 偏移 for pagination:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const holdings = await sdk.token.holdings({
    partyId,
    afterOffset: 10,
    beforeOffset: 100,
})
```

交易 by updateId:

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  const tx = await sdk.tokenStandard.getTransactionById('my-update-id')
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const tx = await sdk.token.transactionsById({ updateId, partyId })
  ```
</div>

## UTXOs

UTXOs (Unspent 交易 Outputs) are the actual holding 合约 that represent token balances.

**Listing UTXOs**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  // List all UTXOs including locked ones
  const allUtxos = await sdk.tokenStandard?.listHoldingUtxos()

  // List only unlocked UTXOs
  const usableUtxos = await sdk.tokenStandard?.listHoldingUtxos(false)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // List only unlocked UTXOs (default)
  const usableUtxos = await sdk.token.utxos.list({
      partyId
  })

  // List all UTXOs including locked ones
  const allUtxos = await sdk.token.utxos.list({
      partyId,
      includeLocked: true,
  })
  ```
</div>

你可以 specify additional parameters for pagination and limits:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const utxos = await sdk.token.utxos.list({
    partyId,
    includeLocked: false,
    limit: 100,
    offset: 0,
    continueUntilCompletion: false,
})
```

**Merging UTXOs**

Merging consolidates multiple small UTXOs into larger ones to improve performance.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  const [commands, disclosedContracts] =
      await sdk.tokenStandard.mergeHoldingUtxos(nodeLimit)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const [commands, disclosedContracts] = await sdk.token.utxos.merge({
      partyId,
      nodeLimit: 200,
      memo: 'merge-utxos',
  })
  ```
</div>

The merge operation groups UTXOs by instrument and creates self-transfers to consolidate them. 你可以 optionally provide specific UTXOs to merge:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const [commands, disclosedContracts] = await sdk.token.utxos.merge({
    partyId,
    inputUtxos,
    memo: 'custom merge',
})
```

## Allocation

Allocations handle the issuance and distribution of new tokens.

**Listing pending allocations**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.setPartyId(partyId)
  // Allocation requests
  const requests = await sdk.tokenStandard
      .fetchPendingAllocationRequestView()

  // Allocation instructions
  const instructions = await sdk.tokenStandard
      .fetchPendingAllocationInstructionView()

  // Allocations
  const allocations = await sdk.tokenStandard
      .fetchPendingAllocationView()
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // All pending allocations (default)
  const allocations = await sdk.token.allocation.pending(myPartyId)
  ```
</div>

The `pending` 方法 accepts an optional interface ID to filter by allocation type:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
    ALLOCATION_REQUEST_INTERFACE_ID,
    ALLOCATION_INSTRUCTION_INTERFACE_ID,
    ALLOCATION_INTERFACE_ID,
} from '@canton-network/core-token-standard'

// Filter by specific type
const requests = await sdk.token.allocation.pending(
    myPartyId,
    ALLOCATION_REQUEST_INTERFACE_ID
)
```

**Executing, withdrawing or cancelling allocations**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const [command, disclosedContracts] = await sdk.tokenStandard.exerciseAllocationChoice(allocationCid, choice /* 'ExecuteTransfer' | 'Withdraw' | 'Cancel' */)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // Execute allocation
  const [executeCommand, disclosedContracts1] = await sdk.token.allocation.execute({
      allocationCid,
      asset
  })

   // Withdraw allocation
  const [withdrawCommand, disclosedContracts2] = await sdk.token.allocation.withdraw({
      allocationCid,
      asset,
  })

  // Cancel allocation
  const [cancelCommand, disclosedContracts3] = await sdk.token.allocation.cancel({
      allocationCid,
      asset,
  })
  ```
</div>

## Migration reference

| v0 方法                                                 | v1 方法                                                                                 |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `sdk.tokenStandard.createTransfer`                        | `sdk.token.transfer.create`                                                               |
| `sdk.tokenStandard.exerciseTransferInstructionChoice`     | `sdk.token.transfer.accept` / `sdk.token.transfer.reject` / `sdk.token.transfer.withdraw` |
| `sdk.tokenStandard.fetchPendingTransferInstructionView`   | `sdk.token.transfer.pending`                                                              |
| `sdk.tokenStandard.listHoldingTransactions({partyId})`    | `sdk.token.持仓({partyId})`                                                           |
| `sdk.tokenStandard.listHoldingUtxos()`                    | `sdk.token.utxos.list({partyId})`                                                         |
| `sdk.tokenStandard.mergeHoldingUtxos`                     | `sdk.token.utxos.merge`                                                                   |
| `sdk.tokenStandard.fetchPendingAllocationRequestView`     | `sdk.token.allocation.pending(partyId, ALLOCATION_REQUEST_INTERFACE_ID)`                  |
| `sdk.tokenStandard.fetchPendingAllocationInstructionView` | `sdk.token.allocation.pending(partyId, ALLOCATION_INSTRUCTION_INTERFACE_ID)`              |
| `sdk.tokenStandard.fetchPendingAllocationView`            | `sdk.token.allocation.pending(partyId)`                                                   |

Token-related 方法 migration

## See also

* `钱包-sdk-config` - SDK 配置
* `preparing-and-signing-交易` - 交易 lifecycle

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/用户.rst" hash="7cf5184f" */}

# 用户 Namespace

The 用户 namespace provides 方法 for 用户 management on the Canton Network.

## Availability

The 用户 namespace is always available as part of the basic SDK interface. It's initialized automatically when you create an SDK instance and doesn't require additional 配置 via `extend()`.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
    })

    const primaryParty = EXISTING_PARTY_1
    const userId = 'user-id'

    // user namespace is immediately available
    await sdk.user.create({ userId, primaryParty })
}
```

## Key changes from v0 to v1

The distinction betwen the 用户 ledger and admin ledger have been removed. Instead, the token is used to determine whether a 用户 has admin rights.

**Creating 用户**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.adminLedger.createUser('userId', primaryParty)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const result = await sdk.user
      .create({
        userId: 'userId',
        primaryParty: primaryParty,
        userRights: {...}
      })
  ```
</div>

**Granting 用户 rights**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.userLedger.grantRights([actAsRights], [readAsRights])
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const result = await sdk.rights
      .grant({
        userRights: {...},
        userId: {'userId'}, //optional parameter
        idp: {'idp'} //optional parameter otherwise will use default IDP
      })
  ```
</div>

The below example demonstrates the full usage of the feature:

<div className="dropdown">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
</div>

## Migration reference

| v0 方法                    | v1 方法               |
| ---------------------------- | ----------------------- |
| `sdk.adminLedger.createUser` | `sdk.用户.create`       |
| `sdk.userLedger.grantRights` | `sdk.用户.rights.grant` |

用户 namespace migration

## See also

* `钱包-sdk-config` - SDK 配置
* `用户 management` - 用户 management overview

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/amulet.rst" hash="3ccdd060" */}

# Amulet Namespace

The amulet namespace is used for Canton coin specific operations.

## Availability and extensibility

The amulet namespace is an extended namespace that requires 配置. 你可以 initialize it either during SDK creation or later using the `extend()` 方法.

**选项 1: Initialize during SDK creation**

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const sdk = await SDK.create({
    auth: authConfig,
    ledgerClientUrl: 'http://localhost:2975',
    amulet: {
        validatorUrl: 'http://localhost:2000/api/validator',
        scanApiUrl: 'http://localhost:2000/api/scan',
        auth: amuletAuthConfig,
        registryUrl: 'http://localhost:2000/api/registry'
    }
})

// amulet namespace is now available
await sdk.amulet.traffic.status()
```

**选项 2: 添加 amulet namespace later using extend()**

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Create basic SDK first
const basicSDK = await SDK.create({
    auth: authConfig,
    ledgerClientUrl: 'http://localhost:2975'
})

// Extend with amulet namespace when needed
const extendedSDK = await basicSDK.extend({
    amulet: {
        validatorUrl: 'http://localhost:2000/api/validator',
        scanApiUrl: 'http://localhost:2000/api/scan',
        auth: amuletAuthConfig,
        registryUrl: 'http://localhost:2000/api/registry'
    }
})

// Now amulet namespace is available
await extendedSDK.amulet.traffic.status()
```

## 配置

The `AmuletConfig` type defines the 配置 for the amulet namespace:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AmuletConfig = {
    auth: TokenProviderConfig
    validatorUrl: string | URL
    scanApiUrl: string | URL
    registryUrl: URL
}
```

* `auth`: 认证 配置 for accessing the validator and scan 服务
* `validatorUrl`: URL of the validator 服务
* `scanApiUrl`: URL of the scan API
* `registryUrl`: URL of the amulet registry

## Key changes from v0 to v1

v0 used the `tokenStandard` controller with implicit party context set via `sdk.setPartyId()` and the instrumentId and instrumentAdmin were passed in explicitly to each function.

v1 uses the `amulet` namespace where you:

* Pass `partyId` explicitly to each operation
* Initialize the namespace with 配置, which determines the instrumentAdmin and instrumentId
* Access operations through logical groupings (`流量` and `preapproval`)

**Creating preapprovals**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const transferPreApprovalProposal =
     await sdk.userLedger?.createTransferPreapprovalCommand(
        validatorOperatorParty!,
        receiver?.partyId!,
        instrumentAdminPartyId
     )

  await sdk.userLedger?.prepareSignExecuteAndWaitFor(
     [transferPreApprovalProposal],
     keyPairReceiver.privateKey,
     v4()
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const createPreapprovalCommand = await sdk.amulet.preapproval.command.create({
     parties: {
        receiver: partyId,
     },
  })

  await sdk.ledger
        .prepare({
           partyId: partyId,
           commands: createPreapprovalCommand,
        })
        .sign(privateKey)
        .execute({
           partyId: partyId,
        })
  ```
</div>

The below example demonstrates the full process of renewing and cancelling preapprovals:

<div className="dropdown">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
</div>

**Buy Member 流量**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const buyMemberTrafficCommand =
     await sdk.tokenStandard.buyMemberTraffic(
        senderPartyId,
        amount,
        participantId,
        inputUtxosOptional
     )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const [buyTrafficCommand, buyTrafficDisclosedContracts] =
     await sdk.amulet.traffic.buy({
        buyer,
        ccAmount,
        inputUtxos: [],
     })
  ```
</div>

**检查 流量 Status**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.tokenStandard.getMemberTrafficStatus(participantId)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.amulet.traffic.status()
  ```
</div>

Refer to the following example for more information:

<div className="dropdown">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import pino from 'pino'
  import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
  import {
      TOKEN_NAMESPACE_CONFIG,
      TOKEN_PROVIDER_CONFIG_DEFAULT,
      AMULET_NAMESPACE_CONFIG,
  } from './utils/index.js'

  const logger = pino({ name: 'v1-06-merge-utxos', level: 'info' })

  const sdk = await SDK.create({
      auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
      ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
      token: TOKEN_NAMESPACE_CONFIG,
      amulet: AMULET_NAMESPACE_CONFIG,
  })
  const aliceKeys = sdk.keys.generate()

  const alice = await sdk.party.external
      .create(aliceKeys.publicKey, {
          partyHint: 'v1-07-alice',
      })
      .sign(aliceKeys.privateKey)
      .execute()

  const bobKeys = sdk.keys.generate()

  const bob = await sdk.party.external
      .create(bobKeys.publicKey, {
          partyHint: 'v1-07-bob',
      })
      .sign(bobKeys.privateKey)
      .execute()

  const createPreapprovalCommand = await sdk.amulet.preapproval.command.create({
      parties: {
          receiver: bob.partyId,
      },
  })

  await sdk.ledger
      .prepare({
          partyId: bob.partyId,
          commands: createPreapprovalCommand,
      })
      .sign(bobKeys.privateKey)
      .execute({
          partyId: bob.partyId,
      })

  // Mint holdings for alice

  const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
      alice.partyId,
      '2000000'
  )

  await sdk.ledger
      .prepare({
          partyId: alice.partyId,
          commands: amuletTapCommand,
          disclosedContracts: amuletTapDisclosedContracts,
      })
      .sign(aliceKeys.privateKey)
      .execute({ partyId: alice.partyId })

  logger.info(`Tapped holdings for alice`)

  const trafficStatusBeforePurchase = await sdk.amulet.traffic.status()

  logger.info(
      `Traffic status before purchase: ${JSON.stringify(trafficStatusBeforePurchase)}`
  )

  const ccAmount = 200000

  const [buyTrafficCommand, buyTrafficDisclosedContracts] =
      await sdk.amulet.traffic.buy({
          buyer: alice.partyId,
          ccAmount,
          inputUtxos: [],
      })

  await sdk.ledger
      .prepare({
          partyId: alice.partyId,
          commands: buyTrafficCommand,
          disclosedContracts: buyTrafficDisclosedContracts,
      })
      .sign(aliceKeys.privateKey)
      .execute({ partyId: alice.partyId })

  logger.info(`buy member traffic for sender (${alice.partyId}) party completed`)

  const utxos = await sdk.token.utxos.list({ partyId: alice.partyId })
  logger.info(utxos, 'alice utxos')

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

  //TODO: This does not work when we run multiple code snippets parallel

  // await new Promise((resolve) => setTimeout(resolve, 61_000))

  // const trafficStatusAfterPurchaseAndSomeTime = await amulet.traffic.status()

  // const difference =
  //     trafficStatusAfterPurchaseAndSomeTime.traffic_status.target
  //         .total_purchased -
  //     trafficStatusBeforePurchase.traffic_status.target.total_purchased

  // if (difference === ccAmount) {
  //     logger.info(
  //         {
  //             trafficStatusBeforePurchase,
  //             trafficStatusAfterPurchaseAndSomeTime,
  //         },
  //         'MemberTraffic status. Traffic purchased successfully'
  //     )
  // } else {
  //     logger.error(
  //         {
  //             trafficStatusBeforePurchase,
  //             trafficStatusAfterPurchaseAndSomeTime,
  //         },
  //         'MemberTraffic status.'
  //     )
  //     throw new Error(
  //         `Member traffic difference is ${difference}, expected ${ccAmount} `
  //     )
  // }
  ```
</div>

**Tap**

The is useful for 测试 against LocalNet or Devnet.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.tokenStandard.createTap(partyId,
         amount,
         {
         instrumentId,
         instrumentAdmin
         })
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.amuet.tap(partyId, amount)
  ```
</div>

## Migration reference

| v0 方法                                           | v1 方法                               |
| --------------------------------------------------- | --------------------------------------- |
| `sdk.tokenStandard.getMemberTrafficStatus`          | `sdk.amulet.流量.status`             |
| `sdk.tokenStandard.buyMemberTraffic`                | `sdk.amulet.流量.buy`                |
| `sdk.userLedger.createTransferPreapprovalCommand`   | `sdk.amulet.preapproval.命令.create` |
| `sdk.tokenStandard.getTransferPreApprovalByParty`   | `sdk.amulet.preapproval.fetchStatus`    |
| `sdk.tokenStandard.createRenewTransferPreapproval`  | `sdk.amulet.preapproval.renew`          |
| `sdk.tokenStandard.createCancelTransferPreapproval` | `sdk.amulet.preapproval.命令.cancel` |
| `sdk.tokenStandard.createTap`                       | `sdk.amulet.tap`                        |
| `sdk.tokenStandard.lookupFeaturedApps`              | `sdk.amulet.featuredApp.rights`         |
| `sdk.tokenStandard.selfGrantFeatureAppRights`       | `sdk.amulet.featuredApp.grant`          |

Amulet namespace migration

## See also

* `钱包-sdk-config` - SDK 配置
* `用户 management` - 用户 management overview

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/ledger.rst" hash="2d397a68" */}

# Ledger Namespace

The ledger namespace is used for preparing, signing, and executing 交易 and other Ledger API operations.

## Availability

The ledger namespace is always available as part of the basic SDK interface. It's initialized automatically when you create an SDK instance and doesn't require additional 配置 via `extend()`.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'

export default async function () {
    const sdk = await SDK.create({
        auth: global.TOKEN_PROVIDER_CONFIG_DEFAULT,
        ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
        amulet: global.AMULET_NAMESPACE_CONFIG,
    })

    const partyId = EXISTING_PARTY_1
    const privateKey = EXISTING_PARTY_1_KEYS.privateKey

    const [commands, disclosedContracts] = await sdk.amulet.tap(partyId, '200')

    // ledger namespace is immediately available
    await sdk.ledger
        .prepare({ partyId, commands, disclosedContracts })
        .sign(privateKey)
        .execute({ partyId })
}
```

## Key changes from v0 to v1

v0 used the `userLedger` or `adminLedger` controller with implicit party context set via `sdk.setPartyId()`.

v1 uses the `ledger` namespace where you:

* Pass `partyId` explicitly to each operation
* Have an explicit lifecycle with `prepare/sign/execute` chain instead of a single 方法
* Access operations through logical groupings (`external`, `internal`, `dar`, and `acs`)

**准备, signing, and executing 交易**

Previously, a single 方法 would handle everything.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.userLedger.prepareSignExecuteAndWaitFor(
     commands,
     privateKey,
     workFlowId,
     disclosedContracts
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  await sdk.ledger
        .prepare({
           partyId: partyId,
           commands: [...],
        })
        .sign(privateKey)
        .execute({
           partyId: partyId,
        })
  ```
</div>

Each step in lifecycle is clearer, workflowIds are generated automatically and there is better typesafety at each step.

The below example demonstrates how offline signing works.

<div className="dropdown">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

**Active 合约 设置 (ACS) queries**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const contracts = await sdk.userLedger.activeContracts({
     offset,
     templateIds: [...],
     parties: [],
     filterByParty: true
  })

  const contractId = LedgerController.getActiveContractCid(contracts?.[0]?.contractEntry!)
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const contracts = await sdk.ledger.acs.read({
     parties: [...],
     templateIds: [...],
     filterByParty: true
  })

  const contractId = contracts[0].contractId
  ```
</div>

No need to manually enter get the ledger end for the 偏移 and there is direct extraction of the activeContracts. However, we still have an `acs.readRaw` 方法 for unfiltered results.

**DAR management**

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const isPackageUploaded = await sdk.userLedger.isPackageUploaded(PACKAGED_ID)

  if(!isPackageUploaded){
     await sdk.adminLedger.uploadDar(darBytes)
  }
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  //automatically checks if uploaded and skips if present
  await sdk.ledger.dar.upload(darBytes, packageId)
  ```
</div>

## Migration reference

| v0 方法                                     | v1 方法                                                                                       |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `sdk.userLedger.prepareSignExecuteAndWaitFor` | `sdk.ledger.prepare({partyId, 命令, disclosedContracts}).sign(privateKey).execute(partyId)` |
| `sdk.userLedger.activeContracts`              | `sdk.ledger.acs.read`                                                                           |
| `sdk.adminLedger.uploadDar`                   | `sdk.ledger.dar.upload`                                                                         |
| `sdk.userLedger.isPackageUploaded`            | `sdk.ledger.dar.check`                                                                          |

Ledger namespace migration

## See also

* `钱包-sdk-config` - SDK 配置
* `preparing-and-signing-交易` - 交易 lifecycle

{/* COPIED_START source="splice-wallet-kernel:docs/wallet-integration-guide/src/钱包-sdk-v1-migration-guide/asset.rst" hash="35d418f7" */}

# Asset Namespace

The asset namespace provides 方法 to discover and find token assets from registries on the Canton Network. In v1, the asset namespace introduces a dedicated API for asset discovery and management.

## Key changes from v0 to v1

v0 required accessing asset information through the token standard 服务 or by manually querying registries.

v1 introduces a dedicated asset namespace with a clean API for asset discovery. This enables:

* Simplified asset discovery from multiple registries
* 类型-safe asset information retrieval
* Centralized asset registry management
* Built-in 错误 handling for asset not found scenarios

## Availability and extensibility

The asset namespace is an extended namespace that requires 配置. 你可以 initialize it either during SDK creation or later using the `extend()` 方法.

**选项 1: Initialize during SDK creation**

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const sdk = await SDK.create({
    auth: authConfig,
    ledgerClientUrl: 'http://localhost:2975',
    asset: {
        auth: assetAuthConfig,
        registries: [new URL('http://localhost:2000/api/registry')]
    }
})

// asset namespace is now available
const assetList = sdk.asset.list
```

**选项 2: 添加 asset namespace later using extend()**

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Create basic SDK first
const basicSDK = await SDK.create({
    auth: authConfig,
    ledgerClientUrl: 'http://localhost:2975'
})

// Extend with asset namespace when needed
const extendedSDK = await basicSDK.extend({
    asset: {
        auth: assetAuthConfig,
        registries: [new URL('http://localhost:2000/api/registry')]
    }
})

// Now asset namespace is available
const assetList = extendedSDK.asset.list
```

## 配置

The `AssetConfig` type defines the 配置 for the asset namespace:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AssetConfig = {
    auth: TokenProviderConfig
    registries: URL[]
}
```

* `auth`: 认证 配置 for accessing registries
* `registries`: Array of registry URLs to fetch assets from

你可以 preview the example config here:

<div className="dropdown">
  ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import { JSContractEntry } from '@canton-network/core-ledger-client'
  import {
      TokenProviderConfig,
      localNetStaticConfig,
  } from '@canton-network/wallet-sdk'
  import {
      TokenConfig,
      AmuletConfig,
      AssetConfig,
  } from '@canton-network/wallet-sdk'

  export function getActiveContractCid(entry: JSContractEntry) {
      if ('JsActiveContract' in entry) {
          return entry.JsActiveContract.createdEvent.contractId
      }
  }

  export const TOKEN_PROVIDER_CONFIG_DEFAULT: TokenProviderConfig = {
      method: 'self_signed',
      issuer: 'unsafe-auth',
      credentials: {
          clientId: localNetStaticConfig.LOCALNET_USER_ID,
          clientSecret: 'unsafe',
          audience: 'https://canton.network.global',
          scope: '',
      },
  }
  export const TOKEN_NAMESPACE_CONFIG: TokenConfig = {
      validatorUrl: localNetStaticConfig.LOCALNET_APP_VALIDATOR_URL,
      registries: [localNetStaticConfig.LOCALNET_REGISTRY_API_URL],
      auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
  }

  export const AMULET_NAMESPACE_CONFIG: AmuletConfig = {
      validatorUrl: localNetStaticConfig.LOCALNET_APP_VALIDATOR_URL,
      scanApiUrl: localNetStaticConfig.LOCALNET_SCAN_API_URL,
      auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
      registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
  }

  export const ASSET_CONFIG: AssetConfig = {
      registries: [localNetStaticConfig.LOCALNET_REGISTRY_API_URL],
      auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
  }
  ```
</div>

## Listing assets

The asset namespace provides a `list` getter to retrieve all assets from configured registries.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // v0 - manually fetch from token standard service
  const tokenStandardService = new TokenStandardService(
      provider, logger, auth, false
  )
  const assetList = await tokenStandardService.registriesToAssets(
      registries.map((url) => url.href)
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const assetList = sdk.asset.list
  ```
</div>

## Finding a specific asset

The `find` 方法 allows you to search for a specific asset by ID, optionally filtering by registry URL.

<div className="before-after">
  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  // v0 - manually filter assets
  const tokenStandardService = new TokenStandardService(
      provider, logger, auth, false
  )
  const assets = await tokenStandardService.registriesToAssets(
      registries.map((url) => url.href)
  )
  const amuletAsset = assets.find(
      (asset) => asset.id === 'Amulet'
  )
  ```

  ***

  ```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  const amuletAsset = await sdk.asset.find('Amulet')
  ```
</div>

### Finding an asset with a specific registry

When multiple registries contain assets with the same ID, you can specify the registry URL to disambiguate:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const amuletAsset = await sdk.asset.find(
    'Amulet',
    new URL('https://registry.example.com')
)
```

## 错误 handling

The asset namespace includes built-in 错误 handling for common scenarios:

**Asset not found**

If an asset with the specified ID does not exist in any registry:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
try {
    const unknownAsset = await sdk.asset.find('NonExistentAsset')
} catch (error) {
    // SDKError with type 'NotFound'
    // message: 'Asset with id NonExistentAsset not found'
}
```

**Multiple assets found**

If multiple assets with the same ID exist across different registries and no registry URL is provided:

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
try {
    const duplicateAsset = await sdk.asset.find('CommonAsset')
} catch (error) {
    // SDKError with type 'BadRequest'
    // message: 'Multiple assets found, please provide a registryUrl'
}
```

## Usage example

In the below example you can find the usage of the `find` 方法:

<div className="dropdown">
  ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
  import pino from 'pino'
  import { localNetStaticConfig, SDK } from '@canton-network/wallet-sdk'
  import path from 'path'
  import { fileURLToPath } from 'url'
  import fs from 'fs/promises'
  import { KeyPair } from '@canton-network/core-signing-lib'
  import { ASSET_CONFIG } from './utils/index.js'
  import { GenerateTransactionResponse } from '@canton-network/core-ledger-client'
  import {
      TOKEN_NAMESPACE_CONFIG,
      TOKEN_PROVIDER_CONFIG_DEFAULT,
      AMULET_NAMESPACE_CONFIG,
  } from './utils/index.js'

  const logger = pino({ name: 'v1-token-standard-allocation', level: 'info' })

  type PartyInfo = Omit<GenerateTransactionResponse, 'topologyTransactions'> & {
      topologyTransactions?: string[] | undefined
      keyPair: KeyPair
  }

  const sdk = await SDK.create({
      auth: TOKEN_PROVIDER_CONFIG_DEFAULT,
      ledgerClientUrl: localNetStaticConfig.LOCALNET_APP_USER_LEDGER_URL,
      token: TOKEN_NAMESPACE_CONFIG,
      amulet: AMULET_NAMESPACE_CONFIG,
      asset: ASSET_CONFIG,
  })

  // This example needs uploaded .dar for splice-token-test-trading-app
  // It's in files of localnet, but it's not uploaded to participant, so we need to do this in the script
  // Adjust if to your .localnet location
  const PATH_TO_LOCALNET = '../../../../.localnet'
  const PATH_TO_DAR_IN_LOCALNET = '/dars/splice-token-test-trading-app-1.0.0.dar'
  const TRADING_APP_PACKAGE_ID =
      'e5c9847d5a88d3b8d65436f01765fc5ba142cc58529692e2dacdd865d9939f71'

  const here = path.dirname(fileURLToPath(import.meta.url))

  const tradingDarPath = path.join(
      here,
      PATH_TO_LOCALNET,
      PATH_TO_DAR_IN_LOCALNET
  )

  //upload dar
  const darBytes = await fs.readFile(tradingDarPath)
  await sdk.ledger.dar.upload(darBytes, TRADING_APP_PACKAGE_ID)

  //allocate parties
  const allocatedParties = await Promise.all(
      ['v1-04-alice', 'v1-04-bob', 'v1-04-venue'].map(async (partyHint) => {
          const partyKeys = sdk.keys.generate()
          const party = await sdk.party.external
              .create(partyKeys.publicKey, {
                  partyHint,
              })
              .sign(partyKeys.privateKey)
              .execute()

          return [
              partyHint,
              {
                  partyId: party.partyId,
                  publicKeyFingerprint: party.publicKeyFingerprint,
                  multiHash: party.multiHash,
                  topologyTransactions: party.topologyTransactions,
                  keyPair: partyKeys,
              },
          ] as const
      })
  )

  const partyInfo: Map<string, PartyInfo> = new Map(allocatedParties)

  const sender = partyInfo.get('v1-04-alice')!
  const recipient = partyInfo.get('v1-04-bob')!
  const venue = partyInfo.get('v1-04-venue')!

  // Mint holdings for alice

  const [amuletTapCommand, amuletTapDisclosedContracts] = await sdk.amulet.tap(
      sender.partyId,
      '2000000'
  )

  await sdk.ledger
      .prepare({
          partyId: sender.partyId,
          commands: amuletTapCommand,
          disclosedContracts: amuletTapDisclosedContracts,
      })
      .sign(sender.keyPair.privateKey)
      .execute({ partyId: sender.partyId })

  // Mint holdings for bob

  const [amuletTapCommandBob, amuletTapDisclosedContractsBob] =
      await sdk.amulet.tap(recipient.partyId, '2000000')

  await sdk.ledger
      .prepare({
          partyId: recipient.partyId,
          commands: amuletTapCommandBob,
          disclosedContracts: amuletTapDisclosedContractsBob,
      })
      .sign(recipient.keyPair.privateKey)
      .execute({ partyId: recipient.partyId })

  //Alice creates OTCTradeProposal

  const amuletAsset = await sdk.asset.find(
      'Amulet',
      localNetStaticConfig.LOCALNET_REGISTRY_API_URL
  )

  const transferLegs = {
      leg0: {
          sender: sender.partyId,
          receiver: recipient.partyId,
          amount: '100',
          instrumentId: { admin: amuletAsset.admin, id: 'Amulet' },
          meta: { values: {} },
      },
      leg1: {
          sender: recipient.partyId,
          receiver: sender.partyId,
          amount: '20',
          instrumentId: { admin: amuletAsset.admin, id: 'Amulet' },
          meta: { values: {} },
      },
  }

  const createProposal = {
      CreateCommand: {
          templateId:
              '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTradeProposal',
          createArguments: {
              venue: venue.partyId,
              tradeCid: null,
              transferLegs,
              approvers: [sender.partyId],
          },
      },
  }

  await sdk.ledger
      .prepare({
          partyId: sender.partyId,
          commands: createProposal,
          disclosedContracts: [],
      })
      .sign(sender.keyPair.privateKey)
      .execute({ partyId: sender.partyId })

  logger.info(
      'OTC Trade Proposal created by Alice, ready for Bob to accept OTCTradeProposal'
  )

  // Bob accepts OTCTradeProposal

  const activeTradeProposals = await sdk.ledger.acsReader.readJsContracts({
      templateIds: [
          '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTradeProposal',
      ],
      parties: [recipient.partyId],
      filterByParty: true,
  })

  const otcpCid = activeTradeProposals[0].contractId

  if (otcpCid === undefined) {
      throw new Error('Unexpected lack of OTCTradeProposal contract')
  }
  const acceptCmd = [
      {
          ExerciseCommand: {
              templateId:
                  '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTradeProposal',
              contractId: otcpCid,
              choice: 'OTCTradeProposal_Accept',
              choiceArgument: { approver: recipient.partyId },
          },
      },
  ]

  await sdk.ledger
      .prepare({
          partyId: recipient.partyId,
          commands: acceptCmd,
          disclosedContracts: [],
      })
      .sign(recipient.keyPair.privateKey)
      .execute({ partyId: recipient.partyId })

  logger.info('Bob accepted OTCTradeProposal')

  //Venue initiates settlement of OTCTradeProposal

  const activeTradeProposals2 = await sdk.ledger.acsReader.readJsContracts({
      templateIds: [
          '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTradeProposal',
      ],
      parties: [venue.partyId],
      filterByParty: true,
  })

  const now = new Date()
  const prepareUntil = new Date(now.getTime() + 60 * 60 * 1000).toISOString()
  const settleBefore = new Date(now.getTime() + 2 * 60 * 60 * 1000).toISOString()

  const otcpCid2 = activeTradeProposals2[0].contractId

  const initiateSettlementCmd = [
      {
          ExerciseCommand: {
              templateId:
                  '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTradeProposal',
              contractId: otcpCid2,
              choice: 'OTCTradeProposal_InitiateSettlement',
              choiceArgument: { prepareUntil, settleBefore },
          },
      },
  ]

  await sdk.ledger
      .prepare({
          partyId: venue.partyId,
          commands: initiateSettlementCmd,
          disclosedContracts: [],
      })
      .sign(venue.keyPair.privateKey)
      .execute({ partyId: venue.partyId })

  logger.info('Venue initated settlement of OTCTradeProposal')

  const otcTrades = await sdk.ledger.acsReader.readJsContracts({
      templateIds: [
          '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTrade',
      ],
      parties: [venue.partyId],
      filterByParty: true,
  })

  const otcTradeCid = otcTrades[0].contractId
  if (!otcTradeCid) throw new Error('OTCTrade not found for venue')

  logger.info({ otcTradeCid }, `OtcTrades were found`)

  const pendingAllocationRequestsAlice =
      await sdk.token.allocation.request.pending(sender.partyId)

  const allocationRequestViewAlice =
      pendingAllocationRequestsAlice?.[0].interfaceViewValue!

  const legIdAlice = Object.keys(allocationRequestViewAlice.transferLegs).find(
      (key) =>
          allocationRequestViewAlice.transferLegs[key].sender === sender.partyId
  )!
  if (!legIdAlice) throw new Error(`No leg found for Alice`)

  const legAlice = allocationRequestViewAlice.transferLegs[legIdAlice]

  const specAlice = {
      settlement: allocationRequestViewAlice.settlement,
      transferLegId: legIdAlice,
      transferLeg: legAlice,
  }

  //TODO: go over if we should pass in expectedAdmin or instrumentId/registryUrl

  const [allocateCmdAlice, allocateDisclosedAlice] =
      await sdk.token.allocation.instruction.create({
          allocationSpecification: specAlice,
          asset: amuletAsset,
      })

  await sdk.ledger
      .prepare({
          partyId: sender.partyId,
          commands: allocateCmdAlice,
          disclosedContracts: allocateDisclosedAlice,
      })
      .sign(sender.keyPair.privateKey)
      .execute({ partyId: sender.partyId })

  logger.info('Alice created Allocation for her TransferLeg')

  const pendingAllocationRequestsBob = await sdk.token.allocation.request.pending(
      recipient.partyId
  )

  const allocationRequestViewBob =
      pendingAllocationRequestsBob?.[0].interfaceViewValue!

  const legIdBob = Object.keys(allocationRequestViewAlice.transferLegs).find(
      (key) =>
          allocationRequestViewAlice.transferLegs[key].sender ===
          recipient!.partyId
  )!
  if (!legIdBob) throw new Error(`No leg found for Bob`)

  const legBob = allocationRequestViewAlice.transferLegs[legIdBob]

  const specBob = {
      settlement: allocationRequestViewBob.settlement,
      transferLegId: legIdBob,
      transferLeg: legBob,
  }

  //TODO: go over if we should pass in expectedAdmin or instrumentId/registryUrl

  const [allocateCmdBob, allocateDisclosedBlice] =
      await sdk.token.allocation.instruction.create({
          allocationSpecification: specBob,
          asset: amuletAsset,
      })

  await sdk.ledger
      .prepare({
          partyId: recipient.partyId,
          commands: allocateCmdBob,
          disclosedContracts: allocateDisclosedBlice,
      })
      .sign(recipient.keyPair.privateKey)
      .execute({ partyId: recipient.partyId })

  logger.info('Bob created Allocation for his TransferLeg')

  // Once the legs have been allocated, venue settles the trade triggering transfer of holdings

  const allocationsVenue = await sdk.token.allocation.pending(venue.partyId)

  const settlementRefId = allocationRequestViewAlice.settlement.settlementRef.id
  const relevantAllocations = allocationsVenue.filter(
      (a) =>
          a.interfaceViewValue.allocation.settlement.executor ===
              venue!.partyId &&
          a.interfaceViewValue.allocation.settlement.settlementRef.id ===
              settlementRefId
  )

  if (relevantAllocations.length === 0)
      throw new Error('No matching allocations for this trade')

  const allocationEntries = await Promise.all(
      relevantAllocations.map(async (a) => {
          const cid = a.contractId
          const choiceContext = await sdk.token.allocation.context.execute({
              allocationCid: cid,
              registryUrl: localNetStaticConfig.LOCALNET_REGISTRY_API_URL,
          })

          return {
              cid,
              legId: a.interfaceViewValue.allocation.transferLegId,
              extraArgs: {
                  context: {
                      values: choiceContext.choiceContextData?.values ?? {},
                  },
                  meta: { values: {} },
              },
              disclosedContracts: choiceContext.disclosedContracts ?? [],
          }
      })
  )

  const allocationsWithContext: Record<string, { _1: string; _2: any }> =
      Object.fromEntries(
          allocationEntries.map((e) => [e.legId, { _1: e.cid, _2: e.extraArgs }])
      )

  const uniqueDisclosedContracts = Array.from(
      new Map(
          allocationEntries
              .flatMap((e) => e.disclosedContracts)
              .map((d: any) => [d.contractId, d])
      ).values()
  )

  const settleCmd = [
      {
          ExerciseCommand: {
              templateId:
                  '#splice-token-test-trading-app:Splice.Testing.Apps.TradingApp:OTCTrade',
              contractId: otcTradeCid,
              choice: 'OTCTrade_Settle',
              choiceArgument: { allocationsWithContext },
          },
      },
  ]

  await sdk.ledger
      .prepare({
          partyId: venue.partyId,
          commands: settleCmd,
          disclosedContracts: uniqueDisclosedContracts,
      })
      .sign(venue.keyPair.privateKey)
      .execute({ partyId: venue.partyId })

  logger.info(
      'Venue settled the OTCTrade, holdings are transfered to Alice and Bob'
  )

  await sdk.token.utxos
      .list({
          partyId: sender.partyId,
      })
      .then((transactions) => {
          logger.info(
              transactions,
              'Token Standard Holding Transactions (Alice):'
          )
      })

  await sdk.token.utxos
      .list({
          partyId: recipient.partyId,
      })
      .then((transactions) => {
          logger.info(transactions, 'Token Standard Holding Transactions (Bob):')
      })

  await sdk.token.holdings({ partyId: recipient.partyId }).then((allHoldings) => {
      logger.info(allHoldings, 'List holding transactions (Bob)')
  })
  ```
</div>

## Migration reference

| v0 approach                                 | v1 方法                                     |
| ------------------------------------------- | --------------------------------------------- |
| `tokenStandardService.registriesToAssets()` | `sdk.asset.list`                              |
| Manual array filtering for specific asset   | `asset.find(id, registryUrl?)`                |
| Manual 错误 handling for missing assets    | Built-in 错误 handling in `sdk.asset.find()` |

Asset-related 方法 migration

## See also

* `钱包-sdk-config` - SDK 配置
* `token-migration-v1` - Token namespace migration

