---
title: "API 参考"
slug: "api-reference"
locale: "zh"
category: "api-reference"
source_url: "https://docs.canton.network/api-reference.md"
source_title: "API Reference"
tags:
  - api-reference
---

# API 参考

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步探索之前，使用此文件发现所有可用页面。

# API 参考

API 参考涵盖 Canton 的每一个程序化接口——查阅端点、请求/响应模式、服务、消息与客户端库类型，并附生命周期注解。

<Columns cols={2}>
  <Card title="Ledger API" icon="bookmark" href="/appdev/reference/pqs-sql-reference">
    Canton Ledger API 生成参考，涵盖 5 个 gRPC 包——查阅服务、请求/响应模式，以及命令、更新等功能的版本历史。
  </Card>

  <Card title="TypeScript" icon="bookmark" href="/reference/typescript">
    Daml TypeScript 类型以及 Wallet SDK 与 dApp SDK 客户端库的生成参考。
  </Card>
</Columns>

<Columns cols={2}>
  <Card title="Daml 标准库" icon="bookmark" href="appdev/reference/daml-standard-library/da-action">
    Daml 标准库模块生成参考——涵盖核心模块等。
  </Card>

  <Card title="dApp API" icon="bookmark" href="reference/wallet-gateway-json-rpc/specs/dapp-api">
    dApp 与 Wallet Provider 交互的 OpenRPC 规范。
  </Card>
</Columns>

<Columns cols={2}>
  <Card title="Wallet Gateway" icon="bookmark" href="/reference/wallet-gateway-json-rpc/specs/user-api">
    版本化 OpenRPC 参考——用于将钱包与 dApp 集成到 Splice Wallet Gateway。
  </Card>

  <Card title="Splice API" icon="bookmark" href="/reference/splice-scan-api/common/readyz">
    使用 Canton Network 的 OpenAPI 端点进行开发：Canton Coin 数据、名称服务、代币标准等。
  </Card>
</Columns>

<Columns cols={2}>
  <Card title="Admin API" icon="bookmark" href="/reference/admin-api/protobuf/index">
    Canton Admin API 服务、消息与生命周期历史的 gRPC 包生成参考。
  </Card>
</Columns>

---

> 由 CC Privacy Club 镜像自 Canton Network 官方文档（CC-BY-4.0），仅供学习用途。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
