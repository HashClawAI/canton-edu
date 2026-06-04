---
title: "dApp 构建概览"
slug: "integrations-dapp-building-overview"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/dapp-building-overview.md"
source_title: "dApp Building Overview"
tags:
  - integrations
  - dapp-building-overview
---

# dApp 构建概览

> dApp SDK、Wallet Gateway 与 Canton Network 如何协同

本指南帮助你在 **Canton Network** 上构建 **dApp**（去中心化应用），通过 **Wallet Gateway** 或其他兼容 dApp API 的钱包与网络交互。你在前端使用 **dApp SDK** 连接用户钱包；Wallet Gateway 在 dApp、Canton 验证者节点与签名提供方之间充当中介。

## 你在构建什么

典型部署包括：

* **dApp** — Web 或移动应用，供用户查看账本数据、创建合约并提交交易。dApp 通过 dApp SDK 连接钱包并调用 dApp API。
* **Wallet Gateway** — 暴露 dApp API 与 User API 的服务器，管理会话，并与 Canton 验证者与签名提供方通信。
* **Canton Network** — 分布式账本。验证者节点暴露 Ledger API；Wallet Gateway 代表已认证用户连接它们。
* **签名** — 交易签名由 **签名提供方**（如 Canton participant、Fireblocks 或 Blockdaemon）处理。用户创建绑定网络与签名提供方的钱包（Party）。测试时 Gateway 也可用于签名。

## 高层架构

```
┌─────────────┐      dApp API        ┌──────────────────┐     Ledger API      ┌─────────────────┐
│   Your dApp │ ◄──────────────────► │  Wallet Gateway  │ ◄─────────────────► │ Canton Validator│
│ (dApp SDK)  │   (HTTP / WebSocket) │                  │                     │                 │
└─────────────┘                      │  ┌────────────┐  │     Signing         └─────────────────┘
       │                             │  │  User API  │  │
       │      User interactions      │  │  User UI   │  │     ┌─────────────────┐
       └────────────────────────────►│  └────────────┘  │ ◄──►│ Signing Provider│
            (User UI / User API)     │                  │     │ (Participant,   │
                                     └──────────────────┘     │  Fireblocks…)   │
                                                              └─────────────────┘
```

* **dApp → Wallet Gateway**：dApp 通过 dApp SDK 调用 **dApp API**（连接、列出账户、准备并执行交易）。SDK 可使用 HTTP（远程 Gateway）或 `postMessage`（浏览器扩展）。
* **用户 → Wallet Gateway**：用户通过 **User UI** 或 **User API** 管理钱包并批准交易（会话、网络、IDP、钱包、签名、执行）。
* **Wallet Gateway → Canton / 签名**：Gateway 向验证者 Ledger API 认证，并将签名请求转发到配置的签名提供方。

## dApp API 与 dApp SDK

**dApp API** 是由 **CIP-103** 定义的 JSON-RPC 2.0 接口。你可从前端或后端直接调用（HTTP 或 WebSocket）。实践中多数开发者使用 **dApp SDK**，它实现同一协议并提供更简洁的 API、多传输支持（远程 Gateway 用 HTTP，浏览器扩展钱包用 `postMessage`），以及类 EIP-1193 的 provider（`window.canton`）。dApp API 让前端连接钱包、列出账户、准备并执行交易并接收实时更新；这一切都需要有效会话（JWT）。参见 [API](/zh/docs/canton/integrations-wallet-gateway-apis) 与 [dApp SDK](/zh/docs/canton/integrations-dapp-sdk-usage) 文档。

## User API 与 User UI

**User API** 面向用户与自动化：会话、网络、身份提供方、钱包与交易签名。**User UI**（由 Wallet Gateway 提供）通过 User API 让用户登录、创建与管理钱包、批准 dApp 交易并修改设置。若需自定义集成或脚本，可直接调用 User API 而不用 User UI。参见 [用法](/zh/docs/canton/integrations-wallet-gateway-usage) 与 [API](/zh/docs/canton/integrations-wallet-gateway-apis)。

## 发现与连接流程

1. **发现**：dApp 发现可用的 Wallet Gateway 实例（如 well-known URL 或注册表）。每个 Gateway 暴露基础 URL 与内核信息。
2. **连接**：用户选择 Gateway。dApp 调用 `connect()`（dApp SDK）。按配置，用户可能被重定向到 Gateway User UI 登录（OAuth 或自签名）。
3. **会话**：登录后 Gateway 创建会话并返回 JWT。dApp SDK 用它调用 dApp API（`listAccounts`、`prepareExecute` 等）。
4. **交易**：dApp 调用 `prepareExecute` 时，用户可能需在 User UI 批准。签名并执行后，dApp 收到结果并可响应 `TxChanged` 事件。

## 下一步

* **构建 dApp？** → 安装 [dApp SDK](https://github.com/canton-network/wallet-gateway/blob/82ec39c9/docs/dapp-building/dapp-sdk/installation.md)，遵循 [dApp SDK 用法](/zh/docs/canton/integrations-dapp-sdk-usage)，并按需查阅 [API](/zh/docs/canton/integrations-wallet-gateway-apis)（dApp API）。
* **运行或配置 Wallet Gateway？** → 从 [Getting Started](https://github.com/canton-network/wallet-gateway/blob/82ec39c9/docs/dapp-building/wallet-gateway/getting-started/index.md) 开始，然后 [Configuration](https://github.com/canton-network/wallet-gateway/blob/82ec39c9/docs/dapp-building/wallet-gateway/configuration/index.md)、[Signing Providers](/zh/docs/canton/integrations-wallet-gateway-signing-providers) 与 [API](/zh/docs/canton/integrations-wallet-gateway-apis)（User API）。
* **使用 User UI 或 User API？** → 参见 [用法](/zh/docs/canton/integrations-wallet-gateway-usage) 了解典型流程及接口选择。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
