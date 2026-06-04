---
title: "GetLedgerApiVersion"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-versionservice-getledgerapiversion"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2/versionservice/getledgerapiversion.md"
source_title: "GetLedgerApiVersion"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2
  - versionservice
---

# GetLedgerApiVersion

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>账本API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2">v2</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>获取LedgerApiVersion</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2</p>

      <h1 class="x2mdx-ref-title">获取LedgerApiVersion</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.VersionService/GetLedgerApiVersion</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>版本服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>获取LedgerApiVersion</dd>
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
        <h3>获取LedgerApiVersionRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.GetLedgerApiVersionRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>获取LedgerApiVersionResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.GetLedgerApiVersionResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl><div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">版本</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">功能</code>
            <span class="x2mdx-ref-type-badge">功能描述符</span>
          </div>
        </div>
      </div>
    </div>

    ## 生命周期变化

    <div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.4.4</span>
        <span class="x2mdx-ref-change-detail">引入</span>
      </div>
    </div>

    ## 相关模式

    <手风琴组>
      <手风琴标题=“com.daml.ledger.api.v2.GetLedgerApiVersionRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-getledgerapiversionrequest" />
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.GetLedgerApiVersionResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-getledgerapiversionresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">版本</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">功能</code>
                <span class="x2mdx-ref-type-badge">功能描述符</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.FeaturesDescriptor”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-featuresdescriptor">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">实验</code>
                <span class="x2mdx-ref-type-badge">实验功能</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">用户\_管理</code>
                <span class="x2mdx-ref-type-badge">用户管理功能</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">派对\_管理</code>
                <span class="x2mdx-ref-type-badge">派对管理功能</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">偏移量\_checkpoint</code>
                <span class="x2mdx-ref-type-badge">OffsetCheckpointFeature</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包\_feature</code>
                <span class="x2mdx-ref-type-badge">软件包功能</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ExperimentalFeatures”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-experimentalfeatures">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">静态\_时间</code>
                <span class="x2mdx-ref-type-badge">实验静态时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">命令\_inspection\_service</code>
                <span class="x2mdx-ref-type-badge">ExperimentalCommandInspectionService</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ExperimentalStaticTime”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-experimentalstatictime">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">支持</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.ExperimentalCommandInspectionService”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-experimentalcommandinspectionservice">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">支持</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.UserManagementFeature”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-usermanagementfeature">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">支持</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">最大\_权限\_per\_user</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_users\_page\_size</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.PartyManagementFeature”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-partymanagementfeature">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_parties\_page\_size</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.OffsetCheckpointFeature”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-offsetcheckpointfeature">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_offset\_checkpoint\_emission\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.PackageFeature”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-packagefeature">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_vetted\_packages\_page\_size</code>
                <span class="x2mdx-ref-type-badge">int32</span>
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
          com.daml.ledger.api.v2.VersionService/GetLedgerApiVersion <<'EOF'
        {}
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
          "version": "string",
          "features": {
            "experimental": {
              "staticTime": {
                "supported": true
              },
              "commandInspectionService": {
                "supported": true
              }
            },
            "userManagement": {
              "supported": true,
              "maxRightsPerUser": 0,
              "maxUsersPageSize": 0
            },
            "partyManagement": {
              "maxPartiesPageSize": 0
            },
            "offsetCheckpoint": {
              "maxOffsetCheckpointEmissionDelay": "string"
            },
            "packageFeature": {
              "maxVettedPackagesPageSize": 0
            }
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
