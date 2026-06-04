---
title: "使用 PQS 查询合约与交易"
slug: "appdev-modules-m4-query-with-pqs"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-query-with-pqs.md"
source_title: "Query Contracts and Transactions with PQS"
tags:
  - appdev
  - modules
  - m4-query-with-pqs
---

# 使用 PQS 查询合约与交易

> 使用 Participant Query Store（PQS）通过 SQL 查询 Daml 合约与交易

# 如何使用 SQL 查询合约与交易

## 查询

### 如何查询活跃合约集（ACS）中的合约

获取 ACS 中的合约使用 `active()` 表函数[^1]，它是 PQS schema 的一部分，可像其他 PostgreSQL 函数一样使用。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from active();

```

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
   ----------------------+----------------------------------------------------------------------------------------------
   template_fqn          | register:DA.Register:IssuerApproval
   payload_type          | template
   create_event_pk       | 124095
   create_event_id       | #12202a593e23a993b63ac897d5e87b4a1ee087bb62cc32d6f5b32ea5001f3d2d40a1:5
   created_at_ix         | 37524
   created_at_offset     | 000000000000009343
   archive_event_pk      |
   archive_event_id      |
   archived_at_ix        |
   archived_at_offset    |
   life_ix               | [37524,)
   contract_id           | 0074486cb0469f59b0b5bda4b5794a68cd9350a677ad5e4363d0e4e69b0b925d77ca0212202e62fe6fd912dc18...
   payload               | {"issue": {...}}
   contract_key          |
   metadata              |
   created_effective_at  | 2025-05-19 03:34:10.929+00
   archived_effective_at |
   redaction_id          |
   package_name          | register
   package_version       | 0.0.0
   package_id            | c9238339098524de2923b702aaf1ea3d832250f05b5930d2fa66c1308590505a
   signatories           | {issuer-12::12209223396a4c57103512bcc3ff188549d14ecebe084b21f6508989c9caf403998b}
   observers             | {}

```

### 如何按类型查询 ACS 中的合约

上一示例资源消耗大，除极小数据集外不建议使用。更典型（且更高效）的用法是将结果集限制为特定 Daml template 类型。效率提升的原因是 PostgreSQL 在规划查询执行时可剪枝未使用的分区。只要类型解析无歧义，以下形式等价：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from active('register:DA.Register:IssuerApproval');
   select * from active('DA.Register:IssuerApproval');
   select * from active('IssuerApproval');

```

### 如何按 payload 中的信息查询 ACS 合约

按 payload 中的业务信息查询，在 `WHERE` 子句中使用 JSONB 运算符[^2]。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from active('register:DA.Register:IssuerApproval')
   where payload->'issue'->>'issuer' = 'foo';

```

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select payload->'token'->'wallet'->>'label'
   from active('TokenOpen')
   where payload->'token'->'issue'->>'issuer' = 'foo'
     and (payload->'token'->>'quantity')::decimal > 42;

```

<Note>
  另见 `pqs-how-to-add-an-index-on-expression-over-jsonb-payload`。
</Note>

<Warning>
  按 payload 内容查询可能需要额外开发与管理工作以达到期望性能。请参阅 [性能优化](/zh/docs/canton/appdev-deep-dives-performance-optimization) 了解入门思路。
</Warning>

### 如何 join ACS 中的合约

join 多种 Daml template 类型的合约使用标准 `JOIN` 语法。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select ia.contract_id, ip.contract_id
   from active('IssuerApproval') ia
   inner join active('IssuerProposal') ip 
     on ia.payload->>'transferId' = ip.payload->>'transferId';

```

### 如何聚合合约值中的数据

PQS 基于 PostgreSQL，可使用 SQL 语法中的聚合函数。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select payload->'token'->'issue'->>'issuer'          as issuer,
          sum((payload->'token'->>'quantity')::decimal) as total_quantity
   from active('TokenOpen')
   group by payload->'token'->'issue'->>'issuer';

```

### 如何查询历史状态

PQS 采用事件溯源[^3]架构，用户可通过显式提供 offset 查看账本历史中任意时点的状态。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select ia.contract_id, ip.contract_id
   from active('IssuerApproval', 'some_offset') ia
   inner join active('IssuerProposal', 'some_offset') ip
     on ia.payload->>'transferId' = ip.payload->>'transferId';

```

### 如何按 contract ID 获取合约

可按 contract ID 获取合约（无论活跃状态）。注意 interface view 与合约共享同一 contract ID，函数也会返回 interface view。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from lookup_contract('contract_id');

```

### 如何获取 offset 范围内的合约创建列表

获取特定 offset 范围内排序的「合约创建」事件列表。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from creates(from_offset := 'from', to_offset := 'to')
   order by created_at_offset, create_event_pk;

```

