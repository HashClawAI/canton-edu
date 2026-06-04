---
title: "外部签名：提交交易"
slug: "appdev-deep-dives-external-signing-transactions"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/external-signing-transactions.md"
source_title: "External Signing: Submitting Transactions"
tags:
  - appdev
  - deep-dives
  - external-signing-transactions
---

# 外部签名：提交交易

> 向 Canton 账本提交外部签名的交易

# 提交外部签名交易 — 第 1 部分

本教程演示如何使用外部私钥授权提交 Daml 命令。建议先阅读外部签名概览。流程使用外部 Party `Alice`、`Bob` 及内置 Ping 模板。

* 第 1 部分：`Alice` 创建 Ping 合约。
* 第 2 部分：`Bob` exercise `Respond` 并归档。

<Warning>仅供演示，勿直接用于生产。</Warning>

# External Signing: Submitting Transactions

# External Signing: Submitting Transactions

# Submit Externally Signed Transactions - Part 1

本教程演示如何使用外部私钥向 Canton 账本提交 Daml 命令 to a Canton ledger using an external private key for transaction authorization. Before proceeding, it is recommended to review the external signing overview to understand the concept of external signing.

The tutorial illustrates the external signing process using two external parties, `Alice` and `Bob`, leveraging the Ping Daml Template which is included by default in all participant nodes.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

module Canton.Internal.Ping where

template Ping
  with
    id : Text
    initiator : Party    
    responder : Party
  where

    signatory initiator
    observer responder

    choice Respond : ()
      controller responder
        do
          return ()

    choice AbortPing : ()
      with
        anyone : Party
      controller anyone
        do
          return ()
```

* In Part 1 `Alice` creates a `Ping` contract.
* In Part 2 `Bob` exercises the `Respond` choice on the contract and archives it.

<Warning>
  This tutorial is for demo purposes. The code snippets should not be used directly in a production environment.
</Warning>

## 前置条件

为简化起见，本教程假设 a minimal Canton setup consisting of one participant node connected to one synchronizer (which includes both a sequencer node and a mediator node).

<Tip>
  If you already have such an instance running or have completed the onboarding tutorial, proceed to the Setup section.
</Tip>

### 启动 Canton

To obtain a Canton artifact refer to the getting started section. First, navigate to the interactive submission example folder located at `examples/08-interactive-submission` in the Canton release artifact.

<Note>
  All commands in this tutorial are expected to be run from that folder.
</Note>

From the artifact directory, start Canton using the command:

```
../../bin/canton -c examples/08-interactive-submission/interactive-submission.conf --bootstrap examples/08-interactive-submission/bootstrap.canton
```

Once the Welcome to Canton message appears, you are ready to proceed.

### 设置

Navigate to the interactive submission example folder located at `examples/08-interactive-submission` in the Canton release artifact.

This tutorial demonstrates external signing with two external parties: Alice and Bob. If you haven't onboarded an external party yet, refer to the onboarding tutorial.

To proceed, gather the following information:

* `Alice`'s Party Id, protocol signing private key, and protocol signing public key fingerprint
* `Bob`'s Party Id
* Synchronizer Id to which the participant is connected
* gRPC Ledger API endpoint

The Party IDs and key-related information should already be known from the onboarding tutorial. To retrieve the participant and synchronizer IDs, as well as the gRPC Ledger API ports, run the following commands in the Canton console:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.synchronizer_id.filterString
    res1: String = "local::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.ledgerApi.address
    res2: String = "127.0.0.1"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.config.ledgerApi.port.unwrap
    res3: Int = 30225
```

For this tutorial, the following values will be used (replace them with actual values):

* `Alice` Party Id: `alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e`
* `Bob` Party Id: `bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a`
* Synchronizer Id: `da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3`
* gRPC Ledger API endpoint: `localhost:4001`

### API

This tutorial interacts with the `InteractiveSubmissionService`, a service available on the gRPC Ledger API of the participant node.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

syntax = "proto3";

package com.daml.ledger.api.v2.interactive;

import "com/daml/ledger/api/v2/commands.proto";
import "com/daml/ledger/api/v2/crypto.proto";
import "com/daml/ledger/api/v2/interactive/interactive_submission_common_data.proto";
import "com/daml/ledger/api/v2/interactive/transaction/v1/interactive_submission_data.proto";
import "com/daml/ledger/api/v2/package_reference.proto";
import "com/daml/ledger/api/v2/transaction.proto";
import "com/daml/ledger/api/v2/transaction_filter.proto";
import "com/daml/ledger/api/v2/value.proto";
import "google/protobuf/duration.proto";
import "google/protobuf/timestamp.proto";

option csharp_namespace = "Com.Daml.Ledger.Api.V2.Interactive";
option java_outer_classname = "InteractiveSubmissionServiceOuterClass";
option java_package = "com.daml.ledger.api.v2.interactive";

// Service allowing interactive construction of command submissions
//
// The prepare and execute endpoints allow to submit commands in 2-steps:
//
// 1. prepare transaction from commands,
// 2. submit the prepared transaction
//
// This gives callers the ability to sign the daml transaction with their own signing keys
service InteractiveSubmissionService {
  // Requires `readAs` scope for the submitting party when LAPI User authorization is enabled
  rpc PrepareSubmission(PrepareSubmissionRequest) returns (PrepareSubmissionResponse);
  // Execute a prepared submission _asynchronously_ on the ledger.
  // Requires a signature of the transaction from the submitting external party.
  rpc ExecuteSubmission(ExecuteSubmissionRequest) returns (ExecuteSubmissionResponse);
  // Similar to ExecuteSubmission but _synchronously_ wait for the completion of the transaction
  // IMPORTANT: Relying on the response from this endpoint requires trusting the Participant Node to be honest.
  // A malicious node could make a successfully committed request appeared failed and vice versa
  rpc ExecuteSubmissionAndWait(ExecuteSubmissionAndWaitRequest) returns (ExecuteSubmissionAndWaitResponse);
  // Similar to ExecuteSubmissionAndWait but additionally returns the transaction
  // IMPORTANT: Relying on the response from this endpoint requires trusting the Participant Node to be honest.
  // A malicious node could make a successfully committed request appear as failed and vice versa
  rpc ExecuteSubmissionAndWaitForTransaction(ExecuteSubmissionAndWaitForTransactionRequest) returns (ExecuteSubmissionAndWaitForTransactionResponse);

  // A preferred package is the highest-versioned package for a provided package-name
  // that is vetted by all the participants hosting the provided parties.
  //
  // Ledger API clients should use this endpoint for constructing command submissions
  // that are compatible with the provided preferred package, by making informed decisions on:
  // - which are the compatible packages that can be used to create contracts
  // - which contract or exercise choice argument version can be used in the command
  // - which choices can be executed on a template or interface of a contract
  //
  // Can be accessed by any Ledger API client with a valid token when Ledger API authorization is enabled.
  //
  // Provided for backwards compatibility, it will be removed in the Canton version 3.4.0
  rpc GetPreferredPackageVersion(GetPreferredPackageVersionRequest) returns (GetPreferredPackageVersionResponse);

  // Compute the preferred packages for the vetting requirements in the request.
  // A preferred package is the highest-versioned package for a provided package-name
  // that is vetted by all the participants hosting the provided parties.
  //
  // Ledger API clients should use this endpoint for constructing command submissions
  // that are compatible with the provided preferred packages, by making informed decisions on:
  // - which are the compatible packages that can be used to create contracts
  // - which contract or exercise choice argument version can be used in the command
  // - which choices can be executed on a template or interface of a contract
  //
  // If the package preferences could not be computed due to no selection satisfying the requirements,
  // a `FAILED_PRECONDITION` error will be returned.
  //
  // Can be accessed by any Ledger API client with a valid token when Ledger API authorization is enabled.
  //
  // Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future releases
  rpc GetPreferredPackages(GetPreferredPackagesRequest) returns (GetPreferredPackagesResponse);
}

