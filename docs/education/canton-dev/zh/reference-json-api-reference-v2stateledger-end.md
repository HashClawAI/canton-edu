---
title: "/v2/state/ledger-end"
slug: "reference-json-api-reference-v2stateledger-end"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateledger-end.md"
source_title: "/v2/state/ledger-end"
tags:
  - reference
  - json-api-reference
  - v2stateledger-end
---

# /v2/state/ledger-end

> 获取当前账本结束。
以返回的偏移量开始的订阅将在调用此 RPC 后为事件提供服务。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/state/ledger-end
开放API：3.0.3
信息：
  标题：JSON Ledger API HTTP 端点
  版本：3.5.0-SNAPSHOT
  描述：>-
    此规范版本修复了某些 API 不一致的地方
    规范中标记为必填的字段实际上是可选的。

    如果您使用基于此文件的代码生成工具，您可能需要调整
    现有的应用程序代码来处理这些字段作为可选。

    如果您不想更改客户端代码，请继续使用 OpenAPI
    最新 Canton 3.4 补丁版本的规范。

    MINIMUM_CANTON_VERSION=3.5.0
服务器：[]
安全：[]
路径：
  /v2/state/ledger-end：
    得到：
      摘要：/v2/state/ledger-end
      描述：>-
        获取当前账本结束。

        以返回的偏移量开始的订阅将在之后提供事件
        这个 RPC 被调用了。
      操作Id：getV2StateLedger-end
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetLedgerEndResponse'
        “400”：
          描述：无效值
          内容：
            文本/纯文本：
              架构：
                类型：字符串
        默认：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsCantonError'
      安全：
        - httpAuth: []
        - apiKeyAuth: []
组件：
  模式：
    获取账本结束响应：
      标题：获取LedgerEndResponse
      类型：对象
      属性：
        偏移量：
          描述：>-
            它始终是一个非负整数。

            如果为零，则分类账的参与者视图为空。

            如果为正，则为分类账的绝对偏移量
            参与者。可选
          类型：整数
          格式：int64
    JsCanton错误：
      标题： JsCantonError
      类型：对象
      需要：
        - 代码
        - 原因
        - 上下文
        - 错误类别
      属性：
        代码：
          类型：字符串
        原因：
          类型：字符串
        相关性ID：
          类型：字符串
        跟踪ID：
          类型：字符串
        上下文：
          $ref: '#/components/schemas/Map_String'
        资源：
          类型：数组
          项目：
            $ref: '#/components/schemas/Tuple2_String_String'
        错误类别：
          类型：整数
          格式：int32
        grpc代码值：
          类型：整数
          格式：int32
        重试信息：
          类型：字符串
        明确答案：
          类型：布尔值
    地图字符串：
      标题：Map_String
      类型：对象
      附加属性：
        类型：字符串
    Tuple2_String_String：
      标题：Tuple2_String_String
      类型：数组
      最大物品数：2
      最少项目：2
      项目：
        类型：字符串
  安全方案：
    http验证：
      类型：http
      描述：Ledger API 标准 JWT 令牌
      方案：承载
    apiKeyAuth:
      类型：apiKey
      描述：Ledger API 标准 JWT 令牌（websocket）
      名称：Sec-WebSocket-协议
      在：标题

````

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
