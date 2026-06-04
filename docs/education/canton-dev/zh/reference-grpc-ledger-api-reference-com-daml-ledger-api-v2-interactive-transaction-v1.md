---
title: "v2.interactive.transaction.v1"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive-transaction-v1"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive-transaction-v1.md"
source_title: "v2.interactive.transaction.v1"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive-transaction-v1
---

# v2.interactive.transaction.v1

> com.daml.ledger.api.v2.interactive.transaction.v1 的包级概述。

<p class="x2mdx-ref-back"><a href="/zh/docs/canton/reference-grpc-ledger-api-reference-details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">v2.interactive.transaction.v1</h1>

  <p class="x2mdx-ref-summary">0 个服务、0 个端点、6 条消息</p>

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
      <dd>6</dd>
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
      <h3>交互式\_submission\_data.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">来自最新描述符快照的源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>6</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/transaction/v1/interactive_s ubmission_data.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/transaction/v1/interactive\_submission\_data.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 类型库存

这些是发布版本快照中的包级消息和枚举形状。

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-create">
  <div class="x2mdx-ref-schema-head">
    <h3>创建</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 8 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">参数</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签署者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">利益相关者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-identifier">
  <div class="x2mdx-ref-schema-head">
    <h3>标识符</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模块\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">实体\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-value">
  <div class="x2mdx-ref-schema-head">
    <h3>值</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 16 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">单位</code>
        <span class="x2mdx-ref-type-badge">空</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">布尔</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">int64</code>
        <span class="x2mdx-ref-type-badge">sint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">日期</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间戳</code>
        <span class="x2mdx-ref-type-badge">sfixed64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">数字</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">派对</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">文本</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">可选</code>
        <span class="x2mdx-ref-type-badge">可选</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">列表</code>
        <span class="x2mdx-ref-type-badge">列表</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">文本\_map</code>
        <span class="x2mdx-ref-type-badge">文本映射</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">gen\_map</code>
        <span class="x2mdx-ref-type-badge">GenMap</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">记录</code>
        <span class="x2mdx-ref-type-badge">记录</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">变体</code>
        <span class="x2mdx-ref-type-badge">变体</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">枚举</code>
        <span class="x2mdx-ref-type-badge">枚举</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-可选">
  <div class="x2mdx-ref-schema-head">
    <h3>可选</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">值</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-list">
  <div class="x2mdx-ref-schema-head">
    <h3>列表</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">元素</code>
        <span class="x2mdx-ref-type-badge">重复值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap">
  <div class="x2mdx-ref-schema-head">
    <h3>文本映射</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">条目</code>
        <span class="x2mdx-ref-type-badge">重复条目</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap-entry">
  <div class="x2mdx-ref-schema-head">
    <h3>TextMap.Entry</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">值</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap">
  <div class="x2mdx-ref-schema-head">
    <h3>GenMap</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">条目</code>
        <span class="x2mdx-ref-type-badge">重复条目</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap-entry">
  <div class="x2mdx-ref-schema-head">
    <h3>GenMap.Entry</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">值</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-record">
  <div class="x2mdx-ref-schema-head">
    <h3>记录</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">记录\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">字段</code>
        <span class="x2mdx-ref-type-badge">重复记录字段</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-recordfield">
  <div class="x2mdx-ref-schema-head">
    <h3>记录字段</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">标签</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">值</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-variant">
  <div class="x2mdx-ref-schema-head">
    <h3>变体</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">变体\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">构造函数</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">值</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-enum">
  <div class="x2mdx-ref-schema-head">
    <h3>枚举</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">枚举\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">构造函数</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkeywithmaintainers">
  <div class="x2mdx-ref-schema-head">
    <h3>GlobalKeyWithMaintainers</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">全局密钥</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">维护者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkey">
  <div class="x2mdx-ref-schema-head">
    <h3>全局密钥</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">哈希</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-exercise">
  <div class="x2mdx-ref-schema-head">
    <h3>练习</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 16 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签署者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">利益相关者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">表演\_当事人</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">接口\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_value</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">消费</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">孩子</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">练习\_结果</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_observers</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">作者\_key</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-fetch">
  <div class="x2mdx-ref-schema-head">
    <h3>获取</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 10 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签署者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">利益相关者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">表演\_当事人</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">接口\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">作者\_key</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-node">
  <div class="x2mdx-ref-schema-head">
    <h3>节点</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 5 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">创建</code>
        <span class="x2mdx-ref-type-badge">创建</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">获取</code>
        <span class="x2mdx-ref-type-badge">获取</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">练习</code>
        <span class="x2mdx-ref-type-badge">练习</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">回滚</code>
        <span class="x2mdx-ref-type-badge">回滚</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">查询\_by\_key</code>
        <span class="x2mdx-ref-type-badge">按密钥查询</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-rollback">
  <div class="x2mdx-ref-schema-head">
    <h3>回滚</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">孩子</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-querybykey">
  <div class="x2mdx-ref-schema-head">
    <h3>按键查询</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 6 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">lf\_version</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">详尽</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">GlobalKeyWithMaintainers</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">结果</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
