---
title: "Subscribe completions"
slug: "reference-json-api-asyncapi-reference-operations-v2-commands-completions-subscribe"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-asyncapi-reference/operations/v2-commands-completions/subscribe.md"
source_title: "Subscribe completions"
tags:
  - reference
  - json-api-asyncapi-reference
  - operations
  - v2-commands-completions
---

# Subscribe completions

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <a href="/zh/docs/canton/reference-json-api-asyncapi-reference-operations-details">JSON API AsyncAPI</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-json-api-asyncapi-reference-operations-v2-commands-completions-details">/v2/commands/completions</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>订阅</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">/v2/commands/completions</p>

      <h1 class="x2mdx-ref-title">订阅完成情况</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">WebSocket</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4 起</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--changed">更改为 3.5</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--subscribe">订阅</span>

      <code>/v2/commands/completions</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>WebSocket</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>频道</dt>
        <dd>/v2/commands/completions</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>行动</dt>
        <dd>订阅</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>操作 ID</dt>
        <dd>onV2CommandsCompletions</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>内容类型</dt>
        <dd>应用程序/json</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>有效负载</dt>
        <dd>其中一个</dd>
      </div>
    </dl>

    ## 输入

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>要么\_JsCantonError\_CompletionStreamResponse</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>方向</dt>
          <dd>服务器 -> 客户端</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>要么\_JsCantonError\_CompletionStreamResponse</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">completionResponse</code>
            <span class="x2mdx-ref-type-badge">对象</span>
          </div>
        </div>
      </div>
    </div>

    ## 生命周期变化<div class="x2mdx-ref-change-list">
      <div class="x2mdx-ref-change-item">
        <span class="x2mdx-ref-change-version">3.5</span>
        <span class="x2mdx-ref-change-detail">频道描述已更新；发布更新的描述；订阅说明已更新</span>
      </div>
    </div>

    ## 相关模式

    <手风琴组>
      <手风琴标题=“Either_JsCantonError_CompletionStreamResponse”>
        <div class="x2mdx-ref-schema" id="schema-v2-commands-completions-subscribe">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">completionResponse</code>
                <span class="x2mdx-ref-type-badge">对象</span>
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
          <span className="x2mdx-ref-rail-heading">wscat</span>
        </div>

        ```bash wscat theme={"theme":{"light":"github-light","dark":"github-dark"}}
        npx wscat -c <WEBSOCKET_URL>
        ```
      </div>
    </div>

    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code x2mdx-ref-rail-code--response">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">消息</span>

          <span className="x2mdx-ref-response-label">application/json</span>
        </div>

        ```json message theme={"theme":{"light":"github-light","dark":"github-dark"}}
        {
          "completionResponse": {
            "Completion": {
              "value": {
                "commandId": "<string>",
                "userId": "<string>",
                "actAs": [
                  "<string>"
                ],
                "offset": "<integer>",
                "同步器Time": "<object>"
              }
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
