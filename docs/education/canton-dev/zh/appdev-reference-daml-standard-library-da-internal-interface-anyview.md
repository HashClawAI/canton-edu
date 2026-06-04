---
title: "DA.Internal.Interface.AnyView"
slug: "appdev-reference-daml-standard-library-da-internal-interface-anyview"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-internal-interface-anyview.md"
source_title: "DA.Internal.Interface.AnyView"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-internal-interface-anyview
---

# DA.Internal.Interface.AnyView

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.Internal.Interface.AnyView

> Daml 模块 DA.Internal.Interface.AnyView 的参考文档。

<span id="module-da-internal-interface-anyview-80474" />

# DA.Internal.Interface.AnyView

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="说明">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

## 类型类

<span id="class-da-internal-interface-anyview-hasfromanyview-30108" />

### `class HasFromAnyView i v`

## 函数

<span id="function-da-internal-interface-anyview-fromanyview-10400" />

### `fromAnyView`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyView : (HasTemplateTypeRep i, HasFromAnyView i v) => AnyView -> Optional v
```

## 孤儿类型类实例

* `instance Eq InterfaceTypeRep`

* `instance Ord InterfaceTypeRep`

* `instance GetField getAnyView AnyView Any`

* `instance SetField getAnyView AnyView Any`

* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
