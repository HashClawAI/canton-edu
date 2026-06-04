---
title: "Prelude"
slug: "appdev-reference-daml-standard-library-prelude"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/prelude.md"
source_title: "Prelude"
tags:
  - appdev
  - reference
  - daml-standard-library
  - prelude
---

# Prelude

> Daml 模块 Prelude 参考文档

# Prelude

<span id="module-prelude-72703" />

# Prelude

构成 Daml 语言的核心部分。

## 模块快照

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="通知">
    状态：`active`
    引入版本：`3.4.9`
    移除版本：`-`
    警告数：`0`
    弃用数：`0`
    弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-internal-any-anychoice-86490" />

### `data AnyChoice`

可包装任意 choice 的存在类型。

构造子：

<span id="constr-da-internal-any-anychoice-64121" />

* `AnyChoice`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyChoice | Any |  |
  \| getAnyChoiceTemplateTypeRep | TemplateTypeRep |  |

实例：

* `instance Eq AnyChoice`
* `instance Ord AnyChoice`

<span id="type-da-internal-any-anycontractkey-68193" />

### `data AnyContractKey`

可包装任意合约键的存在类型。

构造子：

<span id="constr-da-internal-any-anycontractkey-82848" />

* `AnyContractKey`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyContractKey | Any |  |
  \| getAnyContractKeyTemplateTypeRep | TemplateTypeRep |  |

实例：

* `instance Eq AnyContractKey`
* `instance Ord AnyContractKey`

<span id="type-da-internal-any-anytemplate-63703" />

### `data AnyTemplate`

可包装任意 template 的存在类型。

构造子：

<span id="constr-da-internal-any-anytemplate-32540" />

* `AnyTemplate`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyTemplate | Any |  |

实例：

* `instance Eq AnyTemplate`
* `instance Ord AnyTemplate`

<span id="type-da-internal-any-templatetyperep-33792" />

### `data TemplateTypeRep`

模板 Id 的唯一文本表示。

构造子：

<span id="constr-da-internal-any-templatetyperep-57303" />

* `TemplateTypeRep`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getTemplateTypeRep | TypeRep |  |

实例：

* `instance Eq TemplateTypeRep`
* `instance Ord TemplateTypeRep`

<span id="type-da-internal-down-down-61433" />

### `data Down a`

`Down` 可用于反转排序顺序。
例如 `sortOn (\x -> Down x.field)` 按 `field` 降序排序。

构造子：

<span id="constr-da-internal-down-down-26630" />

* `Down a`

实例：

* `instance Action Down`
* `instance Applicative Down`
* `instance Functor Down`
* `instance Eq a => Eq (Down a)`
* `instance Ord a => Ord (Down a)`
* `instance Show a => Show (Down a)`

<span id="type-da-internal-interface-implements-92077" />

### `type Implements = (HasInterfaceTypeRep i, HasToInterface t i, HasFromInterface t i)`

（Daml-LF >= 1.15）表示 template 实现某 interface 的约束。

<span id="type-da-internal-lf-anyexception-7004" />

### `data AnyException`

所有异常类型的包装。

<Warning>
  Deprecated: Exceptions are deprecated, prefer `failWithStatus`, and avoid using catch.
</Warning>

<Warning>
  Deprecated: Use `-Wno-deprecated-exceptions` to disable this warning.
</Warning>

实例：

* `instance HasFromAnyException AnyException`
* `instance HasMessage AnyException`
* `instance HasToAnyException AnyException`

<span id="type-da-internal-lf-contractid-95282" />

### `data ContractId a`

`ContractId a` 表示由 template `a` 创建的合约 ID。
可用于 fetch 等操作。

实例：

* `instance Eq (ContractId a)`
* `instance Ord (ContractId a)`
* `instance Show (ContractId a)`

<span id="type-da-internal-lf-date-32253" />

### `data Date`

`Date` 表示日期，例如 `date 2007 Apr 5`。
Date 范围为 0001-01-01 至 9999-12-31。

实例：

* `instance Eq Date`
* `instance Ord Date`
* `instance Bounded Date`
* `instance Enum Date`
* `instance Show Date`

<span id="type-da-internal-lf-map-90052" />

### `data Map a b`

`Map a b` 是从 `a` 到 `b` 的关联数组，使用内建相等性；
请 import `DA.Map` 使用。

实例：

* `instance Ord k => Foldable (Map k)`
* `instance Ord k => Monoid (Map k v)`
* `instance Ord k => Semigroup (Map k v)`
* `instance GetField map (Set k) (Map k ())`
* `instance SetField map (Set k) (Map k ())`
* `instance Ord k => Traversable (Map k)`
* `instance Ord k => Functor (Map k)`
* `instance (Ord k, Eq v) => Eq (Map k v)`
* `instance (Ord k, Ord v) => Ord (Map k v)`
* `instance (Show k, Show v) => Show (Map k v)`

<span id="type-da-internal-lf-party-57932" />

### `data Party`

`Party` 表示合约参与方。

实例：

* `instance HasFromHex (Optional Party)`
* `instance HasToHex Party`
* `instance IsParties Party`
* `instance IsParties (Optional Party)`
* `instance IsParties (NonEmpty Party)`
* `instance IsParties (Set Party)`
* `instance IsParties [Party]`
* `instance Eq Party`
* `instance Ord Party`
* `instance Show Party`

<span id="type-da-internal-lf-textmap-11691" />

### `data TextMap a`

`TextMap a` 是从 `Text` 到 `a` 的关联数组。

实例：

