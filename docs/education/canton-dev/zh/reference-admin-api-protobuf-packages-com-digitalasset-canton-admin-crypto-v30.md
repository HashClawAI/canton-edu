---
title: "com.digitalasset.canton.admin.crypto.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-crypto-v30"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-crypto-v30.md"
source_title: "com.digitalasset.canton.admin.crypto.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.admin.crypto.v30

> com.digitalasset.canton.admin.crypto.v30 的包级别概述。

<p class="x2mdx-ref-back"><a href="../index">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.admin.crypto.v30</h1>

  <p class="x2mdx-ref-summary">0 个服务、0 个端点、1 条消息、1 个枚举</p>

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
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>端点</dt>
      <dd>0</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>消息</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>枚举</dt>
      <dd>1</dd>
    </div>
  </dl>
</div>

## 源文件

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/crypto/v30/crypto.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">最新发布的描述符快照中的当前源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/crypto/v30/crypto.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/crypto/v30/crypto.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 类型库存

这些是发布版本快照中的包级消息和枚举形状。

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-crypto-v30-salt">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.crypto.v30.Salt</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">hmac</code>
        <span class="x2mdx-ref-type-badge">Hmac算法</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">盐</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-crypto-v30-hmacalgorithm">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.crypto.v30.HmacAlgorithm</h3>

    <p class="x2mdx-ref-schema-summary">2 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>HMAC\_ALGORITHM\_UNSPECIFIED</code></li>

    <li><code>HMAC\_ALGORITHM\_HMAC\_SHA256</code></li>
  </ul>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
