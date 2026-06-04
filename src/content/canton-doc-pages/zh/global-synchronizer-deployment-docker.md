---
title: "Canton Docker 运维"
slug: "global-synchronizer-deployment-docker"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/docker.md"
source_title: "Canton Docker Operations"
tags:
  - global-synchronizer
  - deployment
  - docker
---

# Canton Docker 运维

> Canton 官方 Docker 镜像下载、运行与容器配置说明。

> 获取并运行 Canton Docker 镜像


（有关运行 Canton Docker 映像的说明，请参阅使用 Docker 安装。）

您可以使用以下方式下载 Canton docker 镜像：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker pull \
    europe-docker.pkg.dev/da-images/public/docker/canton-base:3.4.8
docker pull \
    europe-docker.pkg.dev/da-images/public/docker/canton-participant:3.4.8
docker pull \
    europe-docker.pkg.dev/da-images/public/docker/canton-sequencer:3.4.8
docker pull \
    europe-docker.pkg.dev/da-images/public/docker/canton-mediator:3.4.8
```

访问 `https://europe-docker.pkg.dev/v2/da-images/public/docker/canton-participant/tags/list` 查看可用标签。

这些 docker 镜像从 Canton 版本 3.4.8 开始发布。

快照版本在`/da-images/public-unstable/docker/`而不是`/da-images/public/docker/`可用，但不建议将它们用于任何生产用途，并且会定期清理。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/install/docker.rst" hash="10693c6e" */}

下载 docker 镜像的 howto 链接。链接到硬件和软件要求。解释如何从 docker 运行 canton。

# 使用 Docker 容器

## 使用参与者图像

为了方便起见，我们提供了一个预先配置的参与者图像，可用于启动具有合理默认值的 Canton 参与者。

使用此图像需要设置几个环境变量：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker run \
    -e AUTH_TARGET_AUDIENCE="audience" \
    -e AUTH_JWKS_URL="fake.com/jwks" \
    -e CANTON_PARTICIPANT_POSTGRES_SERVER="canton-postgres" \
    -e CANTON_PARTICIPANT_POSTGRES_PORT="5432" \
    -v "$(pwd)/bootstrap.sc:/app/bootstrap.sc" \
    --rm -it \
    europe-docker.pkg.dev/da-images/public-unstable/docker/canton-participant:3.5.0-ad-hoc.20251021.17321.0.v2cdf16447
```

请注意，您需要一个有效的 postgres 实例。

该图像要求您通过引导脚本初始化参与者。有关更多详细信息，请参阅手动身份初始化。

要查看所有配置默认值和可能的环境变量，请运行

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cid=$(docker create europe-docker.pkg.dev/da-images/public-unstable/docker/canton-participant:3.5.0-ad-hoc.20251021.17321.0.v2cdf1644) && docker cp "$cid":/app/app.conf ./app.conf && docker rm "$cid"
cat app.conf
```

## 日志记录

日志采用 JSON 编码并发送到 stdout。日志级别通过`-e LOG_LEVEL_STDOUT=INFO`设置。它默认为调试。

## 绑定端口

`canton-participant` 图片绑定：

* 账本API端口：5001
* 管理API端口：5002
* HTTP 账本 API 端口：7575
* GRPC健康服务器端口：5061

`canton-mediator` 图片绑定：

* 管理API端口：5007
* GRPC健康服务器端口：5061

`canton-sequencer` 图片绑定：

* 公共API：5008
* 管理API：5009
* GRPC健康服务器端口：5061

## 提供自定义配置和 DAR

要提供自定义配置，可以

1.通过`ADDITIONAL_CONFIG`环境变量添加，或者
2. 将`/app/additional-config.conf`安装到容器中。

Dars 必须动态添加。这是通过远程控制台或管理 API 完成的。

要使用自定义配置运行参与者控制台：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker run -e ADDITIONAL_CONFIG="canton.participants.participant1 {
      storage.type = memory
      admin-api.port = 5012
      ledger-api.port = 5011
      http-ledger-api.server.port = 5013
    }" \
    --rm -it \
    europe-docker.pkg.dev/da-images/public-unstable/docker/canton-participant:3.5.0-ad-hoc.20251021.17321.0.v2cdf1644 \
    --console
```

`--console` 标志以交互式控制台模式启动 Canton。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
