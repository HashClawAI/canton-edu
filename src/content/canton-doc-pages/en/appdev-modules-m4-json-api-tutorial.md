---
title: "Canton and the JSON Ledger API"
slug: "appdev-modules-m4-json-api-tutorial"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-json-api-tutorial.md"
source_title: "Canton and the JSON Ledger API"
tags:
  - appdev
  - modules
  - m4-json-api-tutorial
---

# Canton and the JSON Ledger API

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton and the JSON Ledger API

> Get started with Canton and the JSON Ledger API, first with curl and then with TypeScript.

## Get started with Canton and the JSON Ledger API

This tutorial demonstrates how to interact with the Canton Ledger using the JSON Ledger API from the command line. It uses `curl` and optionally `websocat` to communicate with the Ledger.

### Overview

This example shows how to:

* enable the JSON Ledger API in the Canton configuration
* create a contract using the JSON Ledger API and basic Bash tools (`curl`)
* list active contracts using `curl`
* basic error handling and troubleshooting

### Prerequisites

#### Tools

Before running the project, ensure you have the following installed:

* A Bash-compatible terminal (e.g., macOS Terminal, Git Bash, etc.)
* **Dpm** — Install following these instructions

<div className="parsed-literal">
  curl -sSL [https://get.digitalasset.com/install/install.sh](https://get.digitalasset.com/install/install.sh) | sh -s

  (check installed dpm version by entering in bash console `dpm version --active`, it should be at least )
</div>

* `canton` — Canton release with installation and examples, check Canton demo for details
* `curl` — command-line HTTP client: [https://github.com/curl/curl](https://github.com/curl/curl) (installation: [https://curl.se/download.html](https://curl.se/download.html))
* (Optional) `jq` — command-line JSON processor: [https://github.com/jqlang/jq](https://github.com/jqlang/jq) (installation: [https://jqlang.org/download/](https://jqlang.org/download/))

#### Daml Model

To demonstrate the JSON Ledger API, you need an example Daml model.

Run the following command in the console:

```
dpm new json-tests
```

A folder named `json-tests` should be created. Check its contents and inspect the code in `daml/Main.daml`.

It should contain a Daml model with a template named `Asset`:

```
template Asset
  with
    issuer : Party
    owner  : Party
    name   : Text
  where
    ensure name /= ""
    signatory issuer
    observer owner
    choice Give : AssetId
      with
        newOwner : Party
      controller owner
      do create this with
        owner = newOwner
```

Before proceeding, compile the Daml model by running the following command inside the folder:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
```

A file named `.daml/dist/json-tests-0.0.1.dar` should be created.

### Starting Canton with JSON Ledger API

First, ensure you can run the Canton sandbox with the JSON Ledger API enabled.

Start the Canton sandbox, providing a path to the created `dar` file:

```
dpm sandbox --json-api-port 7575 --dar &lt;path_to_json_tests_project&gt;/.daml/dist/json-tests-0.0.1.dar
```

<Note>
  To simplify this tutorial, no security-related configuration is used. You will be able to send commands as any user.
</Note>

Open a new Bash terminal, but keep the Canton sandbox running.

#### Verification - download OpenAPI

To verify that the JSON Ledger API is working, check if the documentation endpoint is available.

In a new Bash terminal, run:

```
curl localhost:7575/docs/openapi
```

You should receive a long YAML document starting with:

```
openapi: 3.0.3
info:
  title: JSON Ledger API HTTP endpoints
  version: 3.3.0
paths:
  /v2/commands/submit-and-wait:
    post:
```

This `openapi.yaml` document provides an overview of the available endpoints and can be pasted into a tool like [https://editor-next.swagger.io](https://editor-next.swagger.io).

It can also be used to generate client stubs in languages like `Java` or `TypeScript`.

<Note>
  You can use the `http://localhost:757/livez` endpoint to check whether the server is running. It might be used as a health check in production environments.
</Note>

#### Create a party

Run this command in the terminal:

```
curl -d '{"partyIdHint":"Alice", "identityProviderId": ""}' -H "Content-Type: application/json" -X POST localhost:7575/v2/parties
```

This should return a response similar to:

```
{"partyDetails":{"party":"Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141","isLocal":true,"localMetadata":{"resourceVersion":"0","annotations":{}},"identityProviderId":""}}
```

Take note of the party ID, which will be used in the following steps. In this example, it is:

`Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141` — but this will differ in your case.

### Create a contract

Create a file called `create.json` with the following content, replacing `\<partyId\>` with the actual party ID shown earlier:

```
{
  "commands": [
    {
      "CreateCommand": {
        "createArguments": {
          "issuer": "<partyId>",
          "owner": "<partyId>",
          "name": "Example Asset Name"
        },
        "templateId": "#json-tests:Main:Asset"
      }
    }
  ],
  "userId": "ledger-api-user",
  "commandId": "example-app-create-1234",
  "actAs": [
    "<partyId>"
  ],
  "readAs": [
    "<partyId>"
  ]
}
```

Now submit the request:

```
curl localhost:7575/v2/commands/submit-and-wait -H "Content-Type: application/json" -d@create.json
```

A successful response should look like:

```
{"updateId":"...","completionOffset":20}
```

This confirms that a contract was created on the ledger.

### Query the ledger

To query the ledger for active contracts, first create a file named \`acs.json\`:

```
{
  "eventFormat": {
    "filtersByParty": {},
    "filtersForAnyParty": {
      "cumulative": [
        {
          "identifierFilter": {
            "WildcardFilter": {
              "value": {
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    },
    "verbose": false
  },
  "verbose": false,
  "activeAtOffset": <offset>
}
```

Replace `\<offset\>` with the `completionOffset` you received earlier (e.g., `20`).

Run the query:

```
curl localhost:7575/v2/state/active-contracts -H "Content-Type: application/json" -d@acs.json
```

You should receive a response containing contract information.

To improve readability, pipe the output to \`jq\`:

```
curl localhost:7575/v2/state/active-contracts -H "Content-Type: application/json" -d@acs.json | jq
```

Look for the `createdEvent` section, which contains contract details like:

```
"createdEvent": {
      "offset": 20,
      "nodeId": 0,
      "contractId": "00572c50513ced94f9cddaf1e6d2d3f050ae35d7fea0affe06f65f4238e84136edca1112202d01e45b5cfafb61e3942e4610547689dbebfebd3ea7d10d57944401fc17e81b",
      "templateId": "6fd1d46124d5ab0c958ce35e9bb370bb2835b2672a0d6fa039a3855c11b8801d:Main:Asset",
      "contractKey": null,
      "createArgument": {
        "issuer": "Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141",
        "owner": "Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141",
        "name": "Example Asset Name"
      },
  ...
}
```

### Troubleshooting

If you encounter issues while calling the using curl - you should enable `-v` (verbose) mode to see the request and response details. For instance:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -v -d '{"partyIdHint":"Alice", "identityProviderId": ""}' -H "Content-Type: application/json" -X POST localhost:7575/v2/parties
```

Http response different than 200 (e.g., 400, 404, etc.) indicates an error. The response body will contain details about the error.

If it does not help, read logs available in the canton sandbox terminal or in the file `\<canton_installation\>/logs/canton.log`.

If nothing is returned when you query `localhost:7575/v2/state/active-contracts` ensure that the offset provided is correct and corresponds to the `completionOffset` from the `localhost:7575/v2/commands/submit-and-wait` command. You can also check current offset by running:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl localhost:7575/v2/state/ledger-end
```

### Next steps

#### Canton examples

For a more advanced scenario involving two parties, explore the examples provided with Canton installation: `\<canton_installation\>/examples/json-ledger-api\>`

A `TypeScript` version is also available that demonstrates how to create a JSON Ledger API client for use in a web browser.

#### OpenAPI and AsyncAPI

Read more about the OpenAPI and AsyncAPI specifications for the Canton JSON Ledger API: `references_json-api`.

#### Authentication and security

Read how to configure and use jwt token to access JSON Ledger API `json-api-access-tokens`.

#### Error codes

For more information about error codes returned by the JSON Ledger API, see `json-error-codes`.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/tutorials/json-api/canton_and_the_json_ledger_api_ts.rst" hash="a2d8fcf5" */}

## Get Started with Canton, the JSON Ledger API, and TypeScript

This tutorial shows you how to interact with a Canton Ledger using the JSON Ledger API and TypeScript.

### Overview

You will use and modify an existing example project provided with the Canton distribution.

### Prerequisites

You should be familiar with the basics of TypeScript and tools such as `npm` and `node.js`.

#### Tools

Before starting, ensure you have the following installed:

* **Node.js and npm** — Download from [https://nodejs.org/en/download/](https://nodejs.org/en/download/). Recommended version: `18.20.x` or later.
* **Dpm** — Install following these instructions

<div className="parsed-literal">
  curl -sSL [https://get.digitalasset.com/install/install.sh](https://get.digitalasset.com/install/install.sh) | sh -s
</div>

Verify the installation by running:

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  dpm version --active

```

You should see a version equal to or later than .

* **Canton** — Includes pre-built examples. See the Canton demo for details.

#### Example TypeScript Project

Open a terminal and navigate to the JSON Ledger API example folder:

```
cd &lt;canton_installation&gt;/examples/09-json-ledger-api
```

Start Canton:

```
./run.sh
```

Once the Canton console is ready, open a new terminal and navigate to the TypeScript example folder:

```
cd &lt;canton_installation&gt;/examples/09-json-ledger-api/typescript
```

### Running the Example

Install the project dependencies:

```
npm install
```

You may see some warnings, which can be ignored for now.

The JSON Ledger API provides an OpenAPI specification. You can use this to generate TypeScript client classes (stubs).

To generate the TypeScript client:

```
npm run generate_api
```

Check the generated code in the `generated/api` folder. It should include the TypeScript classes for the API.

```
less generated/api/ledger-api.d.ts
```

This file contains definitions for services and models, such as `/v2/commands/submit-and-wait`, `CreateCommand`, and many others.

Next, generate TypeScript types from the Daml model:

```
npm run generate_daml_bindings
```

This creates bindings in the `./generated` folder. Each Daml module has its own subfolder, for example: `generated/model-tests-1.0.0/lib/Iou`.

Now compile the TypeScript code:

```
npm run build
```

Once the build succeeds, run the example:

```
npm run scenario
```

You should see output similar to:

```
Alice creates contract
Ledger offset: 23
...
Bob accepts transfer
...
End of scenario
```

### Code Highlights

The JSON Ledger API client is configured in \`src/client.ts\`:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import type { paths } from "../generated/api/ledger-api";

export const client = createClient<paths>({ baseUrl: "http://localhost:7575" });
```

The `openapi-fetch` library is used to create the API client.

#### Allocating a Party

In `src/user.ts`, a party is allocated as follows:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const resp = await client.POST("/v2/parties", {
    body: {
        partyIdHint: user,
        identityProviderId: "",
    }
});
```

<Note>
  `openapi-fetch` uses the Indexed Access Types TypeScript feature to provide type safety. The example above looks like untyped JavaScript, but it is in fact type-safe.
</Note>

#### Creating a Contract

In `src/commands.ts`, a contract is created using:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export async function createContract(userParty: string): Promise<components["schemas"]["SubmitAndWaitResponse"]> {
    const iou: Iou.Iou = {
        issuer: userParty,
        owner: userParty,
        currency: "USD",
        amount: "100",
        observers: []
    };

    const command: components["schemas"]["CreateCommand"] = {
        createArguments: iou,
        templateId: Iou.Iou.templateId
    };

    const jsCommands = makeCommands(userParty, [{ CreateCommand: command }]);
    const resp = await client.POST("/v2/commands/submit-and-wait", {
        body: jsCommands
    });

    return valueOrError(resp);
}
```

#### Querying Contracts

In `src/index.ts`, contracts are queried like this:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const { data, error } = await client.POST("/v2/state/active-contracts", {
    body: filter
});

if (data === undefined)
    return Promise.reject(error);
else {
    const contracts: components["schemas"]["CreatedEvent"][] = data
        .map((res) => res.contractEntry)
        .filter((res) => "JsActiveContract" in res)
        .map((res) => res.JsActiveContract.createdEvent);

    return Promise.resolve(contracts);
}
```

### Extending the Example

In this step, you extend the `Iou` template with a new field and update the TypeScript code accordingly.

1. Open the `Io.daml` file in `canton/examples/09-json-ledger-api/model`.
2. Modify the `Iou` template to include a new `comment` field:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Iou
  with
    issuer : Party
    owner : Party
    currency : Text
    amount : Decimal
    observers : [Party]
    comment : Optional Text -- added field
  where
    -- leave the rest of the template unchanged
```

\> The `comment` field is optional, making this a backwards-compatible change.

3. Stop the Canton server (`Ctrl+C`) and restart it:

```
./run.sh
```

4. Rebuild the TypeScript bindings:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm run generate_daml_bindings
```

5. Update the `createContract` function in `src/commands.ts` to include the new field:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export async function createContract(userParty: string): Promise<components["schemas"]["SubmitAndWaitResponse"]> {
    const iou: Iou.Iou = {
        issuer: userParty,
        owner: userParty,
        currency: "USD",
        amount: "100",
        observers: [],
        comment: "This is a test comment" // new field
    };
    // leave the rest of the function unchanged
```

6. Rebuild the TypeScript code:

```
npm run build
```

7. Run the example:

```
npm run scenario
```

You won’t see the new `comment` field in the output yet. To display it, modify the `showAcs` function call in `src/index.ts` to include the new field:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
showAcs(contracts, ["owner", "amount", "currency", "comment"], c => [c.owner, c.amount, c.currency, c.comment]);
```

The, execute the `npm run scenario` once again.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
