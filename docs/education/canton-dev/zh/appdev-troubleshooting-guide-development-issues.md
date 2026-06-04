---
title: "开发问题"
slug: "appdev-troubleshooting-guide-development-issues"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/development-issues.md"
source_title: "Development Issues"
tags:
  - appdev
  - troubleshooting-guide
  - development-issues
---

# 开发问题

> 排查 Daml 编译错误、API 连接问题与开发期交易失败。

本页解决了您在本地开发期间编写 Daml 代码、连接到 API 以及提交事务时可能遇到的问题。

## Daml 编译错误

### 常见类型不匹配

Daml 编译器强制执行严格类型化。一个常见的错误是在需要模板类型的地方传递 `ContractId`，反之亦然。

```
error:
  Couldn't match expected type 'Asset' with actual type 'ContractId Asset'
```

**修复：** 使用 `fetch` 从 `ContractId` 检索合约有效负载：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asset <- fetch assetCid
```

另一种常见的变体是将 `Party` 与 `Text` 混淆：

```
Couldn't match expected type 'Party' with actual type 'Text'
```

在 Daml 脚本中使用 `getParty` 或直接传递 `Party` 值而不是字符串。

### 缺少导入

如果编译器报告未知类型或函数，您可能需要导入。 Daml 不会自动导入模块。

```
error: Not in scope: 'DA.Optional.fromSome'
```

**修复：**

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import DA.Optional (fromSome)
```

### SCU 兼容性检查失败

升级 Daml 软件包时，智能合约升级 (SCU) 兼容性检查程序可能会拒绝更改。常见的违规行为包括从模板中删除字段或更改字段的类型。

```
error: Upgrade check failed: field 'amount' has changed type from 'Int' to 'Decimal'
```

SCU 要求新的软件包版本与以前的版本保持线路兼容。您可以添加可选字段（使用默认值），但不能删除或更改现有字段。

<Warning>
  Daml exceptions are deprecated. If you see compiler warnings about exception usage, refactor to use `Either` or other error-handling patterns instead.
</Warning>

## API 连接问题

### 端口错误

每个 Canton 组件都侦听不同的端口。如果您的应用程序获得 `Connection refused`，请验证您的目标是正确的：

* **账本 API (gRPC)** -- 5001
* **JSON API** -- 7575
* **管理API** -- 5002
* **参与者健康** -- 5003

检查哪些端口实际在使用：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

### 身份验证令牌问题

如果 Ledger API 返回 `UNAUTHENTICATED`，您的令牌可能已过期、受众群体错误或缺乏所需范围。

```
UNAUTHENTICATED: Could not verify JWT token: token is expired
```

**清单：**

* 代币具有`daml_ledger_api`范围
* 令牌受众与您的配置中的`LEDGER_API_AUTH_AUDIENCE`匹配
* 令牌尚未过期（检查`exp`声明）

解码您的令牌以检查声明：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
echo "$TOKEN" | cut -d'.' -f2 | base64 -d 2>/dev/null | jq .
```

### 沙箱尚未准备好

运行`dpm sandbox`后，沙箱需要几秒钟的时间来初始化。如果您的应用程序立即连接，它可能会失败并显示：

```
UNAVAILABLE: io exception - Connection refused
```

发送请求之前等待沙箱运行状况端点响应：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
until curl -s http://localhost:5003/health | grep -q "SERVING"; do
  sleep 1
done
```

## 开发中的事务失败

### 授权错误最常见的交易拒绝是授权失败。当提交方未被授权为签字人或控制人时，Canton 会拒绝交易。

```
INVALID_ARGUMENT: Interpretation error:
  ... requires authorizers Party('Alice'), but only Party('Bob') were given
```

**修复：** 确保提交命令的一方被列为相关选择的`signatory`或`controller`。如果不同方必须采取行动，请使用委托模式，其中授权方创建授予行使权的合同。

### 同一份合同的争用

当两笔交易试图同时对同一份合约执行消费选择时，其中一笔交易将被拒绝：

```
ABORTED: Interpretation error: ... contract not active
```

这是 Canton 基于 UTXO 的模型中的预期行为。修复取决于您的用例：

* **如果操作是幂等的，则使用退避重试**
* **重新设计工作流程**以减少单合约瓶颈（例如，将计数器合约拆分为分片）
* **订购时客户端的顺序操作**

### 包审核：DAR 未上传

如果您的交易引用了验证器不知道的包，您将得到：

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <package-id>
```

在提交交易之前上传您的 DAR 文件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Using dpm
dpm build
dpm sandbox

# Or upload manually via the Admin API
curl -X POST http://localhost:5002/v2/packages \
  -F "dar=@.build/your-package.dar"
```

验证包是否已知：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost:5002/v2/packages | jq '.package_ids | length'
```

<Note>
  For cn-quickstart, run `make setup` then `make build` before `make start`. The build step compiles Daml and uploads DARs to the local environment.
</Note>

## 其他 Daml 错误消息

### 错误：“\<X> 无权提交更新”

当合同中有多个义务人时，就会出现此错误。

Daml 的基石是您不能创建一个会迫使其他方（或多方）承担义务的合同。此错误意味着一方试图在未经另一方同意的情况下迫使另一方达成协议。

为了解决这个问题，请确保各方通过行使选择自由地签订合同。确保这一点的一个好方法是“初始并接受”模式：有关更多详细信息，请参阅 Daml 模式。

### 错误：“参数不是可序列化类型”

当您使用函数作为模板的参数时，会发生此错误。例如，这是一个由接收者的主管创建 `Payout` 控制器的合约：

将鼠标悬停在编译错误上会显示：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
[Type checker] Argument expands to non-serializable type Party -> Party.
```

