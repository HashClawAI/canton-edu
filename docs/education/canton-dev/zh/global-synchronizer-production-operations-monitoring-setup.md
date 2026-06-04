---
title: "监控搭建"
slug: "global-synchronizer-production-operations-monitoring-setup"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/monitoring-setup.md"
source_title: "Monitoring Setup"
tags:
  - global-synchronizer
  - production-operations
  - monitoring-setup
---

# 监控搭建

> Canton 侧监控搭建、健康检查与 ACS 承诺监控。

> Canton 监控示例、参与者节点健康状况和 ACS 承诺监控

本页面涵盖 Canton 端监控主题：容器化监控设置示例（Prometheus、Grafana、ELK）、参与者节点运行状况端点以及如何监控 ACS 承诺。

对于 Splice / Canton Network 的具体指标 - 每个组件公开什么、如何抓取它以及在验证者和超级验证者上观察哪些指标 - 请参阅：

* [Splice 指标概述](/global-synchronizer/生产-操作/Splice 指标-概述)
* [关键指标](/global-synchronizer/生产运营/关键指标)
* [指标参考](/zh/docs/canton/global-synchronizer-reference-metrics-reference)

本指南和脚本/配置未经测试，它们仍然有效吗？尝试将其分解为特定的操作方法，并确保配置/脚本移至经过测试的示例。

这与我们拥有的其他可观察性文档有何关系？我们有可观察性 gh 的内容以及快速入门中的可观察性的内容

## 监控设置示例

