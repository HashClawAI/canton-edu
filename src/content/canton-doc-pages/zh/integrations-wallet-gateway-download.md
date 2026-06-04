---
title: "下载"
slug: "integrations-wallet-gateway-download"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet-gateway/download.md"
source_title: "Download"
tags:
  - integrations
  - wallet-gateway
  - download
---

# 下载

> 安装 and start the 钱包 Gateway

本指南帮助你 get the 钱包 Gateway up and running quickly.

## 安装

Choose your preferred installation 方法:

**Global 安装 (npm):**

安装 the 钱包 Gateway globally using npm:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm install -g @canton-network/wallet-gateway-remote
```

After installation, you can run it from anywhere:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
wallet-gateway -c ./config.json
```

**运行 with npx (No 安装):**

运行 the 钱包 Gateway directly through npx without installing (tested with Node.js v24):

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npx @canton-network/wallet-gateway-remote -c ./config.json
```

This downloads and runs the latest version each time, useful for 测试 or one-off runs.

## 快速开始

1. **创建 a 配置 File**

   First, generate an example 配置 file:

   **Global 安装:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway --config-example > config.json
   ```

   **npx:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   npx @canton-network/wallet-gateway-remote --config-example > config.json
   ```

2. **Edit the 配置**

   Open `config.json` and customize it for your environment. At minimum, you'll need to configure:

   * **Store connection**: Database 配置 (in-memory, SQLite, or PostgreSQL)
   * **Networks**: At least one Canton 网络 with its Ledger API 端点
   * **Identity 提供方**: 认证 配置 for your networks

   参见 [配置](/集成/钱包-gateway/配置) for detailed 配置 options.

3. **启动 the Gateway**

   **Global 安装:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway -c ./config.json
   ```

   Or with a custom port:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   wallet-gateway -c ./config.json -p 8080
   ```

   **npx:**

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   npx @canton-network/wallet-gateway-remote -c ./config.json
   ```

   Or with a custom port:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   npx @canton-network/wallet-gateway-remote -c ./config.json -p 8080
   ```

4. **验证 it's Running**

   Once started, the 钱包 Gateway exposes three 端点:

   * **Web UI**: `http://localhost:3030` (or your configured port)
   * **dApp JSON-RPC API**: `http://localhost:3030/api/v0/dapp`
   * **用户 JSON-RPC API**: `http://localhost:3030/api/v0/用户`

   Open the web UI in your browser to confirm it's running.

## 命令行选项

钱包 Gateway supports the following 命令-line options:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
-c, --config <path>          Set config path (default: ./config.json)
--config-schema              Output the config schema (JSON Schema) and exit
--config-example             Output an example config and exit
-p, --port [port]            Set port (overrides config file)
-f, --log-format <format>    Set log format: json or pretty (default: pretty)
```

示例:

**Global 安装:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate config schema
wallet-gateway --config-schema

# Run with JSON logging
wallet-gateway -c ./config.json -f json
```

**npx:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate config schema
npx @canton-network/wallet-gateway-remote --config-schema

# Run with JSON logging
npx @canton-network/wallet-gateway-remote -c ./config.json -f json
```

## 配置 Schema

To see the full JSON Schema for the 配置 file, run:

**Global 安装:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
wallet-gateway --config-schema
```

**npx:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npx @canton-network/wallet-gateway-remote --config-schema
```

This outputs a complete JSON Schema that can be used for validation and IDE autocomplete support.

## 下一步

* 读取 [配置](/集成/钱包-gateway/配置) to understand all 配置 options
* Explore the [APIs](/集成/钱包-gateway/apis) to understand how to interact with the Gateway
* Learn about [Signing 提供方](/集成/钱包-gateway/signing-提供方) to configure 交易 signing
* 检查 out the [Deployment](https://github.com/canton-网络/钱包-gateway/blob/82ec39c9/docs/dapp-building/钱包-gateway/deployment/index.md) guide to host the Gateway with Docker or Helm
* 检查 [Troubleshooting](/集成/钱包-gateway/troubleshooting) if you encounter any issues

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
