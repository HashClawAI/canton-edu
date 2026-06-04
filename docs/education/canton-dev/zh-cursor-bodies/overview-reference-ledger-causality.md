> Daml 账本上的因果图、本地账本与 Ledger API 排序保证

# 因果性

Daml 账本不会对全部交易做全序排列。因此，不同 Party 通过 gRPC Ledger API 在不同 Participant 节点上观察同一对交易时，可能看到不同的顺序。此外，不同 Participant 节点对同一 Party 输出的两笔交易顺序也可能不同。本文通过示例，并以因果图与本地账本的概念作形式化说明，解释 Daml 账本实际提供的排序保证。

本文假定读者已熟悉以下概念：

* Ledger API
* Daml Ledger Model

## 因果性示例

与 Daml Ledger Model 中的账本不同，Daml 账本不必对所有交易做全序排列。以下示例说明 Ledger API 的这些排序保证。它们基于 Daml Ledger Model 隐私章节中的油漆 counteroffer 工作流，并忽略 Daml Ledger Model 带来的全序。回顾各 Party 的投影如下。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/divulgence-for-disclosure-counteroffer.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=8b98310636eff182c92997e7c248bf07" className="align-center" style={{width: "100.0%"}} alt="油漆 counteroffer 工作流中各 Party 的时间序列（含披露），如上文链接的隐私章节所述。" width="1380" height="1522" data-path="images/docs_website/divulgence-for-disclosure-counteroffer.svg" />

### 合约利益相关方以相同顺序看到创建与归档

每个 Daml 账本都会将 `CounterOffer A P Bank` 的创建排在油漆工对该 `CounterOffer` 执行 consuming choice 之前。（若 **Create** 排在 **Exercise** 之后，所得共享账本将不一致，这违反 Daml 账本的有效性保证。）因此，Alice 会在其交易流中先看到创建、后看到归档，油漆工亦然。这与他们是否托管在同一 Participant 节点无关。

### 合约签名方与利益相关方 actor 在创建之后、归档之前看到使用

对 Alice 与 Bank 而言，`Fetch A (Iou Bank A)` 动作都排在 `Iou Bank A` 的创建之后、其归档之前，因为 Bank 是 `Iou Bank A` 合约的签名方，而 Alice 是该合约的利益相关方，且是 **Fetch** 动作的 actor。

### 提交是原子的

Alice 会先看到其 `Iou` 的 **Create**，再看到 `CounterOffer` 的创建，因为 `CounterOffer` 与对 `Iou` 的 **Fetch** 在同一 commit 中创建，而 **Fetch** 的 commit 排在 `Iou` 的 **Create** 之后。

### 不同 commit 中的非 consuming 使用可能以不同顺序出现

假设 Bank 在 Alice 创建 `CounterOffer` 的同时，对 `Iou Bank A` 执行一个无后果的非 consuming choice。在下图所示账本中，Bank 的 commit 排在 Alice 的 commit 之前。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-double-fetch.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=72dde9c92dae689a3d6be858beb8ba50" className="align-center" style={{width: "100.0%"}} alt="油漆 counteroffer 工作流的共享账本视图中的时间序列。" width="1567" height="433" data-path="images/docs_website/counteroffer-double-fetch.svg" />

Bank 的投影包含对 `Iou` 的非 consuming **Exercise** 与 **Fetch** 动作。然而，在 Bank 的交易树流中，**Fetch** 可能排在非 consuming **Exercise** 之前。

### 带外因果性不被尊重

以下示例假设 Alice 将其 commit 拆成两个，如下所示：

<div id="split-counteroffer-ledger">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-split-commit.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=6e3fe1c8c7276fefe9ee8cfdac0fb984" className="align-center" style={{width: "100.0%"}} alt="拆分为四个 commit 的 counteroffer 工作流。" width="1380" height="431" data-path="images/docs_website/counteroffer-split-commit.svg" />

    <figcaption>包含四个 commit 的 counteroffer 工作流。</figcaption>
  </figure>
</div>

