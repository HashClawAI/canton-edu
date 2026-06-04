---
title: "v2.interactive"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive.md"
source_title: "v2.interactive"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive
---

# v2.interactive

> com.daml.ledger.api.v2.interactive 的包级概述。

<p class="x2mdx-ref-back"><a href="./details">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">v2.interactive</h1>

  <p class="x2mdx-ref-summary">1 个服务、6 个端点、29 条消息、1 个枚举</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>文件</dt>
      <dd>2</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>服务</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>端点</dt>
      <dd>6</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>消息</dt>
      <dd>29</dd>
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
      <h3>交互式\_submission\_common\_data.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">来自最新描述符快照的源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>2</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_submissio n_common_data.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_common\_data.proto</a></dd>
      </div>
    </dl>
  </div>

  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>交互式\_submission\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">来自最新描述符快照的源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>22</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>1</dd>
      </div><div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_subm ission_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## 交互式提交服务

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>源文件</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive_subm ission_service.proto">community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2/interactive/interactive\_submission\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>操作</dt>
    <dd>6</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmission">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmission</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmission(com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest) 返回 (com.daml.ledger.api.v2.interactive.ExecuteSubmissionResp...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmissionandwait">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmissionAndWait</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div><p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmissionAndWait(com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitRequest) 返回 (com.daml.ledger.api.v2.interactive.Execute...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmissionandwaitfortransaction">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.ExecuteSubmissionAndWaitForTransaction</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.ExecuteSubmissionAndWaitForTransaction(com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionRequest) 返回 (com.daml.ledge...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionAndWaitForTransactionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/getpreferredpackageversion">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.GetPreferredPackageVersion</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div><p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.GetPreferredPackageVersion(com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionRequest) 返回 (com.daml.ledger.api.v2.interactive.Get...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackageVersionResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/getpreferredpackages">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.GetPreferredPackages</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.GetPreferredPackages(com.daml.ledger.api.v2.interactive.GetPreferredPackagesRequest) 返回 (com.daml.ledger.api.v2.interactive.GetPreferredPac...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackagesRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.GetPreferredPackagesResponse</dd>
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

  <a class="x2mdx-ref-card" href="./com-daml-ledger-api-v2-interactive/interactivesubmissionservice/preparesubmission">
    <div class="x2mdx-ref-card-head">
      <h3>InteractiveSubmissionService.PrepareSubmission</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc InteractiveSubmissionService.PrepareSubmission(com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest) 返回 (com.daml.ledger.api.v2.interactive.PrepareSubmissionResp...</p><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.daml.ledger.api.v2.interactive.PrepareSubmissionResponse</dd>
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimation">
  <div class="x2mdx-ref-schema-head">
    <h3>成本估算</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">估计\_timestamp</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">确认\_请求\_流量\_成本\_估计</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">确认\_响应\_流量\_成本\_估计</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">总\_流量\_成本\_估计</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-costestimationhints">
  <div class="x2mdx-ref-schema-head">
    <h3>成本估算提示</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已禁用</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">预期\_签名</code>
        <span class="x2mdx-ref-type-badge">重复签名算法规范</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingalgorithmspec">
  <div class="x2mdx-ref-schema-head">
    <h3>签名算法规范</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>签名\_算法\_SPEC\_UNSPECIFIED</code></li>

    <li><code>签名\_算法\_SPEC\_ED25519</code></li>

    <li><code>签名\_算法\_SPEC\_EC\_DSA\_SHA\_256</code></li>

    <li><code>签名\_算法\_SPEC\_EC\_DSA\_SHA\_384</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction">
  <div class="x2mdx-ref-schema-head">
    <h3>Daml交易</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">版本</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">根</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点</code>
        <span class="x2mdx-ref-type-badge">重复节点</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_seeds</code>
        <span class="x2mdx-ref-type-badge">重复 NodeSeed</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-nodeseed">
  <div class="x2mdx-ref-schema-head">
    <h3>DamlTransaction.NodeSeed</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">种子</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-node">
  <div class="x2mdx-ref-schema-head">
    <h3>DamlTransaction.Node</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">v1</code>
        <span class="x2mdx-ref-type-badge">节点</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-node">
  <div class="x2mdx-ref-schema-head">
    <h3>节点</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 5 个字段</p>
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
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">单位</code>
        <span class="x2mdx-ref-type-badge">空</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">gen\_map</code>
        <span class="x2mdx-ref-type-badge">GenMap</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">标签</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">维护者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkey">
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-fetch">
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
    </div><div class="x2mdx-ref-field-row">
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
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签署者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
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
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-rollback">
  <div class="x2mdx-ref-schema-head">
    <h3>回滚</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive.transaction.v1 · 1 个字段</p>
  </div><div class="x2mdx-ref-fields">
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
    </div>

    <div class="x2mdx-ref-field-row">
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitfortransactionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交并等待事务请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 9 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已准备\_transaction</code>
        <span class="x2mdx-ref-type-badge">准备交易</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">当事人\_签名</code>
        <span class="x2mdx-ref-type-badge">派对签名</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_duration</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">提交\_id</code>
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
        <code class="x2mdx-ref-field-name">散列\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">哈希方案版本</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">交易\_format</code>
        <span class="x2mdx-ref-type-badge">交易格式</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparedtransaction">
  <div class="x2mdx-ref-schema-head">
    <h3>准备交易</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">交易</code>
        <span class="x2mdx-ref-type-badge">DamlTransaction</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">元数据</code>
        <span class="x2mdx-ref-type-badge">元数据</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata">
  <div class="x2mdx-ref-schema-head">
    <h3>元数据</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 10 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">提交者\_info</code>
        <span class="x2mdx-ref-type-badge">提交者信息</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">中介\_group</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">交易\_uuid</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">准备\_时间</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">输入\_合同</code>
        <span class="x2mdx-ref-type-badge">重复输入契约</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_ effective\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_ledger\_ effective\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_record\_time</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">全局\_key\_mapping</code>
        <span class="x2mdx-ref-type-badge">重复的 GlobalKeyMappingEntry</span>
      </div>
    </div>
  </div>
</div><div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-submitterinfo">
  <div class="x2mdx-ref-schema-head">
    <h3>元数据.SubmitterInfo</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">act\_as</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">命令\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-globalkeymappingentry">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata.GlobalKeyMappingEntry</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密钥</code>
        <span class="x2mdx-ref-type-badge">全局密钥</span>
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

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-inputcontract">
  <div class="x2mdx-ref-schema-head">
    <h3>Metadata.InputContract</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">v1</code>
        <span class="x2mdx-ref-type-badge">创建</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已创建\_at</code>
        <span class="x2mdx-ref-type-badge">uint64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">事件\_blob</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-partysignatures">
  <div class="x2mdx-ref-schema-head">
    <h3>当事人签名</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签名</code>
        <span class="x2mdx-ref-type-badge">重复的 SinglePartySignature</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-singlepartysignatures">
  <div class="x2mdx-ref-schema-head">
    <h3>单方签名</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">派对</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签名</code>
        <span class="x2mdx-ref-type-badge">重复签名</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signature">
  <div class="x2mdx-ref-schema-head">
    <h3>签名</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">格式</code>
        <span class="x2mdx-ref-type-badge">签名格式</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签名</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签名\_by</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">签名\_算法\_spec</code>
        <span class="x2mdx-ref-type-badge">签名算法规范</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signatureformat">
  <div class="x2mdx-ref-schema-head">
    <h3>签名格式</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 5 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>签名\_格式\_UNSPECIFIED</code></li>

    <li><code>SIGNATURE\_FORMAT\_RAW</code></li>

    <li><code>SIGNATURE\_FORMAT\_DER</code></li>

    <li><code>SIGNATURE\_FORMAT\_CONCAT</code></li><li><code>签名\_FORMAT\_SYMBOLIC</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-hashingschemeversion">
  <div class="x2mdx-ref-schema-head">
    <h3>哈希方案版本</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>哈希\_SCHEME\_VERSION\_UNSPECIFIED</code></li>

    <li><code>哈希\_SCHEME\_VERSION\_V2</code></li>

    <li><code>哈希\_SCHEME\_VERSION\_V3</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-minledgertime">
  <div class="x2mdx-ref-schema-head">
    <h3>最小账本时间</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time\_abs</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time\_rel</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionformat">
  <div class="x2mdx-ref-schema-head">
    <h3>交易格式</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">事件\_format</code>
        <span class="x2mdx-ref-type-badge">事件格式</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">交易\_shape</code>
        <span class="x2mdx-ref-type-badge">交易形状</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-eventformat">
  <div class="x2mdx-ref-schema-head">
    <h3>事件格式</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">过滤器\_by\_party</code>
        <span class="x2mdx-ref-type-badge">重复地图</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">过滤器\_for\_any\_party</code>
        <span class="x2mdx-ref-type-badge">过滤器</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">详细</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-filters">
  <div class="x2mdx-ref-schema-head">
    <h3>过滤器</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">累计</code>
        <span class="x2mdx-ref-type-badge">重复累积过滤器</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-cumulativefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>累积过滤器</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">通配符\_filter</code>
        <span class="x2mdx-ref-type-badge">通配符过滤器</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">接口\_filter</code>
        <span class="x2mdx-ref-type-badge">接口过滤器</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_filter</code>
        <span class="x2mdx-ref-type-badge">模板过滤器</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-wildcardfilter">
  <div class="x2mdx-ref-schema-head">
    <h3>通配符过滤器</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包含\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfacefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>接口过滤器</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">接口\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包含\_interface\_view</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包含\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-templatefilter">
  <div class="x2mdx-ref-schema-head">
    <h3>模板过滤器</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
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
        <code class="x2mdx-ref-field-name">包含\_created\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionshape">
  <div class="x2mdx-ref-schema-head">
    <h3>交易形状</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个值</p>
  </div>

  <ul class="x2mdx-ref-enum-list">
    <li><code>交易\_SHAPE\_UNSPECIFIED</code></li>

    <li><code>交易\_SHAPE\_ACS\_DELTA</code></li>

    <li><code>交易\_SHAPE\_LEDGER\_EFFECTS</code></li>
  </ul>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitfortransactionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交并等待事务响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">交易</code>
        <span class="x2mdx-ref-type-badge">交易</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transaction">
  <div class="x2mdx-ref-schema-head">
    <h3>交易</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 11 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">更新\_id</code>
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
        <code class="x2mdx-ref-field-name">工作流程\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">有效\_at</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">事件</code>
        <span class="x2mdx-ref-type-badge">重复事件</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">偏移量</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">trace\_context</code>
        <span class="x2mdx-ref-type-badge">TraceContext</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">记录\_时间</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">外部\_transaction\_hash</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">付费\_traffic\_cost</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-event">
  <div class="x2mdx-ref-schema-head">
    <h3>事件</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已创建</code>
        <span class="x2mdx-ref-type-badge">创建事件</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已存档</code>
        <span class="x2mdx-ref-type-badge">存档事件</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已行使</code>
        <span class="x2mdx-ref-type-badge">锻炼事件</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createdevent">
  <div class="x2mdx-ref-schema-head">
    <h3>创建事件</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 16 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">偏移量</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_key</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_key\_hash</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">创建\_arguments</code>
        <span class="x2mdx-ref-type-badge">记录</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已创建\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">界面\_views</code>
        <span class="x2mdx-ref-type-badge">重复的InterfaceView</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">见证\_当事人</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
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
        <code class="x2mdx-ref-field-name">观察者</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已创建\_at</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
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
        <code class="x2mdx-ref-field-name">acs\_delta</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">代表\_package\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfaceview">
  <div class="x2mdx-ref-schema-head">
    <h3>界面视图</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">接口\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">查看\_status</code>
        <span class="x2mdx-ref-type-badge">状态</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">视图\_值</code>
        <span class="x2mdx-ref-type-badge">记录</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">实现\_package\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-archivedevent">
  <div class="x2mdx-ref-schema-head">
    <h3>已存档事件</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 7 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">偏移量</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">见证\_当事人</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
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
        <code class="x2mdx-ref-field-name">已实现\_接口</code>
        <span class="x2mdx-ref-type-badge">重复标识符</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercishedevent">
  <div class="x2mdx-ref-schema-head">
    <h3>锻炼事件</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 15 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">偏移量</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">节点\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
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
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
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
        <code class="x2mdx-ref-field-name">选择</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_argument</code>
        <span class="x2mdx-ref-type-badge">值</span>
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
        <code class="x2mdx-ref-field-name">消费</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">见证\_当事人</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">last\_descendant\_node\_id</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">练习\_结果</code>
        <span class="x2mdx-ref-type-badge">值</span>
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
        <code class="x2mdx-ref-field-name">已实现\_接口</code>
        <span class="x2mdx-ref-type-badge">重复标识符</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">acs\_delta</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-tracecontext">
  <div class="x2mdx-ref-schema-head">
    <h3>跟踪上下文</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">traceparent</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">跟踪状态</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交和等待请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 8 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已准备\_transaction</code>
        <span class="x2mdx-ref-type-badge">准备交易</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">当事人\_签名</code>
        <span class="x2mdx-ref-type-badge">派对签名</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_duration</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">提交\_id</code>
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
        <code class="x2mdx-ref-field-name">散列\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">哈希方案版本</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionandwaitresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交并等待响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">更新\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">完成\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 8 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已准备\_transaction</code>
        <span class="x2mdx-ref-type-badge">准备交易</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">当事人\_签名</code>
        <span class="x2mdx-ref-type-badge">派对签名</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_duration</code>
        <span class="x2mdx-ref-type-badge">持续时间</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">重复数据删除\_offset</code>
        <span class="x2mdx-ref-type-badge">int64</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">提交\_id</code>
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
        <code class="x2mdx-ref-field-name">散列\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">哈希方案版本</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>执行提交响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackageversionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>获取首选包版本请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">各方</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
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
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">审核\_valid\_at</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackageversionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>获取首选包版本响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_首选项</code>
        <span class="x2mdx-ref-type-badge">PackagePreference</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-packagepreference">
  <div class="x2mdx-ref-schema-head">
    <h3>包首选项</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_reference</code>
        <span class="x2mdx-ref-type-badge">软件包参考</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-packagereference">
  <div class="x2mdx-ref-schema-head">
    <h3>封装参考</h3>

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
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_版本</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackagesrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>获取首选包请求</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">package\_vetting\_requirements</code>
        <span class="x2mdx-ref-type-badge">重复 PackageVettingRequirement</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">审核\_valid\_at</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-packagevettingrequirement">
  <div class="x2mdx-ref-schema-head">
    <h3>PackageVettingRequirement</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">各方</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_name</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-getpreferredpackagesresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>获取首选包响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_引用</code>
        <span class="x2mdx-ref-type-badge">重复的PackageReference</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>准备提交请求</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 15 个字段</p>
  </div><div class="x2mdx-ref-fields">
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
        <code class="x2mdx-ref-field-name">命令</code>
        <span class="x2mdx-ref-type-badge">重复命令</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">min\_ledger\_time</code>
        <span class="x2mdx-ref-type-badge">MinLedgerTime</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">max\_record\_time</code>
        <span class="x2mdx-ref-type-badge">时间戳</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">act\_as</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">读取\_as</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">披露\_合同</code>
        <span class="x2mdx-ref-type-badge">重复披露合同</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包\_id\_selection\_preference</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">详细\_散列</code>
        <span class="x2mdx-ref-type-badge">布尔</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">预取\_contract\_keys</code>
        <span class="x2mdx-ref-type-badge">重复 PrefetchContractKey</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">估计\_traffic\_cost</code>
        <span class="x2mdx-ref-type-badge">成本估算提示</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">散列\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">哈希方案版本</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">水龙头\_max\_passes</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-command">
  <div class="x2mdx-ref-schema-head">
    <h3>命令</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">创建</code>
        <span class="x2mdx-ref-type-badge">创建命令</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">练习</code>
        <span class="x2mdx-ref-type-badge">锻炼命令</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">练习\_by\_key</code>
        <span class="x2mdx-ref-type-badge">ExerciseByKeyCommand</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">创建\_和\_练习</code>
        <span class="x2mdx-ref-type-badge">CreateAndExerciseCommand</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createcommand">
  <div class="x2mdx-ref-schema-head">
    <h3>创建命令</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">创建\_arguments</code>
        <span class="x2mdx-ref-type-badge">记录</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisecommand">
  <div class="x2mdx-ref-schema-head">
    <h3>练习命令</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
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
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_argument</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercisebykeycommand">
  <div class="x2mdx-ref-schema-head">
    <h3>通过按键命令练习</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
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
        <code class="x2mdx-ref-field-name">合约\_key</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_argument</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createandexercisecommand">
  <div class="x2mdx-ref-schema-head">
    <h3>CreateAndExerciseCommand</h3><p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
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
        <code class="x2mdx-ref-field-name">创建\_arguments</code>
        <span class="x2mdx-ref-type-badge">记录</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">选择\_argument</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-disclosurecontract">
  <div class="x2mdx-ref-schema-head">
    <h3>披露合同</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 4 个字段</p>
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
        <code class="x2mdx-ref-field-name">合约\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已创建\_event\_blob</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">同步器\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-prefetchcontractkey">
  <div class="x2mdx-ref-schema-head">
    <h3>预取合约密钥</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2 · 3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">模板\_id</code>
        <span class="x2mdx-ref-type-badge">标识符</span>
      </div>
    </div><div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">合约\_key</code>
        <span class="x2mdx-ref-type-badge">值</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">限制</code>
        <span class="x2mdx-ref-type-badge">uint32</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparesubmissionresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>准备提交响应</h3>

    <p class="x2mdx-ref-schema-summary">com.daml.ledger.api.v2.interactive · 5 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">已准备\_transaction</code>
        <span class="x2mdx-ref-type-badge">准备交易</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">准备\_transaction\_hash</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">散列\_scheme\_version</code>
        <span class="x2mdx-ref-type-badge">哈希方案版本</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">散列\_details</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">成本\_估计</code>
        <span class="x2mdx-ref-type-badge">成本估算</span>
      </div>
    </div>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
