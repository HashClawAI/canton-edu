---
title: "Details and history"
slug: "reference-json-api-asyncapi-reference-operations-v2-state-active-contracts-details"
locale: "en"
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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Details and history

> Returns a stream of the snapshot of the active contracts and incomplete (un)assignments at a ledger offset. Once the stream of GetActiveContractsResponses completes, the client SHOULD begin streaming updates from the update service, starting at the GetActiveContractsRequest.active_at_offset specified in this request. Clients SHOULD NOT assume that the set of active contracts they receive reflects the state at the ledger end.

<p class="x2mdx-ref-back"><a href="../details">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">AsyncAPI Channel</p>

  <h1 class="x2mdx-ref-title">/v2/state/active-contracts</h1>

  <p class="x2mdx-ref-summary">Returns a stream of the snapshot of the active contracts and incomplete (un)assignments at a ledger offset. Once the stream of GetActiveContractsResponses completes, the client...</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Channel</dt>
      <dd>/v2/state/active-contracts</dd>
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

Returns a stream of the snapshot of the active contracts and incomplete (un)assignments at a ledger offset.
Once the stream of GetActiveContractsResponses completes,
the client SHOULD begin streaming updates from the update service,
starting at the GetActiveContractsRequest.active\_at\_offset specified in this request.
Clients SHOULD NOT assume that the set of active contracts they receive reflects the state at the ledger end.

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./publish">
    <div class="x2mdx-ref-card-head">
      <h3>publish /v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Publish GetActiveContractsRequest messages from the client to /v2/state/active-contracts.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>sendV2StateActive-contracts</dd>
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

  <a class="x2mdx-ref-card" href="./subscribe">
    <div class="x2mdx-ref-card-head">
      <h3>subscribe /v2/state/active-contracts</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Receive Either\_JsCantonError\_JsGetActiveContractsResponse messages from /v2/state/active-contracts on the subscription stream.</p>

    <div class="x2mdx-ref-badges">
      <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

      <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
    </div>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>onV2StateActive-contracts</dd>
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
