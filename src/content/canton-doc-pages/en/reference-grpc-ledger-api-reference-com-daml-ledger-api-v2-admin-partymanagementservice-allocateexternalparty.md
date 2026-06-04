---
title: "AllocateExternalParty"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-admin-partymanagementservice-allocateexternalparty"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-admin/partymanagementservice/allocateexternalparty.md"
source_title: "AllocateExternalParty"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-admin
  - partymanagementservice
---

# AllocateExternalParty

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# AllocateExternalParty

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Ledger API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../com-daml-ledger-api-v2-admin">v2.admin</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>AllocateExternalParty</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.admin</p>

      <h1 class="x2mdx-ref-title">AllocateExternalParty</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.admin.PartyManagementService/AllocateExternalParty</code>
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
        <dd>AllocateExternalParty</dd>
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
        <h3>AllocateExternalPartyRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.AllocateExternalPartyRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">synchronizer</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">onboarding\_transactions</code>
            <span class="x2mdx-ref-type-badge">repeated SignedTransaction</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">multi\_hash\_signatures</code>
            <span class="x2mdx-ref-type-badge">repeated Signature</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">identity\_provider\_id</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">wait\_for\_allocation</code>
            <span class="x2mdx-ref-type-badge">bool</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">user\_id</code>
            <span class="x2mdx-ref-type-badge">string</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>AllocateExternalPartyResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.AllocateExternalPartyResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">party\_id</code>
            <span class="x2mdx-ref-type-badge">string</span>
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
      <Accordion title="com.daml.ledger.api.v2.admin.AllocateExternalPartyRequest">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-allocateexternalpartyrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">synchronizer</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">onboarding\_transactions</code>
                <span class="x2mdx-ref-type-badge">repeated SignedTransaction</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">multi\_hash\_signatures</code>
                <span class="x2mdx-ref-type-badge">repeated Signature</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">identity\_provider\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">wait\_for\_allocation</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">user\_id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.AllocateExternalPartyRequest.SignedTransaction">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-allocateexternalpartyrequest-signedtransaction">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">transaction</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">signatures</code>
                <span class="x2mdx-ref-type-badge">repeated Signature</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.Signature">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signature">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">format</code>
                <span class="x2mdx-ref-type-badge">SignatureFormat</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">signature</code>
                <span class="x2mdx-ref-type-badge">bytes</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">signed\_by</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">signing\_algorithm\_spec</code>
                <span class="x2mdx-ref-type-badge">SigningAlgorithmSpec</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.SignatureFormat">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signatureformat">
          <ul class="x2mdx-ref-enum-list">
            <li><code>SIGNATURE\_FORMAT\_UNSPECIFIED</code></li>

            <li><code>SIGNATURE\_FORMAT\_RAW</code></li>

            <li><code>SIGNATURE\_FORMAT\_DER</code></li>

            <li><code>SIGNATURE\_FORMAT\_CONCAT</code></li>

            <li><code>SIGNATURE\_FORMAT\_SYMBOLIC</code></li>
          </ul>
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

      <Accordion title="com.daml.ledger.api.v2.admin.AllocateExternalPartyResponse">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-allocateexternalpartyresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
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
          com.daml.ledger.api.v2.admin.PartyManagementService/AllocateExternalParty <<'EOF'
        {
          "synchronizer": "string",
          "onboardingTransactions": [
            {
              "transaction": "BASE64_ENCODED_BYTES",
              "signatures": [
                {
                  "format": "SIGNATURE_FORMAT_UNSPECIFIED",
                  "signature": "BASE64_ENCODED_BYTES",
                  "signedBy": "string",
                  "signingAlgorithmSpec": "SIGNING_ALGORITHM_SPEC_UNSPECIFIED"
                }
              ]
            }
          ],
          "multiHashSignatures": [
            {
              "format": "SIGNATURE_FORMAT_UNSPECIFIED",
              "signature": "BASE64_ENCODED_BYTES",
              "signedBy": "string",
              "signingAlgorithmSpec": "SIGNING_ALGORITHM_SPEC_UNSPECIFIED"
            }
          ],
          "identityProviderId": "string",
          "waitForAllocation": true,
          "userId": "string"
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
          "partyId": "string"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
