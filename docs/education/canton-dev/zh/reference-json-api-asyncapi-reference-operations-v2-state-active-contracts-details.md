---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-v2-state-active-contracts-details"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-state-active-contracts/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-state-active-contracts
---

# Details and history

> 返回活动合约的快照流以及分类帐偏移处的不完整（未）分配。一旦 GetActiveContractsResponses 流完成，客户端应该开始从更新服务流式传输更新，从该请求中指定的 GetActiveContractsRequest.active_at_offset 开始。客户不应该假设他们收到的一组活跃合约反映了账本端的状态。

<p class="x2mdx-ref-back"><a href="../details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">AsyncAPI 通道</p>

  <h1 class="x2mdx-ref-title">/v2/state/active-contracts</h1>

  <p class="x2mdx-ref-summary">返回活动合约的快照流以及分类帐偏移处的不完整（未）分配。一旦 GetActiveContractsResponses 流完成，客户端...</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>频道</dt>
      <dd>/v2/state/active-contracts</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>操作</dt>
      <dd>发布、订阅</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>介绍</dt>
      <dd>3.4</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>已删除</dt>
      <dd>-</dd>
    </div>
  </dl>
</div>

## 行动

返回活动合约的快照流以及分类帐偏移处的不完整（未）分配。
一旦 GetActiveContractsResponses 流完成，
客户端应该开始从更新服务流式传输更新，
从此请求中指定的 GetActiveContractsRequest.active\_at\_offset 开始。
客户不应该假设他们收到的一组活跃合约反映了账本端的状态。

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./publish">
    <div class="x2mdx-ref-card-head">
      <h3>发布/v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">将来自客户端的 GetActiveContractsRequest 消息发布到 /v2/state/active-contracts。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>sendV2StateActive-contracts</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>方法</dt>
        <dd>-</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>有效负载</dt>
        <dd>对象</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="./subscribe">
    <div class="x2mdx-ref-card-head">
      <h3>订阅 /v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">从订阅流上的 /v2/state/active-contracts 接收 \_JsCantonError\_JsGetActiveContractsResponse 消息。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>onV2StateActive-contracts</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>方法</dt>
        <dd>-</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>有效负载</dt>
        <dd>其中一个</dd>
      </div>
    </dl>
  </a>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
