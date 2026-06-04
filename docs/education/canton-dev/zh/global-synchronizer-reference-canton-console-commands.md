---
title: "Canton Console 命令"
slug: "global-synchronizer-reference-canton-console-commands"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/canton-console-commands.md"
source_title: "Canton Console Commands"
tags:
  - global-synchronizer
  - reference
  - canton-console-commands
---

# Canton Console 命令

> Canton 管理控制台完整命令参考。

> Canton 管理控制台命令参考：参与者、调解者、排序者和拓扑命令。

<div id="canton_console_reference">
  <Note>
    按参与者和同步器拆分，将共享命令放在扩展/参与者部分，并添加同步器部分
  </Note>
</div>

# 控制台命令

## 顶级命令

为了方便起见，可以使用以下命令：

<div id="退出"/>

### `exit`

离开控制台。

<div id="帮助"/>

### `help`

帮助控制台命令；输入 help("\<command>") 以获取 \<command> 的详细帮助。

<div id="bootstrap.decentralized_namespace" />

### `bootstrap.decentralized_namespace`

为提供的所有者引导一个分散的命名空间。

返回去中心化命名空间、其定义的完全授权交易以及所有者的所有根证书。这允许其他节点导入并完全验证分散的命名空间定义。此调用成功完成后，所有所有者都已将共同所有者的身份拓扑交易以及完全授权的去中心化命名空间定义存储在指定的拓扑存储中。

**参数**

* `owners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

**返回：** `(com.digitalasset.canton.topology.Namespace, Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction])`

<div id="bootstrap.help" />

### `bootstrap.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="bootstrap.onboard_new_sequencer" />

### `bootstrap.onboard_new_sequencer`

载入新的 Sequencer 节点。

使用网络中的现有节点加载新的 Sequencer 节点。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `newSequencer`: `com.digitalasset.canton.console.SequencerReference`
* `existingSequencer`: `com.digitalasset.canton.console.SequencerReference`
* `同步器Owners`: `Set[com.digitalasset.canton.console.InstanceReference]`
* `customCommandTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `isBftSequencer`: `Boolean`

<div id="bootstrap.同步器" />

### `bootstrap.同步器`

引导一个新的同步器。

使用给定的静态同步器参数和成员引导新的同步器。作为同步器所有者的任何参与者随后仍必须手动连接到同步器。

参数： mediatorsToSequencers：介体引用到定序器引用序列元组的映射、定序器信任阈值和给定介体的活跃度裕度。

**参数**

* `同步器Name`: `String`
* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `mediatorsToSequencers`: `Map[com.digitalasset.canton.console.MediatorReference,(Seq[com.digitalasset.canton.console.SequencerReference], com.digitalasset.canton.config.RequireTypes.PositiveInt, com.digitalasset.canton.config.RequireTypes.NonNegativeInt)]`
* `同步器Owners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `同步器Threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `static同步器Parameters`: `com.digitalasset.canton.admin.api.client.data.Static同步器Parameters`
* `mediatorRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `mediatorThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `com.digitalasset.canton.拓扑.Physical同步器Id`

<div id="bootstrap.同步器_1" />

### `bootstrap.同步器_1`

引导一个新的同步器。

使用给定的静态同步器参数和成员引导新的同步器。作为同步器所有者的任何参与者随后仍必须手动连接到同步器。

**参数*** `同步器Name`: `String`
* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `mediators`: `Seq[com.digitalasset.canton.console.MediatorReference]`
* `同步器Owners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `同步器Threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `static同步器Parameters`: `com.digitalasset.canton.admin.api.client.data.Static同步器Parameters`
* `mediatorRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `mediatorThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `com.digitalasset.canton.拓扑.Physical同步器Id`

<div id="bootstrap.同步器_local" />

### `bootstrap.同步器_local`

使用默认参数引导本地同步器。

这是引导本地同步器的便捷方法。同步器将包括当前正在运行的所有定序器和中介器。它将由定序器拥有，而中介器阈值将设置为要求所有中介器确认。

**参数**

* `同步器Name`: `String`

**退货：** `com.digitalasset.canton.拓扑.同步器Id`

<div id="console.command_timeout" />

### `console.command_timeout`

产生运行控制台命令的超时。

产生运行控制台命令的超时。当超时结束后，控制台停止等待命令结果。该命令将继续在后台运行。

**返回：** `com.digitalasset.canton.config.NonNegativeDuration`

<div id="console.help" />

### `console.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="console.set_command_timeout" />

### `console.set_command_timeout`

设置运行控制台命令的超时。

设置运行控制台命令的超时。当超时结束后，控制台停止等待命令结果。该命令将继续在后台运行。新的超时必须是正值。

**参数**

* `newTimeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="调解员" />

### `mediators`

所有中介节点（.all、.local、.remote）。

<div id="节点"/>

### `nodes`

所有节点（.all、.local、.remote）。

<div id="参与者"/>

### `参与方s`

所有参与者节点（.all、.local、.remote）。

<div id="定序器" />

### `sequencers`

所有定序器节点（.all、.local、.remote）。

<div id="ledger_api_utils.create" />

### `ledger_api_utils.create`

构建创建命令。

**参数**

* `packageId`: `String`
* `module`: `String`
* `template`: `String`
* `arguments`: `Map[String,Any]`

**返回：** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.exercise" />

### `ledger_api_utils.exercise`

从 CreatedEvent 构建练习命令。

**参数**

* `choice`: `String`
* `arguments`: `Map[String,Any]`
* `event`: `com.daml.ledger.api.v2.event.CreatedEvent`

**退货：** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.exercise_1" />

### `ledger_api_utils.exercise_1`

建立演习指挥。

**参数**

* `packageId`: `String`
* `module`: `String`
* `template`: `String`
* `choice`: `String`
* `arguments`: `Map[String,Any]`
* `contractId`: `String`

**返回：** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.help" />

### `ledger_api_utils.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="logging.get_level"/>

### `logging.get_level`

确定当前日志记录级别。

**参数**

* `loggerName`: `String`

**返回：** `Option[ch.qos.logback.classic.Level]`

<div id="logging.help"/>

### `logging.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="logging.last_error_trace" />

### `logging.last_error_trace`

返回具有相同跟踪 ID 的错误的日志事件。

**参数**

* `traceId`: `String`

**退货：** `Seq[String]`

<div id="logging.last_errors" />

### `logging.last_errors`

返回本地记录的最后一个错误（trace-id -> 错误事件）。

**退货：** `Map[String,String]`

<div id="logging.set_level" />

### `logging.set_level`

动态更改日志级别（TRACE、DEBUG、INFO、WARN、ERROR、OFF、null）。

**参数*** `loggerName`: `String`
* `level`: `String`

<div id="mediator1" />

### `mediator1`

管理本地中介“mediator1”；输入“mediator1 help”或“mediator1 help("\<methodName>")”以获得更多帮助。

<div id="参与方1" />

### `参与方1`

管理参与者“参与方1”；输入“参与方1 help”或“参与方1 help("\<methodName>")”以获得更多帮助。

<div id="参与方2"/>

### `参与方2`

管理参与者“参与方2”；输入“参与方2 help”或“参与方2 help("\<methodName>")”以获得更多帮助。

<div id="参与方3" />

### `参与方3`

管理参与者“参与方3”；输入“参与方3 help”或“参与方3 help("\<methodName>")”以获得更多帮助。

<div id="sequencer1" />

### `sequencer1`

管理本地定序器“sequencer1”；输入“sequencer1 help”或“sequencer1 help("\<methodName>")”以获得更多帮助。

<div id="utils.auto_close" />

### `utils.auto_close`

如果Canton 关闭，则注册要关闭的`AutoCloseable` 对象。

**参数**

* `closeable`: `AutoCloseable`

<div id="utils.cantonprocesslogger" />

### `utils.cantonprocesslogger`

将进程日志转发到Canton日志的进程记录器。

**参数**

* `tracedLogger`: `com.digitalasset.canton.logging.TracedLogger`

**返回：** `scala.sys.process.ProcessLogger`

<div id="utils.generate_daml_script_参与方s_conf" />

### `utils.generate_daml_script_参与方s_conf`

为 Daml 脚本创建参与者配置。

生成的配置可以通过`参与方-config`参数传递给`daml script`。有关文件格式的更多信息可以在文档中找到：它需要三个参数：

* 文件（默认为“参与方-config.json”）
* use参与方Alias（默认为true）：使用参与者别名而不是UID
* default参与方（默认为 None）：添加默认参与者（如果提供）

**参数**

* `file`: `Option[String]`
* `use参与方Alias`: `Boolean`
* `default参与方`: `Option[com.digitalasset.canton.console.参与方Reference]`

**返回：** `java.io.File`

<div id="utils.help" />

### `utils.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="utils.object_args" />

### `utils.object_args`

对象参数的反射检查，方便检查案例类对象。

返回给定对象的列表字段名称。检查返回结果时有用的功能。

**参数**

* `obj`: `T`

**返回：** `List[String]`

<div id="utils.read_all_messages_from_file" />

### `utils.read_all_messages_from_file`

从文件中读取多条 Protobuf 消息。

如果无法读取或解析文件，则会失败并出现异常。

**参数**

* `fileName`: `String`

**返回：** `Seq[A]`

<div id="utils.read_byte_string_from_file" />

### `utils.read_byte_string_from_file`

从文件中读取 ByteString。

如果无法读取文件，则失败并出现异常。

**参数**

* `fileName`: `String`

**返回：** `com.google.protobuf.ByteString`

<div id="utils.read_first_message_from_file" />

### `utils.read_first_message_from_file`

从文件中读取一条 Protobuf 消息。

如果无法读取或解析文件，则会失败并出现异常。

**参数**

* `fileName`: `String`

**退货：** `A`

<div id="utils.retry_until_true" />

### `utils.retry_until_true`

等待条件成立。

等待`timeout`持续时间，直到`condition`变为真。重试评估 `condition`，并以指数方式增加后退，直至重试之间的持续时间为 `maxWaitPeriod`。

**参数**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `maxWaitPeriod`: `com.digitalasset.canton.config.NonNegativeDuration`
* `condition`: `=> Boolean`
* `failure`: `=> String`

**退货：** `(condition: => Boolean, failure: => String): Unit`

<div id="utils.retry_until_true_1" />

### `utils.retry_until_true_1`

使用默认超时等待条件变为真。

等待条件变为真，超时时间取自parameters.timeouts.console.bounded 配置参数。

**参数**

* `condition`: `=> Boolean`

<div id="utils.synchronize_拓扑" />

### `utils.synchronize_拓扑`

等待所有拓扑更改在所有可访问节点上生效。

**参数**

* `timeoutO`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="utils.type_args" />

### `utils.type_args`类型参数的反射检查，方便检查案例类类型。

返回给定类型的字段名称列表。为请求创建新对象时的有用功能。

**返回：** `List[String]`

<div id="utils.write_to_file" />

### `utils.write_to_file`

将 ByteString 写入文件。

**参数**

* `data`: `com.google.protobuf.ByteString`
* `fileName`: `String`

<div id="utils.write_to_file_1" />

### `utils.write_to_file_1`

将 Protobuf 消息写入文件。

**参数**

* `data`: `scalapb.GeneratedMessage`
* `fileName`: `String`

<div id="utils.write_to_file_2" />

### `utils.write_to_file_2`

将多条 Protobuf 消息写入文件。

**参数**

* `data`: `Seq[scalapb.GeneratedMessage]`
* `fileName`: `String`

## 参与者命令

<div id="clear_cache"/>

### `clear_cache`

清除本地缓存的变量。

有些命令在客户端缓存值。使用此命令显式清除这些值的缓存。

<div id="配置"/>

### `config`

返回参与者配置。

**返回：** `com.digitalasset.canton.参与方.config.参与方NodeConfig`

<div id="help_1" />

### `help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="id"/>

### `id`

产生该参与者的全局唯一 ID。如果 id 尚未分配（例如，参与者尚未启动），则抛出异常。

**返回：** `com.digitalasset.canton.拓扑.参与方Id`

<div id="is_initialized" />

### `is_initialized`

检查本地实例是否正在运行并且已完全初始化。

**退货：** `Boolean`

<div id="is_running" />

### `is_running`

检查本地实例是否正在运行。

**返回：** `Boolean`

<div id="maybeid"/>

### `maybeid`

如果 id 存在，则生成该参与者的 Some(id)。如果 id 尚未分配（例如，参与者尚未初始化），则返回 None。

**退货：** `Option[com.digitalasset.canton.拓扑.参与方Id]`

<div id="simclock"/>

### `simclock`

返回节点特定的 simClock，如果也使用environment.SimClock，则可能存在竞争条件。

**返回：** `Option[com.digitalasset.canton.time.DelegatingSimClock]`

<div id="开始"/>

### `start`

启动实例。

<div id="停止"/>

### `stop`

停止实例。

### 双边承诺

<div id="commitments.add_config_distinguished_slow_counter_参与方s" />

### `commitments.add_config_distinguished_slow_counter_参与方s`

将额外的杰出计数器参与者添加到现有的慢速计数器参与者配置中。

可以通过向现有同步器添加额外的计数器参与者来扩展配置。如果给定的同步器尚未配置，那么它将被忽略而不会出现错误。

**参数**

* `counter参与方sDistinguished`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

<div id="commitments.add_参与方_to_individual_metrics" />

### `commitments.add_参与方_to_individual_metrics`

将其他单独的指标参与者添加到现有的慢速计数器参与者配置中。

可以通过向现有同步器添加额外的计数器参与者来扩展配置。如果给定的同步器尚未配置，那么它将被忽略而不会出现错误。

**参数**

* `individualMetrics`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

<div id="commitments.compulated" />

### `commitments.computed`

查找 ACS 承诺，作为协调协议的一部分在本地计算。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `start`: `java.time.Instant`
* `end`: `java.time.Instant`
* `counter参与方`: `Option[com.digitalasset.canton.拓扑.参与方Id]`

**返回：** `Iterable[(com.digitalasset.canton.protocol.messages.CommitmentPeriod, com.digitalasset.canton.拓扑.参与方Id, com.digitalasset.canton.protocol.messages.AcsCommitment.HashedCommitmentType)]`

<div id="commitments.get_config_for_slow_counter_参与方s" />

### `commitments.get_config_for_slow_counter_参与方s`

列出给定同步器的慢速对方参与者（即发送承诺落后的参与者）的指标配置。列出每个同步器的以下配置。如果 `同步器s` 为空，该命令列出所有同步器的配置：

* 区分组中的参与者，有两个指标：参与者落后的最大间隔数，以及落后至少`thresholdDistinguished`协调间隔的参与者数
* 不在区分组中的参与者，有两个指标：参与者落后的最大间隔数，以及落后至少`thresholdDefault`协调间隔的参与者数
* 参数`thresholdDistinguished`和`thresholdDefault`
* `individualMetrics` 中的参与者，每个参与者都有单独的指标，显示该参与者落后了多少个调节间隔

**参数**

* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.SlowCounter参与方同步器Config]`

<div id="commitments.get_intervals_behind_for_counter_参与方s" />

### `commitments.get_intervals_behind_for_counter_参与方s`

列出每个参与者和同步器在发送承诺方面落后的间隔数（如果该参与者至少落后阈值间隔）。

如果 `counter参与方s` 为空，则该命令会考虑所有对应参与者。如果 `同步器s` 为空，则该命令考虑所有同步器。如果未设置`threshold`，则该命令认为 0。对于从未发送过承诺的对方参与者，输出显示他们落后于 MaxInt

**参数**

* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`
* `threshold`: `Option[com.digitalasset.canton.config.RequireTypes.NonNegativeInt]`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.Counter参与方Info]`

<div id="commitments.get_wait_commitments_config_from" />

### `commitments.get_wait_commitments_config_from`

检索等待对方参与者承诺的最新配置（即，w\.r.t. 查询执行时间）配置。

等待来自对方参与者的承诺的配置作为两组返回：一组被忽略的对方参与者、同步器和时间戳，以及一组未被忽略的对方参与者和同步器。按指定的对方参与者和同步者进行过滤。如果对方参与者和/或同步器为空，则它会考虑参与者已知的所有同步器和参与者，无论它们是否与参与者共享合约。即使某些参与者在查询执行时可能未连接到某些同步器，如果参与者知道这些同步器或在参数中指定了它们，则响应仍然包含它们。

**参数**

* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`
* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`

**退货：** `(Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.修剪.NoWaitCommitments], Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.修剪.WaitCommitments])`

<div id="commitments.help" />

### `commitments.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="commitments.inspect_commitment_contracts" />

### `commitments.inspect_commitment_contracts`

下载承诺检查和对账所需的合同状态和合同有效负载。

返回参与者从每个同步器上的时间开始到当前时间已知的所有同步器上给定合约的合约状态（已创建、已分配、未分配、已存档、未知）。该命令尽力返回可用的合同更改。具体而言，如果在该时间间隔期间已经修剪了 ACS 和/或重新分配状态，或者如果该时间间隔的部分内容领先于干净的 ACS 状态，则该过程不会失败。如果请求且可用，则可以选择返回合同有效负载。论据是：* `contracts`：我们要获取其状态和负载的合约ID
* `timestamp`：一些相对参与者报告给定合约在预期同步器上处于活动状态时的时间戳。
* `expected同步器Id`：合约预计活跃的同步器
* `downloadPayload`：如果为真，合约的有效负载也会被下载
* `timeout`：grpc调用完成的时间限制

**参数**

* `contracts`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `expected同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `downloadPayload`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `Seq[com.digitalasset.canton.参与方.修剪.CommitmentInspectContract]`

<div id="commitments.lookup_received_acs_commitments" />

### `commitments.lookup_received_acs_commitments`

列出参与者的对应参与者以及从他们那里收到的 ACS 承诺以及承诺状态。

通过参数进行可选过滤：同步器TimeRanges：列出给定同步器上收到的承诺，其周期与每个同步器的任何给定时间范围重叠。如果列表为空，则考虑参与者连接到的所有同步器。对于时间范围为空的同步器，考虑参与者知道的该同步器的最新周期。同步器可以在不同时间范围的列表中多次出现，在这种情况下，我们考虑时间范围的并集。 counter参与方s：列出仅从给定的对应参与者处收到的承诺。如果对方参与者不是某个同步器上的对方参与者，则该同步器上的对方参与者的回复中不会出现任何承诺。 CommitmentState：列出位于给定状态之一的承诺。默认情况下考虑所有状态：

* `MATCH`：远程承诺与本地承诺匹配
* `MISMATCH`: 远程承诺与本地承诺不匹配
* `BUFFERED`: 远程承诺被缓冲，因为相应的本地承诺尚未计算
* `OUTSTANDING`：我们期望尚未收到的远程承诺 verboseMode：如果为 false，则回复不包含承诺字节。如果为 true，则回复包含：
* 如果不匹配，回复将包含收到的和本地计算的不匹配的承诺。
* 若未解决，回复中不包含任何承诺。
* 在所有其他情况下（匹配和缓冲），回复包含收到的承诺。

**参数**

* `同步器TimeRanges`: `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.同步器TimeRange]`
* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `commitmentState`: `Seq[com.digitalasset.canton.参与方.修剪.AcsCommitmentProcessor.ReceivedCmtState]`
* `verboseMode`: `Boolean`

**退货：** `Map[com.digitalasset.canton.拓扑.同步器Id,Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.ReceivedAcsCmt]]`

<div id="commitments.lookup_sent_acs_commitments" />

### `commitments.lookup_sent_acs_commitments`

列出参与者的对应参与者以及参与者计算并发送给他们的 ACS 承诺。具体来说，该命令返回从同步器 ID 到已发送承诺数据元组的映射，根据详细模式指定周期、目标对方参与者、承诺状态和附加数据。通过参数进行可选过滤：同步器TimeRanges：列出给定同步器上收到的承诺，其周期与每个同步器的任何给定时间范围重叠。如果列表为空，则考虑参与者连接到的所有同步器。对于时间范围为空的同步器，考虑参与者知道的该同步器的最新周期。同步器可以在不同时间范围的列表中多次出现，在这种情况下，我们考虑时间范围的并集。 counter参与方s：列出仅发送给给定对方参与者的承诺。如果对方参与者不是某个同步器上的对方参与者，则该同步器上该对方参与者的回复中不会出现任何承诺。 CommitmentState：列出处于给定状态之一的已发送承诺。默认情况下考虑所有状态：

* `MATCH`：本地承诺与远程承诺匹配
* `MISMATCH`: 本地承诺与远程承诺不匹配
* `NOT_COMPARED`：本地承诺已计算并发送，但尚未收到相应的远程承诺，这本质上表明对方正在运行 verboseMode：如果为 true，则回复包含承诺字节，如下所示：
* 如果不匹配，回复将包含收到的和本地计算的不匹配的承诺。
* 在所有其他情况下（MATCH 和 NOT\_COMPARED），回复包含发送的承诺字节。

**参数**

* `同步器TimeRanges`: `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.同步器TimeRange]`
* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `commitmentState`: `Seq[com.digitalasset.canton.参与方.修剪.AcsCommitmentProcessor.SentCmtState]`
* `verboseMode`: `Boolean`

**返回：** `Map[com.digitalasset.canton.拓扑.同步器Id,Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.SentAcsCmt]]`

<div id="commitments.open_commitment" />

### `commitments.open_commitment`

通过检索与对方参与者共享的活动合约的元数据来打开承诺。

在给定时间戳和给定同步器上检索共享活动合约的合约 ID 和重新分配计数器。如果参与者无法再检索给定承诺的数据，则返回错误。论据是：

* `commitment`：待开启的承诺
* `physical同步器Id`：计算承诺的同步器
* `timestamp`：承诺的时间戳。需要对应于承诺勾选。
* `counter参与方`：我们之前发送承诺的柜台参与者
* `outputFile`：写入结果的可选文件
* `timeout`：grpc调用完成的时间限制

**参数**

* `commitment`: `com.digitalasset.canton.protocol.messages.AcsCommitment.HashedCommitmentType`
* `physical同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `counter参与方`: `com.digitalasset.canton.拓扑.参与方Id`
* `outputFile`: `Option[String]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `Seq[com.digitalasset.canton.参与方.修剪.CommitmentContractMetadata]`

<div id="commitments.received" />

### `commitments.received`

作为协调协议的一部分，查找从其他参与者收到的 ACS 承诺。

论据是：

* `同步器Alias`：同步器的别名
* `start`：最低时间独占
* `end`: 含最高时间
* `counter参与方`：可选择按计数器参与者过滤

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `start`: `java.time.Instant`
* `end`: `java.time.Instant`
* `counter参与方`: `Option[com.digitalasset.canton.拓扑.参与方Id]`

**退货：** `Iterable[com.digitalasset.canton.protocol.messages.SignedProtocolMessage[com.digitalasset.canton.protocol.messages.AcsCommitment]]`

<div id="commitments.reinitialize_commitments" />

### `commitments.reinitialize_commitments`

重新初始化当前 ACS 的承诺。同步者、相对参与者和利益相关者群体可以进行过滤。如果参与者的承诺因错误而损坏，则该命令非常有用。该命令重新初始化给定同步器和对方参与者的承诺，并包含与利益相关者（包括给定各方）的合同。如果 `同步器s` 为空，则该命令考虑所有同步器。如果 `counter参与方s` 为空，则该命令会考虑所有对应参与者。如果 `partyIds` 为空，则该命令会考虑所有利益相关者组。 `timeout` 指定命令等待重新初始化完成的时间。小于一秒的粒度将被忽略。过了这个超时，操作员可以使用`commitment_reinitialization_status`查询重新初始化的状态。该命令返回同步器 ID 的序列对以及每个同步器的重新初始化状态：重新初始化的 ACS 时间戳，或者如果重新初始化失败则返回错误消息。

**参数**

* `同步器Ids`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`
* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `partyIds`: `Seq[com.digitalasset.canton.拓扑.PartyId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.ReinitCommitments.CommitmentReinitializationInfo]`

<div id="commitments.remove_config_distinguished_slow_counter_参与方s" />

### `commitments.remove_config_distinguished_slow_counter_参与方s`

从同步器和杰出计数器参与者中删除现有配置。

可以从区分的计数器参与者中删除配置，并且同步器使用与选择所有相关的空序列，因此可以使用“counter参与方sDistinguished”的 Seq.empty 和同步器的 Seq(同步器Id) 来从同步器中删除所有区分的参与者。将两个序列留空会清除所有同步器上的所有配置。

**参数**

* `counter参与方sDistinguished`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

<div id="commitments.remove_参与方_from_individual_metrics" />

### `commitments.remove_参与方_from_individual_metrics`

从同步器和各个指标参与者中删除现有配置。

可以从单个指标计数器参与者中删除配置，同步器使用与选择所有相关的空序列，因此可以使用“individualMetrics”的 Seq.empty 和同步器的 Seq(同步器Id) 来从同步器中删除所有单个指标参与者。将两个序列留空会清除所有同步器上的所有配置。

**参数**

* `individualMetrics`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器s`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

<div id="commitments.set_config_for_slow_counter_参与方s" />

### `commitments.set_config_for_slow_counter_参与方s`

为缓慢的对方参与者（即，发送承诺方面落后的参与者）配置指标，并配置对方参与者被视为缓慢的阈值。

这些配置针对每个同步器或一组同步器，并涉及每个同步器发出的以下指标：

* 杰出参与者落后的最大间隔数。所有不在杰出组或个人组中的参与者都会自动成为默认组的一部分
* 默认组中参与者落后的最大间隔数
* 杰出组中落后至少 `thresholdDistinguished` 协调间隔的参与者数量。
* 落后至少 `thresholdDefault` 协调间隔的不属于杰出组或个别组的参与者数量。
* `individualMetrics` 参数中每个参与者的单独指标，跟踪参与者落后了多少个间隔

**参数**

* `configs`: `Seq[com.digitalasset.canton.admin.api.client.commands.参与方AdminCommands.Inspection.SlowCounter参与方同步器Config]`

<div id="commitments.set_no_wait_commitments_from" />

### `commitments.set_no_wait_commitments_from`

禁用等待给定对方参与者的承诺。禁用等待承诺会忽略这些相对参与者。修剪，它放弃了那些相对参与者的不可否认性，但增加了对那些相对参与者和/或网络的故障和减速的修剪弹性。如果参与者集为空，则该命令不执行任何操作。

**参数**

* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器Ids`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

<div id="commitments.set_wait_commitments_from" />

### `commitments.set_wait_commitments_from`

允许等待给定对方参与者的承诺。等待所有对方参与者的承诺是默认行为；仅当先前禁用等待承诺时才需要显式启用等待承诺。

启用等待承诺，这会阻止在缺少这些对方参与者的承诺的偏移处进行修剪。如果参与者集为空或同步器集为空，则该命令不执行任何操作。

**参数**

* `counter参与方s`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `同步器Ids`: `Seq[com.digitalasset.canton.拓扑.同步器Id]`

### DAR 管理

<div id="dars.download" />

### `dars.download`

将具有提供的主包 ID 的 DAR 文件下载到给定目录。

**参数**

* `mainPackageId`: `String`
* `directory`: `String`

<div id="dars.get_contents" />

### `dars.get_contents`

列出 DAR 文件的内容。

**参数**

* `mainPackageId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.DarContents`

<div id="dars.help" />

### `dars.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="dars.list" />

### `dars.list`

列出已安装的 DAR 文件。

列出此参与者上安装的 DAR 参数为： filterName：按名称过滤 filterDescription：按描述过滤 limit：限制结果数量（默认无）

