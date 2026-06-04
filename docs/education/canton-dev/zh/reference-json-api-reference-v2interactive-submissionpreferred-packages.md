---
title: "/v2/interactive-submission/preferred-packages"
slug: "reference-json-api-reference-v2interactive-submissionpreferred-packages"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionpreferred-packages.md"
source_title: "/v2/interactive-submission/preferred-packages"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionpreferred-packages
---

# /v2/interactive-submission/preferred-packages

> 计算请求中审查要求的首选套餐。
首选包是提供的包名称的最高版本的包
由主办所提供方的所有参与者进行审查。

Ledger API 客户端应使用此端点来构建命令提交
通过做出明智的决定，与所提供的首选软件包兼容：
- 哪些是可用于创建合约的兼容包
- 命令中可以使用哪个合约或执行选择参数版本
- 哪些选择可以在合约的模板或界面上执行

如果由于没有满足要求的选择而无法计算套餐偏好，
将返回`FAILED_PRECONDITION`错误。

当启用 Ledger API 授权时，任何具有有效令牌的 Ledger API 客户端都可以访问。

实验性 API：不保证此端点在未来版本中提供向后兼容性



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/preferred-packages
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
  /v2/交互式提交/首选包：
    帖子：
      摘要：/v2/interactive-submission/preferred-packages
      描述：>-
        计算符合审查要求的首选套餐
        请求。

        首选包是所提供的最高版本的包
        包名

        由主办所提供方的所有参与者进行审查。


        Ledger API 客户端应使用此端点来构建命令
        意见书

        与提供的首选包兼容，通过使
        明智的决定：

        - 哪些是可用于创建合约的兼容包

        - 哪个合同或执行选择参数版本可以用于
        命令

        - 哪些选择可以在合约的模板或界面上执行


        如果由于没有选择而无法计算套餐偏好
        满足要求，

        将返回 `FAILED_PRECONDITION` 错误。任何具有有效令牌的 Ledger API 客户端都可以访问 Ledger
        已启用API授权。


        实验性 API：不保证此端点提供向后功能
        未来版本的兼容性
      操作Id：postV2Interactive-submissionPreferred-packages
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/GetPreferredPackagesRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetPreferredPackagesResponse'
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
    获取首选套餐请求：
      标题：获取首选套餐请求
      类型：对象
      需要：
        - 软件包审核要求
      属性：
        套餐审核要求：
          描述：>-
            首选的包名称审查要求
            包应该得到解决。


            一般来说，提供预期的要求就足够了
            命令的根包名称。

            额外的包名称要求可以提供
            交易通知者需要使用Daml

            命令的根包的包依赖项。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/PackageVettingRequirement'
        同步器ID：
          描述：>-
            其审查状态应用于解析的同步器
            这个查询。

            如果未指定，则所有同步器的审查状态
            参与者已连接并使用。


            可选
          类型：字符串
        审核有效于：
          描述：>-
            包审查有效性的时间戳
            计算的

            参与者看到的最新拓扑快照。

            如果未提供，则使用参与者的当前时钟时间。可选
          类型：字符串
    获取首选套餐响应：
      标题：GetPreferredPackagesResponse
      类型：对象
      需要：
        - 同步器ID
        - 包参考
      属性：
        封装参考：
          描述：>-
            首选软件包的软件包参考。

            对于每个请求的包名称，必须包含一个包引用。


            如果您构建的命令提交的内容取决于
            返回

            首选套餐，那么我们建议提交首选套餐
            包 ID

            在命令提交的``package_id_selection_preference``中
            到

            避免账本并发变化的竞争条件
            包审查状态。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/PackageReference'
        同步器ID：
          描述：>-
            计算包首选项的同步器。

            如果请求中指定了同步器_id，则它匹配
            请求同步器_id。


            必填
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
    套餐审核要求：
      标题：PackageVettingRequirement
      描述：>-
        定义一个包名称，其通常经过审查的包带有
        必须找到最高版本。
      类型：对象
      需要：
        - 包名
        - 聚会
      属性：
        各方：
          描述：>-
            应考虑参与者的审查状态的各方
            解决首选包时。


            必填：必须非空
          类型：数组
          项目：
            类型：字符串
        包名：
          描述：|-
            应解析首选包的包名称。必填
          类型：字符串
    封装参考：
      标题： 封装参考
      类型：对象
      需要：
        - 包ID
        - 包名
        - 包版本
      属性：
        包ID:
          描述：必填
          类型：字符串
        包名：
          描述：必填
          类型：字符串
        软件包版本：
          描述：必填
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
