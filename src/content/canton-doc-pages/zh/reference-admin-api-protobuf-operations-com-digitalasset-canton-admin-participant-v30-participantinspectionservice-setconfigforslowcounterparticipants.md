---
title: "SetConfigForSlowCounterParticipants"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-participantinspectionservice-setconfigforslowcounterparticipants"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/participantinspectionservice/setconfigforslowcounterparticipants.md"
source_title: "SetConfigForSlowCounterParticipants"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# SetConfigForSlowCounterParticipants

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

      <span>SetConfigForSlowCounter参与方s</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.参与方.v30</p>

      <h1 class="x2mdx-ref-title">SetConfigForSlowCounter参与方s</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.参与方.v30.参与方InspectionService/SetConfigForSlowCounter参与方s</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>参与者检查服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>SetConfigForSlowCounter参与方s</dd>
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
        <h3>SetConfigForSlowCounter参与方sRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.SetConfigForSlowCounter参与方sRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">配置</code>
            <span class="x2mdx-ref-type-badge">重复的 SlowCounter参与方同步器Config</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>SetConfigForSlowCounter参与方sResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.SetConfigForSlowCounter参与方sResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>
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
      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.SetConfigForSlowCounter参与方sRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-setconfigforslowcounter参与方srequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">配置</code>
                <span class="x2mdx-ref-type-badge">重复的 SlowCounter参与方同步器Config</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.参与方.v30.SlowCounter参与方同步器Config”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-slowcounter参与方同步器config">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器\_ids</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">尊敬的\_参与方\_uids</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">阈值\_distinguished</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">阈值\_default</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_uids\_metrics</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.SetConfigForSlowCounter参与方sResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-setconfigforslowcounter参与方sresponse" />
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
          com.digitalasset.canton.admin.参与方.v30.参与方InspectionService/SetConfigForSlowCounter参与方s <<'EOF'
        {
          "configs": [
            {
              "同步器Ids": [
                "string"
              ],
              "distinguished参与方Uids": [
                "string"
              ],
              "thresholdDistinguished": "0",
              "thresholdDefault": "0",
              "参与方UidsMetrics": [
                "string"
              ]
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
          <span className="x2mdx-ref-rail-heading">确定</span>

          <span className="x2mdx-ref-response-label">application/json</span>
        </div>

        ```json OK theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {}
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
