---
title: "Canton Improvement Proposals (CIPs)"
slug: "overview-understand-cips-introduction"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/cips-introduction.md"
source_title: "Canton Improvement Proposals (CIPs)"
tags:
  - overview
  - understand
  - cips-introduction
---

# Canton Improvement Proposals (CIPs)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Improvement Proposals (CIPs)

> Introduction to the CIP process for Canton Network standards and governance

Canton Improvement Proposals (CIPs) are the formal mechanism for proposing changes, standards, and improvements to Canton Network.

## What are CIPs?

CIPs are design documents providing information to the Canton community, describing new features, processes, or standards for Canton Network.

| CIP Type            | Purpose                                |
| ------------------- | -------------------------------------- |
| **Standards Track** | Technical specifications and standards |
| **Process**         | Governance and operational procedures  |
| **Informational**   | General guidelines and information     |

## Why CIPs Matter

CIPs ensure that:

* Changes are discussed openly before implementation
* Standards enable interoperability
* The community has input on network evolution
* Decisions are voted on and then documented for reference

## Key CIPs

### CIP-0056: Canton Network Token Standard

The token standard defines interfaces for fungible tokens on Canton Network.

| Aspect               | Specification                |
| -------------------- | ---------------------------- |
| **Purpose**          | Standardize token operations |
| **Interfaces**       | Holding, Transfer, Lock      |
| **Interoperability** | Wallet and app compatibility |

**GitHub:** [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)

Key features:

* Standard holding representation
* Consistent transfer semantics
* Pre-approval support for advanced workflows
* Allocation patterns for multi-step transfers

## CIP Process

### Lifecycle

| Stage        | Description                     |
| ------------ | ------------------------------- |
| **Draft**    | Initial proposal for discussion |
| **Review**   | Community review and feedback   |
| **Accepted** | Approved for implementation     |
| **Final**    | Implemented and stable          |
| **Rejected** | Not accepted (with rationale)   |

### Who Can Propose

CIPs can be proposed by:

* Super Validators
* Community members
* Development teams
* Ecosystem participants

## Implementing CIPs

### For Application Developers

When building applications, consider relevant CIPs:

| Situation              | Action                        |
| ---------------------- | ----------------------------- |
| **Creating tokens**    | Implement CIP-0056 interfaces |
| **Wallet integration** | Support standard interfaces   |
| **Interoperability**   | Follow published standards    |

### Example: Token Standard Implementation

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Implement CIP-0056 holding interface
template MyToken
  with
    issuer : Party
    holder : Party
    amount : Decimal
  where
    signatory issuer
    observer holder

    -- Standard interface implementation
    interface instance Holding.I for MyToken where
      view = Holding.View with ...
```

## Finding CIPs

| Resource                                                                    | Content                |
| --------------------------------------------------------------------------- | ---------------------- |
| [GitHub Repository](https://github.com/global-synchronizer-foundation/cips) | All CIP documents      |
| [canton.foundation](https://canton.foundation)                              | Governance information |
| Community channels                                                          | Discussion and updates |

## Contributing to CIPs

To propose or contribute to CIPs:

1. **Review existing CIPs** to understand the format
2. **Discuss informally** in community channels
3. **Write a draft** following the CIP template
4. **Submit for review** via the appropriate process
5. **Iterate** based on feedback

## Next Steps

<CardGroup cols={2}>
  <Card title="Token Standard" icon="coins" href="https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md">
    Implement the Canton Token Standard.
  </Card>

  <Card title="CIP Repository" icon="github" href="https://github.com/global-synchronizer-foundation/cips">
    Browse all CIPs on GitHub.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
