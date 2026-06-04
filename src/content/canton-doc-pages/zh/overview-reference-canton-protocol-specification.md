---
title: "Canton 协议规范"
slug: "overview-reference-canton-protocol-specification"
locale: "zh"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/canton-protocol-specification.md"
source_title: "Canton Protocol Specification"
tags:
  - overview
  - reference
  - canton-protocol-specification
---

# Canton 协议规范

> Canton 协议架构技术规范：涵盖共识层、交易处理与拓扑管理

本节提供 Canton 协议完整技术规范。[Learn](/zh/docs/canton/overview-learn-architecture) 页面在高层次介绍概念；本参考页详述协议机制——数据结构、信任假设、消息流与形式化性质，它们是 Canton Network 的基础。

## 协议架构

Canton 将多数区块链混为一体的两件事分离：**智能合约验证**与**交易排序**。结果是可独立优化的双层共识架构。

| 层                        | 职责                             | 机制                           | 信任边界         |
| ---------------------------- | ------------------------------------------ | ----------------------------------- | ---------------------- |
| **Smart contract consensus** | 验证交易正确性           | Proof of Stakeholder（点对点） | 仅受影响 Party  |
| **Ordering consensus**       | 建立一致的 synchronizer 排序 | 经 Sequencer 的 BFT 排序         | Synchronizer 运营方 |

协议跨三类节点运行：

* **Participant 节点**托管 Party、维护其 Active Contract Set (ACS)、代其执行智能合约共识协议，并提供 LAPI。
* **Sequencer 节点**提供带发送方隐私的认证、事件有序多播
* **Mediator 节点**促成将验证结果绑定为最终交易决策的两阶段提交协议

Participant 与 Mediator 不直接通信。所有消息经 Sequencer 全局排序。载荷加密，Sequencer 仅见元数据——接收方列表与消息大小——而非交易内容。

## 参考页面

<CardGroup cols={2}>
  <Card title="Ledger Model (Detailed)" icon="layer-group" href="/zh/docs/canton/overview-reference-ledger-model-detailed">
    扩展 UTXO 模型：templates、利益相关方、choices、交易结构、视图与 witnesses。
  </Card>

  <Card title="Smart Contract Consensus" icon="handshake" href="/zh/docs/canton/overview-reference-smart-contract-consensus">
    Proof of Stakeholder 验证、隐私保护共识与信任域对比。
  </Card>

  <Card title="Ordering Consensus" icon="arrow-down-1-9" href="/zh/docs/canton/overview-reference-ordering-consensus">
    Sequencer 与 Mediator 架构、BFT 排序服务与 ISS 启发式共识协议。
  </Card>

  <Card title="Transaction Lifecycle" icon="rotate" href="/zh/docs/canton/overview-reference-transaction-lifecycle">
    从准备到提交的完整五阶段生命周期。
  </Card>

  <Card title="Topology" icon="diagram-project" href="/zh/docs/canton/overview-reference-topology">
    命名空间管理、密码学密钥、Party-to-participant 映射与拓扑交易。
  </Card>
</CardGroup>

## 关键性质

Canton 协议提供以下保证：

* **子交易隐私**：各方仅见与其相关的交易部分。Sequencer 与 Mediator 无法读取交易载荷。
* **完整性**：仅当全部所需利益相关方确认且每个 signatory 的智能合约逻辑通过验证时，交易才可提交。
* **一致性**：排序层通过在给定 synchronizer 上为全部状态变更提供单一全局顺序，有助于防止双花。
* **最终性**：Mediator 发出提交裁决并经排序后，交易结果即为最终。无分叉或重组。
* **活性**：在 BFT 容错阈值内（故障排序节点少于三分之一），协议可推进。

## 两层如何交互

Daml 交易在其生命周期中穿越两层共识：

1. 提交 Participant 在本地准备交易（智能合约层）
2. Participant 向 Sequencer 发送加密视图（排序层）
3. Sequencer 将视图分发给受影响 Participant，并向 Mediator 发送 informee 消息
4. 各确认 Participant 验证其视图并向 Mediator 发送确认或拒绝（智能合约层，经排序层）
5. Mediator 在所需时间窗内汇总裁认并发出裁决，Sequencer 分发给所有 Participant（排序层）

各阶段详见 [Transaction Lifecycle](/zh/docs/canton/overview-reference-transaction-lifecycle)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