**参数**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `filterName`: `String`
* `filterDescription`: `String`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.DarDescription]`

<div id="dars.remove" />

### `dars.remove`

从参与者中删除 DAR。

如果满足以下条件，可用于从参与者中删除 DAR： 1. DAR 的主包必须未使用 - 该包中不应有有效合约

2. DAR 的所有包依赖项都应该未使用或包含在另一个参与节点上传的 DAR 中。 Canton 使用此限制来确保 DAR 的包依赖项在使用时不会“搁浅”。

3. dar的主包不应该被审查。如果通过审查，Canton将尝试自动撤销对DAR主包的审查，但只有当主包审查源自标准`dars.upload`时，这种自动审查撤销才会成功。即使自动撤销失败，您也可以随时手动撤销包审核。

如果synchronizeVetting为true（默认），则该命令将阻塞，直到参与者观察到要向同步器注册的审查事务为止。

**参数**

* `mainPackageId`: `String`
* `synchronizeVetting`: `Boolean`

<div id="dars.upload" />

### `dars.upload`

上传 DAR 至 Canton。

Daml 代码通常作为 Dar 存档提供，并且必须明确上传给参与者。 Dar 是 LF 包的集合，是 Daml 智能合约的本机二进制表示。

Dar 可以作为本地文件的链接或 URL 的形式提供。如果提供了 URL，则任何请求标头都可以作为映射提供。 Dar 将被下载，然后上传给参与者。

为了在参与者上使用 Daml 模板，必须首先上传 Dar，然后由参与者审核。审查将确保其他参与者可以检查他们是否可以实际发送涉及特定 Daml 包和参与者的交易。必须通过注册 VettedPackages 拓扑事务在每个同步器上审查包。如果未设置同步器Id（默认），并且参与者仅连接到一个同步器，则将对包进行审查。如果synchronizeVetting为true（默认），则该命令将阻塞，直到参与者观察到要向同步器注册的审查事务为止。

该命令等待审核交易在同步器上成功注册。这是最小化竞争条件的安全默认设置。

请注意，同步审核可能会阻止仅允许参与者更新拓扑状态的许可同步器。在这种情况下，应关闭synchronizeVetting。可以使用 \$参与方.package.synchronize\_vettings() 手动调用同步审核

**参数**

* `path`: `String`
* `description`: `String`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `expectedMainPackageId`: `String`
* `requestHeaders`: `Map[String,String]`

**Returns:** `String`

<div id="dars.upload_many" />

### `dars.upload_many`

将许多 DAR 上传到 Canton。

Daml 代码通常作为 Dar 存档提供，并且必须明确上传给参与者。 Dar 是 LF 包的集合，是 Daml 智能合约的本机二进制表示。

Dars 可以作为本地文件的链接或 URL 的形式提供。如果提供了 URL，则任何请求标头都可以作为映射提供。 Dars 将被下载然后上传给参与者。

In order to use Daml templates on a 参与方, the Dars must first be uploaded and then vetted by the 参与方.审查将确保其他参与者可以检查他们是否可以实际发送涉及特定 Daml 包和参与者的交易。必须通过注册 VettedPackages 拓扑事务在每个同步器上审查包。

如果未设置同步器Id（默认），并且参与者仅连接到一个同步器，则将对包进行审查。如果synchronizeVetting为true（默认），则该命令将阻塞，直到参与者观察到要向同步器注册的审查事务为止。

This command waits for the vetting transaction to be successfully registered on the 同步器. This is the safe default setting minimizing race conditions.

请注意，同步审核可能会阻止仅允许参与者更新拓扑状态的许可同步器。在这种情况下，应关闭synchronizeVetting。 Synchronize vetting can be invoked manually using \$参与方.package.synchronize\_vettings()

**参数**

* `paths`: `Seq[String]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `requestHeaders`: `Map[String,String]`

**返回：** `Seq[String]`

<div id="dars.validate" />

### `dars.validate`

Validate DARs against the current 参与方s' state.

执行与上传调用执行的相同的 DAR 和 Daml 包验证检查，但对目标参与者没有影响：DAR 未保留或审查。

**参数**

* `path`: `String`

**Returns:** `String`

<div id="dars.vetting.disable" />

### `dars.vetting.disable`

撤销对由提供的主包 ID 标识的 DAR 存档中包含的所有包的审查。

如果用于审查 DAR 包的审查命令是对称的，并且导致 DAR 中所有包的单个审查拓扑事务，则此命令会成功。该命令存在潜在危险，误用可能导致参与者处理交易失败

**参数**

* `mainPackageId`: `String`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

<div id="dars.vetting.enable" />

### `dars.vetting.enable`

Vet all packages contained in the DAR archive identified by the provided main package-id.

**参数**

* `mainPackageId`: `String`
* `synchronize`: `Boolean`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

<div id="dars.vetting.help" />

### `dars.vetting.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

### Database

<div id="db.help" />

### `db.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`<div id="db.migrate" />

### `db.migrate`

如果使用数据库存储，则迁移实例的数据库。

当实例驻留在不同节点上时，它们的数据库迁移可以并行运行以节省时间。请注意，迁移命令必须在每个节点上单独运行，因为不支持通过`参与方s.remote...`进行远程迁移。

<div id="db.repair_migration" />

### `db.repair_migration`

仅在建议时使用 - 修复实例数据库的数据库迁移。

在极少数情况下，我们会在新版本中更改已应用的数据库迁移文件，并且修复命令会重置我们用来确保已应用的迁移文件通常没有更改的校验和。您应该只在建议时使用 `db.repair_migration`，否则使用它需要您自担风险 - 在最坏的情况下，当随后错误地应用不兼容的数据库迁移（应拒绝的数据库迁移，因为已应用的数据库迁移文件已更改）时，运行它可能会导致数据损坏。

**参数**

* `force`: `Boolean`

### 同步器连接

<div id="同步器s.active" />

### `同步器s.active`

测试参与者是否已连接到同步器并获得同步器的许可。

如果同步器未连接或不健康，则返回 false。如果同步器是在 Canton 配置中配置的，并且从同步器的角度来看参与者不是活动的，则返回 false。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**返回：** `Boolean`

<div id="同步器s.config" />

### `同步器s.config`

返回给定同步器的当前配置。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**返回：** `Option[com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig]`

<div id="同步器s.connect" />

### `同步器s.connect`

用于将参与者连接到由连接给出的同步器的宏。

连接宏执行一系列命令，以便将该参与者连接到同步器。首先，`register`将使用给定的参数调用，但首先使用manualConnect = true进行注册。如果您已经设置了manualConnect = true，则不会发生任何其他事情，您必须自己执行其余步骤。最后，该命令将调用`reconnect`来启动连接。如果重新连接成功，注册的配置将更新为manualStart = true。如果出现任何故障，同步器将保持在 `manualConnect = true` 的注册状态，并且您必须手动执行这些步骤。论据是：

