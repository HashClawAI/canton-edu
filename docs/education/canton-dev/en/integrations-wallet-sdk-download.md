---
title: "Wallet SDK Download"
slug: "integrations-wallet-sdk-download"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet/sdk-download.md"
source_title: "Wallet SDK Download"
tags:
  - integrations
  - wallet
  - sdk-download
---

# Wallet SDK Download

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallet SDK Download

> Download and install the Canton Network Wallet SDK for building wallet integrations

The Wallet SDK provides TypeScript/JavaScript libraries for interacting with Canton Coin and the Canton Network Token Standard. Use it to build wallet applications, integrate Canton Coin payments into your dApp, or manage external party signing workflows.

The SDK is published as the [`@canton-network/wallet-sdk`](https://www.npmjs.com/package/@canton-network/wallet-sdk) npm package. Source code and the OpenRPC specification for the dApp API are available in the [wallet-gateway repository](https://github.com/canton-network/wallet-gateway).

## Installation

The Wallet SDK is published on the npm registry. Install it with your preferred package manager:

<Tabs>
  <Tab title="npm">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    npm install @canton-network/wallet-sdk
    ```
  </Tab>

  <Tab title="yarn">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    yarn add @canton-network/wallet-sdk
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    pnpm add @canton-network/wallet-sdk
    ```
  </Tab>
</Tabs>

### dApp SDK

For dApp development only, the dApp SDK has a smaller bundle size and is optimized for browser usage. Both SDKs share the same underlying core packages, and individual core packages (transaction visualization, hash verification) can be used independently.

<Tabs>
  <Tab title="npm">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    npm install @canton-network/dapp-sdk
    ```
  </Tab>

  <Tab title="yarn">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    yarn add @canton-network/dapp-sdk
    ```
  </Tab>

  <Tab title="pnpm">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    pnpm add @canton-network/dapp-sdk
    ```
  </Tab>
</Tabs>

## Source Repository

The Wallet SDK source code is available on GitHub:

* **Repository:** [canton-network/wallet-gateway](https://github.com/canton-network/wallet-gateway)
* **API Specs:** OpenRPC specification for the dApp API is at `api-specs/openrpc-dapp-api.json`

## What the SDK Provides

The Wallet SDK includes:

* **Transaction preparation** — Build and sign Canton Coin transfers using the Token Standard
* **Token Standard client** — Interact with the Canton Network Token Standard APIs for any CN token
* **Transaction history parsing** — Parse ledger updates into structured deposit/withdrawal records
* **Configuration management** — Connect to different environments (LocalNet, DevNet, TestNet, MainNet)
* **External signing support** — Prepare transactions for external party signing workflows

## Language Support

| Language                  | Support                                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TypeScript/JavaScript** | Full SDK via npm                                                                                                                                                                                           |
| **Java/JVM**              | Reference examples (not part of the SDK) at [ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings) — demo code showing how to interact with the JSON Ledger API from Java |
| **Other languages**       | Use the TypeScript SDK or Java samples as a blueprint                                                                                                                                                      |

## Next Steps

* [Wallet Configuration](/docs/canton/integrations-wallet-configuration) — Configure the SDK for your environment
* [Wallet Integration Guidance](/docs/canton/integrations-wallet-guidance) — Signing transactions from dApps

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
