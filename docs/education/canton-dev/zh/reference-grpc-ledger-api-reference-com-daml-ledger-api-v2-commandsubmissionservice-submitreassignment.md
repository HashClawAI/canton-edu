---
title: "SubmitReassignment"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-commandsubmissionservice-submitreassignment"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2/commandsubmissionservice/submitreassignment.md"
source_title: "SubmitReassignment"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2
  - commandsubmissionservice
---

# SubmitReassignment

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>账本API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="../../com-daml-ledger-api-v2">v2</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>提交重新分配</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2</p>

      <h1 class="x2mdx-ref-title">提交重新分配</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.CommandSubmissionService/SubmitReassignment</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>CommandSubmissionService</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>提交重新分配</dd>
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
        <h3>提交重新分配请求</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.SubmitReassignmentRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">重新分配\_commands</code>
            <span class="x2mdx-ref-type-badge">重新分配命令</span>
          </div>
        </div>
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>提交重新分配响应</h3>
      </div><dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.SubmitReassignmentResponse</dd>
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
        <span class="x2mdx-ref-change-version">3.4.4</span>
        <span class="x2mdx-ref-change-detail">引入</span>
      </div>
    </div>

    ## 相关模式

    <手风琴组>
      <手风琴标题=“com.daml.ledger.api.v2.SubmitReassignmentRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-submitreassignmentrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_commands</code>
                <span class="x2mdx-ref-type-badge">重新分配命令</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ReassignmentCommands”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentcommands">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">工作流程\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">用户\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">命令\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提交者</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提交\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">命令</code>
                <span class="x2mdx-ref-type-badge">重复重新分配命令</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ReassignmentCommand”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentcommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">取消分配\_命令</code>
                <span class="x2mdx-ref-type-badge">取消分配命令</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">分配\_命令</code>
                <span class="x2mdx-ref-type-badge">分配命令</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.UnassignCommand”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-unassigncommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">合约\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">源代码</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">目标</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.AssignCommand”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-assigncommand">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">源代码</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">目标</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.SubmitReassignmentResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-submitreassignmentresponse" />
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
          com.daml.ledger.api.v2.CommandSubmissionService/SubmitReassignment <<'EOF'
        {
          "reassignmentCommands": {
            "workflowId": "string",
            "userId": "string",
            "commandId": "string",
            "submitter": "string",
            "submissionId": "string",
            "commands": [
              {
                "unassignCommand": {
                  "contractId": "string",
                  "source": "string",
                  "target": "string"
                }
              }
            ]
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
        {}
        ```
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
