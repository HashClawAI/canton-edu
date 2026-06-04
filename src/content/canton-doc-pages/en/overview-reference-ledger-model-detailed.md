---
title: "Ledger Model (Detailed)"
slug: "overview-reference-ledger-model-detailed"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/ledger-model-detailed.md"
source_title: "Ledger Model (Detailed)"
tags:
  - overview
  - reference
  - ledger-model-detailed
---

# Ledger Model (Detailed)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Ledger Model (Detailed)

> Formal specification of Canton's ledger model: structure, validity, integrity, privacy, and multi-synchronizer interoperability.

# Structure

This section looks at the structure of a ledger that records the interactions between the parties as ledger changes. The definitions presented here address the first question: "What do changes and ledgers look like?". The basic building blocks of the recorded interactions are actions, which get grouped into transactions, *updates*, *commits*, and the Ledger.

## Running workflow example

Most of the examples in this section look at the following Daml Script scenarios based on the templates from the running example. Two banks first each issue one asset to either Alice or Bob and then Alice proposes a DvP to Bob. Bob accepts the proposal and settles the DvP.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let eurAsset = SimpleAsset with
      issuer = bank1
      owner = alice
      asset = "1 EUR"
eur <- submit bank1 do createCmd eurAsset
    
let usdAsset = SimpleAsset with
      issuer = bank2
      owner = bob
      asset = "1 USD"
usd <- submit bank2 do createCmd usdAsset
    
proposeDvP <- submit alice $ do
  createCmd ProposeSimpleDvP with
      proposer = alice
      counterparty = bob
      allocated = eur
      expected = usdAsset
disclosedEur <- fromSome <$> queryDisclosure alice eur
```

Acceptance and settlement can happen either in a single step via the `AcceptAndSettle` choice.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
(newUsd, newEur) <- submitWithDisclosures bob [disclosedEur] do
    exerciseCmd proposeDvP $ AcceptAndSettle with toBeAllocated = usd
```

Or in two separate steps with `Accept` followed by `Settle`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dvp <- submit bob $
  do exerciseCmd proposeDvp $ Accept with toBeAllocated = usd

(newUsd, newEur) <- submitWithDisclosures bob [disclosedEur] do
    exerciseCmd dvp $ Settle with actor = bob
```

## Actions

### Hierarchical structure

One of the main features of the Ledger Model is a *hierarchical action structure*. This structure is illustrated using Bob settling the DvP by exercising the `Settle` choice in the above scenario. Alice and Bob have allocated their assets (contracts #1 and #2) on the ledger to a `SimpleDvp` contract (#4). These contracts appears as inputs (dashed boxes on the left) in the diagram below.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-settle-action.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=92dcd6bdccf7c5050568bbe072b6cb47" alt="The settlement action on the ``SimpleDvp`` contract between Alice and Bob, with the two legs of the swap as consequences." width="1642" height="1093" data-path="images/docs_website/dvp-settle-action.svg" />

Exercising the `Settle` choice yields an Exercise action, which is the tree of nodes shown in blue. The input contracts on the left are not part of the action. The root node describes the parameters of the choice and references the `SimpleDvp` input contract #4. It has two subtrees, which perform the asset transfers automatically as part of the `Settle` choice.

1. The left subtree represents Alice exercising the `Transfer` choice on her `SimpleAsset` contract #1. It consists of two nodes: The root node describes the parameters of the choice and the input contract #1. The child node, which is a one-node subtree of its own, encodes the creation of Bob's new `SimpleAsset` contract #5.
2. The right subtree is analogous: The root node of the subtree describes Bob exercising the `Transfer` choice on his `SimpleAsset` contract #2, and its child encodes the creation of Alice's new `SimpleAsset` contract #6.

Notably, the Exercise action is the whole tree even though the root node already describes all the relevant parameters. The Ledger Model focuses on actions rather than nodes because the root node cannot exist on its own, without its children, as the choice body in the Daml model must always execute when the choice is exercised. The integrity section goes into the details of this.

Nevertheless actions are not indivisible, but hierarchical: The left and right subtrees are actions in their own right, namely the Exercise actions for Alice and Bob exercising their `Transfer` choice on their `SimpleAsset` input contracts #1 and #2, respectively. And each of the two subtrees contains another subtree, namely the creation of Bob's and Alice's new `SimpleAsset` contracts #5 and #6. Each of these subtrees is an action in its own right. This hierarchical structure induces a subaction relationship explained below and forms the basis for the privacy model.

### Definition

Overall, the settlement in the above example contains two types of actions:

1. Creating contracts
2. Exercising choices on contracts.

These are also the two main kinds of actions in the Ledger Model.

A **node** is one of the following:

1. A **Create** node records the creation of the contract. It contains the following pieces of information:

   * The **contract ID** is a unique identifier of the contract. It is equivalent to the transaction output (TxO) in ledgers based on unspent transaction outputs (UTxO).
   * The **template ID** identifies the Daml code associated with the contract, and its arguments define the **contract instance**, which is the immutable data associated with the contract ID.
   * The **signatories** are the non-empty set of parties that must authorize the creation and archival of the contract.
   * The **contract observers**, or just observers for short, are the set of parties that will be informed about the contract creation and archival, in addition to the signatories.

   In Daml, the signatories and contract observers are determined by the `signatory` and `observer` clauses defined by the template.

   Create nodes are depicted as shown below. Diagrams often omit fields with empty values and observers that are also signatories.

   <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/create-node.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9c64445fa65cb58481369dade79bc801" className="align-center" style={{width: "30.0%"}} alt="The structure of a **Create** node." width="442" height="202" data-path="images/docs_website/create-node.svg" />

2. An **Exercise** node records the parameters of a choice that one or more parties have exercised on a contract. It contains the following pieces of information:

   * An exercise **kind**, which is either **consuming** or **non-consuming**. Once consumed, a contract cannot be used again; for example, Alice must not be able to transfer her asset twice, as this would be double spending. In contrast, contracts exercised in a non-consuming fashion can be reused, for example for expressing a delegation from one party to another.
   * The **contract ID** on which the choice is exercised. This contract is called the **input contract**.
   * The **interface ID** if this choice was exercised through a Daml interface.
   * The **template ID** that defines the smart contract code for the choice with the given **choice name**; and the **choice arguments** that are passed to the smart contract code.
   * An associated set of parties called **actors**. These are the parties who perform the action. They are specified in the `controller` clause in the Daml template.
   * An associated set of **choice observers**. These parties will be informed about the choice being exercised.
   * The **exercise result** as the Daml value returned by evaluating the choice body.

   Exercise nodes are depicted as shown below, where the consequences are indicated by arrows ordered left-to-right. Diagrams omit the kind if it is consuming, empty field values, and choice observers that are also actors.

   <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/exercise-node.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=52697fa7f7bd95a232ddd2c1588c62b6" className="align-center" style={{width: "30.0%"}} alt="The structure of an **Exercise** node." width="442" height="282" data-path="images/docs_website/exercise-node.svg" />

3. A **Fetch** node on a contract, which demonstrates that the contract exists and is active at the time of fetching. A Fetch behaves like a non-consuming Exercise with no consequences, and can be repeated. The fetch node contains the following pieces of information, analogous to Exercise nodes: **contract ID**, **interface ID**, **template ID**, and the **actors**, namely the parties who fetch the contract.

   Fetch nodes are depicted as shown below.

   <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/fetch-node.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=6c854090ce405fc45ba634de15d55ca1" className="align-center" style={{width: "30.0%"}} alt="The structure of a **Fetch** node." width="442" height="202" data-path="images/docs_website/fetch-node.svg" />

An **action** consists of a **root node** and a list of **consequences**, which are themselves actions. This gives rise to the tree structure of an action: The root node of an action has as children the root nodes of its consequences.

An action inherits its kind from its root node:

1. A **Create action** has a Create node as the root. The consequences are empty.
2. An **Exercise action** has an Exercise node as the root and the consequences are the subactions. The Exercise action is the **parent action** of its consequences.
3. A **Fetch action** as a Fetch node as the root. The consequences are empty.

The terminology on nodes extends to actions via the root node. For example, the signatories of a Create action are the signatories of the Create node, and an Exercise action is (non)consuming if and only if its root node is. Moreover, an Exercise or a Fetch action on a contract is said to **use** the contract. Finally, a consuming Exercise is said to **consume** (or **archive**) its contract.

### Examples

An example of a Fetch action appears in the `Accept` choice on a DvP proposal contract from the template `ProposeSimpleDvP`. The choice body fetches the `SimpleAsset` that Bob allocates to the DvP, which checks that the asset contract is active and brings the contract instance into the computation, so that the choice implementation can assert that this asset meets the expectation expressed in the proposal contract. The next diagram shows this Exercise action with the Fetch action as its first consequence.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-propose-accept-action.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=7985f68cb49127abf9d49ef7688d6c67" className="align-center" style={{width: "100.0%"}} alt="The accept action on Alice's ``ProposeSimpleDvP`` exercised by Bob." width="1562" height="715" data-path="images/docs_website/dvp-propose-accept-action.svg" />

A non-consuming Exercise shows up in the combined `AcceptAndSettle` choice on the `ProposeSimpleDvP` contract: This choice is non-consuming so that the `Accept` choice exercised in the choice body can consume the proposal contract. As the next diagram shows, non-consuming Exercises yield multiple references to the same input contract #3. The diagram also shows that fetches have the same effect: input contract #2 is used twice.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-propose-accept-and-settle-action.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=7fb2fa37d4a5585387ad222a9afe9349" className="align-center" style={{width: "100.0%"}} alt="The accept-and-settle action on Alice's ``ProposeSimpleDvP`` exercised by Bob." width="2283" height="1255" data-path="images/docs_website/dvp-propose-accept-and-settle-action.svg" />

### Subactions

This example again highlights the hierarchical structure of actions: The `AcceptAndSettle` action contains the corresponding actions for `Accept` and `Settle` as its consequences.

More generally, for an action `act`, its **proper subactions** are all actions in the consequences of `act`, together with all of their proper subactions. Additionally, `act` is a (non-proper) **subaction** of itself.

The subaction relation is visualized below for Bob's `Settle` Exercise. Each borderless box contains an action (via its tree of nodes) and the nesting of these boxes encodes the subaction relation. In detail, both the blue and purple boxes are proper subactions of Bob's `Settle` action shown in grey. The green box is a proper subaction of the blue and the grey boxes, and the yellow box is a proper subaction of the purple and the grey boxes.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-settle-subactions.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=18826aee2e0d531ab1f060dfc332fc00" className="align-center" style={{width: "60.0%"}} alt="The subactions of Bob exercising the ``Settle` choice on the DvP contract." width="1122" height="1122" data-path="images/docs_website/dvp-settle-subactions.svg" />

