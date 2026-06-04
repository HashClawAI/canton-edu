---
title: "/v2/package-vetting/list"
slug: "reference-json-api-reference-v2package-vettinglist"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2package-vettinglist.md"
source_title: "/v2/package-vetting/list"
tags:
  - reference
  - json-api-reference
  - v2package-vettinglist
---

# /v2/package-vetting/list

> 列出哪个参与节点审查了哪个同步器上的哪些包。
任何经过身份验证的用户都可以调用。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/package-vetting/list
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
  /v2/package-vetting/列表：
    帖子：
      摘要：/v2/package-vetting/list
      描述：|-
        列出哪个参与节点审查了哪个同步器上的哪些包。
        任何经过身份验证的用户都可以调用。
      操作Id：postV2Package-vettingList
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/ListVettedPackagesRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/ListVettedPackagesResponse'
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
    列出已审查的包裹请求：
      标题：ListVettedPackagesRequest
      类型：对象
      属性：
        包元数据过滤器：
          $ref: '#/components/schemas/PackageMetadataFilter'
          描述：>-
            包元数据过滤器返回的经过审查的包集必须
            满足。


            可选
        拓扑状态过滤器：
          $ref: '#/components/schemas/TopologyStateFilter'
          描述：|-
            返回的经过审查的包集必须满足的拓扑过滤器。

            可选
        页面令牌：
          描述：>-
            分页标记以确定要获取的特定页面。使用
            代币

            保证后续页面上的``VettedPackages``都是
            更大

            （``VettedPackages`` 按同步器 ID 排序，然后按参与者
            ID）比上一页的最后一个“`VettedPackages`”。


            服务器不存储链接调用之间的中间结果
            由一个

            系列页面标记。因此，如果新的经过审查的包裹
            存在

            添加并使用相同的令牌请求页面两次，更多
            包可以

            在第二次调用时返回。


            保留未指定（即作为空字符串）以获取第一页。


            可选
          类型：字符串
        页面大小：
          描述：>-
            单个返回的“`VettedPackages`”结果的最大数量
            页。


            如果 page_size 未指定（即保留为 0），服务器将
            决定

            要返回的结果数。


            如果 page_size 超过服务器支持的最大值，

            将返回错误。


            要获取服务器的最大值，请查阅 PackageService 描述符

            在 VersionService 中可用。


            可选
          类型：整数
          格式：int32
    ListVettedPackages响应：
      标题：ListVettedPackagesResponse
      类型：对象
      属性：
        已审核套餐：
          描述：>-
            所有``VettedPackages`` that contain at least one ``VettedPackage``
            匹配

            都是``PackageMetadataFilter`` and a ``TopologyStateFilter``。

            按同步器_id 然后参与方_id 排序。


            可选：可以为空
          类型：数组
          项目：
            $ref: '#/components/schemas/VettedPackages'
        下一页令牌：
          描述：|-
            用于检索下一页的分页标记。
            如果没有进一步的结果，则为空字符串。

            可选
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
    包元数据过滤器：
      标题：包元数据过滤器
      描述：>-
        按包元数据过滤 VettedPackages。没有 package_ids 且没有的 PackageMetadataFilter
        包名前缀

        与任何经过审查的包匹配。


        非空字段指定候选值，其中至少一个必须
        比赛。

        如果两个字段均已设置，则返回与其中一个匹配的候选字段
        的字段。
      类型：对象
      属性：
        包 ID：
          描述：>-
            如果此列表非空，则任何经过审查且包 ID 位于
            这个

            列表将与过滤器匹配。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        包名前缀：
          描述：>-
            如果此列表非空，则名称匹配的任何经过审查的包
            至少

            该列表中的一个前缀将与过滤器匹配。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
    拓扑状态过滤器：
      标题：拓扑状态过滤器
      描述：>-
        按参与者和同步器筛选经过审查的包
        是

        主办于.


        空字段将被忽略，这样一个没有的``TopologyStateFilter``

        参与方_ids 和不带同步器_ids 匹配经过审查的包
        主持

        在任何参与者和同步器上。


        非空字段指定候选值，其中至少一个必须
        比赛。

        如果两个字段均已设置，则至少有一个候选值必须与
        每个

        场。
      类型：对象
      属性：
        参与者 ID：
          描述：>-
            如果此列表非空，则仅托管在
            参与者

            此字段中列出的内容与过滤器匹配。

            通过public查询当前Ledger API的参与者ID

            ``Get参与方Id`` command in ``PartyManagementService``。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
        同步器ID：
          描述：>-
            如果此列表非空，则仅检查拓扑中的包
            的状态

            此列表中的同步器与过滤器匹配。


            可选：可以为空
          类型：数组
          项目：
            类型：字符串
    已审核套餐：
      标题：VettedPackages
      描述：>-
        在给定参与者和同步器上审查的包列表，
        建模的

        在 ``VettedPackages`` in `topology.proto 之后
        <https://github.com/digital-asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_。该列表仅包含与查询中的过滤器匹配的包

        起源于它。
      类型：对象
      需要：
        - 参与者ID
        - 同步器ID
        - 拓扑串行
        - 包裹
      属性：
        套餐：
          描述：>-
            按已知的 package_name 和 package_version 排序，以及
            package_id 作为

            最后的手段。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/VettedPackage'
        参与者ID:
          描述：|-
            审查这些包的参与者。

            必填
          类型：字符串
        同步器ID：
          描述：|-
            审查这些包的同步器。

            必填
          类型：字符串
        拓扑序列：
          描述：>-
            最后一个``VettedPackages``拓扑事务的序列
            参与者

            以及这个同步器上。


            必填
          类型：整数
          格式：int32
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
    已审核套餐：
      标题：VettedPackage
      描述：>-
        正在审查给定参与者和同步器的包，

        模仿``VettedPackage`` in `topology.proto
        <https://github.com/digital-asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_，

        丰富了包名称和版本。
      类型：对象
      需要：
        - 包ID
      属性：
        包ID:
          描述：|-
            该包的包ID

            必填
          类型：字符串
        有效自包含：
          描述：>-
            审核此包的时间。审核时间为空
            没有

            下限。


            可选
          类型：字符串
        有效直到独占：
          描述：>-
            审核此包的时间。审核时间为空
            没有

            上限。


            可选
          类型：字符串
        包名：
          描述：>-
            该包的名称。

            仅当包已上传到当前位置时才可用
            参与者。


            可选
          类型：字符串
        软件包版本：
          描述：>-
            该软件包的版本。仅当包已上传到当前位置时才可用
            参与者。


            可选
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
