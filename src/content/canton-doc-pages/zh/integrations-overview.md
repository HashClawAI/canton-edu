---
title: "集成概览"
slug: "integrations-overview"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/overview.md"
source_title: "Integrations Overview"
tags:
  - integrations
  - overview
---

# 集成概览

> 将钱包、交易所与应用接入 Canton Network 生态

集成把你的应用连接到 Canton Network 的钱包、交易所、代币及其他服务生态，为应用开发者提供可直接复用的能力，也为终端用户提供可交互的入口。

## 集成类别

Canton Network 提供多类集成：

* **钱包** — 面向用户与应用开发者的 Canton Coin 管理
* **交易所集成** — 流动性桥接与法币出入金
* **代币标准** — 遵循 [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 的可互操作代币
* **应用集成** — 第三方应用连接

## 面向不同受众

### 终端用户

<CardGroup cols={2}>
  <Card title="选择钱包" icon="wallet" href="/zh/docs/canton/integrations-wallets-for-users">
    发现可用于管理 Canton Coin 的钱包选项。
  </Card>

  <Card title="发现应用" icon="grid-2" href="/zh/docs/canton/integrations-apps-finding-apps">
    探索基于 Canton Network 构建的应用。
  </Card>
</CardGroup>

### 开发者

<CardGroup cols={2}>
  <Card title="钱包集成" icon="code" href="/zh/docs/canton/integrations-wallet-guidance">
    使用 Wallet SDK 为应用添加钱包能力。
  </Card>

  <Card title="交易所集成" icon="building-columns" href="/zh/docs/canton/integrations-exchanges-guidance">
    连接交易所与流动性提供方。
  </Card>
</CardGroup>

## Canton 集成与其他生态的差异

Canton 的隐私模型使集成方式与公链不同：

* **余额私有** — 钱包仅向有权 Party 展示持仓，而非全网公开
* **交易私有** — 转账仅对参与方可见，而非区块浏览器公开
* **代币私有** — 代币余额仅持有人可见
* **探索器面向个人** — Canton 探索器只展示与你相关的交易，而非全网活动

<Note>
  与展示全部交易的以太坊区块浏览器不同，Canton 探索器仅显示你作为利益相关方的交易。这是设计使然。
</Note>

## 下一步

<CardGroup cols={2}>
  <Card title="集成模式" icon="puzzle-piece" href="/zh/docs/canton/integrations-integration-patterns">
    构建集成的常见模式。
  </Card>

  <Card title="Canton 生态" icon="globe" href="/zh/docs/canton/integrations-ecosystem">
    了解更广泛的 Canton Network 生态。
  </Card>
</CardGroup>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
