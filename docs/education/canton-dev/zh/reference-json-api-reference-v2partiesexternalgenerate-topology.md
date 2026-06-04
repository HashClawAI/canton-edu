---
title: "/v2/parties/external/generate-topology"
slug: "reference-json-api-reference-v2partiesexternalgenerate-topology"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2partiesexternalgenerate-topology.md"
source_title: "/v2/parties/external/generate-topology"
tags:
  - reference
  - json-api-reference
  - v2partiesexternalgenerate-topology
---

# /v2/parties/external/generate-topology

> Alpha 3.3：为外部签名生成拓扑交易的便捷端点

预计3.5稳定

您可以使用此端点生成公共外部拓扑事务
可以在外部签名并作为分配方流程的一部分上传

请注意，此请求将使用相同的密钥创建一个普通的命名空间
身份作为签名。更复杂的方案，例如多重签名
或去中心化各方要求您自己构建拓扑交易。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/parties/external/generate-topology
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
  /v2/partys/external/generate-topology：
    帖子：
      摘要：/v2/partys/external/generate-topology
      描述：>-
        Alpha 3.3：生成拓扑事务的便捷端点
        外部签约


        预计3.5稳定


        您可以使用此端点生成公共外部拓扑
        交易

        可以在外部签名并作为分配的一部分上传
        聚会过程


        请注意，此请求将使用相同的密钥创建一个普通的命名空间
        为

        身份作为签名。更复杂的方案，例如多重签名或去中心化各方要求您构建拓扑
        自己交易。
      操作 ID：postV2PartiesExternalGenerate-topology
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/GenerateExternalPartyTopologyRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GenerateExternalPartyTopologyResponse'
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
    生成ExternalPartyTopology请求：
      标题：GenerateExternalPartyTopologyRequest
      类型：对象
      需要：
        - 同步器
        - 派对提示
        - 公钥
      属性：
        同步器：
          描述：|-
            我们正在为其构建此请求的 同步器-id。
            TODO(#27670) 支持同步器别名

            必填
          类型：字符串
        聚会提示：
          描述：>-
            实际的派对 ID 将根据此提示和一个
            公钥的指纹


            必填
          类型：字符串
        公钥：
          $ref: '#/components/schemas/SigningPublicKey'
          描述：|-
            公钥

            必填
        local参与方ObservationOnly：
          描述：>-
            如果为真，那么本地参与者只会观察，而不是
            确认。默认为 false。


            可选
          类型：布尔值
        其他Confirming参与方Uids：
          描述：|-
            该方应确认的其他参与者 ID

            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        确认阈值：
          描述：>-
            该方的确认阈值 >= 1。默认为所有可用的
            确认者（或者如果设置为 0）。


            可选
          类型：整数
          格式：int32
        观察参与方Uids：
          描述：|-
            该聚会的其他观察参与者 ID可选：可以为空
          类型：数组
          项目：
            类型：字符串
    生成ExternalPartyTopology响应：
      标题：GenerateExternalPartyTopologyResponse
      描述：>-
        带有拓扑事务和多重哈希的响应消息
        签署了。
      类型：对象
      需要：
        - 派对ID
        - 公钥指纹
        - 多哈希
        - 拓扑交易
      属性：
        派对 ID:
          描述：|-
            生成的当事人id

            必填
          类型：字符串
        公钥指纹：
          描述：|-
            提供的公钥的指纹

            必填
          类型：字符串
        拓扑事务：
          描述：>-
            需要签名的序列化拓扑交易
            作为分配方流程的一部分提交

            请注意，序列化包括版本控制信息。
            因此，这里的交易是序列化的

            作为 `UntypedVersionedMessage` ，它又包含
            版本中连载`TopologyTransaction`

            由同步器支持。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        多重哈希：
          描述：>-
            可以代替每个单独签名的多重哈希
            交易


            必填：必须非空
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
    签名公钥：
      标题：签名公钥
      类型：对象
      需要：
        - 格式
        - 关键数据
        - 关键规格
      属性：
        格式：
          描述：|-
            公钥的序列化格式

            必填
          示例：CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO
          类型：字符串
        关键数据：
          描述：|-
            采用上述格式的序列化公钥必填：必须非空
          类型：字符串
        关键规格：
          描述：|-
            关键规格

            必填
          示例：SIGNING_KEY_SPEC_EC_CURVE25519
          类型：字符串
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