// Hints to improve cost estimation precision of a prepared transaction
message CostEstimationHints {
  // Disable cost estimation
  // Default (not set) is false
  bool disabled = 1;
  // Details on the keys that will be used to sign the transaction (how many and of which type).
  // Signature size impacts the cost of the transaction.
  // If empty, the signature sizes will be approximated with threshold-many signatures (where threshold is defined
  // in the PartyToKeyMapping of the external party), using keys in the order they are registered.
  // Optional (empty list is equivalent to not providing this field)
  repeated SigningAlgorithmSpec expected_signatures = 2;
}

// Estimation of the cost of submitting the prepared transaction
// The estimation is done against the synchronizer chosen during preparation of the transaction
// (or the one explicitly requested).
// The cost of re-assigning contracts to another synchronizer when necessary is not included in the estimation.
message CostEstimation {
  // Timestamp at which the estimation was made
  google.protobuf.Timestamp estimation_timestamp = 1;
  // Estimated traffic cost of the confirmation request associated with the transaction
  uint64 confirmation_request_traffic_cost_estimation = 2;
  // Estimated traffic cost of the confirmation response associated with the transaction
  // This field can also be used as an indication of the cost that other potential confirming nodes
  // of the party will incur to approve or reject the transaction
  uint64 confirmation_response_traffic_cost_estimation = 3;
  // Sum of the fields above
  uint64 total_traffic_cost_estimation = 4;
}

message PrepareSubmissionRequest {
  // Uniquely identifies the participant user that prepares the transaction.
  // Must be a valid UserIdString (as described in ``value.proto``).
  // Required unless authentication is used with a user token.
  // In that case, the token's user-id will be used for the request's user_id.
  // Optional
  string user_id = 1;

  // Uniquely identifies the command.
  // The triple (user_id, act_as, command_id) constitutes the change ID for the intended ledger change,
  // where act_as is interpreted as a set of party names.
  // The change ID can be used for matching the intended ledger changes with all their completions.
  // Must be a valid LedgerString (as described in ``value.proto``).
  // Required
  string command_id = 2;

  // Individual elements of this atomic command. Must be non-empty.
  // Limitation: Only single command transaction are currently supported by the API.
  // The field is marked as repeated in preparation for future support of multiple commands.
  // Required
  repeated Command commands = 3;

  // Optional
  MinLedgerTime min_ledger_time = 4;

  // Maximum timestamp at which the transaction can be recorded onto the ledger via the synchronizer specified in the `PrepareSubmissionResponse`.
  // If submitted after it will be rejected even if otherwise valid, in which case it needs to be prepared and signed again
  // with a new valid max_record_time.
  // Use this to limit the time-to-life of a prepared transaction,
  // which is useful to know when it can definitely not be accepted
  // anymore and resorting to preparing another transaction for the same
  // intent is safe again.
  // Optional
  optional google.protobuf.Timestamp max_record_time = 11;

  // Set of parties on whose behalf the command should be executed, if submitted.
  // If ledger API authorization is enabled, then the authorization metadata must authorize the sender of the request
  // to **read** (not act) on behalf of each of the given parties. This is because this RPC merely prepares a transaction
  // and does not execute it. Therefore read authorization is sufficient even for actAs parties.
  // Note: This may change, and more specific authorization scope may be introduced in the future.
  // Each element must be a valid PartyIdString (as described in ``value.proto``).
  // Required, must be non-empty.
  repeated string act_as = 5;

  // Set of parties on whose behalf (in addition to all parties listed in ``act_as``) contracts can be retrieved.
  // This affects Daml operations such as ``fetch``, ``fetchByKey``, ``lookupByKey``, ``exercise``, and ``exerciseByKey``.
  // Note: A command can only use contracts that are visible to at least
  // one of the parties in ``act_as`` or ``read_as``. This visibility check is independent from the Daml authorization
  // rules for fetch operations.
  // If ledger API authorization is enabled, then the authorization metadata must authorize the sender of the request
  // to read contract data on behalf of each of the given parties.
  // Optional
  repeated string read_as = 6;

  // Additional contracts used to resolve contract & contract key lookups.
  // Optional
  repeated DisclosedContract disclosed_contracts = 7;

  // Must be a valid synchronizer id
  // If not set, a suitable synchronizer that this node is connected to will be chosen
  // Optional
  string synchronizer_id = 8;

  // The package-id selection preference of the client for resolving
  // package names and interface instances in command submission and interpretation
  // Optional
  repeated string package_id_selection_preference = 9;

  // When true, the response will contain additional details on how the transaction was encoded and hashed
  // This can be useful for troubleshooting of hash mismatches. Should only be used for debugging.
  // Optional, default to false
  bool verbose_hashing = 10;

  // Fetches the contract keys into the caches to speed up the command processing.
  // Should only contain contract keys that are expected to be resolved during interpretation of the commands.
  // Keys of disclosed contracts do not need prefetching.
  //
  // Optional
  repeated PrefetchContractKey prefetch_contract_keys = 15;

  // Hints to improve the accuracy of traffic cost estimation.
  // The estimation logic assumes that this node will be used for the execution of the transaction
  // If another node is used instead, the estimation may be less precise.
  // Request amplification is not accounted for in the estimation: each amplified request will
  // result in the cost of the confirmation request to be charged additionally.
  //
  // Optional - Traffic cost estimation is enabled by default if this field is not set
  // To turn off cost estimation, set the CostEstimationHints#disabled field to true
  optional CostEstimationHints estimate_traffic_cost = 16;
}

// [docs-entry-start: HashingSchemeVersion]
// The hashing scheme version used when building the hash of the PreparedTransaction
enum HashingSchemeVersion {
  HASHING_SCHEME_VERSION_UNSPECIFIED = 0;
  reserved 1; // Hashing Scheme V1 - unsupported
  HASHING_SCHEME_VERSION_V2 = 2;
}
// [docs-entry-end: HashingSchemeVersion]

message PrepareSubmissionResponse {
  // The interpreted transaction, it represents the ledger changes necessary to execute the commands specified in the request.
  // Clients MUST display the content of the transaction to the user for them to validate before signing the hash if the preparing participant is not trusted.
  PreparedTransaction prepared_transaction = 1;
  // Hash of the transaction, this is what needs to be signed by the party to authorize the transaction.
  // Only provided for convenience, clients MUST recompute the hash from the raw transaction if the preparing participant is not trusted.
  // May be removed in future versions
  bytes prepared_transaction_hash = 2;

  // The hashing scheme version used when building the hash
  HashingSchemeVersion hashing_scheme_version = 3;

  // Optional additional details on how the transaction was encoded and hashed. Only set if verbose_hashing = true in the request
  // Note that there are no guarantees on the stability of the format or content of this field.
  // Its content should NOT be parsed and should only be used for troubleshooting purposes.
  optional string hashing_details = 4;

  // Traffic cost estimation of the prepared transaction
  // Optional
  optional CostEstimation cost_estimation = 5;
}

// Signatures provided by a single party
message SinglePartySignatures {
  // Submitting party
  // Required
  string party = 1;
  // Signatures
  // Required
  repeated Signature signatures = 2;
}

// Additional signatures provided by the submitting parties
message PartySignatures {
  // Additional signatures provided by all individual parties
  // Required
  repeated SinglePartySignatures signatures = 1;
}

message ExecuteSubmissionRequest {
  // the prepared transaction
  // Typically this is the value of the `prepared_transaction` field in `PrepareSubmissionResponse`
  // obtained from calling `prepareSubmission`.
  // Required
  PreparedTransaction prepared_transaction = 1;

  // The party(ies) signatures that authorize the prepared submission to be executed by this node.
  // Each party can provide one or more signatures..
  // and one or more parties can sign.
  // Note that currently, only single party submissions are supported.
  // Required
  PartySignatures party_signatures = 2;

  // Specifies the deduplication period for the change ID (See PrepareSubmissionRequest).
  // If omitted, the participant will assume the configured maximum deduplication time.
  // Optional
  oneof deduplication_period {
    // Specifies the length of the deduplication period.
    // It is interpreted relative to the local clock at some point during the submission's processing.
    // Must be non-negative. Must not exceed the maximum deduplication time.
    google.protobuf.Duration deduplication_duration = 3;

    // Specifies the start of the deduplication period by a completion stream offset (exclusive).
    // Must be a valid absolute offset (positive integer).
    int64 deduplication_offset = 4;
  }

  // A unique identifier to distinguish completions for different submissions with the same change ID.
  // Typically a random UUID. Applications are expected to use a different UUID for each retry of a submission
  // with the same change ID.
  // Must be a valid LedgerString (as described in ``value.proto``).
  //
  // Required
  string submission_id = 5;

  // See [PrepareSubmissionRequest.user_id]
  // Optional
  string user_id = 6;

  // The hashing scheme version used when building the hash
  // Required
  HashingSchemeVersion hashing_scheme_version = 7;

  // If set will influence the chosen ledger effective time but will not result in a submission delay so any override
  // should be scheduled to executed within the window allowed by synchronizer.
  // Optional
  MinLedgerTime min_ledger_time = 8;
}

