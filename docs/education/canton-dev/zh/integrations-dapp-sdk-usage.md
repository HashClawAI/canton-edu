---
title: "用法"
slug: "integrations-dapp-sdk-usage"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/dapp-sdk/usage.md"
source_title: "Usage"
tags:
  - integrations
  - dapp-sdk
  - usage
---

# 用法

> Using the dApp SDK from a Canton Network dApp

There are two ways to interact with the dApp API:

1. **dApp SDK** - A high-level SDK that wraps the 提供方 API with convenient 方法 and 事件 handlers. This is the recommended approach for most 应用.

2. **提供方 API** - The low-level interface that follows the [EIP-1193](https://eips.ethereum.org/EIPS/eip-1193) pattern. Use this when you need direct control over the API or are integrating with existing 提供方-based infrastructure.

The examples below show both approaches side by side.

## Setup

**dApp SDK:**

Import the dApp SDK:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import * as sdk from '@canton-network/dapp-sdk'
```

### Initialize the SDK （推荐）

Call `init()` once early (e.g. on app mount). 这会注册 adapters and attempts
to 恢复 a previously connected 会话 **without** opening the 钱包 picker.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init()
```

若你 want to add or replace wallets (e.g. WalletConnect), see
[Adapter registration & 钱包 discovery (picker)](/集成/dapp-sdk/adapters-and-discovery).

**提供方 API:**

Import and create a 提供方 instance:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const provider = window.canton
```

## 请求-响应 方法

### Connecting to a 钱包

Establish a connection to the 钱包. This initiates the 认证 flow if the 用户 is not already authenticated.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init() // optional if already called
const result = await sdk.connect()
console.log(result.isConnected) // true if connected
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const result = await provider.request<ConnectResult>({
    method: 'connect',
})
console.log(result.isConnected) // true if connected
```

### Disconnecting from a 钱包

Close the 会话 between the client and the 钱包.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.disconnect()
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await provider.request({ method: 'disconnect' })
```

### Checking the Connection Status

检查 the connection status of the 钱包. The status returns an object containing 网络 connection- and 会话-related information.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk.status()
    .then((result) => {
        setStatus(
            `${result.connection.isConnected ? 'connected' : 'disconnected'}`
        )
    })
    .catch(() => setStatus('disconnected'))
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
provider
    .request<StatusEvent>({ method: 'status' })
    .then((result) => {
        setStatus(
            `${result.connection.isConnected ? 'connected' : 'disconnected'}`
        )
    })
    .catch(() => setStatus('disconnected'))
```

### Checking if Connected (without login)

检查 if the 用户 is connected without triggering the login flow.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const result = await sdk.isConnected()
console.log(result.isConnected)
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const result = await provider.request<ConnectResult>({
    method: 'isConnected',
})
console.log(result.isConnected)
```

### Getting the Active 网络

Retrieve details about the 网络 the 用户 is connected to.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const network = await sdk.getActiveNetwork()
console.log(network.networkId) // e.g., 'canton:da-mainnet'
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const network = await provider.request<Network>({
    method: 'getActiveNetwork',
})
console.log(network.networkId)
```

### Listing 账户

列出 all 账户 (Party) the 用户 has access to in the 钱包.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const accounts = await sdk.listAccounts()
console.log(accounts)
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const accounts = await provider.request<Account[]>({
    method: 'listAccounts',
})
console.log(accounts)
```

### Getting the Primary 账户

获取 the 账户 currently set as primary by the 用户.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const account = await sdk.getPrimaryAccount()
console.log(account.partyId)
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const account = await provider.request<Account>({
    method: 'getPrimaryAccount',
})
console.log(account.partyId)
```

### Signing a Message

签名 an arbitrary string message using the primary 账户's private key.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const signature = await sdk.signMessage('Hello, Canton!')
console.log(signature)
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const signature = await provider.request<string>({
    method: 'signMessage',
    params: { message: 'Hello, Canton!' },
})
console.log(signature)
```

### Executing a 交易

准备, sign, and execute a Daml 交易. This 方法 handles the full lifecycle: preparing the 命令, requesting 用户 approval/signature, and submitting to the ledger.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const createPingCommand = (party: string) => ({
    commands: [
        {
            CreateCommand: {
                templateId: '#AdminWorkflows:Canton.Internal.Ping:Ping',
                createArguments: {
                    id: `my-test-${new Date().getTime()}`,
                    initiator: party,
                    responder: party,
                },
            },
        },
    ],
})

// Get the primary party the user selected in the Wallet
const primaryParty = (await sdk.listAccounts()).find((w) => w.primary)?.partyId

// Request user's signature and execute the transaction
await sdk.prepareExecute(createPingCommand(primaryParty!))
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const createPingCommand = (party: string) => ({
    commands: [
        {
            CreateCommand: {
                templateId: '#AdminWorkflows:Canton.Internal.Ping:Ping',
                createArguments: {
                    id: `my-test-${new Date().getTime()}`,
                    initiator: party,
                    responder: party,
                },
            },
        },
    ],
})

// Get the primary party the user selected in the Wallet
const accounts = await provider.request<Account[]>({ method: 'listAccounts' })
const primaryParty = accounts.find((w) => w.primary)?.partyId

// Request user's signature and execute the transaction
await provider.request({
    method: 'prepareExecute',
    params: createPingCommand(primaryParty!),
})
```

### Calling the Ledger API

Proxy requests to the Canton JSON Ledger API. The 请求 is authenticated using the 用户's 会话.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const response = await sdk.ledgerApi({
    requestMethod: 'GET',
    resource: '/v2/version',
})
console.log(JSON.parse(response.response))
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const response = await provider.request<LedgerApiResponse>({
    method: 'ledgerApi',
    params: {
        requestMethod: 'GET',
        resource: '/v2/version',
    },
})
console.log(JSON.parse(response.response))
```

## 事件

The dApp API emits 事件 to notify your 应用 of state changes. Subscribe to these 事件 to keep your UI in sync with the 钱包 state.

### Listening for Connection Status Changes

Receive notifications when the connection status or 会话 state changes.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk.onStatusChanged((status) => {
    console.log('Status changed:', status)
    console.log('Connected:', status.connection.isConnected)
})
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
provider.on('statusChanged', (status: StatusEvent) => {
    console.log('Status changed:', status)
    console.log('Connected:', status.connection.isConnected)
})
```

