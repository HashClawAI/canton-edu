---
title: "Testing Strategies"
slug: "appdev-modules-m5-testing-strategies"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-testing-strategies.md"
source_title: "Testing Strategies"
tags:
  - appdev
  - modules
  - m5-testing-strategies
---

# Testing Strategies

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Strategies

> Testing pyramid for Canton applications, from Daml Script unit tests through integration and end-to-end testing

Testing Canton applications follows the same principle as any distributed system: automate as much as possible and test at the lowest level that catches the bug. What differs is the tooling at each layer and the specific challenges that come with multi-party, privacy-preserving ledgers.

## The Testing Pyramid

Canton applications use a three-layer testing approach, where each layer catches different classes of issues:

* **Unit tests** — Daml Script tests that verify smart contract logic in isolation. These run against an in-memory ledger (the Sandbox) without any network overhead.
* **Integration tests** — Tests that exercise your backend and APIs against a running Canton sandbox or LocalNet. These verify that off-ledger code interacts correctly with the ledger.
* **End-to-end tests** — Full workflow tests across multiple validators, backends, and frontends. These validate that the entire system works as users experience it.

## Unit Testing with Daml Script

Daml Script is the primary tool for unit testing smart contract logic. You write test scripts as top-level values of type `Script ()`, and `dpm test` runs them against the Sandbox.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm test
```

Daml Script tests can be run against the Sandbox, giving you rapid test execution — typically seconds.

A Daml Script unit test creates parties, submits commands, and asserts on results:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testTokenTransfer : Script ()
testTokenTransfer = do
  alice <- allocateParty "Alice"
  bob <- allocateParty "Bob"

  -- Alice creates a token
  tokenCid <- submit alice do
    createCmd Token with
      owner = alice
      issuer = alice
      amount = 100.0

  -- Alice transfers to Bob
  submit alice do
    exerciseCmd tokenCid Transfer with
      newOwner = bob
      transferAmount = 50.0

  -- Verify Bob received the token
  bobTokens <- query @Token bob
  assertMsg "Bob should have one token contract" (length bobTokens == 1)
```

Review the `dpm test` output to confirm which test scripts passed and failed.

### What to test at the unit level

Focus on the behaviors that are unique to your Daml model:

* Template creation with valid and invalid parameters
* Choice authorization (correct controller can exercise, others cannot)
* Business logic within choices (calculations, state transitions)
* Edge cases and error conditions (assertions that should fail)
* Multi-party authorization patterns (propose-accept workflows)

### Separating test code from production code

Unit tests for Daml workflows are compiled into DAR files. These DAR files are for testing only and should not be deployed to validators. Keep test code in separate DAR files from production code by placing tests in a dedicated package:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml/
├── main/           # Production Daml code → main.dar
│   └── daml.yaml
└── test/           # Test scripts → test.dar (depends on main.dar)
    └── daml.yaml
```

## Integration Testing

Integration tests verify that your off-ledger code — backend services, API handlers, database queries — works correctly with a live ledger. You have two tools for this:

* **`dpm sandbox`** — Starts a local Canton sandbox in a single process. Good for testing a single backend against the Ledger API without the overhead of a full network.
* **LocalNet** — A Docker Compose-based multi-validator network. Required when your tests need multiple parties on different validators, wallet integration, or PQS.

### Backend integration tests

For backend services that talk to the Ledger API, write tests that:

1. Start a sandbox or connect to a running LocalNet
2. Create test parties and upload your DARs
3. Submit commands through your backend's API layer
4. Assert on the resulting ledger state or API responses

A Java integration test connects to the Ledger API over gRPC and submits commands:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Set up a gRPC channel to the participant's Ledger API
Channel channel = ManagedChannelBuilder
    .forAddress(ledgerhost, ledgerport)
    .usePlaintext()
    .build();

// Create a blocking stub for command submission
CommandServiceGrpc.CommandServiceBlockingStub commandService =
    CommandServiceGrpc.newBlockingStub(channel);

// Submit a contract creation and wait for the transaction result
var updateSubmission = UpdateSubmission
    .create(APP_ID, randomUUID().toString(), update)
    .withActAs(party);
var request = new SubmitAndWaitForTransactionRequest(
    updateSubmission.toCommandsSubmission());
var response = commandService.submitAndWaitForTransaction(request.toProto());
```

For querying active contracts, use the `StateService`:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
StateServiceGrpc.StateServiceBlockingStub stateService =
    StateServiceGrpc.newBlockingStub(channel);
long ledgerEnd = stateService
    .getLedgerEnd(GetLedgerEndRequest.newBuilder().build())
    .getOffset();

var request = new GetActiveContractsRequest(eventFormat, ledgerEnd);
Iterator<GetActiveContractsResponse> activeContracts =
    stateService.getActiveContracts(request.toProto());
```

### Test isolation

A testing optimization is to have a  long-running Canton instances to avoid repeatedly initializing and starting Canton. Isolate tests using unique participant users and parties for each test run.
One approach is appending a test run ID as a suffix to party and user names in your test harness.

This pattern lets you run tests in parallel against the same Canton instance without interference between test cases.

## End-to-End Testing

End-to-end tests exercise workflows between end users and systems across multiple validators, backends, and frontends.

### Browser automation

For frontend-involved tests, use tools like [Selenium](https://www.selenium.dev/) or [Playwright](https://playwright.dev/) to drive browser sessions. These tests simulate real user interactions: logging in, creating contracts through the UI, and verifying that counterparties see the expected results.

### Time-dependent workflows

For time-sensitive workflows, use the `passTime` function in Daml and configure reduced wait times for faster CI execution. Workflows that incorporate calendar or time functions — such as bond lifecycling with coupon payments — can be tested by advancing time with `passTime`. For end-to-end tests, configure workflows to advance in milliseconds to reduce CI execution time. Pause and resume automation from the test harness to prevent race conditions.

## Dealing with Flaky Tests

Distributed systems introduce data propagation delays and concurrent execution that can cause tests to fail inconsistently. These flaky tests erode developer trust and slow down iteration.

Common sources of flakiness in Canton tests:

* **Propagation delay** — A command succeeds but the transaction hasn't appeared on the reading party's validator yet. Use polling with timeouts rather than fixed sleeps.
* **Party visibility** — Querying for contracts before the party has been allocated on all relevant validators.
* **Concurrent exercises** — Two tests exercising the same contract simultaneously, where one succeeds and the other finds the contract already archived.

Investing time to eliminate flaky tests pays off quickly. A reliable test suite means faster feedback cycles and more confident deployments.

## Performance Testing

Start performance testing early and continuously. Create separate performance tests for each relevant workflow. Test at scale with synthetic data resembling production characteristics. Measure performance characteristics and reset them between test runs to detect regressions. Perform soak testing with long-running deployments to detect bottlenecks. Set up alerting to monitor system failures, tuning it over time for optimal observability.

Performance testing for Canton applications should account for the distinction between on-ledger and off-ledger operations. Ledger operations incur synchronization overhead that varies with transaction complexity and the number of involved parties. Off-ledger operations (PQS queries, backend logic) follow standard performance profiling approaches.

## Next Steps

* [LocalNet Development](/appdev/modules/m5-localnet-development) — Set up and work with the cn-quickstart LocalNet environment
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — Automate your test pipeline

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
