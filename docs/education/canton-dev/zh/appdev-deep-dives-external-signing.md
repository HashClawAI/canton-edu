---
title: "外部签名"
slug: "appdev-deep-dives-external-signing"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/external-signing.md"
source_title: "External Signing"
tags:
  - appdev
  - deep-dives
  - external-signing
---

# 外部签名

> 使用外部加密密钥签署 Canton 交易——概述、入网与提交。

# 外部签名

## 你将学到什么

本系列教程介绍如何：

* 使用 Ledger API 以外部密钥入网 Party 并签署交易
* 使用 Ledger API 入网多方托管的外部 Party
* 使用外部签名创建合约
* 使用外部签名在合约上 exercise choice

进阶场景可参考 Admin API 管理 Party 或用外部签名提交更通用的拓扑交易：

* 使用 Admin API 入网外部 Party
* 构建、签署并提交拓扑交易

## 背景

Canton 账本状态由 **Party 拥有的合约** 定义。每份合约规定各方单方面变更共享账本的权利。从 Party 视角，关键活动是 **发起交易** 与 **验证交易**。

**Party** 是账本上的逻辑参与者，其链上表示与状态管理委托给一个或多个所选 **验证者**。因 Canton 隐私特性，只有这些验证者掌握 Party 拥有的全部合约，因而只有它们能权威地验证并确认影响该 Party 合约的交易。

交易只能涉及当前正被托管的 Party；引用无效 Party 的交易会被系统拒绝。

### 拓扑与身份

Party、验证者与同步器在 Canton 中的身份表示为 **唯一标识符**，每个标识符为名称与公钥指纹对 `<prefix>::<fingerprint>`，详见拓扑管理概述。公钥用于最终验证与身份相关的授权。

Party 如何设置由一组拓扑交易定义。这些交易须由所有受影响 Party 与验证者签署并提交到账本。全部拓扑交易之和定义 **拓扑状态**——各方对 Party、密钥、验证者与包的共享认知。

拓扑状态可演进。Party 不绑定初始配置；跨节点复制 Party 是验证者运营方之间的运维流程，不在本节讨论。

### 托管关系

设置 Party 须与一个或多个验证者建立 **托管关系**，通过名为 **party to participant mapping** 的拓扑交易表达，须由 Party 与相关验证者签署。托管关系中，Party 定义用于授权影响其合约的交易的私钥；该私钥可由用户管理，也可将签署委托给验证者。据此区分两类托管：

* **外部 Party**：授权私钥由 Party 用户（终端钱包或后端应用）持有并操作。
* **内部 Party**：验证者密钥代表 Party 授权交易，用户通过 Ledger API 上的 JWT 认证。

内部 Party 运维更简单，无需额外保管私钥，但最终需信任验证者不会滥用私钥授权交易。Party 与 participant 的托管关系通过三类验证者权限定义：

* **Submission**：验证者签名密钥用于授权交易
* **Confirmation**：验证者签名密钥仅用于确认交易
* **Observation**：验证者仅获知并验证状态，无需确认

授予 **Submission** 即该 Party 为内部 Party。若仅授予 **Confirmation** 或 **Observation**，则为外部 Party，须用额外拓扑交易 **party to key mapping** 定义授权密钥。

请继续下一教程了解如何用 Ledger API 入网外部 Party。内部 Party 见 party management 文档。

### 多方托管 Party

为降低对单一验证者的完全信任，Party 可配置托管关系，要求若干验证者批准交易后才视为有效。这又划分部署维度：

* **单托管 Party**：仅由一个验证者托管，最简单，适用于 Party 所有者完全信任该验证者。
* **多方托管 Party**：由多个验证者托管，通过分散信任提升安全与可用性。

请按教程学习如何用 Ledger API 设置多方托管 Party。

概括而言，Party 要使用账本须定义以下拓扑状态：

* Party 名称及其用于授权交易的签名密钥
* 哪些验证者以何种权限与阈值托管该 Party
* 验证拓扑交易签名所需的命名空间委托

托管选择对 Party 的安全与可用性影响重大，请参阅 party trust model 中的信任假设。

### 通过 Admin API 管理拓扑

拓扑系统灵活强大但也复杂。需多方独立签署时，构建、签署与提交流程可能繁琐。拓扑交易也可作为 **proposal** 通过账本分发——proposal 是尚未被所有必要参与者签署的拓扑交易。

与 Party 相关的 Admin API 拓扑管理任务见：

* 使用 Admin API 入网外部 Party
* 构建、签署并提交拓扑交易

### 交易提交

Party 设置完成后即可通过提交创建合约或 exercise choice 的交易使用账本。使用外部密钥授权的 Party，提交流程为：

* 向所选验证者节点提交命令以解释命令并生成结果交易；交易尚未发往账本，而是返回给用户。
* 用 Party 私钥验证并签署交易哈希（对整个结果交易——命令与结果——的承诺）。
* 将预计算交易与签名提交给验证者节点以提交到账本。
* 通过托管该 Party 的验证者节点观察交易结果。

更详细说明见 external signing overview。

注意：签名是对整个交易输出的承诺，而非仅命令。若解释器有误，验证者会拒绝交易。可通过任意节点提交，不限于托管该 Party 的节点。

如何用外部签名密钥提交命令见：创建合约、exercise choice 等教程。


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
