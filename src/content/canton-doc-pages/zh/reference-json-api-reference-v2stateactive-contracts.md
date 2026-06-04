---
title: "/v2/state/active-contracts"
slug: "reference-json-api-reference-v2stateactive-contracts"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateactive-contracts.md"
source_title: "/v2/state/active-contracts"
tags:
  - reference
  - json-api-reference
  - v2stateactive-contracts
---

# /v2/state/active-contracts

> 查询活跃合约列表（阻塞调用）。
查询活动合约是一项昂贵的操作，如果可能的话，不应经常重复。
考虑首先查询活动合约（对于给定的偏移量）
然后重复调用`/v2/updates/...`端点之一以获取后续修改。
您还可以使用 websockets 来获取具有更好性能的更新。

返回活动合约的快照流以及分类帐偏移处的不完整（未）分配。
一旦 GetActiveContractsResponses 流完成，
客户端应该开始从更新服务流式传输更新，
从此请求中指定的 GetActiveContractsRequest.active_at_offset 开始。
客户不应该假设他们收到的一组活跃合约反映了账本端的状态。

注意：此端点应用于小结果集。
当结果数量超过节点配置限制时（`http-list-max-elements-limit`）
将会返回一个错误（`413 Content Too Large`）。
增加此限制可能会导致性能问题和高内存消耗。
考虑使用 websockets (asyncapi) 以获得更高的效率和更大的结果。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/state/active-contracts
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
  /v2/state/active-contracts：
    帖子：
      摘要：/v2/state/active-contracts
      描述：>-
        查询活跃合约列表（阻塞调用）。

        查询活动合约是一项昂贵的操作，如果可能的话
        不应经常重复。

        考虑首先查询活动合约（对于给定的偏移量）

        然后重复调用`/v2/updates/...`端点之一来获取
        后续修改。

        您还可以使用 websockets 来获取具有更好性能的更新。


        返回活动合约和不完整合约的快照流
        分类账抵销的（un）分配。

        一旦 GetActiveContractsResponses 流完成，

        客户端应该开始从更新服务流式传输更新，

        从 GetActiveContractsRequest.active_at_offset 中指定的位置开始
        这个请求。客户不应假设他们收到的一组有效合约
        反映账本端的状态。


        注意：此端点应用于小结果集。

        当结果数量超过节点配置限制时
        (`http-list-max-elements-limit`)

        将会返回一个错误（`413 Content Too Large`）。

        增加此限制可能会导致性能问题和内存占用过高
        消费。

        考虑使用 websockets (asyncapi) 来提高更大的效率
        结果。
      操作 ID：postV2StateActive-contracts
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
              $ref: '#/components/schemas/GetActiveContractsRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                类型：数组
                项目：
                  $ref: '#/components/schemas/JsGetActiveContractsResponse'
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
    获取活动合同请求：
      标题：获取活动合同请求
      描述：>-
        如果给定的偏移量与账本端不同，并且有
        (un)在给定偏移量处进行中的分配，

        快照可能会失败
        “FAILED_PRECONDITION/PARTICIPANT_PRUNED_DATA_ACCESSED”。

        请注意，可以使用以下命令请求 acs 快照以进行参与方迁移
        除账本末端以外的抵消，因为一方迁移与不完整（un）的分配无关。
      类型：对象
      需要：
        - activeAtOffset
      属性：
        过滤器：
          $ref: '#/components/schemas/TransactionFilter'
          描述：>-
            提供向后兼容性，它将在
            Canton版本3.5.0。

            每方包含在所提供的快照中的模板。

            可选，如果指定则必须取消设置 event_format，如果未指定
            必须设置 event_format。
        详细：
          描述：>-
            提供向后兼容性，它将在
            Canton版本3.5.0。

            如果启用，通过 API 提供的值将包含更多信息
            超出了解释数据所必需的范围。

            特别是，将 verbose 标志设置为 true 会触发分类帐
            包括记录字段的标签。

            可选，如果指定了 event_format 则必须取消设置。
          类型：布尔值
        活动偏移量：
          描述：>-
            活动合约快照的偏移量
            计算出来的。

            不得大于当前账本结束偏移量。

            必须大于或等于上次修剪偏移量。

            必须是有效的绝对偏移量（正整数）或分类帐开始
            偏移量（零）。

            如果为零，则返回空集。


            必填
          类型：整数
          格式：int64
        事件格式：
          $ref: '#/components/schemas/EventFormat'
          描述：>-
            结果中的contract_entries 的格式。如果出现以下情况
            CreatedEvent 演示文稿将是

            TRANSACTION_SHAPE_ACS_DELTA。

            为了向后兼容，可选，默认为 EventFormat
            其中：


            -filters_by_party 是来自此请求的filter.filters_by_party

            -filters_for_any_party 是来自的filter.filters_for_any_party
            这个请求

            - verbose 是此请求的详细字段
        流连续令牌：
          描述：>-
            定义位置的连续标记的不透明表示
            活跃合约快照。

            活动合约快照的前缀将被省略
            并包括其中的元素

            读取了继续标记。

            重用来自 a 的继续令牌
            `GetActiveContractsPageResponse`：


            - 后续请求必须在同一参与者上执行
            相同版本的Canton，- 后续请求必须具有相同的 active_at_offset，

            - 后续请求必须具有相同的 event_format

            - 并且参与者不得在之后被修剪
            active_at_offset。


            如果未指定，则整个活跃合约快照将是
            回来了。


            可选：可以为空
          类型：字符串
    JsGetActiveContractsResponse：
      标题：JsGetActiveContractsResponse
      类型：对象
      属性：
        工作流程ID：
          描述：>-
            命令提交时使用的工作流ID，对应于
            合同条目。仅在以下情况下设置

            该命令的“`workflow_id`”已设置。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            可选
          类型：字符串
        合约条目：
          $ref: '#/components/schemas/JsContractEntry'
        流连续令牌：
          描述：>-
            连续标记的不透明表示，可用于
            绕过已处理部分的请求

            活动合约快照。

            仅针对流式“`GetActiveContracts`”rpc 调用进行填充。


            可选：可以为空
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
    交易过滤器：
      标题：交易过滤器
      描述：>-
        提供向后兼容性，它将在 Canton 中删除
        版本 3.5.0。

        用于过滤创建和归档事件以及
        过滤事务树。
      类型：对象
      属性：
        按方筛选：
          $ref: '#/components/schemas/Map_Filters'
          描述：>-
            每个键必须是有效的 PartyIdString（如中所述
            ``value.proto``)。

            过滤器的解释取决于交易形状
            正在过滤：1. 对于**事务树**（在 GetUpdateTreesResponse 中使用）
            向后兼容）所有参与方密钥用作
               通配符过滤器，并返回其根具有列出的各方之一作为被通知者的所有子树。
               如果适用时存在“`CumulativeFilter``s, those will control returned ``CreatedEvent`”字段，但将
               不能用于模板/接口过滤。
            2. 对于**账本效应**，返回创建和执行事件，
            证人至少包括以下之一
               列出的各方并匹配每方过滤器。
            3. 对于 **交易和活动合约集流** 创建并
            为所有合约返回存档事件
               利益相关者至少包括列出的各方之一并匹配每方过滤器。
        过滤器ForAnyParty：
          $ref: '#/components/schemas/Filters'
          描述：>-
            通配符过滤器适用于网络上存在的所有各方
            参与者。过滤器的解释是相同的

            使用如上所述的每方过滤器。
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
    JsContractEntry：
      标题：JsContractEntry
      描述：>-
        对于一个合约来说，整个合约中可能有多个contract_entry-s
        快照。这些共同定义了

        快照中一份合约的状态。

        当且仅当存在 at 时，contract_entry 才会包含在结果中
        合同的至少一个利益相关方

        事件发生时托管在同步器上
        当事人满足

        查询中的“`TransactionFilter`”。


        必填
      其中之一：
        - 类型：对象
          需要：
            - JsActiveContract
          属性：
            JsActiveContract：
              $ref: '#/components/schemas/JsActiveContract'
        - 类型：对象
          需要：
            - JsEmpty
          属性：
            Js空：
              $ref: '#/components/schemas/JsEmpty'
        - 类型：对象
          需要：
            - Js不完整分配
          属性：
            JsIncompleteAssigned：
              $ref: '#/components/schemas/JsIncompleteAssigned'
        - 类型：对象
          需要：
            - JsIncomplete未分配
          属性：
            JsIncomplete未分配：
              $ref: '#/components/schemas/JsIncompleteUnassigned'
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
            累积场。通配符过滤器不应在
            累积场。

            如果没有定义``CumulativeFilter``，则默认单个
            ``WildcardFilter`` 与

            使用 include_created_event_blob 未设置。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/CumulativeFilter'
    JsActiveContract：
      标题：JsActiveContract
      类型：对象
      需要：
        - 创建事件
        - 同步器ID
        - 重新分配计数器
      属性：
        创建事件：
          $ref: '#/components/schemas/CreatedEvent'
          描述：>-
            该事件出现在其上次更新的上下文中（即
            daml 交易或

            重新分配）。特别是，最后一个偏移量，node_id 对是
            保存下来。

            最后更新是创建或分配给此的最新更新
            同步器_id 同步器上的合约。

            CreatedEvent 的偏移量可能指向已修剪的事件
            更新，因此不一定可以使用

            用于查找。


            必填
        同步器ID：
          描述：|-
            有效的同步器 ID

            必填
          类型：字符串
        重新分配计数器：
          描述：>-
            每个对应的已分配和未分配事件具有相同的
            重新分配_计数器。这严格增加

            与同一合同的每个取消分配命令。的创建
            合约对应reassignment_counter

            等于零。

            该字段将是最新可观察值的reassignment_counter
            该同步器上的激活事件，即

            在 active_at_offset 之前。


            必填
          类型：整数
          格式：int64
    Js空：
      标题：JsEmpty
      类型：对象
    JsIncompleteAssigned：
      标题：JsIncompleteAssigned
      类型：对象
      需要：
        - 指定事件
      属性：
        分配事件：
          $ref: '#/components/schemas/JsAssignedEvent'
          描述：必填
    JsIncomplete未分配：
      标题：JsIncompleteUnassigned
      类型：对象
      需要：
        - 创建事件
        - 未分配事件
      属性：
        创建事件：
          $ref: '#/components/schemas/CreatedEvent'
          描述：>-
            上次激活时出现的事件
            更新（即 daml 事务或

            重新分配）。特别是最后一个激活偏移量，node_id
            对被保留。最后的激活更新是最近创建的更新或
            之前在同步器_id同步器上分配了这个合约

            未分配的事件。

            CreatedEvent 的偏移量可能指向已修剪的事件
            更新，因此不一定可以使用

            用于查找。


            必填
        未分配事件：
          $ref: '#/components/schemas/UnassignedEvent'
          描述：必填
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
            必须是有效的 LedgerString（如“`value.proto`”中所述）。

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
    JsAssignedEvent：
      标题：JsAssignedEvent
      描述：>-
        记录合同已被分配，并且可以在
        目标同步器。
      类型：对象
      需要：
        - 来源
        - 目标
        - 重新分配 ID
        - 重新分配计数器
        - 创建事件
      属性：
        来源：
          描述：|-
            源同步器的ID。
            必须是有效的同步器 ID。

            必填
          类型：字符串
        目标：
          描述：|-
            目标同步器的ID。
            必须是有效的同步器 ID。

            必填
          类型：字符串
        重新分配 ID：
          描述：|-
            未分配事件的 ID。
            对于关联能力。
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        提交者：
          描述：|-
            代表其执行分配命令的一方。
            如果通过维修服务离线进行分配，则为空。
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
        创建事件：
          $ref: '#/components/schemas/CreatedEvent'
          描述：|-
            该事件的偏移量指的是赋值的偏移量，
            而node_id是批次内的索引。

            必填
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
            分配重新分配命令。必须是有效的 LedgerString（如``value.proto``中所述）。


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
            标识符使用 package-id 引用格式。

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

            必须是有效的绝对偏移量（正整数）必填
          类型：整数
          格式：int64
        节点ID：
          描述：|-
            此事件在原始重新分配中的位置。
            参与者之间的节点 ID 不一定相同，
            因为这些可能会看到不同的预测/部分重新分配。
            必须是有效的节点 ID（非负整数）

            必填
          类型：整数
          格式：int32
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

            将其作为具有未来命令的披露合同提交。可选
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
            客户

            将其作为具有未来命令的披露合同提交。可选
          类型：布尔值
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
