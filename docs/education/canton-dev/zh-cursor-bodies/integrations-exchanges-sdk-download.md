> 下载用于将交易所接入 Canton Network 的工具与示例代码

交易所集成使用 Wallet SDK、Canton Network 代币标准与 Ledger API，实现 Canton Coin 及其他 CN 代币的充值与提现工作流。

## 集成支持代码

以下支持代码可简化集成开发：

* **JavaScript/TypeScript** — 使用 [Wallet SDK](https://github.com/canton-network/wallet-gateway) 中的函数简化集成构建
* **Java/JVM** — 以 [ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings) 仓库示例为起点
* **其他语言** — 以 Wallet SDK 或 Java 示例为蓝图

## Wallet SDK（TypeScript）

主要集成库，通过 npm 安装：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm install @canton-network/wallet-sdk
```

SDK 提供：

* 代币标准交易准备与解析
* 转账预批准（TransferPreapproval）管理
* 交易历史摄取辅助
* 用于读取 Canton Coin 注册表数据的 Scan API 客户端

## Java 示例代码

Java 示例仓库演示如何从 JVM 语言与 JSON Ledger API 交互：

* **仓库：** [digital-asset/ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings)

## 集成里程碑

交易所集成指南按增量里程碑组织：

1. **Canton Coin（CC）一步提现** — 使用 TransferPreapproval 的 CC 充值与提现，包括对 CC 充值赚取应用奖励。

2. **全部 CN 代币** — 支持所有 Canton Network 代币（不仅 CC），增加多步转账，使接收方可拒绝入账并支持异步检查（KYC/AML）。

3. **全部 CN 代币的应用奖励** — 对所有 CN 代币的充值与提现赚取应用奖励，并可选择与客户分享奖励。

## 下一步

* [交易所集成指南](/integrations/exchanges/guidance) — 工作流、架构与部署
