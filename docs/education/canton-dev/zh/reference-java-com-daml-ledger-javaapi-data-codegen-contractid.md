---
title: "ContractId"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-contractid"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/contractid.md"
source_title: "ContractId"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - contractid
---

# ContractId

> 该类用作由 java codegen 生成的所有具体 ContractId 的超类，具有以下属性： Foo.ContractId fooCid = new Foo.ContractId("test"); Bar.ContractId barCid = new Bar.ContractId("test"); ContractId<Foo> genericFooCid = new ContractId<>("测试"); ContractId<Foo> genericBarCid = new ContractId<>("测试"); fooCid.equals(genericFooCid) == true; genericFooCid.equals(fooCid) == true; fooCid.equals(barCid) == false; barCid.equals(fooCid) == false;由于擦除，我们无法区分 ContractId<Foo> 和 ContractId<Bar>，因此： fooCid.equals(genericBarCid) == true genericBarCid.equals(fooCid) == true genericFooCid.equals(genericBarCid) == true genericBarCid.equals(genericFooCid) == true

## ContractId - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public class ContractId<T> extends Object implements Exercises<ExerciseCommand>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#%3Cinit%3E%28java.lang.String%29) | `ContractId(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#contractId) | `contractId` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#equals%28java.lang.Object%29) | `equals(Object)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#hashCode%28%29) | `hashCode()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#makeExerciseCmd%28com.daml.ledger.javaapi.data.codegen.Choice,A%29) | `makeExerciseCmd(Choice<?, ? super A, R>, A)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#toString%28%29) | `toString()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractId.html#toValue%28%29) | `toValue()` | `3.4.8`| - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
