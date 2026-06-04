---
title: "授权模型"
slug: "appdev-modules-m3-authorization"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-authorization.md"
source_title: "Authorization Model"
tags:
  - appdev
  - modules
  - m3-authorization
---

# 授权模型

> 理解 Daml 授权模型：signatory、observer 与 controller

## Party 与权限

Daml 面向互不信任多方参与的分布式应用。设计良好的合约模型下，各方有强保证：无人可作弊或绕过模板与 Choice 所定规则。

本节学习：

* 如何在合约间传递权限
* 如何编写高级 Choice
* 如何推理 Daml 授权模型

<Tip>
  可运行 `dpm new intro-parties --template daml-intro-parties` 将本节代码载入 `intro-parties` 目录。
</Tip>

## 防止 IOU 被撤销

仅由 `issuer` 签字的 `SimpleIou` 有问题：signatory 有权创建与**归档**合约。Alice 向 Bob 交付 IOU 换货后，可在收货后自行 `archive`，Bob 仅有链下追索记录：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template SimpleIou
  with issuer : Party; owner : Party; cash : Cash
  where signatory issuer
```

要让 Bob 有保证，要么自己是 signatory，要么信任某 signatory 不会以意外方式归档/重建合约。将 Bob 加为 signatory 可防 Alice 单方面删除：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Iou
  with issuer : Party; owner : Party; cash : Cash
  where
    signatory issuer, owner
    choice Transfer : ContractId Iou
      with newOwner : Party
      controller owner
      do
        assertMsg "newOwner cannot be equal to owner." (owner /= newOwner)
        create this with owner = newOwner
```

新问题：Alice 无法单方面向 Bob **签发**或**转让** IOU——`owner = bob` 的 IOU 需要 Bob 的权限才能上链。Alice 可先 `owner = alice` 签发，再转让；她不能未经 Bob 同意把其签名放在 IOU 上（对 Bob 反而是好事，避免负值等未经同意的 IOU）。

## 一次性授权：提议-接受

无长期关系时，Alice 可向 Bob **提议**签发 IOU，由 Bob 接受：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template IouProposal
  with iou : Iou
  where
    signatory iou.issuer
    observer iou.owner
    choice IouProposal_Accept : ContractId Iou
      controller iou.owner
      do create iou
```

`IouProposal` 携带 `issuer` 的权限；Bob exercise `Accept` 时加上自己的权限，故可创建双方均为 signatory 的 `Iou`。Choice 宜命名如 `IouProposal_Accept` 以保证唯一（每 Choice 对应一种 record 类型）。

**转让**同理，用 `IouTransferProposal`，含 `Accept`、`Reject`、`Cancel` 三选一模式，避免 `newOwner` 把开放提议当期权滥用。在 `Iou` 上由 `owner` 的 `ProposeTransfer` 创建转让提议而非直接 `Transfer`。

转让工作流也可用于**签发**（Alice 先 `owner = alice` 的 TransferProposal，Bob Accept）。

## 持续授权：角色合约

许多动作（资产发行、转让）可预先约定，用**关系/角色合约**表达。例如 `Mutual_Transfer` 需 `owner` 与 `newOwner` **共同** controller；`IouSender` 让 `sender` 经 `nonconsuming` 的 `Send_Iou` 多次向 `receiver` 发送正金额 IOU（`receiver` 为 signatory，`sender` 为 observer）。

## Daml 形式化授权模型

交易等价于交易树或动作森林。每个动作有 **required authorizers**（必须授权该动作的 Party）；每个交易有 **authorizers**（实际授权的 Party）。

**规则**：每个动作的 required authorizers 必须是父交易 authorizers 的子集。

**动作的 required authorizers：**

* **exercise**：对应 Choice 的 controllers（`Archive`/`archive` 为 signatories 作 controller 的隐式 Choice）
* **create**：合约的 signatories
* **fetch**（含 `fetchByKey`）：动态，后述

**交易的 authorizers：**

* 提交根交易的一方授权根交易
* exercise 的后果由该动作的 **actors** 加上被 exercise 合约的 **signatories** 授权

### 示例：Send_Iou

Bob 用 `IouSender` 向 Charlie 发送 IOU：Bob 提交根交易；exercise `Send_Iou` 需 controller `sender`（Bob）；后果由 Bob（actor）与 Charlie（`IouSender` signatory）授权；内层 `Mutual_Transfer` 需 Bob 与 Charlie（owner/newOwner），与父级一致；创建新 `Iou` 需 Alice 与 Charlie 为 signatory，是父后果 authorizers 的子集。IDE 交易视图可展示该图。

**权限不会自动传递**。例如 `NonTransitive` 中 Bob exercise `TryB` 调用 Alice 的 `TryA`，`TryA` 后果仅由 Alice 授权，缺少 Bob 创建翻转合约的权限，交易失败。

## 下一步

在 `compose` 中将综合运用所学构建类似 quickstart 的简单资产持有与交易模型，并进一步学习 `Update` 组合与账本隐私。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