Alice 可以在 `CounterOffer` 中指定她用于向油漆工付款的 `Iou`。在已部署的实现中，Alice 的应用会先通过 Update Service 或 State Service 观察到已创建的 `Iou` 合约，再请求创建 `CounterOffer`。此类应用逻辑不会在 commit 之间引入排序。因此，`CounterOffer` 的创建不必排在 `Iou` 的创建之后。

若 Alice 托管在多个 Participant 节点上，这些 Participant 节点因此可以按任意顺序输出这两次创建。

这一行为的理由是：Alice 可能通过带外渠道获知 contract ID，或自行构造该 ID。Participant 节点因此无法知道该合约是否终会出现 **Create** 事件。若 Participant 节点延迟输出 `CounterOffer` 的 **Create** 动作，直到 `Iou` 合约的 **Create** 事件被发布，这种延迟可能无限持续，从而丧失活性（liveness）。因此 Daml 账本不会捕获流经应用的数据流。

### 泄露的动作不引入顺序

当 `ShowIou` 合约被消费时，油漆工见证 Alice 的 `Iou` 被 fetch。当 Alice 因油漆工接受 `CounterOffer` 而执行 transfer choice 时，油漆工也见证对 `Iou` 的 **Exercise**。然而，由于油漆工不是 Alice 的 `Iou` 合约的利益相关方，他可能在 `ShowIou` commit 中观察到 Alice 的 `ShowIou`，而该 commit 却排在接受 `CounterOffer` 时对 `Iou` 的归档之后。

实践中，这可能在如下配置中发生：两个 Participant 节点 `N``1` 与 `N``2` 托管油漆工。他通过 `N``1` 的交易树流看到泄露的 `Iou` 与已创建的 `CounterOffer`，然后通过 `N``1` 提交接受。与前一示例类似，`N``2` 不知道这两次 commit 之间的依赖关系。因此，`N``2` 可能在交易流中*先于* `ShowIou` 合约输出接受交易。

尽管这可能看似意外，但它符合基于利益相关方的账本：由于油漆工不是 `Iou` 合约的利益相关方，他不应关心该合约的归档或创建。事实上，泄露的 `Iou` 合约既不会出现在油漆工的 State Service 中，也不会出现在 update 流中的 ACS delta 里。此类被见证的事件纳入交易树流仅为便利：它们使油漆工无需自行计算 choice 的后果，并使他能够检查该动作是否符合 Daml 模型。

类似地，作为 **Exercise** 动作的 actor，仅当 actor 是合约利益相关方时，才会相对于该合约的其他使用引入顺序。这是因为非利益相关方的 **Exercise** actor 仅授权该动作，但不跟踪合约是否仍活跃；签名方与合约 observer 才负责这一点。同理，**Exercise** 动作的 choice observer 仅在其为合约利益相关方时才受益于排序保证。

### 排序保证取决于 Party

由前一示例可知，对油漆工而言，fetch `Iou` 并不排在 transfer `Iou` 之前。然而对 Alice 而言，**Fetch** 必须出现在 **Exercise** 之前，因为 Alice 是 `Iou` 合约的利益相关方。这表明排序保证取决于 Party。

## 因果图

上述示例表明，Daml 账本仅对交易做偏序排列。Daml 账本可表示为交易的有限有向无环图（DAG）。

<div id="def-causality-graph">
  定义 »因果图«
  **因果图**是交易的有限有向无环图 `G`，且为传递闭包。传递闭包指：只要 `G` 中存在边 `v``1` -> `v``2` 与 `v``2` -> `v``3`，则 `G` 中也存在边 `v``1` -> `v``3`。
</div>

<div id="def-action-order">
  定义 »动作序«
  对因果图 `G`，其诱导的、作用于各交易中动作的 **动作序**，将图在交易之间诱导的顺序与各交易内部动作的执行顺序相结合。它是包含以下两动作 `act``1` 与 `act``2` 之间关系的最小偏序：

  * `act``1` 与 `act``2` 属于同一交易，且在该交易中 `act``1` 先于 `act``2`。

  * `act``1` 与 `act``2` 分别属于顶点 `tx``1` 与 `tx``2` 中的不同交易，且 `G` 中存在从 `tx``1` 到 `tx``2` 的路径。
</div>

