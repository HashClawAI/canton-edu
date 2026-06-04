---
title: "UploadDar"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-packageservice-uploaddar"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/packageservice/uploaddar.md"
source_title: "UploadDar"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# UploadDar

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# UploadDar

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Participant Administration</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../packages/com-digitalasset-canton-admin-participant-v30">com.digitalasset.canton.admin.participant.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>UploadDar</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.participant.v30</p>

      <h1 class="x2mdx-ref-title">UploadDar</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.participant.v30.PackageService/UploadDar</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>PackageService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>UploadDar</dd>
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
        <h3>UploadDarRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.UploadDarRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">dars</code>
            <span class="x2mdx-ref-type-badge">repeated UploadDarData</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">vet\_all\_packages</code>
            <span class="x2mdx-ref-type-badge">bool</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">synchronize\_vetting</code>
            <span class="x2mdx-ref-type-badge">bool</span>
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
        <h3>UploadDarResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.UploadDarResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">dar\_ids</code>
            <span class="x2mdx-ref-type-badge">repeated string</span>
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
      <Accordion title="com.digitalasset.canton.admin.participant.v30.UploadDarRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-uploaddarrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">dars</code>
                <span class="x2mdx-ref-type-badge">repeated UploadDarData</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">vet\_all\_packages</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">synchronize\_vetting</code>
                <span class="x2mdx-ref-type-badge">bool</span>
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

      <Accordion title="com.digitalasset.canton.admin.participant.v30.UploadDarRequest.UploadDarData">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-uploaddarrequest-uploaddardata">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">bytes</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">description</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">expected\_main\_package\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.UploadDarResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-uploaddarresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">dar\_ids</code>
                <span class="x2mdx-ref-type-badge">repeated string</span>
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
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.digitalasset.canton.admin.participant.v30.PackageService/UploadDar <<'EOF'
        {
          "dars": [
            {
              "bytes": "BASE64_ENCODED_BYTES",
              "description": "string",
              "expectedMainPackageId": "string"
            }
          ],
          "vetAllPackages": true,
          "synchronizeVetting": true,
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
        {
          "darIds": [
            "string"
          ]
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
