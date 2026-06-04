---
title: "IDE 配置"
slug: "appdev-tooling-ide-setup"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/ide-setup.md"
source_title: "IDE Setup"
tags:
  - appdev
  - tooling
  - ide-setup
---

# IDE 配置

> 为 Canton 应用开发配置 VS Code 与其他 IDE（Daml、Java、全栈工具）。

正确配置的 IDE 可以使 Canton 开发速度显着加快。本页介绍了编写 Daml 合约、构建后端服务以及使用完整应用程序堆栈的设置。

## Daml Studio（VS Code）

Daml Studio 是用于编写 Daml 智能合约的主要 IDE。它是 VS Code 扩展，提供专为 Daml 构建的语言支持。

### 安装

1.安装[VS Code](https://code.visualstudio.com/)版本1.87或更高版本
2. 如果尚未安装 [DPM](/sdks-tools/cli-tools/dpm)
3. 从您的项目目录中，运行：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm studio
```

这将启动 VS Code，并为您的项目配置了 Daml 扩展。或者，在 VS Code 扩展市场中搜索“Daml”并手动安装。

### 特点

**类型检查**在您编辑时持续运行。错误和警告内联显示，问题面板显示摘要。在运行测试之前，类型检查可以捕获大多数问题。

**脚本结果**允许您直接从编辑器执行 Daml 脚本。单击出现在任何脚本定义上方的“脚本结果”镜头。结果面板将账本状态显示为表格：活动合约、存档合约和交易跟踪。这是验证合约逻辑是否按预期运行的最快方法。

**转到定义**适用于模板、选择、类型定义和导入的模块。在任何标识符上使用 `Ctrl+Click`（或 macOS 上的 `Cmd+Click`）。

**代码完成** 在您键入时建议模板字段、选择参数、标准库函数和导入的名称。

### Daml Studio 故障排除

如果类型检查不起作用：

* 从命令行验证`dpm build`是否成功。如果构建失败，IDE 将无法进行类型检查。
* 检查您的 `daml.yaml` 文件是否列出了正确的 SDK 版本和源目录。
* 重新启动Daml语言服务器：打开VS Code命令面板（`Ctrl+Shift+P`）并运行“Daml：重新启动语言服务器”。

## Java 和 Scala 后端开发

如果您的后端采用 Java 或 Scala（对于使用 Java 绑定的 Canton 应用程序来说很常见），IntelliJ IDEA 会提供最佳体验。

### IntelliJ 设置

1.安装[IntelliJ IDEA](https://www.jetbrains.com/idea/)（社区版或旗舰版）
2. 打开您的项目。如果使用 Maven 或 Gradle，IntelliJ 会自动检测构建系统。
3.运行`dpm codegen-java`后，将生成的代码目录标记为源根目录，以便IntelliJ索引生成的类。

IntelliJ 提供了到生成的 Daml Java 绑定的类型安全导航，这使得从后端代码跟踪到契约定义变得简单。

### TypeScript 后端开发

对于 TypeScript 后端（如 cn-quickstart），VS Code 是自然的选择。运行 `dpm codegen-js` 后，生成的 TypeScript 类型与 VS Code 的内置 TypeScript 语言服务集成，以进行自动完成和类型检查。

## 推荐的 VS Code 扩展

除了 Daml Studio 之外，这些扩展对于 Canton 全栈开发也很有用：* **Daml** -- Daml 语言支持（必需）
* **YAML** (Red Hat) -- 对 `daml.yaml`、`docker-compose.yml` 和配置文件的语法支持
* **Docker** (Microsoft) -- 管理 Docker 容器，对 LocalNet 很有用
* **Kubernetes** (Microsoft) -- 如果部署到 Kubernetes 很有帮助
* **ESLint** -- TypeScript/JavaScript 前端和后端代码的 Linting
* **Prettier** -- TypeScript、JSON 和 YAML 的代码格式
* **GitLens** -- 增强的 Git 集成

## 项目级配置

为了团队的一致性，请考虑将 `.vscode/extensions.json` 添加到您的存储库中，推荐使用 Daml 扩展：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "recommendations": [
    "DigitalAssetHoldingsLLC.daml"
  ]
}
```

您还可以添加具有特定于项目的设置（例如文件关联和编辑器格式设置规则）的 `.vscode/settings.json`。

## 后续步骤

* [开发工具概述](/appdev/tooling/development-tools-overview) -- 所有Canton开发工具汇总
* [开发环境设置](/appdev/modules/m3-dev-environment) -- Daml 开发入门
* [调试工具](/appdev/tooling/debugging-tools) -- 解决开发过程中的问题

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
