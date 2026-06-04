---
title: "Use Cases"
slug: "overview-understand-use-cases"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/use-cases.md"
source_title: "Use Cases"
tags:
  - overview
  - understand
  - use-cases
---

# Use Cases

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Cases

> Real-world applications where Canton's privacy model enables solutions not feasible on traditional blockchains

Canton's architecture enables use cases that are not feasible on public blockchains. This page explores key patterns and concrete examples.

## Delivery vs. Payment (DvP)

The canonical example of Canton's capabilities is atomic delivery vs. payment across different assets and parties.

### The Scenario

Alice wants to buy a tokenized asset from Bob, paying with a tokenized cash instrument settled on a private payment synchronizer. The settlement should be:

* **Atomic**: Either both legs complete, or neither does
* **Private**: Observers shouldn't see the counterparties or the price

### On Traditional Blockchains

This is problematic:

* If done in two transactions: risk of one completing without the other
* If done atomically: all parties (and observers) see all legs of the trade
* Anyone watching can see the price and terms

### On Canton

The entire exchange happens in a single atomic transaction with sub-transaction privacy:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph TX[Atomic DvP Transaction]
        direction LR
        L1[Leg 1: Alice → Bob<br>Cash payment]
        L2[Leg 2: Bob → Alice<br>Asset delivery]
    end

    subgraph Views[What Each Party Sees]
        VA["Alice's View<br>- Paid Bob<br>- Received asset"]
        VB["Bob's View<br>- Received cash from Alice<br>- Transferred asset"]
    end

    TX --> Views
```

| Party           | Sees                         | Doesn't See                 |
| --------------- | ---------------------------- | --------------------------- |
| **Alice**       | Both legs (she is the buyer) | N/A                         |
| **Bob**         | Both legs (he is the seller) | N/A                         |
| **Third party** | Nothing                      | Everything about this trade |

<Note>
  This example assumes the cash and asset legs both settle on synchronizers where the trade participants are the only stakeholders — for instance, a private payment synchronizer for the cash leg and a private securities synchronizer for the asset leg. Trades that involve assets settled on the Global Synchronizer behave differently: Canton Coin transfers, topology transactions, and network governance transactions are visible to the Super Validators that operate the Global Synchronizer, so they are not private in the same sense. Private synchronizers preserve the full sub-transaction privacy model.
</Note>

### Why This Matters

* **Regulatory compliance**: Each party sees only their entitled information
* **Atomic settlement**: No settlement risk — both legs or neither
* **Privacy**: Trading relationships and prices protected
* **Audit trail**: Entitled auditors can be added as observers

## Tokenized Securities

Issue and trade securities with regulatory compliance built in.

### Requirements

* Issuer controls who can hold the security
* Regulator has audit visibility
* Trades are private between buyer and seller
* Corporate actions affect all holders (but holdings remain private)

### Canton Design

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Security
  with
    issuer : Party
    holder : Party
    regulator : Party
    cusip : Text
    quantity : Decimal
    approvedHolders : [Party]  -- Issuer maintains list of eligible holders
  where
    signatory issuer
    observer holder, regulator  -- Regulator sees all holdings

    choice Transfer : ContractId Security
      with
        newHolder : Party
      controller holder, issuer  -- Issuer approval required for compliance
      do
        assert (newHolder `elem` approvedHolders)
        create this with holder = newHolder
```

The regulator observes all holdings (for compliance) without that data being public. The issuer must approve all transfers, ensuring only eligible parties can hold the security. Trades remain private between counterparties while still being auditable.

## Cross-Border Payments

Move value across jurisdictions while respecting data sovereignty requirements.

### The Challenge

* Sender's bank is in Country A with data localization requirements
* Receiver's bank is in Country B with different requirements
* Correspondent banking requires coordination
* Neither country's regulator should see the other's customer data

### Canton Solution

