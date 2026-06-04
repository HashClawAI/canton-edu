---
title: "分配与查询 Daml Party"
slug: "appdev-deep-dives-manage-daml-parties"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/manage-daml-parties.md"
source_title: "How to allocate and query Daml parties"
tags:
  - appdev
  - deep-dives
  - manage-daml-parties
---

# 分配与查询 Daml Party

> 在 participant 上分配新 Party 并查询 Party 元数据。

Canton Participant Node 提供 Party 管理服务，用于创建与发现 Daml Party。本指南说明如何通过 OpenAPI 描述的 JSON Ledger API 以编程方式操作 Party。

要了解 Daml Party 与用户，请参阅关键概念中的 Daml parties and users。

运维指南中的 Party 管理章节介绍如何通过 Canton 控制台创建 Party。

## 启动 Canton Participant Node

确保 Canton Participant Node 在启动时开放 JSON Ledger API HTTP 端口，在启动参数中添加：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
-C canton.participants.participant1.http-ledger-api.port=7575
```

或在 Canton 配置文件中启用 JSON Ledger API。社区版示例见 `examples/09-json-api`。

启动 Participant Node 并连接 Synchronizer。若不熟悉流程，请参阅入门教程中的连接节点步骤。

## 如何查询已有 Party

列出 participant 已知的全部 Party，向 `v2/parties` 端点发送 GET：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost:7575/v2/parties
```

响应包含所有已知 Party，例如：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "partyDetails": [
    {
      "party": "Alice::122091f5d8d174bc0d624616d4f366904f8d4c56d56e33508878db3156c3dd9b8ae9",
      "isLocal": true,
      "localMetadata": {
        "resourceVersion": "0",
        "annotations": {}
      },
      "identityProviderId": ""
    }
  ],
  "nextPageToken": ""
}
```

`isLocal` 为 `true` 表示该 participant 托管该 Party，且 Party 与发起请求的用户属于同一身份提供方。

## 如何创建新的本地 Party

向 `v2/parties` 发送 POST 创建 Party：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -d '{"partyIdHint":"Alice"}' http://localhost:7575/v2/parties
```

返回的 Party Id 由 `partyIdHint` 与托管该 Party 的实体命名空间指纹组成，通常为 Canton Participant Node 的指纹。

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "partyDetails": {
    "party": "Alice::122091f5d8d174bc0d624616d4f366904f8d4c56d56e33508878db3156c3dd9b8ae9",
    "isLocal": true,
    "localMetadata": {
      "resourceVersion": "0",
      "annotations": {}
    },
    "identityProviderId": ""
  }
}
```

若请求中省略 `partyIdHint`，Participant Node 会随机选择 hint 字符串。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
