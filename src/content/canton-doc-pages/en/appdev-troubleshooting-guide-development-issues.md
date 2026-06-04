---
title: "Development Issues"
slug: "appdev-troubleshooting-guide-development-issues"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/development-issues.md"
source_title: "Development Issues"
tags:
  - appdev
  - troubleshooting-guide
  - development-issues
---

# Development Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Development Issues

> Troubleshooting Daml compilation errors, API connection problems, and transaction failures during development

This page addresses problems you are likely to hit while writing Daml code, connecting to APIs, and submitting transactions during local development.

## Daml Compilation Errors

### Common type mismatches

The Daml compiler enforces strict typing. A frequent mistake is passing a `ContractId` where the template type is expected, or vice versa.

```
error:
  Couldn't match expected type 'Asset' with actual type 'ContractId Asset'
```

**Fix:** Use `fetch` to retrieve the contract payload from a `ContractId`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asset <- fetch assetCid
```

Another common variant is confusing `Party` with `Text`:

```
Couldn't match expected type 'Party' with actual type 'Text'
```

Use `getParty` in Daml Script or pass the `Party` value directly rather than a string.

### Missing imports

If the compiler reports an unknown type or function, you likely need an import. Daml does not auto-import modules.

```
error: Not in scope: 'DA.Optional.fromSome'
```

**Fix:**

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import DA.Optional (fromSome)
```

### SCU compatibility check failures

When upgrading Daml packages, the Smart Contract Upgrade (SCU) compatibility checker may reject changes. Common violations include removing a field from a template or changing a field's type.

```
error: Upgrade check failed: field 'amount' has changed type from 'Int' to 'Decimal'
```

SCU requires that new package versions remain wire-compatible with previous versions. You can add optional fields (with defaults), but you cannot remove or change existing fields.

<Warning>
  Daml exceptions are deprecated. If you see compiler warnings about exception usage, refactor to use `Either` or other error-handling patterns instead.
</Warning>

## API Connection Problems

### Wrong port

Each Canton component listens on a different port. If your application gets `Connection refused`, verify you are targeting the correct one:

* **Ledger API (gRPC)** -- 5001
* **JSON API** -- 7575
* **Admin API** -- 5002
* **Participant health** -- 5003

Check which ports are actually in use:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

### Auth token issues

If the Ledger API returns `UNAUTHENTICATED`, your token may be expired, have the wrong audience, or lack the required scope.

```
UNAUTHENTICATED: Could not verify JWT token: token is expired
```

**Checklist:**

* Token has the `daml_ledger_api` scope
* Token audience matches `LEDGER_API_AUTH_AUDIENCE` in your config
* Token has not expired (check `exp` claim)

Decode your token to inspect claims:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
echo "$TOKEN" | cut -d'.' -f2 | base64 -d 2>/dev/null | jq .
```

### Sandbox not ready yet

After running `dpm sandbox`, the sandbox takes a few seconds to initialize. If your application connects immediately, it may fail with:

```
UNAVAILABLE: io exception - Connection refused
```

Wait for the sandbox health endpoint to respond before sending requests:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
until curl -s http://localhost:5003/health | grep -q "SERVING"; do
  sleep 1
done
```

## Transaction Failures in Development

### Authorization errors

The most common transaction rejection is an authorization failure. Canton rejects transactions when the submitting party is not authorized as a signatory or controller.

```
INVALID_ARGUMENT: Interpretation error:
  ... requires authorizers Party('Alice'), but only Party('Bob') were given
```

**Fix:** Ensure the party submitting the command is listed as a `signatory` or `controller` for the relevant choice. If a different party must act, use a delegation pattern where the authorized party creates a contract granting exercise rights.

### Contention on the same contract

When two transactions try to exercise a consuming choice on the same contract simultaneously, one will be rejected:

```
ABORTED: Interpretation error: ... contract not active
```

This is expected behavior in Canton's UTXO-based model. The fix depends on your use case:

* **Retry with backoff** if the operation is idempotent
* **Redesign the workflow** to reduce single-contract bottlenecks (e.g., split a counter contract into shards)
* **Sequence operations** on the client side when ordering matters

### Package vetting: DAR not uploaded

If your transaction references a package the validator does not know about, you get:

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <package-id>
```

Upload your DAR file before submitting transactions:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Using dpm
dpm build
dpm sandbox

# Or upload manually via the Admin API
curl -X POST http://localhost:5002/v2/packages \
  -F "dar=@.build/your-package.dar"
```

Verify the package is known:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost:5002/v2/packages | jq '.package_ids | length'
```

<Note>
  For cn-quickstart, run `make setup` then `make build` before `make start`. The build step compiles Daml and uploads DARs to the local environment.
</Note>

## Additional Daml Error Messages

### Error: "\<X> is not authorized to commit an update"

This error occurs when there are multiple obligables on a contract.

A cornerstone of Daml is that you cannot create a contract that will force some other party (or parties) into an obligation. This error means that a party is trying to do something that would force another parties into an agreement without their consent.

To solve this, make sure each party is entering into the contract freely by exercising a choice. A good way of ensuring this is the "initial and accept" pattern: see the Daml patterns for more details.

### Error: "Argument is not of serializable type"

This error occurs when you're using a function as a parameter to a template. For example, here is a contract that creates a `Payout` controller by a receiver's supervisor:

Hovering over the compilation error displays:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
[Type checker] Argument expands to non-serializable type Party -> Party.
```