<Note>
  由于因果图是传递闭包的，检查 `G` 中从 `tx``1` 到 `tx``2` 的*边*与检查*路径*是等价的。定义使用*路径*，是因为下图为可读性省略了传递边。
</Note>

动作序是因果图中动作上的偏序。例如，下图展示了上文带外因果性示例中账本的因果图。每个灰色框代表一笔交易，图边为框之间的实线箭头。为可读性，图示省略传递边；在此图中，从 `tx1` 到 `tx4` 的边未显示。Alice 的 `Iou` 的 **Create** 动作排在 `ShowIou` 合约的 **Create** 动作之前，因为从含 `Iou` **Create** 的交易 `tx1` 到含 `ShowIou` **Create** 的交易 `tx3` 存在一条边。此外，`ShowIou` 的 **Create** 动作排在 Alice 的 `Iou` 的 **Fetch** 之前，因为 **Create** 在该交易中先于 **Fetch**。相比之下，`CounterOffer` 与 Alice 的 `Iou` 的 **Create** 动作是无序的：它们属于不同交易且彼此之间没有有向路径，因而互不先于对方。

<div id="causality-graph-counteroffer-split">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-split-action-order.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=9d97cdb47ac14872128e11ddd63b81a5" className="align-center" style={{width: "100.0%"}} alt="包含四个 commit 的 counteroffer 工作流的因果图。" width="1440" height="380" data-path="images/docs_website/counteroffer-split-action-order.svg" />

    <figcaption>包含四个 commit 的 counteroffer 工作流的因果图。</figcaption>
  </figure>
</div>

### 一致性

一致性确保因果图对全部交易做了足够排序。它如下文所述，将 Daml Ledger Model 中的账本一致性加以推广。

<div id="def-causal-consistency-contract">
  定义 »合约的因果一致性«
  设 `G` 为因果图，`X` 为 `G` 中属于各笔交易、且作用于合约 `c` 的动作集合。若以下全部成立，则称 `G` 在 `X` 上对合约 `c` **因果一致**：

  * 若 `X` 非空，则 `X` 恰含一个 **Create** 动作。该动作在 `G` 的动作序中先于 `X` 中所有其他动作。
  * 若 `X` 含 consuming **Exercise** 动作 `act`，则 `act` 在 `G` 的动作序中后于 `X` 中除 `act` 外的所有动作。

  定义 »键的因果一致性«
  设 `G` 为因果图，`X` 为 `G` 中属于各笔交易、且作用于键 `k` 的动作集合。若以下全部成立，则称 `G` 在 `X` 上对键 `k` **因果一致**：

  * `X` 中所有 **Create** 与 consuming **Exercise** 动作在 `G` 的动作序中全序排列，且 **Create** 与 consuming **Exercise** 交替出现，以 **Create** 开头。每一对相邻的 **Create**-**Exercise** 作用于同一合约。
  * `X` 中所有 **NoSuchKey** 动作相对于 `X` 中所有 **Create** 与 consuming **Exercise** 动作有动作序关系。任何 **NoSuchKey** 动作不得排在 **Create** 动作与其后续 consuming **Exercise** 动作之间。
</div>

<div id="def-consistency-causality-graph">
  定义 »因果图的一致性«
  设 `X` 为因果图 `G` 中动作的子集。若 `G` 对 `X` 中每个合约 `c` 在 `c` 上的动作集合、以及对 `X` 中每个键 `k` 在 `k` 上的动作集合均因果一致，则称 `G` 在 `X` 上**一致**（或 **X-一致**）。若 `G` 在 `G` 中全部动作上一致，则称 `G` **一致**。
</div>

向 `X`-一致的因果图添加边且仍保持无环与传递闭包时，所得图再次 `X`-一致。因此可以考虑最小一致因果图。

<div id="minimal-consistent-causality-graph">
  定义 »最小一致因果图«
  若 `X`-一致因果图 `G` 的任意真子图（顶点相同、边更少）都不是 `X`-一致因果图，则称 `G` 为 **X-最小**。若 `X` 为 `G` 中全部动作的集合，则省略 `X`。
</div>

例如，上文拆分 counteroffer 工作流的因果图是一致的。如下分析表明该因果图是最小的：

