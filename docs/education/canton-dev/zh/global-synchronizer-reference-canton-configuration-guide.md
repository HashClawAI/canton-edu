---
title: "Canton 配置指南"
slug: "global-synchronizer-reference-canton-configuration-guide"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/canton-configuration-guide.md"
source_title: "Canton Configuration Guide"
tags:
  - global-synchronizer
  - reference
  - canton-configuration-guide
---

# Canton 配置指南

> 使用 HOCON 与命令行配置 Canton 节点的完整指南。

> 使用 HOCON 文件、命令行选项和声明性配置配置 Canton 节点

解释静态配置和动态配置之间的区别。将特定配置部分从此处移至其操作方法部分，例如下面的多同步器。

# 设置配置选项

Canton 区分静态配置和动态配置。静态配置是不可变的，因此必须从流程一开始就知道。对于静态配置，示例是本地持久性存储的连接参数或管理 API 应绑定到的端口。另一方面，连接到同步器或添加各方不是静态配置的问题，因此不是通过配置文件设置，而是通过控制台命令（或管理 API）设置。

<图>
  <图片src =“https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/global-synchronizer/reference/images/canton_ node_initialization.png?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=b2b5178e74e90b16dab27d888c0f88ba" alt="./images/canton_node_initialization.png" width="880" height="300" data-path="global-synchronizer/reference/images/canton_node_initialization.png" />
</图>

配置文件本身以 [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) 格式编写，并带有一些扩展名：

* 持续时间是使用 `<length><unit>` 格式指定的 scala 持续时间。有效单位由 [scala](https://github.com/scala/scala/blob/v2.13.3/src/library/scala/concurrent/duration/Duration.scala#L82) 直接定义，但使用 `ms`、`s`、`m`、`h`、`d` 来引用，其行为与预期一致毫秒、秒、分钟、小时和天。在我们的上下文中，持续时间必须是非负的。

Canton 运行的不是一个节点，而是任意数量的节点，无论是同一进程中的同步器还是参与者节点。因此，根配置允许定义同步器和参与者节点的多个实例以及一组通用过程参数。

下面可以看到两个参与节点和单个同步器的示例配置文件。

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    // user-manual-entry-begin: SimpleSequencerNodeConfig
    sequencers {
      sequencer1 {
        storage.type = memory
        public-api.port = 5001
        admin-api.port = 5002
        sequencer.type = BFT
      }
    }
    // user-manual-entry-end: SimpleSequencerNodeConfig

    // user-manual-entry-begin: SimpleMediatorNodeConfig
    mediators {
      mediator1 {
        storage.type = memory
        admin-api.port = 5202
      }
    }
    // user-manual-entry-end: SimpleMediatorNodeConfig

    参与方s {
      // user-manual-entry-begin: port configuration
      participant1 {
        storage.type = memory
        admin-api.port = 5012
        ledger-api.port = 5011
        http-ledger-api.port = 5013
      }
      // user-manual-entry-end: port configuration
      参与方2 {
        storage.type = memory
        admin-api.port = 5022
        ledger-api.port = 5021
        http-ledger-api.port = 5023
      }
    }
  }