* `同步器Alias`：您将用来指代此同步器的名称。无法再改变了。
* `connection`：连接到此同步器的连接字符串。 IE。 [https://url:port](https://url:port) manualConnect - 是否应手动处理此连接并排除自动重新连接。
* `physical同步器Id`：可选的是您希望在此同步器上看到的物理 ID。
* `certificatesPath`：用作信任锚的 TLS 证书文件的路径。
* `priority`：同步器的优先级。越高，使用同步器的可能性就越大。
* `timeTrackerConfig`：同步器时间跟踪器的配置。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `connection`: `String`
* `manualConnect`: `Boolean`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `certificatesPath`: `String`
* `priority`: `Int`
* `timeTrackerConfig`: `com.digitalasset.canton.config.同步器TimeTrackerConfig`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `sequencerAlias`: `com.digitalasset.canton.SequencerAlias`

**Returns:** `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`

<div id="同步器s.connect_1" />

### `同步器s.connect_1`

用于将参与者连接到实例指定的同步器的宏。这种连接变体需要一个具有定序器连接的实例。否则，该行为相当于带有显式参数的 connect 命令。如果同步器已配置，则将尝试同步器连接。然而，如果同步器离线，该命令将失败。通常，该宏仅应用于与新同步器的第一次连接。但是，为了方便起见，我们支持幂等调用，其中后续调用仅确保参与者重新连接到同步器。

**参数**

* `instance`: `com.digitalasset.canton.console.SequencerReference`
* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

<div id="同步器s.connect_bft" />

### `同步器s.connect_bft`

用于连接到同一同步器的多个定序器的宏。

论据是：

* `同步器Alias`：您将用来指代此同步器的名称。无法再改变了。
* `connections`：定序器连接列表，可以通过url定义。
* `manualConnect`：此连接是否应该手动处理，并且也排除在自动重新连接之外。
* `physical同步器Id`：可选的同步器 ID，以确保连接到正确的同步器。
* `priority`：同步器的优先级。越高，使用同步器的可能性就越大。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `sequencerTrustThreshold`：设置消息被认为有效之前必须同意的最小定序器数量。
* `sequencerLivenessMargin`：设置在`sequencerTrustThreshold`之后维持的额外订阅数量，以保证活跃度。
* `submissionRequestAmplification`：定义客户端应尝试发送符合重复数据删除条件的提交请求的频率。
* `sequencerConnectionPoolDelays`：定义定序器连接池使用的各种延迟。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `connections`: `Seq[com.digitalasset.canton.sequencing.SequencerConnection]`
* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `manualConnect`: `Boolean`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `sequencerTrustThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `sequencerLivenessMargin`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `submissionRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `sequencerConnectionPoolDelays`: `com.digitalasset.canton.sequencing.SequencerConnectionPoolDelays`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="同步器s.connect_by_config" />

### `同步器s.connect_by_config`

用于将参与者连接到由连接给出的同步器的宏。

这种连接变体需要同步器连接配置。否则，该行为相当于带有显式参数的 connect 命令。如果同步器已配置，则将尝试同步器连接。然而，如果同步器离线，该命令将失败。通常，该宏仅应用于与新同步器的第一次连接。但是，为了方便起见，我们支持幂等调用，其中后续调用仅确保参与者重新连接到同步器。

验证 - 是否验证给定定序器的连接性和 ID（默认全部）

**参数**

* `config`: `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="同步器s.connect_local" />

### `同步器s.connect_local`

用于将参与者连接到由定序器参考给出的本地配置的同步器的宏。

论据是：* `sequencer`：本地定序器引用别名 - 您将用来引用此同步器的名称。 Can not be changed anymore.
* `manualConnect`：此连接是否应该手动处理，并且也排除在自动重新连接之外。
* `physical同步器Id`：可选的同步器 ID，以确保连接到正确的同步器。
* `maxRetryDelayMillis`：两次连接尝试之间的最长时间（以毫秒为单位）。
* `priority`: The priority of the 同步器.越高，使用同步器的可能性就越大。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.同步器Alias`
* `manualConnect`: `Boolean`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="同步器s.connect_local_bft" />

### `同步器s.connect_local_bft`

用于连接到同一同步器的多个本地定序器的宏。

论据是：

* `同步器Alias`：您将用来指代此同步器的名称。无法再改变了。
* `sequencers`：要连接的定序器参考列表。
* `manualConnect`：此连接是否应该手动处理，并且也排除在自动重新连接之外。
* `physical同步器Id`：可选的同步器 ID，以确保连接到正确的同步器。
* `priority`：同步器的优先级。越高，使用同步器的可能性就越大。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `sequencerTrustThreshold`：设置消息被认为有效之前必须一致的最小定序器数量。
* `sequencerLivenessMargin`：设置超出`sequencerTrustThreshold`维持的额外订阅数量，以保证活跃度。
* `submissionRequestAmplification`：定义客户端应尝试发送符合重复数据删除条件的提交请求的频率。
* `sequencerConnectionPoolDelays`：定义定序器连接池使用的各种延迟。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `manualConnect`: `Boolean`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `sequencerTrustThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `sequencerLivenessMargin`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `submissionRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `sequencerConnectionPoolDelays`: `com.digitalasset.canton.sequencing.SequencerConnectionPoolDelays`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="同步器s.connect_multi" />

### `同步器s.connect_multi`

用于将参与者连接到支持通过多个端点进行连接的同步器的宏。

同步器可以提供许多端点来连接以获得可用性和性能优势。此版本的 connect 允许为单个同步器连接指定多个端点： connect\_multi("my同步器", Seq(sequencer1,equencer2)) 或： connect\_multi("my同步器", Seq("[https://host1.my同步器.net](https://host1.my同步器.net)", “[https://host2.my同步器.net](https://host2.my同步器.net)”、“[https://host3.my同步器.net](https://host3.my同步器.net)”))要创建更高级的连接配置，请对单个主机使用同步器s.to\_config，然后在连接之前使用 config.addConnection 添加其他连接： config = myparticipaint.同步器s.to\_config("my同步器", "[https://host1.my同步器.net](https://host1.my同步器.net)", ...otherArguments) config = config.addConnection("[https://host2.my同步器.net](https://host2.my同步器.net)", "[https://host3.my同步器.net](https://host3.my同步器.net)") my参与方.同步器s.connect(config)

论据是：

* `同步器Alias`：您将用来指代此同步器的名称。无法再改变了。
* `connections`：连接到此同步器的定序器连接定义（可以是 URL）。 IE。 [https://url:port](https://url:port) 同步 - 超时持续时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `connections`: `Seq[com.digitalasset.canton.sequencing.SequencerConnection]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

**返回：** `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`

<div id="同步器s.disconnect" />

### `同步器s.disconnect`

断开该参与者与给定同步器的连接。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

<div id="同步器s.disconnect_all" />

### `同步器s.disconnect_all`

断开该参与者与所有连接的同步器的连接。

<div id="同步器s.disconnect_local" />

### `同步器s.disconnect_local`

断开该参与者与给定本地同步器的连接。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

<div id="同步器s.help" />

### `同步器s.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="同步器s.id_of" />

### `同步器s.id_of`

返回给定同步器别名的 id。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**退货：** `com.digitalasset.canton.拓扑.同步器Id`

<div id="同步器s.is_connected" />

### `同步器s.is_connected`

测试参与者是否连接到同步器。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**退货：** `Boolean`

<div id="同步器s.is_connected_1" />

### `同步器s.is_connected_1`

测试参与者是否连接到物理同步器。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`

**返回：** `Boolean`

<div id="同步器s.is_connected_2" />

### `同步器s.is_connected_2`

测试参与者是否连接到同步器。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`

**返回：** `Boolean`

<div id="同步器s.is_registered" />

### `同步器s.is_registered`

如果使用给定别名注册同步器，则返回 true。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**返回：** `Boolean`

<div id="同步器s.list_connected" />

### `同步器s.list_connected`

列出该参与者已连接的同步器。

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListConnected同步器sResult]`

<div id="同步器s.list_registered" />

### `同步器s.list_registered`

列出该参与者配置的同步器。

对于每个返回的同步器，布尔值指示参与者当前是否连接到同步器。

**退货：** `Seq[(com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig, com.digitalasset.canton.拓扑.ConfiguredPhysical同步器Id, Boolean)]`

<div id="同步器s.logout" />

### `同步器s.logout`

撤销该参与者的身份验证令牌并关闭给定同步器中的所有定序器连接。同步器Alias：从中注销的同步器别名 在指定同步器的所有定序器上，该参与者的所有现有身份验证令牌都将被撤销。请注意，参与者并未与同步器断开连接；仅关闭与定序器的连接。参与者将自动重新打开连接，执行质询-响应并获取新的代币。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

<div id="同步器s.modify" />

### `同步器s.modify`

修改现有的同步器连接。

论据是：

* `同步器Alias`：同步器修饰符的别名 - 要应用于配置的更改。
* `validation`：需要对连接进行的验证。
* `physical同步器Id`：同步器的物理id。如果为空，则将更新活动的（如果没有活动的，则返回错误）。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `modifier`: `[com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig => com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/参与方/同步器/同步器ConnectionConfig.html)`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`

<div id="同步器s.physical_id_of" />

### `同步器s.physical_id_of`

返回给定同步器别名的物理 ID。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**返回：** `com.digitalasset.canton.拓扑.Physical同步器Id`

<div id="同步器s.reconnect" />

### `同步器s.reconnect`

将此参与者重新连接到给定的同步器。

幂等尝试重新建立与某个同步器的连接。如果重试设置为 false，则该命令在不成功时将抛出异常。如果重试设置为 true，则该命令将在第一次尝试获得结果后终止，但服务器将继续重试连接到同步器。

论据是：

* `同步器Alias`：您将用来指代此同步器的名称。无法再改变了。
* `retry`：重新连接是否应该继续重试直到成功，或者如果连接尝试失败则大声中止。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `retry`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `Boolean`

<div id="同步器s.reconnect_all" />

### `同步器s.reconnect_all`

将此参与者重新连接到所有未标记为手动启动的同步器。

参数是：ignoreFailures - 如果设置为true（默认），我们将尝试连接到所有节点，忽略任何失败synchronize - 超时持续时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `ignoreFailures`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="同步器s.reconnect_local" />

### `同步器s.reconnect_local`

将此参与者重新连接到给定的本地同步器。

幂等尝试重新建立与给定本地同步器的连接。与通用重新连接的行为相同。

论据是：

* `同步器Alias`：连接重试的同步器别名 - 重新连接是否应该继续重试直到成功，或者如果连接尝试失败则大声中止。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `retry`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**返回：** `Boolean`

<div id="同步器s.reconnect_local_1" />

### `同步器s.reconnect_local_1`

将此参与者重新连接到给定的本地同步器。

幂等尝试重新建立与给定本地同步器的连接。与通用重新连接的行为相同。

论据是：* `ref`：连接重试的同步器参考 - 重新连接是否应该继续重试直到成功，或者如果连接尝试失败则大声中止。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `ref`: `com.digitalasset.canton.console.SequencerReference`

**返回：** `Boolean`

<div id="同步器s.register" />

### `同步器s.register`

用于注册由定序器参考给出的本地配置同步器的宏。

论据是：

* `sequencer`：本地定序器引用别名 - 您将用来引用此同步器的名称。无法再改变了。
* `performHandshake`：如果为 true（默认），将与同步器执行握手。如果否，将仅存储配置，而不对同步器进行任何查询。
* `manualConnect`：此连接是否应该手动处理，并且也排除在自动重新连接之外。
* `physical同步器Id`：可选的同步器 ID，以确保连接到正确的同步器。
* `maxRetryDelayMillis`：两次连接尝试之间的最长时间（以毫秒为单位）。
* `priority`：同步器的优先级。越高，使用同步器的可能性就越大。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。
* `validation`: 是否验证给定定序器的连接性和ID（默认全部）

**参数**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.同步器Alias`
* `performHandshake`: `Boolean`
* `manualConnect`: `Boolean`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="同步器s.register_by_config" />

### `同步器s.register_by_config`

用于注册本地配置的同步器的宏。

论据是：

* `config`：同步器连接的配置 PerformHandshake - 如果为 true（默认），将与同步器执行握手。如果否，将仅存储配置，而不对同步器进行任何查询。
* `validation`：是否验证给定定序器的连接和 ID（默认全部）同步 - 超时持续时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `config`: `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`
* `performHandshake`: `Boolean`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

### 健康

<div id="health.active" />

### `health.active`

检查节点是否正在运行并且是活动实例（中介者、参与者）。

**返回：** `Boolean`

<div id="health.count_in_flight" />

### `health.count_in_flight`

计算同步器上待处理的命令提交和事务。

此命令查找所选同步器上当前待处理命令提交和事务的数量。

待处理的命令提交和事务之间不存在同步。并且相应的计数仅供参考！

该命令对于再次确保所选同步器当前不存在正在进行的提交或事务特别有用。例如，这种再保证有助于继续进行维修操作。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

**退货：** `com.digitalasset.canton.admin.api.client.data.InFlightCount`

<div id="health.dump_1" />

### `health.dump_1`

收集 Canton 系统信息以帮助诊断问题。

为本地 Canton 进程和任何连接的远程节点生成全面的运行状况报告。

论据是：

* `outputFile`：指定保存报告的文件路径。如果未设置，则使用默认路径。
* `timeout`：设置收集数据的自定义超时，对于来自慢速远程节点的大型报告很有用。
* `chunkSize`：调整来自远程节点的数据流块大小。使用它可以防止与“最大入站消息大小”相关的 gRPC 错误**参数**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**返回：** `String`

<div id="health.has_identity" />

### `health.has_identity`

如果节点有身份，则返回 true。

**返回：** `Boolean`

<div id="health.help_1" />

### `health.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="health.initialized" />

### `health.initialized`

如果节点已初始化，则返回 true。

**返回：** `Boolean`

<div id="health.is_ready_for_id"/>

### `health.is_ready_for_id`

检查节点是否准备好设置节点的 id。

**退货：** `Boolean`

<div id="health.is_ready_for_initialization" />

### `health.is_ready_for_initialization`

检查节点是否已准备好初始化。

**返回：** `Boolean`

<div id="health.is_ready_for_node_拓扑" />

### `health.is_ready_for_node_拓扑`

检查节点是否准备好上传节点的身份拓扑。

**退货：** `Boolean`

<div id="health.is_running" />

### `health.is_running`

检查节点是否正在运行。

**返回：** `Boolean`

<div id="health.last_error_trace" />

### `health.last_error_trace`

显示最近间隔内使用给定traceId记录的所有消息。

返回与给定跟踪 ID 关联的缓冲日志消息列表。通常，trace-id 取自 last\_errors()

**参数**

* `traceId`: `String`

**退货：** `Seq[String]`

<div id="health.last_errors" />

### `health.last_errors`

显示最后记录的错误。

返回一个映射，其中 Trace-id 作为键，最新的错误消息作为值。要求启用（而不是关闭）--log-last-errors。

**返回：** `Map[String,String]`

<div id="health.maybe_ping" />

### `health.maybe_ping`

通过账本向目标参与者发送 ping。成功时产生一些（持续时间），失败时产生无。

**参数**

* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `id`: `String`

**返回：** `Option[scala.concurrent.duration.Duration]`

<div id="health.ping" />

### `health.ping`

通过账本向目标参与者发送 ping。如果成功，则生成持续时间；如果失败，则抛出 RuntimeException。

**参数**

* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `id`: `String`

**返回：** `scala.concurrent.duration.Duration`

<div id="health.set_log_level" />

### `health.set_log_level`

更改进程的日志级别。

如果使用默认的logback配置，这将改变进程的日志级别。

**参数**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_1" />

### `health.status_1`

获取人类（和机器）可读的状态信息。

**返回：** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity" />

### `health.wait_for_identity`

等待节点拥有身份。

<div id="health.wait_for_initialized" />

### `health.wait_for_initialized`

等待节点初始化。

<div id="health.wait_for_ready_for_id" />

### `health.wait_for_ready_for_id`

等待节点准备好设置节点的 id。

<div id="health.wait_for_ready_for_initialization" />

### `health.wait_for_ready_for_initialization`

等待节点准备好初始化。

<div id="health.wait_for_ready_for_node_拓扑" />

### `health.wait_for_ready_for_node_拓扑`

等待节点准备好上传节点的身份拓扑。

<div id="health.wait_for_running" />

### `health.wait_for_running`

等待节点运行。

### 密钥管理

<div id="keys.help" />

### `keys.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.download" />

### `keys.public.download`

下载公钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**返回：** `com.google.protobuf.ByteString`<div id="keys.public.download_to" />

### `keys.public.download_to`

下载公钥并将其保存到文件中。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help" />

### `keys.public.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.list" />

### `keys.public.list`

列出注册表中的公钥。

返回已添加到密钥注册表中的所有公钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**退货：** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner" />

### `keys.public.list_by_owner`

列出给定 keyOwner 的密钥。

该命令是 `list_key_owners` 的便捷包装，采用显式 keyOwner 作为搜索参数。响应包括公钥。

**参数**

* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners" />

### `keys.public.list_owners`

列出具有给定搜索参数的键的活动所有者。

此命令允许深入检查拓扑状态。响应包括公钥。可选的filterKeyOwnerType类型可以是“参与方Id.Code”、“MediatorId.Code”、“SequencerId.Code”。

**参数**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.拓扑.MemberCode]`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload" />

### `keys.public.upload`

上传公钥。

导入公钥并将其与用于为该密钥提供一些上下文的名称一起存储。

**参数**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**退货：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from" />

### `keys.public.upload_from`

上传公钥。

**参数**

* `filename`: `String`
* `name`: `Option[String]`

**返回：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete" />

### `keys.secret.delete`

删除私钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download" />

### `keys.secret.download`

下载密钥对。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**返回：** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to" />

### `keys.secret.download_to`

下载密钥对并将其保存到文件中。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key" />

### `keys.secret.generate_encryption_key`

生成新的公钥/私钥对进行加密并将其存储在保管库中。

可选的名称参数允许您存储关联的字符串以方便使用。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**返回：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key" />

### `keys.secret.generate_signing_key`

生成新的公钥/私钥对用于签名并将其存储在保管库中。可选的名称参数允许您存储关联的字符串以方便使用。用途指定签名密钥的预期用途，可以是：

* `Namespace`：根命名空间密钥，定义节点身份并签署拓扑请求；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id" />

### `keys.secret.get_wrapper_key_id`

获取用于加密私钥存储的包装器密钥 ID。

**返回：** `String`

<div id="keys.secret.help" />

### `keys.secret.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.secret.list" />

### `keys.secret.list`

列出私人保管库中的密钥。

将所有公钥返回到密钥保管库中相应的私钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**返回：** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key" />

### `keys.secret.register_kms_encryption_key`

在存储其公共信息的存储库中注册指定的 KMS 加密密钥。

KMS 加密密钥的 ID。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `name`: `String`

**退货：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key" />

### `keys.secret.register_kms_signing_key`

在州注册指定的 KMS 签名密钥，将其公共信息存储在保险库中。

KMS 签名密钥的 ID。用途指定签名密钥的预期用途，可以是：

* `Namespace`：用于定义节点身份并签署拓扑请求的根命名空间密钥；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key" />

### `keys.secret.rotate_kms_node_key`

使用新的预生成的 KMS 密钥对轮换给定节点的密钥对。

使用预生成的密钥轮换外部存储在 KMS 中的现有加密或签名密钥。注意：此命令无法轮换命名空间根签名密钥。我们要旋转的密钥的指纹。新 KMS 密钥的 ID（例如资源名称）。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key" />

### `keys.secret.rotate_node_key`

轮换节点的公钥/私钥对。

轮换现有加密或签名密钥。注意：此命令无法轮换命名空间根或中间签名密钥。我们要旋转的密钥的指纹。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `name`: `String`

**退货：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys" />

### `keys.secret.rotate_node_keys`

轮换节点的公钥/私钥对。

对于参与者节点，它轮换签名和加密密钥对。对于定序器或中介器节点，它会轮换签名密钥对，因为这些节点没有加密密钥对。注意：此命令不会轮换命名空间根或中间签名密钥。<div id="keys.secret.rotate_wrapper_key" />

### `keys.secret.rotate_wrapper_key`

更改加密私钥存储的包装密钥。

更改用于加密存储中的私钥的包装器密钥（例如 AWS KMS 密钥）。 newWrapperKeyId：要使用的可选新包装器密钥 ID。如果包装器密钥 ID 为空，Canton 将根据当前配置生成一个新密钥。

**参数**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload" />

### `keys.secret.upload`

上传密钥对。

上传之前下载的密钥对。 pairBytes：先前下载的密钥对的二进制表示形式名称：密钥对的（可选）描述性名称密码：用于解密加密密钥对的可选密码

**参数**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from" />

### `keys.secret.upload_from`

从文件上传（加载并导入）密钥对。

从文件中上传之前下载的密钥对。文件名：保存密钥对的文件的名称 名称：密钥对的（可选）描述性名称 密码：用于解密加密密钥对的可选密码

**参数**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### 账本 API 访问

参与者参考上的以下命令提供对参与者的 Ledger API 服务的访问。

<div id="ledger_api.help" />

### `ledger_api.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.javaapi.help" />

### `ledger_api.javaapi.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

#### 命令完成服务

<div id="ledger_api.completions.help" />

### `ledger_api.completions.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.completions.list" />

### `ledger_api.completions.list`

列出指定偏移量之后的命令完成情况。

如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。空偏移量表示参与者偏移量的开始。

**参数**

* `partyId`: `com.digitalasset.canton.拓扑.Party`
* `atLeastNumCompletions`: `Int`
* `beginOffsetExclusive`: `Long`
* `userId`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `filter`: `com.daml.ledger.api.v2.completion.Completion => Boolean`

**返回：** `Seq[com.daml.ledger.api.v2.completion.Completion]`

<div id="ledger_api.completions.subscribe" />

### `ledger_api.completions.subscribe`

订阅命令完成流。

此函数连接到命令完成流并将命令完成传递到`observer`，直到流完成。仅返回`parties`中派对的完成情况。返回的完成从`beginOffset`开始（默认：零值表示参与者开始）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。

**参数**

* `observer`: `io.grpc.stub.StreamObserver[com.daml.ledger.api.v2.completion.Completion]`
* `parties`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `beginOffsetExclusive`: `Long`
* `userId`: `String`

**退货：** `AutoCloseable`

#### 命令提交服务

<div id="ledger_api.commands.failed" />

### `ledger_api.commands.failed`

调查失败的命令。

与状态（...，状态= CommandState.Failed）相同。

**参数**

* `commandId`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.commands.help" />

### `ledger_api.commands.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.commands.status" />

### `ledger_api.commands.status`

研究成功和失败的命令。

查找命令的状态。请注意，只会返回保存在内存中的最近命令。

**参数*** `commandIdPrefix`: `String`
* `state`: `com.daml.ledger.api.v2.admin.command_inspection_service.CommandState`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.commands.submit" />

### `ledger_api.commands.submit`

提交命令并等待生成的事务，返回事务或失败。

代表`actAs`各方提交命令，等待结果事务提交，并返回“扁平化”事务。如果设置了超时，它还会等待事务出现在参与该事务的所有其他配置的参与者处。调用会阻塞，直到事务提交或失败为止；超时仅指定在其他参与者处等待多长时间。如果事务未提交，或者在分配的时间内对相关参与者不可见，则失败。请注意，如果设置了 optTimeout 并且所涉及的各方同时启用/禁用或其参与者连接/断开，则该命令当前可能会导致虚假超时，或者可能会在事务出现在所有涉及的参与者处之前返回。

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `commandId`: `String`
* `optTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**退货：** `com.daml.ledger.api.v2.transaction.Transaction`

<div id="ledger_api.commands.submit_assign" />

### `ledger_api.commands.submit_assign`

提交分配命令并等待重新分配结果，返回重新分配或失败。

代表`submitter`方提交分配命令，等待结果分配提交，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与该分配的所有其他已配置参与者处。该调用将阻塞，直到分配提交或失败。如果作业未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。 重分配Id 应该是相应的 Submit\_unassign 命令返回的 ID。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `重分配Id`: `String`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.AssignedWrapper`

<div id="ledger_api.commands.submit_assign_async" />

### `ledger_api.commands.submit_assign_async`

异步提交分配命令。

提供对 Ledger API 的命令提交服务的访问。有关参数的文档，请参阅 [Ledger API 参考](/sdks-tools/api-reference/ledger-api)。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `重分配Id`: `String`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `commandId`: `String`
* `submissionId`: `String`

<div id="ledger_api.commands.submit_assign_with_format" />

### `ledger_api.commands.submit_assign_with_format`

提交分配命令并等待重新分配结果，返回重新分配或失败。代表`submitter`方提交分配命令，等待结果分配提交，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与该分配的所有其他已配置参与者处。该调用将阻塞，直到分配提交或失败。如果作业未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。 重分配Id 应该是相应的 Submit\_unassign 命令返回的 ID。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `重分配Id`: `String`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `eventFormat`: `Option[com.daml.ledger.api.v2.transaction_filter.EventFormat]`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.EmptyOrAssignedWrapper`

<div id="ledger_api.commands.submit_async" />

### `ledger_api.commands.submit_async`

异步提交命令。

提供对 Ledger API 的命令提交服务的访问。有关参数的文档，请参阅 [Ledger API 参考](/sdks-tools/api-reference/ledger-api)。

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.PartyId]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `commandId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`

<div id="ledger_api.commands.submit_reassign" />

### `ledger_api.commands.submit_reassign`

将 `submit_unassign` 和 `submit_assign` 组合在一个宏中。

参数见`submit_unassign`和`submit_assign`。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**返回：** `(com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UnassignedWrapper, com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.AssignedWrapper)`

<div id="ledger_api.commands.submit_unassign" />

### `ledger_api.commands.submit_unassign`

提交取消分配命令并等待重新分配结果，返回重新分配或失败。

代表`submitter`方提交取消分配命令，等待提交取消分配结果，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与取消分配的所有其他已配置参与者中。该调用将阻塞，直到取消分配提交或失败。如果取消分配未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UnassignedWrapper`

<div id="ledger_api.commands.submit_unassign_async" />### `ledger_api.commands.submit_unassign_async`

异步提交取消分配命令。

提供对 Ledger API 的命令提交服务的访问。有关参数的文档，请参阅 [Ledger API 参考](/sdks-tools/api-reference/ledger-api)。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `commandId`: `String`
* `submissionId`: `String`

<div id="ledger_api.commands.submit_unassign_with_format" />

### `ledger_api.commands.submit_unassign_with_format`

提交取消分配命令并等待重新分配结果，返回重新分配或失败。

代表`submitter`方提交取消分配命令，等待取消分配结果提交，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与取消分配的所有其他已配置参与者中。该调用将阻塞，直到取消分配提交或失败。如果取消分配未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `eventFormat`: `Option[com.daml.ledger.api.v2.transaction_filter.EventFormat]`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**返回：** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.EmptyOrUnassignedWrapper`

<div id="ledger_api.javaapi.commands.help" />

### `ledger_api.javaapi.commands.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.javaapi.commands.submit" />

### `ledger_api.javaapi.commands.submit`

提交 java codegen 命令并等待生成的事务，返回事务或失败。

代表`actAs`各方提交命令，等待结果事务提交，并返回“扁平化”事务。如果设置了超时，它还会等待事务出现在参与该事务的所有其他配置的参与者处。调用会阻塞，直到事务提交或失败为止；超时仅指定在其他参与者处等待多长时间。如果事务未提交，或者在分配的时间内对相关参与者不可见，则失败。请注意，如果设置了 optTimeout 并且所涉及的各方同时启用/禁用或其参与者连接/断开，则该命令当前可能会导致虚假超时，或者可能会在事务出现在所有涉及的参与者处之前返回。

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `commandId`: `String`
* `optTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**返回：** `com.daml.ledger.javaapi.data.Transaction`

<div id="ledger_api.javaapi.commands.submit_assign" />

### `ledger_api.javaapi.commands.submit_assign`

提交分配命令并等待生成的 java codegen 重新分配，返回重新分配或失败。代表`submitter`方提交分配命令，等待结果分配提交，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与该分配的所有其他参与者处。该调用将阻塞，直到分配提交或失败。如果作业未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。 重分配Id 应该是相应的 Submit\_unassign 命令返回的 ID。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `重分配Id`: `String`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `includeCreatedEventBlob`: `Boolean`

**退货：** `com.daml.ledger.javaapi.data.重分配`

<div id="ledger_api.javaapi.commands.submit_async" />

### `ledger_api.javaapi.commands.submit_async`

异步提交 java codegen 命令。

提供对 Ledger API 的命令提交服务的访问。有关参数的文档，请参阅 [Ledger API 参考](/sdks-tools/api-reference/ledger-api)。

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.PartyId]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `commandId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`

<div id="ledger_api.javaapi.commands.submit_unassign" />

### `ledger_api.javaapi.commands.submit_unassign`

提交分配命令并等待生成的 java codegen 重新分配，返回重新分配或失败。

代表`submitter`方提交取消分配命令，等待提交取消分配结果，并返回重新分配。如果设置了超时，它还会等待重新分配出现在参与取消分配的所有其他参与者处。该调用将阻塞，直到取消分配提交或失败。如果取消分配未提交，或者未及时对相关参与者可见，则失败。超时指定等待重新分配出现在提交和所有相关参与者的更新流中的时间。

**参数**

* `submitter`: `com.digitalasset.canton.拓扑.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**返回：** `com.daml.ledger.javaapi.data.重分配`

<div id="ledger_api.interactive_submission.execute" />

### `ledger_api.interactive_submission.execute`

执行准备好的提交。

preparedTransaction：准备好的交易字节串，通常从\[\[prepare]]响应的prepareTransaction字段获取。 transactionSignatures：交易哈希的签名。哈希值通常是从 \[\[prepare]] 响应的 preparedTransactionHash 字段获取的。但请注意，调用者应重新计算哈希值并确保其与 \[\[prepare]] 中提供的哈希值匹配，以确保他们签署的哈希值能够正确表示他们想要提交的交易。

**参数*** `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.拓扑.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`

**返回：** `com.daml.ledger.api.v2.interactive.interactive_submission_service.ExecuteSubmissionResponse`

<div id="ledger_api.interactive_submission.execute_and_wait" />

### `ledger_api.interactive_submission.execute_and_wait`

执行准备好的提交并等待其完成（成功或失败）。

与执行类似，但它会等待命令完成后再返回。相当于 CommandService 中的“submitAndWait”。重要提示：此命令假定执行参与者被信任返回有效的命令完成。不诚实的执行参与者可能会错误地响应命令失败，即使命令成功。

**参数**

* `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.拓扑.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`

**退货：** `com.daml.ledger.api.v2.interactive.interactive_submission_service.ExecuteSubmissionAndWaitResponse`

<div id="ledger_api.interactive_submission.execute_and_wait_for_transaction" />

### `ledger_api.interactive_submission.execute_and_wait_for_transaction`

执行准备好的提交并返回结果事务。

与executeAndWait类似，但返回结果事务。重要提示：此命令假定执行参与者被信任返回有效的命令完成。不诚实的执行参与者可能会错误地响应命令失败，即使命令成功。

**参数**

* `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.拓扑.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `transactionShape`: `Option[com.daml.ledger.api.v2.transaction_filter.TransactionShape]`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `includeCreatedEventBlob`: `Boolean`

**退货：** `com.daml.ledger.api.v2.transaction.Transaction`

<div id="ledger_api.interactive_submission.help" />

### `ledger_api.interactive_submission.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.interactive_submission.preferred_package_version" />

### `ledger_api.interactive_submission.preferred_package_version`

获取构建命令提交的首选包版本。

首选包是所提供的包名称的最高版本的包，由托管所提供方的所有参与者进行审查。 Ledger API 客户端应使用此端点来构建与所提供的首选包兼容的命令提交，并做出明智的决策：* 哪些是可用于创建合约的兼容包
* 命令中可以使用哪个合约或行权选择参数版本
* 可以在合同方的模板或接口上执行哪些选择：在计算首选包时应考虑其审核状态的各方 packageName：请求首选包的包名称 同步器Id：用于解析此查询的同步器的拓扑状态。如果没有指定。将使用参与者连接到的所有同步器的拓扑状态。 vettingValidAt：应计算包审核有效性的时间戳。如果未提供，则使用参与者的当前时钟时间。

**参数**

* `parties`: `Set[com.digitalasset.canton.拓扑.Party]`
* `packageName`: `com.digitalasset.canton.LfPackageName`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vettingValidAt`: `Option[com.digitalasset.canton.data.CantonTimestamp]`

**返回：** `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.PackagePreference]`

<div id="ledger_api.interactive_submission.preferred_packages" />

### `ledger_api.interactive_submission.preferred_packages`

获取用于构建命令提交的首选包。

首选包是所提供的包名称的最高版本的包，由托管所提供方的所有参与者进行审查。 Ledger API 客户端应使用此端点来构建与所提供的首选包兼容的命令提交，并做出明智的决策：

* 哪些是可用于创建合约的兼容包
* 命令中可以使用哪个合约或行权选择参数版本
* 哪些选择可以在合约模板或界面上执行

一般来说，提供命令的根包名称的要求就足够了。当其他通知者需要使用命令根包的包依赖项时，可以提供其他包名称要求。

party：在计算首选包时应考虑其审查状态的各方 packageName：请求首选包的包名称 同步器Id：用于解析此查询的同步器的拓扑状态。如果没有指定。将使用参与者连接到的所有同步器的拓扑状态。 vettingValidAt：应计算包审核有效性的时间戳。如果未提供，则使用参与者的当前时钟时间。

**参数**

* `packageVettingRequirements`: `Map[com.digitalasset.canton.LfPackageName,Set[com.digitalasset.canton.拓扑.PartyId]]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vettingValidAt`: `Option[com.digitalasset.canton.data.CantonTimestamp]`

**返回：** `com.daml.ledger.api.v2.interactive.interactive_submission_service.GetPreferredPackagesResponse`

<div id="ledger_api.interactive_submission.prepare" />

### `ledger_api.interactive_submission.prepare`

准备一个用于交互式提交的交易。

准备一个用于交互式提交的交易。与提交类似，只不过不是将交易提交到网络，而是返回交易的序列化版本以及哈希值。这允许非托管方在通过执行命令提交哈希之前使用其私钥对哈希进行签名。如果您希望直接提交命令而不需要外部签名步骤，请改用“提交”。

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `commandId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `verboseHashing`: `Boolean`
* `prefetchContractKeys`: `Seq[com.daml.ledger.api.v2.commands.PrefetchContractKey]`
* `maxRecordTime`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `estimate流量Cost`: `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.CostEstimationHints]`**返回：** `com.daml.ledger.api.v2.interactive.interactive_submission_service.PrepareSubmissionResponse`

<div id="ledger_api.javaapi.interactive_submission.help" />

### `ledger_api.javaapi.interactive_submission.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.javaapi.interactive_submission.prepare" />

### `ledger_api.javaapi.interactive_submission.prepare`

准备一个用于交互式提交的交易。

准备交互式提交的交易

**参数**

* `actAs`: `Seq[com.digitalasset.canton.拓扑.PartyId]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `commandId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `verboseHashing`: `Boolean`
* `prefetchContractKeys`: `Seq[com.daml.ledger.javaapi.data.PrefetchContractKey]`
* `maxRecordTime`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `estimate流量Cost`: `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.CostEstimationHints]`

**返回：** `com.daml.ledger.api.v2.interactive.interactive_submission_service.PrepareSubmissionResponse`

#### 活动服务

<div id="ledger_api.event_query.by_contract_id" />

### `ledger_api.event_query.by_contract_id`

通过合约 ID 获取事件。

返回与给定合约 ID 关联的事件

**参数**

* `contractId`: `String`
* `requestingParties`: `Seq[com.digitalasset.canton.拓扑.Party]`

**返回：** `com.daml.ledger.api.v2.event_query_service.GetEventsByContractIdResponse`

<div id="ledger_api.event_query.help" />

### `ledger_api.event_query.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.javaapi.event_query.by_contract_id" />

### `ledger_api.javaapi.event_query.by_contract_id`

通过合约 ID 获取 java codegen 中的事件。

返回与给定合约 ID 关联的事件

**参数**

* `contractId`: `String`
* `requestingParties`: `Seq[com.digitalasset.canton.拓扑.Party]`

**返回：** `com.daml.ledger.api.v2.EventQueryServiceOuterClass.GetEventsByContractIdResponse`

<div id="ledger_api.javaapi.event_query.help" />

### `ledger_api.javaapi.event_query.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

#### 身份提供者配置管理

<div id="ledger_api.identity_provider_config.create" />

### `ledger_api.identity_provider_config.create`

创建新的身份提供商配置。

创建身份提供者配置。如果达到允许的单独配置的最大数量，请求将失败。

**参数**

* `identityProviderId`: `String`
* `isDeactivated`: `Boolean`
* `jwksUrl`: `String`
* `issuer`: `String`
* `audience`: `Option[String]`

**返回：** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

<div id="ledger_api.identity_provider_config.delete" />

### `ledger_api.identity_provider_config.delete`

删除身份提供商配置。

删除现有身份提供商配置

**参数**

* `identityProviderId`: `String`

<div id="ledger_api.identity_provider_config.get" />

### `ledger_api.identity_provider_config.get`

获取身份提供商配置。

通过id获取身份提供者配置

**参数**

* `identityProviderId`: `String`

**返回：** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

<div id="ledger_api.identity_provider_config.help" />

### `ledger_api.identity_provider_config.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.identity_provider_config.list" />

### `ledger_api.identity_provider_config.list`

列出身份提供商配置。

列出所有现有身份提供商配置

**返回：** `Seq[com.digitalasset.canton.ledger.api.IdentityProviderConfig]`

<div id="ledger_api.identity_provider_config.update" />

### `ledger_api.identity_provider_config.update`

更新身份提供商。更新身份提供商

**参数**

* `identityProviderId`: `String`
* `isDeactivated`: `Boolean`
* `jwksUrl`: `String`
* `issuer`: `String`
* `audience`: `Option[String]`
* `updateMask`: `com.google.protobuf.field_mask.FieldMask`

**返回：** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

#### 用户管理服务

<div id="ledger_api.users.create" />

### `ledger_api.users.create`

使用给定的 id 创建一个用户。

用户习惯于动态管理授予 Daml 用户的权限。它们允许我们将（应用程序的）稳定的本地标识符与一组各方链接起来。 id: 用于识别给定用户的 id actAs: 允许该用户充当的各方集合 PrimaryParty: 默认情况下应链接到该用户的可选方 readAs: 允许该用户作为参与者读取的各方集合Admin: flag (默认 false) 指示是否允许用户使用 Ledger Api 的管理命令 IdentityProviderAdmin: flag (默认 false) 指示是否允许用户管理分配给同一身份提供商的用户和各方 isDeactivated: flag (默认) false) 指示用户是否处于活动状态 注释：链接到该用户的键值对集合。

**参数**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `primaryParty`: `Option[com.digitalasset.canton.拓扑.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `参与方Admin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `isDeactivated`: `Boolean`
* `annotations`: `Map[String,String]`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `executeAsAnyParty`: `Boolean`

**退货：** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.delete" />

### `ledger_api.users.delete`

删除一个用户。

通过id删除用户。 id：用户 ID IdentityProviderId：身份提供商 ID

**参数**

* `id`: `String`
* `identityProviderId`: `String`

<div id="ledger_api.users.get" />

### `ledger_api.users.get`

获取给定id的用户的用户数据。

如果没有这样的用户，则获取与给定用户 ID 关联的数据将失败。您将获得用户的主要参与方、活跃状态和注释。如果您需要用户权限，请改用rights.list。 id：用户 ID IdentityProviderId：身份提供商 ID

**参数**

* `id`: `String`
* `identityProviderId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.help" />

### `ledger_api.users.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.users.list" />

### `ledger_api.users.list`

列出用户。

列出该参与者节点的用户 filterUser：使用给定的过滤字符串过滤结果 pageToken：用于分页（如果有更多页面，则结果包含页面令牌） pageSize：应用过滤器之前的默认页面大小 IdentityProviderId：身份提供者 id

**参数**

* `filterUser`: `String`
* `pageToken`: `String`
* `pageSize`: `Int`
* `identityProviderId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.UsersPage`

<div id="ledger_api.users.update" />

### `ledger_api.users.update`

更新用户。

目前您可以更新注释、活动状态和主要方。您无法更新其他用户属性。 id：要更新的用户id modifier：修改用户的函数；例如：`user => { user.copy(isActive = false, primaryParty = None, annotations = user.annotations.updated("a", "b").removed("c")) }`identityProviderId：身份提供商 ID

**参数**

* `id`: `String`
* `modifier`: `[com.digitalasset.canton.admin.api.client.data.User => com.digitalasset.canton.admin.api.client.data.User](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/User.html)`
* `identityProviderId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.update_idp" />### `ledger_api.users.update_idp`

更新用户的身份提供商 ID。

更新用户的身份提供商 ID。 id：用于识别给定用户的 id sourceIdentityProviderId：源身份提供商 id targetIdentityProviderId：目标身份提供商 id

**参数**

* `id`: `String`
* `sourceIdentityProviderId`: `String`
* `targetIdentityProviderId`: `String`

<div id="ledger_api.users.rights.grant" />

### `ledger_api.users.rights.grant`

向用户授予新权限。

用户习惯于动态管理授予 Daml 应用程序的权限。此功能用于向现有用户授予新权限。 id：用于识别给定用户的 id actAs：允许该用户充当的各方集合 readAs：允许该用户作为参与者读取的各方集合 Admin：标志（默认 false）指示是否允许用户使用 Ledger Api 的管理命令 IdentityProviderAdmin：标志（默认 false）指示是否允许用户管理分配给同一身份提供商的用户和各方允许作为任何一方读取executeAs：允许该用户操作交互式提交的各方集合executeAsAnyParty：标志（默认为 false）指示是否允许用户作为任何一方操作交互式提交

**参数**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `参与方Admin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `executeAsAnyParty`: `Boolean`

**返回：** `com.digitalasset.canton.admin.api.client.data.UserRights`

<div id="ledger_api.users.rights.help" />

### `ledger_api.users.rights.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.users.rights.list" />

### `ledger_api.users.rights.list`

列出用户的权限。

列出用户的权限或当前用户的权限。 id：用户 ID IdentityProviderId：身份提供商 ID

**参数**

* `id`: `String`
* `identityProviderId`: `String`

**退货：** `com.digitalasset.canton.admin.api.client.data.UserRights`

<div id="ledger_api.users.rights.revoke" />

### `ledger_api.users.rights.revoke`

撤销用户权限。

用于撤销用户的特定权限。 id：用于识别给定用户的 id actAs：不应允许该用户作为任何一方读取的各方集合 readAs：不应允许该用户作为任何一方读取的各方集合参与方Admin：如果设置为 true，则将删除参与者管理员权限。允许用户操作交互式提交executeAsAnyParty：标志（默认为 false）指示是否允许用户作为任何一方操作交互式提交

**参数**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `参与方Admin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `executeAsAnyParty`: `Boolean`

**退货：** `com.digitalasset.canton.admin.api.client.data.UserRights`

#### 套餐服务

<div id="ledger_api.packages.help" />

### `ledger_api.packages.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.packages.list" />

### `ledger_api.packages.list`

列出 Daml 包。

**参数**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.daml.ledger.api.v2.admin.package_management_service.PackageDetails]`

<div id="ledger_api.packages.upload_dar" />

### `ledger_api.packages.upload_dar`

从 Dar 文件上传包。上传 Dar 可以通过账本 Api 服务器或通过 Canton 管理 Api 完成。 Ledger Api 是跨账本的可移植方法。 Canton 管理 API 更强大，因为它允许控制 Canton 的特定行为。特别是，使用账本 Api 上传的 Dar 将无法在 Dar 商店中使用，并且无法再次下载。此外，使用账本 Api 上传的 Dars 将会被审核，但系统不会等待 Dars 成功注册到所有连接的同步器。因此，如果上传 Dar 并随后立即使用，则命令可能会因缺少软件包审查而退回。

**参数**

* `darPath`: `String`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

<div id="ledger_api.packages.validate_dar" />

### `ledger_api.packages.validate_dar`

根据当前参与者的状态验证 DAR。

执行与上传调用执行的相同的 DAR 和 Daml 包验证检查，但对目标参与者没有影响：DAR 未保留或审查。

**参数**

* `darPath`: `String`

#### 聚会管理服务

<div id="ledger_api.parties.allocate" />

### `ledger_api.parties.allocate`

分配一个新的政党。

在账本上分配一个新方。 party：生成参与方标识符的提示注释：与此参与方关联并本地存储在此 Ledger API 服务器上的键值对。参与者必须连接到同步器。如果参与者仅连接到一个同步器，则可以省略该参数。

**参数**

* `party`: `String`
* `annotations`: `Map[String,String]`
* `identityProviderId`: `String`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `userId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.parties.PartyDetails`

<div id="ledger_api.parties.allocate_external" />

### `ledger_api.parties.allocate_external`

分配一个新的外部方。

在账本上分配一个新的外部方。 同步器Id：用于分配参与方交易的 同步器Id：加入交易及其各自的签名 multiSignatures：所有加入交易的组合哈希上的签名

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `transactions`: `Seq[(com.digitalasset.canton.topology.transaction.拓扑Transaction.Generic拓扑Transaction, Seq[com.digitalasset.canton.crypto.Signature])]`
* `multiSignatures`: `Seq[com.digitalasset.canton.crypto.Signature]`

**返回：** `com.daml.ledger.api.v2.admin.party_management_service.AllocateExternalPartyResponse`

<div id="ledger_api.parties.generate_拓扑" />

### `ledger_api.parties.generate_拓扑`

为外部方生成拓扑交易。

生成必要的拓扑事务的便捷功能。对于更复杂的设置，请手动生成拓扑事务。 同步器Id：应为其生成事务的 同步器Id。 partyHint: 参与方的前缀 publicKey: 外部方的签名公钥 local参与方ObservationOnly: 如果为 true，则分配参与者将仅是观察者 otherConfirming参与方Uids: 将代表该方确认 daml 交易的其他参与者的列表confidentialThreshold: 需要批准 daml 交易的确认参与者的数量observing参与方Uids: 应观察外部方交易的其他参与者的列表

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `partyHint`: `String`
* `publicKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `local参与方ObservationOnly`: `Boolean`
* `otherConfirming参与方Ids`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `confirmationThreshold`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `observing参与方Ids`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`

**返回：** `com.digitalasset.canton.admin.api.client.data.parties.GenerateExternalParty拓扑`

<div id="ledger_api.parties.get" />

### `ledger_api.parties.get`

获取已知派对的派对详细信息。获取给定身份提供商的 Ledger API 服务器已知的各方的详细信息。 IdentityProviderId：身份提供商 ID

**参数**

* `parties`: `Seq[com.digitalasset.canton.拓扑.PartyId]`
* `identityProviderId`: `String`
* `failOnNotFound`: `Boolean`

**返回：** `Map[com.digitalasset.canton.拓扑.PartyId,com.digitalasset.canton.admin.api.client.data.parties.PartyDetails]`

<div id="ledger_api.parties.help" />

### `ledger_api.parties.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.parties.list" />

### `ledger_api.parties.list`

列出 Ledger API 服务器已知的各方。

列出 Ledger API 服务器已知的各方。 IdentityProviderId：身份提供商 ID filterParty：按名称过滤方

**参数**

* `identityProviderId`: `String`
* `filterParty`: `String`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.parties.PartyDetails]`

<div id="ledger_api.parties.update" />

### `ledger_api.parties.update`

更新参与者本地方详细信息。

目前您只能更新注释。您无法更新其他用户属性。 party：要更新的政党，modifier：修改政党详细信息的函数，例如：`partyDetails => { partyDetails.copy(annotations = partyDetails.annotations.updated("a", "b").removed("c")) }`identityProviderId：身份提供者id

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `modifier`: `[com.digitalasset.canton.admin.api.client.data.parties.PartyDetails => com.digitalasset.canton.admin.api.client.data.parties.PartyDetails](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/parties/PartyDetails.html)`
* `identityProviderId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.parties.PartyDetails`

<div id="ledger_api.parties.update_idp" />

### `ledger_api.parties.update_idp`

更新参与方的身份提供商 ID。

更新参与方的身份提供商 ID。 party：要更新的一方 sourceIdentityProviderId：源身份提供商 ID targetIdentityProviderId：目标身份提供商 ID

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `sourceIdentityProviderId`: `String`
* `targetIdentityProviderId`: `String`

#### 国家服务

<div id="ledger_api.state.connected_同步器s" />

### `ledger_api.state.connected_同步器s`

读取一方当前连接的同步器。

**参数**

* `partyId`: `Option[com.digitalasset.canton.拓扑.PartyId]`

**退货：** `com.daml.ledger.api.v2.state_service.GetConnected同步器sResponse`

<div id="ledger_api.state.end" />

### `ledger_api.state.end`

读取当前账本结束偏移量。

**返回：** `Long`

<div id="ledger_api.state.failed" />

### `ledger_api.state.failed`

调查失败的命令。

与状态（...，状态= CommandState.Failed）相同。

**参数**

* `commandId`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.state.help" />

### `ledger_api.state.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.state.status" />

### `ledger_api.state.status`

研究成功和失败的命令。

查找命令的状态。请注意，只会返回保存在内存中的最近命令。

**参数**

* `commandIdPrefix`: `String`
* `state`: `com.daml.ledger.api.v2.admin.command_inspection_service.CommandState`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.javaapi.state.help" />

### `ledger_api.javaapi.state.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.state.acs.active_contracts_of_party" />

### `ledger_api.state.acs.active_contracts_of_party`

列出给定方的有效合同集。

