---
title: "错误码参考"
slug: "global-synchronizer-reference-error-codes"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/error-codes.md"
source_title: "Error Code Reference"
tags:
  - global-synchronizer
  - reference
  - error-codes
---

# 错误码参考

> Canton 运维错误码、类别与常见操作错误说明。

> Canton 错误代码、日志级别含义和错误类别的操作员参考

Canton 在所有组件中使用结构化错误代码系统。通过 API 记录或返回的每个错误都遵循格式 `ERROR_CODE_ID(category_id, correlation_id_prefix): human-readable message`。本页介绍了如何读取这些错误、哪些类别需要操作员采取操作以及最常见的操作错误的含义。

应用开发过程中遇到的gRPC错误码请参见[AppDev错误码参考](/appdev/reference/error-codes)。

## 读取日志中的错误码

## 日志级别

Canton 一致使用日志级别：

* **INFO** -- 请求失败但系统保持正常运行的用户错误。大多数类别 1、2、8、9、10、11 和 12 错误都记录在此级别。
* **警告** - 系统性能下降或可能需要注意的异常行为。安全警报（类别 5）和降级警告（类别 13）记录在此处。
* **错误** - 系统行为不正确且需要立即关注的内部错误。此处记录类别 4 (`SystemInternalAssumptionViolated`) ​​错误。

作为操作员，您应该针对警告和错误级别消息设置警报。 INFO 级错误代码通常是暂时性的或由客户端问题引起的，但持续存在的 INFO 级错误（例如重复的`SEQUENCER_REQUEST_FAILED`）可能表示需要调查的连接问题。

## 错误类别

错误类别

错误类别允许您对错误进行分组，以便可以构建应用程序逻辑来自动处理错误并决定是重试请求还是升级给操作员。

