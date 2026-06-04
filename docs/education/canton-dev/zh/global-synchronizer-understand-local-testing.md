---
title: "本地测试"
slug: "global-synchronizer-understand-local-testing"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/understand/local-testing.md"
source_title: "Local Testing"
tags:
  - global-synchronizer
  - understand
  - local-testing
---

# 本地测试

> LocalNet 本地开发与测试环境部署指南。

LocalNet 提供了一个简单的拓扑，由三个参与者、三个验证者、一个 PostgreSQL 数据库和 NGINX 网关后面的多个 Web 应用程序（钱包、sv、扫描）组成。每个验证者在 Splice 生态系统中扮演着不同的角色：

* **应用程序提供者**：供操作其应用程序的用户使用
* **应用程序用户**：对于想要使用应用程序提供商提供的应用程序的用户
* **sv**：用于提供全局同步器并处理AMT

LocalNet 主要用于开发和测试，不适用于生产用途。

## 设置

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. 从 <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">下载捆绑包 (DevNet 0.6.4)</a> 链接下载发布工件，并解压捆绑包：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.4_splice-node.tar.gz
       > ```

       提取的定义 LocalNet 的 docker compose 文件位于`splice-node/docker-compose/localnet`。

    2、导出后面命令用到的这两个环境变量：

       * **LOCALNET\_DIR**：指定 LocalNet 目录的路径。
       * **IMAGE\_TAG**：指定要在 LocalNet 中使用的 Splice 版本。

       对于您下载的捆绑包，请使用：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.4
       > ```

    3. 有关启动、停止、检查和管理 LocalNet 节点的命令，请参阅`use-localnet`。

    可选：使用 Docker Compose 配置文件（例如，`--profile app-provider`）以及相应的环境变量（例如，`APP_PROVIDER_PROFILE=on/off`）来禁用特定的验证者节点；例如，减少LocalNet的资源需求。默认情况下，所有三个验证者均处于活动状态。

    可选：使用以下附加环境变量进行配置：

    * **LOCALNET\_DIR/compose.env**：包含 Docker Compose 配置变量。
    * **LOCALNET\_ENV\_DIR**：覆盖默认环境文件目录。默认为`$LOCALNET_DIR/env`。
    * **LOCALNET\_ENV\_DIR/common.env**：跨 Docker Compose 和容器配置共享环境变量。它设置默认端口、数据库凭据和 Splice UI 配置。

    容器的资源约束可以通过以下方式配置： - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    1. 从 <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">下载捆绑包 (TestNet 0.6.3)</a> 链接下载发布工件，并解压捆绑包：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.3_splice-node.tar.gz
       > ```

       提取的定义 LocalNet 的 docker compose 文件位于`splice-node/docker-compose/localnet`。

    2、导出后面命令用到的这两个环境变量：

       * **LOCALNET\_DIR**：指定 LocalNet 目录的路径。
       * **IMAGE\_TAG**：指定要在 LocalNet 中使用的 Splice 版本。

       对于您下载的捆绑包，请使用：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.3
       > ```

    3. 有关启动、停止、检查和管理 LocalNet 节点的命令，请参阅`use-localnet`。

    可选：使用 Docker Compose 配置文件（例如，`--profile app-provider`）以及相应的环境变量（例如，`APP_PROVIDER_PROFILE=on/off`）来禁用特定的验证者节点；例如，减少LocalNet的资源需求。默认情况下，所有三个验证者均处于活动状态。

    可选：使用以下附加环境变量进行配置：* **LOCALNET\_DIR/compose.env**：包含 Docker Compose 配置变量。
    * **LOCALNET\_ENV\_DIR**：覆盖默认环境文件目录。默认为`$LOCALNET_DIR/env`。
    * **LOCALNET\_ENV\_DIR/common.env**：跨 Docker Compose 和容器配置共享环境变量。它设置默认端口、数据库凭据和 Splice UI 配置。

    容器的资源约束可以通过以下方式配置： - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tabs>

  <Tab title="主网 (0.6.2)">
    1. 从 <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">下载捆绑包 (MainNet 0.6.2)</a> 链接下载发布工件，并解压捆绑包：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.2_splice-node.tar.gz
       > ```

       提取的定义 LocalNet 的 docker compose 文件位于 `splice-node/docker-compose/localnet` 中。

    2、导出后面命令用到的这两个环境变量：

       * **LOCALNET\_DIR**：指定 LocalNet 目录的路径。
       * **IMAGE\_TAG**：指定要在 LocalNet 中使用的 Splice 版本。

       对于您下载的捆绑包，请使用：

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.2
       > ```

    3. 有关启动、停止、检查和管理 LocalNet 节点的命令，请参阅`use-localnet`。

    可选：使用 Docker Compose 配置文件（例如，`--profile app-provider`）以及相应的环境变量（例如，`APP_PROVIDER_PROFILE=on/off`）来禁用特定的验证者节点；例如，减少LocalNet的资源需求。默认情况下，所有三个验证者均处于活动状态。

    可选：使用以下附加环境变量进行配置：

    * **LOCALNET\_DIR/compose.env**：包含 Docker Compose 配置变量。
    * **LOCALNET\_ENV\_DIR**：覆盖默认环境文件目录。默认为`$LOCALNET_DIR/env`。
    * **LOCALNET\_ENV\_DIR/common.env**：跨 Docker Compose 和容器配置共享环境变量。它设置默认端口、数据库凭据和 Splice UI 配置。

    容器的资源约束可以通过以下方式配置： - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tabs>
</Tabs>

## 暴露的端口

以下部分详细介绍了各种服务使用的端口。默认数据库端口是**DB\_PORT=5432**。

