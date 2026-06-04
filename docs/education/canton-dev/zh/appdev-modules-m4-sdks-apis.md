---
title: "SDK 与 API"
slug: "appdev-modules-m4-sdks-apis"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-sdks-apis.md"
source_title: "SDKs and APIs"
tags:
  - appdev
  - modules
  - m4-sdks-apis
---

# SDK 与 API

> Canton SDK、代码生成、Ledger API、JSON API、PQS 与 Wallet SDK 概览

Canton 提供一套面向账本构建应用的工具与 API。本节说明各组件的作用及使用场景。

## Canton SDK

Daml SDK 包含编译器、代码生成器、sandbox 及开发 Canton 应用所需的辅助工具。主要入口是 `dpm` 命令行工具。

`dpm` 的关键能力：

* `dpm build` — 将 Daml 源码编译为 DAR（Daml Archive）
* `dpm codegen-java` — 从已编译 DAR 生成 Java 绑定
* `dpm codegen-js` — 从已编译 DAR 生成 TypeScript/JavaScript 绑定
* `dpm sandbox` — 启动本地 Canton sandbox 节点用于测试
* `dpm test` — 运行 Daml Script 测试
* `dpm new` — 从模板脚手架新项目

`dpm` 还有更多功能，可通过 `--help` 探索，如 `dpm inspect-dar --help` 或 `dpm test --help`。

SDK 还包含 Daml Studio VS Code 扩展，提供语法高亮、类型检查与错误诊断。

## 代码生成

代码生成从 Daml 模型产出类型安全的客户端绑定。无需手工构造原始 gRPC 消息或 JSON payload，而是使用与 template 和 choice 对应的生成类。

### Java 绑定

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-java .daml/dist/<project>.dar -o generated-java
```

生成的 Java 类与 gRPC Ledger API 客户端集成。每个 Daml template 成为带创建合约与行使 choice 方法的 Java 类。cn-quickstart 后端通过 codegen 能力使用这些绑定。

### TypeScript 绑定

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-js .daml/dist/<project>.dar -o generated-ts
```

生成的 TypeScript 类型可用于 Node.js 后端或直接向 Ledger API 提交命令的前端。在完全中介架构（如 cn-quickstart）中，前端使用后端 REST API，通常不需要这些绑定。

## Ledger API（gRPC）

Ledger API 是提交命令与读取交易的主要接口，通过 validator participant 节点暴露的 gRPC 或 JSON API 传输访问。

Ledger API 提供：

* **命令提交** — 创建合约与行使 choice。命令以 party 身份提交，validator 经 synchronizer 处理。
* **交易流** — 订阅一个或多个 party 的已提交交易流。后端处理这些事件以保持状态同步。
* **活跃合约集** — 查询 party 当前可见的活跃合约。
* **包管理** — 向 validator 上传 DAR。
* **用户与 party 管理** — 在 validator 上创建与管理 party。

生产环境 Ledger API 使用 TLS 与基于 token 的认证。LocalNet 上可通过 Keycloak 配置认证，或完全禁用以加快实验。

## JSON API

Canton 3.x 中 JSON API 集成于 validator，提供 Ledger API 的 HTTP/JSON 接口。架构上，JSON API LAPI 端点将其调用翻译为流经 gRPC LAPI 端点。

适用 JSON API 的场景：

* 需要更简单的 HTTP 集成，无需 gRPC 客户端
* 原型阶段，用 `curl` 测试命令
* 语言或平台对 gRPC 支持有限

JSON API 通过 HTTP 端点与 JSON payload 支持 Ledger API 的相同操作（命令提交、活跃合约、交易流）。cn-quickstart 中每个 validator 的 JSON API 在 `x975` 端口（如 App User validator 为 `2975`）。

需要极高吞吐的生产后端，gRPC Ledger API 更合适，可避免 JSON 翻译层的序列化开销。

## Participant Query Store（PQS）

PQS 订阅 validator 交易流，将合约数据投影到 PostgreSQL 数据库。后端用标准 SQL 查询。

适合使用 PQS 的场景：

* 跨大量合约的过滤查询（如「本月到期的所有许可证」）
* 聚合与报表
* 全文搜索或复杂 join
* 不增加 Ledger API 负载的读路径

PQS 将 PostgreSQL 表与账本保持同步。合约在账本上创建与归档时，PQS 更新对应行。SQL 查询始终反映当前账本状态（有少量传播延迟）。

cn-quickstart 项目中，后端 `repository/` 与 `pqs/` 模块演示如何查询 PQS 表获取合约数据。

## Wallet SDK

Wallet SDK 提供与 Canton Coin（CC）钱包的集成，供需要处理支付或 traffic 管理的应用使用。通过钱包集成，应用可以：

* 发起 party 之间的 CC 转账
* 创建与应用工作流绑定的支付请求（如许可证续期）
* 查询钱包余额

cn-quickstart 的许可应用使用钱包集成处理续期支付。`LicenseRenewalRequest` 合约实现 Splice `AllocationRequest` 接口，钱包系统检测并作为支付处理。

CC 与 traffic 的更多说明见 [Canton Coin 与 Traffic](/appdev/modules/m4-canton-coin)。

## 可运行示例

[cn-quickstart](https://github.com/digital-asset/cn-quickstart) 仓库演示上述组件协同工作：

* `daml/` 中的 Daml 合约经 `dpm build` 编译
* `backend/` 中的 Java 后端使用生成绑定与 PQS
* `frontend/` 中的 React 前端消费后端 REST API
* LocalNet 通过 Docker Compose 运行 validator、PQS、JSON API 与钱包服务

克隆仓库并运行 `cd quickstart && make setup && make build && make start` 即可看到完整技术栈。

## 下一步

* [后端开发](/appdev/modules/m4-backend-dev) — Java 后端使用 Ledger API 与 PQS 的模式
* [前端开发](/appdev/modules/m4-frontend-dev) — 基于后端 API 构建 React 前端

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
