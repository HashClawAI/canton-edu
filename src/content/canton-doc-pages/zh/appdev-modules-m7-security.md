---
title: "安全最佳实践"
slug: "appdev-modules-m7-security"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-security.md"
source_title: "Security Best Practices"
tags:
  - appdev
  - modules
  - m7-security
---

# 安全最佳实践

> Canton 应用的授权模式、API 认证、密钥管理与安全配置

Canton 在协议层提供结构性安全保证——授权在 Daml 中声明，隐私由 synchronizer 强制执行，账本保证不可抵赖。应用开发者的任务是在链下层次不引入缺口地构建于此之上。

## 链上安全

### Signatory 与 controller 声明

Daml 授权模型是第一道防线。每个模板声明 signatory（谁须授权创建），每个 choice 声明 controller（谁可行使）。协议强制执行——API 操纵无法绕过。

设计原则：

* 为每个模板声明最少 signatory 集合
* 用 `observer` 控制谁可见合约而不赋予操作权
* 多方协议优先 propose-accept，避免一方单方面为他人创建义务
* 在创建时及每次 fetch/exercise 运行的 `ensure` 中验证业务逻辑

### 授权链

复杂工作流用委托模式而非宽泛权限。Party 可通过独立授权合约委托特定操作：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuthorizedAgent
  with
    principal : Party
    agent : Party
    scope : Text
  where
    signatory principal
    observer agent

    choice ActOnBehalf : ()
      controller agent
      do assertMsg "Action not in scope"
           (scope == "transfer")
         pure ()
```

授权显式且可审计。principal 可通过归档 `AuthorizedAgent` 撤销委托。

## Ledger API 认证

Canton validator 用基于 token 的认证（JWT）保护 Ledger API。应用须获取有效 token 并在每次 API 调用中携带。

### 后端 token 管理

* 安全存储 token——勿放在客户端代码、会出现在日志的环境变量或版本库中
* 在过期前刷新 token，避免命令失败
* 为不同组件（后端、自动化、管理工具）使用独立服务账号，限制 token 泄露影响面
* gRPC 客户端用 call credentials 配置 token；HTTP/JSON 在 participant 集成 JSON API 上使用 `Authorization: Bearer <token>` 头

### TLS 配置

生产部署须对所有 Ledger API 连接使用 TLS。用 validator CA 证书配置 gRPC 客户端：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
ManagedChannel channel = NettyChannelBuilder
    .forAddress(host, port)
    .sslContext(GrpcSslContexts.forClient()
        .trustManager(new File("ca-cert.pem"))
        .build())
    .build();
```

LocalNet 开发默认禁用 TLS。勿将此类配置带入生产。

## 密钥管理

Canton 使用加密密钥标识 party、节点身份并签署交易。按敏感度保护密钥。

### 开发 vs 生产

LocalNet 上密钥本地生成存储，适合开发。生产中：

* 对私钥使用 [HSM 或云 KMS](/global-synchronizer/production-operations/kms-operations)
* 勿将生产密钥放在开发机或 CI
* 按组织安全策略轮换密钥
* 安全备份密钥材料——丢失密钥意味着失去 party 身份访问

### Validator 密钥保护

若运营自有 validator，其签名密钥是最关键机密。拥有这些密钥者可代表你的 party 提交交易。须存放在 HSM/KMS 并限制仅 validator 运行时环境可访问。

## 安全配置

### 密钥管理

* 用密钥管理器（Vault、AWS Secrets Manager、GCP Secret Manager）存数据库凭据、API 密钥与 auth token
* 勿通过可能出现在进程列表或容器检查中的环境变量传递密钥
* 定期轮换凭据并确保应用可无停机应对轮换

### 网络隔离

* 将 validator 置于私有网段
* 仅向应用服务器暴露 Ledger API 端口
* 用防火墙或安全组限制可访问 validator Admin API 的系统
* Admin API 提供特权操作（party 管理、包上传），不应暴露给应用代码

### 系统边界输入验证

数据到达 Ledger API 前验证所有用户输入。Daml 类型与授权可防多类攻击，后端仍应：

* 验证请求中的 party 标识与已认证用户一致
* 纳入合约载荷前清理文本字段
* 限制请求载荷大小
* 对 API 端点限流防滥用

## 下一步

* [Package Management](/appdev/modules/m7-package-management) — 保护 DAR 分发与部署
* [Performance](/appdev/modules/m7-performance) — Canton 应用优化

## 高级主题

* [Open Tracing in Ledger API Client Applications](/appdev/deep-dives/open-tracing) — 为使用 Ledger API 的应用添加基于 OpenTelemetry 的分布式追踪。
* [Authorization](/appdev/deep-dives/authorization) — Ledger API 的访问 token、身份提供方、scope 与 rights。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
