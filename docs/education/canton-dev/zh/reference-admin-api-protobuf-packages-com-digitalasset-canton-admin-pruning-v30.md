---
title: "com.digitalasset.canton.admin.pruning.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-pruning-v30"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-pruning-v30.md"
source_title: "com.digitalasset.canton.admin.pruning.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.admin.pruning.v30

> com.digitalasset.canton.admin.pruning.v30 的包级别概述。

<p class="x2mdx-ref-back"><a href="/zh/docs/canton/reference-admin-api-protobuf-index">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.admin.pruning.v30</h1>

  <p class="x2mdx-ref-summary">0 个服务、0 个端点、28 条消息</p>

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
      <dd>28</dd>
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
      <h3>community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">最新发布的描述符快照中的当前源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>28</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/pruning/v30/pruning.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 类型库存

这些是发布版本快照中的包级消息和枚举形状。

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-clearschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ClearScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-clearscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ClearScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-findpruningtimestamprequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.FindPruningTimestampRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">索引</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-findpruningtimestampresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.FindPruningTimestampResponse</h3>

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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">参与者\_uids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">忽略\_参与方s</code>
        <span class="x2mdx-ref-type-badge">重复 WaitCommitmentsSetup</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">不\_忽略\_参与者</code>
        <span class="x2mdx-ref-type-badge">重复 WaitCommitmentsSetup</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-waitcommitmentssetup">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.WaitCommitmentsSetup</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">计数器\_参与方\_uid</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器</code>
        <span class="x2mdx-ref-type-badge">同步器</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-同步器s">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.同步器s</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-get参与方schedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-get参与方scheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.Get参与方ScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间表</code>
        <span class="x2mdx-ref-type-badge">参与者修剪计划</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-参与方pruningschedule">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.参与方PruningSchedule</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-pruningschedule">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.PruningSchedule</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div><div class="x2mdx-ref-fields">
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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-getscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.GetScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间表</code>
        <span class="x2mdx-ref-type-badge">修剪时间表</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-resetnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">计数器\_参与方\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-resetnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.ResetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setcronrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetCronRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">cron</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setcronresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetCronResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setmaxdurationrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetMaxDurationRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">最大\_持续时间</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setmaxdurationresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetMaxDurationResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setnowaitcommitmentsfromrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">计数器\_参与方\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_ids</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setnowaitcommitmentsfromresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetNoWaitCommitmentsFromResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-set参与方schedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.Set参与方ScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间表</code>
        <span class="x2mdx-ref-type-badge">参与者修剪计划</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-set参与方scheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.Set参与方ScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setretentionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetRetentionRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">保留</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setretentionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetRetentionResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setschedulerequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetScheduleRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">时间表</code>
        <span class="x2mdx-ref-type-badge">修剪时间表</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-pruning-v30-setscheduleresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.pruning.v30.SetScheduleResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