<div className="caution">
  存在多种 template 类型时此查询可能资源密集，是 Ledger API 交易流的拙劣替代。
</div>

### 如何获取开放 offset 范围内的合约创建列表

默认 `creates()` 与 `archives()` SQL 函数的 offset 边界为闭区间。要使任一边界或两者开放，使用带所需 refinements 的 `WHERE` 子句。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from creates(from_offset := 'from', to_offset := 'to')
   where created_at_offset > 'from';

```

### 如何用 SQL 模拟「合约创建」事件流

尽管 PQS 是 Ledger API 事件流的拙劣替代，有时仍可从 PQS 数据库直接获取「合约创建」事件流。

模拟此类流需在客户端实现类似查询的数据库忙轮询。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * 
   from creates(from_offset := 'last_memoized_offset')
   where created_at_offset > 'last_memoized_offset'
   order by created_at_offset;

```

客户端驱动应在循环中执行此查询，记忆化[^4]最新观察到的 offset 并传入下一次迭代。无结果返回时可在循环中加入睡眠间隔以减少资源浪费。

但若对延迟与可扩展性有硬性要求，最佳做法是从 Ledger API 直接获取账本事件。PQS 设计为 Ledger API 交易流的补充，用于在特定 offset 查询账本*状态*，而非提供事件流。

## 优化

PQS 基于 PostgreSQL，查询优化本质上是数据库/SQL 调优问题。常规 SQL 开发最佳实践适用：

* 为常用子句添加索引
* 限制数据获取（最终投影中移除不必要列，避免 `SELECT *`）
* 设计便于读取的 Daml 模型
* 避免使用 `OFFSET` SQL 子句分页
* 尽可能避免类似 `SELECT COUNT(*)` 的查询

性能优化更多信息见 [性能优化](/zh/docs/canton/appdev-deep-dives-performance-optimization)。

### 如何在 JSONB payload 表达式上添加索引

优化在 `WHERE` 子句中使用 payload 信息的查询，在表达式[^5]上添加索引。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   call create_index_for_contract(
     'token_wallet_holder_idx',
     'register:DA.Register:Token',
     '(payload->''wallet''->>''holder'')',
     'hash'
   );

```

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   call create_index_for_contract(
     'token_open_wallet_qty_idx',
     'register:DA.Register:TokenOpen',
     '((payload->''wallet''->>''quantity'')::decimal)',
     'btree'
   );

```

提供 `WHERE` 子句中使用的完整表达式（含运算符与类型转换）。

### 如何限制数据获取

仅列出所需数据的列，避免使用 `*`。

多数 Read API 函数在结果集中返回大量数据，包括合约生命周期、泄露与披露元数据。获取这些数据需 join 多个内部表。若不需要元数据，查询会对 PostgreSQL 资源造成不必要负担。另一方面，PostgreSQL 查询规划器足够智能，可自动剪枝不必要的 join[^6]。

不推荐：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from active('Token');

```

推荐：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select payload->'wallet'->>'holder' as holder,
          (payload->'wallet'->>'quantity')::decimal as quantity
   from active('Token');

```

### 如何高效分页

确保分页访问[^7]高效且不导致性能下降。

不推荐：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from the_source
   order by the_key
   limit page_size
   offset (page_num * page_size);

```

推荐：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from the_source
   where the_key > prev_page_last_key
   order by the_key
   limit page_size;

```

[^1]: [https://www.postgresql.org/docs/current/xfunc-sql.html#XFUNC-SQL-TABLE-FUNCTIONS](https://www.postgresql.org/docs/current/xfunc-sql.html#XFUNC-SQL-TABLE-FUNCTIONS)

[^2]: [https://www.postgresql.org/docs/current/functions-json.html](https://www.postgresql.org/docs/current/functions-json.html)

[^3]: [https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing)

[^4]: [https://en.wikipedia.org/wiki/Memoization](https://en.wikipedia.org/wiki/Memoization)

[^5]: [https://www.postgresql.org/docs/current/indexes-expressional.html](https://www.postgresql.org/docs/current/indexes-expressional.html)

[^6]: [https://www.oreilly.com/library/view/mastering-postgresql-12/9781838988821/736b4431-b85e-4879-9a93-e5133b42db1f.xhtml](https://www.oreilly.com/library/view/mastering-postgresql-12/9781838988821/736b4431-b85e-4879-9a93-e5133b42db1f.xhtml)

[^7]: [https://www.postgresql.org/docs/current/queries-limit.html](https://www.postgresql.org/docs/current/queries-limit.html)

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
