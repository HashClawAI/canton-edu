---
title: "/v2/interactive-submission/preferred-package-version"
slug: "reference-json-api-reference-v2interactive-submissionpreferred-package-version"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionpreferred-package-version.md"
source_title: "/v2/interactive-submission/preferred-package-version"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionpreferred-package-version
---

# /v2/interactive-submission/preferred-package-version

> 首选软件包是提供的软件包名称的最高版本软件包
由主办所提供方的所有参与者进行审查。

Ledger API 客户端应使用此端点来构建命令提交
通过做出明智的决定，与所提供的首选包兼容：
- 哪些是可用于创建合约的兼容包
- 命令中可以使用哪个合约或执行选择参数版本
- 哪些选择可以在合约的模板或界面上执行

当启用 Ledger API 授权时，任何具有有效令牌的 Ledger API 客户端都可以访问。

为向后兼容而提供，将在 Canton 版本 3.4.0 中删除



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/interactive-submission/preferred-package-version
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
  /v2/交互式提交/首选包版本：
    得到：
      摘要：/v2/interactive-submission/preferred-package-version
      描述：>-
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


        任何具有有效令牌的 Ledger API 客户端都可以访问 Ledger
        已启用API授权。提供向后兼容性，它将在 Canton 中删除
        版本3.4.0
      操作 ID：getV2Interactive-submissionPreferred-package-version
      参数：
        - 名称：派对
          在：查询
          必填：假
          架构：
            类型：数组
            项目：
              类型：字符串
        - name: 包名
          在：查询
          必填：真实
          架构：
            类型：字符串
        - 名称：vetting_valid_at
          在：查询
          必填：假
          架构：
            类型：字符串
            格式：日期-时间
        - 名称：同步器 ID
          在：查询
          必填：假
          架构：
            类型：字符串
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetPreferredPackageVersionResponse'
        “400”：
          描述：>-
            无效值，无效值：查询参数方，无效
            值：查询参数包名称，无效值：查询
            参数 vetting_valid_at，无效值：查询参数
            同步器ID
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
    获取首选包版本响应：
      标题：GetPreferredPackageVersionResponse
      类型：对象
      属性：
        封装偏好：
          $ref: '#/components/schemas/PackagePreference'
          描述：|-
            未找到首选包时不填充可选
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
    套餐偏好：
      标题： 包首选项
      类型：对象
      需要：
        - 同步器ID
        - 包参考
      属性：
        封装参考：
          $ref: '#/components/schemas/PackageReference'
          描述：|-
            首选包的包参考。

            必填
        同步器ID：
          描述：>-
            为其计算首选包的同步器。

            如果请求中指定了同步器_id，则它匹配
            请求同步器_id。


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
