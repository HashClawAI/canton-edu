---
title: "v2.interactive"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive.md"
source_title: "v2.interactive"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive
---

# v2.interactive

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# v2.interactive

> Package-level overview for com.daml.ledger.api.v2.interactive.

<p class="x2mdx-ref-back"><a href="./details">Back to overview</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf Package</p>

  <h1 class="x2mdx-ref-title">v2.interactive</h1>

  <p class="x2mdx-ref-summary">1 services, 6 endpoints, 29 messages, 1 enums</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Files</dt>
      <dd>2</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Services</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Endpoints</dt>
      <dd>6</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Messages</dt>
      <dd>29</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Enums</dt>
      <dd>1</dd>
    </div>
  </dl>
</div>

## Source Files

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>interactive\_submission\_common\_data.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Source file from the latest descriptor snapshot.</p>

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
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_submission_common_data.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_common\_data.proto</a></dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>interactive\_submission\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">Source file from the latest descriptor snapshot.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Services</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Messages</dt>
        <dd>22</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Enums</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Source</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_submission_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## InteractiveSubmissionService

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>Source file</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_submission_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>Operations</dt>
    <dd>6</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmission">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmission</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmission(com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest) returns (com.daml.ledger.api.v2.interactive.ExecuteSubmissionResp...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmissionandwait">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmissionAndWait</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmissionAndWait(com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitRequest) returns (com.daml.ledger.api.v2.interactive.Execute...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmissionandwaitfortransaction">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmissionAndWaitForTransaction</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmissionAndWaitForTransaction(com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionRequest) returns (com.daml.ledge...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/getpreferredpackageversion">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.GetPreferredPackageVersion</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.GetPreferredPackageVersion(com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionRequest) returns (com.daml.ledger.api.v2.interactive.Get...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/getpreferredpackages">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.GetPreferredPackages</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.GetPreferredPackages(com.daml.ledger.api.v2.interactive.GetPreferredPackagesRequest) returns (com.daml.ledger.api.v2.interactive.GetPreferredPac...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackagesRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackagesResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/preparesubmission">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.PrepareSubmission</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.PrepareSubmission(com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest) returns (com.daml.ledger.api.v2.interactive.PrepareSubmissionResp...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Request</dt>
        <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Response</dt>
        <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionResponse</dd>
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimation">
  <div class="x2mdx-ref-schema-head">
    <h3>CostEstimation</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">estimation\_timestamp</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">confirmation\_request\_traffic\_cost\_estimation</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">confirmation\_response\_traffic\_cost\_estimation</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">total\_traffic\_cost\_estimation</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimationhints">
  <div class="x2mdx-ref-schema-head">
    <h3>CostEstimationHints</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">disabled</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">expected\_signatures</code>
        <span class="x2mdx-ref-type-badge">repeated SigningAlgorithmSpec</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingalgorithmspec">
  <div class="x2mdx-ref-schema-head">
    <h3>SigningAlgorithmSpec</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 values</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>SIGNING\_ALGORITHM\_SPEC\_UNSPECIFIED</code></li>

    <li><code>SIGNING\_ALGORITHM\_SPEC\_ED25519</code></li>

    <li><code>SIGNING\_ALGORITHM\_SPEC\_EC\_DSA\_SHA\_256</code></li>

    <li><code>SIGNING\_ALGORITHM\_SPEC\_EC\_DSA\_SHA\_384</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction">
  <div class="x2mdx-ref-schema-head">
    <h3>DamlTransaction</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">roots</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">nodes</code>
        <span class="x2mdx-ref-type-badge">repeated Node</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_seeds</code>
        <span class="x2mdx-ref-type-badge">repeated NodeSeed</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-nodeseed">
  <div class="x2mdx-ref-schema-head">
    <h3>DamlTransaction.NodeSeed</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">seed</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-node">
  <div class="x2mdx-ref-schema-head">
    <h3>DamlTransaction.Node</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">v1</code>
        <span class="x2mdx-ref-type-badge">Node</span>
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitfortransactionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionAndWaitForTransactionRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 9 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prepared\_transaction</code>
        <span class="x2mdx-ref-type-badge">PreparedTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">party\_signatures</code>
        <span class="x2mdx-ref-type-badge">PartySignatures</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">submission\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">user\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">HashingSchemeVersion</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">transaction\_format</code>
        <span class="x2mdx-ref-type-badge">TransactionFormat</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparedtransaction">
  <div class="x2mdx-ref-schema-head">
    <h3>PreparedTransaction</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">transaction</code>
        <span class="x2mdx-ref-type-badge">DamlTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">metadata</code>
        <span class="x2mdx-ref-type-badge">Metadata</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 10 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">submitter\_info</code>
        <span class="x2mdx-ref-type-badge">SubmitterInfo</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">mediator\_group</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">transaction\_uuid</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">preparation\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">input\_contracts</code>
        <span class="x2mdx-ref-type-badge">repeated InputContract</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_effective\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_ledger\_effective\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_record\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">global\_key\_mapping</code>
        <span class="x2mdx-ref-type-badge">repeated GlobalKeyMappingEntry</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-submitterinfo">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata.SubmitterInfo</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">act\_as</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">command\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-globalkeymappingentry">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata.GlobalKeyMappingEntry</h3>

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
        <code class="x2mdx-ref-field-name">value</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-inputcontract">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata.InputContract</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">v1</code>
        <span class="x2mdx-ref-type-badge">Create</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">created\_at</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">event\_blob</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-partysignatures">
  <div class="x2mdx-ref-schema-head">
    <h3>PartySignatures</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signatures</code>
        <span class="x2mdx-ref-type-badge">repeated SinglePartySignatures</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-singlepartysignatures">
  <div class="x2mdx-ref-schema-head">
    <h3>SinglePartySignatures</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">party</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signatures</code>
        <span class="x2mdx-ref-type-badge">repeated Signature</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signature">
  <div class="x2mdx-ref-schema-head">
    <h3>Signature</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">format</code>
        <span class="x2mdx-ref-type-badge">SignatureFormat</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signature</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signed\_by</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">signing\_algorithm\_spec</code>
        <span class="x2mdx-ref-type-badge">SigningAlgorithmSpec</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signatureformat">
  <div class="x2mdx-ref-schema-head">
    <h3>SignatureFormat</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 5 values</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>SIGNATURE\_FORMAT\_UNSPECIFIED</code></li>

    <li><code>SIGNATURE\_FORMAT\_RAW</code></li>

    <li><code>SIGNATURE\_FORMAT\_DER</code></li>

    <li><code>SIGNATURE\_FORMAT\_CONCAT</code></li>

    <li><code>SIGNATURE\_FORMAT\_SYMBOLIC</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-hashingschemeversion">
  <div class="x2mdx-ref-schema-head">
    <h3>HashingSchemeVersion</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 values</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>HASHING\_SCHEME\_VERSION\_UNSPECIFIED</code></li>

    <li><code>HASHING\_SCHEME\_VERSION\_V2</code></li>

    <li><code>HASHING\_SCHEME\_VERSION\_V3</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-minledgertime">
  <div class="x2mdx-ref-schema-head">
    <h3>MinLedgerTime</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time\_abs</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time\_rel</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionformat">
  <div class="x2mdx-ref-schema-head">
    <h3>TransactionFormat</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">event\_format</code>
        <span class="x2mdx-ref-type-badge">EventFormat</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">transaction\_shape</code>
        <span class="x2mdx-ref-type-badge">TransactionShape</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-eventformat">
  <div class="x2mdx-ref-schema-head">
    <h3>EventFormat</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">filters\_by\_party</code>
        <span class="x2mdx-ref-type-badge">repeated map</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">filters\_for\_any\_party</code>
        <span class="x2mdx-ref-type-badge">Filters</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">verbose</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-filters">
  <div class="x2mdx-ref-schema-head">
    <h3>Filters</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">cumulative</code>
        <span class="x2mdx-ref-type-badge">repeated CumulativeFilter</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-cumulativefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>CumulativeFilter</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">wildcard\_filter</code>
        <span class="x2mdx-ref-type-badge">WildcardFilter</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_filter</code>
        <span class="x2mdx-ref-type-badge">InterfaceFilter</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">template\_filter</code>
        <span class="x2mdx-ref-type-badge">TemplateFilter</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-wildcardfilter">
  <div class="x2mdx-ref-schema-head">
    <h3>WildcardFilter</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">include\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfacefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>InterfaceFilter</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">include\_interface\_view</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">include\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-templatefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>TemplateFilter</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
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
        <code class="x2mdx-ref-field-name">include\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionshape">
  <div class="x2mdx-ref-schema-head">
    <h3>TransactionShape</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 values</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>TRANSACTION\_SHAPE\_UNSPECIFIED</code></li>

    <li><code>TRANSACTION\_SHAPE\_ACS\_DELTA</code></li>

    <li><code>TRANSACTION\_SHAPE\_LEDGER\_EFFECTS</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitfortransactionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionAndWaitForTransactionResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">transaction</code>
        <span class="x2mdx-ref-type-badge">Transaction</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transaction">
  <div class="x2mdx-ref-schema-head">
    <h3>Transaction</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 11 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">update\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">command\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">workflow\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">effective\_at</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">events</code>
        <span class="x2mdx-ref-type-badge">repeated Event</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">trace\_context</code>
        <span class="x2mdx-ref-type-badge">TraceContext</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">record\_time</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">external\_transaction\_hash</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">paid\_traffic\_cost</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-event">
  <div class="x2mdx-ref-schema-head">
    <h3>Event</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">created</code>
        <span class="x2mdx-ref-type-badge">CreatedEvent</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">archived</code>
        <span class="x2mdx-ref-type-badge">ArchivedEvent</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exercised</code>
        <span class="x2mdx-ref-type-badge">ExercisedEvent</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createdevent">
  <div class="x2mdx-ref-schema-head">
    <h3>CreatedEvent</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 16 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_key</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">contract\_key\_hash</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">create\_arguments</code>
        <span class="x2mdx-ref-type-badge">Record</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_views</code>
        <span class="x2mdx-ref-type-badge">repeated InterfaceView</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">witness\_parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
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
        <code class="x2mdx-ref-field-name">observers</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">created\_at</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
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
        <code class="x2mdx-ref-field-name">acs\_delta</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">representative\_package\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfaceview">
  <div class="x2mdx-ref-schema-head">
    <h3>InterfaceView</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">interface\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">view\_status</code>
        <span class="x2mdx-ref-type-badge">Status</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">view\_value</code>
        <span class="x2mdx-ref-type-badge">Record</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">implementation\_package\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-archivedevent">
  <div class="x2mdx-ref-schema-head">
    <h3>ArchivedEvent</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 7 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">witness\_parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
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
        <code class="x2mdx-ref-field-name">implemented\_interfaces</code>
        <span class="x2mdx-ref-type-badge">repeated Identifier</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisedevent">
  <div class="x2mdx-ref-schema-head">
    <h3>ExercisedEvent</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 15 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">template\_id</code>
        <span class="x2mdx-ref-type-badge">Identifier</span>
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
        <code class="x2mdx-ref-field-name">choice</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_argument</code>
        <span class="x2mdx-ref-type-badge">Value</span>
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
        <code class="x2mdx-ref-field-name">consuming</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">witness\_parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">last\_descendant\_node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">implemented\_interfaces</code>
        <span class="x2mdx-ref-type-badge">repeated Identifier</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">acs\_delta</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-tracecontext">
  <div class="x2mdx-ref-schema-head">
    <h3>TraceContext</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">traceparent</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">tracestate</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionAndWaitRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 8 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prepared\_transaction</code>
        <span class="x2mdx-ref-type-badge">PreparedTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">party\_signatures</code>
        <span class="x2mdx-ref-type-badge">PartySignatures</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">submission\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">user\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">HashingSchemeVersion</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionAndWaitResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">update\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">completion\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 8 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prepared\_transaction</code>
        <span class="x2mdx-ref-type-badge">PreparedTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">party\_signatures</code>
        <span class="x2mdx-ref-type-badge">PartySignatures</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_duration</code>
        <span class="x2mdx-ref-type-badge">Duration</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">deduplication\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">submission\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">user\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">HashingSchemeVersion</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>ExecuteSubmissionResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 0 fields</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackageversionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>GetPreferredPackageVersionRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
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
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">vetting\_valid\_at</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackageversionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>GetPreferredPackageVersionResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_preference</code>
        <span class="x2mdx-ref-type-badge">PackagePreference</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-packagepreference">
  <div class="x2mdx-ref-schema-head">
    <h3>PackagePreference</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_reference</code>
        <span class="x2mdx-ref-type-badge">PackageReference</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-packagereference">
  <div class="x2mdx-ref-schema-head">
    <h3>PackageReference</h3>

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
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_version</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackagesrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>GetPreferredPackagesRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_vetting\_requirements</code>
        <span class="x2mdx-ref-type-badge">repeated PackageVettingRequirement</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">vetting\_valid\_at</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-packagevettingrequirement">
  <div class="x2mdx-ref-schema-head">
    <h3>PackageVettingRequirement</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">parties</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_name</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackagesresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>GetPreferredPackagesResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_references</code>
        <span class="x2mdx-ref-type-badge">repeated PackageReference</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>PrepareSubmissionRequest</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 15 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">user\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">command\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">commands</code>
        <span class="x2mdx-ref-type-badge">repeated Command</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_record\_time</code>
        <span class="x2mdx-ref-type-badge">Timestamp</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">act\_as</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">read\_as</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">disclosed\_contracts</code>
        <span class="x2mdx-ref-type-badge">repeated DisclosedContract</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_id\_selection\_preference</code>
        <span class="x2mdx-ref-type-badge">repeated string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">verbose\_hashing</code>
        <span class="x2mdx-ref-type-badge">bool</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prefetch\_contract\_keys</code>
        <span class="x2mdx-ref-type-badge">repeated PrefetchContractKey</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">estimate\_traffic\_cost</code>
        <span class="x2mdx-ref-type-badge">CostEstimationHints</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">HashingSchemeVersion</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">taps\_max\_passes</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-command">
  <div class="x2mdx-ref-schema-head">
    <h3>Command</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">create</code>
        <span class="x2mdx-ref-type-badge">CreateCommand</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exercise</code>
        <span class="x2mdx-ref-type-badge">ExerciseCommand</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">exercise\_by\_key</code>
        <span class="x2mdx-ref-type-badge">ExerciseByKeyCommand</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">create\_and\_exercise</code>
        <span class="x2mdx-ref-type-badge">CreateAndExerciseCommand</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createcommand">
  <div class="x2mdx-ref-schema-head">
    <h3>CreateCommand</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 fields</p>
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
        <code class="x2mdx-ref-field-name">create\_arguments</code>
        <span class="x2mdx-ref-type-badge">Record</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisecommand">
  <div class="x2mdx-ref-schema-head">
    <h3>ExerciseCommand</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
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
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_argument</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisebykeycommand">
  <div class="x2mdx-ref-schema-head">
    <h3>ExerciseByKeyCommand</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
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
        <code class="x2mdx-ref-field-name">contract\_key</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_argument</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createandexercisecommand">
  <div class="x2mdx-ref-schema-head">
    <h3>CreateAndExerciseCommand</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
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
        <code class="x2mdx-ref-field-name">create\_arguments</code>
        <span class="x2mdx-ref-type-badge">Record</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">choice\_argument</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-disclosedcontract">
  <div class="x2mdx-ref-schema-head">
    <h3>DisclosedContract</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 fields</p>
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
        <code class="x2mdx-ref-field-name">contract\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">synchronizer\_id</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-prefetchcontractkey">
  <div class="x2mdx-ref-schema-head">
    <h3>PrefetchContractKey</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 fields</p>
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
        <code class="x2mdx-ref-field-name">contract\_key</code>
        <span class="x2mdx-ref-type-badge">Value</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">limit</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>PrepareSubmissionResponse</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 5 fields</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prepared\_transaction</code>
        <span class="x2mdx-ref-type-badge">PreparedTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">prepared\_transaction\_hash</code>
        <span class="x2mdx-ref-type-badge">bytes</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">HashingSchemeVersion</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hashing\_details</code>
        <span class="x2mdx-ref-type-badge">string</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">cost\_estimation</code>
        <span class="x2mdx-ref-type-badge">CostEstimation</span>
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
