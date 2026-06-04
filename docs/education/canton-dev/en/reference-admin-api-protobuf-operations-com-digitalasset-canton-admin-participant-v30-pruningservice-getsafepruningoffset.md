---
title: "GetSafePruningOffset"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-pruningservice-getsafepruningoffset"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/pruningservice/getsafepruningoffset.md"
source_title: "GetSafePruningOffset"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# GetSafePruningOffset

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# GetSafePruningOffset

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

      <span>GetSafePruningOffset</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.participant.v30</p>

      <h1 class="x2mdx-ref-title">GetSafePruningOffset</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.participant.v30.PruningService/GetSafePruningOffset</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>PruningService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>GetSafePruningOffset</dd>
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
        <h3>GetSafePruningOffsetRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">before\_or\_at</code>
            <span class="x2mdx-ref-type-badge">Timestamp</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">ledger\_end</code>
            <span class="x2mdx-ref-type-badge">int64</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">counter\_participants\_commitments\_state</code>
            <span class="x2mdx-ref-type-badge">SafeToPruneCommitmentState</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>GetSafePruningOffsetResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">safe\_pruning\_offset</code>
            <span class="x2mdx-ref-type-badge">int64</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">no\_safe\_pruning\_offset</code>
            <span class="x2mdx-ref-type-badge">NoSafePruningOffset</span>
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
      <Accordion title="com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-getsafepruningoffsetrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">before\_or\_at</code>
                <span class="x2mdx-ref-type-badge">Timestamp</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">ledger\_end</code>
                <span class="x2mdx-ref-type-badge">int64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">counter\_participants\_commitments\_state</code>
                <span class="x2mdx-ref-type-badge">SafeToPruneCommitmentState</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.SafeToPruneCommitmentState">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-safetoprunecommitmentstate">
          <ul class="x2mdx-ref-enum-list">
            <li><code>SAFE\_TO\_PRUNE\_COMMITMENT\_STATE\_UNSPECIFIED</code></li>

            <li><code>SAFE\_TO\_PRUNE\_COMMITMENT\_STATE\_MATCH</code></li>

            <li><code>SAFE\_TO\_PRUNE\_COMMITMENT\_STATE\_MATCH\_MISMATCH</code></li>

            <li><code>SAFE\_TO\_PRUNE\_COMMITMENT\_STATE\_ALL</code></li>
          </ul>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-getsafepruningoffsetresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">safe\_pruning\_offset</code>
                <span class="x2mdx-ref-type-badge">int64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">no\_safe\_pruning\_offset</code>
                <span class="x2mdx-ref-type-badge">NoSafePruningOffset</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.GetSafePruningOffsetResponse.NoSafePruningOffset">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-getsafepruningoffsetresponse-nosafepruningoffset" />
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
          com.digitalasset.canton.admin.participant.v30.PruningService/GetSafePruningOffset <<'EOF'
        {
          "beforeOrAt": "string",
          "ledgerEnd": "0",
          "counterParticipantsCommitmentsState": "SAFE_TO_PRUNE_COMMITMENT_STATE_UNSPECIFIED"
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
          "safePruningOffset": "0"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
