---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-v2-updates-flats-details"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-updates-flats/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-updates-flats
---

# Details and history

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Details and history

> Get flat transactions update stream. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.

<p class="x2mdx-ref-back"><a href="/docs/canton/reference-json-api-asyncapi-reference-operations-details">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">AsyncAPI Channel</p>

  <h1 class="x2mdx-ref-title">/v2/updates/flats</h1>

  <p class="x2mdx-ref-summary">Get flat transactions update stream. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Channel</dt>
      <dd>/v2/updates/flats</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Actions</dt>
      <dd>publish, subscribe</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Introduced</dt>
      <dd>3.4</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Removed</dt>
      <dd>-</dd>
    </div>
  </dl>
</div>

## Actions

Get flat transactions update stream. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-flats-publish">
    <div class="x2mdx-ref-card-head">
      <h3>publish /v2/updates/flats</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Publish GetUpdatesRequest messages from the client to /v2/updates/flats.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>sendV2UpdatesFlats</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Method</dt>
        <dd>-</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Payload</dt>
        <dd>object</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-flats-subscribe">
    <div class="x2mdx-ref-card-head">
      <h3>subscribe /v2/updates/flats</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Receive Either\_JsCantonError\_JsGetUpdatesResponse messages from /v2/updates/flats on the subscription stream.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>onV2UpdatesFlats</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Method</dt>
        <dd>-</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Payload</dt>
        <dd>oneOf</dd>
      </div>
    </dl>
  </a>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
