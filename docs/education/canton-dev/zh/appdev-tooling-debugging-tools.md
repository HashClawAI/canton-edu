---
title: "调试工具"
slug: "appdev-tooling-debugging-tools"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/debugging-tools.md"
source_title: "Debugging Tools"
tags:
  - appdev
  - tooling
  - debugging-tools
---

# 调试工具

> 调试 Canton 应用的工具与工作流：测试输出、Canton Console、PQS 查询与日志分析。

当交易失败、合约丢失或您的应用程序出现意外行为时，Canton 会提供多种工具进行调查。本页面介绍了可用的调试工具和诊断问题的常见工作流程。

## dpm 测试输出

`dpm test` 运行您的 Daml Script测试并向终端报告结果。当测试失败时，输出包括：

* 脚本名称和发生故障的行
* 错误类型（例如，`ContractNotFound`、`AuthorizationError`、`PreconditionFailed`）
* 对于断言失败，预期值和实际值

仔细阅读错误消息——Daml 错误是特定的。 `ContractNotFound`表示您引用的合约 ID 已被存档或对于您的一方来说从未存在过。 `AuthorizationError`意味着提交方缺乏所需的签名者或控制者角色。

### Choice 覆盖率

运行 `dpm test --show-coverage`以查看测试期间执行了模板中的哪些选择。低覆盖率通常与未经测试的边缘情况相关。如果某个选择的覆盖率为零，请考虑您的测试套件是否执行它。

## Canton Console

Canton 控制台是一个交互式 REPL，连接到正在运行的 Canton 节点。这是开发过程中检查账本状态最直接的方法。

### 检查活动合约集

