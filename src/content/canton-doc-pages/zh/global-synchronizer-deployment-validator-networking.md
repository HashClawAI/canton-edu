---
title: "验证者入站与出站要求"
slug: "global-synchronizer-deployment-validator-networking"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-networking.md"
source_title: "Validator Ingress and Egress Requirements"
tags:
  - global-synchronizer
  - deployment
  - validator-networking
---

# 验证者入站与出站要求

> 验证者节点的网络入站与出站要求。

## Ingress

验证者没有外部入站要求，也不需要将任何其他 SV 或验证者列入白名单。

## Egress

验证者必须能够连接到所有 SV，因此需要将所有 SV 的 IP 的端口 443 上的出口列入白名单（有关网络概述，请参阅网络图）。请注意，默认情况下通常允许出口，因此在许多情况下不需要执行任何操作。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
