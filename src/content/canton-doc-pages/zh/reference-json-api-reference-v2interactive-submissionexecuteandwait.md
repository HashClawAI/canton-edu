---
title: "/v2/interactive-submission/executeAndWait"
slug: "reference-json-api-reference-v2interactive-submissionexecuteandwait"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionexecuteandwait.md"
source_title: "/v2/interactive-submission/executeAndWait"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionexecuteandwait
---

# /v2/interactive-submission/executeAndWait

> 与 ExecuteSubmission 类似，但_同步_等待事务完成
重要提示：依赖此端点的响应需要相信参与者节点是诚实的。
恶意节点可能会使成功提交的请求看起来失败，反之亦然



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/executeAndWait
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
  /v2/交互式提交/executeAndWait：
    帖子：
      摘要：/v2/interactive-submission/executeAndWait
      描述：>-
        与 ExecuteSubmission 类似，但_同步_等待完成
        交易的

        重要提示：依赖此端点的响应需要信任
        老实说，参与者节点。

        恶意节点可能会出现成功提交的请求
        失败，反之亦然
      操作Id：postV2Interactive-submissionExecuteandwait
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/JsExecuteSubmissionAndWaitRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/ExecuteSubmissionAndWaitResponse'
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
    JsExecuteSubmissionAndWaitRequest：
      标题：JsExecuteSubmissionAndWaitRequest
      类型：对象
      需要：
        - 准备好的交易
        - 派对签名
        - 提交ID
        - 哈希方案版本
      属性：
        准备好的交易：
          描述：>-
            准备好的交易通常，这是 中 `prepared_transaction` 字段的值
            `PrepareSubmissionResponse`

            通过调用`prepareSubmission`获得。


            必填
          类型：字符串
        当事人签名：
          $ref: '#/components/schemas/PartySignatures'
          描述：>-
            授权准备提交的各方签名
            由该节点执行。

            每一方都可以提供一个或多个签名。

            并且可以由一方或多方签署。

            请注意，目前仅支持单方提交。


            必填
        重复数据删除周期：
          $ref: '#/components/schemas/DeduplicationPeriod2'
        提交ID：
          描述：>-
            区分不同完成情况的唯一标识符
            具有相同更改 ID 的提交。

            通常是随机 UUID。应用程序预计将使用
            每次重试提交时使用不同的 UUID

            具有相同的更改 ID。

            必须是有效的 LedgerString（如“`value.proto`”中所述）。


            必填
          类型：字符串
        用户ID：
          描述：|-
            请参阅[PrepareSubmissionRequest.user_id]

            可选
          类型：字符串
        哈希方案版本：
          描述：|-
            构建哈希时使用的哈希方案版本

            必填
          类型：字符串
          枚举：
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
        最短账本时间：
          $ref: '#/components/schemas/MinLedgerTime'
          描述：>-
            如果设置会影响所选账本的有效时间，但不会影响
            导致提交延迟，因此任何覆盖

            应安排在允许的窗口内执行
            同步器。


            可选
    执行提交并等待响应：
      标题：执行提交并等待响应
      类型：对象
      需要：
        - 更新ID
        - 完成偏移量
      属性：
        更新ID：
          描述：|-
            由提交的命令产生的事务的 ID。
            必须是有效的 LedgerString（如“`value.proto`”中所述）。

            必填
          类型：字符串
        完成偏移量：
          描述：>-
            偏移字段的详细信息描述于
            ``community/ledger-api/README.md``。必填
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
    当事人签名：
      标题： 派对签名
      描述：提交方提供的附加签名
      类型：对象
      需要：
        - 签名
      属性：
        签名：
          描述：|-
            所有各方提供的附加签名

            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/SinglePartySignatures'
    重复数据删除周期2：
      标题：重复数据删除周期
      其中之一：
        - 类型：对象
          需要：
            - 重复数据删除持续时间
          属性：
            重复数据删除持续时间：
              $ref: '#/components/schemas/DeduplicationDuration2'
        - 类型：对象
          需要：
            - 重复数据删除偏移量
          属性：
            重复数据删除偏移量：
              $ref: '#/components/schemas/DeduplicationOffset2'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty10'
    最小账本时间：
      标题：最小账本时间
      类型：对象
      属性：
        时间：
          $ref: '#/components/schemas/Time'
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
    单方签名：
      标题： SinglePartySignatures
      描述：单方提供的签名
      类型：对象
      需要：
        - 聚会
        - 签名
      属性：
        当事人：
          描述：|-
            提交方

            必填
          类型：字符串
        签名：
          描述：|-
            签名必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/Signature'
    重复数据删除持续时间2：
      标题：重复数据删除持续时间
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Duration'
    重复数据删除偏移2：
      标题：重复数据删除偏移
      类型：对象
      需要：
        - 价值
      属性：
        值：
          类型：整数
          格式：int64
    空10：
      标题： 空
      类型：对象
    时间：
      标题： 时间
      描述：必填
      其中之一：
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty9'
        - 类型：对象
          需要：
            - MinLedgerTimeAbs
          属性：
            MinLedgerTimeAbs：
              $ref: '#/components/schemas/MinLedgerTimeAbs'
        - 类型：对象
          需要：
            - MinLedgerTimeRel
          属性：
            MinLedgerTimeRel：
              $ref: '#/components/schemas/MinLedgerTimeRel'
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
            用于生成此签名的签名算法规范必填
          类型：字符串
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
    空9：
      标题： 空
      类型：对象
    MinLedgerTimeAbs：
      标题：MinLedgerTimeAbs
      类型：对象
      需要：
        - 价值
      属性：
        值：
          类型：字符串
    MinLedgerTimeRel：
      标题：MinLedgerTimeRel
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Duration'
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
