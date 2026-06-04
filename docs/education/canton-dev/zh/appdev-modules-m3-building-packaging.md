---
title: "构建与打包"
slug: "appdev-modules-m3-building-packaging"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-building-packaging.md"
source_title: "Building and Packaging"
tags:
  - appdev
  - modules
  - m3-building-packaging
---

# 构建与打包

> 构建 Daml 项目、管理依赖并将 DAR 打包用于部署

# 处理依赖

`compose` 中的原子交换模型可扩展。变更分两类：**升级**（改现有逻辑，见[智能合约升级](/zh/docs/canton/appdev-deep-dives-smart-contract-upgrade)）与**扩展**（仅增模板）。本节用多 leg 交易扩展示例，并说明 Daml 栈架构、依赖与标识符。

设置：在基目录 `dpm new intro-compose --template daml-intro-compose`（目录名 `intro7` 会被引用），同目录 `dpm new intro-9 --template daml-intro-9`。`Dependencies` 含 `Intro.Asset.MultiTrade` 与测试模块。

## DAR、Daml-LF 与引擎

DAR 类似 JAR，为 ZIP。`dpm build -o assets.dar` 后 `dpm damlc inspect-dar assets.dar`：

1. 项目及依赖的 `*.dalf`（Daml-LF 二进制，由 Daml Engine 在账本执行，类比 JVM 与字节码）
2. 原始 `.daml` 源码
3. `*.hi` / `*.hie`
4. 元数据与配置

## 哈希与标识符

`inspect-dar` 列出的十六进制串是**包哈希**，是可靠且持久的包标识。名称/版本（如 intro7-1.0.0）仅供人类阅读，不可单独依赖。Ledger API 上类型以 `(实体名, 模块名, 包哈希)` 标识；客户端应知晓要交互的包哈希。`inspect-dar --json` 的 `main_package_id` 即项目包哈希。

部署到账本后，依赖常丢失名称、只剩哈希；`*.daml`/`*.hi`/`*.hie` 不再保留——引出 data-dependencies。

## dependencies 与 data-dependencies

`daml.yaml` 的 `dependencies` 依赖 `*.hi`（标准库等）。这些信息在链上 DAR 中不保留，且跨 SDK 版本并存两套类型会混乱，故**不支持跨 SDK 的 dependencies**。

从账本取回或旧 SDK 的合约模型应使用 **data-dependencies**（语法相同，仅依赖 `*.dalf`），主要用于跨项目的记录、Choice、Template 与数据组合。扩展模型宜用 data-dependencies；测试脚本通常单独包、勿部署到生产账本。

## 项目结构建议

标识符依赖整个包，包会带上全部依赖——依赖图宜简单，变更频率不同的关注点拆包。脚本与模板同包会使改测试就改全部标识符；`Trade` 与 `Asset` 若变更频率不同可拆项目。

## 使用 dpm 构建

Canton Network 项目用 [`dpm`](https://docs.canton.network/sdks-tools/cli-tools/dpm)：

* `dpm build` — 编译并产出 DAR
* `dpm build --all` — 多包项目全部构建
* `dpm test` — 运行 Daml Script 测试
* `dpm codegen-java` / `dpm codegen-js` — 生成绑定
* `dpm sandbox` — 本地 Canton 沙箱

`dpm` 封装编译器与构建系统，处理 SDK 版本与依赖解析。

# 如何构建 Daml Archive (.dar)

## 定义 Daml 包

### 单包

根目录 `daml.yaml`：`sdk-version`、`name`（小写连字符）、`version`、`source: daml`、`dependencies: [daml-prim, daml-stdlib]`。`.daml` 文件放在 `source` 目录，文件名与模块头一致（点作目录），**UpperCamelCase**。

`dpm new` 提供多种模板。

### 多包

工作流与测试宜分属不同包。在上级目录建 `multi-package.yaml`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
packages:
  - ./my-package1
  - ./my-package2
```

路径指向含 `daml.yaml` 的目录。可用环境变量避免重复，如 `sdk-version: $SDK_VERSION`，构建前设置 `SDK_VERSION=3.4.9 dpm build --all`。

## 构建

单包目录运行 `dpm build`；多包在含 `multi-package.yaml` 的目录运行 `dpm build --all`。默认输出 `.daml/dist/<name>-<version>.dar`，可用 `--output` 或 `build-options` 覆盖。配置变更出问题时可 `daml clean` 或 `daml clean --all`。

## 依赖其他 Daml 包

在 `daml.yaml` 添加：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
data-dependencies:
  - ./path/to/your/dep.dar
```

`dependencies` 保留给 daml-prim、daml-stdlib 及可选 daml-script。模块名冲突见 module-prefixes。`multi-package.yaml` 中的包会按正确顺序构建。

## 第三方包

尚无专用 Daml 包仓库；`.dar` 体积小、变更少，宜检入 `dars/vendored` 并校验哈希。分发时文档说明获取方式。跨 SDK 的 `daml-script` 测试库建议 vendored（如 token-standard 测试 harness）。

## 如何拆分包

* **工作流与测试分家** — 避免把 daml-script 部署到生产账本
* **公开 API 与实现分家** — 接口单独包（如 Token Standard 接口）
* **按业务域拆分** — 减少无关域审计负担

## 下一步

`MultiTrade` 有更复杂控制流与数据处理；[语言基础](/zh/docs/canton/appdev-modules-m3-language-fundamentals) 将讲控制流、fold、类型类、自定义函数与标准库。勿删除 intro 目录。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
