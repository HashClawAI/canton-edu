---
title: "RegisterSynchronizer"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-participant-v30-synchronizerconnectivityservice-registersynchronizer"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-participant-v30/synchronizerconnectivityservice/registersynchronizer.md"
source_title: "RegisterSynchronizer"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# RegisterSynchronizer

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

      <span>注册同步器</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.参与方.v30</p>

      <h1 class="x2mdx-ref-title">注册同步器</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">已更改 3.5.1</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.参与方.v30.同步器ConnectivityService/Register同步器</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>同步器ConnectivityService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>注册同步器</dd>
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
        <h3>注册同步器请求</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.Register同步器Request</dd>
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
            <span class="x2mdx-ref-type-badge">同步器ConnectionConfig</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">同步器\_connection</code>
            <span class="x2mdx-ref-type-badge">同步器Connection</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">sequencer\_connection\_validation</code>
            <span class="x2mdx-ref-type-badge">SequencerConnectionValidation</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>注册同步器响应</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.参与方.v30.Register同步器Response</dd>
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

      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.5.1</span>
        <span class="x2mdx-ref-change-detail">文件</span>
      </div>
    </div>

    ## 相关模式<手风琴组>
      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.Register同步器Request”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-register同步器request">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">配置</code>
                <span class="x2mdx-ref-type-badge">同步器ConnectionConfig</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器\_connection</code>
                <span class="x2mdx-ref-type-badge">同步器Connection</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_connection\_validation</code>
                <span class="x2mdx-ref-type-badge">SequencerConnectionValidation</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.Register同步器Request.同步器Connection”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-register同步器request-同步器connection">
          <ul class="x2mdx-ref-enum-list">
            <li><code>SYNCHRONIZER\_CONNECTION\_UNSPECIFIED</code></li>

            <li><code>SYNCHRONIZER\_CONNECTION\_NONE</code></li>

            <li><code>SYNCHRONIZER\_CONNECTION\_HANDSHAKE</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.同步器ConnectionConfig”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-同步器connectionconfig">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">同步器\_alias</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">音序器\_connections</code>
                <span class="x2mdx-ref-type-badge">SequencerConnections</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">手动\_connect</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">物理\_同步器\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">优先级</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">初始\_重试\_延迟</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_retry\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">时间\_tracker</code>
                <span class="x2mdx-ref-type-badge">同步器TimeTrackerConfig</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">从\_trusted\_同步器初始化\_</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.sequencer.v30.SequencerConnections”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnections">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">音序器\_connections</code>
                <span class="x2mdx-ref-type-badge">重复 SequencerConnection</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_trust\_threshold</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提交\_请求\_放大</code>
                <span class="x2mdx-ref-type-badge">提交请求放大</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_liveness\_margin</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">sequencer\_connection\_pool\_delays</code>
                <span class="x2mdx-ref-type-badge">SequencerConnectionPoolDelay</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.sequencer.v30.SequencerConnection”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnection">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">grpc</code>
                <span class="x2mdx-ref-type-badge">Grpc</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">别名</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">音序器\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.sequencer.v30.SequencerConnection.Grpc”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnection-grpc">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">连接</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">运输\_安全</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">自定义\_trust\_证书</code>
                <span class="x2mdx-ref-type-badge">字节</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.sequencer.v30.SubmissionRequestAmplification”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-submissionrequestamplification">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">因素</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">耐心</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">确认\_response\_factor</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">确认\_response\_patience</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <Accordion title="com.digitalasset.canton.admin.sequencer.v30.SequencerConnectionPoolDelays">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnectionpooldelays">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">min\_restart\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_restart\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">订阅\_request\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">警告\_validation\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.time.v30.同步器TimeTrackerConfig”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-同步器timetrackerconfig">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">观察\_延迟</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">耐心\_duration</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">min\_observation\_duration</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">时间\_proof\_request</code>
                <span class="x2mdx-ref-type-badge">TimeProofRequestConfig</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.time.v30.TimeProofRequestConfig”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-time-v30-timeproofrequestconfig">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">初始\_重试\_延迟</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">max\_retry\_delay</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">最大\_排序\_延迟</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.sequencer.v30.SequencerConnectionValidation”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-sequencer-v30-sequencerconnectionvalidation">
          <ul class="x2mdx-ref-enum-list">
            <li><code>SEQUENCER\_CONNECTION\_VALIDATION\_UNSPECIFIED</code></li>

            <li><code>SEQUENCER\_CONNECTION\_VALIDATION\_DISABLED</code></li>

            <li><code>SEQUENCER\_CONNECTION\_VALIDATION\_ACTIVE</code></li>

            <li><code>SEQUENCER\_CONNECTION\_VALIDATION\_ALL</code></li>

            <li><code>SEQUENCER\_CONNECTION\_VALIDATION\_THRESHOLD\_ACTIVE</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.参与方.v30.Register同步器Response”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-参与方-v30-register同步器response" />
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
          com.digitalasset.canton.admin.参与方.v30.同步器ConnectivityService/Register同步器 <<'EOF'
        {
          "config": {
            "同步器Alias": "string",
            "sequencerConnections": {
              "sequencerConnections": [
                {
                  "grpc": {},
                  "alias": "string",
                  "sequencerId": "string"
                }
              ],
              "sequencerTrustThreshold": 0,
              "submissionRequestAmplification": {
                "factor": 0,
                "patience": "string",
                "confirmationResponseFactor": 0,
                "confirmationResponsePatience": "string"
              },
              "sequencerLivenessMargin": 0,
              "sequencerConnectionPoolDelays": {
                "minRestartDelay": "string",
                "maxRestartDelay": "string",
                "subscriptionRequestDelay": "string",
                "warnValidationDelay": "string"
              }
            },
            "manualConnect": true,
            "physical同步器Id": "string",
            "priority": 0,
            "initialRetryDelay": "string",
            "maxRetryDelay": "string",
            "timeTracker": {
              "observationLatency": "string",
              "patienceDuration": "string",
              "minObservationDuration": "string",
              "timeProofRequest": {
                "initialRetryDelay": "string",
                "maxRetryDelay": "string",
                "maxSequencingDelay": "string"
              }
            }
          },
          "同步器Connection": "SYNCHRONIZER_CONNECTION_UNSPECIFIED",
          "sequencerConnectionValidation": "SEQUENCER_CONNECTION_VALIDATION_UNSPECIFIED"
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
        {}
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
