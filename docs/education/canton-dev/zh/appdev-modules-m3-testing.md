---
title: "测试 Daml 合约"
slug: "appdev-modules-m3-testing"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-testing.md"
source_title: "Testing Daml Contracts"
tags:
  - appdev
  - modules
  - m3-testing
---

# 测试 Daml 合约

> 使用 Daml Script 编写并运行 Daml 智能合约测试

# 测试 Daml 合约

本节介绍如何测试并调试你用前面章节工具构建的 Daml 合约。你已在 IDE 中用 Daml Script 测试代码；本章将介绍更多运行 Script 的方式，以及其他测试与调试工具，具体包括：

* 用 Daml Script 测试与调试模板
* `trace` 与 `debug` 函数
* Choice 覆盖率

注意本节仅涵盖 Daml 合约测试。

<Tip>
  可运行 `dpm new intro-test  --template daml-intro-test` 将本节全部代码加载到 `intro-test` 文件夹。
</Tip>

## 多包项目结构

在项目结构一节你学到应将 script 与模板放在不同包中。本节项目为多包构建，包含 `compose` 与 `dependencies` 的全部代码，目录结构如下：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
.
├── asset
├── asset-tests
├── multi-trade
├── multi-trade-tests
└── multi-package.yaml
```

`asset`、`asset-tests`、`multi-trade`、`multi-trade-tests` 为各包，各有 `daml.yaml`。`asset` 含 `Asset` 与 `Trade` 模板；测试 script 在依赖 `asset` 的 `asset-tests` 包中。与 `asset-tests` 不同，`asset` 用于上传到 Canton 账本。

类似地，`multi-trade` 含 `MultiTrade` 模板，`multi-trade-tests` 含对应 script。

`multi-package.yaml` 为多包配置，使 `dpm` 可编排各子包构建，列出子包：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
packages:
- ./asset
- ./asset-tests
- ./multi-trade
- ./multi-trade-tests
```

在多包项目根目录运行 `dpm build --all` 可构建全部子包；也可在任一子包运行 `dpm build`，会自动检测依赖并按序构建。例如在 `multi-trade-tests` 运行 `dpm build` 会依次构建 `asset`、`multi-trade`、`multi-trade-tests`。

## 用 Daml Script 测试模板

Daml Script 是测试 Daml 合约的主要工具。在 script 中，你可从多个参与方在全新、初始为空的账本上提交命令与查询。

运行 Daml Script 有两种主要方式：- 在 VS Code 点击 `Script results` 透镜：提供表视图与交易视图，便于调试。- 运行 `dpm test`，便于回归检查与覆盖率。

### 在 VS Code 中运行 script

在较早的 script 测试一节中，你已学会在 VS Code 编写并运行 Daml Script。

复习：在 `asset-tests` 或 `multi-trade-tests` 中找到 script，点击 script 名上方的 `Script results` 透镜，VS Code 应在侧栏打开表视图。表视图描述 script 结束时账本的最终状态：列出活跃合约、数据，以及各方是否可见。点击 `Show archived` 可查看已归档合约。

在侧栏点击 `Show transaction view` 切换到交易视图，显示 script 执行的全部交易与子交易；script 失败时也包含失败信息。尝试修改 `exerciseCmd` 的提交方，观察 script 是否仍成功。

可用 VS Code 的表视图与交易视图更好理解各合约的可见性与各方的权限。

### 用 `dpm` 运行全部 script

`dpm` 可运行包内全部 script，便于快速回归并在 CI 中自动化。

在 `multi-trade-tests` 文件夹打开终端并运行 `dpm test`，应成功并打印如下测试摘要：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Test Summary

daml/Intro/Asset/MultiTradeTests.daml:testMultiTrade: ok, 12 active contracts, 28 transactions.
daml/Intro/Asset/TradeSetup.daml:setupRoles: ok, 2 active contracts, 4 transactions.
daml/Intro/Asset/TradeSetup.daml:test_issuance: ok, 3 active contracts, 5 transactions.
daml/Intro/Asset/TradeSetup.daml:tradeSetup: ok, 6 active contracts, 10 transactions.
Modules internal to this package:
- Internal templates
  0 defined
  0 (100.0%) created
