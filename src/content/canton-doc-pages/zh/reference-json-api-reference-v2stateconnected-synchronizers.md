---
title: "/v2/state/connected-synchronizers"
slug: "reference-json-api-reference-v2stateconnected-synchronizers"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateconnected-synchronizers.md"
source_title: "/v2/state/connected-synchronizers"
tags:
  - reference
  - json-api-reference
  - v2stateconnected-synchronizers
---

# /v2/state/connected-synchronizers

> 获取查询时已连接的同步器列表。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/state/connected-同步器s
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
    最新 Canton 3.4 补丁版本的规范。MINIMUM_CANTON_VERSION=3.5.0
服务器：[]
安全：[]
路径：
  /v2/state/connected-同步器s：
    得到：
      摘要：/v2/state/connected-同步器s
      描述：获取查询时已连接的同步器列表。
      操作 ID：getV2StateConnected-同步器s
      参数：
        - 名称：派对
          在：查询
          必填：假
          架构：
            类型：字符串
        - 名称：参与者 ID
          在：查询
          必填：假
          架构：
            类型：字符串
        - 名称：身份提供者 ID
          在：查询
          必填：假
          架构：
            类型：字符串
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetConnected同步器sResponse'
        “400”：
          描述：>-
            无效值，无效值：查询参数方，无效
            值：查询参数参与方Id，无效值：查询
            参数identityProviderId
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
    获取连接同步器响应：
      标题：GetConnected同步器sResponse
      类型：对象
      属性：
        连接的同步器：
          描述：'可选：可以为空'
          类型：数组
          项目：
            $ref: '#/components/schemas/Connected同步器'
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
    连接同步器：
      标题： 连接同步器
      类型：对象
      需要：
        - 同步器别名
        - 同步器ID
      属性：
        同步器别名：
          描述：|-
            同步器的别名必填
          类型：字符串
        同步器ID：
          描述：|-
            同步器ID

            必填
          类型：字符串
        许可：
          描述：|-
            同步器的权限
            如果请求中使用了一方，则设置，否则未指定。

            可选
          类型：字符串
          枚举：
            - PARTICIPANT_PERMISSION_UNSPECIFIED
            - PARTICIPANT_PERMISSION_SUBMISSION
            - PARTICIPANT_PERMISSION_CONFIRMATION
            - PARTICIPANT_PERMISSION_OBSERVATION
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