其他端口是使用基于验证者的特定模式生成的：

* 对于超级验证者（sv），端口指定为`4${PORT_SUFFIX}`。
* 对于应用程序提供商，端口指定为`3${PORT_SUFFIX}`。
* 对于应用程序用户，端口指定为`2${PORT_SUFFIX}`。

这些模式适用于以下端口后缀：

* **PARTICIPANT_LEDGER_API_PORT_SUFFIX**：901
* **PARTICIPANT_ADMIN_API_PORT_SUFFIX**：902
* **PARTICIPANT_JSON_API_PORT_SUFFIX**：975
* **VALIDATOR_ADMIN_API_PORT_SUFFIX**：903
* **CANTON\_HTTP\_HEALTHCHECK\_PORT\_SUFFIX**：900
* **CANTON\_GRPC\_HEALTHCHECK\_PORT\_SUFFIX**：961

UI端口定义如下：

* **APP_USER_UI_PORT**：2000
* **APP\_PROVIDER\_UI\_PORT**：3000
* **SV\_UI\_PORT**：4000

## 数据库

LocalNet 对所有组件使用单个 PostgreSQL 数据库。数据库配置来源于`LOCALNET_ENV_DIR/postgres.env`。

## 应用程序用户界面

* **应用程序用户钱包用户界面**

  > * **URL**: [http://wallet.localhost:2000](http://wallet.localhost:2000)
  > * **描述**：管理用户钱包的界面。

* **应用程序提供商钱包用户界面**

  > * **URL**: [http://wallet.localhost:3000](http://wallet.localhost:3000)
  > * **描述**：管理用户钱包的界面。

* **超级验证者 Web UI**

  > * **URL**: [http://sv.localhost:4000](http://sv.localhost:4000)
  > * **描述**：超级验证者功能的接口。

* **Scan Web UI**

  > * **URL**：[http://scan.localhost:4000](http://scan.localhost:4000)
  > * **描述**：监控交易的接口。

<Note>
  `LocalNet` 轮可能需要最多 6 轮（相当于一小时）才能在Scan UI 中显示。
</Note>在大多数情况下，`*.localhost`域（例如`http://scan.localhost`）将解析为您的本地主机IP`127.0.0.1`。在某些情况下，解决方案不会发生，解决方案是将条目添加到您的 `/etc/hosts` 文件中。例如，要解析 `http://scan.localhost` 和 `http://wallet.localhost`，请将以下条目添加到文件中：

```
127.0.0.1   scan.localhost
127.0.0.1   wallet.localhost
```

## 默认钱包用户

* **应用程序用户**：应用程序用户
* **应用程序提供商**：应用程序提供商
* **SV**：SV

## Swagger UI

启用 `swagger-ui` 配置文件后，所有正在运行的参与者中的 `JSON Ledger API HTTP Endpoints` 的 Swagger UI 可在 [http://localhost:9090](http://localhost:9090) 上使用。注意：使用 **试用** 功能时，某些端点需要 JWT 令牌。获取此令牌的一种方法是通过 Canton Console。启动Canton控制台`make canton-console`并执行以下命令：

```
`app-provider`.adminToken
```

为了实现正确的功能，Swagger UI 依赖于为每个参与者配置的 `canton.localhost` 本地主机 nginx 代理。例如，应用程序提供者的`JSON Ledger API HTTP Endpoints`可以通过Swagger UI在nginx代理URL`http://canton.localhost:${APP_PROVIDER_UI_PORT}`处访问，这相当于直接访问`localhost:3${PARTICIPANT_JSON_API_PORT}`。 nginx 代理仅添加额外的标头来解决 Swagger UI 中的 CORS 问题。

## 使用本地网络

### 启动 LocalNet 节点

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user up -d
```

### 停止 LocalNet 节点

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user down -v
```

### 启动包含 swagger-ui 的节点

更多信息请参见`swagger-ui`。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user \
               --profile swagger-ui up -d
```

### 停止包含 swagger-ui 的节点

更多信息请参见`swagger-ui`。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user \
               --profile swagger-ui down -v
```

### 访问 Canton 管理控制台

使用 Canton 管理控制台检查和修改 LocalNet 部署中 Canton 排序器、中介器和参与者节点的运行配置。

* [Canton Console操作方法](/global-synchronizer/canton-console/console-overview)
* [Canton Console 命令](/global-synchronizer/reference/canton-console-commands)

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               run --rm console
```

## 多个同步器

LocalNet 支持并行运行多个同步器。

默认情况下，由超级验证者 (sv) 控制的单个同步器处于活动状态。该同步器模拟**全局同步器**。要启用名为 `app-synchronizer` 的第二个同步器，请使用 `multi-sync` Docker Compose 配置文件 (`--profile multi-sync`) 启动 LocalNet。附加同步器具有以下特点：

* 它由`app-sequencer`和`app-mediator`节点管理。
* 它模拟一个**私有同步器**。
* `app-provider`和`app-user`参与者都交叉连接到全局同步器和`app-synchronizer`。

## 使用非默认协议版本

LocalNet 同步器和参与者中使用的协议版本可以通过在启动 LocalNet 之前将 `CANTON_PROTOCOL_VERSION` 环境变量设置为所需版本来配置。非稳定协议版本可用于早期测试，但需要明确选择加入。为此，还需要导出一个 `ALPHA_PROTOCOL_VERSION_ENV=$LOCALNET_DIR/env/alpha-protocol-version.env` 环境变量。

<Warning>
  非稳定协议版本是正在开发中的未发布版本，并且可能会发生已宣布的重大更改。这意味着该环境通常无法升级，因此每次更改都需要完全重置。仅用于早期测试和开发目的。
</Warning>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
