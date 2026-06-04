---
title: "v2.testing"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-testing.md"
source_title: "v2.testing"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-testing
---

# v2.testing

> com.daml.ledger.api.v2.testing 的包级概述。

<p class="x2mdx-ref-back"><a href="/zh/docs/canton/reference-grpc-ledger-api-reference-details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">v2.testing</h1>

  <p class="x2mdx-ref-summary">1 个服务、2 个端点、3 条消息</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>文件</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>服务</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>端点</dt>
      <dd>2</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>消息</dt>
      <dd>3</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>枚举</dt>
      <dd>0</dd>
    </div>
  </dl>
</div>

## 源文件

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>时间\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">来自最新描述符快照的源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>3</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 时间服务

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>源文件</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/testing/time\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>操作</dt>
    <dd>2</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing-timeservice-gettime">
    <div class="x2mdx-ref-card-head">
      <h3>TimeService.GetTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div><p class="x2mdx-ref-card-summary">rpc TimeService.GetTime(com.daml.ledger.api.v2.testing.GetTimeRequest) 返回 (com.daml.ledger.api.v2.testing.GetTimeResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.testing.GetTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.testing.GetTimeResponse</dd>
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
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-testing-timeservice-settime">
    <div class="x2mdx-ref-card-head">
      <h3>TimeService.SetTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc TimeService.SetTime(com.daml.ledger.api.v2.testing.SetTimeRequest) 返回 (google.protobuf.Empty);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.testing.SetTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>google.protobuf.Empty</dd>
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
  </a>
</div>

## 类型库存

这些是发布版本快照中的包级消息和枚举形状。

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-gettimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>获取时间请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-gettimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>获取时间响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">当前\_时间</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-testing-settimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>设置时间请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.testing · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">当前\_时间</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">新\_时间</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