此命令将返回给定方当前的活动合同集。

支持的参数：* `party`: 为哪一方加载acs
* `limit`：限制（通过canton.parameter.console默认设置）
* `verbose`：结果事件是否应包含详细的类型信息
* `filterTemplate`：要过滤的模板 ID 列表，空序列充当通配符
* `filterInterfaces`：要过滤的接口 ID 列表，空序列不会影响结果过滤器
* `activeAtOffsetO`：计算活跃合约快照的偏移量，它必须不大于当前账本结束偏移量，并且必须大于或等于最后一次剪枝偏移量。如果未指定偏移量，则将使用当前参与者端。
* `timeout`：完整acs到达的最大等待时间
* `includeCreatedEventBlob`：结果是否应包含createdEventBlobs，仅当filterTemplate非空时才有效

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`

**返回：** `Seq[com.daml.ledger.api.v2.state_service.ActiveContract]`

<div id="ledger_api.state.acs.await_active_contract" />

### `ledger_api.state.acs.await_active_contract`

等待，直到该方在活动合同服务中看到给定的合同。

如果在给定的超时时间内未发现合约处于活动状态，将抛出异常

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `contractId`: `com.digitalasset.canton.protocol.LfContractId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="ledger_api.state.acs.find_generic" />

### `ledger_api.state.acs.find_generic`

合同的一般搜索。

此搜索函数返回一个无类型的 ledger-api 事件。 find 会一直等到合约出现，否则一旦超时就抛出异常。

**参数**

* `partyId`: `com.digitalasset.canton.拓扑.Party`
* `filter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry => Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry`

<div id="ledger_api.state.acs.help" />

### `ledger_api.state.acs.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.state.acs.incomplete_assigned_of_party" />

### `ledger_api.state.acs.incomplete_assigned_of_party`

列出给定方的一组不完整的分配事件。

此命令将返回给定方当前未完成的分配事件集。

支持的参数：

* `party`：你想为哪一方加载acs
* `limit`：限制（通过canton.parameter.console默认设置）
* `verbose`：结果事件是否应包含详细的类型信息
* `filterTemplate`：要过滤的模板 ID 列表，空序列充当通配符
* `filterInterfaces`：要过滤的接口 ID 列表，空序列不会影响结果过滤器
* `activeAtOffsetO`：计算事件快照的偏移量，它必须不大于当前账本结束偏移量，并且必须大于或等于最后一次剪枝偏移量。如果未指定偏移量，则将使用当前参与者端。
* `timeout`：完整acs到达的最大等待时间
* `includeCreatedEventBlob`：结果是否应包含createdEventBlobs，仅当filterTemplate非空时才有效

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedIncompleteAssigned]`

<div id="ledger_api.state.acs.incomplete_unassigned_of_party" />

### `ledger_api.state.acs.incomplete_unassigned_of_party`

列出给定方的一组不完整的未分配事件。

此命令将返回给定方当前的一组不完整的未分配事件。

支持的参数：

* `party`: 为哪一方加载acs
* `limit`：限制（通过canton.parameter.console默认设置）
* `verbose`：结果事件是否应包含详细的类型信息
* `filterTemplate`：要过滤的模板 ID 列表，空序列充当通配符
* `filterInterfaces`：要过滤的接口 ID 列表，空序列不会影响结果过滤器
* `activeAtOffsetO`：计算事件快照的偏移量，它必须不大于当前账本结束偏移量，并且必须大于或等于最后的剪枝偏移量。如果未指定偏移量，则将使用当前参与者端。
* `timeout`：完整acs到达的最大等待时间
* `includeCreatedEventBlob`：结果是否应包含createdEventBlobs，仅当filterTemplate非空时才有效

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedIncompleteUnassigned]`

<div id="ledger_api.state.acs.of_all" />

### `ledger_api.state.acs.of_all`

列出该参与者上托管的所有各方的有效合同集。

此命令将为所有各方返回当前的活动合同集。

支持的参数：

* `limit`：限制（通过canton.parameter.console默认设置）
* `verbose`：结果事件是否应包含详细的类型信息
* `filterTemplate`：要过滤的模板 ID 列表，空序列充当通配符
* `filterInterfaces`：要过滤的接口 ID 列表，空序列不会影响结果过滤器
* `activeAtOffsetO`：计算活跃合约快照的偏移量，它必须不大于当前账本结束偏移量，并且必须大于或等于最后一次剪枝偏移量。如果未指定偏移量，则将使用当前参与者端。
* `timeout`：完整acs到达的最大等待时间
* `identityProviderId`：限制对给定身份提供商管辖的各方的响应
* `includeCreatedEventBlob`：结果是否应包含createdEventBlobs，仅当filterTemplate非空时才有效
* `resultFilter`：结果的自定义过滤器，在限制之前应用

**参数**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `identityProviderId`: `String`
* `includeCreatedEventBlob`: `Boolean`
* `resultFilter`: `com.daml.ledger.api.v2.state_service.GetActiveContractsResponse => Boolean`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry]`

<div id="ledger_api.state.acs.of_party" />

### `ledger_api.state.acs.of_party`

列出给定方的有效合同条目集。

此命令将返回给定方当前的活动合同集和不完整的重新分配。

支持的参数：* `party`: 为哪一方加载acs
* `limit`：限制（通过canton.parameter.console默认设置）
* `verbose`：结果事件是否应包含详细的类型信息
* `filterTemplate`：要过滤的模板 ID 列表，空序列充当通配符
* `activeAtOffsetO`：计算活跃合约快照的偏移量，它不能大于当前账本结束偏移量，并且必须大于或等于最后一次剪枝偏移量。如果未指定偏移量，则将使用当前参与者端。
* `timeout`：完整acs到达的最大等待时间
* `includeCreatedEventBlob`：结果是否应包含createdEventBlobs，仅当filterTemplate非空时才有效
* `resultFilter`：结果的自定义过滤器，在限制之前应用

**参数**

* `party`: `com.digitalasset.canton.拓扑.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`
* `resultFilter`: `com.daml.ledger.api.v2.state_service.GetActiveContractsResponse => Boolean`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry]`

<div id="ledger_api.javaapi.state.acs.await" />

### `ledger_api.javaapi.state.acs.await`

等待合约变得可用并返回 Java codegen 合约。

此函数可用于具有代码生成的 Java 模型的合约。您可以使用 `filter` 函数参数优化搜索。您可以通过指定可选的同步器 ID 将搜索限制为同步器。该命令将等待合约出现，或者一旦超时则抛出异常。

**参数**

* `companion`: `com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T]`
* `partyId`: `com.digitalasset.canton.拓扑.Party`
* `predicate`: `TC => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `(companion: com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T])(partyId: com.digitalasset.canton.拓扑.Party, predicate: TC => Boolean, 同步器Filter: Option[com.digitalasset.canton.拓扑.同步器Id], timeout: com.digitalasset.canton.config.NonNegativeDuration): TC`

<div id="ledger_api.javaapi.state.acs.filter" />

### `ledger_api.javaapi.state.acs.filter`

过滤 ACS 以查找特定 Java 代码生成模板的合约。

要使用此功能，请确保存在目标模板的代码生成的 Java 模型。您可以使用 `predicate` 函数参数优化搜索。您可以通过指定可选的同步器 ID 将搜索限制为同步器。

**参数**

* `templateCompanion`: `com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T]`
* `partyId`: `com.digitalasset.canton.拓扑.Party`
* `predicate`: `TC => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

**退货：** `(templateCompanion: com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T])(partyId: com.digitalasset.canton.拓扑.Party, predicate: TC => Boolean, 同步器Filter: Option[com.digitalasset.canton.拓扑.同步器Id]): Seq[TC]`

<div id="ledger_api.javaapi.state.acs.help" />

### `ledger_api.javaapi.state.acs.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

#### 时间服务

<div id="ledger_api.time.get" />

### `ledger_api.time.get`

为参与者争取时间。

返回参与者的当前时间戳，可以是系统时钟或静态时间

**退货：** `com.digitalasset.canton.data.CantonTimestamp`

<div id="ledger_api.time.set" />

### `ledger_api.time.set`

设定参与者的时间。

如果参与者在静态时间模式下运行，则设置参与者时间

**参数**

* `currentTime`: `com.digitalasset.canton.data.CantonTimestamp`
* `nextTime`: `com.digitalasset.canton.data.CantonTimestamp`

#### 更新服务

<div id="ledger_api.updates.help" />

### `ledger_api.updates.help`特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.updates.重分配s" />

### `ledger_api.updates.重分配s`

获得重新分配。

此函数连接到给定各方和模板 ID 的更新流，并收集重新分配事件（已分配和未分配），直到收到 `completeAfter` 更新或 `timeout` 已过去。如果聚会 ID 集为空，则将获取所有聚会的重新分配。如果模板 ID 集合为空，则将获取所有模板 ID 的重新分配。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `partyIds`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `includeCreatedEventBlob`: `Boolean`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.重分配Wrapper]`

<div id="ledger_api.updates.start_measuring" />

### `ledger_api.updates.start_measuring`

开始测量更新服务的吞吐量。

该函数将代表`parties`订阅更新流并通知各种指标：指标`<name>.<metricSuffix>`计算发出的更新树的数量。指标 `<name>.<metricSuffix>-tx-node-count` 跟踪更新过程中发出的事件数量。指标`<name>.<metricSuffix>-tx-size`跟踪作为更新树的一部分发出的字节数。

要停止测量，需要关闭返回的`AutoCloseable`。使用 `onUpdate` 参数注册在每个更新树上调用的回调。

**参数**

* `parties`: `Set[com.digitalasset.canton.拓扑.Party]`
* `metricName`: `String`
* `onUpdate`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Unit`

**返回：** `AutoCloseable`

<div id="ledger_api.updates.subscribe_updates" />

### `ledger_api.updates.subscribe_updates`

订阅更新流。

该函数连接到更新流并将更新传递给`observer`，直到流完成。将返回更新格式中描述的更新。使用`EventFormat(Map(myParty.toLf -> Filters()))`返回`myParty: PartyId`的交易或重新分配。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `observer`: `io.grpc.stub.StreamObserver[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`

**退货：** `AutoCloseable`

<div id="ledger_api.updates.拓扑_transactions" />

### `ledger_api.updates.拓扑_transactions`

获取拓扑事务。此函数连接到给定方的更新流并收集拓扑事务事件，直到收到 `completeAfter` 更新或`timeout` 已过去。如果参与方 ID seq 为空，则将获取所有参与方的拓扑事务。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `partyIds`: `Seq[com.digitalasset.canton.拓扑.Party]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.拓扑TransactionWrapper]`

<div id="ledger_api.updates.transactions" />

### `ledger_api.updates.transactions`

获取交易。

此函数连接到给定各方的更新流并收集更新，直到收到`completeAfter`交易或`timeout`已过去。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果您需要指定模板 ID 的过滤条件并包括创建事件 blob 以进行显式披露，请考虑使用`tx_with_tx_format`。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `partyIds`: `Set[com.digitalasset.canton.拓扑.Party]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.TransactionWrapper]`

<div id="ledger_api.updates.transactions_with_tx_format" />

### `ledger_api.updates.transactions_with_tx_format`

获取更新。

此函数连接到给定交易格式的更新流并收集更新，直到收到`completeAfter`交易或`timeout`已过去。返回的交易可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果您只需要按一组各方进行过滤，请考虑使用`transactions`。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `transactionFormat`: `com.daml.ledger.api.v2.transaction_filter.TransactionFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.update_by_id" />

### `ledger_api.updates.update_by_id`

通过其 ID 获取更新。通过其 ID 获取更新。如果参与者（尚）不知道更新，或者由于更新格式而过滤了所有更新事件，或者如果更新已通过 `修剪.prune` 修剪，则返回 None。

**参数**

* `id`: `String`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`

**返回：** `Option[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.update_by_offset" />

### `ledger_api.updates.update_by_offset`

通过其偏移量获取更新。

通过其偏移量获取更新。如果参与者（尚）不知道更新，或者由于更新格式而过滤了更新的所有事件，或者如果更新已通过`修剪.prune`修剪，则返回 None。

**参数**

* `offset`: `Long`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`

**返回：** `Option[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.updates" />

### `ledger_api.updates.updates`

获取更新。

此函数连接到给定方的更新流并收集更新，直到收到 `completeAfter` 更新或 `timeout` 已过。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.javaapi.updates.help" />

### `ledger_api.javaapi.updates.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="ledger_api.javaapi.updates.transactions" />

### `ledger_api.javaapi.updates.transactions`

以 Java 绑定期望的格式获取事务。

此函数连接到给定各方的更新流并收集更新，直到收到`completeAfter`交易或`timeout`已过去。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果您需要指定模板 ID 的过滤条件并包括创建事件 blob 以进行显式披露，请考虑使用`tx_with_tx_format`。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `partyIds`: `Set[com.digitalasset.canton.拓扑.Party]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`

**返回：** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

<div id="ledger_api.javaapi.updates.transactions_with_tx_format" />

### `ledger_api.javaapi.updates.transactions_with_tx_format`

以 Java 绑定期望的格式获取事务。此函数连接到给定交易格式的更新流并收集更新，直到收到`completeAfter`交易或`timeout`已过去。返回的交易可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果您只需要按一组各方进行过滤，请考虑使用 `flat` 或 `trees` 代替。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `transactionFormat`: `com.daml.ledger.javaapi.data.TransactionFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`

**退货：** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

<div id="ledger_api.javaapi.updates.updates" />

### `ledger_api.javaapi.updates.updates`

以 Java 绑定期望的格式获取更新。

此函数连接到给定方的更新流并收集更新，直到收到 `completeAfter` 更新或 `timeout` 已过。返回的更新可以被过滤到给定的偏移量之间（默认：不过滤）。如果参与者已通过 `修剪.prune` 进行了修剪，并且 `beginOffset` 低于修剪偏移量，则此命令将失败并出现 `NOT_FOUND` 错误。如果 beginOffset 为零，则参与者 begin 被视为开始偏移。如果 endOffset 为 None，则返回连续流。

**参数**

* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `同步器Filter`: `Option[com.digitalasset.canton.拓扑.同步器Id]`

**退货：** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

### 账本修剪

<div id="修剪.clear_schedule_1" />

### `修剪.clear_schedule_1`

停用自动修剪。

<div id="修剪.find_safe_offset" />

### `修剪.find_safe_offset`

返回记录时间早于或等于给定时间（如果有）的最高参与者账本偏移量，在该时间点可以安全地进行修剪。

**参数**

* `beforeOrAt`: `java.time.Instant`

**退货：** `Option[Long]`

<div id="修剪.get_offset_by_time" />

### `修剪.get_offset_by_time`

根据指定的时间戳确定要修剪的参与者分类帐偏移量。

返回在指定时间戳之前或在指定时间戳处已处理的最大参与者分类帐偏移量。该时间是在参与者处理事件时的某个时刻在参与者的本地时钟上测量的。如果不存在这样的偏移量，则返回 `None`。

**参数**

* `upToInclusive`: `java.time.Instant`

**退货：** `Option[Long]`

<div id="修剪.get_参与方_schedule" />

### `修剪.get_参与方_schedule`

检查自动的、特定于参与者的修剪计划。

该计划由“cron”表达式以及“max\_duration”和“retention”持续时间组成，如`get_schedule`命令描述中所述。另外，“prune\_internally”指示调度是否要求修剪内部状态。

**返回：** `Option[com.digitalasset.canton.admin.api.client.data.参与方修剪Schedule]`

<div id="修剪.get_schedule" />

### `修剪.get_schedule`

检查自动修剪计划。

该计划由“cron”表达式和“max\_duration”和“retention”持续时间组成。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。如果尚未通过 `set_schedule` 配置计划或已调用 `clear_schedule`，则返回 `None`。**返回：** `Option[com.digitalasset.canton.admin.api.client.data.修剪Schedule]`

<div id="修剪.help_1" />

### `修剪.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="修剪.prune" />

### `修剪.prune`

将分类帐修剪到指定的偏移量（包含在内）。

将参与者账本修剪到指定的偏移量，如果账本已成功修剪，则返回`Unit`。请注意，成功修剪后，后续尝试通过 `ledger_api.transactions.flat` 或 `ledger_api.transactions.trees` 读取事务或通过指定低于返回的修剪偏移量的开始偏移量通过 `ledger_api.completions.list` 完成命令将导致 `NOT_FOUND` 错误。 `prune` 操作执行“完全修剪”，释放更多空间，并且如果 `pruneUpTo` 高于`find_safe_offset` 在修剪偏移之前发生事件的任何同步器上返回的偏移量，则还执行额外的安全检查，返回`NOT_FOUND` 错误。

**参数**

* `pruneUpTo`: `Long`

<div id="修剪.prune_internally" />

### `修剪.prune_internally`

仅修剪内部账本状态直至指定的偏移量（包含在内）。

`prune` 命令的特殊用途变体，仅修剪部分内部参与者账本状态，释放服务 `ledger_api.transactions` 和 `ledger_api.completions` 请求所需的空间。与 `prune` 结合使用，`prune_internally` 可以比通过账本 API 外部可观察的数据更积极地修剪内部账本状态。在大多数用例中，应改用`prune`。与 `prune` 不同，`prune_internally` 对 Ledger API 没有明显影响。如果分类帐已成功修剪，则该命令将返回 `Unit`；如果时间戳执行额外的安全检查，则返回一个错误，如果 `pruneUpTo` 高于在修剪偏移之前发生事件的任何同步器上的 `find_safe_offset` 返回的偏移量，则返回 `NOT_FOUND` 错误。

**参数**

* `pruneUpTo`: `Long`
* `safeToPruneCommitmentState`: `Option[com.digitalasset.canton.scheduler.SafeToPruneCommitmentState]`

<div id="修剪.set_cron" />

### `修剪.set_cron`

修改自动修剪使用的cron。

该计划以 cron 格式指定，指的是 GMT 时区的修剪开始时间。如果没有通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `cron`: `String`

<div id="修剪.set_max_duration" />

### `修剪.set_max_duration`

修改自动修剪使用的最大持续时间。

`maxDuration` 被指定为正持续时间并且最多具有每秒粒度。如果没有通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_参与方_schedule" />

### `修剪.set_参与方_schedule`

根据指定的时间表和参与者特定的选项激活自动修剪。

有关“cron”、“max\_duration”和“retention”参数的信息，请参阅`set_schedule`描述。设置“prune\_internally\_only”标志会导致修剪仅删除内部状态，如`prune_internally`命令描述中更详细地描述。

**参数**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `pruneInternallyOnly`: `Boolean`

<div id="修剪.set_retention" />

### `修剪.set_retention`

更新自动修剪使用的修剪保留。`retention` 被指定为正持续时间并且最多具有每秒粒度。如果未通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在此更新时，修剪正在主动运行，则会尽力暂停修剪并以新指定的保留重新启动。这允许新的保留要求保留比以前更多的数据。

**参数**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_schedule_1" />

### `修剪.set_schedule_1`

根据指定的时间表激活自动修剪。

该计划以 cron 格式以及“max\_duration”和“retention”持续时间指定。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。

**参数**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

### 指标

<div id="metrics.get" />

### `metrics.get`

获取特定指标。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point" />

### `metrics.get_double_point`

获得特定的双倍积分。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram" />

### `metrics.get_histogram`

获取特定的直方图。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**退货：** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point" />

### `metrics.get_long_point`

获得一个特定的长点。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary" />

### `metrics.get_summary`

获得具体的总结。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list" />

### `metrics.list`

列出所有指标。

返回具有给定名称和可选匹配属性的指标。

**参数**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**退货：** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

## 多个参与者

本节列出了一系列参与者可用的命令。它们可用于参与者参考`参与方s.all`、`.local` 或`.remote`，如下所示：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
参与方s.all.dars.upload("my.dar")
```

<div id="help_4"/>

### `help_4`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="dars.help_1" />

### `dars.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="dars.upload_1" />

### `dars.upload_1`

将 DAR 上传给参与者。

如果设置了同步器Id，参与者将审查指定同步器上的包。如果synchronizeVetting为true，则该命令将阻塞，直到包审查事务已在所有连接的同步器中注册。

**参数*** `darPath`: `String`
* `description`: `String`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `expectedMainPackageId`: `String`
* `requestHeaders`: `Map[String,String]`

**返回：** `Map[com.digitalasset.canton.console.参与方Reference,String]`

<div id="dars.upload_many_1" />

### `dars.upload_many_1`

将 DAR 上传给参与者。

如果设置了同步器Id，参与者将审查指定同步器上的包。如果synchronizeVetting为true，则该命令将阻塞，直到包审查事务已在所有连接的同步器中注册。

**参数**

* `paths`: `Seq[String]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `requestHeaders`: `Map[String,String]`
* `logger`: `com.digitalasset.canton.logging.TracedLogger`

**退货：** `Map[com.digitalasset.canton.console.参与方Reference,Seq[String]]`

<div id="dars.validate_1" />

### `dars.validate_1`

根据当前参与者的状态验证 DAR。

执行与上传调用执行的相同的 DAR 和 Daml 包验证检查，但对目标参与者没有影响：DAR 未保留或审查。

**参数**

* `darPath`: `String`

**返回：** `Map[com.digitalasset.canton.console.参与方Reference,String]`

<div id="同步器s.connect_2" />

### `同步器s.connect_2`

连接到同步器。

**参数**

* `config`: `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="同步器s.connect_local_1" />

### `同步器s.connect_local_1`

注册并可能连接到新的本地同步器。

论据是：

* `sequencer`：本地定序器引用别名 - 用于注册此连接的同步器别名。
* `manualConnect`：此连接是否应该手动处理，并且也排除在自动重新连接之外。
* `physical同步器Id`：可选的同步器 ID，以确保连接到正确的同步器。
* `synchronize`：超时时间，指示等待所有拓扑更改在所有本地节点上生效的时间。

**参数**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.同步器Alias`
* `manualConnect`: `Boolean`
* `physical同步器Id`: `Option[com.digitalasset.canton.拓扑.Physical同步器Id]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="同步器s.disconnect_1" />

### `同步器s.disconnect_1`

与同步器断开。

**参数**

* `alias`: `com.digitalasset.canton.同步器Alias`

<div id="同步器s.disconnect_all_1" />

### `同步器s.disconnect_all_1`

断开所有连接的同步器。

<div id="同步器s.help_1" />

### `同步器s.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="同步器s.reconnect_1" />

### `同步器s.reconnect_1`

重新连接同步器。

如果重试设置为 true（默认），该命令将在第一次尝试后返回，但会在后台继续尝试。

**参数**

* `alias`: `com.digitalasset.canton.同步器Alias`
* `retry`: `Boolean`

<div id="同步器s.reconnect_all_1" />

### `同步器s.reconnect_all_1`

重新连接到 `manualStart` = false 的所有同步器。

如果ignoreFailures设置为true（默认），即使某些同步器离线，重新连接也会成功。参与者将继续尝试建立同步器连接。

**参数**

* `ignoreFailures`: `Boolean`

<div id="同步器s.register_1" />

### `同步器s.register_1`

注册同步器。

**参数**

* `config`: `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`
* `performHandshake`: `Boolean`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

### 套餐

<div id="packages.find_by_module" />

### `packages.find_by_module`

查找包含具有给定名称的模块的包。

**参数**

* `moduleName`: `String`
* `limitPackages`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.PackageDescription]`

<div id="packages.get_contents" />

### `packages.get_contents`

获取包装内容。

**参数**

* `packageId`: `String`

**返回：** `com.digitalasset.canton.admin.api.client.data.PackageDescription.PackageContents`

<div id="packages.get_references" />

### `packages.get_references`

返回引用给定包的 DAR 列表。

**参数**

* `packageId`: `String`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.DarDescription]`

<div id="packages.help" />

### `packages.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="packages.list" />

### `packages.list`

列出参与者上存储的包。

支持的参数：

limit - 返回包裹数量的限制（默认为 canton.parameters.console.default-limit）

**参数**

* `filterName`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.PackageDescription]`

<div id="packages.remove" />

### `packages.remove`

从 Canton 的包裹商店中取出包裹。

此命令的标准操作检查包是否未使用且未经审查，如果是，则删除该包。强制标志可用于禁用检查，但不要使用强制标志，除非您确定自己知道自己在做什么。

**参数**

* `packageId`: `String`
* `force`: `Boolean`

<div id="packages.synchronize_vetting" />

### `packages.synchronize_vetting`

确保所有配置的参与者都观察到该参与者发出的所有审核交易。

有时，在编写测试和演示脚本时，会上传 dar 或包，我们需要确保仅在控制台已知的其他连接参与者观察到包审查后才提交命令。在这种情况下可以使用该命令。

**参数**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

### 政党管理

参与方管理命令允许方便地启用和禁用本地节点上的参与方。在幕后，他们使用更复杂但功能更丰富的身份管理命令。

<div id="partys.add_party_async" />

### `parties.add_party_async`

将先前存在的一方添加到本地参与者。

开始将先前存在的参与方添加到指定同步器上的此参与者。同步执行一些检查，然后异步启动方复制。返回的`addPartyRequestId`参数允许识别异步进度和错误。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `source参与方`: `com.digitalasset.canton.拓扑.参与方Id`
* `serial`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `参与方Permission`: `com.digitalasset.canton.topology.transaction.参与方Permission`

**退货：** `String`

<div id="partys.clear_party_入驻_flag" />

### `parties.clear_party_入驻_flag`

清除一方的加入标志。

指示参与者单方面清除参与方到参与者拓扑映射上的“加入”标志。

此操作具有时间敏感性。如果运行得太快，则无法安全地清除该标志，并且需要进行另一次尝试。

该端点是幂等的，可以安全地多次调用。轮询是必要的，因为该标志只能在经过特定时间后才能被清除，并且底层的更改可能需要一段时间才能生效。

先决条件：必须存在先前的参与方到参与者映射拓扑事务，该事务可以激活参与者上的参与方，并将加入标志设置为 true。

返回具有当前状态的元组：

* `Cleared`: (true, None) – 标志已成功清除。
* `Pending`: (false, Some(timestamp)) – 标志仍然设置。时间戳表示清除标志的最早安全时间。您可以等到这个时间之后再次运行该命令。

论据是：* `party`：正在加入的一方，它必须已经在参与者上处于活动状态。
* `同步器Id`：限制参与方加入给定的同步器。
* `beginOffsetExclusive`：独家账本偏移量，用作在参与者上查找该方激活的起点。
* `waitForActivationTimeout`：服务等待找到激活该方的拓扑事务的最大持续时间。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `beginOffsetExclusive`: `Long`
* `waitForActivationTimeout`: `Option[com.digitalasset.canton.config.NonNegativeFiniteDuration]`

**返回：** `(Boolean, Option[com.digitalasset.canton.data.CantonTimestamp])`

<div id="partys.disable" />

### `parties.disable`

禁用参与者的聚会。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `同步器`: `Option[com.digitalasset.canton.同步器Alias]`

<div id="party.enable" />

### `parties.enable`

启用/添加一方到参与者。

此函数在同步器上向参与者命名空间中的当前参与者注册一个新方。如果参与者没有适当的签名密钥来发出相应的 PartyTo参与方 拓扑事务，或者参与者未连接到任何同步器，则该功能将失败。如果参与者仅连接到一个同步器，则不必指定同步器参数。如果参与者连接到多个同步器，则需要在每个同步器上显式启用该方。此外，可以添加一系列附加参与者进行同步，以确保在功能终止之前这些参与者也知道该方。

**参数**

* `name`: `String`
* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `同步器`: `Option[com.digitalasset.canton.同步器Alias]`
* `synchronize参与方s`: `Seq[com.digitalasset.canton.console.参与方Reference]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**返回：** `com.digitalasset.canton.拓扑.PartyId`

<div id="partys.export_party_acs" />

### `parties.export_party_acs`

为给定方导出有效合同以复制它。

此命令导出给定方的当前活动合同集 (ACS)，以便于将其从源参与者复制到目标参与者。

它使用该方在目标参与者上的最新激活来确定要从源参与者导出的 ACS 的精确历史状态。

