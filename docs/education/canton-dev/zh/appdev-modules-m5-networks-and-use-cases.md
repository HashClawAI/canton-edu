---
title: "SV 运营网络与用例"
slug: "appdev-modules-m5-networks-and-use-cases"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-networks-and-use-cases.md"
source_title: "SV Operated Networks and Use-cases"
tags:
  - appdev
  - modules
  - m5-networks-and-use-cases
---

# SV 运营网络与用例

> DevNet、TestNet、MainNet 的用途及面向应用开发者的测试指南

超级验证者运营三个网络：

1. DevNet
2. TestNet
3. MainNet

## DevNet

该网络作为 TestNet 的预演场，配置便于探索：自 featured 应用、CC tapping、validator 自助入网。SV 以高可用承诺、尽力而为方式管理 DevNet，及时验证升级，并用于负载测试；约每三个月定期重置，避免达到无法代表 MainNet 的可扩展性瓶颈。特殊情况下若问题修复成本过高，SV 可能进行计划外重置。

DevNet 让应用运营商测试需要全新 validator 节点的入网工作流。

<Note>
  请公平使用网络，避免过量负载。只要运维开销可控，网络预期保持开放。
</Note>

## TestNet

TestNet 是 SV、Validator 与应用运营商的预生产环境，用于在部署到 MainNet 前测试即将发布的 SV 与 Validator 节点软件升级。该环境与 MainNet 配置完全一致。应用运营商在 TestNet 维护应用长期测试实例，主要作用：

在保障应用代码数据连续性的前提下测试升级；让其他应用运营商测试与其应用的集成。

<Note>
  应用运营商应通过活跃度奖励、featured app 奖励及友好 SV 协作获得覆盖 traffic 费用所需的 TestNet-CC。
</Note>

## MainNet

该网络是 SV、Validator 与应用运营商的生产环境，用于将应用部署到网络。

## 测试指南

我们建议应用运营商按以下方式测试应用：

1. **用 Daml Script 做单元测试：** 先用 Daml Script 充分测试 Daml 代码，覆盖应用内全部工作流及依赖，验证逻辑与数据模型正确性。
2. **在 CI 中做集成测试：** 在持续集成流水线中实现集成测试，使用 mock 依赖，针对连接独立 Canton synchronizer（domain）的独立 Canton participant 运行，确保组件在受控环境中正确协作。
3. **TestNet 部署：** 在 TestNet 部署应用测试实例，并与支持以下关键用例的其他应用测试实例集成：
   1. 基础设施升级
   2. 应用版本升级
   3. 消费依赖方的应用升级

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
