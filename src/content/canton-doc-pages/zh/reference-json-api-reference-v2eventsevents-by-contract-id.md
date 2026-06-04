---
title: "/v2/events/events-by-contract-id"
slug: "reference-json-api-reference-v2eventsevents-by-contract-id"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2eventsevents-by-contract-id.md"
source_title: "/v2/events/events-by-contract-id"
tags:
  - reference
  - json-api-reference
  - v2eventsevents-by-contract-id
---

# /v2/events/events-by-contract-id

> 获取具有提供的 ID 的合约的创建和消费执行事件。
对于已被修剪的合约，不会返回任何事件，因为它们
在最新的修剪偏移之前已经存档。
如果找不到请求的合约，或者过滤了所有合约事件，则会引发 CONTRACT_EVENTS_NOT_FOUND 错误。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/events/events-by-contract-id
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
  /v2/events/events-by-contract-id：
    帖子：
      摘要：/v2/events/events-by-contract-id
      描述：>-
        获取合约的创建和消费执行事件
        提供的 ID。

        对于已被修剪的合约，不会返回任何事件，因为
        他们

        在最新的修剪偏移之前已经存档。

        如果找不到该请求的合同，或者所有
        合约事件被过滤，将会出现 CONTRACT_EVENTS_NOT_FOUND 错误
        提出。
      操作Id：postV2EventsEvents-by-contract-id
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/GetEventsByContractIdRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsGetEventsByContractIdResponse'
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
    通过ContractIdRequest获取事件：
      标题：GetEventsByContractIdRequest
      类型：对象
      需要：
        - 合约ID
        - 事件格式
      属性：
        合约编号：
          描述：|-
            正在查询的合约id。必填
          类型：字符串
        事件格式：
          $ref: '#/components/schemas/EventFormat'
          描述：>-
            结果中事件的格式，演示文稿将是
            TRANSACTION_SHAPE_ACS_DELTA。


            必填
    JsGetEventsByContractIdResponse：
      标题：JsGetEventsByContractIdResponse
      类型：对象
      属性：
        创建：
          $ref: '#/components/schemas/JsCreated'
          描述：>-
            合约的创建事件，其中给出了“`contract_id`”
            请求

            前提是它存在并且尚未被修剪。


            可选
        存档：
          $ref: '#/components/schemas/JsArchived'
          描述：>-
            具有“`contract_id`”的合约的归档事件，如下所示
            请求

            前提是这样的存档事件存在并且尚未被
            修剪过的。


            可选
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
            正在过滤：1. 对于 **ledger-effects** 返回创建和执行事件，
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
    Js创建：
      标题：JsCreated
      类型：对象
      需要：
        - 创建事件
        - 同步器ID
      属性：
        创建事件：
          $ref: '#/components/schemas/CreatedEvent'
          描述：>-
            该事件出现在其原始更新的上下文中（即
            daml 交易或

            重新分配）在此参与者节点上。您可以使用它的偏移量和
            查找node_id

            相应的更新及其中的节点。


            必填
        同步器ID：
          描述：|-
            对合约创建进行排序的同步器

            必填
          类型：字符串
    Js存档：
      标题：JsArchive
      类型：对象
      需要：
        - 存档事件
        - 同步器ID
      属性：
        存档事件：
          $ref: '#/components/schemas/ArchivedEvent'
          描述：必填
        同步器ID：
          描述：|-
            对合同存档进行排序的同步器必填
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
            包含 CreatedEvent 的消息。参与者之间的节点 ID 不一定相同，

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

            如果作为 ACS 增量交易的一部分，这些将仅限于``TransactionFilter``中指定的所有各方
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
            对合约的参数进行类型检查。这可能与用于创建的模板的 package-id 不同
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

            问题和``TransactionFilter``中指定的各方。这利益相关者是签署者和观察员的联盟

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


            如果已定义，则标识符使用 package-id 引用格式。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
    累积过滤器：
      标题：累积过滤器
      描述：>-
        一个过滤器，匹配所有合同，这些合同要么是一个实例
        的

        ``template_filters`` or that match one of the ``interface_filters``。
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

            作为计算界面视图的一部分。如果视图计算成功则填充，否则为空。


            可选
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
        值解码：
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