目标参与者上的“激活”意味着新的托管安排已由该方本身和目标参与者通过各方到参与者的拓扑事务授权。

如果目标参与者上尚未激活该方，则此命令将失败。

成功完成后，该命令将写入 GZIP 压缩的 ACS 快照文件。然后应使用 `import_party_acs` 命令将该文件导入到目标参与者的 ACS 中。

论据是：

* `party`：被复制的一方，必须已经在目标参与者上处于活动状态。
* `同步器Id`：限制导出到给定的同步器。
* `target参与方Id`：将复制队伍的目标参与者的唯一标识符。
* `beginOffsetExclusive`：独家账本偏移量，用作在目标参与者上查找该方激活的起点。
* `exportFilePath`：ACS快照存储文件的路径。
* `waitForActivationTimeout`：服务等待找到在目标参与者上激活该方的拓扑事务的最大持续时间。
* `timeout`：此操作完成的超时。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `target参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `beginOffsetExclusive`: `Long`
* `exportFilePath`: `String`
* `waitForActivationTimeout`: `Option[com.digitalasset.canton.config.NonNegativeFiniteDuration]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="party.find" />

### `parties.find`

从过滤字符串中查找一方。将搜索与此过滤字符串匹配的所有各方。如果它恰好找到一方，它将返回该一方。否则，该函数将抛出异常。

**参数**

* `filterParty`: `String`

**返回：** `com.digitalasset.canton.拓扑.PartyId`

<div id="partys.find_highest_offset_by_timestamp" />

### `parties.find_highest_offset_by_timestamp`

按时间戳查找最大账本偏移量。

此命令尝试在属于同步器的所有事件中找到最高的分类帐偏移量，这些事件的记录时间早于给定时间戳或在给定时间戳处。

返回最高的账本偏移量，或返回错误。

可能的故障原因：

* 请求的时间戳距过去太远，不再存在任何事件。
* 给定同步器没有事件。
* 在请求的时间戳之前，并非所有事件都已完全处理和/或发布到 Ledger API DB。

根据失败原因，可以尝试此命令来获取账本偏移量。例如，如果并非所有事件都已完全处理和/或发布到 Ledger API DB，则重试是有意义的。

论据是：

* `同步器Id`：限制对特定同步器的查询。
* `timestamp`：一个时间点。
* `force`：默认为 false。如果为 true，则返回当前已知的最高账本偏移量，记录时间早于给定时间戳或给定时间戳。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `timestamp`: `java.time.Instant`
* `force`: `Boolean`

**返回：** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="partys.find_party_max_activation_offset" />

### `parties.find_party_max_activation_offset`

查找一方的最高激活偏移量。

此命令查找一方的激活与指定条件匹配的最高账本偏移量。

它在账本中搜索拓扑事务，由给定的同步器 (`同步器Id`) 排序，导致该方 (`partyId`) 新托管在参与者 (`参与方Id`) 上。可选的`validFrom`时间戳过滤拓扑事务的有效时间。

账本搜索发生在指定的偏移范围内，针对特定数量的拓扑交易（`completeAfter`）。

如果 `beginOffsetExclusive` 为默认值，则搜索从分类帐开始处开始。如果参与者被剪枝并且 `beginOffsetExclusive` 低于剪枝偏移量，则会发生 `NOT_FOUND` 错误。在所需拓扑交易附近但之前使用`beginOffsetExclusive`。

如果`endOffsetInclusive`未设置（`None`），则搜索将继续，直到找到`completeAfter`数量的交易或`timeout`过期。否则，分类帐搜索将在指定的偏移量处结束。

此命令对于使用 `export_acs` 创建 ACS 快照非常有用，这需要参与方激活分类帐偏移量。

论据是：

* `partyId`：寻找激活的一方。
* `参与方Id`：主持新聚会的参与者。
* `同步器Id`：同步器对激活进行排序。
* `validFrom`：激活的有效时间（默认：无）。
* `beginOffsetExclusive`：起始账本偏移量（默认：0）。
* `endOffsetInclusive`：结束账本偏移量（默认值：None = 尾随搜索）。
* `completeAfter`：要查找的交易数量（默认：最大=无限制）。
* `timeout`：搜索超时（默认：1 分钟）。

**参数**

* `partyId`: `com.digitalasset.canton.拓扑.PartyId`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `validFrom`: `Option[java.time.Instant]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="partys.find_party_max_deactivation_offset" />

### `parties.find_party_max_deactivation_offset`

查找一方的最高停用偏移量。

此命令查找一方的停用符合指定条件的最高账本偏移量。

它在账本中搜索拓扑事务，由给定的同步器 (`同步器Id`) 排序，导致该方 (`partyId`) 在参与者 (`参与方Id`) 上被撤销。可选的`validFrom`时间戳过滤拓扑事务的有效时间。账本搜索发生在指定的偏移范围内，针对特定数量的拓扑交易（`completeAfter`）。

如果 `beginOffsetExclusive` 是默认值，则搜索从分类帐开始处开始。如果参与者被剪枝并且 `beginOffsetExclusive` 低于剪枝偏移量，则会发生 `NOT_FOUND` 错误。在所需拓扑交易附近但之前使用`beginOffsetExclusive`。

如果`endOffsetInclusive`未设置（`None`），则搜索将继续，直到找到`completeAfter`数量的交易或`timeout`过期。否则，分类帐搜索将在指定的偏移量处结束。

此命令对于在账本偏移量中查找一方已从参与者中退出的活动合约非常有用。

论据是：

* `partyId`：寻找停用的一方。
* `参与方Id`：主持新聚会的参与者。
* `同步器Id`：同步器对停用进行排序。
* `validFrom`：停用的有效时间（默认：无）。
* `beginOffsetExclusive`：起始账本偏移量（默认值：0）。
* `endOffsetInclusive`：结束账本偏移量（默认值：None = 尾随搜索）。
* `completeAfter`：要查找的交易数量（默认：最大=无限制）。
* `timeout`：搜索超时（默认：1 分钟）。

**参数**

* `partyId`: `com.digitalasset.canton.拓扑.PartyId`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `validFrom`: `Option[java.time.Instant]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="partys.get_add_party_status" />

### `parties.get_add_party_status`

获取待处理的 `add_party_async` 呼叫的状态。

通过指定先前返回的 `addPartyRequestId` 参数，检索先前通过 `add_party_async` 端点添加的一方的状态信息。

**参数**

* `addPartyRequestId`: `String`

**退货：** `com.digitalasset.canton.admin.api.client.data.AddPartyStatus`

<div id="partys.help" />

### `parties.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="party.hosted" />

### `parties.hosted`

列出该参与者主持的聚会。

检查该参与者主持的用于同步的各方。响应是根据每个同步器的带时间戳的拓扑事务构建的，不包括给定节点的授权存储。搜索将包括所有托管方，相当于使用调用参与者的参与者 ID 运行 `list` 方法。

filterParty：按以给定字符串开头的各方进行过滤。 filter同步器Id：按 id 以给定字符串开头的同步器进行过滤。 asOf：可选时间戳，用于检查给定时间点的拓扑状态。 limit：返回多少个项目（默认为canton.parameters.console.default-limit）

示例：参与方1.partys.hosted(filterParty="alice")

**参数**

* `filterParty`: `String`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListPartiesResult]`

<div id="partys.import_party_acs" />

### `parties.import_party_acs`

从快照文件导入活动合同以复制一方。

此命令将合同从活动合同集 (ACS) 快照文件导入到参与者的 ACS 中。它期望给定的 ACS 快照文件是先前 `export_party_acs` 命令调用的结果。

论据是：* `importFilePath`：表示从中读取 ACS 快照的文件的路径。未定义时默认为“canton-acs-export.gz”。
* `workflowIdPrefix`：为工作流ID设置自定义前缀，以便轻松识别本次导入生成的所有事务。未指定时默认为“import-\<random\_UUID>”。
* `contractImportMode`：管理导入时的合同认证处理。选项包括验证（默认）、\[接受、重新计算]。
* `representativePackageIdOverride`：定义覆盖映射，用于在 ACS 导入时将代表性包 ID 分配给合同。未定义时默认为 NoOverride。

**参数**

* `importFilePath`: `String`
* `workflowIdPrefix`: `String`
* `contractImportMode`: `com.digitalasset.canton.参与方.admin.data.ContractImportMode`
* `representativePackageIdOverride`: `com.digitalasset.canton.参与方.admin.data.RepresentativePackageIdOverride`

<div id="partys.list" />

### `parties.list`

列出活跃方、其活跃参与者以及参与者对同步器的权限。

检查该参与者已知的用于同步的各方。响应是根据每个同步器的带时间戳的拓扑事务构建的，不包括给定节点的授权存储。对于每个已知方，给出了活动参与者的列表以及他们对该方的同步器的许可。

filterParty：按以给定字符串开头的各方进行过滤。 filter参与方：筛选由 id 以给定字符串开头的参与者托管的各方。 filter同步器Id：按 id 以给定字符串开头的同步器进行筛选。 asOf：可选时间戳，用于检查给定时间点的拓扑状态。 limit：获取的参与方数量限制（默认为 canton.parameters.console.default-limit）。

示例：参与方1.partys.list(filterParty="alice")

**参数**

* `filterParty`: `String`
* `filter参与方`: `String`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListPartiesResult]`

### 参与者修复

<div id="repair.add" />

### `repair.add`

将指定合约添加到参与者上的特定同步器。

这是从数据损坏中恢复的最后手段命令，例如在参与者合约以某种方式不同步并且需要手动创建的场景中。参与者需要在调用时断开与指定“同步器”的连接，并且到目前为止，同步器不能有任何正在进行的请求。该命令的效果将在重新连接到同步同步器时生效。由于修复命令是从不可预见的数据损坏中恢复的强大工具，但在正常操作下很危险，因此使用此命令需要（暂时）启用“features.enable-repair-commands”配置。此外，修复命令可以运行无限时间，具体取决于传入的合约数量。请确保在调用返回之前不要将参与者连接到同步器。

论据是：

* `同步器Id`：要添加合约的同步器的id
* `protocolVersion`：同步器使用的协议版本
* `contracts`：添加见证人信息的合约列表

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `contracts`: `Seq[com.digitalasset.canton.参与方.admin.data.RepairContract]`
* `allowContractIdSuffixRecomputation`: `Boolean`

**返回：** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.change_assignation" />

### `repair.change_assignation`

将合约分配从一个同步器更改为另一个同步器。这是在同步器发生不可挽回的损坏并且以前连接的参与者需要将合约分配更改为另一个健康的同步器的情况下从数据损坏中恢复的最后手段命令。参与者需要断开与“source同步器”和“target同步器”的连接。目标同步器不能有任何正在进行的请求。已分配给目标同步器的合约将被跳过，这使得可以以“幂等”方式调用此命令，以防早期尝试导致错误。 “skipInactive”标志使得只能更改“source同步器”中活动合约的分配成为可能。由于修复命令是从不可预见的数据损坏中恢复的强大工具，但在正常操作下很危险，因此使用此命令需要（暂时）启用“features.enable-repair-commands”配置。此外，修复命令可以运行无限时间，具体取决于传入的合约 ID 的数量。请确保在调用返回之前不要将参与者连接到任一同步器。

论据：

* 合约ID
* 一组应将分配更改为新同步器的合约 ID
* 源同步器别名
* 源同步器的别名
* 目标同步器别名
* 目标同步器的别名
* 重新分配CounterOverride
* 默认情况下，在更改分配过程中，重新分配计数器会加一，如果需要强制重新分配计数器的值，可以在map中传递新值
*skipInactive-（默认true）是否跳过contractIds列表中提到的非活动合约

**参数**

* `contractsIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `target同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `重分配CounterOverride`: `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.重分配Counter]`
* `skipInactive`: `Boolean`

<div id="repair.export_acs" />

### `repair.export_acs`

将给定各方的有效合同导出到文件中。

此命令将给定各方的当前活动合同集 (ACS) 导出到 GZIP 压缩的 ACS 快照文件。之后，`import_acs`修复命令再次将其导入参与者的ACS中。

论据是：

* `parties`：识别给定集合中至少有一个利益相关者的合约。
* `ledgerOffset`：ACS快照导出的偏移量。
* `exportFilePath`：ACS快照存储文件的路径。
* `excludedStakeholders`：定义后，任何有一个或多个参与方作为利益相关者的合约都将从 ACS 快照中删除。
* `同步器Id`：定义后，限制导出到给定的同步器。
* `contract同步器Renames`：根据映射将合约的关联同步器ID从一个同步器更改为另一个同步器。
* `timeout`：此操作完成的超时。

**参数**

* `parties`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `ledgerOffset`: `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`
* `exportFilePath`: `String`
* `excludedStakeholders`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `contract同步器Renames`: `Map[com.digitalasset.canton.拓扑.同步器Id,com.digitalasset.canton.拓扑.同步器Id]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="repair.export_acs_old" />

### `repair.export_acs_old`

将给定各方的有效合同导出到文件中。 （已弃用）。

此命令将给定各方的当前活动合同集 (ACS) 导出到 ACS 快照文件。之后，“import\_acs\_old”命令允许将其再次导入参与者的 ACS。此类 ACS 导出（和导入）仅对恢复和操作目的有意义。

请注意，“export\_acs\_old”命令执行可能需要很长时间才能完成，并且可能需要大量资源。

弃用通知：未来版本将删除此命令，请改用 `export_acs`。

论据是：* `parties`：识别给定集合中至少有一个利益相关者的合约。如果为空，则导出各方的合同。
* `partiesOffboarding`：如果各方将被下线（各方迁移），则为 true
* `outputFile`：存储数据的输出文件名。
* `filter同步器Id`：限制导出到给定的同步器
* `timestamp`：可选的我们应该获取状态的时间戳（对于协调同步器的状态很有用）
* `contract同步器Renames`：作为导出的一部分，允许根据映射将合约的关联同步器 ID 从一个同步器重命名为另一个同步器。
* `force`：如果设置为true，则不会检查时间戳是否干净。为了使用此选项生成一致的快照，您需要在上次提交的请求之后至少等待确认响应超时 + mediatorReactionTimeout。

**参数**

* `parties`: `Set[com.digitalasset.canton.拓扑.PartyId]`
* `partiesOffboarding`: `Boolean`
* `outputFile`: `String`
* `filter同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `timestamp`: `Option[java.time.Instant]`
* `force`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="repair.help_1" />

### `repair.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="repair.ignore_events" />

### `repair.ignore_events`

将排序事件标记为忽略。

这是忽略参与者无法处理的事件的最后手段。忽略事件可能会导致后续失败，例如，如果创建合约的事件被忽略并且随后使用该合约。如果其他参与者仍然处理被忽略的事件，也可能导致账本分叉。可以将参与者尚未收到的事件标记为已忽略。

如果将 `fromInclusive` 和 `toInclusive` 之间的事件标记为忽略会导致排序器计数器出现间隙，即如果 `from <= to` 和 `from` 大于 `maxSequencerCounter + 1`，其中 `maxSequencerCounter` 是底层参与者存储的排序事件的最大排序器计数器，则该命令将失败。

如果 `force == false` 和 `from` 小于已标记为干净的最后一个事件的序列计数器，该命令也会失败。 （忽略此类事件通常不会产生任何影响，因为它们已经被处理。）

**参数**

* `physical同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`
* `fromInclusive`: `com.digitalasset.canton.SequencerCounter`
* `toInclusive`: `com.digitalasset.canton.SequencerCounter`
* `force`: `Boolean`

<div id="repair.import_acs" />

### `repair.import_acs`

从活动合同集 (ACS) 快照文件导入活动合同。

此命令将合同从 ACS 快照文件导入到参与者的 ACS 中。它期望给定的 ACS 快照文件是先前 `export_acs` 命令调用的结果。

在开始流程之前可以检查导入合同的合同 ID。如果任何合约 ID 与分配合约的同步器关联的合约 ID 方案不匹配，则整个导入过程将失败，具体取决于 `contractImportMode` 的值。

默认情况下，`contractImportMode` 设置为 `ContractImportMode.Validation`。如果设置为`ContractImportMode.Recomputation`，任何未通过上述检查的合约ID都将被重新计算。请注意，在以下情况下，合约 ID 的重新计算将失败：

* 用于计算合约ID的合约盐缺失
* 合约ID鉴别器版本未知

请注意，仅会重新计算特定于Canton的合同 ID 后缀。鉴别器无法重新计算，将保持原样。

重新计算不会对某些导入合约的有效负载中引用的合约 ID 执行，但在导入本身中缺失（这应该意味着合约已存档，这使得重新计算变得不必要）。

仅限专家：由于合约 ID 的验证或重新计算可能会显着延长导入时间，因此您可以选择简单地接受合约 ID，因为它们正在使用 `ContractImportMode.Accept`。如果导入过程成功，将返回从旧合约 ID 到新合约 ID 的映射。空映射意味着所有合约 ID 都是有效的，或者已按原样接受，并且没有重新计算合约 ID。

论据是：

* `importFilePath`：表示从中读取 ACS 快照的文件的路径。未定义时默认为“canton-acs-export.gz”。
* `workflowIdPrefix`：为工作流ID设置自定义前缀，以便轻松识别本次导入生成的所有事务。未指定时默认为“import-\<random\_UUID>”。
* `contractImportMode`：管理导入时的合同认证处理。选项包括验证（默认）、\[接受、重新计算]。
* `representativePackageIdOverride`：定义覆盖映射，用于在 ACS 导入时将代表性包 ID 分配给合同。
* `excludedStakeholders`：定义后，导入时将忽略其中一个或多个参与方作为利益相关者的任何合同。

**参数**

* `importFilePath`: `String`
* `workflowIdPrefix`: `String`
* `contractImportMode`: `com.digitalasset.canton.参与方.admin.data.ContractImportMode`
* `representativePackageIdOverride`: `com.digitalasset.canton.参与方.admin.data.RepresentativePackageIdOverride`
* `excludedStakeholders`: `Set[com.digitalasset.canton.拓扑.PartyId]`

**退货：** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.import_acs_old" />

### `repair.import_acs_old`

从活动合同集 (ACS) 快照文件导入活动合同。 （已弃用）。

此命令将合同从 ACS 快照文件导入到参与者的 ACS 中。给定的 ACS 快照文件必须是先前“export\_acs\_old”命令调用的结果文件。

在开始流程之前将检查导入合同的合同 ID。如果任何合约 ID 与分配合约的同步器关联的合约 ID 方案不匹配，则整个导入过程将失败，具体取决于 `allowContractIdSuffixRecomputation` 的值。

默认情况下，`allowContractIdSuffixRecomputation` 设置为 `false`。如果设置为`true`，任何未通过上述检查的合约ID都将被重新计算。请注意，在以下情况下，合约 ID 的重新计算将失败：

* 用于计算合约ID的合约盐缺失
* 合约ID鉴别器版本未知

请注意，仅会重新计算特定于Canton的合同 ID 后缀。鉴别器无法重新计算，将保持原样。

重新计算不会对某些导入合约的有效负载中引用的合约 ID 执行，但在导入本身中缺失（这应该意味着合约已存档，这使得重新计算变得不必要）。

如果导入过程成功，将返回从旧合约 ID 到新合约 ID 的映射。空映射意味着所有合约 ID 均有效，并且没有重新计算合约 ID。

弃用通知：未来版本将删除此命令，请改用 `export_acs`。

**参数**

* `inputFile`: `String`
* `workflowIdPrefix`: `String`
* `allowContractIdSuffixRecomputation`: `Boolean`

**退货：** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.migrate_同步器" />

### `repair.migrate_同步器`

将合约从一个同步器迁移到另一个同步器。

将与同步器关联的所有合约迁移到新的同步器。此方法将注册新的同步器，连接到它，然后将所有合约从源同步器重新关联到目标同步器。请注意，此迁移需要所有参与者同时完成。仅当所有参与者完成迁移后才应使用目标同步器。

警告：如果源同步器上存在正在进行的事务，则迁移不会启动。强制迁移可能会导致账本分叉！不要强制迁移，而是通过将所有参与者重新连接到源同步器、停止这些参与者上的活动并等待正在进行的事务完成或超时来确保源同步器没有正在进行的事务。强制迁移旨在当源同步器无法再恢复时实现灾难恢复。参数为： source：源同步器的同步器别名 target：目标同步器的配置 force：如果为 true，则强制迁移忽略正在进行的事务。默认为 false。

**参数**

* `source`: `com.digitalasset.canton.同步器Alias`
* `target`: `com.digitalasset.canton.参与方.同步器.同步器ConnectionConfig`
* `force`: `Boolean`

<div id="repair.purge" />

### `repair.purge`

从本地参与者中清除具有指定合约 ID 的合约。

这是从数据损坏中恢复的最后手段命令，例如在参与者合同以某种方式不同步并需要手动清除的情况下，或者在利益相关者不再同意其存档的情况下。参与者需要在调用时断开与具有“contractIds”的合约所在的同步器的连接，并且到目前为止，同步器不能有任何正在进行的请求。该命令的效果将在重新连接到同步器时生效。 “ignoreAlreadyPurged”标志使得可以使用相同的参数多次调用该命令，以防先前的命令调用失败。由于修复命令是从不可预见的数据损坏中恢复的强大工具，但在正常操作下很危险，因此使用此命令需要（暂时）启用“features.enable-repair-commands”配置。此外，修复命令可以运行无限时间，具体取决于传入的合约 ID 的数量。请确保在调用返回之前不要将参与者连接到同步器。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `ignoreAlreadyPurged`: `Boolean`

<div id="repair.purge_deactivated_同步器" />

### `repair.purge_deactivated_同步器`

清除已停用同步器的数据。

此命令删除同步器数据，并有助于确保指定的已停用同步器中的陈旧数据不再起作用。指定的同步器需要处于`Inactive`状态才能进行清除。清除停用的同步器通常是通过 `repair.migrate_同步器` 作为硬同步器迁移的一部分自动执行的。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`

<div id="repair.rollback_取消分配" />

### `repair.rollback_取消分配`

通过将合约重新分配给源同步器来回滚取消分配。

这是从无法在目标同步器上完成的取消分配中恢复的最后手段命令。论据：

* 重新分配ID
* 应将分配更改为新同步器的合约 ID 集
* 来源
* 源同步器id
* 目标
* 目标同步器的别名

**参数**

* `重分配Id`: `String`
* `source`: `com.digitalasset.canton.拓扑.同步器Id`
* `target`: `com.digitalasset.canton.拓扑.同步器Id`

<div id="repair.unignore_events" />

### `repair.unignore_events`

从排序事件中删除忽略状态。

该命令对普通（即不被忽略）事件和不存在的事件没有影响。

如果将 `fromInclusive` 和 `toInclusive` 之间的事件标记为未忽略会导致定序器计数器出现间隙，即，如果在 `from` 和 `to` 之间存在一个定序器计数器为空的被忽略事件，而另一个定序器计数器大于 `to` 的空被忽略事件，则该命令将会失败。空的忽略事件是已被标记为忽​​略且参与者尚未接收到的事件。

如果 `force == false` 和 `from` 小于已标记为干净的最后一个事件的序列计数器，该命令也会失败。 （忽略此类事件通常不会产生任何影响，因为它们已经被处理。）

**参数**

* `physical同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`
* `fromInclusive`: `com.digitalasset.canton.SequencerCounter`
* `toInclusive`: `com.digitalasset.canton.SequencerCounter`
* `force`: `Boolean`

### 复制

<div id="replication.help" />

### `replication.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="replication.set_passive" />

### `replication.set_passive`将参与者副本设置为被动。

触发从该主动副本到另一个被动副本的正常故障转移。该命令在副本有机会变为活动状态后完成。执行此命令后，您需要检查此副本的运行状况以确保它不再处于活动状态。

### 资源管理

<div id="resources.help" />

### `resources.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="resources.resource_limits" />

### `resources.resource_limits`

获取参与者的资源限制。

**返回：** `com.digitalasset.canton.参与方.admin.ResourceLimits`

<div id="resources.set_resource_limits" />

### `resources.set_resource_limits`

为参与者设置资源限制。

当达到或超过资源限制时，参与者将拒绝任何额外的提交，并且 GRPC 状态为 ABORTED。最重要的是，提交将在消耗大量资源之前被拒绝。

限制分为三种：`maxInflightValidationRequests`、`maxSubmissionRate`、`maxSubmissionBurstFactor`。参与者P的飞行验证请求数涵盖（1）P发起的请求以及（2）除P之外的参与者发起的需要P验证的请求。与最大速率相比，最大飞行验证请求数更准确地反映了参与者的负载。然而，仅飞行验证请求的最大数量并不能保护系统免受“突发”的影响：如果应用程序一次提交大量命令，则可能会超过飞行验证请求的最大数量，因为系统仅在验证期间注册飞行验证请求，而不是在提交期间注册。

最大速率是通过 Ledger API 提交给该参与者的命令速率的硬性限制。由于在收到新的命令提交后会立即检查并更新命令的速率，因此应用程序不能超过最大速率。

`maxSubmissionBurstFactor` 参数（正值，默认 0.5）允许配置对于突发的速率限制的允许程度。遵守`max_burst` \* `max_submission_rate` 命令后将严格执行速率限制。

为了便于说明，我们假设配置的速率限制为`100 commands/s`，突发率为 0.5。如果应用程序在一秒钟内提交 100 个命令，并且连续命令之间正好等待 10 毫秒，那么参与者将接受所有命令。当 `maxSubmissionBurstFactor` 为 0.5 时，参与者将接受前 50 个命令并拒绝其余 50 个命令。如果应用程序再等待 500 毫秒，它可能会再次提交 50 个命令的突发。如果等待 250 毫秒，则可能只提交 25 个命令的突发。

仅当服务器运行 Canton 企业时，才能更改资源限制。在社区版中，服务器使用无法更改的固定限制。

**参数**

* `limits`: `com.digitalasset.canton.参与方.admin.ResourceLimits`

### 测试

<div id="testing.acs_search"/>

### `testing.acs_search`

查找活跃合约。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `exactId`: `String`
* `filterPackage`: `String`
* `filterTemplate`: `String`
* `filterStakeholder`: `Option[com.digitalasset.canton.拓扑.PartyId]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**退货：** `List[com.digitalasset.canton.protocol.ContractInstance]`

<div id="testing.await_同步器_time" />

### `testing.await_同步器_time`

等待给定同步器达到给定时间。

**参数**

* `同步器`: `com.digitalasset.canton.拓扑.同步器`
* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.await_同步器_time_1" />

### `testing.await_同步器_time_1`

等待给定同步器达到给定时间。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.bong"/>

### `testing.bong`通过账本向一组目标方发送烟枪。级别 > 0 会导致 ping 值爆炸，合约数量呈指数级增长。如果失败则抛出 RuntimeException。

向多个参与者发起快速 ping，测量最快响应者的往返时间，并可选择超时。宽限期是烟枪在退出之前等待重复花费的时间（这将表明系统中存在错误）。如果级别 > 0，则 ping 命令将导致二进制爆炸和随后的合约膨胀，其中 `level` 决定我们将爆炸的级别数。结果，系统将创建 (2^(L+2) - 3) 个合约（其中 L 代表`level`）。通常，只有发起者才是验证者。可以使用 验证者s 参数添加其他验证器。 bong 命令可以方便地对系统运行突发测试，并快速导致过载状态。

**参数**

* `targets`: `Set[com.digitalasset.canton.拓扑.参与方Id]`
* `验证者s`: `Set[com.digitalasset.canton.拓扑.参与方Id]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `levels`: `Int`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `id`: `String`

**返回：** `scala.concurrent.duration.Duration`

<div id="testing.crypto_api" />

### `testing.crypto_api`

返回同步加密 api 提供程序，它提供对所有加密方法的访问。

**返回：** `com.digitalasset.canton.crypto.SyncCryptoApi参与方Provider`

<div id="testing.fetch_同步器_time" />

### `testing.fetch_同步器_time`

从给定的同步器获取当前时间。

**参数**

* `同步器`: `com.digitalasset.canton.拓扑.同步器`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.fetch_同步器_time_1" />

### `testing.fetch_同步器_time_1`

