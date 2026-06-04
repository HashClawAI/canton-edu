---
title: "Details and history"
slug: "reference-json-api-reference-details"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/details.md"
source_title: "Details and history"
tags:
  - reference
  - json-api-reference
  - details
---

# Details and history

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Details and history

> JSON Ledger API OpenAPI endpoint details and version history.

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">OpenAPI Reference</p>

  <h1 class="x2mdx-ref-title">Details and history</h1>

  <p class="x2mdx-ref-summary">Endpoint overview for the JSON Ledger API OpenAPI surface, built from versioned release snapshots.</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">OpenAPI</span>

    <span class="x2mdx-ref-badge x2mdx-ref-badge--neutral">3.5</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>Publish version</dt>
      <dd>3.5</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Source</dt>
      <dd>Canton release bundle JSON Ledger API specifications</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>Version filter</dt>
      <dd>3.4, 3.5</dd>
    </div>
  </dl>
</div>

## Endpoints

Select an OpenAPI operation from the sidebar for request and response details. This page summarizes endpoint lifecycle changes across the configured Ledger API versions.

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/submit-and-wait</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submits a single composite command and waits for its result. Propagates the gRPC error of failed submissions including Daml interpretation errors.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/submit-and-wait-for-transaction</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submits a single composite command, waits for its result, and returns the transaction. Propagates the gRPC error of failed submissions including Daml interpretation errors.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/submit-and-wait-for-reassignment</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submits a single composite reassignment command, waits for its result, and returns the reassignment. Propagates the gRPC error of failed submission.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/submit-and-wait-for-transaction-tree</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submit a batch of commands and wait for the transaction trees response. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/async/submit</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submit a single composite command.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/async/submit-reassignment</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Submit a single reassignment.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/commands/completions</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Query completions list (blocking call) Subscribe to command completion events. Notice: This endpoint should be used for small results set. When number of results exceeded node confi...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/events/events-by-contract-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Get the create and the consuming exercise event for the contract with the provided ID. No events will be returned for contracts that have been pruned because they have already been...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/version</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Read the Ledger API version</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/dars/validate</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Validates the DAR and checks the upgrade compatibility of the DAR's packages with the set of the already vetted packages on the target vetting synchronizer. See ValidateDarFileReque...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/dars</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Upload a DAR to the participant node</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/packages</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Returns the identifiers of all supported packages.; POST: Behaves the same as /dars. This endpoint will be deprecated and removed in a future release. Upload a DAR file to the partic...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/packages/\{package-id}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Returns the contents of a single package.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/packages/\{package-id}/status</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Returns the status of a single package.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/package-vetting</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Lists which participant node vetted what packages on which synchronizer. This endpoint (GET /package-vetting) is deprecated and will be removed in a future release. Please use POST /...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/package-vetting/list</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Lists which participant node vetted what packages on which synchronizer. Can be called by any authenticated user.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/package-vetting/update</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Update the vetted packages of this participant</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/parties</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: List the parties known by the participant. The list returned contains parties whose ledger access is facilitated by the participant and the ones maintained elsewhere.; POST: Allocate...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/parties/external/allocate</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Alpha 3.3: Endpoint to allocate a new external party on a synchronizer Expected to be stable in 3.5 The external party must be hosted (at least) on this node with either confirmatio...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/parties/participant-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Return the identifier of the participant. All horizontally scaled replicas should return the same id. daml-on-kv-ledger: returns an identifier supplied on command line at launch time...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/parties/\{party}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, PATCH</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the party details of the given parties. Only known parties will be returned in the list.; PATCH: Update selected modifiable participant-local attributes of a party details resour...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, PATCH</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/parties/external/generate-topology</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Alpha 3.3: Convenience endpoint to generate topology transactions for external signing Expected to be stable in 3.5 You may use this endpoint to generate the common external topolog...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/active-contracts</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Query active contracts list (blocking call). Querying active contracts is an expensive operation and if possible should not be repeated often. Consider querying active contracts ini...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/connected-synchronizers</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the list of connected synchronizers at the time of the query.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/ledger-end</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the current ledger end. Subscriptions started with the returned offset will serve events after this RPC was called.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/state/latest-pruned-offsets</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the latest successfully pruned ledger offsets</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Read the ledger's filtered update stream for the specified contents and filters. It returns the event types in accordance with the stream contents selected. Also the selection crite...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/flats</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Query flat transactions update list (blocking call). Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead. Notice: This endpo...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/trees</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Query update transactions tree list (blocking call). Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead. Notice: This endpo...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/transaction-tree-by-offset/\{offset}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get transaction tree by offset. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates/update-by-offset instead.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/transaction-by-offset</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Get transaction by offset. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates/update-by-offset instead.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/update-by-offset</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Lookup an update by its offset. If there is no update with this offset, or all the events are filtered, an UPDATE\_NOT\_FOUND error will be raised.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/transaction-by-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Get transaction by id. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates/update-by-id instead.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/update-by-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Lookup an update by its ID. If there is no update with this ID, or all the events are filtered, an UPDATE\_NOT\_FOUND error will be raised.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/updates/transaction-tree-by-id/\{update-id}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Deprecated</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get transaction tree by id. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates/update-by-id instead.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/users</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: List all existing users.; POST: Create a new user.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/users/\{user-id}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, DELETE, PATCH</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the user data of a specific user or the authenticated user.; DELETE: Delete an existing user and all its rights.; PATCH: Update selected modifiable attribute of a user resource d...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, DELETE, PATCH</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/authenticated-user</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the user data of the current authenticated user.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/users/\{user-id}/rights</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST, PATCH</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: List the set of all rights granted to a user.; POST: Grant rights to a user. Granting rights does not affect the resource version of the corresponding user.; PATCH: Revoke rights fro...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST, PATCH</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/users/\{user-id}/identity-provider-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">PATCH</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">PATCH: Update the assignment of a user from one IDP to another.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>PATCH</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/idps</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: List all existing identity provider configurations.; POST: Create a new identity provider configuration. The request will fail if the maximum allowed number of separate configuration...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/idps/\{idp-id}</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET, DELETE, PATCH</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Get the identity provider configuration data by id.; DELETE: Delete an existing identity provider configuration.; PATCH: Update selected modifiable attribute of an identity provider...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET, DELETE, PATCH</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/prepare</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Requires `readAs` scope for the submitting party when LAPI User authorization is enabled</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/execute</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Execute a prepared submission *asynchronously* on the ledger. Requires a signature of the transaction from the submitting external party.</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/executeAndWait</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Similar to ExecuteSubmission but *synchronously* wait for the completion of the transaction IMPORTANT: Relying on the response from this endpoint requires trusting the Participant N...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/executeAndWaitForTransaction</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Similar to ExecuteSubmissionAndWait but additionally returns the transaction IMPORTANT: Relying on the response from this endpoint requires trusting the Participant Node to be hones...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/preferred-package-version</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: A preferred package is the highest-versioned package for a provided package-name that is vetted by all the participants hosting the provided parties. Ledger API clients should use th...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/interactive-submission/preferred-packages</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Compute the preferred packages for the vetting requirements in the request. A preferred package is the highest-versioned package for a provided package-name that is vetted by all th...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/livez</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Checks if the service is alive</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/readyz</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">GET</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">GET: Checks if the service is ready to serve requests</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>GET</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>/v2/contracts/contract-by-id</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">POST</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 3.5</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">POST: Looking up contract data by contract ID. This endpoint is experimental / alpha, therefore no backwards compatibility is guaranteed. This endpoint must not be used to look up contrac...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Operations</dt>
        <dd>POST</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Last seen</dt>
        <dd>3.5</dd>
      </div>
    </dl>
  </div>
</div>

## Version Summary

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>3.4</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Added 49</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 0</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Removed 0</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">Endpoint changes included in this release snapshot.</p>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>3.5</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Added 2</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">Changed 49</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--removed">Removed 0</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">Endpoint changes included in this release snapshot.</p>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
