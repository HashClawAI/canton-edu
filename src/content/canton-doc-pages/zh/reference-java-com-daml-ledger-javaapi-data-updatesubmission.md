---
title: "UpdateSubmission"
slug: "reference-java-com-daml-ledger-javaapi-data-updatesubmission"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/updatesubmission.md"
source_title: "UpdateSubmission"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - updatesubmission
---

# UpdateSubmission

> 此类可用于构建有效的更新提交。它提供了用于初始创建的 create(String, String, Update) 和设置可选参数的方法，例如 withActAs(List)、withWorkflowId(String) 等。用法： varsubmission = UpdateSubmission.create(userId, commandId, update) .withAccessToken(token) .withParty(party) .with...

## 更新提交 - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class UpdateSubmission<U> extends Object
```

**会员**|文档 |会员|介绍 |已弃用 |已删除 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#create%28java.lang.String,java.lang.String,com.daml.ledger.javaapi.data.codegen.Update%29) | `create(String, String, Update<U>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getAccessToken%28%29) | `getAccessToken()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getActAs%28%29) | `getActAs()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getCommandId%28%29) | `getCommandId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDeduplicationDuration%28%29) | `getDeduplicationDuration()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDeduplicationOffset%28%29) | `getDeduplicationOffset()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDisclosureContracts%28%29) | `getDisclosedContracts()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getMinLedgerTimeAbs%28%29) | `getMinLedgerTimeAbs()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getMinLedgerTimeRel%28%29) | `getMinLedgerTimeRel()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getPackageIdSelectionPreference%28%29) | `getPackageIdSelectionPreference()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getPrefetchContractKeys%28%29) | `getPrefetchContractKeys()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getReadAs%28%29) | `getReadAs()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#get同步器Id%28%29) | `get同步器Id()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getUpdate%28%29) | `getUpdate()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getUserId%28%29) | `getUserId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getWorkflowId%28%29) | `getWorkflowId()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#toCommandsSubmission%28%29) | `toCommandsSubmission()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withAccessToken%28java.util.Optional%29) | `withAccessToken(Optional<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withActAs%28java.util.List%29) | `withActAs(List<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withActAs%28java.lang.String%29) | `withActAs(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDeduplicationDuration%28java.util.Optional%29) | `withDeduplicationDuration(Optional<Duration>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDeduplicationOffset%28java.util.Optional%29) | `withDeduplicationOffset(Optional<Long>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDisclosureContracts%28java.util.List%29) | `withDisclosedContracts(List<DisclosedContract>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withMinLedgerTimeAbs%28java.util.Optional%29) | `withMinLedgerTimeAbs(Optional<Instant>)`| `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withMinLedgerTimeRel%28java.util.Optional%29) | `withMinLedgerTimeRel(Optional<Duration>)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withPackageIdSelectionPreference%28java.util.List%29) | `withPackageIdSelectionPreference(List<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withPrefetchContractKeys%28java.util.List%29) | `withPrefetchContractKeys(List<PrefetchContractKey>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withReadAs%28java.util.List%29) | `withReadAs(List<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#with同步器Id%28java.lang.String%29) | `with同步器Id(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withWorkflowId%28java.lang.String%29) | `withWorkflowId(String)` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