从给定的同步器获取当前时间。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.fetch_同步器_times" />

### `testing.fetch_同步器_times`

从所有连接的同步器中获取当前时间。

**参数**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.find_clean_commitments_timestamp" />

### `testing.find_clean_commitments_timestamp`

没有未完成承诺的给定时间戳之前或时的最新时间戳。

没有未完成承诺的给定时间戳之前或时的最新时间戳。请注意，这并不意味着可以在此时间戳进行修剪，因为系统可能需要一些额外的数据来进行崩溃恢复。因此，这对于测试承诺很有用；使用剪枝组中的命令进行剪枝。此外，结果不必落在调节间隔指定的“承诺刻度”上。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `beforeOrAt`: `com.digitalasset.canton.data.CantonTimestamp`

**退货：** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="testing.help"/>

### `testing.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="testing.lookup_transaction" />

### `testing.lookup_transaction`

通过更新 ID 查找已接受的交易。

**参数**

* `updateId`: `String`

**返回：** `Option[com.digitalasset.canton.protocol.LfVersionedTransaction]`

<div id="testing.maybe_bong"/>

### `testing.maybe_bong`

与 bong 类似，但如果失败则返回 None。

**参数**

* `targets`: `Set[com.digitalasset.canton.拓扑.参与方Id]`
* `验证者s`: `Set[com.digitalasset.canton.拓扑.参与方Id]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `levels`: `Int`
* `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `workflowId`: `String`
* `id`: `String`

**返回：** `Option[scala.concurrent.duration.Duration]`

<div id="testing.pcs_search"/>

### `testing.pcs_search`

在私人合约存储中查找合约。获取对给定同步器同步控制器的 PCS 的原始访问权限。过滤器命令将检查目标值`contains`给定的字符串。参数可以以 `^` 开头，以便使用 `startsWith` 进行比较，或者使用 `!` 来使用 `equals`。 `activeSet` 参数允许将搜索限制为活动合约集。对于合约 ID 过滤，仅支持精确匹配。

**参数**

* `同步器Alias`: `com.digitalasset.canton.同步器Alias`
* `exactId`: `String`
* `filterPackage`: `String`
* `filterTemplate`: `String`
* `activeSet`: `Boolean`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `List[(Boolean, com.digitalasset.canton.protocol.ContractInstance)]`

<div id="testing.sequencer_messages" />

### `testing.sequencer_messages`

检索所有定序器消息。

（可选）允许从特定时间跨度（包括两端）过滤定序器并限制显示消息的数量。如果给定时间跨度，则返回的消息将在大多数同步器分类帐实现上排序。

如果参与者从未连接到同步器，则失败。

**参数**

* `physical同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`
* `from`: `Option[java.time.Instant]`
* `to`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `warnOnDiscardedEnvelopes`: `Boolean`

**退货：** `Seq[com.digitalasset.canton.sequencing.PossiblyIgnoredProtocolEvent]`

<div id="testing.state_inspection" />

### `testing.state_inspection`

获取状态检查接口的访问权限。使用风险自负。

状态检查方法可能会致命且永久地破坏参与者的状态。 API 可能会发生任何变化。

**返回：** `com.digitalasset.canton.参与方.admin.inspection.SyncStateInspection`

### 拓扑管理

拓扑命令可用于操作和检查拓扑状态。在所有命令中，我们使用指纹来引用公钥。在内部，这些指纹是使用密钥注册表（这是指纹 -> 公钥的映射）来解析的。可以使用 `keys.public.load` 命令将任何密钥添加到密钥注册表中。

<div id="拓扑.help" />

### `拓扑.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.init_id" />

### `拓扑.init_id`

使用唯一标识符初始化节点。

Canton 中的每个节点都使用唯一标识符进行标识，该标识符由用户选择的字符串和签名密钥的指纹组成。签名密钥是定义所谓命名空间的根密钥，其中签名密钥对发布新标识符具有最终控制权。在初始化过程中，我们必须选择这样一个唯一的标识符。默认情况下，初始化会自动发生，但可以更改为手动初始化或从文件中读取一组身份和证书。

自动节点初始化通常会被关闭，以保留参与者或同步器节点的身份（在主要版本升级期间），或者如果节点的根命名空间密钥保持离线状态。

如果已知，可以设置命名空间以验证它是否与根证书匹配。否则将从代表团处宣读。

或者，如果根名称空间密钥不可用，则可以提供一组委托。这些委托可以在文件中，也可以作为对象传递。它们的版本需要与我们要连接的同步器的必要协议版本相匹配。

**参数**

* `identifier`: `String`
* `namespace`: `String`
* `delegations`: `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction]`
* `delegationFiles`: `Seq[String]`
* `waitForReady`: `Boolean`

<div id="拓扑.init_id_from_uid" />

### `拓扑.init_id_from_uid`

使用唯一标识符初始化节点。Canton 中的每个节点都使用唯一标识符进行标识，该标识符由用户选择的字符串和签名密钥的指纹组成。签名密钥是定义所谓命名空间的根密钥，其中签名密钥对发布新标识符具有最终控制权。在初始化过程中，我们必须选择这样一个唯一的标识符。默认情况下，初始化会自动发生，但可以更改为手动初始化或从文件中读取一组身份和委托。

自动节点初始化通常会被关闭，以保留参与者或同步器节点的身份（在主要版本升级期间），或者如果节点的根命名空间密钥保持离线状态。

或者，如果根名称空间密钥不可用，则可以提供一组委托。这些委托可以在文件中，也可以作为对象传递。它们的版本需要与我们要连接的同步器的必要协议版本相匹配。

**参数**

* `identifier`: `com.digitalasset.canton.拓扑.UniqueIdentifier`
* `delegations`: `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction]`
* `delegationFiles`: `Seq[String]`
* `waitForReady`: `Boolean`

<div id="topology.transactions.authorize" />

### `topology.transactions.authorize`

通过哈希值授权交易。

**参数**

* `txHash`: `com.digitalasset.canton.topology.transaction.拓扑Transaction.TxHash`
* `mustBeFullyAuthorized`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,M]`

<div id="topology.transactions.authorize_1" />

### `topology.transactions.authorize_1`

通过哈希值授权交易。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `txHash`: `com.digitalasset.canton.topology.transaction.拓扑Transaction.TxHash`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.拓扑Mapping]`

<div id="topology.transactions.export_identity_transactions" />

### `topology.transactions.export_identity_transactions`

将节点的拓扑身份事务序列化到文件中。

以这种方式序列化的事务应该使用 load\_from\_file 加载到另一个节点中

**参数**

* `file`: `String`

<div id="topology.transactions.export_identity_transactionsv2" />

### `topology.transactions.export_identity_transactionsv2`

将节点的拓扑身份事务序列化到文件中。

以这种方式序列化的事务应该使用 load\_from\_file 加载到另一个节点中

**参数**

* `file`: `String`

<div id="topology.transactions.export_拓扑_snapshot" />

### `topology.transactions.export_拓扑_snapshot`

导出拓扑快照。

此命令将节点的拓扑事务导出为字节字符串。

参数是： excexMappings：要从导出中排除的拓扑映射代码的列表。如果未提供，则包含所有映射。 filterNamespace：用于过滤事务的命名空间。 protocolVersion：用于序列化拓扑事务的协议版本。如果未提供，则使用最新的协议版本。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="topology.transactions.export_拓扑_snapshotv2" />

### `topology.transactions.export_拓扑_snapshotv2`

导出拓扑快照。

此命令将节点的拓扑事务导出为字节字符串。参数是： excexMappings：要从导出中排除的拓扑映射代码的列表。如果未提供，则包含所有映射。 filterNamespace：用于过滤事务的命名空间。 protocolVersion：用于序列化拓扑事务的协议版本。如果未提供，则使用最新的协议版本。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `com.google.protobuf.ByteString`

<div id="topology.transactions.find_latest_by_mapping" />

### `topology.transactions.find_latest_by_mapping`

查找给定映射哈希的最新交易。

商店：

*“授权”：拓扑交易将在节点的授权存储中查找。
* `"<同步器 id>"`：拓扑事务将在指定的同步器存储中查找。 includeProposals：为true时，结果可能是最新的提案，否则只返回最新的完全授权的交易

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `includeProposals`: `Boolean`

**返回：** `Option[com.digitalasset.canton.拓扑.store.Stored拓扑Transaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,M]]`

<div id="topology.transactions.find_latest_by_mapping_hash" />

### `topology.transactions.find_latest_by_mapping_hash`

查找给定映射哈希的最新交易。

mappingHash：查找存储的拓扑映射的唯一键：

*“授权”：拓扑交易将在节点的授权存储中查找。
* `"<同步器 id>"`：拓扑事务将在指定的同步器存储中查找。 includeProposals：为true时，结果可能是最新的提案，否则只返回最新的完全授权的交易

**参数**

* `mappingHash`: `com.digitalasset.canton.topology.transaction.拓扑Mapping.MappingHash`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `includeProposals`: `Boolean`

**返回：** `Option[com.digitalasset.canton.拓扑.store.Stored拓扑Transaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,M]]`

<div id="topology.transactions.genesis_state" />

### `topology.transactions.genesis_state`

下载定序器的创世状态。执行主要同步器升级时应使用此方法。

下载拓扑快照，其中包括拓扑事务的完整历史记录，以初始化定序器以进行主要同步器升级。 validFrom 和 validUntil 设置为 SignedTopologyTransaction.Initial拓扑SequencingTime。 filter同步器Store：如果从参与者节点请求创世状态，则必须指定。 timestamp：如果不指定，则使用最新拓扑事务的最大有效时间。否则，使用给定的时间戳。

**参数**

* `filter同步器Store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.同步器]`
* `timestamp`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="topology.transactions.genesis_statev2" />

### `topology.transactions.genesis_statev2`

下载定序器的创世状态。执行主要同步器升级时应使用此方法。

下载拓扑快照，其中包括拓扑事务的完整历史记录，以初始化定序器以进行主要同步器升级。 validFrom 和 validUntil 设置为 SignedTopologyTransaction.Initial拓扑SequencingTime。 filter同步器Store：如果从参与者节点请求创世状态，则必须指定。 timestamp：如果不指定，则使用最新拓扑事务的最大有效时间。否则，使用给定的时间戳。**参数**

* `filter同步器Store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.同步器]`
* `timestamp`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="topology.transactions.identity_transactions" />

### `topology.transactions.identity_transactions`

下载节点的拓扑身份事务。

节点的身份由 NamespaceDelegation 和 OwnerToKeyMapping 类型的拓扑事务定义。

**返回：** `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.拓扑Mapping]]`

<div id="topology.transactions.import_拓扑_snapshot_from" />

### `topology.transactions.import_拓扑_snapshot_from`

将拓扑事务从文件加载到指定的拓扑存储中。

该文件必须包含由 拓扑Transactions 序列化的数据。

**参数**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

<div id="topology.transactions.import_拓扑_snapshot_fromv2" />

### `topology.transactions.import_拓扑_snapshot_fromv2`

将拓扑事务从文件加载到指定的拓扑存储中。

该文件必须包含由 拓扑Transactions 序列化的数据。

**参数**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

<div id="topology.transactions.list" />

### `topology.transactions.list`

列出所有交易。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.拓扑Mapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`

**退货：** `com.digitalasset.canton.拓扑.store.Stored拓扑Transactions[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.拓扑Mapping]`

<div id="topology.transactions.load_multiple_from_file" />

### `topology.transactions.load_multiple_from_file`

将拓扑事务从文件加载到指定的拓扑存储中。

该文件必须包含由 SignedTopologyTransactions 序列化的数据。

**参数**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.load_single_from_file" />

### `topology.transactions.load_single_from_file`

将拓扑事务从文件加载到指定的拓扑存储中。

该文件必须包含由 SignedTopologyTransaction 序列化的数据。

**参数**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.load_single_from_files" />

### `topology.transactions.load_single_from_files`

将拓扑事务从文件列表加载到指定的拓扑存储中。

这些文件必须包含由 SignedTopologyTransaction 序列化的数据。

**参数**

* `files`: `Seq[String]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.logic_upgrade_state" />

### `topology.transactions.logical_upgrade_state`

下载定序器的升级状态。执行逻辑同步器升级时应使用此方法。

下载拓扑快照，其中包括拓扑事务的完整历史记录，以初始化定序器以进行逻辑同步器升级。逻辑同步器升级必须正在进行，此调用才能成功。

**参数*** `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="topology.transactions.propose" />

### `topology.transactions.propose`

提出交易。

对管理 API 命令的原始访问

**参数**

* `mapping`: `M`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`
* `mustFullyAuthorize`: `Boolean`
* `forceChanges`: `com.digitalasset.canton.拓扑.ForceFlags`
* `waitToBecomeEffective`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,M]`

<div id="拓扑.decentralized_namespaces.help" />

### `拓扑.decentralized_namespaces.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.decentralized_namespaces.propose" />

### `拓扑.decentralized_namespaces.propose`

提议对去中心化命名空间进行更改。

decentralizedNamespace：要提议的 DecentralizedNamespaceDefinition

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹序列：该拓扑交易应具有的预期序列。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数**

* `decentralizedNamespace`: `com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition]`

<div id="拓扑.decentralized_namespaces.propose_new" />

### `拓扑.decentralized_namespaces.propose_new`

提议创建一个新的去中心化命名空间。

owners：去中心化命名空间创始成员的命名空间，用于计算去中心化命名空间的名称。阈值：该阈值指定满足去中心化命名空间的拓扑交易授权要求所需的去中心化命名空间成员的签名的最小数量。

店铺：*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹序列：该拓扑交易应具有的预期序列。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数**

* `owners`: `Set[com.digitalasset.canton.topology.Namespace]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition]`

<div id="拓扑.同步器_parameters.get_dynamic_同步器_parameters" />

### `拓扑.同步器_parameters.get_dynamic_同步器_parameters`

获取配置的动态同步器参数。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`

**退货：** `com.digitalasset.canton.admin.api.client.data.Dynamic同步器Parameters`

<div id="拓扑.同步器_parameters.help" />

### `拓扑.同步器_parameters.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.同步器_parameters.latest" />

### `拓扑.同步器_parameters.latest`

最新动态同步器参数。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `filter同步器`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**返回：** `com.digitalasset.canton.admin.api.client.data.Dynamic同步器Parameters`

<div id="拓扑.同步器_parameters.list" />

### `拓扑.同步器_parameters.list`

列出动态同步器参数。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filter同步器`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.List同步器ParametersStateResult]`

<div id="拓扑.同步器_parameters.propose" />

### `拓扑.同步器_parameters.propose`

建议更改动态同步器参数。

同步器Id：目标同步器参数：要在同步器上使用的新动态同步器参数

商店：*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹序列：该拓扑交易应具有的预期序列。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。同步：同步超时可用于确保状态已传播到节点 waitFor参与方s：如果定义了同步，该命令还将等待，直到参数已传播到列出的参与者强制：执行危险操作时必须设置为 true，例如增加 PreparationTimeRecordTimeTolerance

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `parameters`: `com.digitalasset.canton.admin.api.client.data.Dynamic同步器Parameters`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.同步器ParametersState]`

<div id="拓扑.同步器_parameters.propose_update" />

### `拓扑.同步器_parameters.propose_update`

建议更新动态同步器参数。

同步器Id：目标同步器更新：同步器上使用的新动态同步器参数 MustFullyAuthorize：设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署此提案的密钥的指纹synchronize：同步超时可用于确保状态已传播到节点waitFor参与方s：如果定义了synchronize，该命令还将等待，直到更新已传播到列出的参与者force：执行危险操作时必须设置为true，例如增加preparementTimeRecordTimeTolerance

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `update`: `[com.digitalasset.canton.admin.api.client.data.Dynamic同步器Parameters => com.digitalasset.canton.admin.api.client.data.Dynamic同步器Parameters](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/Dynamic同步器Parameters.html)`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`

<div id="拓扑.同步器_parameters.set_ledger_time_record_time_tolerance" />

### `拓扑.同步器_parameters.set_ledger_time_record_time_tolerance`

更新动态同步器参数中的分类帐时间记录时间容差。

同步器Id：目标同步器 newLedgerTimeRecordTimeTolerance：应用于同步器的新 ledgerTimeRecordTimeTolerance 值

**参数*** `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `newLedgerTimeRecordTimeTolerance`: `com.digitalasset.canton.config.NonNegativeFiniteDuration`

<div id="拓扑.同步器_parameters.set_preparation_time_record_time_tolerance" />

### `拓扑.同步器_parameters.set_preparation_time_record_time_tolerance`

更新动态同步器参数中的准备时间记录时间容差。

如果立即执行更改不安全，则该命令将阻塞并等待，直到安全后才能执行更改。该命令最多会阻塞 `newPreparationTimeRecordTimeTolerance` 的两倍。

如果`mediatorDeduplicationTimeout`小于`newPreparationTimeRecordTimeTolerance`的两倍，该方法将失败。

运行此命令时不要同时修改同步器参数，因为该命令可能会覆盖并发更改。

强制：立即更新`newPreparationTimeRecordTimeTolerance`，不阻塞。在同步器引导期间和测试环境中执行此操作是安全的，但不应在运行的生产系统中执行此操作。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `newPreparationTimeRecordTimeTolerance`: `com.digitalasset.canton.config.NonNegativeFiniteDuration`
* `force`: `Boolean`

<div id="拓扑.同步器_trust_certificates.help" />

### `拓扑.同步器_trust_certificates.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.同步器_trust_certificates.propose" />

### `拓扑.同步器_trust_certificates.propose`

提议更改参与者的同步器信任证书。

参与者的同步器信任证书向同步器发出信号，表明参与者想要对同步器进行操作。

参与方Id：信任证书的目标参与者的标识符同步器Id：参与者想要操作的同步器的标识符

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数**

* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`
* `featureFlags`: `Seq[com.digitalasset.canton.topology.transaction.同步器TrustCertificate.参与方拓扑FeatureFlag]`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.同步器TrustCertificate]`

<div id="拓扑.mediators.help" />

### `拓扑.mediators.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.mediators.list" />

### `拓扑.mediators.list`

列出中介同步器拓扑状态。

同步器Id：可选的目标同步器提案：如果为 true，则显示提案，否则显示实际验证状态

**参数*** `同步器Id`: `Option[com.digitalasset.canton.拓扑.同步器Id]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filter同步器`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`
* `group`: `Option[com.digitalasset.canton.config.RequireTypes.NonNegativeInt]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListMediator同步器StateResult]`

<div id="拓扑.mediators.propose" />

### `拓扑.mediators.propose`

更换中介拓扑。

同步器Id：目标同步器阈值：将消息发送给其他成员需要达成共识的最小中介者数量。 active：将参与该调解者组中调解者共识的调解者列表 Passive：将接收所有消息但不参与调解者共识组的调解者：调解者组标识符存储：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹序列：该拓扑交易应具有的预期序列。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `active`: `Seq[com.digitalasset.canton.拓扑.MediatorId]`
* `observers`: `Seq[com.digitalasset.canton.拓扑.MediatorId]`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.Mediator同步器State]`

<div id="拓扑.mediators.propose_delta" />

### `拓扑.mediators.propose_delta`

对中介拓扑提出更改建议。

同步器Id：目标同步器组：中介器组标识符添加：要添加的活动中介器的唯一标识符。删除：不再是活动调解器的调解器的唯一标识符。 observerAdds：要添加的观察者中介者的唯一标识符。 observerRemoves：不再是观察者调解者的调解者的唯一标识符。 updateThreshold：中介组阈值的更新值（可选）。 wait：可选超时，等待提案保存在指定的拓扑存储中。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹

**参数*** `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `adds`: `List[com.digitalasset.canton.拓扑.MediatorId]`
* `removes`: `List[com.digitalasset.canton.拓扑.MediatorId]`
* `observerAdds`: `List[com.digitalasset.canton.拓扑.MediatorId]`
* `observerRemoves`: `List[com.digitalasset.canton.拓扑.MediatorId]`
* `updateThreshold`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`

<div id="拓扑.mediators.remove_group" />

### `拓扑.mediators.remove_group`

建议删除调解组。

同步器Id：目标同步器组：中介器组标识符

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.Mediator同步器State]`

<div id="拓扑.namespace_delegations.help" />

### `拓扑.namespace_delegations.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.namespace_delegations.propose_delegation" />

### `拓扑.namespace_delegations.propose_delegation`

提出仅限于某些拓扑映射类型的新命名空间委托。

命名空间委托允许命名空间的所有者将代表所述命名空间的拓扑事务的签名权限委托给其他签名密钥。

namespace：目标密钥可用于签署拓扑交易的命名空间 targetKey：用于代表命名空间签署拓扑交易的目标密钥 delegateRestriction：targetKey 可以签署的拓扑映射类型。可以是以下值之一：

* `CanSignAllMappings`：目标密钥可以对当前已知或将在未来版本中添加的所有拓扑映射进行签名。
* `CanSignAllButNamespaceDelegations`：目标密钥可以对当前已知或将在未来版本中添加的所有拓扑映射进行签名，命名空间委托除外。
* CanSignSpecificMappings(拓扑Mapping.Code\*)：目标密钥只能对指定的拓扑映射进行签名。

店铺：*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累足够的签名以满足映射的授权要求。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数**

* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `targetKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `delegationRestriction`: `com.digitalasset.canton.topology.transaction.DelegationRestriction`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.NamespaceDelegation]`

<div id="拓扑.namespace_delegations.propose_replication" />

### `拓扑.namespace_delegations.propose_revocation`

撤销现有的命名空间委托。

命名空间委托允许命名空间的所有者将代表所述命名空间的拓扑事务的签名权限委托给其他签名密钥。

namespace：应撤销目标密钥的命名空间 targetKey：要撤销的目标密钥

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累足够的签名以满足映射的授权要求。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。 force：执行危险操作（例如吊销根证书）时必须设置为 true

**参数**

* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `targetKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `forceChanges`: `com.digitalasset.canton.拓扑.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.NamespaceDelegation]`

<div id="拓扑.owner_to_key_mappings.add_key" />

### `拓扑.owner_to_key_mappings.add_key`将所有者的密钥添加到密钥映射。

将所有者的密钥添加到密钥映射。密钥所有者是系统中需要同步器的所有成员（参与者、中介者、排序者）都知道的密钥对的任何人。如果指定的密钥所有者不存在所有者到密钥的映射，则使用指定的密钥创建新映射。指定的密钥需要事先通过 `keys.secret` api 创建。

key：密钥的指纹 目的：密钥的目的，即密钥是用于签名还是加密 keyOwner：拥有密钥的成员signedBy：授权密钥的可选指纹，该指纹又指特定的本地现有证书。同步：同步超时可用于确保状态已传播到节点中。 必须完全授权：是否仅在成员处于授权更改的位置时才添加密钥。

**参数**

* `key`: `com.digitalasset.canton.crypto.Fingerprint`
* `purpose`: `com.digitalasset.canton.crypto.KeyPurpose`
* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

<div id="拓扑.owner_to_key_mappings.add_keys" />

### `拓扑.owner_to_key_mappings.add_keys`

将一组键添加到所有者到键映射。

将一组键添加到所有者到键映射。密钥所有者是系统中需要同步器的所有成员（参与者、中介者、排序者）都知道的密钥对的任何人。如果指定的密钥所有者不存在所有者到密钥的映射，则使用指定的密钥创建新映射。指定的密钥需要事先通过 `keys.secret` api 创建。

密钥：密钥的指纹和密钥用途 keyOwner：拥有密钥的成员signedBy：授权密钥的可选指纹，该密钥又引用特定的本地现有证书。同步：同步超时可用于确保状态已传播到节点中。 必须完全授权：是否仅在成员处于授权更改的位置时才添加密钥。

**参数**

* `keys`: `Seq[(com.digitalasset.canton.crypto.Fingerprint, com.digitalasset.canton.crypto.KeyPurpose)]`
* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

<div id="拓扑.owner_to_key_mappings.help" />

### `拓扑.owner_to_key_mappings.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.owner_to_key_mappings.list" />

### `拓扑.owner_to_key_mappings.list`

列出所有者到键映射事务。

**参数**

* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.拓扑.MemberCode]`
* `filterKeyOwnerUid`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListOwnerToKeyMappingResult]`

<div id="拓扑.owner_to_key_mappings.remove_key" />

### `拓扑.owner_to_key_mappings.remove_key`

从所有者到密钥映射中删除密钥。

从所有者到密钥映射中删除密钥。密钥所有者是系统中需要同步器的所有成员（参与者、中介者、排序者）都知道的密钥对的任何人。如果指定的键是所有者到键映射中的最后一个键（这要求强制为 true），则所有者到键映射将被删除。指定的密钥需要事先通过 `keys.secret` api 创建。key：密钥的指纹 目的：密钥的目的，即密钥是用于签名还是加密 keyOwner：拥有密钥的成员signedBy：授权密钥的可选指纹，该指纹又指特定的本地现有证书。同步：同步超时可用于确保状态已传播到节点中。 必须完全授权：是否仅在成员处于授权更改的位置时才添加密钥。强制：移除最后一个键很危险，因此必须手动强制

**参数**

* `key`: `com.digitalasset.canton.crypto.Fingerprint`
* `purpose`: `com.digitalasset.canton.crypto.KeyPurpose`
* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`

<div id="拓扑.owner_to_key_mappings.rotate_key" />

### `拓扑.owner_to_key_mappings.rotate_key`

将所有者的密钥轮换到密钥映射。

通过添加新密钥并删除先前的密钥，将所有者所有者的现有密钥轮换为密钥映射。

nodeInstance：用于验证当前密钥和新密钥是否属于该节点的节点实例。当不同节点具有相同的 uuid（即多个定序器）时，这可以避免冲突。 owner：拥有密钥映射所有者的成员 currentKey：将轮换的当前公钥 newKey：已生成的新公钥

**参数**

* `member`: `com.digitalasset.canton.拓扑.Member`
* `currentKey`: `com.digitalasset.canton.crypto.PublicKey`
* `newKey`: `com.digitalasset.canton.crypto.PublicKey`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="拓扑.参与方_同步器_permissions.find" />

### `拓扑.参与方_同步器_permissions.find`

查找同步器上参与者的参与者权限。

返回可选的参与者同步器权限。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`

**退货：** `Option[com.digitalasset.canton.admin.api.client.data.拓扑.List参与方同步器PermissionResult]`

<div id="拓扑.参与方_同步器_permissions.help" />

### `拓扑.参与方_同步器_permissions.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.参与方_同步器_permissions.propose" />

### `拓扑.参与方_同步器_permissions.propose`

对参与者的同步器权限提出更改建议。

同步器操作员可以使用此命令更改参与者对同步器的权限。

同步器Id：目标同步器参与方Id：需要更改权限的参与者permission：参与者的权限loginAfter：参与者最早可以连接到同步器的时间limits：该参与者的同步器限制

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。

**参数*** `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `permission`: `com.digitalasset.canton.topology.transaction.参与方Permission`
* `loginAfter`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `limits`: `Option[com.digitalasset.canton.topology.transaction.参与方同步器Limits]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.参与方同步器Permission]`

<div id="拓扑.参与方_同步器_permissions.revoke" />

### `拓扑.参与方_同步器_permissions.revoke`

撤销参与者的同步器权限。

同步器操作员可以使用此命令撤销参与者对同步器的权限。

同步器Id：目标同步器 参与方Id：需要撤销权限的参与者

商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.参与方同步器Permission]`

<div id="拓扑.参与方_同步器_states.active" />

### `拓扑.参与方_同步器_states.active`

如果给定参与者当前在给定同步器上处于活动状态，则返回 true。

活跃意味着参与者至少被授予了对同步器的观察权，并且参与者已经注册了同步器信任证书

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`

**退货：** `Boolean`

<div id="拓扑.参与方_同步器_states.help" />

### `拓扑.参与方_同步器_states.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.party_hosting_limits.help" />

### `拓扑.party_hosting_limits.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.party_to_key_mappings.help" />

### `拓扑.party_to_key_mappings.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.party_to_key_mappings.list" />

### `拓扑.party_to_key_mappings.list`

列出键映射事务的参与方。