错误类别的完整列表记录在[此处](#error-categories-inventory)。

## 机器可读信息

API 上的每个错误都被构造为允许自动和手动错误处理。首先，错误类别恰好映射到一个 gRPC 状态代码。其次，每个[错误描述](https://grpc.github.io/grpc-java/javadoc/io/grpc/Status.html#getDescription--)（相应的`StatusRuntimeException.Status`）都以错误信息（**SOMETHING\_NOT\_SO\_GOOD\_HAPPENED(CN,x)**）开头，通过冒号（“：”）与人类可读的描述分隔开。描述的其余部分是针对人类的，永远不应该由应用程序解析，因为描述可能会在未来的版本中更改以提高清晰度。

除了状态代码和描述之外，[gRPC 丰富错误模型](https://cloud.google.com/apis/design/errors#error_details) 用于向应用程序传递附加的机器可读信息。

因此，为了支持自动错误处理，应用程序可以：

* 从描述开始解析错误信息，获取错误id、错误类别和组件。
* 使用 gRPC 代码获取可能的错误类别集。
* 如果存在，请使用包含的 `ResourceInfo` 作为 `Status.details`。由于某些明确定义的资源问题（合约、合约密钥、包、参与方、模板、同步器）而失败的任何请求都将包含这些内容，并指出失败是基于哪些资源。
* 使用`RetryInfo`来确定建议的重试间隔（或根据类别/gRPC代码做出此决定）。
* 使用`RequestInfo.id`作为`correlation-id <tracing>`，包含为`Status.details`。
* 使用`ErrorInfo.reason`作为错误ID，使用`ErrorInfo.metadata("category")`作为错误类别，包含为`Status.details`。

所有这些信息都包含在我们控制下的组件生成的错误中，并包含为 `Status.details`。与上述 Daml 错误代码一样，许多错误包含更多信息，但不能保证跨版本保留附加信息。

一般来说，自动错误处理可以在任何级别上完成（例如使用 gRPC 状态代码的负载均衡器、使用 `ErrorCategory` 的应用程序或人工对错误 ID 做出反应）。在大多数情况下，建议按类别处理错误，并在依赖于应用程序的特定情况下处理错误 ID。例如，如果给定应用程序是合约上唯一的参与者，则带有消息“CONTRACT\_NOT\_FOUND”的命令失败可能是应用程序失败，而在多个独立参与者对账本状态进行操作的情况下，预计会出现“CONTRACT\_NOT\_FOUND”消息。

＃＃ 例子如果应用程序提交的 Daml 事务超出了同步器上强制执行的大小限制，则该命令将被拒绝。使用我们的测试用例之一的日志，参与者节点将记录以下消息：

```
2022-04-26 11:37:54,584 [GracefulRejectsIntegrationTestDefault-env-execution-context-30] INFO  c.d.c.p.p.TransactionProcessingSteps:参与方=参与方1/同步器=da tid:13617c1bda402e54e016a6a17637cb20 - SEQUENCER_REQUEST_FAILED(2,13617c1b): Failed to send command err-context:{location=TransactionProcessingSteps.scala:449, sendError=RequestInvalid(Batch size (85134 bytes) is exceeding maximum size (27000 bytes) for 同步器 da::12201253c344...)}
```

错误消息的机器可读部分显示为 `SEQUENCER_REQUEST_FAILED(2,13617c1b)`，提及错误 ID `SEQUENCER_REQUEST_FAILED`、带有 `id=2` 的类别 <span class="title-ref">ContentionOnSharedResources</span> 以及相关标识符 `13617c1b`。请注意，无法保证发出给定错误的记录器的名称，因为该名称是内部名称，可能会更改。日志消息的人类可读部分不应被解析，因为我们随后可能会改进文本。

客户端将收到作为 Grpc 错误的错误信息：

```
2022-04-26 11:37:54,923 [ScalaTest-run-running-GracefulRejectsIntegrationTestDefault] ERROR  c.d.c.i.EnterpriseEnvironmentDefinition$$anon$3 - Request failed for 参与方1.
    GrpcRequestRefusedByServer: ABORTED/SEQUENCER_REQUEST_FAILED(2,13617c1b): Failed to send command
    Request: SubmitAndWaitTransactionTree(actAs = 参与方1::1220baa5cd30..., commandId = '', workflowId = '', submissionId = '', deduplicationPeriod = None(), ledgerId = '参与方1', commands= ...)
    CorrelationId: 13617c1bda402e54e016a6a17637cb20
    RetryIn: 1 second
    Context: HashMap(参与方 -> 参与方1, test -> GracefulRejectsIntegrationTestDefault, 同步器 -> da, sendError -> RequestInvalid(Batch size (85134 bytes) is exceeding maximum size (27000 bytes) for 同步器 da::12201253c344...), definite_answer -> true)
```

请注意，第二个日志是由 Daml 工具创建的，该工具在测试期间将 Grpc 状态打印到日志文件中。实际的 Grpc 错误将由应用程序接收，并且不会由参与者节点以给定的形式记录。

## 错误类别清单

错误类别允许您对错误进行分组，以便可以以合理的方式构建应用程序逻辑来自动处理错误并决定是重试请求还是升级给操作员。

## 错误代码清单

### 1. Grpc 错误

#### 由于关闭而中止

* **说明**：当由于节点关闭而中止请求处理时，返回此错误。
* **解决方案**：针对活动且可用的节点重试请求。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 服务器\_过载

* **解释**：节点已满，因此限制并行请求的数量。
* **解决方案**：使用指数退避重试。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 2. 授权检查错误

#### 访问令牌已过期

* **解释**：当使用一段时间的有效 JWT 令牌过期时，会出现此拒绝。
* **解决方案**：要求您的参与运营商或 IDP 提供商为您提供适当的 JWT 令牌。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 内部\_授权\_错误

* **解释**：发生内部系统授权错误。
* **解决方案**：联系参与运营商。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 无效\_TOKEN* **解释**：当提交的账本 API 命令包含无效令牌时，会发出此错误。
* **解决方案**：检查给出的原因并更正您的申请。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 权限\_拒绝

* **解释**：如果提供的授权令牌不足以执行预期命令，则会给出此拒绝。确切原因已登录参与者，但出于安全原因未提供给用户。
* **解决方案**：检查您的命令和令牌，或者向您的参与操作员询问此命令失败的原因。
* **类别**：权限不足
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它以 grpc-status PERMISSION\_DENIED 的形式公开在 API 上，没有任何详细信息。

#### 过时\_流\_授权

* **解释**：流已中止，因为经过身份验证的用户的权限发生了更改，因此用户可能不再被授权访问此流。
* **解决方案**：应用程序应自动重试获取流。它要么成功，要么因显式拒绝身份验证或权限而失败。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 未经身份验证

* **解释**：如果提交的命令不包含执行 JWT 身份验证的参与者的 JWT 令牌，则会给出此拒绝。
* **解决方案**：要求您的参与运营商或 IDP 提供商为您提供适当的 JWT 令牌。
* **类别**：AuthInterceptorInvalidAuthenticationCredentials
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它以 grpc-status UNAUTHENTICATED 的形式暴露在 API 上，没有任何详细信息。

### 3.参与方ErrorGroup

### 3.1。错误

#### ACS\_COMMITMENT\_INTERNAL\_ERROR

* **解释**：此错误表明 ACS 承诺处理中存在内部错误。
* **解决方案**：检查错误消息以了解详细信息。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。

### 3.1.1。不匹配错误

#### ACS\_承诺\_警报

* **解释**：参与者检测到另一个节点有恶意行为。在多种情况下会出现此警告。首先，当从对方参与者收到的 ACS 承诺具有无效签名时，就会发生这种情况。可能是对方本身恶意，故意添加了错误的签名，也可能是其他人修改了对方正确发送的签名承诺，甚至冒用对方的名义伪造了一条消息。其次，当参与者从覆盖相同时间间隔的同一对方参与者收到两个正确签名但不同的承诺时，就会发生此警报。正确的对方参与者永远不会发送该信息。
* **解决方案**：联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### ACS\_COMMITMENT\_MISMATCH* **解释**：此错误代码表示参与者与一个或多个相对参与者之间的承诺不匹配。在诚实的参与者之间，分叉永远不应该发生，但是，不当行为、错误或使用维修服务对合约商店进行手动更改可能会导致分叉。分叉意味着一份或多份普通合约对参与者有效，但对其相对参与者无效，反之亦然。持不同意见的参与者将对使用有争议合约的交易的一致性检查有不同的本地裁决。只要这些合约处于活动状态，分叉就存在，但如果合约在其生命周期中被停用，则分叉会自动“自行解决”。参与节点操作员还可以通过修复命令手动修复分叉。
* **解决办法**：请参考检查承诺不匹配的操作手册，与对方节点一起确定不匹配的原因。然后修复该参与者的商店和/或对方参与者的商店。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### ACS\_不匹配\_无共享\_合同

* **解释**：此错误代码表示分叉的一种特殊情况，其中对方参与者发送了一段时间的承诺，而该参与者认为在该时间段结束时不存在任何共享的活跃合约。这种情况可能是由于对方参与者的恶意行为、错误或对方节点的管理员使用修复手动更改合约并创建与其他参与者不兼容的 ACS 状态而发生的。对方参与者将记录 ACS\_COMMITMENT\_MISMATCH。
* **解决方案**：请查阅有关检查承诺不匹配的操作手册，以检查不匹配的原因。修复该参与者或柜台参与者的商店。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 3.1.2。退化误差

#### ACS\_承诺\_降级

* **解释**：此错误代码表明参与节点在承诺计算中落后于其某些对应参与者，可能是由于负载过重，并进入追赶模式。这被称为降级。降级参与者的危险在于，其相对参与者可能会将其列入黑名单，以畅通其剪枝，因此这些相对参与者不会等待参与者的承诺，这会削弱不可否认性保证。操作员可以配置参与者需要落后多少个协调间隔才能触发追赶模式的阈值，以及参与者在追赶模式下跳过的协调间隔数量。然而，任何对方参与者的操作员都可以根据自己对慢速参与者的容忍程度，单方面决定将参与者列入黑名单，而不管每个参与者的配置参数如何。
* **解决方案**：追赶模式已启用，参与者应自行恢复。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

#### ACS\_承诺\_降级\_且无效\_配置

* **说明**：此错误代码表示承诺计算出现降级并且启动了追赶模式，但是追赶模式配置无效并且不会提高性能。这是因为追赶模式的配置有一个跳过步骤1，这意味着参与者不会跳过任何承诺计算。参与者面临着持续降级的风险，而其相对参与者可能会将其列入黑名单并且不积极等待承诺，从而削弱不可否认性保证。
* **解决方案**：请更新追赶模式配置，使 catchUpIntervalSkip 大于 1
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

### 3.2。添加方错误

#### 添加与同步器断开连接的一方* **解释**：此错误表示将具有活动合约的一方添加到参与者和同步器已被与同步器断开连接的参与者中断。
* **解决方案**：将参与者重新连接到同步器以解除阻止添加参与者。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 添加\_PARTY\_OTHER

* **解释**：此错误当前用作阻止将一方添加到参与者和同步器的各种故障的统称。
* **解决方案**：检查消息，可能会重建目标参与者，然后重试添加该方。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

### 3.3。 LedgerApi错误组

### 3.3.1。命令执行错误

#### 已披露\_合同\_同步器\_ID\_不匹配

* **解释**：如果附加到命令提交的某些已披露合同（也用于命令解释）指定了不匹配的同步器 ID，则会发生此错误。如果所公开合约的同步器 ID 不同步或者原始合约被分配给不同的同步器，则可能会发生这种情况。
* **解决方案**：使用一组最新的附加披露合约重试提交，或重新创建仅使用驻留在同一同步器上的披露合约的命令提交。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 未能确定\_LEDGER\_TIME

* **解释**：如果参与者无法确定所使用合约的最大账本时间，则会出现此错误。最有可能的是，这意味着其中一份合同不再有效，这可能会在争用情况下发生。合约密钥也可能发生这种情况。
* **解决方案**：重试事务提交。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 执行交易失败

* **说明**：如果参与者未能通过交互式提交服务执行交易，则会出现此错误。
* **解决方案**：检查错误详细信息并报告错误。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 准备交易失败

* **说明**：如果参与者未能通过交互式提交服务准备交易，则会出现此错误。
* **解决方案**：检查错误详细信息并报告错误。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 解释\_时间\_超出* **解释**：当命令的解释超出时间限制时，就会发生此错误，该时间限制定义为分类帐在开始处理命令时可以分配的最大时间。它对应于参与者提交时分配的时间（账本时间）+ <span class="title-ref">ledgerTimeToRecordTimeTolerance</span> 账本配置参数定义的容差。超过此限制的原因可能各不相同：参与者可能处于高负载下，命令解释可能非常复杂，甚至由于 Daml 代码中的错误而陷入无限循环。
* **解决**：由于暂停问题，我们无法确定解释是否最终会完成。作为开发人员：检查代码是否存在可能的非终止循环或考虑降低其复杂性。作为操作员：检查并可能更新分配给系统的资源，以及与时间相关的配置参数（请参阅“Daml Ledger 模型概念”文档部分中的“Daml Ledgers 上的时间”和 <span class="title-ref">set\_ledger\_time\_record\_time\_tolerance</span> 控制台命令）。
* **类别**：共享资源争用
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 程序包\_NAME\_由于\_未审查\_程序包而被丢弃

* **解释**：由于审查拓扑限制，命令解释中所需的包名称在拓扑感知包选择中被丢弃。
* **解决方案**：重新访问命令提交并确保其符合提交者和通知者经过审查的拓扑状态。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 包\_选择\_失败

* **解释**：当拓扑感知包选择无法生成命令提交所需的已审查包的有效候选集时，会发生此错误。
* **解决办法**：检查错误信息并调整拓扑状态或提交的命令
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 指定\_SYNCHRONIZER\_ID\_MISMATCH

* **解释**：当命令提交中提供的同步器 ID 与命令解释中使用的公开合约之一中指定的同步器 ID 不匹配时，会发生此错误。
* **解决方案**：使用驻留在目标提交同步器上的所有已披露合约重试提交。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 3.3.1.1。套餐

#### 允许的\_语言\_版本

* **解释**：此错误表明上传的 DAR 基于不受支持的语言版本。
* **解决方案**：使用使用该参与者支持的语言版本编译的 DAR。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 包\_验证\_失败

* **解释**：如果命令引用的包验证失败，则会出现此错误。这种情况不应该发生，因为包在上传时经过验证。
* **解决方案**：联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 3.3.1.2。预处理

#### 命令\_预处理\_失败

* **解释**：如果命令在解释器预处理期间失败，则会出现此错误。
* **解决方案**：检查错误详细信息并更正您的应用程序。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 3.3.1.3。口译员

#### 合同未实现接口* **解释**：当您尝试通过未实现的接口强制/使用合约时，会发生此错误。
* **解决方案**：确保您正在调用的合约确实实现了您用于执行此操作的接口。避免手动编写 LF/低级接口实现类。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 合同不实现要求接口

* **解释**：当您尝试创建/使用一个未实现它所实现的其他接口所需接口的合约时，就会发生此错误。
* **解决方案**：确保正确实现所有必需的接口，并避免手动编写 LF/低级接口实现类。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 合约\_哈希\_错误

* **解释**：当尝试对格式不正确的合约进行哈希处理时，会发生此错误。
* **解决方案**：确保被哈希的合约是有效合约。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 合同\_ID\_可比性

* **解释**：当您尝试比较同一鉴别器的全局和本地合约 ID 时，会发生此错误。
* **解决方案**：避免手动构建合约 ID。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 合同\_ID\_IN\_合同\_KEY

* **解释**：当合约密钥包含合约 ID 时，会发生此错误，由于哈希原因，合约 ID 是非法的。
* **解决方案**：确保您的合同关键字段不能包含合同 ID。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 合同未生效

* **解释**：如果在交易本地使用的合约上发生执行或获取，则会发生此错误。
* **解决方案**：此错误表示应用程序错误。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 创建\_空\_合同\_密钥\_维护者

* **解释**：当您尝试创建具有密钥但维护者为空的合约时，会发生此错误。
* **解决方案**：检查合约密钥维护者的定义，并确保根据您的创建参数，此列表不会为空。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### DAML\_授权\_错误

* **说明**：如果 Daml 事务由于授权错误而失败，则会出现此错误。授权意味着 Daml 事务计算出的一组所需提交者与您作为 <span class="title-ref">actAs</span> 方提交期间提供的不同。
* **解决方案**：如果存在应用程序错误，则会出现此错误类型。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### DAML\_FAILURE* **说明**：此错误是在 daml 代码中使用 <span class="title-ref">failWithStatus</span> 引发的。 Daml 代码确定 canton 错误类别，从而确定 grpc 状态代码。
* **解决方案**：确保您正确使用合约，并且选择的实现没有错误。
* **类别**：\<由 daml 代码确定>
* **输送**：输送由类别决定，在 daml 代码中选择。有关详细信息，请参阅引发的错误中编码的实际错误类别的文档。

#### DAML\_解释\_错误

* **解释**：如果 Daml 事务在解释过程中失败，则会出现此错误。
* **解决方案**：如果存在应用程序错误，则会出现此错误类型。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### DAML\_INTERPRETER\_INVALID\_ARGUMENT

* **解释**：如果 Daml 事务在解释过程中由于参数无效而失败，则会出现此错误。
* **解决方案**：如果存在应用程序错误，则会出现此错误类型。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 披露\_合同\_密钥\_哈希\_错误

* **解释**：如果用户尝试为我们已缓存的已披露合约提供不同的密钥哈希，则会发生此错误。
* **解决方案**：确保您在披露的合同中提供的合同 ID 和合同有效负载正确。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 获取\_空\_合同\_密钥\_维护者

* **解释**：当您尝试通过密钥获取合约，但该密钥的维护者为空时，会发生此错误。
* **解决方案**：检查合约密钥维护者的定义，并确保在给定您正在获取的合约密钥的情况下此列表不会为空。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 解释\_DEV\_错误

* **解释**：此错误是开发中功能引发的错误的统称，绝不应在生产中引发。
* **解决方案**：有关特定开发中功能错误的详细信息，请参阅错误消息。如果这是生产，请避免使用开发功能。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 解释\_用户\_错误

* **解释**：当用户在引入本机异常之前在 LF 版本上调用 abort 或 error 时，会发生此错误。
* **解决方案**：要么删除对中止、错误或断言的调用，要么确保您按照作者的预期行使合同选择。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 格式错误\_TEXT

* **解释**：当 Daml 文本不是有效的 UTF-8 字符串或包含空字符时，会发生此错误。
* **解决方案**：重构代码并减少值嵌套。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 不可比较的值

* **解释**：当您尝试使用内置比较类型比较不同类型的两个值时，会发生此错误。
* **解决方案**：避免使用低级比较构建，而使用 Eq 类。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。#### 模板\_前提条件\_违反

* **解释**：当合同创建时违反合同的前提条件（确保条款）时，就会出现此错误。
* **解决方案**：确保您传递到创建中的合同参数不违反合同条件。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 未处理\_异常

* **解释**：当用户抛出错误并且没有用try-catch捕获它时，就会出现此错误。
* **解决方案**：要么您在选择主体中的错误处理不充分，要么您错误地使用了合约。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 值\_嵌套

* **解释**：当您嵌套值太深时会出现此错误。
* **解决方案**：重构代码并减少值嵌套。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 错误\_输入\_合同

* **解释**：当您尝试以某种方式获取/使用合同 ID 与账本上的模板类型不匹配的合同时，会发生此错误。
* **解决方案**：确保您使用的合约 ID 是我们在账本上期望的类型。避免不安全地强制合约 ID。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.3.1.3.1。查找错误

#### 未找到合同密钥

* **解释**：如果 Daml 引擎解释器无法将合约密钥解析为活动合约，则会出现此错误。这可能是由于参与者不知道合约密钥、提交方不知道合约密钥或代表已存档密钥的合约造成的。
* **解决方案**：如果合约存在争用，则会出现此错误类型。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未解析的\_PACKAGE\_NAME

* **解释**：如果 Daml 引擎解释器无法将包名称解析为任何经过审查的包，则会出现此错误。这可能是由于命令使用了由尚未经过参与者审查的包生成的显式披露，或者是由使用其创建包已被强制未经审查的合约的命令引起的。
* **解决方案**：确保该命令不使用尚未经过审查或未经审查的包。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.1.3.2。加密错误

#### 解释\_加密\_错误\_格式错误\_字节\_编码

* **解释**：十六进制字符串格式错误
* **解决方案**：确保字符串非空、长度均匀且仅包含十六进制字符（即匹配 \[0-9a-fA-F]+）
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 解释\_加密\_错误\_格式错误\_密钥

* **解释**：公钥十六进制编码格式错误
* **解决方案**：确保公钥是 DER 编码的 Secp256k1 公钥
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 解释\_加密\_错误\_格式错误\_签名* **解释**：签名十六进制编码格式错误
* **解决方案**：确保签名是 DER 编码的 Keccak256 摘要
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.3.1.3.3。升级错误

#### 解释\_升级\_错误\_身份验证\_失败

* **解释**：无法验证合约
* **解决方案**：验证用于加载合同的模板是否与创建合同的模板升级兼容。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 解释\_升级\_错误\_翻译\_失败

* **解释**：合约格式错误或与预期类型不匹配
* **解决方案**：验证用于加载合同的模板是否与创建合同的模板升级兼容。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 解释\_升级\_错误\_验证\_失败

* **说明**：尝试升级合约时验证失败
* **解决方案**：验证签名者、观察者、合约密钥、密钥维护者和包名称均未更改
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 3.3.2。管理服务错误组

### 3.3.2.1。派对管理服务错误

#### 已检测到并发\_派对\_详细信息\_更新\_

* **解释**：可以通过提供带有资源版本的更新请求来控制对一方的并发更新（这是可选的）。可以通过Ledger API读取该参与方来获取该参与方的资源版本。尝试使用过时的资源版本更新一方，这表明之前有不同的进程更新了该方。
* **解决方案**：再次阅读此部分以获取其最新状态，特别是其最新资源版本。使用获得的信息构建并发送新的更新请求。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 内部\_派对\_记录\_已经存在\_

* **解释**：该参与者节点已知的每个账本方都可以分配给它参与者的本地元数据。有关该请求所引用的一方的本地信息在本应找不到的情况下却被找到了。
* **解决方案**：此错误可能表明服务器的存储或实现存在问题。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 内部\_派对\_记录\_未\_找到

* **解释**：该参与者节点已知的每个账本方都可以分配给它参与者的本地元数据。本应找到的有关此请求所引用的一方的本地信息却没有找到。
* **解决方案**：此错误可能表明服务器的存储或实现存在问题。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 无效\_PARTY\_详细信息\_更新\_请求

* **解释**：尝试使用无效的更新请求来更新一方。
* **解决方案**：检查错误详细信息以获取有关导致请求无效的具体信息。使用调整后的更新请求重试。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 最大\_派对\_详细信息\_注释\_大小\_超出* **说明**：一方最多可以拥有 256kb 的注释，以 UTF-8 编码的字节数来衡量。尝试分配或更新一方，导致超出此限制。
* **解决方案**：使用较少的注释重试或删除该方的一些现有注释。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未找到派对

* **解释**：找不到请求引用的一方。
* **解决方案**：检查您是否正在连接到正确的参与者节点以及参与方拼写是否正确。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.2.2。用户管理服务错误

#### 检测到并发\_用户\_更新\_

* **说明**：可以通过提供带有资源版本的更新请求来控制对用户的并发更新（这是可选的）。用户的资源版本可以通过Ledger API读取用户来获取。尝试使用过时的资源版本更新用户，这表明之前有不同的进程更新了用户。
* **解决方案**：再次读取该用户以获取其最新状态，特别是其最新资源版本。使用获得的信息构建并发送新的更新请求。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 无效\_用户\_更新\_请求

* **解释**：尝试使用无效的更新请求来更新用户。
* **解决方案**：检查错误详细信息以获取有关导致请求无效的具体信息。使用调整后的更新请求重试。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 最大\_用户\_注释\_大小\_超出

* **说明**：用户最多可以拥有 256kb 的注释，以 UTF-8 编码的字节数来衡量。尝试创建或更新用户导致超出此限制。
* **解决方案**：使用较少的注释重试或删除用户的一些现有注释。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 太多用户权利

* **说明**：一个用户只能拥有有限数量的用户权限。试图创建具有太多权限的用户或向用户授予太多权限。
* **解决方案**：使用较少数量的权限重试或删除该用户的一些已存在的权限。如果限制太低，请联系参与运营商。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 用户已存在

* **解释**：已经存在具有相同用户 ID 的用户。
* **解决方案**：检查您是否连接到正确的参与者节点并且用户 ID 拼写正确，或者使用已存在的用户。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 用户更新时已删除

* **解释**：尝试更新用户，但不同的进程同时删除了该用户。
* **解决方案**：再次读取所有用户并使用另一个用户重新尝试该操作。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 未找到用户* **解释**：找不到请求引用的用户/idp 组合。
* **解决方案**：检查您是否连接到正确的参与者节点并且用户 ID 拼写正确，如果是，则创建用户。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.2.3。 IdentityProviderConfigService错误

#### IDP\_CONFIG\_已经存在\_EXISTS

* **说明**：已存在具有相同身份提供商 ID 的身份提供商配置。
* **解决方案**：检查您是否连接到正确的参与者节点并且身份提供商 ID 拼写正确，或者使用已存在的身份提供商。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### IDP\_CONFIG\_BY\_ISSUER\_NOT\_FOUND

* **解释**：找不到请求引用的身份提供商配置。
* **解决方案**：检查您是否连接到正确的参与者节点并且身份提供程序配置拼写正确，或者创建配置。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### IDP\_CONFIG\_ISSUER\_已经存在\_EXISTS

* **说明**：已存在具有相同颁发者的身份提供商配置。
* **解决方案**：检查您是否连接到正确的参与者节点并且身份提供商 ID 拼写正确，或者使用已存在的身份提供商。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### IDP\_CONFIG\_NOT\_FOUND

* **解释**：找不到请求引用的身份提供商配置。
* **解决方案**：检查您是否连接到正确的参与者节点并且身份提供程序配置拼写正确，或者创建配置。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 无效\_IDENTITY\_PROVIDER\_UPDATE\_REQUEST

* **解释**：尝试使用无效的更新请求来更新身份提供商配置。
* **解决方案**：检查错误详细信息以获取有关导致请求无效的具体信息。使用调整后的更新请求重试。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 太多身份提供者配置

* **说明**：系统只能有有限数量的身份提供商配置。尝试创建身份提供者配置。
* **解决方案**：删除一些已经存在的身份提供商配置。如果限制太低，请联系参与运营商。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.3.3。管理服务错误

#### 配置\_条目\_被拒绝

* **解释**：当新配置被拒绝时，会给出此拒绝。
* **解决方案**：获取最新配置和/或重试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 内部\_无效\_密钥* **解释**：配置的系统使用的加密密钥无效
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 包\_上传\_被拒绝

* **解释**：当包上传被拒绝时，会给出此拒绝。
* **解决方案**：请参阅收到的错误的详细消息。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.3.4。请求验证错误

#### 已披露\_合同\_冲突\_有效负载

* **解释**：当提交的账本 API 命令包含已披露的合约且同一合约 ID 的有效负载有冲突时，会发出此错误。
* **解决方案**：这可能被视为安全事件或服务器上的缺陷。请联系支持人员或所披露的合同有效负载的提供商。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_参数

* **解释**：当提交的账本 API 命令包含无效参数时，会发出此错误。
* **解决方案**：检查给出的原因并更正您的申请。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_DEDUPLICATION\_PERIOD

* **解释**：当提交的账本 API 命令指定无效的重复数据删除周期时，会发出此错误。
* **解决方法**：检查错误信息，调整重复数据删除周期的值或要求参与运营商增加最大重复数据删除周期。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 无效\_FIELD

* **解释**：当提交的账本 API 命令包含无法理解的字段值时，会发出此错误。
* **解决方案**：检查给出的原因并更正您的申请。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### Ledger\_TIME\_OUTSIDE\_BUNDS

* **解释**：当尝试在交易所需的账本时间范围之外提交交易时，会发出此错误。
* **解决方案**：如果时间范围在未来，则在时间范围内重试，如果在过去，则需要使用当前或未来时间准备新事务
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 缺失\_FIELD

* **解释**：当提交的账本 API 命令中未设置必填字段时，会发出此错误。
* **解决方案**：检查给出的原因并更正您的申请。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 负偏移

* **解释**：提供的偏移量是一个负整数。
* **解决**：确保指定的偏移量是负整数。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 非正偏移* **说明**：提供的偏移量不是正整数。
* **解决方案**：确保指定的偏移量是正（非零）整数。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 偏移\_之后\_LEDGER\_END

* **解释**：当读取请求使用超出当前账本末尾的偏移量时，会给出此拒绝。
* **解决方案**：使用账本结束之前的偏移量。
* **类别**：InvalidGivenCurrentSystemStateSeekAfterEnd
* **传输**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status OUT\_OF\_RANGE 在 API 上公开，包括详细的错误消息。

#### 范围偏移\_OUT\_OF\_范围

* **解释**：当读取请求使用请求上下文中无效的偏移量时，会给出此拒绝。
* **解决方案**：检查错误消息并使用有效的偏移量。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 参与者\_数据\_访问\_在\_LEDGER\_END之后

* **解释**：当读取请求尝试在账本结束后访问数据时，会给出此拒绝
* **解决方案**：使用账本结束之前的偏移量。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 参与者\_修剪\_数据\_访问

* **解释**：当读取请求尝试访问修剪的数据时，会给出此拒绝。
* **分辨率**：使用修剪偏移之后的偏移。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未知\_资源

* **解释**：当提交的账本 API 命令引用不存在的资源时，会发出此错误。
* **解决方案**：检查给出的原因并更正您的申请。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.4.1。未找到

#### 未找到合同事件

* **说明**：指定合约 ID 的事件不存在或指定的事件格式将其过滤掉。
* **解决方案**：检查合约 ID 并验证请求的事件没有被事件格式过滤掉。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 没有\_接口\_PACKAGE\_NAME\_和\_QUALIFIED\_NAME

* **解释**：查询到的指定包名和接口限定名的类型引用没有引用该参与者上传的任何接口
* **解决方案**：使用引用已上传接口 ID 的接口限定名称或要求参与者操作员上传必要的包。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 没有\_PACKAGE\_NAME\_和\_QUALIFIED\_NAME 的模板

* **解释**：查询到的指定包名和模板限定名的类型引用没有引用该参与者上传的任何模板
* **解决方案**：使用引用已上传模板 ID 的模板限定名称或要求参与者操作员上传必要的包。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未找到包名称* **解释**：查询到的包名与该参与者上传的包名不匹配。
* **解决方案**：使用有效的包名称或要求参与者操作员上传必要的包。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未找到包

* **解释**：当读取请求尝试访问分类帐上不存在的包时，会给出此拒绝。
* **解决方案**：使用与账本上现有包相关的包 ID。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 模板\_或接口\_未找到\_

* **解释**：查询的模板或接口id不存在。
* **解决方案**：在查询中使用有效的模板或接口 ID，或要求参与者操作员上传包含必要接口/模板的包。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未找到更新

* **解释**：更新不存在或指定的更新格式将其过滤掉。
* **解决方案**：检查更新 ID 或偏移量，并验证请求的更新没有被更新格式过滤掉。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.5。一致性错误

#### 未找到合同

* **解释**：如果 Daml 引擎找不到引用的合约，则会出现此错误。这可能是由于参与者不知道合同、提交方不知道合同或已经存档而导致的。
* **解决方案**：如果合约存在争用，则会出现此错误类型。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 重复\_命令

* **说明**：具有给定命令 ID 的命令已被成功处理。
* **分辨率**：正确的分辨率取决于用例。如果收到的错误与由于超时而重试的提交有关，则无需执行任何操作，因为之前的命令已被接受。如果意图提交新命令，请使用不同的命令 ID 重新提交。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 重复合同密钥

* **解释**：此错误表明在交易中我们达到了两个具有相同密钥的合约处于活动状态的程度。
* **解决方案**：此错误表示应用程序错误。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 不一致

* **解释**：至少一个输入已被并发事务提交更改。
* **解决方案**：正确的解决方案取决于业务流程，例如，可以在没有存档合同作为输入的情况下继续进行，或者可以重试交易提交以加载合同密钥的最新值。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 不一致的\_合同\_密钥* **解释**：输入合约密钥通过并发交易提交重新分配给不同的合约。
* **解决方案**：重试事务提交。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 已提交\_飞行中\_

* **说明**：具有相同更改 ID（用户 ID、命令 ID、actAs）的另一个命令提交已在处理中。
* **解决方案**：监听命令完成流，直到发布运行中命令提交的完成。或者，重新提交该命令。如果此时正在进行的提交已成功完成，这将返回有关先前提交的更详细信息。如果此时正在进行的提交失败，则重新提交将尝试在分类账上记录新交易。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 3.3.6。包服务错误

#### DAR\_依赖\_无效\_

* **解释**：此错误表明上传的 Dar 已损坏，因为缺少内部依赖项或具有未使用的内部依赖项。
* **解决方案**：联系 Dar 的供应商。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### DAR\_验证\_错误

* **解释**：该错误表明上传的dar验证失败。
* **解决方案**：检查错误消息并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 包\_服务\_内部\_错误

* **解释**：此错误表示软件包服务中存在内部问题。
* **解决方案**：检查错误消息并联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

### 3.3.6.1。阅读

#### DAR_解析错误

* **解释**：该错误表示无法成功解析Dar文件的内容。
* **解决方案**：检查错误消息并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_DAR

* **解释**：此错误表明提供的 dar 文件无效。
* **解决方案**：检查错误消息以了解详细信息并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_DAR\_FILE\_NAME

* **解释**：此错误表明提供的 dar 文件名不符合存储在持久性存储中的要求。
* **解决方案**：检查错误消息以了解详细信息并相应地更改文件名
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_LEGACY\_DAR

* **解释**：此错误表明提供的压缩 dar 是不受支持的旧版 Dar。
* **解决方案**：请使用更新的 dar 版本。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_ZIP\_条目* **解释**：此错误表明提供的压缩 dar 文件无效。
* **解决方案**：检查错误消息以了解详细信息并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### DAR 中的主包与预期不匹配

* **解释**：上传的DAR的主包与预期的包id不匹配。
* **解决方案**：调查 DAR 的来源以及它是否被操纵或提供的包 ID 是否错误。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### ZIP\_BOMB

* **解释**：此错误表明提供的压缩 dar 被视为 zip-bomb。
* **解决方案**：检查 dar 并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 3.3.7。同步服务拒绝错误

#### 派对在 LEDGER 上未知

* **解释**：尚未分配一个或多个知情方。
* **解决方案**：检查所有被通知方标识符是否正确，分配所有被通知方，请求分配或等待分配，然后重试交易提交。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 提交者\_不能\_通过\_参与者采取行动

* **说明**：提交方无权通过参与者行事。
* **解决方案**：联系参与运营商或向授权方重新提交。
* **类别**：权限不足
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它以 grpc-status PERMISSION\_DENIED 的形式公开在 API 上，没有任何详细信息。

#### 正在向 LEDGER 提交未知的当事人

* **说明**：提交方尚未分配。
* **解决办法**：检查参与方标识符是否正确，分配提交方、请求分配或等待分配后再重试交易提交。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.3.7.1。内部

#### 内部\_重复\_键

* **解释**：参与者没有检测到交易提交尝试对两个活动合约使用相同的密钥。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 内部按键不一致

* **解释**：参与者没有检测到交易中密钥使用不一致。在交易中，由于 <span class="title-ref">key -> 合约 ID</span> 的映射与之前的操作不一致，练习、fetch 或 LookupByKey 失败。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

### 3.3.8。 JsonApi错误

#### JSON\_API\_最大\_列表\_元素\_NUMBER\_达到* **说明**：当返回的元素数量等于或大于节点限制时会发生这种情况。该限制由节点配置定义，并且可以由操作员更改。检查“canton.参与方s.\<参与方-id>.http-ledger-api.websocket-config.http-list-max-elements-limit”。注意：如果在参与者节点配置中进行了配置，则实际返回的数量是请求中的“limit”查询参数与该参数之间的最小值。如果请求查询“限制”与上述配置相同，则允许返回设置为服务器限制的结果，而不会产生错误。
* **解决方案**： 1. 首选解决方案是使用 websocket 端点以块的形式获取结果。 2. 可以通过更改节点配置“http-list-max-elements-limit”来增加限制，但这可能会对节点性能产生严重影响。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### JSON\_API\_PACKAGE\_SELECTION\_FAILED

* **解释**：当 Ledger JSON API 服务器无法找到一组合适的 package-id 来解码请求中给定的命令集时，就会发生此错误。
* **解决方法**：检查错误消息并确保： 1. 请求的包已上传到参与节点上。 2. 拓扑状态满足相关方的审查要求
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.4。Canton包裹服务错误

#### 包\_或\_DAR\_删除\_错误

* **解释**：软件包服务在删除软件包时引发的错误。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 程序包\_服务\_无法\_自动检测\_同步器

* **解决办法**：如果节点没有连接任何同步器，请先连接一个同步器。如果参与者连接到多个同步器，请显式指定同步器 ID。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 程序包服务未连接到同步器

* **解决方案**：在审查软件包之前连接到同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.4.1。审查

#### 模糊\_审查\_参考

* **说明**：经过审查的包参考与包存储中的多个包相匹配。
* **解决方案**：检查提供的经过审查的包参考并重试该操作。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未解决\_审查\_参考

* **解释**：经过审查的包引用与包存储中的任何包都不匹配。
* **解决方案**：检查提供的经过审查的包参考并重试该操作。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.4.2。抓取

#### 未找到 DAR

* **解释**：请求中指定的 ID 与参与者上存储的 DAR 的主包 ID 不匹配。
* **解决方案**：检查提供的包 ID 并重试该操作。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 找不到包内容* **解释**：此错误表明请求的包在包存储中不存在。
* **解决方案**：提供现有的包 ID
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.5。交易错误组

### 3.5.1。本地拒绝错误

### 3.5.1.1。作业拒绝

#### 作业\_已经\_完成

* **解释**：如果作业已经完成，则参与者会发出此拒绝。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 当地判决激活现有合同

* **解释**：此错误表明该分配将激活已经存在的合同。
* **解决方案**：此错误表明存在错误或恶意行为。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 3.5.1.2。重新分配拒绝

#### 不一致\_重新分配\_ID

* **解释**：重新分配 ID 的验证检查失败。
* **解决方案**：这表明存在恶意或错误行为。
* **类别**：UnredactedSecurityAlert
* **传送**：此错误在服务器端以日志级别 ERROR 记录，并通过 grpc-status INVALID\_ARGUMENT 公开在 API 上，包括详细的错误消息。

#### 重新分配\_验证\_失败

* **解释**：重新分配的验证检查失败。
* **解决方案**：这表示由于动态拓扑更改或恶意或错误行为而导致的竞争状况。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.5.1.3。格式错误的拒绝

#### 本地\_VERDICT\_BAD\_ROOT\_HASH\_MESSAGES

* **解释**：如果交易不包含有效的根哈希消息，则参与者会做出此拒绝。
* **解决方案**：这表示由于动态拓扑更改或恶意或错误行为而导致的竞争状况。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 当地判决创建现有合同

* **解释**：此错误表明该交易将创建已经存在的合约。
* **解决方案**：此错误表明存在错误或恶意行为。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 本地\_结论\_失败\_模型\_一致性\_检查

* **解释**：如果交易未通过模型一致性检查，则参与者会做出此拒绝。
* **解决方案**：这表示恶意或错误行为。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 本地\_VERDICT\_MALFORMED\_PAYLOAD

* **解释**：如果交易视图格式错误，则参与者会做出此拒绝。
* **解决方案**：这表示恶意或错误行为。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 本地\_VERDICT\_MALFORMED\_REQUEST

* **解释**：如果请求格式不正确，则参与者会做出拒绝。
* **解决方案**：请联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 3.5.1.4。一致性拒绝

#### 当地判决无效合同* **说明**：交易指的是之前已存档、重新分配给另一个同步器或不存在的合约。
* **解决方案**：检查您的合约状态并尝试不同的交易。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 当地\_结论\_锁定\_合同

* **说明**：交易是指正在被其他交易创建、重新分配或存档的锁定合约。如果其他事务失败，则可以成功重试此事务。
* **解决方案**：重试事务
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 3.5.1.5。时间拒绝

#### 本地\_VERDICT\_LEDGER\_TIME\_OUT\_OF\_BOUND

* **解释**：如果账本时间和记录时间相差超过允许的范围，则会抛出此错误。由于高延迟或解释时间长的事务，这种情况可能会发生在过载的系统中。
* **解决方案**：对于长时间运行的交易，通过命令提交指定账本时间或调整动态同步器参数 ledgerTimeRecordTimeTolerance （以及可能的参与者和中介反应超时）。对于短期运行的事务，只需重试即可。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 当地\_VERDICT\_PREPARATION\_TIME\_OUT\_OF\_BOUND

* **解释**：如果准备时间和记录时间相差超过允许的范围，则会抛出此错误。由于高延迟或解释时间长的事务，这种情况可能会发生在过载的系统中。
* **解决方案**：对于长时间运行的事务，调整与命令提交一起使用的分类帐时间范围。对于短期运行的事务，只需重试即可。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 本地判断超时

* **解释**：如果参与者本地确定超时，则会发送此拒绝。
* **解决方案**：首先，重新提交您的交易。如果拒绝仍然虚假出现，请考虑增加 <span class="title-ref">Dynamic同步器Parameters</span> 中的 <span class="title-ref">confirmationResponseTimeout</span> 或 <span class="title-ref">mediatorReactionTimeout</span> 值。如果拒绝看起来与超时设置无关，请验证定序器和中介器是否正常运行。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 3.5.1.6。取消分配拒绝

#### 取消分配\_活动\_检查\_失败

* **解释**：取消分配提交的活动性检查失败。如果要重新分配的合约已被重新分配或当前在同步器上被锁定（由于竞争事务），则会发生此拒绝。
* **解决方案**：根据您的用例和期望，重试事务。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.5.2。交易路由错误

#### 交易失败的自动重新分配

* **解释**：此错误表明自动重新分配无法成功，因为当前拓扑不允许重新分配完成，这主要是由于缺乏相关方的确认权限。
* **解决方案**：检查消息和您的拓扑并确保存在适当的权限。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。#### 路由\_内部\_错误

* **解释**：此错误表示 Canton 同步器路由器中存在内部错误。
* **解决方案**：请联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 无法获取静态参数

* **解释**：该错误表示无法查询静态参数信息。
* **解决办法**：检查参与者是否已连接到同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 无法获取拓扑快照

* **解释**：该错误表示无法查询拓扑信息。
* **解决办法**：检查参与者是否已连接到同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.5.2.1。格式错误的输入错误

#### 披露\_合同\_身份验证\_失败

* **解释**：无法根据提供的合同 ID 来验证所提供的披露合同。
* **解决方案**：确保通过命令提交提供的公开合约与源自 Ledger API 的原始合约创建内容相匹配。如果问题仍然存在，请联系参与运营商。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_已披露\_合同

* **解释**：无法处理所提供的披露合同。
* **解决方案**：确保通过命令提交提供的公开合约具有经过身份验证的合约 ID（即已在运行 Canton 协议版本 4 或更高版本的参与者节点中创建），并与源自 Ledger API 的原始合约创建格式和内容相匹配。如果问题仍然存在，请联系参与运营商。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_PARTY\_IDENTIFIER

* **解释**：给定的政党标识符不是有效的广东政党标识符。
* **解决方案**：确保您的命令仅引用系统上正确启用的政党的正确且有效的广东政党标识符
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_READER

* **说明**：定义为读者（actAs 或 readAs）的当事人无法解析为有效的 Canton 当事人。
* **解决方案**：检查您的应用程序中是否仅使用正确的设置方名称。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 3.5.2.2。拓扑错误

#### 信息\_不\_活跃

* **解释**：此错误表明通知者已知，但没有托管所有通知者的连接同步器。
* **解决方案**：确保有这样一个同步器，因为 Canton 需要一个所有通知者都在场的同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未连接到所有合同同步器* **解释**：此错误表明该交易引用了该参与者当前未连接的同步器上的合约。
* **解决方案**：检查同步器连接的状态。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### NO\_COMMON\_SYNCHRONIZER

* **解释**：此错误表明不存在所有提交者都可以提交并且所有通知者都连接到的公共同步器。
* **解决方案**：检查您的参与者节点是否已连接到您期望的所有同步器，并检查各方是否按照您期望的方式托管在这些同步器上。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 提交时没有同步器

* **解释**：此错误表明没有找到有效的同步器进行提交。
* **解决方案**：检查同步器连接的状态、软件包是否经过审查以及您是否已连接到运行最新协议版本的同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 所有提交者都可以提交的同步器上没有

* **解释**：此错误表明交易已发送，系统找不到任何活动的“+”同步器，该参与者可以在该同步器上以给定提交者集的名义进行提交。
* **解决方案**：确保您已连接到该参与者具有提交权限的同步器。检查您是否确实连接到了您希望连接的同步器，并检查您的参与节点是否具有每个提交方的提交权限。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 提交者\_不\_活跃

* **解释**：此错误表示提交者已知，但没有托管所有提交者的连接同步器。
* **解决方案**：确保存在这样的同步器，因为 Canton 需要所有提交者都在场的同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 提交者\_始终\_利益相关者

* **解释**：此错误表明交易需要重新分配合约，而提交者必须是利益相关者。
* **解决方案**：检查您的参与者节点是否已连接到您期望的所有同步器，并检查各方是否按照您期望的方式托管在这些同步器上。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未知合同同步器

* **解释**：此错误表明该交易引用的合约的同步器当前未知。
* **解决方案**：确保交易使用的合约上的所有重新分配操作均已完成，并检查与同步器的连接。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未知\_信息者* **解释**：此错误表明该事务引用了一些在任何连接的同步器上都不知道的通知者。
* **解决方案**：检查提交的通知者列表，并检查您的参与者是否连接到您期望的同步器。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未知\_提交者

* **解释**：此错误表明事务引用了任何连接的同步器上未知的某些提交者。
* **解决方案**：检查提供的提交者列表，并检查您的参与者是否连接到您期望的同步器。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.5.2.3。配置错误

#### 指定同步器 ID 无效

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 提交\_SYNCHRONIZER\_NOT\_READY

* **解释**：此错误表明事务应该提交到未连接或未配置的同步器。
* **解决办法**：确保workflowId中指定的同步器已正确连接。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.5.3。本地弃权错误

#### 无法执行所有验证

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.5.4。提交错误

#### 选择的调解员不活跃

* **解释**：为事务选择的中介在请求排序之前被停用。
* **解决方案**：重新提交。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 合同\_身份验证\_失败

* **解释**：至少一项交易的输入合约无法验证。
* **解决方案**：使用经过正确验证的合约重试提交。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_外部\_签名

* **解释**：当提交带有外部签名的交易，但签名无效时，会出现此错误。这可能是由不正确的哈希计算或无效的签名密钥引起的。
* **解决方案**：检查使用的哈希函数是否正确，以及签名密钥是否为提交方正确注册。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_外部\_交易

* **说明**：当提交具有外部签名的无效交易且无法计算有效哈希时，会发生此错误。
* **解决方案**：检查错误消息并重新提交有效的交易。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 格式错误\_REQUEST

* **解释**：此错误尚未正确分类为子错误代码。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 未排序超时* **解释**：当事务未在预定义的最大排序时间内排序并因此超时时，就会发生此错误。最大排序时间是通过账本时间模型偏差从交易的账本时间导出的。
* **解决办法**：如果由于高负载导致延迟，请重新提交。如果命令需要对参与者进行大量处理，请在命令提交时指定更高的最小分类账时间，以便得出更高的最大排序时间。或者，您可以增加动态同步器参数 ledgerTimeRecordTimeTolerance。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 没有有效收件人查看

* **解释**：当交易不包含有效的收件人集时，会发生此错误。
* **解决方案**：在请求提交期间，各方和参与者之间的关系可能同时发生变化。重新提交请求。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 包裹未经收件人审核

* **解释**：如果提交的交易引用了接收参与者尚未审查的包，则会发生此错误。任何交易视图只能引用已被接收参与者明确批准的包。
* **解决方案**：确保接收参与者上传并审查相应的包。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 参与者\_过载

* **解释**：参与者在可配置的宽限期内拒绝了所有传入命令。
* **解决方案**：配置更严格的资源限制（仅限企业）。更改应用程序以较低的速率提交命令。为 <span class="title-ref">my参与方.parameters.warnIfOverloadedFor</span> 配置更高的值。
* **类别**：共享资源争用
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 定序器\_BACKPRESSURE

* **解释**：当定序器由于背压而拒绝接受命令时，会发生此错误。
* **解决方案**：稍等一下然后重试，最好有一些退避系数。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 定序器\_请求\_失败

* **解释**：当命令无法发送到同步器时会出现此错误。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 提交\_在关机期间\_

* **解释**：当系统执行关闭时提交命令时，会出现此错误。
* **解决方案**：假设参与者最终将重新启动或故障转移，请在几秒钟后重试。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 提交\_内部\_错误

* **解释**：事务提交期间发生内部错误。
* **解决方案**：请联系支持人员并提供失败原因。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 同步器\_不带\_中介* **解释**：参与者将交易路由到没有活动中介者的同步器。
* **解决方案**：向同步器添加中介者。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 未知\_合同\_同步器

* **解释**：如果提交的交易引用同步器上未知的合约，则会发生此错误。如果事务与归档或取消分配之间存在竞争条件，则可能会发生这种情况。
* **解决方案**：检查同步器是否提交和/或重新提交事务。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.5.5。同步服务注入错误

#### 命令\_注入\_失败

* **说明**：如果内部错误导致异常，则会出现此错误。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 节点\_IS\_被动\_副本

* **解释**：如果将命令提交到被动副本，则会出现此错误。
* **解决方案**：将命令发送到活动副本。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 未连接到任何同步器

* **解释**：当特定请求提交给未连接到任何同步器的参与者时，会出现此错误。
* **解决方案**：将您的参与者连接到同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未连接到同步器

* **解释**：如果将命令提交给未连接到处理该命令所需的同步器的参与者，则会出现此错误。
* **解决方案**：将您的参与者连接到所需的同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.6。同步服务错误

#### 无效\_参数\_同步\_服务

* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 各方分配_无法确定同步器

* **说明**：参与者连接到多个同步器，因此无法自动检测该方应分配到哪个同步器。
* **解决方案**：显式指定要在其上分配一方的同步器或与除一个同步器之外的所有同步器断开连接。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 方\_分配\_没有\_连接\_同步器

* **解释**：参与者未连接到同步器，因此无法分配参与方，因为参与方通知配置为`party-notification.type = via-同步器`。
* **解决方案**：首先将参与者连接到同步器或将参与者的派对通知配置更改为`eager`。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器\_注册* **解释**：此错误是由于尝试注册新同步器而导致的。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 同步\_服务\_警报

* **解释**：参与者检测到另一个节点有恶意行为。
* **解决方案**：联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 同步\_服务\_别名\_分辨率

* **解释**：如果服务无法推断别名的活动同步器，则会出现此错误。
* **解决方案**：请确认同步器别名正确，或在（重新）连接之前配置同步器。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_坏\_连接

* **解释**：如果尝试注册新的或更改现有定序器连接时验证失败，则会报告此错误。这可能是由于无法访问的节点、错误的 TLS 配置、或者定序器报告的同步器 ID 不匹配或定序器组内的定序器 ID 不匹配导致的。
* **解决方案**：检查提供的连接设置是否正确。如果它们只是对应于暂时不活动的定序器，您也可以关闭验证。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_变为被动\_

* **解释**：当连接的同步器由于参与者变得被动而断开连接时，会记录此错误。
* **解决方案**：故障转移到活动参与者副本。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_内部\_错误

* **解释**：此错误表明存在内部问题。
* **解决方案**：请联系支持人员并提供失败原因。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 同步\_服务\_被动\_副本

* **解释**：如果向被动副本提交管理命令，则会出现此错误。
* **解决方案**：将管理命令发送到活动副本。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_物理\_ID\_注册

* **解释**：如果服务无法注册给定别名的物理同步器 ID，则会出现此错误。
* **解决方法**：请确认同步器别名和 ID 是否正确。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_启动\_错误

* **解释**：此错误表示同步器无法正确启动或初始化。
* **解决方案**：请检查潜在错误并重试（如果可能）。如果没有，请联系支持人员并提供失败原因。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步服务同步器必须离线* **解释**：当尝试执行操作（例如需要断开同步器并进行清理的修复）时，会发出此错误。
* **解决方案**：在尝试该命令之前断开仍然连接的同步器。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_同步器\_禁用\_US

* **解释**：当同步服务因远程定序器 API 拒绝访问而关闭时，会记录此错误。
* **解决方案**：联系定序器操作员并询问为什么不允许您再连接。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步服务同步器已断开

* **解释**：当连接的同步器意外地与 Canton 同步服务断开连接时（之前已连接），会记录此错误
* **解决方案**：请联系支持人员并提供失败原因。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 同步服务同步器不得在飞行交易中进行

* **解释**：当事务仍在源同步器上进行时尝试同步器迁移时，会发出此错误。
* **解决方案**：通过将参与者重新连接到源同步器、停止参与者上的活动并等待正在进行的事务完成或超时，确保源同步器没有正在进行的事务。然后再次调用 <span class="title-ref">migrate\_同步器</span>。作为最后的手段，您可以使用命令上的 <span class="title-ref">force</span> 标志强制同步器迁移忽略正在进行的事务。请注意，强制迁移可能会导致账本分叉。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_同步器\_状态\_不\_活动

* **解释**：当同步器处于非活动状态时，会记录此错误。
* **解决方案**：如果您尝试连接到已迁移或有待迁移的同步器，则会发出此错误。请在尝试连接之前完成迁移。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步\_服务\_未知\_同步器

* **解释**：如果同步器连接命令引用尚未注册的同步器别名，则会出现此错误。
* **解决方案**：请确认同步器别名正确，或在（重新）连接之前配置同步器。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.6.1。同步器迁移错误

#### 同步器迁移损坏

* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 无效的同步器迁移请求

* **解释**：当无效参数传递给迁移命令时，会出现此错误。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.6.2。同步器注册表错误

#### 初始\_ONBOARDING\_错误* **解释**：此错误表明存在初始登录问题。
* **解决方案**：检查根本原因并重试（如果可能）。如果没有，请联系支持人员并提供失败原因。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器\_注册表\_内部\_错误

* **解释**：此错误表明 Canton 注意到存在内部错误。
* **解决方案**：联系支持人员并提供失败原因。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 拓扑\_转换\_错误

* **解释**：此错误表示在连接到同步器期间转换拓扑事务时出现错误。
* **解决方法**：联系该节点的拓扑管理运营商。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 3.6.2.1。配置错误

#### 无法颁发\_SYNCHRONIZER\_TRUST\_CERTIFICATE

* **解释**：此错误表明参与者无法颁发同步器信任证书。这样的证书是同步器上激活所必需的。因此，它必须存在于参与者拓扑管理器的授权存储中。
* **解决方案**：手动上传给定同步器的有效同步器信任证书或上传必要的证书，以便参与者可以自动颁发此类证书。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 静态同步器参数配置错误

* **解释**：此错误表明参与者配置为连接到同步器的多个定序器，但它们的静态同步器参数与其他定序器不同。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 来自不同同步器的序列器已配置

* **解释**：此错误表明参与者被配置为从不同的同步器连接到多个同步器排序器。
* **解决方案**：仔细验证连接设置。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器参数已更改

* **解释**：错误表明同步器参数已更改，但尚不支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.6.2.2。连接错误

#### 连接到SEQUENCER 失败

* **解释**：此错误表明参与者无法连接到定序器。
* **解决方案**：检查提供的原因。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 连接到序列器失败

* **解释**：此错误表示参与者无法连接到定序器。
* **解决方案**：检查提供的原因。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### GRPC\_CONNECTION\_FAILURE* **解释**：此错误表示参与者由于一般 GRPC 错误而无法连接。
* **解决方案**：检查提供的原因并联系支持人员。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 参与者\_不\_活跃

* **解释**：此错误表明连接参与者尚未被同步器操作员激活。如果参与者之前已成功连接到同步器，则此错误表明同步器操作员已停用该参与者。
* **解决方案**：联系同步器操作员并查询您的参与节点对给定同步器的权限。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器不可用

* **解释**：如果与同步器服务的 GRPC 连接失败且 GRPC 状态为 UNAVAILABLE，则会出现此错误。
* **解决方案**：检查您的连接设置并确保确实可以到达同步器。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

### 3.6.2.3。握手错误

#### 同步器\_别名\_重复

* **解释**：此错误表明同步器别名之前曾用于连接到具有不同同步器 ID 的同步器。当现有参与者尝试连接到新近重新初始化的同步器时，这是一种已知的情况。
* **解决方案**：仔细验证连接设置。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器\_加密\_握手\_失败

* **解释**：此错误表明同步器正在使用该参与者不支持或未启用的加密设置。
* **解决方案**：查阅错误消息并调整该参与者支持的加密方案。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器\_握手\_失败

* **解释**：此错误表明参与者与同步器握手失败。
* **解决方案**：检查提供的原因以了解更多详细信息并联系支持人员。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 同步器\_ID\_MISMATCH

* **解释**：此错误表明同步器 id 与参与者期望的不匹配。如果此错误发生在第一次连接时，则同步器连接设置中定义的同步器 ID 与远程同步器不匹配。如果重新连接时发生这种情况，则远程同步器已因某种原因被重置。
* **解决方案**：仔细验证连接设置。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.7。管理工作流程服务

#### 不能自动\_VET\_ADMIN\_WORKFLOW\_PACKAGE* **解释**：此错误表示无法审查管理工作流程包。管理工作流程是一组预安装的包，可用于管理流程。如果手动初始化参与者但缺少适当的签名密钥或证书以便在参与者命名空间内发出新的拓扑事务，则可能会发生错误。在参与者审核该包之前，无法使用管理工作流程。
* **解决方案**：可以通过确保以该参与者的名义发出适当的审核交易并将其导入该参与者节点来修复此错误。如果参与者启动后已添加相应的证书，则可以通过重新启动参与者节点、手动发出审核交易或重新上传 Dar（将 vetAllPackages 参数保留为 true）来修复此错误
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

### 3.8。维修服务错误

#### 合同\_分配\_变更\_错误

* **解释**：合同的分配由于错误而无法更改。
* **解决方案**：操作员干预后重试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 合同\_清除\_错误

* **说明**：合约因错误而无法被清除。
* **解决方案**：操作员干预后重试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 合同\_序列化\_错误

* **解释**：由于错误，合约无法序列化。
* **解决方案**：操作员干预后重试。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 导入\_ACS\_错误

* **解释**：导入 ACS 失败。
* **解决方案**：操作员干预后重试。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 不一致\_ACS\_SNAPSHOT

* **解释**：无法返回 ACS 快照，因为它包含不一致的内容。这可能是由于请求与修剪同时发生。
* **解决方案**：重试该操作
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 无效\_ACS\_SNAPSHOT\_TIMESTAMP

* **解释**：参与者不支持在请求的时间戳处提供 ACS 快照，可能是因为某些并发处理尚未完成。
* **解决方案**：确保已通过某种方式从参与者处获取指定的时间戳。如果是这样，请稍后重试（可能会重复）。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 无效\_参数\_修复

* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_状态\_修复\_错误

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### IO\_STREAM\_修复\_错误

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 手动\_逻辑\_同步器\_升级\_错误* **解释**：手动逻辑同步器升级失败
* **解决方案**：操作员干预后重试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 不可用\_ACS\_SNAPSHOT

* **解释**：参与者不支持在请求的时间戳处提供 ACS 快照，因为其数据库已被修剪，例如通过连续后台修剪过程。
* **解决方案**：请求时间戳处的快照不再可用。如果可能，选择较新的时间戳。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.9。 LedgerApi错误

#### 堆内存超过限制

* **解释**：当 JVM 堆内存池超过预先配置的限制时，就会发生此错误。
* **解决方案**：可以采取以下操作： 1. 通过检查消息中给出的指标来查看堆空间的历史使用情况。 2. 查看速率限制配置中配置的当前堆空间限制。 3. 尝试将可能需要大量内存来处理的请求分开。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### LEDGER\_API\_内部\_错误

* **解释**：如果 Ledger API 中出现意外错误，则会发生此错误。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 最大\_NUMBER\_OF\_流

* **解释**：当并发 gRPC 流请求数量超过配置的限制时，会发生此错误。
* **解决方案**：可以采取以下操作： 1. 通过检查消息中给出的指标来查看并发流式传输的历史需求。 2. 查看速率限制配置中配置的最大流限制。 3. 尝试分隔流请求，以便它们不需要彼此并行运行。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 未找到\_首选包\_

* **解释**：如果参与者连接的同步器的拓扑状态无法满足请求中提供的审核要求，则会发生此错误。
* **解决方案**：检查错误消息并优化请求或稍后重试。如果错误仍然存​​在，请通知相关交易方其无效的拓扑状态。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 未经过审查的接口实施包

* **解释**：由于缺少经过审查的包，模板包名称的请求界面视图不可用。这可能是由于流订阅过时或由于兼容包的审查而导致接口实现停用。
* **解决**：关闭并重新打开流订阅以刷新用于渲染界面视图的审核状态。如果问题仍然存在并且是意外情况，请联系参与运营商。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 参与者\_背压* **解释**：当参与者由于负载过大而拒绝命令时，会发生此错误。负载可能由以下因素引起： 1. 当通过其 Ledger API 向参与者提交命令时， 2. 当参与者通过连接的同步器接收来自其他参与者的验证请求时。为了防止参与者过载，一旦达到一定的负载阈值，它将开始拒绝命令。主要阈值是参与者当前正在处理的正在进行的验证请求的数量。这些请求可以由该参与者或其他参与者引起。为了将提交算作正在进行的验证请求，参与者必须首先观察其顺序，这意味着提交和提交的命令之间存在延迟，该延迟将计入当前正在进行的验证请求。为了避免突然爆发的命令造成过载情况，参与者还将在接受提交进行解释之前强制执行速率限制。该速率限制可以配置稳态速率和突发因子。突发因子是稳态速率的乘数，允许在速率限制生效之前突发提交一定数量的命令。例如，速率限制为每秒 1000 个命令，突发因子为 2，一旦在速率限制允许的命令之上提交了 2000 个命令，速率限制就会生效。
* **解决方案**：验证参与者上配置的限制、负载和命令延迟，并在必要时进行调整。如果参与者负载较高，请确保您的应用程序在重新提交时等待一段时间，最好有一些退避系数。如果可能，请其他参与者发送更少的请求；同步器操作员可以通过施加速率限制来强制执行此操作。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 线程池\_OVERLOADED

* **说明**：当提交的 gRPC 请求的速率需要比可用的 CPU 或数据库能力更多时，就会发生这种情况。
* **解决方案**：可以采取以下操作：这里线程池的“队列大小”被认为是由执行器本身报告的。 1. 通过检查消息中给出的指标来查看历史“队列大小”增长情况。 2. 查看速率限制配置中配置的最大“队列大小”限制。 3. 尝试将可能需要大量 CPU 或数据库能力的请求分开。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 3.10。修剪服务错误

#### 非法\_参数\_修剪\_错误

* **解释**：由于非法参数，修剪失败。
* **解决方案**：识别调用返回的 gRPC 状态消息的错误详细信息中的非法参数。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 内部\_修剪\_错误

* **说明**：由于内部服务器错误，修剪失败。
* **解决方案**：确定服务器日志中的错误。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 之前无内部参与者数据* **解释**：参与者不持有指定时间和偏移量之前的内部账本状态。
* **解决方案**：参与者之前或当时不持有任何内部账本数据，并且偏移量指定为 <span class="title-ref">find\_safe\_offset</span> 的参数。通常，这意味着参与者已经修剪了指定时间和偏移量内的所有内部数据。因此，此错误表明之前无法找到要修剪的安全偏移量。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 清除\_未知\_同步器\_错误

* **解释**：已在未知同步器上调用同步器清除。
* **解决**：确保指定的同步器id存在。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 关闭\_中断\_修剪

* **解释**：修剪已中止，因为参与者正在关闭。
* **解决方案**：参与者重新启动后，确保参与者处于一致的状态。因此无需干预。重新启动后，可以像往常一样再次调用修剪，以将参与者修剪到所需的偏移量。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 修剪不安全

* **说明**：当前时间无法在指定偏移处进行剪枝。
* **解决方案**：指定较低的偏移量或稍后重试修剪。通常，您只能修剪较旧的事件。特别是，事件必须早于每个同步器的中介者反应超时和参与者超时之和。而且，您只能删除早于为此参与者配置的重复数据删除时间的事件。因此，如果您发现此错误，您要么只删除较旧的事件，要么调整该参与者的设置。错误详细信息字段<span class="title-ref">safe\_offset</span>包含当前可以修剪的最高偏移量（如果有）。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.11。索引错误

### 3.11.1。数据库错误

#### 索引\_DB\_SQL\_NON\_TRANSIENT\_ERROR

* **解释**：如果对索引数据库执行查询时出现非暂时性错误，则会出现此错误。
* **解决方案**：联系参与运营商。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 索引\_DB\_SQL\_TRANSIENT\_ERROR

* **解释**：如果在对索引数据库执行查询时出现暂时性错误，则会出现此错误。
* **解决方案**：重新提交请求。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

### 3.12。派对管理服务错误

#### 无效\_参数\_方\_管理\_错误

* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效\_STATE\_PARTY\_MANAGEMENT\_ERROR

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 无效\_时间戳\_派对\_管理\_错误* **解释**：参与者（尚）不支持在请求的时间戳处提供账本偏移量。发生这种情况可能是因为账本状态处理尚未跟上。
* **解决方案**：确保请求的时间戳有效。如果是这样，请在一段时间后重试（可能会重复）。
* **类别**：InvalidGivenCurrentSystemStateSeekAfterEnd
* **传输**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status OUT\_OF\_RANGE 在 API 上公开，包括详细的错误消息。

#### IO\_STREAM\_PARTY\_MANAGEMENT\_ERROR

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.13。参与者检查服务错误

#### 参与者\_检查\_非法\_争论\_错误

* **解释**：由于非法参数，检查失败。
* **解决方案**：识别调用返回的 gRPC 状态消息的错误详细信息中的非法参数。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 参与者\_检查\_内部\_错误

* **解释**：由于内部服务器错误，检查失败。
* **解决方案**：确定服务器日志中的错误。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

### 3.14。参与者复制服务错误

#### 参与者\_复制\_内部\_错误

* **解释**：内部参与者复制错误时发出内部错误
* **解决方案**：联系支持人员
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 参与者复制不支持存储

* **解释**：如果提供的存储配置不支持复制，则会发出错误。
* **解决方案**：使用支持复制的参与者存储后端。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 3.15。常见错误

#### 请求已在飞行中

* **说明**：具有相同 id 的另一个请求已在处理中。
* **解决方案**：监听适当的流，直到发布正在进行的请求的结果。或者，重新提交请求。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 请求\_截止日期\_超出

* **说明**：由于预定义的截止日期已过，请求尚未提交处理。
* **解决方案**：在更长的期限内重试请求。
* **类别**：DeadlineExceededRequestStateUnknown
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status DEADLINE\_EXCEEDED 在 API 上公开，包括详细的错误消息。

#### 请求\_超时\_OUT

* **解释**：当请求处理状态未知并且达到超时时，会给出此拒绝。
* **解决方案**：重试暂时性问题。如果是非瞬态，请联系操作员，因为超时限制可能太短。
* **类别**：DeadlineExceededRequestStateUnknown
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status DEADLINE\_EXCEEDED 在 API 上公开，包括详细的错误消息。

#### 服务\_内部\_错误

* **解释**：如果其中一项服务遇到意外异常，则会发生此错误。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 服务未运行* **解释**：当请求的服务未运行时，会给出此拒绝。它尚未启动或已关闭。
* **解决方案**：重试重新提交请求。如果错误仍然存​​在，请联系参与者操作员。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 不支持的\_操作

* **说明**：此错误类别用于表示客户端或参与者操作员请求已触发未实现的代码路径。
* **解决方案**：此错误是由参与者节点配置错误或实施错误引起的。解决方案需要参与者操作员干预。
* **类别**：内部不支持的操作
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它以 grpc-status UNIMPLMENTED 的形式暴露在 API 上，没有任何详细信息。

### 4. 序列器错误

#### 未找到块

* **解释**：此错误表示找不到给定时间戳的块。
* **解决方案**：验证时间戳是否正确以及排序器是否正常。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 无效\_确认\_签名

* **解释**：此错误表明定序器检测到无效的确认请求签名。这很可能表明该请求是伪造的并且是由恶意定序器创建的。所以它不会被处理。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_确认\_时间戳

* **解释**：此错误表示成员已确认其收到的事件之后的时间戳。这违反了测序协议。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_信封\_签名

* **解释**：此错误表明排序器在提交请求中检测到无效的信封签名。这很可能表明该请求是伪造的并且是由恶意定序器创建的。所以它不会被处理。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_LEDGER\_事件

* **解释**：排序器检测到无法解析分类帐上的某些事件。这可能是由于某些定序器节点的恶意行为或故障造成的。该事件将被忽略，处理将照常进行。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 无效\_提交\_请求\_签名

* **解释**：此错误表明排序器检测到无效的提交请求签名。这很可能表明该请求是伪造的并且是由恶意定序器创建的。所以它不会被处理。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 最大请求大小超出

* **解释**：这个错误表示请求大小已经超过了配置的值maxRequestSize。
* **解决方案**：发送较小的请求或增加同步器参数中的 maxRequestSize
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 最大排序时间超出* **解释**：此错误表示请求未排序，因为排序时间将超过请求的最大排序时间。如果参与者或中介节点响应请求太慢，或者在停机一段时间后赶上，通常会发生此错误。在极少数情况下，如果定序器节点严重过载，则可能会发生这种情况。如果重复发生，此信息可能表明相应的参与者或中介节点存在问题。
* **分辨率**：检查排序时间和最大排序时间之间的时间差。如果时间差很大，则某个远程节点正在追赶，但在追赶期间发送消息。如果差异不是太大，则提交节点或该定序器节点可能会过载。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 多个\_中介\_接收者

* **解释**：此错误表明参与者正在尝试在同一提交请求中向多个调解员或调解员组发送信封。这很可能表明该请求是伪造的并且是由恶意定序器创建的。所以它不会被处理。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 有效负载\_TO\_EVENT\_TIME\_BOUND\_EXCEEDED

* **解释**：此警告表示存储有效负载和写入“事件”之间的时间差超出了配置的时间限制，从而导致消息被丢弃。这种情况可能发生在数据库上的某些故障事件期间，导致这两个数据库操作之间出现意外延迟。（这两个事件需要足够接近，以支持按时间戳修剪有效负载）。
* **解决方案**：提交节点通常会重试该命令，但您应该检查定序器节点的运行状况，特别是在数据库处理方面。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

#### 在 \_BEFORE\_OR\_AT\_LOWER\_BOUND 处排序

* **解释**：此错误表示请求未排序，因为请求的排序时间早于排序器配置的排序时间下限。
* **解决方案**：等待时间提前超过测序时间下限。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端以日志级别 INFO 记录。

#### 未找到快照

* **解释**：此错误表示找不到给定时间戳的定序器快照。
* **解决方案**：验证时间戳是否正确以及排序器是否正常。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 5. Sequencer管理错误

#### 无法\_禁用\_本地\_SEQUENCER\_MEMBER

* **说明**：排序器无法禁用其本地订阅，因为这会禁用其适应拓扑更改的能力。
* **解决方案**：禁用定序器订阅通常是为了促进定序器修剪。如果排序器的本地订阅阻止排序器修剪，请考虑降低排序器时间跟踪器 <span class="title-ref">min\_observation\_duration</span>。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 6. 配置错误

#### 无法解析配置文件

* **解释**：通常会抛出此错误，因为配置文件不包含有效 HOCON 格式的配置。 HOCON 格式无效的最常见原因是忘记了括号。
* **解决方案**：确保所有文件均为有效的 HOCON 格式。
* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

#### 无法读取_配置文件* **解释**：当 Canton 找不到给定的配置文件时，通常会抛出此错误。
* **解决方案**：确保正确指定所有配置文件的路径和名称。
* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

#### 配置\_替换\_错误

* **解决方案**：此错误的常见原因是尝试使用配置文件中未定义的环境变量。
* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

#### 配置\_验证\_错误

* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

#### 通用\_配置\_错误

* **解决方案**：一般来说，这可能是许多错误之一，因为这是配置错误的“杂项类别”。此类别中最常见的错误之一是“未知密钥”错误。此错误通常意味着关键字无效（例如，它可能有拼写错误“bort”而不是“port”），或者在配置层次结构的错误部分使用了有效关键字（例如，要为参与者启用数据库复制，正确的配置是 <span class="title-ref">canton.参与方s.参与方2.replication.enabled = true</span> 而不是 <span class="title-ref">canton.参与方s.replication.enabled = true</span>）。请参阅产品配置参考，了解有效的配置关键字以及配置层次结构中的正确位置。
* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

#### 无配置文件

* **类别**：InvalidIndependentOfSystemState
* **传送**：如果使用给定配置启动 Canton 失败，则会记录配置错误并将其输出到标准输出

### 7. 拓扑管理错误组

### 7.1。拓扑管理器错误

#### 预览\_FEATURE

* **解释**：此错误表明需要启用预览功能。
* **解决方案**：将标记 <span class="title-ref">enablePreviewFeatures</span> 设置为 true 并重试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_无法\_删除\_映射

* **解释**：此错误表示无法删除映射。
* **解决方案**：使用REPLACE操作更改现有映射。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_确认\_阈值\_无法\_达到\_

* **解释**：此错误表明确认阈值高于托管节点数量，这将导致一方无法正常运行。
* **解决办法**：降低阈值或增加托管节点数量。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_危险\_命令\_需要\_FORCE\_ALIEN\_MEMBER

* **解释**：此错误表示可能破坏节点的危险命令被拒绝。如果在一个节点上运行危险命令以向另一个节点发出交易，就会出现这种情况。此类命令必须强制执行，因为它们非常危险，很容易破坏节点。举个例子，如果我们为参与者分配一个该参与者没有的加密密钥，那么该参与者将无法处理传入的交易。因此，我们必须非常小心，不要造成这样的情况。
* **解决方案**：如果您确实知道自己在做什么，请设置 ForceFlag.AlienMember。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_非法删除\_活动\_交易* **解释**：此错误表明参与者在仍然是托管方的情况下尝试撤销主动使用的拓扑事务。
* **解决方案**：参与者必须将自己从仍然引用它的参与者到参与者的映射中删除。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_不一致\_快照

* **解释**：此错误表明提交的拓扑快照内部不一致。
* **解决方案**：检查错误详细信息元数据中`transactions`字段中提到的事务是否不一致。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑增加准备时间容差

* **解释**：此错误表明已尝试以不安全的方式增加`preparationTimeRecordTimeTolerance`同步器参数。增加此参数可能会禁用安全检查，因此可能存在安全风险。
* **解决**：确保`preparationTimeRecordTimeTolerance`的新值最多为`mediatorDeduplicationTimeout`同步器参数的一半。使用 `my同步器.service.set_preparation_time_record_time_tolerance` 安全地增加 PreparationTimeRecordTimeTolerance。或者，如果您不关心安全性，请将标志 `ForceFlag.PreparationTimeRecordTimeToleranceIncrease` 添加到您的命令中。安全检查将在`preparationTimeRecordTimeTolerance`新值的两倍后再次生效。在同步器引导时使用`ForceFlag.PreparationTimeRecordTimeToleranceIncrease`是安全的。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_键不足\_

* **解释**：此错误表示拓扑事务中引用的成员尚未声明至少一个签名密钥或至少 1 个加密密钥或两者。
* **解决方案**：确保拓扑事务中引用的所有成员都已声明至少一个签名密钥和至少一个加密密钥，然后重新提交失败的事务。此错误的元数据详细信息包含字段 `members` 中缺少键的成员。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_无效\_映射

* **解释**：此错误表明提交的拓扑映射无效。
* **解决方案**：参与者应与错误详细信息元数据中的`parties`字段中提到的各方所有者合作，将自己从这些各方的托管参与者列表中删除。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_所有者\_到\_密钥\_映射无效

* **解释**：此错误表明提供的所有者到键映射不符合同步器的要求。
* **解决方案**：每个同步器都定义了支持的有效关键规范集。任何成员都必须提供至少一个具有有效规格的签名密钥。参与者还必须提供加密密钥。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_所有者\_至密钥\_映射的删除无效* **解释**：此错误表明所有者到键的映射仍在被另一个事务使用。
* **解决方案**：每个同步器成员都需要密钥才能注册。因此，在移除钥匙之前需要先移除该成员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_无效\_后继者

* **解释**：此错误表明后继同步器 ID 无效。
* **解决方案**：更改后继者的物理同步器 ID，使其满足： - 它大于当前的物理同步器 ID - 它大于所有先前的同步器公告
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_无效\_同步器

* **说明**：如果提交的事务仅限于另一个同步器，则会返回此错误。
* **解决方案**：使用正确的同步器标识符重新创建事务的内容。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_无效\_TX\_签名

* **解释**：此错误表明上传的签名交易包含无效签名。
* **解决方案**：确保交易有效并使用该参与者理解的加密版本。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 拓扑\_无效\_升级\_时间

* **解释**：此错误表明同步器升级公告指定了无效的升级时间。
* **解决方案**：在未来足够的升级时间内重新提交同步器公告。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_MANAGER\_ALARM

* **解释**：拓扑管理器从另一个节点接收到格式错误的消息。
* **解决方案**：检查错误消息以了解详细信息。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 拓扑\_管理器\_内部\_错误

* **解释**：此错误表明拓扑管理器中存在内部错误。
* **解决方案**：检查错误消息以了解详细信息。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 拓扑\_映射\_已存在\_

* **解释**：此错误表示拓扑事务将创建一个已存在且已使用相同密钥授权的状态。
* **解决方案**：您预期的更改已生效。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_中介\_已在\_OTHER\_组中

* **解释**：此错误表示拓扑事务尝试将中介器添加到多个中介器组。
* **解决方案**：首先从当前组中删除调解员，或者选择其他调解员进行添加。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_成员\_无法\_重新加入\_同步器* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_缺失\_映射

* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_多\_交易\_哈希\_不匹配

* **说明**：当签名未覆盖交易的预期交易哈希时，返回此错误。
* **解决方案**：仅为此特定交易的哈希添加签名，或者添加覆盖此交易的签名作为多交易哈希的一部分。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_命名空间\_已在\_使用

* **解释**：此错误表明该命名空间已被另一个实体使用。
* **解决方案**：更改提交的拓扑事务中使用的命名空间。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_命名空间\_已\_被\_撤销

* **解释**：此错误表明命名空间已被撤销。
* **解决方案**：使用不同的命名空间。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_不\_适当\_签名\_KEY\_IN\_STORE

* **解释**：如果拓扑管理器在其存储中没有找到用于授权特定拓扑事务的密钥，则会出现此错误。
* **解决方案**：检查您的拓扑事务和密钥存储，并检查您是否拥有适当的证书和密钥来发出所需的拓扑事务。如果您明确请求使用特定密钥进行签名，则会列出不可用的密钥。否则，如果列表为空，则表明您缺少证书。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_NO\_相应\_ACTIVE\_TX\_TO\_REVOKE

* **解释**：此错误表示添加删除事务的尝试被拒绝，因为影响删除的映射不存在。
* **解决方案**：检查拓扑状态并确保您尝试撤销的活动事务的映射与您的撤销参数匹配。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_没有\_正在进行\_同步器\_升级

* **解释**：此错误表示同步器升级未正在进行，这会阻止执行某些升级操作。
* **解决方案**：联系同步器的所有者了解正在进行的同步器升级。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_正在进行\_同步器\_升级

* **解释**：此错误表明同步器升级正在进行，并且仅允许与同步器升级相关的映射。
* **解决方案**：联系同步器的所有者了解正在进行的同步器升级。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_参与者\_ID\_冲突\_与\_派对* **解释**：此错误表示参与者未能加入，因为它与现有参与者具有相同的 UID。
* **解决方案**：通过更改命名空间或参与者的 UID 来更改参与者的身份，然后再次尝试加入同步器。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_参与者\_入职\_拒绝

* **解释**：此错误表示参与者无法加入同步器，因为存在加入限制。
* **解决方案**：验证同步器的加入限制。如果同步器未锁定，则首先需要通过发出 参与方同步器Permission 事务将参与者放入允许列表中。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_PARTY\_ID\_与\_ADMIN\_PARTY 冲突

* **解释**：此错误表明要分配的 partyId 与已存在的管理方相同。
* **解决方案**：使用更改后的 partyId 提交拓扑事务。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_删除\_不得\_更改\_映射

* **解释**：此错误表明删除拓扑映射与之前序列的映射相比也改变了内容。
* **解决方案**：使用与之前序列相同的拓扑映射提交交易，但使用 REMOVE 操作。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_秘密\_密钥\_不在\_存储中

* **解释**：此错误表明无法找到具有相应指纹的密钥。
* **解决方案**：确保您仅使用存储在密钥存储中的密钥指纹。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_串行\_不匹配

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_签名\_阈值\_无法\_达到\_

* **解释**：此错误表明签名阈值高于签名密钥的数量，这将导致一方无法正常工作。
* **解决方案**：降低阈值或增加签名密钥的数量。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 拓扑\_STORE\_NOT\_FOUND

* **解释**：此错误表示未找到预期的拓扑存储。
* **解决方案**：重试之前，请检查提供的拓扑存储名称是否正确。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_临时\_存储\_已存在\_

* **解释**：此错误表明已存在具有所需标识符的临时拓扑存储。
* **解决方案**：在重新提交请求之前首先使用现有的临时拓扑存储，或者按原样使用该存储。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。#### 拓扑\_太多\_许多\_待处理\_拓扑\_事务

* **解释**：此错误表明当前该节点有太多拓扑事务正在等待处理。
* **解决方案**：更改同步器发件箱的最大队列大小或重试。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 拓扑\_太多\_事务\_WITH\_HASH

* **解释**：此错误表示发现多个具有相同交易哈希的拓扑交易。
* **解决方案**：检查拓扑状态的一致性并在重试之前采取纠正措施。该错误的元数据详细信息包含字段`transactions`中的交易。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_事务\_未\_找到

* **解释**：此错误表示找不到拓扑事务。
* **解决方案**：拓扑事务已被拒绝、不再有效、尚未有效或尚不存在。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_未经授权\_交易

* **解释**：此错误表明添加交易的尝试被拒绝，因为签名密钥在当前状态下未获得授权。
* **解决方案**：检查拓扑状态并确保签名密钥的有效命名空间委托存在，或者在添加此交易之前上传一个。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 拓扑\_未知\_成员

* **解释**：此错误表明拓扑事务引用了当前未知的成员。
* **解决方案**：等待成员的加入变得活跃或从拓扑事务中删除未知成员。此错误的元数据详细信息包含字段 `members` 中的未知成员。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_VALUE\_OUT\_OF\_BOUNDS

* **解释**：当新参数值超出定义的下限和上限时，会出现此错误。
* **分辨率**：选择一个在允许的下限和上限内的值。或者，添加标志 `ForceFlag.AllowOutOfBoundsValue` 来强制更改值。注意：强制更改值可能会导致不良的系统行为。仅当您了解风险时才继续。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 7.1.1。同步器

#### 同步器\_节点\_初始化\_失败

* **解释**：此错误表示同步器节点的初始化由于参数无效而失败。
* **解决方案**：查阅错误详细信息。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 7.1.1.1。 GrpcSequencer身份验证服务

#### 客户端\_身份验证\_故障

* **解释**：此错误表示客户端由于可能指出错误或恶意行为的原因而未能通过定序器进行身份验证。该消息被记录在服务器上，以便支持操作员向难以连接的客户端提供解释。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。

#### 客户端\_身份验证\_被拒绝* **解释**：此错误表示客户端无法通过定序器进行身份验证。该消息被记录在服务器上，以便支持操作员向难以连接的客户端提供解释。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端以日志级别 INFO 记录。

### 7.1.2。参与者拓扑管理器错误

#### DAML\_PRIM\_NOT\_UTILITY\_PACKAGE

* **解释**：此错误表示正在审查名称为 <span class="title-ref">daml-prim</span> 或 <span class="title-ref">daml-std-lib</span> 的包，该包不是实用程序包。所有 <span class="title-ref">daml-prim</span> 和 <span class="title-ref">daml-std-lib</span> 包都应该是实用程序包。
* **解决方案**：联系 Dar 的供应商。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 外部\_派对\_已经存在\_

* **解释**：当为已存在的一方发出分配外部方的请求时，会发生此错误。
* **解决方案**：分配具有唯一密钥的新方。如果您尝试更改聚会的托管节点，请按照聚会复制过程进行操作。
* **类别**：InvalidGivenCurrentSystemStateResourceExists
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ALREADY\_EXISTS 在 API 上公开，包括详细的错误消息。

#### 已知\_PACKAGE\_版本

* **解释**：此错误表示某个软件包的升级检查失败，因为之前已审查过另一个具有相同名称和版本的软件包。
* **解决方案**：检查错误消息并联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 无效升级包

* **解释**：此错误表明要审查的软件包无效，因为它没有升级它声称要升级的已审查软件包。
* **解决方案**：联系 DAR 的供应商或确保审核状态更改不会导致同时审核的升级不兼容的软件包。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 拓扑\_无法\_VET\_由于\_缺少\_包

* **解释**：此错误表示由于本地不存在软件包，软件包审核命令失败。这可能是由于软件包不存在或其依赖项丢失。在审核包时，该包必须存在于参与者上，否则参与者将无法处理依赖于特定包的交易。
* **解决方案**：先将包上传到本地，然后再发出此类交易。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 拓扑\_依赖项\_未经审查

* **解释**：此错误表示由于未审查依赖项而导致审查请求失败。对于每个审查请求，都会分析所提供的软件包的依赖性。该系统不仅要求显式审查主包，还要求所有依赖项都经过显式审查。这是必要的，因为并非所有参与者都需要安装相同的软件包，因此并非每个参与者都可以隐式解决依赖关系。
* **解决方案**：首先检查依赖关系，然后重复您的尝试。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_DISABLE\_PARTY\_WITH\_ACTIVE\_CONTRACTS* **解释**：此错误表示危险的 PartyTo参与方 映射删除被拒绝。如果运行该命令并且存在该方是利益相关者的活动合约，则这些合约将永远不会被修剪，从而导致无法回收存储。
* **解决方案**：如果您确实知道自己在做什么，请设置 ForceFlag.PackageVettingReplication。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_签字方\_许可不足

* **解释**：此错误表示将参与者权限更改为观察者的请求被拒绝。如果运行该命令并且该方仍然是有效合同的签署方，则此转换将阻止其使用合同。
* **解决方案**：如果您确实知道自己在做什么，请设置 ForceFlag.AllowInsufficient参与方PermissionForSignatoryParty。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 拓扑\_签名\_分配\_参与者不足

* **解释**：此错误表示危险的 PartyTo参与方 映射被拒绝。如果运行该命令，将不再有足够的签名分配参与者（即重新分配具有分配确认权限的参与者）来完成正在进行的重新分配，这些重新分配将保持卡住状态。
* **解决方案**：如果您确实知道自己在做什么，请设置 ForceFlag.AllowInsufficientSignatoryAssigning参与方sForParty。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 8. 命令错误

#### 控制台\_命令\_内部\_错误

* **类别**：系统内部假设违反
* **传送**：这些错误在控制台上显示为错误。

#### 控制台\_命令\_超时\_OUT

* **类别**：系统内部假设违反
* **传送**：这些错误在控制台上显示为错误。

#### 节点未启动

* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：这些错误在控制台上显示为错误。

### 9.CryptoPrivateStoreError

#### 加密\_私人\_存储\_错误

* **解释**：此错误表明无法存储密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 10. 加密公共存储错误

#### 加密\_公共\_存储\_错误

* **解释**：此错误表明无法存储密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 11. 数据库存储错误

#### 数据库\_连接\_丢失

* **解释**：此错误表明与数据库的连接已丢失。
* **解决方案**：检查错误消息以了解详细信息。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

#### 数据库存储降级

* **解释**：此错误表明数据库存储组件降级。
* **解决方案**：此错误表示性能下降。当数据库任务被拒绝时会出现此错误，通常是由于任务队列太小。该任务将在延迟后重试。但是，如果此错误频繁发生，您可能需要考虑增加任务队列。 （配置参数：canton.\<path-to-my-node>.storage.config.queueSize）。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

### 12. 握手错误

#### 已弃用的协议版本* **解释**：如果参与者或同步器使用已弃用的协议版本，则会记录或返回此错误。已弃用的协议版本可能不再安全。
* **解决方案**：迁移到使用最新协议版本的新同步器。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 13. 调解器错误

#### 重复\_确认\_请求\_UUID

* **说明**：调解器跟踪最近处理的确认请求的 UUID，以检测重复提交。该请求与已在重复数据删除窗口内处理的先前请求具有相同的 UUID。该请求将被拒绝。预计账本不会被损坏。
* **解决方案**：使用新的 UUID 重新提交请求。请注意，如果先前的请求成功，重新提交可能会导致重复的效果。
* **类别**：UnredactedSecurityAlert
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 中介\_内部\_错误

* **解释**：由于违反内部不变量，请求处理失败。它表明调解器存在错误。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 中介\_INVALID\_MESSAGE

* **解释**：调解器收到无效消息（请求或响应）。该消息将被丢弃。因此，底层请求可能会被拒绝。预计账本不会被损坏。在中介器重新启动或故障转移后，会出现此错误。
* **解决方案**：解决错误原因。让提交者重试该命令。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 调解者\_参与者\_歧义

* **解释**：参与者对同一请求和视图提交了相互矛盾的裁决（拒绝和批准，反之亦然），从而产生了模棱两可的情况。这是一个严重的安全问题，表明参与者有恶意，或者参与者的软件存在严重错误。第二个判决被忽略。预计账本不会被损坏，但应该对这一事件进行调查。
* **解决方案**：调查参与者是否有不当行为。联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 中介\_已收到\_格式错误\_消息

* **解释**：调解器收到一条格式错误的消息。这可能是由于消息发送者的错误而发生的。该消息将被丢弃。因此，底层请求可能会被拒绝。预计账本不会被损坏。
* **解决方案**：联系支持人员。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 调解员\_说\_TX\_超时\_OUT

* **解释**：此拒绝表示交易已被中介者拒绝，因为它在确认响应超时内没有收到足够的确认。错误信息中的“unresponsiveParties”字段包含在确认响应超时内未能发送响应的各方的逗号分隔列表。该字段仅从协议版本 6 开始出现
* **解决方案**：检查所有涉及的参与者是否可用且未超载。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

### 14.加密密钥创建错误

#### 加密\_密钥\_创建\_错误* **解释**：此错误表示无法创建加密密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 15. 加密密钥生成错误

#### 加密\_密钥\_生成\_错误

* **解释**：此错误表示无法创建加密密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 16. 信封打开器错误

#### 事件\_反序列化\_错误

* **解释**：此错误表明定序器客户端无法解析消息。这表明该邮件是由虚假或恶意发件人创建的。该消息将被丢弃。
* **解决**：如果没有报告其他错误，Canton 已自动恢复。您仍应考虑开始调查，以了解发件人发送无效邮件的原因。
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 17. 签名检查错误

#### 签名不一致检查警报

* **解释**：调解组的签名验证通过，但某些个人签名检查失败。当有效签名的数量足以达到阈值时，即使某些签名由于不匹配或验证错误而被拒绝，也会发生这种情况。虽然这不会阻止进度，但它可能表明密钥使用不正确或恶意、配置问题或签名过程中的错误。受影响的签名被忽略，但系统继续运行。
* **解决方案**：联系支持人员
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 18. SequencerRateLimitError

#### 错误\_事件\_成本

* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

### 19.GrpcVaultServiceError

#### 无效\_KMS\_KEY\_ID

* **解释**：所选的 KMS 密钥 ID 无效
* **解决方案**：指定有效的密钥 ID 并重试。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 无\_加密\_私人\_密钥\_存储\_错误

* **说明**：节点未运行加密的私有存储
* **解决方案**：验证是否为此节点设置了加密存储和 KMS 配置。
* **类别**：内部不支持的操作
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它以 grpc-status UNIMPLMENTED 的形式暴露在 API 上，没有任何详细信息。

#### 注册\_KMS\_KEY\_内部\_错误

* **解释**：在 Canton 注册 KMS 密钥失败时发出内部错误
* **解决方案**：联系支持人员
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### WRAPPER\_KEY\_ALREADY\_IN\_USE\_ERROR

* **说明**：选择的用于轮换的包装密钥 ID 已在使用中
* **解决方案**：选择不同的密钥 ID 并重试。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### WRAPPER\_KEY\_DISABLED\_OR\_DELETED\_ERROR* **说明**：无法使用所选的用于轮换的包装器密钥 ID，因为密钥已禁用或设置为删除
* **解决方案**：指定活动密钥中的密钥 ID 并重试。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### WRAPPER\_KEY\_NOT\_EXIST\_ERROR

* **说明**：选择的用于轮换的包装密钥 ID 与任何现有 KMS 密钥都不匹配
* **解决方案**：指定与现有 KMS 密钥匹配的密钥 ID，然后重试。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### WRAPPER\_KEY\_ROTATION\_INTERNAL\_ERROR

* **解释**：内部包装器密钥轮换错误时发出内部错误
* **解决方案**：联系支持人员
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

### 20. 交通控制错误

#### 无效\_流量\_控制\_购买\_消息

* **解释**：成员收到无效的流量控制消息。这可能是由于消息发送者的错误而发生的。该消息将被丢弃。因此，购买的底层流量更新将不会生效。
* **解决方案**：联系支持人员
* **类别**：安全警报
* **传送**：此错误在服务器端以日志级别 WARN 记录。出于安全原因，它在 API 上公开，并带有 grpc-status INVALID\_ARGUMENT，没有任何详细信息。

#### 交通控制已禁用

* **解释**：同步器上的流量控制未激活。
* **解决方法**：通过设置流量控制动态同步器参数来启用流量控制。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 流量\_控制\_串行\_太\_低

* **说明**：提供的序列号低于或等于最新记录的余额更新。
* **解决方案**：重新提交充值请求，其序列号高于最新记录的余额更新。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 交通\_控制\_状态\_未发现\_

* **解释**：此错误表明参与者没有流量状态。
* **解决方案**：确保参与者连接到启用了流量控制的同步器，并且自连接以来至少已从同步器接收到一个事件。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

#### 流量\_控制\_顶部\_向上\_提交\_失败

* **解释**：发送排序充值提交请求时收到意外错误。
* **解决方案**：使用指数退避策略重新提交充值请求。
* **类别**：InvalidGivenCurrentSystemStateResourceMissing
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status NOT\_FOUND 公开在 API 上，包括详细的错误消息。

### 21. SequencerErrors

#### 过时的\_TRAFFIC\_COST

* **说明**：与排序时的同步器状态相比，提供的提交成本已过时。
* **解决方案**：重新提交请求并更新提交费用。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 序列器\_聚合\_提交\_已发送\_* **解释**：当排序器已经发出请求的聚合提交时，会发生此错误。
* **解决方案**：这预计会在启用聚合提交的系统运行期间发生。无需采取任何行动。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 定序器\_聚合\_提交\_填充

* **解释**：当排序器已经收到来自同一发件人的相同提交请求时，会发生此错误。
* **解决方案**：此错误表明排序器已接受聚合提交，并且由于某种原因存在重复提交。这可能是由于重试提交造成的。这通常可以被忽略。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 定序器\_INTERNAL

* **解释**：定序器上发生内部错误。
* **解决方案**：联系支持人员。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 定序器\_内部\_测试

* **解释**：定序器上发生内部错误。只能出现在测试中。
* **解决方案**：联系支持人员。
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 定序器\_MAX\_SEQUENCING\_TIME\_TOO\_FAR

* **解释**：提交请求的最大排序时间超出了未来允许的最大间隔。可能是sequencerAggregateSubmissionTimeout 的并发动态同步器参数更改的结果。
* **解决方案**：如果最近发生并发动态同步器参数更改，只需重试提交即可。否则，此错误代码表示 Canton 中存在错误（错误的节点行为）。请联系客户支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 序列器\_不够\_流量\_信用

* **解释**：由于发送者购买的流量条目中积分不足，Sequencer 拒绝了提交请求。
* **解决方案**：通过为发送方购买流量积分，为系统获取更多流量积分。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 音序器\_过载

* **解释**：定序器过载，无法处理请求。
* **解决方案**：使用指数退避重试。
* **类别**：共享资源争用
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status ABORTED 公开在 API 上，包括详细的错误消息。

#### 序列器\_SENDER\_UNKNOWN

* **解释**：排序器不知道提交请求的发送者或聚合规则中符合条件的发送者。
* **解决方案**：这表示拓扑更改的竞赛或 Canton 中的错误（错误的节点行为）。如果此问题仍然存在，请联系客户支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 序列器\_提交\_请求\_格式错误* **解释**：当排序器收到无效的提交请求时，会发生此错误，例如它有一个具有无法到达阈值的聚合规则。格式错误的请求不会发出任何传递事件。
* **解决方案**：检查发件人是否正在发起攻击。如果您可以排除攻击的可能性，请联系 Canton 支持人员。
* **类别**：UnredactedSecurityAlert
* **传送**：此错误在服务器端以日志级别 WARN 记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

#### 定序器\_提交\_请求\_拒绝

* **解释**：当排序器因系统当前状态而无法接受提交请求时，会发生此错误。
* **解决方案**：这通常表明系统组件配置错误或应用程序错误，需要操作员干预。请参阅具体的错误消息以了解具体原因。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 定序器\_TOMBSTONE\_PERSISTED

* **解释**：装载的定序器已将逻辑删除代替了拓扑时间戳早于定序器签名密钥的事件。
* **解决方案**：客户端应连接到具有较旧事件历史记录的另一个定序器，以在重新连接到最近加载的定序器之前使用逻辑删除事件。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 排序器\_拓扑\_时间戳\_之后\_排序\_时间戳

* **解释**：提交请求上的拓扑时间戳晚于排序时间。
* **解决方案**：这表明 Canton 存在错误（错误的节点行为）。请联系客户支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 定序器\_拓扑\_时间戳\_太早\_

* **说明**：提交请求上的拓扑时间戳早于动态同步器参数允许的时间。
* **解决方案**：这表明 Canton 存在错误（错误的节点行为）。请联系客户支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

#### 定序器\_不可用

* **说明**：音序器当前不可用。
* **解决方案**：快速重试。
* **类别**：瞬时服务器故障
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status UNAVAILABLE 公开在 API 上，包括详细的错误消息。

#### 序列器\_未实现

* **说明**：此定序器不支持请求的功能。
* **解决方案**：联系测序仪操作员。
* **类别**：内部不支持的操作
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它以 grpc-status UNIMPLMENTED 的形式暴露在 API 上，没有任何详细信息。

#### 定序器\_未知\_接收者

* **解释**：当提交请求指定排序器未知的节点时，会发生此错误。
* **解决方案**：这表明 Canton 存在错误（错误的节点行为）。请联系客户支持。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 22. 原型反序列化错误

#### 原型\_反序列化\_失败

* **解释**：此错误表示由于消息格式错误而无法处理传入的管理命令。
* **解决方案**：检查错误详细信息并更正您的应用程序
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。### 23.ResilientSequencer订阅

#### 检测到定序器\_FORK\_

* **解释**：当定序器客户端确定分类账分叉时，会记录此错误，其中定序器节点对同一时间戳/计数器响应不同的事件。每当客户端重新连接到同步器时，它都会从收到的最后一条消息开始，并比较最后一条消息是否与之前收到的消息匹配。如果没有，它将报告此错误。正常操作下不应发生账本分叉。如果备份的顺序错误，例如，可能会发生这种情况。参与者比测序者更先进。
* **解决方案**：您可以通过使用正确顺序的备份恢复系统来恢复。请查阅手册中的相应章节。
* **类别**：系统内部假设违反
* **传送**：此错误在服务器端以日志级别 ERROR 记录。出于安全原因，它通过 grpc-status INTERNAL 公开在 API 上，没有任何详细信息。

#### 定序器\_订阅\_丢失

* **说明**：当定序器订阅中断时会记录此警告。系统将无限期地不断重试重新连接。
* **解决方案**：监控情况，如果问题没有自动解决，请联系服务器操作员。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。

### 24.SendAsyncClientError

#### 序列器\_SEND\_ASYNC\_CLIENT\_ERROR

* **解释**：此错误表示无法通过定序器发送消息。
* **解决办法**：检查错误详细信息
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 25. SequencerSubscriptionError

#### 序列器\_墓碑\_遭遇

* **解释**：此错误表示最近加入的定序器的定序器订阅尝试读取被逻辑删除替换的事件。如果与事件关联的时间戳早于定序器签名密钥的有效性，则会出现逻辑删除。此错误会导致定序器客户端与定序器断开连接。
* **解决方案**：连接到具有较旧事件历史记录的另一个定序器，以在重新连接到最近加载的定序器之前使用逻辑删除事件。
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 26.SigningKeyCreationError

#### 签名\_KEY\_CREATION\_错误

* **解释**：此错误表示无法创建加密密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidGivenCurrentSystemStateOther
* **传送**：此错误在服务器端使用日志级别 INFO 记录，并通过 grpc-status FAILED\_PRECONDITION 公开在 API 上，包括详细的错误消息。

### 27. 签名密钥生成错误

#### 签名\_KEY\_GENERATION\_ERROR

* **解释**：此错误表明无法创建签名密钥。
* **解决办法**：检查错误详细信息
* **类别**：InvalidIndependentOfSystemState
* **传送**：此错误在服务器端使用日志级别 INFO 进行记录，并通过 grpc-status INVALID\_ARGUMENT 在 API 上公开，包括详细的错误消息。

### 28.时钟

#### 系统时钟向后运行

* **解释**：如果唯一时间生成检测到主机系统时钟落后唯一时间源超过一秒，则会发出此错误。如果系统每秒处理超过 2e6 个事件（不太可能）或者底层主机系统时钟向后运行，则可能会发生这种情况。例如，当网络时间协议（NTP）等时钟同步方法向后调整时钟时，主机系统时钟会向后运行。
* **解决方案**：检查您的主机系统。一般来说，独特的时间源不会受到时钟向后移动的负面影响，并将继续发挥作用。因此，此消息只是关于检测到异常情况的警告。
* **类别**：BackgroundProcessDegradationWarning
* **传送**：此错误在服务器端以日志级别 WARN 记录。类别 8 到 12（`InvalidIndependentOfSystemState`、`InvalidGivenCurrentSystemState*`）通常是应用程序级别的问题，而不是操作员级别的问题。如果您在操作员日志中持续看到它们，则它们可能表示配置问题。

## 同步器连接错误

当您的参与者无法与同步器通信时，就会出现这些错误。

## 定序器错误

此部分将在未来的更新中扩展。有关定序器相关的故障排除，请参阅[故障排除方法](/global-synchronizer/troubleshooting-guide/troubleshooting-methodology)。

## 中介错误

此部分将在未来的更新中扩展。有关调解器相关的故障排除，请参阅[故障排除方法](/global-synchronizer/troubleshooting-guide/troubleshooting-methodology)。

## ACS 承诺错误

活动合约集 (ACS) 承诺错误与参与者用来验证他们是否同意共享合约状态的完整性检查机制有关。

## 数据库和存储错误

**`DB_STORAGE_DEGRADATION(13,...):`** 数据库任务队列拒绝任务，通常是因为队列对于当前工作负载来说太小。任务将在延迟后重试。如果这种情况经常发生，请通过`canton.<path-to-node>.storage.config.queueSize`增加任务队列大小或提高数据库的I/O容量（IOPS、存储类型）。

**`DB_CONNECTION_LOST(13,...):`** 与数据库的连接丢失。检查您的 PostgreSQL 实例是否正在运行且可访问，并且连接限制尚未耗尽。

## 拓扑管理错误

这些错误在管理拓扑状态（参与方分配、包审查、密钥管理和同步器配置）时发生。

**`TOPOLOGY_UNAUTHORIZED_TRANSACTION(9,...):`** 拓扑交易未获授权。验证签名密钥是否具有所需的权限。

**`TOPOLOGY_INSUFFICIENT_KEYS(9,...):`** 缺少所需的密钥。确保节点已注册必要的签名和加密密钥。

**`TOPOLOGY_INVALID_MAPPING(9,...):`** 拓扑映射无效。检查您提交的拓扑事务的参数。

**`TOPOLOGY_MANAGER_ALARM(5,...):`** 来自拓扑管理器的安全警报。调查并联系支持人员。

## 特定于熔接的操作错误

这些错误特定于 Canton Network 上的 Splice 验证器和 SV 应用程序操作。

**流量余额低于预留量** -- 您的验证器应用程序无法购买流量。一旦余额低于预留阈值，验证器就会阻止交易（流量购买除外）。检查`TopupMember流量Trigger`日志以查找根本原因。如果您只想使用免费流量，请删除验证器充值配置。

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
    ABORTED: 流量 balance below reserved 流量 amount (0 < 200000)
```

**资金不足，无法购买配置的流量** -- 验证人尝试购买流量，但没有足够的广东币。测试网和主网上的新节点从零余额开始，并随着时间的推移通过验证者活跃度奖励累积 CC。您还可以从另一个节点接收 CC 传输。如果您只想要免费流量，请删除验证器充值配置。

**节点身份不匹配** -- 您在初始化后更改了参与者标识符。对于验证器，节点标识符默认为`验证者PartyHint`，因此更改它也会触发此错误。在新节点上，您可以通过删除数据库并重新启动来重置。在已建立的节点上，恢复到原始标识符。

**连接到定序器时会员被禁用** - 您的参与者的停机时间超过了 30 天定序器修剪窗口，并且 SV 已将其禁用。通过启动新节点并重新加入来恢复您的 CC 平衡。

## 错误升级

有关如何分类和升级错误的决策路径，请参阅故障排除方法中的[错误升级](/global-synchronizer/troubleshooting-guide/troubleshooting-methodology#error-escalation)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