* `instance Foldable TextMap`
* `instance Monoid (TextMap b)`
* `instance Semigroup (TextMap b)`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance Traversable TextMap`
* `instance Functor TextMap`
* `instance Eq a => Eq (TextMap a)`
* `instance Ord a => Ord (TextMap a)`
* `instance Show a => Show (TextMap a)`

<span id="type-da-internal-lf-time-63886" />

### `data Time`

`Time` 表示 UTC 下的具体日期时间，
例如 `time (date 2007 Apr 5) 14 30 05`。
Time 范围为 0001-01-01T00:00:00.000000Z 至
9999-12-31T23:59:59.999999Z。

实例：

* `instance Eq Time`
* `instance Ord Time`
* `instance Bounded Time`
* `instance Show Time`

<span id="type-da-internal-lf-update-68072" />

### `data Update a`

`Update a` 表示更新或查询账本并返回 `a` 的 `Action`，
例如 `create`、`fetch`。

实例：

* `instance CanAssert Update`
* `instance ActionCatch Update`
* `instance ActionThrow Update`
* `instance ActionFailWithStatus Update`
* `instance CanAbort Update`
* `instance HasTime Update`
* `instance Action Update`
* `instance ActionFail Update`
* `instance Applicative Update`
* `instance Functor Update`

<span id="type-da-internal-prelude-optional-37153" />

### `data Optional a`

`Optional a` 封装可选值：`Some a` 含值，`None` 为空。

用 `Optional` 处理错误或边界情况，
无需使用 `error` 等激烈手段。

`Optional` 也是 `Action`，
错误以 `None` 表示；更丰富的错误可用 `Either`。

构造子：

<span id="constr-da-internal-prelude-none-34906" />

* `None`

<span id="constr-da-internal-prelude-some-71164" />

* `Some a`

实例：

* `instance HasFromHex (Optional Party)`
* `instance HasFromHex (Optional Int)`
* `instance HasFromHex (Optional Text)`
* `instance Foldable Optional`
* `instance Action Optional`
* `instance ActionFail Optional`
* `instance Applicative Optional`
* `instance IsParties (Optional Party)`
* `instance Traversable Optional`
* `instance Functor Optional`
* `instance Eq a => Eq (Optional a)`
* `instance Ord a => Ord (Optional a)`
* `instance Show a => Show (Optional a)`

<span id="type-da-internal-template-archive-15178" />

### `data Archive`

对应每个 template 隐式 `Archive`
choice 的数据类型。

构造子：

<span id="constr-da-internal-template-archive-55291" />

* `Archive`
  （无字段）

实例：

* `instance Eq Archive`
* `instance Show Archive`

<span id="type-da-internal-template-functions-choice-82157" />

### `type Choice = (Template t, HasExercise t c r, HasToAnyChoice t c r, HasFromAnyChoice t c r)`

choice 需满足的约束。

<span id="type-da-internal-template-functions-template-31804" />

### `type Template = (HasTemplateTypeRep t, HasToAnyTemplate t, HasFromAnyTemplate t)`

<span id="type-da-internal-template-functions-templatekey-95200" />

### `type TemplateKey = (Template t, HasKey t k, HasLookupByKey t k, HasFetchByKey t k, HasMaintainer t k, HasToAnyContractKey t k, HasFromAnyContractKey t k)`

template key 需满足的约束。

## 类型类

<span id="class-da-internal-assert-canassert-67323" />

### `class Action m => CanAssert m`

决定当前上下文是否可断言的约束。

方法：

* `assertFail : Text -> m t`
  断言失败时中止。在 Update/Scenario/Script 中抛 AssertionFailed；
  
  在 `Either Text` 中返回错误消息。
  

实例：

* `instance CanAssert Update`
* `instance CanAssert (Either Text)`

<span id="class-da-internal-interface-hasinterfacetyperep-84221" />

### `class HasInterfaceTypeRep i`

（Daml-LF >= 1.15）暴露 `interfaceTypeRep`，仅用于 interface。

<span id="class-da-internal-interface-hastointerface-68104" />

### `class HasToInterface t i`

（Daml-LF >= 1.15）暴露 `toInterface` 与 `toInterfaceContractId`。

<span id="class-da-internal-interface-hasfrominterface-43863" />

### `class HasFromInterface t i`

（Daml-LF >= 1.15）暴露 `fromInterface` 与 `fromInterfaceContractId`。

方法：

* `fromInterface : i -> Optional t`
  （Daml-LF >= 1.15）尝试将 interface 值转回 template 值；
  `None` 表示底层 template 类型不匹配。
  
  

  例如 `fromInterface @MyTemplate value` 尝试将 interface 值转为 `MyTemplate`。
  

<span id="class-da-internal-interface-hasinterfaceview-4492" />

### `class HasInterfaceView i v`

方法：

* `_view : i -> v`

<span id="class-da-internal-lf-hastime-96546" />

### `class HasTime m`

`HasTime` 用于可获取时间的上下文（如 `Update`）。

方法：

* `getTime : HasCallStack => m Time`
  获取当前时间。

实例：

* `instance HasTime Update`

<span id="class-da-internal-lf-canabort-29060" />

### `class Action m => CanAbort m`

`CanAbort` 用于可中止的 `Action`。

方法：

* `abort : Text -> m a`
  带消息中止当前动作。

实例：

* `instance CanAbort Update`
* `instance CanAbort (Either Text)`

<span id="class-da-internal-prelude-applicative-9257" />

### `class Functor f => Applicative f`

方法：

* `pure : a -> f a`
  提升值。
* `<*> : f (a -> b) -> f a -> f b`
  顺序应用函数。

  部分 functor 的 `<*>` 实现比默认更高效。
  
* `liftA2 : (a -> b -> c) -> f a -> f b -> f c`
  将二元函数提升到动作。

  部分 functor 的 `liftA2` 比默认更高效；
  若 `fmap` 开销大，优先用 `liftA2` 而非 `fmap` 后再 `<*>`。
  
  
* `*> : f a -> f b -> f b`
  顺序执行动作，丢弃第一个结果。
* `<* : f a -> f b -> f a`
  顺序执行动作，丢弃第二个结果。

实例：

* `instance Applicative (-> r)`
* `instance Applicative (State s)`
* `instance Applicative Down`
* `instance Applicative Update`
* `instance Applicative Optional`
* `instance Applicative Formula`
* `instance Applicative NonEmpty`
* `instance Applicative (Validation err)`
* `instance Applicative (Either e)`
* `instance Applicative []`

<span id="class-da-internal-prelude-action-68790" />

### `class Applicative m => Action m`

方法：

* `>>= : m a -> (a -> m b) -> m b`
  顺序组合两个动作，将第一个的结果传给第二个。
  

实例：

* `instance Action (-> r)`
* `instance Action (State s)`
* `instance Action Down`
* `instance Action Update`
* `instance Action Optional`
* `instance Action Formula`
* `instance Action NonEmpty`
* `instance Action (Either e)`
* `instance Action []`

<span id="class-da-internal-prelude-actionfail-34438" />

### `class Action m => ActionFail m`

此类用于 do 记法中模式匹配的脱糖。
不建议多态使用或直接调用 `fail`；
请考虑 `CanAbort`。

方法：

* `fail : Text -> m a`
  以错误消息失败。

实例：

* `instance ActionFail Update`
* `instance ActionFail Optional`
* `instance ActionFail (Either Text)`
* `instance ActionFail []`

<span id="class-da-internal-prelude-semigroup-78998" />

### `class Semigroup a`

半群类型类（具有结合二元运算的类型）。

方法：

* `<> : a -> a -> a`
  结合运算。

实例：

* `instance Ord k => Semigroup (Map k v)`
* `instance Semigroup (TextMap b)`
* `instance Semigroup All`
* `instance Semigroup Any`
* `instance Semigroup (Endo a)`
* `instance Multiplicative a => Semigroup (Product a)`
* `instance Additive a => Semigroup (Sum a)`
* `instance Semigroup (NonEmpty a)`
* `instance Ord a => Semigroup (Max a)`
* `instance Ord a => Semigroup (Min a)`
* `instance Ord k => Semigroup (Set k)`
* `instance Semigroup (Validation err a)`
* `instance Semigroup Ordering`
* `instance Semigroup Text`
* `instance Semigroup [a]`

<span id="class-da-internal-prelude-monoid-6742" />

### `class Semigroup a => Monoid a`

幺半群类型类（具有结合二元运算与单位元的类型）。

方法：

* `mempty : a`
  `(<>)` 的单位元
* `mconcat : [a] -> a`
  用幺半群折叠列表。
  例如对字符串列表 `mconcat` 会拼接成单个字符串。

实例：

* `instance Ord k => Monoid (Map k v)`
* `instance Monoid (TextMap b)`
* `instance Monoid All`
* `instance Monoid Any`
* `instance Monoid (Endo a)`
* `instance Multiplicative a => Monoid (Product a)`
* `instance Additive a => Monoid (Sum a)`
* `instance Ord k => Monoid (Set k)`
* `instance Monoid Ordering`
* `instance Monoid Text`
* `instance Monoid [a]`

<span id="class-da-internal-template-functions-hassignatory-17507" />

### `class HasSignatory t`

暴露 `signatory`，属于 `Template` 约束。

方法：

* `signatory : t -> [Party]`
  合约的 signatory。

<span id="class-da-internal-template-functions-hasobserver-3182" />

### `class HasObserver t`

暴露 `observer`，属于 `Template` 约束。

方法：

* `observer : t -> [Party]`
  合约的 observer。

<span id="class-da-internal-template-functions-hasensure-18132" />

### `class HasEnsure t`

暴露 `ensure`，属于 `Template` 约束。

方法：

* `ensure : t -> Bool`
  必须为 true 的谓词，否则创建合约失败。

<span id="class-da-internal-template-functions-hascreate-45738" />

### `class HasCreate t`

暴露 `create`，属于 `Template` 约束。

方法：

* `create : t -> Update (ContractId t)`
  基于 template `t` 创建合约。

<span id="class-da-internal-template-functions-hasfetch-52387" />

### `class HasFetch t`

暴露 `fetch`，属于 `Template` 约束。

方法：

* `fetch : ContractId t -> Update t`
  获取给定合约 ID 的合约数据。
  若 ID 不对应活跃合约，
  则失败并中止整个交易。

<span id="class-da-internal-template-functions-hassoftfetch-65731" />

### `class HasSoftFetch t`

暴露 `softFetch`

<span id="class-da-internal-template-functions-hassoftexercise-29758" />

### `class HasSoftExercise t c r`

<span id="class-da-internal-template-functions-hasarchive-7071" />

### `class HasArchive t`

暴露 `archive`，属于 `Template` 约束。

方法：

* `archive : ContractId t -> Update ()`
  归档给定合约 ID 的合约。

<span id="class-da-internal-template-functions-hastemplatetyperep-24134" />

### `class HasTemplateTypeRep t`

在 Daml-LF 1.7+ 暴露 `templateTypeRep`，属于 `Template` 约束。

<span id="class-da-internal-template-functions-hastoanytemplate-94418" />

### `class HasToAnyTemplate t`

在 Daml-LF 1.7+ 暴露 `toAnyTemplate`，属于 `Template` 约束。

<span id="class-da-internal-template-functions-hasfromanytemplate-95481" />

### `class HasFromAnyTemplate t`

在 Daml-LF 1.7+ 暴露 `fromAnyTemplate`，属于 `Template` 约束。

<span id="class-da-internal-template-functions-hasexercise-70422" />

### `class HasExercise t c r`

暴露 `exercise`，属于 `Choice` 约束。

方法：

* `exercise : ContractId t -> c -> Update r`
  对给定合约 ID 行使 choice。

<span id="class-da-internal-template-functions-haschoicecontroller-39229" />

### `class HasChoiceController t c`

暴露 `choiceController`，属于 `Choice` 约束。

<span id="class-da-internal-template-functions-haschoiceobserver-31221" />

### `class HasChoiceObserver t c`

暴露 `choiceObserver`，属于 `Choice` 约束。

<span id="class-da-internal-template-functions-hasexerciseguarded-97843" />

### `class HasExerciseGuarded t c r`

（仅 1.dev）暴露 `exerciseGuarded`，仅用于 interface choice。

方法：

* `exerciseGuarded : (t -> Bool) -> ContractId t -> c -> Update r`
  （仅 1.dev）仅当谓词为 `True` 时对合约行使 choice。
  

<span id="class-da-internal-template-functions-hastoanychoice-82571" />

### `class HasToAnyChoice t c r`

在 Daml-LF 1.7+ 暴露 `toAnyChoice`，属于 `Choice` 约束。
Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-hasfromanychoice-81184" />

### `class HasFromAnyChoice t c r`

在 Daml-LF 1.7+ 暴露 `fromAnyChoice`，属于 `Choice` 约束。
Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-haskey-87616" />

### `class HasKey t k`

暴露 `key`，属于 `TemplateKey` 约束。

方法：

* `key : t -> k`
  合约键。

<span id="class-da-internal-template-functions-haslookupbykey-92299" />

### `class HasLookupByKey t k`

暴露 `lookupByKey`，属于 `TemplateKey` 约束。

方法：

* `lookupByKey : k -> Update (Optional (ContractId t))`
  查找与合约键 `k` 关联的 template `t` 的合约 ID。

  须显式类型应用 `t`，
  例如 `lookupByKey @Account k`。
  

<span id="class-da-internal-template-functions-hasfetchbykey-54638" />

### `class HasFetchByKey t k`

暴露 `fetchByKey`，属于 `TemplateKey` 约束。

方法：

* `fetchByKey : k -> Update (ContractId t, t)`
  获取与合约键关联的合约 ID 与数据；
  

  须显式类型应用 `t`，
  instance, if you want to fetch a contract of template `Account` by its
  key `k`, you must call `fetchByKey @Account k`.

<span id="class-da-internal-template-functions-hasmaintainer-28932" />

### `class HasMaintainer t k`

暴露 `maintainer`，属于 `TemplateKey` 约束。

<span id="class-da-internal-template-functions-hastoanycontractkey-35010" />

### `class HasToAnyContractKey t k`

在 Daml-LF 1.7+ 暴露 `toAnyContractKey`，属于 `TemplateKey` 约束。
Part of the `TemplateKey` constraint.

<span id="class-da-internal-template-functions-hasfromanycontractkey-95587" />

### `class HasFromAnyContractKey t k`

在 Daml-LF 1.7+ 暴露 `fromAnyContractKey`，属于 `TemplateKey` 约束。
Part of the `TemplateKey` constraint.

<span id="class-da-internal-template-functions-hasexercisebykey-36549" />

### `class HasExerciseByKey t k c r`

暴露 `exerciseByKey`。

<span id="class-da-internal-template-functions-isparties-53750" />

### `class IsParties a`

指定 party 列表的方式：单个 party 或 party 列表。

方法：

* `toParties : a -> [Party]`
  转为 party 列表。

实例：

* `instance IsParties Party`
* `instance IsParties (Optional Party)`
* `instance IsParties (NonEmpty Party)`
* `instance IsParties (Set Party)`
* `instance IsParties [Party]`

## 函数

<span id="function-da-internal-assert-assert-75697" />

### `assert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assert : CanAssert m => Bool -> m ()
```

检查条件是否为真；否则中止交易。

<span id="function-da-internal-assert-assertmsg-31545" />

### `assertMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertMsg : CanAssert m => Text -> Bool -> m ()
```

检查条件是否为真；否则带消息中止交易。

<span id="function-da-internal-assert-assertafter-43038" />

### `assertAfter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertAfter : (CanAssert m, HasTime m) => Time -> m ()
```

检查给定时间是否在未来；否则中止交易。

<span id="function-da-internal-assert-assertbefore-99854" />

### `assertBefore`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertBefore : (CanAssert m, HasTime m) => Time -> m ()
```

