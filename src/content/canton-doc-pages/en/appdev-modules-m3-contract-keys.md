---
title: "Contract Keys"
slug: "appdev-modules-m3-contract-keys"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-contract-keys.md"
source_title: "Contract Keys"
tags:
  - appdev
  - modules
  - m3-contract-keys
---

# Contract Keys

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Contract Keys

> Use contract keys for stable references to contracts and key-based lookups

# Reference: Contract Keys

Contract keys are an optional addition to templates. They let you specify a way of identifying contracts using the parameters to the template — similar to a key in a database.

Contract keys do not change and can be used to refer to a contract even when the contract ID changes. As a contract is updated via archive and create operations, the currently active contract(s) can easily be referenced via the contract key.

<Note>
  In Canton 3.x, it is possible for multiple active contracts of the same template to share the same key.

  The general usage is that key uniqueness is guaranteed outside of the Daml engine — for example, in the Daml business logic or at the backend client level (e.g., a unique account number or invoice number). Because of this, the primary key-based API (`lookupByKey`, `fetchByKey`, `exerciseByKey`) are optimized for the common case where there is at most a key references one contract.
</Note>

Here's an example of setting up a contract key for a bank account, to act as a bank account ID:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AccountKey = (Party, Text)

template Account with
    bank : Party
    number : Text
    owner : Party
    balance : Decimal
    observers : [Party]
  where
    signatory [bank, owner]
    observer observers

    key (bank, number) : AccountKey
    maintainer key._1