**参数**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterParty`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListPartyToKeyMappingResult]`

<div id="拓扑.party_to_key_mappings.propose" />

### `拓扑.party_to_key_mappings.propose`

建议参与键映射。

**参数**

* `partyId`: `com.digitalasset.canton.拓扑.PartyId`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `signingKeys`: `com.daml.nonempty.NonEmpty[Seq[com.digitalasset.canton.crypto.SigningPublicKey]]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `ops`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.PartyToKeyMapping]`

<div id="拓扑.party_to_参与方_mappings.help" />

### `拓扑.party_to_参与方_mappings.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.party_to_参与方_mappings.list" />

### `拓扑.party_to_参与方_mappings.list`

列出来自同步器存储的一方到参与者的映射事务。

列出商店中存在的参与方映射交易。参与方到参与者的映射是用于将一方分配给某些参与者的拓扑事务。同一方可以分配给多个具有不同权限的参与者。

同步器Id：要考虑的同步器提案：是否查询提案而不是授权交易。 timeQuery：时间查询允许按时间自定义查询。支持以下选项： TimeQuery.HeadState（默认）：最近的已知状态。 TimeQuery.Snapshot(ts)：某个时间点的状态。 TimeQuery.Range(fromO, toO)：交易添加到存储操作的时间范围：可选，交易应该具有什么类型的操作。 filterParty：过滤以给定过滤字符串开头的各方。 filter参与方：如果非空，则仅返回在此参与者上托管的各方。 filterSigningKey：过滤使用以给定过滤字符串开头的密钥授权的交易。协议版本：以可选协议版本导出拓扑事务。

**参数**

* `同步器Id`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.同步器`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterParty`: `String`
* `filter参与方`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListPartyTo参与方Result]`

<div id="拓扑.party_to_参与方_mappings.list_from_all" />

### `拓扑.party_to_参与方_mappings.list_from_all`

列出来自所有商店的各方到参与者的映射交易。

列出商店中存在的参与方映射交易。参与方到参与者的映射是用于将一方分配给某些参与者的拓扑事务。同一方可以分配给多个具有不同权限的参与者。

提案：是否查询提案而不是授权交易。 timeQuery：时间查询允许按时间自定义查询。支持以下选项： TimeQuery.HeadState（默认）：最近的已知状态。 TimeQuery.Snapshot(ts)：某个时间点的状态。 TimeQuery.Range(fromO, toO)：交易添加到存储操作的时间范围：可选，交易应该具有什么类型的操作。 filterParty：过滤以给定过滤字符串开头的各方。 filter参与方：过滤以给定过滤字符串开头的参与者。 filterSigningKey：过滤使用以给定过滤字符串开头的密钥授权的交易。协议版本：以可选协议版本导出拓扑事务。**参数**

* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterParty`: `String`
* `filter参与方`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListPartyTo参与方Result]`

<div id="拓扑.party_to_参与方_mappings.list_from_authorized" />

### `拓扑.party_to_参与方_mappings.list_from_authorized`

列出来自授权商店的各方到参与者的映射交易。

列出商店中存在的参与方映射交易。参与方到参与者的映射是用于将一方分配给某些参与者的拓扑事务。同一方可以分配给多个具有不同权限的参与者。

提案：是否查询提案而不是授权交易。 timeQuery：时间查询允许按时间自定义查询。支持以下选项： TimeQuery.HeadState（默认）：最近的已知状态。 TimeQuery.Snapshot(ts)：某个时间点的状态。 TimeQuery.Range(fromO, toO)：交易添加到存储操作的时间范围：可选，交易应该具有什么类型的操作。 filterParty：过滤以给定过滤字符串开头的各方。 filter参与方：过滤以给定过滤字符串开头的参与者。 filterSigningKey：过滤使用以给定过滤字符串开头的密钥授权的交易。协议版本：以可选协议版本导出拓扑事务。

**参数**

* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filterParty`: `String`
* `filter参与方`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListPartyTo参与方Result]`

<div id="拓扑.party_to_参与方_mappings.list_hosting_proposals" />

### `拓扑.party_to_参与方_mappings.list_hosting_proposals`

列出多方主办方的提案。

多托管方要求所有相关参与者签署拓扑交易。没有足够签名的拓扑交易称为提案。它们的分发方式与完全授权的拓扑交易相同，并且签名会被聚合，直到交易得到完全授权。此方法允许检查开放托管提案的待处理队列。返回的建议与指定同步器上看到的一样。它们可以由各个参与者通过调用 node.topology.transactions.authorize(\<同步器-id>, \<tx-hash>) 来批准。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `参与方Id`: `com.digitalasset.canton.拓扑.参与方Id`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListMultiHostingProposal]`

<div id="拓扑.party_to_参与方_mappings.propose" />

### `拓扑.party_to_参与方_mappings.propose`

替换方到参与者的映射。替换一方与主办参与者的关联。 party：要修改其参与者权限集的一方的唯一标识符。 new参与方s：主办聚会的参与者的唯一标识符。每个参与者条目指定参与者的权限（提交、确认、观察）。 参与方sRequiringPartyToBeOnboarded：在参与者完全主持聚会之前，需要独立于此呼叫加入聚会的参与者。阈值：普通方的阈值为`1`，“联盟方”的阈值大于`1`。该阈值指示需要多少参与者确认才能代表该方确认 Daml 交易。 partySigningKeys：带有阈值的参与方签名密钥。如果指定，则将从该字段获取密钥。否则，必须在 PartyToKey 映射中提前指定它们。 signedBy：指授权密钥的可选指纹，而授权密钥又指特定的本地现有证书。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。操作：要使用的操作。添加映射或进行更改时，请使用 拓扑ChangeOp.Replace。删除映射时，请使用 拓扑ChangeOp.Remove 并传递与当前有效映射相同的值。默认值为 拓扑ChangeOp.Replace。同步：同步超时可用于确保状态已传播到节点中。 MustFullyAuthorize：设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累足够的签名以满足映射的授权要求。商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `new参与方s`: `Seq[(com.digitalasset.canton.拓扑.参与方Id, com.digitalasset.canton.topology.transaction.参与方Permission)]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `partySigningKeys`: `Option[com.digitalasset.canton.crypto.SigningKeysWithThreshold]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `operation`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `参与方sRequiringPartyToBeOnboarded`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.PartyTo参与方]`

<div id="拓扑.party_to_参与方_mappings.propose_delta" />

### `拓扑.party_to_参与方_mappings.propose_delta`

更改参与方到参与者的映射。将一方的关联更改为主办参与者。 party：参与者集或修改权限的一方的唯一标识符。添加：主持聚会的参与者的唯一标识符，每个参与者指定参与者的权限（提交、确认、观察）。如果参与者已主持指定的聚会，请更新参与者的权限。删除：不应再主持聚会的参与者的唯一标识符。 signedBy：指授权密钥的可选指纹，而授权密钥又指特定的本地现有证书。串行：此拓扑事务应具有的预期串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。同步：同步超时可用于确保状态已传播到节点中。 MustFullyAuthorize：设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累足够的签名以满足映射的授权要求。商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 force：禁用具有活动合同的一方时必须设置。 requirePartyToBeOnboarded：设置为 true 时，指示添加的参与者需要首先独立于此呼叫加入该方，然后再添加的参与者完全主持该方。

**参数**

* `party`: `com.digitalasset.canton.拓扑.PartyId`
* `adds`: `Seq[(com.digitalasset.canton.拓扑.参与方Id, com.digitalasset.canton.topology.transaction.参与方Permission)]`
* `removes`: `Seq[com.digitalasset.canton.拓扑.参与方Id]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.拓扑.ForceFlags`
* `requiresPartyToBeOnboarded`: `Boolean`

**返回：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.PartyTo参与方]`

<div id="拓扑.sequencers.help" />

### `拓扑.sequencers.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.sequencers.propose" />

### `拓扑.sequencers.propose`

建议更改定序器拓扑。

同步器Id：目标同步器 Active：活动定序器列表 Passive：接收消息但不可用于成员连接的定序器

商店：*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥的指纹序列：该拓扑交易应具有的预期序列。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。同步：同步超时，等待在同步器上观察到提案。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `active`: `Seq[com.digitalasset.canton.拓扑.SequencerId]`
* `passive`: `Seq[com.digitalasset.canton.拓扑.SequencerId]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**退货：** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.拓扑ChangeOp,com.digitalasset.canton.topology.transaction.Sequencer同步器State]`

<div id="拓扑.synchronization.await_idle" />

### `拓扑.synchronisation.await_idle`

等待节点的拓扑处理空闲。

该函数等待`is_idle()`函数返回true。

**参数**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="拓扑.synchronization.is_idle" />

### `拓扑.synchronisation.is_idle`

检查节点的拓扑处理是否空闲。

拓扑事务在同步器上生效之前会经过一组队列。该函数允许检查所有队列是否为空。虽然同步器和参与者节点都支持类似的队列，但参与者队列存在一些模糊性。虽然同步器确实了解任何时间点的所有正在进行的事务，但参与者不会知道同步器拓扑调度程序当前正在处理的任何事务的状态。

**退货：** `Boolean`

<div id="拓扑.stores.create_temporary_拓扑_store" />

### `拓扑.stores.create_temporary_拓扑_store`

创建临时拓扑存储。

临时拓扑存储对于协调同步器创建仪式或导入拓扑快照以供以后检查非常有用。临时拓扑存储不会持久化，所有事务仅保存在内存中，这意味着重新启动节点会导致该存储中的所有事务丢失。此外，临时拓扑存储未连接到任何同步器，因此拓扑事务不会从临时存储自动传播到连接的同步器。

**参数**

* `name`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**返回：** `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Temporary`

<div id="拓扑.stores.drop_temporary_拓扑_store" />

### `拓扑.stores.drop_temporary_拓扑_store`

此命令删除临时拓扑存储及其中包含的所有事务。

删除临时拓扑存储是不可逆的，并且存储中的所有拓扑事务都将被永久删除。无法使用此命令删除授权存储或任何同步器存储。

**参数**

* `temporaryStoreId`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Temporary`<div id="拓扑.stores.help" />

### `拓扑.stores.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.stores.list" />

### `拓扑.stores.list`

列出可用的拓扑存储。

**返回：** `Seq[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`

<div id="拓扑.vetted_packages.help" />

### `拓扑.vetted_packages.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="拓扑.vetted_packages.list" />

### `拓扑.vetted_packages.list`

列出经过审查的包。

store：从提案中查询的可选拓扑存储：如果为 true，则显示提案，否则实际验证状态

**参数**

* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.拓扑.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.拓扑ChangeOp]`
* `filter参与方`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListVettedPackagesResult]`

<div id="拓扑.vetted_packages.propose" />

### `拓扑.vetted_packages.propose`

更换包裹审查。

参与者将仅处理引用所有相关参与者之前已审查过的包的交易。审查是通过向同步器注册相应的拓扑事务来完成的，然后其他参与者可以使用同步器来验证事务是否仅使用经过审查的包。请注意，所有引用和依赖的包必须存在于包存储中。

参与方Id：审查包的参与者的标识符packages：具有要审查的有效性边界的lf-package id，将替换以前审查的包。商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。串行：此拓扑事务应具有的 ted 串行。序列号必须是连续的，并且从 1 开始。如果已经存在另一个具有相同序列号的完全授权交易，或者如果该序列号与最近使用的序列号之间存在间隙，则该交易将被拒绝。如果没有，则节点将自动选择串行。 signedBy：用于签署该提案的密钥指纹。force：撤销packagesIds审核时必须设置

**参数**

* `参与方`: `com.digitalasset.canton.拓扑.参与方Id`
* `packages`: `Seq[com.digitalasset.canton.topology.transaction.VettedPackage]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`
* `operation`: `com.digitalasset.canton.topology.transaction.拓扑ChangeOp`

<div id="拓扑.vetted_packages.propose_delta" />

### `拓扑.vetted_packages.propose_delta`

更改包审查。

参与者将仅处理引用所有相关参与者之前已审查过的包的交易。审查是通过向同步器注册相应的拓扑事务来完成的，然后其他参与者可以使用同步器来验证事务是否仅使用经过审查的包。请注意，所有引用和依赖的包必须存在于包存储中。参与方Id：审查包的参与者的标识符添加：要审查的 lf-package id。删除： lf-package id 未经审查。商店：

*“授权”：拓扑事务将存储在节点的授权存储中，并自动传播到连接的同步器（如果适用）。
* `"<同步器 id>"`：拓扑事务将直接提交到指定的同步器，而不先存储在本地。这也意味着它不会自动同步到其他同步器。 filter参与方：过滤以给定过滤字符串开头的参与者。 MustFullyAuthorize：当设置为 true 时，提案之前收到的签名和该节点的签名必须足以完全授权拓扑交易。如果不是这种情况，则请求失败。当设置为 false 时，提案将保留提案状态，直到积累了足够的签名以满足映射的授权要求。 signedBy：用于签署该提案的密钥指纹。force：撤销packagesIds审核时必须设置

**参数**

* `参与方`: `com.digitalasset.canton.拓扑.参与方Id`
* `adds`: `Seq[com.digitalasset.canton.topology.transaction.VettedPackage]`
* `removes`: `Seq[com.digitalasset.daml.lf.data.Ref.PackageId]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `force`: `com.digitalasset.canton.拓扑.ForceFlags`

### 交通

<div id="流量_control.help" />

### `流量_control.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="流量_control.流量_state" />

### `流量_control.流量_state`

返回节点的流量状态。

使用此命令获取特定同步器 ID 在给定时间节点的流量状态。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`

**返回：** `com.digitalasset.canton.sequencing.protocol.流量State`

## 排序器管理命令

<div id="bft.add_peer_endpoint" />

### `bft.add_peer_endpoint`

添加新的对等端点。

**参数**

* `endpointConfig`: `com.digitalasset.canton.同步器.sequencer.block.bftordering.core.BftBlockOrdererConfig.P2PEndpointConfig`

<div id="bft.disable_performance_metrics" />

### `bft.disable_performance_metrics`

禁用 BFT 排序性能指标。

<div id="bft.enable_performance_metrics" />

### `bft.enable_performance_metrics`

启用 BFT 排序性能指标。

<div id="bft.get_ordering_拓扑" />

### `bft.get_ordering_拓扑`

获取当前活动的排序拓扑。

**退货：** `com.digitalasset.canton.同步器.sequencer.block.bftordering.admin.SequencerBftAdminData.Ordering拓扑`

<div id="bft.get_peer_network_status"/>

### `bft.get_peer_network_status`

获取对等网络状态。

**参数**

* `endpoints`: `Option[Iterable[com.digitalasset.canton.同步器.sequencer.block.bftordering.core.BftBlockOrdererConfig.EndpointId]]`

**返回：** `com.digitalasset.canton.同步器.sequencer.block.bftordering.admin.SequencerBftAdminData.PeerNetworkStatus`

<div id="bft.remove_peer_endpoint" />

### `bft.remove_peer_endpoint`

删除对等端点。

**参数**

* `peerEndpointId`: `com.digitalasset.canton.同步器.sequencer.block.bftordering.core.BftBlockOrdererConfig.EndpointId`

<div id="clear_cache_2" />

### `clear_cache_2`

清除本地缓存的变量。

有些命令在客户端缓存值。使用此命令显式清除这些值的缓存。

<div id="config_2" />

### `config_2`

返回定序器配置。

**退货：** `com.digitalasset.canton.同步器.sequencer.config.SequencerNodeConfig`

<div id="help_3"/>

### `help_3`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="id_2"/>

### `id_2`

产生该定序器的全局唯一 ID。如果 id 尚未分配（例如，排序器尚未启动），则抛出异常。

**退货：** `com.digitalasset.canton.拓扑.SequencerId`

<div id="is_initialized_2"/>

### `is_initialized_2`检查本地实例是否正在运行并且已完全初始化。

**返回：** `Boolean`

<div id="is_running_2"/>

### `is_running_2`

检查本地实例是否正在运行。

**返回：** `Boolean`

<div id="maybeid_2"/>

### `maybeid_2`

如果 id 存在，则产生该定序器的 Some(id)。如果 id 尚未分配（例如，排序器尚未初始化），则返回 None。

**返回：** `Option[com.digitalasset.canton.拓扑.SequencerId]`

<div id="physical_同步器_id" />

### `physical_同步器_id`

返回同步器的物理同步器 ID。

**返回：** `com.digitalasset.canton.拓扑.Physical同步器Id`

<div id="修剪.clear_schedule_3" />

### `修剪.clear_schedule_3`

停用自动修剪。

<div id="修剪.find_修剪_timestamp_1" />

### `修剪.find_修剪_timestamp_1`

获取定序器状态开始处或附近的时间戳。

当使用默认值 `index` 1 调用时，此命令可以深入了解定序器修剪的当前状态。当通过 `prune_at` 手动修剪定序器并打算批量修剪时，请指定一个值（例如 1000）以获取与批次“结束”相对应的修剪时间戳。

**参数**

* `index`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="修剪.force_prune" />

### `修剪.force_prune`

强制从 Sequencer 中删除数据，包括脱机客户端可能尚未读取的数据。

将通过可能禁用尚未读取我们想要删除的数据的客户端来强制修剪直到默认保留期。禁用这些客户端将阻止它们重新连接到同步器，因此仅当同步器操作员确信它们可以被永久忽略时才应使用。使用 `dryRun = true` 运行以查看将首先禁用哪些客户端的描述。使用 `dryRun = false` 运行以禁用这些客户端并执行强制修剪。

**参数**

* `dryRun`: `Boolean`

**退货：** `String`

<div id="修剪.force_prune_at" />

### `修剪.force_prune_at`

强制从 Sequencer 中删除数据，包括在指定时间之前离线客户端可能尚未读取的数据。

与上面的`force_prune`命令类似，但允许指定修剪的确切时间

**参数**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `dryRun`: `Boolean`

**返回：** `String`

<div id="修剪.force_prune_with_retention_period" />

### `修剪.force_prune_with_retention_period`

强制从 Sequencer 中删除数据，包括在自定义保留期内离线客户端可能尚未读取的数据。

与上面的`force_prune`命令类似，但允许指定自定义保留期

**参数**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`
* `dryRun`: `Boolean`

**返回：** `String`

<div id="修剪.get_schedule_2" />

### `修剪.get_schedule_2`

检查自动修剪计划。

该计划由“cron”表达式和“max\_duration”和“retention”持续时间组成。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。如果尚未通过 `set_schedule` 配置计划或已调用 `clear_schedule`，则返回 `None`。

**退货：** `Option[com.digitalasset.canton.admin.api.client.data.修剪Schedule]`

<div id="修剪.help_3" />

### `修剪.help_3`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="修剪.prune_2" />

### `修剪.prune_2`

从排序器中删除不必要的数据，直到默认保留点。

从 Sequencer 中删除早于默认保留期的不必要数据。默认保留期在`parameters.retention-period-defaults.sequencer`下运行此命令的Canton处理配置中设置。此修剪命令要求客户端读取并确认数据，然后才考虑安全删除。如果没有数据被删除，则可能表明客户端没有及时读取或确认数据（通常是由于节点长时间离线）。您可以选择禁用在这些节点上运行的成员以允许删除此数据，但这意味着它们将来将无法重新连接到同步器。为此，运行 `force_prune(dryRun = true)` 返回将禁用哪些成员的描述，以修剪 Sequencer。如果您愿意禁用所描述的客户端，请运行`force_prune(dryRun = false)`以永久删除其未读数据。

一旦离线客户端被禁用，您就可以继续正常运行`prune`。

**返回：** `String`

<div id="修剪.prune_at_1" />

### `修剪.prune_at_1`

删除指定时间之前已读取的数据。

与上面的`prune`命令类似，但允许指定修剪的确切时间。如果客户端在指定时间之前尚未读取并确认某些数据，则该命令将失败。

**参数**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**返回：** `String`

<div id="修剪.prune_with_retention_period_1" />

### `修剪.prune_with_retention_period_1`

删除在自定义保留期限之前已读取的数据。

与上面的`prune`命令类似，但允许指定自定义保留期

**参数**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`

**返回：** `String`

<div id="修剪.set_cron_2" />

### `修剪.set_cron_2`

修改自动修剪使用的cron。

该计划以 cron 格式指定，指的是 GMT 时区的修剪开始时间。如果没有通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `cron`: `String`

<div id="修剪.set_max_duration_2" />

### `修剪.set_max_duration_2`

修改自动修剪使用的最大持续时间。

`maxDuration` 被指定为正持续时间并且最多具有每秒粒度。如果没有通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_retention_2" />

### `修剪.set_retention_2`

更新自动修剪使用的修剪保留。

`retention` 被指定为正持续时间并且最多具有每秒粒度。如果没有通过 `set_schedule` 配置计划或通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在此更新时，修剪正在主动运行，则会尽力暂停修剪并以新指定的保留重新启动。这允许新的保留要求保留比以前更多的数据。

**参数**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_schedule_3" />

### `修剪.set_schedule_3`

根据指定的时间表激活自动修剪。

该计划以 cron 格式以及“max\_duration”和“retention”持续时间指定。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。

**参数**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.status" />

### `修剪.status`

定序器及其连接的客户端的状态。

提供修剪所需信息的详细分类：* 根据此定序器实例的当前时间
* 定序器支持的同步器成员
* 每个会员的注册时间以及是否启用
* 每个成员的客户列表、他们的最后确认以及是否启用

**返回：** `com.digitalasset.canton.同步器.sequencer.Sequencer修剪Status`

<div id="repair.disable_member" />

### `repair.disable_member`

禁用 Sequencer 中提供的成员，这将允许删除它们的任何未读数据。

这将防止给定成员的任何客户端重新连接 Sequencer，并允许删除任何未读/未确认的数据。仅当同步器操作确信成员永远不需要重新连接时才应使用此选项，因为无法重新启用成员。要使用排序器查看成员，请运行 `sequencer.status()`。”

**参数**

* `member`: `com.digitalasset.canton.拓扑.Member`

<div id="setup.assign_from_genesis_state" />

### `setup.assign_from_genesis_state`

从事件流的开头初始化定序器。仅当定序器节点与相应的同步器节点同时初始化时才应调用此方法。这是作为 同步器.setup.bootstrap 命令的一部分调用的，因此您不太可能需要直接调用它。

**参数**

* `genesisState`: `com.google.protobuf.ByteString`
* `同步器Parameters`: `com.digitalasset.canton.admin.api.client.data.Static同步器Parameters`
* `waitForReady`: `Boolean`

**返回：** `com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_genesis_statev2" />

### `setup.assign_from_genesis_statev2`

从事件流的开头初始化定序器。仅当定序器节点与相应的同步器节点同时初始化时才应调用此方法。这是作为 同步器.setup.bootstrap 命令的一部分调用的，因此您不太可能需要直接调用它。

**参数**

* `genesisState`: `com.google.protobuf.ByteString`
* `同步器Parameters`: `com.digitalasset.canton.admin.api.client.data.Static同步器Parameters`
* `waitForReady`: `Boolean`

**退货：** `com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_入驻_state" />

### `setup.assign_from_入驻_state`

从事件流开头之后的某个点动态初始化定序器。

**参数**

* `入驻State`: `com.google.protobuf.ByteString`
* `waitForReady`: `Boolean`

**返回：** `com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_入驻_statev2" />

### `setup.assign_from_入驻_statev2`

从事件流开头之后的某个点动态初始化定序器。

**参数**

* `入驻State`: `com.google.protobuf.ByteString`
* `waitForReady`: `Boolean`

**返回：** `com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.help_1" />

### `setup.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="setup.initialize_from_同步器_predecessor" />

### `setup.initialize_from_同步器_predecessor`

从其前身的状态初始化逻辑升级的定序器。

**参数**

* `predecessorState`: `com.google.protobuf.ByteString`
* `同步器Parameters`: `com.digitalasset.canton.admin.api.client.data.Static同步器Parameters`
* `waitForReady`: `Boolean`

<div id="setup.入驻_state_at_timestamp" />

### `setup.入驻_state_at_timestamp`

下载给定时间点的启动状态以引导另一个定序器。

**参数**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**退货：** `com.google.protobuf.ByteString`

<div id="setup.入驻_state_for_sequencer" />

### `setup.入驻_state_for_sequencer`

下载给定定序器的入门状态。

**参数**

* `sequencerId`: `com.digitalasset.canton.拓扑.SequencerId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="setup.入驻_state_for_sequencerv2" />### `setup.入驻_state_for_sequencerv2`

下载给定定序器的入门状态。

**参数**

* `sequencerId`: `com.digitalasset.canton.拓扑.SequencerId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.google.protobuf.ByteString`

<div id="setup.snapshot" />

### `setup.snapshot`

在给定时间点下载定序器快照以引导另一个定序器。

建议使用 入驻\_state\_for\_sequencer 来载入新的定序器。

**参数**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**返回：** `com.digitalasset.canton.同步器.sequencer.SequencerSnapshot`

<div id="start_2"/>

### `start_2`

启动实例。

<div id="stop_2" />

### `stop_2`

停止实例。

<div id="同步器_id"/>

### `同步器_id`

返回同步器的逻辑同步器 ID。

**返回：** `com.digitalasset.canton.拓扑.同步器Id`

### 数据库

<div id="db.help_2" />

### `db.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="db.migrate_2" />

### `db.migrate_2`

如果使用数据库存储，则迁移实例的数据库。

当实例驻留在不同节点上时，它们的数据库迁移可以并行运行以节省时间。请注意，迁移命令必须在每个节点上单独运行，因为不支持通过`参与方s.remote...`进行远程迁移。

<div id="db.repair_migration_2" />

### `db.repair_migration_2`

仅在建议时使用 - 修复实例数据库的数据库迁移。

在极少数情况下，我们会在新版本中更改已应用的数据库迁移文件，并且修复命令会重置我们用来确保已应用的迁移文件通常没有更改的校验和。您应该只在建议时使用`db.repair_migration`，否则使用它需要您自担风险 - 在最坏的情况下，当随后错误地应用不兼容的数据库迁移（由于已应用的数据库迁移文件已更改而应被拒绝的迁移）时，运行它可能会导致数据损坏。

**参数**

* `force`: `Boolean`

### 同步器参数

<div id="同步器_parameters" />

### `同步器_parameters`

同步器参数相关命令。

**返回：** `SequencerReference.this.同步器_parameters.type`

### 健康

<div id="health.active_2" />

### `health.active_2`

检查节点是否正在运行并且是活动实例（中介者、参与者）。

**返回：** `Boolean`

<div id="health.dump_3" />

### `health.dump_3`

收集 Canton 系统信息以帮助诊断问题。

为本地 Canton 进程和任何连接的远程节点生成全面的运行状况报告。

论据是：

* `outputFile`：指定保存报告的文件路径。如果未设置，则使用默认路径。
* `timeout`：设置收集数据的自定义超时，对于来自慢速远程节点的大型报告很有用。
* `chunkSize`：调整来自远程节点的数据流块大小。使用它可以防止与“最大入站消息大小”相关的 gRPC 错误

**参数**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**返回：** `String`

<div id="health.has_identity_2" />

### `health.has_identity_2`

如果节点有身份，则返回 true。

**退货：** `Boolean`

<div id="health.help_3" />

### `health.help_3`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="health.initialized_2" />

### `health.initialized_2`

如果节点已初始化，则返回 true。

**返回：** `Boolean`

<div id="health.is_ready_for_id_2" />

### `health.is_ready_for_id_2`

检查节点是否准备好设置节点的 id。

**返回：** `Boolean`

<div id="health.is_ready_for_initialization_2" />

### `health.is_ready_for_initialization_2`

检查节点是否已准备好初始化。

**退货：** `Boolean`

<div id="health.is_ready_for_node_拓扑_2" />

### `health.is_ready_for_node_拓扑_2`

检查节点是否准备好上传节点的身份拓扑。

**退货：** `Boolean`

<div id="health.is_running_2" />

### `health.is_running_2`

检查节点是否正在运行。

**返回：** `Boolean`

<div id="health.last_error_trace_2" />

### `health.last_error_trace_2`显示最近间隔内使用给定traceId记录的所有消息。

