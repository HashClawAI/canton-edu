---
title: "合规考量"
slug: "appdev-modules-m7-compliance"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-compliance.md"
source_title: "Compliance Considerations"
tags:
  - appdev
  - modules
  - m7-compliance
---

# 合规考量

> Canton 应用的隐私、审计与监管相关考量

Canton 架构在隐私与审计方面与公链有本质差异。本文汇总在 Canton Network 上构建应用时需了解的合规相关技术特性。

<Warning>
  本文提供 Canton 能力的技术事实，不构成法律意见。请就所在司法辖区的监管合规咨询合格法律顾问。
</Warning>

## 隐私特性

### 子交易隐私

Canton 不会向所有 validator 广播完整交易。每笔交易分解为**视图**，各 validator 仅接收与其托管 party 相关的视图。非某部分 stakeholder 的 validator 看不到该部分——无载荷、无参与 party，甚至不知其存在。

因此：

* 合约数据仅对 Daml 模板定义的 signatory、observer 与 controller 可见
* Synchronizer（sequencer 与 mediator）处理加密消息，不见明文交易数据
* Validator 仅存储涉及其托管 party 的合约与交易

可见性规则详见 [Privacy Model Explained](/zh/docs/canton/overview-learn-privacy-model)。

### 无全局状态可见性

与任何参与者可读全账本不同，Canton validator 维护私有本地账本分片。无共享的全合约数据库。Party 无法查询无权查看的合约，validator 也无法访问未托管 party 的数据。

## 审计能力

### Ledger API 交易历史

各 validator 维护其托管 party 相关交易的完整只追加历史。应用可通过 Ledger API 更新流读取按时间顺序的合约创建、choice exercise 与归档记录。

### PQS 历史查询

Participant Query Store（PQS）维护镜像账本状态的 PostgreSQL 数据库，保存当前活跃合约集与完整合约事件历史，适合审计查询：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find all archived contracts of a given template, with timestamps
SELECT contract_id, payload, created_at, archived_at
FROM contracts('your-module:YourTemplate')
WHERE archived_at IS NOT NULL
ORDER BY archived_at DESC;
```

PQS 数据保留取决于底层 PostgreSQL 维护策略，由你控制保留策略。

### Daml 中的审计方模式

可在智能合约层将审计 party 加为 observer，审计方可见合约及影响它的所有事件但不可修改。代码示例见 [Privacy Model](/zh/docs/canton/overview-learn-privacy-model)。

## 数据驻留

### 私有 Synchronizer

若监管要求数据留在特定地理区域，可在你选择的司法辖区内运营**私有 synchronizer**。连接私有 synchronizer 的 validator 仅通过你控制的该基础设施通信。

Validator 可同时连接 Global Synchronizer（跨网络互操作）与一个或多个私有 synchronizer（辖区专属工作流）。多 synchronizer 架构可在不为此每种工作流单独建全套基础设施的情况下，将受监管工作流与公开工作流分离。

### Validator 级数据控制

Validator 仅存储托管 party 的数据，组织数据位于自有 validator 基础设施。你可选择部署位置——本地、特定云区域或多地。除非另一 validator 托管共享合约的 stakeholder party，否则其他 validator 不持有你的数据副本。

## 不可变账本与数据修改请求

Canton 账本只追加。合约就地修改，而是归档并替换。交易历史不可重写。

对要求修改或删除数据的法规（如 GDPR 删除权），可考虑：

* **合约设计** — 将个人身份信息（PII）存于链下，账本上仅保留不透明 ID 引用。删除链下数据可使链上引用失效。
* **PQS 数据管理** — PQS 是你控制的投影，可在不影响账本的情况下清除或匿名化 PQS 记录。
* **修剪（Pruning）** — Canton 支持账本修剪，在可配置保留期后从 validator 本地存储删除旧交易数据，修剪后无法通过 Ledger API 访问。

以上为技术机制。是否满足具体监管要求取决于法规与法律顾问解释。

## 应用设计指南

* 在合约层用 Daml signatory/observer 强制执行可见性，而非仅在应用层
* 需审计轨迹的合约将审计 party 加为 observer
* 敏感 PII 存链下，账本上仅 ID 引用
* 严格数据驻留要求的工作流使用私有 synchronizer
* 按监管义务配置账本修剪保留期

## 延伸阅读

* [Privacy Model Explained](/zh/docs/canton/overview-learn-privacy-model) — 子交易隐私详情
* [Security Best Practices](/zh/docs/canton/appdev-modules-m7-security) — 保护 Canton 应用
* [Architecture Overview](/zh/docs/canton/overview-learn-architecture) — Validator 与 synchronizer 关系

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
