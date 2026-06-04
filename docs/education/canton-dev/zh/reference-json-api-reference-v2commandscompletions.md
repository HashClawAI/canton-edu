---
title: "/v2/commands/completions"
slug: "reference-json-api-reference-v2commandscompletions"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandscompletions.md"
source_title: "/v2/commands/completions"
tags:
  - reference
  - json-api-reference
  - v2commandscompletions
---

# /v2/commands/completions

> 查询完成列表（阻塞调用）

订阅命令完成事件。
注意：此端点应用于小结果集。
当结果数量超过节点配置限制时（`http-list-max-elements-limit`）
将会返回一个错误（`413 Content Too Large`）。
增加此限制可能会导致性能问题和高内存消耗。
考虑使用 websockets (asyncapi) 以获得更高的效率和更大的结果。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/completions
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
  /v2/命令/完成：
    帖子：
      摘要：/v2/commands/completions
      描述：>-
        查询完成列表（阻塞调用）


        订阅命令完成事件。

        注意：此端点应用于小结果集。

        当结果数量超过节点配置限制时
        (`http-list-max-elements-limit`)

        将会返回一个错误（`413 Content Too Large`）。

        增加此限制可能会导致性能问题和内存占用过高
        消费。考虑使用 websockets (asyncapi) 来提高更大的效率
        结果。
      操作 ID：postV2CommandsCompletions
      参数：
        - 名称：限制
          在：查询
          描述：>-
            要返回的最大元素数，如果是，则忽略此参数
            大于服务器设置
          必填：假
          架构：
            类型：整数
            格式：int64
        - 名称：stream_idle_timeout_ms
          在：查询
          描述：>-
            如果没有收到新元素，则完成并发送结果超时
            （对于开放式流）
          必填：假
          架构：
            类型：整数
            格式：int64
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/CompletionStreamRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                类型：数组
                项目：
                  $ref: '#/components/schemas/CompletionStreamResponse'
        “400”：
          描述：>-
            无效值、无效值：主体、无效值：查询
            参数限制，无效值：查询参数
            流空闲超时毫秒
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
    完成流请求：
      标题：CompleteStreamRequest
      类型：对象
      需要：
        - 聚会
      属性：
        用户ID：
          描述：>-
            只有使用相同 user_id 提交的命令才会完成
            在流中可见。

            必须是有效的 UserIdString（如``value.proto``中所述）。


            除非使用用户令牌进行身份验证，否则是必需的。

            在这种情况下，令牌的用户 ID 将用于请求的
            用户 ID。


            可选
          类型：字符串
        各方：
          描述：>-
            应包含其数据的各方的非空列表。

            该流仅显示命令的完成情况，其中至少有一个
            ``act_as`` 方属于给定的方组。

            必须是有效的 PartyIdString（如``value.proto``中所述）。必填：必须非空
          类型：数组
          项目：
            类型：字符串
        开始独家：
          描述：>-
            该可选字段指示完成的最小偏移量。
            这可用于恢复较早的完成流。

            如果未设置，分类帐将使用分类帐开始偏移量。

            如果指定，它必须是有效的绝对偏移量（正整数）
            或零（分类帐开始偏移）。

            如果账本已被剪枝，则必须指定该参数
            大于修剪偏移量。可选
          类型：整数
          格式：int64
    完成流响应：
      标题：CompleteStreamResponse
      类型：对象
      属性：
        完成响应：
          $ref: '#/components/schemas/CompletionResponse'
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
    完成响应：
      标题：完成响应
      描述：必填
      其中之一：
        - 类型：对象
          需要：
            - 完成
          属性：
            完成：
              $ref: '#/components/schemas/Completion'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty4'
        - 类型：对象
          需要：
            - 偏移检查点
          属性：
            偏移检查点：
              $ref: '#/components/schemas/OffsetCheckpoint'
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
    完成：
      标题：完成
      描述：>-
        完成表示账本上已提交命令的状态：
        它可能成功，也可能失败。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Completion1'
    空4：
      标题： 空
      类型：对象
    偏移检查点：
      标题：OffsetCheckpoint
      描述：|-
        OffsetCheckpoints 可用于：- 检测命令超时。
        - 提供可用于重新启动消费的偏移量。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/OffsetCheckpoint1'
    完成1：
      标题：完成
      描述：>-
        完成表示账本上已提交命令的状态：
        它可能成功，也可能失败。
      类型：对象
      需要：
        - 命令ID
        - 用户ID
        - 偏移量
        - 充当
        - 同步器时间
      属性：
        命令ID：
          描述：|-
            成功或失败命令的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        状态：
          $ref: '#/components/schemas/JsStatus'
          描述：>-
            识别错误的确切类型。

            它使用与用于传送错误详细信息相同的格式
            API 的 RPC 响应。


            可选
        更新ID：
          描述：>-
            交易或重新分配的 update_id
            带有 command_id 的命令。


            仅为成功执行的命令设置。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            可选
          类型：字符串
        用户ID：
          描述：>-
            用于提交的用户 ID，如中所述
            ``commands.proto``。

            必须是有效的 UserIdString（如``value.proto``中所述）。


            必填
          类型：字符串
        充当：
          描述：>-
            代表其执行命令的各方的集合。

            包含``act_as`` parties from ``commands.proto``

            过滤到 CompletionStreamRequest 中的请求方。

            各方的顺序不必与提交时的顺序相同。

            每个元素必须是有效的 PartyIdString（如中所述
            ``value.proto``)。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        提交ID：
          描述：>-
            此完成引用的提交 ID，如中所述
            ``commands.proto``。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            可选
          类型：字符串
        重复数据删除周期：
          $ref: '#/components/schemas/DeduplicationPeriod1'
        跟踪上下文：
          $ref: '#/components/schemas/TraceContext'
          描述：>-
            Ledger API 跟踪上下文该消息中传输的跟踪上下文对应于
            提供跟踪上下文

            由客户端应用程序在原始命令的 HTTP2 标头中执行
            提交。

            我们通常使用标头来传输此类信息。这里
            我们使用消息

            body，因为它用在不支持 per 的 gRPC 流中
            消息标题。

            该字段将填充包含在
            原始提交。

            如果未提供，则会生成唯一的 ledger-api-server 跟踪
            将使用上下文

            相反。


            可选
        偏移量：
          描述：>-
            可以在后续的 CompletionStreamRequest 中使用来恢复
            稍后消耗该流。

            必须是有效的绝对偏移量（正整数）。


            必填
          类型：整数
          格式：int64
        同步器时间：
          $ref: '#/components/schemas/同步器Time'
          描述：>-
            同步器及其记录时间。

            提供的同步器 ID，以防出现


            - 成功/失败的交易：标识交易的同步器
            交易

            - 对于成功/失败的取消分配命令：标识源
            同步器

            - 对于成功/失败的分配命令：识别目标
            同步器


            必填
        支付流量费用：
          描述：>-
            该参与节点为确认所付出的流量费用
            要求

            对于提交的命令。


            在其相应命令之前执行被拒绝的命令

            同步器命令确认请求将报告
            付费的

            流量成本为零。

            如果为命令订购了确认请求，但该请求
            失败

            （例如，由于与并发合同档案的争用），
            交通

            支付费用并报告请求未能完成的情况。


            如果您想关联成功完成的流量成本

            对于该命令产生的事务，您可以使用

            ``offset`` 字段用于检索交易

            同一参与节点上的``UpdateService.GetUpdateByOffset``；或
            或者使用``update_id``

            使用字段检索交易
            任意参与节点上的“`UpdateService.GetUpdateById`”

            看到交易。注意：对于参与者开始之前处理的完成情况
            服务

            Ledger API 上的流量成本，该字段将设置为零。

            此外，提交节点所产生的总成本
            提交的交易可能会更大

            比报告的成本高，例如，如果由于以下原因而发出重试
            向同步器提交失败。

            这里报告的费用是订购确认所支付的费用
            请求。


            可选
          类型：整数
          格式：int64
    偏移检查点1：
      标题：OffsetCheckpoint
      描述：|-
        OffsetCheckpoints 可用于：

        - 检测命令超时。
        - 提供可用于重新启动消费的偏移量。
      类型：对象
      需要：
        - 偏移量
      属性：
        偏移量：
          描述：>-
            参与者的offset，offset字段的详细信息为
            在``community/ledger-api/README.md``中描述。

            必须是有效的绝对偏移量（正整数）。


            必填
          类型：整数
          格式：int64
        同步器时间：
          描述：|-
            与此偏移处的每个同步器关联的时间。

            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/同步器Time'
    Js状态：
      标题：JsStatus
      类型：对象
      需要：
        - 代码
        - 消息
      属性：
        代码：
          类型：整数
          格式：int32
        留言：
          类型：字符串
        详细信息：
          类型：数组
          项目：
            $ref: '#/components/schemas/ProtoAny'
    重复数据删除Period1：
      标题：重复数据删除周期
      描述：>-
        用于提交的实际重复数据删除窗口，即
        源自

        ``Commands.deduplication_period``。账本可以将
        重复数据删除期进入其他

        描述并以实施指定的方式延长期限。


        用于审核中描述的重复数据删除保证
        ``commands.proto``。


        即使完成忽略此，重复数据删除保证也适用
        场。可选
      其中之一：
        - 类型：对象
          需要：
            - 重复数据删除持续时间
          属性：
            重复数据删除持续时间：
              $ref: '#/components/schemas/DeduplicationDuration1'
        - 类型：对象
          需要：
            - 重复数据删除偏移量
          属性：
            重复数据删除偏移量：
              $ref: '#/components/schemas/DeduplicationOffset1'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty3'
    跟踪上下文：
      标题：TraceContext
      类型：对象
      属性：
        追踪父级：
          描述：|-
            https://www.w3.org/TR/trace-context/

            可选
          类型：字符串
        跟踪状态：
          描述：可选
          类型：字符串
    同步器时间：
      标题：同步器时间
      类型：对象
      需要：
        - 同步器ID
        - 记录时间
      属性：
        同步器ID：
          描述：|-
            同步器的id。

            必填
          类型：字符串
        记录时间：
          描述：>-
            最大记录时间低于该值的所有命令都必须
            如果在此之前尚未完成，则视为失败
            检查站。必填
          类型：字符串
    原型：
      标题：ProtoAny
      类型：对象
      需要：
        - 类型 URL
        - 价值
        - 未知字段
      属性：
        类型网址：
          类型：字符串
        值：
          类型：字符串
        未知字段：
          $ref: '#/components/schemas/UnknownFieldSet'
        值解码：
          类型：字符串
    重复数据删除持续时间1：
      标题：重复数据删除持续时间
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Duration'
    重复数据删除偏移1：
      标题：重复数据删除偏移
      类型：对象
      需要：
        - 价值
      属性：
        值：
          类型：整数
          格式：int64
    空3：
      标题： 空
      类型：对象
    未知字段集：
      标题：未知字段集
      类型：对象
      需要：
        - 字段
      属性：
        字段：
          $ref: '#/components/schemas/Map_Int_Field'
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
