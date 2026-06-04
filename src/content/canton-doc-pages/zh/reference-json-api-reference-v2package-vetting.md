---
title: "/v2/package-vetting"
slug: "reference-json-api-reference-v2package-vetting"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2package-vetting.md"
source_title: "/v2/package-vetting"
tags:
  - reference
  - json-api-reference
  - v2package-vetting
---

# /v2/package-vetting

> 更新该参与者的审核包
此端点 (POST /package-vetting) 已弃用，并将在未来版本中删除。请改用 POST /package-vetting/update。



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/package-vetting
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
  /v2/包审查：
    帖子：
      摘要：/v2/package-vetting
      描述：>-
        更新该参与者的已审核包

        此端点 (POST /package-vetting) 已弃用并将被删除
        在未来的版本中。请改用 POST /package-vetting/update。
      操作 ID：postV2Package-vetting
      请求正文：
        内容：
          应用程序/json：
            架构：
              $ref: '#/components/schemas/UpdateVettedPackagesRequest'
        必填：真实
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/UpdateVettedPackagesResponse'
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
      已弃用：true
      安全：
        - httpAuth: []
        - apiKeyAuth: []
组件：
  模式：
    更新VettedPackages请求：
      标题：更新VettedPackagesRequest
      类型：对象
      需要：
        - 变化
      属性：
        变化：
          描述：>-
            适用于参与者当前审核状态的更改
            的

            指定的同步器。更改按顺序应用。

            任何未更改的包将保留其先前的审核状态。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/VettedPackagesChange'
        干运行：
          描述：>-
            如果 dry_run 为 true，则仅准备更改，但未准备更改
            应用。如果请求在运行时会触发错误（例如
            TOPOLOGY_DEPENDENCIES_NOT_VETTED),

            dry_run 时也会触发错误。


            使用此标志可以在应用更改之前预览更改。

            默认为 false。


            可选
          类型：布尔值
        同步器ID：
          描述：>-
            如果设置，请求的更改将发生在指定的

            同步器。如果同步器_id未设置并且参与者是
            仅

            连接到单个同步器，将使用该同步器
            通过

            默认。如果同步器_id未设置并且参与者是
            连接到

            多个同步器，请求将出错

            PACKAGE_SERVICE_CANNOT_AUTODETECT_SYNCHRONIZER。


            可选
          类型：字符串
        预期拓扑序列：
          $ref: '#/components/schemas/PriorTopologySerial'
          描述：>-
            最后一个``VettedPackages``拓扑事务的序列号
            这个

            参与者和此同步器上。


            如果不正确，请求的执行将失败。用这个来
            守卫

            反对并发更改。


            如果未指定，则不会针对最后一个进行验证
            交易的

            串行。


            可选
        更新VettedPackagesForceFlags：
          描述：|-
            控制是否允许潜在不安全的审查更新。

            可选：可以为空
          类型：数组
          项目：
            类型：字符串
            枚举：
              - UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED
              ->-
                UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES
              - UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES
    更新VettedPackages响应：
      标题：UpdateVettedPackagesResponse
      类型：对象
      需要：
        - 新的VettedPackages
      属性：
        过去已审查的套餐：
          $ref: '#/components/schemas/VettedPackages'
          描述：>-
            在该参与者和同步器上的所有经过审查的包之前

            指定的更改。如果事先不存在审查状态，则为空。


            如果在之前不存在经过审查的拓扑状态，则不会填充
            更新。


            可选
        新的Vetted套餐：
          $ref: '#/components/schemas/VettedPackages'
          描述：>-
            在此参与者和同步器上的所有经过审查的包，在
            指定的更改。必填
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
    VettedPackages变更：
      标题：VettedPackagesChange
      描述：对一组经过审查的软件包进行了更改。
      类型：对象
      属性：
        操作：
          $ref: '#/components/schemas/Operation'
    PriorTopology系列：
      标题：PriorTopology系列
      描述：|-
        给定上最后一个“`VettedPackages`”拓扑事务的序列
        参与者和同步者。
      类型：对象
      属性：
        序列号：
          $ref: '#/components/schemas/Serial'
    已审核套餐：
      标题：VettedPackages
      描述：>-
        在给定参与者和同步器上审查的包列表，
        建模的

        在 ``VettedPackages`` in `topology.proto 之后
        <https://github.com/digital-asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_。

        该列表仅包含与查询中的过滤器匹配的包

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

            以及这个同步器上。必填
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
    操作：
      标题： 操作
      描述：必填
      其中之一：
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty5'
        - 类型：对象
          需要：
            - 未受审查
          属性：
            未审查：
              $ref: '#/components/schemas/Unvet'
        - 类型：对象
          需要：
            - 兽医
          属性：
            兽医：
              $ref: '#/components/schemas/Vet'
    序列号：
      标题：连续剧
      描述：可选
      其中之一：
        - 类型：对象
          需要：
            - 空
          属性：
            空：
              $ref: '#/components/schemas/Empty6'
        - 类型：对象
          需要：
            - 无先验
          属性：
            无先验：
              $ref: '#/components/schemas/NoPrior'
        - 类型：对象
          需要：
            - 事先
          属性：
            之前：
              $ref: '#/components/schemas/Prior'
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
    空5：
      标题： 空
      类型：对象
    未审查：
      标题： 温维特
      描述：从经过审查的包集中删除包
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Unvet1'
    兽医：
      标题： 兽医
      描述：>-
        设置包列表的审查范围。不存在的包
        以前

        已审查的边界已添加，以前的审查边界将被覆盖。
      类型：对象
      需要：
        - 价值
      属性：
        值：
          $ref: '#/components/schemas/Vet1'
    空6：
      标题： 空
      类型：对象
    无先验：
      标题：无先验
      类型：对象
    之前：
      标题： 先前
      类型：对象
      需要：
        - 价值
      属性：
        值：
          类型：整数
          格式：int32
    未审查1：
      标题： 温维特
      描述：从经过审查的包集中删除包
      类型：对象
      需要：
        - 包裹
      属性：
        套餐：
          描述：|-
            软件包未经审查。

            如果此列表中的引用与多个包匹配，则它们都是
            未经审查。

            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/VettedPackagesRef'
    兽医1：
      标题： 兽医
      描述：>-
        设置包列表的审查范围。不存在的包
        以前

        已审查的边界已添加，以前的审查边界将被覆盖。
      类型：对象
      需要：
        - 包裹
      属性：
        套餐：
          描述：>-
            待审查的包裹。


            如果此列表中的引用与多个包匹配，则
            改变是

            被认为不明确并且整个更新请求被拒绝。在
            其他

            换句话说，每个引用都必须与一个包完全匹配。


            必填：必须非空
          类型：数组
          项目：
            $ref: '#/components/schemas/VettedPackagesRef'
        newValidFromInclusive：
          描述：>-
            应审查这些包裹的时间，优先较低
            界限

            被覆盖。

            可选
          类型：字符串
        newValidUntilExclusive：
          描述：>-
            审查这些包裹的时间，优先于上层
            界限

            被覆盖。可选
          类型：字符串
    已审查的软件包参考：
      标题：VettedPackagesRef
      描述：>-
        用于识别一个或多个包的参考。


        如果“`package_id`”与包匹配，则引用与包匹配
        包裹的ID，

        它的 ``package_name`` 与包的名称匹配，并且它的
        ``package_version``

        与包的版本匹配。如果引用中的属性被保留

        未指定（即作为空字符串），该属性被视为

        通配符。至少，``package_id`` or the ``package_name``必须是

        指定。


        如果参考与任何包都不匹配，则考虑该参考

        未解决，整个更新请求被拒绝。
      类型：对象
      属性：
        包ID:
          描述：|-
            包的包 ID 必须与此字段相同。

            可选
          类型：字符串
        包名：
          描述：|-
            包的名称必须与此字段相同。

            可选
          类型：字符串
        软件包版本：
          描述：|-
            包的版本必须与此字段相同。

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
