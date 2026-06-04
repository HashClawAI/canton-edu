---
title: "配置参考"
slug: "appdev-reference-configuration-reference"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/configuration-reference.md"
source_title: "Configuration Reference"
tags:
  - appdev
  - reference
  - configuration-reference
---

# 配置参考

> Canton 配置文件、DPM 项目设置、存储后端、命令行参数与环境变量参考。

Canton 节点使用 [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md)（人类优化配置对象表示法）作为其静态配置文件。静态配置涵盖进程启动时必须知道的设置，例如存储后端、API 端口和节点标识。动态设置（例如 Party 注册与 synchronizer连接）在运行时通过 [console](/global-synchronizer/reference/canton-console-reference) 或管理 API 进行管理。

## HOCON 格式基础知识

HOCON 支持类似 JSON 的对象语法，具有宽松的引用、嵌套键路径 (`a.b.c = value`) 和 `//` 或 `#` 注释。重复的键将被合并，最后一个定义获胜。

### 文件包含

### 环境变量替换

HOCON 使用 `${VAR_NAME}` 语法替换环境变量。有两种形式可供选择：

* `${VAR_NAME}` -- 必填。如果未设置该变量，则进程将无法启动。
* `${?VAR_NAME}` -- 可选。仅当变量存在时才设置键。

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
properties = {
    serverName = "localhost"
    serverName = ${?POSTGRES_HOST}  # overrides only if POSTGRES_HOST is set
    user = ${?POSTGRES_USER}          # required, fails if unset
    password = ${?POSTGRES_PASSWORD}  # required, fails if unset
```

<Warning>
  切勿在配置文件中对凭据进行硬编码。使用环境变量替换密码和其他机密。
</Warning>

## Canton 配置结构

CamelCase Scala 名称在配置文件中映射为小写加破折号（例如，`synchronizerParameters` 变为`synchronizer-parameters`）。

### 初始化配置

某些值仅在节点的首次初始化期间应用，之后无法更改。这些位于 `init` 部分：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}

participant1 {
  init {
    ledger-api.max-deduplication-duration = 1 minute
    identity.node-identifier.type = random
  }
```

## 命令行参数

### 运行模式

### JVM 参数

## 存储配置

Canton 支持三种存储后端：

* **内存** -- 用于快速测试；重启后数据丢失
* **H2** -- 嵌入式数据库，适合本地开发
* **PostgreSQL** -- 生产环境中唯一受支持的选项

### PostgreSQL 示例

每个 Canton 节点都需要自己的数据库。使用 UTF-8 编码创建数据库：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
CREATE DATABASE participant1_db ENCODING = 'UTF8';
CREATE USER participant1_user WITH PASSWORD 'change-me';
GRANT ALL PRIVILEGES ON DATABASE participant1_db TO participant1_user;
```

Canton 使用 [HikariCP](https://github.com/brettwooldridge/HikariCP) 进行连接池。您可以在`storage.config`下调整池属性（`maximumPoolSize`、`connectionTimeout`、`idleTimeout`等）。

### 配置混合模式

当针对同一数据库服务器运行多个节点时，在 mixin 中定义共享存储设置并在每个节点引用它们：

## 关键参数

### 快速失败模式

<Note>
  请谨慎使用此选项 - 如果数据库无法访问，禁用快速失败可能会导致无限期的、嘈杂的等待。
</Note>

### 协议版本

### 早期访问协议版本

Alpha 和 Beta 协议版本仅适用于非生产环境。启用它们需要在`canton.parameters`级别设置`non-standard-config = yes`以及参与者上相应的版本支持标志：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}

canton.parameters {
  non-standard-config = yes
  alpha-version-support = yes
}

canton.participants.participant1.parameters = {
  alpha-version-support = yes
```

## DPM 项目配置

DPM 使用 YAML 文件进行项目配置，与 Canton 的 HOCON 节点配置分开。

### daml.yaml（单个包）

每个Daml包都有一个`daml.yaml`指定SDK版本、包名称、源目录和依赖项。

### multi-package.yaml（多包项目）

对于多包项目配置，请参阅[构建和打包](/appdev/modules/m3-building-packaging)，其中涵盖了`multi-package.yaml`结构和依赖解析。

### DPM 环境变量

有关 DPM 环境变量的详细信息，请参阅[构建和打包](/appdev/modules/m3-building-packaging)。

### DPM 全局配置

DPM 从 `${DPM_HOME}/dpm-config.yaml` 读取全局设置。环境变量优先于文件值：

* `DPM_REGISTRY` -- 覆盖 SDK 和组件的 Docker 注册表
* `DPM_REGISTRY_AUTH` -- 覆盖注册表验证文件
* `DPM_INSECURE_REGISTRY` -- 允许从 HTTP 注册表中拉取
* `DPM_LOG_LEVEL` -- 设置日志级别 (`debug`, `info`, `warn`, `error`)
* `DPM_SDK_VERSION` -- 在所有项目中全局覆盖 SDK 版本
* `DAML_PACKAGE` -- 在包上下文中运行 `dpm` 命令而不更改目录

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
