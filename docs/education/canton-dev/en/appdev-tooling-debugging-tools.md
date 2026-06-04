---
title: "Debugging Tools"
slug: "appdev-tooling-debugging-tools"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/debugging-tools.md"
source_title: "Debugging Tools"
tags:
  - appdev
  - tooling
  - debugging-tools
---

# Debugging Tools

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Debugging Tools

> Tools and workflows for debugging Canton applications: test output, Canton Console, PQS queries, and log analysis

When a transaction fails, a contract goes missing, or your application behaves unexpectedly, Canton provides several tools to investigate. This page covers the debugging tools available and common workflows for diagnosing issues.

## dpm test Output

`dpm test` runs your Daml Script tests and reports results to the terminal. When a test fails, the output includes:

* The script name and the line where the failure occurred
* The error type (e.g., `ContractNotFound`, `AuthorizationError`, `PreconditionFailed`)
* For assertion failures, the expected and actual values

Read the error message carefully -- Daml errors are specific. A `ContractNotFound` means the contract ID you referenced has been archived or never existed for your party. An `AuthorizationError` means the submitting party lacks the required signatory or controller role.

### Choice Coverage

Run `dpm test --show-coverage` to see which choices in your templates were exercised during testing. Low coverage often correlates with untested edge cases. If a choice has zero coverage, consider whether your test suite exercises it.

## Canton Console

The Canton Console is an interactive REPL that connects to a running Canton node. It is the most direct way to inspect ledger state during development.

### Inspecting the Active Contract Set

