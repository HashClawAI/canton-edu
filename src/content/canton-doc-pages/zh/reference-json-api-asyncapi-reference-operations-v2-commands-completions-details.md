---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-v2-commands-completions-details"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-commands-completions/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-commands-completions
---

# Details and history

> 订阅命令完成事件。

<p class="x2mdx-ref-back"><a href="../details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">AsyncAPI 通道</p>

  <h1 class="x2mdx-ref-title">/v2/commands/completions</h1>

  <p class="x2mdx-ref-summary">订阅命令完成事件。</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>频道</dt>
      <dd>/v2/commands/completions</dd>
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

订阅命令完成事件。

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./publish">
    <div class="x2mdx-ref-card-head">
      <h3>发布 /v2/commands/completions</h3>
    </div>

    <p class="x2mdx-ref-card-summary">将来自客户端的 CompletionStreamRequest 消息发布到 /v2/commands/completions。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>sendV2CommandsCompletions</dd>
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
      <h3>订阅/v2/commands/completions</h3>
    </div>

    <p class="x2mdx-ref-card-summary">从订阅流上的 /v2/commands/completions 接收 Either\_JsCantonError\_CompletionStreamResponse 消息。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>onV2CommandsCompletions</dd>
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
