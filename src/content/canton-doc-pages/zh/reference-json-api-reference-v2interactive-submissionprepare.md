---
title: "/v2/interactive-submission/prepare"
slug: "reference-json-api-reference-v2interactive-submissionprepare"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionprepare.md"
source_title: "/v2/interactive-submission/prepare"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionprepare
---

# /v2/interactive-submission/prepare

> 当启用LAPI用户授权时，需要提交方的`readAs`范围



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/prepare
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
  /v2/交互式提交/准备：
    帖子：
      摘要：/v2/交互式提交/准备
      描述：>-
        当 LAPI 用户时，提交方需要`readAs`范围
        授权已启用
      操作Id：postV2Interactive-submissionPrepare
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/JsPrepareSubmissionRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/JsPrepareSubmissionResponse'
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
    JsPrepareSubmissionRequest：
      标题：JsPrepareSubmissionRequest
      类型：对象
      需要：
        - 命令ID
        - 命令
        - 充当
      属性：
        用户ID：
          描述：>-
            唯一标识准备的参与用户
            交易。

            必须是有效的 UserIdString（如``value.proto``中所述）。

            除非使用用户令牌进行身份验证，否则是必需的。

            在这种情况下，令牌的用户 ID 将用于请求的
            用户 ID。


            可选
          类型：字符串
        命令ID：
          描述：>-
            唯一标识该命令。

            三元组(user_id, act_as, command_id)构成变更ID
            对于预期的账本变更，

            其中 act_as 被解释为一组参与方名称。变更 ID 可用于匹配预期的账本变更
            以及他们所有的完成。

            必须是有效的 LedgerString（如``value.proto``中所述）。


            必填
          类型：字符串
        命令：
          描述：>-
            该原子命令的各个元素。必须非空。

            限制：目前仅支持单命令事务
            通过 API。

            该字段被标记为重复，以准备将来的支持
            多个命令。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/Command'
        最短账本时间：
          $ref: '#/components/schemas/MinLedgerTime'
          描述：可选
        充当：
          描述：>-
            应代表其执行命令的各方集合，如果
            已提交。

            如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者

            代表每一方**阅读**（而非行动）。这个
            是因为这个 RPC 只是准备一个事务

            并且不执行它。因此读取授权就足够了
            即使对于行动方来说也是如此。

            注意：这可能会改变，更具体的授权范围可能是
            未来会介绍。

            每个元素必须是有效的 PartyIdString（如中所述
            ``value.proto``)。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        读作：
          描述：>-
            代表其的一组各方（除了列表中列出的所有各方之外）
            ``act_as``) 合约可以检索。

            这会影响Daml操作，例如``fetch``, ``fetchByKey``，
            ``lookupByKey``, ``exercise``, and ``exerciseByKey``。

            注意：命令只能使用至少对以下人员可见的合约

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
        披露的合同：
          描述：>-
            用于解析合同和合同密钥的附加合同
            查找。可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/DisclosureContract'
        同步器ID：
          描述：>-
            必须是有效的同步器 ID

            如果未设置，则该节点连接到的合适同步器
            将被选择


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
        详细哈希：
          描述：>-
            如果为真，响应将包含有关如何
            交易被编码和散列

            这对于解决哈希不匹配问题很有用。应该
            仅用于调试。

            默认为 false


            可选
          类型：布尔值
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
        最大记录时间：
          描述：>-
            交易可以记录到的最大时间戳
            通过指定的同步器进行分类帐
            `PrepareSubmissionResponse`。

            如果在此之后提交，即使其他方面有效，也会被拒绝
            哪种情况需要重新准备并签字

            具有新的有效 max_record_time。

            使用它来限制准备好的交易的生命周期，

            知道什么时候绝对不能接受是有用的

            不再并诉诸于为同一交易准备另一笔交易

            意图再次安全。


            可选
          类型：字符串
        预估交通费用：
          $ref: '#/components/schemas/CostEstimationHints'
          描述：>-
            提高流量成本估算准确性的提示。

            估计逻辑假设该节点将用于
            交易的执行

            如果使用另一个节点代替，估计可能不太精确。估计中未考虑请求放大：每个
            放大的请求将

            导致收取确认请求的费用
            另外。


            如果未设置此字段，则默认启用流量成本估算
            设置

            要关闭成本估算，请设置 CostEstimationHints#disabled
            字段为真


            可选
        最大点击次数：
          描述：>-
            拓扑感知包的最大传递次数
            选择（TAPS）。

            较高的值可以增加打包成功的机会
            选择解释事务的路由。

            如果未设置，则默认为参与者中定义的值
            配置。

            提供的值不得超过规定的限制
            参与者配置。


            可选
          类型：整数
          格式：int32
        哈希方案版本：
          描述：|-
            构建哈希时要使用的哈希方案版本。
            默认为 HASHING_SCHEME_VERSION_V2。

            可选
          类型：字符串
          枚举：
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
    JsPrepareSubmissionResponse：
      标题：JsPrepareSubmissionResponse
      描述：'[文档条目结束：HashingSchemeVersion]'
      类型：对象
      需要：
        - 准备好的交易
        - 准备好的交易哈希
        - 哈希方案版本
      属性：
        准备好的交易：
          描述：>-
            被解释的交易，它代表账本的变化
            执行请求中指定的命令所必需的。

            客户端必须向用户显示交易内容
            如果准备好，他们在签署哈希之前进行验证
            参与者不可信。


            必填
          类型：字符串
        准备好的交易哈希：
          描述：>-
            交易的哈希值，这是需要由交易者签名的
            授权交易的一方。

            只是为了方便而提供，客户端必须重新计算哈希值
            如果准备参与者不可信，则原始交易。

            可能会在未来版本中删除


            必填：必须非空
          类型：字符串
        哈希方案版本：
          描述：|-
            构建哈希时使用的哈希方案版本必填
          类型：字符串
          枚举：
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
        散列详细信息：
          描述：>-
            有关交易如何编码的可选附加详细信息以及
            散列。仅当请求中 verbose_hashing = true 时才设置

            请注意，不保证格式的稳定性或
            该字段的内容。

            其内容不应被解析且仅应用于
            排除故障的目的。


            可选
          类型：字符串
        成本估算：
          $ref: '#/components/schemas/CostEstimation'
          描述：|-
            已准备交易的流量成本估算可选
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
    最小账本时间：
      标题：最小账本时间
      类型：对象
      属性：
        时间：
          $ref: '#/components/schemas/Time'
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
            在created_event_blob中序列化。可选
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
            支持模板 ID。

            注意：package-id 引用标识符格式已弃用。我们
            计划在 3.4 版本中终止对此格式的支持。


            必填
          类型：字符串
        合约密钥：
          描述：|-
            客户端想要预取的合约的密钥。

            必填
    成本估算提示：
      标题：成本估算提示
      描述：提高已准备交易的成本估算精度的提示
      类型：对象
      属性：
        禁用：
          描述：|-
            禁用成本估算
            默认（未设置）为 false

            可选
          类型：布尔值
        预期签名：
          描述：>-
            有关将用于签署交易的密钥的详细信息（如何
            许多以及哪种类型）。

            签名大小影响交易成本。

            如果为空，签名大小将近似为
            阈值多签名（其中阈值定义为

            在外部方的 PartyTo参与方 中），使用
            以便他们注册。

            空列表相当于不提供该字段


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
            枚举：
              - SIGNING_ALGORITHM_SPEC_UNSPECIFIED
              - SIGNING_ALGORITHM_SPEC_ED25519
              - SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256
              - SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384
    成本估算：
      标题：成本估算
      描述：>-
        估计提交准备好的交易的成本

        估计是根据期间选择的同步器完成的
        交易准备

        （或明确要求的）。将合约重新分配给另一个同步器的成本
        必要的不包括在估计中。
      类型：对象
      需要：
        - 确认请求交通成本估算
        - 确认ResponseTrafficCostEstimation
        - 总流量成本估算
        - 估计时间戳
      属性：
        估计时间戳：
          描述：|-
            进行估计的时间戳

            必填
          类型：字符串
        确认请求流量成本估算：
          描述：>-
            与相关确认请求的估计流量成本
            交易


            必填
          类型：整数
          格式：int64
        确认响应TrafficCostEstimation：
          描述：>-
            与相关的确认响应的估计流量成本
            交易

            该字段还可以用作其他成本的指示
            潜在的确认节点

            当事人将同意或拒绝交易


            必填
          类型：整数
          格式：int64
        总流量成本估算：
          描述：|-
            上面字段的总和

            必填
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
            必须是有效的名称字符串（如``value.proto``中所述）。必填
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
            计划在 3.4 版本中终止对此格式的支持。要对接口进行选择，请指定接口
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
