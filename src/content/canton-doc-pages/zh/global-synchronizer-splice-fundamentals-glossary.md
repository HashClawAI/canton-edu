---
title: "术语表"
slug: "global-synchronizer-splice-fundamentals-glossary"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/splice-fundamentals/glossary.md"
source_title: "Glossary"
tags:
  - global-synchronizer
  - splice-fundamentals
  - glossary
---

# 术语表

> Canton Network、Splice 与 CNS 术语表。

> Canton网络、熔接和 CNS 术语表

<div className="词汇表">
  ACS

  > `Active Contract Set`

  有效合约集

  > 根据给定参与者的视图，当前在分类账上处于活动状态的合约集。

  Amulet

  > 实现Canton币的代码和逻辑的通用名称。

  Amulet名称服务

  > 实现 Canton 名称服务的代码和逻辑的通用名称。

  抄送

  > `Canton Coin`

  中国

  > `Canton Network`

  Canton网

  > 由业务实体以 CN 应用程序形式运行的多方业务流程网络。

  中国申请

  > 由单个业务实体操作的一组 Canton 参与者和域节点以及支持代码，目的是为 Canton 网络上的其他实体提供对特定多方业务流程的访问。

  拜耳费托

  > 拜占庭容错。分布式系统的一个属性，允许其在存在一定数量的故障节点的情况下继续正常运行。通常`f`表示系统可以容忍的故障节点数量。在 Splice 的所有层中，`f` 相当于略小于 SV 总数的 1/3（准确地说是`floor((n-1)/3)`）。

  CN全球同步器

  > * 全局同步域
  > * 可以直接在域上托管小型应用程序
  > * 充当共享同步域，在不同应用程序的域之间进行中介
  > * 由超级验证者集体与 BFT 运行
  > * 域名使用费用`同步器 fees` 由每个验证人的运营者以 Canton Coin 支付

  Canton币

  > * 由验证者、应用程序提供商和超级验证者铸造的实用代币，作为在全局同步器上完成的活动的奖励
  > * 用于`同步器 fees`
  > * 代币会产生持有费用，用于支付代币使用超级验证者存储空间的费用
  > * 所有 CC 交易都是公开的
  > * 支持锁定币，可由锁持有者解锁
  > * 支持单发送方转账、多接收方转账
  > * 转账会产生管理费，并为接收者产生应用程序奖励，并为托管发送者的验证者产生验证者奖励
  > * 转账与挖矿轮次相关
  > * 奖励可在下一轮挖矿中领取

  CN验证者

  > * CN中的一个节点
  > * 由州参与者、验证者应用程序、钱包应用程序组成
  > * 验证者应用程序用于验证者操作员的管理操作，例如用户/团体管理

  CN超级验证者

  > * CN中的一个节点
  > * 除 CN 验证者 组件外，还包含 Canton Sequencer、Canton Mediator、sv App 和 Scan App
  > * sv 应用程序用于 `CN 全局同步器` 的管理操作
  > * 扫描应用程序以提供公开可见的数据

  中国钱包

  > * 为其他应用程序提供支付 API（“使用 CC 支付”）和相应的 UI，例如批准支付
  > * CN 用户用来管理他们的 CC 持有量和奖励领取
  > * 提供用于管理两个用户之间的点对点传输的 UI

  坎顿名称服务（有时也称为目录服务）

  > * 允许各方在映射到其一方的时间段内购买全球唯一的、人类可读的名称（类似于 DNS）
  > * 允许每一方将其条目之一声明为主要条目，用于向其一方提供人类可读的名称（类似于反向 DNS）
  > * 提供用于双向解析的 API，其他应用程序（例如钱包）可以使用这些 API 来显示和接受 CNS 名称而不是参与方 ID

  全球同步器基金会

  * 基金会负责促进Canton网络中全球同步器的发展和成长，并促进其治理，请参阅[https://sync.global/](https://sync.global/)。

  谷胱甘肽

  > * `全局同步器 Foundation` 的缩写

  拼接

  > * HyperLedger 实验室项目的名称，该项目将托管 Amulet、DSO 治理、Amulet Name Service、SV 节点和验证者节点的代码。

  同步器费用

  > `流量`
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