## Transactions

A **transaction** is a list of actions that are executed atomically. Those actions are called the **root actions** of the transaction. That is, for a transaction `tx = act``1``, …, act``n`, every `act``i` is a root action. For example, if Alice and Charlie have made one DvP proposal each for Bob, then Bob may want to both accept simulataneously. To that end, Bob exercises both `Accept` choices in a single transaction with two root actions (blue and purple), as shown next. Visually, transactions are delimited by the dashed lines on both sides, to distinguish them from actions. Like for actions, the input contracts on the left are not part of the transaction.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-accept-two.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=ee3f6ea1f8df103166460369377101d2" className="align-center" style={{width: "100.0%"}} alt="A transaction with two top-level actions where Bob accepts two DvP proposal, one from Alice and one from Charlie." width="2442" height="1155" data-path="images/docs_website/dvp-accept-two.svg" />

For another example, the consequences of an Exercise action are a list of actions and therefore form a transaction In the example of the `Settle` action on Alice's and Bob's `SimpleDvP`, the consequences of the `Settle` action form the following transaction, where actions are ordered left-to-right as before. The transaction consists of two root actions (blue and purple), namely the two `Transfer` actions of the two legs of the DvP.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-settle-consequences-are-transactions.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=5b0538ddeb688764316720634ea98d6a" className="align-center" style={{width: "50.0%"}} alt="The consequences of the ``Settle`` action are a transaction of two actions, namely the two ``Transfer`` legs of the DvP." width="962" height="612" data-path="images/docs_website/dvp-settle-consequences-are-transactions.svg" />

The hierarchical structure of actions extends to transactions and yields the notion of subtransactions. A **proper subtransaction** of a transaction is obtained by (repeatedly) replacing an action by its consequences; and a **subtransaction** of a transaction is either the transaction itself or a proper subtransaction thereof.

For example, given the transaction shown above consisting only of the two consequences of the `Settle` action, the next diagram shows all seven proper non-empty subtransactions, each with their dashed delimiters.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-settle-consequences-subtransactions.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=809e7066dbf0b44649bada35081b06d9" className="align-center" style={{width: "100.0%"}} alt="All proper subtransactions of the consequences of the ``Settle`` action." width="1942" height="1308" data-path="images/docs_website/dvp-settle-consequences-subtransactions.svg" />

The privacy model uses the concept of subtransactions to define the visibility rules.

## Inputs and outputs

The Ledger Model falls into the category of (extended) UTxO-style ledgers where the set of unspent transaction outputs (UTxOs) constitutes the current state of a ledger. Here, the **transaction outputs** are the contract IDs of the contracts created in a transaction. When a contract is consumed, its contract ID is spent and thus removed from the UTxO set. The data associated with each UTxO is immutable; modifications happen by consuming a contract ID and recreating a new contract with a different contract ID.

This Ledger Model extends the UTxO model in two aspects:

* A transaction may use a contract without consuming it, for example by exercising a non-consuming choice or fetching it. In such a case, the contract ID remains in the set of UTxOs even though it appears as an input to a transaction.
* Transactions are structured hierarchically and contract IDs created in the transaction may be consumed within the same transaction. For example, inside the `AcceptAndSettle` action, the created `SimpleDvP` in the first consequence is consumed by the second consequence. Such contracts are called **transient**.

These aspects are discussed in more detail in the remaining sections of the Ledger Model.

## Ledger

The transaction structure records the contents of a party interaction. The ledger records two more aspects of an interaction:

* An identifier to uniquely refer a particular party interaction.
* The parties who requested a particular party interaction.

Due to the privacy model, not everyone sees all parts of a party interaction. A unique identifier for a party interaction allows different parties to correlate whether they see parts of the same interactions. The notion of an **update** adds such an identifier. It consists of a single transaction and the so-called **update ID**, a string. Examples in the Ledger Model use update IDs of the form `TX i` for some number `i`, similar to the transaction view in Daml Studio. On the Ledger API, update IDs are arbitrary strings whose lexicographic order is independent from their order on the ledger.

A **commit** adds the information *who requested a party interaction*. It consists of an update and the one or more parties that requested it. Those parties are called the **requesters** of the commit. In Daml Script, the requesters correspond to the `actAs` parties given to the `submit` commands.

<Note>
  **Definition: Ledger**

  A **Ledger** is a directed acyclic graph (DAG) of commits, where the update IDs are unique.
</Note>

<Note>
  **Definition: top-level action**

  For a commit, the root actions of its transaction are called the **top-level actions**. A top-level action of any ledger commit is also a top-level action of the ledger.
</Note>

A Canton Ledger thus represents the full history of all actions taken by parties. The graph structure of the Ledger induces a **happens-before order** on the commits in the ledger. We say that commit `c``1` *happens before* `c``2` if and only if the ledger contains a non-empty path from `c``1` to `c``2`, or equivalently, the transitive closure of the graph contains an edge from `c``1` to `c``2`.

<Note>
  The integrity conditions on a ledger require that the happens-before order respects the lifecycle of contracts. For example, the commit that creates a contract must happen before the commit that spends the contract unless they are the same. For the next few sections, we will consider only ledgers that meet these conditions.
</Note>

Visually, a ledger can be represented as a sequence growing from left to right as time progresses. Below, dashed vertical lines in purple mark the boundaries of commits, and each commit is annotated with its requester(s) and the update ID. Blue arrows link each Exercise and Fetch action to the Create action of the input contract. These arrows highlight that the ledger forms a **transaction graph** in the sense of a UTXO blockchain.

For example, the following Daml Script encodes the whole workflow of the running DvP example.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let eurAsset = SimpleAsset with
      issuer = bank1
      owner = alice
      asset = "1 EUR"
eur <- submit bank1 do createCmd eurAsset
    
let usdAsset = SimpleAsset with
      issuer = bank2
      owner = bob
      asset = "1 USD"
usd <- submit bank2 do createCmd usdAsset
    
proposeDvP <- submit alice $ do
  createCmd ProposeSimpleDvP with
      proposer = alice
      counterparty = bob
      allocated = eur
      expected = usdAsset
disclosedEur <- fromSome <$> queryDisclosure alice eur
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
(newUsd, newEur) <- submitWithDisclosures bob [disclosedEur] do
    exerciseCmd proposeDvP $ AcceptAndSettle with toBeAllocated = usd
```

This workflow gives rise to the ledger shown below with four commits:

* In the first commit, Bank 1 requests the creation of the `SimpleAsset` of `1 EUR` issued to Alice (contract #1).
* In the second commit, Bank 2 requests the creation of the `SimpleAsset` of `1 USD` issued to Bob (contract #2).
* In the thrid commit, Alice requests the creation of the `SimpleDvpPoposal` (contract #3).
* In the forth commit, Bob requests to exercise the `AcceptAndSettle` choice on the DvP proposal.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-ledger.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=2905a7d8b725484c0035079b45d2ba07" className="align-center" alt="The sequence of commits for the whole DvP workflow. First, banks 1 and 2 issue the assets, then Alice proposes the DvP, and finally Bob accepts and settles it." width="3322" height="1362" data-path="images/docs_website/dvp-ledger.svg" />

<Note>
  The integrity constraints do not impose an order between independent commits. In this example, there need not be edges among the first three commits `TX 0`, `TX 1`, and `TX 2`, so they could be presented in any order.

  As the Ledger is a DAG, one can always extend the order into a linear sequence via a topological sort. For the next sections, we pretend that the Ledger is totally ordered (unless otherwise specified). We discuss the more general partial orders in the causality section.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/overview/explanations/ledger-model/ledger-validity.rst" hash="3710723f" */}

# Valid Ledgers

At the core is the concept of a *valid ledger*; changes are permissible if adding the corresponding commit to the ledger results in a valid ledger. **Valid ledgers** are those that fulfill three conditions:

`da-model-consistency`
Exercises and fetches on inactive contracts are not allowed, i.e. contracts that have not yet been created or have already been consumed by an exercise. A contract with a contract key can be created only if the key is not associated to another unconsumed contract, and all key assertions hold.

`da-model-conformance`
Only a restricted set of actions is allowed on a given contract.

`da-model-authorization`
The parties who may request a particular change are restricted.

Only the last of these conditions depends on the party (or parties) requesting the change; the other two are general.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/overview/explanations/ledger-model/ledger-integrity.rst" hash="c93dba12" */}

# Integrity

This section addresses the question of who can request which changes.

To answer the next question, "who can request which changes", a precise definition is needed of which ledgers are permissible, and which are not. For example, the above paint offer ledger is intuitively permissible, while all of the following ledgers are not.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/double-spend.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c7c57fe21551e142d5260e4cd19757f3" className="align-center" alt="./images/double-spend.svg" width="1220" height="362" data-path="images/docs_website/double-spend.svg" />

  <figcaption>Alice spending her IOU twice ("double spend"), once transferring it to `B` and once to `P`.</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/non-conformant-action.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=8c316201ce7b19be6d74a60c83d5e1fc" id="alice-changes-offer" className="align-center" alt="./images/non-conformant-action.svg" width="1220" height="502" data-path="images/docs_website/non-conformant-action.svg" />

  <figcaption>Alice changing the offer's outcome by removing the transfer of the `Iou`.</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/invalid-obligation.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=87da739c05b2ea006c1370a44095d7c4" id="obligation-imposed-on-painter" className="align-center" alt="./images/invalid-obligation.svg" width="1220" height="242" data-path="images/docs_website/invalid-obligation.svg" />

  <figcaption>An obligation imposed on the painter without his consent.</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/stealing-ious.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0c702257241fcc8597ad84a16b602477" id="painter-stealing-ious" className="align-center" alt="./images/stealing-ious.svg" width="1220" height="482" data-path="images/docs_website/stealing-ious.svg" />

  <figcaption>Painter stealing Alice's IOU. Note that the ledger would be intuitively permissible if it was Alice performing the last commit.</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/failed-key-assertion.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=fee78b7c103c1b1be86e8a9376ebad15" id="alice-claiming-retracted-offer" className="align-center" alt="./images/failed-key-assertion.svg" width="1220" height="202" data-path="images/docs_website/failed-key-assertion.svg" />

  <figcaption>Painter falsely claiming that there is no offer.</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/double-key-creation.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=5a5a0addd2e124de2edba64b36174cf7" id="painter-creating-two-offers-with-same-key" className="align-center" alt="./images/double-key-creation.svg" width="1220" height="202" data-path="images/docs_website/double-key-creation.svg" />

  <figcaption>Painter trying to create two different paint offers with the same reference number.</figcaption>
</figure>

## Consistency

Consistency consists of two parts:

1. Contract consistency: Contracts must be created before they are used, and they cannot be used once they are consumed.
2. Key consistency: Keys are unique and key assertions are satisfied.

To define this precisely, notions of "before" and "after" are needed. These are given by putting all actions in a sequence. Technically, the sequence is obtained by a pre-order traversal of the ledger's actions, noting that these actions form an (ordered) forest. Intuitively, it is obtained by always picking parent actions before their proper subactions, and otherwise always picking the actions on the left before the actions on the right. The image below depicts the resulting order on the paint offer example:

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/consistency-order-on-actions.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=dad56899a6c7f7695b4b59005554d5cf" className="align-center" style={{width: "100.0%"}} alt="The time sequence of commits. In the first commit, Iou Bank A is requested by the bank. In the second, PaintOffer P A P123 is requested by P. In the last commit, requested by A, Exe A (PaintOffer P A P123) leads to Exe A (Iou Bank A) leads to Iou Bank P leads to PaintAgree P A P123" width="1251" height="518" data-path="images/docs_website/consistency-order-on-actions.svg" />

In the image, an action `act` happens before action `act'` if there is a (non-empty) path from `act` to `act'`. Then, `act'` happens after `act`.

