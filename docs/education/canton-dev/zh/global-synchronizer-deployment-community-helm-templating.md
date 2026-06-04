---
title: "社区 Helm 模板工具"
slug: "global-synchronizer-deployment-community-helm-templating"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/community-helm-templating.md"
source_title: "Automated Helm/Kubernetes Templating Tool (Community)"
tags:
  - global-synchronizer
  - deployment
  - community-helm-templating
---

# 社区 Helm 模板工具

> 社区 Helm values 自动化模板工具说明。

> 社区贡献的用于模板化 Helm 和 Kubernetes 部署的工具

<Warning>
  This section features solutions shared by community members. While they haven’t been formally tested by the Splice maintainers, users are encouraged to verify the information independently. Contributions to enhance accuracy and completeness are always welcome.
</Warning>

使用 Kubernetes、Helm 和 Git 管理验证器和超级验证器节点的部署可能具有挑战性，尤其是在使多个环境（DevNet、TestNet、MainNet）与不断变化的配置文件和值保持同步时。频繁的版本更新、新变量和硬迁移通常需要对大量 `values-*.yml` 文件进行手动且容易出错的更新。此手动过程可能会导致不一致、错过配置更改并增加运营开销。引入的解决方案提供了一个模板工具，旨在自动化和简化 Helm 值和特定于环境的配置的管理。该工具旨在为寻求额外自动化和模板灵活性以及官方部署指南的用户提供补充资源。如需了解官方支持的基于 Kubernetes 的部署的更多信息，请参阅基于 Kubernetes 的 Validator 节点部署和基于 Kubernetes 的超级 Validator 节点部署。

感谢 Stéphane Loeuillet 在社区讨论中分享此解决方案。有关更多详细信息和未来更新，请参阅 [kaikodata/canton-tooling](https://github.com/kaikodata/canton-tooling/blob/master/kubernetes/README.md#canton-templated-script) 存储库。

## 解决方案的主要特点

* 从源目录和环境变量文件自动模板化 YAML 配置，包括替换文件内容和文件名中的占位符，最大限度地减少手动编辑并降低错过更新的风险。
* 对 DevNet、TestNet 和 MainNet 的多环境支持，处理不同的图表版本、迁移 ID、OIDC 参数和其他环境特定值，以便跨网络无缝部署。
* 为因变量替换而重命名的目录创建符号链接，自动清理现有符号链接以防止嵌套并确保重复运行时的干净处理。
* 用于调试日志记录的 CLI 选项，用于字符串替换（包括支持包含 # 的变量）、别名前缀和基于 Chart.yaml 依赖项的 YAML 重新缩进，以及 .gitignore 管理（每个输出目录或存储库根目录）。
* 与 yamllint 等 CI 工具兼容的“合法”YAML 文件的一致输出。
* 提供 Shell 脚本，用于使用新版本批量更新所有 YAML 文件，从而简化升级并减少运营开销。
* 开放社区贡献和建议，重点是改进自动化和上游示例值文件，以使所有用户受益。
* 计划对机密和入口模板进行扩展，支持 Kubernetes 环境的高级部署场景和未来增强功能（截至 2025 年 5 月正在进行中）。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
