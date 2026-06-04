---
title: "Ledger API 错误"
slug: "appdev-troubleshooting-guide-ledger-api-errors"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/ledger-api-errors.md"
source_title: "Ledger API Errors"
tags:
  - appdev
  - troubleshooting-guide
  - ledger-api-errors
---

# Ledger API 错误

> 提交命令时常见的 Ledger API 错误码、原因与解决办法。

# Ledger API 错误

这些 gRPC 状态码来自 Ledger API 层。

### AUTH_INVALID_TOKEN

```
UNAUTHENTICATED: Could not verify JWT token
```

**原因：** Bearer 令牌缺失、格式错误、已过期，或由未识别的密钥签名。

**修复：**

* 确认令牌未过期（检查 `exp` 声明）
* 确认令牌受众与 `LEDGER_API_AUTH_AUDIENCE` 一致
* 确保令牌包含 `daml_ledger_api` 作用域
* 检查验证者上配置的 JWKS URL 可访问且返回正确的签名密钥

### PACKAGE_NOT_FOUND

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <package-id>
```

**原因：** 验证者未安装包含所引用包的 DAR，或该包尚未通过 vetting。

**修复：** 上传 DAR：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
curl -X POST http://localhost:5002/v2/packages -F "dar=@.build/your-package.dar"
```

上传后，在重试命令前确认该包已出现在包列表中。

### PARTY_NOT_KNOWN

```
NOT_FOUND: PARTY_NOT_KNOWN - Party not known on participant
```

**原因：** 命令中的 party 标识与本验证者上已分配的 party 不匹配。

**修复：** 先分配 party，或确认使用了正确的 party 标识。Party ID 区分大小写并包含指纹后缀（例如 `Alice::1220abcd...`）。列出已知 party：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost:5002/v2/parties | jq '.party_details[].party'
```

### PERMISSION_DENIED

```
PERMISSION_DENIED: An error occurred. Please contact the operator.
```

**原因：** 已认证用户无权以所请求的 party 身份操作。

**修复：** 通过 Admin API 授予用户对该 party 的读写权限：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST http://localhost:5002/v2/users/<user-id>/rights \
  -H "Content-Type: application/json" \
  -d '{"rights": [{"can_act_as": {"party": "<party-id>"}}]}'
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
