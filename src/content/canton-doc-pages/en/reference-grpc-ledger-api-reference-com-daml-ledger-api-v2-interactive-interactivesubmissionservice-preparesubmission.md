---
title: "PrepareSubmission"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive-interactivesubmissionservice-preparesubmission"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive/interactivesubmissionservice/preparesubmission.md"
source_title: "PrepareSubmission"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive
  - interactivesubmissionservice
---

# PrepareSubmission

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# PrepareSubmission

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Ledger API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-grpc-ledger-api-reference-details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive">v2.interactive</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>PrepareSubmission</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.interactive</p>

      <h1 class="x2mdx-ref-title">PrepareSubmission</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/PrepareSubmission</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>InteractiveSubmissionService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>PrepareSubmission</dd>
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
        <h3>PrepareSubmissionRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

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

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>PrepareSubmissionResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

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

    ## Lifecycle Changes

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.4.4</span>
        <span class="x2mdx-ref-change-detail">introduced</span>
      </div>
    </div>

    ## Related Schemas

    <AccordionGroup>
      <Accordion title="com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionrequest">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Command">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-command">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.CreateCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createcommand">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Identifier">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-identifier">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Record">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-record">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.RecordField">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-recordfield">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Value">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-value">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Optional">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-optional">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">value</code>
                <span class="x2mdx-ref-type-badge">Value</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.List">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-list">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">elements</code>
                <span class="x2mdx-ref-type-badge">repeated Value</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.TextMap">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">entries</code>
                <span class="x2mdx-ref-type-badge">repeated Entry</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.TextMap.Entry">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap-entry">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.GenMap">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">entries</code>
                <span class="x2mdx-ref-type-badge">repeated Entry</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.GenMap.Entry">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap-entry">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Variant">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-variant">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Enum">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-enum">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.ExerciseCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisecommand">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.ExerciseByKeyCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisebykeycommand">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.CreateAndExerciseCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createandexercisecommand">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.MinLedgerTime">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-minledgertime">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.DisclosedContract">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-disclosedcontract">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.PrefetchContractKey">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-prefetchcontractkey">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.CostEstimationHints">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimationhints">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.SigningAlgorithmSpec">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingalgorithmspec">
          <ul class="x2mdx-ref-enum-list">
            <li><code>SIGNING\_ALGORITHM\_SPEC\_UNSPECIFIED</code></li>

            <li><code>SIGNING\_ALGORITHM\_SPEC\_ED25519</code></li>

            <li><code>SIGNING\_ALGORITHM\_SPEC\_EC\_DSA\_SHA\_256</code></li>

            <li><code>SIGNING\_ALGORITHM\_SPEC\_EC\_DSA\_SHA\_384</code></li>
          </ul>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.HashingSchemeVersion">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-hashingschemeversion">
          <ul class="x2mdx-ref-enum-list">
            <li><code>HASHING\_SCHEME\_VERSION\_UNSPECIFIED</code></li>

            <li><code>HASHING\_SCHEME\_VERSION\_V2</code></li>

            <li><code>HASHING\_SCHEME\_VERSION\_V3</code></li>
          </ul>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.PrepareSubmissionResponse">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionresponse">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.PreparedTransaction">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparedtransaction">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.DamlTransaction">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.DamlTransaction.NodeSeed">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-nodeseed">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.DamlTransaction.Node">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-node">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.Node">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-node">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.Create">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-create">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.GlobalKeyWithMaintainers">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkeywithmaintainers">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.GlobalKey">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkey">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.Fetch">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-fetch">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.Exercise">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-exercise">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.Rollback">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-rollback">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">children</code>
                <span class="x2mdx-ref-type-badge">repeated string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.transaction.v1.QueryByKey">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-querybykey">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.Metadata">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.Metadata.SubmitterInfo">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-submitterinfo">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.Metadata.GlobalKeyMappingEntry">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-globalkeymappingentry">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.Metadata.InputContract">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-inputcontract">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.interactive.CostEstimation">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimation">
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
          com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/PrepareSubmission <<'EOF'
        {
          "userId": "string",
          "commandId": "string",
          "commands": [
            {
              "create": {
                "templateId": {
                  "packageId": "string",
                  "moduleName": "string",
                  "entityName": "string"
                },
                "createArguments": {
                  "recordId": {},
                  "fields": [
                    {}
                  ]
                }
              }
            }
          ],
          "minLedgerTime": {
            "minLedgerTimeAbs": "string"
          },
          "maxRecordTime": "string",
          "actAs": [
            "string"
          ],
          "readAs": [
            "string"
          ],
          "disclosedContracts": [
            {
              "templateId": {
                "packageId": "string",
                "moduleName": "string",
                "entityName": "string"
              },
              "contractId": "string",
              "createdEventBlob": "BASE64_ENCODED_BYTES",
              "synchronizerId": "string"
            }
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
          "preparedTransaction": {
            "transaction": {
              "version": "string",
              "roots": [
                "string"
              ],
              "nodes": [
                {
                  "nodeId": "string",
                  "v1": {}
                }
              ],
              "nodeSeeds": [
                {
                  "nodeId": 0,
                  "seed": "BASE64_ENCODED_BYTES"
                }
              ]
            },
            "metadata": {
              "submitterInfo": {
                "actAs": [
                  "string"
                ],
                "commandId": "string"
              },
              "synchronizerId": "string",
              "mediatorGroup": 0,
              "transactionUuid": "string",
              "preparationTime": "0",
              "inputContracts": [
                {
                  "v1": {},
                  "createdAt": "0",
                  "eventBlob": "BASE64_ENCODED_BYTES"
                }
              ],
              "minLedgerEffectiveTime": "0",
              "maxLedgerEffectiveTime": "0"
            }
          },
          "preparedTransactionHash": "BASE64_ENCODED_BYTES",
          "hashingSchemeVersion": "HASHING_SCHEME_VERSION_UNSPECIFIED",
          "hashingDetails": "string",
          "costEstimation": {
            "estimationTimestamp": "string",
            "confirmationRequestTrafficCostEstimation": "0",
            "confirmationResponseTrafficCostEstimation": "0",
            "totalTrafficCostEstimation": "0"
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
