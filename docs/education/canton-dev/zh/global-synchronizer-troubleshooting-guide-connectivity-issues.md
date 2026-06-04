---
title: "连接问题"
slug: "global-synchronizer-troubleshooting-guide-connectivity-issues"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/connectivity-issues.md"
source_title: "Connectivity Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - connectivity-issues
---

# 连接问题

> synchronizer连接、TLS 与 VPN 连通性故障排查。

> 诊断和解决synchronizer连接故障、TLS 错误和 VPN 问题

连接故障会阻止验证者与synchronizer通信。症状各不相同——从彻底的连接拒绝到微妙的 TLS 握手错误——但诊断方法是一致的。

## 无法连接到synchronizer

如果您的验证者日志显示：

```
Request failed for sequencer. Is the server running?
```

或

```
SEQUENCER_SUBSCRIPTION_LOST: Lost subscription to sequencer
```

按顺序完成这些检查。

### 1. 验证Sequencer URL

确认您的配置指向目标网络的正确Sequencer端点：

* **开发网：** `https://sequencer.dev.sync.global`
* **测试网：** `https://sequencer.test.sync.global`
* **主网：** `https://sequencer.sync.global`

一个常见的错误是在入职期间使用扫描 URL (`https://scan.sv-2...`) 而不是 SV 赞助商 URL。扫描 URL 用于只读网络数据，不适用于验证者注册。

### 2. 测试网络可达性

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# DNS resolution
dig +short sequencer.sync.global

# TCP connectivity
nc -zv sequencer.sync.global 443

# Full TLS handshake
openssl s_client -connect sequencer.sync.global:443 -servername sequencer.sync.global </dev/null
```

如果 `nc` 超时，则说明防火墙或安全组正在阻止端口 443 上的出站。

### 3.检查防火墙和安全组

您的验证者需要端口 443 上的出站 HTTPS 到synchronizer。如果您在云环境中运行，请验证：

* 附加到您的实例或 Pod 的安全组允许出站 TCP/443。
* 没有网络 ACL 阻止流量。
* 如果您使用 HTTP 代理，Canton 支持通过 JVM 系统属性（`-Dhttps.proxyHost`、`-Dhttps.proxyPort`）进行代理配置。

## TLS 握手失败

TLS 错误通常会生成如下日志消息：

```
io.grpc.StatusRuntimeException: UNAVAILABLE: io exception
Channel Pipeline: [SslHandler#0, ...]
Caused by: javax.net.ssl.SSLHandshakeException: PKIX path building failed
```

### 证书到期

检查服务器证书是否过期：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect sequencer.sync.global:443 -servername sequencer.sync.global 2>/dev/null \
  | openssl x509 -noout -dates
```

如果证书已过期并且您可以控制它（例如，用于您自己的验证者的 TLS 终止），请续订该证书并重新启动 TLS 终止代理或入口控制器。

### CA信任链

如果您看到`PKIX path building failed`，则验证者的 JVM 不信任服务器的证书颁发机构。可能的修复：

* 将CA证书导入到JVM信任库中：

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  keytool -importcert -alias myca -file ca-cert.pem \
    -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit
  ```

* 对于 Kubernetes，将 CA 捆绑包挂载为卷并设置 `JAVA_OPTS`：

  ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  env:
    - name: JAVA_OPTS
      value: "-Djavax.net.ssl.trustStore=/etc/ssl/truststore.jks"
  ```

### 主机名不匹配

如果证书的使用者备用名称 (SAN) 不包含您要连接的主机名，则握手将失败。验证：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect sequencer.sync.global:443 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```

## VPN 问题

DevNet 需要 VPN 连接。测试网和主网验证者通过公共互联网连接，但仍可能使用 VPN 作为内部基础设施。

### VPN 连接断开

如果您的验证者定期失去连接，请检查：

* VPN 客户端重新连接事件日志
* VPN是否分配稳定的IP（某些提供商在重新连接时轮换IP，这可能会破坏IP白名单访问）

### MTU 问题

VPN 隧道会降低有效 MTU。如果您看到适用于小请求但挂在较大负载上的停滞连接：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Test with reduced packet size
ping -M do -s 1400 sequencer.dev.sync.global
```

如果 ping 在 1400 字节处成功，但在 1500 字节处失败，请降低 VPN 接口上的 MTU：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo ip link set dev tun0 mtu 1400
```

### 分割隧道配置如果您的 VPN 通过隧道路由所有流量，验证者可能无法访问外部服务（OIDC 提供商、容器注册表）。配置分割隧道路由，以便只有synchronizer流量通过 VPN，而其他流量则使用默认网关。

请参阅 VPN 提供商的文档以了解分割隧道设置。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