| 边           | 依据                                                                        |
| -------------- | ------------------------------------------------------------------------------------ |
| `tx1` -> `tx3` | Alice 的 `Iou` **Create** 动作必须先于 **Fetch** 动作。                |
| `tx2` -> `tx4` | `CounterOffer` **Create** 动作必须先于 **Exercise** 动作。        |
| `tx3` -> `tx4` | 对 Alice 的 `Iou` 的 consuming **Exercise** 必须后于 **Fetch** 动作。 |

我们可以通过限制集合 `X` 来聚焦因果图的一部分。若 `X` 由 `Iou` 合约上的动作组成，该因果图是 `X`-一致的。然而它并非 `X`-最小，因为边 `tx2` -> `tx4` 可在不违反 `X`-一致性的情况下去除：该边仅因 `CounterOffer` 动作而需要，而这些动作不在 `X` 中。`X`-最小一致因果图如下所示，其中 `X` 中的动作以红色高亮。

<div id="causality-counteroffer-Iou-minimal">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/causality-counteroffer-Iou-minimal.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=3c297cb67620500a99ca350f443f5492" className="align-center" style={{width: "100.0%"}} alt="高亮动作的最小一致因果图。" width="1440" height="380" data-path="images/docs_website/causality-counteroffer-Iou-minimal.svg" />

    <figcaption>高亮动作的最小一致因果图。</figcaption>
  </figure>
</div>

下图展示了另一个最小因果图示例。上方，交易 `tx1` 至 `tx4` 为 Alice 创建 `Iou`、对其执行两次非 consuming choice，并将 `Iou` 转给油漆工。下方，`tx5` 断言油漆工的 Account 合约不存在对应键；随后 `tx6` 创建余额为 0 的此类账户，`tx7` 将油漆工来自 `tx4` 的 `Iou` 存入该账户，将余额更新为 1。

<img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/causality-consistency-examples.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=e2525433fcd1f5b858f417ac7c97e8b5" className="align-center" style={{width: "100.0%"}} alt="最小因果图示例：油漆工从 Alice 收到 Iou，并自动创建用于持有该 Iou 的 Account 合约，如上所述。" width="980" height="620" data-path="images/docs_website/causality-consistency-examples.svg" />

与线性有序账本不同，因果图仅在最后——将 `Iou` 存入账户时——才将 `Iou` 转账工作流的交易与 `Account` 创建工作流的交易关联起来。如下文将形式化说明，Bank、Alice 与油漆工因此不必以相同顺序观察交易 `tx1` 至 `tx7`。

此外，尽管交易 `tx2` 与 `tx3` 作用于同一 `Iou` 合约，它们在此因果图中仍是无序的。然而，由于两个动作都是非 consuming，它们互不干扰，因此也可以并行化。因此 Alice 与 Bank 可能以不同顺序观察它们。

按键一致性条件，`tx5` 中的 **NoSuchKey** 动作必须相对于 `tx6` 与 `tx7` 中的两个 Account **Create** 动作，以及 `tx7` 中对 Account 合约的 consuming **Exercise** 排序。对该组交易，一致性仅允许一种此类顺序：由于 `tx7` 是原子的，`tx5` 排在 `tx6` 之前——`tx5` 不能与 `tx7` 交错，例如不能插在 `Acc Bank P P 0` 的 consuming **Exercise** 与更新后账户 `Acc Bank P P 1` 的 **Create** 之间。

在因果排序方面，**NoSuchKey** 动作类似于对合约的非 consuming **Exercise** 与 **Fetch**：若还有另一笔交易 `tx5'`，其中含 **NoSuchKey** `(Acc, Bank, P)` 动作，则 `tx5` 与 `tx5'` 不必有序，正如 `tx2` 与 `tx3` 无序一样。

### 从因果图到账本

由于因果图无环，其顶点可拓扑排序，所得列表再次构成因果图，其中每个顶点向所有后续顶点有一条出边。若原因果图是 `X`-一致的，则拓扑排序亦然，因为拓扑排序仅添加边。例如，带外因果性示例中账本上的交易，即是对应因果图的拓扑排序。

反之，我们可以将 `X`-一致因果图约简为仅保留 `X`-一致性所强加的因果依赖。这给出最小 `X`-一致因果图。

