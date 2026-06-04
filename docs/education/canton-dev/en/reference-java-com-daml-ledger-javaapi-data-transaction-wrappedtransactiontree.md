---
title: "Transaction.WrappedTransactionTree"
slug: "reference-java-com-daml-ledger-javaapi-data-transaction-wrappedtransactiontree"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/transaction-wrappedtransactiontree.md"
source_title: "Transaction.WrappedTransactionTree"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - transaction-wrappedtransactiontree
---

# Transaction.WrappedTransactionTree

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Transaction.WrappedTransactionTree

> A generic class that encapsulates a transaction tree along with a list of the wrapped root events of the tree. The wrapped root events are used to construct the tree that is described by the transaction as a tree of WrappedEvents.

## Transaction.WrappedTransactionTree - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Transaction.WrappedTransactionTree.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public static class Transaction.WrappedTransactionTree<WrappedEvent> extends Object
```

**Members**

| Docs                                                                                                                                                                                                      | Member                                                    | Introduced | Deprecated | Removed |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Transaction.WrappedTransactionTree.html#%3Cinit%3E%28com.daml.ledger.javaapi.data.Transaction,java.util.List%29) | `WrappedTransactionTree(Transaction, List<WrappedEvent>)` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Transaction.WrappedTransactionTree.html#getTransaction%28%29)                                                    | `getTransaction()`                                        | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Transaction.WrappedTransactionTree.html#getWrappedRootEvents%28%29)                                              | `getWrappedRootEvents()`                                  | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
