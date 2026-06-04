---
title: "ListVettedPackages"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-topology-admin-v30-topologymanagerreadservice-listvettedpackages"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-topology-admin-v30/topologymanagerreadservice/listvettedpackages.md"
source_title: "ListVettedPackages"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# ListVettedPackages

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>共享管理</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../packages/com-digitalasset-canton-topology-admin-v30">com.digitalasset.canton.topology.admin.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>列出VettedPackages</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.topology.admin.v30</p>

      <h1 class="x2mdx-ref-title">列出VettedPackages</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/ListVettedPackages</code>
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
        <dd>列出VettedPackages</dd>
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
        <h3>ListVettedPackagesRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.ListVettedPackagesRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">base\_query</code>
            <span class="x2mdx-ref-type-badge">基本查询</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">过滤器\_参与方</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>ListVettedPackagesResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.topology.admin.v30.ListVettedPackagesResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">结果</code>
            <span class="x2mdx-ref-type-badge">重复结果</span>
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
      <Accordion title="com.digitalasset.canton.topology.admin.v30.ListVettedPackagesRequest">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-listvettedpackagesrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">base\_query</code>
                <span class="x2mdx-ref-type-badge">基本查询</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">过滤器\_参与方</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.BaseQuery”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-basequery">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">商店</code>
                <span class="x2mdx-ref-type-badge">商店 ID</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提案</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">操作</code>
                <span class="x2mdx-ref-type-badge">TopologyChangeOp</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">快照</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">head\_state</code>
                <span class="x2mdx-ref-type-badge">空</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">范围</code>
                <span class="x2mdx-ref-type-badge">时间范围</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">过滤器\_signed\_key</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">协议\_版本</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.topology.admin.v30.BaseQuery.TimeRange”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-basequery-timerange">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">来自</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">直到</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.topology.admin.v30.StoreId”>
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

      <Accordion title="com.digitalasset.canton.topology.admin.v30.ListVettedPackagesResponse">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-listvettedpackagesresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">结果</code>
                <span class="x2mdx-ref-type-badge">重复结果</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <Accordion title="com.digitalasset.canton.topology.admin.v30.ListVettedPackagesResponse.Result">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-listvettedpackagesresponse-result">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">上下文</code>
                <span class="x2mdx-ref-type-badge">基本结果</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">项目</code>
                <span class="x2mdx-ref-type-badge">经过审查的包</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.topology.admin.v30.BaseResult”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-baseresult">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">商店</code>
                <span class="x2mdx-ref-type-badge">商店 ID</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">序列</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">有效\_from</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">有效\_直到</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">操作</code>
                <span class="x2mdx-ref-type-badge">TopologyChangeOp</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">交易\_hash</code>
                <span class="x2mdx-ref-type-badge">字节</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">序列号</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">签名\_by\_fingerprints</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
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
          com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/ListVettedPackages <<'EOF'
        {
          "baseQuery": {
            "store": {
              "authorized": {}
            },
            "proposals": true,
            "operation": "string",
            "snapshot": "string",
            "filterSignedKey": "string",
            "protocolVersion": 0
          },
          "filter参与方": "string"
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
        </div>```json OK theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {
          "results": [
            {
              "context": {
                "store": {
                  "authorized": {}
                },
                "sequenced": "string",
                "validFrom": "string",
                "validUntil": "string",
                "operation": "string",
                "transactionHash": "BASE64_ENCODED_BYTES",
                "serial": 0,
                "signedByFingerprints": [
                  "string"
                ]
              },
              "item": "string"
            }
          ]
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
