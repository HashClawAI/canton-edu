---
title: "Canton Name Service"
slug: "overview-reference-canton-name-service"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/canton-name-service.md"
source_title: "Canton Name Service"
tags:
  - overview
  - reference
  - canton-name-service
---

# Canton Name Service

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Name Service

> Human-readable names mapped to party identifiers on Canton Network

The Canton Name Service (CNS) maps human-readable names to party identifiers on Canton Network. It serves a similar function to DNS on the internet: instead of sharing a long, opaque party ID like `auth0_007c675a429eaf831f0991308d85::12201abe669f...`, you can share a name like `alice.unverified.cns`.

CNS is implemented as a set of Daml contracts on the Global Synchronizer, governed by the DSO party. The underlying code is called the Amulet Name Service (ANS) in the [Splice](https://github.com/canton-network/splice) codebase.

## Name Format

CNS entry names follow the pattern `<chosen-name>.unverified.cns`. The suffix `.unverified.cns` is appended to all user-registered names. The `unverified` label indicates that no identity verification has been performed on the registrant -- anyone with a wallet and sufficient Canton Coin can register a name.

The DSO itself holds a special entry, `dso.cns`, which has no expiration and no contract ID (it is provided directly by the DSO rather than through the standard registration flow).

## How Registration Works

Registering a CNS entry is a multi-step process built on the Daml subscription payment model:

1. The user calls the **POST** `/v0/entry/create` endpoint on the Validator App's ANS API, providing a `name`, `url`, and `description`.
2. The Validator App exercises the `AnsRules_RequestEntry` choice, which creates an `AnsEntryContext` contract and a `SubscriptionRequest` contract.
3. The user accepts the subscription request through their wallet, which triggers an initial payment in Canton Coin.
4. The DSO automation collects the initial payment (`AnsEntryContext_CollectInitialEntryPayment`), burns the Canton Coin transferred to the DSO, and creates the `AnsEntry` contract.

The entry fee and lifetime are configured in the `AnsRulesConfig` on the `AnsRules` contract. The payment goes to the DSO party and is burned -- it is not redistributed.

## Renewal

CNS entries expire. Each entry has an `expiresAt` timestamp, and the owner must renew before that time to keep the name.

Renewal uses the same subscription payment mechanism. When a renewal payment comes due, the wallet automation can process it automatically if the user has sufficient Canton Coin and has enabled auto-renewal. The DSO automation then exercises `AnsEntryContext_CollectEntryRenewalPayment`, which burns the payment and extends `expiresAt` by the configured `entryLifetime` interval.

If an entry is not renewed before expiration, any signatory can archive it by exercising `AnsEntry_Expire`.

## Name Resolution

CNS supports resolution in both directions -- name to party, and party to name (similar to forward and reverse DNS).

The Scan API provides three public endpoints for lookups:

* **GET** `/v0/ans-entries/by-name/{name}` -- resolves an exact name to its entry, including the owning party ID
* **GET** `/v0/ans-entries/by-party/{party}` -- resolves a party ID to its CNS entry
* **GET** `/v0/ans-entries?name_prefix=<prefix>&page_size=<n>` -- searches entries by name prefix

Applications such as the wallet use these endpoints to display human-readable names instead of raw party identifiers. For example, when sending Canton Coin to another user, you can type `alice.unverified.cns` instead of the full party ID.

These same endpoints are available through the Validator App's Scan Proxy API (under `/v0/scan-proxy/ans-entries/*`), which provides BFT verification by querying multiple Super Validator nodes and returning the consensus result.

## Storage on the Global Synchronizer

CNS state lives entirely on the Global Synchronizer as Daml contracts in the `splice-amulet-name-service` package. The key contract types are:

* **`AnsRules`** -- singleton contract holding the configuration (entry fee, lifetime, renewal duration). Signed by the DSO party.
* **`AnsEntryContext`** -- tracks the relationship between a CNS entry and its subscription. Signed by both the DSO and the entry owner.
* **`AnsEntry`** -- the actual name record, containing the name, owner party, URL, description, and expiration time. Signed by both the DSO and the entry owner.

Because these contracts follow standard Daml authorization rules, the entry owner and the DSO must both consent to creation, renewal, and expiration.

## API Reference

CNS functionality is split across two APIs exposed by the Validator App:

**ANS API** (entry management) -- see the [ans-external.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/validator/src/main/openapi/ans-external.yaml) OpenAPI spec:

* **POST** `/v0/entry/create` -- request creation of a new entry
* **GET** `/v0/entry/all` -- list all entries owned by the authenticated user

**Scan API** (name resolution) -- see the [scan.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/scan/src/main/openapi/scan.yaml) OpenAPI spec:

* **GET** `/v0/ans-entries` -- list entries by name prefix
* **GET** `/v0/ans-entries/by-name/{name}` -- look up an entry by exact name
* **GET** `/v0/ans-entries/by-party/{party}` -- look up an entry by party ID
* **POST** `/v0/ans-rules` -- retrieve the current ANS rules configuration

The ANS API requires JWT authentication where the token subject matches the user requesting or listing entries. The Scan API endpoints are public.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
