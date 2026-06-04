---
title: "高级 Canton Console"
slug: "global-synchronizer-production-operations-canton-console"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/canton-console.md"
source_title: "Advanced Canton Console"
tags:
  - global-synchronizer
  - production-operations
  - canton-console
---

# 高级 Canton Console

> 使用 Canton 管理控制台进行高级节点运维。

> 使用 Canton 管理控制台对参与者和同步节点进行高级操作。


Canton 提供了一个控制台 (REPL)，可以在其中动态启动和停止实体，并且可以运行各种管理或调试命令。

所有控制台命令都必须是有效的 Scala（控制台基于 [Ammonite]() - 基于 Scala 的脚本和 [REPL]() 框架）。请注意，我们还定义了一组隐式类型 [conversions]() 来提高控制台可用性：值得注意的是，每当控制台命令需要 [synchronizerAlias]()、[Fingerprint]() 或 [Identifier]() 时，您也可以使用 `String` 来调用它，它将自动转换为正确的类型。

`examples/`子目录包含一些示例脚本，扩展名为`.canton`。

<div className="contents" local="">
  内容
</div>

命令是按主题组组织的。某些命令还需要通过配置指令显式打开才能访问。

有些操作在两种类型的节点上都可用，而有些操作特定于参与节点或同步器。为了保持一致性，我们按节点类型组织手册，这意味着某些命令会出现两次。然而，详细的解释仅在参与者文档中给出。

## 远程管理

Canton 控制台可与本地进程内节点和远程节点配合使用。配置网络地址、端口和身份验证信息后，您可以使用单个 Canton 控制台来管理系统中的所有节点。

例如，您之前可能已使用类似以下内容在守护进程模式下启动了 Canton 实例：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton daemon -c <some config>
```

然后，您可以使用 `remote-participant` 配置针对此正在运行的参与者执行命令，例如：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Example remote participant configuration

// Include TLS configuration
include required("../tls/mtls-admin-api.conf")
include required("../tls/tls-ledger-api.conf")
canton {
    remote-participants.participant {
        ledger-api {
            address = localhost
            port = 10001
            tls = ${?_shared.ledger-api-client-tls}
        }
        admin-api {
            address = localhost
            port = 10002
            tls = ${?_shared.admin-api-client-mtls}
        }
    }
}
```

给定远程配置文件，启动本地 Canton 控制台，配置为在远程 Canton 实例上执行命令，如下所示：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c config/remote-participant1.conf
```

此外，您可以使用远程配置来运行脚本：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run <some-canton-script> -c config/remote-participant1.conf
```

请注意，大多数 Canton 命令可以从远程控制台执行。然而，一些命令只能从节点本身的本地控制台调用。

给定参与者的配置文件，您可以使用 `generate` 命令生成框架远程配置文件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton generate remote-config -c participant1.conf
```

根据您的网络，您可能需要手动编辑自动生成的配置来调整主机名。要访问多个远程节点，请将自动生成的配置合并到单个远程配置文件中或在命令行上包含所有配置文件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c participant1.conf,participant2.conf,mySynchronizer.conf
```

### TLS 和授权

对于生产用例，特别是如果管理 API 不仅仅绑定到本地主机，我们建议启用具有相互身份验证的 TLS。

只要远程控制台具有有效的访问令牌，就可以在使用授权的安装中使用。这可以通过修改配置或向远程控制台的启动命令添加选项来实现，如以下代码片段所示：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton daemon \
   -c remote-participant1.conf \
   -C canton.remote-participants.<remote-participant-name>.token="<encoded-and-signed-access-token-as-string>" \
   --bootstrap <some-script>
```

远程控制台在与目标参与者的 Ledger API 交互时使用该令牌。它还从令牌中提取用户 ID，并使用它来填充命令提交和完成订阅请求中的 userId 字段。这会影响以下控制台命令：

* ledger_api.commands.submit
* ledger_api.commands.submit\_flat
* ledger_api.commands.submit\_async
* ledger_api.completions.list
* ledger_api.completions.list\_with\_checkpoint
* ledger_api.completions.subscribe

<div className="todo">
  #22917: 修复损坏的参考注释:: 如果您想了解有关授权的更多信息，请阅读以下有关 ref:authorization tokens 的文章
</div>

## 节点参考

要在特定节点上发出命令，您必须通过其引用来引用它，该引用是一个 Scala 变量。命名变量是使用其配置的标识符为所有同步器实体和参与者创建的。例如，示例`examples/01-simple-拓扑/simple-拓扑.conf`配置文件引用同步器`mySynchronizer`以及参与者`participant1`和`participant2`。这些在控制台中可用为 `mySynchronizer`、`participant1` 和 `participant2`。

该控制台还提供其他通用参考，允许您按类型查阅节点列表。通用节点引用支持每种节点类型的三个子集：本地、远程或该类型的所有节点。对于参与者，您可以使用：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.local
participants.remote
participants.all
```

