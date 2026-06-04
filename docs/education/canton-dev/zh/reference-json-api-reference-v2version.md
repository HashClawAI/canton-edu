---
title: "/v2/version"
slug: "reference-json-api-reference-v2version"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2version.md"
source_title: "/v2/version"
tags:
  - reference
  - json-api-reference
  - v2version
---

# /v2/version

> 阅读 Ledger API 版本



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/version
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
  /v2/版本：
    得到：
      摘要：/v2/版本
      描述：阅读Ledger API版本
      操作Id：获取V2版本
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetLedgerApiVersionResponse'
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
    获取LedgerApiVersion响应：
      标题：GetLedgerApiVersionResponse
      类型：对象
      需要：
        - 版本
        - 特点
      属性：
        版本：
          描述：|-
            账本 API 的版本。

            必填
          类型：字符串
        特点：
          $ref: '#/components/schemas/FeaturesDescriptor'
          描述：|-
            此 Ledger API 端点支持的功能。

            Daml 应用程序可以使用特征描述符
            确定 Ledger API 版本的版本限制
            给定的 Ledger API 端点是否支持这些功能
            运行应用程序所需的。

            请参阅功能描述本身以了解之间的关系
            Ledger API 版本和功能存在。必填
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
    特点描述：
      标题：功能描述
      类型：对象
      需要：
        - 实验性的
        - 用户管理
        - 政党管理
        - 偏移检查点
        - 包功能
      属性：
        实验：
          $ref: '#/components/schemas/ExperimentalFeatures'
          描述：|-
            正在开发的功能或已使用的功能
            仅用于分类帐实施测试目的。

            Daml 应用程序在生产中不应依赖于这些。

            必填
        用户管理：
          $ref: '#/components/schemas/UserManagementFeature'
          描述：>-
            如果设置，则 Ledger API 服务器支持用户管理。

            建议客户查询该字段进行优雅调整
            他们的行为是为了

            不支持用户管理的账本。


            必填
        党务管理：
          $ref: '#/components/schemas/PartyManagementFeature'
          描述：>-
            如果设置，则 Ledger API 服务器支持参与方管理
            可配置性。

            建议客户查询该字段进行优雅调整
            他们的行为

            最大聚会页面大小。


            必填
        偏移检查点：
          $ref: '#/components/schemas/OffsetCheckpointFeature'
          描述：>-
            它包含与周期性偏移检查点相关的超时
            排放


            必填
        封装特点：
          $ref: '#/components/schemas/PackageFeature'
          描述：>-
            如果设置，则 Ledger API 服务器支持包列表

            可配置性。建议客户查询该字段

            优雅地将其行为调整为最大包列表页面
            尺寸。必填
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
    实验特点：
      标题：实验功能
      描述：请参阅功能消息定义以获取描述。
      类型：对象
      属性：
        静态时间：
          $ref: '#/components/schemas/ExperimentalStaticTime'
          描述：可选
        命令检查服务：
          $ref: '#/components/schemas/ExperimentalCommandInspectionService'
          描述：可选
    用户管理功能：
      标题：用户管理功能
      类型：对象
      需要：
        - 支持
        - 每个用户的最大权限
        - 最大用户页面大小
      属性：
        支持：
          描述：|-
            Ledger API服务器是否提供用户管理服务。

            必填
          类型：布尔值
        每个用户的最大权限：
          描述：>-
            可以分配给单个用户的最大权限数。

            服务器必须支持每个用户至少 100 个权限。

            值 0 表示服务器不对每个用户强制执行任何权限
            限制。


            必填
          类型：整数
          格式：int32
        最大用户页面大小：
          描述：>-
            服务器单次返回的最大用户数
            响应（页面）。

            服务器必须支持每页至少 100 个用户。

            值 0 表示服务器不强制执行页面大小限制。


            必填
          类型：整数
          格式：int32
    派对管理功能：
      标题：派对管理功能
      类型：对象
      需要：
        - maxPartiesPageSize
      属性：
        最大派对页面大小：
          描述：>-
            服务器一次可以返回的最大参与方数量
            响应（页面）。


            必填
          类型：整数
          格式：int32
    偏移检查点功能：
      标题：OffsetCheckpointFeature
      类型：对象
      需要：
        - maxOffsetCheckpointEmissionDelay
      属性：
        最大偏移检查点发射延迟：
          $ref: '#/components/schemas/Duration'
          描述：|-
            发出新 OffsetCheckpoint（如果存在）的最大延迟必填
    封装特点：
      标题： 包功能
      类型：对象
      需要：
        - maxVettedPackagesPageSize
      属性：
        最大VettedPackagesPageSize：
          描述：>-
            服务器一次可以返回的已审查包裹的最大数量
            单身

            列出它们时的响应（页面）。


            必填
          类型：整数
          格式：int32
    实验静态时间：
      标题：实验静态时间
      描述：Ledger处于静态时间模式，公开了一个时间服务。
      类型：对象
      需要：
        - 支持
      属性：
        支持：
          描述：必填
          类型：布尔值
    实验命令检查服务：
      标题：实验命令检查服务
      描述：Ledger API是否支持命令检查服务
      类型：对象
      需要：
        - 支持
      属性：
        支持：
          描述：必填
          类型：布尔值
    持续时间：
      标题： 持续时间
      类型：对象
      需要：
        - 秒
        - 纳米
      属性：
        秒：
          类型：整数
          格式：int64
        纳米：
          类型：整数
          格式：int32
        未知字段：
          $ref: '#/components/schemas/UnknownFieldSet'
          描述：>-
            该字段会作为 protobuf 的一部分自动添加到 json
            映射
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
