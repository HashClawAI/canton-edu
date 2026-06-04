---
title: "Admin API 参考"
slug: "appdev-reference-admin-api-reference"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/admin-api-reference.md"
source_title: "Admin API Reference"
tags:
  - appdev
  - reference
  - admin-api-reference
---

# Admin API 参考

> Canton 节点管理用 Admin API 参考文档

Admin API 提供对 Canton participant、sequencer 与 mediator 节点的管理访问，用于节点配置、拓扑管理、密钥管理及 Ledger API 不暴露的运维任务。

<Warning>
  切勿将 Admin API 暴露到公网。仅通过 VPN 或私有网络限制访问。Admin API 对节点拥有完整管理权限。
</Warning>

## 访问方式

Admin API 使用 gRPC，位于 participant 的 Admin API 端口（默认 5002）。也可通过 Canton Console 访问，Console 在 Scala REPL 中封装 Admin API 调用。

## 核心服务组

### 健康与状态

* **StatusService** — 检查节点健康、就绪状态及已连接 synchronizer

### 拓扑管理

拓扑命令管理分布式拓扑状态，控制 party 与 participant 映射、包 vetting 与 synchronizer 参数。

* **TopologyManagerReadService** — 读取当前拓扑（party 映射、已 vet 包、命名空间委托等）
* **TopologyManagerWriteService** — 提议拓扑变更（需相应授权）

### Synchronizer 连接

* **SynchronizerConnectivityService** — 连接、断开与重连 synchronizer；列出已连接与已注册 synchronizer

### 包管理

* **PackageService** — 上传 DAR、列出包、管理包 vetting
* **DarService** — 上传与管理 DAR 文件

### 密钥管理

* **VaultService** — 管理加密密钥：生成、列出、轮换；支持外部 KMS 集成

### 修剪（Pruning）

* **PruningService** — 修剪旧账本数据以控制存储增长；配置自动修剪计划

### 修复（Repair）

* **RepairService** — 灾难恢复用底层修复：导入/导出 ACS 快照、清除合约等

<Warning>
  修复操作若使用不当可能导致数据不一致。仅在运维文档或 Digital Asset 支持指导下使用。
</Warning>

## Canton Console 访问

Canton Console 提供更易用的 Admin API 操作界面。常用命令见 [Essential Commands](/zh/docs/canton/global-synchronizer-canton-console-essential-commands)。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// 示例：通过 Canton Console 列出已连接 synchronizer
participant.synchronizers.list_connected

// 示例：上传 DAR
participant.participant1.dars.upload("dars/CantonExamples.dar")

// 示例：检查节点健康
participant.health.status
```

## 下一步

* [API Reference](/zh/docs/canton/api-reference) — 所有生成 API 文档中心，含 Ledger API
* [Canton Console](/zh/docs/canton/global-synchronizer-canton-console-console-overview) — 交互式控制台

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