检查给定时间是否在过去；否则中止交易。

<span id="function-da-internal-date-dayssinceepochtodate-57782" />

### `daysSinceEpochToDate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
daysSinceEpochToDate : Int -> Date
```

将自 epoch（1970-01-01）起的天数转为日期。

<span id="function-da-internal-date-datetodayssinceepoch-98906" />

### `dateToDaysSinceEpoch`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dateToDaysSinceEpoch : Date -> Int
```

将日期转为自 epoch 起的天数。

<span id="function-da-internal-interface-interfacetyperep-28987" />

### `interfaceTypeRep`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interfaceTypeRep : HasInterfaceTypeRep i => i -> TemplateTypeRep
```

（Daml-LF >= 1.15）从 interface 值获取其 template 的 `TemplateTypeRep`。

<span id="function-da-internal-interface-tointerface-33774" />

### `toInterface`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toInterface : HasToInterface t i => t -> i
```

（Daml-LF >= 1.15）将 template 值转为 interface 值。
例如 `toInterface @MyInterface value` 将 template 值转为 `MyInterface`。

<span id="function-da-internal-interface-tointerfacecontractid-24085" />

### `toInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toInterfaceContractId : HasToInterface t i => ContractId t -> ContractId i
```

（Daml-LF >= 1.15）将 template 合约 ID 转为 interface 合约 ID。

<span id="function-da-internal-interface-frominterfacecontractid-39614" />

### `fromInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromInterfaceContractId : HasFromInterface t i => ContractId i -> ContractId t
```

（Daml-LF >= 1.15）将 interface 合约 ID 转为 template 合约 ID。

也可转为所需 interface 的合约 ID。

此函数不验证 ID 是否指向预期 template；
后续 fetch/exercise/archive 可能失败。

仅在已知类型正确或会立即 fetch/exercise/archive 时使用；
否则请用 `fetchFromInterface`。

<span id="function-da-internal-interface-coerceinterfacecontractid-23361" />

### `coerceInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
coerceInterfaceContractId : (HasInterfaceTypeRep i, HasInterfaceTypeRep j) => ContractId i -> ContractId j
```

（Daml-LF >= 1.15）将 interface 合约 ID 转为另一 interface 的合约 ID。

This function does not verify that the contract id
actually points to a contract that implements either interface. This means

for example, the contract id points to a contract of template `A` but it was
coerced into a `ContractId B` where `B` is an interface and there's no
interface instance B for A.

Therefore, you should only use `coerceInterfaceContractId` in situations
否则请用 `fetchFromInterface`。 right
type. You can also use it in situations where you will fetch, exercise, or
archive the contract right away, when a transaction failure is the
appropriate response to the contract having the wrong type.

<span id="function-da-internal-interface-fetchfrominterface-99354" />

### `fetchFromInterface`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchFromInterface : (HasFromInterface t i, HasFetch i) => ContractId i -> Update (Optional (ContractId t, t))
```