Each jurisdiction's data stays with validators in that jurisdiction:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph CountryA[Country A]
        SenderBank[Sender's Bank<br>Validator A]
        RegA[Regulator A<br>Observer]
    end

    subgraph CountryB[Country B]
        ReceiverBank[Receiver's Bank<br>Validator B]
        RegB[Regulator B<br>Observer]
    end

    SenderBank <--> |atomic settlement<br>via synchronizer| ReceiverBank

    RegA --> |sees sender details| SenderBank
    RegB --> |sees receiver details| ReceiverBank
```

* Sender's details stay in Country A
* Receiver's details stay in Country B
* Settlement is atomic across the synchronizer
* Each regulator sees only their jurisdiction's data

## Syndicated Loan Management

Multiple banks participate in a loan without seeing each other's positions or terms.

### The Scenario

In syndicated loans:

* Multiple banks hold portions of the same loan
* Each bank's position is confidential
* The agent bank coordinates payments
* Borrower interacts with the group as a whole

On public systems, all participants would see all positions, defeating confidentiality.

### Canton Solution

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Loan[Syndicated Loan Structure]
        Agent[Agent Bank<br>Coordinates]
        B1[Bank A<br>$100M position]
        B2[Bank B<br>$75M position]
        B3[Bank C<br>$50M position]
        Borrower[Borrower]
    end

    Borrower --> Agent
    Agent --> B1
    Agent --> B2
    Agent --> B3

    Note1[Bank A sees: own position, agent coordination<br>Bank A doesn't see: Bank B or C positions]
```

Each bank sees:

* Their own position and terms
* Payments flowing to/from them
* Agent coordination for their portion

Each bank doesn't see:

* Other banks' positions
* Other banks' terms
* Total syndicate size (unless explicitly shared)

## Supply Chain Finance

Track goods and payments across multiple parties without exposing commercial relationships.

### The Scenario

A manufacturer ships to a distributor, who ships to a retailer. Financing is provided at each step.

### Privacy Requirements

* Manufacturer shouldn't see retailer's purchase price
* Retailer shouldn't see manufacturing cost
* Each financier sees only their debtor's portion
* Logistics providers see shipping info, not financial terms

### Canton Approach

Canton's privacy works at the contract level—observers see entire contracts, not individual fields. To give different parties access to different information, you design separate contracts for each audience:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Shipping details: visible to logistics provider
template ShipmentTracking
  with
    shipper : Party
    receiver : Party
    logisticsProvider : Party
    goods : GoodsDescription
    trackingId : Text
  where
    signatory shipper, receiver
    observer logisticsProvider
    -- Logistics provider sees goods and routing, not financial terms

-- Financing terms: visible to financier
template ShipmentFinancing
  with
    shipper : Party
    receiver : Party
    financier : Party
    terms : FinancingTerms
    shipmentRef : Text  -- Reference to link related contracts
  where
    signatory shipper, receiver
    observer financier
    -- Financier sees payment terms, not goods details or other legs' pricing
```

A single atomic transaction can create both contracts. The logistics provider and financier each see only their relevant contract, while the shipper and receiver (as signatories on both) see everything. Downstream participants in the supply chain never see upstream pricing, because those contracts have different stakeholders.

This pattern—separating data by audience into distinct contracts—is how Canton achieves fine-grained privacy while maintaining atomicity.

## When Canton Fits

Canton is ideal when you need:

| Requirement                  | Canton Provides                                          |
| ---------------------------- | -------------------------------------------------------- |
| **Multi-party coordination** | Native multi-party contracts with explicit authorization |
| **Confidential execution**   | Sub-transaction privacy by design                        |
| **Regulatory compliance**    | Selective disclosure to authorized parties               |
| **Atomic settlement**        | All-or-nothing execution across parties                  |
| **Audit trails**             | Observer roles for entitled auditors                     |

## When Canton May Not Fit

Consider alternatives if you need:

| Requirement                   | Consideration                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Fully public applications** | Transparency is a feature, not a limitation (e.g., public governance, open auctions) |
| **EVM compatibility**         | Canton does not natively interoperate with Ethereum smart contracts                  |
| **Anonymous participation**   | Canton parties have identity; truly anonymous systems need different approaches      |
| **Simple single-party apps**  | Blockchain overhead may not be justified                                             |

## Next Steps

<CardGroup cols={2}>
  <Card title="Core Concepts" icon="book" href="/overview/understand/core-concepts">
    Understand parties, validators, and synchronizers.
  </Card>

  <Card title="Start Building" icon="code" href="/appdev/get-started/choose-your-path">
    Begin your development journey.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
