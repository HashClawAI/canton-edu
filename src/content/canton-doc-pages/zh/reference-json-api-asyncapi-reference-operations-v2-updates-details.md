---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-v2-updates-details"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-updates/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-updates
---

# Details and history

> 读取分类帐的过滤更新流以获取指定的内容和过滤器。它根据所选的流内容返回事件类型。此外，各个事件的选择标准取决于所选的交易形式。
- ACS delta：请求方必须是事件的利益相关者才能将其包括在内。 - 账本效应：请求方必须是事件的见证人才能将其包括在内。

<p class="x2mdx-ref-back"><a href="/zh/docs/canton/reference-json-api-asyncapi-reference-operations-details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">AsyncAPI 通道</p>

  <h1 class="x2mdx-ref-title">/v2/updates</h1>

  <p class="x2mdx-ref-summary">读取分类帐的过滤更新流以获取指定的内容和过滤器。它根据所选的流内容返回事件类型。还有选择c...</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>频道</dt>
      <dd>/v2/更新</dd>
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

读取分类帐的过滤更新流以获取指定的内容和过滤器。
它根据所选的流内容返回事件类型。还有选择标准
个别事件取决于所选的交易形式。

* ACS delta：请求方必须是事件的利益相关者才能将其包括在内。
* 账本效应：请求方必须是事件的见证人才能将其包含在内。

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-publish">
    <div class="x2mdx-ref-card-head">
      <h3>发布/v2/更新</h3>
    </div>

    <p class="x2mdx-ref-card-summary">将 GetUpdatesRequest 消息从客户端发布到 /v2/updates。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>发送V2更新</dd>
      </div><div class="x2mdx-ref-meta-item">
        <dt>方法</dt>
        <dd>-</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>有效负载</dt>
        <dd>对象</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-subscribe">
    <div class="x2mdx-ref-card-head">
      <h3>订阅/v2/updates</h3>
    </div>

    <p class="x2mdx-ref-card-summary">从订阅流上的 /v2/updates 接收 \_JsCantonError\_JsGetUpdatesResponse 消息。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>onV2更新</dd>
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
