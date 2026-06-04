---
title: "/v2/users/{user-id}/rights"
slug: "reference-json-api-reference-v2users-rights"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2users-rights.md"
source_title: "/v2/users/{user-id}/rights"
tags:
  - reference
  - json-api-reference
  - v2users-rights
---

# /v2/users/{user-id}/rights

> 撤销用户的权限。
撤销权限不会影响对应用户的资源版本。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 补丁 /v2/users/{user-id}/rights
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
  /v2/users/{用户 ID}/权限：
    补丁：
      摘要：/v2/users/{user-id}/rights
      描述：>-
        撤销用户的权利。

        撤销权限不影响资源版本
        对应的用户。
      操作Id：patchV2UsersUser-idRights
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
              $ref: '#/components/schemas/RevokeUserRightsRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/RevokeUserRightsResponse'
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
    撤销用户权限请求：
      标题：撤销用户权限请求
      描述：>-
        从授予用户的权限集中删除权限。


        所需授权：``HasRight(参与方Admin) 或
        IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``
      类型：对象
      需要：
        - 用户ID
      属性：
        用户ID：
          描述：|-
            要撤销权利的用户。

            必填
          类型：字符串
        权利：
          描述：|-
            撤销的权利。可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/Right'
        身份提供者 ID：
          描述：>-
            ``Identity Provider`` 的 id

            如果未设置，则假设用户由默认身份管理
            提供者。


            可选
          类型：字符串
    撤销用户权限响应：
      标题：撤销用户权限响应
      类型：对象
      属性：
        新撤销的权利：
          描述：|-
            请求实际撤销的权利。可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/Right'
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
    右：
      标题：右
      描述：授予用户的权利。
      类型：对象
      属性：
        种类：
          $ref: '#/components/schemas/Kind'
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
    种类：
      标题： 种类
      描述：必填
      其中之一：
        - 类型：对象
          需要：
            - 可以作为
          属性：
            可以充当：
              $ref: '#/components/schemas/CanActAs'
        - 类型：对象
          需要：
            - 可以执行为
          属性：
            可以执行为：
              $ref: '#/components/schemas/CanExecuteAs'
        - 类型：对象
          需要：
            - 可以执行为任何一方
          属性：
            可以作为任何一方执行：
              $ref: '#/components/schemas/CanExecuteAsAnyParty'
        - 类型：对象
          需要：
            - 可以读为
          属性：
            可以读为：
              $ref: '#/components/schemas/CanReadAs'
        - 类型：对象
          需要：
            - CanReadAsAnyParty
          属性：
            可以作为任何一方阅读：
              $ref: '#/components/schemas/CanReadAsAnyParty'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty8'
        - 类型：对象
          需要：
            - 身份提供者管理
          属性：
            身份提供者管理员：
              $ref: '#/components/schemas/IdentityProviderAdmin'
        - 类型：对象
          需要：
            - 参与者管理员
          属性：
            参与者管理员：
              $ref: '#/components/schemas/参与方Admin'可以充当：
      标题： 可以行动
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CanActAs1'
    可以执行为：
      标题：可以执行为
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CanExecuteAs1'
    可以作为任何一方执行：
      标题：CanExecuteAsAnyParty
      描述：>-
        用户作为任何一方准备和执行交易的权利。

        它的实用性主要针对执行交互的用户
        意见书

        代表多方。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CanExecuteAsAnyParty1'
    可以读为：
      标题： 可以读为
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CanReadAs1'
    可以作为任何一方阅读：
      标题：CanReadAsAnyParty
      描述：>-
        参与者超级读者的权利。其效用主要是
        为了

        不断地为外部工具（例如 PQS）提供数据，而无需
        更改订阅

        随着新政党的出现和消失。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CanReadAsAnyParty1'
    空8：
      标题： 空
      类型：对象
    身份提供者管理员：
      标题：IdentityProviderAdmin
      描述：>-
        管理分配给用户的身份提供商的权利
        到。

        这意味着能够管理也被分配的用户和各方

        到同一个身份提供商。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/IdentityProviderAdmin1'
    参与者管理员：
      标题： 参与者管理员
      描述：参与节点的管理权限。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/参与方Admin1'
    可以充当1：
      标题： 可以行动
      类型：对象
      需要：
        - 聚会
      属性：
        当事人：
          描述：|-
            为本方授权指挥的权利。

            必填
          类型：字符串
    可以执行为1：
      标题：可以执行为
      类型：对象
      需要：
        - 聚会
      属性：
        当事人：
          描述：>-
            作为该方准备和执行提交材料的权利。

            此权利并不赋予用户执行任何读取的权利。如果需要阅读，则必须添加单独的 ReadAs 权限。

            作为一方执行的权利也隐含在
            可以按照正确的方式行事。


            必填
          类型：字符串
    可以作为AnyParty1执行：
      标题：CanExecuteAsAnyParty
      描述：>-
        用户作为任何一方准备和执行交易的权利。

        它的实用性主要针对执行交互的用户
        意见书

        代表多方。
      类型：对象
    可以读为1：
      标题： 可以读为
      类型：对象
      需要：
        - 聚会
      属性：
        当事人：
          描述：|-
            读取该方可见的账本数据的权利。

            必填
          类型：字符串
    CanReadAsAnyParty1：
      标题：CanReadAsAnyParty
      描述：>-
        参与者超级读者的权利。其效用主要是
        为了

        不断地为外部工具（例如 PQS）提供数据，而无需
        更改订阅

        随着新政党的出现和消失。
      类型：对象
    身份提供者管理员1：
      标题：IdentityProviderAdmin
      描述：>-
        管理分配给用户的身份提供商的权利
        到。

        这意味着能够管理也被分配的用户和各方

        到同一个身份提供商。
      类型：对象
    参与者管理员1：
      标题： 参与者管理员
      描述：参与节点的管理权限。
      类型：对象
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
