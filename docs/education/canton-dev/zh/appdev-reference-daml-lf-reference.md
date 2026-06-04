---
title: "Daml-LF 参考"
slug: "appdev-reference-daml-lf-reference"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-lf-reference.md"
source_title: "Daml-LF Reference"
tags:
  - appdev
  - reference
  - daml-lf-reference
---

# Daml-LF 参考

> Daml-LF 类型转换、JSON 编码、Protobuf 映射、包与 DAR 结构说明。


## 什么是账本 API

**Ledger API** 是由任何参与者节点公开的 API。用户通过 Ledger API 访问和操作账本状态。 Ledger API 有两种可用的协议：gRPC 和 JSON。核心服务是使用[gRPC]()和[Protobuf]()实现的。还有一个转换层，将所有 Ledger API 服务额外公开为 JSON Ledger API。

有关服务的高级介绍，请参阅`ledger-api-services`。

您可能还想阅读 API 的 protobuf 文档，其中解释了如何通过其 protobuf 消息定义每个服务。

## 如何访问 Ledger API

您可以通过 Java 绑定访问 gRPC Ledger API。

如果您不使用面向 JVM 的语言，则可以使用 gRPC 生成代码来以支持 `proto` 标准的多种编程语言访问 Ledger API。

如果您不想使用 gRPC API，也可以使用 JSON Ledger API。此 API 使用 openapi 和 asyncapi 描述进行正式描述。您可以使用任何支持 OpenAPI 标准的语言来使用 OpenAPI [Generators]() 生成客户端。

## Daml-LF

当您将 Daml 源代码编译为 .dar 文件时，底层格式为 Daml-LF。 Daml-LF 与 Daml 类似，但被精简为一组核心功能。表面 Daml 语法和 Daml-LF 之间的关系与 Java 和 JVM 字节码之间的关系大致相似。

作为用户，您不需要直接与 Daml-LF 交互。但在内部，它用于：

* 在Ledger上执行Daml代码
* 通过 Ledger API 发送和接收值
* 生成其他语言的代码以与 Daml 模型交互（通常称为“codegen”）

Daml 助手提供了两个代码生成器，可将 DAML-LF 转换为 Java 或 Typescript 中 Daml 的惯用表示形式。

### 当您需要了解 Daml-LF 时

仅当您处理发送到分类帐或从分类帐接收的对象时，Daml-LF 才真正相关。如果您使用任何提供的代码生成器，则根本不需要了解 Daml-LF。

否则，了解 Daml 代码中的类型在 Daml-LF 级别是什么样子会很有帮助，这样您就知道对 Ledger API 有何期望。

例如，如果您正在编写一个创建一些 Daml 合约的应用程序，则需要构造值作为参数传递给合约。这些值由该合约模板中的 Daml-LF 类型确定。这意味着您需要了解 Daml-LF 类型如何与原始 Daml 模型中的类型相对应。

在大多数情况下，类型从 Daml 到 Daml-LF 的转换应该不足为奇。本页详细介绍了所有案例。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/reference/json-api/lf-value-specation.rst" hash="a3820c5d" */}

# Daml-LF JSON 编码

