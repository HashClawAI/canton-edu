---
title: "com.digitalasset.canton.time.admin.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-time-admin-v30"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-time-admin-v30.md"
source_title: "com.digitalasset.canton.time.admin.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.time.admin.v30

> com.digitalasset.canton.time.admin.v30 的包级别概述。

<p class="x2mdx-ref-back"><a href="../index">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.time.admin.v30</h1>

  <p class="x2mdx-ref-summary">1 个服务、2 个端点、4 条消息</p>

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
      <dd>4</dd>
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
      <h3>community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/同步器\_time\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">最新发布的描述符快照中的当前源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>4</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronize r_time_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/同步器\_time\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 同步器时间服务

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>源文件</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/synchronize r_time_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/time/admin/v30/同步器\_time\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>操作</dt>
    <dd>2</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-time-admin-v30/同步器timeservice/awaittime">
    <div class="x2mdx-ref-card-head">
      <h3>同步器TimeService.AwaitTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc 同步器TimeService.AwaitTime(com.digitalasset.canton.time.admin.v30.AwaitTimeRequest) 返回 (com.digitalasset.canton.time.admin.v30.AwaitTimeResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.time.admin.v30.AwaitTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.time.admin.v30.AwaitTimeResponse</dd>
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

  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-time-admin-v30/同步器timeservice/fetchtime">
    <div class="x2mdx-ref-card-head">
      <h3>同步器TimeService.FetchTime</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc 同步器TimeService.FetchTime(com.digitalasset.canton.time.admin.v30.FetchTimeRequest) 返回 (com.digitalasset.canton.time.admin.v30.FetchTimeResponse);</p><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.time.admin.v30.FetchTimeRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.time.admin.v30.FetchTimeResponse</dd>
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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-awaittimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.AwaitTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器</code>
        <span class="x2mdx-ref-type-badge">同步器</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间戳</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-topology-admin-v30-同步器">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.topology.admin.v30.同步器</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-awaittimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.AwaitTimeResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-fetchtimerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.FetchTimeRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器</code>
        <span class="x2mdx-ref-type-badge">同步器</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">新鲜度\_bound</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-time-admin-v30-fetchtimeresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.time.admin.v30.FetchTimeResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间戳</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