message ExecuteSubmissionResponse {}

message ExecuteSubmissionAndWaitRequest {
  // the prepared transaction
  // Typically this is the value of the `prepared_transaction` field in `PrepareSubmissionResponse`
  // obtained from calling `prepareSubmission`.
  // Required
  PreparedTransaction prepared_transaction = 1;

  // The party(ies) signatures that authorize the prepared submission to be executed by this node.
  // Each party can provide one or more signatures..
  // and one or more parties can sign.
  // Note that currently, only single party submissions are supported.
  // Required
  PartySignatures party_signatures = 2;

  // Specifies the deduplication period for the change ID (See PrepareSubmissionRequest).
  // If omitted, the participant will assume the configured maximum deduplication time.
  // Optional
  oneof deduplication_period {
    // Specifies the length of the deduplication period.
    // It is interpreted relative to the local clock at some point during the submission's processing.
    // Must be non-negative. Must not exceed the maximum deduplication time.
    google.protobuf.Duration deduplication_duration = 3;

    // Specifies the start of the deduplication period by a completion stream offset (exclusive).
    // Must be a valid absolute offset (positive integer).
    int64 deduplication_offset = 4;
  }

  // A unique identifier to distinguish completions for different submissions with the same change ID.
  // Typically a random UUID. Applications are expected to use a different UUID for each retry of a submission
  // with the same change ID.
  // Must be a valid LedgerString (as described in ``value.proto``).
  //
  // Required
  string submission_id = 5;

  // See [PrepareSubmissionRequest.user_id]
  // Optional
  string user_id = 6;

  // The hashing scheme version used when building the hash
  // Required
  HashingSchemeVersion hashing_scheme_version = 7;

  // If set will influence the chosen ledger effective time but will not result in a submission delay so any override
  // should be scheduled to executed within the window allowed by synchronizer.
  // Optional
  MinLedgerTime min_ledger_time = 8;
}

message ExecuteSubmissionAndWaitResponse {
  // The id of the transaction that resulted from the submitted command.
  // Must be a valid LedgerString (as described in ``value.proto``).
  // Required
  string update_id = 1;

  // The details of the offset field are described in ``community/ledger-api/README.md``.
  // Required
  int64 completion_offset = 2;
}

message ExecuteSubmissionAndWaitForTransactionRequest {
  // the prepared transaction
  // Typically this is the value of the `prepared_transaction` field in `PrepareSubmissionResponse`
  // obtained from calling `prepareSubmission`.
  // Required
  PreparedTransaction prepared_transaction = 1;

  // The party(ies) signatures that authorize the prepared submission to be executed by this node.
  // Each party can provide one or more signatures..
  // and one or more parties can sign.
  // Note that currently, only single party submissions are supported.
  // Required
  PartySignatures party_signatures = 2;

  // Specifies the deduplication period for the change ID (See PrepareSubmissionRequest).
  // If omitted, the participant will assume the configured maximum deduplication time.
  // Optional
  oneof deduplication_period {
    // Specifies the length of the deduplication period.
    // It is interpreted relative to the local clock at some point during the submission's processing.
    // Must be non-negative. Must not exceed the maximum deduplication time.
    google.protobuf.Duration deduplication_duration = 3;

    // Specifies the start of the deduplication period by a completion stream offset (exclusive).
    // Must be a valid absolute offset (positive integer).
    int64 deduplication_offset = 4;
  }

  // A unique identifier to distinguish completions for different submissions with the same change ID.
  // Typically a random UUID. Applications are expected to use a different UUID for each retry of a submission
  // with the same change ID.
  // Must be a valid LedgerString (as described in ``value.proto``).
  //
  // Required
  string submission_id = 5;

  // See [PrepareSubmissionRequest.user_id]
  // Optional
  string user_id = 6;

  // The hashing scheme version used when building the hash
  // Required
  HashingSchemeVersion hashing_scheme_version = 7;

  // If set will influence the chosen ledger effective time but will not result in a submission delay so any override
  // should be scheduled to executed within the window allowed by synchronizer.
  // Optional
  MinLedgerTime min_ledger_time = 8;

  // If no ``transaction_format`` is provided, a default will be used where ``transaction_shape`` is set to
  // TRANSACTION_SHAPE_ACS_DELTA, ``event_format`` is defined with ``filters_by_party`` containing wildcard-template
  // filter for all original ``act_as`` and ``read_as`` parties and the ``verbose`` flag is set.
  // When the ``transaction_shape`` TRANSACTION_SHAPE_ACS_DELTA shape is used (explicitly or is defaulted to as explained above),
  // events will only be returned if the submitting party is hosted on this node.
  // Optional
  TransactionFormat transaction_format = 9;
}

message ExecuteSubmissionAndWaitForTransactionResponse {
  // The transaction that resulted from the submitted command.
  // The transaction might contain no events (request conditions result in filtering out all of them).
  // Required
  Transaction transaction = 1;
}

message MinLedgerTime {
  oneof time {
    // Lower bound for the ledger time assigned to the resulting transaction.
    // The ledger time of a transaction is assigned as part of command interpretation.
    // Important note: for interactive submissions, if the transaction depends on time, it **must** be signed
    // and submitted within a time window around the ledger time assigned to the transaction during the prepare method.
    // The time delta around that ledger time is a configuration of the ledger, usually short, around 1 minute.
    // If however the transaction does not depend on time, the available time window to sign and submit the transaction is bound
    // by the preparation time, which is also assigned in the "prepare" step (this request),
    // but can be configured with a much larger skew, allowing for more time to sign the request (in the order of hours).
    // Must not be set at the same time as min_ledger_time_rel.
    // Optional
    google.protobuf.Timestamp min_ledger_time_abs = 1;

    // Same as min_ledger_time_abs, but specified as a duration, starting from the time this request is received by the server.
    // Must not be set at the same time as min_ledger_time_abs.
    // Optional
    google.protobuf.Duration min_ledger_time_rel = 2;
  }
}

/**
 * Prepared Transaction Message
 */
message PreparedTransaction {
  // Daml Transaction representing the ledger effect if executed. See below
  DamlTransaction transaction = 1;
  // Metadata context necessary to execute the transaction
  Metadata metadata = 2;
}

// Transaction Metadata
// Refer to the hashing documentation for information on how it should be hashed.
message Metadata {
  message SubmitterInfo {
    repeated string act_as = 1;
    string command_id = 2;
  }

  message GlobalKeyMappingEntry {
    interactive.GlobalKey key = 1;
    optional Value value = 2;
  }

  message InputContract {
    oneof contract {
      // When new versions will be added, they will show here
      interactive.transaction.v1.Create v1 = 1;
    }
    uint64 created_at = 1000;
    reserved 1001; // Used to contain driver_metadata, now contained in event_blob
    bytes event_blob = 1002;
  }

  /* ************************************************** */
  /* ** Metadata information that needs to be signed ** */
  /* ************************************************** */

  // this used to contain the ledger effective time
  reserved 1;

  SubmitterInfo submitter_info = 2;
  string synchronizer_id = 3;
  uint32 mediator_group = 4;
  string transaction_uuid = 5;
  uint64 preparation_time = 6;
  repeated InputContract input_contracts = 7;

  /*
   * Where ledger time constraints are imposed during the execution of the contract they will be populated
   * in the fields below. These are optional because if the transaction does NOT depend on time, these values
   * do not need to be set.
   * The final ledger effective time used will be chosen when the command is submitted through the [execute] RPC.
   * If the ledger effective time is outside of any populated min/max bounds then a different transaction
   * can result, that will cause a confirmation message rejection.
   */
  optional uint64 min_ledger_effective_time = 9;
  optional uint64 max_ledger_effective_time = 10;

  /* ********************************************************** */
  /* ** Metadata information that does NOT need to be signed ** */
  /* ********************************************************** */

  // Contextual information needed to process the transaction but not signed, either because it's already indirectly
  // signed by signing the transaction, or because it doesn't impact the ledger state
  repeated GlobalKeyMappingEntry global_key_mapping = 8;

  // Maximum timestamp at which the transaction can be recorded onto the ledger via the synchronizer `synchronizer_id`.
  // If submitted after it will be rejected even if otherwise valid, in which case it needs to be prepared and signed again
  // with a new valid max_record_time.
  // Unsigned in 3.3 to avoid a breaking protocol change
  // Will be signed in 3.4+
  // Set max_record_time in the PreparedTransactionRequest to get this field set accordingly
  optional uint64 max_record_time = 11;
}

