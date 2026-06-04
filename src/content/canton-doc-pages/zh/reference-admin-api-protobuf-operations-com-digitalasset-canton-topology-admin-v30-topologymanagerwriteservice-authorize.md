---
title: "Authorize"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-topology-admin-v30-topologymanagerwriteservice-authorize"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-topology-admin-v30/topologymanagerwriteservice/authorize.md"
source_title: "Authorize"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# Authorize

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>共享管理</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-admin-api-protobuf-packages-com-digitalasset-canton-topology-admin-v30">com.digitalasset.canton.topology.admin.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>授权</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.topology.admin.v30</p>

      <h1 class="x2mdx-ref-title">授权</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/Authorize</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>TopologyManagerWriteService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>授权</dd>
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
        <h3>授权请求</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.AuthorizeRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">提案</code>
            <span class="x2mdx-ref-type-badge">提案</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">交易\_hash</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">必须\_完全\_授权</code>
            <span class="x2mdx-ref-type-badge">布尔</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">强制\_changes</code>
            <span class="x2mdx-ref-type-badge">重复的 ForceFlag</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">签名\_by</code>
            <span class="x2mdx-ref-type-badge">重复字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">商店</code>
            <span class="x2mdx-ref-type-badge">商店 ID</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">等待\_变得\_有效</code>
            <span class="x2mdx-ref-type-badge">持续时间</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>授权响应</h3>
      </div><dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.AuthorizeResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">交易</code>
            <span class="x2mdx-ref-type-badge">签名拓扑事务</span>
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
      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.AuthorizeRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-authorizerequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提案</code>
                <span class="x2mdx-ref-type-badge">提案</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">交易\_hash</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">必须\_完全\_授权</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">强制\_changes</code>
                <span class="x2mdx-ref-type-badge">重复的 ForceFlag</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">签名\_by</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">商店</code>
                <span class="x2mdx-ref-type-badge">商店 ID</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">等待\_变得\_有效</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.AuthorizeRequest.Proposal”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-authorizerequest-proposal">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">更改</code>
                <span class="x2mdx-ref-type-badge">TopologyChangeOp</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">序列号</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">映射</code>
                <span class="x2mdx-ref-type-badge">拓扑映射</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.topology.admin.v30.ForceFlag”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-forceflag">
          <ul class="x2mdx-ref-enum-list">
            <li><code>强制\_FLAG\_UNSPECIFIED</code></li>

            <li><code>强制\_FLAG\_ALIEN\_MEMBER</code></li>

            <li><code>强制\_FLAG\_LEDGER\_TIME\_RECORD\_TIME\_TOLERANCE\_INCREASE</code></li>

            <li><code>强制\_FLAG\_ALLOW\_UNKNOWN\_PACKAGE</code></li>

            <li><code>强制\_FLAG\_ALLOW\_UNVETTED\_DEPENDENCIES</code></li>

            <li><code>强制\_FLAG\_DISABLE\_PARTY\_WITH\_ACTIVE\_CONTRACTS</code></li>

            <li><code>强制\_FLAG\_ALLOW\_UNVALIDATED\_SIGNING\_KEYS</code></li>

            <li><code>强制\_FLAG\_PREPARATION\_TIME\_RECORD\_TIME\_TOLERANCE\_INCREASE</code></li>

            <li><code>强制\_FLAG\_ALLOW\_INSUFFICIENT\_PARTICIPANT\_PERMISSION\_FOR\_SIGNATORY\_PARTY</code></li>

            <li><code>强制\_FLAG\_ALLOW\_INSUFFICIENT\_SIGNATORY\_ASSIGNING\_PARTICIPANTS\_FOR\_PARTY</code></li>

            <li><code>强制\_FLAG\_ALLOW\_VET\_INCOMPATIBLE\_UPGRADES</code></li>

            <li><code>强制\_FLAG\_ALLOW\_OUT\_OF\_BOUNDS\_VALUE</code></li>

            <li><code>强制\_FLAG\_ALLOW\_CONFIRMING\_THRESHOLD\_CANNOT\_BE\_MET</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.StoreId”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">已授权</code>
                <span class="x2mdx-ref-type-badge">授权</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器</code>
                <span class="x2mdx-ref-type-badge">同步器</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">临时</code>
                <span class="x2mdx-ref-type-badge">临时</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.StoreId.Authorized”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid-authorized" />
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.StoreId.Temporary”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-storeid-temporary">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">名称</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.同步器”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-同步器">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">物理\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.topology.admin.v30.AuthorizeResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-authorizeresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">交易</code>
                <span class="x2mdx-ref-type-badge">签名拓扑事务</span>
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
          com.digitalasset.canton.topology.admin.v30.TopologyManagerWriteService/Authorize <<'EOF'
        {
          "proposal": {
            "change": "string",
            "serial": 0,
            "mapping": "string"
          },
          "mustFullyAuthorize": true,
          "forceChanges": [
            "FORCE_FLAG_UNSPECIFIED"
          ],
          "signedBy": [
            "string"
          ],
          "store": {
            "authorized": {}
          },
          "waitToBecomeEffective": "string"
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
          "transaction": "string"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