<div id="def-reduction-causality-graph">
  定义 »一致因果图的约简«
  对 `X`-一致因果图 `G`，存在唯一的最小 `X`-一致因果图 `reduce``X``(G)`，其顶点与 `G` 相同，边是 `G` 边的子集。图 `reduce``X``(G)` 称为 `G` 的 **X-约简**。与之前一样，若 `X` 包含 `G` 中全部动作，则省略 `X`。
</div>

拆分 `CounterOffer` 工作流的因果图是最小的，因此是其自身的约简。它也是拓扑排序的约简，即带外因果性示例中的账本。

<Note>
  `X`-一致因果图 `G` 的约简 `reduce``X``(G)` 可如下计算：

  1. 将 `G'` 的顶点设为 `G` 的顶点。
  2. 合约与键的因果一致性条件要求 `X` 中某些动作对 `act``1` 与 `act``2` 必须有动作序关系。对每一此类动作对，确定它们在 `G` 中的顺序，并向 `G'` 添加从较早动作所在交易到较晚动作所在交易的边。
  3. `reduce``X``(G)` 是 `G'` 的传递闭包。
</Note>

拓扑排序与约简将因果图 `G` 与 Daml Ledger Model 中的账本 `L` 联系起来。拓扑排序将因果图 `G` 变换为交易序列；为其补充 requester 即得 commit 序列，亦即 Daml Ledger Model 中的账本。反之，commit 序列 `L` 通过以交易为顶点、并在序列中 `tx1` 的 commit 先于 `tx2` 的 commit 时添加从 `tx1` 到 `tx2` 的边，得到因果图 `G``L`。

现在有两种一致性定义：

* 按 Daml Ledger Model 的账本一致性
* 因果图的一致性

幸运的是，两者等价：若 `G` 是一致因果图，则其拓扑排序是账本一致的。反之，若 commit 序列 `L` 账本一致，则 `G``L` 是一致因果图，约简 `reduce(G``L``)` 亦然。

## 本地账本

如 Daml Ledger Model 所述，出于隐私原因，Party 仅看到共享账本的投影。与一致性类似，投影可如下扩展到因果图。

定义 »利益相关方 informee«
当以下全部成立时，Party `P` 是动作 `act` 的**利益相关方 informee**：

* `P` 是 `act` 的 informee。
* 若 `act` 是合约上的动作，则 `P` 是该合约的利益相关方。

**Exercise** 与 **Fetch** 动作作用于输入合约，**Create** 动作作用于所创建合约，**NoSuchKey** 动作不作用于合约。因此对 **NoSuchKey** 动作，利益相关方 informee 是键维护者（key maintainer）。

定义 »Party 的因果一致性«
若因果图 `G` 在 `P` 作为利益相关方 informee 的全部动作上一致，则称 `G` 对 Party `P` **一致**（**P-一致**）。

`X`-最小性与 `X`-约简的概念可相应地扩展到 Party。

例如，去掉边 tx2 -> tx4 的拆分 counteroffer 因果图对 Bank 是一致的，因为 Bank 恰是高亮动作的利益相关方 informee。它也是 Bank-最小且是原拆分 counteroffer 因果图的 Bank-约简。

定义 »一致因果图的投影«
一致因果图 `G` 到 Party `P` 的**投影** `proj``P``(G)`，是下列因果图 \`G'\` 的 `P`-约简：

* `G'` 的顶点是 `G` 投影到 `P` 的顶点，排除空投影。
* 若 `G` 中存在从对应于 `v``1` 的顶点到对应于 `v``2` 的顶点的边，则 `G'` 中顶点 `v``1` 与 `v``2` 之间有一条边。

对拆分 counteroffer 因果图，投影到 Alice、Bank 与油漆工的结果如下。

<div id="counteroffer-causality-projections">
  <figure>
    <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/counteroffer-causality-projection.svg?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=b2c9cdebf369055e671fa822791e1320" className="align-center" style={{width: "100.0%"}} alt="拆分 counteroffer 因果图的投影。" width="1448" height="1040" data-path="images/docs_website/counteroffer-causality-projection.svg" />

    <figcaption>拆分 counteroffer 因果图的投影。</figcaption>
  </figure>