```

## 配置参考

静态属性的 Canton 配置文件基于 [PureConfig](https://pureconfig.github.io/)。 PureConfig 将 Scala 案例类及其类结构映射到模拟配置选项（例如，请参阅 [PureConfig 快速入门](https://pureconfig.github.io/docs/#quick-start) 的示例）。因此，所有可用配置选项和配置文件语法的最终真实来源由 [CantonConfig Scala 参考](https://docs.canton.network/reference/scala/com-digitalasset-canton-config/cantonconfig) 和 `com.digitalasset.canton.config` 中的相关类型给出。

在理解从 scaladocs 到配置的映射时，请记住：

* CamelCase Scala 名称映射为配置文件中带破折号的小写名称，例如scaladocs 中的`同步器Parameters` 变成配置文件中的`同步器-parameters`（破折号，而不是下划线）。
* `Option[<scala-class>]` 表示配置可以指定但不需要指定，例如您可以通过 [Remote参与方Config](https://docs.canton.network/reference/scala/com-digitalasset-canton-participant-config/remoteparticipantconfig) 中的 `token=token` 指定 JWT 令牌，但不指定 `token` 也是有效的。

## 配置兼容性企业版配置文件扩展了社区配置。因此，任何社区配置都可以使用企业二进制文件运行，但并非每个企业配置文件也可以使用社区版本。

## 高级配置

配置文件可以嵌套并组合在一起。首先，使用 `include required` 指令（带有相对路径），配置文件可以包含其他配置文件。

```
canton {
    同步器s {
        include required(file("同步器1.conf"))
    }
}
```

如果包含的文件不存在，`required`关键字将触发错误；如果没有 `required` 关键字，任何丢失的文件都将被默默忽略。 `file`关键字指示配置解析器将其参数解释为文件名；如果没有此关键字，解析器可能会将给定名称解释为 URL 或类路径资源。通过使用`file`关键字，你还将获得`include`最直观的语义和最稳定的语义。解析相对路径的精确规则可以在[此处](https://github.com/lightbend/config/blob/master/HOCON.md#include-semantics- located-resources)找到。

其次，通过提供多个配置文件，我们可以使用显式配置选项路径覆盖配置设置：

```
canton.参与方s.my参与方.admin-api.port = 11234
```

如果多个配置中包含相同的键，则最后一个定义具有最高优先级。

此外，HOCON 支持使用语法 `key = ${ENV_VAR_NAME}` 或可选替换 `key = ${?ENV_VAR_NAME}` 来替换配置值的环境变量，其中仅当环境变量存在时才会设置密钥。

## 配置混入

甚至不仅仅是多个配置文件，我们还可以利用 [PureConfig](https://github.com/pureconfig/pureconfig) 来创建引用环境变量的共享配置项。下面是一个方便的示例，它允许在涉及多个同步器或参与者节点的设置中共享数据库配置设置：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Postgres persistence configuration mixin
#
# This file defines a shared configuration resources. You can mix it into your configuration by
# refer to the shared storage resource and add the database name.
#
# Example:
#   participant1 {
#     storage = ${_shared.storage}
#     storage.config.properties.databaseName = "参与方1"
#   }
#
# The user and password is not set. You want to either change this configuration file or pass
# the settings in via environment variables POSTGRES_USER and POSTGRES_PASSWORD.
#
_shared {
    storage {
        type = postgres
        config {
            dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
            properties = {
                serverName = "localhost"
                # the next line will override above "serverName" in case the environment variable POSTGRES_HOST exists
                # which makes it optional
                serverName = ${?POSTGRES_HOST}
                portNumber = "5432"
                portNumber = ${?POSTGRES_PORT}
                # user and password are required
                user = ${POSTGRES_USER}
                password = ${POSTGRES_PASSWORD}
            }
        }
        parameters {
            # If defined, will configure the number of database connections per node.
            # Please note that the number of connections can be fine tuned for 参与方节点s (see 参与方.conf)
            max-connections = ${?POSTGRES_NUM_CONNECTIONS}
            # If true, then database migrations will be applied on startup automatically
            # Otherwise, you will have to run the migration manually using 参与方.db.migrate()
            migrate-and-start = false
            # If true (default), then the node will fail to start if it can not connect to the database.
            # The setting is useful during initial deployment to get immediate feedback when the
            # database is not available.
            # In a production setup, you might want to set this to false to allow uncoordinated startups between
            # the database and the node.
            fail-fast-on-startup = true
        }
    }
}
```

随后可以在实际的节点定义中引用这样的定义：```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
    同步器s {
        my同步器 {
            storage = ${_shared.storage}
            storage.config.properties.databaseName = ${CANTON_DB_NAME_SYNCHRONIZER}
        }
    }
}
```

