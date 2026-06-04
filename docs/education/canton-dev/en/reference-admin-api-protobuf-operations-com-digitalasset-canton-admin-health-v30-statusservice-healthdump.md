---
title: "HealthDump"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-health-v30-statusservice-healthdump"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-health-v30/statusservice/healthdump.md"
source_title: "HealthDump"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# HealthDump

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# HealthDump

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Shared Administration</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-health-v30">com.digitalasset.canton.admin.health.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>HealthDump</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.health.v30</p>

      <h1 class="x2mdx-ref-title">HealthDump</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.health.v30.StatusService/HealthDump</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>StatusService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>HealthDump</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Client stream</dt>
        <dd>No</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Server stream</dt>
        <dd>Yes</dd>
      </div>
    </dl>

    ## Inputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>HealthDumpRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.health.v30.HealthDumpRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">chunk\_size</code>
            <span class="x2mdx-ref-type-badge">uint32</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>HealthDumpResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.health.v30.HealthDumpResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>Yes</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">chunk</code>
            <span class="x2mdx-ref-type-badge">bytes</span>
          </div>
        </div>
      </div>
    </div>

    ## Lifecycle Changes

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.4.0</span>
        <span class="x2mdx-ref-change-detail">introduced</span>
      </div>
    </div>

    ## Related Schemas

    <AccordionGroup>
      <Accordion title="com.digitalasset.canton.admin.health.v30.HealthDumpRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-healthdumprequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">chunk\_size</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.health.v30.HealthDumpResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-healthdumpresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">chunk</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>
    </AccordionGroup>
  </div>

  <div className="x2mdx-ref-right-rail" role="complementary" aria-label="Examples and responses">
    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">grpcurl</span>
        </div>

        ```bash grpcurl theme={"theme":{"light":"github-light","dark":"github-dark"}}
        # Add -plaintext if the server is not using TLS.
        # This RPC uses streaming semantics. Send additional JSON messages on stdin as needed.
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.digitalasset.canton.admin.health.v30.StatusService/HealthDump <<'EOF'
        {
          "chunkSize": 0
        }
        EOF
        ```
      </div>
    </div>

    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code x2mdx-ref-rail-code--response">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">OK</span>

          <span className="x2mdx-ref-response-label">application/json</span>
        </div>

        ```json OK theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {
          "chunk": "BASE64_ENCODED_BYTES"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
