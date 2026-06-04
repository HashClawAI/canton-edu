---
title: "Token Standard"
slug: "appdev-deep-dives-token-standard"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/token-standard.md"
source_title: "Token Standard"
tags:
  - appdev
  - deep-dives
  - token-standard
---

# Token Standard

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Token Standard

> The Canton Network Token Standard APIs and Daml interfaces

## Overview

* See the [text of the CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) for an overview of the APIs that are part of the Canton Network Token Standard.
* See the [README in its source-code](https://github.com/canton-network/splice/tree/main/token-standard#readme) for background on how to use the APIs.

## Holding UTXO Management

Analogous to Bitcoin, Canton uses a UTXO model, where the UTXOs are all the active contracts that implement the `Holding` interface.

Active `Holding` contracts incur both storage and compute cost on the validator nodes hosting users that own `Holding` contracts and the validator nodes hosting the token administrator. To make efficient use of the network's resources, we thus recommend that wallet providers aim to keep the number of UTXOs per user low, i.e, below \~10 UTXOs per user on average.

This also optimizes traffic costs, as each UTXO input to a transfer costs extra traffic. Furthermore, this recommendation aligns with the incentives put in place by tokens like Canton Coin, which:

* allows at most 100 input contracts for a single transfer, and thus discourages excessive splitting of holdings
* expires coin UTXOs whose initial amount is lower than the accrued holding fee, and thus discourages the creation of dust UTXOs

We recommend wallet providers to implement a UTXO management strategy that:

* prefers the selection of `Holding` UTXOs with small amounts to provide the input holdings to fund a transfer
* asks the user to setup a `MergeDelegation` contract (see docs) as part of wallet onboarding, which enables the wallet provider to automatically merge small `Holding` UTXOs on behalf of the user

<Note>
  `MergeDelegation` contracts also allow wallet providers to run airdrop campaigns jointly with the auto merging of holdings using a single, batched call to airdrop and merge holdings for multiple users and multiple instruments. Furthermore, featured wallet providers earn featured app rewards for performing merges for their users.
</Note>

### Setting up MergeDelegations

<Tabs>
  <Tab title="DevNet (0.6.4)">
    Assuming you are a wallet provider that runs a validator node for your users, you can set up `MergeDelegation` contracts for your users as follows.

    1. Extract the latest version of the `splice-util-token-standard-wallet.dar` file from the release bundle (<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">Download Bundle (DevNet 0.6.4)</a>).
    2. Upload the extracted `.dar` file to your validator node.
    3. Adjust your user onboarding procedure such that the users signs the creation of a `MergeDelegationProposal` contract (see docs).
    4. Accept the `MergeDelegationProposal` contracts by exercising their `Accept` choice using your wallet provider's party.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    Assuming you are a wallet provider that runs a validator node for your users, you can set up `MergeDelegation` contracts for your users as follows.

    1. Extract the latest version of the `splice-util-token-standard-wallet.dar` file from the release bundle (<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">Download Bundle (TestNet 0.6.3)</a>).
    2. Upload the extracted `.dar` file to your validator node.
    3. Adjust your user onboarding procedure such that the users signs the creation of a `MergeDelegationProposal` contract (see docs).
    4. Accept the `MergeDelegationProposal` contracts by exercising their `Accept` choice using your wallet provider's party.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    Assuming you are a wallet provider that runs a validator node for your users, you can set up `MergeDelegation` contracts for your users as follows.

    1. Extract the latest version of the `splice-util-token-standard-wallet.dar` file from the release bundle (<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">Download Bundle (MainNet 0.6.2)</a>).
    2. Upload the extracted `.dar` file to your validator node.
    3. Adjust your user onboarding procedure such that the users signs the creation of a `MergeDelegationProposal` contract (see docs).
    4. Accept the `MergeDelegationProposal` contracts by exercising their `Accept` choice using your wallet provider's party.
  </Tab>
</Tabs>

### Using MergeDelegations

We recommend to use the `MergeDelegation` contracts in a batched fashion as follows.

1. Create a single `BatchMergeUtility` contract (see docs) for your wallet provider's party as part of your validator node's setup.

2. Grant your wallet provider's user the `CanReadAsAnyParty` right on your validator node to allow it to read all users' `Holding` UTXOs.

3. Run a background process that regularly performs the following steps:

   > 1. Determines all users that have more than 10 `Holding` UTXOs. For example, using the DB provided by the [Participant Query Store](/appdev/deep-dives/query-with-pqs); or by reading the Holding contracts directly from the Ledger API of your validator node. The former being the more scalable option.
   >
   > 2. Constructs the transfer choices to merge the extra `Holding` contracts by querying the registry API as explained in `token_standard_usage_executing_factory_choice`.
   >
   > 3. Lookup the `MergeDelegation` contract for each user and construct the corresponding call to exercise the `MergeDelegation_Merge` choice.
   >
   > 4. Assemble batches of \~100 merge delegation choices into a single call to the `BatchMergeUtility_MergeHoldings` choice.
   >
   > 5. Lookup the contract-id of the `BatchMergeUtility` contract that you setup above.
   >
   > 6. Execute the batched merge by exercising the `BatchMergeUtility_MergeHoldings` choice using your wallet provider user on your validator node. Use the Ledger API to exercise the choice and make sure that you add all disclosed contracts obtained from the previous steps to the single call.
   >
   >    Note that for you can execute multiple batches in parallel for higher throughput.

Optionally, you can add transfers from your operator party to the merge calls to implement airdrop campaigns in a batched fashion.

### Upgrading from custom MergeDelegation implementations

Some wallet providers already implement their own custom merge delegation contracts. They can continue to use them alongside the `MergeDelegation` contracts provided by Splice. There is no requirement to upgrade to the Splice-provided contracts.

However, if you would like to upgrade to the Splice-provided contracts (e.g., to benefit from the additional features), then you can do so as follows.

1. Add a `CustomMergeDelegation_Upgrade` choice to your `CustomMergeDelegation` template that creates a `MergeDelegation` contract for the user. Make the choice `consuming`, so that the old `CustomMergeDelegation` contract is archived as part of exercising the upgrade choice.
2. Bump the version of your custom merge delegation `.dar` file and build a new release.
3. Upload the new `custom-merge-delegation.dar` file to your validator node.
4. Call the `CustomMergeDelegation_Upgrade` choice on all existing `CustomMergeDelegation` contracts to upgrade them to the Splice-provided `MergeDelegation` contracts

## Wallet integration with Token Standard Assets

This section provides wallet developers with guidance on how to integrate with token standard assets. Such an integration works by sending the right read and write requests to the Ledger API of the validator node hosting the wallet user's party. There are five kinds of integration patterns:

> * `token_standard_usage_reading_contracts`
> * `token_standard_usage_reading_tx_history`
> * `token_standard_usage_executing_factory_choice`
> * `token_standard_usage_executing_nonfactory_choice`
> * `token_standard_usage_custom_daml_code`

These integrations patterns have recently been nicely packaged in the [Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk) maintained in the `canton-network/wallet-gateway` repository and [documented here](/docs/canton/integrations-wallet-guidance).

All of these integration patterns are also demonstrated in the form of executable code as part of the [experimental command-line interface](https://github.com/canton-network/splice/tree/main/token-standard#cli) for token standard assets. The sections below explaining the patterns below thus all start with a link to the code. They then provide additional context for an implementor.

All interaction works via the JSON Ledger API (see its [OpenAPI definition here](/sdks-tools/api-reference/json-api)). This OpenAPI definition is also accessible at `http(s)://${YOUR_PARTICIPANT}/docs/openapi`. We encourage developers to use OpenAPI code generation tools as opposed to manually writing HTTP requests.

Check out the [Authentication docs](/docs/canton/global-synchronizer-reference-security-configuration#configure-api-authentication-and-authorization-with-jwt) for more information on how to authenticate the requests.

### Reading contracts implementing a Token Standard interface for a party

Reference code from the Token Standard CLI to [list contracts by interface](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/listContractsByInterface.ts)

The Token Standard includes several interfaces that are implemented by Daml templates. To list all contracts implementing a particular interface, you have to query the participant's [active-contracts endpoint](/sdks-tools/api-reference/json-api).

The `activeAtOffset` parameter can be set to the result of [the ledger-end endpoint on the participant](/sdks-tools/api-reference/json-api#ledger-end) to get the latest ACS, or an older (non-pruned) one to get the ACS at that point in time.

To filter for a particular party and interface, it should include a `filtersByParty` with an `InterfaceFilter`:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "filtersByParty": {
    "$A_PARTY": {
      "cumulative": [
        {
          "identifierFilter": {
            "InterfaceFilter": {
              "value": {
                "interfaceId": "$AN_INTERFACE_ID",
                "includeInterfaceView": true,
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    }
  }
}
```

For example:

* `"$A_PARTY"` could look like `test::1220a0db3761b3fc919b55e7ff80ad740824336010bfde8829611c0e64477ab7bee5`.
* `"$AN_INTERFACE_ID"` could be `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding`.

Additionally, there's three flags that can be set:

* `includeInterfaceView`: to include the interface view of the contract in the response.
* `includeCreatedEventBlob`: to include a binary blob that is required for [explicit disclosure](/docs/canton/appdev-deep-dives-explicit-contract-disclosure).
* `verbose`: to include additional information in the response.

The response for such a query will contain the `createdEvent` of the contract, including the interface views requested (if any). The `viewValue` within it will be the JSON-serialized Daml interface view. If more than one interface is requested, you can distinguish them by checking the `interfaceId` field. You can find an [example response for Holdings here](https://github.com/canton-network/splice/blob/main/token-standard/cli/__tests__/mocks/data/holdings.json).

### Reading and parsing transaction history involving Token Standard contracts

Example code: [Token Standard CLI's code to list transactions](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/listHoldingTransactions.ts)

The participant has an [endpoint to list all transactions](/sdks-tools/api-reference/json-api) involving the provided parties and interfaces.

To filter for a particular party and interface, it should include a `filtersByParty` with an `InterfaceFilter`:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "filtersByParty": {
    "$A_PARTY": {
      "cumulative": [
        {
          "identifierFilter": {
            "InterfaceFilter": {
              "value": {
                "interfaceId": "$AN_INTERFACE_ID",
                "includeInterfaceView": true,
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    }
  }
}
```

For example:

* `"$A_PARTY"` could look like `test::1220a0db3761b3fc919b55e7ff80ad740824336010bfde8829611c0e64477ab7bee5`.
* `"$AN_INTERFACE_ID"` could be `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding` to read all `Holding` contracts of the specified party.

To include other transaction nodes that don't directly involve the interfaces (e.g., non-interface-specific children nodes), a `WildcardFilter` can be included in the `cumulative` filter array:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "identifierFilter": {
    "WildcardFilter": {
      "value": {
        "includeCreatedEventBlob": true
      }
    }
  }
}
```

The `beginExclusive` field is the offset from which to start reading transactions. To paginate, you can start with the `participantPrunedUpToInclusive` from `GET ${PARTICIPANT_URL}/v2/state/latest-pruned-offsets` and continue by passing the offset of the last transaction from the previous response.

#### Parsing the history

Example code: [the parser here](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/txparse/parser.ts). It extracts a user-readable wallet history by parsing transactions involving the `Holding` and `TransferInstruction` interfaces.

The endpoint returns transaction trees as an array. The transactions are ordered as they occur in the ledger. Given an `ExercisedEvent` with `nodeId=X` and `lastDescendantNodeId=Y`, the children of that node are those with `nodeId` in the range `[X+1, Y]`. `CreatedEvent` and `ArchivedEvent` (or equivalently, `ExercisedEvent` where `consuming=true`) do not have children.

Given the above, a tree-like traversal can be performed on the transaction nodes. Generally, a Token Standard parser will focus on the exercise of Token Standard choices and creation of contracts implementing Token Standard interfaces. Where further customization is required, a parser can decide to also focus on internal/specific choices that are not available in the standard, but in some specific implementation.

In each Token Standard exercise node, one can find:

* The choice being executed, useful to distinguish what operation was performed.
* As part of the archival/creation of children, one can find out other relevant operations that happened. For example, creation or archival of `Holdings`.
* Meta key/values, of which part of the standard:
  * `splice.lfdecentralizedtrust.org/tx-kind`: the kind of operation happening in the node. This can give more information than the exercised choice does. It can be one of:
    * `transfer`
    * `merge-split`
    * `burn`
    * `mint`
    * `unlock`
    * `expire-dust`
  * `splice.lfdecentralizedtrust.org/sender`: which party is the sender in the node.
  * `splice.lfdecentralizedtrust.org/reason`: a text specifying the reason for the operation in the node.
  * `splice.lfdecentralizedtrust.org/burned`: how much of a holding was burned in the node.

<Warning>
  Meta key/values can be specified in several optional fields. For transfers, the values from fields that are present should be merged in last-write-wins order of:

  * event.choiceArgument.transfer.meta,
  * event.choiceArgument.extraArgs.meta,
  * event.choiceArgument.meta,
  * event.exerciseResult.meta,
</Warning>

### Executing a factory choice

Example code: [Token Standard CLI's code to create a transfer via TransferFactory](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/transfer.ts)

To execute a choice via a Token Standard factory, first you need need to fetch the factory from the corresponding registry.

<Note>
  The mapping from an instrument's `admin` party-id to the corresponding registry URL needs to be maintained currently by wallets themselves, until a generic solution ([likely based on CNS](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#off-ledger-api-discovery-and-access)) is implemented.
</Note>

The registry will return the relevant factory in the corresponding endpoint:

* TransferFactory
* AllocationFactory

The response's payload will include three relevant fields:

* `factoryId`: the contract id of the factory
* `disclosedContracts`: must be provided to the exercise of the factory's choice for it to work
* `choiceContextData`: to be passed as `context` in the `choiceArgument`.

With this data, you can execute a choice on the factory. For external parties you must call the [prepare](/sdks-tools/api-reference/json-api#interactive-submission) and [execute](/sdks-tools/api-reference/json-api#interactive-submission) endpoints of the participant. For non-external parties, you can just use the [submit-and-wait endpoint](/sdks-tools/api-reference/json-api#command-submission).

In both cases, you must include an `ExerciseCommand` in your payload with the following fields:

* `templateId`: the interface id of the factory you want to exercise the choice on. For example, `#splice-api-token-transfer-instruction-v1:Splice.Api.Token.TransferInstructionV1:TransferFactory`.
* `contractId`: the `factoryId` obtained from the registry.
* `choice`: the name of the choice you want to execute. For example, `TransferFactory_Transfer`.
* `choiceArgument`: the arguments that will be passed to the Daml choice. These will be decoded from JSON. For a `TransferFactory_Transfer`, this will include for example the sender, receiver and amount, among other fields.

### Executing a non-factory choice

Example code: [Token Standard CLI's code to accept a transfer instruction](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/acceptTransferInstruction.ts)

To execute a choice on a contract implementing a Token Standard interface for external parties, you must call the [prepare](/sdks-tools/api-reference/json-api#interactive-submission) and [execute](/sdks-tools/api-reference/json-api#interactive-submission) endpoints of the participant. For non-external parties, you can just use the [submit-and-wait endpoint](/sdks-tools/api-reference/json-api#command-submission).

In both cases, you must include an `ExerciseCommand` in your payload with the following fields:

* `templateId`: the interface id of the contract you want to exercise the choice on. For example, `#splice-api-token-transfer-instruction-v1:Splice.Api.Token.TransferInstructionV1:TransferInstruction`.
* `contractId`: the contract id of the contract you want to exercise the choice on. Typically, you'll get this from the current ACS of a party.
* `choice`: the name of the choice you want to execute. For example, `TransferInstruction_Accept`.
* `choiceArgument`: the arguments that will be passed to the Daml choice. These will be decoded from JSON.

Where a `context` is required as part of the `choiceArgument`, it can be fetched from the corresponding registry:

* To accept a TransferInstruction
* To reject a TransferInstruction
* To withdraw a TransferInstruction
* To withdraw an Allocation
* To cancel an Allocation

The response of these endpoints include two fields:

* `choiceContextData`: to be passed as `context` in the `choiceArgument`.
* `disclosedContracts`: to be passed in the submit or prepare request.

<Warning>
  Note that `AllocationRequest_Reject` and `AllocationRequest_Withdraw` should be called with an empty choice context. This `ChoiceContext` is present to allow for potential future extensions of the behavior of implementations of these choices.
</Warning>

### Using token standard choices from custom Daml code

Calling the token standard choices from custom Daml code is useful when integrating one's own app workflows with the token standard. Example workflows relevant to a wallet provider are merging of holdings for a user to keep their ACS small, doing bulk transfers, or marking a user's action as activity of the wallet app.

Splice releases the optional `splice-util-token-standard-wallet.dar` file, which packages common workflows that improve the operations of a wallet app. See [splice-util-token-standard-wallet](/sdks-tools/api-reference/splice-daml/splice-util-token-standard-wallet) for the per-template reference.

## API References

Refer to [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#details) for more context on the APIs.

### Token Metadata

* Daml reference: [splice-api-token-metadata-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-metadata-v1)
* OpenAPI reference: [Token Metadata Service](/reference/splice-token-metadata-service/get-registry-metadata-v1-info)

### Holding

This allows implementation of a [Portfolio View](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#wallet-client--portfolio-view).

* Daml reference: [splice-api-token-holding-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-holding-v1)

### Transfer Instruction

This allows implementation of [Direct Peer-to-Peer / Free of Payment (FOP) Transfers](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#direct-peer-to-peer--free-of-payment-fop-transfer-workflow).

* Daml reference: [splice-api-token-transfer-instruction-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-transfer-instruction-v1)
* OpenAPI reference: [Transfer Instruction API](/reference/splice-transfer-instruction-api/post-registry-transfer-instruction-v1-transfer-factory)

### Allocation

This allows implementation of [Delivery versus Payment (DVP) Transfer Workflows](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md#delivery-versus-payment-dvp-transfer-workflows), jointly with the Allocation Instruction and Allocation Request APIs below.

* Daml reference: [splice-api-token-allocation-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-v1)
* OpenAPI reference: [Allocation API](/reference/splice-allocation-api/post-registry-allocations-v1-allocationid-choice-contexts-execute-transfer)

### Allocation Instruction

* Daml reference: [splice-api-token-allocation-instruction-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-instruction-v1)
* OpenAPI reference: [Allocation Instruction API](/reference/splice-allocation-instruction-api/post-registry-allocation-instruction-v1-allocation-factory)

### Allocation Request

* Daml reference: [splice-api-token-allocation-request-v1](/sdks-tools/api-reference/splice-daml/splice-api-token-allocation-request-v1)

{/* Mintlify preview rebuild marker. */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
