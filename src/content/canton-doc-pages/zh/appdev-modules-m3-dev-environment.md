---
title: "开发环境搭建"
slug: "appdev-modules-m3-dev-environment"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-dev-environment.md"
source_title: "Development Environment Setup"
tags:
  - appdev
  - modules
  - m3-dev-environment
---

# 开发环境搭建

> 为编写 Daml 智能合约配置开发环境

## 简介

Daml 是一种智能合约语言，用于在 Canton 账本上构建可组合应用。

在本模块中，你将了解 Daml 账本的结构，并通过构建资产持有与交易应用，学习如何在 Canton Network 上编写 Daml 应用。你将概览最重要的语言特性，以及如何使用 Daml 开发者工具来编写、测试、编译、打包并交付应用。

## 前置条件

* 已安装 [dpm](https://docs.canton.network/sdks-tools/cli-tools/dpm)

## 加载示例代码

本模块各节会呈现一个比上一节功能更完整、可独立运行的应用。你可以用 `dpm` 加载各节代码，例如：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 加载合约模板示例
dpm new intro-contracts --template daml-intro-contracts

# 加载 choice 示例
dpm new intro-choices --template daml-intro-choices
```

## 下一步

继续阅读 [合约模板](/zh/docs/canton/appdev-modules-m3-contract-templates)，开始编写 Daml 智能合约。

若你刚接触函数式编程，或想复习 Daml 语法（类型、模式匹配、记录、类型类），请先阅读 [语言基础](/zh/docs/canton/appdev-modules-m3-language-fundamentals)。若你熟悉 Haskell 或其他 ML 系语言，可跳过该节，需要时再查阅。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