### Contract Consistency

Contract consistency ensures that contracts are used after they have been created and before they are consumed.

<div id="def-contract-consistency">
  Definition »contract consistency«
  A ledger is **consistent for a contract c** if all of the following holds for all actions `act` on \`c\`:

  1. either `act` is itself **Create c** or a **Create c** happens before `act`
  2. `act` does not happen before any **Create c** action
  3. `act` does not happen after any **Exercise** action consuming `c`.
</div>

The consistency condition rules out the double spend example. As the red path below indicates, the second exercise in the example happens after a consuming exercise on the same contract, violating the contract consistency criteria.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/consistency-banning-double-spends.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=f905e3b64ca7636365f4631da7185fe1" className="align-center" style={{width: "100.0%"}} alt="Another time sequence of commits. In the first commit, Iou Bank A is requested by the bank. In the second, Exe A (Iou Bank A) leads to Iou Bank B via a red line, indicating contract consistency violations. Iou Bank B leads to Exe A (Iou Bank A) in the third commit, also via a red line, and Exe A (Iou Bank A) leads to Iou Bank P." width="1220" height="362" data-path="images/docs_website/consistency-banning-double-spends.svg" />

<div id="def-contract-state">
  In addition to the consistency notions, the before-after relation on actions can also be used to define the notion of **contract state** at any point in a given transaction. The contract state is changed by creating the contract and by exercising it consumingly. At any point in a transaction, we can then define the latest state change in the obvious way. Then, given a point in a transaction, the contract state of `c` is:
</div>

1. **active**, if the latest state change of `c` was a create;
2. **archived**, if the latest state change of `c` was a consuming exercise;
3. **inexistent**, if `c` never changed state.

A ledger is consistent for `c` exactly if **Exercise** and **Fetch** actions on `c` happen only when `c` is active, and **Create** actions only when `c` is inexistent. The figures below visualize the state of different contracts at all points in the example ledger.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/consistency-paint-offer-activeness.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=166f2ac81a3fbf9309dd910c050956cf" className="align-center" style={{width: "100.0%"}} alt="./images/consistency-paint-offer-activeness.svg" width="1251" height="502" data-path="images/docs_website/consistency-paint-offer-activeness.svg" />

  <figcaption>Activeness of the `PaintOffer` contract</figcaption>
</figure>

<figure>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/consistency-alice-iou-activeness.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=1707ba950349e96fa049806cf0dc1350" className="align-center" style={{width: "100.0%"}} alt="./images/consistency-alice-iou-activeness.svg" width="1251" height="502" data-path="images/docs_website/consistency-alice-iou-activeness.svg" />

  <figcaption>Activeness of the `Iou Bank A` contract</figcaption>
</figure>

The notion of order can be defined on all the different ledger structures: actions, transactions, lists of transactions, and ledgers. Thus, the notions of consistency, inputs and outputs, and contract state can also all be defined on all these structures. The **active contract set** of a ledger is the set of all contracts that are active on the ledger. For the example above, it consists of contracts `Iou Bank P` and `PaintAgree P A`.

### Key Consistency

Contract keys introduce a key uniqueness constraint for the ledger. To capture this notion, the contract model must specify for every contract in the system whether the contract has a key and, if so, the key. Every contract can have at most one key.

Like contracts, every key has a state. An action `act` is an **action on a key** `k` if

* `act` is a **Create**, **Exercise**, or a **Fetch** action on a contract `c` with key `k`, or
* `act` is the key assertion **NoSuchKey** `k`.

<div id="def-key-state">
  Definition »key state«
  The **key state** of a key on a ledger is determined by the last action `act` on the key:

  * If `act` is a **Create**, non-consuming **Exercise**, or **Fetch** action on a contract `c`, then the key state is **assigned** to `c`.
  * If `act` is a consuming **Exercise** action or a **NoSuchKey** assertion, then the key state is **free**.
  * If there is no such action `act`, then the key state is **unknown**.
</div>

A key is **unassigned** if its key state is either **free** or **unknown**.

Key consistency ensures that there is at most one active contract for each key and that all key assertions are satisfied.

<div id="def-key-consistency">
  Definition »key consistency«
  A ledger is **consistent for a key** `k` if for every action `act` on `k`, the key state `s` before `act` satisfies

  * If `act` is a **Create** action or **NoSuchKey** assertion, then `s` is **free** or **unknown**.
  * If `act` is an **Exercise** or **Fetch** action on some contract `c`, then `s` is **assigned** to `c` or **unknown**.
</div>

Key consistency rules out the problematic examples around key consistency. For example, suppose that the painter `P` has made a paint offer to `A` with reference number `P123`, but `A` has not yet accepted it. When `P` tries to create another paint offer to `David` with the same reference number `P123`, then this creation action would violate key uniqueness. The following ledger violates key uniqueness for the key `(P, P123)`.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/double-key-creation-highlighted.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=acbd46af202ad664921151e0e182811a" id="double-key-creation" className="align-center" alt="./images/double-key-creation-highlighted.svg" width="1220" height="202" data-path="images/docs_website/double-key-creation-highlighted.svg" />
</figure>

Key assertions can be used in workflows to evidence the inexistence of a certain kind of contract. For example, suppose that the painter `P` is a member of the union of painters `U`. This union maintains a blacklist of potential customers that its members must not do business with. A customer `A` is considered to be on the blacklist if there is an active contract `Blacklist @U &A`. To make sure that the painter `P` does not make a paint offer if `A` is blacklisted, the painter combines its commit with a **NoSuchKey** assertion on the key `(U, A)`. The following ledger shows the transaction, where `UnionMember U P` represents `P`'s membership in the union `U`. It grants `P` the choice to perform such an assertion, which is needed for authorization.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/paint-offer-blacklist.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=75d1f46d626bebacf828a8139db90405" id="paint-offer-blacklist" className="align-center" alt="./images/paint-offer-blacklist.svg" width="1251" height="371" data-path="images/docs_website/paint-offer-blacklist.svg" />
</figure>

Key consistency extends to actions, transactions and lists of transactions just like the other consistency notions.

### Ledger Consistency

Definition »ledger consistency«
A ledger is **consistent** if it is consistent for all contracts and for all keys.

### Internal Consistency

The above consistency requirement is too strong for actions and transactions in isolation. For example, the acceptance transaction from the paint offer example is not consistent as a ledger, because `PaintOffer A P Bank` and the `Iou Bank A` contracts are used without being created before:

However, the transaction can still be appended to a ledger that creates these contracts and yields a consistent ledger. Such transactions are said to be internally consistent, and contracts such as the `PaintOffer A P Bank P123` and `Iou Bank A` are called input contracts of the transaction. Dually, output contracts of a transaction are the contracts that a transaction creates and does not archive.

<div id="def-internal-consistency">
  Definition »internal consistency for a contract«
  A transaction is **internally consistent for a contract c** if the following holds for all of its subactions `act` on the contract `c`

  1. `act` does not happen before any **Create c** action
  2. `act` does not happen after any exercise consuming `c`.

  A transaction is **internally consistent** if it is internally consistent for all contracts and consistent for all keys.
</div>

<div id="def-input-contract">
  Definition »input contract«
  For an internally consistent transaction, a contract `c` is an **input contract** of the transaction if the transaction contains an **Exercise** or a **Fetch** action on `c` but not a **Create c** action.
</div>

<div id="def-output-contract">
  Definition »output contract«
  For an internally consistent transaction, a contract `c` is an **output contract** of the transaction if the transaction contains a **Create c** action, but not a consuming **Exercise** action on `c`.
</div>

Note that the input and output contracts are undefined for transactions that are not internally consistent. The image below shows some examples of internally consistent and inconsistent transactions.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/internal-consistency-examples.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=ac4fdf1301dcb0ae79c2da90326df85f" className="align-center" style={{width: "100.0%"}} alt="./images/internal-consistency-examples.svg" width="1100" height="583" data-path="images/docs_website/internal-consistency-examples.svg" />

  <figcaption>The first two transactions violate the conditions of internal consistency. The first transaction creates the `Iou` after exercising it consumingly, violating both conditions. The second transaction contains a (non-consuming) exercise on the `Iou` after a consuming one, violating the second condition. The last transaction is internally consistent.</figcaption>
</figure>

Similar to input contracts, we define the input keys as the set that must be unassigned at the beginning of a transaction.

Definition »input key«
A key `k` is an **input key** to an internally consistent transaction if the first action `act` on `k` is either a **Create** action or a **NoSuchKey** assertion.

In the blacklisting example, `P`'s transaction has two input keys: `(U, A)` due to the **NoSuchKey** action and `(P, P123)` as it creates a `PaintOffer` contract.

## Conformance

The *conformance* condition constrains the actions that may occur on the ledger. This is done by considering a **contract model** `M` (or a **model** for short), which specifies the set of all possible actions. A ledger is **conformant to M** (or conforms to M) if all top-level actions on the ledger are members of `M`. Like consistency, the notion of conformance does not depend on the requesters of a commit, so it can also be applied to transactions and lists of transactions.

For example, the set of allowed actions on IOU contracts could be described as follows.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/models-simple-iou.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=367e3af7930fd69042909a29a8eff573" className="align-center" style={{width: "80.0%"}} alt="A set of create, transfer, and settle actions allowed on IOU contracts, as described in the paragraph immediately below." width="907" height="420" data-path="images/docs_website/models-simple-iou.svg" />

The boxes in the image are templates in the sense that the contract parameters in a box (such as obligor or owner) can be instantiated by arbitrary values of the appropriate type. To facilitate understanding, each box includes a label describing the intuitive purpose of the corresponding set of actions. As the image suggests, the transfer box imposes the constraint that the bank must remain the same both in the exercised IOU contract, and in the newly created IOU contract. However, the owner can change arbitrarily. In contrast, in the settle actions, both the bank and the owner must remain the same. Furthermore, to be conformant, the actor of a transfer action must be the same as the owner of the contract.

Of course, the constraints on the relationship between the parameters can be arbitrarily complex, and cannot conveniently be reproduced in this graphical representation. This is the role of Daml -- it provides a much more convenient way of representing contract models. The link between Daml and contract models is explained in more detail in a later section.

To see the conformance criterion in action, assume that the contract model allows only the following actions on `PaintOffer` and `PaintAgree` contracts.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/models-paint-offer.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=18c41c80ee34b639d2667e24cd9cb211" className="align-center" style={{width: "90.0%"}} alt="The available create and accept actions on the PaintOffer and PaintAgree contracts." width="942" height="551" data-path="images/docs_website/models-paint-offer.svg" />

The problem with the example where Alice changes the offer's outcome to avoid transferring the money now becomes apparent.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/non-conformant-action.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=8c316201ce7b19be6d74a60c83d5e1fc" className="align-center" alt="A time sequence illustrating the problem as described below." width="1220" height="502" data-path="images/docs_website/non-conformant-action.svg" />

`A`'s commit is not conformant to the contract model, as the model does not contain the top-level action she is trying to commit.

## Authorization

The last criterion rules out the last two problematic examples, an obligation imposed on a painter, and the painter stealing Alice's money. The first of those is visualized below.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/invalid-obligation.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=87da739c05b2ea006c1370a44095d7c4" className="align-center" style={{width: "100.0%"}} alt="A time sequence showing only one commit, in which PaintAgree P A P123 is requested by A." width="1220" height="242" data-path="images/docs_website/invalid-obligation.svg" />

The reason why the example is intuitively impermissible is that the `PaintAgree` contract is supposed to express that the painter has an obligation to paint Alice's house, but he never agreed to that obligation. On paper contracts, obligations are expressed in the body of the contract, and imposed on the contract's *signatories*.

### Signatories and Maintainers

To capture these elements of real-world contracts, the **contract model** additionally specifies, for each contract in the system:

1. A non-empty set of **signatories**, the parties bound by the contract.
2. If the contract is associated with a key, a non-empty set of **maintainers**, the parties that make sure that at most one unconsumed contract exists for the key. The maintainers must be a subset of the signatories and depend only on the key. This dependence is captured by the function `maintainers` that takes a key and returns the key's maintainers.

In the example, the contract model specifies that

1. An `Iou obligor owner` contract has only the `obligor` as a signatory.
2. A `MustPay obligor owner` contract has both the `obligor` and the `owner` as signatories.
3. A `PaintOffer houseOwner painter obligor refNo` contract has only the painter as the signatory. Its associated key consists of the painter and the reference number. The painter is the maintainer.
4. A `PaintAgree houseOwner painter refNo` contract has both the house owner and the painter as signat The key consists of the painter and the reference number. The painter is the only maintainer.

In the graphical representation below, signatories of a contract are indicated with a dollar sign (as a mnemonic for an obligation) and use a bold font. Maintainers are marked with `@` (as a mnemonic who enforces uniqueness). Since maintainers are always signatories, parties marked with `@` are implicitly signatories. For example, annotating the paint offer acceptance action with signatories yields the image below.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/signatories-paint-offer.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=f59d4caeae372b52ca5a79b4043248b9" className="align-center" style={{width: "60.0%"}} alt="The original paint deal flowchart. P is a maintainer; A and the Bank are signatories." width="620" height="363" data-path="images/docs_website/signatories-paint-offer.svg" />

### Authorization Rules

Signatories allow one to precisely state that the painter has an obligation. The imposed obligation is intuitively invalid because the painter did not agree to this obligation. In other words, the painter did not *authorize* the creation of the obligation.

In a Daml ledger, a party can **authorize** a subaction of a commit in either of the following ways:

* Every top-level action of the commit is authorized by all requesters of the commit.
* Every consequence of an exercise action `act` on a contract `c` is authorized by all signatories of `c` and all actors of `act`.

The second authorization rule encodes the offer-acceptance pattern, which is a prerequisite for contract formation in contract law. The contract `c` is effectively an offer by its signatories who act as offerers. The exercise is an acceptance of the offer by the actors who are the offerees. The consequences of the exercise can be interpreted as the contract body so the authorization rules of Daml ledgers closely model the rules for contract formation in contract law.

<div id="da-ledgers-def-well-authorized">
  <div id="da-ledgers-required-authorizers">
    A commit is **well-authorized** if every subaction `act` of the commit is authorized by at least all of the **required authorizers** of `act`, where:
  </div>
</div>

1. the required authorizers of a **Create** action on a contract `c` are the signatories of `c`.
2. the required authorizers of an **Exercise** or a **Fetch** action are its actors.
3. the required authorizers of a **NoSuchKey** assertion are the maintainers of the key.

We lift this notion to ledgers, whereby a ledger is well-authorized exactly when all of its commits are.

### Examples

An intuition for how the authorization definitions work is most easily developed by looking at some examples. The main example, the paint offer ledger, is intuitively legitimate. It should therefore also be well-authorized according to our definitions, which it is indeed.

In the visualizations below, `Π ✓ act` denotes that the parties `Π` authorize the action `act`. The resulting authorizations are shown below.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/authorization-paint-offer.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=489df8e52d59814ff917a1f669b1e202" className="align-center" alt="The original paint deal time sequence, described in depth with respect to authorizations below." width="1311" height="502" data-path="images/docs_website/authorization-paint-offer.svg" />

In the first commit, the bank authorizes the creation of the IOU by requesting that commit. As the bank is the sole signatory on the IOU contract, this commit is well-authorized. Similarly, in the second commit, the painter authorizes the creation of the paint offer contract, and painter is the only signatory on that contract, making this commit also well-authorized.

The third commit is more complicated. First, Alice authorizes the exercise on the paint offer by requesting it. She is the only actor on this exercise, so this complies with the authorization requirement. Since the painter is the signatory of the paint offer, and Alice the actor of the exercise, they jointly authorize all consequences of the exercise. The first consequence is an exercise on the IOU, with Alice as the actor, so this is permissible. The second consequence is the creation of the new IOU (for P) by exercising the old IOU (for A). As the IOU was formerly signed by the bank, with Alice as the actor of the exercise, they jointly authorize this creation. This action is permissible as the bank is the sole signatory. The final consequence is creating the paint agreement with Alice and the painter as signatories. Since they both authorize the action, this is also permissible. Thus, the entire third commit is also well-authorized, and so is the ledger.

Similarly, the intuitively problematic examples are prohibited by our authorization criterion. In the first example, Alice forced the painter to paint her house. The authorizations for the example are shown below.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/authorization-invalid-obligation.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d200a3bae13cf1b9de6cbf4664112c70" className="align-center" alt="A time sequence for a scenario where Alice forces the painter to paint her house, described in depth with respect to authorization below." width="1220" height="242" data-path="images/docs_website/authorization-invalid-obligation.svg" />

Alice authorizes the **Create** action on the `PaintAgree` contract by requesting it. However, the painter is also a signatory on the `PaintAgree` contract, but he did not authorize the **Create** action. Thus, this ledger is indeed not well-authorized.

In the second example, the painter steals money from Alice.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/authorization-stealing-ious.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=46bd84bcbf8f39ac6fff1787bc759dc4" className="align-center" alt="A time sequence for a scenario where the painter steals Alice's money, described in depth with respect to authorization below." width="1220" height="355" data-path="images/docs_website/authorization-stealing-ious.svg" />

The bank authorizes the creation of the IOU by requesting this action. Similarly, the painter authorizes the exercise that transfers the IOU to him. However, the actor of this exercise is Alice, who has not authorized the exercise. Thus, this ledger is not well-authorized.

## Valid Ledgers, Obligations, Offers and Rights

Daml ledgers are designed to mimic real-world interactions between parties, which are governed by contract law. The validity conditions on the ledgers, and the information contained in contract models have several subtle links to the concepts of the contract law that are worth pointing out.

First, contracts specify implicit **on-ledger obligations**, which result from consequences of the exercises on contracts. For example, the `PaintOffer` contains an on-ledger obligation for `A` to transfer her IOU in case she accepts the offer.

Second, every contract on a Daml ledger can model a real-world offer, whose consequences (both on- and off-ledger) are specified by the **Exercise** actions on the contract allowed by the contract model.

Third, in Daml ledgers, as in the real world, one person's rights are another person's obligations. For example, `A`'s right to accept the `PaintOffer` is `P`'s obligation to paint her house in case she accepts. In Daml ledgers, a party's rights according to a contract model are the exercise actions the party can perform, based on the authorization and conformance rules.

Finally, validity conditions ensure three important properties of the Daml ledger model, that mimic the contract law.

1. **Obligations need consent**. Daml ledgers follow the offer-acceptance pattern of the contract law, and thus ensures that all ledger contracts are formed voluntarily. For example, the following ledger is not valid.

   <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/authorization-invalid-obligation.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d200a3bae13cf1b9de6cbf4664112c70" className="align-center" style={{width: "100.0%"}} alt="The time sequence for a scenario where Alice forces the painter to paint her house, explained previously in the Authorization Rules Example section." width="1220" height="242" data-path="images/docs_website/authorization-invalid-obligation.svg" />

2. **Consent is needed to take away on-ledger rights**. As only **Exercise** actions consume contracts, the rights cannot be taken away from the actors; the contract model specifies exactly who the actors are, and the authorization rules require them to approve the contract consumption.

   In the examples, Alice had the right to transfer her IOUs; painter's attempt to take that right away from her, by performing a transfer himself, was not valid.

   <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/authorization-stealing-ious.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=46bd84bcbf8f39ac6fff1787bc759dc4" className="align-center" style={{width: "100.0%"}} alt="The time sequence for a scenario where the painter steals Alice's money, explained previously in the Authorization Rules Example section." width="1220" height="355" data-path="images/docs_website/authorization-stealing-ious.svg" />

   Parties can still **delegate** their rights to other parties. For example, assume that Alice, instead of accepting painter's offer, decides to make him a counteroffer instead. The painter can then accept this counteroffer, with the consequences as before:

   <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-acceptance.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9923105b566068031bd08e1f6787c44d" id="counteroffer-acceptance" className="align-center" style={{width: "60.0%"}} alt="The original PaintAgreement flow chart, but now the topmost contract is the CounterOffer." width="600" height="363" data-path="images/docs_website/counteroffer-acceptance.svg" />

   Here, by creating the `CounterOffer` contract, Alice delegates her right to transfer the IOU contract to the painter. In case of delegation, prior to submission, the requester must get informed about the contracts that are part of the requested transaction, but where the requester is not a signatory. In the example above, the painter must learn about the existence of the IOU for Alice before he can request the acceptance of the `CounterOffer`. The concepts of observers and divulgence, introduced in the next section, enable such scenarios.

3. **On-ledger obligations cannot be unilaterally escaped**. Once an obligation is recorded on a Daml ledger, it can only be removed in accordance with the contract model. For example, assuming the IOU contract model shown earlier, if the ledger records the creation of a `MustPay` contract, the bank cannot later simply record an action that consumes this contract:

   <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/validity-no-removal-of-obligations.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=8eb83f0989399fc8152a044a779fa839" className="align-center" style={{width: "100.0%"}} alt="A time sequence in which the first commit includes the creation of a MustPay contract and the second commit includes the bank consuming this contract, as described above." width="1220" height="251" data-path="images/docs_website/validity-no-removal-of-obligations.svg" />

   That is, this ledger is invalid, as the action above is not conformant to the contract model.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/overview/explanations/ledger-model/ledger-privacy.rst" hash="b3c9457c" */}

# Privacy

The ledger structure section answered the question "What does the Ledger looks like?" by introducing a hierarchical format to record the party interactions as changes. This section addresses the question "Who sees which changes and data?". That is, it explains the privacy model for Canton Ledgers.

The privacy model of Canton Ledgers is based on a **need-to-know basis**, and provides privacy **on the level of subtransactions**. Namely, a party learns only those parts of party interactions that affect contracts in which the party has a stake, and the consequences of those interactions. The hierarchical structure is key here because it yields a natural notion of sub-transaction privacy. To make the sub-transaction privacy notion precise, we introduce the concepts of *informee* and *witness*.

## Informee

A party can take different roles in Daml templates and choices; the party can be declared as `signatory`, choice `controller`, or contract or choice `observer`. For a contract, a party is a **stakeholder** if it is a signatory or contract observer of the contract.

* Every contract and choice `observer` should observe changes to the contract (creation or archival) and exercises of a choice, respectively, as the name suggests.
* A `signatory` is bound by a contract and thus has a stake in it; they should learn when the contract is created or used.
* An actor of an Exercise, which is the `controller` of the choice, has a stake in the action and should therefore see the exercise; they may not have a stake in the contract though.

These observations motivate the following definition of an **informee**, namely the set of parties that should be informed about an action. The informees for a node are the union of the sets marked with X in the following table,

<div id="def-informee">
  | Action                     | Signatories | Contract observers | Actors | Choice observers |
  | -------------------------- | ----------- | ------------------ | ------ | ---------------- |
  | **Create**                 | X           | X                  |        |                  |
  | consuming **Exercise**     | X           | X                  | X      | X                |
  | non-consuming **Exercise** | X           |                    | X      | X                |
  | **Fetch**                  | X           |                    | X      |                  |

  Definiton: The **informees** of a node are the union of the sets marked with X.
</div>

For example, the informees of a **Create** node are the stakeholders of the created contract, that is, the signatories and observers. For consuming **Exercise** node, the informees consist of the stakeholders of the consumed contract, the action's actors and choice observers.

As a design decision, a contract observer is not informed about non-consuming **Exercise** and **Fetch** actions, unless they are explicitly among the actors or choice observers. This is because such actions do not change the state of the contract itself.

<Note>
  Templates can declare `preconsuming` and `postconsuming` choices. Daml compiles such choices to a non-consuming choice whose first or last consequence exercises the `Archive` choice on the template. Accordingly, contract observers are only informees of the `Archive` subaction, but not of the main `Exercise` action itself.
</Note>

To illustrate the concept of informees, we use the running example of Alice and Bob swapping their assets. The nodes in the `AcceptAndSettle` action have the informees shown in the blue hexagons of the next figure. For example, Alice is an informee of the root node ① because she is a signatory of the input contract #3, and Bob is an informee because he is the actor of the choice. Similarly, Bank 2 and Bob are informees of the Fetch node ③ because Bank 2 is a signatory of the input contract #2 and Bob is the actor. Had Bob not been the actor, he would not be an informee because contract observers are not automatically informees of non-consuming Exercises and Fetches.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-acceptandsettle-informees.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=deab88d50ec2ecdae62259b6fc20baa5" className="align-center" style={{width: "100.0%"}} alt="The informees of the nodes in the ``AcceptAndSettle`` action." width="2321" height="1311" data-path="images/docs_website/dvp-acceptandsettle-informees.svg" />

The informees for an action are the informees of its root node. Importantly, nodes cannot exist without their children on the Ledger, as mentioned in the ledger structure section; only actions can as they are whole trees. Accordingly, the informees of an action are entitled to see all nodes in the action, even if they are not informees of some of the individual nodes themselves. This discrepancy is formalized under this notion of witnesses in the next section.

## Witness

A single node can be part of multiple actions. For example, the diagram below extends the subaction diagram with the informees shown in the top right corner of the borderless box for each subaction. Here, the Create node ③ is part of three subactions, namely those rooted at nodes ①, ②, and ③. Accordingly, this Create node is shown to the informees of all these actions, even if they are not informees of the node itself. Those parties are called witnesses. Formally, for a given transaction `tx`, the **witnesses** of a node in `tx` are the union of the informees of all subactions of `tx` that contain the node. In particular, every informee of the node is also a witness.

The diagram shows the witnesses of a subaction in purple on its root action. For node ③, the witnesses are Alice, Bob, and Bank 1, because Bob is an informee of ① and ③; Bank 1 is an informee of ② and ③; and Alice is an informee of ① and ②.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/dvp-settle-witness.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=fced7c0cefb8dc1176e5657ff6ce9e75" className="align-center" style={{width: "60.0%"}} alt="The informees of the subactions of the ``Settle`` choice and the witnesses of the nodes." width="1122" height="1082" data-path="images/docs_website/dvp-settle-witness.svg" />

## Projection

Informees should see the changes they are entitled to see, but this does not mean that they are entitled to see the entirety of any transaction that includes such a change. This is made precise through *projections* of a transaction, which define the view that a group of parties gets on a transaction. Intuitively, given a transaction within a commit, a group of parties sees only the subtransaction consisting of all actions on contracts whose informees include at least one of the parties. Equivalently, the group of parties sees only those nodes whose witnesses include at least one of the parties. Thus, privacy is obtained on the subtransaction level.

This section first defines projections for transactions and then for ledgers.

### Transaction projection

The next diagram gives an example for a transaction with the `AcceptAndSettle` Exercise action as the only root action, whose informees are shown in the diagrams above.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-acceptandsettle-projection.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=19d1943bd83536d7d81d2d3748a81ef1" className="align-center" style={{width: "100.0%"}} alt="image" width="1748" height="3362" data-path="images/docs_website/dvp-acceptandsettle-projection.svg" />

Since both Alice and Bob are informees of the root action, namely Bob exercising the `AcceptAndSettle` choice on Alice's `ProposeSimpleDvP` contract, the projection to either Alice or Bob or both consists of the whole Exercise action. As an action consists of the whole subtree underneath its root node, Alice and Bob each see all the nodes they are witnesses of. For example, Alice's projection includes the Fetch subaction, Bob's `Transfer` exercise of on #2, and the creation of Bob's `SimpleAsset` contract #5. Similarly, Bob's projection includes Alice's `Transfer` Exercise on #1 and the creation of Alice's `SimpleAsset` contract #6.

In contrast, the banks are *not* informees of the root action. In fact, Bank 1 appears as an informee only in the `Transfer` Exercise action on #1 and its subaction, the creation of Bob's new asset #5. Accordingly, the projection to Bank 1 consists of just this Exercise action. Bank 2 appears as an informee of two unrelated actions in the tree: the Fetch action and the `Transfer` Exercise action on #2. The projection to Bank 2 therefore consists of a transaction with these two actions as root actions. This shows that projection can turn a single root action into a list of subactions.

<Note>
  Note the privacy implications of the banks' projections. While each bank learns that a `Transfer` has occurred from Alice to Bob or vice versa, each bank does *not* learn anything about *why* the transfer occurred. In particular, Bank 2 does not learn what happens between the Fetch and the Exercise on contract #2. In practice, this means that Bank 1 and Bank 2 do not learn what Alice and Bob is exchanging their asset for, providing privacy to Alice and Bob with respect to the banks.
</Note>

The projection to both Bank 1 and Bank 2 at the bottom shows that a projection to several parties may contain strictly more information than the projections to each of the parties together. Said differently, it is impossible to reconstruct the projection to Bank 1 and Bank 2 solely from the projection for Bank 1 and the projection for Bank 2. Here, this is because the order of the three root actions cannot be uniquely determined from the individual projections. For this reason, projection is defined for a set of parties.

<div id="def-tx-projection">
  <Note>
    **Definition: projection**

    The **projection** of a transaction for a set `P` of parties is the subtransaction obtained by doing the following for each root action `act` of the transaciton.

    1. If `P` contains at least one of the informees of `act`, keep `act` as-is, including its consequences.
    2. Else, if `act` has consequences, replace `act` by the projection (for `P`) of its consequences, which might be empty.
    3. Else, drop `act` including its consequences.
  </Note>
</div>

This definition does not operate on nodes, but on actions, that is, subtrees of nodes. Accordingly, the projection of a transaction for a set of parties `P` contains a node if and only if `P` contains at least one of the witnesses of the node.

As a projection is a transaction, it is possible to project a projection further. The projection operation has the following **absorbtion** property: Projection to decreasing subsets of parties is absorbing. That is, if a set of parties `P` is a subset of `Q`, then projecting a transaction first to `Q` and then to `P` is the same as projecting it directly to `P`. Intuitively, this property expresses the fact that a group of parties jointly learns at least as much about a transaction as any subgroup of these parties learns by themselves. The converse is false, as the above example with projection to Banks 1 and 2 has shown.

Conversely, if `P` is not a subset of `Q`, then projecting a transaction first to `Q` and then to `P` will merely result in a subtransaction of the projection to `P`. For example, if we project the above projection for Bank 1 to Bob, the resulting transaction consists only of the Create action for contract #5. This is a proper subtransaction of Bob's projection.

This difference reflects that Bank 1 learns less about the Exercise node than Bob. In particular, Bank 1 cannot infer from its projection that Bob is a witness of the Exercise node. This is a general pattern: the informees of an action may not learn about witnesses of nodes therein. This is crucial from a privacy perspective as it hides who is involved in the hidden parts of the transaction.

### Ledger projection

Finally, the **projection of a ledger** `l` for a set `P` of parties is a DAG of updates obtained as follows:

* Project the transaction of each update in `l` for `P`, but retain the update ID.
* Remove updates with empty transactions from the result.

We defer defining the edges in the projection to the causality section. Until then, we pretend that the ledger is totally ordered and projections retain the same ordering.

Notably, the projection of a ledger is not a ledger, but a DAG of updates. The requesters from the commit cannot be retained because they are typically witnesses of the actions in the projection, but not informees. Yet, the informees of the action must not know all the witnesses. For example, if Bank 1's projection did mention Bob as the requester of the last commit, then Bank 1 could infer that Bob is a witness of Alice exercising the `Transfer` choice on contract #1.

Projecting the ledger of the complete DvP example yields the following projections for each party.

<div id="da-dvp-ledger-projections" />

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/dvp-ledger-projections.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9f32669cafa03a1f454985a745255eee" id="da-ledgers-projections-example" className="align-center" style={{width: "100.0%"}} alt="Time sequences for each party's projection, explained in-depth in the numbered list below." width="3802" height="5682" data-path="images/docs_website/dvp-ledger-projections.svg" />

Examine each party's projection in turn:

1. Alice sees all of the first, thrid, and forth commit as she is an informee of all root actions. In contrast, Alice does not see anything of the second commit, as she is not a stakeholder of Bob's `SimpleAsset` of 1 USD. This transaction is not present in Alice's projection at all. Yet, the output of this transaction (contract #2) is used in the last commit of Alice's projection. Accordingly, contract #2 is shown as an input to the left, outside of the ledger. This effect is discussed below under retroactive divulgence.
2. Bob's projection is analogous to Alice's: He sees everything of the second, third, and forth commit, but nothing of the first commit and instead merely contract #1 as an input.
3. Banks 1 and 2 only see the commits in which they create their `SimpleAsset` and the `Transfer` Exercises on them. Additionally, Bank 2 sees the Fetch of the `SimpleAsset` in the last commit, as already discussed above for transaction projections.

The update IDs enable correlation across the different projections. For example, Bank 1 and Bank 2 both see the update ID `TX 3`. They can therefore infer that their projections have happened in the same atomic transaction even though their projections do not share a single node.

<Note>
  A user of a Participant Node can request the Ledger projection for the user's parties via the updates tree stream.
</Note>

## Divulgence: When non-stakeholders see contracts

The guiding principle for the privacy model of Canton ledgers is that contracts should only be shown to their stakeholders. However, ledger projections can cause contracts to become visible to other parties as well. Showing contracts to non-stakeholders through ledger projections is called **divulgence**. Divulgence is a deliberate choice in the design of Canton Ledgers and comes in two forms:

* **Immediate divulgence** refers to witnesses seeing contract creations they are not an informee of. In the example of ledger projections of the DvP, Bob is a witness of the Create action for Alice's new `SimpleAsset` (contract #6), but not an informee. Conceptually, at the instant where Bob exercises the `Transfer` choice, he also gains a temporary stake in the outcome of the `Transfer`, namely to see that the asset now belongs to Alice.

  In general, there is no point in hiding the consequences of an action. Bob could anyway compute the consequences of the actions it is an informee of, because Daml is deterministic.

* **Retroactive divulgence** refers to an input contract being shown to the non-informee witnesses of a node using this contract. For example, the Fetch on Bob's `SimpleAsset` (contract #2) is visible to Alice and Alice's projection therefore references this contract as an input even though the Create action for #2 is not part of Alice's projection.

  Retroactive divulgence enables Alice to validate the transactions in her projection (see `da-model-consistency` for ledger integrity). That is, Alice can check that Bob does allocate a suitable `SimpleAsset` according to what she specified in her proposal.

  Retroactive divulgence does not make Alice a witness of the Create action for Bob's `SimpleAsset` (contract #2), because an input contract is not the same as its Create action. In the diagrams, this distinction is visualized via the dashed border for input contracts and them being placed to the left.

Via the Ledger API's update service, a user can see the immediately divulged contracts in the trees of the parties' projection as these trees contain the Create nodes. In contrast, the Ledger API currently does not offer a means for a user to look up a contract ID of a retroactive divulgence.

## Disclosure: When non-stakeholders use contracts

Divulgence from the previous section refers to parties learning about contracts they are not a stakeholder of. Disclosure is about such parties using contracts in their own transactions.

Recall from the running example that Bob uses `submitWithDisclosures` for the exercising `Settle` choice. This is because Bob (and its Participant Node) in general does not know about the `SimpleAsset` contract #2 that Alice has allocated to the proposal. Disclosure means that Alice tells Bob via an off-ledger communication channel about this contract. In the Daml script running example, the script itself is the communication channel. In real-world contexts, Alice would offer an API for Bob to retrieve the relevant data.

It is a design decision that immediate divulgence does not entail disclosure for subsequent transactions. For example, after the DvP has been settled, Alice creates another DvP proposal for Bob to swap the two assets again:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
proposeDvP2 <- submit alice $ do
  createCmd ProposeSimpleDvP with
      proposer = alice
      counterparty = bob
      allocated = newUsd
      expected = eurAsset
```

