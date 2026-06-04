---
title: "MigrateSynchronizer"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-participantrepairservice-migratesynchronizer"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/participantrepairservice/migratesynchronizer.md"
source_title: "MigrateSynchronizer"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# MigrateSynchronizer

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# MigrateSynchronizer

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

      <span>MigrateSynchronizer</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.participant.v30</p>

      <h1 class="x2mdx-ref-title">MigrateSynchronizer</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.0</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.participant.v30.ParticipantRepairService/MigrateSynchronizer</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>ParticipantRepairService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>MigrateSynchronizer</dd>
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
        <h3>MigrateSynchronizerRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.MigrateSynchronizerRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">source\_synchronizer\_alias</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">target\_synchronizer\_connection\_config</code>
            <span class="x2mdx-ref-type-badge">SynchronizerConnectionConfig</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">force</code>
            <span class="x2mdx-ref-type-badge">bool</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>MigrateSynchronizerResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.digitalasset.canton.admin.participant.v30.MigrateSynchronizerResponse</dd>
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
      <Accordion title="com.digitalasset.canton.admin.participant.v30.MigrateSynchronizerRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-migratesynchronizerrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">source\_synchronizer\_alias</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">target\_synchronizer\_connection\_config</code>
                <span class="x2mdx-ref-type-badge">SynchronizerConnectionConfig</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">force</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.SynchronizerConnectionConfig">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-synchronizerconnectionconfig">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">synchronizer\_alias</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_connections</code>
                <span class="x2mdx-ref-type-badge">SequencerConnections</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">manual\_connect</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">physical\_synchronizer\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">priority</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>

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
                <code class="x2mdx-ref-field-name">time\_tracker</code>
                <span class="x2mdx-ref-type-badge">SynchronizerTimeTrackerConfig</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">initialize\_from\_trusted\_synchronizer</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SequencerConnections">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnections">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_connections</code>
                <span class="x2mdx-ref-type-badge">repeated SequencerConnection</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_trust\_threshold</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">submission\_request\_amplification</code>
                <span class="x2mdx-ref-type-badge">SubmissionRequestAmplification</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_liveness\_margin</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_connection\_pool\_delays</code>
                <span class="x2mdx-ref-type-badge">SequencerConnectionPoolDelays</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SequencerConnection">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnection">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">grpc</code>
                <span class="x2mdx-ref-type-badge">Grpc</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">alias</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SequencerConnection.Grpc">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnection-grpc">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">connections</code>
                <span class="x2mdx-ref-type-badge">repeated string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">transport\_security</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">custom\_trust\_certificates</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SubmissionRequestAmplification">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-submissionrequestamplification">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">factor</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">patience</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">confirmation\_response\_factor</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">confirmation\_response\_patience</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SequencerConnectionPoolDelays">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnectionpooldelays">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">min\_restart\_delay</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_restart\_delay</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">subscription\_request\_delay</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">warn\_validation\_delay</code>
                <span class="x2mdx-ref-type-badge">Duration</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.time.v30.SynchronizerTimeTrackerConfig">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-synchronizertimetrackerconfig">
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
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.time.v30.TimeProofRequestConfig">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-timeproofrequestconfig">
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
      </Accordion>

      <Accordion title="com.digitalasset.canton.admin.participant.v30.MigrateSynchronizerResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-participant-v30-migratesynchronizerresponse" />
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
          com.digitalasset.canton.admin.participant.v30.ParticipantRepairService/MigrateSynchronizer <<'EOF'
        {
          "sourceSynchronizerAlias": "string",
          "targetSynchronizerConnectionConfig": {
            "synchronizerAlias": "string",
            "sequencerConnections": {
              "sequencerConnections": [
                {
                  "grpc": {},
                  "alias": "string",
                  "sequencerId": "string"
                }
              ],
              "sequencerTrustThreshold": 0,
              "submissionRequestAmplification": {
                "factor": 0,
                "patience": "string",
                "confirmationResponseFactor": 0,
                "confirmationResponsePatience": "string"
              },
              "sequencerLivenessMargin": 0,
              "sequencerConnectionPoolDelays": {
                "minRestartDelay": "string",
                "maxRestartDelay": "string",
                "subscriptionRequestDelay": "string",
                "warnValidationDelay": "string"
              }
            },
            "manualConnect": true,
            "physicalSynchronizerId": "string",
            "priority": 0,
            "initialRetryDelay": "string",
            "maxRetryDelay": "string",
            "timeTracker": {
              "observationLatency": "string",
              "patienceDuration": "string",
              "minObservationDuration": "string",
              "timeProofRequest": {
                "initialRetryDelay": "string",
                "maxRetryDelay": "string",
                "maxSequencingDelay": "string"
              }
            }
          },
          "force": true
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
