---
title: "SubmitAndWaitForReassignment"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-commandservice-submitandwaitforreassignment"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2/commandservice/submitandwaitforreassignment.md"
source_title: "SubmitAndWaitForReassignment"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2
  - commandservice
---

# SubmitAndWaitForReassignment

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SubmitAndWaitForReassignment

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Ledger API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../com-daml-ledger-api-v2">v2</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>SubmitAndWaitForReassignment</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2</p>

      <h1 class="x2mdx-ref-title">SubmitAndWaitForReassignment</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.CommandService/SubmitAndWaitForReassignment</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>CommandService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>SubmitAndWaitForReassignment</dd>
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
        <h3>SubmitAndWaitForReassignmentRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.SubmitAndWaitForReassignmentRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">reassignment\_commands</code>
            <span class="x2mdx-ref-type-badge">ReassignmentCommands</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">event\_format</code>
            <span class="x2mdx-ref-type-badge">EventFormat</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>SubmitAndWaitForReassignmentResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.SubmitAndWaitForReassignmentResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">reassignment</code>
            <span class="x2mdx-ref-type-badge">Reassignment</span>
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
      <Accordion title="com.daml.ledger.api.v2.SubmitAndWaitForReassignmentRequest">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-submitandwaitforreassignmentrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_commands</code>
                <span class="x2mdx-ref-type-badge">ReassignmentCommands</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">event\_format</code>
                <span class="x2mdx-ref-type-badge">EventFormat</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.ReassignmentCommands">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentcommands">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">workflow\_id</code>
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
                <code class="x2mdx-ref-field-name">command\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">submitter</code>
                <span class="x2mdx-ref-type-badge">string</span>
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
                <code class="x2mdx-ref-field-name">commands</code>
                <span class="x2mdx-ref-type-badge">repeated ReassignmentCommand</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.ReassignmentCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentcommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">unassign\_command</code>
                <span class="x2mdx-ref-type-badge">UnassignCommand</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">assign\_command</code>
                <span class="x2mdx-ref-type-badge">AssignCommand</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.UnassignCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-unassigncommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">contract\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">source</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">target</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.AssignCommand">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-assigncommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">source</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">target</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.EventFormat">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-eventformat">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Filters">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-filters">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">cumulative</code>
                <span class="x2mdx-ref-type-badge">repeated CumulativeFilter</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.CumulativeFilter">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-cumulativefilter">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.WildcardFilter">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-wildcardfilter">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">include\_created\_event\_blob</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.InterfaceFilter">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfacefilter">
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

      <Accordion title="com.daml.ledger.api.v2.TemplateFilter">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-templatefilter">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.SubmitAndWaitForReassignmentResponse">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-submitandwaitforreassignmentresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment</code>
                <span class="x2mdx-ref-type-badge">Reassignment</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Reassignment">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignment">
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
                <code class="x2mdx-ref-field-name">offset</code>
                <span class="x2mdx-ref-type-badge">int64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">events</code>
                <span class="x2mdx-ref-type-badge">repeated ReassignmentEvent</span>
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
                <code class="x2mdx-ref-field-name">synchronizer\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.ReassignmentEvent">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">unassigned</code>
                <span class="x2mdx-ref-type-badge">UnassignedEvent</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">assigned</code>
                <span class="x2mdx-ref-type-badge">AssignedEvent</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.UnassignedEvent">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-unassignedevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_id</code>
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
                <code class="x2mdx-ref-field-name">template\_id</code>
                <span class="x2mdx-ref-type-badge">Identifier</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">source</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">target</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">submitter</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_counter</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">assignment\_exclusivity</code>
                <span class="x2mdx-ref-type-badge">Timestamp</span>
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
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.AssignedEvent">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-assignedevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">source</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">target</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">submitter</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">reassignment\_counter</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">created\_event</code>
                <span class="x2mdx-ref-type-badge">CreatedEvent</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.CreatedEvent">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createdevent">
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

      <Accordion title="com.daml.ledger.api.v2.InterfaceView">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfaceview">
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
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.TraceContext">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-tracecontext">
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
          com.daml.ledger.api.v2.CommandService/SubmitAndWaitForReassignment <<'EOF'
        {
          "reassignmentCommands": {
            "workflowId": "string",
            "userId": "string",
            "commandId": "string",
            "submitter": "string",
            "submissionId": "string",
            "commands": [
              {
                "unassignCommand": {
                  "contractId": "string",
                  "source": "string",
                  "target": "string"
                }
              }
            ]
          },
          "eventFormat": {
            "filtersByParty": [
              {
                "key": {
                  "cumulative": [
                    {
                      "wildcardFilter": {}
                    }
                  ]
                }
              }
            ],
            "filtersForAnyParty": {
              "cumulative": [
                {
                  "wildcardFilter": {}
                }
              ]
            },
            "verbose": true
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
          "reassignment": {
            "updateId": "string",
            "commandId": "string",
            "workflowId": "string",
            "offset": "0",
            "events": [
              {
                "unassigned": {
                  "reassignmentId": "string",
                  "contractId": "string",
                  "templateId": {},
                  "source": "string",
                  "target": "string",
                  "submitter": "string",
                  "reassignmentCounter": "0",
                  "assignmentExclusivity": "string"
                }
              }
            ],
            "traceContext": {
              "traceparent": "string",
              "tracestate": "string"
            },
            "recordTime": "string",
            "synchronizerId": "string"
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
