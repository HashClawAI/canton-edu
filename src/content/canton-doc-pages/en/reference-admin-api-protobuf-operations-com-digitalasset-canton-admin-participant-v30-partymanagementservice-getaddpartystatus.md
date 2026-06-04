---
title: "GetAddPartyStatus"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-partymanagementservice-getaddpartystatus"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/partymanagementservice/getaddpartystatus.md"
source_title: "GetAddPartyStatus"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# GetAddPartyStatus

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# GetAddPartyStatus

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Participant Administration</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-participant-v30">com.digitalasset.canton.admin.participant.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>GetAddPartyStatus</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.participant.v30</p>

      <h1 class="x2mdx-ref-title">GetAddPartyStatus</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.participant.v30.PartyManagementService/GetAddPartyStatus</code>
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
        <dd>GetAddPartyStatus</dd>
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
        <h3>GetAddPartyStatusRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.GetAddPartyStatusRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
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

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>GetAddPartyStatusResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.GetAddPartyStatusResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">status</code>
            <span class="x2mdx-ref-type-badge">PartyReplicationStatus</span>
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
      <Accordion title="com.digitalasset.canton.admin.participant.v30.GetAddPartyStatusRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-getaddpartystatusrequest">
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

      <Accordion title="com.digitalasset.canton.admin.participant.v30.GetAddPartyStatusResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-getaddpartystatusresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">status</code>
                <span class="x2mdx-ref-type-badge">PartyReplicationStatus</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">parameters</code>
                <span class="x2mdx-ref-type-badge">ReplicationParameters</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">agreement</code>
                <span class="x2mdx-ref-type-badge">SequencerChannelAgreement</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">authorization</code>
                <span class="x2mdx-ref-type-badge">PartyReplicationAuthorization</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">replication</code>
                <span class="x2mdx-ref-type-badge">AcsReplicationProgress</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">indexing</code>
                <span class="x2mdx-ref-type-badge">AcsIndexingProgress</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">has\_completed</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">error\_message</code>
                <span class="x2mdx-ref-type-badge">PartyReplicationError</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.ReplicationParameters">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-replicationparameters">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">request\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

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
                <code class="x2mdx-ref-field-name">target\_participant\_uid</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">topology\_serial</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.SequencerChannelAgreement">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-sequencerchannelagreement">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_uid</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.PartyReplicationAuthorization">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-partyreplicationauthorization">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">onboarding\_at</code>
                <span class="x2mdx-ref-type-badge">Timestamp</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">is\_onboarding\_flag\_cleared</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.AcsReplicationProgress">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-acsreplicationprogress">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">processed\_contract\_count</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">fully\_processed\_acs</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.AcsIndexingProgress">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-acsindexingprogress" />
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.PartyReplicationStatus.PartyReplicationError">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-partyreplicationstatus-partyreplicationerror">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">error\_message</code>
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
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.digitalasset.canton.admin.participant.v30.PartyManagementService/GetAddPartyStatus <<'EOF'
        {
          "addPartyRequestId": "string"
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
          "status": {
            "parameters": {
              "requestId": "string",
              "partyId": "string",
              "synchronizerId": "string",
              "sourceParticipantUid": "string",
              "targetParticipantUid": "string",
              "topologySerial": 0
            },
            "agreement": {
              "sequencerUid": "string"
            },
            "authorization": {
              "onboardingAt": "string",
              "isOnboardingFlagCleared": true
            },
            "replication": {
              "processedContractCount": "0",
              "fullyProcessedAcs": true
            },
            "indexing": {},
            "hasCompleted": true,
            "errorMessage": {
              "errorMessage": "string"
            }
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
