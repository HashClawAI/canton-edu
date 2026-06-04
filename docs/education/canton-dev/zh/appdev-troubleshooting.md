---
title: "故障排查速查表"
slug: "appdev-troubleshooting"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting.md"
source_title: "Troubleshooting Cheat Sheet"
tags:
  - appdev
  - troubleshooting
---

# 故障排查速查表

> Canton Network 应用开发详细故障排查指南索引。

有关详细的故障排除步骤，请参阅下面的主题指南。有关诊断和调试工具，请参阅[调试工具](/zh/docs/canton/appdev-tooling-debugging-tools)。

<CardGroup cols={2}>
  <Card title="安装问题" icon="wrench" href="/zh/docs/canton/appdev-troubleshooting-guide-installation-issues">
    Nix shell 失败、Docker 配置、内存分配与 JDK 设置。
  </Card>

  <Card title="开发问题" icon="bug" href="/zh/docs/canton/appdev-troubleshooting-guide-development-issues">
    Daml 编译错误、API 连接问题、开发期交易失败。
  </Card>

  <Card title="运维问题" icon="server" href="/zh/docs/canton/appdev-troubleshooting-guide-operational-issues">
    流量耗尽、升级问题、DevNet/TestNet/MainNet 上的 PQS 故障。
  </Card>

  <Card title="常见问题 FAQ" icon="circle-question" href="/zh/docs/canton/appdev-faq">
    应用开发与 validator 运维常见问题，含简短答案与后续步骤。
  </Card>

  <Card title="常见问题" icon="circle-question" href="/zh/docs/canton/appdev-troubleshooting-guide-common-questions">
    Canton Network 应用开发常见问题。
  </Card>

  <Card title="Daml 错误码" icon="circle-exclamation" href="/zh/docs/canton/appdev-troubleshooting-guide-error-code-reference">
    Daml 编译错误与 Canton 运行时错误码，含原因与解决方案。
  </Card>

  <Card title="Ledger API 错误" icon="circle-exclamation" href="/zh/docs/canton/appdev-troubleshooting-guide-ledger-api-errors">
    命令提交时常见的 Ledger API 错误码。
  </Card>
</CardGroup>

## 诊断工具

有关故障排除时使用的日志捕获、lnav 工作流程、Canton Console 诊断和 PQS 查询示例，请参阅[调试工具](/zh/docs/canton/appdev-tooling-debugging-tools)。

## 获取帮助

如果上述主题指南无法解决您的问题：

* **自助服务**：搜索此故障排除指南和[调试工具](/zh/docs/canton/appdev-tooling-debugging-tools) 页面。
* **社区**：在 `#gsf-global-synchronizer-appdev` (Slack) 或 [forum.canton.network](https://forum.canton.network/) 中发布您的错误消息、经过编辑的日志和环境详细信息（验证器 ID、网络、SDK/Splice 版本）。
* **电子邮件支持**：`da-support@digitalasset.com` 提供尽最大努力的酌情支持。
* **通过 SLA 提供付费支持**：`support@digitalasset.com`（打开跟踪的 Jira 票证）。

寻求帮助时，请包括：

* 您的验证者 ID 和网络（DevNet、TestNet 或 MainNet）
* 您正在运行的 Splice / SDK 版本
* 相关日志摘录（编辑私钥、密码和 JWT 令牌；保留错误代码、相关 ID 和时间戳）
* 问题开始的时间以及最近的任何更改的时间表

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
