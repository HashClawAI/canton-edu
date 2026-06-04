---
title: "v2.testing"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-testing.md"
source_title: "v2.testing"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-testing
---

# v2.testing

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# v2.testing

> Package-level overview for com.daml.ledger.api.v2.testing.

<p class="x2mdx-ref-back"><a href="/docs/canton/reference-grpc-ledger-api-reference-details">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">v2.testing</h1>

  <p class="x2mdx-ref-summary">1 services, 2 endpoints, 3 messages</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Files</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Services</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Endpoints</dt>
      <dd>2</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Messages</dt>
      <dd>3</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Enums</dt>
      <dd>0</dd>
    </div>
  </dl>
</div>

## Source Files

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>time\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Source file from the latest descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>3</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## TimeService

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>Source file</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>Operations</dt>
    <dd>2</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing-timeservice-gettime">
    <div class="x2mdx-ref-card-head">
      <h3>TimeService.GetTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc TimeService.GetTime(com.daml.ledger.api.v2.testing.GetTimeRequest) returns (com.daml.ledger.api.v2.testing.GetTimeResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.testing.GetTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.testing.GetTimeResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Client stream</dt>
        <dd>No</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Server stream</dt>
        <dd>No</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing-timeservice-settime">
    <div class="x2mdx-ref-card-head">
      <h3>TimeService.SetTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc TimeService.SetTime(com.daml.ledger.api.v2.testing.SetTimeRequest) returns (google.protobuf.Empty);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.testing.SetTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>google.protobuf.Empty</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Client stream</dt>
        <dd>No</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Server stream</dt>
        <dd>No</dd>
      </div>
    </dl>
  </a>
</div>

## Type Inventory

These are the package-level message and enum shapes in the publish-version snapshot.

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-gettimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>GetTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-gettimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>GetTimeResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">current\_time</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-settimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>SetTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">current\_time</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">new\_time</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
