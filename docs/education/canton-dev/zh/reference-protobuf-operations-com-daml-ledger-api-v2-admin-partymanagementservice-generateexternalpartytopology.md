---
title: "GenerateExternalPartyTopology"
slug: "reference-protobuf-operations-com-daml-ledger-api-v2-admin-partymanagementservice-generateexternalpartytopology"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/protobuf/operations/com-daml-ledger-api-v2-admin/partymanagementservice/generateexternalpartytopology.md"
source_title: "GenerateExternalPartyTopology"
tags:
  - reference
  - protobuf
  - operations
  - com-daml-ledger-api-v2-admin
---

# GenerateExternalPartyTopology

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>账本API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="https://docs.canton.network/reference/protobuf/packages/com-daml-ledger-api-v2-admin">com.daml.ledger.api.v2.admin</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>生成ExternalParty拓扑</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.admin</p>

      <h1 class="x2mdx-ref-title">生成ExternalPartyTopology</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.admin.PartyManagementService/GenerateExternalPartyTopology</code>
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
        <dd>生成ExternalPartyTopology</dd>
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
        <h3>生成ExternalPartyTopologyRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.admin.GenerateExternalPartyTopologyRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">同步器</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div><div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">派对\_hint</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">公共\_key</code>
            <span class="x2mdx-ref-type-badge">签名公钥</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">本地\_参与方\_observation\_only</code>
            <span class="x2mdx-ref-type-badge">布尔</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">其他\_确认\_参与者\_uids</code>
            <span class="x2mdx-ref-type-badge">重复字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">确认\_threshold</code>
            <span class="x2mdx-ref-type-badge">uint32</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">观察\_参与方\_uids</code>
            <span class="x2mdx-ref-type-badge">重复字符串</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>生成ExternalPartyTopologyResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.admin.GenerateExternalPartyTopologyResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">party\_id</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">public\_key\_fingerprint</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div><div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">拓扑\_transactions</code>
            <span class="x2mdx-ref-type-badge">重复字节</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">multi\_hash</code>
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

    ## 相关模式

    <手风琴组>
      <手风琴标题=“com.daml.ledger.api.v2.admin.GenerateExternalPartyTopologyRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-generateexternalpartytopologyrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">派对\_hint</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">公共\_key</code>
                <span class="x2mdx-ref-type-badge">签名公钥</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">本地\_参与方\_observation\_only</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">其他\_确认\_参与者\_uids</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">确认\_threshold</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">观察\_参与方\_uids</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.SigningPublicKey”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingpublickey">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">格式</code>
                <span class="x2mdx-ref-type-badge">加密密钥格式</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">key\_data</code>
                <span class="x2mdx-ref-type-badge">字节</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">key\_spec</code>
                <span class="x2mdx-ref-type-badge">签名密钥规范</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.CryptoKeyFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-cryptokeyformat">
          <ul class="x2mdx-ref-enum-list">
            <li><code>CRYPTO\_KEY\_FORMAT\_UNSPECIFIED</code></li>

            <li><code>CRYPTO\_KEY\_FORMAT\_DER</code></li>

            <li><code>CRYPTO\_KEY\_FORMAT\_RAW</code></li>

            <li><code>CRYPTO\_KEY\_FORMAT\_DER\_X509\_SUBJECT\_PUBLIC\_KEY\_INFO</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.SigningKeySpec”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingkeyspec">
          <ul class="x2mdx-ref-enum-list">
            <li><code>签名\_KEY\_SPEC\_UNSPECIFIED</code></li>

            <li><code>SIGNING\_KEY\_SPEC\_EC\_CURVE25519</code></li>

            <li><code>签名\_KEY\_SPEC\_EC\_P256</code></li>

            <li><code>签名\_KEY\_SPEC\_EC\_P384</code></li>

            <li><code>签名\_KEY\_SPEC\_EC\_SECP256K1</code></li>
          </ul>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.admin.GenerateExternalPartyTopologyResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-admin-generateexternalpartytopologyresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">public\_key\_fingerprint</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">拓扑\_transactions</code>
                <span class="x2mdx-ref-type-badge">重复字节</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">multi\_hash</code>
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
        </div>

        ```bash grpcurl theme={"theme":{"light":"github-light","dark":"github-dark"}}
        # Add -plaintext if the server is not using TLS.
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.daml.ledger.api.v2.admin.PartyManagementService/GenerateExternalPartyTopology <<'EOF'
        {
          "同步器": "string",
          "partyHint": "string",
          "publicKey": {
            "format": "CRYPTO_KEY_FORMAT_UNSPECIFIED",
            "keyData": "BASE64_ENCODED_BYTES",
            "keySpec": "SIGNING_KEY_SPEC_UNSPECIFIED"
          },
          "local参与方ObservationOnly": true,
          "otherConfirming参与方Uids": [
            "string"
          ],
          "confirmationThreshold": 0,
          "observing参与方Uids": [
            "string"
          ]
        }
        EOF
        ```
      </div>
    </div><div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code x2mdx-ref-rail-code--response">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">确定</span>

          <span className="x2mdx-ref-response-label">application/json</span>
        </div>

        ```json OK theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {
          "partyId": "string",
          "publicKeyFingerprint": "string",
          "topologyTransactions": [
            "BASE64_ENCODED_BYTES"
          ],
          "multiHash": "BASE64_ENCODED_BYTES"
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