Then, Bob's command submission must include the disclosure of Alice's `SimpleAsset` even though Bob is a witness of the creation of Alice's `SimpleAsset`. A plain `submit` without disclosure does not work.

The motivation for not using immediate divulgence implicitly for disclosure is that it leads to brittle workflows. The problem is that the non-stakeholders only learn about the creation of the contract, but not about subsequent actions on the contract like archivals. Accordingly, there is no general rule as to how long the non-stakeholder should long to keep the contract around. Keeping it for too long will waste storage; and keeping it too short may break certain applications. Instead, this rule forces the application to explicitly design for disclosure even for divulged contracts and come up with a suitable application-specific rule.

An alternative approach to disclosure is to replace the original `SimpleAsset` contract by one on which the Bob becomes a contract observer. This requires extending the contract model with a (consuming) exercise action on the `SimpleAsset` that creates a new `SimpleAsset`, with observers of Alice's choice. In addition to the increase in actions on the Ledger, the two approaches differ in in who learns about the parties that are informed about the contract:

* If Alice discloses her `SimpleAsset` to Bob via an off-ledger channel, only Alice and Bob need to know about this disclosure. So when Alice discloses the same contract to Charlie, Charlie does not need to know that Alice had already shown the contract to Bob, and Bob does not need to know that Alice is disclosing it to Charlie.
* In contrast, when Alice adds Bob as a contract observer and then subsequently adds Charlie as another observer, Bob as a contract observer is notified about the archival and the creation. Similarly, Charlie learns that Bob is an observer on the contract, too. That is, all stakeholders learn about each other. This created a privacy problem when Alice actually does not want that Bob and Charlie know of each other.

