---
title: "DA.Action.State"
slug: "appdev-reference-daml-standard-library-da-action-state"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action-state.md"
source_title: "DA.Action.State"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action-state
---

# DA.Action.State

> Daml 标准库模块 DA.Action.State 参考文档。

<span id="module-da-action-state-50232" />

# DA.Action.State

DA.动作.状态

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Stable.
  </Card>

  <Card title="Notices">
    状态：`active`
    引入于：`3.4.9`
    删除于：`-`
    警告：`0`
    弃用：`0`
    已弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-action-state-type-state-76783" />

### `data State s a`

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
A value of type `State s a` represents a computation that has access to a state variable
of type `s` and produces a value of type `a`.

>>> runState (modify (+1)) 0
((), 1)

>>> evalState (modify (+1)) 0
()

>>> execState (modify (+1)) 0
1

>>> runState (do x <- get; modify (+1); pure x) 0
(0, 1)

>>> runState (put 1) 0
((), 1)

>>> runState (modify (+1)) 0
((), 1)

Note that values of type `State s a` are not serializable.
```

构造函数：

<span id="constr-da-action-state-type-state-26" />

* `State`
  \|领域|类型 |描述 |
  \| :---- | :--- | :---------- |
  \|运行状态| s -> (a, s) | s -> (a, s) |  |

实例：

* `instance ActionState s (State s)`
* `instance Action (State s)`
* `instance Applicative (State s)`
* `instance GetField runState (State s a) (s -> (a, s))`
* `instance SetField runState (State s a) (s -> (a, s))`
* `instance Functor (State s)`

## 函数

<span id="function-da-action-state-evalstate-95640" />

### `evalState`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
evalState : State s a -> s -> a
```

`runState` 的特殊情况，不返回最终状态。

<span id="function-da-action-state-execstate-48251" />

### `execState`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
execState : State s a -> s -> s
```

`runState` 的特殊情况，仅重新调整最终状态。

## 孤立类型类实例

* `instance Functor (State s)`

* `instance Applicative (State s)`

* `instance Action (State s)`

* `instance ActionState s (State s)`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
