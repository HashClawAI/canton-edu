---
title: "UnassignedEvent"
slug: "reference-java-com-daml-ledger-javaapi-data-unassignedevent"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/unassignedevent.md"
source_title: "UnassignedEvent"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - unassignedevent
---

# UnassignedEvent

> 从本地 Javadoc 快照生成 UnassignedEvent 的对象参考页面。

## UnassignedEvent - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class UnassignedEvent extends Object implements ReassignmentEvent
```

**会员**|文档 |会员|介绍 |已弃用 |已删除 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#%3Cinit%3E%28long,java.lang.String,java.lang.St环，com.daml.ledger.javaapi.data.Identifier，java.lang.String，java.lang.String，java.lang.String，java.lang.String，long，java.time.Instant，java.util.List，int％29） | `UnassignedEvent(long, String, String, Identifier, String, String, String, String, long, Instant, List<String>, int)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#equals%28java.lang.Object%29) | `equals(Object)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#fromProto%28com.daml.ledger.api.v2.ReassignmentOuterClass.UnassignedEvent%29) | `fromProto(ReassignmentOuterClass.UnassignedEvent)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getAssignmentExclusivity%28%29) | `getAssignmentExclusivity()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getContractId%28%29) | `getContractId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getNodeId%28%29) | `getNodeId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getOffset%28%29) | `getOffset()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getPackageName%28%29) | `getPackageName()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getReassignmentCounter%28%29) | `getReassignmentCounter()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getReassignmentId%28%29) | `getReassignmentId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getSource%28%29) | `getSource()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getSubmitter%28%29) | `getSubmitter()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getTarget%28%29) | `getTarget()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getTemplateId%28%29) | `getTemplateId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#getWitnessParties%28%29) | `getWitnessParties()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#hashCode%28%29) | `hashCode()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#toProto%28%29) | `toProto()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UnassignedEvent.html#toString%28%29) | `toString()` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
