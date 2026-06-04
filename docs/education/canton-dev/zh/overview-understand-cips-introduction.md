---
title: "CIP 简介"
slug: "overview-understand-cips-introduction"
locale: "zh"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/cips-introduction.md"
source_title: "Canton Improvement Proposals (CIPs)"
tags:
  - overview
  - understand
  - cips-introduction
---

# CIP 简介

> 面向开发者的 Canton Improvement Proposal（CIP）入门。

> Canton Network 标准与治理的 CIP流程介绍

Canton 改进提案 (CIP) 是对 Canton Network 提出变更、标准和改进建议的正式机制。

## 什么是 CIP？

CIP 是向 Canton 社区提供信息的设计文档，描述 Canton 网络的新功能、流程或标准。

| CIP 类型 |目的|
| ------------------- | -------------------------------------- |
| **标准轨道** |技术规格和标准|
| **流程** |治理和运营程序|
| **信息** |一般准则和信息 |

## 为什么 CIP 很重要

CIP 确保：

* 实施前公开讨论变更
* 标准实现互操作性
* 社区对网络演进提出了意见
* 决定经过投票后记录以供参考

## 关键 CIP

### CIP-0056：Canton Network 令牌标准

代币标准定义了 Canton Network 上可互换代币的接口。

|方面|规格|
| -------------------- | ---------------------------- |
| **目的** |标准化代币运营 |
| **接口** |持有、转让、锁定 |
| **互操作性** |钱包和应用程序兼容性 |

**GitHub：** [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)

主要特点：

* 标准控股代表
* 一致的传输语义
* 对高级工作流程的预先批准支持
* 多步转移的分配模式

## CIP 流程

### 生命周期

|舞台|描述 |
| ------------ | ------------------------------------------- |
| **草稿** |供讨论的初步提案|
| **评论** |社区评论和反馈 |
| **已接受** |批准实施 |
| **决赛** |已实施且稳定 |
| **被拒绝** |不被接受（有理由）|

### 谁可以提议

CIP 可以通过以下方式提出：

* 超级验证者
* 社区成员
* 开发团队
* 生态系统参与者

## 实施 CIP

### 对于应用程序开发人员

构建应用程序时，请考虑相关的 CIP：

|情况|行动|
| ---------------------- | -------------------------------------- |
| **创建代币** |实施 CIP-0056 接口 |
| **钱包集成** |支持标准接口|
| **互操作性** |遵循公布的标准 |

### 示例：代币标准实施

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Implement CIP-0056 holding interface
template MyToken
  with
    issuer : Party
    holder : Party
    amount : Decimal
  where
    signatory issuer
    observer holder

    -- Standard interface implementation
    interface instance Holding.I for MyToken where
      view = Holding.View with ...
```

## 查找 CIP

|资源 |内容 |
| --------------------------------------------------------------------------- | ---------------------- |
| [GitHub 存储库](https://github.com/global-synchronizer-foundation/cips) |所有 CIP 文件 |
| [canton.foundation](https://canton.foundation) |治理资讯|
|社区频道|讨论和更新|

## 为 CIP 做出贡献

提议或为 CIP 做出贡献：

1. **查看现有 CIP** 以了解格式
2. **在社区渠道中进行非正式讨论**
3. **按照 CIP 模板写草稿**
4. **通过适当的流程提交审核**
5. **根据反馈进行迭代**

## 后续步骤

<CardGroup cols={2}>
  <Card title="Token Standard" icon="coins" href="https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md">
    实施Canton Token 标准。
  </Card>

  <Card title="CIP 存储库" icon="github" href="https://github.com/global-synchronizer-foundation/cips">
    浏览 GitHub 上的所有 CIP。
  </Card>
</CardGroup>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
