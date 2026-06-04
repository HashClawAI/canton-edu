---
title: "/v2/commands/async/submit"
slug: "reference-json-api-reference-v2commandsasyncsubmit"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandsasyncsubmit.md"
source_title: "/v2/commands/async/submit"
tags:
  - reference
  - json-api-reference
  - v2commandsasyncsubmit
---

# /v2/commands/async/submit

> 提交单个复合命令。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/async/submit
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
  /v2/命令/异步/提交：
    帖子：
      摘要：/v2/commands/async/submit
      描述：提交单个复合命令。
      操作 ID：postV2CommandsAsyncSubmit
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/JsCommands'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/SubmitResponse'
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

            必须是有效的 LedgerString（如``value.proto``中所述）。必填
          类型：字符串
        充当：
          描述：>-
            应代表其执行命令的一组各方。

            如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者

            代表每一方行事。

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
            花费相当多的时间，这样通过结果交易被排序的时间，其分配的分类账
            时间不再有效。

            不得与 min_ledger_time_rel 同时设置。


            可选
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
            配置。提供的值不得超过规定的限制
            参与者配置。


            可选
          类型：整数
          格式：int32
    提交回复：
      标题：提交回复
      类型：对象
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
            客户想要创建的合同模板。

            package-name 和 package-id 引用标识符格式
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        创建参数：
          描述：|-
            从此模板创建合同所需的参数。必填
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
            必须是有效的 LedgerString（如``value.proto``中所述）。

            必填
          类型：字符串
        选择：
          描述：|-
            客户想要行使的选择的名称。
            必须是有效的名称字符串（如``value.proto``中所述）

            必填
          类型：字符串
        选择参数：
          描述：|-
            这一选择的论据。必填
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
