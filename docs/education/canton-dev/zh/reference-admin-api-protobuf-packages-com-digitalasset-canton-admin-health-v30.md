---
title: "com.digitalasset.canton.admin.health.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-admin-health-v30"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-admin-health-v30.md"
source_title: "com.digitalasset.canton.admin.health.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.admin.health.v30

> com.digitalasset.canton.admin.health.v30 的包级别概述。

<p class="x2mdx-ref-back"><a href="../index">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.admin.health.v30</h1>

  <p class="x2mdx-ref-summary">1 个服务、2 个端点、9 条消息、1 个枚举</p>

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
      <dd>9</dd>
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
      <h3>community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/status\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">最新发布的描述符快照中的当前源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>8</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/ status_service.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/status\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 状态服务

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>源文件</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/ status_service.proto">community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/status\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>操作</dt>
    <dd>2</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-admin-health-v30/statusservice/healthdump">
    <div class="x2mdx-ref-card-head">
      <h3>StatusService.HealthDump</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc StatusService.HealthDump(com.digitalasset.canton.admin.health.v30.HealthDumpRequest) 返回（流 com.digitalasset.canton.admin.health.v30.HealthDumpResponse）；</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.admin.health.v30.HealthDumpRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.admin.health.v30.HealthDumpResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>是</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="../operations/com-digitalasset-canton-admin-health-v30/statusservice/setloglevel">
    <div class="x2mdx-ref-card-head">
      <h3>StatusService.SetLogLevel</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc StatusService.SetLogLevel(com.digitalasset.canton.admin.health.v30.SetLogLevelRequest) 返回 (com.digitalasset.canton.admin.health.v30.SetLogLevelResponse);</p><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.admin.health.v30.SetLogLevelRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.admin.health.v30.SetLogLevelResponse</dd>
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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-componentstatus">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.ComponentStatus</h3>

    <p class="x2mdx-ref-schema-summary">5 个字段</p>
  </div>

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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-componentstatus-statusdata">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.ComponentStatus.StatusData</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">描述</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-healthdumprequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.HealthDumpRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">块\_size</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-healthdumpresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.HealthDumpResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">块</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-notinitialized">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.NotInitialized</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">活动</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-notinitialized-waitingforexternalinput">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.NotInitialized.WaitingForExternalInput</h3>

    <p class="x2mdx-ref-schema-summary">4 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>正在等待\_FOR\_EXTERNAL\_INPUT\_UNSPECIFIED</code></li>

    <li><code>正在等待\_FOR\_EXTERNAL\_INPUT\_ID</code></li>

    <li><code>等待\_FOR\_EXTERNAL\_INPUT\_NODE\_TOPOLOGY</code></li>

    <li><code>等待\_FOR\_EXTERNAL\_INPUT\_INITIALIZATION</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-setloglevelrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.SetLogLevelRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">级别</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-setloglevelresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.SetLogLevelResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-status">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.Status</h3>

    <p class="x2mdx-ref-schema-summary">7 个字段</p>
  </div>

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

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-admin-health-v30-topologyqueuestatus">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.admin.health.v30.TopologyQueueStatus</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">经理</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
