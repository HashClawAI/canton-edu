---
title: "How to upload and query Daml packages"
slug: "appdev-modules-m5-manage-daml-packages"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-manage-daml-packages.md"
source_title: "How to upload and query Daml packages"
tags:
  - appdev
  - modules
  - m5-manage-daml-packages
---

# How to upload and query Daml packages

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# How to upload and query Daml packages

> Upload DAR files to a participant and query available Daml packages at runtime.

# How to upload and query Daml packages

Canton Participant Node exposes a package management service that allows uploading and discovery of the Daml packages. This guide explains how to programmatically manipulate the packages using the JSON Ledger API, which is described using OpenAPI specifications.

To learn about the Daml packages, see :brokenref:'DAR files and Daml packages' in the key concepts section.

Refer to the package management section in the operational guide to learn how to upload packages and inspected them using the Canton console.

## Prerequisites

Ensure that your Canton Participant Node opens a JSON Ledger API HTTP port. To learn about how to do it, read the tutorial: Get started with Canton and the JSON Ledger API.

Ensure that you have access to Daml tools such as the Assistant (`daml`) and the Compiler (`damlc`).

Install `curl` or other similar tool that facilitates interactions over the HTTP protocol.

If you want to be able to format and filter JSON output from `curl` command responses, install `jq` or a similar tool.

Before any ledger interaction, ensure to build the model into a .dar file.

## How to upload a DAR archive file

Assume you are working on a Daml model called `MyModel`, and you want to start on-ledger interactions based on this model. The first step is to upload its containing package and to make sure it is vetted on all the interacting Participant Nodes.

The JSON Ledger API provides endpoints that enable you to upload the package and get it vetted on the Participant Node as an intrinsic part of the upload process.

As most of the interactions are based on a package ID, use the damlc compiler to inspect the resulting DAR archive file and extract the package ID of your project's main package.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml damlc inspect-dar --json .daml/dist/mymodel-1.0.0.dar | jq '.main_package_id'
```

The damlc responds with the package ID:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed"
```

To upload the package, invoke a POST command on the `v2/packages` endpoint:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --data-binary @.daml/dist/mymodel-1.0.0.dar http://localhost:7575/v2/packages
```

You can verify that the package is present and registered on the ledger.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages/47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed/status
```

The ledger responds with the package status:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageStatus": "PACKAGE_STATUS_REGISTERED"
}
```

## How to query for existing packages

To list all packages known to the Participant Node, issue a GET request towards the `v2/packages` endpoint.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages
```

The Participant responds with a message containing all the known packages:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageIds": [
    "9e70a8b3510d617f8a136213f33d6a903a10ca0eeec76bb06ba55d1ed9680f69",
    "47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed",
    "bfda48f9aa2c89c895cde538ec4b4946c7085959e031ad61bde616b9849155d7"
  ]
}
```

If the list is long, use `jq` to filter the output and determine if the expected package ID is among the results.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages | jq '.packageIds | .[] | select(startswith("47"))'
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
