---
title: "AddPartyAsync"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-partymanagementservice-addpartyasync"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/partymanagementservice/addpartyasync.md"
source_title: "AddPartyAsync"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# AddPartyAsync

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>参与者管理</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-参与方-v30">com.digitalasset.canton.admin.参与方.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>AddPartyAsync</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.参与方.v30</p>

      <h1 class="x2mdx-ref-title">AddPartyAsync</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.参与方.v30.PartyManagementService/AddPartyAsync</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>派对管理服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>AddPartyAsync</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>

    ## 输入

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>AddPartyAsyncRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.AddPartyAsyncRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">参数</code>
            <span class="x2mdx-ref-type-badge">AddPartyArguments</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>AddPartyAsyncResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.AddPartyAsyncResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">添加\_party\_request\_id</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>
      </div>
    </div>

    ## 生命周期变化

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.4.0</span>
        <span class="x2mdx-ref-change-detail">引入</span>
      </div>
    </div>

    ## 相关模式

    <手风琴组>
      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.AddPartyAsyncRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-addpartyasyncrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参数</code>
                <span class="x2mdx-ref-type-badge">AddPartyArguments</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.参与方.v30.AddPartyArguments”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-addpartyarguments">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">源\_参与方\_uid</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">拓扑\_serial</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_权限</code>
                <span class="x2mdx-ref-type-badge">参与者权限</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.参与方Permission”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-参与方permission">
          <ul class="x2mdx-ref-enum-list">
            <li><code>参与者\_PERMISSION\_UNSPECIFIED</code></li>

            <li><code>参与者\_PERMISSION\_SUBMISSION</code></li>

            <li><code>参与者\_PERMISSION\_CONFIRMATION</code></li>

            <li><code>参与者\_PERMISSION\_OBSERVATION</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.AddPartyAsyncResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-addpartyasyncresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">添加\_party\_request\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>
    </手风琴组>
  </div>

  <div className="x2mdx-ref-right-rail" role="complementary" aria-label="示例和响应">
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
          com.digitalasset.canton.admin.参与方.v30.PartyManagementService/AddPartyAsync <<'EOF'
        {
          "arguments": {
            "partyId": "string",
            "同步器Id": "string",
            "source参与方Uid": "string",
            "topologySerial": 0,
            "参与方Permission": "PARTICIPANT_PERMISSION_UNSPECIFIED"
          }
        }
        EOF
        ```
      </div>
    </div>

    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code x2mdx-ref-rail-code--response">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">确定</span>

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

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
