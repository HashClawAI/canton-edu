---
title: "AddPartyWithAcsAsync"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-partymanagementservice-addpartywithacsasync"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/partymanagementservice/addpartywithacsasync.md"
source_title: "AddPartyWithAcsAsync"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# AddPartyWithAcsAsync

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# AddPartyWithAcsAsync

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

      <span>AddPartyWithAcsAsync</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.participant.v30</p>

      <h1 class="x2mdx-ref-title">AddPartyWithAcsAsync</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.5.1</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.participant.v30.PartyManagementService/AddPartyWithAcsAsync</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>PartyManagementService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>AddPartyWithAcsAsync</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Client stream</dt>
        <dd>Yes</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Server stream</dt>
        <dd>No</dd>
      </div>
    </dl>

    ## Inputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>AddPartyWithAcsAsyncRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.AddPartyWithAcsAsyncRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>Yes</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">acs\_snapshot</code>
            <span class="x2mdx-ref-type-badge">bytes</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">arguments</code>
            <span class="x2mdx-ref-type-badge">AddPartyArguments</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>AddPartyWithAcsAsyncResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.AddPartyWithAcsAsyncResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">add\_party\_request\_id</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>
      </div>
    </div>

    ## Lifecycle Changes

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.5.1</span>
        <span class="x2mdx-ref-change-detail">introduced</span>
      </div>
    </div>

    ## Related Schemas

    <AccordionGroup>
      <Accordion title="com.digitalasset.canton.admin.participant.v30.AddPartyWithAcsAsyncRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-addpartywithacsasyncrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">acs\_snapshot</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">arguments</code>
                <span class="x2mdx-ref-type-badge">AddPartyArguments</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.AddPartyArguments">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-addpartyarguments">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
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
                <code class="x2mdx-ref-field-name">source\_participant\_uid</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">topology\_serial</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">participant\_permission</code>
                <span class="x2mdx-ref-type-badge">ParticipantPermission</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.ParticipantPermission">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-participantpermission">
          <ul class="x2mdx-ref-enum-list">
            <li><code>PARTICIPANT\_PERMISSION\_UNSPECIFIED</code></li>

            <li><code>PARTICIPANT\_PERMISSION\_SUBMISSION</code></li>

            <li><code>PARTICIPANT\_PERMISSION\_CONFIRMATION</code></li>

            <li><code>PARTICIPANT\_PERMISSION\_OBSERVATION</code></li>
          </ul>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.AddPartyWithAcsAsyncResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-addpartywithacsasyncresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">add\_party\_request\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
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
          com.digitalasset.canton.admin.participant.v30.PartyManagementService/AddPartyWithAcsAsync <<'EOF'
        {
          "acsSnapshot": "BASE64_ENCODED_BYTES",
          "arguments": {
            "partyId": "string",
            "synchronizerId": "string",
            "sourceParticipantUid": "string",
            "topologySerial": 0,
            "participantPermission": "PARTICIPANT_PERMISSION_UNSPECIFIED"
          }
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
          "addPartyRequestId": "string"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
