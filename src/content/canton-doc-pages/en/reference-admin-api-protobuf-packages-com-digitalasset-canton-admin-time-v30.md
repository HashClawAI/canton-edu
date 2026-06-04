---
title: "com.digitalasset.canton.admin.time.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-time-v30"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-time-v30.md"
source_title: "com.digitalasset.canton.admin.time.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.admin.time.v30

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# com.digitalasset.canton.admin.time.v30

> Package-level overview for com.digitalasset.canton.admin.time.v30.

<p class="x2mdx-ref-back"><a href="../index">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.admin.time.v30</h1>

  <p class="x2mdx-ref-summary">0 services, 0 endpoints, 2 messages</p>

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
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Endpoints</dt>
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Messages</dt>
      <dd>2</dd>
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
      <h3>community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/time/v30/time\_tracker\_config.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Current source file in the latest published descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>2</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/time/v30/time_tracker_config.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/time/v30/time\_tracker\_config.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## Type Inventory

These are the package-level message and enum shapes in the publish-version snapshot.

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-synchronizertimetrackerconfig">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.time.v30.SynchronizerTimeTrackerConfig</h3>

    <p class="x2mdx-ref-schema-summary">4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">observation\_latency</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">patience\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_observation\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">time\_proof\_request</code>
        <span class="x2mdx-ref-type-badge">TimeProofRequestConfig</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-timeproofrequestconfig">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.time.v30.TimeProofRequestConfig</h3>

    <p class="x2mdx-ref-schema-summary">3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">initial\_retry\_delay</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_retry\_delay</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_sequencing\_delay</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
