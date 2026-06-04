#!/usr/bin/env python3
"""Generate zh bodies for hashing / onboarding / topology from EN markdown."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "src/content/canton-doc-pages/en"
OUT = Path(__file__).parent / "batch2-zh-part2-bodies"

FOOTER_RE = re.compile(
    r"\n---\n\n> Mirrored from Canton Network.*$", re.DOTALL
)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(
    r"> ## Documentation Index\n.*?\n\n", re.DOTALL
)


def strip_en(md: str, intro_quote: str) -> str:
    md = FRONTMATTER_RE.sub("", md)
    md = DOC_INDEX_RE.sub("", md)
    md = FOOTER_RE.sub("", md)
    lines = md.splitlines()
    while lines:
        line = lines[0].strip()
        if not line:
            lines.pop(0)
            continue
        if line.startswith("# ") or line.startswith("> "):
            lines.pop(0)
            continue
        break
    md = "\n".join(lines).lstrip("\n")
    return intro_quote + "\n\n" + md.strip() + "\n"


def drop_trailing_english_duplicate(line: str) -> str:
    """Remove partial-regex leftover English tails on mixed lines."""
    if not re.search(r"[\u4e00-\u9fff]", line):
        return line
    markers = [
        " used to ",
        " of the ",
        " in any ",
        " with a ",
        " This enables",
        " because it",
        " topology transaction to include",
        " to be uploaded to the Ledger API",
        " if you have two participants",
        " using participant1:",
        " through the ",
        " the second participant",
    ]
    for m in markers:
        if m in line:
            return line.split(m, 1)[0].rstrip()
    return line


def polish_body(text: str) -> str:
    lines = [drop_trailing_english_duplicate(ln) for ln in text.splitlines()]
    return "\n".join(lines) + "\n"


def split_codeblock_segments(text: str) -> list[tuple[str, bool]]:
    parts = re.split(r"(```[\s\S]*?```)", text)
    segs: list[tuple[str, bool]] = []
    for p in parts:
        if not p:
            continue
        segs.append((p, p.startswith("```")))
    return segs


def translate_hashing_prose(chunk: str) -> str:
    full = [
        (
            "This document specifies the encoding algorithm used to produce a deterministic hash of a `com.daml.ledger.api.v2.interactive.PreparedTransaction`. The resulting hash is signed by the holder of the external party's private key. The signature authorizes the ledger changes described by the transaction on behalf of the external party.",
            "本文规定用于对 `com.daml.ledger.api.v2.interactive.PreparedTransaction` 产生确定性哈希的编码算法。外部 Party 私钥持有者对该哈希签名，以代表该外部 Party 授权交易所描述的账本变更。",
        ),
        (
            "The specification can be implemented in any language, but certain encoding patterns are biased due to Canton being implemented in a JVM-based language and using the Java protobuf library. Those biases are made explicit in the specification.",
            "可在任意语言实现；因 Canton 基于 JVM 并使用 Java protobuf 库，部分编码模式带有实现偏好，规范中已明示。",
        ),
        (
            "Protobuf serialization is unsuitable for signing cryptographic hashes because it is not canonical. We must define a more precise encoding specification that can be re-implemented deterministically across languages and provide the required cryptographic guarantees. See [https://protobuf.dev/programming-guides/serialization-not-canonical/](https://protobuf.dev/programming-guides/serialization-not-canonical/) for more information on the topic.",
            "Protobuf 序列化不适合直接用于密码学签名哈希，因其非规范形式。须定义更精确的编码规范以便跨语言确定性重实现并提供密码学保证。详见 [https://protobuf.dev/programming-guides/serialization-not-canonical/](https://protobuf.dev/programming-guides/serialization-not-canonical/)。",
        ),
        (
            "The hashing algorithm as a whole is versioned. This enables updates to accommodate changes in the underlying Daml format, or, for instance, to the way the protocol verifies signatures. The implementation must respect the specification of the version it implements.",
            "哈希算法整体带版本号，以便在底层 Daml 格式或签名验证方式变更时演进；实现须遵循所实现版本的规范。",
        ),
        (
            "The hashing algorithm is tied to the protocol version of the synchronizer used to synchronize the transaction. Specifically, each hashing scheme version is supported on one or several protocol versions. Implementations must use a hashing scheme version supported on the synchronizer on which the transaction is submitted.",
            "哈希算法与用于同步交易的 synchronizer 协议版本绑定；各哈希方案版本在一个或多个协议版本上受支持，提交交易的 synchronizer 上须使用受支持的哈希方案版本。",
        ),
        (
            "Transaction nodes are additionally individually versioned with a Daml version (also called LF version). The encoding version is decoupled from the LF version and implementations should only focus on the hashing version. However, new LF versions may introduce new fields in nodes or new node types. For that reason, the protobuf representation of a node is versioned to accommodate those future changes. In practice, every new Daml language version results in a new hashing version.",
            "交易节点另以 Daml（LF）版本单独版本化。编码版本与 LF 版本解耦，实现应聚焦哈希版本；新 LF 版本可能引入新字段或节点类型，故节点 protobuf 亦版本化。实践中每个新 Daml 语言版本对应新哈希版本。",
        ),
        (
            "The hash of the `PreparedTransaction` is computed by encoding every protobuf field of the messages to byte arrays, and feeding those encoded values into a `SHA-256` hash builder. The rest of this section details how to deterministically encode every proto message into a byte array. Sometimes during the process, partially encoded results are hashed with SHA-256, and the resulting hash value serves as the encoding in messages further up. This is explicit when necessary.",
            "`PreparedTransaction` 的哈希通过将消息各 protobuf 字段编码为字节数组并送入 `SHA-256` 哈希构建器计算。下文说明如何确定性编码各 proto 消息；部分中间结果会先 SHA-256，其哈希作为上层编码（必要时会明示）。",
        ),
        (
            "Big Endian notation is used for numeric values. Furthermore, protobuf numeric values are encoded according to their Java type representation. Refer to the official protobuf documentation for more information about protobuf to Java type mappings: [https://protobuf.dev/programming-guides/proto3/#scalar](https://protobuf.dev/programming-guides/proto3/#scalar) In particular:",
            "数值使用大端序；protobuf 数值按 Java 类型表示编码，映射见 [https://protobuf.dev/programming-guides/proto3/#scalar](https://protobuf.dev/programming-guides/proto3/#scalar)。",
        ),
        (
            "Additionally, this is the java library used under the hood in Canton to serialize and deserialize protobuf: [https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java](https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java)",
            "Canton 底层序列化 protobuf 使用的 Java 库：[https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java](https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java)",
        ),
        (
            "`repeated` protobuf fields represent an ordered collection of values of a specific message of type `T``. It is critical that the order of values in the list is not modified, both for the encoding process and in the protobuf itself when submitting the transaction for execution. Below is the pseudocode algorithm encoding a protobuf value ``repeated T list;`\\`",
            "`repeated` 字段为类型 `T` 的有序集合；列表顺序在编码与提交交易的 protobuf 中均不得改变。编码 `repeated T list` 的伪代码如下。",
        ),
        (
            "A transaction is a forest (list of trees). It is represented with a following protobuf message found here.",
            "交易是森林（树列表），由下述 protobuf 消息表示。",
        ),
        (
            "The final part of `PreparedTransaction` is metadata. Note that all fields of the metadata need to be signed. Only some fields contribute to the ledger change triggered by the transaction. The rest of the fields are required by the Canton protocol but either have no impact on the ledger change, or have already been signed indirectly by signing the transaction itself.",
            "`PreparedTransaction` 的最后部分是元数据；元数据所有字段均须签名。仅部分字段影响交易所触发的账本变更，其余为 Canton 协议所需或已通过签名交易间接承诺。",
        ),
        (
            "Finally, compute the hash that needs to be signed to commit to the ledger changes.",
            "最后计算须签名以承诺账本变更的哈希。",
        ),
        (
            "This resulting hash must be signed with the protocol signing private key(s) used to onboard the external party. Both the signature along with the `PreparedTransaction` must be sent to the API to submit the transaction to the ledger.",
            "须用入网外部 Party 时使用的协议签名私钥对该哈希签名，并将签名与 `PreparedTransaction` 一并提交 API 写入账本。",
        ),
    ]
    out = chunk
    for en, zh in full:
        out = out.replace(en, zh)
    out = re.sub(r"^# External Signing: Hashing Algorithm\s*\n+", "", out, flags=re.MULTILINE)
    reps = [
        (r"^# External Signing Hashing Algorithm\s*$", "# 外部签名哈希算法"),
        (r"^## Introduction\s*$", "## 简介"),
        (r"^## Versioning\s*$", "## 版本"),
        (r"^### Hashing Scheme Version\s*$", "### 哈希方案版本"),
        (r"^\| Protocol Version \|", "| 协议版本 |"),
        (r"^\| Supported Hashing Schemes \|", "| 支持的哈希方案 |"),
        (r"^> Deterministic hashing specification.*$", ""),
        (r"^### Transaction Nodes\s*$", "### 交易节点"),
        (r"^## V2\s*$", "## V2"),
        (r"^### General approach\s*$", "### 总体方法"),
        (r"^### Changes from V1\s*$", "### 相对 V1 的变更"),
        (r"^\* Addition of an `interface_id`", "* Fetch 节点新增 `interface_id` 以支持 Daml 接口"),
        (
            r"^\* Addition of the hashing scheme version",
            "* 最终哈希中加入哈希方案版本，降低跨版本碰撞风险",
        ),
        (
            r"^\* Replace `ledger_effective_time`",
            "* 元数据中以 `min_ledger_effective_time` 与 `max_ledger_effective_time` 替代 `ledger_effective_time`",
        ),
        (
            r"^  > \* These effectively replace",
            "  > * 以时间界替代固定 ledger 时间，使 Daml 模型可基于时间断言而不把签名窗口限制得过窄",
        ),
        (r"^### Notation and Utility Functions\s*$", "### 符号与工具函数"),
        (r"^Unless otherwise specified", "除非另有说明，原始 protobuf 类型编码如下"),
        (r"^#### google\.protobuf\.Empty", "#### google.protobuf.Empty"),
        (r"^### Collections / Wrappers\s*$", "### 集合与包装类型"),
        (r"^#### repeated\s*$", "#### repeated"),
        (
            r"^`repeated` protobuf fields represent",
            "`repeated` 字段为有序集合，列表顺序在编码过程与提交交易的 protobuf 中均不得改变",
        ),
        (r"^#### optional\s*$", "#### optional"),
        (r"^#### map\s*$", "#### map"),
        (
            r"^The ordering of `map` entries",
            "protobuf `map` 条目顺序不保证，不利于确定性编码；因此在 protobuf 定义中普遍用 `repeated` 替代 `map`",
        ),
        (r"^### gRPC Ledger API Value\s*$", "### gRPC Ledger API Value"),
        (
            r"^Encoding for the `Value` message",
            "编码 `com.daml.ledger.api.v2.value.proto` 中的 `Value` 消息。为清晰起见列出全部值类型；各值前有类型唯一标签（见下文）",
        ),
        (r"^## Transaction\s*$", "## Transaction"),
        (
            r"^A transaction is a forest",
            "交易是森林（树列表），由如下 protobuf 消息表示",
        ),
        (r"^The encoding function for a transaction is", "交易编码函数为"),
        (r"^### Node\s*$", "### Node"),
        (
            r"^`Exercise` and `Rollback` nodes both",
            "`Exercise` 与 `Rollback` 节点的 `children` 字段通过 `NodeId` 引用其他节点",
        ),
        (r"^#### Create\s*$", "#### Create"),
        (r"^#### Exercise\s*$", "#### Exercise"),
        (r"^#### Fetch\s*$", "#### Fetch"),
        (r"^#### Rollback\s*$", "#### Rollback"),
        (r"^#### Transaction Hash\s*$", "#### 交易哈希"),
        (
            r"^Once the transaction is encoded",
            "交易编码完成后，对编码字节数组运行 `sha_256`，并加哈希用途前缀",
        ),
        (r"^## Metadata\s*$", "## Metadata"),
        (
            r"^The final part of `PreparedTransaction` is metadata",
            "`PreparedTransaction` 的最后部分是元数据。元数据所有字段均须签名；仅部分字段影响账本变更，其余为 Canton 协议所需或已通过签名交易间接承诺",
        ),
        (r"^### ProcessedDisclosedContract\s*$", "### ProcessedDisclosedContract"),
        (r"^### Metadata Hash\s*$", "### 元数据哈希"),
        (r"^## Final Hash\s*$", "## 最终哈希"),
        (
            r"^Finally, compute the hash",
            "最后计算须由外部 Party 协议签名私钥签名的哈希，以承诺账本变更",
        ),
        (
            r"^This resulting hash must be signed",
            "须用入网外部 Party 时使用的协议签名私钥对该哈希签名，并将签名与 `PreparedTransaction` 一并提交 API 以写入账本",
        ),
        (r"^## Example\s*$", "## 示例"),
        (r"^Example implementation in Python\s*$", "Python 示例实现"),
        (
            r"<Note>\s*\n\s*In Java, unsigned",
            "<Note>\n  在 Java 中，无符号 32/64 位整数用有符号对应类型表示，最高位存放在符号位\n</Note>",
        ),
        (
            r"<Note>\s*\n\s*Not all protobuf types",
            "<Note>\n  此处仅列出编码 `PreparedTransaction` 所需的 protobuf 类型，并非全部类型\n</Note>",
        ),
        (
            r"<Warning>\s*\n\s*Even default values",
            "<Warning>\n  即使默认值也必须编码。例如 int32 未设置时仍应编码 0；空 repeated 字段仍编码为 `0x00` 字节（详见 repeated 节）\n</Warning>",
        ),
        (
            r"<Note>\s*\n\s*This encoding function also applies",
            "<Note>\n  该编码函数同样适用于工具函数生成的列表（如 `split`）\n</Note>",
        ),
        (
            r"<Warning>\s*\n\s*`encode\(node_id\)` effectively",
            "<Warning>\n  `encode(node_id)` 会在 nodes 列表中找到对应节点并编码；`node_id` 本身从不编码，仅作引用。每个节点编码会 **经 sha_256 哈希**，在编码根节点及递归编码 `Exercise`/`Rollback` 子节点时均相关\n</Warning>",
        ),
        (
            r"<Warning>\s*\n\s*For Exercise nodes",
            "<Warning>\n  Exercise 节点的 node seed **必须**已定义，因此按非 optional 编码（见 `find_seed(...).get`）。若在 `node_seeds` 中找不到 seed，应停止编码并报错\n</Warning>",
        ),
        (
            r"<Note>\s*\n\s*The last encoded value of the exercise",
            "<Note>\n  Exercise 节点最后编码的是 `children` 字段，会递归遍历交易树\n</Note>",
        ),
        (
            r"<Note>\s*\n\s*Each node's encoding is prefixed",
            "<Note>\n  每个节点编码前会加节点元信息前缀，在各节点编码中明示\n</Note>",
        ),
        (
            r"<Note>\s*\n\s*Rollback nodes do not",
            "<Note>\n  Rollback 节点没有 lf version\n</Note>",
        ),
    ]
    out = chunk
    for pat, repl in reps:
        out = re.sub(pat, repl, out, flags=re.MULTILINE)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out


def translate_onboarding_prose(chunk: str) -> str:
    """Section headers + common phrases for onboarding doc."""
    full = [
        (
            "The flag `--multi-hosted` will pass the second participant id into the `generate-topology` request through the",
            "标志 `--multi-hosted` 会在 `generate-topology` 请求中通过下列字段传入第二个 participant id：",
        ),
        (
            "field. This will cause the generated topology transaction to include the additional participant id in the hosting relation ship. Other options are fields such as `observingParticipantUids`, `confirmationThreshold` and more. If not configured, then the confirmation threshold will be set to the number of confirming nodes.",
            "该字段使生成的拓扑交易在托管关系中包含额外 participant id。亦可配置 `observingParticipantUids`、`confirmationThreshold` 等；未配置时确认阈值默认为确认节点数。",
        ),
        (
            "The generated topology transactions then just need to be uploaded to the Ledger API of the second participant:",
            "生成的拓扑交易还须上传到第二个 participant 的 Ledger API：",
        ),
        (
            "This tutorial uses a script which is included as an example in the Canton artifact. Please note that the script uses openssl to create keys on the file system, which is not secure for production use.",
            "本教程使用 Canton 制品中的示例脚本；注意脚本用 openssl 在文件系统创建密钥，生产环境不安全。",
        ),
    ]
    corrupt = (
        "\\`\\`bash\nALLOCATE=\\$(cat:\n\nYou can try this out on the Canton console"
    )
    if corrupt in chunk:
        chunk = chunk.replace(
            "\\`\\`bash\nALLOCATE=\\$(cat:\n\nYou can try this out on the Canton console if you have two participants connected to the same synchronizer. In the following example, you will use the participant1 to create the hosting proposal for an internal party. This way, you don't need to deal with creating signatures for the topology transactions externally. The approval of the proposal will be done using participant2.",
            "（将 `ALLOCATE` 请求提交到第二个 participant 的 Ledger API，步骤同上一教程。）\n\n若两个 participant 连接同一 synchronizer，可在 Canton 控制台试验：用 participant1 为内部 Party 创建托管提议（无需外部签署拓扑），由 participant2 批准。",
        )
    out = chunk
    for en, zh in full:
        out = out.replace(en, zh)
    reps = [
        (r"^# Onboard External Party Using the Admin API\s*$", "# 使用 Admin API 入网外部 Party"),
        (
            r"^This tutorial demonstrates how to onboard",
            "本教程演示如何使用 **Admin API** 入网 **外部 Party**。外部 Party 可用自管密钥签署 Daml 交易而无需信任网络节点。建议先阅读外部签名概述；拓扑概念见拓扑教程",
        ),
        (
            r"^The tutorial illustrates the onboarding",
            "教程以名为 `Alice` 的 Party 为例，可重复该流程入网更多 Party",
        ),
        (
            r"^<Warning>\s*\n\s*This tutorial is for demo",
            "<Warning>\n  本教程仅供演示，代码片段请勿直接用于生产环境\n</Warning>",
        ),
        (r"^## Prerequisites\s*$", "## 前提条件"),
        (
            r"^For simplicity, this tutorial assumes",
            "为简化起见，假设最小 Canton 部署：一个 participant 连接一个 synchronizer（含 sequencer 与 mediator）",
        ),
        (
            r"^<Tip>\s*\n\s*If you already have",
            "<Tip>\n  若已有此类实例，可直接进入 Setup 节\n</Tip>",
        ),
        (
            r"^This configuration is not necessary",
            "该配置并非入网外部 Party 的硬性要求，但在提交外部签名交易时会需要",
        ),
        (r"^### Start Canton\s*$", "### 启动 Canton"),
        (
            r"^To obtain a Canton artifact",
            "获取 Canton 制品见 getting started。在制品目录执行：",
        ),
        (
            r"^Once the \"Welcome to Canton\"",
            "出现 “Welcome to Canton” 后即可继续",
        ),
        (r"^### Setup\s*$", "### 配置"),
        (
            r"^Navigate to the interactive submission",
            "进入 Canton 发行包中 `examples/08-interactive-submission` 目录",
        ),
        (
            r"^To proceed, gather the following",
            "在 Canton 控制台运行下列命令收集：",
        ),
        (r"^\* Participant Id\s*$", "* Participant Id"),
        (r"^\* Admin API endpoint\s*$", "* Admin API 端点"),
        (
            r"^In the rest of the tutorial",
            "下文示例值请替换为你自己的：",
        ),
        (r"^### API\s*$", "### API"),
        (
            r"^This tutorial interacts with the",
            "本教程使用 participant **Admin API** 上的 gRPC 服务 `TopologyManagerWriteService`，定义见外部签名拓扑交易教程",
        ),
        (
            r"^It uses Python to demonstrate",
            "使用 Python 演示入网流程",
        ),
        (
            r"^It is recommended to use a dedicated",
            "建议使用独立 Python 虚拟环境，避免依赖冲突，可使用 [venv](https://docs.python.org/3/library/venv.html)",
        ),
        (
            r"^Then run the setup script",
            "然后运行 setup 脚本生成与 Canton gRPC 交互所需的 Python 文件：",
        ),
        (r"^## Topology Mappings\s*$", "## 拓扑映射"),
        (
            r"^Onboarding an external party requires three",
            "入网外部 Party 需要三种拓扑映射：",
        ),
        (r"^## Signing Keys\s*$", "## 签名密钥"),
        (
            r"^Canton uses digital signatures",
            "Canton 用数字签名做认证。上一节中 `NamespaceDelegation` 与 `PartyToKeyMapping` 用于注册相应公钥。最佳实践是为不同用途使用不同密钥；本教程为简化使用同一密钥对",
        ),
        (r"^## Fingerprint\s*$", "## 指纹"),
        (
            r"^Canton uses fingerprints to efficiently",
            "Canton 用指纹高效标识签名密钥，详见拓扑教程指纹一节",
        ),
        (r"^## Party ID\s*$", "## Party ID"),
        (r"^A `Party ID` is composed", "`Party ID` 由两部分组成："),
        (r"^## External Party Onboarding Transactions\s*$", "## 外部 Party 入网交易"),
        (
            r"^Generate the three topology transactions",
            "生成入网 `Alice` 所需的三笔拓扑交易",
        ),
        (
            r"^This tutorial uses a single signing key",
            "本教程使用单一签名密钥，故除 `PartyToParticipant` 需托管 participant 签署外，各交易均仅用该密钥签名。生产环境使用多密钥时，每笔交易须用对应密钥签署：",
        ),
        (r"^## Multi Transaction Hash\s*$", "## 多交易哈希"),
        (
            r"^In order to reduce the number",
            "为减少签名次数，可合并三笔交易的哈希一次性签名；教程开头工具函数已提供 `compute_multi_transaction_hash`",
        ),
        (r"^## Signing\s*$", "## 签名"),
        (r"^First, sign the multi hash", "先用命名空间密钥签署 multi hash："),
        (
            r"^Then, build the `SignedTopologyTransaction`",
            "再构建 Topology API 所需的 `SignedTopologyTransaction` 消息：",
        ),
        (r"^## Submit\s*$", "## 提交"),
        (
            r"^Submit the transactions signed",
            "提交已由外部 Party 密钥签名的交易：",
        ),
        (r"^## Authorize PartyToParticipant Mapping\s*$", "## 授权 PartyToParticipant 映射"),
        (
            r"^The hosting participant must authorize",
            "托管 participant 须显式授权 PartyToParticipant 交易。本教程仅一个托管 participant，其授权即可完成入网。若有多个托管方，各方须分别授权，详见 party replication",
        ),
        (r"^## Observe Onboarded Party\s*$", "## 观察已入网 Party"),
        (
            r"^Finally, wait to observe the party",
            "最后在拓扑中等待观察到该 Party，确认创建成功：",
        ),
        (
            r"^`Alice` is now successfully onboarded",
            "`Alice` 已成功入网，可继续学习如何提交外部签名交易",
        ),
        (r"^## Tooling\s*$", "## 工具"),
        (
            r"^The scripts mentioned in this tutorial",
            "本教程脚本可用于测试与开发",
        ),
        (r"^### Onboard external party\s*$", "### 入网外部 party"),
        (
            r"^Create an external party on the ledger",
            "在账本创建外部 Party 并将公私钥写入本地 `der` 文件。默认从本目录 canton bootstrap 写入的文件读取 synchronizer ID 与 participant ID，可用 `--synchronizer-id` 与 `--participant-id` 覆盖",
        ),
        (r"^Output:\s*$", "输出："),
        (r"^## Advanced Onboarding Topics\s*$", "## 高级入网主题"),
        (r"^### Multi-Hosted Party\s*$", "### 多方托管 Party"),
        (
            r"^A multi hosted party is a party",
            "多方托管 Party 托管在多个 Participant 节点上。本教程为单 participant 简化环境，外部 Party 亦可多方托管",
        ),
        (
            r"^To create a multi-hosted external party",
            "创建多方托管外部 Party 时，在以上流程基础上做两处调整：",
        ),
        (r"^Example usage:\s*$", "示例用法："),
        (r"^### Offline party replication\s*$", "### 离线 Party 复制"),
        (
            r"^Offline party replication is the action",
            "离线 Party 复制是将已有 Party 复制到额外托管节点的复杂流程，详见离线 party replication 文档。本地与外部 Party 流程类似，但外部 Party 拓扑变更须用拓扑交易签名显式授权",
        ),
        (
            r"^For a complete example demonstrating",
            "完整多方托管外部 Party 示例见：",
        ),
        (r"^# Onboard External Party\s*$", "# 使用 Ledger API 入网外部 Party"),
        (
            r"^This tutorial demonstrates how to onboard an \*\*external party\*\* using the Ledger API\.$",
            "本教程演示如何使用 **Ledger API** 入网 **外部 Party**",
        ),
        (r"^## Run The Script\s*$", "## 运行脚本"),
        (
            r"^The steps of this tutorial are included",
            "本教程步骤包含在制品 `examples/08-interactive-submission/external_party_onboarding.sh` 中，涵盖：",
        ),
        (r"^\* Create a private key", "* 用 openssl 为外部 Party 创建私钥"),
        (r"^\* Determine the synchronizer-id", "* 确定可用 synchronizer-id"),
        (r"^\* Create a set of topology", "* 创建定义新外部 Party 的拓扑交易集"),
        (r"^\* Sign the topology transactions", "* 签署拓扑交易"),
        (r"^\* Upload the signed topology", "* 将已签拓扑交易上传到 Ledger API"),
        (
            r"^Make sure to run the script",
            "请在启动 Canton 的同一目录运行脚本以便读取 `canton_ports.json`，或用 `-p1 <host>:<port>` 指定 Ledger API 地址",
        ),
        (r"^Once you start it", "启动后示例输出："),
        (
            r"^Note that the script supports",
            "脚本支持若干命令行参数，见源码",
        ),
        (r"^## The Details of the Script\s*$", "## 脚本细节"),
        (
            r"^First, the script determines the available",
            "脚本先用 `v2/connected-synchronizers` 获取 synchronizer-id（假设仅一个）。Party 须在欲托管的每个 synchronizer 上重复分配",
        ),
        (
            r"^Next, openssl is used to create",
            "接着用 openssl 创建外部 Party 的 Ed25519 私钥（亦支持其他密钥类型），导出 DER 公钥并转 base64",
        ),
        (
            r"^The script uses the convenience endpoint",
            "脚本使用便捷端点 `/v2/parties/external/generate-topology` 生成拓扑交易（节点可信时可用；否则应手工构建或签署前检查并自行重算哈希）",
        ),
        (
            r"^The convenience endpoint returns",
            "便捷端点返回拓扑交易、新 Party 的 party-id、公钥指纹及 multi-hash（对整个交易集的承诺）",
        ),
        (
            r"^This hash needs to be signed",
            "该哈希须由新 Party 私钥签署；脚本用 openssl 签名并转 base64",
        ),
        (
            r"^Using the signature and the data",
            "用签名与前述数据向 Ledger API 提交以完成入网：",
        ),
        (
            r"^The transactions can be signed one by one",
            "交易可逐笔签署，也可像脚本中一样对合并哈希一次性签署",
        ),
        (r"^# Onboard Multi-Hosted External Party\s*$", "# 入网多方托管外部 Party"),
        (
            r"^This tutorial demonstrates how to onboard an \*\*external party\*\* using the Ledger API which is hosted",
            "本教程演示如何使用 Ledger API 入网托管在**多个验证者**上的外部 Party，是上一教程的简单扩展",
        ),
        (
            r"^Make sure that you have completed",
            "请先完成「入网外部 Party」教程并保留运行中的 Canton 示例",
        ),
        (
            r"^The example script used in the previous",
            "上一教程脚本亦支持多方托管，默认加 `--multi-hosted` 会在两个节点入网",
        ),
        (
            r"^You can try this out on the Canton console",
            "若两个 participant 连接同一 synchronizer，可在 Canton 控制台试验：用 participant1 为内部 Party 创建托管提议（无需外部签署拓扑），participant2 批准",
        ),
        (r"^First, create a hosting proposal", "先用 participant1 创建托管提议："),
        (
            r"^Then, list the proposals on participant2",
            "在 participant2 列出提议，新提议会很快出现：",
        ),
        (
            r"^This will show the pending proposal",
            "显示待批准提议，等待第二 participant 签名；可从上一命令输出取得 `txHash`：",
        ),
        (
            r"^Authorize the proposal using the console",
            "用 `topology.transactions.authorize` 授权：",
        ),
        (
            r"^This will add the signature of participant2",
            "为提议加上 participant2 签名；完全签署后 Party 会出现在两节点：",
        ),
    ]
    out = chunk
    for pat, repl in reps:
        out = re.sub(pat, repl, out, flags=re.MULTILINE)
    return out


def translate_topology_prose(chunk: str) -> str:
    reps = [
        (r"^# Externally Signed Topology Transactions\s*$", "# 外部签署的拓扑交易"),
        (
            r"^Canton's \[Topology\]",
            "Canton [拓扑](/overview/reference/topology) 形式化 synchronizer 上的共享状态，并提供安全的分布式变更机制",
        ),
        (
            r"^This tutorial demonstrates how to build",
            "本教程演示如何构建、签署并提交拓扑交易，适用于签名密钥在网外的场景，例如外部 Party 入网或 participant 根命名空间初始化。流程以导入根命名空间委托为例，可推广到任意拓扑映射",
        ),
        (
            r"^<Warning>\s*\n\s*This tutorial is for demo",
            "<Warning>\n  本教程仅供演示，代码片段请勿直接用于生产\n</Warning>",
        ),
        (r"^## Prerequisites\s*$", "## 前提条件"),
        (
            r"^For simplicity, this tutorial assumes",
            "为简化起见，假设一个 participant 连接一个 synchronizer",
        ),
        (r"^### Start Canton\s*$", "### 启动 Canton"),
        (
            r"^To obtain a Canton artifact",
            "获取 Canton 制品见 getting started，执行：",
        ),
        (
            r"^Once the \"Welcome to Canton\"",
            "出现 “Welcome to Canton” 后继续",
        ),
        (r"^### Setup\s*$", "### 配置"),
        (
            r"^Navigate to the interactive submission",
            "进入发行包 `examples/08-interactive-submission`",
        ),
        (
            r"^<Tip>\s*\n\s*The code examples",
            "<Tip>\n  本教程代码摘自该目录脚本\n</Tip>",
        ),
        (
            r"^To proceed, gather the following",
            "在 Canton 控制台收集：",
        ),
        (r"^\* Admin API endpoint\s*$", "* Admin API 端点"),
        (r"^\* Synchronizer ID\s*$", "* Synchronizer ID"),
        (
            r"^In the rest of the tutorial we use",
            "下文示例值请替换为你自己的：",
        ),
        (r"^### API\s*$", "### API"),
        (
            r"^This tutorial interacts with the",
            "本教程使用 participant **Admin API** 的 `TopologyManagerWriteService` gRPC 服务，假设 Admin API 未启用客户端证书认证",
        ),
        (r"^### Python\s*$", "### Python"),
        (
            r"^It is recommended to use a dedicated",
            "建议使用独立 Python 虚拟环境，见 [venv](https://docs.python.org/3/library/venv.html)",
        ),
        (
            r"^Then run the setup script",
            "运行 setup 脚本生成 Python gRPC 绑定：",
        ),
        (r"^Finally, the following imports", "最后需要以下 import："),
        (r"^### Shell\s*$", "### Shell"),
        (r"^For a terminal-based approach", "终端方式请安装："),
        (
            r"^The tutorial uses a buf proto image",
            "教程使用 buf proto 镜像（反）序列化 proto 消息",
        ),
        (
            r"^The following functions will be used",
            "教程将使用以下 shell 函数：",
        ),
        (r"^### Error Handling\s*$", "### 错误处理"),
        (
            r"^When encountering RPC errors",
            "遇到 RPC 错误时可能需要额外反序列化以获取可操作信息。RPC 错误示例：",
        ),
        (
            r"^The `type` field specifies",
            "`type` 指明错误 protobuf 类型。下列工具代码可提取有用信息",
        ),
        (r"^Bash\s*$", "Bash"),
        (r"^Python\s*$", "Python"),
        (r"^## 1\. Signing Keys\s*$", "## 1. 签名密钥"),
        (
            r"^First, generate an external signing key",
            "首先生成外部签名密钥对供本教程使用",
        ),
        (r"^## 2\. Hash\s*$", "## 2. 哈希"),
        (
            r"^Hashing is required at several steps",
            "若干步骤需对字节序列哈希。过程使用底层算法，并在输入与最终哈希上加特定前缀：",
        ),
        (
            r"^1\. A hash purpose \(a 4-byte",
            "1. 在字节序列前加 hash purpose（4 字节整数），取值定义于 Canton 代码库",
        ),
        (r"^2\. The resulting data is hashed", "2. 对结果数据用底层算法哈希"),
        (
            r"^3\. The final multihash is prefixed",
            "3. 最终 multihash 再按 [multi-codec](https://github.com/multiformats/multicodec) 加两字节前缀：",
        ),
        (r"^\* The identifier for the hash", "* 所用哈希算法标识"),
        (r"^\* The length of the hash\.\s*$", "* 哈希长度"),
        (
            r"^<Tip>\s*\n\s*For most practical",
            "<Tip>\n  多数场景可用 SHA-256 作为底层算法，本教程亦如此\n</Tip>",
        ),
        (r"^## 3\. Fingerprint\s*$", "## 3. 指纹"),
        (
            r"^Canton uses fingerprints to efficiently",
            "Canton 用指纹标识签名密钥；指纹为公钥哈希。用前述算法计算，指纹的 hash purpose 为 `12`",
        ),
        (
            r"^<Tip>\s*\n\s*The scripts in this tutorial",
            "<Tip>\n  本教程脚本可快速验证第三方哈希/签名实现，例如对 base64 公钥输出有效指纹\n</Tip>",
        ),
        (r"^## 4\. Namespace Delegation Mapping\s*$", "## 4. 命名空间委托映射"),
        (
            r"^There is a number of different mappings",
            "有多种拓扑映射，各建模拓扑状态的一部分",
        ),
        (
            r"^This tutorial illustrates the process",
            "本教程以导入根 `NamespaceDelegation` 为例，流程可推广到任意映射",
        ),
        (
            r"^The Namespace Delegation mapping requires",
            "Namespace Delegation 映射需要三个值：",
        ),
        (r"^1\. `namespace`: Root key's fingerprint", "1. `namespace`：根密钥指纹"),
        (
            r"^2\. `target_key`: Public key expected",
            "2. `target_key`：委托使用的公钥。根命名空间委托为自签",
        ),
        (r"^3\. `is_root_delegation`:", "3. `is_root_delegation`：根委托为 `true`"),
        (r"^## 5\. Topology Transaction\s*$", "## 5. 拓扑交易"),
        (
            r"^The topology state is scoped to a synchronizer",
            "拓扑状态作用于 synchronizer。各 synchronizer 支持特定 Canton 协议版本（Protocol Version），使用拓扑 API 时须选择目标 synchronizer",
        ),
        (
            r"^Once a synchronizer is selected",
            "选定 synchronizer 后，可通过 sequencer API 的 `SequencerConnectService#GetSynchronizerParameters` 获取其 `ProtocolVersion`",
        ),
        (
            r"^The Canton console on a sequencer",
            "在目标 synchronizer 的 sequencer 节点上，Canton 控制台也可查询：",
        ),
        (
            r"^Each `Protocol Version` has a corresponding",
            "各 `Protocol Version` 对应 Canton 协议涉及 protobuf 的 `Protobuf Version`，包括 `TopologyTransaction`",
        ),
        (r"^\| Protocol Version \| Topology", "| 协议版本 | 拓扑交易 Protobuf 版本 |"),
        (
            r"^<Note>\s*\n\s*The versioning of protobuf",
            "<Note>\n  protobuf 消息版本相对稳定，下文假设 protobuf 版本为 `30`\n</Note>",
        ),
        (r"^Topology transactions consist of three", "拓扑交易由三部分组成："),
        (r"^### Topology Mapping\s*$", "### 拓扑映射"),
        (r"^See the Namespace Delegation Mapping", "见命名空间委托映射一节"),
        (r"^### Serial\s*$", "### Serial"),
        (
            r"^The `serial` is a monotonically",
            "`serial` 为从 1 起单调递增的序号。创建、替换或删除唯一拓扑映射的交易须将 serial 设为该映射上一笔已接受交易 serial 加 1。唯一性因映射而异，见各映射 protobuf。这可避免并发更新同一映射时相互覆盖。查询现有 serial 请用 `TopologyManagerReadService` 列出相关映射",
        ),
        (
            r"^In this tutorial, it is assumed",
            "本教程假设新建的 `NamespaceDelegation` 尚无既有根委托，故 serial 设为 1",
        ),
        (
            r"^<Tip>\s*\n\s*For an example of how to read",
            "<Tip>\n  读取并递增 serial 的示例见外部 Party 入网教程\n</Tip>",
        ),
        (r"^### Operation\s*$", "### 操作"),
        (r"^There are two operations possible:", "两种操作："),
        (r"^\* `ADD_REPLACE`:", "* `ADD_REPLACE`：新增或替换映射"),
        (r"^\* `REMOVE`:", "* `REMOVE`：删除既有映射"),
        (r"^## 6\. Version Wrapper\s*$", "## 6. 版本包装"),
        (
            r"^In order to guarantee backwards compatibility",
            "为保证 protobuf 变更时的向后兼容，Canton 用包装消息包含与消息绑定的 protobuf 版本",
        ),
        (r"^\* `data`: serialized protobuf", "* `data`：序列化的拓扑交易"),
        (r"^\* `version`: protobuf version", "* `version`：拓扑交易的 protobuf 版本"),
        (
            r"^Wrap the serialized transaction",
            "将序列化交易包入 `UntypedVersionedMessage` 并序列化结果：",
        ),
        (r"^## 7\. Transaction Hash\s*$", "## 7. 交易哈希"),
        (
            r"^The next step is to compute the hash",
            "下一步计算交易哈希：对版本化交易的序列化 protobuf 使用前文哈希函数，此次 hash purpose 为 `11`",
        ),
        (
            r"^<Tip>\s*\n\s*To facilitate steps",
            "<Tip>\n  步骤 5–7 可用拓扑 API 的 `GenerateTransactions` RPC 生成序列化版本化交易及其哈希；使用时强烈建议反序列化返回交易、校验内容并**重新计算哈希**，以防生成方误用或恶意行为\n</Tip>",
        ),
        (r"^## 8\. Signature\s*$", "## 8. 签名"),
        (
            r"^The hash is now ready to be signed",
            "哈希现可签署。根命名空间交易仅涉及一个密钥；其他映射可能需额外签名（如 `OwnerToKeyMapping` 中的密钥，或 `PartyToParticipant` 的多方授权规则）。所有交易均须由目标命名空间的根密钥或经 `NamespaceDelegation` 注册的委托密钥签署；各映射授权规则见 protobuf，超出本教程范围",
        ),
        (
            r"^<Tip>\s*\n\s*The topology API allows",
            "<Tip>\n  拓扑 API 可用单一哈希认证多笔交易，见外部签名入网教程\n</Tip>",
        ),
        (r"^Sign the hash with the private key:", "用私钥签署哈希："),
        (r"^## 9\. Submit the transaction\s*$", "## 9. 提交交易"),
        (
            r"^Submit the transaction and its signature",
            "通过 `TopologyManagerWriteService` 的 `AddTransactions` RPC 提交交易与签名：",
        ),
        (
            r"^If everything goes well",
            "成功时应显示 `Transaction submitted successfully`",
        ),
        (r"^### Proposal\s*$", "### Proposal"),
        (
            r"^The `SignedTopologyTransaction` message contains",
            "`SignedTopologyTransaction` 含布尔字段 `proposal`：为 true 时可提交尚未集齐全部所需签名的拓扑交易，便于需多方签名的场景",
        ),
        (r"^## 10\. Observe the transaction\s*$", "## 10. 观察交易"),
        (
            r"^The last step of the tutorial is to observe",
            "最后一步是在 synchronizer 拓扑状态中观察 `NamespaceDelegation`。提交是异步的，可能需要等待",
        ),
        (
            r"^This concludes the tutorial",
            "教程结束，交易已在 synchronizer 拓扑状态中生效。代码位于 `examples/08-interactive-submission`，可运行：",
        ),
    ]
    out = chunk
    for pat, repl in reps:
        out = re.sub(pat, repl, out, flags=re.MULTILINE)
    return out


def build_body(slug: str, intro: str, translate_fn) -> str:
    raw = (EN / f"{slug}.md").read_text(encoding="utf-8")
    stripped = strip_en(raw, intro)
    out_parts: list[str] = []
    for seg, is_code in split_codeblock_segments(stripped):
        if is_code:
            out_parts.append(seg)
        else:
            out_parts.append(translate_fn(seg))
    return "".join(out_parts).strip() + "\n"


def main() -> None:
    specs = [
        (
            "appdev-deep-dives-external-signing-hashing-algorithm",
            "> 外部签名所用 PreparedTransaction 的确定性哈希规范（V2）。",
            translate_hashing_prose,
        ),
        (
            "appdev-deep-dives-external-signing-onboarding",
            "> 通过 Admin API 或 Ledger API 入网外部 Party 并签署拓扑交易。",
            translate_onboarding_prose,
        ),
        (
            "appdev-deep-dives-external-signing-topology",
            "> 使用外部密钥构建、签署并提交 Canton 拓扑交易。",
            translate_topology_prose,
        ),
    ]
    for slug, intro, fn in specs:
        body = polish_body(build_body(slug, intro, fn))
        path = OUT / f"{slug}.body.md"
        path.write_text(body, encoding="utf-8")
        print("generated", path.name, len(body))


if __name__ == "__main__":
    main()
