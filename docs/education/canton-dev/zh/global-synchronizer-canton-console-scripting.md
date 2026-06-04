---
title: "脚本编写"
slug: "global-synchronizer-canton-console-scripting"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/scripting.md"
source_title: "Scripting"
tags:
  - global-synchronizer
  - canton-console
  - scripting
---

# 脚本编写

> Canton Console 脚本化与自动化运维模式。

> 使用 Scala 为 Canton 控制台编写脚本

Canton 控制台基于 [Ammonite](http://ammonite.io) 构建，这是一个基于 Scala 的脚本和 REPL 框架。您键入的每个命令都是有效的 Scala，这意味着您可以像在任何 Scala 程序中一样编写循环、定义函数、绑定变量和组合操作。

本页涵盖了脚本编写的实用方面：如何编写 `.canton` 脚本文件、如何运行它们以及自动化操作员任务的常见模式。

## 控制台中的 Scala 基础知识

控制台接受标准 Scala 语法。一些模式在操作员脚本中反复出现。

**变量绑定**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val id = participant1.id
    id : ParticipantId = PAR::participant1::12201ff69b1d...
```

**字符串插值**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ println(s"Participant ID: $id")
```

**集合和迭代**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participants.all.foreach { p => println(s"${p.name}: ${p.health.status}") }
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status match { case status if status.isActive.contains(true) => println("Healthy"); case _ => println("Check this node") }
```

为了方便起见，控制台还提供隐式类型转换。当命令需要 `SynchronizerAlias`、`Fingerprint` 或 `Identifier` 时，您可以传递普通的 `String`，它将自动转换。

## 加载并运行脚本文件

按照惯例，广东脚本使用 `.canton` 文件扩展名。您可以通过两种方式运行它们。

**启动时运行脚本**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run myscript.canton -c myconfig.conf
```

这将启动控制台，执行脚本，然后退出。这是无人值守自动化的标准方法。

**在控制台内加载脚本**

从交互式会话中，使用 Ammonite 的 `interp.load` 机制或 `utils` 帮助程序加载脚本文件：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
utils.run_script("path/to/myscript.canton")
```

您还可以将已编译的 JAR（例如，Daml codegen 绑定）加载到控制台中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
interp.load.cp(os.Path("codegen.jar", base = os.pwd))

@ // the @ triggers compilation so imports are available afterward

import com.myorg.mypackage._
```

**引导脚本**

控制台启动时会自动运行引导脚本：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c myconfig.conf --bootstrap myscript.canton
```

与`run`不同，引导脚本完成后控制台保持打开状态，这对于设置初始状态然后切换到交互使用非常有用。

## 超时

控制台命令超时在 Canton 配置文件中配置：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters.timeouts.console {
  bounded = 1.minute
  unbounded = 10.minutes
}

```

* `bounded` 适用于预计在已知持续时间内完成的命令。
* `unbounded` 适用于完成时间不可预测的长时间运行的命令。

您还可以直接在脚本命令中传递超时：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1, timeout = 30.seconds)
    res5: Duration = 1875 milliseconds
```

控制台默认导入 `scala.concurrent.duration._`，因此像 `10.seconds` 和 `1.minute` 这样的表达式无需额外导入即可工作。

## 自动化模式

### 健康检查

一个简单的健康检查脚本，用于验证所有本地节点是否正在运行：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ nodes.local.foreach { node => val status = node.health.status; if (!status.isActive.getOrElse(false)) { println(s"WARNING: ${node.name} is not active") } }
```

对于两个参与者之间的定向 ping 测试：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val roundTrip = participant1.health.ping(participant2, timeout = 30.seconds)
    roundTrip : Duration = 1823 milliseconds
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ println(s"Round trip: ${roundTrip}")
```

### 批量操作

将 DAR 上传给所有本地参与者：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res9: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

通用节点引用（`participants.local`、`participants.remote`、`participants.all`）直接支持批量操作。当您需要更多控制时，您还可以迭代：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participants.all.foreach { p => println(s"DARs on ${p.name}: ${p.dars.list().size}") }
```

### 具有外部编排的计划任务

Canton 控制台不包含内置调度程序。对于重复任务，请从外部调度程序（例如 `cron` 或 Kubernetes CronJob）调用 `.canton` 脚本：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# crontab entry: run health check every 5 minutes
*/5 * * * * /opt/canton/bin/canton run /opt/canton/scripts/health-check.canton -c /opt/canton/config/remote-participant.conf
```

这种方法将自动化逻辑保留在版本控制的`.canton`文件中，同时依赖经过实战考验的调度基础设施。

## 常见脚本编写方法

### 列出已连接的同步器

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected().foreach { sync => println(s"Connected to: ${sync.synchronizerAlias}") }
```

### 检查聚会主办情况

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list().foreach { party => println(s"Party: ${party.party}") }
```

### 导出和导入 DAR

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Export all DARs to a directory
participant1.dars.download("backup/dars/")

// Upload a DAR
participant1.dars.upload("backup/dars/my-model.dar")
```

### 远程管理

如果您的节点作为守护进程运行，您可以从远程控制台针对它们编写脚本。在您的配置中配置远程参与者：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
  admin-api {
    address = "participant-host"
    port = 5012
  }
  ledger-api {
    address = "participant-host"
    port = 5011
  }
}
```

然后针对远程节点运行脚本：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run myscript.canton -c remote-config.conf
```

<Note>
  Some commands are only available from the local console of the node process itself. Remote consoles cover most administrative operations, but a few low-level operations require local access.
</Note>

## 制作脚本的技巧

* 始终指定显式超时而不是依赖默认值。无限期挂起的脚本比快速失败的脚本更难诊断。
* 在可能失败的操作周围使用`try/catch`块，尤其是网络调用和DAR上传。
* 使用`println`记录输出或写入文件——默认情况下控制台不会保留输出。
* 尽可能保持脚本幂等。如果脚本可以安全地重新运行，那么从部分故障中恢复就很简单。
* 在生产中运行脚本之前，先在 LocalNet 环境中测试脚本。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
