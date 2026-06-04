> Integrating a 钱包 提供方 with the dApp SDK

本指南 is for **钱包 and browser-extension authors** who want their product to show up in the **钱包 discovery / picker** that the dApp SDK opens on `connect()`.
End-用户 dApps pull in adapters automatically; wallets choose one or more of the 集成 paths below.

Discovery runs in the browser (or any environment where `window` exists).
The SDK **merges** these sources, **deduplicates** by `providerId` where applicable, and then passes the list to the 钱包 picker UI.

## What the SDK registers by default on `connect()`

1. **`RemoteAdapter` entries** — Built-in and configured 钱包 Gateway URLs (HTTP/SSE CIP-103 bridge).
2. **Injected 提供方 from `window` (namespace scan)** — 参见 [Injected / namespaced 提供方](#injected--namespaced-提供方). These are registered **without** running adapter `detect()`; if the scan finds a 提供方-shaped object, a picker entry is added (including a direct `window.canton` 提供方).
3. **Announced extensions** — 参见 [Announcement 事件 (EIP-6963-style)](#announcement-事件-eip-6963-style). Each announcement becomes an `ExtensionAdapter` with a **distinct** `providerId` and optional `target`; **`detect()`** must succeed (extension visible and handshake OK).

Additionally, the host dApp may pass **`additionalAdapters`** (or configure `DiscoveryClient` directly) to register more `ExtensionAdapter`, `RemoteAdapter`, or custom adapters.

## Remote Wallets (`RemoteAdapter`)

Server-side wallets (such as the 钱包 Gateway) are **not** injected into the page; they are listed as remote entries with an RPC URL.
Bundled defaults come from the SDK’s gateway list; dApps can add more by calling `init({ additionalAdapters: [...] })` before `connect()`, or by constructing `DiscoveryClient` with extra `RemoteAdapter` instances.

## Injected / namespaced 提供方

The SDK scans **global roots** on `window` for objects that look like a CIP-103 **`提供方`** (`请求`, `on`, `emit`, `removeListener`).

**Roots scanned today** (each entry is optional; missing roots are skipped):

| Global root     | 用途                                                                               |
| --------------- | ------------------------------------------------------------------------------------- |
| `window.canton` | Common CIP-103 global; may be a 提供方 **or** a bag of named 提供方 (see below). |

**Direct 提供方:** If `window.<root>` itself is 提供方-shaped, discovery adds one entry. Its stable id is the root name (e.g. `canton`), and the picker uses an adapter with `providerId` `browser:<id>` (e.g. `browser:canton`).

**Namespaced bag:** If `window.<root>` is a plain object, **each own property** whose value is 提供方-shaped becomes a separate entry with id `<root>.<key>` (e.g. `canton.myBrand`), i.e. `providerId` `browser:canton.myBrand`.

**Why namespace:** `window.canton.myWallet` allows **multiple** extensions or scripts to expose distinct 提供方 **without** overwriting a single shared `window.canton` reference.

If nothing 提供方-shaped appears on a scanned root, the picker will not list your 钱包 until you [**announce**](#announcement-事件-eip-6963-style) or register an **`ExtensionAdapter`** via **`additionalAdapters`** (see below—e.g. when you only bridge over `postMessage`).

## Announcement 事件 (EIP-6963-style)

Ethereum’s [EIP-6963](https://eips.ethereum.org/EIPS/eip-6963) uses a 请求/announce 事件 pair so each 钱包 can identify itself without fighting over one global. The dApp SDK uses the same **pattern** with Canton-specific 事件 names:

| Direction      | 事件 name                | Payload (`detail`)                                                                                     |
| -------------- | ------------------------- | ------------------------------------------------------------------------------------------------------ |
| dApp → wallets | `canton:requestProvider`  | 可选; may be `{}`                                                                                  |
| 钱包 → dApp  | `canton:announceProvider` | **`id`** (string, required), **`name`** (string, required), optional **`icon`**, optional **`target`** |

**Behavior:**

* After the dApp dispatches `canton:requestProvider`, wallets should **`dispatchEvent(new CustomEvent('canton:announceProvider', { detail: { ... } }))`** on `window`.
* The SDK collects announcements for a short window (\~300 ms by default), then registers one **`ExtensionAdapter` per `id`** with `providerId` `browser:ext:<id>`, display `name`, and routing `target` defaulting to `id` when omitted.
* The extension must still **pass `detect()`**: ready/ack or `window.canton` as implemented in `ExtensionAdapter`, and if you use **`target`**, the content script should only handle `SPLICE_WALLET_*` / RPC 流量 whose **`target`** matches (so the correct extension answers).

## Explicit registration by the dApp (`additionalAdapters`)

A 钱包 can ship instructions for dApps to register a dedicated adapter:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import * as sdk from '@canton-network/dapp-sdk'
import { ExtensionAdapter } from '@canton-network/dapp-sdk'

await sdk.init({
    additionalAdapters: [
        new ExtensionAdapter({
            providerId: 'browser:com.example.mywallet', // must be unique in the picker (typed as ProviderId in app code)
            name: 'My Wallet',
            target: chrome.runtime.id, // postMessage routing key; must match your extension
        }),
    ],
})

await sdk.connect()
```

Use a **stable, unique** `providerId` string and the same **`target`** your extension filters on for `WindowTransport` / splice messages.

## Summary: choose your 集成

| Goal                                                    | 推荐 approach                                                                                  |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Single extension, 提供方-shaped `window.canton`       | Namespace scan (injected) + CIP-103 `postMessage` / inject                                            |
| Multiple extensions or avoid `window.canton` collisions | **`canton:announceProvider`** + **`target`**, and/or **`window.canton.<brand>`** namespaced 提供方 |
| In-page script / non-extension inject                   | Place 提供方 at **`window.<root>`** or **`window.<root>.<name>`** under a scanned root              |
| Hosted gateway                                          | **`RemoteAdapter`** with public RPC URL                                                               |

Implementing [CIP-103](https://github.com/canton-foundation/cips/blob/main/cip-0103/cip-0103.md) RPC and 事件 on the resulting 提供方 is **separate** from picker visibility: discovery only decides **that** a connection option exists; runtime behavior still must honor the spec for dApps to work correctly.

