---
title: "CommandsSubmission"
slug: "reference-java-com-daml-ledger-javaapi-data-commandssubmission"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/commandssubmission.md"
source_title: "CommandsSubmission"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - commandssubmission
---

# CommandsSubmission

> 该类可用于构建有效的提交。它提供了用于初始创建的create(String、String、Optional、List)以及设置可选参数的方法，例如withActAs(List)、withWorkflowId(String)等。用法：varsubmission = CommandsSubmission.create(userId,commandId,Optional.of(同步器Id),commands).withAccessToken(token).withWorkflowId(workflowId).with...

## CommandsSubmission - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class CommandsSubmission extends Object
```

**会员**|文档 |会员|介绍 |已弃用 |已删除 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#%3Cinit%3E%28java.util.Optional,java.lang.String,java.lang.String,java.util.List,java.uti l.Optional,java.util.Optional,java.util.Optional,java.util.Optional,java.util.List,java.util.List,java.util.Optional,java.util.List,java.util.Optional,java.util.Optional,java.util.List,java.util.List%29) | `CommandsSubmission(Optional<String>, String, String, List<? extends HasCommands>, Optional<Duration>, Optional<Long>, Optional<Instant>, Optional<Duration>, List<String>, List<String>, Optional<String>, List<DisclosedContract>, Optional<String>, Optional<String>, List<String>, List<PrefetchContractKey>)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#create%28java.lang.String,java.lang.String,java.util.Optional,java.util.List%29) | `create(String, String, Optional<String>, List<? extends HasCommands>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#equals%28java.lang.Object%29) | `equals(Object)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#fromProto%28com.daml.ledger.api.v2.CommandsOuterClass.Commands%29) | `fromProto(CommandsOuterClass.Commands)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getAccessToken%28%29) | `getAccessToken()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getActAs%28%29) | `getActAs()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getCommandId%28%29) | `getCommandId()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getCommands%28%29) | `getCommands()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getDeduplicationDuration%28%29) | `getDeduplicationDuration()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getDeduplicationOffset%28%29) | `getDeduplicationOffset()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getDisclosureContracts%28%29) | `getDisclosedContracts()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getMinLedgerTimeAbs%28%29) | `getMinLedgerTimeAbs()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getMinLedgerTimeRel%28%29) | `getMinLedgerTimeRel()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getPackageIdSelectionPreference%28%29) | `getPackageIdSelectionPreference()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getPrefetchContractKeys%28%29) | `getPrefetchContractKeys()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getReadAs%28%29) | `getReadAs()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getSubmissionId%28%29) | `getSubmissionId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#get同步器Id%28%29) | `get同步器Id()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getUserId%28%29) | `getUserId()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#getWorkflowId%28%29) | `getWorkflowId()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#hashCode%28%29) | `hashCode()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#toProto%28%29) | `toProto()` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#toString%28%29) | `toString()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withAccessToken%28java.lang.String%29) | `withAccessToken(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withActAs%28java.util.List%29) | `withActAs(List<String>)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withActAs%28java.lang.String%29) | `withActAs(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withCommands%28java.util.List%29) | `withCommands(List<? extends HasCommands>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withDeduplicationDuration%28java.time.Duration%29) | `withDeduplicationDuration(Duration)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withDeduplicationOffset%28java.lang.Long%29) | `withDeduplicationOffset(Long)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withDisclosureContracts%28java.util.List%29) | `withDisclosedContracts(List<DisclosedContract>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withMinLedgerTimeAbs%28java.time.Instant%29) | `withMinLedgerTimeAbs(Instant)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withMinLedgerTimeRel%28java.time.Duration%29) | `withMinLedgerTimeRel(Duration)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withPackageIdSelectionPreference%28java.util.List%29) | `withPackageIdSelectionPreference(List<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withPrefetchContractKeys%28java.util.List%29) | `withPrefetchContractKeys(List<PrefetchContractKey>)` | `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withReadAs%28java.util.List%29) | `withReadAs(List<String>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/CommandsSubmission.html#withWorkflowId%28java.lang.String%29) | `withWorkflowId(String)` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
