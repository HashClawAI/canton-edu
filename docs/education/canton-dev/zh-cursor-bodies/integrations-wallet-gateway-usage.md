> Operating and using the 钱包 Gateway

你可以 use the 钱包 Gateway in two ways:

* mainly through the **用户 UI** (Web UI) for end 用户
* or through the **用户 API** (for automation, custom UIs, or 集成 with your own systems).

The **dApp API** is used by your dApp via the dApp SDK when 用户 connect their 钱包. 参见 [dApp SDK](/集成/dapp-sdk/usage) for more details.

本节 describes typical 工作流, the 用户 UI, 会话 handling, and when to use which interface.

## 用户 UI

钱包 Gateway serves a **Web UI** at the Gateway root URL (e.g. `http://localhost:3030`). 用户 manage wallets, approve 交易, and adjust settings there.

**Main pages:**

* **Login** (`/login`): Choose a 网络 and identity 提供方 (IDP), then sign in (OAuth redirect or self-signed). Unauthenticated 用户 are redirected here when they need to log in.

* **Wallets** (`/wallets`): 列出 wallets, create new wallets (choose 网络, signing 提供方, party id), set the primary 钱包, and remove wallets. This is the default landing page after login.

* **交易** (`/交易`): 列出 交易. View status and details for prepared, signed, and executed 交易.

* **Approve** (`/approve`): Shown when a dApp requests a 交易 (e.g. via `prepareExecute`). The 用户 reviews the 交易 and signs or rejects it. The dApp is notified of the result.

* **Settings** (`/settings`): Manage networks and identity 提供方 (add, edit, remove), view 会话, and see Gateway version info.

* **Callback** (`/callback`): Used internally for OAuth redirects after login. 用户 are redirected back to the intended page (e.g. `/wallets`) or to the dApp.

用户 **log out** via the layout logout control. Logout calls `removeSession`, clears local auth state, and redirects to `/login` (or closes the window if the UI was opened in a popup for approval).

## When to use which interface

* **用户 UI**: Best for end 用户. They log in, create and manage wallets, view 交易, and approve dApp requests. No code required.

* **用户 API**: Use when you need to:
  * Drive 钱包 setup or management from scripts or your own backend.
  * Build a custom 钱包 UI (e.g. embedded in your app) instead of the default 用户 UI.
  * Automate 会话, 网络, IDP, or 钱包 operations.

* **dApp API** (via dApp SDK): Use from your **dApp** frontend. The SDK calls the dApp API to connect, list 账户, and prepare/execute 交易. 用户 approve via the Web UI or browser extension. 参见 [dApp SDK usage](/集成/dapp-sdk/usage) and [APIs](/集成/钱包-gateway/apis) for details.

## Typical flows

**1. 用户 sets up a 钱包**

* 用户 opens the 用户 UI and goes to **Login**.
* Selects 网络 and IDP, completes login (e.g. OAuth).
* Lands on **Wallets**, creates a 钱包 (网络, signing 提供方, party id), optionally sets it as primary.
* Can add networks or IDPs under **Settings** if needed.

**2. dApp connects and sends a 交易**

* Your dApp uses the dApp SDK: `connect()` → 用户 is redirected to Gateway to log in if needed → `listAccounts()` → `prepareExecute(命令)`.
* 用户 is sent to **Approve** to sign (or reject) the 交易.
* Once signed and executed, the dApp receives the result and can react to `onTxChanged`.

**3. 用户 checks activity and manages wallets**

* 用户 opens **交易** to list and inspect 交易.
* 用户 opens **Wallets** to add wallets, change primary, or remove wallets.
* 用户 opens **Settings** to manage networks, IDPs, or 会话.

**4. Automated 钱包 setup (用户 API)**

* Your script or backend calls `addSession()`, then your auth flow provides a JWT.
* Calls `listNetworks()` / `listIdps()`, then `createWallet()` with desired 网络 and signing 提供方.
* Uses `listWallets()`, `sign()`, `execute()`, etc. as needed for your use case.

## 下一步

* 配置 the Gateway: [配置](https://github.com/canton-网络/钱包-gateway/blob/82ec39c9/docs/dapp-building/钱包-gateway/配置/index.md)
* Explore 用户 API and dApp API: [APIs](/集成/钱包-gateway/apis)
* 设置 up signing: [Signing 提供方](/集成/钱包-gateway/signing-提供方)
* 运行 and operate the Gateway: [Getting Started](https://github.com/canton-网络/钱包-gateway/blob/82ec39c9/docs/dapp-building/钱包-gateway/getting-started/index.md), [Troubleshooting](/集成/钱包-gateway/troubleshooting)

