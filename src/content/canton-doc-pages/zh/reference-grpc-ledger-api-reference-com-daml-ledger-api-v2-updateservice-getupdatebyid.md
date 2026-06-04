---
title: "GetUpdateById"
slug: "reference-grpc-ledger-api-reference-com-daml-ledger-api-v2-updateservice-getupdatebyid"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2/updateservice/getupdatebyid.md"
source_title: "GetUpdateById"
tags:
  - reference
  - grpc-ledger-api-reference
  - com-daml-ledger-api-v2
  - updateservice
---

# GetUpdateById

<div class="x2mdx-ref-page x2mdx-ref-page--操作" />

<div className="x2mdx-ref-operation-shell">
  <div className="x2mdx-ref-operation-main">
    <div class="x2mdx-ref-breadcrumbs" role="navigation" aria-label="Breadcrumb">
      <span>账本API</span>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-details">gRPC API</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <a href="/zh/docs/canton/reference-grpc-ledger-api-reference-com-daml-ledger-api-v2">v2</a>

      <span class="x2mdx-ref-breadcrumb-separator">›</span>

      <span>获取UpdateById</span>
    </div>

    <div class="x2mdx-ref-hero">
      <p class="x2mdx-ref-eyebrow">com.daml.ledger.api.v2</p>

      <h1 class="x2mdx-ref-title">GetUpdateById</h1>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.4 起</span>
      </div>
    </div>

    <div class="x2mdx-ref-operation-bar">
      <span class="x2mdx-ref-operation-method x2mdx-ref-operation-method--rpc">RPC</span>

      <code>/com.daml.ledger.api.v2.UpdateService/GetUpdateById</code>
    </div>

    ## 协议详细信息

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>协议</dt>
        <dd>gRPC</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>更新服务</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>RPC</dt>
        <dd>获取UpdateById</dd>
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
        <h3>GetUpdateByIdRequest</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.GetUpdateByIdRequest</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>客户端流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">更新\_id</code>
            <span class="x2mdx-ref-type-badge">字符串</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">更新\_格式</code>
            <span class="x2mdx-ref-type-badge">更新格式</span>
          </div>
        </div>
      </div>
    </div>## 输出

    <div class="x2mdx-ref-panel">
      <div class="x2mdx-ref-panel-head">
        <h3>获取更新响应</h3>
      </div>

      <dl class="x2mdx-ref-meta-grid">
        <div class="x2mdx-ref-meta-item">
          <dt>消息</dt>
          <dd>com.daml.ledger.api.v2.GetUpdateResponse</dd>
        </div>

        <div class="x2mdx-ref-meta-item">
          <dt>服务器流</dt>
          <dd>否</dd>
        </div>
      </dl>

      <div class="x2mdx-ref-fields">
        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">交易</code>
            <span class="x2mdx-ref-type-badge">交易</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">重新分配</code>
            <span class="x2mdx-ref-type-badge">重新分配</span>
          </div>
        </div>

        <div class="x2mdx-ref-field-row">
          <div class="x2mdx-ref-field-main">
            <code class="x2mdx-ref-field-name">拓扑\_transaction</code>
            <span class="x2mdx-ref-type-badge">拓扑事务</span>
          </div>
        </div>
      </div>
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
      <手风琴标题=“com.daml.ledger.api.v2.GetUpdateByIdRequest”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-getupdatebyidrequest">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">更新\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">更新\_格式</code>
                <span class="x2mdx-ref-type-badge">更新格式</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.UpdateFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-updateformat">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">include\_transactions</code>
                <span class="x2mdx-ref-type-badge">交易格式</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包括\_重新分配</code>
                <span class="x2mdx-ref-type-badge">事件格式</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包括\_topology\_events</code>
                <span class="x2mdx-ref-type-badge">拓扑格式</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TransactionFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionformat">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.EventFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-eventformat">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">过滤器\_by\_party</code>
                <span class="x2mdx-ref-type-badge">重复地图</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">过滤器\_for\_any\_party</code>
                <span class="x2mdx-ref-type-badge">过滤器</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">详细</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Filters”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-filters">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">累计</code>
                <span class="x2mdx-ref-type-badge">重复累积过滤器</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.CumulativeFilter”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-cumulativefilter">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.WildcardFilter”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-wildcardfilter">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包含\_created\_event\_blob</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.InterfaceFilter”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfacefilter">
          <div class="x2mdx-ref-fields">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Identifier”>
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

      <手风琴标题=“com.daml.ledger.api.v2.TemplateFilter”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-templatefilter">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">模板\_id</code>
                <span class="x2mdx-ref-type-badge">标识符</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包含\_created\_event\_blob</code>
                <span class="x2mdx-ref-type-badge">布尔</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TransactionShape”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transactionshape">
          <ul class="x2mdx-ref-enum-list">
            <li><code>交易\_SHAPE\_UNSPECIFIED</code></li>

            <li><code>交易\_SHAPE\_ACS\_DELTA</code></li>

            <li><code>交易\_SHAPE\_LEDGER\_EFFECTS</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TopologyFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-topologyformat">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">包括\_参与方\_authorization\_events</code>
                <span class="x2mdx-ref-type-badge">参与者授权拓扑格式</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.参与方AuthorizationTopologyFormat”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方authorizationtopologyformat">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">各方</code>
                <span class="x2mdx-ref-type-badge">重复字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.GetUpdateResponse”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-getupdateresponse">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">交易</code>
                <span class="x2mdx-ref-type-badge">交易</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配</code>
                <span class="x2mdx-ref-type-badge">重新分配</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">拓扑\_transaction</code>
                <span class="x2mdx-ref-type-badge">拓扑事务</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Transaction”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-transaction">
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
            </div><div class="x2mdx-ref-field-row">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.Event”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-event">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.CreatedEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-createdevent">
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
            </div><div class="x2mdx-ref-field-row">
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
            </div>

            <div class="x2mdx-ref-field-row">
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
            </div><div class="x2mdx-ref-field-row">
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

      <手风琴标题=“com.daml.ledger.api.v2.InterfaceView”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-interfaceview">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ArchivedEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-archivedevent">
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
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">已实现\_接口</code>
                <span class="x2mdx-ref-type-badge">重复标识符</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.ExercisedEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-exercishedevent">
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
            </div><div class="x2mdx-ref-field-row">
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
            </div>

            <div class="x2mdx-ref-field-row">
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
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TraceContext”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-tracecontext">
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.Reassignment”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignment">
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
                <code class="x2mdx-ref-field-name">偏移量</code>
                <span class="x2mdx-ref-type-badge">int64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">事件</code>
                <span class="x2mdx-ref-type-badge">重复重新分配事件</span>
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
                <code class="x2mdx-ref-field-name">同步器\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
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
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.ReassignmentEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-reassignmentevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">未分配</code>
                <span class="x2mdx-ref-type-badge">未分配事件</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">已分配</code>
                <span class="x2mdx-ref-type-badge">分配事件</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.UnassignedEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-unassignedevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_id</code>
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
                <code class="x2mdx-ref-field-name">模板\_id</code>
                <span class="x2mdx-ref-type-badge">标识符</span>
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

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提交者</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_counter</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">分配\_排他性</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
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
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.AssignedEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-assignedevent">
          <div class="x2mdx-ref-fields">
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

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div><div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">提交者</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">重新分配\_counter</code>
                <span class="x2mdx-ref-type-badge">uint64</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">已创建\_event</code>
                <span class="x2mdx-ref-type-badge">创建事件</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.TopologyTransaction”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-topologytransaction">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">更新\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
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
                <code class="x2mdx-ref-field-name">记录\_时间</code>
                <span class="x2mdx-ref-type-badge">时间戳</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">事件</code>
                <span class="x2mdx-ref-type-badge">重复拓扑事件</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">trace\_context</code>
                <span class="x2mdx-ref-type-badge">TraceContext</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.TopologyEvent”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-topologyevent">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_authorization\_changed</code>
                <span class="x2mdx-ref-type-badge">参与者授权更改</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_authorization\_revoked</code>
                <span class="x2mdx-ref-type-badge">参与者授权已撤销</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_授权\_添加</code>
                <span class="x2mdx-ref-type-badge">已添加参与者授权</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_authorization\_onboarding</code>
                <span class="x2mdx-ref-type-badge">参与者授权加入</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.参与方AuthorizationChanged”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方authorizationchanged">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_权限</code>
                <span class="x2mdx-ref-type-badge">参与者权限</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.参与方Permission”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方permission">
          <ul class="x2mdx-ref-enum-list">
            <li><code>参与者\_PERMISSION\_UNSPECIFIED</code></li>

            <li><code>参与者\_PERMISSION\_SUBMISSION</code></li>

            <li><code>参与者\_PERMISSION\_CONFIRMATION</code></li>

            <li><code>参与者\_PERMISSION\_OBSERVATION</code></li>
          </ul>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.参与方AuthorizationRevoked”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方authorizationrevoked">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴>

      <手风琴标题=“com.daml.ledger.api.v2.参与方AuthorizationAdded”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方authorizationadd">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_权限</code>
                <span class="x2mdx-ref-type-badge">参与者权限</span>
              </div>
            </div>
          </div>
        </div>
      </手风琴><手风琴标题=“com.daml.ledger.api.v2.参与方AuthorizationOnboarding”>
        <div class="x2mdx-ref-schema" id="schema-com-daml-ledger-api-v2-参与方authorizationonboarding">
          <div class="x2mdx-ref-fields">
            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">party\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_id</code>
                <span class="x2mdx-ref-type-badge">字符串</span>
              </div>
            </div>

            <div class="x2mdx-ref-field-row">
              <div class="x2mdx-ref-field-main">
                <code class="x2mdx-ref-field-name">参与者\_权限</code>
                <span class="x2mdx-ref-type-badge">参与者权限</span>
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
          <span className="x2mdx-ref-rail-heading">grpcurl</span>
        </div>```bash grpcurl theme={"theme":{"light":"github-light","dark":"github-dark"}}
        # Add -plaintext if the server is not using TLS.
        grpcurl \
          -d @ \
          <HOST:PORT> \
          com.daml.ledger.api.v2.UpdateService/GetUpdateById <<'EOF'
        {
          "updateId": "string",
          "updateFormat": {
            "includeTransactions": {
              "eventFormat": {
                "filtersByParty": [
                  {
                    "key": {}
                  }
                ],
                "filtersForAnyParty": {},
                "verbose": true
              },
              "transactionShape": "TRANSACTION_SHAPE_UNSPECIFIED"
            },
            "includeReassignments": {
              "filtersByParty": [
                {
                  "key": {
                    "cumulative": [
                      {}
                    ]
                  }
                }
              ],
              "filtersForAnyParty": {
                "cumulative": [
                  {}
                ]
              },
              "verbose": true
            },
            "includeTopologyEvents": {
              "include参与方AuthorizationEvents": {
                "parties": [
                  "string"
                ]
              }
            }
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
        {
          "transaction": {
            "updateId": "string",
            "commandId": "string",
            "workflowId": "string",
            "effectiveAt": "string",
            "events": [
              {
                "created": {
                  "offset": "0",
                  "nodeId": 0,
                  "contractId": "string",
                  "templateId": {},
                  "contractKey": {},
                  "contractKeyHash": "BASE64_ENCODED_BYTES",
                  "createArguments": {},
                  "createdEventBlob": "BASE64_ENCODED_BYTES"
                }
              }
            ],
            "offset": "0",
            "同步器Id": "string",
            "traceContext": {
              "traceparent": "string",
              "tracestate": "string"
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