（Daml-LF >= 1.15）fetch interface 并转为指定 template；
成功则返回 `(ContractId t, t)`，否则 `None`。

也可 fetch 并转为所需 interface 的合约与 ID。

示例：

```
do
  fetchResult <- fetchFromInterface @MyTemplate ifaceCid
  case fetchResult of
    None -> abort "Failed to convert interface to appropriate template type"
    Some (tplCid, tpl) -> do
       ... do something with tpl and tplCid ...
```

<span id="function-da-internal-interface-exerciseinterfaceguard-49471" />

### `_exerciseInterfaceGuard`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
_exerciseInterfaceGuard : a -> b -> c -> Bool
```

<span id="function-da-internal-interface-view-38554" />

### `view`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
view : HasInterfaceView i v => i -> v
```

<span id="function-da-internal-lf-partytotext-91600" />

### `partyToText`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partyToText : Party -> Text
```

将 `Party` 转为 `Text`（与 `getParty` 传入一致）。
多数情况用 `show`；`show` 会用反引号标明原为 `Party`。

<span id="function-da-internal-lf-partyfromtext-17681" />

### `partyFromText`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partyFromText : Text -> Optional Party
```

将 `Text` 转为 `Party`；含非法字符则 `None`。
见 Daml-LF 规范；接受无单引号的文本。