Moveover, adding parties as observers scales poorly to large numbers, because every observer learns about every other observer: A Create event with `N` observers appears in the projection of at least those `N` parties. So the size of all projections together is already quadratic in `N` as an action of size at least `N` appears in `N` different projection. If the observers are added one by one, then `N` archives and creations are needed, which means the size of all projections together is cubic in `N`.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/overview/explanations/ledger-model/interoperability.rst" hash="a2bb1cc4" */}

# Synchronizer-aware projection

<Note>
  * Disentangle abuse of ledger term: the VSL from what is coordinated over a synchronizer
  * Define synchronizer-aware projections (assign and unassign events)
</Note>

Certain Daml ledgers can interoperate with other Daml ledgers. That is, the contracts created on one ledger can be used and archived in transactions on other ledgers. Some Participant Nodes can connect to multiple ledgers and provide their parties unified access to those ledgers via the Ledger API. For example, when an organization initially deploys two workflows to two Daml ledgers, it can later compose those workflows into a larger workflow that spans both ledgers.

Interoperability may limit the visibility a Participant Node has into a party's ledger projection, i.e., its local ledger, when the party is hosted on multiple Participant Nodes. These limitations influence what parties can observe via the Ledger API of each Participant Node. In particular, interoperability affects which events a party observes and their order. This document explains the visibility limitations due to interoperability and their consequences for the Update Service, by example and formally by introducing interoperable versions of causality graphs and projections.

