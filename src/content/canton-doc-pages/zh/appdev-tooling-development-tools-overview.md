---
title: "开发工具概览"
slug: "appdev-tooling-development-tools-overview"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/development-tools-overview.md"
source_title: "Development Tools Overview"
tags:
  - appdev
  - tooling
  - development-tools-overview
---

# 开发工具概览

> Canton 开发工具链概览：DPM、Daml Studio、Canton Console、Sandbox、LocalNet 与 PQS。

Canton 应用程序开发涉及多种处理工作流程不同部分的工具——从编写和编译 Daml 合约到本地测试和查询账本状态。本页总结了每个工具以及使用它的时间。

## DPM（Daml 包管理器）

DPM 是 Canton 项目管理的主要命令行工具。它处理项目初始化、依赖关系管理、编译、代码生成和测试。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm init                  # Create a new project
dpm build                 # Compile Daml contracts to DAR files
dpm test                  # Run Daml Script tests
dpm codegen-js .dar -o out  # Generate TypeScript bindings
dpm codegen-java .dar -o out # Generate Java bindings
dpm sandbox               # Start a local Sandbox node
dpm studio                # Launch Daml Studio (VS Code)
```

DPM 取代了旧的 `daml` CLI，并且是所有构建和项目任务的推荐入口点。有关完整命令集，请参阅 [DPM 参考](/sdks-tools/cli-tools/dpm)。

## Daml Studio（VS Code 扩展）

Daml Studio 是一个 VS Code 扩展，为编写 Daml 智能合约提供 IDE 体验。它包括：

* 在您键入时进行实时类型检查和错误诊断
* 转到定义和查找参考导航
* 脚本结果可视化——直接从编辑器运行 Daml 脚本，并在表格视图中检查生成的账本状态
* 模板、选择和标准库函数的代码完成

通过从项目目录运行 `dpm studio` 来安装它，或者在 VS Code 扩展市场中搜索“Daml”。需要 VS Code 1.87 或更高版本。

有关完整的设置说明，请参阅 [IDE 设置](/zh/docs/canton/appdev-tooling-ide-setup)。

## Canton Console

Canton 控制台是一个基于 Scala 的交互式 REPL，用于检查和管理 Canton 节点。您可以用它来：

* 查询验证器上的活动合约集（ACS）
* 检查事务树和事件详细信息
* 将DAR包上传到验证器
* 管理 Party及其举办
* 检查节点健康状况和连接性

该控制台连接到正在运行的 Canton 节点，并提供对管理和诊断操作的直接访问。它在开发过程中对于验证事务是否产生了预期状态特别有用。

## Sandbox

Sandbox 是一个轻量级的单节点 Canton 环境，用于快速本地测试。开始：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm sandbox
```

Sandbox 为您提供了一个带有内存分类账的本地验证器。它启动速度快，适合运行 Daml Script 测试、试验合约逻辑以及迭代 Daml 代码，而无需外部依赖。

沙箱不会模拟多验证器或多方不同验证器的场景。为此，请使用 LocalNet。

有关配置选项，请参阅[沙盒](/sdks-tools/development-tools/sandbox)。

## LocalNet

LocalNet 是一个基于 Docker Compose 的本地环境，它模拟具有多个验证器的全局同步器。 [cn-quickstart](https://github.com/digital-asset/cn-quickstart) 存储库将 LocalNet 打包为其开发设置的一部分：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd cn-quickstart/quickstart
make setup
make build
make start
```LocalNet 提供本地同步器、多个验证器节点、具有水龙头访问的测试 Canton Coin 和 Splice 钱包。它是部署到 DevNet 之前进行集成测试、多方工作流程和端到端应用程序测试的正确环境。

有关详细信息，请参阅 [LocalNet](/sdks-tools/development-tools/localnet)。

## PQS（参与者查询存储）

PQS 维护一个与验证器的账本状态同步的 PostgreSQL 数据库。它将分类帐事件（创建、存档、练习）投影到 SQL 表中，您可以使用标准 SQL 进行查询。

当您需要以下情况时，PQS 非常有用：

* 跨多种合约类型的复杂查询（连接、聚合、过滤器）
* 历史账本数据的报告和分析
* 与使用 SQL 的 BI 工具或仪表板集成
* 合约有效负载的全文搜索或自定义索引

PQS 尊重与 Ledger API 相同的隐私边界——它只包含您方有权查看的数据。

有关架构详细信息和查询示例，请参阅 [PQS](/sdks-tools/development-tools/pqs) 和 [PQS SQL 参考](/zh/docs/canton/api-reference)。

## 选择正确的工具

* **编写和编译 Daml 合约** -- DPM + Daml Studio
* **运行合约逻辑的单元测试** -- `dpm test`（Daml 脚本）
* **Daml 代码的快速本地迭代** -- 沙箱
* **多验证器集成测试** -- LocalNet
* **交互式检查合约状态** -- Canton Console
* **复杂的查询和报告** -- PQS

## 后续步骤

* [IDE 设置](/zh/docs/canton/appdev-tooling-ide-setup) -- 配置您的编辑器以进行 Canton 开发
* [调试工具](/zh/docs/canton/appdev-tooling-debugging-tools) -- 交易和合约状态故障排除
* [Canton Development Stack](/zh/docs/canton/appdev-modules-m1-development-stack) -- 所有部分如何组合在一起

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