要查看一方当前存在哪些合约：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.state.acs.of_party(myParty)
    res1: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry] = List(
      WrappedContractEntry(
        entry = ActiveContract(
          value = ActiveContract(
            createdEvent = Some(
              value = CreatedEvent(
                offset = 12L,
                nodeId = 0,
                contractId = "00ca4d69609a01f4506bbe595d3a9618fc6efbba7937d86ae2ef1394d08b63968bca1212204d04a08c5b516a06ee4030d85e69b7df88445fbd5237b25a86322efd422054bf",
                templateId = Some(
                  value = Identifier(
                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                    moduleName = "Iou",
                    entityName = "Iou"
                  )
                ),
                contractKey = None,
                contractKeyHash = <ByteString@289c748 size=0 contents="">,
                createArguments = Some(
                  value = Record(
                    recordId = Some(
                      value = Identifier(
                        packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                        moduleName = "Iou",
                        entityName = "Iou"
                      )
                    ),
                    fields = Vector(
                      RecordField(
                        label = "payer",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "owner",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "amount",
                        value = Some(
                          value = Value(
                            sum = Record(
                              value = Record(
                                recordId = Some(
                                  value = Identifier(
                                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                                    moduleName = "Iou",
                                    entityName = "Amount"
                                  )
                                ),
                                fields = Vector(
                                  RecordField(
                                    label = "value",
                                    value = Some(value = Value(sum = Numeric(value = "100.0000000000")))
                                  ),
                                  RecordField(
                                    label = "currency",
                                    value = Some(value = Value(sum = Text(value = "EUR")))
                                  )
                                )
                              )
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "viewers",
                        value = Some(value = Value(sum = List(value = List(elements = Vector()))))
                      )
                    )
                  )
                ),
                createdEventBlob = <ByteString@289c748 size=0 contents="">,
                interfaceViews = Vector(),
                witnessParties = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                signatories = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                observers = Vector(),
                createdAt = Some(
                  value = Timestamp(
                    seconds = 1777917306L,
    ...
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.state.acs.of_party(myParty).filter(_.templateId.toString.contains("Iou"))
    res2: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry] = List(
      WrappedContractEntry(
        entry = ActiveContract(
          value = ActiveContract(
            createdEvent = Some(
              value = CreatedEvent(
                offset = 12L,
                nodeId = 0,
                contractId = "00ca4d69609a01f4506bbe595d3a9618fc6efbba7937d86ae2ef1394d08b63968bca1212204d04a08c5b516a06ee4030d85e69b7df88445fbd5237b25a86322efd422054bf",
                templateId = Some(
                  value = Identifier(
                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                    moduleName = "Iou",
                    entityName = "Iou"
                  )
                ),
                contractKey = None,
                contractKeyHash = <ByteString@289c748 size=0 contents="">,
                createArguments = Some(
                  value = Record(
                    recordId = Some(
                      value = Identifier(
                        packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                        moduleName = "Iou",
                        entityName = "Iou"
                      )
                    ),
                    fields = Vector(
                      RecordField(
                        label = "payer",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "owner",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "amount",
                        value = Some(
                          value = Value(
                            sum = Record(
                              value = Record(
                                recordId = Some(
                                  value = Identifier(
                                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                                    moduleName = "Iou",
                                    entityName = "Amount"
                                  )
                                ),
                                fields = Vector(
                                  RecordField(
                                    label = "value",
                                    value = Some(value = Value(sum = Numeric(value = "100.0000000000")))
                                  ),
                                  RecordField(
                                    label = "currency",
                                    value = Some(value = Value(sum = Text(value = "EUR")))
                                  )
                                )
                              )
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "viewers",
                        value = Some(value = Value(sum = List(value = List(elements = Vector()))))
                      )
                    )
                  )
                ),
                createdEventBlob = <ByteString@289c748 size=0 contents="">,
                interfaceViews = Vector(),
                witnessParties = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                signatories = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                observers = Vector(),
                createdAt = Some(
                  value = Timestamp(
                    seconds = 1777917306L,
    ...
```如果 ACS 中缺少您期望存在的合约，则该合约要么已存档，要么您所在的一方从未是该合约的利益相关者。

### 检查交易

查看最近的交易：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.completions.list(myParty, atLeastNumCompletions = 1, beginOffsetExclusive = 0L)
    res3: Seq[com.daml.ledger.api.v2.completion.Completion] = List(
      Completion(
        commandId = "a557110b-c367-4ef6-9888-746ce1547675",
        status = Some(
          value = Status(
            code = 0,
            message = "",
            details = Vector(),
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        updateId = "12203fcc195b7cdfc1c05b9ff8a461680e40dcbc6320ace860fbeae67c4f1a84cfd4",
        userId = "CantonConsole",
        actAs = Vector("MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"),
        submissionId = "e4a3d2cd-ccf7-4aaa-b6ee-e0a4ff062030",
        deduplicationPeriod = DeduplicationOffset(value = 0L),
        traceContext = Some(
          value = TraceContext(
            traceparent = Some(value = "00-4d7fe627685d2ee4451147e433d1710a-55ec0568e44f195b-03"),
            tracestate = None
          )
        ),
        offset = 12L,
        synchronizerTime = Some(
          value = SynchronizerTime(
            synchronizerId = "da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d",
            recordTime = Some(
              value = Timestamp(
                seconds = 1777917304L,
                nanos = 179712000,
                unknownFields = UnknownFieldSet(fields = Map())
              )
            )
          )
        ),
        paidTrafficCost = 0L
      )
    )
```交易详细信息显示了哪些合约被创建、存档和执行。将事务跟踪与您的期望进行比较，以确定逻辑分歧的地方。

### 上传包

如果您需要在正在运行的节点上更新 Daml 包：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res4: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```## PQS SQL 查询

PQS 将账本状态投影到 PostgreSQL 表中。当您需要跨多个模板调查合约状态或跟踪历史事件时，SQL 通常是最快的方法。

### 寻找合约```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find active contracts of a given template
SELECT contract_id, create_arguments
FROM active_contracts
WHERE template_id LIKE '%MyTemplate%';
```### 追踪已存档的合约```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find when and why a contract was archived
SELECT contract_id, archive_event_id, effective_at
FROM contracts
WHERE template_id LIKE '%MyTemplate%'
  AND contract_id = 'your-contract-id';
```### 检查事件历史记录```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- List recent events for a template
SELECT event_id, event_type, contract_id, effective_at
FROM events
WHERE template_id LIKE '%MyTemplate%'
ORDER BY effective_at DESC
LIMIT 20;
```PQS 查询的范围仅限于您所在方的数据。如果您在 PQS 中找不到合约，则您的一方可能不是该合约的利益相关者。

## 日志分析

运行 LocalNet 或本地沙箱时，日志会捕获有关事务处理、验证错误和节点行为的详细信息。

### 捕获日志

在cn-quickstart环境中：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make capture-logs
```这会将所有 Docker 容器的日志收集到本地目录中以供分析。

### 使用 lnav

[lnav](https://lnav.org/) 是一个日志文件查看器，可以很好地处理结构化日志。它支持同时跨多个日志文件进行过滤、搜索和时间线导航。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
lnav logs/*.log
```在 lnav 中，使用 `:filter-in` 来关注特定模式（例如，事务 ID 或错误关键字），并使用 `:filter-out` 来消除噪音。

### 寻找什么

* **警告和错误级别消息** -- 这些表明存在问题。从失败的操作中搜索事务 ID 或命令 ID。
* **拒绝原因** -- 当中介者拒绝交易时，日志包含原因（超时、不一致、授权失败）。
* **连接问题** -- 如果您的验证器无法到达同步器，交易就会停止。查找连接错误或超时消息。

## 常见的调试工作流程

###“为什么我的交易失败？”

1. 检查Ledger API或您的后端返回的错误。记下命令 ID。
2. 在验证器日志中搜索该命令 ID 以查找详细的拒绝原因。
3. 常见原因：授权不足（提交方错误）、合约已存档（竞态条件）、流量积分不足（检查验证人的流量预算）。

### “我的合约在哪里？”

1. 在 PQS 或 Canton Console ACS 中查询合约 ID 或模板。
2. 如果合约不在 ACS 中，请检查 PQS 中的存档事件 - 它可能已被选择消耗。
3. 如果您从未看到合约，请验证您的一方是合约的利益相关者（签署人或观察员）。坎顿的隐私模式意味着您的一方根本不会看到与它没有利益关系的合约。

###“为什么我看不到这份合约？”

这几乎总是一个隐私问题。仅当您的一方是签字人、观察员或通过泄露或明确披露收到合约时，才能看到合约。检查模板定义以确认您所在团队的角色。如果您的政党未列出，您需要将其添加为 Daml 模型中的观察者或使用显式披露。

## 后续步骤

* [开发工具概述](/appdev/tooling/development-tools-overview) -- 所有可用工具的摘要
* [Troubleshooting](/appdev/troubleshooting) -- 广州开发常见问题的解决方案
* [测试 Daml 合约](/appdev/modules/m3-testing) -- 编写有效的测试以尽早发现问题

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