/*
 * Daml Transaction.
 * This represents the effect on the ledger if this transaction is successfully committed.
 */
message DamlTransaction {
  message NodeSeed {
    int32 node_id = 1;
    bytes seed = 2;
  }

  // A transaction may contain nodes with different versions.
  // Each node must be hashed using the hashing algorithm corresponding to its specific version.
  // [docs-entry-start: DamlTransaction.Node]
  message Node {
    string node_id = 1;

    // Versioned node
    oneof versioned_node {
      // Start at 1000 so we can add more fields before if necessary
      // When new versions will be added, they will show here
      interactive.transaction.v1.Node v1 = 1000;
    }
  }
  // [docs-entry-end: DamlTransaction.Node]

  // serialization version, will be >= max(nodes version)
  string version = 1;
  // Root nodes of the transaction
  repeated string roots = 2;
  // List of nodes in the transaction
  repeated Node nodes = 3;
  // Node seeds are values associated with certain nodes used for generating cryptographic salts
  repeated NodeSeed node_seeds = 4;
}

message GetPreferredPackageVersionRequest {
  // The parties whose participants' vetting state should be considered when resolving the preferred package.
  // Required
  repeated string parties = 1;
  // The package-name for which the preferred package should be resolved.
  // Required
  string package_name = 2;

  // The synchronizer whose vetting state should be used for resolving this query.
  // If not specified, the vetting states of all synchronizers to which the participant is connected are used.
  // Optional
  string synchronizer_id = 3;

  // The timestamp at which the package vetting validity should be computed
  // on the latest topology snapshot as seen by the participant.
  // If not provided, the participant's current clock time is used.
  // Optional
  google.protobuf.Timestamp vetting_valid_at = 4;
}

message GetPreferredPackageVersionResponse {
  // Not populated when no preferred package is found
  // Optional
  PackagePreference package_preference = 1;
}

message PackagePreference {
  // The package reference of the preferred package.
  // Required
  PackageReference package_reference = 1;

  // The synchronizer for which the preferred package was computed.
  // If the synchronizer_id was specified in the request, then it matches the request synchronizer_id.
  // Required
  string synchronizer_id = 2;
}

// Defines a package-name for which the commonly vetted package with the highest version must be found.
message PackageVettingRequirement {
  // The parties whose participants' vetting state should be considered when resolving the preferred package.
  // Required
  repeated string parties = 1;

  // The package-name for which the preferred package should be resolved.
  // Required
  string package_name = 2;
}

message GetPreferredPackagesRequest {
  // The package-name vetting requirements for which the preferred packages should be resolved.
  //
  // Generally it is enough to provide the requirements for the intended command's root package-names.
  // Additional package-name requirements can be provided when additional Daml transaction informees need to use
  // package dependencies of the command's root packages.
  //
  // Required
  repeated PackageVettingRequirement package_vetting_requirements = 1;

  // The synchronizer whose vetting state should be used for resolving this query.
  // If not specified, the vetting states of all synchronizers to which the participant is connected are used.
  // Optional
  string synchronizer_id = 2;

  // The timestamp at which the package vetting validity should be computed
  // on the latest topology snapshot as seen by the participant.
  // If not provided, the participant's current clock time is used.
  // Optional
  google.protobuf.Timestamp vetting_valid_at = 3;
}

message GetPreferredPackagesResponse {
  // The package references of the preferred packages.
  // Must contain one package reference for each requested package-name.
  //
  // If you build command submissions whose content depends on the returned
  // preferred packages, then we recommend submitting the preferred package-ids
  // in the ``package_id_selection_preference`` of the command submission to
  // avoid race conditions with concurrent changes of the on-ledger package vetting state.
  //
  // Required
  repeated PackageReference package_references = 1;

  // The synchronizer for which the package preferences are computed.
  // If the synchronizer_id was specified in the request, then it matches the request synchronizer_id.
  // Required
  string synchronizer_id = 2;
}
```

### Python

It is recommended to use a dedicated python environment to avoid conflicting dependencies. Considering using [venv](https://docs.python.org/3/library/venv.html).

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the setup script to generate the necessary python files to interact with Canton's gRPC interface:

```
./setup.sh
```

### Shell

For a terminal-based approach, install the following tools:

* [grpcurl](https://github.com/fullstorydev/grpcurl)
* [openssl](https://www.openssl.org/)
* [jq](https://jqlang.org/)

## 1. 准备交易

Transform `Ledger Command` into a `Daml Transaction`.

Bash

Request:

> ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
> echo '{
>   "user_id": "demo_app",
>   "command_id": "f2ec4d8f-ccc1-402b-b278-7556fdd2b412",
>   "act_as": ["alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"],
>   "synchronizer_id": "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3",
>   "commands": [
>     {
>       "create": {
>         "template_id": {
>           "package_id": "#canton-builtin-admin-workflow-ping",
>           "module_name": "Canton.Internal.Ping",
>           "entity_name": "Ping"
>         },
>         "create_arguments": {
>           "record_id": null,
>           "fields": [
>             {
>                 "label" :"id",
>                 "value": { "text": "ping_id" }
>             },
>             {
>                 "label" :"initiator",
>                 "value": { "party": "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e" }
>             },
>             {
>                 "label" :"responder",
>                 "value": { "party": "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a" }
>             }
>           ]
>         }
>       }
>     }
>   ]
> }' > create_ping_prepare_request.json
>
> cat "create_ping_prepare_request.json" | grpcurl -emit-defaults -plaintext -d @ localhost:4001 com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/PrepareSubmission > create_ping_prepare_response.json
> ```

Record the response in `create_ping_prepare_response.json` to make it easier to submit the transaction afterwards. Now inspect the response with

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cat create_ping_prepare_response.json
```

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "prepared_transaction": {
    "transaction": {
      "version": "2.1",
      "roots": [
        "0"
      ],
      "nodes": [
        {
          "node_id": "0",
          "v1": {
            "create": {
              "lf_version": "2.1",
              "contract_id": "004c3409aa2e8f8e22604d58ea6211f667df2bae4abc7984a95d76b3d120b8bd85",
              "package_name": "canton-builtin-admin-workflow-ping",
              "template_id": {
                "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
                "moduleName": "Canton.Internal.Ping",
                "entityName": "Ping"
              },
              "argument": {
                "record": {
                  "recordId": {
                    "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
                    "moduleName": "Canton.Internal.Ping",
                    "entityName": "Ping"
                  },
                  "fields": [
                    {
                      "label": "id",
                      "value": {
                        "text": "ping_id"
                      }
                    },
                    {
                      "label": "initiator",
                      "value": {
                        "party": "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
                      }
                    },
                    {
                      "label": "responder",
                      "value": {
                        "party": "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
                      }
                    }
                  ]
                }
              },
              "signatories": [
                "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
              ],
              "stakeholders": [
                "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e",
                "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
              ]
            }
          }
        }
      ],
      "node_seeds": [
        {
          "seed": "Gv8neKcoUyIvsa5vdfjUxwGQLGuJOUeVO3j26YB4vOQ="
        }
      ]
    },
    "metadata": {
      "submitter_info": {
        "act_as": [
          "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
        ],
        "command_id": "f2ec4d8f-ccc1-402b-b278-7556fdd2b412"
      },
      "synchronizer_id": "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3",
      "transaction_uuid": "0c36b6ea-a5a8-40ee-8708-d47589f34db7",
      "submission_time": "1739897973772660"
    }
  },
  "prepared_transaction_hash": "lafpRryDAe5lA8sBONBv0u2umlGKtnJXnhec/7AN+Ro=",
  "hashing_scheme_version": "HASHING_SCHEME_VERSION_V2"
}
```