### Listening for 账户 Changes

Receive notifications when 账户 are added, removed, or when the primary 账户 changes.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk.onAccountsChanged((accounts) => {
    console.log('Accounts changed:', accounts)
    const primary = accounts.find((a) => a.primary)
    console.log('Primary account:', primary?.partyId)
})
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
provider.on('accountsChanged', (accounts: Account[]) => {
    console.log('Accounts changed:', accounts)
    const primary = accounts.find((a) => a.primary)
    console.log('Primary account:', primary?.partyId)
})
```

### Listening for 交易 Changes

Receive notifications about the lifecycle of 交易 initiated via `prepareExecute`. The 事件 payload includes the 交易 status (`pending`, `signed`, `executed`, `failed`) and relevant details.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk.onTxChanged((tx) => {
    console.log('Transaction status:', tx.status)
    if (tx.status === 'executed') {
        console.log('Update ID:', tx.payload.updateId)
    }
})
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
provider.on('txChanged', (tx: TxChangedEvent) => {
    console.log('Transaction status:', tx.status)
    if (tx.status === 'executed') {
        console.log('Update ID:', tx.payload.updateId)
    }
})
```

### Removing 事件 Listeners

When your 组件 unmounts or you no longer need to listen for 事件, remove the listeners to prevent memory leaks.

**dApp SDK:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const handleStatus = (status) => console.log(status)

// Subscribe
sdk.onStatusChanged(handleStatus)

// Unsubscribe (when cleaning up)
sdk.offStatusChanged(handleStatus)
```

**提供方 API:**

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const handleStatus = (status: StatusEvent) => console.log(status)

// Subscribe
provider.on('statusChanged', handleStatus)

// Unsubscribe (when cleaning up)
provider.removeListener('statusChanged', handleStatus)
```

## Adapter / 提供方 information

### 获取 the current 提供方

`sdk.getConnectedProvider()` returns the raw CIP-103 提供方 for the **currently active
discovery 会话**, or `null` if you are not connected. Use this when you need direct
access to `提供方.请求(...)`, to subscribe to 提供方-level 事件, or to
instantiate the 钱包 SDK (upcoming feature).

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const provider = sdk.getConnectedProvider()
if (!provider) {
    // Not connected yet
    return
}

const status = await provider.request({ method: 'status' })
console.log(status.connection.isConnected)
```

## Adapter registration & 钱包 discovery (picker)

参见 [Adapter registration & 钱包 discovery (picker)](/集成/dapp-sdk/adapters-and-discovery) for multiple ways
to register adapters and what appears in the 钱包 picker.

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
