---
title: "/v2/idps/{idp-id}"
slug: "reference-json-api-reference-v2idps"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2idps.md"
source_title: "/v2/idps/{idp-id}"
tags:
  - reference
  - json-api-reference
  - v2idps
---

# /v2/idps/{idp-id}

> 更新所描述的身份提供者配置资源的选定可修改属性
通过``IdentityProviderConfig``消息。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 补丁 /v2/idps/{idp-id}
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
  /v2/idps/{idp-id}：
    补丁：
      摘要：/v2/idps/{idp-id}
      描述：>-
        更新身份提供者配置的选定可修改属性
        资源描述

        通过``IdentityProviderConfig``消息。
      操作Id：patchV2IdpsIdp-id
      参数：
        - 名称：idp-id
          在：路径
          必填：真实
          架构：
            类型：字符串
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/UpdateIdentityProviderConfigRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/UpdateIdentityProviderConfigResponse'
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
    更新IdentityProviderConfig请求：
      标题：UpdateIdentityProviderConfigRequest
      类型：对象
      需要：
        - 身份提供者配置
        - 更新掩码
      属性：
        身份提供者配置：
          $ref: '#/components/schemas/IdentityProviderConfig'
          描述：|-
            要更新的身份提供商配置。
            可修改

            必填
        更新掩码：
          $ref: '#/components/schemas/FieldMask'
          描述：>-
            更新掩码指定更新的方式和属性
            ``IdentityProviderConfig``消息待更新。

            更新掩码由一组更新路径组成。有效的更新路径指向相对于
            ``IdentityProviderConfig``消息。

            有效的更新掩码必须：


            1. 包含至少一个更新路径，

            2. 仅包含有效的更新路径。


            可更新的字段标记为“`Modifiable`”。

            有关更多信息，请参阅标准文档
            protobuf3 的 ``google.protobuf.FieldMask``。


            必填
    更新IdentityProviderConfig响应：
      标题：UpdateIdentityProviderConfigResponse
      类型：对象
      需要：
        - 身份提供者配置
      属性：
        身份提供者配置：
          $ref: '#/components/schemas/IdentityProviderConfig'
          描述：|-
            更新了身份提供商配置

            必填
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
    身份提供者配置：
      标题：IdentityProviderConfig
      类型：对象
      需要：
        - 身份提供者ID
        - 发行人
        -jwksUrl
      属性：
        身份提供者 ID：
          描述：|-
            身份提供商标识符
            必须是有效的 LedgerString（如“`value.proto`”中所述）。

            必填
          类型：字符串
        已停用：
          描述：>-
            设置后，调用者使用此身份颁发的 JWT 令牌
            提供商被拒绝所有访问

            到账本 API。

            可修改


            可选
          类型：布尔值
        发行人：
          描述：>-
            指定 JWT 令牌的颁发者。

            颁发者值是一个区分大小写的 URL，使用 https 方案
            包含方案、主机、

            以及可选的端口号和路径组件，并且没有查询或
            片段组件。

            可修改


            在`UpdateIdentityProviderConfigRequest`使用时可以留空
            如果发行人没有更新。必填
          类型：字符串
        jwks网址：
          描述：>-
            JWKS（JSON Web 密钥集）URL。

            Ledger API 使用提供的 URL 中的 JWK（JSON Web 密钥）来
            验证 JWT 是否已

            与加载的 JWK 签名。仅 RS256（带有 SHA-256 的 RSA 签名）
            支持签名算法。

            可修改


            必填
          类型：字符串
        观众：
          描述：>-
            指定 JWT 令牌的受众。

            设置后，调用者使用此身份颁发的 JWT 令牌
            允许提供商获得访问权限

            仅当“aud”声明包含此处指定的字符串时

            可修改


            可选
          类型：字符串
    字段掩码：
      标题： 场掩模
      类型：对象
      需要：
        - 未知字段
      属性：
        路径：
          类型：数组
          项目：
            类型：字符串
        未知字段：
          $ref: '#/components/schemas/UnknownFieldSet'
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
    未知字段集：
      标题：未知字段集
      类型：对象
      需要：
        - 字段
      属性：
        字段：
          $ref: '#/components/schemas/Map_Int_Field'
    地图内部字段：
      标题：Map_Int_Field
      类型：对象
      附加属性：
        $ref: '#/components/schemas/Field'
    领域：
      标题： 田野
      类型：对象
      属性：
        变体：
          类型：数组
          项目：
            类型：整数
            格式：int64
        固定64：
          类型：数组
          项目：
            类型：整数
            格式：int64
        固定32：
          类型：数组
          项目：
            类型：整数
            格式：int32
        长度分隔：
          类型：数组
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
