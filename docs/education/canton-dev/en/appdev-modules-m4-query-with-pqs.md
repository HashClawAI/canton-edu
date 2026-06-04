---
title: "Query Contracts and Transactions with PQS"
slug: "appdev-modules-m4-query-with-pqs"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-query-with-pqs.md"
source_title: "Query Contracts and Transactions with PQS"
tags:
  - appdev
  - modules
  - m4-query-with-pqs
---

# Query Contracts and Transactions with PQS

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Contracts and Transactions with PQS

> Use the Participant Query Store (PQS) to query Daml contracts and transactions via SQL.

# How to query contracts and transactions using SQL

## Query

### How to query contracts that are in Active Contract Set (ACS)

To fetch contracts in the ACS use the `active()` table function[^1] which is part of Participant Query Store’s (PQS) schema and can be used as any other PostgreSQL function.

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

### How to query contracts that are in ACS by type

The previous example is very resource-consuming and unadvisable to use except on tiny datasets. A more typical (and efficient at the same time) use case is to limit the result set to a specific Daml template type. The reason for improved efficiency is PostgreSQL’s ability to prune unused partitions when planning the query execution. As long as there is no ambiguity in resolving the type, the following forms are equivalent.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from active('register:DA.Register:IssuerApproval');
   select * from active('DA.Register:IssuerApproval');
   select * from active('IssuerApproval');

```

### How to query contracts that are in ACS by information in payload

To query contracts by business information in the payload, use JSONB operators[^2] in the `WHERE` clause.

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
  See also `pqs-how-to-add-an-index-on-expression-over-jsonb-payload`.
</Note>

<Warning>
  Querying by payload contents may require additional development and administrative work in order to achieve desired performance outcomes. Please refer to [Performance Optimization](/docs/canton/appdev-deep-dives-performance-optimization) for ideas on how to get started.
</Warning>

### How to join contracts that are in ACS

To join contracts from multiple Daml template types use standard `JOIN` syntax.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select ia.contract_id, ip.contract_id
   from active('IssuerApproval') ia
   inner join active('IssuerProposal') ip 
     on ia.payload->>'transferId' = ip.payload->>'transferId';

```

### How to aggregate data from contract values

Since PQS is backed by PostgreSQL database, one can use aggregate functions available as part of Structured Query Language (SQL) syntax.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select payload->'token'->'issue'->>'issuer'          as issuer,
          sum((payload->'token'->>'quantity')::decimal) as total_quantity
   from active('TokenOpen')
   group by payload->'token'->'issue'->>'issuer';

```

### How to query state in the past

PQS uses Event Sourcing[^3] architecture and therefore users can peek into the state at an arbitrary point in ledger history by providing an offset explicitly.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select ia.contract_id, ip.contract_id
   from active('IssuerApproval', 'some_offset') ia
   inner join active('IssuerProposal', 'some_offset') ip
     on ia.payload->>'transferId' = ip.payload->>'transferId';

```

### How to fetch a contract by its contract ID

Contracts may be fetched by their contract ID (regardless of their activeness state). Keep in mind, that interface views and contracts share the same contract ID so the function will return interface views as well.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from lookup_contract('contract_id');

```

### How to get a list of contracts created in an offset range

To get a sorted list of "contract created" events within a specific offset range.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from creates(from_offset := 'from', to_offset := 'to')
   order by created_at_offset, create_event_pk;

```

<div className="caution">
  This query is potentially resource-heavy in the presence of multiple template types and is a poor substitute for Ledger API transaction stream.
</div>

### How to get a list of contracts created in an open offset range

By default, offset edges in `creates()` and `archives()` SQL functions represent closed ranges. To make either or both open, use `WHERE` clauses with desired refinements.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from creates(from_offset := 'from', to_offset := 'to')
   where created_at_offset > 'from';

```

### How to emulate a stream of "contract created" events with SQL

Although PQS is a poor substitute for Ledger API stream of events, it is sometimes justifiable to get a stream of "contract created" events directly from a PQS database.

To emulate such a stream, one needs to implement client-side busy polling of the database using a similar query.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * 
   from creates(from_offset := 'last_memoized_offset')
   where created_at_offset > 'last_memoized_offset'
   order by created_at_offset;

```

The client driver should execute this query in a loop, memoizing[^4] the latest observed offset and passing it into the next iteration. It might be a good idea to add sleeping intervals in the loop when no results are returned to minimize resource wasting.

However, if there is a hard requirement on latency and scalability, the best approach is to source ledger events directly from the Ledger API. PQS is designed to be used best as a complementary source to Ledger API’s transaction stream to query ledger *states* at particular offsets, rather than provide event streams.

## Optimize

PQS is backed by PostgreSQL database. Any query optimization is essentially a database/SQL tuning concern. The usual SQL development best practices apply here:

* Apply indexes for frequently used clauses
* Limit data fetching (remove unnecessary columns in final projection, avoid using `SELECT *`)
* Design Daml models to be read-friendly
* Avoid paginating with the help of `OFFSET` SQL clause
* Avoid using queries similar to `SELECT COUNT(*)` if possible

For additional information concerning performance optimization, refer to [Performance Optimization](/docs/canton/appdev-deep-dives-performance-optimization).

### How to add an index on expression over JSONB payload

To optimize read performance of queries that use `WHERE` clauses with information from payload add indexes on expression[^5].

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

Provide full expressions used in `WHERE` clauses (including operators and casts).

### How to limit data fetching

List only columns with data required and avoid using `*`.

Most Read API functions return an abundance of data in the result set, including contract’s liveness, divulgence and disclosure metadata. Fetching this data involves joining several internal tables. However, if metadata is not required, the query will cause unnecessary burden on PostgreSQL resources. On the other hand, the query planner in PostgreSQL is smart to prune automatically unnecessary joins[^6].

Bad:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select * from active('Token');

```

Good:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select payload->'wallet'->>'holder' as holder,
          (payload->'wallet'->>'quantity')::decimal as quantity
   from active('Token');

```

### How to paginate efficiently

Make sure your paginated access[^7] to data is efficient and does not cause performance degradation.

Bad:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   select *
   from the_source
   order by the_key
   limit page_size
   offset (page_num * page_size);

```

Good:

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

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
