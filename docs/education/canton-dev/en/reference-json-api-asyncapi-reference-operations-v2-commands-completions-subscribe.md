---
title: "Subscribe completions"
slug: "reference-json-api-asyncapi-reference-operations-v2-commands-completions-subscribe"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-commands-completions/subscribe.md"
source_title: "Subscribe completions"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-commands-completions
---

# Subscribe completions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribe completions

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <a href="/docs/canton/reference-json-api-asyncapi-reference-operations-details">JSON API AsyncAPI</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-json-api-asyncapi-reference-operations-v2-commands-completions-details">/v2/commands/completions</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>subscribe</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">/v2/commands/completions</p>

      <h1 class="x2mdx-ref-title">Subscribe completions</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--subscribe">SUBSCRIBE</span>

      <code>/v2/commands/completions</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>WebSocket</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Channel</dt>
        <dd>/v2/commands/completions</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Action</dt>
        <dd>subscribe</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Operation ID</dt>
        <dd>onV2CommandsCompletions</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Content type</dt>
        <dd>application/json</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Payload</dt>
        <dd>oneOf</dd>
      </div>
    </dl>

    ## Inputs

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>Either\_JsCantonError\_CompletionStreamResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Direction</dt>
          <dd>Server -> Client</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>Either\_JsCantonError\_CompletionStreamResponse</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">completionResponse</code>
            <span class="x2mdx-ref-type-badge">object</span>
          </div>
        </div>
      </div>
    </div>

    ## Lifecycle Changes

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.5</span>
        <span class="x2mdx-ref-change-detail">channel description updated; publish description updated; subscribe description updated</span>
      </div>
    </div>

    ## Related Schemas

    <AccordionGroup>
      <Accordion title="Either_JsCantonError_CompletionStreamResponse">
        <div class="x2mdx-ref-schema" id="schema-v2-commands-completions-subscribe">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">completionResponse</code>
                <span class="x2mdx-ref-type-badge">object</span>
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
        npx wscat -c <WEBSOCKET_URL>
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
          "completionResponse": {
            "Completion": {
              "value": {
                "commandId": "<string>",
                "userId": "<string>",
                "actAs": [
                  "<string>"
                ],
                "offset": "<integer>",
                "synchronizerTime": "<object>"
              }
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
