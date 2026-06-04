---
title: "/v2/parties/external/allocate"
slug: "reference-json-api-reference-v2partiesexternalallocate"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2partiesexternalallocate.md"
source_title: "/v2/parties/external/allocate"
tags:
  - reference
  - json-api-reference
  - v2partiesexternalallocate
---

# /v2/parties/external/allocate

> Alpha 3.3：在同步器上分配新外部方的端点

预计3.5稳定

外部方必须（至少）托管在该节点上，并具有确认或观察权限
它可以选择托管在其他节点上（然后称为多托管方）。
如果托管在其他节点上，则必须在这些节点上执行托管关系的显式授权
在派对可以使用之前。
支持分散式命名空间，但必须获得其所有者的完全授权。
各个所有者名称空间事务可以在同一调用中提交（也可以完全授权）。
在非多托管、非去中心化一方的简单情况下，一旦该方退出，RPC 将返回
有效分配并准备使用，类似于 AllocateParty 行为。
对于更复杂的场景，应用程序可能需要显式查询聚会状态（目前仅通过管理 API）。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/parties/external/allocate
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
  /v2/partys/external/allocate：
    帖子：
      摘要：/v2/partys/external/allocate
      描述：>-
        Alpha 3.3：在同步器上分配新外部方的端点


        预计3.5稳定


        外部方必须（至少）托管在该节点上
        确认或观察许可

        它可以选择托管在其他节点上（然后称为多托管
        党）。

        如果托管在其他节点上，则托管的显式授权
        必须在这些节点上执行关系

        在派对可以使用之前。

        支持分散式命名空间，但必须完全提供
        经其所有者授权。

        各个所有者名称空间事务可以在同一
        调用（也完全授权）。

        在非多方托管、非去中心化一方的简单情况下，
        一旦聚会结束，RPC就会返回

        有效分配并准备使用，类似于 AllocateParty
        行为。对于更复杂的场景应用程序可能需要查询方
        明确状态（目前仅通过管理 API）。
      操作 ID：postV2PartiesExternalAllocate
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/AllocateExternalPartyRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/AllocateExternalPartyResponse'
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
    分配ExternalPartyRequest：
      标题：分配ExternalPartyRequest
      描述：|-
        所需授权：
          ``HasRight(参与方Admin) OR IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR IsAuthenticatedUser(user_id)``
      类型：对象
      需要：
        - 同步器
        - 入职交易
      属性：
        同步器：
          描述：|-
            TODO(#27670) 支持同步器别名
            用于加入队伍的同步器 ID

            必填
          类型：字符串
        入职交易：
          描述：>-
            加入外部方的拓扑交易

            可包含：

            - 聚会的命名空间。

            这可以是单个命名空间委托，

            或 DecentralizedNamespaceDefinition 及其授权的
            NamespaceDelegations 形式的命名空间所有者。

            可以提供，如果提供，必须经过签名完全授权
            在此请求中结合现有的拓扑状态。

            - 用于注册托管关系的 PartyTo参与方
            参与方，以及参与方的签名密钥和阈值。

            必须提供。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/SignedTransaction'
        多重哈希签名：
          描述：>-
            所有组合哈希的可选签名
            入职交易

            这可以用来代替为每个人提供签名
            交易可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/Signature'
        身份提供者 ID：
          描述：>-
            ``Identity Provider`` 的 id

            如果未设置，则假设该方由默认身份管理
            提供者。


            可选
          类型：字符串
        等待分配：
          描述：>-
            当 true 时，该 RPC 将尝试等待该方
            返回之前在同步器上分配。

            当为 false 时，分配将异步发生。

            这是尽最大努力，因为这种同步是唯一可能的
            对于非去中心化各方（单个托管节点）。

            对于去中心化各方，该标志将被忽略。

            默认为 true。


            可选
          类型：布尔值
        用户ID：
          描述：>-
            将获得新分配的 act_as 权限的用户
            聚会。

            如果设置为空字符串（默认），则没有用户将获得权限
            聚会。


            可选
          类型：字符串
    分配外部方响应：
      标题：AllocateExternalPartyResponse
      类型：对象
      需要：
        - 派对ID
      属性：
        派对 ID:
          描述：|-
            分配的参与方 ID

            必填
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
    签署交易：
      标题：签名交易
      类型：对象
      需要：
        - 交易
      属性：
        交易：
          描述：|-
            序列化的TopologyTransaction

            必填：必须非空
          类型：字符串
        签名：
          描述：>-
            特别针对此交易的附加签名

            用于需要额外签名的交易
            命名空间密钥签名例如：PartyTo参与方 必须由所有注册密钥签名


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/Signature'
    签名：
      标题： 签名
      类型：对象
      需要：
        - 格式
        - 签名
        - 签署人
        - 签名算法规范
      属性：
        格式：
          描述：必填
          类型：字符串
        签名：
          描述：'必填：必须非空'
          类型：字符串
        签署者：
          描述：>-
            用于创建此签名的密钥对的指纹/ID
            需要验证。


            必填
          类型：字符串
        签名算法规范：
          描述：|-
            用于生成此签名的签名算法规范

            必填
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
