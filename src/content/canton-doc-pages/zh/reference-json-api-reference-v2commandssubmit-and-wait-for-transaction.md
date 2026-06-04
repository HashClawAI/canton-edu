---
title: "/v2/commands/submit-and-wait-for-transaction"
slug: "reference-json-api-reference-v2commandssubmit-and-wait-for-transaction"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandssubmit-and-wait-for-transaction.md"
source_title: "/v2/commands/submit-and-wait-for-transaction"
tags:
  - reference
  - json-api-reference
  - v2commandssubmit-and-wait-for-transaction
---

# /v2/commands/submit-and-wait-for-transaction

> 提交单个复合命令，等待其结果，然后返回事务。
传播失败提交的 gRPC 错误，包括 Daml 解释错误。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/submit-and-wait-for-transaction
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
  /v2/commands/提交并等待交易：
    帖子：
      摘要：/v2/commands/submit-and-wait-for-transaction
      描述：>-
        提交单个复合命令，等待其结果并返回
        交易。

        传播失败提交的 gRPC 错误，包括 Daml
        解释错误。
      操作 ID：postV2Commands提交并等待交易
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/JsSubmitAndWaitForTransactionRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsSubmitAndWaitForTransactionResponse'
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
    JsSubmitAndWaitForTransactionRequest：
      标题：JsSubmitAndWaitForTransactionRequest
      描述：这些命令作为单个原子事务执行。
      类型：对象
      需要：
        - 命令
      属性：
        命令：
          $ref: '#/components/schemas/JsCommands'
          描述：|-
            要提交的命令。

            必填
        交易格式：
          $ref: '#/components/schemas/TransactionFormat'
          描述：>-
            如果没有提供``transaction_format``，将使用默认值
            其中 ``transaction_shape`` 设置为TRANSACTION_SHAPE_ACS_DELTA，``event_format`` 定义为
            ``filters_by_party`` 包含通配符模板

            过滤所有原始``act_as`` and ``read_as``方和
            ``verbose`` 标志已设置。


            可选
    JsSubmitAndWaitForTransactionResponse：
      标题：JsSubmitAndWaitForTransactionResponse
      类型：对象
      需要：
        - 交易
      属性：
        交易：
          $ref: '#/components/schemas/JsTransaction'
          描述：>-
            由提交的命令产生的事务。

            事务可能不包含任何事件（请求条件结果
            过滤掉所有这些）。


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
    Js命令：
      标题：Js命令
      描述：将多个命令组合在一起的复合命令。
      类型：对象
      需要：
        - 命令ID
        - 命令
        - 充当
      属性：
        命令：
          描述：|-
            该原子命令的各个元素。必须非空。

            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/Command'
        命令ID：
          描述：>-
            唯一标识该命令。

            三元组(user_id, act_as, command_id)构成变更ID
            对于预期的账本变更，

            其中 act_as 被解释为一组参与方名称。

            变更 ID 可用于匹配预期的账本变更
            以及他们所有的完成。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            必填
          类型：字符串
        充当：
          描述：>-
            应代表其执行命令的一组各方。

            如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者代表每一方行事。

            每个元素必须是有效的 PartyIdString（如中所述
            ``value.proto``)。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        用户ID：
          描述：>-
            唯一标识发出命令的参与用户。

            必须是有效的 UserIdString（如``value.proto``中所述）。

            除非使用用户令牌进行身份验证，否则是必需的。

            在这种情况下，令牌的用户 ID 将用于请求的
            用户 ID。


            可选
          类型：字符串
        读作：
          描述：>-
            代表其的一组各方（除了列表中列出的所有各方之外）
            ``act_as``) 合约可以检索。

            这会影响Daml操作，例如``fetch``, ``fetchByKey``，
            ``lookupByKey``, ``exercise``, and ``exerciseByKey``。

            注意：Daml网络的一个参与节点可以托管多个
            派对。参与者身上的每份合同

            节点仅对这些参与方的子集可见。一个命令可以
            只使用至少可见的合同

            ``act_as`` or ``read_as``中的当事人之一。这个可见度
            检查独立于Daml授权

            获取操作的规则。

            如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者

            代表每一方读取合同数据。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        工作流程ID：
          描述：|-
            该命令所属的账本工作流程的标识符。
            必须是有效的 LedgerString（如“`value.proto`”中所述）。

            可选
          类型：字符串
        重复数据删除周期：
          $ref: '#/components/schemas/DeduplicationPeriod'
        minLedgerTimeAbs：
          描述：>-
            分配给结果的分类账时间的下限
            交易。

            注意：交易的分类账时间被分配为
            命令解释。

            如果您期望命令解释将使用此属性
            花费相当多的时间，这样通过

            结果交易被排序的时间，其分配的分类账
            时间不再有效。

            不得与 min_ledger_time_rel 同时设置。可选
          类型：字符串
        minLedgerTimeRel：
          $ref: '#/components/schemas/Duration'
          描述：>-
            与 min_ledger_time_abs 相同，但指定为持续时间，从
            从服务器收到命令的时间算起。

            不得与 min_ledger_time_abs 同时设置。


            可选
        提交ID：
          描述：>-
            区分不同完成情况的唯一标识符
            具有相同更改 ID 的提交。

            通常是随机 UUID。应用程序预计将使用
            每次重试提交时使用不同的 UUID

            具有相同的更改 ID。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            如果省略，参与者或提交者可以设置一个值
            他们的选择。


            可选
          类型：字符串
        披露的合同：
          描述：>-
            用于解析合同和合同密钥的附加合同
            查找。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/DisclosureContract'
        同步器ID：
          描述：|-
            必须是有效的同步器 ID

            可选
          类型：字符串
        packageIdSelectionPreference：
          描述：>-
            客户端解析时的package-id选择偏好

            命令提交中的包名和接口实例
            解释


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        预取合约密钥：
          描述：>-
            将合约密钥提取到缓存中以加快命令速度
            处理。

            应该只包含预计要解析的合约密钥
            在解释命令期间。

            公开合约的密钥不需要预取。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/PrefetchContractKey'
        最大点击次数：
          描述：>-
            拓扑感知包的最大传递次数
            选择（TAPS）。

            较高的值可以增加打包成功的机会
            选择解释事务的路由。

            如果未设置，则默认为参与者中定义的值
            配置。

            提供的值不得超过规定的限制
            参与者配置。可选
          类型：整数
          格式：int32
    交易格式：
      标题：交易格式
      描述：|-
        指定 Daml 事务中包含哪些事件的格式
        以及要计算和包含哪些数据。
      类型：对象
      需要：
        - 交易形状
        - 事件格式
      属性：
        事件格式：
          $ref: '#/components/schemas/EventFormat'
          描述：必填
        交易形态：
          描述：>-
            使用什么交易形状来解释过滤器
            事件格式。


            必填
          类型：字符串
          枚举：
            - 交易形状未指定
            - TRANSACTION_SHAPE_ACS_DELTA
            - TRANSACTION_SHAPE_LEDGER_EFFECTS
    Js事务：
      标题：JsTransaction
      描述：账本交易的创建和存档事件的过滤视图。
      类型：对象
      需要：
        - 更新ID
        - 有效
        - 偏移量
        - 同步器ID
        - 记录时间
        - 活动
      属性：
        更新ID：
          描述：|-
            由服务器分配。对于关联日志很有用。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        命令ID：
          描述：>-
            导致此事务的命令的 ID。失踪
            对于除提交方之外的所有人。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            可选
          类型：字符串
        工作流程ID：
          描述：|-
            命令提交中使用的工作流 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            可选
          类型：字符串
        有效于：
          描述：|-
            账本有效时间。

            必填
          类型：字符串
        事件：
          描述：>-
            事件的集合。

            包含：


            - 如果是 ACS_DELTA，则为“`CreatedEvent`` or ``ArchivedEvent`”
            交易形态

            - 如果是 LEDGER_EFFECTS，则为“`CreatedEvent`` or ``ExercisedEvent`”
            交易形态


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/Event'
        偏移量：
          描述：>-
            绝对偏移量。该字段的详细信息描述于
            ``community/ledger-api/README.md``。

            它是一个有效的绝对偏移量（正整数）。必填
          类型：整数
          格式：int64
        同步器ID：
          描述：|-
            有效的同步器 ID。
            标识同步事务的同步器。

            必填
          类型：字符串
        跟踪上下文：
          $ref: '#/components/schemas/TraceContext'
          描述：>-
            Ledger API 跟踪上下文


            该消息中传输的跟踪上下文对应于
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
        记录时间：
          描述：>-
            记录交易的时间。记录时间
            指的是同步器

            这同步了事务。


            必填
          类型：字符串
        外部交易哈希：
          描述：>-
            对于外部签名的交易，包含外部交易
            散列

            由外方签署。可用于关联外部
            提交已提交的事务。


            可选：可以为空
          类型：字符串
        支付流量费用：
          描述：>-
            该参与节点为此支付的流量费用
            确认

            请求此交易。


            未设置的交易

            - 由另一位参与者发起

            - 通过维修服务离线启动

            - 在参与者开始提供流量费用之前处理
            账本 API

            - 作为非提交方查询过滤的一部分返回可选
          类型：整数
          格式：int64
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
    命令：
      标题：命令
      描述：>-
        命令可以创建新合约或对某个合约执行选择
        现有合同。
      其中之一：
        - 类型：对象
          需要：
            - 创建和练习命令
          属性：
            创建和练习命令：
              $ref: '#/components/schemas/CreateAndExerciseCommand'
        - 类型：对象
          需要：
            - 创建命令
          属性：
            创建命令：
              $ref: '#/components/schemas/CreateCommand'
        - 类型：对象
          需要：
            - 通过按键命令进行练习
          属性：
            通过按键命令进行练习：
              $ref: '#/components/schemas/ExerciseByKeyCommand'
        - 类型：对象
          需要：
            - 演习指挥
          属性：
            练习命令：
              $ref: '#/components/schemas/ExerciseCommand'
    重复数据删除周期：
      标题：重复数据删除周期
      描述：>-
        指定更改 ID 的重复数据删除周期。

        如果省略，参与者将采用配置的最大
        重复数据删除时间。可选
      其中之一：
        - 类型：对象
          需要：
            - 重复数据删除持续时间
          属性：
            重复数据删除持续时间：
              $ref: '#/components/schemas/DeduplicationDuration'
        - 类型：对象
          需要：
            - 重复数据删除偏移量
          属性：
            重复数据删除偏移量：
              $ref: '#/components/schemas/DeduplicationOffset'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty'
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
    披露合同：
      标题： 披露合同
      描述：|-
        用于解决的附加合同
        合约和合约密钥查找。
      类型：对象
      需要：
        - 创建事件Blob
      属性：
        模板ID：
          描述：>-
            合约的模板id。

            标识符使用 package-id 引用格式。


            如果提供，用于验证合约的模板 ID
            在created_event_blob中序列化。


            可选
          类型：字符串
        合约编号：
          描述：>-
            合约编号


            如果提供，用于验证合约的合约 ID
            在created_event_blob中序列化。


            可选
          类型：字符串
        创建事件Blob：
          描述：>-
            包含所需的完整有效负载的不透明字节字符串
            达米尔发动机

            重建接收参与者不知道的合同。


            必填：必须非空
          类型：字符串
        同步器ID：
          描述：|-
            当前分配合约的同步器的ID

            可选
          类型：字符串
    预取合约密钥：
      标题：PrefetchContractKey
      描述：预载合约
      类型：对象
      需要：
        - 模板ID
        - 合约密钥
      属性：
        模板ID：
          描述：>-
            客户想要预取的合同模板。

            package-name 和 package-id 引用标识符格式
            支持模板 ID。注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        合约密钥：
          描述：|-
            客户端想要预取的合约的密钥。

            必填
    事件格式：
      标题：事件格式
      描述：>-
        事件格式，定义应包含哪些事件

        以及应该为它们计算和包含哪些数据。


        请注意，某些过滤行为取决于
        `TransactionShape`,

        预计将与 `EventFormat` 的用法一起指定。
      类型：对象
      属性：
        按方筛选：
          $ref: '#/components/schemas/Map_Filters'
          描述：>-
            每个键必须是有效的 PartyIdString（如中所述
            ``value.proto``)。

            过滤器的解释取决于交易形状
            正在过滤：


            1. 对于 **ledger-effects** 返回创建和执行事件，
            证人至少包括以下之一
               列出的各方并匹配每方过滤器。
            2. 对于 **交易和活动合约集流** 创建并
            为所有合约返回存档事件
               利益相关者至少包括列出的各方之一并匹配每方过滤器。

            可选：可以为空
        过滤器ForAnyParty：
          $ref: '#/components/schemas/Filters'
          描述：>-
            通配符过滤器适用于网络上存在的所有各方
            参与者。过滤器的解释是相同的

            使用如上所述的每方过滤器。


            可选
        详细：
          描述：>-
            如果启用，通过 API 提供的值将包含更多信息
            超出了解释数据所必需的范围。

            特别是，将 verbose 标志设置为 true 会触发分类帐
            包括记录字段的标签。


            可选
          类型：布尔值
    活动：
      标题： 活动
      描述：|-
        交易中的事件可以有两种主要形式：

        - ACS delta：事件可以是 CreatedEvent 或 ArchivedEvent
        - 账本效应：事件可以是CreatedEvent或ExercusedEvent在更新服务中，事件仅限于事件
        对于交易过滤器中指定的各方可见。每个
        下面的事件消息类型包含一个“`witness_parties`”字段，其中
        指示可以看到事件的请求方的子集
        有问题。
      其中之一：
        - 类型：对象
          需要：
            - 存档事件
          属性：
            存档事件：
              $ref: '#/components/schemas/ArchivedEvent'
        - 类型：对象
          需要：
            - 创建事件
          属性：
            创建事件：
              $ref: '#/components/schemas/CreatedEvent'
        - 类型：对象
          需要：
            - 锻炼事件
          属性：
            行使事件：
              $ref: '#/components/schemas/ExercisedEvent'
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
    创建和练习命令：
      标题：CreateAndExerciseCommand
      描述：创建合约并在同一交易中对其行使选择权。
      类型：对象
      需要：
        - 模板ID
        - 创建参数
        - 选择
        - 选择论证
      属性：
        模板ID：
          描述：>-
            客户想要创建的合同模板。

            package-name 和 package-id 引用标识符格式
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        创建参数：
          描述：|-
            从此模板创建合同所需的参数。

            必填
        选择：
          描述：|-
            客户想要行使的选择的名称。
            必须是有效的名称字符串（如``value.proto``中所述）。

            必填
          类型：字符串
        选择参数：
          描述：|-
            这一选择的论据。

            必填
    创建命令：
      标题：创建命令
      描述：根据模板创建新的合约实例。
      类型：对象
      需要：
        - 模板ID
        - 创建参数
      属性：
        模板ID：
          描述：>-
            客户想要创建的合同模板。package-name 和 package-id 引用标识符格式
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        创建参数：
          描述：|-
            从此模板创建合同所需的参数。

            必填
    通过按键命令进行练习：
      标题：通过按键命令进行练习
      描述：对由其密钥指定的现有合约进行选择。
      类型：对象
      需要：
        - 模板ID
        - 合约密钥
        - 选择
        - 选择论证
      属性：
        模板ID：
          描述：>-
            客户想要行使的合同模板。

            package-name 和 package-id 引用标识符格式
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        合约密钥：
          描述：|-
            客户想要执行的合约的密钥。

            必填
        选择：
          描述：|-
            客户想要行使的选择的名称。
            必须是有效的名称字符串（如``value.proto``中所述）

            必填
          类型：字符串
        选择参数：
          描述：|-
            这一选择的论据。

            必填
    练习命令：
      标题：演习指挥
      描述：对现有合同进行选择。
      类型：对象
      需要：
        - 模板ID
        - 合约ID
        - 选择
        - 选择论证
      属性：
        模板ID：
          描述：>-
            客户想要的合同模板或界面
            锻炼。

            package-name 和 package-id 引用标识符格式
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。

            要对接口进行选择，请指定接口
            template_id 字段中的标识符。


            必填
          类型：字符串
        合约编号：
          描述：|-
            客户想要执行的合约的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。必填
          类型：字符串
        选择：
          描述：|-
            客户想要行使的选择的名称。
            必须是有效的名称字符串（如``value.proto``中所述）

            必填
          类型：字符串
        选择参数：
          描述：|-
            这一选择的论据。

            必填
    重复数据删除持续时间：
      标题：重复数据删除持续时间
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Duration'
    重复数据删除偏移量：
      标题：重复数据删除偏移
      类型：对象
      需要：
        - 价值
      属性：
        值：
          类型：整数
          格式：int64
    空：
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
    地图过滤器：
      标题：地图过滤器
      类型：对象
      附加属性：
        $ref: '#/components/schemas/Filters'
    过滤器：
      标题： 过滤器
      描述：>-
        一组模板过滤器、接口过滤器或
        通配符。
      类型：对象
      属性：
        累积：
          描述：>-
            累积列表中的每个过滤器都会扩展过滤器的范围
            产生的流。每个接口，

            模板或通配符过滤器意味着将匹配的其他事件
            查询。

            include_interface_view 和 include_created_event_blob 的影响
            过滤器中的字段将

            也得以积累。

            模板或界面不应在文档中出现两次
            累积场。

            通配符过滤器不应在
            累积场。

            如果没有定义``CumulativeFilter``，则默认单个
            ``WildcardFilter`` 与

            使用 include_created_event_blob 未设置。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/CumulativeFilter'
    存档事件：
      标题：存档事件
      描述：>-
        记录合同已存档，并且选项可能不再存在
        对它进行了锻炼。
      类型：对象
      需要：
        - 偏移量
        - 节点ID
        - 合约ID
        - 模板ID
        - 包名
        - 见证方
      属性：
        偏移量：
          描述：>-
            原点的偏移量。

            偏移量由参与节点管理。因此不能假设交易具有相同的偏移量
            不同的参与节点。

            它是一个有效的绝对偏移量（正整数）


            必填
          类型：整数
          格式：int64
        节点ID：
          描述：>-
            该事件在原始交易中的位置或
            重新分配。

            参与者之间的节点 ID 不一定相同，

            因为这些可能会看到不同的预测/交易部分。

            必须是有效的节点 ID（非负整数）


            必填
          类型：整数
          格式：int32
        合约编号：
          描述：|-
            已归档合同的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        模板ID：
          描述：>-
            标识定义存档选项的模板
            合同。

            该模板的 package-id 可能与目标合约的 package-id 不同
            包 ID

            目标合约是否已升级或降级。


            标识符使用 package-id 引用格式。


            必填
          类型：字符串
        见证方：
          描述：>-
            收到此事件通知的各方。对于一个
            ``ArchivedEvent``,

            这些是合同利益相关者的交集

            问题和``TransactionFilter``中指定的各方。的

            利益相关者是签署者和观察员的联盟

            合同。

            它的每个元素都必须是有效的 PartyIdString（如所述

            在``value.proto``中）。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        包名：
          描述：|-
            合约的包名。

            必填
          类型：字符串
        实现的接口：
          描述：>-
            目标模板实现的接口

            从接口过滤器查询中匹配。

            仅在使用 include_interface_view 进行接口过滤器的情况下填充
            设置。


            如果已定义，则标识符使用 package-id 引用格式。可选：可以为空
          类型：数组
          项目：
            类型：字符串
    创建事件：
      标题：创建事件
      描述：>-
        记录合同已创建，现在可以进行选择
        对它进行了锻炼。
      类型：对象
      需要：
        - 偏移量
        - 节点ID
        - 合约ID
        - 模板ID
        - 创建于
        - 包名
        - 代表PackageId
        - acsDelta
        - 创建参数
        - 见证方
        - 签署者
      属性：
        偏移量：
          描述：>-
            origin的偏移量，有上下文含义，请参见
            包含 CreatedEvent 的消息中的描述。

            偏移量由参与节点管理。

            因此不能假设交易具有相同的偏移量
            不同的参与节点。

            它是一个有效的绝对偏移量（正整数）


            必填
          类型：整数
          格式：int64
        节点ID：
          描述：>-
            该事件在原始交易中的位置或
            重新分配。

            起源具有上下文含义，请参阅描述
            包含 CreatedEvent 的消息。

            参与者之间的节点 ID 不一定相同，

            因为这些可能会看到不同的预测/交易部分。

            必须是有效的节点 ID（非负整数）


            必填
          类型：整数
          格式：int32
        合约编号：
          描述：|-
            创建的合约ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        模板ID：
          描述：|-
            创建的合同模板。
            标识符使用 package-id 引用格式。

            必填
          类型：字符串
        合约密钥：
          描述：>-
            创建合约的密钥。

            当且仅当``template_id``定义了一个合约时才会设置
            关键。


            可选
        合约密钥哈希：
          描述：>-
            Contract_key 的哈希值。

            当且仅当 ``template_id`` 定义了一个合约时才会设置
            关键。


            可选：可以为空
          类型：字符串
        创建参数：
          描述：|-
            用于创建合同的参数。

            必填
        创建事件Blob：
          描述：>-
            合约创建事件有效负载的不透明表示
            转发作为命令一部分公开的合同到 API 服务器

            提交。


            可选：可以为空
          类型：字符串
        界面视图：
          描述：>-
            事务过滤器中指定的接口视图。

            包括每个接口的“`InterfaceView`”
            一个 ``InterfaceFilter`` 与


            - 本次活动“`witness_parties`”中的派对，

            - 这是通过该事件的模板实现的，

            - 并且设置了``include_interface_view``。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/JsInterfaceView'
        见证方：
          描述：>-
            收到此事件通知的各方。当``CreatedEvent``

            作为交易树或账本效应的一部分返回
            交易，这将包括所有

            ``TransactionFilter``中指定的各方是
            事件目击者

            （合同的利益相关者和所有被告知者
            祖先

            该参与者知道的创建操作的一部分）。

            如果作为 ACS 增量交易的一部分，这些将

            仅限于``TransactionFilter``中指定的所有各方
            那个

            是合同的利益相关者（即签字人或
            观察员）。

            如果``CreatedEvent``作为AssignedEvent的一部分返回，

            ActiveContract 或 IncompleteUnsigned （因此该事件与

            转让或取消转让）：这将包括各方

            ``TransactionFilter`` 是合约的利益相关者。


            阅读行为会创建对未托管方可见的事件

            为 Ledger API 提供服务的参与者节点上未定义。
            具体来说，

            既不保证参与节点将提供服务
            他们所有的

            在 ACS 流上创建事件，也不保证
            匹配存档

            为此类创建事件传递事件。


            对于大多数客户端来说这不是问题，因为他们只读取事件
            聚会

            托管在参与者节点上。如果您需要阅读事件

            对于可能无法始终在参与者上举办的聚会
            节点，

            通过设置订阅该方的“`TopologyEvent`”
            相应的

            ``UpdateFormat``。  使用这些事件，查询 ACS 的偏移量
            哪里的party 托管在参与者节点上，并忽略创建事件
            偏移量

            其中聚会不托管在参与者节点上。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        签署者：
          描述：|-
            本合同的签署人按照模板指定。

            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        观察员：
          描述：>-
            本合同明确指定的观察员
            模板或隐式作为选择控制器。

            该字段从不包含签署方。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        创建于：
          描述：|-
            创建合约的交易的账本有效时间。

            必填
          类型：字符串
        包名：
          描述：|-
            创建的合约的包名。

            必填
          类型：字符串
        代表PackageId:
          描述：>-
            参与者包存储中存在的包 ID
            对合约的参数进行类型检查。

            这可能与用于创建的模板的 package-id 不同
            合同。

            对于 Canton 3.4 之前创建的合约，该字段匹配
            合约的创建包id。


            注意：实验性的，服务器内部概念，不适用于客户端
            消费。如有更改，恕不另行通知。


            必填
          类型：字符串
        acsDelta：
          描述：>-
            此事件是否是相应 ACS_DELTA 形状的一部分
            流，

            因此，在跟踪合同活跃度时应考虑
            客户端。


            必填
          类型：布尔值
    行使事件：
      标题： 锻炼事件
      描述：记录对目标合约执行的选择。
      类型：对象
      需要：
        - 偏移量
        - 节点ID
        - 合约ID
        - 模板ID
        - 选择
        - 选择论证
        - 消耗
        - 最后的后代节点ID
        - 包名
        - acsDelta
        - 代理方
        - 见证方
      属性：
        偏移量：
          描述：>-
            原点的偏移量。

            偏移量由参与节点管理。

            因此不能假设交易具有相同的偏移量
            不同的参与节点。它是一个有效的绝对偏移量（正整数）


            必填
          类型：整数
          格式：int64
        节点ID：
          描述：>-
            该事件在原始交易中的位置或
            重新分配。

            参与者之间的节点 ID 不一定相同，

            因为这些可能会看到不同的预测/交易部分。

            必须是有效的节点 ID（非负整数）


            必填
          类型：整数
          格式：int32
        合约编号：
          描述：|-
            目标合约的ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        模板ID：
          描述：>-
            标识定义执行选择的模板。

            该模板的 package-id 可能与目标合约的 package-id 不同
            包 ID

            目标合约是否已升级或降级。


            标识符使用 package-id 引用格式。


            必填
          类型：字符串
        接口ID：
          描述：|-
            定义选择的接口（如果继承）。
            如果已定义，则标识符使用 package-id 引用格式。

            可选
          类型：字符串
        选择：
          描述：|-
            对目标合约行使的选择。
            必须是有效的名称字符串（如``value.proto``中所述）。

            必填
          类型：字符串
        选择参数：
          描述：|-
            所行使选择的论点。

            必填
        代理方：
          描述：>-
            行使选择权的各方。

            每个元素必须是有效的 PartyIdString（如中所述
            ``value.proto``)。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        消耗：
          描述：|-
            如果属实，目标合约可能不再被执行。

            必填
          类型：布尔值
        见证方：
          描述：>-
            收到此事件通知的各方。一个事件的目击者
            锻炼

            节点将取决于练习是否消耗。

            如果消费，见证人是利益相关者的联合体，

            这次事件的所有祖先的演员和所有知情者

            参与者知道。

            如果不消费，见证人就是签署者的联合体，

            这次事件的所有祖先的演员和所有知情者参与者知道。

            在这两种情况下，证人仅限于询问方，或
            不

            在使用anyParty 过滤器的情况下受到限制。

            请注意，参与者不一定是观察者

            以及利益相关者。当 a 的控制器

            使用“灵活控制器”指定选择，使用

            ``choice ... controller`` 语法，并且所述控制器不是

            明确标记为观察员。

            每个元素必须是有效的 PartyIdString（如中所述
            ``value.proto``)。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        最后后代节点 ID：
          描述：>-
            指定事件的节点 ID 的上限
            由于以下原因出现的同一交易

            这个``ExercisedEvent``。这允许明确识别
            以此为根的子树的所有成员

            节点。当所有后代节点都可以构建完整子树
            存在于流中。如果节点很重

            过滤后，只能确定一个节点是否在
            是否为后续子树。


            必填
          类型：整数
          格式：int32
        练习结果：
          描述：|-
            行使选择的结果。

            可选
        包名：
          描述：|-
            合约的包名。

            必填
          类型：字符串
        实现的接口：
          描述：>-
            如果事件正在消耗，则目标实现的接口
            已经有的模板

            从接口过滤器查询中匹配。

            仅在使用 include_interface_view 进行接口过滤器的情况下填充
            设置。


            标识符使用 package-id 引用格式。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        acsDelta：
          描述：>-
            此事件是否是相应 ACS_DELTA 形状的一部分
            流，

            因此，在跟踪合同活跃度时应考虑
            客户端。


            必填
          类型：布尔值
    地图内部字段：
      标题：Map_Int_Field
      类型：对象
      附加属性：
        $ref: '#/components/schemas/Field'
    累积过滤器：
      标题：累积过滤器
      描述：>-
        一个过滤器，匹配所有合同，这些合同要么是一个实例
        的``template_filters`` or that match one of the ``interface_filters``。
      类型：对象
      属性：
        标识符过滤器：
          $ref: '#/components/schemas/IdentifierFilter'
    JsInterfaceView：
      标题：JsInterfaceView
      描述：接口过滤器匹配的创建事件的视图。
      类型：对象
      需要：
        - 接口ID
        - 查看状态
      属性：
        接口ID：
          描述：|-
            匹配事件实现的接口。
            标识符使用 package-id 引用格式。

            必填
          类型：字符串
        查看状态：
          $ref: '#/components/schemas/JsStatus'
          描述：>-
            视图计算是否成功，如果没有，

            错误的原因。使用相同的规则报告错误

            错误代码和消息作为 API 返回的错误
            请求。


            必填
        查看值：
          描述：|-
            该事件的接口视图方法的值。
            设置是否在``InterfaceFilter``中请求，并且可以是
            计算成功。

            可选
        实现包 ID：
          描述：>-
            定义用于计算的接口实现的包
            的观点。

            可能与用于创建的包不同
            合同本身，

            因为合同参数可以使用升级或降级
            智能合约升级

            作为计算界面视图的一部分。

            如果视图计算成功则填充，否则为空。可选
          类型：字符串
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
    标识符过滤器：
      标题： 标识符过滤器
      描述：必填
      其中之一：
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty1'
        - 类型：对象
          需要：
            - 接口过滤器
          属性：
            接口过滤器：
              $ref: '#/components/schemas/InterfaceFilter'
        - 类型：对象
          需要：
            - 模板过滤器
          属性：
            模板过滤器：
              $ref: '#/components/schemas/TemplateFilter'
        - 类型：对象
          需要：
            - 通配符过滤器
          属性：
            通配符过滤器：
              $ref: '#/components/schemas/WildcardFilter'
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
    空1：
      标题： 空
      类型：对象
    接口过滤器：
      标题： 接口过滤器
      描述：此过滤器匹配实现特定接口的合约。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/InterfaceFilter1'
    模板过滤器：
      标题：模板过滤器
      描述：该过滤器匹配特定模板的合约。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/TemplateFilter1'
    通配符过滤器：
      标题：通配符过滤器
      描述：此过滤器匹配所有模板。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/WildcardFilter1'
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
        值解码：类型：字符串
    接口过滤器1：
      标题： 接口过滤器
      描述：此过滤器匹配实现特定接口的合约。
      类型：对象
      需要：
        - 接口ID
      属性：
        接口ID：
          描述：>-
            匹配合约必须实现的接口。

            ``interface_id``需要有效：对应接口
            应定义在

            查询时可用的包之一。

            包名称和包 ID 参考格式
            支持标识符。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        包括InterfaceView：
          描述：>-
            是否在合约中包含接口视图
            返回``CreatedEvent``。

            使用它可以在 API 中以统一的方式访问合约数据
            客户。


            可选
          类型：布尔值
        包括CreatedEventBlob：
          描述：>-
            返回值中是否包含``created_event_blob``
            ``CreatedEvent``。

            使用它来访问 API 中的合约创建事件负载
            客户

            将其作为具有未来命令的披露合同提交。


            可选
          类型：布尔值
    模板过滤器1：
      标题：模板过滤器
      描述：该过滤器匹配特定模板的合约。
      类型：对象
      需要：
        - 模板ID
      属性：
        模板ID：
          描述：>-
            其负载应包含在响应中的模板。

            ``template_id``需要有效：对应的模板应该
            被定义在

            查询时可用的包之一。

            包名称和包 ID 参考格式
            支持标识符。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        包括CreatedEventBlob：
          描述：>-
            返回值中是否包含``created_event_blob``
            ``CreatedEvent``。

            使用它来访问 API 客户端中的合约事件负载

            将其作为具有未来命令的披露合同提交。可选
          类型：布尔值
    通配符过滤器1：
      标题：通配符过滤器
      描述：此过滤器匹配所有模板。
      类型：对象
      属性：
        包括CreatedEventBlob：
          描述：>-
            返回值中是否包含``created_event_blob``
            ``CreatedEvent``。

            使用它来访问 API 中的合约创建事件负载
            客户

            将其作为具有未来命令的披露合同提交。


            可选
          类型：布尔值
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