本节提供了如何在 Docker 容器的连接网络中运行 Canton 的示例。该示例还展示了如何监视网络活动。请参阅[词汇表](/zh/docs/canton/overview-understand-glossary) 了解监控术语定义，并参阅[监控选择](#monitoring-choices) 部分了解示例监控设置背后的原因。

<Note>
  Canton 容器镜像发布于`ghcr.io/digital-asset/decentralized-canton-sync/docker/canton`。下面的示例 Docker Compose 片段使用 `${CANTON_VERSION}` 作为标签的占位符 — 在运行它们之前将 `CANTON_VERSION` 导出到目标网络的值，或者内联替换它。请参阅 [版本兼容性仪表板](/shared/version-compatibility-dashboard) 了解 MainNet、TestNet 和 DevNet 上的当前标签。
</Note>

### 容器设置

要配置 [Docker Compose](https://docs.docker.com/compose/) 以启动图中所示的 Docker 容器网络，请使用以下信息。有关配置文件结构的详细信息，请参阅`compose`文档。

`compose` 允许您提供跨多个文件的整体配置。下面描述了每个配置文件，然后是有关如何将它们组合到正在运行的网络中的信息。

<图片src =“https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/global-synchronizer/生产-操作/imag es/basic-canton-setup.svg?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=5052fcfd8a0917843e8c50f89f2285cc" className="align-center" style={{width: "100%"}} alt="显示 Docker 网络设置示例的图表" width="999" height="1260" data-path="global-同步器/product-operations/images/basic-canton-setup.svg" />

#### 预期用途

此示例旨在演示如何公开、聚合和观察来自 Canton 的监控信息。不经改造不适合生产。请注意以下警告：<Warning>
  从 Docker 网络公开的端口不是支持 UI 所必需的。例如，网络可以允许通过 REST 或类似接口与底层服务进行低级交互。在生产系统中，唯一应该公开的端口是系统运行所需的端口。
</Warning>

<Warning>
  示例中使用的一些服务（例如 Postgres 和 Elasticsearch）将数据保存到磁盘。对于此示例，用于此持久数据的卷位于 Docker 容器的内部。这意味着当 Docker 网络被拆除时，所有数据都会与容器一起被清除。在生产系统中，这些卷将被安装到永久存储上。
</Warning>

<Warning>
  密码以明文形式存储在配置文件中。在生产系统中，应在运行时从安全密钥库中提取密码。
</Warning>

<Warning>
  网络连接不安全。在生产系统中，服务之间的连接应启用 TLS，并提供证书颁发机构 (CA)。
</Warning>

<Warning>
  容器的内存使用仅适合轻型演示负载。在生产设置中，需要根据内存分析为容器提供足够的内存。
</Warning>

<Warning>
  示例中使用的 Docker 映像的版本可能会过时。在生产系统中，仅应使用最新的修补版本。
</Warning>

#### 网络配置

在此 compose 文件中，定义将用于连接所有正在运行的容器的网络：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Create with `docker network create monitoring`
# Note that `external: false` will fail the docker-compose execution if the network `monitoring` already exists

version: "3.8"

networks:
  default:
    name: monitoring
    external: false
```

#### Postgres 设置

仅使用单个 Postgres 容器，为同步器创建数据库，并为每个参与者创建 Canton 和索引数据库。为此，请将 `postgres-init.sql` 挂载到 Postgres 初始化的目录中。请注意，在生产环境中，密码不得内联在 config 中。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  postgres:
    image: postgres:17.5-bullseye
    hostname: postgres
    container_name: postgres
    environment:
      - POSTGRES_USER=pguser
      - POSTGRES_PASSWORD=pgpass
    volumes:
      - ../etc/postgres-init.sql:/docker-entrypoint-initdb.d/init.sql
    expose:
      - "5432"
    ports:
      - "5432:5432"
    healthcheck:
      test: "pg_isready -U postgres"
      interval: 5s
      timeout: 5s
      retries: 5
```

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
create database canton1db;
create database index1db;

create database 同步器0db;

create database canton2db;
create database index2db;
```

#### 同步器设置

使用 `--log-profile container` 运行同步器，在调试级别将纯文本写入标准输出。

#### 参与者设置参与者容器在创建容器时映射了两个文件。 `.conf` 文件提供同步器和数据库位置的详细信息。公开了一个 HTTP 指标端点，它以 [Prometheus 基于文本的格式](https://github.com/prometheus/docs/blob/main/content/docs/instrumenting/exposition_formats.md#text-based-format) 返回指标。默认情况下，参与者不会连接到远程同步器，因此提供了一个引导脚本来完成此任务。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  participant1:
    image: ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:${CANTON_VERSION}
    container_name: participant1
    hostname: participant1
    volumes:
      - ./participant1.conf:/canton/etc/participant1.conf
      - ./participant1.bootstrap:/canton/etc/participant1.bootstrap
    command: daemon --log-profile container --config etc/participant1.conf --bootstrap etc/participant1.bootstrap
    expose:
      - "10011"
      - "10012"
      - "10013"
    ports:
      - "10011:10011"
      - "10012:10012"
      - "10013:10013"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.connect_local(sequencer1, alias = "同步器0")
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  participants {
    participant1 {
      storage {
        type = postgres
        config {
        dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
          properties = {
            databaseName = "canton1db"
            serverName = "postgres"
            portNumber = "5432"
            user = pguser
            password = pgpass
          }
        }
        ledger-api-jdbc-url = "jdbc:postgresql://postgres:5432/index1db?user=pguser&password=pgpass"
      }
      ledger-api {
        port = 10011
        address = "0.0.0.0"
      }
      admin-api {
        port = 10012
        address = "0.0.0.0"
      }
    }
  }
  monitoring.metrics.reporters = [{
    type = prometheus
    address = "0.0.0.0"
    port = 10013
  }]
}
```

参与者 2 的设置相同，只是名称和端口发生了更改。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  participant2:
    image: ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:${CANTON_VERSION}
    container_name: participant2
    hostname: participant2
    volumes:
      - ./participant2.conf:/canton/etc/participant2.conf
      - ./participant2.bootstrap:/canton/etc/participant2.bootstrap
    command: daemon --log-profile container --config etc/participant2.conf --bootstrap etc/participant2.bootstrap
    expose:
      - "10021"
      - "10022"
      - "10023"
    ports:
      - "10021:10021"
      - "10022:10022"
      - "10023:10023"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.connect_local(sequencer1, alias = "同步器0")
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  participants {
    participant1 {
      storage {
        type = postgres
        config {
        dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
          properties = {
            databaseName = "canton1db"
            serverName = "postgres"
            portNumber = "5432"
            user = pguser
            password = pgpass
          }
        }
        ledger-api-jdbc-url = "jdbc:postgresql://postgres:5432/index1db?user=pguser&password=pgpass"
      }
      ledger-api {
        port = 10011
        address = "0.0.0.0"
      }
      admin-api {
        port = 10012
        address = "0.0.0.0"
      }
    }
  }
  monitoring.metrics.reporters = [{
    type = prometheus
    address = "0.0.0.0"
    port = 10013
  }]
}
```

#### 日志存储

Docker容器可以指定日志驱动程序来自动将日志信息从容器导出到聚合服务。该示例使用 Logstash 作为所有 GELF 流的聚合点，导出 GELF 中的日志信息。您可以使用 Logstash 为许多下游日志记录数据存储提供数据，包括 Elasticsearch、Loki 和 Graylog。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  logstash:
    image: docker.elastic.co/logstash/logstash:8.5.1
    hostname: logstash
    container_name: logstash
    expose:
      - 12201/udp
    volumes:
      - ./pipeline.yml:/usr/share/logstash/config/pipeline.yml
      - ./logstash.yml:/usr/share/logstash/config/logstash.yml
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    ports:
      - "12201:12201/udp"
```

Logstash 读取 `pipeline.yml` 来发现所有管道的位置。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
- pipeline.id: main
  path.config: "/usr/share/logstash/pipeline/logstash.conf"
```

配置的管道读取 GELF 格式的输入，然后将其输出到以 `logs-` 为前缀并以日期为后缀的 Elasticsearch 索引。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Main logstash pipeline

input { 
  gelf {
    use_udp => true
    use_tcp => false
    port => 12201   
  }
} 

filter {}

output { 

  elasticsearch { 
    hosts => ["http://elasticsearch:9200"] 
    index => "logs-%{+YYYY.MM.dd}"
  }

}
```

使用默认的 Logstash 设置，并将 HTTP 端口绑定到所有主机 IP 地址。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# For full set of descriptions see
# https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html

http.host: "0.0.0.0"
```

#### 弹性搜索

Elasticsearch 支持在具有内置弹性的集群配置中运行。该示例仅运行一个 Elasticsearch 节点。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.2
    container_name: elasticsearch
    environment:
      ELASTIC_PASSWORD: elastic
      node.name: elasticsearch
      cluster.name: elasticsearch
      cluster.initial_master_nodes: elasticsearch
      xpack.security.enabled: false
      bootstrap.memory_lock: true
    ulimits:
      memlock:
        soft: -1
        hard: -1
    expose:
      - 9200
    ports:
      - 9200:9200
    healthcheck:
      test: "curl -s -I http://localhost:9200 | grep 'HTTP/1.1 200 OK'"
      interval: 10s
      timeout: 10s
      retries: 10
```

#### 基巴纳

Kibana 提供了一个 UI，允许搜索 Elasticsearch 日志索引。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  kibana:
    image: docker.elastic.co/kibana/kibana:8.5.2
    container_name: kibana
    expose:
      - 5601
    ports:
      - 5601:5601
    environment:
      - SERVERNAME=kibana
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    healthcheck:
      test: "curl -s -I http://localhost:5601 | grep 'HTTP/1.1 302 Found'"
      interval: 10s
      timeout: 10s
      retries: 10
```

您必须手动配置数据视图才能查看日志。有关说明，请参阅 [Kibana 日志监控](#kibana-log-monitoring)。

#### 顾问

cAdvisor 向 Prometheus 公开容器系统指标（CPU、内存、磁盘和网络）。它还提供了一个 UI 来查看这些指标。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  cadvisor:
    image: gcr.io/cadvisor/cadvisor:v0.45.0
    container_name: cadvisor
    hostname: cadvisor
    privileged: true
    devices:
      - /dev/kmsg:/dev/kmsg
    volumes:
      - /var/run:/var/run:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
      # Although the following two directories are not present on OSX removing them stops cAdvisor working
      # Maybe some internal logic checks for the existence of the directory.
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    expose:
      - 8080
    ports:
      - "8080:8080"
```

查看容器指标：

> 1. 导航到 [http://localhost:8080/docker/](http://localhost:8080/docker/)。
> 2. 选择感兴趣的 Docker 容器。

您现在应该会看到与所示类似的 UI。

<图片src =“https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/global-synchronizer/生产-操作/images/c-advisor.png?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=ecd9278225b4212a7eba610e97eb0d9b" className="align-center" style={{width: "100%"}} alt="cAdvisor UI 示例" width="973" height="623" data-path="global-同步器/product-operations/images/c-advisor.png" />

默认情况下，[http://localhost:8080/metrics](http://localhost:8080/metrics) 提供 Prometheus 格式的指标。

#### 普罗米修斯

使用 `prometheus.yml` 配置 Prometheus 以提供应从中抓取指标数据的端点。默认情况下，端口`9090`可以查询存储的监控数据。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  prometheus:
    image: prom/prometheus:v2.40.6
    container_name: prometheus
    hostname: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - 9090:9090
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
global:
  scrape_interval: 15s
  scrape_timeout: 10s
  evaluation_interval: 1m

scrape_configs:

  - job_name: canton
    static_configs:
      - targets:
          - participant1:10013
          - participant2:10023

  - job_name: cadvisor
    static_configs:
      - targets:
          - cadvisor:8080

    # Exclude container labels by default
    # curl cadvisor:8080/metrics to see all available labels
    metric_relabel_configs:
      - regex: "container_label_.*"
        action: labeldrop
```

#### 格拉法纳

Grafana 提供：

* Prometheus 指标存储的连接详细信息
* 使用Web UI所需的用户名和密码
* 任何外部提供的仪表板的位置
* 实际的仪表板

请注意，docker-compose.yml 文件 (`grafana-message-count-dashboard.json`) 中引用的 `Metric Count` 仪表板未内联在下面。原因是这不是手动配置的，而是通过 Web UI 构建然后导出的。有关登录 Grafana 并显示仪表板的说明，请参阅 [Grafana 指标监控](#grafana-metric-monitoring)。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
services:
  grafana:
    image: grafana/grafana:9.3.1-ubuntu
    container_name: grafana
    hostname: grafana
    volumes:
      - ./grafana.ini:/etc/grafana/grafana.ini
      - ./grafana-datasources.yml:/etc/grafana/provisioning/datasources/default.yml
      - ./grafana-dashboards.yml:/etc/grafana/provisioning/dashboards/default.yml
      - ./grafana-message-count-dashboard.json:/var/lib/grafana/dashboards/grafana-message-count-dashboard.json
    ports:
      - 3000:3000
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
instance_name = "docker-compose"

[security]
admin_user = "grafana"
admin_password = "grafana"

[unified_alerting]
enabled = false

[alerting]
enabled = false

[plugins]
plugin_admin_enabled = true
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
---
apiVersion: 1

datasources:
- name: prometheus
  type: prometheus
  access: proxy
  orgId: 1
  uid: prometheus
  url: http://prometheus:9090
  isDefault: true
  version: 1
  editable: false
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
---
apiVersion: 1

providers:
  - name: local
    orgId: 1
    folder: ''
    folderUid: default
    type: file
    disableDeletion: true
    updateIntervalSeconds: 30
    allowUiUpdates: true
    options:
      path: /var/lib/grafana/dashboards
      foldersFromFilesStructure: true
```

#### 依赖关系

Docker 容器之间存在启动依赖关系。例如，同步器需要在参与者之前运行，数据库需要在同步器之前运行。`yaml` 锚点 `x-logging` 启用 GELF 容器日志记录，并在您想要捕获日志记录输出的容器之间复制。请注意，主机地址是主机，而不是网络地址（在 OSX 上）。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
x-logging: &logging
  driver: gelf
  options:
    # Should be able to use "udp://logstash:12201"
    gelf-address: "udp://host.docker.internal:12201"

services:

  logstash:
    depends_on:
      elasticsearch:
        condition: service_healthy

  postgres:
    logging:
      <<: *logging
    depends_on:
      logstash:
        condition: service_started

  participant1:
    logging:
      <<: *logging
    depends_on:
      同步器0:
        condition: service_started
      logstash:
        condition: service_started

  participant2:
    logging:
      <<: *logging
    depends_on:
      同步器0:
        condition: service_started
      logstash:
        condition: service_started

  kibana:
    depends_on:
      elasticsearch:
        condition: service_healthy

  grafana:
    depends_on:
      prometheus:
        condition: service_started
```

#### Docker 镜像

在启动网络之前需要下载 Docker 镜像：

* `ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:${CANTON_VERSION}`
* docker.elastic.co/elasticsearch/elasticsearch:8.5.2
* docker.elastic.co/kibana/kibana:8.5.2
* docker.elastic.co/logstash/logstash:8.5.1
* gcr.io/cadvisor/cadvisor:v0.45.0
* grafana/grafana:9.3.1-ubuntu
* postgres：17.5-牛眼
*舞会/普罗米修斯：v2.40.6

#### 运行 Docker Compose

由于使用上面显示的所有撰写文件运行 `docker compose` 会创建一个很长的命令行，因此使用了帮助程序脚本 `dc.sh`。

建议 Docker 至少使用 **12GB** 内存。要验证 Docker 是否运行内存不足，请运行 `docker stats` 并确保总 `MEM%` 不会太高。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
#!/bin/bash

if [ $# -eq 0 ];then
    echo "Usage: $0 <docker compose command>"
    echo "Use '$0 up --force-recreate --renew-anon-volumes' to re-create network"
    exit 1
fi

set -x

docker compose \
    -p monitoring \
    -f etc/network-docker-compose.yml \
    -f etc/cadvisor-docker-compose.yml \
    -f etc/elasticsearch-docker-compose.yml \
    -f etc/logstash-docker-compose.yml \
    -f etc/postgres-docker-compose.yml \
    -f etc/同步器0-docker-compose.yml0-docker-compose.yml \
    -f etc/participant1-docker-compose.yml \
    -f etc/participant2-docker-compose.yml \
    -f etc/kibana-docker-compose.yml \
    -f etc/prometheus-docker-compose.yml \
    -f etc/grafana-docker-compose.yml \
    -f etc/dependency-docker-compose.yml \
    $*
```

**有用的命令**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./dc.sh up -d       # Spins up the network and runs it in the background

./dc.sh ps          # Shows the running containers

./dc.sh stop        # Stops the containers

./dc.sh start       # Starts the containers

./dc.sh down        # Stops and tears down the network, removing any created containers
```

### 连接到节点为了与正在运行的网络进行交互，可以使用 Canton 控制台进行远程配置。例如：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton -c etc/remote-participant1.conf
```

#### 远程配置

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {

  features.enable-testing-commands = yes  // Needed for ledger-api

  remote-participants.participant1 {
    ledger-api {
      address="0.0.0.0"
      port="10011"
    }
    admin-api {
      address="0.0.0.0"
      port="10012"
    }
  }
} 
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {

  features.enable-testing-commands = yes  // Needed for ledger-api

  remote-participants.participant2 {
    ledger-api {
      address="0.0.0.0"
      port="10021"
    }
    admin-api {
      address="0.0.0.0"
      port="10022"
    }
  }

}  
```

#### 开始使用

使用前面的脚本，您可以按照入门指南中提供的示例进行操作。

### Kibana日志监控

Kibana第一次启动时，必须设置一个数据视图以允许查看日志数据：

> 1. 导航到 [http://localhost:5601/](http://localhost:5601/)。
> 2. 单击“**自行探索**”。
> 3. 从菜单中选择 **分析** > **发现**。
> 4. 单击**创建数据视图**。
> 5. 保存具有以下属性的数据视图：
> * 姓名：`Logs`
> * 索引模式：`logs-\*`
> * 时间戳字段：`@timestamp`

您现在应该看到类似于此处所示的 UI：

<图片src =“https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/global-synchronizer/生产-操作s/images/kibana.png?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=cd4ec5612e9e37131e6a26d0755bc4d0" className="align-center" style={{width: "100%"}} alt="Kibana UI 示例" width="1381" height="724" data-path="global-同步器/product-operations/images/kibana.png" />

在Kibana界面中，您可以：

> * 根据选定字段创建视图
> * 通过日志时间戳查看日志消息
> * 按字段值过滤
> * 搜索文本
> * 使用`KSQL`或`Lucene`查询语言进行查询

有关更多详细信息，请参阅 Kibana 文档。请注意，基于纯文本的宽时间窗口查询可能会导致 UI 性能不佳。有关改进的想法，请参阅[日志记录改进](#logging-improvements)。

### Grafana 指标监控

您可以登录 Grafana UI 并设置仪表板。该示例导入一个 [GrafanaLabs 社区仪表板](https://grafana.com/grafana/dashboards/)，其中包含 cAdvisor 指标的图表。下面导入的 [cAdvisor Export 仪表板](https://grafana.com/grafana/dashboards/14282-cadvisor-exporter/) 的 ID 为 **14282**。

> 1. 导航到 [http://localhost:3000/login](http://localhost:3000/login)。
> 2. 输入用户名/密码：`grafana/grafana`。
> 3. 在侧边框中，选择 **仪表板**，然后选择 **导入**。
> 4. 输入仪表板ID `14282`，然后点击**加载**。
> 5. 在屏幕上选择“**Prometheus**”作为数据源，然后单击“**导入**”。

您应该会看到类似于此处所示的容器系统指标仪表板：<图片src =“https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/global-synchronizer/生产-操作/ima ges/grafana-cadvisor.png?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=0f766d5c12ad5f7201d05a4bff71a7a5" className="align-center" style={{width: "100%"}} alt="示例指标仪表板" width="1034" height="734" data-path="global-同步器/product-operations/images/grafana-cadvisor.png" />

有关如何配置仪表板的信息，请参阅 [Grafana 文档](https://grafana.com/grafana/)。有关可用指标的信息，请参阅本用户手册“监控”部分中的指标文档。

### 监控选择

本节记录了示例监控设置中使用的技术背后的推理。

#### 使用 Docker 日志驱动程序

**原因：**

* 大多数 Docker 容器可以配置为将所有调试输出记录到 stdout。
* 容器可以按提供的方式运行。
* 不需要添加额外的 dockerfile 层来安装和启动日志抓取器。
* 无需担心本地文件命名、日志轮转等问题。

#### 使用 GELF Docker 日志驱动程序

**原因：**

* 它随 Docker 一起提供。
* 它有一个可解码的 JSON 负载。
* 没有syslog的大小限制。
* UDP监听器可用于调试问题。

#### 使用 Logstash

**原因：**

* 这是一种将容器提供的 GELF 输出桥接到 Elasticsearch 的轻量级方法。
* 它有一个简单的概念模型（由输入/过滤器/输出插件组成的管道）。
* 它拥有一个庞大的输入/过滤器和输出插件生态系统。
* 它将容器日志记录输出映射到结构/ECS 格式的逻辑具体化。
* 它可以与`stdin`/`stdout`输入/输出插件一起运行以用于测试。
* 它可用于提供 Elasticsearch、Loki 或 Graylog。
* 如果需要，它支持弹性通用架构 (ECS)。

#### 使用 Elasticsearch/Kibana

**原因：**

* 将 Logstash 与 Elasticsearch 和 Kibana（ELK 堆栈）结合使用是建立日志记录基础设施的成熟方法。
* 这些产品的良好默认设置允许以几乎零配置启动基本设置。
* 与 Loki 或 Graylog 等其他选项相比，ELK 设置可以作为良好的基准。

#### 使用 Prometheus/Grafana

**原因：**

* Prometheus 定义并使用 OpenTelemetry 参考文件格式。
* 通过 HTTP 端点公开指标可以轻松直接检查指标值。
* Prometheus 从底层系统提取指标的方法意味着运行的容器不需要基础设施来存储和推送指标数据。
* Grafana 与 Prometheus 配合得很好。

### 日志记录改进

该版本的示例仅具有通过 GELF 提供的日志记录结构。可以通过以下方式改进这一点：

> * 从底层容器中提取数据作为 JSON 流。
> * 将此 JSON 数据中的字段映射到 ECS，以便常用字段值（例如日志级别）使用相同的名称。
> * 使用允许快速过滤某些字段（例如日志级别）的模式配置 Elasticsearch。{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/observe/health.rst" hash="64490235" */}

## 参与者节点健康状况

参与者以多种方式公开健康状态信息，这些信息可以在故障排除时手动检查或集成到更大的监控和编排系统中。

### 使用 gRPC Health 服务进行负载平衡和编排

参与者节点提供`grpc.health.v1.Health`服务，实现[gRPC健康检查协议](https://github.com/grpc/grpc/blob/master/doc/health-checking.md)协议。

Kubernetes 容器可以被配置为使用它来进行就绪或活跃性探测，例如

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
readinessProbe:
  grpc:
    port: <port>
```

默认情况下，该端口是用于 `Ledger API` 的端口。

同样，[gRPC 客户端](https://grpc.io/docs/guides/health-checking/#enabling-client-health-checking) 和 [NGinx](https://docs.nginx.com/nginx/admin-guide/load-balancer/grpc-health-check/) 可以配置为监视运行状况服务以进行流量管理和负载平衡。

您可以使用 [grpcurl](https://github.com/fullstorydev/grpcurl) 等命令行工具手动检查参与者的运行状况（使用参与者的实际地址）：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
$ grpcurl -plaintext <host>:<port> grpc.health.v1.Health/Check
{
  "status": "SERVING"
}
```

如果当前已准备好并可用于处理请求，则调用 [Check](https://github.com/grpc/grpc-proto/blob/6565a1ba38af695ace7c3ce6e6ff837ee87d4c10/grpc/health/v1/health.proto#L55) 将响应 `SERVING`。

调用 [Watch](https://github.com/grpc/grpc-proto/blob/6565a1ba38af695ace7c3ce6e6ff837ee87d4c10/grpc/health/v1/health.proto#L72) 将执行流式运行状况检查。服务器将立即发送参与者当前的健康状况，然后每当健康状况发生变化时发送新消息。

当配置多个参与者副本时，被动节点返回`NOT_SERVING`。

实际上，参与者的健康状况由其所依赖的组件的健康状况组成。您可以通过将 [service](https://github.com/grpc/grpc-proto/blob/6565a1ba38af695ace7c3ce6e6ff837ee87d4c10/grpc/health/v1/health.proto#L29) 字段设置为组件名称来发出请求，按名称单独查询这些组件。空或未设置的 `service` 字段返回所有组件的聚合运行状况。未知名称将导致 gRPC `NOT_FOUND` 错误。

### 通过 HTTP 检查健康状况

健康检查也可以通过 HTTP 完成，这对于不支持 gRPC 健康检查协议的框架非常有用。在节点的配置中设置monitoring.http-health-server.port=将在URL`http://<host>:<port>/health`公开健康信息。

这里通过 HTTP 响应状态代码报告重要信息。* `200` 状态相当于 gRPC Health Service 中的 `SERVING`。
* `503`的状态相当于`NOT_SERVING`。
* 状态`500` 表示检查因任何其他原因失败。

Kubernetes 还可以将它们用于就绪探针：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
readinessProbe:
  httpGet:
    port: <port>
    path: /health
```

### 总体健康状况检查

通过在节点上调用 `health.status` 命令，可以在 Canton 控制台中显示有关参与者节点的一般信息，包括不健康的同步器和依赖项以及节点当前是否处于活动状态。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res1: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
    Uptime: 2.069737s
    Ports: 
        ledger: 30183
        admin: 30184
        json: 30185
    Connected synchronizers: None
    Unhealthy synchronizers: None
    Active: true
    Components: 
        memory_storage : Ok()
        connected-同步器 : Not Initialized
        sync-ephemeral-state : Not Initialized
        sequencer-client : Not Initialized
        acs-commitment-processor : Not Initialized
    Version: 3.4.11-SNAPSHOT
    Supported protocol version(s): 34
```

参与者节点的管理 API 通过 [ParticipantStatusService](https://github.com/DACH-NY/canton/blob/release-line-3.3/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/participant/v30/participant_status_service.proto#L10) 以结构化形式提供对此数据的编程访问`ParticipantStatus` 通话。

广州控制台还可以通过调用顶层命令来提供有关“所有”连接节点的信息，包括远程连接的节点。

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
@健康状况
    res2：CantonStatus = Sequencer“sequencer1”的状态：
    序列器 ID：da::1220a82692abc55c0367abefc4bdbc23df25688230430ddfeef5759845f26d5cc29c
    同步器 ID：da::1220a82692abc55c0367abefc4bdbc23df25688230430ddfeef5759845f26d5cc29c::34-0
    正常运行时间：5.968597s
    端口： 
        公众号：30187
        管理员：30188
    连接的参与者： 
        PAR::参与者2::1220a4d7463b...
        PAR::参与者1::12201ff69b1d...
    连接的Mediator： 
        医学::调解员1::122009299340...
    序列器：SequencerHealthStatus（活动 = true）
    额外细节：无
    组件： 
        内存存储：好的（）
        Sequencer：好的（）
    接受管理员更改：true
    版本：3.4.11-快照
    协议版本：34Mediator“mediator1”的状态：
    节点 uid: mediator1::12200929934059da3e012af672ee8a5d26a7e4b3e5084920be298f791f7619843c78
    同步器 ID：da::1220a82692abc55c0367abefc4bdbc23df25688230430ddfeef5759845f26d5cc29c::34-0
    正常运行时间：5.920214s
    端口： 
        管理员：30186
    活跃：真实
    组件： 
        内存存储：好的（）
        Sequencer客户端：Ok()
        序列器连接池：Ok()
        序列器订阅池：Ok()
        内部Sequencer连接-sequencer1-0 : Ok()
        订阅-sequencer-connection-sequencer1-0 : 好的()
    版本：3.4.11-快照
    协议版本：34

    参与者“participant1”的状态：
    参与者 ID：PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
    正常运行时间：7.954779s
    端口： 
        账本：30183
        管理员：30184
        数据格式：30185
    连接的同步器： 
        达::1220a82692ab...::34-0
    不健康的同步器：无
    活跃：真实
    组件： 
        内存存储：好的（）
        连接同步器：Ok()
        同步短暂状态：Ok()
        Sequencer客户端：Ok()
        acs-承诺处理器：Ok()
        序列器连接池：Ok()
        序列器订阅池：Ok()
        内部Sequencer连接-sequencer1-0 : Ok()
        订阅-sequencer-connection-sequencer1-0 : 好的()
    版本：3.4.11-快照
    支持的协议版本：34

    参与者“participant2”的状态：
    参与者 ID：PAR::participant2::1220a4d7463bd34b2ba3704401b48ab41d8f88cdcbe512fc1ef071aad97fef106161
    正常运行时间：8.670214s
    端口： 
        账本：30180
        管理员：30181
        数据格式：30182
    连接的同步器： 
        达::1220a82692ab...::34-0
    不健康的同步器：无
    活跃：真实
    组件： 
        内存存储：好的（）
        连接同步器：Ok()
        同步短暂状态：Ok()
        Sequencer客户端：Ok()
        acs-承诺处理器：Ok()
        序列器连接池：Ok()
        序列器订阅池：Ok()
        内部Sequencer连接-sequencer1-0 : Ok()
        订阅-sequencer-connection-sequencer1-0 : 好的()
    版本：3.4.11-快照
    支持的协议版本：34
```

### Generating a Node Health Dump for Troubleshooting

When interacting with support or attempting to troubleshoot an issue, it is often necessary to capture a snapshot of relevant execution state. Canton implements a facility that gathers key system information and bundles it into a ZIP file.

This will contain:

* The configuration you are using, with all sensitive data stripped from it (no passwords).
* An extract of the log file. Sensitive data is not logged into log files.
* A current snapshot on Canton metrics.
* A stacktrace for each running thread.

These health dumps can be triggered from the canton console with `health.dump()`, which returns the path to the resulting ZIP file.

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
@health.dump()
    ..
````如果控制台配置为访问远程节点，它们的状态也将包括在内。您可以通过在运行命令时定位特定节点来获取特定节点的数据，例如`remoteParticipant1.health.dump()`

当打包大量数据时，增加dump命令的默认超时时间：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ health.dump(timeout = 2.minutes)
    ..
```

还可以通过 [StatusService](https://github.com/DACH-NY/canton/blob/release-line-3.3/community/admin-api/src/main/protobuf/com/digitalasset/canton/admin/health/v30/status_service.proto#L10) 在参与者节点的 `Admin API` 上通过 gRPC 收集运行状况转储`HealthDump`。此调用流回生成的 ZIP 文件的字节。

### 监控缓慢或卡住的任务

如果您启用，某些操作可以在速度缓慢时报告

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.monitoring.logging.log-slow-futures = yes
```

如果任务花费的时间比预期长，将定期发出日志行直到完成，例如`<task name> has not completed after <duration>`。默认情况下禁用此功能以减少开销。

Canton 还提供了一个工具来定期测试我们是否能够及时安排新任务，通过配置启用

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.monitoring.deadlock-detection.enabled = yes
```

如果检测到问题，将发出包含`Task runner <name> is stuck or overloaded for <duration>`的日志行。这可能表明 CPU 等资源过载、执行上下文太小，或者太多任务被卡住。如果问题自行解决，将发出后续日志消息：`Task runner <name> is just overloaded, but operating correctly. Task got executed in the meantime`。

### 禁用致命故障重新启动

进程应该在进程管理器下运行，例如`systemd`或Kubernetes，它可以监视它们并根据需要重新启动它们。默认情况下，如果发生致命故障，参与者节点进程将退出。

如果您想禁用此行为

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters.exit-on-fatal-failures = no
```

在这种情况下，这将导致节点保持活动状态并报告不健康。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/observe/commitments.rst" hash="448aca51" */}

## 监控 ACS 承诺

未能及时发送承诺的参与者对其对应参与者来说是有问题的：对应参与者无法修剪其状态，因为他们没有证据证明其状态与参与者的状态相同。有关承诺的更多信息，请参阅修剪概述部分。本页描述 ACS 承诺的监控选项。承诺监控以多种方式支持参与节点运营商。首先，监控提供了对承诺生成性能的洞察，允许参与节点操作员排除和修复潜在的性能问题。例如，监控指标表明潜在的性能瓶颈，操作员可以将其用作配置承诺生成的输入。

其次，监控可以洞察相对参与者的承诺状况。这与参与者节点运营商相关，因为在承诺生成中落后的对方参与者（无论是因为它有故障还是因为网络速度慢）会阻止对参与者的修剪：参与者不知道其状态和对方参与者的状态是否分歧，并且无法修剪，因为它可能需要调查潜在的分叉。操作员可以使用监控指标来识别速度慢的对方参与者，并可能将其列入黑名单。

### 监控自己的承诺

我们提供以下用于承诺生成的指标，这些指标在指标参考部分中有详细描述：

* `daml.participant.sync.commitments.compute`：衡量参与节点花费计算承诺的时间。
* `daml.participant.sync.commitments.sequencing-time`：测量承诺期结束与Sequencer观察相应承诺的时间之间的时间。
* `daml.participant.sync.commitments.catchup-mode-enabled`：测量追赶模式被触发的次数。

### 监控相对参与者的承诺

运营商可以通过延迟指标监控对方参与者的承诺状态。这些指标可以揭示在发送承诺方面落后的缓慢对方参与者，并使操作员能够配置阈值，定义何时认为对方参与者速度缓慢。

操作员可以将相对参与者分为三类，这会影响指标报告：

* *默认*
* *杰出*
* *单独监控*

*单独监控的*对方参与者始终显示该参与者的承诺延迟。对方参与者的*杰出*和*默认*分组仅显示该组中最大的延迟。然后可以使用检查工具和直接监控来识别缓慢的对手参与者。

以下所有指标均在指标参考部分中详细描述。

* *默认*：所有未区分或单独监控的相对参与者默认属于该组。我们为该组中的所有参与者发布一个聚合指标：`daml.participant.sync.commitments.同步器.largest-counter-participant-latency`，它代表未完成的对应参与者的承诺超过阈值数量的调节间隔的最高延迟（以毫秒为单位）。* *尊贵*：运营商可以选择将部分默认的对方参与者升级为尊贵组，例如与其有重要业务关系的对方参与者。我们为所有杰出参与者生成一个聚合指标，在`daml.participant.sync.commitments.同步器.largest-distinguished-counter-participant-latency`下发布，就像默认组一样，该指标代表超过`thresholdDistinguished`数量的对帐间隔内未完成承诺的最高延迟（以毫秒为单位）。

  以下示例展示了`participant1`的算子如何将对方`participant4`添加到同步器`同步器2Id`上的区分组中，并将对方`participant2`从同步器`同步器1Id`上的区分组中删除：

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  participant1.commitments.add_config_distinguished_slow_counter_participants(
    Seq(participant4Id),
    Seq(同步器2Id),
  )
  ```

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  participant1.commitments.remove_config_distinguished_slow_counter_participants(
    Seq(participant2.id),
    Seq(同步器1Id),
  )
  ```

* *单独监控*：操作员可以选择要单独监控其承诺状态的对应参与者，例如因为他们最近出现间歇性故障并且刚刚恢复，或者因为操作员观察到其他组之一的速度下降并希望找到原因。每个参与者在 daml.participant.sync.commitments.同步器.counter-participant-latency 下都有自己独特的标签。可以根据业务关系设置单独的警报。 （注意：任何参与者，无论是*默认*还是*杰出*，都可以添加到*单独监控*。杰出参与者即使是*单独监控*，仍保留在*杰出*组中。相反，添加到*单独监控*的*默认*参与者将从默认组中删除。）

  以下示例显示`participant1`的操作员如何添加/删除要在同步器`synchronizerId`上*单独监控*的对方参与者`participant3`：

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  participant1.commitments.add_participant_to_individual_metrics(
    Seq(participant3.id),
    Seq(synchronizerId),
  )
  ```

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  participant1.commitments.remove_participant_from_individual_metrics(
    Seq(participant3.id),
    Seq(synchronizerId),
  )
  ```

参与者的操作员可以同时在多个同步器上设置监控配置，包括“默认”和“杰出”组以及“单独监控”的阈值。下面的示例显示了`participant1`的操作员如何将监控配置应用于同步器`同步器1Id`和`同步器2Id`。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val update1Config = new SlowCounterParticipant同步器Config(
  synchronizerIds = Seq(同步器1Id, 同步器2Id),
  distinguishedParticipants = Seq(participant3.id),
  thresholdDistinguished = 15,
  thresholdDefault = 15,
  individuallyMonitored = Seq.empty,
)
participant1.commitments.set_config_for_slow_counter_participants(Seq(update1Config))
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
