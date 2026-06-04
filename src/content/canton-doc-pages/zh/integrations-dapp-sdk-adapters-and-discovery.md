---
title: "适配器与发现"
slug: "integrations-dapp-sdk-adapters-and-discovery"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/dapp-sdk/adapters-and-discovery.md"
source_title: "Adapters and Discovery"
tags:
  - integrations
  - dapp-sdk
  - adapters-and-discovery
---

# 适配器与发现

> dApp SDK 适配器注册与钱包发现

在 `init()` 中注册的适配器决定 SDK 能发现哪些钱包，以及 `connect()` 打开的**钱包选择器**中向用户展示哪些选项。换言之：

* 若适配器已注册（且通过 `detect()`），即可在选择器中显示。
* 会话恢复仅对已注册的适配器生效。

## 选项 1：使用内置默认网关

这会注册 SDK 的默认网关列表（来自 `gateways.json`），以及所有注入/公告的钱包：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init()
```

## 选项 2：添加适配器（推荐）

使用 `additionalAdapters` 在保留默认网关的同时添加更多钱包（自定义远程 Gateway、WalletConnect 等）。

### 添加 WalletConnect

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { WalletConnectAdapter } from '@canton-network/dapp-sdk'

const wc = WalletConnectAdapter.create({
    projectId: import.meta.env.VITE_WC_PROJECT_ID,
})

await sdk.init({ additionalAdapters: [wc] })
```

### 添加自定义远程 Wallet Gateway URL

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

### 添加自定义扩展适配器（postMessage 目标）

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

## 选项 3：替换默认网关

若只想提供特定远程网关（不使用 SDK 默认项），请提供 `defaultAdapters`。

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

## 选项 4：有意不注册远程网关

传入空列表表示明确选择「无」（适用于 dApp 仅支持注入/公告钱包，或稍后自行添加适配器）。

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
await sdk.init({ defaultAdapters: [] })
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
