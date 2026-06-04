---
title: "DA.Record"
slug: "appdev-reference-daml-standard-library-da-record"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-record.md"
source_title: "DA.Record"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-record
---

# DA.Record

> Daml 模块 DA.Record 参考文档。

<span id="module-da-record-78710" />

# DA.Record

导出记录相关机制，使代码能对底层记录类型多态。

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定（Stable）。
  </Card>

  <Card title="说明">
    状态：`active`
    引入版本：`3.4.9`
    移除版本：`-`
    警告：`0`
    弃用：`0`
    弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-internal-record-hasfield-59910" />

### `type HasField = (GetField x r a, SetField x r a)`

`HasField` 是 `GetField` 与 `SetField` 的类型同义词，分别为每条记录字段自动提供 getter 与 setter。

**绝大多数场景应优先使用普通记录语法**：

```
daml> let a = MyRecord 1 "hello"
daml> a.foo
1
daml> a.bar
"hello"
daml> a { bar = "bye" }
MyRecord {foo = 1, bar = "bye"}
daml> a with foo = 3
MyRecord {foo = 3, bar = "hello"}
daml>
```

更多记录语法见 [DA.Record](/appdev/reference/daml-standard-library/da-record)。

`GetField x r a` 与 `SetField x r a` 为三参数类型类：第一参数 `x` 为字段名，第二参数 `r` 为记录类型，第三参数 `a` 为该字段类型。

例如定义：

```
data MyRecord = MyRecord with
    foo : Int
    bar : Text
```

则自动得到下列 GetField / SetField 实例：

```
GetField "foo" MyRecord Int
SetField "foo" MyRecord Int
GetField "bar" MyRecord Text
SetField "bar" MyRecord Text
```

取值可使用 `GetField` 的 `getField`：

```
getFoo : MyRecord -> Int
getFoo r = getField @"foo" r

getBar : MyRecord -> Text
getBar r = getField @"bar" r
```

注意这里使用类型应用语法（`f @t`）指定字段名。

设值可使用 `SetField` 的 `setField`：

```
setFoo : Int -> MyRecord -> MyRecord
setFoo a r = setField @"foo" a r

setBar : Text -> MyRecord -> MyRecord
setBar a r = setField @"bar" a r
```

## 类型类

<span id="class-da-internal-record-getfield-53979" />

### `class GetField x r a`

`GetField x r a` 提供 `HasField` 的 getter 部分。

方法：

* `getField : r -> a`

实例：

* `instance GetField _1 (a, b) a`
* `instance GetField _1 (a, b, c) a`
* `instance GetField _1 (a, b, c, d) a`
* `instance GetField _1 (a, b, c, d, e) a`
* `instance GetField _2 (a, b) b`
* `instance GetField _2 (a, b, c) b`
* `instance GetField _2 (a, b, c, d) b`
* `instance GetField _2 (a, b, c, d, e) b`
* `instance GetField _3 (a, b, c) c`
* `instance GetField _3 (a, b, c, d) c`
* `instance GetField _3 (a, b, c, d, e) c`
* `instance GetField _4 (a, b, c, d) d`
* `instance GetField _4 (a, b, c, d, e) d`
* `instance GetField _5 (a, b, c, d, e) e`
* `instance GetField appEndo (Endo a) (a -> a)`
* `instance GetField category FailureStatus FailureCategory`
* `instance GetField errorId FailureStatus Text`
* `instance GetField getAll All Bool`
* `instance GetField getAny Any Bool`
* `instance GetField getAnyView AnyView Any`
* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance GetField hd (NonEmpty a) a`
* `instance GetField map (Set k) (Map k ())`
* `instance GetField message FailureStatus Text`
* `instance GetField message ArithmeticError Text`
* `instance GetField message AssertionFailed Text`
* `instance GetField message GeneralError Text`
* `instance GetField message PreconditionFailed Text`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance GetField runState (State s a) (s -> (a, s))`
* `instance GetField srcLocEndCol SrcLoc Int`
* `instance GetField srcLocEndLine SrcLoc Int`
* `instance GetField srcLocFile SrcLoc Text`
* `instance GetField srcLocModule SrcLoc Text`
* `instance GetField srcLocPackage SrcLoc Text`
* `instance GetField srcLocStartCol SrcLoc Int`
* `instance GetField srcLocStartLine SrcLoc Int`
* `instance GetField tl (NonEmpty a) [a]`

<span id="class-da-internal-record-setfield-4311" />

### `class SetField x r a`

`SetField x r a` 提供 `HasField` 的 setter 部分。

方法：

* `setField : a -> r -> r`

实例：

* `instance SetField _1 (a, b) a`
* `instance SetField _1 (a, b, c) a`
* `instance SetField _1 (a, b, c, d) a`
* `instance SetField _1 (a, b, c, d, e) a`
* `instance SetField _2 (a, b) b`
* `instance SetField _2 (a, b, c) b`
* `instance SetField _2 (a, b, c, d) b`
* `instance SetField _2 (a, b, c, d, e) b`
* `instance SetField _3 (a, b, c) c`
* `instance SetField _3 (a, b, c, d) c`
* `instance SetField _3 (a, b, c, d, e) c`
* `instance SetField _4 (a, b, c, d) d`
* `instance SetField _4 (a, b, c, d, e) d`
* `instance SetField _5 (a, b, c, d, e) e`
* `instance SetField appEndo (Endo a) (a -> a)`
* `instance SetField category FailureStatus FailureCategory`
* `instance SetField errorId FailureStatus Text`
* `instance SetField getAll All Bool`
* `instance SetField getAny Any Bool`
* `instance SetField getAnyView AnyView Any`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField hd (NonEmpty a) a`
* `instance SetField map (Set k) (Map k ())`
* `instance SetField message FailureStatus Text`
* `instance SetField message ArithmeticError Text`
* `instance SetField message AssertionFailed Text`
* `instance SetField message GeneralError Text`
* `instance SetField message PreconditionFailed Text`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance SetField runState (State s a) (s -> (a, s))`
* `instance SetField srcLocEndCol SrcLoc Int`
* `instance SetField srcLocEndLine SrcLoc Int`
* `instance SetField srcLocFile SrcLoc Text`
* `instance SetField srcLocModule SrcLoc Text`
* `instance SetField srcLocPackage SrcLoc Text`
* `instance SetField srcLocStartCol SrcLoc Int`
* `instance SetField srcLocStartLine SrcLoc Int`
* `instance SetField tl (NonEmpty a) [a]`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
