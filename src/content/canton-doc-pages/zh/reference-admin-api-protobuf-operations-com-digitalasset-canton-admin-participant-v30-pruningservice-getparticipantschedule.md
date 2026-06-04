---
title: "GetParticipantSchedule"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-pruningservice-getparticipantschedule"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/pruningservice/getparticipantschedule.md"
source_title: "GetParticipantSchedule"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# GetParticipantSchedule

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>参与者管理</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../../packages/com-digitalasset-canton-admin-参与方-v30">com.digitalasset.canton.admin.参与方.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>获取参与者时间表</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.参与方.v30</p>

      <h1 class="x2mdx-ref-title">获取参与者时间表</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.参与方.v30.PruningService/Get参与方Schedule</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>修剪服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>获取参与者时间表</dd>
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
        <h3>获取参与方ScheduleRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleRequest</dd>
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
        <h3>获取参与方ScheduleResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">时间表</code>
            <span class="x2mdx-ref-type-badge">参与者修剪计划</span>
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
      <手风琴标题=“com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-get参与方schedulerequest" />
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-get参与方scheduleresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">时间表</code>
                <span class="x2mdx-ref-type-badge">参与者修剪计划</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.pruning.v30.参与方PruningSchedule”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-参与方pruningschedule">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">时间表</code>
                <span class="x2mdx-ref-type-badge">修剪时间表</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">修剪\_internally\_only</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.pruning.v30.PruningSchedule”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-pruningschedule">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">cron</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">最大\_持续时间</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">保留</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
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
          com.digitalasset.canton.admin.参与方.v30.PruningService/Get参与方Schedule <<'EOF'
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
          "schedule": {
            "schedule": {
              "cron": "string",
              "maxDuration": "string",
              "retention": "string"
            },
            "pruneInternallyOnly": true
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