To see what contracts currently exist for a party:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.state.acs.of_party(myParty)
    res1: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry] = List(
      WrappedContractEntry(
        entry = ActiveContract(
          value = ActiveContract(
            createdEvent = Some(
              value = CreatedEvent(
                offset = 12L,
                nodeId = 0,
                contractId = "00ca4d69609a01f4506bbe595d3a9618fc6efbba7937d86ae2ef1394d08b63968bca1212204d04a08c5b516a06ee4030d85e69b7df88445fbd5237b25a86322efd422054bf",
                templateId = Some(
                  value = Identifier(
                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                    moduleName = "Iou",
                    entityName = "Iou"
                  )
                ),
                contractKey = None,
                contractKeyHash = <ByteString@289c748 size=0 contents="">,
                createArguments = Some(
                  value = Record(
                    recordId = Some(
                      value = Identifier(
                        packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                        moduleName = "Iou",
                        entityName = "Iou"
                      )
                    ),
                    fields = Vector(
                      RecordField(
                        label = "payer",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "owner",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "amount",
                        value = Some(
                          value = Value(
                            sum = Record(
                              value = Record(
                                recordId = Some(
                                  value = Identifier(
                                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                                    moduleName = "Iou",
                                    entityName = "Amount"
                                  )
                                ),
                                fields = Vector(
                                  RecordField(
                                    label = "value",
                                    value = Some(value = Value(sum = Numeric(value = "100.0000000000")))
                                  ),
                                  RecordField(
                                    label = "currency",
                                    value = Some(value = Value(sum = Text(value = "EUR")))
                                  )
                                )
                              )
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "viewers",
                        value = Some(value = Value(sum = List(value = List(elements = Vector()))))
                      )
                    )
                  )
                ),
                createdEventBlob = <ByteString@289c748 size=0 contents="">,
                interfaceViews = Vector(),
                witnessParties = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                signatories = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                observers = Vector(),
                createdAt = Some(
                  value = Timestamp(
                    seconds = 1777917306L,
    ...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.state.acs.of_party(myParty).filter(_.templateId.toString.contains("Iou"))
    res2: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry] = List(
      WrappedContractEntry(
        entry = ActiveContract(
          value = ActiveContract(
            createdEvent = Some(
              value = CreatedEvent(
                offset = 12L,
                nodeId = 0,
                contractId = "00ca4d69609a01f4506bbe595d3a9618fc6efbba7937d86ae2ef1394d08b63968bca1212204d04a08c5b516a06ee4030d85e69b7df88445fbd5237b25a86322efd422054bf",
                templateId = Some(
                  value = Identifier(
                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                    moduleName = "Iou",
                    entityName = "Iou"
                  )
                ),
                contractKey = None,
                contractKeyHash = <ByteString@289c748 size=0 contents="">,
                createArguments = Some(
                  value = Record(
                    recordId = Some(
                      value = Identifier(
                        packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                        moduleName = "Iou",
                        entityName = "Iou"
                      )
                    ),
                    fields = Vector(
                      RecordField(
                        label = "payer",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "owner",
                        value = Some(
                          value = Value(
                            sum = Party(
                              value = "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "amount",
                        value = Some(
                          value = Value(
                            sum = Record(
                              value = Record(
                                recordId = Some(
                                  value = Identifier(
                                    packageId = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25",
                                    moduleName = "Iou",
                                    entityName = "Amount"
                                  )
                                ),
                                fields = Vector(
                                  RecordField(
                                    label = "value",
                                    value = Some(value = Value(sum = Numeric(value = "100.0000000000")))
                                  ),
                                  RecordField(
                                    label = "currency",
                                    value = Some(value = Value(sum = Text(value = "EUR")))
                                  )
                                )
                              )
                            )
                          )
                        )
                      ),
                      RecordField(
                        label = "viewers",
                        value = Some(value = Value(sum = List(value = List(elements = Vector()))))
                      )
                    )
                  )
                ),
                createdEventBlob = <ByteString@289c748 size=0 contents="">,
                interfaceViews = Vector(),
                witnessParties = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                signatories = Vector(
                  "MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                observers = Vector(),
                createdAt = Some(
                  value = Timestamp(
                    seconds = 1777917306L,
    ...
```

If a contract you expect to exist is missing from the ACS, it has either been archived or your party was never a stakeholder on it.

### Inspecting Transactions

To see recent transactions:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.completions.list(myParty, atLeastNumCompletions = 1, beginOffsetExclusive = 0L)
    res3: Seq[com.daml.ledger.api.v2.completion.Completion] = List(
      Completion(
        commandId = "a557110b-c367-4ef6-9888-746ce1547675",
        status = Some(
          value = Status(
            code = 0,
            message = "",
            details = Vector(),
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        updateId = "12203fcc195b7cdfc1c05b9ff8a461680e40dcbc6320ace860fbeae67c4f1a84cfd4",
        userId = "CantonConsole",
        actAs = Vector("MyParty::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"),
        submissionId = "e4a3d2cd-ccf7-4aaa-b6ee-e0a4ff062030",
        deduplicationPeriod = DeduplicationOffset(value = 0L),
        traceContext = Some(
          value = TraceContext(
            traceparent = Some(value = "00-4d7fe627685d2ee4451147e433d1710a-55ec0568e44f195b-03"),
            tracestate = None
          )
        ),
        offset = 12L,
        synchronizerTime = Some(
          value = SynchronizerTime(
            synchronizerId = "da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d",
            recordTime = Some(
              value = Timestamp(
                seconds = 1777917304L,
                nanos = 179712000,
                unknownFields = UnknownFieldSet(fields = Map())
              )
            )
          )
        ),
        paidTrafficCost = 0L
      )
    )
```

Transaction details show which contracts were created, archived, and exercised. Compare the transaction trace against your expectations to identify where logic diverged.

### Uploading Packages

If you need to update your Daml packages on a running node:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res4: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

## PQS SQL Queries

PQS projects ledger state into PostgreSQL tables. When you need to investigate contract state across multiple templates or trace historical events, SQL is often the fastest approach.

### Finding a Contract

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find active contracts of a given template
SELECT contract_id, create_arguments
FROM active_contracts
WHERE template_id LIKE '%MyTemplate%';
```

### Tracing an Archived Contract

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find when and why a contract was archived
SELECT contract_id, archive_event_id, effective_at
FROM contracts
WHERE template_id LIKE '%MyTemplate%'
  AND contract_id = 'your-contract-id';
```

### Checking Event History

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- List recent events for a template
SELECT event_id, event_type, contract_id, effective_at
FROM events
WHERE template_id LIKE '%MyTemplate%'
ORDER BY effective_at DESC
LIMIT 20;
```

PQS queries are scoped to your party's data. If you cannot find a contract in PQS, your party may not be a stakeholder on it.

## Log Analysis

When running LocalNet or a local Sandbox, logs capture detailed information about transaction processing, validation errors, and node behavior.

### Capturing Logs

In the cn-quickstart environment:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make capture-logs
```

This collects logs from all Docker containers into a local directory for analysis.

### Using lnav

[lnav](https://lnav.org/) is a log file viewer that handles structured logs well. It supports filtering, searching, and timeline navigation across multiple log files simultaneously.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
lnav logs/*.log
```

Within lnav, use `:filter-in` to focus on specific patterns (e.g., a transaction ID or error keyword) and `:filter-out` to remove noise.

### What to Look For

* **WARN and ERROR level messages** -- These indicate problems. Search for the transaction ID or command ID from your failing operation.
* **Rejection reasons** -- When the mediator rejects a transaction, the logs include the reason (timeout, inconsistency, authorization failure).
* **Connectivity issues** -- If your validator cannot reach the synchronizer, transactions stall. Look for connection errors or timeout messages.

## Common Debugging Workflows

### "Why did my transaction fail?"

1. Check the error returned by the Ledger API or your backend. Note the command ID.
2. Search the validator logs for that command ID to find the detailed rejection reason.
3. Common causes: insufficient authorization (wrong submitting party), contract already archived (race condition), insufficient traffic credits (check your validator's traffic budget).

### "Where is my contract?"

1. Query PQS or the Canton Console ACS for the contract ID or template.
2. If the contract is not in the ACS, check PQS for archive events -- it may have been consumed by a choice.
3. If you never see the contract, verify that your party is a stakeholder (signatory or observer) on it. Canton's privacy model means your party simply will not see contracts it has no stake in.

### "Why can't I see this contract?"

This is almost always a privacy question. Your party can see a contract only if it is a signatory, observer, or has received the contract through divulgence or explicit disclosure. Check the template definition to confirm your party's role. If your party is not listed, you need to either add it as an observer in the Daml model or use explicit disclosure.

## Next Steps

* [Development Tools Overview](/docs/canton/appdev-tooling-development-tools-overview) -- Summary of all available tools
* [Troubleshooting](/docs/canton/appdev-troubleshooting) -- Solutions for common Canton development issues
* [Testing Daml Contracts](/docs/canton/appdev-modules-m3-testing) -- Writing effective tests to catch issues early

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
