---
title: "CreateUser"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-admin-usermanagementservice-createuser"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-admin/usermanagementservice/createuser.md"
source_title: "CreateUser"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-admin
  - usermanagementservice
---

# CreateUser

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# CreateUser

<div class="x2mdx-ref-page x2mdx-ref-page--operation" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>Ledger API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-grpc-ledger-api-reference-details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-admin">v2.admin</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>CreateUser</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.admin</p>

      <h1 class="x2mdx-ref-title">CreateUser</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--added">Since 3.4.4</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.admin.UserManagementService/CreateUser</code>
    </div>

    ## Protocol Details

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>Protocol</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>Service</dt>
        <dd>UserManagementService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>CreateUser</dd>
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
        <h3>CreateUserRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.CreateUserRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Client stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">user</code>
            <span class="x2mdx-ref-type-badge">User</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">rights</code>
            <span class="x2mdx-ref-type-badge">repeated Right</span>
          </div>
        </div>
      </div>
    </div>

    ## Outputs

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>CreateUserResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>Message</dt>
          <dd>com.daml.ledger.api.v2.admin.CreateUserResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>Server stream</dt>
          <dd>No</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">user</code>
            <span class="x2mdx-ref-type-badge">User</span>
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
      <Accordion title="com.daml.ledger.api.v2.admin.CreateUserRequest">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-createuserrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">user</code>
                <span class="x2mdx-ref-type-badge">User</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">rights</code>
                <span class="x2mdx-ref-type-badge">repeated Right</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.User">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-user">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">id</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">primary\_party</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">is\_deactivated</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">metadata</code>
                <span class="x2mdx-ref-type-badge">ObjectMeta</span>
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
                <code class="x2mdx-ref-field-name">primary\_party\_authentication</code>
                <span class="x2mdx-ref-type-badge">bool</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.ObjectMeta">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-objectmeta">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">resource\_version</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">annotations</code>
                <span class="x2mdx-ref-type-badge">repeated map</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">participant\_admin</code>
                <span class="x2mdx-ref-type-badge">ParticipantAdmin</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">can\_act\_as</code>
                <span class="x2mdx-ref-type-badge">CanActAs</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">can\_read\_as</code>
                <span class="x2mdx-ref-type-badge">CanReadAs</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">identity\_provider\_admin</code>
                <span class="x2mdx-ref-type-badge">IdentityProviderAdmin</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">can\_read\_as\_any\_party</code>
                <span class="x2mdx-ref-type-badge">CanReadAsAnyParty</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">can\_execute\_as</code>
                <span class="x2mdx-ref-type-badge">CanExecuteAs</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">can\_execute\_as\_any\_party</code>
                <span class="x2mdx-ref-type-badge">CanExecuteAsAnyParty</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.ParticipantAdmin">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-participantadmin" />
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.CanActAs">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-canactas">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.CanReadAs">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-canreadas">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.CanExecuteAs">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-canexecuteas">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party</code>
                <span class="x2mdx-ref-type-badge">string</span>
              </div>
            </div>
          </div>
        </div>
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.IdentityProviderAdmin">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-identityprovideradmin" />
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.CanReadAsAnyParty">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-canreadasanyparty" />
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.Right.CanExecuteAsAnyParty">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-right-canexecuteasanyparty" />
      </Accordion>

      <Accordion title="com.daml.ledger.api.v2.admin.CreateUserResponse">
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-createuserresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">user</code>
                <span class="x2mdx-ref-type-badge">User</span>
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
          com.daml.ledger.api.v2.admin.UserManagementService/CreateUser <<'EOF'
        {
          "user": {
            "id": "string",
            "primaryParty": "string",
            "isDeactivated": true,
            "metadata": {
              "resourceVersion": "string",
              "annotations": [
                {
                  "key": "string"
                }
              ]
            },
            "identityProviderId": "string",
            "primaryPartyAuthentication": true
          },
          "rights": [
            {
              "participantAdmin": {}
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
          "user": {
            "id": "string",
            "primaryParty": "string",
            "isDeactivated": true,
            "metadata": {
              "resourceVersion": "string",
              "annotations": [
                {
                  "key": "string"
                }
              ]
            },
            "identityProviderId": "string",
            "primaryPartyAuthentication": true
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