The presentation assumes that you are familiar with the following concepts:

* The Ledger API
* The Daml Ledger Model
* Local ledgers and causality graphs

<Note>
  Interoperability for Daml ledgers is under active development. This document describes the vision for interoperability and gives an idea of how the Ledger API services may change and what guarantees are provided. The described services and guarantees may change without notice as the interoperability implementation proceeds.
</Note>

## Interoperability Examples

### Topology

Participant Nodes connect to Daml ledgers and parties access projections of these ledgers via the Ledger API. The following picture shows such a setup.

<figure>
  <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/multiple-domains.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=8a18fc12d93bfbf8bdfc408395b6650c" id="multiple-ledgers" className="align-center" alt="./../images/multiple-domains.svg" width="1200" height="637" data-path="images/docs_website/multiple-domains.svg" />

  <figcaption>Example topology with two interoperable ledgers</figcaption>
</figure>

The components in this diagram are the following:

* There is a set of interoperable **Daml ledgers**: Ledger 1 (green) and Ledger 2 (yellow).
* Each **Participant Node** is connected to a subset of the Daml ledgers.
  * Participant Nodes 1 and 3 are connected to Ledger 1 and 2.
  * Participant Node 2 is connected to Ledger 1 only.
* Participant Nodes host parties on a subset of the Daml ledgers they are connected to. A Participant Node provides a party access to the Daml ledgers that it hosts the party on.
  * Participant Node 1 hosts Alice on Ledger 1 and 2.
  * Participant Node 2 hosts Alice on Ledger 1.
  * Participant Node 3 hosts the painter on Ledger 1 and 2.

### Aggregation at the Participant

The Participant Node assembles the updates from these ledgers and outputs them via the party's Update Service and State Service. When a Participant Node hosts a party only on a subset of the interoperable Daml ledgers, then the Update and State Services of the Participant Node are derived only from those ledgers.

For example, in the above topology, when a transaction creates a contract with stakeholder Alice on Ledger 2, then `P1`'s transaction stream for Alice will emit this transaction and report the contract as active, but Alice's stream at `P2` will not.

### Enter and Leave Events

With interoperability, a transaction can use a contract whose creation was recorded on a different ledger. In the above topology, e.g., one transaction creates a contract `c1` with stakeholder Alice on Ledger 1 and another archives the contract on Ledger 2. Then the Participant Node `P2` outputs the **Create** action as a `CreatedEvent`, but not the **Exercise** in form of an `ArchiveEvent` on the Update Service because Ledger 2 can not notify `P2` as `P2` does not host Alice on Ledger 2. Conversely, when one transaction creates a contract `c2` with stakeholder Alice on Ledger 2 and another archives the contract on Ledger 1, then `P2` outputs the `ArchivedEvent`, but not the `CreatedEvent`.

To keep the transaction stream consistent, `P2` additionally outputs a **Leave** `c1` action on Alice's transaction stream. This action signals that the Participant Node no longer outputs events concerning this contract; in particular not when the contract is archived. The contract is accordingly no longer reported in the State Service and cannot be used by command submissions.

