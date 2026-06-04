---
title: "DA.Action.State.Class"
slug: "appdev-reference-daml-standard-library-da-action-state-class"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-action-state-class.md"
source_title: "DA.Action.State.Class"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-action-state-class
---

# DA.Action.State.Class

> Daml 标准库模块 DA.Action.State.Class 参考文档。

<span id="module-da-action-state-class-12696" />

# DA.Action.State.Class

DA.Action.State.Class

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

## 类型类

<span id="class-da-action-state-class-actionstate-80467" />

### `class ActionState s m`

动作`m`有一个`s`类型的状态变量。

规则：

* `get *> ma  =  ma`
* `ma <* get  =  ma`
* `put a >>= get   =  put a $> a`
* `put a *> put b  =  put b`
* `(,) <$> get <*> get  =  get <&> \a -> (a, a)`

非正式地，这些规则意味着它的行为就像普通的可赋值变量：
如果你把一个值放在那里，它并不会通过查看它来神奇地改变值
如果您阅读它并分配一个值，那么这始终是您将获得的值，但是
从不读取该值没有任何影响，等等。

方法：

* `get : m s`
  获取状态变量的当前值。
* `put : s -> m ()`
  设置状态变量的值。
* `modify : (s -> s) -> m ()`
  使用给定函数修改状态变量。
* `modify : Action m => (s -> s) -> m ()`

实例：

* `instance ActionState s (State s)`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
