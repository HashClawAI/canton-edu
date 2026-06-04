---
title: "v2.interactive.transaction.v1"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive-transaction-v1"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive-transaction-v1.md"
source_title: "v2.interactive.transaction.v1"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive-transaction-v1
---

# v2.interactive.transaction.v1

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# v2.interactive.transaction.v1

> Package-level overview for com.daml.ledger.api.v2.interactive.transaction.v1.

<p class="x2mdx-ref-back"><a href="/docs/canton/reference-grpc-ledger-api-reference-details">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">v2.interactive.transaction.v1</h1>

  <p class="x2mdx-ref-summary">0 services, 0 endpoints, 6 messages</p>

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
      <dd>6</dd>
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
      <h3>interactive\_submission\_data.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Source file from the latest descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>6</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/transaction/v1/interactive_submission_data.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/transaction/v1/interactive\_submission\_data.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## Type Inventory

These are the package-level message and enum shapes in the publish-version snapshot.

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-create">
  <div class="x2mdx-ref-schema-head">
    <h3>Create</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 8 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">argument</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signatories</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">stakeholders</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-identifier">
  <div class="x2mdx-ref-schema-head">
    <h3>Identifier</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">module\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">entity\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-value">
  <div class="x2mdx-ref-schema-head">
    <h3>Value</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 16 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">unit</code>
        <span class="x2mdx-ref-type-badge">Empty</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">bool</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">int64</code>
        <span class="x2mdx-ref-type-badge">sint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">date</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">timestamp</code>
        <span class="x2mdx-ref-type-badge">sfixed64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">numeric</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">party</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">text</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">optional</code>
        <span class="x2mdx-ref-type-badge">Optional</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">list</code>
        <span class="x2mdx-ref-type-badge">List</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">text\_map</code>
        <span class="x2mdx-ref-type-badge">TextMap</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">gen\_map</code>
        <span class="x2mdx-ref-type-badge">GenMap</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">record</code>
        <span class="x2mdx-ref-type-badge">Record</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">variant</code>
        <span class="x2mdx-ref-type-badge">Variant</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">enum</code>
        <span class="x2mdx-ref-type-badge">Enum</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-optional">
  <div class="x2mdx-ref-schema-head">
    <h3>Optional</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-list">
  <div class="x2mdx-ref-schema-head">
    <h3>List</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">elements</code>
        <span class="x2mdx-ref-type-badge">repeated Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap">
  <div class="x2mdx-ref-schema-head">
    <h3>TextMap</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">entries</code>
        <span class="x2mdx-ref-type-badge">repeated Entry</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap-entry">
  <div class="x2mdx-ref-schema-head">
    <h3>TextMap.Entry</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap">
  <div class="x2mdx-ref-schema-head">
    <h3>GenMap</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">entries</code>
        <span class="x2mdx-ref-type-badge">repeated Entry</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap-entry">
  <div class="x2mdx-ref-schema-head">
    <h3>GenMap.Entry</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-record">
  <div class="x2mdx-ref-schema-head">
    <h3>Record</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">record\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">fields</code>
        <span class="x2mdx-ref-type-badge">repeated RecordField</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-recordfield">
  <div class="x2mdx-ref-schema-head">
    <h3>RecordField</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">label</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-variant">
  <div class="x2mdx-ref-schema-head">
    <h3>Variant</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">variant\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">constructor</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-enum">
  <div class="x2mdx-ref-schema-head">
    <h3>Enum</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">enum\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">constructor</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkeywithmaintainers">
  <div class="x2mdx-ref-schema-head">
    <h3>GlobalKeyWithMaintainers</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">GlobalKey</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">maintainers</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkey">
  <div class="x2mdx-ref-schema-head">
    <h3>GlobalKey</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hash</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-exercise">
  <div class="x2mdx-ref-schema-head">
    <h3>Exercise</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 16 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signatories</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">stakeholders</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">acting\_parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">chosen\_value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">consuming</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">children</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exercise\_result</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_observers</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">by\_key</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-fetch">
  <div class="x2mdx-ref-schema-head">
    <h3>Fetch</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 10 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signatories</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">stakeholders</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">acting\_parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">by\_key</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-node">
  <div class="x2mdx-ref-schema-head">
    <h3>Node</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 5 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">create</code>
        <span class="x2mdx-ref-type-badge">Create</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">fetch</code>
        <span class="x2mdx-ref-type-badge">Fetch</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exercise</code>
        <span class="x2mdx-ref-type-badge">Exercise</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">rollback</code>
        <span class="x2mdx-ref-type-badge">Rollback</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">query\_by\_key</code>
        <span class="x2mdx-ref-type-badge">QueryByKey</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-rollback">
  <div class="x2mdx-ref-schema-head">
    <h3>Rollback</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">children</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-querybykey">
  <div class="x2mdx-ref-schema-head">
    <h3>QueryByKey</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 6 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exhaustive</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">result</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