Conversely, `P2` outputs an **Enter** `c2` action some time before the `ArchivedEvent` on the transaction stream. This action signals that the Participant Node starts outputting events concerning this contract. The contract is reported in the State Service and can be used by command submission.

The actions **Enter** and **Leave** are similar to a **Create** and a consuming **Exercise** action, respectively, except that **Enter** and **Leave** may occur several times for the same contract whereas there should be at most one **Create** action and at most one consuming **Exercise** action for each contract.

These **Enter** and **Leave** events are generated by the underlying interoperability protocol. This may happen as part of command submission or for other reasons, e.g., load balancing. It is guaranteed that the **Enter** action precedes contract usage, subject to the trust assumptions of the underlying ledgers and the interoperability protocol.

A contract may enter and leave the visibility of a Participant Node several times. For example, suppose that the painter submits the following commands and their commits end up on the given ledgers.

1. Create a contract `c` with signatories Alice and the painter on Ledger 2
2. Exercise a non-consuming choice `ch1` on `c` on Ledger 1.
3. Exercise a non-consuming choice `ch2` on `c` on Ledger 2.
4. Exercise a consuming choice `ch3` on `c` on Ledger 1.

Then, the transaction tree stream that `P2` provides for `A` contains five actions involving contract \`c\`: **Enter**, non-consuming **Exercise**, **Leave**, **Enter**, consuming **Exercise**. Importantly, `P2` must not omit the **Leave** action and the subsequent **Enter**, even though they seem to cancel out. This is because their presence indicates that `P2`'s event stream for Alice may miss some events in between; in this example, exercising the choice `ch2`.

The flat transaction stream by `P2` omits the non-consuming exercise choices. It nevertheless contains the three actions **Enter**, **Leave**, **Enter** before the consuming **Exercise**. This is because the Participant Node cannot know at the **Leave** action that there will be another **Enter** action coming.

In contrast, `P1` need not output the **Enter** and **Leave** actions at all in this example because `P1` hosts Alice on both ledgers.

### Cross-ledger Transactions

With interoperability, a cross-ledger transaction can be committed on several interoperable Daml ledgers simultaneously. Such a cross-ledger transaction avoids some of the synchronization overhead of **Enter** and **Leave** actions. When a cross-ledger transaction uses contracts from several Daml ledgers, stakeholders may witness actions on their contracts that are actually not visible on the Participant Node.

For example, suppose that the split paint counteroffer workflow from the causality examples is committed as follows: The actions on `CounterOffer` and `PaintAgree` contracts are committed on Ledger 1. All actions on `Iou`s are committed on Ledger 2, assuming that some Participant Node hosts the Bank on Ledger 2. The last transaction is a cross-ledger transaction because the archival of the `CounterOffer` and the creation of the `PaintAgree`ment commits on Ledger 1 simultaneously with the transfer of Alice's `Iou` to the painter on Ledger 2.

For the last transaction, Participant Node 1 notifies Alice of the transaction tree, the two archivals and the `PaintAgree` creation via the Update Service as usual. Participant Node 2 also output's the whole transaction tree on Alice's transaction tree stream, which contains the consuming **Exercise** of Alice's `Iou`. However, it has not output the **Create** of Alice's `Iou` because `Iou` actions commit on Ledger 2, on which Participant Node 2 does not host Alice. So Alice merely *witnesses* the archival even though she is an informee of the exercise. The **Exercise** action is therefore marked as merely being witnessed on Participant Node 2's transaction tree stream.

In general, an action is marked as **merely being witnessed** when a party is an informee of the action, but the action is not committed on a ledger on which the Participant Node hosts the party. Unlike **Enter** and **Leave**, such witnessed actions do not affect causality from the participant's point of view and therefore provide weaker ordering guarantees. Such witnessed actions show up neither in the flat transaction stream nor in the State Service.

For example, suppose that the **Create** `PaintAgree` action commits on Ledger 2 instead of Ledger 1, i.e., only the `CounterOffer` actions commit on Ledger 1. Then, Participant Node 2 marks the **Create** `PaintAgree` action also as merely being witnessed on the transaction tree stream. Accordingly, it does not report the contract as active nor can Alice use the contract in her submissions via Participant Node 2.

## Multi-ledger Causality Graphs

This section generalizes causality graphs to the interoperability setting.

Every active Daml contract resides on at most one Daml ledger. Any use of a contract must be committed on the Daml ledger where it resides. Initially, when the contract is created, it takes up residence on the Daml ledger on which the **Create** action is committed. To use contracts residing on different Daml ledgers, cross-ledger transactions are committed on several Daml ledgers.

However, cross-ledger transactions incur overheads and if a contract is frequently used on a Daml ledger that is not its residence, the interoperability protocol can migrate the contract to the other Daml ledger. The process of the contract giving up residence on the origin Daml ledger and taking up residence on the target Daml ledger is called a **contract transfer**. The **Enter** and **Leave** events on the transaction stream originate from such contract transfers, as will be explained below. Moreover, contract transfers are synchronization points between the origin and target Daml ledgers and therefore affect the ordering guarantees. We therefore generalize causality graphs for interoperability.

Definition »Transfer action«
A **transfer action** on a contract `c` is written **Transfer** `c`. The **informees** of the transfer actions are the stakeholders of `c`.

In the following, the term *action* refers to transaction actions (**Create**, **Exercise**, **Fetch**, and **NoSuchKey**) as well as transfer actions. In particular, a transfer action on a contract `c` is an action on `c`. Transfer actions do not appear in transactions though. So a transaction action cannot have a transfer action as a consequence and transfer actions do not have consequences at all.

Definition »Multi-Ledger causality graph«
A **multi-ledger causality graph** `G` for a set `Y` of Daml ledgers is a finite, transitively closed, directed acyclic graph. The vertices are either transactions or transfer actions. Every action is possibly annotated with an **incoming ledger** and an **outgoing ledger** from `Y` according to the following table:

| Action                     | incoming ledger | outgoing ledger |
| -------------------------- | --------------- | --------------- |
| **Create**                 | no              | yes             |
| consuming **Exercise**     | yes             | no              |
| non-consuming **Exercise** | yes             | yes             |
| **Fetch**                  | yes             | yes             |
| **NoSuchKey**              | no              | no              |
| **Transfer**               | maybe           | maybe           |

For non-consuming **Exercise** and **Fetch** actions, the incoming ledger must be the same as the outgoing ledger. **Transfer** actions must have at least one of them. A **transfer** action with both set represents a complete transfer. If only the incoming ledger is set, it represents the partial information of an **Enter** event; if only outgoing is set, it is the partial information of a **Leave** event. **Transfer** actions with missing incoming or outgoing ledger annotations referred to as **Enter** or **Leave** actions, respectively.

The action order generalizes to multi-ledger causality graphs accordingly.

In the example for Enter and Leave events where the painter exercises three choices on contract `c` with signatories Alice and the painter, the four transactions yield the following multi-ledger causality graph. Incoming and outgoing ledgers are encoded as colors (green for Ledger 1 and yellow for Ledger 2). **Transfer** vertices are shown as circles, where the left half is colored with the incoming ledger and the right half with the outgoing ledger.

<div id="interoperable-causality-graph-linear">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/interoperable-causality-graph-linear.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=24daba5cd4c959fd25e6e92123ae70de" className="align-center" style={{width: "100.0%"}} alt="./../images/interoperable-causality-graph-linear.svg" width="1440" height="183" data-path="images/docs_website/interoperable-causality-graph-linear.svg" />

    <figcaption>Multi-Ledger causality graph with transfer actions</figcaption>
  </figure>
</div>

<Note>
  As for ordinary causality graphs, the diagrams for multi-ledger causality graphs omit transitive edges for readability.
</Note>

As an example of a cross-domain transaction, consider the split paint counteroffer workflow with the cross-domain transaction. The corresponding multi-ledger causality graph is shown below. The last transaction `tx4` is a cross-ledger transaction because its actions have more than one color.

<div id="counteroffer-interoperable-causality-graph">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-interoperable-causality-graph.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=a00a595da5b5ff73b7432c091c20ac2f" className="align-center" style={{width: "100.0%"}} alt="./../images/counteroffer-interoperable-causality-graph.svg" width="1440" height="380" data-path="images/docs_website/counteroffer-interoperable-causality-graph.svg" />

    <figcaption>Multi-Ledger causality graph for the split paint counteroffer workflow on two Daml ledgers</figcaption>
  </figure>
</div>

### Consistency

Definition »Ledger trace«
A **ledger trace** is a finite list of pairs `(a``i``, b``i``)` such that `b``i - 1` = `a``i` for all `i` > 0. Here `a``i` and `b``i` identify Daml ledgers or are the special value `NONE`, which is different from all Daml ledger identifiers.

Definition »Multi-Ledger causal consistency for a contract«
Let `G` be a multi-ledger causality graph and `X` be a set of actions from `G` on a contract in `c`. The graph `G` is **multi-ledger consistent for the contract** `c` on `X` if all of the following hold:

1. If `X` is not empty, then `X` contains a **Create** or at least one **Enter** action. If it contains a create, then this create precedes all other actions in `X`. If it does not, then there exists one **Enter** action that precedes all other actions in `X`.
2. `X` contains at most one **Create** action.
3. If `X` contains a consuming **Exercise** action `act`, then `act` follows all other actions in `X` in `G`'s action order.
4. All **Transfer** actions in `X` are ordered with all other actions in `X`.
5. For every maximal chain in `X` (i.e., maximal totally ordered subset of `X`), the sequence of `(`incoming ledger, outgoing ledger`)` pairs is a ledger trace, using `NONE` if the action does not have an incoming or outgoing ledger annotation.

The first three conditions mimic the conditions of causal consistency for ordinary causality graphs. They ensure that **Create** actions come first and consuming **Exercise** actions last. An **Enter** action takes the role of a **Create** if there is no **Create**. The fourth condition ensures that all transfer actions are synchronization points for a contract. The last condition about ledger traces ensures that contracts reside on only one Daml ledger and all usages happen on the ledger of residence. In particular, the next contract action after a **Leave** must be an **Enter**.

For example, the above multi-ledger causality graph with transfer actions is multi-ledger consistent for `c`. In particular, there is only one maximal chain in the actions on `c`, namely

> **Create** `c` -> `tf1` -> **ExeN** `B` `c` `ch1` -> `tf2` -> **ExeN** `B` `c` `ch2` -> `tf3` -> **ExeN** `B` `c` `ch3`,

and for each edge `act``1` -> `act``2`, the outgoing ledger color of `act``1` is the same as the incoming ledger color of `act``2`. The restriction to maximal chains ensures that no node is skipped. For example, the (non-maximal) chain

> **Create** `c` -> **ExeN** `B` `c` `ch1` -> `tf2` -> **ExeN** `B` `c` `ch2` -> `tf3` -> **Exe** `B` `c` `ch3`

is not a ledger trace because the outgoing ledger of the **Create** action (yellow) is not the same as the incoming ledger of the non-consuming **Exercise** action for `ch1` (green). Accordingly, the subgraph without the `tf1` vertex is not multi-ledger consistent for `c` even though it is a multi-ledger causality graph.

Definition »Consistency for a multi-ledger causality graph«
Let `X` be a subset of actions in a multi-ledger causality graph `G`. Then `G` is **multi-ledger consistent** for `X` (or `X`-**multi-ledger consistent**) if `G` is multi-ledger consistent for all contracts `c` on the set of actions on `c` in `X`. `G` is **multi-ledger consistent** if `G` is multi-ledger consistent on all the actions in `G`.

<Note>
  There is no multi-ledger consistency requirement for contract keys yet. So interoperability does not provide consistency guarantees beyond those that come from the contracts they reference. In particular, contract keys need not be unique and **NoSuchKey** actions do not check that the contract key is unassigned.
</Note>

The multi-ledger causality graph for the split paint counteroffer workflow is multi-ledger consistent. In particular all maximal chains of actions on a contract are ledger traces:

| contract                | maximal chains                          |
| ----------------------- | --------------------------------------- |
| `Iou Bank A`            | **Create** -> **Fetch** -> **Exercise** |
| `ShowIou A P Bank`      | **Create** -> **Exercise**              |
| `Counteroffer A P Bank` | **Create** -> **Exercise**              |
| `Iou Bank P`            | **Create**                              |
| `PaintAgree P A`        | **Create**                              |

### Minimality and Reduction

When edges are added to an `X`-multi-ledger consistent causality graph such that it remains acyclic and transitively closed, the resulting graph is again `X`-multi-ledger consistent. The notions minimally consistent and reduction therefore generalize from ordinary causality graphs accordingly.

Definition »Minimal multi-ledger-consistent causality graph«
An `X`-multi-ledger consistent causality graph `G` is `X`-**minimal** if no strict subgraph of `G` (same vertices, fewer edges) is an `X`-multi-ledger consistent causality graph. If `X` is the set of all actions in `G`, then `X` is omitted.

Definition »Reduction of a multi-ledger consistent causality graph«
For an `X`-multi-ledger consistent causality graph `G`, there exists a unique minimal `X`-multi-ledger consistent causality graph `reduce``X``(G)` with the same vertices and the edges being a subset of `G`. `reduce``X``(G)` is called the `X`-**reduction** of `G`. As before, `X` is omitted if it contains all actions in `G`.

Since multi-ledger causality graphs are acyclic, their vertices can be sorted topologically and the resulting list is again a causality graph, where every vertex has an outgoing edge to all later vertices. If the original causality graph is `X`-consistent, then so is the topological sort, as topological sorting merely adds edges.

### From Multi-ledger Causality Graphs to Ledgers

Multi-Ledger causality graphs `G` are linked to ledgers `L` in the Daml Ledger Model via topological sort and reduction.

* Given a multi-ledger causality graph `G`, drop the incoming and outgoing ledger annotations and all transfer vertices, topologically sort the transaction vertices, and extend the resulting list of transactions with the requesters to obtain a sequence of commits `L`.
* Given a sequence of commits `L`, use the transactions as vertices and add an edge from `tx1` to `tx2` whenever `tx1`'s commit precedes `tx2`'s commit in the sequence. Then add transfer vertices and incoming and outgoing ledger annotations as needed and connect them with edges to the transaction vertices.

This link preserves consistency only to some extent. Namely, if a multi-ledger causality graph is multi-ledger consistent for a contract `c`, then the corresponding ledger is consistent for the contract `c`, too. However, a multi-ledger-consistent causality graph does not yield a consistent ledger because key consistency may be violated. Conversely, a consistent ledger does not talk about the incoming and outgoing ledger annotations and therefore cannot enforce that the annotations are consistent.

## Ledger-aware Projection

A Participant Node maintains a local ledger for each party it hosts and the Update Service outputs a topological sort of this local ledger. When the Participant Node hosts the party on several ledgers, this local ledger is an multi-ledger causality graph. This section defines the ledger-aware projection of an multi-ledger causality graph, which yields such a local ledger.

Definition »Y-labelled action«
An action with incoming and outgoing ledger annotations is **Y-labelled** for a set `Y` if its incoming or outgoing ledger annotation is an element of `Y`.

Definition »Ledger-aware projection for transactions«
Let `Y` be a set of Daml ledgers and `tx` a transaction whose actions are annotated with incoming and outgoing ledgers. Let `Act` be the set of `Y`-labelled subactions of `tx` that the party `P` is an informee of. The **ledger-aware projection** of `tx` for `P` on `Y` (`P`-**projection on** `Y`) consists of all the maximal elements of `Act` (w\.r.t. the subaction relation) in execution order.

<Note>
  Every action contains all its subactions. So if `act` is included in the `P`-projection on `Y` of `tx`, then all subactions of `act` are also part of the projection. Such a subaction `act'` may not be `Y`-labelled itself though, i.e., belong to a different ledger. If `P` is an informee of `act'`, the Participant Node will mark `act'` as merely being witnessed on `P`'s transaction stream, as explained below.
