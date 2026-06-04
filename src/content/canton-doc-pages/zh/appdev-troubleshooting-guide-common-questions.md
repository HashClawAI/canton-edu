---
title: "常见问题"
slug: "appdev-troubleshooting-guide-common-questions"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/common-questions.md"
source_title: "Common Questions"
tags:
  - appdev
  - troubleshooting-guide
  - common-questions
---

# 常见问题

> Canton Network 应用开发常见问题与解答。

解答 Canton Network 应用程序开发中经常出现的问题。有关验证器操作问题，请参阅[常见问题常见问题解答](/appdev/faq)。

## 开始使用

### 我应该使用什么版本的 SDK？

使用最新稳定的Daml SDK（3.x系列）。 2.x Daml SDK 为历史开发，不支持 Canton Network 功能，如全局同步器或 Canton Coin。

检查 [cn-quickstart 存储库](https://github.com/digital-asset/cn-quickstart) 中当前推荐的版本，该版本始终在其配置中固定兼容的 SDK 版本。

### 我可以使用 JavaScript、Python 或 Go 吗？

Daml 模型必须用 Daml 语言编写。但是，您的应用程序的后端和前端可以使用任何支持 gRPC 或 HTTP 的语言。

* **Java 和 Scala** 具有官方语言绑定和来自 Daml 包的代码生成
* **JavaScript/TypeScript** 可以使用 JSON API (HTTP) 或 gRPC 客户端库。 cn-quickstart 包含一个 TypeScript 前端作为参考
* **Python 和 Go** 可以使用从 Ledger API `.proto` 文件生成的 gRPC 客户端库

还有一些语言的社区维护的绑定。请参阅[语言绑定](/sdks-tools/language-bindings/community)页面。

### 在哪里可以找到示例代码？

[cn-quickstart](https://github.com/digital-asset/cn-quickstart) 存储库是主要参考应用程序。它包括：

* 完整的 Daml 模型，具有 SCU 兼容升级
* TypeScript 前端
* 使用 Daml 脚本实现后端自动化
* LocalNet 的 Docker Compose 配置
* CI/CD 模式

克隆存储库并按照自述文件获取本地运行的工作应用程序。

## 开发

### 如何在本地测试多方工作流程？

沙箱和 LocalNet 都支持多方。您可以在同一本地环境中以不同身份分配参与方并提交命令。

使用 `dpm sandbox`，在 Daml 脚本中分配各方：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
alice <- allocateParty "Alice"
bob <- allocateParty "Bob"
```

使用 LocalNet（通过 cn-quickstart），各方已在 Docker Compose 设置中预先配置。您可以通过修改引导脚本来添加更多内容。

对于跨多个验证器的测试工作流程，请使用 LocalNet 而不是单节点沙箱。 LocalNet 运行单独的验证器进程，通过本地同步器进行通信，从而更好地模拟真实的网络拓扑。

### 我如何处理合同争用？

当多笔交易同时针对同一合同时，Canton 会拒绝除一笔以外的所有交易。您的应用程序应该实现具有指数退避的重试逻辑：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
async function submitWithRetry(command: Command, maxRetries = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await ledgerClient.submit(command);
    } catch (error) {
      if (error.code === "ABORTED" && attempt < maxRetries - 1) {
        await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 100));
        continue;
      }
      throw error;
    }
  }
}
```

对于高竞争场景，请考虑重新设计 Daml 模型，将经常竞争的合约拆分为独立的分片。

### 沙箱和 LocalNet 有什么区别？**Sandbox** 是一个轻量级、单进程的 Daml 账本。使用`dpm sandbox`运行它。它启动速度快，适合对 Daml 模型和脚本进行单元测试，但它不运行完整的 Canton 协议栈。

**LocalNet** 是一个多容器环境，运行实际的 Canton 验证器、同步器和支持服务（JSON API、PQS、钱包）。它是通过 cn-quickstart 使用 `make start` 启动的，并且密切反映了真实的网络部署。

使用沙箱对 Daml 代码进行快速迭代。当您需要测试网络级行为（例如跨验证器的多方交易、流量消耗或钱包交互）时，请使用 LocalNet。

## 部署

### 如何从 LocalNet 迁移到 DevNet？

1. 使用 `dpm build` 构建您的 DAR
2. 向超级验证者赞助商请求 DevNet 访问权限（需要 2-4 周的批准时间）
3. 一旦您拥有 VPN 凭据并且您的 IP 被列入白名单，请将您的 DAR 上传到 DevNet 验证器
4. 更新应用程序的连接设置以指向 DevNet Ledger API 端点而不是 localhost
5. 使用DevNet水龙头（Tap）获取流量测试Canton Coin

您的 Daml 代码不会在环境之间发生变化。仅连接配置和身份验证设置不同。

### 如何将 DAR 上传到远程验证器？

使用验证器的管理 API 或 Canton 控制台。

**通过管理API：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://your-validator:5002/v2/packages" \
  -H "Authorization: Bearer $TOKEN" \
  -F "dar=@.build/your-package.dar"
```

**通过Canton Console：**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res1: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

上传后，验证包是否可见：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl "https://your-validator:5002/v2/packages" \
  -H "Authorization: Bearer $TOKEN" | jq '.package_ids | length'
```

### 如何让我的应用程序在 Canton Network 上得到推荐？

申请者可以通过坎顿改进提案（CIP）流程申请特色地位。首先查看 [CIP 简介](/overview/understand/cips-introduction) 和 [让您的应用成为特色](/overview/understand/getting-app-featured) 指南。

该过程包括提交一份提案，描述您的应用程序、其对网络的价值以及它如何使用 Canton Network 基础设施。特色应用程序可以在 canton.network 上获得曝光，并可能获得 Global Synchronizer Foundation 的支持。

## 建模问题

### 与另一方签订协议模型

要签订协议，请从具有明确 `signatory` 声明的模板创建合同。

您需要使用一系列合同，让各方都有机会通过合同选择表示同意。

由于 Daml 强制执行的规则，单方不可能创建多方协议的实例。这是因为这样的创造将迫使其他各方签署该协议，而不给他们选择是否签署该协议的权利。

### 模特权利

使用合同选择来模拟权利。一方通过行使选择权来行使该权利。

### 合同无效要允许撤销合同，请提供不创建任何新合同的选项。当做出消费选择时，Daml 合约会被存档（但不会删除） - 因此，执行该选择实际上会使合约失效。

但是，您应该记住谁可以撤销合同，尤其是在没有重新征求其他签署方同意的情况下。

### 代表账外各方

如果您无法将所有参与方设置为账本参与者，则需要执行此操作，因为 Daml `Party` 类型与加密密钥关联，因此只能与已相应设置的参与方一起使用。

要在 Daml 中对账外各方进行建模，他们必须由可以代表他们签名的参与者在账本上代表。您可以用普通的 `Text` 参数来表示它们。

这不是很私密，因此您可以使用数字 ID/accountId 来识别账外客户端。

### 按时间限制选择

有些权利有时间限制：要么是必须行使的时间，要么是不能行使的时间。

您可以使用`getTime`获取当前时间，并将您想要的时间与它进行比较。如果不满足您的时间条件，请使用`assert`中止选择。

### 模拟强制行动

如果您想确保一方在给定时间段内采取某些行动。如果他们不这样做，可能会受到处罚——因为这会违反合同。

例如：必须在特定日期之前支付的发票，并附带罚金（可能是附加利息费用或罚金）。为此，您可以选择有时间限制的惩罚选项，该选项只能在期限到期*之后*才可以执行。

但请注意，惩罚行动只能在账本上创建另一份合同，这代表各方就违反初始合同达成一致。最终，任何违规行为的追索权都是某种法律行动。 Daml 提供的内容可证明违反了协议。

### 使用可选

标准库中的 `Optional` 类型，表示某个值是可选的，即在某些情况下该值可能会丢失。

在函数式语言中，`Optional` 是一种比使用更熟悉的值“NULL”更好的指示缺失值的方法，“NULL”存在于命令式语言（如 Java）中。

要使用`Optional`，请包含标准库中的`Optional.daml`：

然后，您可以像这样创建 `Optional` 值：

您可以通过多种方式测试是否存在：

如果需要提取值，请使用`optional`函数。

它返回一个已定义类型的值，并采用一个 `Optional` 值和一个函数，该函数可以将 `Optional` 的 `Some` 值中包含的值转换为该类型。如果缺少，`optional`也会采用返回类型的值（默认值），如果`Optional`值为`None`，则会返回该值

如果 `optionalValue` 是 `Some 5`，则 `t` 的值为 `"The number is 5"`。如果是`None`，`t`就是`"No number"`。请注意，使用`optional`，可以返回与`Optional`值中包含的类型不同的类型。这使得`Optional`类型非常灵活。

“Optional.daml”中还有许多其他函数，可让您对包含 `Optional` 值的结构执行熟悉的函数操作，例如对 `Lists` 或 `Optional` 值进行`map`、`filter` 等。

## 测试

### 测试合同对一方是否可见使用`queryContractId`：它的第一个参数是一方，第二个参数是`ContractId`。如果`ContractId`对应的合约存在并且对该方可见，则结果将被包装在`Some`中，否则结果将是`None`。

使用 `submit` 块和 `fetch` 操作。 `submit` 块测试合约（作为`ContractId`）对该方可见，`fetch` 测试它是否有效，即合约确实存在。

例如，如果我们想测试“Alice”可见的`Invoice`的存在性和可见性，其ContractId绑定到`invoiceCid`，我们可以说：

请注意，我们在 `Some` 构造函数上进行模式匹配。如果合约不存在或对“Alice”不可见，则测试将失败并出现模式匹配错误。

现在合约已绑定到一个变量，我们可以检查它是否有一些期望值：

### 测试是否无法提交更新操作

使用`submitMustFail`功能。这在形式上与`submit`函数类似，但断言如果某些方尝试更新将会失败。

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
