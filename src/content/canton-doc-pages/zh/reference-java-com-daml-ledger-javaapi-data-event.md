---
title: "Event"
slug: "reference-java-com-daml-ledger-javaapi-data-event"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/event.md"
source_title: "Event"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - event
---

# Event

> 该接口代表事务中的事件。

## 事件 - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public interface Event
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#fromProtoEvent%28com.daml.ledger.api.v2.EventOuterClass.Event%29) | `fromProtoEvent(EventOuterClass.Event)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getContractId%28%29) | `getContractId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getNodeId%28%29) | `getNodeId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getOffset%28%29) | `getOffset()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getPackageName%28%29) | `getPackageName()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getTemplateId%28%29) | `getTemplateId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#getWitnessParties%28%29) | `getWitnessParties()` | `3.4.8`| - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Event.html#toProtoEvent%28%29) | `toProtoEvent()` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