Daml-LF 值在 JSON Ledger API 中表示为 JSON 值。每当 `JSON Ledger API` 需要 `Daml` 记录或值时，例如在 `CreateCommand` 组件的 `createArguments` 字段中，就会使用此表示形式。当从 `JSON Ledger API` 返回值时，也会发生从 Daml 值到 JSON 的转换。有关 `Daml` 类型的更多信息，请参阅 `daml-ref-built-in-types`。| Daml-LF型| JSON 类型 |示例|       |        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -----| ------ |
| `Int` | `string`优先；接受作为输入的数字。范围：`[-9223372036854775808, 9223372036854775807]`。                                          | `1234567890` |       |        |
| `Decimal` | `string`优先；接受作为输入的数字。范围：`[-(10^38 - 1) / 10^10, (10^38 - 1) / 10^10]`。格式：`-?[0-9]{1,28}(\.[0-9]{1,10})?`。 | `"1234.56"` |       |        |
| `Timestamp` | `string` ISO 8601 时间戳。                                                                                                                 | `"2023-04-06T04:30:23.1234569Z"` |       |        |
| `Date` | `string` ISO 8601 日期。                                                                                                                      | `"2023-04-06"`|       |        |
| `Unit` |空 JSON 对象。                                                                                                                           | `{}` |       |        |
| `Text` | `string` | `"my text value"` |       |        |
| `Bool` | `boolean` | `false` |       |        |
| `ContractId` | `string` | `"1234:56:7890"` |       |        |
| `Party` | `string` | `"Alice:1234567890"` |       |        |
| `Record` |每个记录字段具有一个属性的 JSON 对象。                                                                                              | `{"field1Label": "value of field1", "field2Label": "value of field2"}` |       |        |
| `List` | JSON 数组。                                                                                                                                  | `[1, 7, 3, 4, 5]` |       |        |
| `TextMap` |由文本值作为键控的 JSON 对象。                                                                                                            | `{"key1": "value1", "key2": "value2"}` |       |        |
| `Variant` |具有 `tag` 和 `value` 属性的 JSON 对象。                                                                                               | `{"tag": "InAccount", "value": {"number": "CH-1234567890", "bank": {}}}` |       |        |
| `Optional` |定义时为 JSON 值，或为空时为 `null`。                                                                                               | `null` |       |        |
| `Enum` | `string` 枚举值名称。                                                                                                                    | `"Red"` 为 Daml \`data Color = Red                                      | Green | Blue\` |<Note>
  `Int` 和 `Decimal` 值首选字符串，因为许多语言（尤其是 JavaScript）使用 IEEE 双精度数表示 JSON 数字，并且无法精确表示每个 Daml-LF 值。为了方便起见，解析同时接受 JSON 数字和字符串。
</Note>

<Note>
  时间戳解析很灵活，接受`yyyy-mm-ddThh:mm:ss(.s+)?Z`。超过微秒的亚秒级精度会下降。必须包含 UTC 时区指示符，以降低意外超过当地时间的风险。
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/damllf/daml-lf-translation.rst" hash="2de9f83c" */}

# Daml 类型如何转换为 Daml-LF

此页面显示如何将 Daml 中的类型转换为 Daml-LF。它应该可以帮助您理解和预测生成的客户端接口，这在您构建使用 Ledger API 或其他语言的客户端绑定的基于 Daml 的应用程序时非常有用。

## 原始类型

Daml 中的内置数据类型可以直接映射到 Daml-LF。

本节仅涵盖可序列化类型，因为这些是客户端应用程序可以通过生成的 Daml-LF 进行交互的类型。 （可序列化类型是指其值可以存在于账本上的类型。函数类型、`Update`和`Scenario`类型以及由这些类型构建的任何类型均被排除在外，并且还有其他一些限制。）

大多数内置类型在 Daml-LF 中的名称与在 Daml 中的名称相同。这些是精确的映射：

| Daml 原始类型 | Daml-LF 原始类型 |
| ------------------- | ---------------------- |
| `Int` | `Int64` |
| `Time` | `Timestamp` |
| `()` | `Unit` |
| `[]` | `List` |
| `Decimal` | `Decimal`|
| `Text` | `Text` |
| `Date` | `Date` |
| `Party` | `Party` |
| `Optional` | `Optional` |
| `ContractId` | `ContractId` |

请注意，只有 Prelude 模块导出的 Daml 基元类型映射到上面的 Daml-LF 基元类型。这意味着，如果您定义自己的类型名为 `Party`，它不会转换为 Daml-LF 原语 `Party`。

## 元组类型

Daml 元组类型构造函数将类型 `T1, T2, …, TN` 转换为类型 `(T1, T2, …, TN)`。这些通过 Prelude 模块以 Daml 表面语言公开。

对于每个特定的 N（其中 2 <= N \<= 20），等效的 Daml-LF 类型构造函数是 `daml-prim:DA.Types:TupleN`。该限定名称是指包名称（`ghc-prim`）和模块名称（`GHC.Tuple`）。

例如：Daml 对类型`(Int, Text)` 转换为`daml-prim:DA.Types:Tuple2 Int64 Text`。

## 数据类型

Daml-LF 具有三种数据声明：

* **记录**类型，定义数据集合
* **Variant** 或 **sum** 类型，定义了许多替代方案
* **Enum**，它定义了没有类型参数或参数的简化 **sum** 类型。

Daml 中的数据类型声明（以 `data` 关键字开头）被转换为记录、变体或枚举类型。有时它们将被翻译成什么并不明显，因此本节列出了 Daml 中数据类型的许多示例及其在 Daml-LF 中的翻译。

### 记录声明

本节使用带大括号的 Daml 记录语法。

|达姆声明| Daml-LF 翻译 |
| ------------------------------------------------------ | ------------------------------------------------------ |
| `data Foo = Foo { foo1: Int; foo2: Text }` | `record Foo ↦ { foo1: Int64; foo2: Text }` |
| `data Foo = Bar { bar1: Int; bar2: Text }` | `record Foo ↦ { bar1: Int64; bar2: Text }` |
| `data Foo = Foo { foo: Int }` | `record Foo ↦ { foo: Int64 }` |
| `data Foo = Bar { foo: Int }` | `record Foo ↦ { foo: Int64 }` |
| `data Foo = Foo {}` | `record Foo ↦ {}` |
| `data Foo = Bar {}` | `record Foo ↦ {}` |

### 变体声明|达姆声明 | Daml-LF 翻译 |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data Foo = Bar Int \| Baz Text` | `variant Foo ↦ Bar Int64 \| Baz Text` |
| `data Foo a = Bar a \| Baz Text` | `variant Foo a ↦ Bar a \| Baz Text` |
| `data Foo = Bar Unit \| Baz Text` | `variant Foo ↦ Bar Unit \| Baz Text` |
| `data Foo = Bar Unit \| Baz` | `variant Foo ↦ Bar Unit \| Baz Unit` |
| `data Foo a = Bar \| Baz` | `variant Foo a ↦ Bar Unit \| Baz Unit` |
| `data Foo = Foo Int` | `variant Foo ↦ Foo Int64` |
| `data Foo = Bar Int` | `variant Foo ↦ Bar Int64` |
| `data Foo = Foo ()` | `variant Foo ↦ Foo Unit` |
| `data Foo = Bar ()` | `variant Foo ↦ Bar Unit` |
| `data Foo = Bar { bar: Int } \| Baz Text` | `variant Foo ↦ Bar Foo.Bar \| Baz Text`、`record Foo.Bar ↦ { bar: Int64 }` |
| `data Foo = Foo { foo: Int } \| Baz Text` | `variant Foo ↦ Foo Foo.Foo \| Baz Text`、`record Foo.Foo ↦ { foo: Int64 }` |
| `data Foo = Bar { bar1: Int; bar2: Decimal } \| Baz Text` | `variant Foo ↦ Bar Foo.Bar \| Baz Text`、`record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }` |
| `data Foo = Bar { bar1: Int; bar2: Decimal } \| Baz { baz1: Text; baz2: Date }` | `variant Foo ↦ Bar Foo.Bar \| Baz Foo.Baz`、`record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }`、`record Foo.Baz ↦ { baz1: Text; baz2: Date }` |

