---
title: "SignTransactions"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-topology-admin-v30-topologymanagerwriteservice-signtransactions"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-topology-admin-v30/topologymanagerwriteservice/signtransactions.md"
source_title: "SignTransactions"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# SignTransactions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SignTransactions

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Shared Administration</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-packages-com-digitalasset-canton-topology-admin-v30">com.digitalasset.canton.topology.admin.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>SignTransactions</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.topology.admin.v30</p>

      <h1 class="x2mdx-ref-title">SignTransactions</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/SignTransactions</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>TopologyManagerWriteService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>SignTransactions</dd>
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
        <h3>SignTransactionsRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.SignTransactionsRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">transactions</code>
            <span class="x2mdx-ref-type-badge">repeated SignedTopologyTransaction</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">signed\_by</code>
            <span class="x2mdx-ref-type-badge">repeated string</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">store</code>
            <span class="x2mdx-ref-type-badge">StoreId</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">force\_flags</code>
            <span class="x2mdx-ref-type-badge">repeated ForceFlag</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>SignTransactionsResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.SignTransactionsResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">transactions</code>
            <span class="x2mdx-ref-type-badge">repeated SignedTopologyTransaction</span>
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
      <Accordion title="com.digitalasset.canton.topology.admin.v30.SignTransactionsRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-signtransactionsrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">transactions</code>
                <span class="x2mdx-ref-type-badge">repeated SignedTopologyTransaction</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">signed\_by</code>
                <span class="x2mdx-ref-type-badge">repeated string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">store</code>
                <span class="x2mdx-ref-type-badge">StoreId</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">force\_flags</code>
                <span class="x2mdx-ref-type-badge">repeated ForceFlag</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.StoreId">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">authorized</code>
                <span class="x2mdx-ref-type-badge">Authorized</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">synchronizer</code>
                <span class="x2mdx-ref-type-badge">Synchronizer</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">temporary</code>
                <span class="x2mdx-ref-type-badge">Temporary</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.StoreId.Authorized">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid-authorized" />
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.StoreId.Temporary">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid-temporary">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">name</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.Synchronizer">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-synchronizer">
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
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.ForceFlag">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-forceflag">
          <ul class="x2mdx-ref-enum-list">
            <li><code>FORCE\_FLAG\_UNSPECIFIED</code></li>

            <li><code>FORCE\_FLAG\_ALIEN\_MEMBER</code></li>

            <li><code>FORCE\_FLAG\_LEDGER\_TIME\_RECORD\_TIME\_TOLERANCE\_INCREASE</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_UNKNOWN\_PACKAGE</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_UNVETTED\_DEPENDENCIES</code></li>

            <li><code>FORCE\_FLAG\_DISABLE\_PARTY\_WITH\_ACTIVE\_CONTRACTS</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_UNVALIDATED\_SIGNING\_KEYS</code></li>

            <li><code>FORCE\_FLAG\_PREPARATION\_TIME\_RECORD\_TIME\_TOLERANCE\_INCREASE</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_INSUFFICIENT\_PARTICIPANT\_PERMISSION\_FOR\_SIGNATORY\_PARTY</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_INSUFFICIENT\_SIGNATORY\_ASSIGNING\_PARTICIPANTS\_FOR\_PARTY</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_VET\_INCOMPATIBLE\_UPGRADES</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_OUT\_OF\_BOUNDS\_VALUE</code></li>

            <li><code>FORCE\_FLAG\_ALLOW\_CONFIRMING\_THRESHOLD\_CANNOT\_BE\_MET</code></li>
          </ul>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.SignTransactionsResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-signtransactionsresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">transactions</code>
                <span class="x2mdx-ref-type-badge">repeated SignedTopologyTransaction</span>
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
          com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/SignTransactions <<'EOF'
        {
          "transactions": [
            "string"
          ],
          "signedBy": [
            "string"
          ],
          "store": {
            "authorized": {}
          },
          "forceFlags": [
            "FORCE_FLAG_UNSPECIFIED"
          ]
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
          "transactions": [
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
