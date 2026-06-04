---
title: "去中心化"
slug: "appdev-deep-dives-decentralization"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/decentralization.md"
source_title: "Decentralization"
tags:
  - appdev
  - deep-dives
  - decentralization
---

# 去中心化

> 从单验证者到 BFT 同步器，Canton 栈各层的去中心化策略。

Canton 支持从集中到完全去中心化的光谱。不必一开始就全力去中心化——可从简单单验证者部署起步，随应用信任需求演进逐步去中心化。

## 去中心化光谱

Canton 架构有多层可做去中心化选择，信任含义各不相同：

* **应用层** — 多少验证者托管应用中的 Party（如多方托管或去中心化 Party）
* **同步器层** — 同步器由单一还是多个实体运营
* **网络层** — 使用 Global Synchronizer、私有同步器或两者

每一层去中心化程度越高，对单一实体的信任越少，但运维复杂度也越高。

## 单验证者

最简单部署：应用所有 Party 托管在连接 Global Synchronizer 的单一验证者上。

**信任模型：** 你信任验证者运营方（自己或第三方）诚实处理交易并保持数据可用。Global Synchronizer 的 BFT 仍防范同步器层攻击，但验证者是应用在验证者层面的单点故障。

**适用场景：**

* 早期开发与原型
* 所有 Party 同属一个组织的应用
* 可接受单一可信运营方的场景

## 多验证者

应用中不同 Party 托管在不同、独立运营的验证者上。这是 Canton Network 上跨组织应用的标准部署。

**信任模型：** 各组织运营自己的验证者并控制自己的数据。没有单一验证者能看到全部交易——Canton 隐私模型保证每个验证者仅看到涉及其 Party 的交易。同步器将加密交易视图路由到相应验证者。每个 Party 信任自己的验证者运营方。

**适用场景：**

* 跨组织工作流（交易、结算、供应链）
* 各方不愿将数据托付给单一运营方的应用
* Canton Network 上的生产应用

## 多方托管 Party

单个 Party 可同时托管在多个验证者上。一个验证者宕机时，Party 可在其他节点继续操作，无需改动 Daml 逻辑即可提升韧性。

**信任模型：** Party 至少信任一个托管它的验证者。这会削弱对运营方的信任要求——托管该 Party 的所有验证者在达到共识阈值时需一致。若阈值为 1，涉及该 Party 的交易可能由任一托管验证者处理，降低单点故障风险，但需信任多个验证者。

**适用场景：**

* 不能接受单一验证者宕机的高可用需求
* 需要地理冗余的组织
* 在验证者之间逐步迁移

实现细节见 [多方托管](/appdev/deep-dives/multi-hosting)。

## BFT 同步器

Global Synchronizer 本身是去中心化的，由一组 Super Validator（SV）通过拜占庭容错（BFT）共识（CometBFT）运营。单个 SV 无法审查交易或操纵排序。

**信任模型：** Global Synchronizer 可容忍最多三分之一 SV 故障或恶意；只要三分之二 SV 诚实，同步器即正确运行。这是 Canton 在基础设施层提供的最高去中心化程度。

**适用场景：**

* Global Synchronizer 已是 BFT——其上所有应用自动受益
* 多运营方联合运行私有同步器时也可配置 BFT

## 多同步器

Canton 支持验证者同时连接多个同步器。Party 可在 Global Synchronizer 与一个或多个私有（扩展）同步器上拥有合约，并能在其间 **reassign** 合约。

**信任模型：** 不同工作流可有不同信任属性。敏感双边交易可用双方运营的私有同步器，而针对 Canton Coin 的结算发生在公共 Global Synchronizer。

**适用场景：**

* 隐私/性能需求混合的应用
* 既需公共结算又需私有处理的工作流
* 对数据处理位置有监管要求或特殊隐私需求的组织

## 如何选择

合适去中心化程度取决于应用具体需求：

* **从简开始** — 多数应用因跨组织工作流是 Canton 主场景，从多验证者部署起步
* **增加韧性** — 需要高可用时采用多方托管
* **BFT 内置** — 使用 Global Synchronizer 的应用无需额外应用层配置即享有 BFT
* **增强隐私** — 部分工作流需私有处理时使用多同步器

不必一开始就按最高去中心化设计。Canton 允许通过增加验证者、在更多节点托管 Party 或连接新同步器逐步去中心化——**无需修改 Daml 代码**。

## 下一步

* [多方托管](/appdev/deep-dives/multi-hosting) — 跨验证者分布 Party 的实现细节
* [组合与多方工作流](/appdev/deep-dives/composition-multi-party) — 多方交互的 Daml 模式


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