不检查 ledger 上是否存在该 party；
仅做类型转换。
要保证 party 存在须让其参与合约。

`partyFromText` 与 `partyToText` 在合法 party 字符串与 party 间构成同构。

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
∀ p. partyFromText (partyToText p) = Some p
∀ txt p. partyFromText txt = Some p ==> partyToText p = txt
```

若编译目标为 Daml-LF < 1.2，此函数会在运行时崩溃。

<span id="function-da-internal-lf-coercecontractid-14371" />

### `coerceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
coerceContractId : ContractId a -> ContractId b
```

转换 `ContractId` 的类型索引（仅为指针）；
若 ledger 上 template 不匹配，后续 fetch/exercise 可能失败。

<span id="function-da-internal-prelude-curry-6393" />

### `curry`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
curry : ((a, b) -> c) -> a -> b -> c
```

将接受二元组的函数转为接受两个参数的函数。

<span id="function-da-internal-prelude-uncurry-79420" />

### `uncurry`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry : (a -> b -> c) -> (a, b) -> c
```

将接受两个参数的函数转为接受二元组的函数。

<span id="function-da-internal-prelude-gtgt-56231" />

### `>>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
>> : Action m => m a -> m b -> m b
```

顺序组合两个动作，丢弃第一个结果（类似命令式分号）。

<span id="function-da-internal-prelude-ap-60204" />

### `ap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ap : Applicative f => f (a -> b) -> f a -> f b
```

`<*>` 的同义词。

<span id="function-da-internal-prelude-return-15945" />

### `return`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
return : Applicative m => a -> m a
```

将值注入 monadic 类型；例如 `Update` 中 `return` 得到 `Update a`。

<span id="function-da-internal-prelude-join-43001" />

