---
title: "/v2/commands/async/submit-reassignment"
slug: "reference-json-api-reference-v2commandsasyncsubmit-reassignment"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandsasyncsubmit-reassignment.md"
source_title: "/v2/commands/async/submit-reassignment"
tags:
  - reference
  - json-api-reference
  - v2commandsasyncsubmit-reassignment
---

# /v2/commands/async/submit-reassignment

> 提交单个重新分配。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/async/submit-reassignment
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
  /v2/commands/async/提交重新分配：
    帖子：
      摘要：/v2/commands/async/submit-reassignment
      描述：提交单个重新分配。
      操作 ID：postV2CommandsAsyncSubmit-重新分配
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/SubmitReassignmentRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/SubmitReassignmentResponse'
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
    提交重新分配请求：
      标题：提交重新分配请求
      类型：对象
      需要：
        - 重新分配命令
      属性：
        重新分配命令：
          $ref: '#/components/schemas/ReassignmentCommands'
          描述：|-
            要提交的重新分配命令。必填
    提交重新分配回复：
      标题：提交重新分配响应
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
            应代表其执行命令的一方。

            如果开启了ledger API授权，则授权
            元数据必须授权请求的发送者

            代表指定方行事。

            必须是有效的 PartyIdString（如``value.proto``中所述）。


            必填
          类型：字符串
        提交ID：
          描述：>-
            区分不同完成情况的唯一标识符
            具有相同更改 ID 的提交。通常是随机 UUID。应用程序预计将使用
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
            必须是有效的 LedgerString（如``value.proto``中所述）。必填
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
            必须是有效的同步器 ID

            必填
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
