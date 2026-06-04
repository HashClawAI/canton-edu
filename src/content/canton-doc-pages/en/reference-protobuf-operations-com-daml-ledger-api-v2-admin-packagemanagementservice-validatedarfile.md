---
title: "ValidateDarFile"
slug: "reference-protobuf-operations-com-daml-ledger-api-v2-admin-packagemanagementservice-validatedarfile"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/protobuf/operations/com-daml-ledger-api-v2-admin/packagemanagementservice/validatedarfile.md"
source_title: "ValidateDarFile"
tags:
  - reference
  - protobuf
  - operations
  - com-daml-ledger-api-v2-admin
---

# ValidateDarFile

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# ValidateDarFile

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Ledger API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../packages/com-daml-ledger-api-v2-admin">com.daml.ledger.api.v2.admin</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>ValidateDarFile</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.admin</p>

      <h1 class="x2mdx-ref-title">ValidateDarFile</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.admin.PackageManagementService/ValidateDarFile</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>PackageManagementService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>ValidateDarFile</dd>
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

    ## Inputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>ValidateDarFileRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.ValidateDarFileRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">dar\_file</code>
            <span class="x2mdx-ref-type-badge">bytes</span>
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
            <code class="x2mdx-ref-field-name">synchronizer\_id</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>ValidateDarFileResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.ValidateDarFileResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>
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
      <Accordion title="com.daml.ledger.api.v2.admin.ValidateDarFileRequest">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-validatedarfilerequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">dar\_file</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
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
                <code class="x2mdx-ref-field-name">synchronizer\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.ValidateDarFileResponse">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-validatedarfileresponse" />
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
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.daml.ledger.api.v2.admin.PackageManagementService/ValidateDarFile <<'EOF'
        {
          "darFile": "BASE64_ENCODED_BYTES",
          "submissionId": "string",
          "synchronizerId": "string"
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
        {}
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
