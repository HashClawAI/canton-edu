---
title: "ExecuteSubmission"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive-interactivesubmissionservice-executesubmission"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2-interactive/interactivesubmissionservice/executesubmission.md"
source_title: "ExecuteSubmission"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2-interactive
  - interactivesubmissionservice
---

# ExecuteSubmission

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>账本API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-interactive">v2.interactive</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>执行提交</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2.interactive</p>

      <h1 class="x2mdx-ref-title">执行提交</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/ExecuteSubmission</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>交互式提交服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>执行提交</dd>
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
        <h3>执行提交请求</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

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
      </div>
    </div>

    ## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>执行提交响应</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.interactive.ExecuteSubmissionResponse</dd>
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

    ## 相关模式<手风琴组>
      <手风琴标题=“com.daml.ledger.api.v2.interactive.ExecuteSubmissionRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionrequest">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.interactive.PreparedTransaction”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-preparedtransaction">
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
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.DamlTransaction”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.DamlTransaction.NodeSeed”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-nodeseed">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">节点\_id</code>
                <span class="x2mdx-ref-type-badge">int32</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">种子</code>
                <span class="x2mdx-ref-type-badge">字节</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.DamlTransaction.Node”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-damltransaction-node">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.Node”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-node">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.Create”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-create">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.Identifier”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-identifier">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Value”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-value">
          <div class="x2mdx-ref-fields">
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
            </div><div class="x2mdx-ref-field-row">
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
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">枚举</code>
                <span class="x2mdx-ref-type-badge">枚举</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Optional”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-可选">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">值</code>
                <span class="x2mdx-ref-type-badge">值</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.List”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-list">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">元素</code>
                <span class="x2mdx-ref-type-badge">重复值</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TextMap”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">条目</code>
                <span class="x2mdx-ref-type-badge">重复条目</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TextMap.Entry”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-textmap-entry">
          <div class="x2mdx-ref-fields">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.GenMap”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">条目</code>
                <span class="x2mdx-ref-type-badge">重复条目</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.GenMap.Entry”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-genmap-entry">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Record”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-record">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.RecordField”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-recordfield">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Variant”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-variant">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Enum”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-enum">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.GlobalKeyWithMaintainers”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkeywithmaintainers">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.GlobalKey”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-globalkey">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.Fetch”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-fetch">
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
            </div><div class="x2mdx-ref-field-row">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.Exercise”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-exercise">
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
            </div><div class="x2mdx-ref-field-row">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.Rollback”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-rollback">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">孩子</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.transaction.v1.QueryByKey”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-transaction-v1-querybykey">
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
            </div><div class="x2mdx-ref-field-row">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.Metadata”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata">
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
            </div><div class="x2mdx-ref-field-row">
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
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.Metadata.SubmitterInfo”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-submitterinfo">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.Metadata.GlobalKeyMappingEntry”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-globalkeymappingentry">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">密钥</code>
                <span class="x2mdx-ref-type-badge">全局密钥</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">值</code>
                <span class="x2mdx-ref-type-badge">值</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.Metadata.InputContract”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-metadata-inputcontract">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.PartySignatures”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-partysignatures">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">签名</code>
                <span class="x2mdx-ref-type-badge">重复的 SinglePartySignature</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.SinglePartySignatures”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-singlepartysignatures">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.Signature”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signature">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.SignatureFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signatureformat">
          <ul class="x2mdx-ref-enum-list">
            <li><code>签名\_格式\_UNSPECIFIED</code></li>

            <li><code>SIGNATURE\_FORMAT\_RAW</code></li>

            <li><code>SIGNATURE\_FORMAT\_DER</code></li>

            <li><code>SIGNATURE\_FORMAT\_CONCAT</code></li>

            <li><code>签名\_FORMAT\_SYMBOLIC</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.SigningAlgorithmSpec”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-signingalgorithmspec">
          <ul class="x2mdx-ref-enum-list">
            <li><code>签名\_算法\_SPEC\_UNSPECIFIED</code></li>

            <li><code>签名\_算法\_SPEC\_ED25519</code></li>

            <li><code>签名\_算法\_SPEC\_EC\_DSA\_SHA\_256</code></li>

            <li><code>签名\_算法\_SPEC\_EC\_DSA\_SHA\_384</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.HashingSchemeVersion”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-hashingschemeversion">
          <ul class="x2mdx-ref-enum-list">
            <li><code>哈希\_SCHEME\_VERSION\_UNSPECIFIED</code></li><li><code>哈希\_SCHEME\_VERSION\_V2</code></li>

            <li><code>哈希\_SCHEME\_VERSION\_V3</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.MinLedgerTime”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-minledgertime">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.interactive.ExecuteSubmissionResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interactive-executesubmissionresponse" />
      </手风琴>
    </手风琴组>
  </div>

  <div className="x2mdx-ref-right-rail" role="complementary" aria-label="示例和响应">
    <div className="x2mdx-ref-rail-panel">
      <div className="x2mdx-ref-rail-code">
        <div className="x2mdx-ref-rail-head">
          <span className="x2mdx-ref-rail-heading">grpcurl</span>
        </div>```bash grpcurl theme={"theme":{"light":"github-light","dark":"github-dark"}}
        # Add -plaintext if the server is not using TLS.
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/ExecuteSubmission <<'EOF'
        {
          "preparedTransaction": {
            "transaction": {
              "version": "string",
              "roots": [
                "string"
              ],
              "nodes": [
                {
                  "nodeId": "string",
                  "v1": {}
                }
              ],
              "nodeSeeds": [
                {
                  "nodeId": 0,
                  "seed": "BASE64_ENCODED_BYTES"
                }
              ]
            },
            "metadata": {
              "submitterInfo": {
                "actAs": [
                  "string"
                ],
                "commandId": "string"
              },
              "同步器Id": "string",
              "mediatorGroup": 0,
              "transactionUuid": "string",
              "preparationTime": "0",
              "inputContracts": [
                {
                  "v1": {},
                  "createdAt": "0",
                  "eventBlob": "BASE64_ENCODED_BYTES"
                }
              ],
              "minLedgerEffectiveTime": "0",
              "maxLedgerEffectiveTime": "0"
            }
          },
          "partySignatures": {
            "signatures": [
              {
                "party": "string",
                "signatures": [
                  {
                    "format": "SIGNATURE_FORMAT_UNSPECIFIED",
                    "signature": "BASE64_ENCODED_BYTES",
                    "signedBy": "string",
                    "signingAlgorithmSpec": "SIGNING_ALGORITHM_SPEC_UNSPECIFIED"
                  }
                ]
              }
            ]
          },
          "deduplicationDuration": "string",
          "submissionId": "string",
          "userId": "string",
          "hashingSchemeVersion": "HASHING_SCHEME_VERSION_UNSPECIFIED",
          "minLedgerTime": {
            "minLedgerTimeAbs": "string"
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