</div>

Alice 的投影与原最小因果图相同。Bank 仅看到 `Iou` 合约上的动作，因此因果图投影不再包含 `tx2`。类似地，油漆工不知道 `tx1`（Alice 的 `Iou` 在此创建）。此外，油漆工本地账本中不再存在从 `tx3` 到 `tx4` 的边。这是因为该边由 Alice 的 `Iou` 的 **Fetch** 先于 consuming **Exercise** 所诱导。然而油漆工不是这两动作的 informee；他仅作为泄露的一部分见证 **Fetch** 与 **Exercise** 动作。因此从油漆工视角无需排序。这一差异解释了泄露因果性示例。

### Ledger API 排序保证

Update Service 以 Daml 交易流的形式提供更新，State Service 则通过给定时点的活跃合约汇总截至该时点的全部更新。概念上，两项服务均派生自 Participant 节点为每个托管 Party 维护的本地账本。也就是说，某 Party 的交易树流是其本地账本的拓扑排序。扁平交易流（flat transaction stream）精确包含与交易树流中、Party 为受影响合约利益相关方的交易树里 **Create** 与 consuming **Exercise** 动作对应的 `CreatedEvent` 与 `ArchivedEvent`。

<Note>
  Update Service 的交易树省略本地账本交易所含的部分 **Fetch** 与 **NoSuchKey** 动作。因此 **Fetch** 与 **NoSuchKey** 在 Update Service 输出交易树之前被移除。
</Note>

类似地，State Service 根据 Update Service 流，提供在返回 offset 处仍活跃的合约集合。也就是说，交易事件流中全部事件的合约状态变化都会计入所提供的合约集合。特别地，应用可处理扁平交易流或交易树流中的后续事件，而无需考虑快照之前的事件。

由于本地账本的拓扑排序不唯一，不同 Participant 节点可能对同一 Party 的交易流选择不同顺序。类似地，不同 Party 的交易流可能对共同交易采用不同顺序，因为各 Party 的本地账本施加不同的排序约束。尽管如此，Daml 账本确保所有本地账本都是虚拟共享因果图的投影，该因果图如上所述与 Daml Ledger Model 相连。因此账本有效性保证通过本地账本延伸到 Ledger API。这些保证受所部署 Daml 账本的信任假设约束。

<Note>
  虚拟共享因果图仅作为概念存在，用于推理 Daml 账本保证。已部署的 Daml 账本通常既不存储也不构造此类共享因果图。Participant 节点仅为各自 Party 维护本地账本。它们在本地账本保持一致的前提下同步这些本地账本。也就是说，所有本地账本在理论上可合并为一个一致的单因果图，而它们正是该图的投影。
</Note>

### 因果性示例的解释

因果性示例可用因果图与本地账本解释如下：

1. `causality-example-create-archive` 合约的因果一致性要求 **Create** 先于合约上的 consuming **Exercise** 动作。由于全部利益相关方都是其合约 **Create** 与 consuming **Exercise** 动作的 informee，利益相关方的本地账本对这些动作施加此顺序。
2. `causality-example-create-use-archive` 合约的因果一致性要求 **Create** 先于合约的非 consuming **Exercise** 与 **Fetch** 动作，且 consuming **Exercise** 后于它们。由于签名方与利益相关方 actor 是 **Create**、**Exercise** 与 **Fetch** 动作的 informee，利益相关方的本地账本对这些动作施加此顺序。
3. `causality-example-commit-atomic` 本地账本是（投影后）交易的 DAG。对此类 DAG 做拓扑排序时，不能将一笔交易与另一笔交错，即使该交易由多个顶层动作组成。
4. `causality-example-non-consuming` 因果一致性不要求合约的非 consuming 使用之间有序。由于交易中没有其他动作规定顺序，Participant 节点可以任意顺序输出它们。
5. `causality-example-out-of-band` 带外数据流不被因果一致性捕获，因此不引入排序。
6. `causality-divulgence-example` 油漆工不是 Alice 的 `Iou` 上 **Fetch** 与 **Exercise** 动作的 informee；他仅见证它们。因此油漆工的本地账本不将 `tx3` 排在 `tx4` 之前。油漆工的交易流因此可以先输出 `tx4`、后输出 `tx3`。
7. `causality-example-depend-on-party` Alice 是其 `Iou` 上 **Fetch** 与 **Exercise** 动作的 informee。与油漆工不同，她的本地账本将 `tx3` 排在 `tx4` 之前，因此 Alice 保证在所有她连接 Daml 账本的 Participant 节点上先观察到 `tx3`、后观察到 `tx4`。

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/overview/explanations/ledger-model/time.rst" hash="e88a1d96" */}

