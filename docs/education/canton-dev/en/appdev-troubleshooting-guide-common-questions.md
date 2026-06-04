---
title: "Common Questions"
slug: "appdev-troubleshooting-guide-common-questions"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/common-questions.md"
source_title: "Common Questions"
tags:
  - appdev
  - troubleshooting-guide
  - common-questions
---

# Common Questions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Questions

> Frequently asked questions about Canton Network application development

Answers to questions that come up regularly in Canton Network application development. For validator operations questions, see the [Common Issues FAQ](/docs/canton/appdev-faq).

## Getting Started

### What SDK version should I use?

Use the latest stable Daml SDK (3.x series). The 2.x Daml SDK is for historical development and does not support Canton Network features like the Global Synchronizer or Canton Coin.

Check the current recommended version in the [cn-quickstart repository](https://github.com/digital-asset/cn-quickstart), which always pins a compatible SDK version in its configuration.

### Can I use JavaScript, Python, or Go?

Daml models must be written in the Daml language. Your application's backend and frontend, however, can use any language that speaks gRPC or HTTP.

* **Java and Scala** have official language bindings and code generation from Daml packages
* **JavaScript/TypeScript** can use the JSON API (HTTP) or gRPC client libraries. The cn-quickstart includes a TypeScript frontend as a reference
* **Python and Go** can use gRPC client libraries generated from the Ledger API `.proto` files

There are also community-maintained bindings for some languages. See the [language bindings](https://docs.canton.network/sdks-tools/language-bindings/community) page.

### Where do I find example code?

The [cn-quickstart](https://github.com/digital-asset/cn-quickstart) repository is the primary reference application. It includes:

* A complete Daml model with SCU-compatible upgrades
* A TypeScript frontend
* Backend automation with Daml Script
* Docker Compose configuration for LocalNet
* CI/CD patterns

Clone the repository and follow the README to get a working application running locally.

## Development

### How do I test multi-party workflows locally?

The sandbox and LocalNet both support multiple parties. You can allocate parties and submit commands as different identities within the same local environment.

With `dpm sandbox`, allocate parties in Daml Script:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
alice <- allocateParty "Alice"
bob <- allocateParty "Bob"
```

With LocalNet (via cn-quickstart), parties are pre-configured in the Docker Compose setup. You can add more by modifying the bootstrap scripts.

For testing workflows that span multiple validators, use LocalNet rather than the single-node sandbox. LocalNet runs separate validator processes that communicate through a local synchronizer, which better simulates a real network topology.

### How do I handle contract contention?

When multiple transactions target the same contract simultaneously, Canton rejects all but one. Your application should implement retry logic with exponential backoff:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
async function submitWithRetry(command: Command, maxRetries = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await ledgerClient.submit(command);
    } catch (error) {
      if (error.code === "ABORTED" && attempt < maxRetries - 1) {
        await new Promise(r => setTimeout(r, Math.pow(2, attempt) * 100));
        continue;
      }
      throw error;
    }
  }
}
```

For high-contention scenarios, consider redesigning your Daml model to split frequently-contested contracts into independent shards.

### What is the difference between sandbox and LocalNet?

**Sandbox** is a lightweight, single-process Daml ledger. Run it with `dpm sandbox`. It is fast to start and good for unit testing Daml models and scripts, but it does not run the full Canton protocol stack.

**LocalNet** is a multi-container environment that runs actual Canton validators, a synchronizer, and supporting services (JSON API, PQS, wallet). It is started through cn-quickstart with `make start` and closely mirrors a real network deployment.

Use sandbox for rapid iteration on Daml code. Use LocalNet when you need to test network-level behavior like multi-party transactions across validators, traffic consumption, or wallet interactions.

## Deployment

### How do I move from LocalNet to DevNet?

1. Build your DAR with `dpm build`
2. Request DevNet access from a Super Validator sponsor (allow 2-4 weeks for approval)
3. Once you have VPN credentials and your IP is whitelisted, upload your DAR to your DevNet validator
4. Update your application's connection settings to point at the DevNet Ledger API endpoint instead of localhost
5. Use the DevNet faucet (Tap) to get test Canton Coin for traffic

Your Daml code does not change between environments. Only the connection configuration and authentication setup differ.

### How do I upload a DAR to a remote validator?

Use the validator's Admin API or the Canton Console.

**Via Admin API:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://your-validator:5002/v2/packages" \
  -H "Authorization: Bearer $TOKEN" \
  -F "dar=@.build/your-package.dar"
```

**Via Canton Console:**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res1: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

After uploading, verify the package is visible:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl "https://your-validator:5002/v2/packages" \
  -H "Authorization: Bearer $TOKEN" | jq '.package_ids | length'
```

### How do I get my app featured on Canton Network?

Applications can apply for featured status through the Canton Improvement Proposal (CIP) process. Start by reviewing the [CIP introduction](/docs/canton/overview-understand-cips-introduction) and the [getting your app featured](/docs/canton/overview-understand-getting-app-featured) guide.

The process involves submitting a proposal that describes your application, its value to the network, and how it uses Canton Network infrastructure. Featured apps gain visibility on canton.network and may receive support from the Global Synchronizer Foundation.

## Modeling Questions

### Model an Agreement With Another Party

To enter into an agreement, create a contract from a template that has an explicit `signatory` statement.

You'll need to use a series of contracts that give each party the chance to consent, via a contract choice.

Because of the rules that Daml enforces, it is not possible for a single party to create an instance of a multi-party agreement. This is because such a creation would force the other parties into that agreement, without giving them a choice to enter it or not.

### Model Rights

Use a contract choice to model a right. A party exercises that right by exercising the choice.

### Void a Contract

To allow voiding a contract, provide a choice that does not create any new contracts. Daml contracts are archived (but not deleted) when a consuming choice is made - so exercising the choice effectively voids the contract.

However, you should bear in mind who is allowed to void a contract, especially without the re-sought consent of the other signatories.

### Represent Off-ledger Parties

You'd need to do this if you can't set up all parties as ledger participants, because the Daml `Party` type gets associated with a cryptographic key and can so only be used with parties that have been set up accordingly.

To model off-ledger parties in Daml, they must be represented on-ledger by a participant who can sign on their behalf. You could represent them with an ordinary `Text` argument.

This isn't very private, so you could use a numeric ID/an accountId to identify the off-ledger client.

### Limit a Choice by Time

Some rights have a time limit: either a time by which it must be exercised or a time before which it cannot be exercised.

You can use `getTime` to get the current time, and compare your desired time to it. Use `assert` to abort the choice if your time condition is not met.

### Model a Mandatory Action

If you want to ensure that a party takes some action within a given time period. Might want to incur a penalty if they don't - because that would breach the contract.

For example: an Invoice that must be paid by a certain date, with a penalty (could be something like an added interest charge or a penalty fee). To do this, you could have a time-limited Penalty choice that can only be exercised *after* the time period has expired.

However, note that the penalty action can only ever create another contract on the ledger, which represents an agreement between all parties that the initial contract has been breached. Ultimately, the recourse for any breach is legal action of some kind. What Daml provides is provable violation of the agreement.

### Use Optional

The `Optional` type, from the standard library, to indicate that a value is optional, i.e, that in some cases it may be missing.

In functional languages, `Optional` is a better way of indicating a missing value than using the more familiar value "NULL", present in imperative languages like Java.

To use `Optional`, include `Optional.daml` from the standard library:

Then, you can create `Optional` values like this:

You can test for existence in various ways:

If you need to extract the value, use the `optional` function.

It returns a value of a defined type, and takes a `Optional` value and a function that can transform the value contained in a `Some` value of the `Optional` to that type. If it is missing `optional` also takes a value of the return type (the default value), which will be returned if the `Optional` value is `None`

If `optionalValue` is `Some 5`, the value of `t` would be `"The number is 5"`. If it was `None`, `t` would be `"No number"`. Note that with `optional`, it is possible to return a different type from that contained in the `Optional` value. This makes the `Optional` type very flexible.

There are many other functions in "Optional.daml" that let you perform familiar functional operations on structures that contain `Optional` values – such as `map`, `filter`, etc. on `Lists` of `Optional` values.

## Testing

### Test That a Contract Is Visible to a Party

Use `queryContractId`: its first argument is a party, and the second is a `ContractId`. If the contract corresponding to that `ContractId` exists and is visible to the party, the result will be wrapped in `Some`, otherwise the result will be `None`.

Use a `submit` block and a `fetch` operation. The `submit` block tests that the contract (as a `ContractId`) is visible to that party, and the `fetch` tests that it is valid, i.e., that the contract does exist.

For example, if we wanted to test for the existence and visibility of an `Invoice`, visible to 'Alice', whose ContractId is bound to `invoiceCid`, we could say:

Note that we pattern match on the `Some` constructor. If the contract doesn't exist or is not visible to 'Alice', the test will fail with a pattern match error.

Now that the contract is bound to a variable, we can check whether it has some expected values:

### Test That an Update Action Cannot Be Committed

Use the `submitMustFail` function. This is similar in form to the `submit` function, but is an assertion that an update will fail if attempted by some Party.

{/* COPIED_END */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
