> Finding and using Canton Network wallets

A 钱包 is your gateway to Canton Network—it lets you manage Canton Coin（CC）, interact with 应用, and track your activity.

## What is a Canton 钱包?

A Canton 钱包 allows you to:

| 职能               | 说明                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hold Canton Coin（CC）**   | Store and manage your CC 余额                                                                                                                      |
| **Hold other tokens**  | Hold any [CIP-0056](https://github.com/global-同步器-foundation/cips/blob/main/cip-0056/cip-0056.md) compliant token (support varies by 钱包) |
| **转账 value**     | Send CC to other Party                                                                                                                              |
| **Interact with apps** | 连接 to Canton Network 应用                                                                                                                |
| **View activity**      | See your 交易 history                                                                                                                          |

## Finding a 钱包

### Splice 钱包 (Reference Implementation)

The Splice project provides a reference 钱包 implementation:

* **类型**: Web-based 钱包
* **Access**: Through validator or 应用 interfaces
* **Features**: Core 钱包 functionality

<Note>
  The Splice reference 钱包 is not yet [CIP-0056](https://github.com/global-同步器-foundation/cips/blob/main/cip-0056/cip-0056.md) compliant. Support for the token standard is planned for a future release.
</Note>

### 验证者-Provided Wallets

Some validators offer 钱包 interfaces as part of their 服务. 检查 with your validator or 应用 提供方.

### 应用-Integrated Wallets

Many Canton 应用 include 钱包 functionality:

* Built into the 应用 interface
* Seamless experience within the app
* May have 应用-specific features

## 钱包 Basics

### Your 余额

Your 钱包 展示 your Canton Coin（CC） 余额. Wallets may also display other tokens that follow the [CIP-0056](https://github.com/global-同步器-foundation/cips/blob/main/cip-0056/cip-0056.md) token standard—check your specific 钱包 for supported assets. Unlike other cryptocurrencies:

* Only you can see your 余额
* Others cannot query your 持仓
* Your 交易 are private

### Transfers

To send CC to another party:

1. Enter the recipient's party identifier
2. Specify the amount
3. Confirm the transfer
4. 交易 completes (typically within seconds)

### 交易 History

View your past 交易:

* Transfers sent and received
* 流量 fees paid
* 应用 interactions

<Note>
  你可以 only see 交易 where you were a 参与者. There's no public ledger of all 交易.
</Note>

## Security

### Protecting Your 钱包

| Practice               | 说明                                  |
| ---------------------- | -------------------------------------------- |
| **Secure access**      | Use strong 认证                    |
| **验证 Party**     | Confirm recipient identifiers before sending |
| **Trusted validators** | Use wallets from reputable sources           |

### Understanding the Trust Model

Your 钱包 connects to a validator that:

* Hosts your party
* Stores your 合约 data
* Processes your 交易

Choose your validator carefully—they have visibility into your operations.

## Differences from Other Crypto Wallets

| Aspect                  | Traditional Crypto     | Canton                       |
| ----------------------- | ---------------------- | ---------------------------- |
| **余额 visibility**  | Public                 | Private                      |
| **交易 history** | Public                 | Private                      |
| **Address format**      | Hex address            | Party identifier             |
| **网络 explorer**    | Shows all 交易 | Shows only your 交易 |

## Getting Started

### On DevNet/TestNet

1. Access a 钱包 interface (through your validator or 应用)
2. 创建 or import your party
3. Use the faucet ("tap") to receive test CC
4. 启动 transacting

### On MainNet

1. 连接 to a 钱包 through your validator or 应用
2. Obtain CC through:
   * Exchange purchase
   * 转账 from another party
   * 网络 activity 奖励

## Common Tasks

### Checking Your 余额

Open your 钱包 interface to see your current CC 余额.

### Sending CC

1. Navigate to "Send" or "转账"
2. Enter the recipient party
3. Enter the amount
4. Review and confirm

### Receiving CC

1. Share your party identifier with the sender
2. CC appears in your 余额 after confirmation

### Topping Up 流量

若你're running an 应用 that needs 流量:

1. Navigate to 流量 management
2. Initiate a top-up
3. CC is converted to 流量 credits

## Troubleshooting

| Issue             | Solution                                                |
| ----------------- | ------------------------------------------------------- |
| 余额 展示 0   | 确保 钱包 is connected to correct validator         |
| 转账 failed   | 检查 recipient party format; ensure sufficient 余额 |
| Slow confirmation | 网络 may be busy; wait a few moments                 |
| Can't connect     | 检查 网络 connectivity; verify validator status     |

## 下一步

<CardGroup cols={2}>
  <Card title="How Canton Wallets Differ" icon="code-compare" href="/集成/wallets/canton-vs-web3">
    Understand the technical differences.
  </Card>

  <Card title="Find Apps" icon="grid-2" href="/集成/apps/finding-apps">
    Discover Canton Network 应用.
  </Card>
</CardGroup>

