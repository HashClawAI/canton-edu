---
title: "/v2/updates/transaction-tree-by-id/{update-id}"
slug: "reference-json-api-reference-v2updatestransaction-tree-by-id"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2updatestransaction-tree-by-id.md"
source_title: "/v2/updates/transaction-tree-by-id/{update-id}"
tags:
  - reference
  - json-api-reference
  - v2updatestransaction-tree-by-id
---

# /v2/updates/transaction-tree-by-id/{update-id}

> 通过id获取交易树。为了向后兼容，它将在 Canton 版本 3.5.0 中删除，使用 v2/updates/update-by-id 代替。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/updates/transaction-tree-by-id/{update-id}
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
    最新 Canton 3.4 补丁版本的规范。MINIMUM_CANTON_VERSION=3.5.0
服务器：[]
安全：[]
路径：
  /v2/updates/transaction-tree-by-id/{update-id}：
    得到：
      摘要：/v2/updates/transaction-tree-by-id/{update-id}
      描述：>-
        通过id获取交易树。提供向后兼容性，它
        将在 Canton 3.5.0 版本中删除，使用 v2/updates/update-by-id
        相反。
      操作Id：getV2UpdatesTransaction-tree-by-idUpdate-id
      参数：
        - 名称：更新 ID
          在：路径
          必填：真实
          架构：
            类型：字符串
        - 名称：派对
          在：查询
          必填：假
          架构：
            类型：数组
            项目：
              类型：字符串
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsGetTransactionTreeResponse'
        “400”：
          描述：“值无效，值无效：查询参数各方”
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
      已弃用：true
      安全：
        - httpAuth: []
        - apiKeyAuth: []
组件：
  模式：
    JsGetTransactionTreeResponse：
      标题：JsGetTransactionTreeResponse
      描述：>-
        提供向后兼容性，它将在 Canton 中删除
        版本 3.5.0。
      类型：对象
      需要：
        - 交易
      属性：
        交易：
          $ref: '#/components/schemas/JsTransactionTree'
          描述：必填
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
    Js事务树：
      标题：JsTransactionTree
      描述：>-
        提供向后兼容性，它将在 Canton 中删除
        版本 3.5.0。账本交易的完整视图。
      类型：对象
      需要：
        - 更新ID
        - 有效
        - 偏移量
        - eventsById
        - 同步器ID
        - 记录时间
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
          描述：>-
            命令提交中使用的工作流 ID。仅当设置
            命令的“`workflow_id`”已设置。

            必须是有效的 LedgerString（如“`value.proto`”中所述）。

            可选
          类型：字符串
        有效于：
          描述：|-
            账本有效时间。
            必填
          类型：字符串
        偏移量：
          描述：>-
            绝对偏移量。该字段的详细信息描述于
            ``community/ledger-api/README.md``。

            必填，它是一个有效的绝对偏移量（正整数）。
          类型：整数
          格式：int64
        eventsById:
          $ref: '#/components/schemas/Map_Int_TreeEvent'
          描述：>-
            由该交易引起的账本变更。的节点
            交易树。

            每个键必须是有效的节点 ID（非负整数）。

            必填
        同步器ID：
          描述：|-
            有效的同步器 ID。
            标识同步事务的同步器。
            必填
          类型：字符串
        跟踪上下文：
          $ref: '#/components/schemas/TraceContext'
          描述：>-
            可选；账本 API 跟踪上下文


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
            将使用上下文反而。
        记录时间：
          描述：>-
            记录交易的时间。记录时间
            指的是同步器

            这同步了事务。

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
    Map_Int_TreeEvent：
      标题：Map_Int_TreeEvent
      类型：对象
      附加属性：
        $ref: '#/components/schemas/TreeEvent'
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
    树事件：
      标题： 树事件
      描述：>-
        提供向后兼容性，它将在 Canton 中删除
        版本 3.5.0。

        下面的每个树事件消息类型都包含一个“`witness_parties`”字段
        其中

        指示可以看到事件的请求方的子集

        有问题。


        请注意，事务树可能包含以下事件：

        _没有_证人方，将其包括在内只是因为他们是有目击者的事件的孩子。
      其中之一：
        - 类型：对象
          需要：
            - 创建树事件
          属性：
            创建树事件：
              $ref: '#/components/schemas/CreatedTreeEvent'
        - 类型：对象
          需要：
            - 练习树事件
          属性：
            锻炼树事件：
              $ref: '#/components/schemas/ExercisedTreeEvent'
    创建树事件：
      标题：CreateTreeEvent
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/CreatedEvent'
    锻炼树事件：
      标题：ExercedTreeEvent
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/ExercisedEvent'
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
            标识符使用 package-id 引用格式。必填
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

            当且仅当``template_id``定义了一个合约时才会设置
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


            阅读行为会创建对未托管方可见的事件为 Ledger API 提供服务的参与者节点上未定义。
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
            流，因此，在跟踪合同活跃度时应考虑
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
            ``value.proto``)。必填：必须非空
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

            这次事件的所有祖先的演员和所有知情者

            参与者知道。

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

            从接口过滤器查询中匹配。仅在使用 include_interface_view 进行接口过滤器的情况下填充
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

            如果视图计算成功则填充，否则为空。可选
          类型：字符串
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
