---
title: "前置条件与安装"
slug: "appdev-quickstart-prerequisites"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/prerequisites.md"
source_title: "Prerequisites and Installation"
tags:
  - appdev
  - quickstart
  - prerequisites
---

# 前置条件与安装

> 配置开发环境并安装 Canton Network Quickstart。

# 前置条件与安装

# Canton Network quickstart 安装

## 简介

Quickstart 应用通过提供**必要**脚手架，帮助你和团队熟悉 CN 应用开发。它是可扩展的起点，用于满足业务需求。熟悉 Quickstart 后，请审视技术选型与应用设计以确定所需变更；技术与设计决策由你决定。

## 概览

本指南介绍 CN Quickstart 的安装与 `LocalNet` 部署。我们按经验水平提供[快速安装](#fast-path-installation)与[分步说明](#step-by-step-instructions)。如发现错误请联系 Digital Asset 代表。

### 路线图

* 安装后[探索演示](/appdev/quickstart/running-the-demo)，在示例应用中完成一次业务操作。
* 了解 Quickstart 项目结构，请阅读[项目结构指南](/appdev/quickstart/project-structure)。
* 在 [使用 lnav 调试与排障](/appdev/quickstart/lnav) 中学习日志调试。
* 更多调试信息见 [cn-quickstart 仓库](https://github.com/digital-asset/cn-quickstart) 中的可观测性与排障章节。

## 前置条件

访问 [CN-Quickstart GitHub 仓库](https://github.com/digital-asset/cn-quickstart) 为公开；会拉取 Digital Asset 提供的部分制品。

CN Quickstart 为 Docker 化应用，需要 [Docker Desktop](https://www.docker.com/products/docker-desktop/)。建议为 Docker Desktop 分配 8 GB 内存；若容器不健康可酌情增加资源。内存不足时请关闭 Observability。

其他要求包括：

* [Curl](https://curl.se/download.html)
* [Direnv](https://direnv.net/docs/installation.html)
* [Nix](https://nixos.org/download/)
* Windows 用户须以管理员权限安装并使用 [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)。

### Nix 安装说明

检查本机是否已安装 Nix：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nix --version
```

若返回类似 `Nix (Nix) 2.25.2`，则已就绪。

macOS 推荐安装：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sh <(curl -L https://nixos.org/nix/install)
```

Linux 推荐安装（Windows 用户应在 WSL 2 中执行本命令及后续所有命令）：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sh <(curl -L https://nixos.org/nix/install) --daemon
```

## 快速安装

若已熟悉前置条件，可使用下列精简步骤；更详细说明见下文。

1. [从 GitHub 克隆](#clone-from-github) and cd into the `cn-quickstart` repository: `git clone https://github.com/digital-asset/cn-quickstart.git`
2. Verify that the [Docker Desktop](#docker) app is running on your computer: `docker info`
3. Login to Docker repositories via the terminal: `docker login`
4. **cd** into the `quickstart` subdirectory: `cd quickstart`
5. [安装 Daml SDK](#install-daml-sdk) from the quickstart subdirectory: `make install-daml-sdk`
6. [配置本地开发](#deploy-a-validator-on-localnet) environment: `make setup`
7. When prompted, enable OAuth2, disable Observability, disable TEST MODE, and leave the party hint blank to use the default value.
8. Build the application from the `quickstart` subdirectory: `make build`
9. In a new terminal window, initiate log collection from the `quickstart` subdirectory: `make capture-logs`
10. Return to the previous terminal window to start the application and Canton services: `make start`
11. Optional - In a separate shell, from the `quickstart` subdirectory, run the [Canton 控制台](#connecting-to-the-local-canton-nodes): `make canton-console`
12. Optional - In a fourth shell, from the `quickstart` subdirectory, begin the Daml Shell: `make shell`
13. When complete, [关闭应用](#closing-the-application) and other services with: `make stop && make clean-all`
14. If applicable, close Canton Console with `exit` and close Daml Shell with `quit`.

## 分步说明

### 从 GitHub 克隆

将 `cn-quickstart` 仓库克隆到本机并 **cd** 进入。

git clone [https://github.com/digital-asset/cn-quickstart.git](https://github.com/digital-asset/cn-quickstart.git)
cd cn-quickstart
direnv allow

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-allow-direnv.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=add8265c0387084840d113832461ca2e" alt="允许 direnv" width="792" height="211" data-path="images/docs_website/01-allow-direnv.png" />

### Docker

确认本机 Docker Desktop 正在运行。

在终端登录 Docker 仓库。

docker login

上一条命令需要 [Docker Hub](https://app.docker.com/) 用户名与密码，或*个人访问令牌（PAT）*。

应返回「Login Succeeded」。

### 安装 Daml SDK

进入 `quickstart` 子目录并安装 Daml SDK。

cd quickstart
make install-daml-sdk

<Note>
  提供项目编排的 `Makefile` 位于 `quickstart/`；`make` 仅在该目录内有效。

  若出现与 `make` 相关的错误，请确认当前工作目录。
</Note>

Daml SDK 体积较大，安装可能需要数分钟。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/06-unpack-sdk.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=bbfffb42c7250a27209501a2eb47adcf" alt="Daml SDK 解压" width="718" height="275" data-path="images/docs_website/06-unpack-sdk.png" />

### 在 LocalNet 部署验证者

运行 `make setup` 配置本地开发环境。

关闭 `Observability`，启用 OAuth2；party hint 留空使用默认值，并关闭 `TEST MODE`。

<Note>
  party hint 是 party 节点对其身份哈希的别名，并非用户身份的一部分，仅为便利功能；多个 party 节点可使用相同 hint。
</Note>

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
% make setup
Starting local environment setup tool...
./gradlew configureProfiles --no-daemon --console=plain --quiet
Enable Observability? (Y/n): n
OBSERVABILITY_ENABLED set to 'false'.

Enable OAUTH2? (Y/n): y
AUTH_MODE set to 'oauth2'.

Specify a party hint (this will identify the participant in the
  network) [quickstart-USERNAME-1]:
PARTY_HINT set to 'quickstart-USERNAME-1'.

Enable TEST_MODE? (Y/n): n
TEST_MODE set to 'off'.

.env.local updated successfully.
```

可随时再次运行 `make setup` 修改上述选项。

<Note>
  若分配给 Docker Desktop 的内存少于 8 GB，OAuth2 与 Observability 可能不稳定。
</Note>

构建应用。

make build

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/07-build-success-1.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=932899ab2d860f43ca157a6904434228" alt="构建成功" width="619" height="90" data-path="images/docs_website/07-build-success-1.png" />

在新终端窗口中，于 `quickstart` 子目录启动日志采集。

make capture-logs

完成后回到原终端，启动应用与 Canton 服务。

make start

### 连接本地 Canton 节点

在另一 shell 中，于 `quickstart` 子目录运行 Canton Console。

make canton-console

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/11-canton-console.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=a43a087a3b359953280e29e0568e3acf" alt="Canton 控制台" width="567" height="255" data-path="images/docs_website/11-canton-console.png" />

在第四个 shell 中，于 quickstart 子目录启动 Daml Shell。

make shell

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/12-daml-shell.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=7389585ba51905f5af1dabde12f65319" alt="Daml Shell" width="638" height="159" data-path="images/docs_website/12-daml-shell.png" />

### 关闭应用

*⚠️（若将立即继续使用 CN Quickstart，请暂缓执行本节）*

#### 关闭 Canton 控制台

完成后在 Canton 控制台终端运行 `exit`，停止并移除控制台容器。

#### 关闭 Daml Shell

在 Daml Shell 终端执行 `quit` 停止 shell 容器。

#### 关闭 CN Quickstart

最后关闭应用与可观测性服务：

make stop && make clean-all

开发与每次会话结束时运行 `make clean-all` 可避免后续构建冲突。

## 下一步

你已成功安装 CN Quickstart。

下一节「探索演示」将演示示例应用。

### 将应用连接到 Canton Network

`LocalNet` 部署连接本地验证者，再连接本地超级验证者（synchronizer）。预发布与生产需连接再接入公共 Canton Network 的验证者。

Canton Network 提供三个 synchronizer 池：生产为 `MainNet`，生产预发布为 `TestNet`；开发者多数时间连接开发预发布网络 `DevNet`。

连接 DevNet 需要接入在 CN 白名单上的 [SV 节点](/global-synchronizer/deployment/onboarding-process)。GSF 发布可赞助验证者节点的 [SV 列表](https://sync.global/sv-network/)。访问 `DevNet` 请联系赞助 SV 获取 VPN 信息。

## 资源

* [Curl](https://curl.se/download.html)
* [Direnv](https://direnv.net/docs/installation.html)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Docker Hub](https://app.docker.com/)
* [GSF list of SV Nodes](https://sync.global/sv-network/)
* [Digital Asset Docker](https://console.cloud.google.com/artifacts/docker/da-images/europe/public)
* [Nix](https://nixos.org/download/)
* [Quickstart GitHub repository](https://github.com/digital-asset/cn-quickstart)
* [Validator onboarding documentation](/global-synchronizer/deployment/onboarding-process)
* [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
