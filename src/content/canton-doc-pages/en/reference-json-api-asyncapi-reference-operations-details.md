---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-details"
locale: "en"
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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Details and history

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">asyncapi reference</p>

      <h1 class="x2mdx-ref-title">JSON API AsyncAPI Reference</h1>
      <h2>Details and history</h2>
      <p>JSON Ledger API WebSocket AsyncAPI reference and version history. Operation-first WebSocket reference pages built from AsyncAPI channel snapshots and lifecycle deltas.</p>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">AsyncAPI</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--neutral">v3.5</span>
      </div>
    </div>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Publish version</dt>
      <dd>3.5</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>AsyncAPI version</dt>
      <dd>2.6.0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Source</dt>
      <dd>Canton release bundle JSON Ledger API AsyncAPI fixtures</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Version filter</dt>
      <dd>configured docs major versions from Canton release bundles</dd>
    </div>
  </dl>
</div>

## Channels

Use the channel page to choose a specific `publish` or `subscribe` action. Action pages are the primary reference surface.

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-commands-completions-details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/completions</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Subscribe to command completion events.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Actions</dt>
        <dd>publish, subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-state-active-contracts-details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Returns a stream of the snapshot of the active contracts and incomplete (un)assignments at a ledger offset. Once the stream of GetActiveContractsResponses completes, the client...</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Actions</dt>
        <dd>publish, subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Read the ledger's filtered update stream for the specified contents and filters. It returns the event types in accordance with the stream contents selected. Also the selection c...</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Actions</dt>
        <dd>publish, subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-flats-details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/flats</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Get flat transactions update stream. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Actions</dt>
        <dd>publish, subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-trees-details">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/trees</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Get update transactions tree stream. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Actions</dt>
        <dd>publish, subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </a>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
