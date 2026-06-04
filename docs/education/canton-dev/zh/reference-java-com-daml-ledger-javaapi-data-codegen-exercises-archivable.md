---
title: "Exercises.Archivable"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-exercises-archivable"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/exercises-archivable.md"
source_title: "Exercises.Archivable"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - exercises-archivable
---

# Exercises.Archivable

> 将exerciseArchive() 添加到每个锻炼目标。目标是纠正 ContractId 直接实现 Exercises.makeExerciseCmd(com.daml.ledger.javaapi.data.codegen.Choice<?, ? super A, R>, A) 的问题。这是一个错误，但至少可以通过这样一个事实来避免这一错误：Exercises.makeExerciseCmd(com.daml.ledger.javaapi.data.codegen.Choice<?, ? super A, R>, A) 显然是内部 API 的一部分，因此，如果您直接使用它并且遇到奇怪的异常，则可以保留程序的两个部分。使用exerciseArchive()，我们可以通过让Exercises.Archivable成为真正的Exercises接口来纠正问题，并且在破坏兼容性时可以消除区别。

## 练习.可存档 - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/Exercises.Archivable.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public static interface Exercises.Archivable<Cmd> extends Exercises<Cmd>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/Exercises.Archivable.html#exerciseArchive%28%29) | `exerciseArchive()` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
