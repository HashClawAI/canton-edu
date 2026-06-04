---
title: "签名提供方"
slug: "integrations-wallet-gateway-signing-providers"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet-gateway/signing-providers.md"
source_title: "Signing Providers"
tags:
  - integrations
  - wallet-gateway
  - signing-providers
---

# 签名提供方

> 钱包 Gateway signing 提供方 集成

钱包 Gateway supports multiple signing 提供方 that handle cryptographic key management and 交易 signing. Each 提供方 has different use cases and security characteristics.

## 可用提供方

## 钱包 Gateway (Internal)

钱包 Gateway 提供方 stores private keys directly in the signing store database. This is suitable for 开发 and 测试 but **not recommended for 生产** use cases where security is critical.

**配置：**

This 提供方 is automatically available when a `signingStore` is configured in the Gateway 配置. No additional setup is required.

**适用场景：**

* Local 开发
* 测试 environments
* Proof-of-concept 应用

**安全注意事项:**

> \[!IMPORTANT]
> Private keys are stored in the database. 若 database is compromised, all keys are at risk. Use only in non-生产 environments.

## 参与者-Based Signing

The 参与者 signing 提供方 uses Canton's 参与者 node for signing 交易. The 参与者 maintains the key material and handles all cryptographic operations.

**配置：**

This 提供方 is always available and requires no additional 配置. You simply select it when creating a party.

**适用场景：**

* 企业 deployments where the 参与者 node manages keys
* Scenarios where key management is handled by the infrastructure
* 生产 environments with dedicated 参与者 nodes

**工作原理:**

当交易 is submitted, the Gateway forwards the 命令 to the 参与者 node, which signs it using the party's key stored in the 参与者's keystore.

## Fireblocks

Fireblocks is a third-party crypto custody 服务 提供方 that offers enterprise-grade key management and signing 服务.

**设置：**

1. Complete steps 1-3 from the [Fireblocks signing documentation](https://github.com/canton-网络/钱包-gateway/tree/main/core/signing-fireblocks)

2. Supply an environment variable named `FIREBLOCKS_API_KEY` containing your Fireblocks API key (from the `API 用户 (ID)` column in the Fireblocks API 用户 table).

**配置：**

The Fireblocks 提供方 reads 配置 from environment variables and key files. No additional Gateway 配置 is needed beyond placing the required files.

**适用场景：**

* 企业 deployments requiring HSM-backed key storage
* Compliance-sensitive 应用
* High-security 生产 environments

## Blockdaemon

Blockdaemon provides signing 服务 as part of their infrastructure offerings.

**配置：**

设置 the following environment variables:

* `BLOCKDAEMON_API_URL` - The base URL for the Blockdaemon API
* `BLOCKDAEMON_API_KEY` - Your Blockdaemon API key

**适用场景：**

* 托管 infrastructure deployments
* Cloud-native 应用
* Environments leveraging Blockdaemon's 服务

## Dfns

Dfns is a crypto custody platform that provides programmable key management and signing infrastructure.

**配置：**

设置 the following environment variables:

* `DFNS_ORG_ID` - Your Dfns organization ID
* `DFNS_BASE_URL` - The Dfns API URL (defaults to `https://api.dfns.io`)
* `DFNS_CRED_ID` - Your 服务 账户 credential ID
* `DFNS_PRIVATE_KEY` - Your 服务 账户 private key (PEM format)
* `DFNS_AUTH_TOKEN` - Your 服务 账户 认证 token

**前置条件:**

1. 设置 up a 服务 账户 with appropriate permissions in Dfns
2. Generate and download the 服务 账户 credentials

**适用场景：**

* 企业 deployments requiring MPC-based key management
* Programmable custody with policy controls
* Multi-party approval 工作流
* High-security 生产 environments

**工作原理:**

Dfns creates and activates Canton wallets directly through its validator 集成. When the Gateway requests a 钱包, Dfns provisions a Canton-formatted key, registers the party on the 网络, and returns the 钱包 ready for use. When signing a prepared 交易, Dfns broadcasts it to Canton in a single step and returns the resulting update ID. Only `Canton` and `CantonTestnet` 网络 wallets are supported.

## 选择提供方

创建时 a new party through the 用户 API or web UI, you can select which signing 提供方 to use. The choice depends on your security requirements, infrastructure setup, and compliance needs.

**建议：**

* **开发/测试**: Use 钱包 Gateway (internal) or 参与者-based signing
* **生产 (企业)**: Use Fireblocks, Dfns, or 参与者-based signing
* **生产 (托管)**: Use Blockdaemon, Dfns, or 参与者-based signing

The signing 提供方 is selected per-party, so you can have different Party using different 提供方 within the same Gateway instance.

## 密钥管理

Each 提供方 handles key management differently:

* **钱包 Gateway**: Keys are stored in the signing store database
* **参与者**: Keys are managed by the Canton 参与者 node
* **Fireblocks**: Keys are stored in Fireblocks' secure infrastructure (HSM-backed)
* **Blockdaemon**: Keys are managed by Blockdaemon's infrastructure
* **Dfns**: Keys are managed by Dfns' secure infrastructure

迁移时 between 提供方, keys cannot be directly transferred. You'll need to:

1. 创建 a new party with the new 提供方
2. 转账 any assets/合约 to the new party
3. 更新 your dApp to use the new party

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
