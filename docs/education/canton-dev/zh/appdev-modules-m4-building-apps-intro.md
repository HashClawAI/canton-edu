---
title: "构建应用"
slug: "appdev-modules-m4-building-apps-intro"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-building-apps-intro.md"
source_title: "Building Applications"
tags:
  - appdev
  - modules
  - m4-building-apps-intro
---

# 构建应用

> 从 Daml 智能合约到完整的 Canton Network 应用

模块 4 架起编写 Daml 合约与交付完整应用之间的桥梁。你将了解 Canton 应用如何组织、有哪些 SDK 与 API，以及如何构建与账本交互的后端与前端组件。

## 前置条件

开始本模块前，应已完成 [模块 3：Daml 智能合约](/appdev/modules/m3-dev-environment)。你需要对 Daml 中的 template、choice 与授权有基本理解。熟悉 Java 或 TypeScript 有帮助，但非必需。

## 你将学到

* Canton 应用架构如何将角色（应用提供方、应用用户、终端用户）映射到基础设施
* 构建账本应用时可用的 SDK、API 与代码生成工具
* 如何构建提交命令并读取交易的后端服务
* 如何构建展示合约数据并集成钱包的前端
* 从应用开发者视角理解 Canton Coin 与 traffic

## 模块页面

<CardGroup cols={2}>
  <Card title="Application Architecture" icon="sitemap" href="/appdev/modules/m4-app-architecture">
    角色、层次及 Canton 应用各组件如何协同。
  </Card>

  <Card title="SDKs and APIs" icon="plug" href="/appdev/modules/m4-sdks-apis">
    代码生成、Ledger API、JSON API、PQS 与 Wallet SDK。
  </Card>

  <Card title="Backend Development" icon="server" href="/appdev/modules/m4-backend-dev">
    连接账本、提交命令、读取交易并查询 PQS。
  </Card>

  <Card title="Frontend Development" icon="browser" href="/appdev/modules/m4-frontend-dev">
    用生成的 TypeScript 绑定与钱包集成构建 React UI。
  </Card>

  <Card title="Canton Coin and Traffic" icon="coins" href="/appdev/modules/m4-canton-coin">
    了解 CC 如何购买 traffic 及管理交易成本。
  </Card>
</CardGroup>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