### 错误：“模块中的递归限制溢出”

当将 DAR 上传到分类帐或通过沙箱使用脚本时，通常会发生该错误。它可以在上传时显示为：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{"code":"DAR_PARSE_ERROR", "cause": "Failed to parse the dar file content.", ...}
```

或在您的日志中为：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
Recursion limit overflow in module '<pkgid>:<modulename>'
```此错误通常是由于 DAR 中的序列化表示深度超过 1000 层的表达式引起的。这可能是由长 Daml 脚本引起的，因为每次使用函数调用或 `<-` 来绑定 `do` 块中的变量都可能会在 `do` 块的序列化表示中产生多层递归。具有超过 160 个字段且带有 `deriving` 子句的大型数据类型也可能导致此问题。

### 解决脚本递归限制

通常，`do` 内的一次调用会引入 4 层递归，这意味着脚本中大约 250 个绑定可能会导致溢出。但是，do 块中的其他表达式（例如 let binds）也会引入一层递归，因此绑定较少的函数也可能会触发限制。

可能的解决方法包括将大型脚本拆分为多个脚本或将脚本中的逻辑分离为辅助函数。例如，假设您编写了以下长脚本：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data State = State { partA : Text, partB : Text, partC : Text }

-- MyTemplate defines three choices that update parts A, B, and C of the State
myScript : Party -> ContractId MyTemplate -> State -> Script State
myScript party cid state0 = do
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state0)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state0)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state0)
  let state1 = State newPartA newPartB newPartC

  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state1)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state1)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state1)
  let state2 = State newPartA newPartB newPartC

  ...
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state99)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state99)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state99)
  let state100 = State newPartA newPartB newPartC

  pure state100
```

该脚本有 300 个绑定，远远超过了 250 个绑定的暂定限制。我们可以重构这个脚本来定义和使用一个帮助器`updateStateOnce`，它一起运行所有三个选择。

**注意：** 在许多情况下，编译器会优化您的脚本以生成一个表达式，尽管有许多绑定，但该表达式不会打破递归限制。在这个例子中，我们故意给出了一个复杂的例子，编译器很难优化掉它。

通过使用这个助手，三个练习的每个块都减少为一个绑定，这样 `myScript` 现在只有 100 个绑定，远低于递归限制。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data State = State { partA : Text, partB : Text, partC : Text }
  deriving (Show, Eq)

helper : Party -> ContractId MyTemplate -> State -> Script State
helper party cid state = do
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state.partA)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state.partB)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state.partC)
  pure (State newPartA newPartB newPartC)

myScript : Party -> ContractId MyTemplate -> State -> Script State
myScript party cid state0 = do
  state1 <- helper party cid state0
  state2 <- helper party cid state1
  ...
  state100 <- helper party cid state99

  pure state100
```一般来说，通过最大化代码重用并将逻辑拆分为可维护的块来保持脚本较小是一个好主意。

### 解决数据类型递归限制

带有 `deriving` 子句的大数据类型也可能导致溢出错误。考虑以下具有 300 个字段的数据类型和一个 `deriving Show` 实例的情况：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyData = MyData
  { field1A : Text
  , field1B : Text
  , field1C : Text
  , field2A : Text
  , field2B : Text
  , field2C : Text
  ...
  , field100A : Text
  , field100B : Text
  , field100C : Text
  }
  deriving Show
```

在这种情况下，`deriving Show`子句意味着`Show MyData`的实例自动派生为如下所示：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Something similar to this code is implicitly autogenerated by the `deriving Show` clause
instance Show MyData where
  show MyData {..} =
    show field1A <> (show field1B <> (show field1C <> (
      (show field2A <> (show field2B <> (show field2C <> (
        ...
        (show field100A <> (show field100B <> (show field100C)))
      ))))
    )))
```

您可以看到，`show` 的隐式自动生成定义的表达式随着您的进行而嵌套得越来越深。一旦字段数超过 160 左右，该表达式就有可能达到所需的深度，从而导致 DAR 中的序列化表示溢出。

与 Daml 脚本类似，针对此问题的建议解决方法是将数据类型拆分为多个部分。例如，我们可以创建一个附加数据类型 `Helper`，其中包含元素 `a`、`b` 和 `c`，并在 `MyData` 中使用它：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Helper = Helper
  { a : Text
  , b : Text
  , c : Text
  }
  deriving Show

data MyData = MyData
  { field1 : Helper
  , field2 : Helper
  ...
  , field100 : Helper
  }
  deriving Show
```

`MyData` 生成的代码现在只有 100 个字段需要遍历和嵌套。与脚本类似，通过最大化代码重用并将逻辑拆分为可维护的块，保持数据类型较小是一个好主意。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
