---
title: "DA.Internal.Interface.AnyView.Types"
slug: "appdev-reference-daml-standard-library-da-internal-interface-anyview-types"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-internal-interface-anyview-types.md"
source_title: "DA.Internal.Interface.AnyView.Types"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-internal-interface-anyview-types
---

# DA.Internal.Interface.AnyView.Types

> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

# DA.Internal.Interface.AnyView.Types

> Daml 模块 DA.Internal.Interface.AnyView.Types 的参考文档。

<span id="module-da-internal-interface-anyview-types-13315" />

# DA.Internal.Interface.AnyView\.Types

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

## 数据类型

<span id="type-da-internal-interface-anyview-types-anyview-16883" />

### `data AnyView`

可包装任意合约键的存在类型。

构造子：

<span id="constr-da-internal-interface-anyview-types-anyview-58868" />

* `AnyView`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyView | Any |  |
  \| getAnyViewInterfaceTypeRep | InterfaceTypeRep |  |

实例：

* `instance GetField getAnyView AnyView Any`
* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField getAnyView AnyView Any`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`

<span id="type-da-internal-interface-anyview-types-interfacetyperep-5047" />

### `data InterfaceTypeRep`

构造子：

<span id="constr-da-internal-interface-anyview-types-interfacetyperep-24802" />

* `InterfaceTypeRep`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getInterfaceTypeRep | TypeRep |  |

实例：

* `instance GetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance SetField getAnyViewInterfaceTypeRep AnyView InterfaceTypeRep`
* `instance Eq InterfaceTypeRep`
* `instance Ord InterfaceTypeRep`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
