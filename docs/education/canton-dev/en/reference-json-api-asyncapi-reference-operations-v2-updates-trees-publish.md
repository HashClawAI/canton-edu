---
title: "Publish trees"
slug: "reference-json-api-asyncapi-reference-operations-v2-updates-trees-publish"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-updates-trees/publish.md"
source_title: "Publish trees"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-updates-trees
---

# Publish trees

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Publish trees

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <a href="/docs/canton/reference-json-api-asyncapi-reference-operations-details">JSON API AsyncAPI</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-updates-trees-details">/v2/updates/trees</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>publish</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">/v2/updates/trees</p>

      <h1 class="x2mdx-ref-title">Publish trees</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--publish">PUBLISH</span>

      <code>/v2/updates/trees</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>WebSocket</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Channel</dt>
        <dd>/v2/updates/trees</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Action</dt>
        <dd>publish</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>sendV2UpdatesTrees</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Content type</dt>
        <dd>application/json</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Payload</dt>
        <dd>object</dd>
      </div>
    </dl>

    ## Inputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>GetUpdatesRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Direction</dt>
          <dd>Client -> Server</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>GetUpdatesRequest</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">beginExclusive</code>
            <span class="x2mdx-ref-type-badge">string</span>

            <span class="x2mdx-ref-required-badge">required</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    ## Lifecycle Changes

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.5</span>
        <span class="x2mdx-ref-change-detail">publish description updated; publish required fields added: `beginExclusive`; publish required fields removed: `updateFormat`; subscribe description updated</span>
      </div>
    </div>

    ## Related Schemas

    <AccordionGroup>
      <Accordion title="GetUpdatesRequest">
        <div class="x2mdx-ref-schema" id="schema-v2-updates-trees-publish">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">beginExclusive</code>
                <span class="x2mdx-ref-type-badge">string</span>

                <span class="x2mdx-ref-required-badge">required</span>
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
          <span className="x2mdx-ref-rail-heading">wscat</span>
        </div>

        ```bash wscat theme={"theme":{"light":"github-light","dark":"github-dark"}}
        npx wscat \
          -c <WEBSOCKET_URL> \
          -x '{"beginExclusive": "<integer>"}' \
          -w -1
        ```
      </div>
    </div>

    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code x2mdx-ref-rail-code--response">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">message</span>

          <span className="x2mdx-ref-response-label">application/json</span>
        </div>

        ```json message theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {
          "beginExclusive": "<integer>"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