- Internal template choices
  0 defined
  0 (100.0%) exercised
- Internal interface implementations
  0 defined
    0 internal interfaces
    0 external interfaces
- Internal interface choices
  0 defined
  0 (100.0%) exercised
Modules external to this package:
- External templates
  7 defined
  5 ( 71.4%) created in any tests
  5 ( 71.4%) created in internal tests
  0 (  0.0%) created in external tests
- External template choices
  27 defined
  7 ( 25.9%) exercised in any tests
  7 ( 25.9%) exercised in internal tests
  0 (  0.0%) exercised in external tests
- External interface implementations
  0 defined
- External interface choices
  0 defined
  0 (100.0%) exercised in any tests
  0 (100.0%) exercised in internal tests
  0 ( 100.0%) exercised in external tests
```

摘要第一部分列出每个执行的 script，含交易总数与 script 结束时的活跃合约数。例如 `testMultiTrade` 执行 28 笔交易，最终 12 个活跃合约。

第二部分为覆盖率报告，显示包内全部 script 测试了多少模板与 choice，占模板与 choice 总数的比例。

## 调试、trace 与堆栈

上文展示了如何测试 happy path；若函数未按预期行为呢？Daml 提供 `debug` 与 `trace` 做细粒度 printf 调试：代码执行到时会向 StdOut 打印。二者关系类似 `abort` 与 `error`：

* `debug : Text -> m ()` 将文本映射为打印到 StdOut 的 Action。
* `trace : Text -> a -> a` 在表达式求值时打印到 StdOut。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml> let a : Script () = debug "foo"
daml> let b : Script () = trace "bar" (debug "baz")
[Daml.Script:378]: "bar"
daml> a
[DA.Internal.Prelude:532]: "foo"
daml> b
[DA.Internal.Prelude:532]: "baz"
daml>
```

不确定时优先用 `debug`，结果更易解读。

方括号内为最后位置，会给出触发打印的 Daml 文件与行号，但常无完整堆栈，因完整堆栈可能违反子交易隐私。若要为模块中纯函数代码启用堆栈，可使用 `DA.Stack` 模块机制，本节不再展开。

## 用 dpm sandbox 做本地测试

除 Daml Script 外，可用 `dpm sandbox` 运行本地 Canton sandbox 做集成测试。这会启动带内存账本的本地参与方节点，便于在部署到 DevNet 或 TestNet 前在更真实环境中测试合约。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm sandbox
```

sandbox 运行后，可通过 Ledger API（gRPC 或 JSON）交互，用 codegen 的 Java 或 TypeScript 客户端提交命令，并以真实 API 认证测试多方工作流。

### 何时用 sandbox 与 Daml Script

**用 Daml Script** 隔离测试合约逻辑：授权规则、choice 行为、多方工作流与边界情况。Script 进程内运行、无需账本，快速且确定，适合 Daml 模型的单元测试。

**用 sandbox** 当你需要测试应用与账本的集成，例如：

* 用 Java 或 TypeScript 后端对 Ledger API 测试
* 验证 codegen 类型序列化/反序列化
* 从前端测试 JSON API
* 运行多参与方配置
* 通过 Admin API 测试 DAR 上传、参与方分配与用户管理
* 在应用中验证授权 token 处理

### 何时用本地 Canton Network

[CN Quickstart](/sdks-tools/reference-projects/cn-quickstart) 含 LocalNet 配置，可在本地运行完整 Canton Network（参与方、sequencer、mediator 与 Splice 应用）。需要测试以下内容时用 LocalNet 而非 sandbox：

* Canton Coin 转账与 traffic 购买
* Wallet SDK 集成
* Splice API（Scan、Validator APIs）
* 涉及 Global Synchronizer 的端到端应用流

启动 LocalNet 见 [QuickStart 演练](/appdev/quickstart/running-the-demo)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