### 枚举声明

|达姆声明| Daml-LF 声明 |
| ----------------------------------- | ----------------------------------- |
| `data Foo = Bar \| Baz` | `enum Foo ↦ Bar \| Baz` |
| `data Color = Red \| Green \| Blue` | `enum Color ↦ Red \| Green \| Blue` |

### 禁止声明

有两个问题需要注意：您可能期望在 Daml 中能够执行的操作，但由于 Daml-LF 而无法执行。

第一：单个构造函数数据类型必须明确说明它是记录类型还是变体类型。具体来说，数据类型声明`data Foo = Foo`会导致编译时错误，因为不清楚它是在声明记录类型还是变体类型。

要解决此问题，您必须明确区分。编写 `data Foo = Foo {}` 来声明没有字段的记录类型，或者编写 `data Foo = Foo ()` 来声明带有单位参数的单个构造函数的变体。第二个问题是数据类型声明中的构造函数最多可以有一个未标记的参数类型。此限制是为了让我们能够以各种客户端语言提供 Daml-LF 类型的直接编码。

|禁止声明|解决方法|
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `data Foo = Foo` | `data Foo = Foo {}` 生产 `record Foo ↦ {}` 或 `data Foo = Foo ()` 生产 `variant Foo ↦ Foo Unit` |
| `data Foo = Bar` | `data Foo = Bar {} to produce record Foo ↦ {}` 或 `data Foo = Bar () to produce variant Foo ↦ Bar Unit` |
| `data Foo = Foo Int Text` |使用记录声明命名构造函数参数，例如 `data Foo = Foo { x: Int; y: Text }` |
| `data Foo = Bar Int Text` |使用记录声明命名构造函数参数，例如 `data Foo = Bar { x: Int; y: Text }` |
| `data Foo = Bar \| Baz Int Text` | Baz 构造函数的名称参数，例如 `data Foo = Bar \| Baz { x: Int; y: Text }` |

### 升级限制

数据类型的 Daml-LF 表示的风格限制了它可以通过智能合约升级进行升级的方式：只有记录可以添加字段，只有变体和枚举可以添加新的构造函数。一旦选择了数据类型，就无法更改它的风格。

因此，数据类型风格的理想选择很大程度上取决于为其计划的升级行为。例如，以下数据类型：

```
data Foo = Foo { foo: Int }
```

被翻译成 Daml-LF 中的记录：

```
record Foo ↦ { foo: Int64 }
```

我们可以在升级时添加字段，因为这不会改变它的风格：

```
-- Add a field to Foo in version 2 of its package
data Foo = Foo { foo: Int, newField: Int }
```

```
// Still a record
record Foo ↦ { foo: Int64, newField: Int }
```

但是，我们无法添加新的构造函数，因为这会将其风格从记录更改为变体：

```
-- Add a constructor to Foo in version 2 of its package
data Foo
  = Foo { foo: Int }
  | NewConstructor
```

```
// Flavour changed from a record to a variant
variant Foo ↦ Foo Foo.Foo | NewConstructor
```

请注意，如上所述，带有字段的变体将脱糖为单个变体和每个构造函数的记录，如下所示：

```
-- Add a constructor to Foo in version
data Foo
  = Bar { bar1: Int; bar2: Decimal }
  | Baz { baz1: Text; baz2: Date }
```

```
// Desugars to a variant datatype and two record datatypes, one for each
// of the variant's constructors
variant Foo ↦ Bar Foo.Bar | Baz Foo.Baz
record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }
record Foo.Baz ↦ { baz1: Text; baz2: Date }
```

这意味着我们可以升级构造函数的字段，并同时向该特定数据类型添加新的构造函数，因为这些更改是对底层 Daml-LF 定义的有效升级。

例如，如果我们添加一个字段`bar3`和一个构造函数`Bat`：

```
data Foo
  = Bar { bar1: Int; bar2: Decimal, bar3: Text } -- Add a bar3 field
  | Baz { baz1: Text; baz2: Date }
  | Bat { bat1: Int } -- Add a Bat constructor
```

```
variant Foo ↦ Bar Foo.Bar | Baz Foo.Baz | Bat Foo.Bat // Variant adds a constructor - allowed under upgrades
record Foo.Bar ↦ { bar1: Int64; bar2: Decimal; bar3: Text } // Record adds a variant - allowed under upgrades
record Foo.Baz ↦ { baz1: Text; baz2: Date }
record Foo.Bat ↦ { bat1: Int64 } // New variant constructor's underlying datatype
```

