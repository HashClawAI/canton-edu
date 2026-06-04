---
title: "超级验证者升级"
slug: "global-synchronizer-production-operations-sv-upgrades"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/sv-upgrades.md"
source_title: "SV Upgrades"
tags:
  - global-synchronizer
  - production-operations
  - sv-upgrades
---

# 超级验证者升级

> 超级验证者节点的小版本升级流程。

> 超级验证者节点的小升级程序

有两种类型的升级：

版本升级（相当于从`0.A.X`升级到`0.B.Y`）和协议升级（实际版本可以保持不变，只是协议升级）。

版本升级可以由每个节点独立完成，只需要一个`helm upgrade`。请务必阅读 `release_notes` 了解升级过程中可能需要进行的更改。

协议升级是通过逻辑同步器升级来执行的，这允许在非常有限的网络停机时间内升级协议版本。

<Card title="逻辑同步器升级" icon="shuffle" href="/zh/docs/canton/global-synchronizer-production-operations-logical-synchronizer-upgrade">
  查看安排和执行逻辑同步器升级的操作流程。
</Card>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