Python

<Warning>
  Ensure you have followed the setup instructions for Python before proceeding.
</Warning>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
import argparse
import sys

import grpc
import uuid
from google.protobuf.json_format import MessageToJson
from com.daml.ledger.api.v2.interactive import interactive_submission_service_pb2_grpc
from com.daml.ledger.api.v2.interactive import interactive_submission_service_pb2
from com.daml.ledger.api.v2 import commands_pb2, value_pb2, completion_pb2, crypto_pb2
from external_party_onboarding_admin_api import onboard_external_party
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from daml_transaction_hashing_v2 import (
    create_nodes_dict,
    encode_prepared_transaction,
    HASHING_SCHEME_VERSION_V2,
)
from com.daml.ledger.api.v2 import (
    command_completion_service_pb2,
    command_completion_service_pb2_grpc,
    update_service_pb2,
    update_service_pb2_grpc,
    event_pb2,
    state_service_pb2_grpc,
    state_service_pb2,
    transaction_filter_pb2,
    event_query_service_pb2_grpc,
    event_query_service_pb2,
)
import os
import json
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
initiator = "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
responder = "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
synchronizer_id = "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3"
user_id = "demo_app"
party = "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
lapi_port="4001"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
ping_template_id = value_pb2.Identifier(
    package_id="#canton-builtin-admin-workflow-ping",
    module_name="Canton.Internal.Ping",
    entity_name="Ping",
)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
lapi_channel = grpc.insecure_channel(f"localhost:{lapi_port}")
# Interactive submission service client - used to submit externally signed transactions
iss_client = interactive_submission_service_pb2_grpc.InteractiveSubmissionServiceStub(
    lapi_channel
)
# Command completion service client - used to observe command execution results
ccs_client = command_completion_service_pb2_grpc.CommandCompletionServiceStub(
    lapi_channel
)
# Update service client - used to query transactions once they've completed
us_client = update_service_pb2_grpc.UpdateServiceStub(lapi_channel)
# State service client - used to query active contracts
state_client = state_service_pb2_grpc.StateServiceStub(lapi_channel)
# Event query service client - used to retrieve event information of a completed transaction
eqs_client = event_query_service_pb2_grpc.EventQueryServiceStub(lapi_channel)
```

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def prepare_create_ping_contract(
    initiator: str,
    responder: str,
    synchronizer_id: str,
) -> interactive_submission_service_pb2.PrepareSubmissionResponse:
    ping_create_command = commands_pb2.Command(
        create=commands_pb2.CreateCommand(
            template_id=ping_template_id,
            create_arguments=value_pb2.Record(
                record_id=None,
                fields=[
                    value_pb2.RecordField(
                        label="id", value=value_pb2.Value(text="ping_id")
                    ),
                    value_pb2.RecordField(
                        label="initiator", value=value_pb2.Value(party=initiator)
                    ),
                    value_pb2.RecordField(
                        label="responder", value=value_pb2.Value(party=responder)
                    ),
                ],
            ),
        )
    )

    print("Preparing create ping transaction")
    # Prepare the submission request
    prepare_create_request = (
        interactive_submission_service_pb2.PrepareSubmissionRequest(
            user_id=user_id,
            command_id=str(uuid.uuid4()),
            act_as=[initiator],
            read_as=[initiator],
            synchronizer_id=synchronizer_id,
            commands=[ping_create_command],
        )
    )

    # Call the PrepareSubmission RPC
    prepare_create_response = iss_client.PrepareSubmission(prepare_create_request)

    return prepare_create_response
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
prepare_create_response = prepare_create_ping_contract(
    initiator, responder, synchronizer_id
)
if not auto_accept:
    inspect_and_validate_transaction(prepare_create_response.prepared_transaction)
print(
    "Returned transaction hash is "
    + prepare_create_response.prepared_transaction_hash.hex()
)
prepared_create_transaction = prepare_create_response.prepared_transaction
```

### 请求

* `user_id`: Identifier for the application interacting with the ledger.
* `command_id`: Unique, random string identifying this specific command. Each command submission must have a new and unique `command_id`.
* `act_as`: ID of the party issuing the command.
* `synchronizer_id`: ID of the synchronizer that processes the transaction upon submission.
* `commands`: Ledger commands for submission. In this case, it shows the creation of a Ping contract with `Alice` as the initiator, `Bob` as the responder, and a `ping_id` value. See the [Ledger API command reference](/reference/grpc-ledger-api-reference/com-daml-ledger-api-v2) for details.

### 响应

#### 交易

Represents the explicit ledger changes upon successful commitment.

* `version`: Version of the transaction. This is also called `LF Version`.
* `roots`: List of root node ids. A Daml transaction is a list of trees. The nodes are flattened in a single list (see below). The root node ids design the root node of each individual tree in the transaction.

<Note>
  A current limitation of externally signed transactions is that they can only contain a single root node, and therefore a single transaction tree.
</Note>

* `nodes`: List of all nodes in the transaction. There are 4 types of nodes: `Create`, `Exercise`, `Fetch` and `Rollback`. The number, type and content of each node depends on the Daml model and the state of the ledger.
* `node_seeds`: List of seeds used by the Canton protocol to generate cryptographically secure salts. They can be ignored.

#### 元数据

Additional information required for transaction processing.

* `ledger_effective_time`: Time picked during the interpretation of the command into a transaction. Set if and only if the daml model makes use of time.

* `submitter_info`: Contains the `act_as` party and `command_id`

* `synchronizer_id`: Synchronizer that will be used for transaction processing

* `transaction_uuid`: Unique value generated by the prepare endpoint to uniquely identify this transaction

  > * The transaction UUID is randomly selected during the `prepare` step and is fixed from that point forward. This allows the mediator node to de-duplicate transactions and prevent replays.

* `mediator_group`: Group of mediators that will gather confirmation responses for the transaction. Can be ignored.

* `submission_time`: The timestamp that the Canton protocol will use as a submission time to perform validations (e.g for de-duplication)

* `disclosed_events`: Existing input contracts used in the transaction

* `global_key_mapping`: Unused in the current version, can be ignored.

#### 哈希

* `prepared_transaction_hash`: Pre-computed transaction hash. For security reasons the hash should be re-computed client-side as mentioned in the Compute transaction hash section.

<Note>
  The `prepare` API can return additional details on how the Canton node is hashing the transaction to help troubleshoot hash-related errors (for example: pre-computed and re-computed hash mismatch).
  To enable it:

  1. Enable verbose hashing on the participant config `ledger-api.interactive-submission-service.enable-verbose-hashing = true`.
  2. Set the `verbose_hashing` field in the `PrepareSubmissionRequest` to `true`.
</Note>

#### 哈希方案版本

Version of the hashing scheme:

| Protocol Version | Hashing Scheme Version       |
| ---------------- | ---------------------------- |
| 33               | HASHING\_SCHEME\_VERSION\_V2 |

<Note>
  If the gRPC Ledger API authorization is enabled, the user must have the `readAs` claim on behalf of `Alice` to call the `prepare` endpoint.
</Note>

#### 流量成本估算

Estimates the traffic cost for the Participant Node that submits the transaction to the synchronizer. See the API documentation for details on the estimation response fields.

The precision of the estimation is influenced by several factors that cannot be known when the transaction is being prepared. Additionally, the traffic cost will be incurred by the node submitting the transaction, not the one preparing it. When they are the same, the cost estimation will be more accurate. The following factors contribute to the uncertainty of the cost estimation:

> * Hosting relationship of the submitting party with the executing node
> * Number and type of external signatures provided upon submission of the transaction
> * Topology state of the network when the transaction will be submitted
> * Request amplification during submission
> * Part of the transaction that will be confirmed (root view or sub views)
> * Whether nodes approve or reject the transaction
> * IDs of contract created within the transaction are not suffixed in the cost estimation, whereas they are suffixed in the actual submission
> * Whether session signing keys are enabled on the submitting or confirming nodes

In most cases the impact of those factors is low and the variance they cause can generally be expected to be 10% or less. Hints can be specified in the prepare request to help improve the precision of the estimation.

It's worth noting that request amplification can significantly increase traffic cost when triggered. The estimation provided is valid for a single confirmation request submission. Subsequent amplified requests sent will cost additional traffic cost as they correspond to a new confirmation request being sent.

<Tip>
  Traffic cost estimation is enabled by default. To disable it, set the disabled field in the `CostEstimationHints` message to `true`.
</Tip>

For details on traffic management, read the related explanation page.

## 2. 校验交易

Deserialize and inspect the transaction to verify its correctness before proceeding. The initiator of the transaction must be able to inspect and validate it to ensure it matches their intent before proceeding. See the Trust Model for guidance.

## 3. 计算交易哈希

强烈建议客户端根据交易与元数据重新计算哈希 be recomputed from the transaction and metadata to verify correctness. The pre-computed hash provided in the `Prepare` step is for debugging purposes.

* The hashing algorithm specification is available here as well as in the release artifact under `protobuf/ledger-api/com/daml/ledger/api/v2/interactive/README.md`
* An example implementation in python is available in the release articact under `examples/08-interactive-submission/daml_transaction_hashing_v2.py`

## 4. 签署交易哈希

Using `Alice`'s protocol signing private key, sign the hash.

<Note>
  Technically what is needed is the ability to sign with `Alice`'s key, not the key itself. The management of the key can be delegated to a wallet, HSM or crypto custody provider. In this tutorial the key is managed locally and explicitly to demonstrate the signing process. Refer to the onboarding tutorial for details on how to generate a key for this tutorial.
</Note>

Bash

Assuming `Alice's` private key is stored in a file called `alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e-private-key.der`, he hash can be signed using `openssl`.

<Note>
  In this tutorial the hash retrieved from the response of step 1 will be signed, without re-computing it as suggested in step 3. For an example of how to re-compute the hash, see the `Python` example.
</Note>

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
TRANSACTION_HASH=$(cat create_ping_prepare_response.json | jq -r .prepared_transaction_hash)
PREPARED_TRANSACTION=$(cat create_ping_prepare_response.json | jq -r .prepared_transaction)
SIGNATURE=$(echo -n "$TRANSACTION_HASH" | base64 --decode | openssl pkeyutl -rawin -inkey alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e-private-key.der -keyform DER -sign | openssl base64 -e -A)
```

Python

The Python example demo includes an implementation of the transaction hashing algorithm. In this example, `party_private_key` is assumed to be an `EllipticCurvePrivateKey` Python object containing Alice's private key. If the onboarding tutorial was followed, this key should already be available.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
transaction_hash = encode_prepared_transaction(
    prepared_transaction, create_nodes_dict(prepared_transaction)
)
print("Computed hash: " + transaction_hash.hex())
# Sign it
signature = party_private_key.sign(
    transaction_hash, signature_algorithm=ec.ECDSA(hashes.SHA256())
)
```

## 5. 执行交易

Submit the transaction and its signature to the ledger.

Bash

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl -emit-defaults -plaintext -d @ localhost:4001 com.daml.ledger.api.v2.interactive.InteractiveSubmissionService/ExecuteSubmission <<EOM
    {
      "prepared_transaction": $PREPARED_TRANSACTION,
      "hashing_scheme_version": "HASHING_SCHEME_VERSION_V2",
      "user_id": "demo_app",
      "submission_id": "51dd5a0e-2ab6-4ca4-aa9d-9333fb603eb0",
      "party_signatures": {
        "signatures": [
          {
            "party": "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e",
            "signatures": [
              {
                "format": "SIGNATURE_FORMAT_DER",
                "signature": "$SIGNATURE",
                "signing_algorithm_spec": "SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256",
                "signed_by": "1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
              }
            ]
          }
        ]
      }
    }
    EOM
```

Python

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Create the execute request
execute_request = interactive_submission_service_pb2.ExecuteSubmissionRequest(
    prepared_transaction=prepared_transaction,
    user_id=user_id,
    party_signatures=interactive_submission_service_pb2.PartySignatures(
        signatures=[
            interactive_submission_service_pb2.SinglePartySignatures(
                party=party,
                signatures=[
                    crypto_pb2.Signature(
                        format=crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
                        signature=signature,
                        signed_by=pub_fingerprint,
                        signing_algorithm_spec=crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
                    )
                ],
            )
        ]
    ),
    hashing_scheme_version=HASHING_SCHEME_VERSION_V2,
    submission_id=str(uuid.uuid4()),
)

# Submit the transaction to the ledger
iss_client.ExecuteSubmission(execute_request)
```

In the request, note the presence of:

* `submission_id`: Random string uniquely generated for this submission. This differs from the `command_id` in that a retry of this same prepared transaction would necessitate a new `submission_id`. The `submission_id` is used to correlate several submissions of the same command with completion events (See next step for more on completion events).

  > * Because `submission_id` is not part of the signature, a command can be re-submitted with a different `submission_id` without requiring a new signature.

* `signatures`: Object containing the signature of the transaction hash, along with metadata. In particular:

  > * `signing_algorithm_spec`: Will vary depending on the key used during onboarding.
  > * `signed_by`: Fingerprint of the protocol signing *public* key of `Alice`. This tutorial assumes the same key was used to create `Alice`'s namespace and her protocol signing key. This is why the fingerprint of the signing key matches the second part of her Party Id (after `::`). For more details check out the onboarding tutorial and the [Daml parties guide](/appdev/deep-dives/manage-daml-parties).

<Note>
  If the gRPC Ledger API authorization is enabled, the user must have the `actAs` claim on behalf of `Alice` to call the `execute` endpoint.
</Note>

## 6. 观察交易结果

Monitor the completion stream for transaction confirmation, then retrieve the contract ID and binary blob representation.

Bash

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl -emit-defaults -plaintext -d @ localhost:4001 com.daml.ledger.api.v2.CommandCompletionService/CompletionStream <<EOM
{
  "user_id": "demo_app",
  "parties": ["alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"]
}
EOM
```

Wait until observing a completion event:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "completion": {
    "command_id": "f2ec4d8f-ccc1-402b-b278-7556fdd2b412",
    "status": {
      "code": 0,
      "message": "",
      "details": [

      ]
    },
    "update_id": "122049bb312e4ba2e6f142b2221f58589b75b0ad253685d3fc82f5758686b037efdb",
    "user_id": "demo_app",
    "act_as": [
      "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
    ],
    "submission_id": "51dd5a0e-2ab6-4ca4-aa9d-9333fb603eb0",
    "deduplication_offset": "0",
    "trace_context": {
      "traceparent": "00-65bc60e1399cad60cd2bceea6eddf4a7-9730a005a8779537-01"
    },
    "offset": "24",
    "synchronizer_time": {
      "synchronizer_id": "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3",
      "record_time": "2025-02-19T17:21:50.512523Z"
    }
  }
}
```

* `status.code`: A value of `0` indicates the command completed successfully
* `offset`: Ledger offset for the event
* `update_id`: Unique Id for this completion event
* `submission_id`: The submission Id chosen in the submission step

