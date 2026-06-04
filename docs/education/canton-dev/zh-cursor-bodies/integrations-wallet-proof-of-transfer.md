> Enable end-用户 to independently verify privacy-enabled asset transfers on the Canton Network.

# Proof of 转账

## 概览

Privacy-enabled assets on the Canton Network, such as DA registry assets, require a specialized mechanism for 用户 to verify 交易 outcomes while preserving the privacy of the involved Party. 用户 need a way to independently and indisputably verify that an asset transfer was successful, obtaining a reliable, 网络-verified confirmation that is independent of any single platform's internal reporting.

To enable this transfer proofing capability, wallets must make the **转账 Object** payload and **UpdateID** extractable, allowing end-用户 to easily locate and copy this data directly from their 交易 history to use in proofing 服务 or 网络 explorers.

本指南 provides the technical specifications for locating and extracting the 转账 Object from the ledger via the JSON API.

## Exposing the 转账 Object and UpdateID

### Technical Guidelines: What Constitutes the 转账 Object?

The **UpdateID** is the unique identifier for a 交易 on the ledger. With it, you can fetch the Created, Exercised, and Archived 事件 for that specific 交易. **NOTE: The wallets needs to ensure that they display the most recent updated for a given transfer. 例如, in the case of a 2 step transfer, 钱包 提供方 will need to explicitly refresh the updateID, after the 交易 has been accepted, so that they display the transfer, not just the offer.**

The underlying schema defining the 转账 Object can be referenced in the DAML model here: [`Splice/Api/Token/TransferInstructionV1.daml`](https://github.com/hyperledger-labs/splice/blob/0.5.14/token-standard/splice-api-token-transfer-instruction-v1/daml/Splice/Api/Token/TransferInstructionV1.daml#L13)

The 转账 Object can also be serialized into JSON format, as shown in the following example:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "sender": "issuer::122...",
    "receiver": "holder::122...",
    "amount": "2.0000000000",
    "instrumentId": { "admin": "...", "id": "INST" },
    "requestedAt": "2026-03-01T13:58:32.626Z",
    "executeBefore": "2026-03-04T13:58:27.335Z",
    "inputHoldingCids": ["005152f0eae9..."],
    "meta": {
        "values": {
            "splice.lfdecentralizedtrust.org/reason": ""
        }
    }
}
```

**Fetching the Data via JSON API**

While gRPC can be used, this guide assumes 集成 via the [DAML JSON API](/sdks-tools/api-reference/json-api).

To fetch update info from the 参与者 node, query the following 端点 using the 交易's `UpdateID`: `GET /v2/updates/update-by-id`

### Locating the 转账 Object (By 交易 State)

Depending on the lifecycle stage of the 交易, the 转账 Object is located in different 事件 arguments. 你将 need to parse the 事件 returned from the 端点 above based on these three scenarios:

**Scenario A: The 转账 Offer is Created**

若 update represents the creation of a transfer offer, look for a **Created** 事件.

* **Template:** `Utility.Registry.App.V0.Model.转账:TransferOffer`
* **Location:** Extract the 转账 Object directly from the `createArgument` of this 事件.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "createdEvent": {
    "templateId": "...:Utility.Registry.App.V0.Model.Transfer:TransferOffer",
    "createArgument": {
      "operator": "operator::122...",
      "provider": "provider::122...",
      "transfer": {
        "sender": "issuer::122...",
        "receiver": "holder::122...",
        "amount": "2.0000000000",
        "instrumentId": { "admin": "...", "id": "INST" },
        "requestedAt": "2026-03-01T13:58:32.626Z",
        "executeBefore": "2026-03-04T13:58:27.335Z",
        "inputHoldingCids": ["005152f0eae9..."],
        "meta": {
          "values": {
            "splice.lfdecentralizedtrust.org/reason": ""
          }
        }
      }
    }
  }
}
```

**Scenario B: The 转账 is Concluded**

若 update represents a concluded transfer (e.g., an accepted offer or a pre-approved transfer), look for an **Exercised** 事件.

* **Template:** `Utility.Registry.V0.Rule.转账:TransferRule`

