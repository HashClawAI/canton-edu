---
title: "接口"
slug: "appdev-modules-m3-interfaces"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-interfaces.md"
source_title: "Interfaces"
tags:
  - appdev
  - modules
  - m3-interfaces
---

# 接口

> 定义并实现 Daml 接口，实现多态合约行为与跨模板互操作

# 参考：接口

在 Daml 中，接口定义抽象类型，并通过 view 类型、方法签名与 choice 规定行为。模板要符合该接口，须有对应的 `interface instance` 定义，实现接口的全部方法（含特殊的 `view` 方法）。这样可将行为与实现解耦，其他开发者可面向接口而非具体模板编写应用。

## 配置

使用本特性时 Daml 项目须目标 Daml-LF 版本 `1.15` 或更高（当前默认）。

若使用 Canton，sync domain 的协议版本应为 `4` 或更高，详见 Canton 协议版本说明。

## 接口声明

接口声明与模板声明有些相似。

### 接口名称

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface MyInterface where
```

* 即接口名称。
* 以关键字 `interface` 开头，`where` 结尾。
* 须以大写字母开头，与其他类型名相同。

### 隐式抽象类型

* 定义接口时，会定义同名抽象类型。「抽象」指：
  * 不能用数据构造子创建该类型的值，须对模板值应用 `toInterface` 构造。
  * 不能直接通过 case 分析检查该类型的值，须使用 `fromInterface` 等函数。
  * 更多交互函数见 `daml-ref-interface-functions`。
* 接口值内部携带用于构造它的模板类型与参数。
* 与模板类似，局部绑定 `b : I`（`I` 为接口）不一定意味着账本上存在用构造 `b` 的模板类型与参数创建的合约；仅当 `b` 来自同一交易内账本 fetch 时可作此假设。

### 接口方法

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
method1 : Party
  method2 : Int
  method3 : Bool -> Int -> Int -> Int
```

* 接口可定义任意数量的方法。
* 方法定义由方法名与类型组成，中间单个冒号 `:`。方法名须为以小写字母或下划线开头的合法标识符。
* 方法定义引入同名顶层函数：
  * 若接口为 `I`、方法为 `m`、类型为 `M`（可为函数类型），则引入 `m : I -> M`：

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    func1 : MyInterface -> Party
    func1 = method1

    func2 : MyInterface -> Int
    func2 = method2

    func3 : MyInterface -> Bool -> Int -> Int -> Int
    func3 = method3
    ```

  * 第一个参数类型 `I` 表示函数只能应用于接口类型 `I` 的值。即使有该模板的 `interface instance`，也不能对模板值直接应用方法，须先用 `toInterface` 转换。
  * 对该类参数应用后得到类型 `M` 的值，对应底层模板类型 `t`（构造接口值的模板类型）的 `I` 的 interface instance 中 `m` 的实现。
* 须为 view 类型定义特殊方法 `view`（见下文 **View 类型**）。

### 接口 View 类型

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyInterfaceViewType =
  MyInterfaceViewType { name : Text, value : Int }
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
viewtype MyInterfaceViewType
```

* 所有 interface instance 须实现返回 `viewtype` 声明类型的特殊 `view` 方法。
* 该类型须为记录。
* 对接口的订阅返回此类型。

### 接口 Choice

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice MyChoice : (ContractId MyInterface, Int)
    with
      argument1 : Bool
      argument2 : Int
    controller method1 this
    do
      let n0 = method2 this
      let n1 = method3 this argument1 argument2 n0
      pure (self, n1)

  nonconsuming choice MyNonConsumingChoice : Int
    controller method1 this
    do
      pure $ method2 this
```

* 接口 choice 与模板 choice 非常相似。存在 interface instance 的模板合约会向控制方授予该 choice。
* 接口 choice 只能在对应接口类型的值上 exercise；对模板值 exercise 接口 choice 须先用 `toInterface` 转换。
* 接口方法可用于定义 choice 的 controller（如 `method1`）以及 exercise 时执行的动作（如 `method2`、`method3`）。
* 与模板 choice 一样，`choice` 前可加 `nonconsuming`，表示 exercise 时不消耗合约；未指定则为 `consuming`。接口 choice 不支持 `preconsuming`、`postconsuming`。
* 完整参考见 `choices`，但接口 choice 不支持 controller-first 语法。

### 空接口

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data EmptyInterfaceView = EmptyInterfaceView {}

interface YourInterface where
  viewtype EmptyInterfaceView
```

* 可（虽未必有用）定义无方法、前置条件或 choice 的接口，但须始终定义 view 类型，可设为 unit。

## Interface Instance

上下文：简单模板定义：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    field1 : Party
    field2 : Int
  where
    signatory field1
```

### `interface instance` 子句

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance MyInterface for NameOfTemplate where
      view = MyInterfaceViewType "NameOfTemplate" 100
      method1 = field1
      method2 = field2
      method3 False _ _ = 0
      method3 True x y
        | x > 0 = x + y
        | otherwise = y
```

* 要使模板成为已有接口的实例，须在模板声明中定义 `interface instance` 子句。
* 子句中的模板须与外围声明一致：模板 `T` 的声明只能包含模板为 `T` 的 `interface instance`。
* 子句以 `interface instance` 开头，后跟接口名、`for`、模板名，`where` 引入块，**必须**实现接口的**全部**方法。
* 子句内有隐式局部绑定 `this`，指应用方法的合约，类型为模板数据记录；该合约的模板参数也在作用域。
* 方法实现可用与顶层函数相同的语法，含模式匹配与 guards（如 `method3`）。
* 每个方法实现的返回类型须与接口声明中该方法的类型一致。
* 特殊 `view` 方法的实现须返回接口声明中 `viewtype` 指定的类型。