Let's record both the `offset` and `update_id` for the next steps.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
UPDATE_ID="122049bb312e4ba2e6f142b2221f58589b75b0ad253685d3fc82f5758686b037efdb"
OFFSET="24"
```

<Note>
  You may need to interrupt the command with `Ctrl-C` as the completion stream is a gRPC server streaming RPC which waits for updates from the server until interrupted.
</Note>

Let's now retrieve the corresponding transaction:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl -emit-defaults -plaintext -d @ localhost:4001 com.daml.ledger.api.v2.UpdateService/GetUpdateById <<EOM
{
  "update_id": "$UPDATE_ID",
  "update_format": {
    "include_transactions": {
      "event_format": {
        "filters_by_party": {
          "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e": {
            "cumulative": [
              {
                "wildcard_filter": {
                  "include_created_event_blob": true
                }
              }
            ]
          }
        }
      },
      "transaction_shape": TRANSACTION_SHAPE_ACS_DELTA
    }
  }
}
EOM
```

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "transaction": {
    "update_id": "122049bb312e4ba2e6f142b2221f58589b75b0ad253685d3fc82f5758686b037efdb",
    "command_id": "f2ec4d8f-ccc1-402p-b278-7556fdd2b412",
    "workflow_id": "",
    "effective_at": "2025-02-19T17:21:50.485967Z",
    "events": [
      {
        "created": {
          "offset": "24",
          "node_id": 0,
          "contract_id": "00aa1fb173904244c175e87ecc226ab652ecce76554c7f5700efd21d11484a2877ca101220a19a8de75c840e5063010386a811ca392e848441102749bf522cd394a816750a",
          "template_id": {
            "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
            "moduleName": "Canton.Internal.Ping",
            "entityName": "Ping"
          },
          "contract_key": null,
          "create_arguments": {
            "recordId": {
              "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
              "moduleName": "Canton.Internal.Ping",
              "entityName": "Ping"
            },
            "fields": [
              {
                "label": "id",
                "value": {
                  "text": "ping_id"
                }
              },
              {
                "label": "initiator",
                "value": {
                  "party": "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
                }
              },
              {
                "label": "responder",
                "value": {
                  "party": "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
                }
              }
            ]
          },
          "created_event_blob": "",
          "interface_views": [

          ],
          "witness_parties": [
            "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
          ],
          "signatories": [
            "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
          ],
          "observers": [
            "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
          ],
          "created_at": "2025-02-19T17:21:50.485967Z",
          "package_name": "canton-builtin-admin-workflow-ping"
        }
      }
    ],
    "offset": "24",
    "synchronizer_id": "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3",
    "trace_context": {
      "traceparent": "00-65bc60e1399cad60cd2bceea6eddf4a7-9730a005a8779537-01"
    },
    "record_time": "2025-02-19T17:21:50.512523Z"
  }
}
```

The `events` list includes a `created object`, representing the newly created contract. Extract the corresponding `contract_id` for reference. To finalize this step, retrieve the binary blob representation of the created contract. This serialized form will be required when executing a choice on the contract in Part 2.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl -emit-defaults -plaintext -d @ localhost:4001 com.daml.ledger.api.v2.StateService/GetActiveContracts <<EOM
{
  "event_format": {
    "filters_by_party": {
      "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e": {
        "cumulative": [
          {
            "wildcard_filter": {
               "include_created_event_blob": true
            }
          }
        ]
      }
    }
  },
  "active_at_offset": "$OFFSET"
}
EOM
```

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "workflow_id": "",
  "active_contract": {
    "created_event": {
      "offset": "24",
      "node_id": 0,
      "contract_id": "00aa1fb173904244c175e87ecc226ab652ecce76554c7f5700efd21d11484a2877ca101220a19a8de75c840e5063010386a811ca392e848441102749bf522cd394a816750a",
      "template_id": {
        "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
        "moduleName": "Canton.Internal.Ping",
        "entityName": "Ping"
      },
      "contract_key": null,
      "create_arguments": {
        "recordId": {
          "packageId": "9a19e9cc152538d3ad3b99b933ccf881e53b193ee6af17bdd9a65905a6e1f8ab",
          "moduleName": "Canton.Internal.Ping",
          "entityName": "Ping"
        },
        "fields": [
          {
            "label": "id",
            "value": {
              "text": "ping_id"
            }
          },
          {
            "label": "initiator",
            "value": {
              "party": "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
            }
          },
          {
            "label": "responder",
            "value": {
              "party": "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
            }
          }
        ]
      },
      "created_event_blob": "CgMyLjESuQQKRQBjTUl2dyqzat8236jWAVQ7N5fKufP9tC25XfYKc8tcGMoQEiCC572aoJidPFPbnuK4QKF9wAuxGP1l7xumvhhNwM7khRIOQWRtaW5Xb3JrZmxvd3MaYApAOWExOWU5Y2MxNTI1MzhkM2FkM2I5OWI5MzNjY2Y4ODFlNTNiMTkzZWU2YWYxN2JkZDlhNjU5MDVhNmUxZjhhYhIGQ2FudG9uEghJbnRlcm5hbBIEUGluZxoEUGluZyKwAWqtAQoLCglCB3BpbmdfaWQKTwpNOkthbGljZTo6MTIyMGQ0NjZhNWQ5NmEzNTA5NzM2YzgyMWUyNWZlODFmYzhhNzNmMjI2ZDkyZTU3ZTk0YTY1MTcwZTU4YjA3ZmMwOGUKTQpLOklib2I6OjEyMjAyNTRkMDYwOTViNDA3ZjhjNmEzNzhiNmZjNDQzYTY3ZDMzNTZhYjhlZGZiZjEzNzhjYjNlNDQyMThkZTMyYzhhKkthbGljZTo6MTIyMGQ0NjZhNWQ5NmEzNTA5NzM2YzgyMWUyNWZlODFmYzhhNzNmMjI2ZDkyZTU3ZTk0YTY1MTcwZTU4YjA3ZmMwOGUySWJvYjo6MTIyMDI1NGQwNjA5NWI0MDdmOGM2YTM3OGI2ZmM0NDNhNjdkMzM1NmFiOGVkZmJmMTM3OGNiM2U0NDIxOGRlMzJjOGE544B3nIAuBgBCKgomCiQIARIgZrl+7TfHbM1LcYFnlh0pNxS091G09Le5mhD5PUCvwmkQHg==",
      "interface_views": [

      ],
      "witness_parties": [
        "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
      ],
      "signatories": [
        "alice::1220d466a5d96a3509736c821e25fe81fc8a73f226d92e57e94a65170e58b07fc08e"
      ],
      "observers": [
        "bob::1220254d06095b407f8c6a378b6fc443a67d3356ab8edfbf1378cb3e44218de32c8a"
      ],
      "created_at": "2025-02-19T15:42:56.032995Z",
      "package_name": "canton-builtin-admin-workflow-ping"
    },
    "synchronizer_id": "da::12203c0ecb446b35b0efa78e0bda9fd91716855866150a5eb7611a2ed5d418129de3",
    "reassignment_counter": "0"
  }
}
```

The request above might return multiple contracts if additional ones were created after the offset. The relevant contract should be identified by matching its `contract_id`. The `created_event_blob` contains a serialized version of the contract, which can be used in subsequent transactions to exercise choices on it.

Python

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
update_request = command_completion_service_pb2.CompletionStreamRequest(
    user_id=user_id, parties=[party]
)
completion_stream = ccs_client.CompletionStream(update_request)
for update in completion_stream:
    if (
        update.HasField("completion")
        and update.completion.submission_id == execute_request.submission_id
    ):
        completion: completion_pb2.Completion = update.completion
        break

update_response: update_service_pb2.GetUpdateResponse = (
    us_client.GetUpdateById(
        update_service_pb2.GetUpdateByIdRequest(
            update_id=completion.update_id,
            update_format=transaction_filter_pb2.UpdateFormat(
                include_transactions=transaction_filter_pb2.TransactionFormat(
                    event_format=get_event_format(party),
                    transaction_shape=transaction_filter_pb2.TransactionShape.TRANSACTION_SHAPE_ACS_DELTA
                )
            )
        )
    )
)
for event in update_response.transaction.events:
    if event.HasField("created"):
        contract_id = event.created.contract_id
        break
    if event.HasField("archived"):
        contract_id = event.archived.contract_id
        break
```

At this stage, the contract has been successfully created, and its `contract_id` is available.

