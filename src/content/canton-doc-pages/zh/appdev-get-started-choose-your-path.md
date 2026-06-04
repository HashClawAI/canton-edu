---
title: "选择你的学习路径"
slug: "appdev-get-started-choose-your-path"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/get-started/choose-your-path.md"
source_title: "Choose Your Path"
tags:
  - appdev
  - get-started
  - choose-your-path
---

# 选择你的学习路径

> 根据背景与目标找到合适的学习路径

无论你是区块链新手还是从其他平台迁移，本页帮助你在 Canton Network 上找到最高效的路径。

## 快速自测

**我是区块链开发新手 — 推荐路径：**

1. 五分钟概览 — 理解 Canton 是什么
2. 核心概念 — 掌握基础
3. 模块 1：理解 Canton — 建立心智模型
4. 模块 3：Daml 智能合约 — 开始写代码
5. 模块 4：构建应用 — 用示例应用动手

**我有以太坊 / Solidity 经验 — 推荐路径：**

1. 面向以太坊开发者的 Canton — 概念对照
2. 隐私模型 — 理解关键差异
3. 模块 3：Daml 智能合约 — 学习语法
4. 模块 4：构建应用 — 全栈实践

**需要内化的差异：**

* 合约不可变（归档 + 新建，而非原地修改）
* 显式授权（signatory/controller，而非 msg.sender）
* 默认隐私（声明 observer，而非事后隐藏）

**我有其他链经验（Solana、Cosmos 等）— 推荐路径：**

1. 五分钟概览
2. 面向以太坊开发者的 Canton（概念映射仍有用）
3. 架构概览
4. 模块 3：Daml 智能合约

**我想理解 Canton 但不写代码（架构/PM）— 推荐路径：**

1. 五分钟概览
2. Canton 要解决的问题
3. Canton 的解决方案
4. 用例
5. 架构概览

## 学习模块

开发者文档按模块递进：

| 模块 | 重点 | 前置 |
|------|------|------|
| **模块 1** | 理解 Canton | 无 |
| **模块 2** | 面向以太坊开发者 | 有区块链经验 |
| **模块 3** | Daml 智能合约 | 模块 1 或 2 |
| **模块 4** | 构建应用 | 模块 3 |
| **模块 5** | 测试与部署 | 模块 4 |
| **模块 6** | 智能合约升级 | 模块 3–5 |
| **模块 7** | 生产最佳实践 | 模块 5 |

## 开发栈概览

典型组件：前端、后端、Daml 智能合约；基础设施含验证者节点、PQS（SQL 查询）、同步器（Synchronizer）。后端连接验证者与 PQS，合约部署到验证者。

## 前置条件

**必需：** 任意语言编程经验、命令行、Git。

**有帮助：** 函数式编程概念、Docker、PostgreSQL（PQS）。

**环境：** 安装 Daml SDK 与 VS Code Daml 扩展。

## 动手实践

准备好构建？从模块 4「构建应用」开始，端到端完成全栈 Canton 应用（含 JSON Ledger API 与可观测性）。

## 获取帮助

可通过社区 Slack、Canton 论坛与 FAQ 获取支持。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
