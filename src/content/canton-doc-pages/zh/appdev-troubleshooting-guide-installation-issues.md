---
title: "安装问题"
slug: "appdev-troubleshooting-guide-installation-issues"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/installation-issues.md"
source_title: "Installation Issues"
tags:
  - appdev
  - troubleshooting-guide
  - installation-issues
---

# 安装问题

> 排查 Canton Network 开发环境安装中的 Nix、Docker 与内存问题。

本页面介绍了设置 Canton Network 开发环境时可能遇到的常见安装问题，包括 Nix shell 故障、Docker 配置和内存分配。

## 尼克斯问题

### Nix shell 无法启动

如果 `nix-shell` 因哈希不匹配或下载错误而退出，则您的本地 Nix 缓存可能已过时。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Clear the Nix store cache for the affected derivation
nix-collect-garbage -d

# Retry
nix-shell
```

当 `nix-shell` 在评估过程中挂起时，请检查您的 `NIX_PATH` 设置是否正确，并且不存在冲突的 Nix 通道：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nix-channel --list
```

删除任何意外的通道并重新运行`nix-shell`。

### 安装后“未找到命令：nix”

您的 shell 配置文件可能不源自 Nix 环境。将以下内容添加到您的`~/.bashrc`或`~/.zshrc`：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
source ~/.nix-profile/etc/profile.d/nix.sh
```

或者，完全重新启动终端会话。在 macOS 上，系统更新后 Nix 有时需要重新安装：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Uninstall first
/nix/nix-installer uninstall

# Reinstall from https://nixos.org/download
```

### Nix 和系统包之间的 PATH 冲突

如果系统安装的工具（例如，不同的 Java 版本）优先于 Nix 提供的工具，请验证您的 PATH 顺序：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
which java
# Should point to /nix/store/... if using nix-shell
```

在`nix-shell`内，Nix 将其路径添加到`$PATH`。如果您仍然看到系统二进制文件，请检查您的 shell 配置文件是否在 Nix 之后附加路径或覆盖它们。

## Docker 配置

### LocalNet 内存不足

LocalNet 在本地运行完整的 Canton 拓扑，需要大量资源。如果容器因 OOM（内存不足）而崩溃或无法启动，请增加 Docker 的内存分配。

**LocalNet 的最低要求：**

* 内存：16GB
* CPU：4核
* 磁盘：50 GB 可用空间

**Docker 桌面：** 设置 > 资源 > 将内存设置为 16 GB 或更高，然后应用并重新启动。

**科利马 (macOS)：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
colima stop
colima start --memory 16 --cpu 4
```

### 卷安装权限错误

在 Linux 上，如果您的用户 ID 与容器的预期 UID 不匹配，Docker 容器可能无法写入已安装的卷。通过确保主机目录具有适当的权限来修复此问题：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
chmod -R 777 .data/
```

或者使用与您的主机 UID 匹配的 `--user` 标志运行 Docker：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose run --user "$(id -u):$(id -g)" <service>
```

### Docker Compose 版本不匹配

Canton 快速入门需要 Docker Compose 2.26.0 或更高版本。如果您看到：

```
'env_file[1]' expected type 'string', got unconvertible type 'map[string]interface {}'
```

升级 Docker Compose：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose version  # Check current version

# macOS with Homebrew
brew install docker-compose

# Or update Docker Desktop to the latest version
```## 内存分配

### 沙箱的 JVM 堆

Daml 沙箱在 JVM 上运行，并默认采用保守的堆设置。如果遇到`java.lang.OutOfMemoryError: Java heap space`，增加堆：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export JAVA_OPTS="-Xmx4g -Xms2g"
dpm sandbox
```

### LocalNet 上的 OOM 杀死

当 Docker 以静默方式终止容器时，检查 OOM 事件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker inspect <container_name> --format='{{.State.OOMKilled}}'
```

如果返回`true`，则需要增加 Docker 的内存分配（请参阅上面的 Docker 部分）。您还可以检查系统级 OOM 事件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dmesg | grep -i "out of memory"
```

### 资源限制摘要

|环境 |最小内存|推荐内存 |最低 CPU |
| ------------- | ---------- | ------------------ | -------- |
|仅沙盒 | 4GB| 8GB| 2 核 |
|本地网| 16GB| 24GB| 4 核 |
| cn-快速入门 | 8GB| 16GB| 4 核 |

<Note>
  Before running cn-quickstart, you must execute `make setup` and `make build` before `make start`. Skipping these steps causes startup failures that can look like resource problems.
</Note>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