```

## What Can Be a Contract Key

The key can be an arbitrary serializable expression that does **not** contain contract IDs. However, it **must** include every party that you want to use as a `maintainer` (see [Specify Maintainers](#specify-maintainers) below).

It's best to use simple types for your keys like `Text` or `Int`, rather than a list or more complex type.

## Specify Maintainers

If you specify a contract key for a template, you must also specify a `maintainer` or maintainers, in a similar way to specifying signatories or observers. The maintainers "own" the key in the same way the signatories "own" a contract. Just like signatories of contracts prevent double spends or use of false contract data, maintainers of keys ensure consistent key lookups. Since the key is part of the contract, the maintainers **must** be signatories of the contract. However, maintainers are computed from the `key` instead of the template arguments. In the example above, the `bank` is ultimately the maintainer of the key.

Since multiple templates may use the same key type, some key-related functions must be annotated using the `@ContractType` as shown in the examples below.

When you are writing Daml models, the maintainers matter since they affect authorization -- much like signatories and observers. You don't need to do anything to "maintain" the keys. Validators hosting the maintainers of a key involved in a transaction verify that contracts are retrieved in a consistent order for that key within the transaction.

## Contract Lookups

The primary purpose of contract keys is to provide a stable, and possibly meaningful, identifier that can be used in Daml to fetch contracts. The main functions for key-based lookups are `fetchByKey`, `lookupByKey`, and `exerciseByKey`, all available by default.

When multiple contracts share the same key, these functions return the **first** contract according to the following lookup order:

1. Contracts created within the current transaction, starting with the most recent.
2. Explicitly disclosed contracts, in the order provided in the command.
3. Contracts known to the participant, in any order. (The current implementation returns them in recency order, but this is not guaranteed and should not be relied on.)

For use cases where multiple contracts per key are expected, the `DA.ContractKeys` module provides `lookupNByKey` and `lookupAllByKey` (see [Multi-Contract Key Lookups](#multi-contract-key-lookups) below).

Because disclosed contracts are prioritized over known contracts, you can use disclosures to ensure a specific retrieval order during command submission.

### fetchByKey

`(fetchedContractId, fetchedContract) <- fetchByKey @ContractType contractKey`

Use `fetchByKey` to fetch the ID and data of the first contract with the specified key (according to the lookup order above). It is an alternative to `fetch` and behaves the same in most ways.

It returns a tuple of the ID and the contract object (containing all its data).

Like `fetch`, `fetchByKey` needs to be authorized by at least one stakeholder.

`fetchByKey` fails and aborts the transaction with a [`CONTRACT_KEY_NOT_FOUND`](/appdev/reference/error-codes#contracts-and-transactions) error if no contract with the given key is visible to the submitting party.

### lookupByKey

`optionalContractId <- lookupByKey @ContractType contractKey`

Use `lookupByKey` to check whether a contract with the specified key exists. If it does exist, `lookupByKey` returns `Some contractId`, where `contractId` is the ID of the first contract matching the key (according to the lookup order above); otherwise, it returns `None`.

`lookupByKey` requires authorization from **all** maintainers of the key. This is necessary so that confirming participants hosting the maintainers can verify that contracts are retrieved in a consistent order for the given key within the transaction.

More precisely:

* `lookupByKey` returns `Some contractId` if a contract with the given key exists and the submitter is a stakeholder on that contract, and authorization from all maintainers is present.
* `lookupByKey` returns `None` if no contract with the given key exists (or none is visible to the submitter), and authorization from all maintainers is present.
* `lookupByKey` aborts the transaction if authorization from any maintainer is missing.

## exerciseByKey

`exerciseByKey @ContractType contractKey`

Use `exerciseByKey` to exercise a choice on the first contract with the given key (according to the lookup order above). Just like `exercise`, running `exerciseByKey` requires visibility of the contract and authorization from the controllers of the choice.

## Multi-Contract Key Lookups

For use cases where multiple contracts may share the same key, the `DA.ContractKeys` module provides:

* **`lookupNByKey @ContractType n key`** — looks up up to `n` contracts with the given key, returned in the lookup order described above.
* **`lookupAllByKey @ContractType key`** — looks up all contracts with the given key.

These functions are not imported by default. To use them, add `import DA.ContractKeys` to your module.

<Note>
  Performance is optimized for the common case of zero or one contract per key. The multi-contract functions (`lookupNByKey`, `lookupAllByKey`) may be less performant when many contracts share a key.
</Note>

## Daml Script Functions

In addition to the Daml language primitives above (which run inside transactions), there are Daml Script functions for querying keys outside of transactions:

* **`queryByKey @ContractType party key`** — looks up a contract by key and returns its ID and data. Runs as a top-level `Script` action.
* **`queryNByKey @ContractType party n key`** — looks up up to `n` contracts by key and returns their IDs and data. Runs as a top-level `Script` action.
* **`exerciseByKeyCmd @ContractType key choiceArg`** — exercises a choice on the first contract with the given key. This is a `Commands` action and must be used inside a `submit` block, where it can be combined with other commands.

## Example

An example demonstrating key-based lookups and exercises:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

module Test where

import Daml.Script
import DA.Assert
import DA.ContractKeys
import DA.Optional

template WithKey
  with
    p : Party
    payload : Text
  where
    signatory p
    key p : Party
    maintainer key
    nonconsuming choice GetText : Text
      with
        party : Party
      controller party
      do pure payload

template Helper
  with
    p : Party
  where
    signatory p

    choice PerformLookupByKey : Optional (ContractId WithKey)
      controller p
      do lookupByKey @WithKey p
    
    choice PerformFetchByKey : (ContractId WithKey, WithKey)
      controller p
      do fetchByKey @WithKey p
    
    choice PerformExerciseByKey : Text
      controller p
      do exerciseByKey @WithKey p GetText with party = p
    
    choice PerformLookupNByKey : [(ContractId WithKey, WithKey)]
      with n : Int
      controller p
      do lookupNByKey @WithKey n p
    
    choice CreateThenPerformLookupNByKey : [(ContractId WithKey, WithKey)]
      with 
        payload : Text
        n : Int
      controller p
      do create (WithKey p payload)
         lookupNByKey @WithKey n p

-- Demonstrates basic key operations: lookupByKey, fetchByKey, exerciseByKey
useKeyOperations : Script ()
useKeyOperations = script do
  alice <- allocateParty "alice"

  -- Create a contract with a key
  cid <- alice `submit` createCmd (WithKey alice "hello")

  -- lookupByKey returns Some if a contract with the key exists
  mcid <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformLookupByKey
  assert (isSome mcid)

  -- fetchByKey returns the contract ID and data
  (kcid, contract) <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformFetchByKey
  kcid === cid
  contract.payload === "hello"

  -- exerciseByKey exercises a choice on the contract with the key
  result <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformExerciseByKey
  result === "hello"

-- Demonstrates non-unique keys: multiple contracts can share a key.
-- lookupByKey and fetchByKey return the first contract per lookup order;
-- lookupNByKey (from DA.ContractKeys) returns up to n contracts.
multipleContractsPerKey : Script ()
multipleContractsPerKey = script do
  alice <- allocateParty "alice"

  -- Create multiple contracts with the same key
  cid1 <- alice `submit` createCmd (WithKey alice "first")
  cid2 <- alice `submit` createCmd (WithKey alice "second")
  cid3 <- alice `submit` createCmd (WithKey alice "third")

  let contracts = [(cid1, "first"), (cid2, "second"), (cid3, "third")]

  -- fetchByKey returns one of the created contracts
  (kcid, contract) <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformFetchByKey
  assert ((kcid, contract.payload) `elem` contracts)

  -- lookupNByKey returns up to n contracts (any 2 of 3, in any order)
  result <- alice `submit`
    createAndExerciseCmd (Helper alice) PerformLookupNByKey with n = 2
  let results = [(cid, c.payload) | (cid, c) <- result]
  length results === 2
  let [r1, r2] = results
  assert (r1 `elem` contracts)
  assert (r2 `elem` contracts)
  r1 =/= r2

  -- lookupNByKey returns:
  --   - local contracts in recency order
  --   - then disclosures in command-specified order
  --   - then contracts known to the participant in any order
  Some disclosure <- alice `queryDisclosure` cid1
  result <- submit (actAs alice <> disclose disclosure) do
    createAndExerciseCmd (Helper alice) CreateThenPerformLookupNByKey with
      payload = "fourth"
      n = 3
  let results = [(cid, c.payload) | (cid, c) <- result]
  length results === 3
  let [r1, r2, r3] = results
  r1._2 === "fourth"
  r2 === (cid1, "first")
  r3._1 =/= cid1
  r3._2 =/= "fourth"
  assert (r3 `elem` contracts)

-- Demonstrates exerciseByKeyCmd in a submit block
exerciseByKeyCmdExample : Script ()
exerciseByKeyCmdExample = script do
  alice <- allocateParty "alice"

  alice `submit` createCmd (WithKey alice "payload")

  -- exerciseByKeyCmd is a Commands action used inside submit
  result <- alice `submit` do
    exerciseByKeyCmd @WithKey alice GetText with party = alice
  result === "payload"
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