### `join`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
join : Action m => m (m a) -> m a
```

将嵌套动作折叠为单一动作。

<span id="function-da-internal-prelude-identity-53027" />

### `identity`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
identity : a -> a
```

恒等函数。

<span id="function-da-internal-prelude-guard-82483" />

### `guard`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
guard : ActionFail m => Bool -> m ()
```

<span id="function-da-internal-prelude-foldl-3431" />

### `foldl`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl : (b -> a -> b) -> b -> [a] -> b
```

左折叠，用于检查/分析/消费列表。
`foldl f i xs` 用 `f` 与初值 `i` 从左到右折叠 `xs`。

示例：

```
>>> foldl (+) 0 [1,2,3]
6

>>> foldl (^) 10 [2,3]
1000000
```

foldl 从左到右处理列表。

<span id="function-da-internal-prelude-find-82808" />

### `find`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
find : (a -> Bool) -> [a] -> Optional a
```

`find p xs` 返回 `xs` 中首个满足 `p` 的元素（`Optional`）。

<span id="function-da-internal-prelude-length-32819" />

### `length`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
length : [a] -> Int
```

返回列表长度。

<span id="function-da-internal-prelude-any-88476" />

### `any`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
any : (a -> Bool) -> [a] -> Bool
```

列表中是否存在满足谓词的元素？

<span id="function-da-internal-prelude-all-93363" />

### `all`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
all : (a -> Bool) -> [a] -> Bool
```

谓词是否对列表所有元素为真？

<span id="function-da-internal-prelude-or-54324" />

### `or`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
or : [Bool] -> Bool
```

Bool 列表中是否至少有一个为 True？

<span id="function-da-internal-prelude-and-20777" />

### `and`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
and : [Bool] -> Bool
```

Bool 列表是否全为 True？

<span id="function-da-internal-prelude-elem-84192" />

### `elem`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
elem : Eq a => a -> [a] -> Bool
```

值是否在列表中？

<span id="function-da-internal-prelude-notelem-95004" />

### `notElem`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
notElem : Eq a => a -> [a] -> Bool
```

`elem` 的否定：

<span id="function-da-internal-prelude-ltdollargt-82160" />

### `<$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<$> : Functor f => (a -> b) -> f a -> f b
```

`fmap` 的同义词。

<span id="function-da-internal-prelude-optional-80885" />

### `optional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
optional : b -> (a -> b) -> Optional a -> b
```

`optional` 取默认值、函数与 `Optional` 值；
`None` 时返回默认值，否则对 `Some` 内值应用函数。

基本示例：

```
>>> optional False (> 2) (Some 3)
True
```

```
>>> optional False (> 2) None
False
```

```
>>> optional 0 (*2) (Some 5)
10
>>> optional 0 (*2) None
0
```

对 `Optional Int` 应用 `show`：`Some n` 显示 `n`，`None` 显示空串。

```
>>> optional "" show (Some 5)
"5"
>>> optional "" show (None : Optional Int)
""
```

<span id="function-da-internal-prelude-either-9020" />

### `either`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
either : (a -> c) -> (b -> c) -> Either a b -> c
```

`either` 对 `Either` 做分支：`Left` 用第一个函数，`Right` 用第二个。

示例：

示例：`Left [Int]` 用 `length`，`Right Int` 用翻倍。

```
>>> let s = Left [1,2,3] : Either [Int] Int in either length (*2) s
3
>>> let n = Right 3 : Either [Int] Int in either length (*2) n
6
```

<span id="function-da-internal-prelude-concat-86947" />

### `concat`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concat : [[a]] -> [a]
```

将列表的列表拼接为一个列表。

<span id="function-da-internal-prelude-plusplus-64685" />

### `++`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
++ : [a] -> [a] -> [a]
```

连接两个列表。

<span id="function-da-internal-prelude-flip-60304" />

### `flip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
flip : (a -> b -> c) -> b -> a -> c
```

翻转二元函数的两个参数顺序。

<span id="function-da-internal-prelude-reverse-91564" />

### `reverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverse : [a] -> [a]
```

反转列表。

<span id="function-da-internal-prelude-mapa-5250" />

### `mapA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA : Applicative m => (a -> m b) -> [a] -> m [b]
```

对列表每个元素应用 applicative 函数。

<span id="function-da-internal-prelude-fora-2999" />

### `forA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA : Applicative m => [a] -> (a -> m b) -> m [b]
```

`forA` 是参数翻转的 `mapA`。

<span id="function-da-internal-prelude-sequence-43906" />

### `sequence`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequence : Applicative m => [m a] -> m [a]
```

顺序执行动作列表并收集结果。

<span id="function-da-internal-prelude-eqltlt-62567" />

### `=<<`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=<< : Action m => (a -> m b) -> m a -> m b
```

`=<<` 是参数翻转的 `>>=`。

<span id="function-da-internal-prelude-concatmap-18810" />

### `concatMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concatMap : (a -> [b]) -> [a] -> [b]
```

映射函数到列表各元素并拼接所有结果。

<span id="function-da-internal-prelude-replicate-97857" />

### `replicate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicate : Int -> a -> [a]
```

`replicate i x` 生成 `i` 个 `x` 的列表。

<span id="function-da-internal-prelude-take-28256" />

### `take`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
take : Int -> [a] -> [a]
```

取列表前 `n` 个元素。

<span id="function-da-internal-prelude-drop-39374" />