<Note>
  * 将 LAPI 部分移至 BUILD 子站
  * 将时间单调性整合进 ledger model
  * SKEW 应放在何处？
</Note>

# Daml 账本上的时间

Daml 语言包含函数 getTime，它返回「当前时间」。然而，在分布式环境中，「当前时间」这一概念可能颇具挑战。

本文描述 Daml 账本上时间的详细语义，围绕分配给每笔交易的两个时间戳：*ledger time* `lt_TX` 与 *record time* `rt_TX`。

## Ledger Time

*Ledger time* `lt_TX` 是交易的属性。它是时间戳，定义给定交易中所有 getTime 调用的值，精度为微秒。ledger time 由提交 participant 在 Daml 命令解释过程中分配。

## Record Time

*Record time* `rt_TX` 是交易的另一属性。它是微秒精度的时间戳，在交易持久化时由底层存储机制分配。

record time 应是「真实时间」的直观表示，但 Daml 抽象账本模型并不严格规定如何分配 record time。每种持久化技术在分布式环境中可能采用不同的时间表示方式。

## 保证

有效交易 `TX` 的 ledger time 必须满足以下规则：

1. **因果单调性**：对 `TX` 中合约 `C` 上的任意动作（create、exercise、fetch、lookup），`lt_TX >= lt_C`，其中 `lt_C` 是创建 `C` 的交易的 ledger time。
2. **有界偏移**：`rt_TX - skew_min <= lt_TX <= rt_TX + skew_max`，其中 `skew_min` 与 `skew_max` 是账本定义的参数。

除此之外，不对 ledger time 给出其他保证。特别地，ledger time 与 record time 均不必单调递增。

因此在 Daml 中时间应视为略有模糊，模糊程度取决于 skew 参数。Daml 应用不应将 getTime 的返回值解释为精确时间戳。

## 分配 Ledger Time

ledger time 由 participant 自动分配。在大多数情况下，Daml 应用完全无需关心 ledger time 与 record time。

供参考，本节描述当前如何分配 ledger time 的细节。该算法不属于 Daml 时间定义的一部分，未来可能变更。

1. 通过 Ledger API 提交命令时，用户可选指定 `min_ledger_time_rel` 或 `min_ledger_time_abs` 参数。它们分别以相对与绝对方式定义 ledger time 的下界。
2. ledger time 设为以下值中的最大值：
   1. `max(lt_C_1, ..., lt_C_n)`，即给定交易所用全部合约的 ledger time 最大值
   2. `t_p`，participant 上的本地时间
   3. `t_p + min_ledger_time_rel`（若给定 `min_ledger_time_rel`）
   4. `min_ledger_time_abs`（若给定 `min_ledger_time_abs`）
3. 由于给定交易所用命令集合可能取决于所选时间，上述过程可能需要重复，直到找到合适的 ledger time。
4. 若 3 次迭代后仍未找到合适的 ledger time，提交将被拒绝。这可能发生在合约存在争用，或交易基于非常细粒度的时间控制流时。
5. 此时 ledger time 可能位于未来（例如若 `min_ledger_time_rel` 取值较大）。participant 会等待至 `lt_TX - transaction_latency` 再将交易提交到账本——意图是交易在 `lt_TX == rt_TX` 时被记录。

若预期命令解释将耗时较长，以致所得交易提交到账本时其分配的 ledger time 已不再有效，可使用参数 `min_ledger_time_rel` 与 `min_ledger_time_abs`。请注意，这些参数只能确保交易大致在 `rt_TX` 时刻到达账本。若账本上的后续验证耗时超过 `skew_max`，交易仍会被拒绝，你需要请账本操作员增大 `skew_max` 时间模型参数。