简而言之：如果数据类型计划随着时间的推移逐渐添加更多构造函数，则应将其定义为变体。如果数据类型计划随着时间的推移添加字段，则应将其定义为记录。如果数据类型计划同时执行这两种操作，则应将其定义为带有字段的变体。

有关智能合约升级对不同类型数据类型施加的限制的更多信息，请参阅升级变体的限制。

## 输入同义词

类型同义词（以 `type` 关键字开头）在转换为 Daml-LF 期间被消除。对于所有出现的类型同义词名称，类型同义词的主体都是内联的。

例如，请考虑以下 Daml 类型声明。```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type Username = Text
data User = User { name: Username }
```

`Username`类型在Daml-LF翻译中被消除，如下：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record User ↦ { name: Text }
```

## 模板类型

Daml 中的模板声明会在幕后生成一个或多个数据类型声明。本节详细介绍的这些数据类型不是在 Daml 程序中显式编写的，而是由编译器创建的。

使用与上述记录声明相同的规则将它们转换为 Daml-LF。

这些声明都位于定义模板的模块的顶层。

### 模板数据类型

每个合约模板都定义了合约参数的记录类型。例如，模板声明：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Iou
  with
    issuer: Party
    owner: Party
    currency: Text
    amount: Decimal
  where
```

导致此记录声明：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Iou = Iou { issuer: Party; owner: Party; currency: Text; amount: Decimal }
```

这转化为 Daml-LF 记录声明：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record Iou ↦ { issuer: Party; owner: Party; currency: Text; amount: Decimal }
```

### Choice数据类型

合约模板中的每个选择都会产生该选择的参数的记录类型。例如，假设早期的 `Iou` 模板有以下选择：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonconsuming choice DoNothing: ()
  controller owner
  do
    return ()

choice Transfer: ContractId Iou
  with newOwner: Party
  controller owner
  do
    updateOwner newOwner
```

这会产生以下两种记录类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data DoNothing = DoNothing {}
data Transfer = Transfer { newOwner: Party }
```

选择是消耗型还是非消耗型与数据类型声明无关。即使没有字段，数据类型也是记录。

这些转化为 Daml-LF 记录声明：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record DoNothing ↦ {}
record Transfer ↦ { newOwner: Party }
```

## 带有特殊字符的名称

Daml 中的所有名称（类型、模板、选择、字段和变体数据构造函数）都被转换为更严格的 Daml-LF 规则。 ASCII 字母、数字和`_`下划线在Daml-LF中保持不变；所有其他字符必须以某种方式进行破坏，如下所示：

* `$`更改为`$$`，
* 小于 65536 的 Unicode 代码点转换为 `$uABCD`，其中 `ABCD` 恰好是相关代码点的四个（零填充）十六进制数字，仅使用小写字母 `a-f`，并且
* Unicode 代码点更大转换为 `$UABCD1234`，其中 `ABCD1234` 恰好是相关代码点的八个（零填充）十六进制数字，具有相同的 `a-f` 规则。

|达米尔名字| Daml-LF 标识符 |
| --------- | ------------------------ |
| `Foo_bar` | `Foo_bar` |
| `baz'` | `baz$u0027` |
| `:+:` | `$u003a$u002b$u003a` |
| `naïveté` | `na$u00efvet$u00e9` |
| `:🙂:` | `$u003a$U0001f642$u003a` |

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/integrate/grpc/daml-to-ledger-api.rst" hash="b7b29e30" */}

# Daml 类型如何转换为 Protobuf

本页面概述和参考了 Daml 类型和合约如何由 gRPC Ledger API 作为 protobuf 消息表示，最值得注意的是：

* 在`com.daml.ledger.api.v1.transactionservice`的交易流中
* 作为`com.daml.ledger.api.v1.createcommand`和`com.daml.ledger.api.v1.exercisecommand`的有效负载发送到`com.daml.ledger.api.v1.commandsubmissionservice`和`com.daml.ledger.api.v1.commandservice`。

下面示例中的 Daml 代码是用 Daml *1.1* 编写的。

## 符号

此页面上用于 protobuf 消息的符号与调用 `protoc --decode=Foo < some_payload.bin` 时得到的符号相同。为了说明符号，这里是消息`Foo`和`Bar`的简单定义：```protobuf theme={"theme":{"light":"github-light","dark":"github-dark"}}
message Foo {
  string field_with_primitive_type = 1;
  Bar field_with_message_type = 2;
}

message Bar {
  repeated int64 repeated_field_inside_bar = 1;
}
```

然后，Ledger API 以如下方式表示 `Foo` 的特定值：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Foo
  field_with_primitive_type: "some string"
  field_with_message_type { // Bar
    repeated_field_inside_bar: 17
    repeated_field_inside_bar: 42
    repeated_field_inside_bar: 3
  }
}
```

消息名称作为注释添加在左大括号之后。

## 记录和原始类型

记录或产品类型被翻译为`com.daml.ledger.api.v1.record`。下面是一个示例 Daml 记录类型，其中包含每个基本类型的字段：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyProductType = MyProductType with
  intField : Int
  textField : Text
  decimalField : Decimal
  boolField : Bool
  partyField : Party
  timeField : Time
  listField : [Int]
  contractIdField : ContractId SomeTemplate
```

