---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-details"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - details
---

# Details and history

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">asyncapi 参考</p>

      <h1 class="x2mdx-ref-title">JSON API AsyncAPI 参考</h1>
      <h2>详细信息和历史记录</h2>
      <p>JSON Ledger API WebSocket AsyncAPI 参考和版本历史记录。根据 AsyncAPI 通道快照和生命周期增量构建的操作优先 WebSocket 参考页面。</p>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">AsyncAPI</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--neutral">v3.5</span>
      </div>
    </div>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>发布版本</dt>
      <dd>3.5</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>AsyncAPI版本</dt>
      <dd>2.6.0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>来源</dt>
      <dd>Canton 发布捆绑包 JSON Ledger API AsyncAPI 固定装置</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>版本过滤器</dt>
      <dd>配置来自 Canton 发行包的文档主要版本</dd>
    </div>
  </dl>
</div>

## 频道

使用频道页面选择特定的 `publish` 或 `subscribe` 操作。操作页面是主要参考表面。

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./v2-commands-completions/details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/命令/完成</h3>
    </div>

    <p class="x2mdx-ref-card-summary">订阅命令完成事件。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作</dt>
        <dd>发布、订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>最后一次见到</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="./v2-state-active-contracts/details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">返回活动合约的快照流以及分类帐偏移处的不完整（未）分配。一旦 GetActiveContractsResponses 流完成，客户端...</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span><span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作</dt>
        <dd>发布、订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>最后一次见到</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="./v2-updates/details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/更新</h3>
    </div>

    <p class="x2mdx-ref-card-summary">读取分类帐的过滤更新流以获取指定的内容和过滤器。它根据所选的流内容返回事件类型。还有选择c...</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作</dt>
        <dd>发布、订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>最后一次见到</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="./v2-updates-flats/details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/更新/公寓</h3>
    </div>

    <p class="x2mdx-ref-card-summary">获取固定交易更新流。为向后兼容而提供，它将在 Canton 3.5.0 版本中删除，改用 v2/updates。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作</dt>
        <dd>发布、订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>最后一次见到</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="./v2-updates-trees/details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/更新/树</h3>
    </div>

    <p class="x2mdx-ref-card-summary">获取更新交易树流。为向后兼容而提供，它将在 Canton 3.5.0 版本中删除，改用 v2/updates。</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span><span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>操作</dt>
        <dd>发布、订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>最后一次见到</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