### `drop`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
drop : Int -> [a] -> [a]
```

丢弃列表前 `n` 个元素。

<span id="function-da-internal-prelude-splitat-62285" />

### `splitAt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitAt : Int -> [a] -> ([a], [a])
```

在指定索引处拆分列表。

<span id="function-da-internal-prelude-takewhile-28496" />

### `takeWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhile : (a -> Bool) -> [a] -> [a]
```

取列表中谓词为真的前缀元素。

<span id="function-da-internal-prelude-dropwhile-40350" />

### `dropWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhile : (a -> Bool) -> [a] -> [a]
```

丢弃列表中谓词为真的前缀元素。

<span id="function-da-internal-prelude-span-51013" />

### `span`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
span : (a -> Bool) -> [a] -> ([a], [a])
```

`span p xs` 等价于 `(takeWhile p xs, dropWhile p xs)`。

<span id="function-da-internal-prelude-partition-74270" />

### `partition`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partition : (a -> Bool) -> [a] -> ([a], [a])
```

`partition p xs` 返回满足/不满足 `p` 的两部分列表。

即

> partition p xs == (filter p xs, filter (not . p) xs)

```
>>> partition (<0) [1, -2, -3, 4, -5, 6]
([-2, -3, -5], [1, 4, 6])
```

<span id="function-da-internal-prelude-break-18317" />

### `break`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
break : (a -> Bool) -> [a] -> ([a], [a])
```

在首个满足谓词的元素前拆成两部分。

<span id="function-da-internal-prelude-lookup-7541" />

### `lookup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookup : Eq a => a -> [(a, b)] -> Optional b
```

查找首个键匹配的元素的值。

<span id="function-da-internal-prelude-enumerate-9854" />

### `enumerate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
enumerate : (Enum a, Bounded a) => [a]
```

生成给定枚举的所有值列表。

<span id="function-da-internal-prelude-zip-87479" />

### `zip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zip : [a] -> [b] -> [(a, b)]
```

`zip` 将两列表配对；较短列表决定长度。

<span id="function-da-internal-prelude-zip3-8569" />

### `zip3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zip3 : [a] -> [b] -> [c] -> [(a, b, c)]
```

`zip3` 类似 `zip`，但生成三元组。

<span id="function-da-internal-prelude-zipwith-13207" />

### `zipWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipWith : (a -> b -> c) -> [a] -> [b] -> [c]
```

`zipWith` 用函数组合两列表对应元素。

<span id="function-da-internal-prelude-zipwith3-3785" />

### `zipWith3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipWith3 : (a -> b -> c -> d) -> [a] -> [b] -> [c] -> [d]
```

`zipWith3` 类似 `zip3`，但用函数组合元素。

<span id="function-da-internal-prelude-unzip-18278" />

### `unzip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unzip : [(a, b)] -> ([a], [b])
```

将键值对列表拆成两个列表。

<span id="function-da-internal-prelude-unzip3-67086" />

### `unzip3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unzip3 : [(a, b, c)] -> ([a], [b], [c])
```

将三元组列表拆成三个列表。

<span id="function-da-internal-prelude-traceraw-94102" />

### `traceRaw`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traceRaw : Text -> a -> a
```

`traceRaw msg a` 打印 `msg` 并返回 `a`（调试用）。

participant 默认以 DEBUG 级别记录这些消息。

<span id="function-da-internal-prelude-trace-56451" />

### `trace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
trace : Show b => b -> a -> a
```

participant 默认以 DEBUG 级别记录这些消息。

<span id="function-da-internal-prelude-traceid-75962" />

### `traceId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traceId : Show b => b -> b
```

participant 默认以 DEBUG 级别记录这些消息。

<span id="function-da-internal-prelude-debug-24649" />

### `debug`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
debug : (Show b, Action m) => b -> m ()
```

`debug x` 打印 `x`（调试用）。

participant 默认以 DEBUG 级别记录这些消息。

<span id="function-da-internal-prelude-debugraw-7384" />

### `debugRaw`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
debugRaw : Action m => Text -> m ()
```

`debugRaw msg` 打印 `msg`（调试用）。

participant 默认以 DEBUG 级别记录这些消息。

<span id="function-da-internal-prelude-fst-55341" />

### `fst`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fst : (a, b) -> a
```

返回元组第一元素。

<span id="function-da-internal-prelude-snd-88623" />

### `snd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
snd : (a, b) -> b
```

返回元组第二元素。

<span id="function-da-internal-prelude-truncate-45759" />

### `truncate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
truncate : Numeric n -> Int
```

`truncate x` 向零取整。

<span id="function-da-internal-prelude-inttonumeric-99696" />

### `intToNumeric`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intToNumeric : NumericScale n => Int -> Numeric n
```

将 `Int` 转为 `Numeric`。

<span id="function-da-internal-prelude-inttodecimal-16628" />

### `intToDecimal`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intToDecimal : Int -> Decimal
```

将 `Int` 转为 `Decimal`。

<span id="function-da-internal-prelude-roundbankers-80419" />

### `roundBankers`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
roundBankers : Int -> Numeric n -> Numeric n
```

银行家舍入：`roundBankers dp x` 保留 `dp` 位小数，`.5` 舍入到最近偶数。

<span id="function-da-internal-prelude-roundcommercial-50292" />

### `roundCommercial`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
roundCommercial : NumericScale n => Int -> Numeric n -> Numeric n
```

商业舍入：`roundCommercial dp x` 保留 `dp` 位小数，`.5` 远离零舍入。

<span id="function-da-internal-prelude-round-17808" />

### `round`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
round : NumericScale n => Numeric n -> Int
```

将 `Numeric` 四舍五入到最近整数，`.5` 远离零。

