---
title: "验证者网络重置"
slug: "global-synchronizer-deployment-validator-network-resets"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-network-resets.md"
source_title: "Validator Network Resets"
tags:
  - global-synchronizer
  - deployment
  - validator-network-resets
---

# 验证者网络重置

> DevNet 与 TestNet 重置时验证者节点的处理方式。

> 处理验证者节点上的 DevNet 和 TestNet 重置

DevNet 和 TestNet 大约每 3 个月重置一次，并且重置是分散的，这样它们就不会在 DevNet 和 TestNet 上同时发生。具体时间在[全局同步器基金会](https://sync.global/)运行的`#validator-operations`频道中公布。

重置需要完全重新部署节点，并会丢失节点上的所有数据。在完成重置之前，您的节点将无法运行。

要完成重置，请执行以下步骤：

1. 卸载所有 Helm Chart。
2. 删除所有 PVC、docker 卷和数据库（包括 Amazon AWS、GCP CloudSQL 或类似数据库）。
3. 获取新的入驻密钥（在 DevNet 上，您可以通过调用相应的端点自行完成，在 TestNet 上，请联系您的 SV 赞助商）。
4. 使用迁移 ID 0 重新部署节点。请注意，这需要更改验证者 Helm 图表值中的迁移 ID 以及参与者 Helm 图表值。
5. 当节点身份在重置过程中发生更改时，对其进行备份。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
