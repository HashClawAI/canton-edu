---
title: "DA.Stack"
slug: "appdev-reference-daml-standard-library-da-stack"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-stack.md"
source_title: "DA.Stack"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-stack
---

# DA.Stack

> Daml 模块 DA.Stack 参考文档

# DA.Stack

<span id="module-da-stack-24914" />

# DA.Stack

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

<span id="type-da-stack-types-srcloc-15887" />

### `data SrcLoc`

源代码中的位置。

行号与列号从 0 开始。

构造子：

<span id="constr-da-stack-types-srcloc-29880" />

* `SrcLoc`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| srcLocPackage | Text |  |
  \| srcLocModule | Text |  |
  \| srcLocFile | Text |  |
  \| srcLocStartLine | Int |  |
  \| srcLocStartCol | Int |  |
  \| srcLocEndLine | Int |  |
  \| srcLocEndCol | Int |  |

实例：

* `instance GetField srcLocEndCol SrcLoc Int`
* `instance GetField srcLocEndLine SrcLoc Int`
* `instance GetField srcLocFile SrcLoc Text`
* `instance GetField srcLocModule SrcLoc Text`
* `instance GetField srcLocPackage SrcLoc Text`
* `instance GetField srcLocStartCol SrcLoc Int`
* `instance GetField srcLocStartLine SrcLoc Int`
* `instance SetField srcLocEndCol SrcLoc Int`
* `instance SetField srcLocEndLine SrcLoc Int`
* `instance SetField srcLocFile SrcLoc Text`
* `instance SetField srcLocModule SrcLoc Text`
* `instance SetField srcLocPackage SrcLoc Text`
* `instance SetField srcLocStartCol SrcLoc Int`
* `instance SetField srcLocStartLine SrcLoc Int`

## 函数

<span id="function-da-stack-prettycallstack-78669" />

### `prettyCallStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
prettyCallStack : CallStack -> Text
```

美化打印 `CallStack`。

<span id="function-da-stack-getcallstack-34576" />

### `getCallStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
getCallStack : CallStack -> [(Text, SrcLoc)]
```

从 `CallStack` 提取调用点列表。

最近的调用排在最前。

<span id="function-da-stack-callstack-89067" />

### `callStack`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
callStack : HasCallStack => CallStack
```

访问当前 `CallStack`。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
