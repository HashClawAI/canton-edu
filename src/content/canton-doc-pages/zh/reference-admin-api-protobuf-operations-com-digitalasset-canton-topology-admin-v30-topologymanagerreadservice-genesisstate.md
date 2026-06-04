---
title: "GenesisState"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-topology-admin-v30-topologymanagerreadservice-genesisstate"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-topology-admin-v30/topologymanagerreadservice/genesisstate.md"
source_title: "GenesisState"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# GenesisState

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

      <span>创世状态</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.topology.admin.v30</p>

      <h1 class="x2mdx-ref-title">创世状态</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/GenesisState</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>TopologyManagerReadService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>创世状态</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>是</dd>
      </div>
    </dl>

    ## 输入

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>GenesisStateRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.GenesisStateRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">同步器\_store</code>
            <span class="x2mdx-ref-type-badge">商店 ID</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">时间戳</code>
            <span class="x2mdx-ref-type-badge">时间戳</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>创世状态响应</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.GenesisStateResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>是</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">块</code>
            <span class="x2mdx-ref-type-badge">字节</span>
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

    ## 相关模式<手风琴组>
      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.GenesisStateRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-genesisstaterequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器\_store</code>
                <span class="x2mdx-ref-type-badge">商店 ID</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">时间戳</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>
          </div>
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
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.GenesisStateResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-genesisstateresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">块</code>
                <span class="x2mdx-ref-type-badge">字节</span>
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
        </div>```bash grpcurl theme={"theme":{"light":"github-light","dark":"github-dark"}}
        # Add -plaintext if the server is not using TLS.
        # This RPC uses streaming semantics. Send additional JSON messages on stdin as needed.
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/GenesisState <<'EOF'
        {
          "同步器Store": {
            "authorized": {}
          },
          "timestamp": "string"
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
          "chunk": "BASE64_ENCODED_BYTES"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