## 多个同步器

Canton 配置允许您定义多个同步器。此外，Canton 参与者可以连接到多个同步器。然而，这仅作为预览功能支持，尚不适合生产使用。

特别是，合约密钥的唯一性不能在多个同步器上强制执行。在这种情况下，您必须在 Canton 配置中关闭合约密钥唯一性。请注意，该设置是最终设置，以后无法更改。一旦多同步器功能完全实现，我们将提供迁移路径。

## 快速失败模式

默认情况下，如果 Canton 无法访问某些外部依赖项（例如数据库），则 Canton 将无法启动。这在初始部署和开发期间是更可取的，因为它提供即时反馈，但可能会在生产中引起问题。例如，如果 Canton 与数据库并行启动，如果在 Canton 进程尝试访问数据库之前数据库尚未准备好，则 Canton 进程将会失败。为了避免此问题，您可以将节点配置为无限期等待外部依赖项（例如数据库）启动。下面的配置选项将禁用 `参与方1` 的“快速失败”行为。

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.参与方s.参与方1.storage.parameters.fail-fast-on-startup = "no"

```

应谨慎使用此选项，因为根据设计，它可能会导致无限的、嘈杂的等待。

## 初始化配置

某些配置值仅在节点的首次初始化期间使用，之后无法更改。这些值位于节点相关配置的`init`部分下。下面是一个示例，其中包含参与者配置的一些初始值

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1 {
  init {
    // example settings
    ledger-api.max-deduplication-duration = 1 minute
    identity.node-identifier.type = random
  }
}
```

选项`ledger-api.max-deduplication-duration`设置参与者用于命令重复数据删除的最大重复数据删除持续时间。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/configure/general/command_line.rst" hash="5d37a7f5" */}

# 使用 Canton 命令行

Canton 支持多种命令行参数。请运行`bin/canton --help`查看所有内容。在这里，我们解释最相关的内容。

## 选择配置

Canton 需要配置文件才能运行。没有内置的默认拓扑配置，因此，用户至少需要定义哪种节点（同步器或参与者）以及他们想要在给定进程中运行的节点数量。示例配置文件可以在我们的发布包中的`examples`目录下找到。

启动 Canton 时，可以使用以下方式提供配置文件

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton --config conf_filename -c conf_filename2
```

它将通过将`conf_filename2`的内容合并到`conf_filename`来启动Canton。选项 `-c` 和 `--config` 是等效的。如果多个配置文件将值分配给同一个键，则采用*最后*值。静态配置部分解释了如何编写配置文件。

您还可以在命令行上单独或与配置文件一起指定配置参数，以指定缺少的参数或覆盖其他参数。这对于提供简单的简短配置信息非常有用。可以使用`-C`提供配置参数：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton --config conf_filename -C canton.参与方s.参与方1.storage.type=memory
```

## 运行模式

您可以根据所需的环境和任务以各种模式运行 Canton。

### 交互式控制台

运行 Canton 的默认方法是交互模式。该过程将启动一个命令行界面（REPL），可以方便地操作、修改和检查 Canton 应用程序。

在此模式下，所有错误都会以 `CommandExecutionException` 的形式报告给控制台，但 Canton 将继续运行。交互式控制台可以使用 `--bootstrap=...` 选项与脚本一起启动。该脚本使用与控制台相同的语法。

交互模式对于开发、教育和专家使用很有用。

### 守护进程

如果不需要控制台，例如在服务器操作中，Canton 可以以守护程序模式启动

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton daemon --config ...
```

所有配置的实体将自动启动并恢复运行。

连接到数据库存储失败将导致进程以非零退出代码退出。可以使用以下方法关闭此功能：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.参与方s.参与方1.storage.parameters.fail-fast-on-startup = "no"

```

运行引导脚本时遇到的任何故障都将立即以非零退出代码关闭 Canton 进程。