### Error: "Recursion limit overflow in module"

The error usually occurs when uploading a DAR to a ledger or using a script via the sandbox. It can manifest on upload as:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{"code":"DAR_PARSE_ERROR", "cause": "Failed to parse the dar file content.", ...}
```

or in your logs as:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
Recursion limit overflow in module '<pkgid>:<modulename>'
```

This error is usually caused by having an expression in the DAR whose serialized representation exceeds a depth of 1000 layers. This can be caused by long Daml scripts, since every use of a function call or `<-` to bind a variable in a `do` block can incur several layers of recursion in the `do` block's serialized representation. Large datatypes with more than 160 fields with `deriving` clauses can also cause this.

### Solving script recursion limits

Normally, one call inside `do` introduces 4 layers of recursion, meaning about 250 binds in a script can cause an overflow. However, other expressions in a do block, such as let binds, also introduce a layer of recursion, so functions with fewer binds can also trigger the limit.

Possible workarounds include splitting a large script into multiple scripts or separating logic in the script out into helper functions. For example, assume you have written the following long script:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data State = State { partA : Text, partB : Text, partC : Text }

-- MyTemplate defines three choices that update parts A, B, and C of the State
myScript : Party -> ContractId MyTemplate -> State -> Script State
myScript party cid state0 = do
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state0)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state0)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state0)
  let state1 = State newPartA newPartB newPartC

  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state1)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state1)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state1)
  let state2 = State newPartA newPartB newPartC

  ...
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state99)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state99)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state99)
  let state100 = State newPartA newPartB newPartC

  pure state100
```

This script has 300 binds, well exceeding the tentative limit of 250 binds. We can refactor this script to instead define and use a helper `updateStateOnce`, which runs all three choices together.

**Note:** In many cases, the compiler optimizes your script to produce an expression that does not break the recursion limit despite having many binds. In this example, we have given an intentionally convoluted example that is difficult for the compiler to optimize away.

By using this helper, each block of three exercises is reduced to a single bind, such that `myScript` now has only 100 binds, well below the recursion limit.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data State = State { partA : Text, partB : Text, partC : Text }
  deriving (Show, Eq)

helper : Party -> ContractId MyTemplate -> State -> Script State
helper party cid state = do
  newPartA <- party `submit` exerciseCmd cid (UpdateStatePartA state.partA)
  newPartB <- party `submit` exerciseCmd cid (UpdateStatePartB state.partB)
  newPartC <- party `submit` exerciseCmd cid (UpdateStatePartC state.partC)
  pure (State newPartA newPartB newPartC)

myScript : Party -> ContractId MyTemplate -> State -> Script State
myScript party cid state0 = do
  state1 <- helper party cid state0
  state2 <- helper party cid state1
  ...
  state100 <- helper party cid state99

  pure state100
```

In general, it is a good idea to keep your scripts small, by maximizing code reuse and splitting logic into maintainable chunks.

### Solving datatype recursion limits

Large datatypes with `deriving` clauses can also cause overflow errors. Consider the following case of a datatype with 300 fields and a `deriving Show` instance:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyData = MyData
  { field1A : Text
  , field1B : Text
  , field1C : Text
  , field2A : Text
  , field2B : Text
  , field2C : Text
  ...
  , field100A : Text
  , field100B : Text
  , field100C : Text
  }
  deriving Show
```

In this case, the `deriving Show` clause means that instance of `Show MyData` is automatically derived to be something like the following:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Something similar to this code is implicitly autogenerated by the `deriving Show` clause
instance Show MyData where
  show MyData {..} =
    show field1A <> (show field1B <> (show field1C <> (
      (show field2A <> (show field2B <> (show field2C <> (
        ...
        (show field100A <> (show field100B <> (show field100C)))
      ))))
    )))
```

You can see that the implicit, autogenerated definition of `show` has an expression that becomes more and more deeply nested as you go along. Once the number of fields exceeds about 160, this expression has the potential to reach the depth necessary to cause an overflow in its serialized representation in the DAR.

Similarly to Daml Scripts, the recommended workaround for this issue is to split your datatype into many parts. For example, we could create an additional datatype `Helper` which contains the elements `a`, `b`, and `c`, and use that within `MyData`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Helper = Helper
  { a : Text
  , b : Text
  , c : Text
  }
  deriving Show

data MyData = MyData
  { field1 : Helper
  , field2 : Helper
  ...
  , field100 : Helper
  }
  deriving Show
```

The generated code for `MyData` now has only 100 fields to traverse and nest. Similarly to scripts, it is a good idea to keep your datatypes small, by maximizing code reuse and splitting logic into maintainable chunks.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