通用节点引用可以以 Scala 语法方式使用：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.all.foreach(_.dars.upload("my.dar"))
```

但参与者参考还支持一些通常必须同时对多个节点执行的操作的通用命令，例如：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.local.dars.upload("my.dar")
```

可用的节点参考有：

\<控制台主题标记：通用节点引用>

## 帮助

如果您寻求帮助，坎顿会非常有帮助。尝试输入

帮助

或

参与者1.help()

获取现有命令和命令组的概述。 `help()`适用于各个级别（例如`participant1.synchronizers.help()`），或者可用于搜索特定功能（`help("list")`）或获取每个命令的详细帮助说明（`participant1.parties.help("list")`）。

## 生命周期操作

这些由同步器和参与者的个体和序列支持。如果调用序列，则操作将按照序列的顺序依次调用。例如：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nodes.local.start()
```

可用于启动所有已配置的本地同步器和参与者。

如果节点运行数据库持久化，它将支持数据库迁移命令（`db.migrate`）。第一次启动节点时会自动执行迁移。但是，作为软件新版本的一部分添加的新迁移默认情况下必须使用该命令手动运行。在极少数情况下，可能还需要在运行`db.migrate`之前运行`db.repair_migration` - 请参阅`db.repair_migration`的说明了解更多详细信息。如果需要，还可以通过使用以下配置选项启用“迁移并启动”模式来自动执行数据库迁移：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.storage.parameters.migrate-and-start = yes

```

请注意，数据连续性（以及数据库迁移）仅保证在次要版本和补丁版本更新中有效。

同步器、Sequencer和Mediator 节点可能需要额外的设置才能完全正常工作。检查同步器引导以了解更多详细信息。

## 超时

可以使用配置文件中相应的控制台命令超时部分来配置控制台命令超时：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters.timeouts.console = {
    bounded = 2.minutes
    unbounded = Inf // infinity
    ledger-command = 2.minutes
    ping = 30.seconds
}
```

`bounded` 参数用于处理完成后应完成的所有命令，而 `unbounded` 超时用于我们不控制处理时间的命令。这尤其适用于可能运行时间很长的命令。

某些命令具有特定的超时参数，可以将其作为类型 `NonNegativeDuration` 显式传递。为了方便起见，控制台默认包含 `scala.concurrent.duration._` 的隐式转换以及从 Scala 类型 `scala.concurrent.duration.FiniteDuration` 到 `NonNegativeDuration` 的隐式转换。因此，您可以使用普通的 Scala 表达式并将超时编写为

参与者1.health.ping（参与者1，超时= 10.秒）

而隐式转换将负责将其转换为正确的类型。

通常，无需重新配置超时，我们建议使用安全的默认值。

## 在控制台中生成代码

Daml SDK 提供代码生成 [实用程序]()，为 Daml 模型创建 **Java** 或 **Scala** 绑定。这些绑定是从控制台以键入方式与分类账进行交互的便捷方式。链接的文档解释了如何使用 `daml` 命令创建这些绑定。 **Scala** 绑定不受官方支持，因此不应用于应用程序开发。

成功构建绑定后，您可以使用控制台脚本中神奇的 **Ammonite** 导入技巧将生成的 `jar` 加载到 Canton 控制台中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
interp.load.cp(os.Path("codegen.jar", base = os.pwd))

@ // the at triggers the compilation such that we can use the imports subsequently

import ...
```

## 广州管理 API

Canton 提供控制台作为管理交互的内置模式。然而，在幕后，所有管理控制台操作都是使用管理 gRPC API 来实现的。因此，还可以编写自己的管理应用程序并将其连接到管理 gRPC 端点。

发布工件中的 `protobuf/` 子目录包含 gRPC 底层协议缓冲区。特别是，管理 gRPC API 位于 `admin` 子目录中。

例如，Ping Pong 服务实现了一个简单的工作流程来对部署进行冒烟测试，它是使用协议缓冲区`*/protobuf/*/admin/*/ping_pong_service.proto`（其中`*`表示中间目录）定义的。然后控制台命令 health.ping 使用该服务。

协议缓冲区也可在 [repository]() 中使用，遵循如上所述的类似子目录结构。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
