---
title: "/v2/users/{user-id}/identity-provider-id"
slug: "reference-json-api-reference-v2users-identity-provider-id"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2users-identity-provider-id.md"
source_title: "/v2/users/{user-id}/identity-provider-id"
tags:
  - reference
  - json-api-reference
  - v2users-identity-provider-id
---

# /v2/users/{user-id}/identity-provider-id

> 将用户的分配从一个 IDP 更新到另一个 IDP。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 补丁 /v2/users/{user-id}/identity-provider-id
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
  /v2/users/{user-id}/identity-provider-id:
    补丁：
      摘要：/v2/users/{user-id}/identity-provider-id
      描述：将用户的分配从一个 IDP 更新到另一个 IDP。
      操作Id：patchV2UsersUser-idIdentity-provider-id
      参数：
        - 名称：用户 ID
          在：路径
          必填：真实
          架构：
            类型：字符串
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/UpdateUserIdentityProviderIdRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/UpdateUserIdentityProviderIdResponse'
        “400”：
          描述：'无效值，无效值：正文'
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
    更新用户身份提供商Id请求：
      标题：更新用户身份提供商Id请求
      描述：'所需授权：``HasRight(参与方Admin)``'
      类型：对象
      需要：
        - 用户ID
      属性：
        用户ID：
          描述：|-
            要更新的用户

            必填
          类型：字符串
        源身份提供者 ID：
          描述：|-
            用户当前的身份提供商 ID
            如果省略，则采用默认 IDP

            可选
          类型：字符串
        目标身份提供者 ID：
          描述：|-
            用户的目标身份提供商 ID
            如果省略，则采用默认 IDP可选
          类型：字符串
    更新用户身份提供商Id响应：
      标题：UpdateUserIdentityProviderIdResponse
      类型：对象
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
