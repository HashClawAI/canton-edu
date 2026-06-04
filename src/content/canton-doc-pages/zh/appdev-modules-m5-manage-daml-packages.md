---
title: "如何上传与查询 Daml 包"
slug: "appdev-modules-m5-manage-daml-packages"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-manage-daml-packages.md"
source_title: "How to upload and query Daml packages"
tags:
  - appdev
  - modules
  - m5-manage-daml-packages
---

# 如何上传与查询 Daml 包

> 向 participant 上传 DAR 并在运行时查询可用 Daml 包。

Canton Participant Node 暴露包管理服务，支持上传与发现 Daml 包。本指南说明如何用 JSON Ledger API（OpenAPI 描述）以编程方式操作包。

要了解 Daml 包概念，请参阅关键概念中的 DAR 文件与 Daml 包（官方文档）。

运维指南中的包管理章节介绍如何用 Canton console 上传并检查包。

## 前置条件

确保 Canton Participant Node 开放 JSON Ledger API HTTP 端口。参见教程：Get started with Canton and the JSON Ledger API。

确保可使用 Daml 工具（Assistant `daml`、Compiler `damlc`）。

安装 `curl` 或类似 HTTP 工具。

若需格式化、过滤 `curl` 的 JSON 响应，安装 `jq` 或类似工具。

任何账本交互前，先将模型构建为 `.dar` 文件。

## 如何上传 DAR 归档文件

假设你在开发名为 `MyModel` 的 Daml 模型，要基于此模型开始链上交互。第一步是上传其包，并确保在所有交互的 Participant Node 上完成 vetting。

JSON Ledger API 提供端点，可在上传过程中将包 vet 到 Participant Node。

多数交互基于 package ID，用 damlc 检查生成的 DAR 并提取主包 ID：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml damlc inspect-dar --json .daml/dist/mymodel-1.0.0.dar | jq '.main_package_id'
```

damlc 返回包 ID：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed"
```

上传包时对 `v2/packages` 发起 POST：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --data-binary @.daml/dist/mymodel-1.0.0.dar http://localhost:7575/v2/packages
```

可验证包已在账本上注册：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages/47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed/status
```

账本返回包状态：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageStatus": "PACKAGE_STATUS_REGISTERED"
}
```

## 如何查询已有包

列出 Participant Node 已知全部包，对 `v2/packages` 发起 GET：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages
```

Participant 返回包含全部已知包 ID 的消息：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageIds": [
    "9e70a8b3510d617f8a136213f33d6a903a10ca0eeec76bb06ba55d1ed9680f69",
    "47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed",
    "bfda48f9aa2c89c895cde538ec4b4946c7085959e031ad61bde616b9849155d7"
  ]
}
```

列表较长时，用 `jq` 过滤并确认期望的包 ID 是否存在：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages | jq '.packageIds | .[] | select(startswith("47"))'
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
