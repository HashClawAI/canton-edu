---
title: "com.digitalasset.canton.time.admin.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-time-admin-v30"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-time-admin-v30.md"
source_title: "com.digitalasset.canton.time.admin.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.time.admin.v30

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# com.digitalasset.canton.time.admin.v30

> Package-level overview for com.digitalasset.canton.time.admin.v30.

<p class="x2mdx-ref-back"><a href="../index">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.time.admin.v30</h1>

  <p class="x2mdx-ref-summary">1 services, 2 endpoints, 4 messages</p>

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
      <dd>4</dd>
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
      <h3>community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronizer\_time\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Current source file in the latest published descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>4</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronizer_time_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronizer\_time\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## SynchronizerTimeService

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>Source file</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronizer_time_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronizer\_time\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>Operations</dt>
    <dd>2</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-time-admin-v30/synchronizertimeservice/awaittime">
    <div class="x2mdx-ref-card-head">
      <h3>SynchronizerTimeService.AwaitTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc SynchronizerTimeService.AwaitTime(com.digitalasset.canton.time.admin.v30.AwaitTimeRequest) returns (com.digitalasset.canton.time.admin.v30.AwaitTimeResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.digitalasset.canton.time.admin.v30.AwaitTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.digitalasset.canton.time.admin.v30.AwaitTimeResponse</dd>
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

  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-time-admin-v30/synchronizertimeservice/fetchtime">
    <div class="x2mdx-ref-card-head">
      <h3>SynchronizerTimeService.FetchTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc SynchronizerTimeService.FetchTime(com.digitalasset.canton.time.admin.v30.FetchTimeRequest) returns (com.digitalasset.canton.time.admin.v30.FetchTimeResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.digitalasset.canton.time.admin.v30.FetchTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.digitalasset.canton.time.admin.v30.FetchTimeResponse</dd>
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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-awaittimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.AwaitTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer</code>
        <span class="x2mdx-ref-type-badge">Synchronizer</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">timestamp</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-synchronizer">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.topology.admin.v30.Synchronizer</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">physical\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-awaittimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.AwaitTimeResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-fetchtimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.FetchTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer</code>
        <span class="x2mdx-ref-type-badge">Synchronizer</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">freshness\_bound</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-fetchtimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.FetchTimeResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">timestamp</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