下面是创建 \`MyProductType\` 类型值的示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
alice <- allocateParty "Alice"
bob <- allocateParty "Bob"
someCid <- submit alice do createCmd SomeTemplate with owner=alice

let myProduct = MyProductType with
            intField = 17
            textField = "some text"
            decimalField = 17.42
            boolField = False
            partyField = bob
            timeField = datetime 2018 May 16 0 0 0
            listField = [1,2,3]
            contractIdField = someCid
```

对于此数据，Ledger API 上的相应数据如下所示。请注意，该值将包含在包含 `MyProductType` 类型字段的特定合约中。请参阅[合约模板](#contract-templates)，了解 Daml 合约到 Ledger API 表示的转换。

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Record
  record_id { // Identifier
    package_id: "some-hash"
    name: "Types.MyProductType"
  }
  fields { // RecordField
    label: "intField"
    value { // Value
      int64: 17
    }
  }
  fields { // RecordField
    label: "textField"
    value { // Value
      text: "some text"
    }
  }
  fields { // RecordField
    label: "decimalField"
    value { // Value
      decimal: "17.42"
    }
  }
  fields { // RecordField
    label: "boolField"
    value { // Value
      bool: false
    }
  }
  fields { // RecordField
    label: "partyField"
    value { // Value
      party: "Bob"
    }
  }
  fields { // RecordField
    label: "timeField"
    value { // Value
      timestamp: 1526428800000000
    }
  }
  fields { // RecordField
    label: "listField"
    value { // Value
      list { // List
        elements { // Value
          int64: 1
        }
        elements { // Value
          int64: 2
        }
        elements { // Value
          int64: 3
        }
      }
    }
  }
  fields { // RecordField
    label: "contractIdField"
    value { // Value
      contract_id: "some-contract-id" 
    }
  }
}
```

## 变体

变体或求和类型是具有多个构造函数的类型。此示例定义了一个带有两个构造函数的简单变体类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MySumType = MySumConstructor1 Int
               | MySumConstructor2 (Text, Bool)
```

构造函数`MyConstructor1`采用`Integer`类型的单个参数，而构造函数`MyConstructor2`采用具有两个字段的元组作为参数。下面的代码片段展示了如何使用任一构造函数创建值。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let mySum1 = MySumConstructor1 17
let mySum2 = MySumConstructor2 ("it's a sum", True)
```

与记录类似，变体也包含在合约、记录或其他变体中。

下面的片段分别显示了 `mySum1` 和 `mySum2` 的值，因为它们将在合约内的 Ledger API 上传输。

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Value
  variant { // Variant
    variant_id { // Identifier
      package_id: "some-hash"
      name: "Types.MySumType"
    }
    constructor: "MyConstructor1"
    value { // Value
      int64:  17
    }
  }
}
``````text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Value
  variant { // Variant
    variant_id { // Identifier
      package_id: "some-hash"
      name: "Types.MySumType"
    }
    constructor: "MyConstructor2"
    value { // Value
      record { // Record
        fields { // RecordField
          label: "sumTextField"
          value { // Value
            text: "it's a sum"
          }
        }
        fields { // RecordField
          label: "sumBoolField"
          value { // Value
            bool: true
          }
        }
      }
    }
  }
}
```

## Contract Templates

合约模板表示为具有与模板相同标识符的记录。

下面的第一个示例模板仅包含签字方和一个要执行的简单选择：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MySimpleTemplateKey =
  MySimpleTemplateKey
    with
      party: Party

template MySimpleTemplate
    with
        owner: Party
    where
        signatory owner

        key MySimpleTemplateKey owner: MySimpleTemplateKey
        maintainer key.party
```

### Create a Contract

创建合约是通过将`com.daml.ledger.api.v1.createcommand`发送到`com.daml.ledger.api.v1.commandsubmissionservice`或`com.daml.ledger.api.v1.commandservice`来完成的。 The message to create a `MySimpleTemplate` contract with *Alice* being the owner is shown below:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // CreateCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  create_arguments { // Record
    fields { // RecordField
      label: "owner"
      value { // Value
        party: "Alice"
      }
    }
  }
}
```

### Receive a Contract

Contracts are received from the `com.daml.ledger.api.v1.transactionservice` in the form of a `com.daml.ledger.api.v1.createdevent`. The data contained in the event corresponds to the data that was used to create the contract.

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // CreatedEvent
  event_id: "some-event-id"
  contract_id: "some-contract-id"
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  create_arguments { // Record
    fields { // RecordField
      label: "owner"
      value { // Value
        party: "Alice"
      }
    }
  }
  witness_parties: "Alice"
}
```

### Exercise a Choice

通过发送`com.daml.ledger.api.v1.exercisecommand`来进行选择。 Taking the same contract template again, exercising the choice `MyChoice` would result in a command similar to the following:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // ExerciseCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  contract_id: "some-contract-id"
  choice: "MyChoice"
  choice_argument { // Value
    record { // Record
      fields { // RecordField
        label: "parameter"
        value { // Value
          int64: 42
        }
      }
    }
  }
}
```