返回与给定跟踪 ID 关联的缓冲日志消息列表。通常，trace-id 取自 last\_errors()

**参数**

* `traceId`: `String`

**返回：** `Seq[String]`

<div id="health.last_errors_2" />

### `health.last_errors_2`

显示最后记录的错误。

返回一个映射，其中 Trace-id 作为键，最新的错误消息作为值。要求启用（而不是关闭）--log-last-errors。

**返回：** `Map[String,String]`

<div id="health.set_log_level_2" />

### `health.set_log_level_2`

更改进程的日志级别。

如果使用默认的logback配置，这将改变进程的日志级别。

**参数**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_3" />

### `health.status_3`

获取人类（和机器）可读的状态信息。

**返回：** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity_2" />

### `health.wait_for_identity_2`

等待节点拥有身份。

<div id="health.wait_for_initialized_2" />

### `health.wait_for_initialized_2`

等待节点初始化。

<div id="health.wait_for_ready_for_id_2" />

### `health.wait_for_ready_for_id_2`

等待节点准备好设置节点的 id。

<div id="health.wait_for_ready_for_initialization_2" />

### `health.wait_for_ready_for_initialization_2`

等待节点准备好初始化。

<div id="health.wait_for_ready_for_node_拓扑_2" />

### `health.wait_for_ready_for_node_拓扑_2`

等待节点准备好上传节点的身份拓扑。

<div id="health.wait_for_running_2" />

### `health.wait_for_running_2`

等待节点运行。

### 密钥管理

<div id="keys.help_2" />

### `keys.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.download_2" />

### `keys.public.download_2`

下载公钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**返回：** `com.google.protobuf.ByteString`

<div id="keys.public.download_to_2" />

### `keys.public.download_to_2`

下载公钥并将其保存到文件中。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help_2" />

### `keys.public.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.list_2" />

### `keys.public.list_2`

列出注册表中的公钥。

返回已添加到密钥注册表中的所有公钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**返回：** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner_2" />

### `keys.public.list_by_owner_2`

列出给定 keyOwner 的密钥。

该命令是 `list_key_owners` 的便捷包装，采用显式 keyOwner 作为搜索参数。响应包括公钥。

**参数**

* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners_2" />

### `keys.public.list_owners_2`

列出具有给定搜索参数的键的活动所有者。

此命令允许深入检查拓扑状态。响应包括公钥。可选的filterKeyOwnerType类型可以是“参与方Id.Code”、“MediatorId.Code”、“SequencerId.Code”。

**参数**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.拓扑.MemberCode]`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload_2" />

### `keys.public.upload_2`

上传公钥。

导入公钥并将其与用于为该密钥提供一些上下文的名称一起存储。

**参数**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**返回：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from_2" />

### `keys.public.upload_from_2`

上传公钥。

**参数**

* `filename`: `String`
* `name`: `Option[String]`

**返回：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete_2" />

### `keys.secret.delete_2`

删除私钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download_2" />

### `keys.secret.download_2`

下载密钥对。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**退货：** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to_2" />

### `keys.secret.download_to_2`

下载密钥对并将其保存到文件中。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key_2" />

### `keys.secret.generate_encryption_key_2`

生成新的公钥/私钥对进行加密并将其存储在保管库中。

可选的名称参数允许您存储关联的字符串以方便使用。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**退货：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key_2" />

### `keys.secret.generate_signing_key_2`

生成新的公钥/私钥对用于签名并将其存储在保管库中。

可选的名称参数允许您存储关联的字符串以方便使用。用途指定签名密钥的预期用途，可以是：

* `Namespace`：用于定义节点身份并签署拓扑请求的根命名空间密钥；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id_2" />

### `keys.secret.get_wrapper_key_id_2`

获取用于加密私钥存储的包装器密钥 ID。

**返回：** `String`

<div id="keys.secret.help_2" />

### `keys.secret.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.secret.list_2" />

### `keys.secret.list_2`

列出私人保管库中的密钥。

将所有公钥返回到密钥保管库中相应的私钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**返回：** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key_2" />

### `keys.secret.register_kms_encryption_key_2`

在存储其公共信息的存储库中注册指定的 KMS 加密密钥。

KMS 加密密钥的 ID。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key_2" />

### `keys.secret.register_kms_signing_key_2`在州注册指定的 KMS 签名密钥，将其公共信息存储在保险库中。

KMS 签名密钥的 ID。用途指定签名密钥的预期用途，可以是：

* `Namespace`：根命名空间密钥，定义节点身份并签署拓扑请求；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key_2" />

### `keys.secret.rotate_kms_node_key_2`

使用新的预生成的 KMS 密钥对轮换给定节点的密钥对。

使用预生成的密钥轮换外部存储在 KMS 中的现有加密或签名密钥。注意：此命令无法轮换命名空间根签名密钥。我们要旋转的密钥的指纹。新 KMS 密钥的 ID（例如资源名称）。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key_2" />

### `keys.secret.rotate_node_key_2`

轮换节点的公钥/私钥对。

轮换现有加密或签名密钥。注意：此命令无法轮换命名空间根或中间签名密钥。我们要旋转的密钥的指纹。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys_2" />

### `keys.secret.rotate_node_keys_2`

轮换节点的公钥/私钥对。

对于参与者节点，它轮换签名和加密密钥对。对于定序器或中介器节点，它会轮换签名密钥对，因为这些节点没有加密密钥对。注意：此命令不会轮换命名空间根或中间签名密钥。

<div id="keys.secret.rotate_wrapper_key_2" />

### `keys.secret.rotate_wrapper_key_2`

更改加密私钥存储的包装密钥。

更改用于加密存储中的私钥的包装器密钥（例如 AWS KMS 密钥）。 newWrapperKeyId：要使用的可选新包装器密钥 ID。如果包装器密钥 ID 为空，Canton 将根据当前配置生成一个新密钥。

**参数**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload_2" />

### `keys.secret.upload_2`

上传密钥对。

上传之前下载的密钥对。 pairBytes：先前下载的密钥对的二进制表示形式名称：密钥对的（可选）描述性名称密码：用于解密加密密钥对的可选密码

**参数**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from_2" />

### `keys.secret.upload_from_2`

从文件上传（加载并导入）密钥对。

从文件中上传之前下载的密钥对。文件名：保存密钥对的文件的名称 名称：密钥对的（可选）描述性名称 密码：用于解密加密密钥对的可选密码

**参数**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### 指标

<div id="metrics.get_2" />

### `metrics.get_2`

获取特定指标。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point_2" />

### `metrics.get_double_point_2`

获得特定的双倍积分。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram_2" />

### `metrics.get_histogram_2`

获取特定的直方图。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point_2" />

### `metrics.get_long_point_2`

获得一个特定的长点。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**退货：** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary_2" />

### `metrics.get_summary_2`

获得具体的总结。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list_2" />

### `metrics.list_2`

列出所有指标。

返回具有给定名称和可选匹配属性的指标。

**参数**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

### 交通

<div id="流量_control.help_2" />

### `流量_control.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="流量_control.last_流量_state_update_of_members" />

### `流量_control.last_流量_state_update_of_members`

返回每个成员给定成员的最后一次交通状态更新。

使用此命令获取每个成员的最后一次流量状态更新。它将在会员消耗流量时最后更新。

**参数**

* `members`: `Seq[com.digitalasset.canton.拓扑.Member]`

**退货：** `com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status`

<div id="流量_control.set_流量_balance" />

### `流量_control.set_流量_balance`

设置会员的流量购买条目。

该命令用于设置成员新购买的流量表项。 member：要设置流量购买条目的成员serial：请求的序列号，必须严格大于该成员的最新更新newBalance：要设置的新流量购买条目

返回：用于更新的最大排序时间，并且只有在该时间之后，如果流量状态中仍然没有出现新的余额，则可以认为更新失败，应重试。

**参数**

* `member`: `com.digitalasset.canton.拓扑.Member`
* `serial`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `newBalance`: `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="流量_control.流量_state_2" />

### `流量_control.流量_state_2`

Return the 流量 state of the node.

使用此命令获取特定同步器 ID 在给定时间节点的流量状态。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`

**退货：** `com.digitalasset.canton.sequencing.protocol.流量State`

<div id="流量_control.流量_state_of_all_members" />

### `流量_control.流量_state_of_all_members`

返回所有成员的流量状态。

使用此命令可以获取所有成员的流量状态。将latestApproximate 设置为true，以获取排序器可以计​​算的最新可能时间戳处的流量状态（包括基本流量）的近似值。这只是一个近似值，因为定序器可能使用其挂钟，该挂钟可能超出同步器时间。

**参数**

* `latestApproximate`: `Boolean`

**返回：** `com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status`

<div id="流量_control.流量_state_of_members" />

### `流量_control.流量_state_of_members`

返回给定成员的流量状态。

使用此命令获取最新安全时间戳的成员列表的流量状态。

**参数**

* `members`: `Seq[com.digitalasset.canton.拓扑.Member]`

**退货：** `com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status`

<div id="流量_control.流量_state_of_members_approximate" />

### `流量_control.流量_state_of_members_approximate`

返回给定成员在最近大概时间的流量状态。使用此命令可以使用排序器可以估计状态的最晚可能时间来获取成员列表的流量状态。小心：返回的状态只是未来的近似状态，到同步器达到此时间戳时可能不是实际的正确状态。

**参数**

* `members`: `Seq[com.digitalasset.canton.拓扑.Member]`

**返回：** `com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status`

<div id="流量_control.流量_state_of_members_at_timestamp" />

### `流量_control.流量_state_of_members_at_timestamp`

Return the 流量 state of the given members at a specific timestamp.

使用此命令获取指定成员在给定时间戳的流量状态。

**参数**

* `members`: `Seq[com.digitalasset.canton.拓扑.Member]`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**返回：** `com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status`

## 调解器管理命令

<div id="clear_cache_1" />

### `clear_cache_1`

清除本地缓存的变量。

有些命令在客户端缓存值。使用此命令显式清除这些值的缓存。

<div id="config_1" />

### `config_1`

返回中介配置。

**返回：** `com.digitalasset.canton.同步器.mediator.MediatorNodeConfig`

<div id="help_2" />

### `help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="id_1"/>

### `id_1`

产生该中介者的中介者ID。 Throws an exception, if the id has not yet been allocated (e.g., the mediator has not yet been initialised).

**返回：** `com.digitalasset.canton.拓扑.MediatorId`

<div id="检查"/>

### `inspection`

中介者的检查功能。

**返回：** `com.digitalasset.canton.console.commands.MediatorInspectionGroup`

<div id="is_initialized_1" />

### `is_initialized_1`

检查本地实例是否正在运行并且已完全初始化。

**退货：** `Boolean`

<div id="is_running_1"/>

### `is_running_1`

检查本地实例是否正在运行。

**返回：** `Boolean`

<div id="maybeid_1"/>

### `maybeid_1`

如果 id 存在，则产生该中介者的 Some(id)。 Returns None, if the id has not yet been allocated (e.g., the mediator has not yet been initialised).

**返回：** `Option[com.digitalasset.canton.拓扑.MediatorId]`

<div id="setup.assign" />

### `setup.assign`

将中介者分配给同步器。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.Physical同步器Id`
* `sequencerConnections`: `com.digitalasset.canton.sequencing.SequencerConnections`
* `sequencerConnectionValidation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `waitForReady`: `Boolean`

<div id="setup.help" />

### `setup.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="start_1"/>

### `start_1`

启动实例。

<div id="stop_1" />

### `stop_1`

停止实例。

### 数据库

<div id="db.help_1" />

### `db.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="db.migrate_1" />

### `db.migrate_1`

如果使用数据库存储，则迁移实例的数据库。

当实例驻留在不同节点上时，它们的数据库迁移可以并行运行以节省时间。请注意，迁移命令必须在每个节点上单独运行，因为不支持通过`参与方s.remote...`进行远程迁移。

<div id="db.repair_migration_1" />

### `db.repair_migration_1`

仅在建议时使用 - 修复实例数据库的数据库迁移。

在极少数情况下，我们会在新版本中更改已应用的数据库迁移文件，并且修复命令会重置我们用来确保已应用的迁移文件通常没有更改的校验和。您应该只在建议时使用`db.repair_migration`，否则使用它需要您自担风险 - 在最坏的情况下，当随后错误地应用不兼容的数据库迁移（由于已应用的数据库迁移文件已更改而应被拒绝的迁移）时，运行它可能会导致数据损坏。

**参数**

* `force`: `Boolean`

### 健康

<div id="health.active_1" />

### `health.active_1`检查节点是否正在运行并且是活动实例（中介者、参与者）。

**返回：** `Boolean`

<div id="health.dump_2" />

### `health.dump_2`

收集 Canton 系统信息以帮助诊断问题。

为本地 Canton 进程和任何连接的远程节点生成全面的运行状况报告。

论据是：

* `outputFile`：指定保存报告的文件路径。如果未设置，则使用默认路径。
* `timeout`：设置收集数据的自定义超时，对于来自慢速远程节点的大型报告很有用。
* `chunkSize`：调整来自远程节点的数据流块大小。使用它可以防止与“最大入站消息大小”相关的 gRPC 错误

**参数**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**返回：** `String`

<div id="health.has_identity_1" />

### `health.has_identity_1`

如果节点有身份，则返回 true。

**返回：** `Boolean`

<div id="health.help_2" />

### `health.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="health.initialized_1" />

### `health.initialized_1`

如果节点已初始化，则返回 true。

**返回：** `Boolean`

<div id="health.is_ready_for_id_1" />

### `health.is_ready_for_id_1`

检查节点是否准备好设置节点的 id。

**退货：** `Boolean`

<div id="health.is_ready_for_initialization_1" />

### `health.is_ready_for_initialization_1`

检查节点是否已准备好初始化。

**返回：** `Boolean`

<div id="health.is_ready_for_node_拓扑_1" />

### `health.is_ready_for_node_拓扑_1`

检查节点是否准备好上传节点的身份拓扑。

**返回：** `Boolean`

<div id="health.is_running_1" />

### `health.is_running_1`

检查节点是否正在运行。

**返回：** `Boolean`

<div id="health.last_error_trace_1" />

### `health.last_error_trace_1`

显示最近间隔内使用给定traceId记录的所有消息。

返回与给定跟踪 ID 关联的缓冲日志消息列表。通常，trace-id 取自 last\_errors()

**参数**

* `traceId`: `String`

**退货：** `Seq[String]`

<div id="health.last_errors_1" />

### `health.last_errors_1`

显示最后记录的错误。

返回一个映射，其中 Trace-id 作为键，最新的错误消息作为值。要求启用（而不是关闭）--log-last-errors。

**返回：** `Map[String,String]`

<div id="health.set_log_level_1" />

### `health.set_log_level_1`

更改进程的日志级别。

如果使用默认的logback配置，这将改变进程的日志级别。

**参数**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_2" />

### `health.status_2`

获取人类（和机器）可读的状态信息。

**返回：** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity_1" />

### `health.wait_for_identity_1`

等待节点拥有身份。

<div id="health.wait_for_initialized_1" />

### `health.wait_for_initialized_1`

等待节点初始化。

<div id="health.wait_for_ready_for_id_1" />

### `health.wait_for_ready_for_id_1`

等待节点准备好设置节点的 id。

<div id="health.wait_for_ready_for_initialization_1" />

### `health.wait_for_ready_for_initialization_1`

等待节点准备好初始化。

<div id="health.wait_for_ready_for_node_拓扑_1" />

### `health.wait_for_ready_for_node_拓扑_1`

等待节点准备好上传节点的身份拓扑。

<div id="health.wait_for_running_1" />

### `health.wait_for_running_1`

等待节点运行。

### 密钥管理

<div id="keys.help_1" />

### `keys.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.download_1" />

### `keys.public.download_1`

下载公钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**返回：** `com.google.protobuf.ByteString`

<div id="keys.public.download_to_1" />

### `keys.public.download_to_1`

下载公钥并将其保存到文件中。

**参数*** `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help_1" />

### `keys.public.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.public.list_1" />

### `keys.public.list_1`

列出注册表中的公钥。

返回已添加到密钥注册表中的所有公钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**返回：** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner_1" />

### `keys.public.list_by_owner_1`

列出给定 keyOwner 的密钥。

该命令是 `list_key_owners` 的便捷包装，采用显式 keyOwner 作为搜索参数。响应包括公钥。

**参数**

* `keyOwner`: `com.digitalasset.canton.拓扑.Member`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**退货：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners_1" />

### `keys.public.list_owners_1`

列出具有给定搜索参数的键的活动所有者。

此命令允许深入检查拓扑状态。响应包括公钥。可选的filterKeyOwnerType类型可以是“参与方Id.Code”、“MediatorId.Code”、“SequencerId.Code”。

**参数**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.拓扑.MemberCode]`
* `同步器Ids`: `Set[com.digitalasset.canton.拓扑.同步器Id]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload_1" />

### `keys.public.upload_1`

上传公钥。

导入公钥并将其与用于为该密钥提供一些上下文的名称一起存储。

**参数**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**返回：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from_1" />

### `keys.public.upload_from_1`

上传公钥。

**参数**

* `filename`: `String`
* `name`: `Option[String]`

**返回：** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete_1" />

### `keys.secret.delete_1`

删除私钥。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download_1" />

### `keys.secret.download_1`

下载密钥对。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**返回：** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to_1" />

### `keys.secret.download_to_1`

下载密钥对并将其保存到文件中。

**参数**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key_1" />

### `keys.secret.generate_encryption_key_1`

生成新的公钥/私钥对进行加密并将其存储在保管库中。

可选的名称参数允许您存储关联的字符串以方便使用。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**返回：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key_1" />

### `keys.secret.generate_signing_key_1`

生成新的公钥/私钥对用于签名并将其存储在保管库中。

可选的名称参数允许您存储关联的字符串以方便使用。用途指定签名密钥的预期用途，可以是：* `Namespace`：根命名空间密钥，定义节点身份并签署拓扑请求；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。 keySpec 可用于选择关键规范，例如，使用哪个椭圆曲线，如果未指定，则使用默认规范。

**参数**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id_1" />

### `keys.secret.get_wrapper_key_id_1`

获取用于加密私钥存储的包装器密钥 ID。

**返回：** `String`

<div id="keys.secret.help_1" />

### `keys.secret.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="keys.secret.list_1" />

### `keys.secret.list_1`

列出私人保管库中的密钥。

将所有公钥返回到密钥保管库中相应的私钥。可选参数可用于过滤。

**参数**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**返回：** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key_1" />

### `keys.secret.register_kms_encryption_key_1`

在存储其公共信息的存储库中注册指定的 KMS 加密密钥。

KMS 加密密钥的 ID。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `name`: `String`

**退货：** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key_1" />

### `keys.secret.register_kms_signing_key_1`

在州注册指定的 KMS 签名密钥，将其公共信息存储在保险库中。

KMS 签名密钥的 ID。用途指定签名密钥的预期用途，可以是：

* `Namespace`：用于定义节点身份并签署拓扑请求的根命名空间密钥；
* `SequencerAuthentication`：用于向定序器验证网络成员身份的签名密钥；
* `Protocol`：用于处理作为协议一部分发生的所有签名的签名密钥。可选的名称参数允许您存储关联的字符串以方便使用。

**参数**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key_1" />

### `keys.secret.rotate_kms_node_key_1`

使用新的预生成的 KMS 密钥对轮换给定节点的密钥对。

使用预生成的密钥轮换外部存储在 KMS 中的现有加密或签名密钥。注意：此命令无法轮换命名空间根签名密钥。我们要旋转的密钥的指纹。新 KMS 密钥的 ID（例如资源名称）。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**返回：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key_1" />

### `keys.secret.rotate_node_key_1`

轮换节点的公钥/私钥对。

轮换现有加密或签名密钥。注意：此命令无法轮换命名空间根或中间签名密钥。我们要旋转的密钥的指纹。新密钥的可选名称。

**参数**

* `fingerprint`: `String`
* `name`: `String`

**退货：** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys_1" />

### `keys.secret.rotate_node_keys_1`

轮换节点的公钥/私钥对。

对于参与者节点，它轮换签名和加密密钥对。对于定序器或中介器节点，它会轮换签名密钥对，因为这些节点没有加密密钥对。注意：此命令不会轮换命名空间根或中间签名密钥。

<div id="keys.secret.rotate_wrapper_key_1" />

### `keys.secret.rotate_wrapper_key_1`

更改加密私钥存储的包装密钥。更改用于加密存储中的私钥的包装器密钥（例如 AWS KMS 密钥）。 newWrapperKeyId：要使用的可选新包装器密钥 ID。如果包装器密钥 ID 为空，Canton 将根据当前配置生成一个新密钥。

**参数**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload_1" />

### `keys.secret.upload_1`

上传密钥对。

上传之前下载的密钥对。 pairBytes：先前下载的密钥对的二进制表示形式名称：密钥对的（可选）描述性名称密码：用于解密加密密钥对的可选密码

**参数**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from_1" />

### `keys.secret.upload_from_1`

从文件上传（加载并导入）密钥对。

从文件中上传之前下载的密钥对。文件名：保存密钥对的文件的名称 名称：密钥对的（可选）描述性名称 密码：用于解密加密密钥对的可选密码

**参数**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### 指标

<div id="metrics.get_1" />

### `metrics.get_1`

获取特定指标。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point_1" />

### `metrics.get_double_point_1`

获得特定的双倍积分。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram_1" />

### `metrics.get_histogram_1`

获取特定的直方图。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point_1" />

### `metrics.get_long_point_1`

获得一个特定的长点。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**退货：** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary_1" />

### `metrics.get_summary_1`

获得具体的总结。

返回具有给定名称和可选匹配属性的指标，如果找到多个匹配，则返回错误。

**参数**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**退货：** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list_1" />

### `metrics.list_1`

列出所有指标。

返回具有给定名称和可选匹配属性的指标。

**参数**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**返回：** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

### 定序器连接

<div id="sequencer_connection.get" />

### `sequencer_connection.get`

获取定序器连接。

使用此命令获取此定序器客户端当前配置的定序器连接详细信息。如果该节点尚未初始化，则返回 None。

**返回：** `Option[com.digitalasset.canton.sequencing.SequencerConnections]`

<div id="sequencer_connection.help" />

### `sequencer_connection.help`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="sequencer_connection.logout" />

### `sequencer_connection.logout`

撤销此定序器客户端节点的身份验证令牌并关闭所有定序器连接。

在所有定序器上，该定序器客户端节点的所有现有身份验证令牌都将被撤销。请注意，该节点并未与同步器断开连接；仅关闭与定序器的连接。节点将自动重新打开连接，执行质询-响应并获取新的令牌。

<div id="sequencer_connection.modify" />

### `sequencer_connection.modify`

修改默认定序器连接。通过传递对现有默认连接进行操作的修改器函数，修改此定序器客户端节点的定序器连接详细信息。

**参数**

* `modifier`: `[com.digitalasset.canton.sequencing.SequencerConnection => com.digitalasset.canton.sequencing.SequencerConnection](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/sequencing/SequencerConnection.html)`

<div id="sequencer_connection.modify_connections" />

### `sequencer_connection.modify_connections`

修改定序器连接。

通过传递对现有连接配置进行操作的修改器函数，修改此定序器客户端节点的定序器连接详细信息。

**参数**

* `modifier`: `[com.digitalasset.canton.sequencing.SequencerConnections => com.digitalasset.canton.sequencing.SequencerConnections](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/sequencing/SequencerConnections.html)`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="sequencer_connection.set" />

### `sequencer_connection.set`

设置定序器连接。

为此定序器客户端节点设置新的定序器连接详细信息。这将替换任何预先配置的连接详细信息。该命令仅在节点初始化后才起作用。

**参数**

* `connections`: `com.digitalasset.canton.sequencing.SequencerConnections`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="sequencer_connection.set_single" />

### `sequencer_connection.set_single`

设置定序器连接。

为此定序器客户端节点设置新的定序器连接详细信息。这将替换任何预先配置的连接详细信息。该命令仅在节点初始化后才起作用。

**参数**

* `connection`: `com.digitalasset.canton.sequencing.SequencerConnection`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

### 测试

<div id="修剪.clear_schedule_2" />

### `修剪.clear_schedule_2`

停用自动修剪。

<div id="修剪.find_修剪_timestamp" />

### `修剪.find_修剪_timestamp`

获取调解器状态开始处或附近的时间戳。

当使用默认值 `index` 1 调用时，此命令可以深入了解中介器修剪的当前状态。当通过 `prune_at` 手动修剪中介器并打算批量修剪时，请指定一个值（例如 1000）以获取与批次“结束”相对应的修剪时间戳。

**参数**

* `index`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**返回：** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="修剪.get_schedule_1" />

### `修剪.get_schedule_1`

检查自动修剪计划。

该计划由“cron”表达式和“max\_duration”和“retention”持续时间组成。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。如果尚未通过 `set_schedule` 配置计划或已调用 `clear_schedule`，则返回 `None`。

**退货：** `Option[com.digitalasset.canton.admin.api.client.data.修剪Schedule]`

<div id="修剪.help_2" />

### `修剪.help_2`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="修剪.prune_1" />

### `修剪.prune_1`

修剪调解器中不必要的数据，同时将数据保留在默认保留期内。

从中介器中删除早于默认保留期的不必要数据。默认保留期限在`parameters.retention-period-defaults.mediator`下运行此命令的canton节点的配置中设置。

<div id="修剪.prune_at" />

### `修剪.prune_at`

修剪调解器中不必要的数据，直到给定的时间戳（包括给定的时间戳）。

**参数**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

<div id="修剪.prune_with_retention_period"/>

### `修剪.prune_with_retention_period`

修剪调解器中不必要的数据，同时在提供的保留期内保留数据。

**参数**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`

<div id="修剪.set_cron_1" />

### `修剪.set_cron_1`修改自动修剪使用的cron。

该计划以 cron 格式指定，指的是 GMT 时区的修剪开始时间。如果未通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `cron`: `String`

<div id="修剪.set_max_duration_1" />

### `修剪.set_max_duration_1`

修改自动修剪使用的最大持续时间。

`maxDuration` 被指定为正持续时间并且最多具有每秒粒度。如果未通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在进行此修改时，修剪正在主动运行，则将尽力暂停修剪并根据新的时间表重新启动。这允许新计划当前不再允许修剪的情况。

**参数**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_retention_1" />

### `修剪.set_retention_1`

更新自动修剪使用的修剪保留。

`retention` 被指定为正持续时间并且最多具有每秒粒度。如果未通过 `set_schedule` 配置计划，或者已通过 `clear_schedule` 禁用自动修剪，则此调用将返回错误。此外，如果在此更新时，修剪正在主动运行，则会尽力暂停修剪并以新指定的保留重新启动。这允许新的保留要求保留比以前更多的数据。

**参数**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="修剪.set_schedule_2" />

### `修剪.set_schedule_2`

根据指定的时间表激活自动修剪。

该计划以 cron 格式以及“max\_duration”和“retention”持续时间指定。 cron 字符串指示在 GMT 时区中应开始修剪的时间点，最大持续时间指示只要修剪尚未完成修剪直到指定的保留期限，允许修剪从开始时间运行多长时间。

**参数**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="testing.await_同步器_time_2" />

### `testing.await_同步器_time_2`

等待同步器达到给定时间。

**参数**

* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.fetch_同步器_time_2" />

### `testing.fetch_同步器_time_2`

从同步器获取当前时间。

**参数**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**返回：** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.help_1" />

### `testing.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

### 交通

<div id="流量_control.help_1" />

### `流量_control.help_1`

特定命令的帮助（使用 help() 或 help("method") 获取更多信息）。

**参数**

* `methodName`: `String`

<div id="流量_control.流量_state_1" />

### `流量_control.流量_state_1`

返回节点的流量状态。

使用此命令获取特定同步器 ID 在给定时间节点的流量状态。

**参数**

* `同步器Id`: `com.digitalasset.canton.拓扑.同步器Id`

**返回：** `com.digitalasset.canton.sequencing.protocol.流量State`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
