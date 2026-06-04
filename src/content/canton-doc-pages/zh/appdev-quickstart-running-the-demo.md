---
title: "运行演示"
slug: "appdev-quickstart-running-the-demo"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/running-the-demo.md"
source_title: "Running the Demo"
tags:
  - appdev
  - quickstart
  - running-the-demo
---

# 运行演示

> 启动 Canton Network QuickStart 演示并走通许可工作流。

# 运行演示

# 运行演示

# Explore the Canton Network Application Quickstart demo

## 业务场景

CN Quickstart 是构建、测试与部署 CN 应用的脚手架，解决每个 CN 应用都需处理的基础设施问题，让团队专注业务而非构建系统、部署与测试基础设施。

### 核心业务操作

Quickstart 以示例许可应用演示 Canton 开发模式：提供方销售基于时间的服务访问，用户用 Canton Coin（CC）并通过 Canton 钱包管理支付。

The app involves four parties:

* **应用提供方**销售许可。
* **应用用户**购买许可。
* 底层 **Amulet** 代币系统处理支付，使用 [CC](https://www.canton.network/blog/canton-coin-a-canton-network-native-payment-application)。
* **DSO Party**（去中心化 Synchronizer 运营方）运营 Amulet 支付系统；在 CN 中为 Super Validator。

The application issues licenses using the following process:

#### 签发许可

提供方为已入驻用户创建新许可；许可初始为过期，使用前须续期。

#### 请求许可续期

提供方创建续期请求并为用户生成付款请求；账本上创建匹配的 CC 付款请求。

#### 支付许可续期

用户通过 Canton 钱包批准付款，在账本创建已接受付款合约。

#### 续期许可

提供方处理已接受付款并更新许可过期日。

## 概览

本节帮助你在 CN App Quickstart 中熟悉一次 CN 业务操作。应用可由团队扩展；熟悉后请审视技术选型与设计。技术与设计决策由你决定。

发现错误请联系 Digital Asset 代表。

## 前置条件

演示前请先完成 [CN App Quickstart 安装](/zh/docs/canton/appdev-quickstart-prerequisites)。

## 演练

CN App Quickstart 可按需启用授权；在 `quickstart` 子目录用 `make setup` 切换。演示关闭 `TEST MODE`、使用默认 party hint，并分别展示启用/未启用 OAUTH2 的路径，任选其一即可。Observability 可选。

**选择你的路径：**

`make setup` **未启用** OAUTH2：

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/make-setup-noauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=1408916657066dfd2af2a46b8d3eb678" alt="Make setup no auth" width="711" height="185" data-path="images/docs_website/make-setup-noauth.png" />

`make setup` **启用** OAUTH2：

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/make-setup-with-oauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=d9e3d88dd7c5285588b698b1ce54a40e" alt="Make setup with auth" width="703" height="184" data-path="images/docs_website/make-setup-with-oauth.png" />

### 构建 Quickstart

<iframe width="560" height="315" src="https://www.youtube.com/embed/xsuMDLED6gI" title="Build Quickstart" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

构建并启动 App Quickstart：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   make build; make start

```

用无痕浏览器打开：

app-provider.localhost:3000

或在 quickstart/ 终端运行：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make open-app-ui
```

<Note>
  Safari 用户可能须在 `/etc/hosts` 手动映射 `app-provider` 子域：`sudo nano /etc/hosts` 添加：

  `127.0.0.1       app-provider.localhost`

  使系统将 `app-provider.localhost` 解析到本机，保存后重启 Safari。
</Note>

### 登录

**未启用 OAUTH2**

未启用 OAUTH2 时，首页为简单登录框；在 User 字段输入 "app-provider" 以 `AppProvider` 登录。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-noauth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d59ab8fc8fac6a24e0f7f9b080a865cd" alt="CN App Quickstart Login screen without Auth" width="1028" height="658" data-path="images/docs_website/01-login-app-qs-noauth.png" />

**已启用 OAUTH2**

启用 OAUTH2 时，首页通过 Keycloak OAuth 2.0 门户登录：

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-auth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3e86e1e6eceb3ab42a0c54f69b011a6e" alt="CN App Quickstart Login screen with Auth" width="1074" height="720" data-path="images/docs_website/01-login-app-qs-auth.png" />

请记住 `AppProvider` 用户名为 app-provider，密码为 abc123（全小写）。

在 Keycloak 以 app-provider 登录。

凭据：用户名 app-provider，密码 abc123

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/login-app-provider-view.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0ebbacbedf9bb9f6e86c27a3068b5d33" alt="AppProvider login screen" width="1214" height="966" data-path="images/docs_website/login-app-provider-view.png" />

### 应用安装菜单

登录后选择菜单 **AppInstalls**。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/qs-demo-app-installs-view.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=4ceb4f09666c5dc802ee454ba0ba9b47" alt="App Installs view" width="1204" height="274" data-path="images/docs_website/qs-demo-app-installs-view.png" />

打开终端创建应用安装请求。

在 `/quickstart/` 运行：

make create-app-install-request

该命令代表 Participant 创建应用安装请求。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/04-create-install-req.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=26967c3281af1c82122ec6ef2b9b6869" alt="App Install Request" width="865" height="666" data-path="images/docs_website/04-create-install-req.png" />

<Note>
  若机器不足以运行 `LocalNet` 或容器无响应，可能返回 404/000；将 Docker 内存增至至少 8 GB 通常可恢复。
</Note>

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/05-error-app-install.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=f69a71143e15df482c1577bac0adf83e" alt="App Install Request error" width="855" height="198" data-path="images/docs_website/05-error-app-install.png" />

回到浏览器。

### AppInstallRequest

安装请求出现在列表中。

点击 **Accept**。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/accept-awaiting-request.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9343412c86851e6732bb53842df08640" alt="accept request" width="2786" height="640" data-path="images/docs_website/accept-awaiting-request.png" />

`AppInstallRequest` 已接受。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/success-accepted-appinstallrequest.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=b9e1db88000687ae2729bcb430ed70e6" alt="accepted request" width="788" height="428" data-path="images/docs_website/success-accepted-appinstallrequest.png" />

操作更新为 Cancel 与 Create license。

### 创建许可

点击 **Create License**；许可已创建，“# Licenses” 字段更新。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/created-license.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=35f926610b07bc1fef45d0be2d4ee4dc" alt="create license" width="2784" height="616" data-path="images/docs_website/created-license.png" />

进入 Licenses 菜单选择 **Renewals**。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/new-license-select-renewals.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=95ec9e7abab4f3b476744338bec788c2" alt="Licenses view" width="2776" height="528" data-path="images/docs_website/new-license-select-renewals.png" />

打开「License Renewal Request」模态框。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/license-renewal-request-modal.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=d886889cfb347fbfa47f6d99ab0ff5a9" alt="license renewal request modal" width="2518" height="744" data-path="images/docs_website/license-renewal-request-modal.png" />

点击 **New** 打开 Renew License 模态框。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/renew-license-modal.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=29534a7fc893b80cded1f139b76e48f3" alt="renew license modal" width="2300" height="1018" data-path="images/docs_website/renew-license-modal.png" />

在模态框设置续期天数、费用、准备时间与结算时间；须填写描述。

「Prepare in」提示 app-user 须在此前接受分配；「Settle in」为提供方完成 `completeRenewal` 的期限，逾期分配失效。

点击 **Issue License Renewal Request**。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/new-license-renewal-request.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=265a21249aa5bf1a08da03a16d6a45a5" alt="new license renewal request" width="2573" height="1226" data-path="images/docs_website/new-license-renewal-request.png" />

按 Daml 合约，许可创建时为过期；须发出续期付款请求以激活。

### 付款

付款请打开 [Canton 钱包](http://wallet.localhost:2000/allocations)，按需以 `app-user` 登录。

查找钱包位置：

1. 阅读 [LocalNet 应用 UI 参考](/zh/docs/canton/appdev-modules-m5-localnet-development#application-uis)。
2. 进入应用提供方「Tenants」菜单。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider-tenants.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=977310daf3ed1412cc3486604d2af9db" alt="AppProvider Tenants menu" width="2576" height="1036" data-path="images/docs_website/app-provider-tenants.png" />

3. 以 `app-user` 登录应用，在 Licenses 菜单点击 **Renewals**。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user-licenses-menu.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=169fcbca3a2c61ed799c28818cb1773d" alt="AppUser Licenses menu" width="2056" height="845" data-path="images/docs_website/app-user-licenses-menu.png" />

若提示，以 `app-user` 登录 CC 钱包。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-app-user-log-in.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=590880b15dfa7537790f4057342d7cbd" alt="Canton Coin Wallet login" width="541" height="297" data-path="images/docs_website/canton-coin-wallet-app-user-log-in.png" />

若钱包无 CC，输入金额并点击 **TAP**；余额将自动更新。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/tap-canton-wallet.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=245af052dabbfd2e8cd7de3c58857cbb" alt="Tap for CC" width="1441" height="793" data-path="images/docs_website/tap-canton-wallet.png" />

钱包有余额后，在 Allocations 菜单于「Allocate before」前接受 Allocation Request。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-allocations-menu.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=6d98ac7d9e67b87babc946dc0928f7b0" alt="CC Wallet accept allocation" width="1582" height="975" data-path="images/docs_website/canton-coin-wallet-allocations-menu.png" />

接受后会出现 Allocations 区，显示 `licenseFeePayment` 信息。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-coin-wallet-accepted-allocation.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=0305dabc187ee90a1a7c7c6b09cda92a" alt="CC Wallet accepted allocation" width="1179" height="537" data-path="images/docs_website/canton-coin-wallet-accepted-allocation.png" />

### 续期许可

以 `AppProvider` 回到 Quickstart，在 Licenses 选择 **Renewals**，点击绿色 **Complete Renewal**。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider-complete-renewal-after-payment.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c324401b73bb9ee2cbd66c6a158d27c8" alt="complete renewal after payment" width="2542" height="954" data-path="images/docs_website/app-provider-complete-renewal-after-payment.png" />

出现许可续期成功确认。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/license-renewal-completed-successfully.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=f668dae8d5b6df522fed0a9f25777749" alt="renewal success after payment" width="866" height="236" data-path="images/docs_website/license-renewal-completed-successfully.png" />

退出 `AppProvider` 并以 `AppUser` 登录。

**未启用 OAUTH2**

未启用 OAUTH2 时直接以 app-user 登录。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/login-app-user-noauth.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0066a63f9fea2644e82cf1c089f81434" alt="AppUser login screen without Auth" width="700" height="358" data-path="images/docs_website/login-app-user-noauth.png" />

**已启用 OAUTH2**

启用 OAUTH2 时用 app-user 用户名与密码登录。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/01-login-app-qs-auth.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3e86e1e6eceb3ab42a0c54f69b011a6e" alt="login screen" width="1074" height="720" data-path="images/docs_website/01-login-app-qs-auth.png" />

Login as `AppUser` with “app-user" as the username and the password is “abc123”.

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/appuser-auth-login-view.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b312b838303aa6e9ec67bde4630dff8b" alt="AppUser login screen" width="1194" height="950" data-path="images/docs_website/appuser-auth-login-view.png" />

AppInstall 显示为已接受。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/accepted-app-install.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c0f3be69a014c5946c9e0281ae6c02e4" alt="accepted AppInstall" width="1948" height="510" data-path="images/docs_website/accepted-app-install.png" />

许可显示为 active。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user-license-active.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=2eba63df270f01f4f51adf922921d238" alt="logout AppProvider" width="2782" height="480" data-path="images/docs_website/app-user-license-active.png" />

恭喜！你已在 Canton 钱包中完成许可创建、付款分配与激活！

## Canton Console

<iframe width="560" height="315" src="https://www.youtube.com/embed/zADHja_8TSg" title="Canton Console" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Canton Console 连接运行中的应用账本，可绕过 UI 直接交互，例如查看 Participant 位置与 synchronizer 域。

在 `quickstart/` 运行：

make canton-console

启动后分别运行 `participants` 与 `participants.all`。

participants

返回 participant 详细分类。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-console-participants.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=8c3d1cea96249b903b88c0da306ec93d" alt="Participant location in the ledger" width="583" height="142" data-path="images/docs_website/canton-console-participants.png" />

participants.all

列出所有 participant 引用。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/canton-console-participants-all.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=df883230ed833027274e2ceea8f4fc64" alt="Participant synchronizer" width="544" height="95" data-path="images/docs_website/canton-console-participants-all.png" />

在 `LocalNet` 可连接任一列出的 participant。连接 app user 验证者：

`app-user`

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-user.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b01573fcbc32b72885075c33152069df" alt="App User" width="1446" height="92" data-path="images/docs_website/app-user.png" />

若报错请确认使用了反引号。

连接 app provider：

`app-provider`

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/app-provider.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=4a4bcd7454bf593f2f4c118b97552a87" alt="App Provider" width="1512" height="84" data-path="images/docs_website/app-provider.png" />

连接模拟 Global Synchronizer 的超级验证者：

`sv`

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/sv.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=43495c2192db25d7959eb0f0eac8b951" alt="super validator" width="1354" height="86" data-path="images/docs_website/sv.png" />

Canton Console 还提供验证者健康诊断：

health.status

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/health-status.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=51203c8b4855d2105fb450166523df9f" alt="Ping yourself" width="1458" height="1614" data-path="images/docs_website/health-status.png" />

## Daml Shell

<iframe width="560" height="315" src="https://www.youtube.com/embed/bwUyYEFCo5w" title="Daml Shell" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Daml Shell 连接应用提供方 Participant 的 PQS；可实时查看资产与详情。

在 quickstart/ 运行：

make shell

运行下列命令查看数据：

active

显示唯一标识与资产数量：

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/28-shell-ids.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=7e70568b90c6973178010c24d3d092bf" alt="Active identifiers" width="1072" height="422" data-path="images/docs_website/28-shell-ids.png" />

active quickstart-licensing:Licensing.License:License

列出许可详情。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/29-license-details.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=96fcfbcf24fefeed145f2b0204786703" alt="License details" width="2004" height="424" data-path="images/docs_website/29-license-details.png" />

active quickstart-licensing:Licensing.License:LicenseRenewalRequest

显示许可续期请求详情。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/active-quickstart-appinstallrequest.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3b2865a66adc42d69afd314bac8df094" alt="License renewal request details" width="1476" height="564" data-path="images/docs_website/active-quickstart-appinstallrequest.png" />

archives quickstart-licensing:Licensing.AppInstall:AppInstallRequest

显示已归档许可。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/30-archive-licenses.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=150ef56808c53ccf89334ef49c426e3b" alt="Archived licenses" width="2048" height="306" data-path="images/docs_website/30-archive-licenses.png" />

## Canton Coin Scan

在 [http://scan.localhost:4000/](http://scan.localhost:4000/) 打开 CC Scan。

默认活动视图显示 CC 总余额与验证者奖励。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/36-cc-balance.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baef92a8fb40484bbd32259f47bee3" alt="CC balance" width="1762" height="1250" data-path="images/docs_website/36-cc-balance.png" />

选择 **Network Info** 查看 SV 标识。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/34-active-svs.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baeac098a8ffb96118ad7bd82289dd" alt="Active SVs" width="1690" height="763" data-path="images/docs_website/34-active-svs.png" />

Validators 菜单显示本地验证者已向 SV 注册。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/37-registered-validator.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=18513ea59e63c153cdb7efc7d7ed9111" alt="Registered validator" width="1764" height="896" data-path="images/docs_website/37-registered-validator.png" />

## 可观测性仪表板

<Note>
  App Quickstart 修订期间 Observability 可能不可用。
</Note>

浏览器打开 [http://localhost:3030/dashboards](http://localhost:3030/dashboards)，选择 **Quickstart - consolidated logs**。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/38-obs-dash.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=d2a79818718bd41e4efad50afdc757ea" alt="observability dashboard" width="1568" height="548" data-path="images/docs_website/38-obs-dash.png" />

默认视图显示所有服务日志流。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/39-service-stream.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=342cbdb1ea90bceed4b57c9c49941a0b" alt="service stream" width="1988" height="875" data-path="images/docs_website/39-service-stream.png" />

将服务过滤从 All 改为 participant；点击条目查看详情。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/40-log-entry-details.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b40da7d84eb5760da8d9b21866333f6a" alt="log entry details" width="1394" height="740" data-path="images/docs_website/40-log-entry-details.png" />

## SV UI

SV Web UI：[http://sv.localhost:4000/](http://sv.localhost:4000/)，数据直接来自验证者。

以 sv 登录。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/33-sv-ui-login.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=56f28dbeeb635a41a95fafae9a745bc7" alt="SV UI login" width="1086" height="644" data-path="images/docs_website/33-sv-ui-login.png" />

UI 显示 SV 信息与活跃 SV 列表。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/34-active-svs.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=93baeac098a8ffb96118ad7bd82289dd" alt="Active SVs" width="1690" height="763" data-path="images/docs_website/34-active-svs.png" />

Validator Onboarding 菜单可创建验证者 onboarding secret。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/35-validator-onboarding.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=f1d1f3f9f901d215d3c33f1bb1a09d50" alt="Validator onboarding" width="2048" height="1169" data-path="images/docs_website/35-validator-onboarding.png" />

## 下一步

你已完成 CN App Quickstart 中的一次业务操作，并初步了解 Canton Console 与 Daml Shell。建议探索代码库并按业务修改；可继续阅读[项目结构](/zh/docs/canton/appdev-quickstart-project-structure)或[模块 4：构建应用](/zh/docs/canton/appdev-modules-m4-building-apps-intro)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