以守护进程模式启动的节点可以通过设置提供交互式用户体验的远程控制台进行管理，同时节点在单独的进程中运行。

### 沙盒

在开发过程中，使用给定的 DAR 运行轻量级账本可能会很有用。为此，您可以在沙盒模式下运行 Canton，该模式运行 Daml 沙盒。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton sandbox --dar Main.dar ...
```

### 无头脚本模式

出于测试和脚本编写的目的，Canton 还可以以无头脚本模式启动：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton run <script-path> --config ...
```

在这种情况下，命令是在脚本中指定的，而不是以交互方式执行的。脚本或命令执行期间的任何错误都会导致 Canton 进程以非零退出代码退出。当脚本完成时，所有组件都将停止。

### 使用 Screen 的交互式服务器进程

在某些情况下，我们发现以交互方式运行服务器进程也很方便。对于 Linux / OSX 上的服务器使用，可以使用 [screen](https://linux.die.net/man/1/screen) 命令来完成：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
screen -S canton -d -m ./bin/canton -c ...
```

将在名为 `canton` 的屏幕会话中启动 Canton 进程，该会话不会在用户注销时终止，因此允许在必要时检查 Canton 进程。

可以使用以下方式加入先前启动的进程

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
screen -r canton
```

并且可以使用 CTRL-A + D（按顺序）分离活动屏幕会话。请小心并避免键入 CTRL-D，因为它会终止会话。即使您注销计算机，屏幕会话也将继续运行。

## Java 虚拟机参数

`bin/canton` 应用程序是一个方便的包装器，用于启动运行 Canton 进程的 Java 虚拟机。包装器支持使用 `JAVA_OPTS` 环境变量或使用 `-D` 命令行选项提供其他 JVM 选项。

例如，您可以按如下方式配置堆大小：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
JAVA_OPTS="-Xmx2G" ./bin/canton --config ...
```

有几个可以指定的与日志相关的选项。有关更多详细信息，请参阅日志记录。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/configure/general/declarative_conf.rst" hash="29ee858d" */}

# 声明式配置

<Note>
  声明式配置是一项 alpha 功能，最初仅适用于参与者节点。
</Note>

默认情况下，出于可扩展性的目的，运行时的 Canton 是使用 API 请求进行管理的。对于较小规模的部署，Canton 还支持动态更改的配置设置。此配置可以添加或删除 DAR、参与方、同步器、用户和身份提供者，并且可以按如下方式使用：

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
// 显式启用动态配置（alpha 功能，默认关闭）
canton.parameters.enable-alpha-state-via-config = 是
canton.parameters.state-refresh-interval = 5s// 这是一个示例配置文件
// 请注意，配置格式将来可能会发生变化
// 根据我们从社区获得的反馈
canton.参与方s.my参与方.alpha-dynamic {
  fetched-dar-directory =“fetched-dars”
  // 上传达尔
  达斯 = [
    { 位置 = "dars/CantonExamples.dar", 预期主包 = "abcd" }
    { 位置 = "https://path.to/repo/token.dar", request-headers = { AuthenticationToken : "mytoken" }}
  ],
  // 定义各方
  各方 = [
    { party = "Alice", 同步器 = ["mysync"] }
    { 派对 =“鲍勃”}
  ],
  // 如果为 true，则发现不在配置文件中的各方将被删除
  删除当事人= false
  // 定义身份提供者
  国内流离失所者 = [
    {identity-provider-id =“idp1”，发行者=“发行者”，jwks-url =“https://path.to/jwks”，受众=“可选”，is-deactivated = false}
  ]
  // 如果为 true，则删除发现的配置文件中没有的 idps
  删除 idps = false
  // 定义用户
  用户=[
    { user =“User1”，primary-party =“Alice”，is-deactivated = false，annotations = {“key”：“value”}，
      身份提供者 id =“idp1”，权限 = {
        充当= [“爱丽丝”]，
        读为 = [“鲍勃”]，
        读取为任意一方 = true
        参与者管理员 = true
        身份提供者管理 = true
      }
    }
  ]
  // 如果为true，则发现不在配置文件中的用户将被删除
  删除用户= false
  // 定义同步器
  连接= [{
    同步器别名=“mysync”
    手动连接= false
    优先级 = 0
    信任阈值 = 1
    连接数={
      “第一”：{
        端点 = [{ 主机 = "localhost", 端口 = 1234 }]
        传输安全 = true
        自定义信任证书 =“cert.pem”
      }
    }
  }]
}
````

请注意，将定期检查所有配置文件是否有文件修改，触发重新加载并将更改应用到节点。

指标`daml.declarative_api.items`和`daml.declarative_api.errors`提供了对通过状态配置文件管理的项目数量的深入了解。负错误代码意味着同步的某些基本内容未成功（如果无法解析配置文件，则为 -1；如果在准备同步期间出现某些问题，则为 -2；如果同步本身从根本上失败，则为 -3），而正错误代码则表示许多项目失败。 0 错误以外的任何错误都意味着出现问题。

某些设置只有在满足某些先决条件时才能应用。仅当同步器已注册时才可以将一方分配给用户。因此，有些变化只有在满足这些前提条件后才会出现。但是，在参与者连接到同步器之前，与各方定义目标状态是安全的。

也可以混合声明式和命令式配置。通过 API 定义的多余项目不会被删除，除非明确配置这样做。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/configure/storage/storage.rst" hash="02111269" */}

# 配置存储

Canton需要持久化数据来运营。参与者节点、中介节点和同步器节点都需要存储配置。

<Note>
  Canton 在启动时直接创建、管理和升级数据库模式。
</Note>

## 配置生产存储

对于生产部署，唯一支持的存储是 [PostgreSQL](https://www.postgresql.org/)。有关如何配置的详细信息，请参阅使用 Postgres 配置 Canton。

## 其他存储配置

<警告>
  生产部署不支持以下存储配置。它们仅用于测试、开发和实验目的。
</警告>

### 配置内存存储

如果没有提供其他存储配置，则默认使用内存存储。使用内存存储，内存数据结构代替关系数据库来存储数据。这样做的结果是当节点停止时所有数据都会丢失。

此示例显示了 Sequencer、Mediator 和 参与方节点 的显式内存配置：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Configures sequencer1, mediator1, and 参与方1 to use in-memory storage.
canton {
  sequencers.sequencer1.storage.type = memory
  mediators.mediator1.storage.type = memory
  参与方s.参与方1.storage.type = memory
}
```

### 配置H2存储

此示例显示了 Sequencer、Mediator 和 参与方节点 的 [H2](https://www.h2database.com/) 存储配置：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Configures sequencer1, mediator1, and 参与方1 to use file based H2 storage.
canton {
  sequencers.sequencer1.storage {
    type = h2
    config.url = "jdbc:h2:file:./data/sequencer1;MODE=PostgreSQL;LOCK_TIMEOUT=10000;DB_CLOSE_DELAY=-1"
  }
  mediators.mediator1.storage {
    type = h2
    config.url = "jdbc:h2:file:./data/mediator1;MODE=PostgreSQL;LOCK_TIMEOUT=10000;DB_CLOSE_DELAY=-1"
  }
  参与方s.参与方1.storage {
    type = h2
    config.url = "jdbc:h2:file:./data/参与方1;MODE=PostgreSQL;LOCK_TIMEOUT=10000;DB_CLOSE_DELAY=-1"
  }
}
```

前缀为 `url` 的 `jdbc:` 可以[以多种方式配置](https://www.h2database.com/html/features.html#database_url)。上面的例子配置：

基于嵌入式文件的存储
Canton启动时，嵌入式 H2 数据库将在相对于Canton节点工作目录的`./data`目录中创建，并且文件后缀为`.mv.db`。当使用H2[嵌入式连接模式](https://www.h2database.com/html/features.html#connection_modes)时，一次只有一个进程可以访问数据库，因此要检查数据库，需要先停止Canton。一旦没有其他进程访问数据库，就可以使用 H2 工具进行检查，例如 [H2 Console](https://www.h2database.com/html/quickstart.html#h2-console)。

模式=PostgreSQL
这是至关重要的，因为 Canton 使用的 SQL 方言是 PostgreSQL。此设置启用[PostgreSQL兼容模式](https://www.h2database.com/html/features.html#postgresql_mode)。

锁定超时=10000
这为线程提供了 10 秒的时间来在超时之前获取数据库锁。

DB\_CLOSE\_DELAY=-1
此设置使数据库保持打开状态，直到 Canton 进程终止。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/configure/storage/postgres.rst" hash="e08b03d4" */}

# 使用 PostgreSQL 配置 Canton<span id="postgres-config" />

## 配置示例

此示例显示了 Sequencer、Mediator 和 参与方节点 的 [PostgreSQL](https://www.postgresql.org/) 存储配置，这些节点均在端口 `5432` 上的本地 PostgreSQL 数据库实例上运行。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Configures sequencer1, mediator1, and 参与方1 with locally running PostgreSQL storage.
canton {
  sequencers.sequencer1.storage {
    type = postgres
    config {
      dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
      properties = {
        serverName = "localhost"
        databaseName = "sequencer1_db"
        portNumber = "5432"
        user = "sequencer1"
        password = "pgpass"
      }
    }
  }
  mediators.mediator1.storage {
    type = postgres
    config {
      dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
      properties = {
        serverName = "localhost"
        databaseName = "mediator1_db"
        portNumber = "5432"
        user = "mediator1"
        password = "pgpass"
      }
    }
  }
  参与方s.参与方1.storage {
    type = postgres
    config {
      dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
      properties = {
        serverName = "localhost"
        databaseName = "参与方1_db"
        portNumber = "5432"
        user = "参与方1"
        password = "pgpass"
      }
    }
  }
}
```

## 配置连接池

Canton 使用 [HikariCP](https://github.com/brettwooldridge/HikariCP) 进行连接池。这是在`storage.config`中配置的。我们推荐这篇关于如何[选择池大小]的文章。(https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing)

<Note>
  PostgreSQL 的 `dataSourceClassName` 和 `properties` 设置将在下一节中讨论。
</Note>下面给出了可以设置的池属性集，属性的描述可以在 [HikariConfig](https://www.javadoc.io/doc/com.zaxxer/HikariCP/3.2.0/com/zaxxer/hikari/HikariConfig.html) 的相关 `get`/`set` 方法描述中找到。

|                        |                           |                        |
| ---------------------- | ---------------------------------- | ---------------------- |
|允许池暂停 |目录 |连接初始化Sql |
|连接测试查询 |连接超时 |数据源类名 |
|空闲超时 |初始化失败超时 |隔离内部查询 |
|泄漏检测阈值 |最大生命周期 |最大池大小 |
|最小空闲|池名称 |属性 |
|只读 |注册Mbeans |架构|
|验证超时 |                           |                        |

## 配置PostgreSQL数据源

要创建连接`HikariCP`，请使用使用`properties`中的属性配置的*数据源*`dataSourceClassName`。我们建议使用配置有以下属性的 `org.postgresql.ds.PGSimpleDataSource` *数据源*：

> * 服务器名称
> * 数据库名称
> * 端口号
> * 用户
> * 密码

您可以通过查看 [PGSimpleDataSource](https://jdbc.postgresql.org/documentation/publicapi/org/postgresql/ds/PGSimpleDataSource.html) 的关联 `get`/`set` 方法描述来找到其他受支持属性的详细信息。

### 在配置中使用环境变量

您可以使用环境变量来配置 PostgreSQL 数据源属性。这对于密码等敏感信息或当您想避免在配置文件中硬编码值时非常有用。

在此示例中，所有数据库属性都是使用环境变量设置的。环境变量以`SEQUENCER1_`为前缀，以避免与其他配置冲突。

```
config {
  dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
  properties = {
    serverName = ${SEQUENCER1_SERVER}
    databaseName = ${SEQUENCER1_DB}
    portNumber = ${SEQUENCER1_PORT}
    user = ${SEQUENCER1_USER}
    password = ${SEQUENCER1_PASSWORD}
  }
```

### 跨节点共享数据库配置

此示例展示了如何使用 [PureConfig](https://github.com/pureconfig/pureconfig) 在 Canton 设置中的多个节点之间共享通用数据库配置。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Postgres persistence configuration mixin
#
# This file defines a shared configuration resources. You can mix it into your configuration by
# refer to the shared storage resource and add the database name.
#
# Example:
#   participant1 {
#     storage = ${_shared.storage}
#     storage.config.properties.databaseName = "参与方1"
#   }
#
# The user and password is not set. You want to either change this configuration file or pass
# the settings in via environment variables POSTGRES_USER and POSTGRES_PASSWORD.
#
_shared {
    storage {
        type = postgres
        config {
            dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
            properties = {
                serverName = "localhost"
                # the next line will override above "serverName" in case the environment variable POSTGRES_HOST exists
                # which makes it optional
                serverName = ${?POSTGRES_HOST}
                portNumber = "5432"
                portNumber = ${?POSTGRES_PORT}
                # user and password are required
                user = ${POSTGRES_USER}
                password = ${POSTGRES_PASSWORD}
            }
        }
        parameters {
            # If defined, will configure the number of database connections per node.
            # Please note that the number of connections can be fine tuned for 参与方节点s (see 参与方.conf)
            max-connections = ${?POSTGRES_NUM_CONNECTIONS}
            # If true, then database migrations will be applied on startup automatically
            # Otherwise, you will have to run the migration manually using 参与方.db.migrate()
            migrate-and-start = false
            # If true (default), then the node will fail to start if it can not connect to the database.
            # The setting is useful during initial deployment to get immediate feedback when the
            # database is not available.
            # In a production setup, you might want to set this to false to allow uncoordinated startups between
            # the database and the node.
            fail-fast-on-startup = true
        }
    }
}
```

## 使用 SSL

使用以下 `PGSimpleDataSource` 属性配置 SSL。

ssl=真
验证 SSL 证书并验证主机名

sslmode=“验证 ca”
检查证书链直至客户端上存储的根证书。

sslrootcert =“路径/到/root.cert”
（可选）将其设置为根证书的路径。

有关如何在 PostgreSQL 中配置 SSL 的更多详细信息，请参阅 [PostgreSQL SSL](https://jdbc.postgresql.org/documentation/ssl/) 文档。

### 使用 mTLS

要配置双向 TLS ([mTLS](https://en.wikipedia.org/wiki/Mutual_authentication#mTLS))，您可以使用以下附加属性：

> * sslcert =“路径/到/client-cert.pem”
> * sslkey =“路径/到/client-key.p12”

## 设置 PostgreSQL 数据库

每个Canton节点都需要一个单独的数据库。在启动 Canton 之前创建数据库。

<Note>
  canton 发行版提供了一个脚本 `config/utils/postgres/db.sh` 来帮助创建数据库和用户。
</Note>

### 创建数据库

数据库必须使用 UTF8 编码创建，以确保正确处理 Unicode 字符。以下 SQL 命令创建一个名为 `参与方1_db` 且采用 UTF8 编码的数据库：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
create database 参与方1_db encoding = 'UTF8';
```

### 创建数据库用户

除了读取和写入数据之外，*data-source* 属性中配置的数据库用户还必须拥有创建和修改数据库架构所需的权限。

以下 SQL 命令创建一个名为 `参与方1_user` 并带有密码的用户，并授予数据库的所有权限：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
create user 参与方1_user with password 'change-me';
grant all privileges on database 参与方1_db to 参与方1_user;
```

## 操作

### 优化存储

请参阅存储优化。

### 备份

请参阅备份和恢复。

### 设置高可用性

请参阅高可用性使用情况。

## 使用云托管数据库您可以使用云托管的 PostgreSQL 数据库，例如 [Amazon RDS](https://aws.amazon.com/rds/postgresql/)、[Google Cloud SQL](https://cloud.google.com/sql/docs/postgres) 或 [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/services/postgresql/)。

有关如何设置、配置和保护 PostgreSQL 数据库的详细信息，请参阅相应云提供商的文档。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/configure/parameters/parameters.rst" hash="978f5ecd" */}

# 配置Canton参数

## 参与者节点协议版本

在参与者节点连接到定序器节点时，节点之间会进行握手，以确保同步器协议版本兼容。默认情况下，参与者节点可以连接到运行任何稳定协议版本的同步器。

### 确保最低协议版本

设置最低协议版本可确保参与者节点只能连接到运行协议版本至少与配置的最低版本一样高的同步器。使用此选项可确保参与者节点无法连接到运行已知存在安全漏洞或不支持所需功能的协议版本的同步器。

例如，为了确保 同步器 协议版本至少为版本 **33**，请设置 `minimum-protocol-version` 参与者节点参数：

```
canton.参与方s.参与方1.parameters.minimum-protocol-version=33
```

### 启用早期访问协议功能

<警告>
  抢先体验的用途适用于非生产环境，并且不在支持范围内
</警告>

#### 启用 alpha 协议版本

要允许参与者节点连接到运行 alpha 协议版本的同步器，请将 `alpha-version-support` 参数设置为 `true`。由于这是一个实验性功能，因此还需要将 `non-standard-config` 参数设置为 `true`：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters {
  # turn on non-standard configuration support
  non-standard-config = yes

  # turn on support of alpha version support for 同步器 nodes
  alpha-version-support = yes
}

canton.参与方s.参与方1.parameters = {
  # enable alpha version support on the participant (this will allow the participant to connect to a 同步器 running protocol version dev or any other alpha protocol)
  # and it will turn on support for unsafe daml lf dev versions
  # not to be used in production and requires you to define non-standard-config = yes
  alpha-version-support = yes
}
```

#### 启用 beta 协议版本

要允许参与者节点连接到运行 beta 协议版本的同步器，请将 `beta-version-support` 参数设置为 `true`。由于这是一个实验性功能，因此还需要将 `non-standard-config` 参数设置为 `true`：

```
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters {
  # turn on support of beta version support for 同步器 nodes
  beta-version-support = yes
}

canton.参与方s.参与方1.parameters = {
  # enable beta version on the participant (this will allow the participant to connect to a 同步器 with beta protocol version)
  beta-version-support = yes
}
```

## 检测 Canton 何时开始

在测试环境中运行 Canton 时，检测 Canton 何时启动可能很有用。

要指示 Canton 在初始化时写入包含运行端口详细信息的文件，请配置 ports 文件：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.parameters.ports-file=ports.json

```

启动时，Canton 将其服务正在运行的端口的值写入端口文件：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "参与方1" : {
    "ledgerApi" : 5021,
    "adminApi" : 5022,
    "jsonApi" : null
  }
}
```

## 启用预览命令

Canton 控制台 *预览命令* 是不被认为稳定且未在命令组帮助请求中列出的命令。

要启用预览命令，请在配置文件中将`enable-preview-commands`参数设置为`yes`。预览命令现在列在命令组帮助请求中并且可以使用。

<警告>
  不保证预览命令稳定，并且可能在未来版本中发生变化。
</警告>```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.features.enable-preview-commands=yes

```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
