> 配置 the 钱包 SDK for LocalNet, DevNet, TestNet, and MainNet environments

The 钱包 SDK includes default 配置 that works with a standard LocalNet setup from [cn-quickstart](https://github.com/digital-asset/cn-quickstart). When deploying to other environments, you need to provide custom connection settings.

## 默认配置（LocalNet）

The default 配置 connects to a LocalNet instance running on standard ports. Use it for local 开发 and 测试 without modification.

迁移时 to a different environment, you must create custom factories for each controller with the correct URLs and ports for that environment.

## 按环境配置

Each environment requires different connection 端点:

### LocalNet

LocalNet runs all 服务 on `localhost` with standard ports. The default SDK 配置 works without changes.

### DevNet / TestNet / MainNet

For remote environments, configure the following connection parameters:

* **JSON Ledger API URL** — The HTTP/JSON API 端点 for your validator's 参与者
* **gRPC Admin API URL** — The gRPC 端点 for 参与者 administration
* **验证者 API URL** — The validator app's REST API 端点
* **Scan API URL** — The Scan 服务 端点 (either direct or via the BFT scan proxy)
* **Auth token** — A valid JWT token from your OIDC 提供方

## 验证配置

验证 your connection 端点 with these 命令:

**JSON Ledger API** — 检查 the version 端点:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://${JSON_LEDGER_API_URL}/v2/version
```

Expected output includes `version`, `features`, and `userManagement` fields. The exact values depend on your Canton version and 配置.

## 认证

All remote environments require JWT 认证. Obtain tokens from the OIDC 提供方 configured for your validator deployment.

The SDK accepts 认证 tokens through factory functions. For remote environments, create custom factories for each controller with the correct URLs and an `AuthTokenProvider`:

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

参见 [config template](https://github.com/canton-网络/钱包-gateway/blob/main/docs/wallet-integration-guide/examples/snippets/config-template.ts) in the 钱包 SDK repository for a complete example.

## 下一步

* [钱包 SDK 下载](/集成/钱包/sdk-download) — 安装 instructions
* [钱包 集成 Guidance](/集成/钱包/guidance) — Signing 交易 from dApps

