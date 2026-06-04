---
title: "Development Environment Setup"
slug: "appdev-modules-m3-dev-environment"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-dev-environment.md"
source_title: "Development Environment Setup"
tags:
  - appdev
  - modules
  - m3-dev-environment
---

# Development Environment Setup

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Development Environment Setup

> Set up your development environment for writing Daml smart contracts

## Introduction

Daml is a smart contract language designed to build composable applications on Canton ledgers.

In this module, you will learn about the structure of a Daml ledger and how to write Daml applications that run on the Canton Network by building an asset-holding and trading application. You will gain an overview of the most important language features and how to use Daml's developer tools to write, test, compile, package and ship your application.

## Prerequisites

* You have installed [dpm](https://docs.canton.network/sdks-tools/cli-tools/dpm)

## Loading Example Code

Each section in this module presents a new self-contained application with more functionality than the previous section. You can load the code for each section using `dpm`. For example:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Load the contract templates example
dpm new intro-contracts --template daml-intro-contracts

# Load the choices example
dpm new intro-choices --template daml-intro-choices
```

## Next Steps

Continue to [Contract Templates](/docs/canton/appdev-modules-m3-contract-templates) to start building Daml smart contracts.

If you're new to functional programming or want a refresher on Daml's syntax (types, pattern matching, records, type classes), see [Language Fundamentals](/docs/canton/appdev-modules-m3-language-fundamentals) first. If you have experience with Haskell or other ML-family languages, you can skip it and refer back as needed.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
