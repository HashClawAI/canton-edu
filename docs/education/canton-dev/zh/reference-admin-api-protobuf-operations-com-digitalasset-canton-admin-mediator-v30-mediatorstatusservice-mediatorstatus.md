---
title: "MediatorStatus"
slug: "reference-admin-api-protobuf-operations-com-digitalasset-canton-admin-mediator-v30-mediatorstatusservice-mediatorstatus"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/operations/com-digitalasset-canton-admin-mediator-v30/mediatorstatusservice/mediatorstatus.md"
source_title: "MediatorStatus"
tags:
  - reference
  - admin-api
  - protobuf
  - operations
---

# MediatorStatus

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>调解员</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-admin-api-protobuf-index">Protobuf</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-mediator-v30">com.digitalasset.canton.admin.mediator.v30</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>调解员状态</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.digitalasset.canton.admin.mediator.v30</p>

      <h1 class="x2mdx-ref-title">MediatorStatus</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.digitalasset.canton.admin.mediator.v30.MediatorStatusService/MediatorStatus</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>MediatorStatusService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>调解器状态</dd>
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
        <h3>MediatorStatusRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.mediator.v30.MediatorStatusRequest</dd>
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
        <h3>MediatorStatusResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.digitalasset.canton.admin.mediator.v30.MediatorStatusResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">状态</code>
            <span class="x2mdx-ref-type-badge">MediatorStatusResponseStatus</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">未\_初始化</code>
            <span class="x2mdx-ref-type-badge">未初始化</span>
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
      <手风琴标题=“com.digitalasset.canton.admin.mediator.v30.MediatorStatusRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-mediator-v30-mediatorstatusrequest" />
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.mediator.v30.MediatorStatusResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-mediator-v30-mediatorstatusresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">状态</code>
                <span class="x2mdx-ref-type-badge">MediatorStatusResponseStatus</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">未\_初始化</code>
                <span class="x2mdx-ref-type-badge">未初始化</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <Accordion title="com.digitalasset.canton.admin.mediator.v30.MediatorStatusResponse.MediatorStatusResponseStatus">
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-mediator-v30-mediatorstatusresponse-mediatorstatusresponsestatus">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">常见\_status</code>
                <span class="x2mdx-ref-type-badge">状态</span>
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
                <code class="x2mdx-ref-field-name">协议\_版本</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.health.v30.Status”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-status">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">uid</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">正常运行时间</code>
                <span class="x2mdx-ref-type-badge">持续时间</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">端口</code>
                <span class="x2mdx-ref-type-badge">重复地图</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">活动</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">拓扑\_队列</code>
                <span class="x2mdx-ref-type-badge">拓扑队列状态</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">组件</code>
                <span class="x2mdx-ref-type-badge">重复的 ComponentStatus</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">版本</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.health.v30.TopologyQueueStatus”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-topologyqueuestatus">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">经理</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">调度程序</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">客户端</code>
                <span class="x2mdx-ref-type-badge">uint32</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.health.v30.ComponentStatus”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-componentstatus">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">名称</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">好的</code>
                <span class="x2mdx-ref-type-badge">状态数据</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">降级</code>
                <span class="x2mdx-ref-type-badge">状态数据</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">失败</code>
                <span class="x2mdx-ref-type-badge">状态数据</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">致命</code>
                <span class="x2mdx-ref-type-badge">状态数据</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.health.v30.ComponentStatus.StatusData”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-componentstatus-statusdata">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">描述</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.digitalasset.canton.admin.health.v30.NotInitialized”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-notinitialized">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">活动</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">等待\_for\_external\_input</code>
                <span class="x2mdx-ref-type-badge">等待外部输入</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">版本</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.digitalasset.canton.admin.health.v30.NotInitialized.WaitingForExternalInput”>
        <div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-notinitialized-waitingforexternalinput">
          <ul class="x2mdx-ref-enum-list">
            <li><code>正在等待\_FOR\_EXTERNAL\_INPUT\_UNSPECIFIED</code></li>

            <li><code>正在等待\_FOR\_EXTERNAL\_INPUT\_ID</code></li>

            <li><code>等待\_FOR\_EXTERNAL\_INPUT\_NODE\_TOPOLOGY</code></li>

            <li><code>等待\_FOR\_EXTERNAL\_INPUT\_INITIALIZATION</code></li>
          </ul>
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
          com.digitalasset.canton.admin.mediator.v30.MediatorStatusService/MediatorStatus <<'EOF'
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
          "status": {
            "commonStatus": {
              "uid": "string",
              "uptime": "string",
              "ports": [
                {
                  "key": 0
                }
              ],
              "active": true,
              "topologyQueues": {
                "manager": 0,
                "dispatcher": 0,
                "clients": 0
              },
              "components": [
                {
                  "name": "string",
                  "ok": {}
                }
              ],
              "version": "string"
            },
            "physical同步器Id": "string",
            "protocolVersion": 0
          }
        }
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
