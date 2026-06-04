> 下载 and install the Canton Network 钱包 SDK for building 钱包 集成

The 钱包 SDK provides TypeScript/JavaScript libraries for interacting with Canton Coin（CC） and the Canton Network Token Standard. Use it to build 钱包 应用, integrate Canton Coin（CC） payments into your dApp, or manage external party signing 工作流.

The SDK is published as the [`@canton-网络/钱包-sdk`](https://www.npmjs.com/package/@canton-网络/钱包-sdk) npm package. Source code and the OpenRPC specification for the dApp API are available in the [钱包-gateway repository](https://github.com/canton-网络/钱包-gateway).

## 安装

The 钱包 SDK is published on the npm registry. 安装 it with your preferred package manager:

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

For dApp 开发 only, the dApp SDK has a smaller bundle size and is optimized for browser usage. Both SDKs share the same underlying core packages, and individual core packages (交易 visualization, hash verification) can be used independently.

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

The 钱包 SDK source code is available on GitHub:

* **Repository:** [canton-网络/钱包-gateway](https://github.com/canton-网络/钱包-gateway)
* **API Specs:** OpenRPC specification for the dApp API is at `api-specs/openrpc-dapp-api.json`

## What the SDK Provides

The 钱包 SDK includes:

* **交易 preparation** — Build and sign Canton Coin（CC） transfers using the Token Standard
* **Token Standard client** — Interact with the Canton Network Token Standard APIs for any CN token
* **交易 history parsing** — Parse ledger updates into structured deposit/withdrawal records
* **配置 management** — 连接 to different environments (LocalNet, DevNet, TestNet, MainNet)
* **External signing support** — 准备 交易 for external party signing 工作流

## Language Support

| Language                  | Support                                                                                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TypeScript/JavaScript** | Full SDK via npm                                                                                                                                                                                           |
| **Java/JVM**              | Reference examples (not part of the SDK) at [ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings) — demo code showing how to interact with the JSON Ledger API from Java |
| **Other languages**       | Use the TypeScript SDK or Java samples as a blueprint                                                                                                                                                      |

## 下一步

* [钱包 配置](/集成/钱包/配置) — 配置 the SDK for your environment
* [钱包 集成 Guidance](/集成/钱包/guidance) — Signing 交易 from dApps

