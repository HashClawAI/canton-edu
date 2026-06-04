---
title: "多托管与韧性"
slug: "appdev-deep-dives-multi-hosting"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/multi-hosting.md"
source_title: "Multi-Hosting and Resilience"
tags:
  - appdev
  - deep-dives
  - multi-hosting
---

# 多托管与韧性

> 将 Party 分布在多个验证者上，实现高可用、故障转移与数据韧性

多托管（multi-hosting）允许单个 Party 同时在多个验证者上托管。若某验证者下线，该 Party 可在其余验证者上继续运行——无需修改任何 Daml 逻辑。本文说明多托管原理、适用场景与配置方法。

## 为何需要多托管

仅托管在单一验证者上的 Party 存在单点故障：验证者离线期间无法提交交易或接收更新，直至恢复。多托管通过在多个验证者间分布 Party 解决该问题。

常见动机：

* **高可用** — 业务关键 Party 不能容忍停机
* **地理冗余** — 不同区域的验证者以抵御区域性故障
* **验证者迁移** — 在不中断业务的前提下逐步将 Party 迁到新验证者
* **组织韧性** — 将运营风险分散到独立管理的验证者
* **防范恶意运营方** — 确认阈值大于 1 时，单个恶意运营方无法单独作恶

## 多托管如何工作

多托管由 Canton 拓扑系统管理。Party-to-participant 映射声明哪些验证者托管某 Party，以及各验证者的权限（Submission、Confirmation 或 Observation）。

当本地 Party 在多个验证者上以 Submission 权限托管时，任一验证者均可代表该 Party 提交命令。对外部 Party，提交发生在以 Confirmation 权限托管该 Party 的任一验证者上。同步器将交易视图投递到所有托管验证者，各自维护该 Party 合约的一致视图。

### 确认阈值

可配置确认阈值：需有多少托管验证者确认后交易才继续。阈值为 1（未指定时的默认）时，任一托管验证者可确认；更高阈值需多方独立确认，完整性更强但延迟更高。阈值大于 1 可防范恶意验证者。

### 权限级别

每个托管验证者分配三种权限之一：

* **Submission** — 可代表 Party 提交命令；仅适用于本地 Party（密钥由验证者管理）。
* **Confirmation** — 可确认该 Party 的交易；主动托管的标准权限。
* **Observation** — 接收交易数据但不能提交或确认；适用于只读副本、审计节点或迁移目标预置。

## 为新 Party 配置多托管

多托管需要拓扑交易，将 Party 映射到多个验证者。所有托管验证者须签署该映射——提案仅在各方同意后生效。

<Note>
  以下说明适用于**新的外部 Party**。为既有 Party 增加托管节点称为 [party replication](/zh/docs/canton/global-synchronizer-production-operations-party-management#simple-party-replication)，流程更复杂。外部 Party 须用自身密钥授权 party-to-participant 映射，详见[外部签名入驻](/zh/docs/canton/appdev-deep-dives-external-signing-onboarding)。
</Note>

### 通过 Ledger API

入驻外部 Party 时，在拓扑请求中包含额外验证者：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "otherConfirmingParticipantUids": ["PAR::participant2::1220a4d7..."],
  "confirmationThreshold": 1
}
```

生成的拓扑交易须上传到各托管验证者的 Ledger API。通过 allocate 端点上传且提及本地验证者的映射会自动由本地验证者签署并转发。若未完全授权，则作为提案；既有提案会合并新签名，足够后生效。

### 通过 Canton 控制台

适用于可访问双方控制台的内置 Party。在第一个验证者上创建提案，在第二个验证者上 `list_hosting_proposals` 后 `authorize`。双方签署后可用 `parties.hosted` 验证。

## 数据韧性模式

多托管解决**计算韧性**；**数据韧性**依赖 PQS 等查询层。见 [PQS](/sdks-tools/development-tools/pqs#high-availability-and-database-sharing)。

## 多托管与其他韧性策略

* 单验证者 + 备份 — 可接受停机时最简单
* 多托管 — 持续可用且防恶意验证者
* 多托管 + 观察节点 — 只读扩展/审计
* 跨同步器多托管 — 韧性与多同步器访问

## 运维考量

* **成本** — 确认方数量与阈值影响流量消耗
* **一致性** — 交易一致，PQS offset 可能略异
* **密钥** — 各方独立密钥；安全取决于阈值
* **移除托管** — 新拓扑交易移除验证者即可

## 下一步

* [去中心化](/zh/docs/canton/appdev-deep-dives-decentralization)
* [组合与多方工作流](/zh/docs/canton/appdev-deep-dives-composition-multi-party)


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