* **Triggering Choices:** The 事件 must be triggered by one of the following choices:
  * `TransferRule_DirectTransfer`
  * `TransferRule_TwoStepTransfer`
  * `TransferRule_Transfer` (This choice will be deprecated. It is only required for backwards compatibility)

* **Location:** Extract the 转账 Object from the `choiceArgument` of this 事件.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "exercisedEvent": {
    "templateId": "...:Utility.Registry.V0.Rule.Transfer:TransferRule",
    "choice": "TransferRule_DirectTransfer",
    "choiceArgument": {
      "transfer": {
        "sender": "auth0...::122...",
        "receiver": "auth0...::122...",
        "amount": "12.0000000000",
        "instrumentId": { "admin": "...", "id": "INST" },
        "requestedAt": "2026-02-24T16:27:33.139Z",
        "executeBefore": "2026-02-27T16:27:31.633Z",
        "inputHoldingCids": ["0000c37c6..."],
        "meta": {
          "values": {
            "splice.lfdecentralizedtrust.org/reason": ""
          }
        }
      }
    }
  }
}
```

**Scenario C: The 转账 Offer is Rejected or Withdrawn**

若 update represents an offer that was ultimately rejected or withdrawn, locating the object is a two-step process:

1. **Identify the 事件:** Look for an **Exercised** 事件 matching the following:
   * **Interface ID:** `Splice.Api.Token.TransferInstructionV1:TransferInstruction`
   * **Triggering Choices:** `TransferInstruction_Reject` OR `TransferInstruction_Withdraw`
2. **Fetch the 合约 ID:** Extract the 合约 ID of the transfer offer from this exercised 事件.
3. **Fetch the Original Offer:** 查询 the JSON API using the extracted 合约 ID: `GET /v2/事件/事件-by-合约-id`
4. **Location:** Extract the 转账 Object from the `createArgument` of the original transfer offer (transfer instruction) returned by this secondary query.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "createdEvent": {
    "templateId": "...:Utility.Registry.App.V0.Model.Transfer:TransferOffer",
    "createArgument": {
      "operator": "operator::12209b02d...",
      "provider": "provider::1220c07e7...",
      "transfer": {
        "sender": "issuer::1220c07e7...",
        "receiver": "holder::1220c07e7...",
        "amount": "2.0000000000",
        "instrumentId": { "admin": "registrar::1220c07e7...", "id": "INST" },
        "requestedAt": "2026-03-01T13:58:32.626Z",
        "executeBefore": "2026-03-04T13:58:32.626Z",
        "inputHoldingCids": ["005152f0eae9..."],
        "meta": {
          "values": {
            "splice.lfdecentralizedtrust.org/reason": ""
          }
        }
      }
    }
  }
}
```

### Data Persistence and Pruning

**Ledger data is subject to pruning.** The JSON API queries described in previous section will only succeed if the 交易 事件 have not yet been pruned from the 参与者 node.

**钱包 开发者 Action 必需:** To ensure end-用户 can always access their 转账 Objects for the proofing 服务, **wallets MUST persist the 转账 Object and UpdateID data in their own backend databases** at the time the 交易 occurs. Relying strictly on real-time ledger queries for historical 交易 will result in 错误 once the 交易 are pruned. PQS can be considered as an option for storing ledger data.

### Locating the 转账 Object (as an end-用户)

**Labelling**

There are two key items to be displayed within the 交易 details:

1. Updated ID
2. 转账 object

**Displaying value**

A truncated preview of the Updated ID can be displayed or in full. A truncated preview of the json object can be displayed as needed or none at all.

**Interactive options**

用户 must be able to review the full json object.

选项 1

* Click to open a modal/side-panel 组件 or an external browser window. Since the content is hidden to start, when a 用户 clicks to open this 组件, the json object should by default be displayed fully. This 组件 展示 the label of "转账 object", contains the full json object for reviewing, and accessible copy button.
* If an external window is used, its domain must match the 应用 domain from which the window was triggered.
* The icon or button for a 用户 to click to review the json object must be accessible, along side the copy icon/button. 用户 can copy the object without opening the review 组件.

选项 2

* Click to open the accordion containing the content. The accordion is closed by default, and a copy button is accessible without opening the accordion.

**Copying behavior**

The copy behavior must always copy the full Updated ID and full json object, never the truncated preview string.

