---
title: "Daml 语言参考"
slug: "appdev-reference-daml-language-reference"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-language-reference.md"
source_title: "Daml Language Reference"
tags:
  - appdev
  - reference
  - daml-language-reference
---

# Daml 语言参考

> Daml 模板、choice、数据类型、表达式、包、接口与异常等语言参考。

## 概述：模板结构

本页介绍了模板的外观：模板的哪些部分以及它们的位置。

有关模板*外部*的 Daml 文件的结构，请参阅`file-structure`。

### 模板大纲结构

以下是 Daml 模板的结构：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    exampleParty : Party
    exampleParty2 : Party
    exampleParty3 : Party
    exampleParameter : Text
    -- more parameters here
  where
    signatory exampleParty
    observer exampleParty2
    ensure
      -- boolean condition
      True
    key (exampleParty, exampleParameter) : (Party, Text)
    maintainer (exampleFunction key)
    -- a choice goes here; see next section
```

[模板名称](#模板名称)
`template`关键词

[参数](#模板参数)
`with` 后面是参数名称及其类型

模板体
`where`关键词

可以包括：

[模板本地定义（已弃用）](#template-local-definitions-deprecated)
`let`关键词

允许您创建可以访问合约参数并且在模板定义的其余部分中可用的定义。

[签署方](#signatory-partys)
`signatory`关键词

必填。必须同意创建本合约的各方（请参阅 [Party](#built-in-types) 类型）。在所有各方都授权之前，您将无法创建此合约。

[观察者](#观察者)
`observer`关键词

可选。非签署方但您仍希望能够看到本合约的各方。

[前提条件](#preconditions)
`ensure`关键词

仅当 `ensure` 之后的条件评估为 true 时才创建合约。

[合约密钥](#contract-keys-and-maintainers)
`key`关键词

可选。允许您指定唯一标识此模板合约的一方和其他数据的组合。请参阅[合约密钥和维护者](#contract-keys-and-maintainers)。

[维护者](#contract-keys-and-maintainers)
`maintainer`关键词

如果您指定了`key`，则为必填项。按键仅对 `maintainer` 是唯一的。请参阅[合约密钥和维护者](#contract-keys-and-maintainers)。

[选择](#选择)
`choice NameOfChoice : ReturnType controller nameOfParty do`

定义可以执行的选择。请参阅[Choice 结构](#choice-struct) 了解选择中可以包含哪些内容。

### Choice结构

以下是模板内选项的结构：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoice
  : () -- replace () with the actual return type
  with
    party : Party -- parameters here
  controller party
  do
    return () -- replace this line with the choice body
```