<Tip>
  The execution and extraction of the `contract_id` above are summarized in the following function, which is reused in Part 2 of the tutorial:

  ```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
  def execute_and_get_contract_id(
      prepared_transaction: interactive_submission_service_pb2.PreparedTransaction,
      party: str,
      party_private_key: EllipticCurvePrivateKey,
      pub_fingerprint: str,
  ):
      # [Compute transaction hash]
      transaction_hash = encode_prepared_transaction(
          prepared_transaction, create_nodes_dict(prepared_transaction)
      )
      print("Computed hash: " + transaction_hash.hex())
      # Sign it
      signature = party_private_key.sign(
          transaction_hash, signature_algorithm=ec.ECDSA(hashes.SHA256())
      )
      # [Signed hash]
      # Create the execute request
      execute_request = interactive_submission_service_pb2.ExecuteSubmissionRequest(
          prepared_transaction=prepared_transaction,
          user_id=user_id,
          party_signatures=interactive_submission_service_pb2.PartySignatures(
              signatures=[
                  interactive_submission_service_pb2.SinglePartySignatures(
                      party=party,
                      signatures=[
                          crypto_pb2.Signature(
                              format=crypto_pb2.SignatureFormat.SIGNATURE_FORMAT_DER,
                              signature=signature,
                              signed_by=pub_fingerprint,
                              signing_algorithm_spec=crypto_pb2.SigningAlgorithmSpec.SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256,
                          )
                      ],
                  )
              ]
          ),
          hashing_scheme_version=HASHING_SCHEME_VERSION_V2,
          submission_id=str(uuid.uuid4()),
      )

      # Submit the transaction to the ledger
      iss_client.ExecuteSubmission(execute_request)
      # [Submitted request]

      # [Waiting for the transaction to show on the completion stream]
      update_request = command_completion_service_pb2.CompletionStreamRequest(
          user_id=user_id, parties=[party]
      )
      completion_stream = ccs_client.CompletionStream(update_request)
      for update in completion_stream:
          if (
              update.HasField("completion")
              and update.completion.submission_id == execute_request.submission_id
          ):
              completion: completion_pb2.Completion = update.completion
              break

      update_response: update_service_pb2.GetUpdateResponse = (
          us_client.GetUpdateById(
              update_service_pb2.GetUpdateByIdRequest(
                  update_id=completion.update_id,
                  update_format=transaction_filter_pb2.UpdateFormat(
                      include_transactions=transaction_filter_pb2.TransactionFormat(
                          event_format=get_event_format(party),
                          transaction_shape=transaction_filter_pb2.TransactionShape.TRANSACTION_SHAPE_ACS_DELTA
                      )
                  )
              )
          )
      )
      for event in update_response.transaction.events:
          if event.HasField("created"):
              contract_id = event.created.contract_id
              break
          if event.HasField("archived"):
              contract_id = event.archived.contract_id
              break
      # [Got Contract Id from Transaction]

      return contract_id
  ```
</Tip>

To complete this part, the next step is to retrieve the binary blob of the creation event for the Ping contract. This serialized representation will be required in Part 2 when executing a choice on the contract.

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def get_active_contracts(party: str):
    ledger_end_response: state_service_pb2.GetLedgerEndResponse = (
        state_client.GetLedgerEnd(state_service_pb2.GetLedgerEndRequest())
    )
    active_contracts_response = state_client.GetActiveContracts(
        state_service_pb2.GetActiveContractsRequest(
            event_format=get_event_format(party),
            active_at_offset=ledger_end_response.offset,
        )
    )
    return active_contracts_response
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
ping_created_event: event_pb2.CreatedEvent
initiator_active_contracts = get_active_contracts(initiator)
# Find the contract in the active contract set
for active_contract_response in initiator_active_contracts:
    if (
        active_contract_response.HasField("active_contract")
        and active_contract_response.active_contract.created_event.contract_id
        == contract_id
    ):
        ping_created_event = active_contract_response.active_contract.created_event
        break
```

This concludes Part 1 of the tutorial. In Part 2, `Bob` exercises the `Respond` choice to archive the contract.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/tutorials/app-dev/external_signing_submission_part_2.rst" hash="cdbe11dc" */}

# Submit Externally Signed Transactions - Part 2

Complete Part 1 before proceeding.

The tutorial illustrates the external signing process using two external parties, `Alice` and `Bob`, leveraging the same Ping Daml Template used in Part 1 of the tutorial.

* In Part 1 `Alice` created a `Ping` contract.
* In Part 2 `Bob` exercises the `Respond` choice on the contract and archives it.

The majority of the work involved in external transaction signing was completed in Part 1. The key addition in Part 2 is utilizing the Ping contract created earlier through **explicit disclosure** and executing the Respond choice on that contract. The overall process remains similar to Part 1.

<Warning>
  This tutorial is for demo purposes. The code snippets should not be used directly in a production environment.
</Warning>

## 设置

To proceed, gather the following information:

* `Bob`'s Party ID, protocol signing private key, and protocol signing public key fingerprint
* Synchronizer ID of the synchronizer to which the participant is connected
* gRPC Ledger API endpoint
* `ping_created_event`: Event retrieved in the last step of Part 1.
* `contract_id`: ID of the contract created in Part 1.

This information should already be known from the onboarding tutorial and the first part of the external signing tutorial.

## Python

If you are following this tutorial in Python, generate gRPC Python classes by following the setup instructions in the `README` in the example folder.

## 行使 `Respond` Choice

This tutorial does not repeat the material covered in Part 1 regarding transaction preparation, validation, signing, and execution, as these steps remain largely the same. Instead, it highlights the key differences from Part 1.

### Prepare the transaction

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
ping_exercise_command = commands_pb2.Command(
    exercise=commands_pb2.ExerciseCommand(
        template_id=ping_template_id,
        contract_id=contract_id,
        choice="Respond",
        choice_argument=value_pb2.Value(
            record=value_pb2.Record(record_id=None, fields=[])
        ),
    )
)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
prepare_exercise_request = interactive_submission_service_pb2.PrepareSubmissionRequest(
    user_id=user_id,
    command_id=str(uuid.uuid4()),
    act_as=[responder],
    read_as=[responder],
    synchronizer_id=synchronizer_id,
    commands=[ping_exercise_command],
    # We need to explicitly disclosed the ping contract we created earlier
    disclosed_contracts=[
        commands_pb2.DisclosedContract(
            template_id=template_id,
            contract_id=contract_id,
            created_event_blob=created_event_blob,
            synchronizer_id=synchronizer_id,
        )
    ],
)

prepare_exercise_response = iss_client.PrepareSubmission(prepare_exercise_request)
```

The `Prepare` request is very similar to the one from Part 1, with the following differences:

* `act_as`: Now the `responder`, `Bob`, instead of the `initiator`, `Alice`. This makes sense because `Bob` is the one exercising the choice on the contract.
* `commands`: The command is now an `Exercise`command instead of a `Create` command. Notably it requires the `contract_id` from Part 1.
* `disclosed_contracts`: The serialized representation of contracts required to process the transaction.

#### 元数据

The only significant difference with Part 1 in the metadata is: `disclosed_events`. This field now contains the input `Ping` contract. It is also included in the hash of the transaction.

<Warning>
  Like in Part 1, the transaction must be validated, hashed and signed. The hash computation and signature is performed by the `execute_and_get_contract_id` function provided at the end of Part 1, as shown in the next section.
</Warning>

### Submit and observe archived contract

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
execute_and_get_contract_id(
    prepared_exercise_transaction,
    responder,
    responder_private_key,
    responder_fingerprint,
)

# The contract was archived by exercising the choice, we get an archived event this time
contract_events = get_events(responder, contract_id)
if contract_events.HasField("archived"):
    print(
        f"Ping contract with ID {contract_events.archived.archived_event.contract_id} has been archived"
    )
else:
    raise Exception("Expected an archive event")
```

By querying the event service and filtering for the contract ID, an archived event is observed, confirming that the contract has been successfully archived.

This concludes the external signing tutorial. The code used in this tutorial is available in the `examples/08-interactive-submission` folder and can be run with

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python interactive_submission.py run-demo
```

## 工具

The scripts mentioned in this tutorial can be used as tools for testing and development purposes

### Decode base64 encoded prepared transaction to JSON

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./setup.sh
python daml_transaction_util.py --decode --base64 <base64_encoded_transaction>
```

### Compute hash of base64 encoded prepared transaction

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./setup.sh
python daml_transaction_util.py --hash --base64 <base64_encoded_transaction>
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
