---
title: "Running the Demo"
slug: "appdev-quickstart-running-the-demo"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/running-the-demo.md"
source_title: "Running the Demo"
tags:
  - appdev
  - quickstart
  - running-the-demo
---

# Running the Demo

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Running the Demo

> Start the Canton Network QuickStart demo and walk through the licensing workflow

# Explore the Canton Network Application Quickstart demo

## Business case

The Canton Network (CN) Quickstart is scaffolding to support development efforts to build, test, and deploy CN applications. It resolves infrastructure problems that every CN application must solve. Use the CN Quickstart Application so you and your team can focus on building your application, instead of build systems, deployment configurations, and testing infrastructure.

### Core business operations

The Quickstart features a sample licensing app to demonstrate Canton development patterns. In the app, providers sell time-based access to their services. Users pay with Canton Coin (CC) and manage payments through a Canton Wallet.

The app involves four parties:

* The **Application Provider** who sells licenses.
* The **Application User** who buys licenses.
* The underlying **Amulet** token system that handles payments, using [CC](https://www.canton.network/blog/canton-coin-a-canton-network-native-payment-application).
* The **DSO Party**, the Decentralized Synchronizer Operations Party who operates the Amulet payment system. In CN, this is the Super Validators.

The application issues licenses using the following process:

#### Issuing a license

The provider creates a new license for an onboarded user. The license starts expired and needs to be renewed before use.

#### Requesting a license renewal

The provider creates a renewal request, generating a payment request for the user. A matching CC payment request is created on the ledger.

#### Paying for a license renewal

The user approves the payment through their Canton Wallet, which creates an accepted payment contract on the ledger.

#### Renewing the license

The provider processes the accepted payment and updates the license with a new expiration date.

## Overview

This section helps you become familiar with a Canton Network (CN) business operation within the CN App Quickstart. The App Quickstart application is intended to be extended by your team to meet your business needs. When you are familiar with the App Quickstart, review the technology choices and application design to determine what changes are needed. Technology and design decisions are ultimately up to you.

If you find errors, please contact your representative at Digital Asset.

## Prerequisites

Install the [CN App Quickstart](/appdev/quickstart/prerequisites) before beginning this demonstration.

## Walkthrough

The CN App Quickstart can run with or without authorization, based on your business needs. Toggle authorization with the `make setup` command in the `quickstart` subdirectory. `make setup` asks to enable Observability, OAUTH2, and specify a party hint. In this demo, we disable `TEST MODE`, use the default party hint, and show OAUTH2 as enabled and disabled. When OAUTH2 makes a difference, we display both paths, one after the other. You can follow your path and ignore the other. You may enable Observability, but it is not required for this demo.

**Choose your adventure:**

`make setup` **without** OAUTH2:

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/make-setup-noauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=1408916657066dfd2af2a46b8d3eb678" alt="Make setup no auth" width="711" height="185" data-path="images/docs_website/make-setup-noauth.png" />

`make setup` **with** OAUTH2:

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/make-setup-with-oauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=d9e3d88dd7c5285588b698b1ce54a40e" alt="Make setup with auth" width="703" height="184" data-path="images/docs_website/make-setup-with-oauth.png" />

### Build Quickstart

<iframe width="560" height="315" src="https://www.youtube.com/embed/xsuMDLED6gI" title="Build Quickstart" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Build and start App Quickstart:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   make build; make start

```

Open an incognito browser and navigate to:

app-provider.localhost:3000

Alternatively, in the terminal, from quickstart/ run:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make open-app-ui
```

<Note>
  Safari users may need to manually map the `app-provider` subdomain in `/etc/hosts`. Use the terminal command `sudo nano /etc/hosts` to add:

  `127.0.0.1       app-provider.localhost`

  This tells your system to resolve `app-provider.localhost` to your local machine. Then save and close the file. Restart Safari.
</Note>

### Login

**OAUTH2 disabled**

When OAUTH2 is **disabled**, the homepage presents a simple login field. Begin by logging in as the `AppProvider` by entering "app-provider" in the User field.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-noauth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d59ab8fc8fac6a24e0f7f9b080a865cd" alt="CN App Quickstart Login screen without Auth" width="1028" height="658" data-path="images/docs_website/01-login-app-qs-noauth.png" />

**OAUTH2 enabled**

When OAUTH2 is **enabled**, the homepage prompts to login with Keycloak's OAuth 2.0 portal:

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-auth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3e86e1e6eceb3ab42a0c54f69b011a6e" alt="CN App Quickstart Login screen with Auth" width="1074" height="720" data-path="images/docs_website/01-login-app-qs-auth.png" />

Make a mental note that `AppProvider`’s username is “app-provider” and the password is "abc123" (all lowercase).

Login with `app-provider` with keycloak.

Fill in the login credentials: username: app-provider, password: abc123

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/login-app-provider-view.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0ebbacbedf9bb9f6e86c27a3068b5d33" alt="AppProvider login screen" width="1214" height="966" data-path="images/docs_website/login-app-provider-view.png" />

### The App Installs Menu

Once you are logged in select **AppInstalls** in the menu.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/qs-demo-app-installs-view.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=4ceb4f09666c5dc802ee454ba0ba9b47" alt="App Installs view" width="1204" height="274" data-path="images/docs_website/qs-demo-app-installs-view.png" />

Open a terminal to create an app install request.

From `/quickstart/` run:

make create-app-install-request

This command creates an App Installation Request on behalf of the Participant.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/04-create-install-req.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=26967c3281af1c82122ec6ef2b9b6869" alt="App Install Request" width="865" height="666" data-path="images/docs_website/04-create-install-req.png" />

<Note>
  If your machine is not powerful enough to host `LocalNet` or if the docker containers are not responsive then the response may show a failure with status code 404 or 000 (as shown in the image below). Increasing Docker memory limit to at least 8 GB should allow the `LocalNet` containers to operate properly.
</Note>

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/05-error-app-install.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=f69a71143e15df482c1577bac0adf83e" alt="App Install Request error" width="855" height="198" data-path="images/docs_website/05-error-app-install.png" />

Return to the browser.

### AppInstallRequest

The install request appears in the list.

Click **Accept**.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/accept-awaiting-request.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9343412c86851e6732bb53842df08640" alt="accept request" width="2786" height="640" data-path="images/docs_website/accept-awaiting-request.png" />

The `AppInstallRequest` is Accepted.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/success-accepted-appinstallrequest.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=b9e1db88000687ae2729bcb430ed70e6" alt="accepted request" width="788" height="428" data-path="images/docs_website/success-accepted-appinstallrequest.png" />

The actions update to Cancel and Create license.

### Create a license

Click **Create License**. The license is created and the “# Licenses” field is updated.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/created-license.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=35f926610b07bc1fef45d0be2d4ee4dc" alt="create license" width="2784" height="616" data-path="images/docs_website/created-license.png" />

Next, navigate to the Licenses menu and select **Renewals**.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/new-license-select-renewals.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=95ec9e7abab4f3b476744338bec788c2" alt="Licenses view" width="2776" height="528" data-path="images/docs_website/new-license-select-renewals.png" />

A "License Renewal Request” modal opens with an option to renew a license.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/license-renewal-request-modal.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=d886889cfb347fbfa47f6d99ab0ff5a9" alt="license renewal request modal" width="2518" height="744" data-path="images/docs_website/license-renewal-request-modal.png" />

Click **New** to open the "Renew License" modal.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/renew-license-modal.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=29534a7fc893b80cded1f139b76e48f3" alt="renew license modal" width="2300" height="1018" data-path="images/docs_website/renew-license-modal.png" />

In the modal, set the number of days to renew the license, the fee, time to prepare the license, and time to settle the license. You must add a description to proceed.

"Prepare in" is an indication for the sender (app-user) that they are expected to accept allocation before that time. "Settle in" is a time that the provider has to `completeRenewal`. After that, the allocation will be expired.

Click **Issue License Renewal Request**.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/new-license-renewal-request.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=265a21249aa5bf1a08da03a16d6a45a5" alt="new license renewal request" width="2573" height="1226" data-path="images/docs_website/new-license-renewal-request.png" />

Per the Daml contract, licenses are created in an expired state. To activate the license, a renewal payment request must be issued.

### Make a payment

To make payment, navigate to the Canton Wallet at [http://wallet.localhost:2000/allocations](http://wallet.localhost:2000/allocations) and log in as `app-user` if prompted.

You can find the wallet's location by:

1. Reading the [LocalNet Application UIs reference](/sdks-tools/development-tools/localnet#application-uis).
2. Navigating to the App Provider's "Tenants" menu.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider-tenants.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=977310daf3ed1412cc3486604d2af9db" alt="AppProvider Tenants menu" width="2576" height="1036" data-path="images/docs_website/app-provider-tenants.png" />

3. Logging into the app as `app-user`, navigating to the Licenses menu, then clicking the **Renewals** action.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user-licenses-menu.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=169fcbca3a2c61ed799c28818cb1773d" alt="AppUser Licenses menu" width="2056" height="845" data-path="images/docs_website/app-user-licenses-menu.png" />

If prompted, log in to the CC Wallet as `app-user`.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-app-user-log-in.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=590880b15dfa7537790f4057342d7cbd" alt="Canton Coin Wallet login" width="541" height="297" data-path="images/docs_website/canton-coin-wallet-app-user-log-in.png" />

If your wallet does not have CC then enter an amount and click **TAP**. After a moment, the available balance will automatically update.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/tap-canton-wallet.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=245af052dabbfd2e8cd7de3c58857cbb" alt="Tap for CC" width="1441" height="793" data-path="images/docs_website/tap-canton-wallet.png" />

Once your CC wallet is loaded, navigate to the "Allocations" menu and accept the "Allocation Request" before the "Allocate before" time expires.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-allocations-menu.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=6d98ac7d9e67b87babc946dc0928f7b0" alt="CC Wallet accept allocation" width="1582" height="975" data-path="images/docs_website/canton-coin-wallet-allocations-menu.png" />

If the allocation request is accepted, a new "Allocations" section appears. This section shows the `licenseFeePayment` information.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-accepted-allocation.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=0305dabc187ee90a1a7c7c6b09cda92a" alt="CC Wallet accepted allocation" width="1179" height="537" data-path="images/docs_website/canton-coin-wallet-accepted-allocation.png" />

### Renew the license

Return to the Quickstart as the `AppProvider`. In the Licenses menu, select **Renewals**. This opens the License Renewals Request modal. Click the green **Complete Renewal** button.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider-complete-renewal-after-payment.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c324401b73bb9ee2cbd66c6a158d27c8" alt="complete renewal after payment" width="2542" height="954" data-path="images/docs_website/app-provider-complete-renewal-after-payment.png" />

A confirmation appears that the license renewal completed successfully.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/license-renewal-completed-successfully.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=f668dae8d5b6df522fed0a9f25777749" alt="renewal success after payment" width="866" height="236" data-path="images/docs_website/license-renewal-completed-successfully.png" />

Log out from the `AppProvider` and log in as `AppUser`.

**OAUTH2 disabled**

If OAUTH2 is disabled, simply log in as `app-user`.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/login-app-user-noauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0066a63f9fea2644e82cf1c089f81434" alt="AppUser login screen without Auth" width="700" height="358" data-path="images/docs_website/login-app-user-noauth.png" />

**OAUTH2 enabled**

When OAUTH2 is enabled, you log in using the app-user username and password.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-auth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3e86e1e6eceb3ab42a0c54f69b011a6e" alt="login screen" width="1074" height="720" data-path="images/docs_website/01-login-app-qs-auth.png" />

Login as `AppUser` with “app-user" as the username and the password is “abc123”.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/appuser-auth-login-view.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b312b838303aa6e9ec67bde4630dff8b" alt="AppUser login screen" width="1194" height="950" data-path="images/docs_website/appuser-auth-login-view.png" />

The AppInstall now shows as accepted.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/accepted-app-install.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c0f3be69a014c5946c9e0281ae6c02e4" alt="accepted AppInstall" width="1948" height="510" data-path="images/docs_website/accepted-app-install.png" />

The license shows as active.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user-license-active.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=2eba63df270f01f4f51adf922921d238" alt="logout AppProvider" width="2782" height="480" data-path="images/docs_website/app-user-license-active.png" />

Congratulations. You’ve successfully created and activated a license with a payment allocation in Canton wallet!

## Canton Console

<iframe width="560" height="315" src="https://www.youtube.com/embed/zADHja_8TSg" title="Canton Console" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

The Canton Console connects to the running application ledger. The console allows a developer to bypass the UI to interact with the CN in a more direct manner. For example, in Canton Console you can connect to the Participant to see the location of the Participant and their synchronizer domain.

Activate the Canton Console in a terminal from the `quickstart/` directory. Run:

make canton-console

After the console initiates, run the `participants` and `participants.all` commands, respectively.

participants

Returns a detailed categorization of participants.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-console-participants.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=8c3d1cea96249b903b88c0da306ec93d" alt="Participant location in the ledger" width="583" height="142" data-path="images/docs_website/canton-console-participants.png" />

participants.all

Shows a list of all participant references.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-console-participants-all.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=df883230ed833027274e2ceea8f4fc64" alt="Participant synchronizer" width="544" height="95" data-path="images/docs_website/canton-console-participants-all.png" />

On `LocalNet`, you can connect to any of the listed participants. Connect to the app user's validator with

`app-user`

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b01573fcbc32b72885075c33152069df" alt="App User" width="1446" height="92" data-path="images/docs_website/app-user.png" />

If you receive an error, double check that you used the backticks.

The app provider can be connected with:

`app-provider`

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=4a4bcd7454bf593f2f4c118b97552a87" alt="App Provider" width="1512" height="84" data-path="images/docs_website/app-provider.png" />

Connect to the Super Valdiator that is simulating the Global Synchronizer using:

`sv`

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/sv.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=43495c2192db25d7959eb0f0eac8b951" alt="super validator" width="1354" height="86" data-path="images/docs_website/sv.png" />

Canton Console also provides a diagnostic tool that displays the health of Canton Network validators:

health.status

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/health-status.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=51203c8b4855d2105fb450166523df9f" alt="Ping yourself" width="1458" height="1614" data-path="images/docs_website/health-status.png" />

## Daml Shell

<iframe width="560" height="315" src="https://www.youtube.com/embed/bwUyYEFCo5w" title="Daml Shell" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Daml Shell connects to the running PQS database of the application provider’s Participant. In the Shell, the assets and their details are available in real time.

Run the shell from quickstart/ in the terminal with:

make shell

Run the following commands to see the data:

active

Shows unique identifiers and the asset count:

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/28-shell-ids.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=7e70568b90c6973178010c24d3d092bf" alt="Active identifiers" width="1072" height="422" data-path="images/docs_website/28-shell-ids.png" />

active quickstart-licensing:Licensing.License:License

List the license details.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/29-license-details.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=96fcfbcf24fefeed145f2b0204786703" alt="License details" width="2004" height="424" data-path="images/docs_website/29-license-details.png" />

active quickstart-licensing:Licensing.License:LicenseRenewalRequest

Displays license renewal request details.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/active-quickstart-appinstallrequest.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3b2865a66adc42d69afd314bac8df094" alt="License renewal request details" width="1476" height="564" data-path="images/docs_website/active-quickstart-appinstallrequest.png" />

archives quickstart-licensing:Licensing.AppInstall:AppInstallRequest

Shows any archived license(s).

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/30-archive-licenses.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=150ef56808c53ccf89334ef49c426e3b" alt="Archived licenses" width="2048" height="306" data-path="images/docs_website/30-archive-licenses.png" />

## Canton Coin Scan

Explore the CC Scan Web UI at [http://scan.localhost:4000/](http://scan.localhost:4000/).

The default activity view shows the total CC balance and the Validator rewards.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/36-cc-balance.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baef92a8fb40484bbd32259f47bee3" alt="CC balance" width="1762" height="1250" data-path="images/docs_website/36-cc-balance.png" />

Select the **Network Info** menu to view SV identification.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/34-active-svs.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baeac098a8ffb96118ad7bd82289dd" alt="Active SVs" width="1690" height="763" data-path="images/docs_website/34-active-svs.png" />

The Validators menu shows that the local validator has been registered with the SV.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/37-registered-validator.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=18513ea59e63c153cdb7efc7d7ed9111" alt="Registered validator" width="1764" height="896" data-path="images/docs_website/37-registered-validator.png" />

## Observability Dashboard

<Note>
  Observability may no longer work while App Quickstart is under revisions.
</Note>

In a web browser, navigate to [http://localhost:3030/dashboards](http://localhost:3030/dashboards) to view the observability dashboards. Select **Quickstart - consolidated logs**.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/38-obs-dash.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d2a79818718bd41e4efad50afdc757ea" alt="observability dashboard" width="1568" height="548" data-path="images/docs_website/38-obs-dash.png" />

The default view shows a running stream of all services.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/39-service-stream.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=342cbdb1ea90bceed4b57c9c49941a0b" alt="service stream" width="1988" height="875" data-path="images/docs_website/39-service-stream.png" />

Change the services filter from “All” to “participant” to view participant logs. Select any log entry to view its details.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/40-log-entry-details.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b40da7d84eb5760da8d9b21866333f6a" alt="log entry details" width="1394" height="740" data-path="images/docs_website/40-log-entry-details.png" />

## SV UIs

Navigate to [http://sv.localhost:4000/](http://sv.localhost:4000/) for the SV Web UI. The SV view displays data directly from the validator in a GUI that is straightforward to navigate.

Login as ‘sv’.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/33-sv-ui-login.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=56f28dbeeb635a41a95fafae9a745bc7" alt="SV UI login" width="1086" height="644" data-path="images/docs_website/33-sv-ui-login.png" />

The UI shows information about the SV and lists the active SVs.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/34-active-svs.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baeac098a8ffb96118ad7bd82289dd" alt="Active SVs" width="1690" height="763" data-path="images/docs_website/34-active-svs.png" />

The Validator Onboarding menu allows for the creation of validator onboarding secrets.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/35-validator-onboarding.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=f1d1f3f9f901d215d3c33f1bb1a09d50" alt="Validator onboarding" width="2048" height="1169" data-path="images/docs_website/35-validator-onboarding.png" />

## Next steps

You've completed a business operation in the CN App Quickstart and have been introduced to the basics of the Canton Console and Daml Shell. We encourage you to explore the CN App Quickstart codebase and modify it to meet your business needs. You might be interested in learning more about the [App Quickstart project structure](/appdev/quickstart/project-structure) or the application development modules in [Module 4: Building Applications](/appdev/modules/m4-building-apps-intro).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