[消费注释](#contract-consumation)
可选 `preconsuming`、`postconsuming`、`nonconsuming` 之一，这会更改有关隐私以及合约存档时的选择行为。更多详情请参见[选择中的合约消费](#contract-consumation)。

[名称](#choice 名称)
必须以大写字母开头。必须是唯一的 - 不同模板中的选项不能具有相同的名称。

[返回类型](#return-type)
在`:`之后，选择的返回类型

[choice 参数](#choice 参数)
`with`关键词

如果您包含 `Party` 作为choice 参数，则可以将 `Party` 设为选择的 `controller`。这意味着控制器可以在执行选择时指定，而不是在创建合约时指定。为了使练习发挥作用，当事人需要能够看到合约，即它必须是`observer`或`signatory`。

[一个（或多个）控制器](#controllers)
`controller`关键词

谁可以行使选择权。

[choice 观察者](#choice-observers)
`observer`关键词

可选。保证被告知行使选择权的其他各方。

要指定choice 观察者，您必须以 `choice` 关键字开始选择。

可选的 `observer` 关键字必须位于强制的 `controller` 关键字之前。

[选择身体](#choice-body)
在`do`关键字之后

当有人做出选择时会发生什么。选择主体可以包含更新语句：请参阅下面的[选择主体结构](#choice-body-struct)。

### Choice身体结构

选择主体包含 `Update` 表达式，包裹在 [do](#do) 块中。更新表达式为：

[创建](#创建)
创建此模板的新合约。

`create NameOfContract with contractArgument1 = value1; contractArgument2 = value2; ...`

[练习](#练习)
对特定合约行使选择权。

`exercise idOfContract NameOfChoiceOnContract with choiceArgument1 = value1; choiceArgument2 = value 2; ...`

[获取](#获取)
使用合约 ID 获取合约。通常与断言一起使用来检查合约内容的条件。

`fetchedContract <- fetch IdOfContract`

[fetchByKey](#fetchbykey)
与`fetch`类似，但使用[合约密钥](#contract-keys-and-maintainers)而不是ID。

`fetchedContract <- fetchByKey @ContractType contractKey`

[lookupByKey](#lookupbykey)
确认具有给定[合约密钥](#contract-keys-and-maintainers)的合约存在。

`fetchedContractId <- lookupByKey @ContractType contractKey`

[中止](#中止)
停止执行选择，更新失败。

`if False then abort`

[断言](#断言)
除非条件为真，否则更新失败。通常用于限制可以提供给合约选择的参数。

`assert (amount > 0)`

[获取时间](#获取时间)
获取账本时间。通常用于限制何时可以行使选择。

`currentTime <- getTime`

[返回](#返回)
显式返回一个值。默认情况下，选择返回其上次更新表达式的结果。这意味着如果您想退回其他东西，只需使用`return`。

`return ContractID ExampleTemplate`

选择主体还可以包含：

[let 关键字](#let)
用于分配值或函数。

为更新语句的结果赋值
例如：`contractFetched <- fetch someContractId`

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/templates.rst" hash="964a20f1" */}

## 参考：模板

此页面提供有关模板的参考信息：

模板的结构请参见`structure`。

### 模板名称

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
```

* 这是模板的名称。它前面有 `template` 关键字。必须以大写字母开头。
* 这是最高级别的嵌套。
* 创建此模板的合约时使用该名称（通常是在选择中）。

### 模板参数

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
with
  exampleParty : Party
  exampleParty2 : Party
  exampleParty3 : Party
  exampleParam : Text
  -- more parameters here
```

* `with` 关键字。参数采用记录类型的形式。
* 从此模板创建合约时传入。然后它们就在模板主体内的范围内。
* 模板参数不能与模板内的任何choice 参数同名。
* 对于参与合约的所有各方（无论是`signatory`、`observer`还是`controller`），您必须将它们作为参数传递给合约，无论是单独的还是作为列表（`[Party]`）。

### 隐式记录

每当定义模板时，都会使用与该模板相同的名称和字段隐式定义记录。此记录结构在 Daml 代码中用于表示基于该模板的合约的数据。

请注意，在一般情况下，`T`类型的本地绑定`b`的存在，其中`T`是一个模板（因此也是一条记录），并不一定意味着账本上存在与`b`具有相同数据的合约。仅当 `b` 是同一交易中从账本获取的结果时，您才能假设存在此类合约。

您可以创建 `T` 类型记录的新实例，而无需与账本进行任何交互；事实上，这就是构建创建命令的方式。

### `this` 和 `self`

在模板主体中，我们隐式定义本地绑定`this`来表示当前合约的数据。对于模板`T`，此绑定的类型为`T`，即模板定义的隐式记录。

在选项中，您还可以使用绑定`self`来引用当前合约（正在执行选项的合约）的合约ID。对于模板`T`的合约，`self`绑定的类型为`ContractId T`。

### 模板本地定义（已弃用）

<div className="todo">
  修复或删除此文字包含
</div>* `let` 关键字。启动一个块，后跟任意数量的定义，就像任何其他 `let` 块一样。
* 模板参数以及`this`在范围内，但`self`不在范围内。
* `let` 块中的定义可以在模板的 `where` 块中的任何其他位置使用。

<Warning>
  自 Daml 2.8.0 起，模板本地定义已被弃用，它们的存在将导致以下警告：

  ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  Template-local binding syntax ("template-let") is deprecated,
  it will be removed in a future version of Daml.
  Instead, use plain top level definitions, taking parameters
  for the contract fields or body ("this") if necessary.
  ```

  不推荐使用的原因是，在模板本地定义中使用 `this` 关键字会创建隐式循环依赖关系，从而导致求值时出现无限循环。
</Warning>

#### 迁移

强烈建议用户调整其代码以避免此功能。这涉及将每个模板本地定义替换为常规顶级定义。如果旧定义使用合约字段或合约主体（“this”），则新定义应将它们作为参数。相应地，这些定义的使用场所应该提供适当的值作为参数。

例如，考虑下面的模板`Person`。它定义并使用模板本地绑定`fullName`，现在会触发弃用警告。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Person
  with
    owner : Party
    first : Text
    last : Text
  where
    signatory owner
    let fullName = last <> ", " <> first
    nonconsuming choice GetDescription : ()
      controller owner
      do
        let desc = "An account owned by " <> fullName <> "."
        debug desc
```

为了确保该代码在删除该功能后继续工作，`fullName`应定义为顶级函数，并且其使用站点现在显式传递`this`。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fullName : Person -> Text
fullName Person {first, last} = last <> ", " <> first
-- takes 'Person' as an explicit parameter and unpacks required fields

template Person
  with
    owner : Party
    first : Text
    last : Text
  where
    signatory owner
    nonconsuming choice GetDescriptionV3 : ()
      controller owner
      do
        -- let bindings in choice bodies are unaffected
        let desc = "An account owned by " <> fullName this <> "."
                                             -- 'this' is passed explicitly
        debug desc
```

#### 关闭警告

该警告由警告标志`template-let`控制，这意味着它可以独立于其他警告进行切换。这对于逐步迁移使用此语法的代码特别有用。

要关闭 Daml 文件中的警告，请在文件顶部添加以下行：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
{-# OPTIONS_GHC -Wno-template-let #-}
```

要为整个 Daml 项目关闭它，请将以下条目添加到项目的 `daml.yaml` 文件的 `build-options` 字段中

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
build-options:
- --ghc-option=-Wno-template-let
```

在通过 `daml.yaml` 文件关闭警告的项目中，可以通过在每个文件的顶部添加以下行来为各个 Daml 文件重新打开警告：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
{-# OPTIONS_GHC -Wtemplate-let #-}
```

### 签署方

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
signatory exampleParty
```

* `signatory` 关键字。 `where`之后。后面至少有一个`Party`。

* 签字人是指必须同意订立本合约的各方（参见`Party`类型）。他们是在创建本合约时将处于“义务地位”的各方。

  未经他人同意，Daml 不会让你将某人置于有义务的位置。因此，如果合约会给一方带来义务，他们“必须”是签字人。 **如果他们没有授权，您将无法创建合约。** 在这种情况下，您可能会看到如下错误：

  `NameOfTemplate requires authorizers Party1,Party2,Party, but only Party1 were given.`* 当签署人同意创建合约时，这意味着他们也授权可以在本合约上行使的选择的后果。

* 合约对所有签署者（以及合约的其他利益相关者）都是可见的。也就是说，编译器自动将签署者添加为观察员。

* 每个模板**必须** 至少有一名签字人。签名声明由 `signatory` 关键字组成，后跟一个或多个表达式的逗号分隔列表，每个表达式表示一个 `Party` 或其集合。

### 观察员

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
observer exampleParty2
```

* `observer` 关键字。 `where`之后。后面至少有一个`Party`。
* 观察员是额外的利益相关者，因此合约对这些各方是可见的（参见`Party`类型）。
* 选修的。您可以有很多，可以是逗号分隔的列表，也可以重复使用关键字。您可以传入一个列表（类型为`[Party]`）。
* 当一方需要了解合约或了解合约事件但不是签字人或控制人时使用。
* 如果您从 `choice` 而不是 `controller` 开始选择（请参阅下面的 `daml-ref-choices`），则必须确保将任何潜在控制器添加为观察者。否则，他们将无法行使选择权，因为他们看不到合约。

### Choice

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoice
  : ()  -- replace () with the actual return type
  with
    exampleParameter : Text -- parameters here
  controller exampleParty
  do
    return () -- replace this line with the choice body
```

* 合约赋予控制方的权利。可以*锻炼*。
* 这本质上是模板所有逻辑的所在。
* 默认情况下，选择是“消耗性”的：也就是说，行使选择会将合约存档，因此无法对其执行进一步的选择。您可以使用 `nonconsuming` 关键字进行非消耗性选择。
* 完整参考信息请参见`choices`。

### 可序列化类型

模板的每个参数、choice 参数和选择结果都必须具有*可序列化类型*。这不仅仅意味着“可转换为字节”；它还意味着“可转换为字节”。它在Daml中有特定的含义。可序列化规则有三个目的：

1. 提供一种稳定的方式来永久存储账本价值。
2. 通过 `ledger-api` 提供合理的编码。
3. 为语言代码生成提供与 Java 等语言中的 Daml 对应项直接匹配的合理*类型*。

例如，Daml 提供的某些类型参数与 (1) 和 (2) 兼容，但在 (3) 中没有适当的对应项，因此不允许使用它们。类似地，函数类型有合理的 Java 对应项，满足 (3)，但没有可靠的方法来通过 API 存储或共享它们，因此无法满足 (1) 和 (2)。

以下类型*不可序列化*，因此不能在模板中使用。

* 函数类型。
* 具有任何不可序列化字段的记录类型。
* 具有任何不可序列化值情况的变体类型。
* 没有构造函数的变体和枚举类型。
* 对具有任何不可序列化类型参数的参数化数据类型的引用。无论数据类型定义是否使用类型参数，这都适用。
* 使用 `Nat` 类型参数或 `*` 以外的任何类型参数定义的数据类型。这意味着更高种类的类型以及仅将参数传递给 `Numeric` 的类型是不可序列化的。

#### 迁移

用户应从其代码中删除任何协议声明，因为此功能已从该语言中完全删除。

### 前提条件

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ensure
  True -- a boolean condition goes here
```

* `ensure` 关键字，后跟布尔条件。
* 用于合约创建。 `ensure` 限制了可以传递给合约的参数值：只有布尔条件为 true 时才能创建合约。

### 合约密钥和维护者<span id="daml-ref-contract-keys" />

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
key (exampleParty, exampleParam) : (Party, Text)
maintainer (exampleFunction key)
```

* `key` 和 `maintainer` 关键字。

* 此功能允许您指定一个“密钥”，您可以使用该“密钥”来唯一标识此合约作为此模板的实例。* 如果指定`key`，则还必须指定`maintainer`。这是一个`Party`，它将确保它所识别的所有键的唯一性。

  因此，`key`必须包含`maintainer``Party`或各方（例如，作为元组或记录的一部分），并且`maintainer`必须是签名者。

* 完整说明请参见`contractkeys`。

### 接口实例

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

* 用于使模板成为现有接口的实例。
* 该子句必须以关键字 `interface instance` 开头，后跟接口名称，然后是关键字 `for` 和模板名称（必须与包含的声明匹配），最后是关键字 `where`，它引入一个块，其中必须实现接口的 **所有** 方法。
* 有关接口的完整参考信息，请参阅`interfaces`，或具体了解接口实例的`interface-instances`部分。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/choices.rst" hash="a391ce22" */}

## 参考：选择

此页面提供有关选择的参考信息。有关选择的高级结构的信息，请参阅`structure`。

### Choice名称

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice ExampleChoice
  : () -- replace () with the actual return type
```

* `choice`关键字
* 选择的名称。必须以大写字母开头。
* 在模块中必须是唯一的。同一模块中定义的不同模板不能共享choice 名称。

### 控制器

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
controller exampleParty
```

* `controller`关键字

* 控制器是一个以逗号分隔的值列表，其中每个值要么是一个方，要么是多个方的集合。

  行使此选择权时，需要**所有**各方共同授权。

<Warning>
  您**必须**确保控制方是合约的观察者（或签署者），否则他们无法看到合约（因此无法行使选择权）。
</Warning>

### Choice观察员

*choice 观察者*可以使用 `observer` 关键字附加到选择。选择观察员是一系列非利益相关者，但可以看到该行动的所有后果的各方。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoiceWithObserver
  : () -- replace () with the actual return type
  with
    party : Party -- parameters here
  observer party -- optional specification of choice observers
  controller exampleParty
  do
    return () -- replace this line with the choice body
```

#### 合约消费

如果不存在限定符，则选择是“消耗性的”：合约在选择机构评估之前存档，控制者和所有合约利益相关者都可以看到该操作的所有后果。

### 预先选择

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
preconsuming choice ExamplePreconsumingChoice
  : () -- replace () with the actual return type
```

* `preconsuming` 关键字。选修的。
* 在消费前做出选择：在执行练习主体之前对合约进行存档。
* 合约的创建参数仍然可以在练习正文中使用，但不能通过其合约 id 获取。
* 归档行为类似于“消费”默认行为。
* 只有控制者和合约签署者才能看到该行为的所有后果。其他利益相关者仅看到存档操作。
* 可以被认为是一种非消耗性的选择，在任何其他事情发生之前隐式存档合约

### 消费后选择

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
postconsuming choice ExamplePostconsumingChoice
  : () -- replace () with the actual return type
```* `postconsuming` 关键字。选修的。
* 消费后做出选择：合约在练习主体执行后存档。
* 合约的创建参数以及用于获取合约的合约 ID 仍然可以在练习正文中使用。
* 只有控制者和合约签署者才能看到该行为的所有后果。其他利益相关者仅看到存档操作。
* 可以被认为是一种非消费 choice，在选择被行使后隐式存档合约

### 非消费 choice

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonconsuming choice ExampleNonconsumingChoice
  : () -- replace () with the actual return type
```

* `nonconsuming` 关键字。选修的。
* 做出非消耗性选择：即，行使选择不会存档合约。
* 只有控制者和合约签署者才能看到该行为的所有后果。
* 当您希望能够多次执行某个选择时，在许多情况下非常有用。

#### 返回类型

* 返回类型紧跟在choice 名称之后。
* 所有选择都有返回类型。不返回任何内容的合约应标记为返回“单位”，即`()`。
* 如果在选择主体中创建了合约，通常您会返回合约 ID（其类型为 `ContractId <name of template>`）。当执行选择时会返回该值，并且可以以多种方式使用。

### Choice参数

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
with
  exampleParameter : Text
```

* `with` 关键字。
* choice 参数的结构类似于`daml-ref-template-parameters`：记录类型。
* choice 参数不能与选择所在模板的任何参数同名。
* 可选 - 仅当您需要传递额外信息来进行选择时。

### Choice身体

* 与`do`一起介绍
* 本节中的逻辑是在执行选择时执行的逻辑。
* choice 体包含`Update`表达式。详细内容请参见`updates`。
* 默认情况下，返回选择中的最后一个表达式。您可以以元组形式或自定义数据类型返回多个更新。要返回不是 `Update` 类型的内容，请使用 `return` 关键字。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/updates.rst" hash="f8b9a0ff" */}

## 参考：更新

此页面提供有关更新的参考信息。其周围的结构参见`structure`。

### 背景

* `Update` 是账本更新。它们有很多不同的种类，下面列出了它们。
* 它们是可以选择的主体。

### 绑定变量

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boundVariable <- UpdateExpression1
```

* 您可以在选择主体中执行的操作之一是将 Update 表达式绑定（分配）到变量。这适用于以下任何更新。

### 做

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
   updateExpression1
   updateExpression2
```

* `do` 可用于对 `Update` 表达式进行分组。一个选择中只能有一个更新表达式，因此除了非常简单的选择之外的任何选择都将使用 `do` 块。

* 任何你可以放入choice 体的东西，你都可以放入`do`块。

* 默认情况下，`do` 返回块中**最后一个表达式**返回的内容。

  因此，如果您想返回其他内容，则需要显式使用 `return` - 有关示例，请参阅 `daml-ref-return`。

### 存档

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
archive ContractId
```

* `archive`功能。
* 归档已创建并驻留在分类账上的合约。合约通过其唯一的合约标识符`ContractId <name of template>`获取，然后对其执行`Archive`选择。
* 返回单位。
* 需要合约控制者/签署者的授权。如果没有所需的授权，交易就会失败。有关授权的更多详细信息，请参阅`daml-ref-signatories`。
* 所有模板都隐式有一个无法删除的`Archive`选项，相当于：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Archive : ()
  controller (signatory this)
  do return ()
```

### 创建

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
create NameOfTemplate with exampleParameters
```* `create`功能。

* 在账本上创建合约。当合约被提交到账本时，它会被赋予一个`ContractId <name of template>`类型的唯一合约标识符。

* 创建合约返回`ContractId`。

* 使用`with`指定模板参数。

* 需要所创建合约签署方的授权。这是通过作为创建其他合约的合约的签署者、作为控制者或显式创建合约本身来实现的。

  如果未给予所需的授权，交易将失败。更多授权详情请参见`daml-ref-signatories`。

###练习

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise IdOfContract NameOfChoiceOnContract with choiceArgument1 = value1
```

* `exercise`功能。
* 对指定合约执行指定选择。
* 使用`with`指定choice 参数。
* 需要所选控制器的授权。如果未授权，则交易失败。

### 练习按键

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseByKey @ContractType contractKey NameOfChoiceOnContract with choiceArgument1 = value1
```

* `exerciseByKey`功能。
* 类似`exercise`，但合约是通过合约key来指定的，而不是合约ID。
* 详情请参见参考：合约密钥：exerciseByKey

### 获取

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContract <- fetch IdOfContract
```

* `fetch`功能。
* 获取具有该 ID 的合约。通常与绑定变量一起使用，如上例所示。
* 通常用于在对合约进行选择之前检查合约的详细信息。也用于引用某些参考数据时。
* 如果`cid`不是活跃合约的合约id，`fetch cid`会失败，从而导致整个交易中止。
* 提交方必须是合约的观察者或签署者，否则`fetch`失败，同样会导致整个交易中止。

### fetchByKey

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContract <- fetchByKey @ContractType contractKey
```

* `fetchByKey`功能。
* 与 `fetch` 类似，但使用该合约密钥而不是合约 ID 来获取合约。
* 详细信息请参见参考：合约密钥：fetchByKey。

### 可见键

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isVisible <- visibleByKey @ContractType contractKey
```

* `visibleByKey`功能。
* 使用它来检查具有给定合约密钥的合约是否存在。
* 详情请参见参考：合约密钥：visibleByKey

### 通过键查找

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContractId <- lookupByKey @ContractType contractKey
```

* `lookupByKey`功能。
* 使用它来确认具有给定合约密钥的合约存在。
* 详情请参见参考：合约密钥：lookupByKey

### 中止

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
abort errorMessage
```

* `abort`功能。
* 交易失败 - 交易中的任何内容都不会提交到分类账中。
* `errorMessage` 属于类型 `Text`。使用错误消息向外部系统提供更多上下文（例如，它显示在 Daml Studio 脚本结果中）。
* 您可以使用`assert False`作为替代。

### 断言

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assert (condition == True)
```

* `assert` 关键字。
* 如果条件不成立则交易失败。因此，只有当布尔表达式的计算结果为 `True` 时，才能进行选择。
* 通常用于限制可提供给合约选择的参数。

以下是使用 `assert` 来防止在作为参数传递的 `Party` 位于黑名单上时执行选择的示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Transfer : ContractId RestrictedPayout
  with newReceiver : Party
  controller receiver
  do
    assert (newReceiver /= blacklisted)
    create RestrictedPayout with receiver = newReceiver; giver; blacklisted; qty
```

### 获取时间

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
currentTime <- getTime
```* `getTime` 关键字。
* 获取账本时间。 （您通常希望立即将其绑定到变量以便能够访问该值。）
* 用于限制何时可以做出选择。例如，对于`assert`，时间晚于某个时间。

以下是使用当前时间检查的选择示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Complete : ()
  controller party
  do
    -- bind the ledger effective time to the tchoose variable using getTime
    tchoose <- getTime
    -- assert that tchoose is no earlier than the begin time
    assert (begin <= tchoose && tchoose < addRelTime begin period)
```

###返回

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
return ()
```

* `return` 关键字。
* 用于从`do`块返回不属于`Update`类型的值。

下面是一个示例，其中在一个选项中创建了两个合约，并且它们的 id 都作为元组返回：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
  firstContract <- create SomeContractTemplate with arg1; arg2
  secondContract <- create SomeContractTemplate with arg1; arg2
  return (firstContract, secondContract)
```

###让

请参阅 `daml-ref-let` 的文档。

Let 看起来和绑定变量很相似，但是却有很大不同！此代码示例展示了如何：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
  -- defines a function, createdContract, taking a single argument that when
  -- called _will_ create the new contract using argument for issuer and owner
  let createContract x = create NameOfContract with issuer = x; owner = x

  createContract party1
  createContract party2
```

###这个

`this` 让您可以从选择主体内引用当前合约。这是指合约，*不是*合约 ID。

例如，如果您想将当前合约传递给模板外部的辅助函数，那么它很有用。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/data-types.rst" hash="e8514698" */}

## 参考：数据类型

此页面提供有关 Daml 数据类型的参考信息。

### 内置类型

#### 内置基本类型表|类型 |对于 |示例|笔记|
| ----------- | -------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| `Int` |整数 | `1`、`1000000`、`1_000_000` | `Int`值是有符号的64位整数，表示`-9,223,372,036,854,775,808`和`9,223,372,036,854,775,807`之间的数字（含）。算术运算会在溢出和除以 `0` 时引发错误。为了使长数字更具可读性，您可以选择添加下划线。                                                                                                       |
| `Decimal` | `Numeric 10` 的缩写 | `1.0` | `Decimal` 值是精度为 38、小数位数为 10 的有理数。
| `Numeric n` |定点十进制数 | `1.0` | `Numeric n` 值是总位数为 `38` 的有理数。比例参数`n`控制小数点后的位数，因此例如，`Numeric 10`值小数点前有28位，小数点后10位，`Numeric 20`值小数点前有18位，小数点后有20位。 `n` 的值必须在 `0` 和 `37` 之间（含）。 |
| `Text` |字符串| `"hello"` | `Text` 值是用双引号括起来的字符串。                                                                                                                                                                                                                                                                                                                                  |
| `Bool` |布尔值 | `True`、`False` |                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Party` |代表一方的 unicode 字符串 | `alice <- getParty "Alice"` | Daml 系统中的每个*方*都有一个`Party`类型的唯一标识符。要创建`Party`类型的值，请对调用`getParty`的结果使用绑定。派对文本只能包含字母数字字符、`-`、`_` 和空格。                                                                                                                                                           |
| `Date` |型号日期| `date 2007 Apr 5` |允许的日期范围从 `0001-01-01` 到 `9999-12-31`（使用年月日格式）。要创建`Date`类型的值，请使用函数`date`（要获取此函数，请导入`DA.Date`）。                                                                                                                                                                                                      |
| `Time` |型号绝对时间 (UTC) | `time (date 2007 Apr 5) 14 30 05` | `Time` 值具有微秒精度，允许范围从 `0001-01-01` 到 `9999-12-31`（使用年月日格式）。要创建`Time`类型的值，请使用`Date`和函数`time`（要获取此函数，请导入`DA.Time`）。                                                                                                                                                     |
| `RelTime` |模型时间值之间的差异 | `seconds 1`、`seconds (-2)` | `RelTime` 值具有微秒精度，允许范围从 `-9,223,372,036,854,775,808ms` 到 `9,223,372,036,854,775,807ms` `RelTime` 没有文字。相反，它们是使用 `days`、`hours`、`minutes`、`seconds`、`milliseconds` 和 `microseconds` 之一创建的（要获取这些函数，请导入 `DA.Time`）。                                                                 |#### 转义字符

`Text` 文字支持反斜杠转义以包含其分隔符 (`\"`) 和反斜杠本身 (`\\`)。

#### 时间

账本上时间的定义是执行环境的一个属性。 Daml 假设合约的利益相关者对时间有共识。

### 列表

`[a]` 是`a` 类型元素列表的内置数据类型。空列表由 `[]` 表示，`[1, 3, 2]` 是 `[Int]` 类型列表的示例。

您还可以使用 `[]` （空列表）和 `::` （这是一个将元素附加到列表前面的运算符）来构造列表。例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
twoEquivalentListConstructions =
  script do
    assert ( [1, 2, 3] == 1 :: 2 :: 3 :: [] )
```

#### 总结一个列表

要对列表求和，请使用 *fold* （因为 Daml 中没有循环）。详情请参阅`daml-ref-folding`。

### 记录和记录类型

您使用 `data` 和 `with` 关键字声明新的记录类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyRecord = MyRecord
  with
    label1 : type1
    label2 : type2
    ...
    labelN : typeN
  deriving (Eq, Show)
```

其中：

* `label1`、`label2`、...、`labelN` 是*标签*，在记录类型中必须是唯一的
* `type1`, `type2`, ..., `typeN` 是字段的类型

还有一种编写记录类型的替代方法：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyRecord = MyRecord { label1 : type1; label2 : type2; ...; labelN : typeN }
  deriving (Eq, Show)
```

使用`with`的格式和使用`{ }`的格式在语法上完全相同。主要区别在于，当您使用`with`时，您可以使用换行符和适当的缩进来避免分隔分号。

`deriving (Eq, Show)` 确保可以比较（使用`==`）和显示（使用`show`）数据类型。对于 `template` 字段中使用的数据类型，需要以 `deriving` 开头的行。

一般来说，除非数据类型包含函数类型（例如`Int -> Int`），否则无法比较或显示，否则添加`deriving`。

例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- This is a record type with two fields, called first and second,
-- both of type `Int`
data MyRecord = MyRecord with first : Int; second : Int
  deriving (Eq, Show)

-- An example value of this type is:
newRecord = MyRecord with first = 1; second = 2

-- You can also write:
newRecord = MyRecord 1 2
```

#### 数据构造函数

您可以使用`data`关键字来定义新的数据类型，例如`data Floor a = Floor a`用于某些类型`a`。

表达式中的第一个`Floor`是*类型构造函数*。第二个`Floor`是一个*数据构造函数*，可用于指定`Floor Int`类型的值：例如，`Floor 0`、`Floor 1`。

在 Daml 中，数据构造函数最多可以采用一个参数*。

具有零参数的数据构造函数的一个示例是`data Empty = Empty {}`。 `Empty`类型的唯一值是`Empty`。

<Note>
  在`data Confusing = Int`中，`Int`是一个不带参数的数据构造函数。与内置`Int`类型无关。
</Note>

#### 访问记录字段

要访问记录类型的字段，请使用点表示法。例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Access the value of the field `first`
val.first

-- Access the value of the field `second`
val.second
```

#### 更新记录字段

您还可以使用 `with` 关键字在现有替换选择字段的基础上创建新记录。

例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
myRecord = MyRecord with first = 1; second = 2

myRecord2 = myRecord with second = 5
```

产生新的记录值`MyRecord with first = 1; second = 5`。

如果您有一个与标签同名的变量，Daml 允许您使用它而不分配它，以使事情看起来更好：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- if you have a variable called `second` equal to 5
second = 5

-- you could construct the same value as before with
myRecord2 = myRecord with second = second

-- or with
myRecord3 = MyRecord with first = 1; second = second

-- but Daml has a nicer way of putting this:
myRecord4 = MyRecord with first = 1; second

-- or even
myRecord5 = r with second
```<Note>
  `with` 关键字比函数应用程序绑定更牢固。因此，对于函数，例如 `return`，可以写 `return IntegerCoordinate with first = 1; second = 5` 或 `return (IntegerCoordinate {first = 1; second = 5})`，其中后一个表达式括在括号中。
</Note>

#### 参数化数据类型

Daml 支持参数化数据类型。

例如，要表达 2D 坐标的更通用类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Here, a and b are type parameters.
-- The Coordinate after the data keyword is a type constructor.
data Coordinate a b = Coordinate with first : a; second : b
```

可以使用 `Coordinate` 构造的类型的示例是 `Coordinate Int Int`。

### 类型同义词

要声明类型的同义词，请使用 `type` 关键字。

例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type IntegerTuple = (Int, Int)
```

这使得 `IntegerTuple` 和 `(Int, Int)` 成为同义词：它们具有相同的类型并且可以互换使用。

您可以对任何类型使用 `type` 关键字，包括 `daml-ref-built-in-types`。

#### 函数类型

函数的类型包括其参数和结果类型。具有两个参数的函数 `foo` 具有类型 `ParamType1 -> ParamType2 -> ReturnType`。

请注意，这可以被视为任何其他类型。例如，您可以使用 `type FooType = ParamType1 -> ParamType2 -> ReturnType` 为其指定同义词。

### 代数数据类型

代数数据类型是复合类型：由其他类型组合而成的类型。枚举数据类型就是一个例子。本节介绍更强大的代数数据类型。

#### 产品类型

以下数据构造函数在 Daml 中无效：`data AlternativeCoordinate a b = AlternativeCoordinate a b`。这是因为数据构造函数只能有一个参数。

要解决此问题，请将值包装在记录中：`data Coordinate a b = Coordinate {first: a; second: b}`。

这些类型称为*产品*类型。

思考这个问题的一种方法是，`Coordinate Int Int`类型具有第一维和第二维（即二维乘积空间）。通过向记录添加额外的类型，您可以获得第三个维度，依此类推。

#### 总和类型

总和类型捕获了属于一种或另一种的概念。

一个例子是内置数据类型 `Bool`。这是由`data Bool = True | False deriving (Eq,Show)`定义的，其中`True`和`False`是零参数的数据构造函数。这意味着`Bool`值是`True`或`False`并且不能用任何其他值实例化。

请注意，您打算用作模板或choice 参数的所有类型都需要至少从 `(Eq, Show)` 派生。

一个非常有用的求和类型是`data Optional a = None | Some a deriving (Eq,Show)`。它是 Daml 标准库的一部分。

`Optional` 捕捉了盒子的概念，盒子可以是空的，也可以包含`a`类型的值。

`Optional` 是一个 sum 类型构造函数，以类型 `a` 作为参数。它生成由数据构造函数`None`和`Some`定义的和类型。

`Some` 数据构造函数采用一个参数，并且它需要 `a` 类型的值作为参数。

#### 模式匹配

您可以使用 `case` 关键字将值与特定模式匹配。

该模式用数据构造函数来表达。例如，`Optional Int`求和类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Daml.Script
import DA.Assert

optionalIntegerToText (x : Optional Int) : Text =
  case x of
    None -> "Box is empty"
    Some val -> "The content of the box is " <> show val

optionalIntegerToTextTest =
  script do
```

在 `optionalIntegerToText` 函数中，`case` 构造函数首先尝试将 `x` 参数与 `None` 数据构造函数进行匹配，如果匹配，则返回 `"Box is empty"` 文本。如果不匹配，则尝试将 `x` 与列表中的下一个模式进行匹配，即使用 `Some` 数据构造函数。如果匹配，附加到 `Some` 标签的值的内容将绑定到 `val` 变量，然后在相应的输出文本字符串中使用。请注意，case 构造中的所有模式都需要*完整*，即对于每个 `x` 必须至少有一个匹配的模式。从上到下测试模式，并且将执行第一个匹配的模式的表达式。请注意，`_` 可以用作包罗万象的模式。

您还可以使用 `True` 和 `False` 数据构造函数区分 `Bool` 变量，并实现与 if-then-else 表达式相同的行为。

作为示例，以下是 `Text` 的表达式：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}


tmp =
  let
    l = [1, 2, 3]
  in case l of
```

请注意上面嵌套模式匹配的使用。

<Note>
  使用下划线代替变量名。原因是 Daml Studio 会对所有未使用的变量生成警告。这对于检测未使用的变量很有用。您可以通过以下划线开头的变量命名来抑制警告。
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/expressions.rst" hash="ed2e9625" */}

## 参考：表达式

此页面提供未更新的 Daml 表达式的参考信息。

### 定义

使用赋值来绑定 Daml 文件顶层或合约模板主体中的值或函数。

#### 价值观

例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

-- The TubeSurfaceArea example.

module TubeSurfaceArea where


pi = 3.1415926535

tubeSurfaceArea2 (r : Decimal) (h : Decimal) : Decimal =
  2.0 * pi * r * h

tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h

tubeSurfaceArea3 = \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

`pi` 具有类型 `Decimal` 的事实是从该值推断出来的。要显式注释类型，请在变量名称后面的冒号后面提及它：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

-- The TubeSurfaceArea example.

module TubeSurfaceArea2 where

-- Type synonym for Decimal -> Decimal -> Decimal
type BinaryDecimalFunction = Decimal -> Decimal -> Decimal

pi : Decimal = 3.1415926535

tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

#### 函数

您可以定义函数。这是一个示例：用于计算管表面积的函数：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h
```

在这里你看到：

* 函数名称

* 函数的类型签名`Decimal -> Decimal -> Decimal`

  这意味着它需要两个小数并返回另一个小数。

* 定义`= 2.0 * pi * r * h`（使用之前定义的`pi`）

### 算术运算符

|操作员|适用于 |
| --------------------------------- | ------------------------ | |
| `+` | `Int`、`Decimal`、`RelTime` |
| `-` | `Int`、`Decimal`、`RelTime` |
| `*` | `Int`、`Decimal` |
| `/`（整数除法）| `Int` |
| `%`（整数求余运算）| `Int` |
| `^`（整数指数）| `Int` |

模运算的结果与被除数具有相同的符号：

* `7 / 3` 和 `(-7) / (-3)` 计算为 `2`
* `(-7) / 3` 和 `7 / (-3)` 计算为 `-2`
* `7 % 3` 和 `7 % (-3)` 计算为 `1`
* `(-7) % 3` 和 `(-7) % (-3)` 计算为 `-1`

要以前缀形式编写中缀表达式，请将运算符括在括号中。例如，`(+) 1 2`是`1 + 2`的另一种写法。

### 比较运算符|操作员|适用于 |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `<`、`<=`、`>`、`>=` | `Bool`、`Text`、`Int`、`Decimal`、`Party`、`Time` |
| `==`、`/=` | `Bool`、`Text`、`Int`、`Decimal`、`Party`、`Time`以及源自同一合约模板的合约标识符 |

### 逻辑运算符

Daml 中的逻辑运算符有：

* `not` 表示否定，例如 `not True == False`
* `&&` 为合取，其中 `a && b == and a b`
* `||` 用于析取，其中 `a || b == or a b`

对于`Bool`变量`a`和`b`。

### 如果-那么-否则

您可以使用条件 *if-then-else* 表达式，例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
if owner == scroogeMcDuck then "sell" else "buy"
```

###让

要将值或函数绑定到表达式下方的范围内，请使用 block 关键字 `let`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
doubled =
  -- let binds values or functions to be in scope beneath the expression
  let
    double (x : Int) = 2 * x
    up = 5
  in double up
```

您还可以在 `do` 块内使用 `let`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
blah = script
  do
    let
      x = 1
      y = 2
      -- x and y are in scope for all subsequent expressions of the do block,
      -- so can be used in expression1 and expression2.
    expression1
    expression2
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/functions.rst" hash="2a0983ac" */}

## 参考：函数

此页面提供有关 Daml 中函数的参考信息。

Daml 是一种函数式语言。它允许您部分应用函数，并且还可以具有将其他函数作为参数的函数。本页讨论这些*高阶函数*。

### 定义函数

在`expressions`中，`tubeSurfaceArea`函数定义为：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h
```

您可以使用 lambda 等效地定义此函数，包括 `\`、参数序列和箭头 `->`，如下所示：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

### 部分应用

前面描述的`tubeSurfaceArea`函数的类型是`Decimal -> Decimal -> Decimal`。一种等效但更具指导意义的读取其类型的方法是： `Decimal -> (Decimal -> Decimal)`：表示 `tubeSurfaceArea` 是一个接受*一个*参数并返回另一个函数的函数。

因此，`tubeSurfaceArea`需要一个`Decimal`类型的参数，并返回一个`Decimal -> Decimal`类型的函数。换句话说，这个函数返回另一个函数。 *只有最后一次应用参数才会产生非函数。*

这称为“柯里化”：柯里化是将多个参数的函数转换为仅采用单个参数并返回另一个函数的函数的过程。在 Daml 中，所有函数都是柯里化的。

这对事情影响不大。如果您以经典方式使用函数（将它们应用于所有参数），那么没有什么区别。

如果您只对函数应用几个参数，这称为*部分应用*。结果是一个带有部分定义参数的函数。例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
multiplyThreeNumbers : Int -> Int -> Int -> Int
multiplyThreeNumbers xx yy zz =
  xx * yy * zz

multiplyTwoNumbersWith7 = multiplyThreeNumbers 7

multiplyWith21 = multiplyTwoNumbersWith7 3

multiplyWith18 = multiplyThreeNumbers 3 6
```

您还可以定义等效的 lambda 函数：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
multiplyWith18_v2 : Int -> Int
multiplyWith18_v2 xx =
  multiplyThreeNumbers 3 6 xx
```

### 函数就是值

函数类型可以显式添加到 `tubeSurfaceArea` 函数中（当使用 lambda 表示法编写时）：```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Type synonym for Decimal -> Decimal -> Decimal
type BinaryDecimalFunction = Decimal -> Decimal -> Decimal

pi : Decimal = 3.1415926535

tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

请注意，`tubeSurfaceArea : BinaryDecimalFunction = ...` 遵循与绑定值时相同的模式，例如 `pi : Decimal = 3.14159265359`。

函数有类型，就像值一样。这意味着它们可以像普通变量一样使用。事实上，在Daml中，函数就是值。

这意味着一个函数可以接受另一个函数作为参数。例如，定义一个函数 `applyFilter: (Int -> Int -> Bool) -> Int -> Int -> Bool`，它将第一个参数（高阶函数）应用于第二个和第三个参数以产生结果。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
applyFilter (filter : Int -> Int -> Bool)
    (x : Int)
    (y : Int) = filter x y

compute = script do
    applyFilter (<) 3 2 === False
    applyFilter (/=) 3 2 === True

    round (2.5 : Decimal) === 3
    round (3.5 : Decimal) === 4

    explode "me" === ["m", "e"]

    applyFilter (\a b -> a /= b) 3 2 === True
```

`daml-ref-folding` 部分研究了两个有用的内置函数 `foldl` 和 `foldr`，它们也将函数作为参数。

<Note>
  Daml 不允许函数作为合约模板和合约选择的参数。但是，后续选择可以使用在顶层或合约模板主体中定义的内置函数。
</Note>

### 通用函数

如果一个函数对于所有类型（至少在其一个类型参数中）表现一致，则该函数是“参数多态”的。例如，您可以按如下方式定义函数组合：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
compose (f : b -> c) (g : a -> b) (x : a) : c = f (g x)
```

其中 `a`、`b` 和 `c` 是任意数据类型。 `compose ((+) 4) ((*) 2) 3 == 10` 和`compose not ((&&) True) False` 的计算结果均为`True`。请注意，`((+) 4)` 具有类型 `Int -> Int`，而 `not` 具有类型 `Bool -> Bool`。

您可以在 Daml 标准库中找到许多其他通用函数，包括这个函数。

<Note>
  Daml 目前不支持特定类型集的通用函数，例如 `Int` 和 `Decimal` 数字。例如，当 `a` 等于类型 `Party` 时，`sum (x: a) (y: a) = x + y` 未定义。 *有界多态性*可能会在后续版本中添加到 Daml 中。
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/file-struct.rst" hash="4bb0b27c" */}

##参考：Daml文件结构

此页面提供有关模板之外的 Daml 文件结构的参考信息。

### 文件结构

* 该文件的模块名称（`module NameOfThisFile where`）。

  分层模块系统的一部分，以促进代码重用。必须与 Daml 文件名相同，不带文件扩展名。

  对于路径为 `./Scenarios/Demo.daml` 的文件，请使用 `module Scenarios.Demo where`。

### 进口

* 您可以导入其他模块（`import OtherModuleName`），包括合格的导入（`import qualified AndYetOtherModuleName`、`import qualified AndYetOtherModuleName as Signifier`）。不能有循环导入引用。
* 要导入`./Prelude.daml`的`Prelude`模块，请使用`import Prelude`。
* 要导入`./Scenarios/Demo.daml`的模块，请使用`import Scenarios.Demo`。
* 如果省略 `qualified`，并且指定了模块别名，则导入模块的顶级声明将导入到模块的命名空间以及给定别名指定的命名空间中。

### 图书馆

Daml 库是相关 Daml 模块的集合。

使用 `LibraryModules.daml` 文件定义 Daml 库：导入库根模块的普通 Daml 文件。该库由 `LibraryModules.daml` 文件及其所有依赖项组成，通过递归跟踪每个模块的导入来找到。

Daml Studio 中按每个库报告错误。这意味着即使文件未显式打开，也会显示共享 Daml 模块上的重大更改。

### 评论

使用 `--` 进行单行注释。使用 `{-` 和 `-}` 进行多行注释。

### 合约标识符当模板的实例（即合约）添加到分类帐时，它会被分配一个类型为 `ContractId <name of template>` 的唯一标识符。

这些标识符的运行时表示取决于执行环境：沙盒中的合约标识符可能与其他 Daml 账本上的合约标识符不同。

您可以在相同类型的合约标识符上使用`==`和`/=`。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/packages.rst" hash="4011d059" */}

## 参考：Daml 包

此页面提供有关 Daml 包依赖项的参考信息。

### 建立 Daml 档案

当编译 Daml 项目时，编译器会生成一个`Daml archive`。这些是已编译的 Daml 代码的独立于平台的包，可以上传到 Daml 分类帐或导入到其他 Daml 项目中。

Daml 存档的文件结尾为 `.dar`。默认情况下，运行`dpm build`时，会在项目根文件夹的`.daml/dist`文件夹中生成`.dar`文件。例如，在项目版本为 `0.0.1` 的项目 `foo` 中运行 `dpm build` 将生成 Daml 存档 `.daml/dist/foo-0.0.1.dar`。

您可以使用 `-o` 标志为 Daml 存档指定不同的路径：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build -o foo.dar

The rest of this page will focus on how to import a Daml package in other Daml projects.
```

### 检查 DAR

请参阅有关解码 DAR 和 DALF 文件的部分。

### 导入 Daml 包

在项目中导入Daml包有两种方法：通过`dependencies`和通过`data-dependencies`。它们各有一定的优点和缺点。总结一下：

* `dependencies` 允许您将 Daml 存档导入为库。依赖项中的定义将全部可供导入项目使用。但依赖必须使用相同的 SDK 版本进行编译，因此这种方法只适合将大项目分解为相互依赖的小项目，或者重用现有的库。
* `data-dependencies` 允许您导入 Daml 存档 (.dar) 或 Daml-LF 包 (.dalf)，包括已部署到分类帐的包。这些包可以使用任何以前的 SDK 版本进行编译。另一方面，并​​非所有定义都可以完美地继承，因为 Daml 接口需要从二进制文件重建。

以下部分将更深入地介绍这两种方法。

#### 通过 Dependency 导入 Daml 包

Daml 项目可以将 Daml 存档声明为 `daml.yaml` 的 `dependencies` 字段中的依赖项。这使您可以导入模块并重用另一个 Daml 项目中的定义。此方法的主要限制是必须为与导入项目相同的 SDK 版本构建依赖项。

让我们看一个例子。假设您有一个位于 `/home/user/foo` 的现有 Daml 项目 `foo`，并且您希望将其用作位于 `/home/user/bar` 的项目 `bar` 中的依赖项。

为此，您首先需要生成`foo`的Daml存档。进入`/home/user/foo`并运行`dpm build -o foo.dar`。这将创建 Daml 存档，`/home/user/foo/foo.dar`。

接下来，我们将更新 `bar` 的项目配置，以使用生成的 Daml 存档作为依赖项。进入`/home/user/bar`，将`daml.yaml`中的`dependencies`字段更改为指向创建的\`Daml archive\`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
  - daml-prim
  - daml-stdlib
  - ../foo/foo.dar
```

导入路径也可以是绝对路径，例如，将最后一行更改为：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
- /home/user/foo/foo.dar
```

当您在`bar`项目中运行`dpm build`时，编译器将使`foo.dar`中的定义可供导入。例如，如果`foo`导出模块`Foo`，则可以按照通常的方式导入它：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Foo
```

默认情况下，当将 `foo` 作为依赖项导入时，`foo` 的所有模块都可用。要限制导出哪些`foo`模块，您可以在`daml.yaml`文件中为`foo`添加`exposed-modules`字段：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
exposed-modules:
- Foo
```

#### 通过 `data-dependencies` 导入 Daml 存档您可以使用 `data-dependencies` 导入 Daml 存档 (.dar) 或 Daml-LF 包 (.dalf)。与`dependencies`不同，当SDK版本不匹配时可以使用此功能。

例如，您可以按如下方式导入`foo.dar`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- ../foo/foo.dar
```

当以这种方式导入包时，Daml 编译器将尝试从编译的二进制文件重建原始的 Daml 接口。然而，为了让`data-dependencies`能够跨SDK版本工作，编译器必须抽象出一些跨SDK版本不兼容的细节。这意味着使用`data-dependencies`时，有些Daml功能无法恢复。特别是：

1.导出列表无法恢复，因此通过`data-dependencies`导入可以访问原来隐藏的定义。这意味着导入模块需要尊重原始模块的数据抽象。请注意，这对于在分类帐上运行的所有代码都是相同的，因为分类帐不提供对数据抽象的特殊支持。
2. 如果您有一个 `dependency` 限制了可以通过 `exposed-modules` 访问的模块，并且您还有一个 `data-dependency` 引用了隐藏模块中的某些内容（即使只是重新导出），则可能会出现错误。由于`exposed-modules`一般在账本上不可用，我们建议不要使用它们，而是依靠命名约定（例如，在模块名称后缀`.Internal`）来明确哪些模块是公共API的一部分。
3. 在Daml-LF 1.8版本之前，类型类无法重建。这意味着，如果您有一个使用旧版本的 Daml-LF 编译的包，类型类和类型类实例将不会通过数据依赖项进行继承，并且您将无法调用依赖于类型类实例的函数。这包括模板函数，例如 `create`、`signatory` 和 `exercise`，因为它们依赖于类型类实例。
4. 从Daml-LF 1.8版本开始，在可能的情况下，将通过重用依赖项中的类型类定义来重建类型类实例，例如`daml-stdlib`中导出的类型类。但是，如果类型类签名已更改，您将获得重建类型类的实例，该实例不会与依赖项中的代码进行互操作。

#### 传递依赖管理

Daml 编译器通过其 `packageId` 和完全限定名称（Daml 项目包名称和版本号）来标识项目中的每个 DAR 依赖项。

如果您的 Daml 项目包含多个常见的传递 DAR 依赖项，那么这些常见的传递依赖项必须：

* 如果它们在 Daml 项目的 `daml.yaml` 文件中指定了相同的名称和版本，则具有相同的内容，或者
* 在各自的 `daml.yaml` 文件中，`version` 条目具有不同的值。

否则，由于包标识冲突，Daml 项目无法构建到可部署的 DAR 中。

例如：

* Daml 项目 X（顶级）具有依赖项 `DarA` 和 `DarB`。
* `DarA`和`DarB`都包含DAR依赖`DarC`

编译Daml项目X时，必须确保`DarA`和`DarB`引用的`DarC`依赖具有相同的Daml内容，或者如果内容不同，则版本号不同。版本号在生成 `DarC` 的 Daml 项目的 daml.yaml 文件中定义，位于 `version` 键下。

#### 参考 Daml 包已在 Ledger 上

如果您拥有下载这些包的必要权限，则可以将已上传到分类帐的 Daml 包作为数据依赖项导入。要导入此类包，请将用冒号分隔的包名称和版本添加到数据依赖项节中，如下所示：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
ledger:
  host: localhost
  port: 6865
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- foo:1.0.0
```

如果您的账本在默认主机和端口（`localhost:6865`）上运行，则可以省略账本节。这将获取并安装包`foo-1.0.0`。将在项目目录的根目录下创建一个 `daml.lock` 文件，将已解析的包固定到其确切的包 ID：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
- pkgId: 51255efad65a1751bcee749d962a135a65d12b87eb81ac961142196d8bbca535
  name: foo
  version: 1.0.0
```

`daml.lock` 文件需要签入项目的版本控制中。这可确保数据依赖项中指定的包名称/版本元组始终解析为相同的包 ID。要重新创建或更新您的 `daml.lock` 文件，请将其删除并再次运行 `dpm build`。

### 处理模块名称冲突

有时您会有多个具有相同模块名称的包。在这种情况下，简单的导入将会失败，因为编译器不知道要加载哪个版本的模块。幸运的是，您可以使用一些工具来解决这个问题。

第一种是使用包合格的导入。假设您有不同名称的包，`foo`和`bar`，它们都公开了一个模块`X`，您可以通过包限定导入来选择您想要的模块。

从`foo`得到`X`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "foo" X
```

从`bar`得到`X`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "bar" X
```

要获得两者，您需要在执行导入时重命名模块：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "foo" X as FooX
import "bar" X as BarX
```

有时，包限定导入不会有帮助，因为您正在导入两个同名的包。例如，如果您正在加载同一包的不同版本。要处理这种情况，您需要 `--package` 构建选项。

假设您要导入包 `foo-1.0.0` 和 `foo-2.0.0`。请注意，它们具有相同的名称`foo`，但版本不同。要获取两个包中公开的模块，您需要提供模块别名。您可以通过传递 `--package` 构建选项来做到这一点。打开`daml.yaml`并添加以下`build-options`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
build-options:
- '--package'
- 'foo-1.0.0 with (X as Foo1.X)'
- '--package'
- 'foo-2.0.0 with (X as Foo2.X)'
```

这会将`foo-1.0.0`中的`X`别名为`Foo1.X`，并将`foo-2.0.0`中的`X`别名为`Foo2.X`。现在您将能够使用新名称导入两个 `X`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import qualified Foo1.X
import qualified Foo2.X
```

还可以使用 `daml.yaml` 中的 `module-prefixes` 字段为包中的所有模块添加前缀。这对于升级特别有用，您可以将软件包版本 `v` 的所有模块映射到 `V$v` 下。对于上面的示例，您可以使用以下内容：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
module-prefixes:
  foo-1.0.0: Foo1
  foo-2.0.0: Foo2
```

这将允许您从包`foo-1.0.0`导入模块`X`作为`Foo1.X`，并从包`foo-2.0.0`作为`Foo2`导入模块`X`。

您还可以使用更复杂的模块前缀，例如，`foo-1.0.0: Foo1.Bar`，这将使模块`X`在`Foo1.Bar.X`下可用。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/contract-keys.rst" hash="85971992" */}

## 参考：合约密钥

<Warning>
  Canton 3.5 版本中将提供合约密钥。该文档将在那时更新。
</Warning>

### 不支持的功能

合约密钥是模板的可选补充。它们允许您使用模板参数指定唯一标识合约的方法 - 类似于数据库的主键。

合约密钥不会改变，即使合约 ID 发生变化，也可以用来引用合约。

以下是为银行账户设置合约密钥以充当银行账户 ID 的示例：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AccountKey = (Party, Text)

template Account with
    bank : Party
    number : Text
    owner : Party
    balance : Decimal
    observers : [Party]
  where
    signatory [bank, owner]
    observer observers

    key (bank, number) : AccountKey
    maintainer key._1
```

### 什么可以是合约密钥

键可以是不包含合约 ID 的任意可序列化表达式。但是，它**必须**包含您想要用作 `maintainer` 的每一方（请参阅下面的[指定维护者](#specify-maintainers)）。最好对键使用简单类型，例如 `Text` 或 `Int`，而不是列表或更复杂的类型。

### 指定维护者

如果为模板指定合约密钥，则还必须指定`maintainer`或维护者，与指定签署者或观察者类似。维护者“拥有”密钥，就像签名者“拥有”合约一样。就像合约签署者防止双重支出或使用虚假合约数据一样，密钥维护者也防止双重分配或不正确的查找。由于密钥是合约的一部分，因此维护者**必须**是合约的签署人。但是，维护者是根据 `key` 而不是模板参数计算的。在上面的例子中，`bank`最终是密钥的维护者。

每个模板保证键的唯一性。由于多个模板可能使用相同的密钥类型，因此一些与密钥相关的函数必须使用`@ContractType`进行注释，如下例所示。

当您编写 Daml 模型时，维护者很重要，因为他们会影响授权——就像签名者和观察者一样。您不需要执行任何操作来“维护”密钥。在上面的例子中，保证在给定的`bank`处只能存在一个具有给定`number`的`Account`。

密钥的检查是在执行时由 Daml 执行引擎自动完成的：如果有人尝试创建一个复制现有合约密钥的新合约，执行引擎将导致该创建失败。

### 合约查找

合约密钥的主要目的是提供一个稳定且可能有意义的标识符，可在 Daml 中使用该标识符来获取合约。有两个函数可以执行此类查找：`fetchbykey` 和 `lookupbykey`。两种类型的查找都是在解释时在提交的参与者节点上尽最大努力执行的。目前，这种尽力意味着查找仅返回合约（如果提交方是该合约的利益相关者）。

特别是，上述意味着如果同时提交多个命令，所有命令都使用合约查找来查找并使用给定的合约，那么这些命令之间将会出现争用，并且最多一个会成功。有关更多信息，请参阅避免 [争用]() 部分。

限制利益相关者使用密钥还意味着密钥不能用于访问泄露的合约，即可能存在`fetch`成功而`fetchByKey`不成功的情况。有关详细信息，请参阅本节末尾的示例。

#### fetchByKey

`(fetchedContractId, fetchedContract) <- fetchByKey @ContractType contractKey`

使用`fetchByKey`获取指定key的合约ID和数据。它是 `fetch` 的替代品，并且在大多数方面表现相同。

它返回 ID 和合约对象（包含其所有数据）的元组。

与`fetch`一样，`fetchByKey`需要至少一位利益相关者的授权。

如果出现以下情况，`fetchByKey` 将失败并中止事务：

* 提交方不是具有给定密钥的合约的利益相关者，或者
* 找到了合约，但`fetchByKey`违反了授权规则，即没有利益相关者授权`fetch`。

这意味着如果失败，并不能保证具有该密钥的合约不存在，只是提交方不知道它，或者存在授权问题。

####visibleByKey

`boolean <- visibleByKey @ContractType contractKey`

使用`visibleByKey`检查您是否可以看到具有当前授权的给定密钥的活动合约。如果合约存在并且您有权查看它，则返回`True`，否则返回`False`。

为了澄清，忽略争论：1. 如果所有这些都为真，则`visibleByKey`将返回`True`：给定密钥存在合约，提交者是该合约的利益相关者，并且在调用时我们拥有该密钥的**所有**维护者的授权。
2. 如果所有这些都为真，`visibleByKey` 将返回`False`：给定密钥没有合约，并且在调用时我们获得了密钥的**所有**维护者的授权。
3. 如果在调用时我们缺少任何一位密钥维护者的授权，`visibleByKey` 将在解释时中止交易。
4. 如果所有这些都为真，`visibleByKey`将在验证时失败（在解释时返回`False`之后）：在调用时，我们拥有**所有**维护者的授权，并且给定密钥存在有效的合约，但提交者不是该合约的利益相关者。

虽然乍一看似乎限制性太强，要求**所有**维护者授权调用，但这实际上是验证负查找所必需的。在积极的情况下，当您可以看到合约时，交易很容易提及它找到了哪个合约，因此验证器可以检查该合约是否确实存在，并且在执行交易时处于活动状态。

然而，对于负面情况，提交执行的交易不能说它没有找到*哪个*合约（因为根据定义，它还没有找到它，甚至可能不存在）。尽管如此，验证者必须能够重现找不到合约的结果，因此他们需要能够寻找它，这意味着有权向维护者询问它。

#### 通过键查找

`optionalContractId <- lookupByKey @ContractType contractKey`

使用`lookupByKey`检查指定密钥的合约是否存在。如果存在，`lookupByKey`返回`Some contractId`，其中`contractId`是合约的ID；否则，返回`None`。

`lookupByKey` 在概念上等同于

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookupByKey : forall c k. (HasFetchByKey c k) => k -> Update (Optional (ContractId c))
lookupByKey k = do
  visible <- visibleByKey @c k
  if visible then do
    (contractId, _ignoredContract) <- fetchByKey @c k
    return $ Some contractId
  else
    return None
```

因此，出于相同的原因，`lookupByKey` 需要与 `visibleByKey` 相同的授权，并在相同的情况下失败。

在确认合约存在后，要从合约中获取数据，您仍然需要使用`fetch`。

### 练习按键

`exerciseByKey @ContractType contractKey`

使用 `exerciseByKey` 对由 `key` 标识的合约行使选择权（与 `exercise` 相比，`exercise` 允许您行使由 `ContractId` 标识的合约）。就像`exercise`一样，运行`exerciseByKey`需要合约的可见性（通过泄露、`readAs`或成为利益相关者）以及所选择的控制者的授权。

### 示例

下面显示了`fetchByKey`和`lookupByKey`可能成功和失败场景的完整示例。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- 版权所有 (c) 2025 Digital Asset (Switzerland) GmbH 和/或其附属公司。版权所有。
-- SPDX 许可证标识符：Apache-2.0

模块键在哪里

导入 Daml.Script
导入DA.Assert
导入DA.可选

模板键控
  与
    签名：派对
    对象：聚会
  哪里
    签字人
    观察者观测站

    关键标志：派对
    维护者密钥

模板泄露者
  与
    泄露者：派对
    签名：派对
  哪里
    签署人披露
    观察员信号

    非消费 choice DivulgeKeyed
      ： 有键
      与
        keyedCid : ContractId 键控
      控制器信号
      做
        获取 keyedCid

模板委托
  与
    签名：派对
    代表们：[当事人]
  哪里
    签字人
    观察员学员

    非消耗选择 CreateKeyed
      : ContractId 键控
      与
        受托人：聚会
        对象：聚会
      控制员委托人
      做
        使用 sig 创建 Keyed；观测值

    非消耗性选择 ArchiveKeyed
      ：（）
      与
        受托人：聚会
        keyedCid : ContractId 键控
      控制员委托人
      做
        存档 keyedCid非消耗选择UnkeyedFetch
      ： 有键
      与
        cid ：合约 ID 键控
        受托人：聚会
      控制员委托人
      做
        获取用户ID

    非消耗性选择 VisibleKeyed
      : 布尔
      与
        关键词 : 派对
        受托人：聚会
      控制员委托人
      做
        visibleByKey @Keyed 密钥

    非消耗选择 LookupKeyed
      ：可选（ContractId 键控）
      与
        查找键：派对
        受托人：聚会
      控制员委托人
      做
        LookupByKey @Keyed LookupKey

    非消耗性选择 FetchKeyed
      ：（ContractId 键控，键控）
      与
        查找键：派对
        受托人：聚会
      控制员委托人
      做
        fetchByKey @Keyed LookupKey

模板助手
  与
    p：聚会
  哪里
    签署人p

    选择 FetchByKey : (ContractId Keyed, Keyed)
      与
        keyedKey : 派对
      控制器p
      做 fetchByKey @Keyed keyedKey

    选择 VisibleByKey : Bool
      与
        keyedKey : 派对
      控制器p
      做visibleByKey @Keyed keyedKey

    选择 LookupByKey ：（可选（ContractId 键控））
      与
        keyedKey : 派对
      控制器p
      执行lookupByKey @Keyed keyedKey

    选择 AssertNotVisibleKeyed : ()
      与
        delegateCid : ContractId 委托
        受托人：聚会
        关键词 : 派对
      控制器p
      做
        b <- 练习 delegateCid VisibleKeyed with
          受托人
          钥匙
        断言 $ 不是 b

    选择 AssertLookupKeyedIsNone : ()
      与
        delegateCid : ContractId 委托
        受托人：聚会
        查找键：派对
      控制器p
      做
        b <- 练习 delegateCid LookupKeyed with
          受托人
          查找键
        断言 $ isNone b

    选择 AssertFetchKeyedEqExpected : ()
      与
        delegateCid : ContractId 委托
        受托人：聚会
        查找键：派对
        ExpectedCid : ContractId 键控
      控制器p
      做
        (cid, keyed) <- 练习委托Cid FetchKeyed with
          受托人
          查找键
        cid === 预期Cid


LookupTest = 脚本执行

  -- 将四方放入 `Keyed` 的四种可能关系中
  sig <- allocateParty "s" -- 签名者
  obs <- allocateParty "o" -- 观察者
  divulgee <- allocateParty "d" -- Divulgee
  盲 <- allocateParty "b" -- 盲

  keyedCid <- 提交 sig do createCmd 键控为 ..
  divulgercid <- 提交 divulgee do createCmd Divulger with ..
  提交 sig doexerciseCmd divulgercid DivulgeKeyed with ..

  -- 现在签字人和观察员代表他们的选择
  sigDelegationCid <- 提交 sig do
    createCmd 委托与
      信号
      delegees = [obs、泄露、盲人]
  obsDelegationCid <- 提交 obs do
    createCmd 委托与
      信号= OB
      delegees = [泄露者，盲人]

  -- 测试查找和获取

  -- 维护者可以获取
  (cid, keyed) <- 提交 sig do
    帮助程序 sig `createAndExerciseCmd` FetchByKey sig
  cid === keyedCid
  -- 维护者可以看到
  b <- 提交 sig do
    助手 sig `createAndExerciseCmd` VisibleByKey sig
  断言 b
  -- 维护者可以查找
  mcid <- 提交 sig do
    助手 sig `createAndExerciseCmd` LookupByKey sig
  mcid === 一些 keyedCid


  -- 利益相关者可以获取
  (cid, l) <- 提交 obs do
    辅助 obs `createAndExerciseCmd` FetchByKey sig
  keyedCid === cid
  -- 利益相关者未经授权无法查看
  提交必须失败 obs do
    辅助 obs `createAndExerciseCmd` VisibleByKey sig

  -- 利益相关者授权即可查看
  b <- 提交 obs 做
    运动Cmd sigDelegationCid VisibleKeyed with
      受托人 = obs
      密钥=签名
  断言 b
  -- 利益相关者未经授权不得查询
  提交必须失败 obs do
    辅助 obs `createAndExerciseCmd` LookupByKey sig
  -- 利益相关者授权即可查询
  mcid <- 提交 obs do
    运动Cmd sigDelegationCid Lookup键入
      受托人 = obs
      查找键 = sig
  mcid === 一些 keyedCid-- Divulgee 无法直接获取合约
  提交必须失败，泄露信息
    运动Cmd obsDelegationCid UnkeyedFetch with
        受托人 = 泄露者
        cid = keyedCid
  -- Divulgee 无法通过密钥获取
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` FetchByKey sig
  -- Divulgee 看不见
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` VisibleByKey sig
  -- Divulgee 看不到利益相关者的权威
  提交必须失败，泄露信息
    运动Cmd obsDelegationCid VisibleKeyed with
        受托人 = 泄露者
        密钥=签名
  -- Divulgee 无法查找
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` LookupByKey sig
  -- Divulgee 无法通过利益相关者权限进行查找
  提交必须失败，泄露信息
    运动Cmd obsDelegationCid Lookup键入
        受托人 = 泄露者
        查找键 = sig
  -- Divulgee 无法使用维护者权限进行正向查找。
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegateCid = sigDelegationCid
      受托人 = 泄露者
      密钥=签名
  -- Divulgee 无法使用维护者权限进行正向查找。
  -- 请注意，查找返回`None`，因此断言通过。
  -- 如果断言改为`isSome`，则断言失败，
  -- 这意味着错误消息发生了变化。原因是，
  -- 在解释时、查找之前检查断言
  -- 在验证时检查。
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` AssertLookupKeyedIsNone 与
      delegateCid = sigDelegationCid
      受托人 = 泄露者
      查找键 = sig
  -- Divulgee 无法以利益相关者的权限获取
  提交必须失败，泄露信息
    帮助者泄露 `createAndExerciseCmd` AssertFetchKeyedEqExpected with
      delegateCid = obsDelegationCid
      受托人 = 泄露者
      查找键 = sig
      预期Cid = keyedCid

  -- 盲方无法获取
  盲目提交MustFail
    辅助盲`createAndExerciseCmd` FetchByKey sig
  ——盲人看不到
  盲目提交MustFail
    盲人助手 `createAndExerciseCmd` VisibleByKey sig
  ——盲人看不到利益相关者的权威
  盲目提交MustFail
    运动Cmd obsDelegationCid VisibleKeyed with
      受托人=盲人
      密钥=签名
  -- 盲人看不到维护者的权限
  盲目提交MustFail
    辅助盲 `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegateCid = sigDelegationCid
      受托人=盲人
      密钥=签名
  -- 盲人无法查找
  盲目提交MustFail
    辅助盲`createAndExerciseCmd` LookupByKey sig
  -- 盲方无法利用利益相关者的权限进行查找
  盲目提交MustFail
    运动Cmd obsDelegationCid Lookup键入
      受托人=盲人
      查找键 = sig
  -- 盲人无法使用维护者权限进行查找。
  -- 查找最初返回`None`，但在以下位置被拒绝
  -- 验证时间
  盲目提交MustFail
    辅助盲 `createAndExerciseCmd` AssertLookupKeyedIsNone 与
      delegateCid = sigDelegationCid
      受托人=盲人
      查找键 = sig
  -- 盲方无法使用涉众权限进行获取，因为查找结果是否定的
  盲目提交MustFail
    运动Cmd obsDelegationCid FetchKeyed with
      受托人=盲人
      查找键 = sig
  -- 盲人可以看到合约不存在
  提交盲做
    辅助盲 `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegateCid = obsDelegationCid
      受托人=盲人
      键 = 观测值
  -- Blind 可以对真正不存在的合约进行否定查找
  提交盲做
    辅助盲 `createAndExerciseCmd` AssertLookupKeyedIsNone 与
      delegateCid = obsDelegationCid
      受托人=盲人
      查找键 = obs

  -- 测试创建和存档

  -- Divulgee 无法存档
  提交必须失败，泄露信息
    运动Cmd sigDelegationCid ArchiveKeyed with
      受托人 = 泄露者
      键控Cid

  提交签名
     exerciseCmd keyedCid 存档

  -- Divulgee 可以创建
  keyedCid2 <- 提交泄露信息
    运动Cmd sigDelegationCid CreateKeyed with
      受托人 = 泄露者
      观测值

  -- 利益相关者可以存档
  提交 obs 做
    运动Cmd sigDelegationCid ArchiveKeyed with
      受托人 = obs
      keyedCid = keyedCid2
  -- 利益相关者可以创建
  keyedCid3 <- 提交 obs 执行
    运动Cmd sigDelegationCid CreateKeyed with
      受托人 = obs
      观测值返回（）
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/interfaces.rst" hash="fdeb13bb" */}

## Reference: Interfaces

In Daml, an interface defines an abstract type together with a behavior specified by its view type, method signatures, and choices. For a template to conform to this interface, there must be a corresponding `interface instance` definition where all the methods of the interface (including the special `view` method) are implemented. This allows decoupling such behavior from its implementation, so other developers can write applications in terms of the interface instead of the concrete template.

### Configuration

To use this feature your Daml project must target Daml-LF version `1.15` or higher, which is the current default.

If using Canton, the protocol version of the sync domain should be `4` or higher, see Canton protocol version for more details.

### Interface Declaration

An interface declaration is somewhat similar to a template declaration.

#### Interface Name

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
接口 MyInterface 其中
```

* This is the name of the interface.
* It's preceded by the keyword `interface` and followed by the keyword `where`.
* It must begin with a capital letter, like any other type name.

#### Implicit abstract type

* Whenever an interface is defined, an abstract type is defined with the same name. "Abstract" here means:
  * Values of this type cannot be created using a data constructor. Instead, they are constructed by applying the function `toInterface` to a template value.
  * Values of this type cannot be inspected directly via case analysis. Instead, use functions such as `fromInterface`.
  * See `daml-ref-interface-functions` for more information on these and other functions for interacting with interface values.
* An interface value carries inside it the type and parameters of the template value from which it was constructed.
* As for templates, the existence of a local binding `b` of type `I`, where `I` is an interface does not necessarily imply the existence on the ledger of a contract with the template type and parameters used to construct `b`. This can only be assumed if `b` the result of a fetch from the ledger within the same transaction.

#### Interface Methods

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
方法一：聚会
方法2：整数
方法3：布尔 -> Int -> Int -> Int
```

* An interface may define any number of methods.
* A method definition consists of the method name and the method type, separated by a single colon `:`. The name of the method must be a valid identifier beginning with a lowercase letter or an underscore.
* A method definition introduces a top level function of the same name:
  * If the interface is called `I`, the method is called `m`, and the method type is `M` (which might be a function type), this introduces the function `m : I -> M`:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
<DamlInterfacesINTERFACEMETHODSTOPLEVEL />
```

* The first argument's type `I` means that the function can only be applied to values of the interface type `I` itself. Methods cannot be applied to template values, even if there exists an `interface instance` of `I` for that template. To use an interface method on a template value, first convert it using the `toInterface` function.

* Applying the function to such argument results in a value of type `M`, corresponding to the implementation of `m` in the interface instance of `I` for the underlying template type `t` (the type of the template value from which the interface value was constructed).

* One special method, `view`, must be defined for the viewtype. (see `interface-viewtype` below).

#### Interface View Type

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
数据 MyInterfaceViewType =
  MyInterfaceViewType { 名称：文本，值：Int }
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
视图类型 MyInterfaceViewType
````

* 所有接口实例必须实现一个特殊的`view`方法，该方法返回`viewtype`声明的类型的值。
* 类型必须是记录。
* 该类型由接口上的订阅返回。

#### 接口选择```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

* 界面选择的工作方式与模板选择非常相似。任何存在接口实例的模板类型合约都会将选择权授予控制方。
* 接口选择只能针对相应接口类型的值进行。要对模板值执行接口选择，请首先使用 `toInterface` 函数对其进行转换。
* 接口方法可用于定义选择的控制器（例如`method1`）以及*执行选择*时运行的操作（例如`method2`和`method3`）。
* 对于模板选择，`choice`关键字可以选择性地加上`nonconsuming`关键字作为前缀，以指定在执行选择时合约不会被消耗。如果没有指定，则选择`consuming`。请注意，接口选择不支持 `preconsuming` 和 `postconsuming` 限定符。
* 有关完整参考信息，请参阅`choices`，但请注意接口选择不支持控制器优先语法。

#### 空接口

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data EmptyInterfaceView = EmptyInterfaceView {}

interface YourInterface where
  viewtype EmptyInterfaceView
```

* 可以（尽管不一定有用）定义一个没有方法、前提条件或选择的接口。但是，尽管可以将视图类型设置为单位，但必须始终定义视图类型。

### 接口实例

对于上下文，一个简单的模板定义：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    field1 : Party
    field2 : Int
  where
    signatory field1
```

#### `interface instance` 条款

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

* 要使模板成为现有接口的实例，必须在模板声明中定义`interface instance`子句。
* 子句的模板必须与随附的声明相匹配。换句话说，模板`T`声明只能包含模板为`T`的`interface instance`子句。
* 该子句必须以关键字`interface instance`开头，然后是接口名称，然后是关键字`for`和模板名称，最后是关键字`where`，它引入了一个必须实现接口的**所有**方法的块。
* 在该子句中，有一个隐式本地绑定`this`指的是应用该方法的合约，它具有模板数据记录的类型。本合约的模板参数也在范围内。
* 可以使用与顶级函数相同的语法来定义方法实现，包括模式匹配和保护（例如`method3`）。
* 每个方法实现必须返回与接口声明中为该方法指定的相同类型。
* 特殊`view`方法的实现必须返回接口声明中指定为`viewtype`的类型。

#### 空 `interface instance` 条款

* 如果接口没有方法，则接口实例只需实现`view`方法：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance YourInterface for NameOfTemplate where
  view = EmptyInterfaceView
```

### 接口函数

#### `interfaceTypeRep`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>HasInterfaceTypeRep i =></code><br />
      <code>i -> TemplateTypeRep</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>MyInterface -> TemplateTypeRep</code></td>
    </tr><tr className="奇数">
      <td>注释</td>
      <td>生成的 <code>TemplateTypeRep</code> 的值指示使用什么模板来构造接口值。</td>
    </tr>
  </tbody>
</表>

#### `toInterface`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>就这样吧。</code><br />
      <code>HasToInterface =></code><br />
      <code>t -> i</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>MyTemplate -> MyInterface</code></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>将模板值转换为接口值。</td>
    </tr>
  </tbody>
</表>

#### `fromInterface`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>HasFromInterface =></code><br />
      <code>i -> 可选 t</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>MyInterface -> 可选 MyTemplate</code></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>尝试将接口值转换回模板值。如果预期的模板类型与用于构建合约的基础模板类型不匹配，结果为<code>None</code>。</td>
    </tr>
  </tbody>
</表>

#### `toInterfaceContractId`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>就这样吧。</code><br />
      <code>HasToInterface =></code><br />
      <code>ContractId t -> ContractId i</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>ContractId MyTemplate -> ContractId MyInterface</code></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>将模板合约ID转换为接口合约ID。</td>
    </tr>
  </tbody>
</表>

#### `fromInterfaceContractId`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>forall t i。</code><br />
      <code>HasFromInterface =></code><br />
      <code>ContractId i -> ContractId t</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>ContractId MyInterface -> ContractId MyTemplate</code></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>将接口合约id转换为模板合约id。该函数不会验证给定的合约 id 实际上是否指向结果类型的合约；如果不是这种情况，后续的<code>fetch</code>、<code>exercise</code>或<code>archive</code>将会失败。因此，只有当已知基础合约属于结果类型时，或者当结果立即被 <code>fetch</code>、<code>exercise</code> 或 <code>archive</code> 操作使用并且交易失败是不匹配情况下的期望行为时，才应使用此方法。在所有其他情况下，请考虑改用 <code>fetchFromInterface</code>。</td>
    </tr>
  </tbody>
</表>

#### `coerceInterfaceContractId`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>forall j i。</code><br />
      <code>(HasInterfaceTypeRep i, HasInterfaceTypeRep j) =></code><br />
      <code>ContractId i -> ContractId j</code></p></td>
    </tr>

    <tr className="偶">
      <td>实例化类型</td>
      <td><code>ContractId SourceInterface -> ContractId TargetInterface</code></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>将接口合约id转换为不同接口的合约id。该函数不会验证给定的合约 id 实际上是否指向结果类型的合约；如果不是这种情况，后续的<code>fetch</code>、<code>exercise</code>或<code>archive</code>将会失败。因此，只有当已知底层合约属于结果类型，或者当<code>fetch</code>、<code>exercise</code>或<code>archive</code>操作立即使用结果并且交易失败是不匹配情况下的期望行为时，才应使用此方法。</td>
    </tr>
  </tbody>
</表>

#### `fetchFromInterface`

<表>
  <正文>
    <tr className="奇数">
      <td>类型</td>
      <td><p><code>forall t i。</code><br />
      <code>(HasFromInterface t i, HasFetch i) =></code><br />
      <code>ContractId i -> 更新（可选（ContractId t, t））</code></p></td>
    </tr><tr className="偶">
      <td>实例化类型</td>
      <td><p><code>ContractId MyInterface -></code><br />
      <code>更新（可选（ContractId MyTemplate、MyTemplate））</code></p></td>
    </tr>

    <tr className="奇数">
      <td>注释</td>
      <td>尝试获取接口合约 ID 并将其转换为模板，如果转换成功，则返回转换后的合约及其合约 ID，否则返回<code>None</code>。</td>
    </tr>
  </tbody>
</表>

### 所需接口

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface OurInterface requires MyInterface, YourInterface where
  viewtype EmptyInterfaceView
```

* 一个接口可以依赖于其他接口。这些是通过接口名称之后、`where` 关键字之前的 `requires` 关键字指定的，并以逗号分隔。

* 为了使接口声明有效，其所需接口的列表必须是传递关闭的。换句话说，接口 `I` 不能要求接口 `J`，除非还明确要求 `J` 所需的所有接口。然而，顺序无关紧要。

  例如，给定

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Shape where
    viewtype EmptyInterfaceView

  interface Rectangle requires Shape where
    viewtype EmptyInterfaceView
  ```

  接口 `Square` 的声明会导致编译器错误

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  -- Compiler error! "Interface Square is missing requirement [Shape]"
  interface Square requires Rectangle where
    viewtype EmptyInterfaceView
  ```

  显式添加 `Shape` 到所需的接口修复了错误

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Square requires Rectangle, Shape where
    viewtype EmptyInterfaceView
  ```

* 为了使模板`T`成为接口`I`的有效`interface instance`，`T`还必须是`I`所需的每个接口的`interface instance`。

#### 接口函数

|功能|笔记|
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `toInterface` |还可以用于将接口值转换为其所需的接口之一。                                                  |
| `fromInterface` |还可用于将接口类型的值转换为其所需的接口之一。                                       |
| `toInterfaceContractId` |还可用于将接口合约 ID 转换为其所需接口之一的合约 ID。                         |
| `fromInterfaceContractId` |还可用于将接口合约 ID 转换为其所需接口之一的合约 ID。                        |
| `fetchFromInterface` |还可用于获取接口合约 ID 并将其转换为其所需接口之一的合约和合约 ID。 |

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/exceptions.rst" hash="0c6fee4c" */}

## 参考：异常（已弃用）

<Warning>
  用户定义的 Daml 异常、捕获和抛出已被弃用，并正在逐步淘汰，以支持 Canton 错误框架，该框架将 Daml 错误表示为 `InvalidGivenCurrentSystemStateOther`。
</Warning>

异常是一项已弃用的 Daml 功能，它提供了一种方法来处理解释过程中出现的某些错误，而不是中止事务，并回滚导致错误的状态更改。

有两种类型的错误：

### 内置错误

|异常类型 |扔在 |
| -------------------- | ----------------------------------------------------------- |
| `GeneralError` |致电 `error` 和 `abort` |
| `ArithmeticError` |溢出和除以零等算术错误 |
| `PreconditionFailed` |返回 `False` 的 `ensure` 语句 |
| `AssertionFailed` | `assert` 调用失败（或来自 `DA.Assert` 的其他功能） |请注意，其他错误无法通过异常处理，例如，对不活动合约的执行仍会导致交易中止。

### 用户定义的异常

用户可以定义自己的可以抛出和捕获的异常类型。该定义看起来与模板类似，就像模板一样，该定义生成给定名称的记录类型以及使该类型可抛出和可捕获的实例。

除了记录字段之外，异常还需要定义一个`message`函数。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exception MyException
  with
    field1 : Int
    field2 : Text
  where
    message "MyException(" <> show field1 <> ", " <> show field2 <> ")"
```

### 抛出异常

抛出异常有两种方式：

1. 在`Action`（如`Update`或`Script`）内部，您可以使用`DA.Exception`中的`throw`。这适用于作为 `ActionThrow` 实例的任何 `Action`。
2. 在`ActionThrow`之外，您可以使用`throwPure`抛出异常。

如果两者都是一个选项，通常最好使用`throw`，因为更容易推断何时抛出异常。

### 捕获异常

异常在 try-catch 块中捕获，类似于 Java 等语言中的异常。 `try`块定义了应处理错误的范围，而`catch`子句定义了处理哪些类型的错误以及程序应如何继续。如果捕获到异常，`try`和抛出异常的点之间的子事务将被回滚。回滚节点下的操作仍然经过验证，因此，例如，您永远无法获取当时不活动的合约或同时拥有两个具有相同密钥的合约。但是，所有账本状态更改（创建、消耗练习）都会回滚到回滚节点之前的状态。

每个 try-catch 块可以有多个 `catch` 子句，第一个适用的子句优先。

在下面的示例中，`T`的`create`将被回滚，并且第一个`catch`条款适用，这将创建一个`Error`合约。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
try do
  _ <- create (T p)
  throw MyException with
    field1 = 0
    field2 = "42"
catch
  (MyException field1 field2) ->
    create Error with
      p = p
      msg = "MyException"
  (ArithmeticError _) ->
    create Error with
      p = p
      msg = "ArithmeticError"
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/working-with.rst" hash="56b3d265" */}

## 参考：内置函数

此页面提供有关使用各种常见概念的内置函数的参考信息。

### 与时间共事

Daml 具有以下用于处理时间的内置函数：

* `datetime`：创建一个给定年、月、日、小时、分钟和秒作为参数的 `Time`。
* `subTime`：一个时间减去另一个时间。返回 `time1` 和 `time2` 之间的 `RelTime` 差异。
* `addRelTime`：添加次数。获取`Time`和`RelTime`，并将`RelTime`添加到`Time`。
* `days`、`hours`、`minutes`、`seconds`：构造指定长度的`RelTime`。
* `pass`：（仅在 Daml 脚本测试中）使用 `pass : RelTime -> Script Time` 将账本时间提前参数金额。返回新时间。

### 处理数字

Daml 具有以下用于处理数字的内置函数：

* `round`：将 `Decimal` 数字舍入为 `Int`。

  `round d` 是 `d` *最近的* `Int`。平局通过从零舍入来解决，例如：

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  round 2.5 == 3    round (-2.5) == -3
  round 3.4 == 3    round (-3.7) == -4
  ```

* `truncate`：将`Decimal`数字转换为`Int`，将值截断为零，例如：

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  truncate 2.2 == 2    truncate (-2.2) == -2
  truncate 4.9 == 4    v (-4.9) == -4
  ```

* `intToDecimal`：将`Int`转换为`Decimal`。

`Decimal` 表示的数字集在除法下不是封闭的，因为结果可能需要 10 位以上的小数来表示。例如，`1.0 / 3.0 == 0.3333...`是有理数，但不是`Decimal`。

### 处理文本

Daml 具有以下用于处理文本的内置函数：* `<>` 运算符：连接两个 `Text` 值。
* `show` 将基本类型（`Bool`、`Int`、`Decimal`、`Party`、`Time`、`RelTime`）的值转换为`Text`。

要转义 Daml 字符串中的文本，请使用 `\`：

<表格样式={{宽度：“69%”}}>
  <colgroup>
    <col style={{宽度: "27%"}} />

    <col style={{宽度: "41%"}} />
  </colgroup>

  <标题>
    <tr 类名=“标题”>
      <第>
        <块引用>
          <p>人物</p>
        </块引用>
      </th>

      <th>如何逃脱</th>
    </tr>
  </标题>

  <正文>
    <tr className="奇数">
      <td>`\`</td>
      <td>`\\`</td>
    </tr>

    <tr className="偶">
      <td>`"`</td>
      <td>`\"`</td>
    </tr>

    <tr className="奇数">
      <td><代码>'</代码></td>
      <td><代码>'</代码></td>
    </tr>

    <tr className="偶">
      <td>换行符</td>
      <td><代码>\n</代码></td>
    </tr>

    <tr className="奇数">
      <td>标签</td>
      <td><代码>\t</代码></td>
    </tr>

    <tr className="偶">
      <td>回车</td>
      <td><代码>\r</代码></td>
    </tr>

    <tr className="奇数">
      <td>Unicode（以<code>!</code>为例）</td>

      <td>
        <ul>
          <li>十进制代码：<code>\33</code></li>
          <li>八进制代码：<code>\o41</code></li>
          <li>十六进制代码：<code>\x21</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</表>

### 使用列表

Daml 具有以下用于处理列表的内置函数：

* `foldl` 和`foldr`：参见下文`daml-ref-folding`。

#### 折叠

*折叠*需要：

* 二元运算符
*第一个*累加器*值
* 值列表

列表中的元素被逐一处理（在 `foldl` 中从左侧开始，或者在 `foldr` 中从右侧开始）。

<Note>
  我们通常建议使用`foldl`，因为`foldr`通常较慢。这是因为它需要在开始释放其元素之前遍历整个列表。
</Note>

处理过程如下：

1. 二元运算符应用于第一个累加器值和列表中的第一个元素。这会产生第二个累加器值。
2. 二元运算符应用于*第二个*累加器值和列表中的第二个元素。这会产生第三个累加器值。
3. 如此继续，直到列表中不再有元素为止。然后，返回最后一个累加器值。

举个例子，要对 Daml 中的整数列表求和：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumList =
  script do
    assert (foldl (+) 0 [1, 2, 3] == 6)
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/fixity.rst" hash="a12a5d86" */}

## 固定性、关联性和优先级

对于普通的*前缀*运算符（例如函数），`f g h`的语义很清楚：`f`是一个以`g`和`h`作为参数的函数。如果我们希望`f`取得将`g`应用到`h`的结果，我们就写为`f (g h)`。

对于*中缀*运算符（例如`+`和`*`等符号运算符，或反引号包围的函数，例如`` `elem```), it is less clear. What does ``x - y - z`mean？从`y`first中减去`x` （即`(x - y) - z`）通常会产生与先从`y`减去`z`（即`x - (y - z)`）不同的结果。在Daml中，减法运算符`-`被定义为\*左关联\*运算符。也就是说，当我们编写`x - y - z - ...`时，解析器将\*关联到left\*，意味着解析器将其解释为`((x - y) - z) - ...`\`。

一些运算符是*右关联的*。我们已经遇到过一种：函数应用！ `a -> b -> c -> ...`的函数签名被解析为`(a -> (b -> (c -> ...)))`。

最后，一些运算符是非关联的。一个很好的例子是比较运算符，例如 `==` 和 `>`。这意味着这些运算符的任何不明确使用（例如`a == b == c`或`a > b > c`）都会导致**解析错误**。

<Note>
  不要将非关联运算符与左 * 和 * 右关联的运算符混淆，例如 `+` （自 `(x + y) + z = x + (y + z))` 起）。为了获得确定性解析器，必须将此类运算符声明为左关联或右关联之一。在 Daml 中，`+` 运算符已被声明为左结合
</Note>运算符的“优先级”定义了在组合不同运算符时首先处理哪个运算符。例如，一般来说（在 Daml 中），乘法*优先*于加法。也就是说，`x + y * z`被解析为`x + (y * z)`。运算符优先级以数字表示，数字越大表示优先级越高。相同优先级的运算符与左侧关联（例如，`x + y - z` 被解析为`(x + y) - z`。

运算符的固定性和优先级使用 `infixl`、`infix` 和 `infixr` 关键字（分别表示左结合性、非结合性和右结合性）来声明，这些关键字采用 0 到 9 之间的整数以及固定性适用的运算符。例如，`infixl 6 +` 声明 `+` 是优先级为 `6` 的 `left-associative` 运算符。这些关键字也可用于用户定义的运算符。下表显示了 Daml 语言内置运算符（例如 `+` 和 `-`）的固定性和优先级：

<表>
  <标题>
    <tr 类名=“标题”>
      <th>优先级</th>
      <th>左关联</th>
      <th>非关联</th>
      <th>右结合</th>
    </tr>
  </标题>

  <正文>
    <tr className="奇数">
      <td><p>9 8 7 6 5 4 3 2 1 0</p></td>
      <td><p><代码>`!!</code></p> <p><code>*</code>, <code>/</code>, <code>%</code> <code>+</code>, <code>-</code></p> <p><code>&lt;$</code>, <code>&lt;$&gt;</code>, <code>$&gt;</code>, <code>&lt;*</code>, <code>&lt;*&gt;</code>, <code>*&gt;</code></p> <p><code>&gt;&gt;</code>, <code>&gt;&gt;=</code>, <code>&lt;&amp;&gt;</code></p></td> <td><p><code>==</code>, <code>/=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;==</code>, <code>&gt;</code>, <code>===</code>, <code>=/=</code></p></td> <td><p><code>.</code> <code>&lt;#&amp;&amp;&gt;</code>, <code>^</code>, <code>**</code></p> <p><code>&lt;&gt;</code> <code>`++</代码>，<代码>::</代码></p>
      <p><code>&&</code>、<code>&&&</code> <code>||</code>、<code>|||</code> <code>=\<\<</code>、<code>\<=\<</code>、<code>>=></code> <code>\$</code></p></td>
    </tr>
  </tbody>
</表>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
