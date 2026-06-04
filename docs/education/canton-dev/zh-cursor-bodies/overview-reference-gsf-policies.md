> Global Synchronizer Foundation 政策与治理框架

[Global Synchronizer Foundation](https://canton.foundation) (GSF) 是与 Linux Foundation 合作成立的独立非营利组织，治理 Canton Network 的去中心化互操作与同步基础设施 Global Synchronizer。

## 宗旨与角色

GSF 对 Global Synchronizer 提供透明治理并推动其生态发展。职责包括：

* 定义并维护 Global Synchronizer 治理框架
* 公开 Super Validator 运营与治理投票
* 运营 Super Validator 节点并代表成员参与治理
* 在 Super Validator 集合间协调升级时间表与网络政策
* 通过外联、开发者计划与 Protocol Development Fund 支持生态发展

GSF 不单方面控制网络。治理决策须通过链上投票在 Super Validator 间达成共识。GSF 作为众多 Super Validator 之一参与投票。

## 会员

GSF 提供三档会员：

* **Premier**（\$150,000/年）— 董事会席位、董事会委员会代表、战略日参与及营销材料优先展示
* **General**（\$5,000–\$30,000/年，按组织规模）— 参与 Member Committees 与博客发布
* **Associate**（免费）— 限政府机构、监管机关、非营利与学术机构；须董事会批准

任何成员可加入 Member Committees。申请见 [GSF membership page](https://canton.foundation/membership)。

## Member Committees

GSF 通过六个 Member Committees 组织治理与运营工作：

* **Tech and Operations** — 技术方向与运营标准
* **Tokenomics** — Canton Coin 经济、费用校准与奖励参数
* **Accountability** — 监督与合规
* **Marketing** — 生态外联与传播
* **Legal** — 法律框架与监管事项
* **Audit and Finance** — 财务监督

Premier 成员还可接触 Board Committees 并委派代表。

## 治理框架

Global Synchronizer 由称为 Super Validator 的独立组织运营，运行核心基础设施——Sequencer、Mediator 与 SV 应用节点——并通过链上治理应用参与治理。

治理行动通过 DSO（Decentralized Synchronizer Operations）party 执行，该去中心化 Daml party 的确认阈值约为已入驻 Super Validator 的 2/3。无单一实体（含 GSF）可单方面变更。DSO party、确认协议与投票机制详见 [SV Governance Reference](/overview/reference/sv-governance-reference)。

治理框架涵盖：

* **网络配置** — 流量定价、费用表、代币经济学配置等参数
* **Super Validator 成员** — Super Validator 入驻与退出
* **软件升级** — Canton 与 Splice 版本升级协调
* **Daml 包升级** — 链上治理与代币经济学包升级管理
* **Canton Improvement Proposals (CIPs)** — 提议与批准网络规则与标准的结构化流程

## 网络政策

### 验证者入驻

验证者须获准方可加入 TestNet 或 MainNet：

1. 通过 [GSF validator request form](https://sync.global/validator-request/) 提交请求。
2. Tokenomics Committee 审查并批准。
3. 赞助 Super Validator 将你的出口 IP 加入 SV 集合维护的 allowlist。每网络仅允许一个 IP，且 DevNet、TestNet、MainNet 须各不相同。
4. 多数 Super Validator 采用更新 allowlist 后（通常 2–7 天），你从赞助 SV 获得一次性 onboarding secret（48 小时有效）。
5. 使用该 secret 部署验证者节点。

DevNet 对任何验证者开放，无需 Tokenomics Committee 批准，但 IP 仍须加入 allowlist。

### 流量与费用政策

Super Validator 通过治理投票共同设定流量定价。`extraTrafficPrice` 参数决定 synchronizer 写流量成本，校准使标准 Canton Coin 转账约 1 USD（见 [CIP-0042](https://github.com/canton-foundation/cips/blob/main/cip-0042/cip-0042.pdf)）。Super Validator 应定期测量实际流量成本并调整参数。

费用参数通过链上中位数投票更新：各 SV 发布偏好值，系统取中位数，避免单一 SV 大幅移动参数。

### 参与要求

Super Validator 须满足运营要求：

* 运行所需基础设施（Sequencer、Mediator、SV 应用）
* 保持在线与连通以支持 BFT 共识
* 参与治理投票与升级协调
* 满足 CometBFT 验证者共识参与要求

Global Synchronizer 使用的 CometBFT 要求超过 2/3 Super Validator 在线网络才能推进；任一 Super Validator 故障都会缩小容错余量。

### 奖励政策

Super Validator 因运营基础设施获得奖励，由 reward weight 参数配置。变更 reward weight 流程：

1. Super Validator 所有者商定新权重。
2. 通过 SV Web UI 发起治理投票。
3. 须获 Super Validator 法定人数批准。
4. 更新反映于 [GSF configs repository](https://github.com/global-synchronizer-foundation/configs) 以保证入驻一致。

## 升级协调

网络升级——Canton、Splice 或 Daml 包——须全体 Super Validator 协调。GSF 通过以下方式促进：

* 向所有运营方传达升级时间与要求
* 跟踪 Super Validator 集合就绪情况
* 提供特定升级程序操作指南（如 Daml 升级期间暂停 trigger）

未及时升级的 Super Validator 可能引发运营问题。例如 Daml 包升级期间，运行旧版的验证者可能阻塞奖励过期自动化。GSF 协调变通并设定合规截止日期。

## CIP 治理

网络规则、标准与协议变更通过 Canton Improvement Proposals (CIPs) 提议。CIP 流程为生态任何人提供结构化变更路径，最终由 Super Validator 投票批准。

流程详情见 [CIP Reference](/overview/reference/what-are-cips)。完整列表见 [github.com/global-synchronizer-foundation/cips](https://github.com/global-synchronizer-foundation/cips)。

## 沟通渠道

GSF 为验证者运营方与生态参与者维护：

* **Slack** — `#validator-operations`（运营协调）、`#gsf-global-synchronizer-appdev`（应用开发）、`#gsf-outreach`（生态讨论）
* **邮件列表** [lists.sync.global](https://lists.sync.global/) — 含 `main`（Canton Network 公告）、`cip-announce`（新 CIP）、`tokenomics-announce`（Tokenomics Committee 决定）、`validator-announce`（面向运营方）
* **支持** — `da-support@digitalasset.com`（尽力支持）、`support@digitalasset.com`（SLA 支持）

## 延伸阅读

* [GSF website](https://canton.foundation) — 基金会信息与会员
* [Canton Network](https://canton.network) — 网络概览与入口
* [GSF configs repository](https://github.com/global-synchronizer-foundation/configs) — 网络配置参数
* [CIP repository](https://github.com/global-synchronizer-foundation/cips) — Canton Improvement Proposals
* [SV Governance Reference](/overview/reference/sv-governance-reference) — DSO party 与投票机制技术细节
