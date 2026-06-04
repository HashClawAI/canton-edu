---
title: "Wallet Configuration"
slug: "integrations-wallet-configuration"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet/configuration.md"
source_title: "Wallet Configuration"
tags:
  - integrations
  - wallet
  - configuration
---

# Wallet Configuration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallet Configuration

> Configure the Wallet SDK for LocalNet, DevNet, TestNet, and MainNet environments

The Wallet SDK includes default configuration that works with a standard LocalNet setup from [cn-quickstart](https://github.com/digital-asset/cn-quickstart). When deploying to other environments, you need to provide custom connection settings.

## Default Configuration (LocalNet)

The default configuration connects to a LocalNet instance running on standard ports. Use it for local development and testing without modification.

When migrating to a different environment, you must create custom factories for each controller with the correct URLs and ports for that environment.

## Environment-Specific Configuration

Each environment requires different connection endpoints:

### LocalNet

LocalNet runs all services on `localhost` with standard ports. The default SDK configuration works without changes.

### DevNet / TestNet / MainNet

For remote environments, configure the following connection parameters:

* **JSON Ledger API URL** — The HTTP/JSON API endpoint for your validator's participant
* **gRPC Admin API URL** — The gRPC endpoint for participant administration
* **Validator API URL** — The validator app's REST API endpoint
* **Scan API URL** — The Scan service endpoint (either direct or via the BFT scan proxy)
* **Auth token** — A valid JWT token from your OIDC provider

## Validating Your Configuration

Verify your connection endpoints with these commands:

**JSON Ledger API** — Check the version endpoint:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://${JSON_LEDGER_API_URL}/v2/version
```

Expected output includes `version`, `features`, and `userManagement` fields. The exact values depend on your Canton version and configuration.

## Authentication

All remote environments require JWT authentication. Obtain tokens from the OIDC provider configured for your validator deployment.

The SDK accepts authentication tokens through factory functions. For remote environments, create custom factories for each controller with the correct URLs and an `AuthTokenProvider`:

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import {
  WalletSDKImpl,
  LedgerController,
  ValidatorController,
  TokenStandardController,
  AuthTokenProvider,
} from "@canton-network/wallet-sdk";

const myLedgerFactory = (
  userId: string,
  authTokenProvider: AuthTokenProvider
) => {
  return new LedgerController(
    userId,
    new URL("https://json-api.validator.YOUR_HOSTNAME"),
    undefined,
    false,
    authTokenProvider
  );
};

const myValidatorFactory = (
  userId: string,
  authTokenProvider: AuthTokenProvider
) => {
  return new ValidatorController(
    userId,
    new URL("https://wallet.validator.YOUR_HOSTNAME"),
    authTokenProvider
  );
};

const myTokenStandardFactory = (
  userId: string,
  authTokenProvider: AuthTokenProvider
) => {
  return new TokenStandardController(
    userId,
    new URL("https://json-api.validator.YOUR_HOSTNAME"),
    new URL("https://wallet.validator.YOUR_HOSTNAME"),
    undefined,
    authTokenProvider
  );
};

const sdk = new WalletSDKImpl().configure({
  logger: console,
  authFactory: myAuthFactory, // your OIDC auth implementation
  ledgerFactory: myLedgerFactory,
  validatorFactory: myValidatorFactory,
  tokenStandardFactory: myTokenStandardFactory,
});

await sdk.connect();
await sdk.connectAdmin();
await sdk.connectTopology(
  new URL("https://scan.sv.YOUR_HOSTNAME")
);
```

See the [config template](https://github.com/canton-network/wallet-gateway/blob/main/docs/wallet-integration-guide/examples/snippets/config-template.ts) in the Wallet SDK repository for a complete example.

## Next Steps

* [Wallet SDK Download](/docs/canton/integrations-wallet-sdk-download) — Installation instructions
* [Wallet Integration Guidance](/docs/canton/integrations-wallet-guidance) — Signing transactions from dApps

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
