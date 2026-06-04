---
title: "前置条件"
slug: "global-synchronizer-deployment-prerequisites"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/prerequisites.md"
source_title: "Prerequisites"
tags:
  - global-synchronizer
  - deployment
  - prerequisites
---

# 前置条件

> 验证者部署系统要求与资源参考值。

> 在 Canton 网络上运行验证器的系统要求

本节描述运行验证器的硬件要求。请注意，这些是参考值。实际要求可能会根据验证器的使用情况而有所不同。我们建议监控生产验证器节点的所有组件的 CPU 和内存使用情况以及数据库的磁盘使用情况，并根据需要调整资源。

要求包括验证者和参与者容器。

基于 docker-compose 的部署和 k8s 部署之间的这些要求基本相同，但不包括 k8s 本身或入口的开销。

|用途 | CPU |内存|数据库CPU |数据库内存|数据库大小 |
| --------------------------------------------------------------------------- | ---- | ------ | -------- | --------- | -------- |
|在本地笔记本电脑或最小虚拟机上进行实验 | 1 | 6GB | 1 | 1GB | 1GB |
|生产验证器活动很少 | 2 | 8GB | 2 | 4GB | 10GB |
|适合中等活动的应用程序提供商的生产验证器 | 2 | 16GB | 2 | 4GB | 100GB |

## 数据库延迟

组件对数据库延迟相对敏感。如果您使用 GCP CloudSQL 等托管数据库产品，建议您将其分配在集群运行的同一区域和可用区中。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
