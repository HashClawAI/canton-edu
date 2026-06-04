---
title: "/v2/parties/participant-id"
slug: "reference-json-api-reference-v2partiesparticipant-id"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2partiesparticipant-id.md"
source_title: "/v2/parties/participant-id"
tags:
  - reference
  - json-api-reference
  - v2partiesparticipant-id
---

# /v2/parties/participant-id

> 返回参与者的标识符。
所有水平扩展的副本应返回相同的 id。
daml-on-kv-ledger：返回启动时在命令行上提供的标识符
canton：返回参与者的全球唯一标识符



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/parties/参与方-id
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
  /v2/partys/参与者 ID：
    得到：
      摘要：/v2/partys/参与方-id
      描述：>-
        返回参与者的标识符。

        所有水平扩展的副本应返回相同的 id。

        daml-on-kv-ledger：返回命令行上提供的标识符
        发射时间

        canton：返回参与者的全球唯一标识符
      操作 ID：getV2Parties参与方-id
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/Get参与方IdResponse'
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
    获取参与者 ID 响应：
      标题：获取参与者Id响应
      类型：对象
      需要：
        - 参与者ID
      属性：
        参与者ID:
          描述：|-
            参与者的标识符，应该是全局唯一的。
            必须是有效的 LedgerString（如“`value.proto`”中所述）。必填
          类型：字符串
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