If the template specifies a key, the `com.daml.ledger.api.v1.exercisebykeycommand` can be used. It works in a similar way as `com.daml.ledger.api.v1.exercisecommand`, but instead of specifying the contract identifier you have to provide its key.上面的例子可以重写如下：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // ExerciseByKeyCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  contract_key { // Value
    record { // Record
      fields { // RecordField
        label: "party"
        value { // Value
          party: "Alice"
        }
      }
    }
  }
  choice: "MyChoice"
  choice_argument { // Value
    record { // Record
      fields { // RecordField
        label: "parameter"
        value { // Value
          int64: 42
        }
      }
    }
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/explanations/daml-packages-and-archive-files.rst" hash="b5af20b7" */}

# Daml 包和归档 (.dar) 文件

When a Daml package is compiled, it is packed into a final artifact called a DAR (`.dar`) file.此 DAR 文件的目的是包含运行包模板所需的所有代码和逻辑，而不需要任何其他文件。例如，假设一个简单的包 `mypkg` 具有单个依赖项 `dep`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: mypkg
version: 1.0.0
source: daml
...
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- /path/to/dep-1.0.0.dar
```

命令 `dpm build` 编译它并在最后一行报告生成的 DAR 的路径：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm build

Running single package build of mypkg as no multi-package.yaml was found.
...
Compiling mypkg to a DAR.
...
Created .daml/dist/mypkg-1.0.0.dar
```

该 DAR 将包含该包的所有代码及其依赖项的所有代码。

## Structure of an archive file

DAR 实际上是一个 zip 文件，其中包含许多不同的文件，所有这些文件一起工作以提供分类帐所需的一切信息，以便运行其编译的代码。

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> unzip -Z1 .daml/dist/mypkg-1.0.0.dar

META-INF/MANIFEST.MF
...
mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.daml
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hi
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hie
mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
```

给定 DAR 中的大多数文件都是 DALF 文件 (`.dalf`)。每个 `.dalf` 文件包含特定包的完整编译代码。

DALF 文件之一将是编译 DAR 的“主”或“主”包 - 该 DALF 将包含最初在编译 DAR 的 Daml 代码中描述的模板、接口、数据类型和函数的定义。在本例中，即上面列出的 `mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf` 文件。

所有其他 DALF 文件将用于该“主”包的依赖包，这是运行该包所必需的。这包括 `dep-1.0.0-&lt;dep-package-id&gt;.dalf` 文件，以及 `daml-prim` 和 `daml-stdlib` 库的许多 DALF 文件。

Aside from these files, there will be:

* 一个 `MANIFEST.MF` 文件，其中包含有关 DAR 中其余工件的元数据。
  * 编译到 DAR 中的“主”包的名称
  * 主包的所有依赖项的列表
  * some more metadata about the package
* 主包的源代码（`.daml`）。 DAR 的使用者可以使用它来验证他们正在运行的 DALF 是否与其内部的代码相对应。 Daml Studio 还使用它来实现代码智能，例如当 DAR 作为另一个项目的依赖项包含时跳转到定义。
* 主包的接口文件（`.hi`、`.hie`、`.conf`）。 Daml Studio 也使用它来提供跳转到定义的功能。

除了 Daml Studio 之外，任何其他工具都不需要源代码和接口文件 - 它们可以由参与者（例如参与者跑步者）安全地从 DAR 中删除。

## Difference between DALF files and Daml files

一个常见的问题是为什么 DAR 文件包含 DALF 文件 - 为什么它们不直接包含所有包的所有源代码？

要了解原因，了解 Daml 和 DALF 文件之间的区别非常重要：

* Daml 文件包含 Daml 开发人员编写的 Daml 源代码。 Daml 源代码是人类可写和可读的，并且可以作为通用编程语言来阅读。
* 另一方面，DALF 文件包含 Daml-LF 的紧凑、二进制编码表示。 Daml-LF 是一种非常受限制的、相对简单的计算机可执行编程语言。 Daml-LF 的目的不是人类可读或人类可写，它的目的是确定性、快速执行和安全。

由于 DAR 文件旨在执行和传递，因此它们主要包含可以直接执行的 Daml-LF——它们不需要存储编译它的 Daml 代码。

## DAR 作为依赖项

当新项目需要依赖于不同的包时，该包编译到的 DAR 将作为新项目的 `daml.yaml` 中的数据依赖项提供。

例如，假设一个新包 `next-project` 使用 `mypkg` 包作为依赖项：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: next-project
version: 1.0.0
source: daml
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- ../mypkg/.daml/dist/mypkg-1.0.0.dar
```

在这种情况下，编译过程会解压 `mypkg-1.0.0` DAR，找到其主包，并将其公开为 `next-project` 内代码的依赖项。 When `next-project` is compiled, it retains all of the DALF files inside the `mypkg` DAR, including the `mypkg` package's dependencies.

一般来说，每当为具有进一步 DAR 依赖项的包编译 DAR 时，这些 DAR 依赖项都会被解包，并且它们的所有 DALF 文件都会复制到新的输出 DAR 中。但是，当复制 DALF 文件时，不会复制依赖项 DAR 的清单文件，也不会复制源代码和接口文件。 Only the source code and interface files for the primary package of a DAR can show up in a DAR.

For more information on how to open up and inspect the DAR files and DALF files, refer to the documentation on how to parse Daml archive files.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/component-howtos/development-tooling-authors/how-to-parse-daml-archive-files.rst" hash="1a25e77f" */}

# How to parse Daml archive files

When a Daml project is compiled, it produces a DAR (extension `.dar`), short for Daml Archive. The Daml compiler exposes commands for inspecting this archive.

## Inspecting a DAR file

You can run `dpm damlc inspect-dar /path/to/your.dar` to get a human-readable listing of the files inside it and a list of packages and their package ids. This is often useful to find the package id of the project you just built.

For example, consider a package `mypkg` which depends on a package `dep`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: mypkg
version: 1.0.0
source: daml/Main.daml
...
data-dependencies:
- ../dep/.daml/dist/dep-1.0.0.dar
```

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: dep
version: 1.0.0
source: daml/Dep.daml
...
```

当`mypkg-1.0.0`编译为DAR时，我们可以检查该DAR以确保它包含`mypkg`包及其依赖项`dep`：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm build
...
Created .daml/dist/mypkg-1.0.0.dar

> dpm damlc inspect-dar .daml/dist/mypkg-1.0.0.dar

DAR archive contains the following files:

...
mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.daml
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.hi
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.hie
META-INF/MANIFEST.MF

DAR archive contains the following packages:

...
dep-1.0.0-&lt;dep-package-id&gt; "&lt;dep-package-id&gt;"
mypkg-1.0.0-&lt;mypkg-package-id&gt; "&lt;mypkg-package-id&gt;"
```

The first section reports all of the files in DAR, and the second section reports the package name and package ID for every DALF in the archive.

More information on the exact structure of the zip file is available in the explanation on Daml packages and archive files.

## Inspecting a DAR file as JSON

In addition to the human-readable output, you can also get the output as JSON. This is easier to consume programmatically and it is more robust to changes across SDK versions:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm damlc inspect-dar --json .daml/dist/mypkg-1.0.0.dar
{
    "files": [
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.daml",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hi",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hie",
        "META-INF/MANIFEST.MF"
    ],
    "main_package_id": "&lt;mypkg-package-id&gt;",
    "packages": {
        "&lt;mypkg-package-id&gt;": {
            "name": "mypkg",
            "path":
              "mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf",
            "version": "1.0.0"
        },
        "&lt;dep-package-id&gt;": {
            "name": "dep",
            "path": "mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf",
            "version": "1.0.0"
        }
    }
}
```请注意，对于 Daml-LF \< 1.8 中的包，`name` 和 `version` 将是 `null`。

## 检查 DAR 文件的主包

如果您想检查 DAR 主包内的代码，Daml 编译器提供了 `inspect` 工具；运行 `dpm damlc inspect &lt;path-to-dar-file&gt;` 会以人类可读的格式打印该 DAR 文件主包中的所有代码。

例如，在上一节生成的 DAR 上运行 `inspect` 工具：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Human-readable dump of code in "mypkg" package inside of "mypkg" DAR
> dpm damlc inspect .daml/dist/mypkg-1.0.0.dar
package &lt;mypkg-package-id&gt;
daml-lf 2.1
metadata mypkg-1.0.0

module Main where
...
```

## 检查 DALF 文件

`inspect`工具也接受DALF文件；在 DALF 文件上运行 `dpm damlc inspect &lt;path-to-dalf-file&gt;` 会打印该 DALF 文件中的所有代码。

我们可以解压缩 DAR 以访问其 dalf 并检查它们，例如使用上一节中的 DAR：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Unzip the DAR to get its DALFs
> unzip .daml/dist/mypkg-1.0.0.dar

# Human-readable dump of code in dep
> dpm damlc inspect mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
package &lt;dep-package-id&gt;
daml-lf 2.1
metadata dep-1.0.0

module Dep where
...
```

我们甚至可以通过这种方式检查 DAR 的主包，尽管直接在 DAR 文件上运行 `inspect` 需要更少的步骤。

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Identical to dump from `dpm damlc inspect .daml/dist/mypkg-1.0.0.dar`
> dpm damlc inspect mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
package &lt;mypkg-package-id&gt;
daml-lf 2.1
metadata mypkg-1.0.0

module Main where
...
```

## 解析 DAR 和 DALF 文件

为了从 Scala 代码中解析 DAR 或 DALF 文件，Maven 上的`com-daml:daml-lf-archive-reader` 库提供了一个带有多个解码器的 Scala 包对象 `com.digitalasset.daml.lf.archive`。以下是解码器可以具有的常见输入和输出类型，以及根据所需的输入和输出使用哪些解码器。有关输入、输出和解码器的更多详细信息，请参阅 Maven 查找相关库的源代码。

### 输出类型

对包进行解码时，解码器可以根据需要具有多种可能的输出之一。

* 当需要包的完整代码时，选择一个返回元组`(PackageId, Package)`的解码器。

  在这种情况下，`PackageId`是一个类似字符串的类型，来自Maven上`com.daml:daml-lf-data`库中的`com.digitalasset.daml.lf.language.Ref`。 `Package`代表包的完整结构，来自Maven上`com.daml:daml-lf-language`库中的`com.digitalasset.daml.lf.language.Ast`。

  由于完全解码包比接下来的两个示例需要更多的处理时间，因此仅在需要完整包代码时才使用它。

  例如，Maven 上 `com-daml:daml-lf-api-type-signature` 库中的 `com.digitalasset.daml.lf.typesig.reader.SignatureReader` 类采用 `(PackageId, Package)` 对来生成 `com.digitalasset.daml.lf.typesig.PackageSignature`（也来自 `api-type-signature`）包，该包指定包中的所有模板、数据类型和接口。

* 当只需要包的 protobuf 的最简单表示时，选择返回 `com.digitalasset.daml.lf.ArchivePayload` 的解码器（来自 Maven 上的 `com-daml:daml-lf-archive` 库）。仅当使用包的内部 protobuf 表示时才需要这样做。

* 当只需要包的字节表示和哈希时，使用返回 `Archive`（来自 Maven 上的 `com-daml:daml-lf-archive-proto` 库）的解码器。使用此功能时，解码器不会花时间解码包的任何实际内容，例如其元数据或其代码。

### 输入类型

解码器可以接受 DALF 文件、DAR 文件，也可以同时接受两者。* 如果解码器接受 DALF 文件，它将将该 DALF 文件中的单个包解析为其输出类型（上面指定的三种类型之一）。
* If a decoder accepts DAR files, it will parse multiple packages from a DAR file to a struct `Dar[X]`, which is a case class that encodes a DAR as two public fields, `main: X` and `dependencies: List[X]`.
* 如果解码器接受两者，它将始终生成 `Dar[X]`。当给定 DAR 时，解码器将像普通 DAR 解码器一样运行。 When given a DALF, the decoder will decode the DALF as a single package and return a `Dar[X]` with a `main` package and an empty list of dependencies.

### 解码器

用于读取 DALF 的解码器是`GenReader[X]`的实例，它提供了方法`readArchiveFromFile(file: java.io.File): Either[Error, X]`。

* `val ArchiveReader: GenReader[ArchivePayload]`

  运行`ArchiveReader.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))`，解析出dalf文件的`ArchivePayload`。

* `val ArchiveDecoder: GenReader[(PackageId, Ast.Package)]`

  运行`ArchiveDecoder.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))`，解析出dalf文件的`(Ref.PackageId, Ast.Package)`。

* `val ArchiveParser: GenReader[DamlLf.Archive]`

  运行`ArchiveParser.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))`，解析出dalf文件的`DamlLf.Archive`。

用于读取 DAR 的解码器是`GenDarReader`的实例，它提供了方法`readArchiveFromFile(file: java.io.File): Either[Error, Dar[X]]`。

* `val DarReader: GenDarReader[ArchivePayload]`

  运行`DarReader.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))`解析出dar文件的`Dar[ArchivePayload]`。

* `val DarDecoder: GenDarReader[(PackageId, Ast.Package)]`

  运行`DarDecoder.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))`解析出dar文件的`Dar[(Ref.PackageId, Ast.Package)]`。

* `val DarParser: GenDarReader[DamlLf.Archive]`

  运行`DarParser.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))`解析出dar文件的`Dar[DamlLf.Archive]`。

用于读取 DAR 的解码器是`GenUniversalArchiveReader`的实例，它提供了方法`readFile(file: java.io.File): Either[Error, Dar[X]]`。

* `val UniversalArchiveReader: GenUniversalArchiveReader[ArchivePayload]`

  运行`UniversalArchiveReader.readFile(new java.io.File("&lt;path-to-dar-or-dalf&gt;"))`解析出dar文件的`Dar[ArchivePayload]`。

* `val UniversalArchiveDecoder: GenUniversalArchiveReader[(PackageId, Ast.Package)]`

  运行`UniversalArchiveDecoder.readFile(new java.io.File("&lt;path-to-dar-or-dalf&gt;"))`解析出dar文件的`Dar[(Ref.PackageId, Ast.Package)]`。

### 示例

我们可以使用 `daml-lf-archive-reader` 库加载 Scala REPL，以交互方式解析我们的 `mypkg` DAR：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> // Start a REPL
scala> val darEither = DarDecoder.readArchiveFromFile(".daml/dist/mypkg-1.0.0.dar")
val dar: Either[Error, Dar[(Ref.PackageId, Ast.Package)]]
Right(Dar((..., GenPackage(Map(Main -> ...
...

scala> // Extract the resulting value
scala> val dar = darEither.toOption.get

scala> :t dar.main
(Ref.PackageId, Ast.Package)

scala> :t dar.dependencies
List[(Ref.PackageId, Ast.Package)]
```

Dar 数据类型还有一个方法 `.all` ，它将主包和依赖项作为单个列表返回。对此进行映射 `_1` 即可获取 DAR 中的所有包 ID：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> dar.all.map(_._1)
val res1: List[Ref.PackageId] = List(224..., 54f..., ...)
```

通过`Ast.Package`数据类型中的`.metadata.name`字段获取DAR中所有依赖包的名称：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> dar.dependencies.map(_._2.metadata.name)
val res2: List[com.digitalasset.daml.lf.data.Ref.PackageName] = List(daml-prim, daml-prim-DA-Exception-ArithmeticError, ...
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
