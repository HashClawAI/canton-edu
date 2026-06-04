---
title: "/v2/authenticated-user"
slug: "reference-json-api-reference-v2authenticated-user"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2authenticated-user.md"
source_title: "/v2/authenticated-user"
tags:
  - reference
  - json-api-reference
  - v2authenticated-user
---

# /v2/authenticated-user

> 获取当前认证用户的用户数据。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/authenticated-user
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
  /v2/经过身份验证的用户：
    得到：
      摘要：/v2/authentiated-user
      描述：获取当前认证用户的用户数据。
      操作 ID：getV2Authenticated-user
      参数：
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
                $ref: '#/components/schemas/GetUserResponse'
        “400”：
          描述：>-
            值无效，值无效：查询参数
            身份提供者 ID
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
    获取用户响应：
      标题：获取用户响应
      类型：对象
      需要：
        - 用户
      属性：
        用户：
          $ref: '#/components/schemas/User'
          描述：|-
            检索到的用户。必填
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
    用户：
      标题： 用户
      描述： |2-
         用户和权利
        //////////////////////////////////
         用户用于动态管理授予 Daml 应用程序的权限。
         它们是按参与者节点存储和管理的。
      类型：对象
      需要：
        - 身份证号码
      属性：
        身份证号：
          描述：>-
            用户标识符，必须是最多 128 位的非空字符串

            字符可以是字母数字 ASCII 字符或以下之一
            符号“@^$.!`-#+'~_|:()”。


            必填
          类型：字符串
        主要政党：
          描述：>-
            该用户默认阅读并执行操作的主要方
            分类账

            *假设*它具有相应的``CanReadAs(primary_party)``或

            ``CanActAs(primary_party)``权利。

            Ledger API 客户端应该将此字段设置为非空值
            所有用户到

            使用户能够使用自己的 Daml 方对账本进行操作。

            参与者管理员的用户可以有一个关联的主要
            聚会。

            可修改


            可选
          类型：字符串
        已停用：
          描述：>-
            设置后，用户将被拒绝对 Ledger API 的所有访问。

            否则，用户可以根据用户的权限访问 Ledger API
            权利。

            可修改


            可选
          类型：布尔值
        元数据：
          $ref: '#/components/schemas/ObjectMeta'
          描述：>-
            该用户的元数据。

            请注意，``metadata.resource_version`` 跟踪对
            由 ``User`` 消息描述的属性，而不是用户的属性
            权利。

            可修改可选
        身份提供者 ID：
          描述：>-
            由“Identity Provider”配置的身份提供者的ID
            配置``

            如果未设置，则假设用户由默认身份管理
            提供者。


            可选
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
    对象元：
      标题：对象元
      描述：>-
        表示与参与者资源对应的元数据（例如
        有关一方的参与者用户或参与者本地信息）。


        基于 Kubernetes API 中使用的 ``ObjectMeta`` 元。

        参见
        https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/ generated.proto#L640
      类型：对象
      属性：
        资源版本：
          描述：>-
            一个不透明的非空值，由参与者服务器填充
            代表资源的内部版本

            此“`ObjectMeta`”消息已附加到。参与服务器
            每次相应的时候都会将其更改为唯一值
            资源已更新。

            您不能依赖资源版本的格式。参加者
            服务器可能会更改它，恕不另行通知。

            您可以通过发出读取来获取最新的资源版本值
            请求。

            您可以通过将其传回来将其用于并发更改检测
            在更新请求中未修改。

            然后，参与者服务器会将传递的值与
            由系统维护的值来确定

            自您阅读资源以来是否发生了任何其他更新
            版本。

            成功更新后，保证不会有其他更新
            发生在您的读取-修改-写入序列期间。

            但是，如果在读取-修改-写入期间发生了另一次更新
            序列，那么您的更新将失败并出现相应的错误。

            并发变更控制是可选的。仅当以下情况时才会应用
            您在更新请求中包含资源版本。

            创建资源的新实例时，您必须保留
            资源版本为空。

            它的值将由参与者服务器填充
            成功的资源创建。可选
          类型：字符串
        注释：
          $ref: '#/components/schemas/Map_String'
          描述：>-
            一组可修改的键值对，可用于表示
            任意的、特定于客户端的元数据。

            限制条件：


            1. 所有键和值的总大小不能超过 256kb
            UTF-8 编码。

            2. 密钥由可选的前缀段和必需的前缀段组成
            命名段，这样：

               - 键前缀（如果存在）必须是最多 253 个字符的有效 DNS 子域，后跟“/”（正斜杠）字符，
               - 名称段必须最多包含 63 个字符，这些字符可以是字母数字 ([a-z0-9A-Z]) 或“.” （点）、“-”（破折号）或“_”（下划线）；
                 并且它必须以字母数字字符开头和结尾。

            3. 值可以是任何非空字符串。


            带有空前缀的密钥是为最终用户保留的。

            由外部工具或参与者内部设置的属性
            服务器必须使用非空键前缀。

            protobuf3 的语义不允许重复的键
            地图。

            请参阅：https://developers.google.com/protocol-buffers/docs/proto3#maps

            注释可以是可修改资源的一部分。

            使用资源的更新 RPC 来更新其注释。

            为了添加新注释或使用以下命令更新现有注释
            更新 RPC，在更新请求中提供所需的注释。

            为了使用更新 RPC 删除注释，请提供
            目标注释的键，但将其值设置为空字符串
            更新请求。

            可修改


            可选：可以为空
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
