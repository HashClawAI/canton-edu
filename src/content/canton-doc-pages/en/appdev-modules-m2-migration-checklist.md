---
title: "Migration Checklist"
slug: "appdev-modules-m2-migration-checklist"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-migration-checklist.md"
source_title: "Migration Checklist"
tags:
  - appdev
  - modules
  - m2-migration-checklist
---

# Migration Checklist

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Migration Checklist

> Practical checklist for Ethereum developers migrating to Canton

Use this checklist when planning and executing a migration from Ethereum to Canton. Each section covers a key area with specific action items.

## Before You Start

<AccordionGroup>
  <Accordion title="Assess your application architecture">
    * [ ] **Identify state model dependencies**: Does your app rely on global state queries?
    * [ ] **Map multi-party relationships**: Who are the parties in your contracts?
    * [ ] **Evaluate privacy requirements**: Do you need sub-transaction privacy?
    * [ ] **Review integration points**: What systems connect to your smart contracts?

    If your app heavily relies on global state queries (e.g., "show all NFTs"), you'll need to redesign this functionality using party-scoped queries or off-ledger indexing.
  </Accordion>

  <Accordion title="Understand the paradigm shift">
    | Area          | Ethereum Assumption  | Canton Reality               |
    | ------------- | -------------------- | ---------------------------- |
    | State         | Global, queryable    | Distributed, party-scoped    |
    | Contracts     | Mutable              | Immutable (archive + create) |
    | Authorization | Runtime `msg.sender` | Compile-time signatories     |
    | Privacy       | Public by default    | Private by default           |
    | Identity      | Anonymous addresses  | Named parties                |
  </Accordion>

  <Accordion title="Set up your development environment">
    * [ ] Install the [Daml SDK](/sdks-tools/sdks/daml-sdk)
    * [ ] Install VS Code with the [Daml extension](https://marketplace.visualstudio.com/items?itemName=DigitalAssetHoldingsLLC.daml)
    * [ ] Clone the [CN Quickstart](/sdks-tools/reference-projects/cn-quickstart)
    * [ ] Run `make setup && make build && make start` to verify your setup works
  </Accordion>
</AccordionGroup>

## Smart Contract Migration

### Phase 1: Model Your Parties

<Steps>
  <Step title="Identify all actors">
    List everyone who interacts with your contracts and map them to Canton parties:

    * **Contract owner** → `admin : Party` (signatory for admin contracts)
    * **Users** → `user : Party` (each user is a distinct party)
    * **Operators** → `operator : Party` (may be signatory or controller)
  </Step>

  <Step title="Define party relationships">
    For each contract, determine:

    * **Who must agree to create it?** → Signatories
    * **Who should see it?** → Observers
    * **Who can act on it?** → Controllers (per choice)
  </Step>

  <Step title="Plan party hosting">
    Decide where parties will be hosted:

    * **User parties**: Often on the application provider's validator
    * **Admin parties**: On your organization's validator
    * **External parties**: On their own validators
  </Step>
</Steps>

### Phase 2: Translate Contracts

<AccordionGroup>
  <Accordion title="Translate Solidity structs to Daml data types">
    ```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Solidity
    struct Asset {
        address owner;
        uint256 value;
        bool locked;
    }
    ```

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    -- Daml
    data Asset = Asset with
      owner : Party
      value : Decimal
      locked : Bool
      deriving (Eq, Show)
    ```
  </Accordion>

  <Accordion title="Translate storage mappings to contracts">
    ```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Solidity: Global mapping
    mapping(address => uint256) public balances;
    ```

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    -- Daml: Individual contracts per holding
    template TokenHolding
      with
        owner : Party
        issuer : Party
        amount : Decimal
      where
        signatory issuer
        observer owner
    ```

    The key insight: Instead of one contract with a mapping, you have many contracts—one per holding.
  </Accordion>

  <Accordion title="Translate functions to choices">
    ```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Solidity
    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount);
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }
    ```

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    -- Daml
    choice Transfer : ContractId TokenHolding
      with
        newOwner : Party
      controller owner
      do
        create this with owner = newOwner
    ```
  </Accordion>

  <Accordion title="Translate access control to signatories/controllers">
    ```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Solidity
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    ```

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    -- Daml: No modifier needed
    choice AdminAction : ()
      controller admin  -- Only admin can exercise
      do
        -- Protocol enforces this
        pure ()
    ```
  </Accordion>
</AccordionGroup>

### Phase 3: Handle State Differently

* [ ] **Replace global queries**: Design party-scoped query patterns
* [ ] **Plan for contract keys**: Use keys for lookups instead of addresses
* [ ] **Accept contract ID changes**: IDs change on every update; use keys for stable references

<Warning>
  Canton has no equivalent to Ethereum's `eth_getLogs` or event filtering across all contracts. Plan your indexing strategy early.
</Warning>

## Integration Migration

### API Changes

| Ethereum            | Canton                                                        | Notes                             |
| ------------------- | ------------------------------------------------------------- | --------------------------------- |
| JSON-RPC            | Ledger API (gRPC or JSON API)                                 | Different protocol                |
| Web3.js / ethers.js | Ledger API client or [dApp SDK](/appdev/modules/m4-sdks-apis) | Language-specific clients         |
| Event logs          | Transaction streams                                           | Subscribe to party's transactions |
| `eth_call`          | Exercise non-consuming choice                                 | Read-only operations              |

### Authentication Changes

Ethereum authenticates via private key signatures and derives identity from `msg.sender`. In Canton, identity comes from party authentication with JWT tokens. Where Ethereum allows anyone to call a public function, Canton restricts access to authenticated parties only.

### Indexing Strategy

Since there's no global state query:

* [ ] **Use the Participant Query Store (PQS)** for SQL-based querying
* [ ] **Stream transactions** to your own database
* [ ] **Design contracts with query-friendly keys**

## Testing Migration

### Unit Tests

* [ ] Replace Hardhat/Foundry tests with Daml Script tests
* [ ] Test authorization rules (who can exercise what)
* [ ] Test multi-party workflows (propose-accept patterns)

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Daml Script test
testTransfer = script do
  alice <- allocateParty "Alice"
  bob <- allocateParty "Bob"

  -- Alice creates a token
  tokenId <- submit alice do
    createCmd Token with owner = alice, issuer = alice, amount = 100.0

  -- Alice transfers to Bob
  newTokenId <- submit alice do
    exerciseCmd tokenId Transfer with newOwner = bob

  -- Verify Bob owns it
  Some token <- queryContractId bob newTokenId
  assert (token.owner == bob)
```

### Integration Tests

* [ ] Test against LocalNet (CN Quickstart provides this)
* [ ] Verify API integration works
* [ ] Test error scenarios and rollback behavior

## Deployment Migration

### Network Selection

* **LocalNet** — development and testing
* **DevNet** — integration testing
* **TestNet** — pre-production validation
* **MainNet** — production

### Deployment Checklist

* [ ] **Package your Daml code**: `dpm build`
* [ ] **Upload to validator**: Via admin or LAPI APIs
* [ ] **Allocate parties**: Create party identities
* [ ] **Initialize contracts**: Create initial state
* [ ] **Configure applications**: Point to Ledger API

## Operational Changes

### Monitoring

Where Ethereum has block explorers, Canton uses validator logs and metrics. Transaction hash lookups become transaction ID queries. Gas tracking maps to traffic unit tracking.

### Key Management

Ethereum EOA private keys correspond to Canton party keys, which can live on the validator or be held externally. Hardware wallets map to HSM and KMS integrations. Multisig wallets are replaced by multi-signatory contracts, where authorization is enforced at the Daml level.

## Common Migration Pitfalls

<Warning>
  Avoid these common mistakes when migrating from Ethereum.
</Warning>

| Pitfall                         | Why It Happens                         | How to Avoid                                    |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| **Building global state views** | Expecting Ethereum-like queries        | Design for party-scoped data from start         |
| **Overusing parties**           | Treating parties like addresses        | Parties have hosting costs; design deliberately |
| **Ignoring propose-accept**     | Expecting unilateral contract creation | Multi-party contracts need workflow             |
| **Expecting event logs**        | Using Ethereum event patterns          | Use transaction streams and indexing            |
| **Contract ID as identifier**   | Treating IDs like addresses            | Use contract keys for stable references         |

## Migration Phases

| Phase              | Focus                     | Completion Criteria                |
| ------------------ | ------------------------- | ---------------------------------- |
| **1. Learning**    | Understand Canton model   | Team comfortable with Daml basics  |
| **2. Design**      | Redesign for Canton       | Party model and contracts designed |
| **3. Development** | Implement in Daml         | Contracts and tests complete       |
| **4. Integration** | Connect applications      | APIs working on LocalNet           |
| **5. Testing**     | Validate on test networks | Passed DevNet/TestNet testing      |
| **6. Deployment**  | Go to production          | Running on MainNet                 |

## Next Steps

<CardGroup cols={2}>
  <Card title="Module 3: Daml Development" icon="code" href="/appdev/modules/m3-dev-environment">
    Start building with Daml.
  </Card>

  <Card title="CN Quickstart" icon="rocket" href="/sdks-tools/reference-projects/cn-quickstart">
    Get hands-on with a working example.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
