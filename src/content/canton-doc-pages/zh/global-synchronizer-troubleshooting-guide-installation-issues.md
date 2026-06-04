---
title: "安装问题"
slug: "global-synchronizer-troubleshooting-guide-installation-issues"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/installation-issues.md"
source_title: "Installation Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - installation-issues
---

# 安装问题

> Docker/Kubernetes 与网络导致的安装故障排查。

> 解决验证者安装过程中的 Docker、Kubernetes 和网络问题

安装失败通常分为三类：容器运行时问题、Kubernetes 配置问题或阻止验证者到达synchronizer的网络级块。

## Docker 问题

### 镜像拉取失败

如果 `docker compose up` 因镜像拉取错误而失败：

```
Error response from daemon: pull access denied for digitalasset/canton-participant
```

可能的原因：

* 您尚未登录容器注册表。使用您的 JFrog 凭据运行 `docker login digitalasset-docker.jfrog.io`。
* 您的 JFrog 帐户无权访问所需的存储库。通过 [support.digitalasset.com](https://support.digitalasset.com) 请求访问。
* 图像标签中的拼写错误。根据发行说明验证 `docker-compose.yaml` 或 `.env` 文件中的映像名称和版本。

### 资源限制

立即崩溃或显示`OOMKilled`状态的容器需要更多内存。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check if any container was OOM-killed
docker inspect --format='{{.State.OOMKilled}}' <container_name>
```

验证者的最低资源要求：

* **内存：** 8 GB 分配给 Docker
* **CPU：** 4 核
* **磁盘：** 50 GB 可用空间

对于 macOS 上的 Colima 用户：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
colima stop
colima start --memory 8 --cpu 4 --disk 100
```

### 卷权限错误

如果容器因已安装卷上的权限被拒绝错误而失败：

```
java.io.IOException: Permission denied: /data/canton
```

容器用户（通常 UID 1000）必须具有对主机目录的写访问权限。解决这个问题：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo chown -R 1000:1000 ./data
```

## Kubernetes 问题

### Helm 图表错误

`helm install`或`helm upgrade`期间常见的Helm故障：

* **`Error: INSTALLATION FAILED: cannot re-use a name that is still in use`** -- 存在先前版本。请使用`helm upgrade`代替，或先使用`helm uninstall 验证者 -n validator`卸载。
* **`Error: template: splice-验证者/templates/...: ... not defined`** -- 您的值文件引用了此图表版本中不存在的变量。将您的 `validator-values.yaml` 与目标版本的图表 `values.yaml` 进行比较。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Inspect the chart's default values
helm show values splice-validator/splice-validator --version 0.5.4
```

### PVC 配置失败

如果 pod 仍处于 `Pending` 状态，请检查 PersistentVolumeClaim (PVC) 事件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl describe pvc -n validator
```

常见原因：

* 您的集群中不存在该 StorageClass。使用 `kubectl get storageclass` 列出可用的课程。
* 您的云提供商帐户中的磁盘配额不足。
* 请求的存储大小超出可用容量。

### 初始化容器失败

如果主容器从未启动，则初始化容器可能会失败：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl logs -n validator <pod-name> -c init-db --previous
```

Init 容器通常会由于数据库连接问题而失败 - PostgreSQL 实例无法访问或凭据错误。

### 图像拉取秘密

Kubernetes 需要显式凭据才能从私有注册表中提取：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret docker-registry jfrog-creds \
  --docker-server=digitalasset-docker.jfrog.io \
  --docker-username=$JFROG_USER \
  --docker-password=$JFROG_TOKEN \
  -n validator
```

然后在`imagePullSecrets`下的`validator-values.yaml`中引用`jfrog-creds`。

## 网络问题

### DNS 解析

如果您的验证者无法解析synchronizer主机名：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# From inside a Kubernetes pod
kubectl exec -n validator deployment/validator-app -- nslookup sequencer.sync.global
```

如果 DNS 失败，请检查集群的 CoreDNS Pod 和任何自定义 DNS 配置。

### 防火墙规则

您的验证者需要以下端口的出站访问权限：* **443 (HTTPS/gRPC-TLS)** -- 到 synchronizer sequencer
* **5432** -- 到您的 PostgreSQL 数据库（如果是外部的）
* **443** -- 发送给您的 OIDC 提供商（如果使用身份验证）

测试连通性：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nc -zv sequencer.sync.global 443
nc -zv sequencer.test.sync.global 443
```

如果连接超时，请与您的网络团队合作打开所需的出口规则。对于 DevNet，您还需要通过 VPN 连接到 DevNet Sequencer。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
