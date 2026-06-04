---
title: "Canton Network QuickStart"
slug: "appdev-quickstart-index"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/index.md"
source_title: "Canton Network QuickStart"
tags:
  - appdev
  - quickstart
  - index
---

# Canton Network QuickStart

> 用 cn-quickstart 项目在本地运行完整 Canton Network 应用

[Canton Network QuickStart](https://github.com/digital-asset/cn-quickstart)（cn-quickstart）是在本机获得可工作 Canton Network 环境的参考应用，包含 Daml 模型、Java 后端、React 前端、带模拟 Global Synchronizer 节点的本地 Canton 沙箱，以及构建与测试自有应用的工具。

QuickStart 演示软件许可工作流：应用提供方为用户创建许可，用户可请求续期并用 Canton Coin 付款。该流程覆盖生产 Canton Network 应用的核心模式：多方协议、提议-接受流程与代币转账。

## 你将获得什么

QuickStart 会搭建名为 LocalNet 的本地环境，包括：

* **模拟 Canton Network**：超级验证者节点、sequencer 与 mediator
* **应用提供方节点**：运行 participant 并部署许可应用
* **应用用户节点**：独立 participant 与钱包
* **React 前端**：支持提供方与用户角色
* **Java 后端**：处理 Ledger API 交互
* **Canton Coin 钱包**：用于流量购买与支付流程
* **[lnav](/appdev/quickstart/lnav)** 日志分析，便于调试与排障

## 本节页面

<CardGroup cols={2}>
  <Card title="前置条件与安装" icon="download" href="/appdev/quickstart/prerequisites">
    系统要求、依赖与分步安装
  </Card>

  <Card title="项目结构" icon="folder-tree" href="/appdev/quickstart/project-structure">
    QuickStart 项目组织与各组件职责
  </Card>

  <Card title="运行演示" icon="play" href="/appdev/quickstart/running-the-demo">
    启动应用并走通许可工作流
  </Card>
</CardGroup>

## 开始之前

QuickStart 假定你已熟悉模块 1（理解 Canton），理想情况下也学过模块 3（Daml 智能合约）。运行演示不必是 Daml 专家，但理解模板、choice 与多方授权有助于理解应用在做什么。

<Note>
  QuickStart 仓库是构建自有 Canton Network 应用的推荐起点。跑通演示后，可修改 Daml 模型、后端与前端以实现你的业务逻辑。
</Note>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
