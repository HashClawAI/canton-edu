---
title: "Adapters and Discovery"
slug: "integrations-dapp-sdk-adapters-and-discovery"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/dapp-sdk/adapters-and-discovery.md"
source_title: "Adapters and Discovery"
tags:
  - integrations
  - dapp-sdk
  - adapters-and-discovery
---

# Adapters and Discovery

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Adapters and Discovery

> dApp SDK adapter registration and wallet discovery

Adapters you register in `init()` determine what the SDK can discover and what the
user will see in the **wallet picker** opened by `connect()`. In other words:

* If an adapter is registered (and passes `detect()`), it can show up as an entry in the picker.
* Session restore can only happen for adapters that are registered.

## Option 1: Use the built-in default gateways

This registers the SDK’s default gateway list (from `gateways.json`) plus any injected / announced wallets:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init()
```

## Option 2: Add adapters (recommended)

Use `additionalAdapters` to add extra wallets (custom remote gateways, WalletConnect, etc.) while keeping
the default gateways.

### Add WalletConnect

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { WalletConnectAdapter } from '@canton-network/dapp-sdk'

const wc = WalletConnectAdapter.create({
    projectId: import.meta.env.VITE_WC_PROJECT_ID,
})

await sdk.init({ additionalAdapters: [wc] })
```

### Add a custom remote wallet gateway URL

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { RemoteAdapter } from '@canton-network/dapp-sdk'

await sdk.init({
    additionalAdapters: [
        new RemoteAdapter({
            name: 'My Gateway',
            rpcUrl: 'https://my-gateway.example/api/v0/dapp',
        }),
    ],
})
```

### Add a custom extension adapter (postMessage target)

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { ExtensionAdapter } from '@canton-network/dapp-sdk'

await sdk.init({
    additionalAdapters: [
        new ExtensionAdapter({
            providerId: 'browser:ext:com.example.mywallet' as never,
            name: 'My Wallet',
            target: 'com.example.mywallet',
        }),
    ],
})
```

## Option 3: Replace the default gateways

If you want to *only* offer specific remote gateways (and not the SDK defaults), provide `defaultAdapters`.

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { RemoteAdapter } from '@canton-network/dapp-sdk'

await sdk.init({
    defaultAdapters: [
        new RemoteAdapter({
            name: 'Production Gateway',
            rpcUrl: 'https://gateway.example/api/v0/dapp',
        }),
    ],
})
```

## Option 4: Intentionally register no remote gateways

If you pass an empty list, you are explicitly choosing “none” (useful if your dApp only supports
injected/announced wallets, or only supports adapters you add later).

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init({ defaultAdapters: [] })
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