### 空 `interface instance` 子句

* 若接口无方法，interface instance 只需实现 `view`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance YourInterface for NameOfTemplate where
      view = EmptyInterfaceView
```

## 接口函数

### `interfaceTypeRep`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>HasInterfaceTypeRep i =></code><br />
      <code>i -> TemplateTypeRep</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>MyInterface -> TemplateTypeRep</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>得到的 <code>TemplateTypeRep</code> 表示用于构造该接口值的模板。</td>
    </tr>
  </tbody>
</table>

### `toInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>t -> i</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>MyTemplate -> MyInterface</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>将模板值转换为接口值。</td>
    </tr>
  </tbody>
</table>

### `fromInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>HasFromInterface t i =></code><br />
      <code>i -> Optional t</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>MyInterface -> Optional MyTemplate</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>尝试将接口值转回模板值。若底层模板类型与期望不符，结果为 <code>None</code>。</td>
    </tr>
  </tbody>
</table>

### `toInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>ContractId t -> ContractId i</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>ContractId MyTemplate -> ContractId MyInterface</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>将模板 Contract ID 转为接口 Contract ID。</td>
    </tr>
  </tbody>
</table>

### `fromInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>forall t i.</code><br />
      <code>HasFromInterface t i =></code><br />
      <code>ContractId i -> ContractId t</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>ContractId MyInterface -> ContractId MyTemplate</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>将接口 contract id 转为模板 contract id。不验证该 id 是否指向结果类型的合约；若不匹配，后续 <code>fetch</code>、<code>exercise</code> 或 <code>archive</code> 会失败。因此仅当已知底层合约为结果类型，或结果立即用于 <code>fetch</code>/<code>exercise</code>/<code>archive</code> 且希望类型不匹配时交易失败时使用；其他情况考虑 <code>fetchFromInterface</code>。</td>
    </tr>
  </tbody>
</table>

### `coerceInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>forall j i.</code><br />
      <code>(HasInterfaceTypeRep i, HasInterfaceTypeRep j) =></code><br />
      <code>ContractId i -> ContractId j</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><code>ContractId SourceInterface -> ContractId TargetInterface</code></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>将接口 contract id 转为另一接口的 contract id。不验证底层类型；不匹配时后续 <code>fetch</code>、<code>exercise</code> 或 <code>archive</code> 会失败。仅当已知底层类型或立即用于上述操作且接受失败时使用。</td>
    </tr>
  </tbody>
</table>

### `fetchFromInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>类型</td>
      <td><p><code>forall t i.</code><br />
      <code>(HasFromInterface t i, HasFetch i) =></code><br />
      <code>ContractId i -> Update (Optional (ContractId t, t))</code></p></td>
    </tr>

    <tr class="even">
      <td>实例化类型</td>
      <td><p><code>ContractId MyInterface -></code><br />
      <code>Update (Optional (ContractId MyTemplate, MyTemplate))</code></p></td>
    </tr>

    <tr class="odd">
      <td>说明</td>
      <td>尝试 fetch 并将接口 contract id 转为模板，成功则返回转换后的合约与其 contract id，否则 <code>None</code>。</td>
    </tr>
  </tbody>
</table>

## 必需接口

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface OurInterface requires MyInterface, YourInterface where
  viewtype EmptyInterfaceView
```

* 接口可依赖其他接口，在接口名之后、`where` 之前用 `requires` 列出，逗号分隔。

* 接口声明有效时，其必需接口列表须传递闭包：接口 `I` 不能要求 `J` 却不显式要求 `J` 所要求的一切。顺序无关。

  例如给定

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Shape where
    viewtype EmptyInterfaceView

  interface Rectangle requires Shape where
    viewtype EmptyInterfaceView
  ```

  下列 `Square` 声明会编译错误

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  -- Compiler error! "Interface Square is missing requirement [Shape]"
  interface Square requires Rectangle where
    viewtype EmptyInterfaceView
  ```

  显式将 `Shape` 加入必需接口可修复

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Square requires Rectangle, Shape where
    viewtype EmptyInterfaceView
  ```

* 模板 `T` 要成为接口 `I` 的有效 `interface instance`，`T` 还须是 `I` 所要求的每个接口的 `interface instance`。

### 接口函数

| 函数                  | 说明                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `toInterface`             | 也可用于将接口值转换为其必需接口之一。                                                  |
| `fromInterface`           | 也可用于将接口类型值转换为其要求方接口之一。                                       |
| `toInterfaceContractId`   | 也可用于将接口 contract id 转为某必需接口的 contract id。                         |
| `fromInterfaceContractId` | 也可用于将接口 contract id 转为某要求方接口的 contract id。                        |
| `fetchFromInterface`      | 也可用于 fetch 并将接口 contract id 转为某要求方接口的合约与 contract id。 |

## Canton Network 上的接口

接口是 Canton Network 互操作的核心。两项 Canton Improvement Proposal（CIP）定义了应用开发者应了解的标准接口：

* [CIP-0056 — Token Standard](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)：定义 Canton Network 上同质化代币的标准接口。若应用发行或转移代币，实现该接口可与生态中的钱包及其他应用兼容。

* [CIP-0103 — dApp Standard](https://github.com/mjuchli-da/cips/blob/cip-dapp-standard/cip-0103/cip-0103.md)：定义去中心化应用的标准接口，对来自 Ethereum 的开发者尤其相关，将熟悉的 ERC 风格模式映射到 Daml 接口。

在 Canton Network 上构建应用时，实现这些标准接口可使合约参与更广泛生态，而无需为每个对手方定制集成。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