</Note>

The cross-domain transaction in the split paint counteroffer workflow, for example, has the following projections for Alice and the painter on the `Iou` ledger (yellow) and the painting ledger (green). Here, the projections on the green ledger include the actions of the yellow ledger because a projection includes the subactions.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/projecting-transactions-paint-offer-ledger-aware.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=9545c405bf28aaf0d8098af837f2e42a" className="align-center" style={{width: "60.0%"}} alt="Projections for various parties to the split paint counteroffer workflow. The green ledger projections include the yellow ledger, but the yellow ledger projections do not include the green ledger." width="660" height="1100" data-path="images/docs_website/projecting-transactions-paint-offer-ledger-aware.svg" />

Definition »Projection for transfer actions«
Let `act` be a transfer action annotated with an incoming ledger and/or an outgoing ledger. The **projection** of `act` on a set of ledgers `Y` removes the annotations from `act` that are not in `Y`. If the projection removes all annotations, it is empty.

The **projection** of `act` to a party `P` on `Y` (`P`-**projection** on `Y`) is the projection of `act` on `Y` if `P` is a stakeholder of the contract, and empty otherwise.

Definition »Multi-Ledger consistency for a party«
An multi-ledger causality graph `G` is **consistent for a party** `P` on a set of ledgers `Y` (`P`-**consistent** on `Y`) if `G` is multi-ledger consistent on the set of `Y`-labelled actions in `G` of which `P` is a stakeholder informee.

The notions of `X`-minimality and `X`-reduction extend to a party `P` on a set `Y` of ledgers accordingly.

Definition »Ledger-aware projection for multi-ledger causality graphs«
Let `G` be a multi-ledger consistent causality graph and `Y` be a set of Daml ledgers. The **projection** of `G` to party `P` on `Y` (`P`-**projection** on `Y`) is the `P`-reduction on `Y` of the following causality graph `G'`, which is `P`-consistent on \`Y\`:

* The vertices of `G'` are the vertices of `G` projected to `P` on `Y`, excluding empty projections.
* There is an edge between two vertices `v``1` and `v``2` in `G'` if there is an edge from the `G`-vertex corresponding to `v``1` to the `G`-vertex corresponding to `v``2`.

If `G` is a multi-ledger consistent causality graph, then the `P`-projection on `Y` is `P`-consistent on `Y`, too.

For example, the multi-ledger causality graph for the split paint counteroffer workflow is projected as follows:

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-causality-ledgeraware-projection.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=56332b2eb0f3b2c26fdf386b3b4fb024" className="align-center" style={{width: "100.0%"}} alt="More projections for various parties to the split paint counteroffer workflow, showing greater detail. Alice and the painter have green and yellow, just green, and just yellow projections; the bank has only a yellow projection." width="1452" height="2389" data-path="images/docs_website/counteroffer-causality-ledgeraware-projection.svg" />

The following points are worth highlighting:

* In Alice's projection on the green ledger, Alice witnesses the archival of her `Iou`. As explained in the `interop-ordering-guarantees` below, the **Exercise** action is marked as merely being witnessed in the transaction stream of a Participant Node that hosts Alice on the green ledger but not on the yellow ledger. Similarly, the Painter merely witnesses the **Create** of his `Iou` in the Painter's projection on the green ledger.
* In the Painter's projections, the `ShowIou` transaction `tx3` is unordered w\.r.t. to the `CounterOffer` acceptance in `tx4` like in the case of ordinary causality graphs. The edge `tx3` -> `tx4` is removed by the reduction step during projection.

The projection of transfer actions can be illustrated with the `interoperable-causality-graph-linear`. The `A`-projections on the yellow and green ledger look as follows. The white color indicates that a transfer action has no incoming or outgoing ledger annotation. That is, a **Leave** action is white on the right hand side and an **Enter** action is white on the left hand side.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/transfer-projection.svg?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=08e1311acdd7eadfa8f1cd145f8c6ccc" className="align-center" style={{width: "100.0%"}} alt="Causality graphs showing only the green or only the yellow ledger." width="1464" height="451" data-path="images/docs_website/transfer-projection.svg" />

## Ledger API Ordering Guarantees

The Update Service and the State Service are derived from the local ledger that the Participant Node maintains for the party. Let `Y` be the set of ledgers on which the Participant Node hosts a party. The transaction tree stream outputs a topological sort of the party's local ledger on `Y`, with the following modifications:

1. **Transfer** actions with either an incoming or an outgoing ledger annotation are output as **Enter** and **Leave** events. **Transfer** actions with both incoming and outgoing ledger annotations are omitted.
2. The incoming and outgoing ledger annotations are not output. Transaction actions with an incoming or outgoing ledger annotation that is not in `Y` are marked as merely being witnessed if the party is an informee of the action.
3. **Fetch** nodes and **NoSuchKey** are omitted.

The flat transaction stream contains precisely the `CreatedEvent`s, `ArchivedEvent`s, and the **Enter** and **Leave** actions that correspond to **Create**, consuming **Exercise**, **Enter** and **Leave** actions in transaction trees on the transaction tree stream where the party is a stakeholder of the affected contract and that are not marked as merely being witnessed.

Similarly, the State Service provides the set of contracts that are active at the returned offset according to the flat transaction stream. That is, the contract state changes of all events from the transaction event stream are taken into account in the provided set of contracts.

The ordering guarantees for single Daml ledgers extend accordingly. In particular, interoperability ensures that all local ledgers are projections of a virtual shared multi-ledger causality graph that connects to the Daml Ledger Model as described above. The ledger validity guarantees therefore extend via the local ledgers to the Ledger API.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