<span id="function-da-internal-prelude-floor-26810" />

### `floor`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
floor : NumericScale n => Numeric n -> Int
```

将 `Decimal` 向下取整。

<span id="function-da-internal-prelude-ceiling-19727" />

### `ceiling`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ceiling : NumericScale n => Numeric n -> Int
```

将 `Decimal` 向上取整。

<span id="function-da-internal-prelude-null-12330" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : [a] -> Bool
```

列表是否为空？

<span id="function-da-internal-prelude-filter-41317" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : (a -> Bool) -> [a] -> [a]
```

用谓词过滤列表。

<span id="function-da-internal-prelude-sum-46659" />

### `sum`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sum : Additive a => [a] -> a
```

对列表元素求和。

<span id="function-da-internal-prelude-product-15907" />

### `product`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
product : Multiplicative a => [a] -> a
```

对列表元素求积。

<span id="function-da-internal-prelude-undefined-12708" />

### `undefined`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
undefined : a
```

标记未实现的便捷函数；
总是抛出 "Not implemented."。

<span id="function-da-internal-template-functions-softfetch-60405" />

### `softFetch`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
softFetch : HasSoftFetch t => ContractId t -> Update t
```

<span id="function-da-internal-template-functions-softexercise-80500" />

### `softExercise`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
softExercise : HasSoftExercise t c r => ContractId t -> c -> Update r
```

<span id="function-da-internal-template-functions-stakeholder-47883" />

### `stakeholder`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stakeholder : (HasSignatory t, HasObserver t) => t -> [Party]
```

合约 stakeholder：signatory 与 observer。

<span id="function-da-internal-template-functions-maintainer-44226" />

### `maintainer`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maintainer : HasMaintainer t k => k -> [Party]
```

合约键的 maintainer 列表。

<span id="function-da-internal-template-functions-exercisebykey-78695" />

### `exerciseByKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseByKey : HasExerciseByKey t k c r => k -> c -> Update r
```

对与给定键关联的合约行使 choice。

须显式类型应用 `t`，
instance, if you want to exercise a choice `Withdraw` on a contract of
template `Account` given by its key `k`, you must call
`exerciseByKey @Account k Withdraw`.

<span id="function-da-internal-template-functions-createandexercise-2676" />

### `createAndExercise`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
createAndExercise : (HasCreate t, HasExercise t c r) => t -> c -> Update r
```

创建合约并在新合约上行使 choice。

<span id="function-da-internal-template-functions-templatetyperep-92004" />

### `templateTypeRep`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
templateTypeRep : HasTemplateTypeRep t => TemplateTypeRep
```

生成 template id 的唯一文本表示。

<span id="function-da-internal-template-functions-toanytemplate-14372" />

### `toAnyTemplate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyTemplate : HasToAnyTemplate t => t -> AnyTemplate
```

将 template 包装为 `AnyTemplate`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-fromanytemplate-39771" />

### `fromAnyTemplate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyTemplate : HasFromAnyTemplate t => AnyTemplate -> Optional t
```

类型匹配时从 `AnyTemplate` 提取 template，否则 `None`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-toanychoice-22033" />

### `toAnyChoice`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyChoice : (HasTemplateTypeRep t, HasToAnyChoice t c r) => c -> AnyChoice
```

将 choice 包装为 `AnyChoice`。

须显式类型应用 template 类型 `t`。
例如 `toAnyChoice @Account Withdraw`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-fromanychoice-95102" />

### `fromAnyChoice`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyChoice : (HasTemplateTypeRep t, HasFromAnyChoice t c r) => AnyChoice -> Optional c
```

template 与 choice 类型匹配时从 `AnyChoice` 提取 choice，否则 `None`。

须显式类型应用 template 类型 `t`。
例如 `fromAnyChoice @Account choice`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-toanycontractkey-75916" />

### `toAnyContractKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyContractKey : (HasTemplateTypeRep t, HasToAnyContractKey t k) => k -> AnyContractKey
```

将合约键包装为 `AnyContractKey`。

须显式类型应用 template 类型 `t`。
例如 `toAnyContractKey @Proposal k`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-fromanycontractkey-60533" />

### `fromAnyContractKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyContractKey : (HasTemplateTypeRep t, HasFromAnyContractKey t k) => AnyContractKey -> Optional k
```

类型匹配时从 `AnyContractKey` 提取键，否则 `None`。

须显式类型应用 template 类型 `t`。
例如 `fromAnyContractKey @Proposal k`。

仅 Daml-LF 1.7 或更高版本可用。

<span id="function-da-internal-template-functions-visiblebykey-51464" />

### `visibleByKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
visibleByKey : HasLookupByKey t k => k -> Update Bool
```

合约存在且提交者为 stakeholder 且所有 maintainer 授权时为 True；
合约不存在且所有 maintainer 授权时为 False；
否则失败。

## 孤立类型类实例

* `instance Eq a => Eq (Down a)`

* `instance Show a => Show (Down a)`

* `instance Functor Down`

* `instance Functor a`

* `instance Functor []`

* `instance Functor (-> r)`

* `instance Functor (Either e)`

* `instance Ord a => Ord (Down a)`

* `instance Ord TemplateTypeRep`

* `instance Eq Archive`

* `instance Show Archive`

* `instance Eq AnyTemplate`

* `instance Eq AnyChoice`

* `instance Eq AnyContractKey`

* `instance Ord AnyTemplate`

* `instance Ord AnyChoice`

* `instance Ord AnyContractKey`

* `instance Eq TemplateTypeRep`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
