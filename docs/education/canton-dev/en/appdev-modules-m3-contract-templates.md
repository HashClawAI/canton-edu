---
title: "Contract Templates"
slug: "appdev-modules-m3-contract-templates"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-contract-templates.md"
source_title: "Contract Templates"
tags:
  - appdev
  - modules
  - m3-contract-templates
---

# Contract Templates

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Contract Templates

> Learn how to define Daml contract templates - the core building blocks of Canton smart contracts

## Introduction

To begin with, you're going to write a very small Daml template, which represents a self-issued, non-transferable token. Because it's a minimal template, it isn't actually useful on its own - you'll make it more useful later - but it's enough that it can show you the most basic concepts:

* Transactions
* Daml modules and files
* Templates
* Contracts
* Signatories

<Tip>
  You can load the code for this section by running `dpm new intro-contracts --template daml-intro-contracts`
</Tip>

## Daml ledger basics

Like most structures called ledgers, a Daml Ledger is just a list of *commits*. When we say *commit*, we mean the final result of when a *party* successfully *submits* a *transaction* to the ledger.

*Transaction* is a concept we'll cover in more detail through this introduction. The most basic examples are the creation and archival of a *contract*.

A contract is *active* from the point where there is a committed transaction that creates it, up to the point where there is a committed transaction that *archives* it.

Individual contracts are *immutable* in the sense that an active contract can not be changed. You can only change the *active contract set* by creating a new contract, or archiving an old one.

Daml specifies what transactions are legal on a Daml Ledger. The rules the Daml code specifies are collectively called a *Daml model* or *contract model*.

## Daml modules and files

Each `.daml` file defines a *Daml Module* at the top:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Token where
```

Code comments in Daml are introduced with `--`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- A Daml file defines a module.
module Token where
```

## Templates

A `template` defines a type of contract that can be created, and who has the right to do so. *Contracts* are instances of *templates*.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Token
  with
    owner : Party
  where
    signatory owner
```

You declare a template starting with the `template` keyword, which takes a name as an argument.

Daml is whitespace-aware and uses layout to structure *blocks*. Everything that's below the first line is indented, and thus part of the template's body.

*Contracts* contain data, referred to as the *create arguments* or simply *arguments*. The `with` block defines the data type of the create arguments by listing field names and their types. The single colon `:` means "of type", so you can read this as "template `Token` with a field `owner` of type `Party`".

`Token` contracts have a single field `owner` of type `Party`. The fields declared in a template's `with` block are in scope in the rest of the template body, which is contained in a `where` block.

## Signatories

The `signatory` keyword specifies the *signatories* of a contract. These are the parties whose *authority* is required to create the contract or archive it -- just like a real contract. Every contract must have at least one signatory.

Furthermore, Daml ledgers *guarantee* that parties see all transactions where their authority is used. This means that signatories of a contract are guaranteed to see the creation and archival of that contract.

## Next up

In [Choices](/docs/canton/appdev-modules-m3-choices), you'll learn how to add behavior to your contracts using choices.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
