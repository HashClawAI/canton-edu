---
title: "ReassignmentCommands"
slug: "reference-java-com-daml-ledger-javaapi-data-reassignmentcommands"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/reassignmentcommands.md"
source_title: "ReassignmentCommands"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - reassignmentcommands
---

# ReassignmentCommands

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# ReassignmentCommands

> This class can be used to build a valid submission. It provides create(String, String, String, UnassignCommand) for initial creation and methods to set optional parameters e.g withWorkflowId(String), withSubmissionId(String) etc. Usage: var submission = ReassignmentCommands.create(userId, commandId, synchronizerId, unassingnCommand) .withWorkflowId(workflowId) .with...

## ReassignmentCommands - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class ReassignmentCommands extends Object
```

**Members**

| Docs                                                                                                                                                                                                                                        | Member                                                                                                        | Introduced | Deprecated | Removed |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#%3Cinit%3E%28java.util.Optional,java.lang.String,java.lang.String,java.lang.String,java.util.List,java.util.Optional%29) | `ReassignmentCommands(Optional<String>, String, String, String, List<ReassignmentCommand>, Optional<String>)` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#create%28java.lang.String,java.lang.String,java.lang.String,com.daml.ledger.javaapi.data.AssignCommand%29)               | `create(String, String, String, AssignCommand)`                                                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#create%28java.lang.String,java.lang.String,java.lang.String,com.daml.ledger.javaapi.data.UnassignCommand%29)             | `create(String, String, String, UnassignCommand)`                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#equals%28java.lang.Object%29)                                                                                            | `equals(Object)`                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#fromProto%28com.daml.ledger.api.v2.ReassignmentCommandOuterClass.ReassignmentCommands%29)                                | `fromProto(ReassignmentCommandOuterClass.ReassignmentCommands)`                                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getCommandId%28%29)                                                                                                      | `getCommandId()`                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getCommands%28%29)                                                                                                       | `getCommands()`                                                                                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getSubmissionId%28%29)                                                                                                   | `getSubmissionId()`                                                                                           | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getSubmitter%28%29)                                                                                                      | `getSubmitter()`                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getUserId%28%29)                                                                                                         | `getUserId()`                                                                                                 | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#getWorkflowId%28%29)                                                                                                     | `getWorkflowId()`                                                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#hashCode%28%29)                                                                                                          | `hashCode()`                                                                                                  | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#toProto%28%29)                                                                                                           | `toProto()`                                                                                                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#toString%28%29)                                                                                                          | `toString()`                                                                                                  | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#withSubmissionId%28java.lang.String%29)                                                                                  | `withSubmissionId(String)`                                                                                    | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ReassignmentCommands.html#withWorkflowId%28java.lang.String%29)                                                                                    | `withWorkflowId(String)`                                                                                      | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
