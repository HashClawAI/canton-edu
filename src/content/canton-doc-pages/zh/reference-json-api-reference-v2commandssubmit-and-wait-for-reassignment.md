---
title: "/v2/commands/submit-and-wait-for-reassignment"
slug: "reference-json-api-reference-v2commandssubmit-and-wait-for-reassignment"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandssubmit-and-wait-for-reassignment.md"
source_title: "/v2/commands/submit-and-wait-for-reassignment"
tags:
  - reference
  - json-api-reference
  - v2commandssubmit-and-wait-for-reassignment
---

# /v2/commands/submit-and-wait-for-reassignment

> 提交单个复合重新分配命令，等待其结果，并返回重新分配。
传播提交失败的 gRPC 错误。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/submit-and-wait-for-reassignment
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
  /v2/commands/提交并等待重新分配：
    帖子：
      摘要：/v2/commands/submit-and-wait-for-resignment
      描述：>-
        提交单个复合重新分配命令，等待其结果，
        并返回重新分配。

        传播提交失败的 gRPC 错误。
      操作 ID：postV2Commands提交并等待重新分配
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/SubmitAndWaitForReassignmentRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsSubmitAndWaitForReassignmentResponse'
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
    提交并等待重新分配请求：
      标题：提交并等待重新分配请求
      描述：此重新分配作为单个原子更新执行。
      类型：对象
      需要：
        - 重新分配命令
      属性：
        重新分配命令：
          $ref: '#/components/schemas/ReassignmentCommands'
          描述：|-
            要提交的重新分配命令。

            必填
        事件格式：
          $ref: '#/components/schemas/EventFormat'
          描述：>-
            如果未提供 event_format，结果将不包含任何事件。

            事件的结果，将初具规模
            TRANSACTION_SHAPE_ACS_DELTA。可选
    JsSubmitAndWaitForReassignmentResponse：
      标题：JsSubmitAndWaitForReassignmentResponse
      类型：对象
      需要：
        - 重新分配
      属性：
        重新分配：
          $ref: '#/components/schemas/JsReassignment'
          描述：>-
            由提交的重新分配导致的重新分配
            命令。

            重新分配可能不包含任何事件（请求条件结果
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
    重新分配命令：
      标题：重新分配命令
      类型：对象
      需要：
        - 命令ID
        - 提交者
        - 命令
      属性：
        工作流程ID：
          描述：|-
            该命令所属的账本工作流程的标识符。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            可选
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
        命令ID：
          描述：>-
            唯一标识该命令。

            三元组（user_id、提交者、command_id）构成变更
            预期账本变更的 ID。

            变更 ID 可用于匹配预期的账本变更
            以及他们所有的完成。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            必填
          类型：字符串
        提交者：
          描述：>-
            应代表其执行命令的一方。如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者

            代表指定方行事。

            必须是有效的 PartyIdString（如``value.proto``中所述）。


            必填
          类型：字符串
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
        命令：
          描述：|-
            此次重新分配的各个要素。必须非空。

            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/ReassignmentCommand'
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

            使用如上所述的每方过滤器。可选
        详细：
          描述：>-
            如果启用，通过 API 提供的值将包含更多信息
            超出了解释数据所必需的范围。

            特别是，将 verbose 标志设置为 true 会触发分类帐
            包括记录字段的标签。


            可选
          类型：布尔值
    Js重新分配：
      标题：Js重新分配
      描述：账本重新分配的完整视图。
      类型：对象
      需要：
        - 更新ID
        - 偏移量
        - 记录时间
        - 同步器ID
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
            导致此重新分配的命令的 ID。失踪
            对于除提交方之外的所有人
            参与者。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            可选
          类型：字符串
        工作流程ID：
          描述：>-
            重新分配命令提交时使用的工作流 ID。仅在以下情况下设置
            该命令的“`workflow_id`”已设置。

            必须是有效的 LedgerString（如“`value.proto`”中所述）。


            可选
          类型：字符串
        偏移量：
          描述：>-
            参与者的偏移量。该字段的详细信息描述于
            ``community/ledger-api/README.md``。

            必须是有效的绝对偏移量（正整数）。


            必填
          类型：整数
          格式：int64
        事件：
          描述：|-
            重新分配事件的集合。

            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/JsReassignmentEvent'
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
            原始提交。如果未提供，则会生成唯一的 ledger-api-server 跟踪
            将使用上下文

            相反。


            可选
        记录时间：
          描述：>-
            记录重新分配的时间。记录时间
            指源/目标

            分别用于取消分配/分配事件的同步器。


            必填
          类型：字符串
        同步器ID：
          描述：|-
            有效的同步器 ID。
            标识同步此重新分配的同步器。

            必填
          类型：字符串
        支付流量费用：
          描述：>-
            该参与节点为此支付的流量费用
            相应的（取消）分配请求。


            未设置的交易

            - 由另一位参与者发起

            - 通过维修服务离线启动

            - 在参与者开始提供流量费用之前处理
            账本 API

            - 作为非提交方查询过滤的一部分返回


            可选
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
    重新分配命令：
      标题：重新分配命令
      类型：对象
      属性：
        命令：
          $ref: '#/components/schemas/Command1'
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

            使用 include_created_event_blob 未设置。可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/CumulativeFilter'
    Js重新分配事件：
      标题：JsReassignmentEvent
      其中之一：
        - 类型：对象
          需要：
            - JsAssignmentEvent
          属性：
            JsAssignmentEvent：
              $ref: '#/components/schemas/JsAssignmentEvent'
        - 类型：对象
          需要：
            - JsUnassignedEvent
          属性：
            JsUnassignedEvent：
              $ref: '#/components/schemas/JsUnassignedEvent'
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
    命令1：
      标题：命令
      描述：>-
        命令可以创建新合约或对某个合约执行选择
        现有合同。
      其中之一：
        - 类型：对象
          需要：
            - 分配命令
          属性：
            分配命令：
              $ref: '#/components/schemas/AssignCommand'
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty2'
        - 类型：对象
          需要：
            - 取消分配命令
          属性：
            取消分配命令：
              $ref: '#/components/schemas/UnassignCommand'
    累积过滤器：
      标题：累积过滤器
      描述：>-
        一个过滤器，匹配所有合同，这些合同要么是一个实例
        的``template_filters`` or that match one of the ``interface_filters``。
      类型：对象
      属性：
        标识符过滤器：
          $ref: '#/components/schemas/IdentifierFilter'
    JsAssignmentEvent：
      标题：JsAssignmentEvent
      类型：对象
      需要：
        - 来源
        - 目标
        - 重新分配 ID
        - 提交者
        - 重新分配计数器
        - 创建事件
      属性：
        来源：
          类型：字符串
        目标：
          类型：字符串
        重新分配 ID：
          类型：字符串
        提交者：
          类型：字符串
        重新分配计数器：
          类型：整数
          格式：int64
        创建事件：
          $ref: '#/components/schemas/CreatedEvent'
    JsUnassignedEvent：
      标题：JsUnassignedEvent
      描述：>-
        记录合同已取消转让，并且在以下时间变得不可用
        源同步器
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/UnassignedEvent'
    分配命令：
      标题：分配命令
      描述：分配合同
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/AssignCommand1'
    空2：
      标题： 空
      类型：对象
    取消分配命令：
      标题：取消分配命令
      描述：取消分配合同
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/UnassignCommand1'
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
        - 见证方- 签署者
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
            转发

            作为命令一部分公开的合同到 API 服务器

            提交。


            可选：可以为空
          类型：字符串
        界面视图：
          描述：>-
            事务过滤器中指定的接口视图。

            包括每个接口的“`InterfaceView`”
            一个 ``InterfaceFilter`` 与


            - 本次活动‘`witness_parties`’的派对，

            - 这是通过该事件的模板实现的，- 并且设置了``include_interface_view``。


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
            哪里的

            party 托管在参与者节点上，并忽略创建事件
            偏移量

            其中聚会不托管在参与者节点上。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        签署者：
          描述：|-
            本合同的签署人按照模板指定。必填：必须非空
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
    未分配事件：
      标题：未分配事件
      描述：>-
        记录合同已取消转让，并且在以下时间变得不可用
        源同步器
      类型：对象
      需要：
        - 重新分配 ID
        - 合约ID
        - 来源
        - 目标
        - 重新分配计数器
        - 包名
        - 偏移量
        - 节点ID
        - 模板ID
        - 见证方
      属性：
        重新分配 ID：
          描述：>-
            取消分配的 ID。这需要用作
            分配重新分配命令。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            必填
          类型：字符串
        合约编号：
          描述：|-
            重新分配的合约的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        模板ID：
          描述：|-
            重新转让合同的模板。
            标识符使用 package-id 引用格式。必填
          类型：字符串
        来源：
          描述：|-
            源同步器ID
            必须是有效的同步器 ID

            必填
          类型：字符串
        目标：
          描述：|-
            目标同步器的ID
            必须是有效的同步器 ID

            必填
          类型：字符串
        提交者：
          描述：|-
            代表其执行取消分配命令的一方。
            如果通过维修服务离线取消分配，则为空。
            必须是有效的 PartyIdString（如``value.proto``中所述）。

            可选
          类型：字符串
        重新分配计数器：
          描述：>-
            每个对应的已分配和未分配事件具有相同的
            重新分配_计数器。这严格增加

            与同一合同的每个取消分配命令。的创建
            合约对应reassignment_counter

            等于零。


            必填
          类型：整数
          格式：int64
        分配排他性：
          描述：>-
            转让排他性

            在此时间之前（在目标同步器上测量），仅
            取消分配的提交者可以发起分配

            定义用于重新分配参与者。


            可选
          类型：字符串
        见证方：
          描述：|-
            收到此事件通知的各方。

            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        包名：
          描述：|-
            合约的包名。

            必填
          类型：字符串
        偏移量：
          描述：>-
            原点的偏移量。

            偏移量由参与节点管理。

            因此不能假设重新分配具有相同的偏移量
            不同的参与节点。

            必须是有效的绝对偏移量（正整数）


            必填
          类型：整数
          格式：int64
        节点ID：
          描述：|-
            此事件在原始重新分配中的位置。
            参与者之间的节点 ID 不一定相同，
            因为这些可能会看到不同的预测/部分重新分配。
            必须是有效的节点 ID（非负整数）必填
          类型：整数
          格式：int32
    分配命令1：
      标题：分配命令
      描述：分配合同
      类型：对象
      需要：
        - 重新分配 ID
        - 来源
        - 目标
      属性：
        重新分配 ID：
          描述：|-
            此分配要完成的未分配事件的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        来源：
          描述：|-
            源同步器ID
            必须是有效的同步器 ID

            必填
          类型：字符串
        目标：
          描述：|-
            目标同步器的ID
            必须是有效的同步器 ID

            必填
          类型：字符串
    取消分配命令1：
      标题：取消分配命令
      描述：取消分配合同
      类型：对象
      需要：
        - 合约ID
        - 来源
        - 目标
      属性：
        合约编号：
          描述：|-
            客户端想要取消分配的合约的 ID。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        来源：
          描述：|-
            源同步器ID
            必须是有效的同步器 ID

            必填
          类型：字符串
        目标：
          描述：|-
            目标同步器的ID
            必须是有效的同步器 ID必填
          类型：字符串
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
            设置是否在``InterfaceFilter``中请求，可以是
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

            如果视图计算成功则填充，否则为空。


            可选
          类型：字符串
    接口过滤器1：
      标题： 接口过滤器
      描述：此过滤器匹配实现特定接口的合约。
      类型：对象
      需要：
        - 接口ID
      属性：
        接口ID：
          描述：>-
            匹配合约必须实现的接口。``interface_id``需要有效：对应接口
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

            将其作为具有未来命令的披露合同提交。


            可选
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
            客户将其作为具有未来命令的披露合同提交。


            可选
          类型：布尔值
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
