---
title: "Smart Contract Paradigm Shift"
slug: "appdev-modules-m2-smart-contract-paradigm"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-smart-contract-paradigm.md"
source_title: "Smart Contract Paradigm Shift"
tags:
  - appdev
  - modules
  - m2-smart-contract-paradigm
---

# Smart Contract Paradigm Shift

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Smart Contract Paradigm Shift

> Understanding the fundamental differences between Solidity and Daml programming models

Moving from Solidity to Daml requires a significant mental shift. This page explains the paradigm differences and how to adapt your thinking.

## Programming Model Comparison

| Aspect           | Solidity                    | Daml                    |
| ---------------- | --------------------------- | ----------------------- |
| **Paradigm**     | Imperative, object-oriented | Functional, declarative |
| **State**        | Mutable storage             | Immutable contracts     |
| **Execution**    | Sequential operations       | Transaction trees       |
| **Types**        | Static with dynamic calls   | Strongly typed, ADTs    |
| **Side effects** | Unlimited                   | Controlled via monads   |

## State Model: Mutable vs. Immutable

### Solidity: Mutable State

In Solidity, contracts have mutable storage that you modify directly:

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
contract Token {
    mapping(address => uint256) public balances;

    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Mutate state in place
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }
}
```

**Mental model:** The contract is a persistent object with state you modify.

### Daml: Immutable Contracts

In Daml, contracts are immutable data. State changes create new contracts or archive existing contracts:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Token
  with
    owner : Party
    issuer : Party
    amount : Decimal
  where
    signatory issuer
    observer owner

    choice Transfer : ContractId Token
      with
        newOwner : Party
        transferAmount : Decimal
      controller owner
      do
        -- This contract will be archived
        -- Create new contracts for the split
        create Token with owner = newOwner, issuer, amount = transferAmount
        create this with amount = amount - transferAmount
```

**Mental model:** Contracts are facts. Exercise archives the fact and creates new facts.

## UTXO vs. Account Model

### Ethereum: Account Model

* State is a global mapping of accounts to balances
* Transfers modify account entries
* Easy to query total balance
* Contention on popular accounts

### Canton: Extended UTXO Model

* State is a set of contracts (like unspent outputs)
* Transfers archive existing contracts, create new ones
* Balance is sum of owned contracts
* Better parallelism, explicit data flow

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Canton: Holdings are individual contracts
-- Alice's total balance = sum of all Token contracts where owner = Alice

-- Query: Find all my tokens
myTokens <- queryContractKey @Token myParty
totalBalance <- pure $ sum [amount | Token{amount} <- myTokens]
```

## Language Comparison

### Type System

| Feature           | Solidity           | Daml                         |
| ----------------- | ------------------ | ---------------------------- |
| **Type safety**   | Moderate           | Strong                       |
| **Null handling** | Implicit (0/empty) | Explicit (Optional)          |
| **Custom types**  | Structs, enums     | ADTs, records                |
| **Generics**      | Limited            | Full parametric polymorphism |

### Solidity Types

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
struct Asset {
    address owner;
    uint256 value;
    bool isLocked;
}

enum State { Pending, Active, Completed }
```

### Daml Types

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Record type (like struct)
data Asset = Asset with
  owner : Party
  value : Decimal
  isLocked : Bool

-- Sum type (algebraic data type)
data AssetState
  = Pending
  | Active with activatedAt : Time
  | Completed with result : Text

-- Optional (explicit null handling)
data MaybeApprover = Some Party | None
```

### Solidity Control Flow

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
function process(uint256[] memory items) public {
    for (uint i = 0; i < items.length; i++) {
        if (items[i] > threshold) {
            revert("Over threshold");
        }
        results[i] = items[i] * 2;
    }
}
```

### Daml Control Flow

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
process : [Decimal] -> Update [Decimal]
process items = do
  forA items \item -> do
    assertMsg "Over threshold" (item <= threshold)
    pure (item * 2.0)
```

## Authorization Model

### Solidity: Runtime Authorization

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
contract Ownable {
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    function sensitiveAction() public onlyOwner {
        // Only owner can call
    }
}
```

**Issues:**

* Authorization checked at runtime
* Easy to forget checks
* Anyone can attempt the call
* Authorization mixed with logic

### Daml: Declarative Authorization

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template OwnedAsset
  with
    owner : Party
    data : Text
  where
    signatory owner  -- owner must authorize creation

    choice SensitiveAction : ()
      controller owner  -- only owner can exercise
      do
        -- Protocol enforces: only owner can reach here
        pure ()
```

**Benefits:**

* Authorization declared, not coded
* Impossible to forget (compiler enforces)
* Only authorized parties can attempt
* Clear separation of concerns

## Multi-Party Coordination

### Solidity: Manual Multi-Sig

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
contract MultiSig {
    mapping(address => bool) public approved;
    uint256 public approvalCount;
    uint256 public requiredApprovals;

    function approve() public {
        require(!approved[msg.sender], "Already approved");
        approved[msg.sender] = true;
        approvalCount++;
    }

    function execute() public {
        require(approvalCount >= requiredApprovals, "Not enough approvals");
        // Execute action
    }
}
```

### Daml: Native Multi-Party

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Agreement
  with
    partyA : Party
    partyB : Party
    terms : Text
  where
    signatory partyA, partyB  -- Both must sign to create

-- Proposal pattern for gathering signatures
template AgreementProposal
  with
    proposer : Party
    counterparty : Party
    terms : Text
  where
    signatory proposer
    observer counterparty

    choice Accept : ContractId Agreement
      controller counterparty
      do create Agreement with
           partyA = proposer
           partyB = counterparty
           terms
```

## Common Patterns Translated

| Solidity Pattern      | Daml Equivalent                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Ownable**           | Signatory declaration                                                                                              |
| **Pausable**          | Contract archival + recreation                                                                                     |
| **ERC-20**            | Token Standard ([CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)) |
| **Proxy/Upgradeable** | Smart Contract Upgrade (SCU)                                                                                       |
| **Pull payment**      | Propose/accept pattern                                                                                             |
| **Factory**           | Template + create                                                                                                  |
| **Registry**          | Contract keys (when available)                                                                                     |

## What to Unlearn

| Solidity Habit                   | Daml Reality                                         |
| -------------------------------- | ---------------------------------------------------- |
| Mutate state in place            | Archive + create new contracts                       |
| Runtime `msg.sender` checks      | Compile-time controller declarations                 |
| Public functions anyone can call | Only controllers can exercise                        |
| Global contract address          | Contract IDs change on every update                  |
| Loops for iteration              | Use `forA`, `mapA`, fold patterns                    |
| Try/catch everywhere             | Assertions for validation; exceptions are deprecated |

## Next Steps

<CardGroup cols={2}>
  <Card title="Network Architecture" icon="network-wired" href="/appdev/modules/m2-network-architecture">
    Compare network architecture and topology.
  </Card>

  <Card title="Module 3: Daml" icon="code" href="/appdev/modules/m3-dev-environment">
    Start writing Daml smart contracts.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
