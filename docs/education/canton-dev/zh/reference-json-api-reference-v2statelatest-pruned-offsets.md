---
title: "/v2/state/latest-pruned-offsets"
slug: "reference-json-api-reference-v2statelatest-pruned-offsets"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2statelatest-pruned-offsets.md"
source_title: "/v2/state/latest-pruned-offsets"
tags:
  - reference
  - json-api-reference
  - v2statelatest-pruned-offsets
---

# /v2/state/latest-pruned-offsets

> 获取最新成功修剪的账本偏移量



## 开放API

````yaml /openapi/json-ledger-api/openapi.yaml 获取 /v2/state/latest-pruned-offsets
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
  /v2/state/latest-pruned-offsets：
    得到：
      摘要：/v2/state/latest-pruned-offsets
      描述：获取最新成功剪枝的账本偏移量
      操作 ID：getV2StateLatest-pruned-offsets
      回应：
        “200”：
          描述：''
          内容：
            应用程序/json：
              架构：
                $ref: '#/components/schemas/GetLatestPrunedOffsetsResponse'
        “400”：
          描述：无效值
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
    GetLatestPrunedOffsets响应：
      标题：GetLatestPrunedOffsetsResponse
      类型：对象
      属性：
        参与者PrunedUpToInclusive：
          描述：>-
            它始终是一个非负整数。

            如果为正，则分类账已达到的绝对偏移量
            修剪过的，

            不考虑所有泄露合同修剪的状态。

            如果为零，则分类账尚未被修剪。


            可选
          类型：整数
          格式：int64
        allDivulgedContractsPrunedUpToInclusive：
          描述：>-
            它始终是一个非负整数。

            如果为正，则所有泄露事件的绝对偏移量
            已在账本上被修剪。

            它可以位于``参与方_pruned_up_to_inclusive``处或之前
            偏移。

            有关所有泄露事件修剪的更多详细信息，

            参见“`PruneRequest.prune_all_divulged_contracts`”
            ``参与方_pruning_service.proto``。

            如果为零，则泄露的事件尚未被修剪。可选
          类型：整数
          格式：int64
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
