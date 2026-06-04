#!/usr/bin/env python3
"""Write batches 18–20 overview zh-cursor JSON (EN → zh-CN, code preserved)."""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

BATCHES: dict[str, list[str]] = {
    "18": [
        "overview-reference-ledger-model-detailed",
        "overview-reference-ordering-consensus",
        "overview-reference-pruning",
        "overview-reference-reassignment-protocol",
        "overview-reference-smart-contract-consensus",
        "overview-reference-splice-wallet-reference",
        "overview-reference-super-validator-components",
        "overview-reference-sv-governance-reference",
        "overview-reference-synchronizer-overview",
        "overview-reference-tokenomics-of-gs",
    ],
    "19": [
        "overview-reference-topology",
        "overview-reference-transaction-lifecycle",
        "overview-reference-validator-node-components",
        "overview-reference-what-are-cips",
        "overview-understand-canton-coin",
        "overview-understand-cantons-solution",
        "overview-understand-cips-introduction",
        "overview-understand-core-concepts",
        "overview-understand-five-minute-overview",
        "overview-understand-getting-app-featured",
    ],
    "20": [
        "overview-understand-global-synchronizer",
        "overview-understand-glossary",
        "overview-understand-the-problem",
        "overview-understand-use-cases",
        "overview-understand-what-is-canton",
        "overview-understand-who-should-read",
    ],
}

META: dict[str, tuple[str, str, str]] = {
    "overview-reference-ledger-model-detailed": (
        "账本模型（详解）",
        "Canton 账本模型详解：合约、交易、授权、隐私视图与多同步器语义。",
        "Canton 账本模型参考：合约生命周期、交易结构与隐私规则。",
    ),
    "overview-reference-ordering-consensus": (
        "排序与共识",
        "全局同步器上的排序协议、BFT 共识与 Sequencer/Mediator 角色。",
        "Canton 排序层与拜占庭容错共识机制说明。",
    ),
    "overview-reference-pruning": (
        "修剪（Pruning）",
        "参与方与同步器节点的数据修剪策略、保留窗口与运维注意事项。",
        "Canton 数据修剪与历史保留策略参考。",
    ),
    "overview-reference-reassignment-protocol": (
        "重分配协议",
        "合约在参与方节点间迁移（reassignment）的协议步骤与安全保证。",
        "Canton 合约重分配（跨参与方迁移）协议参考。",
    ),
    "overview-reference-smart-contract-consensus": (
        "智能合约共识",
        "Daml 交易在参与方侧的验证、视图分解与合约级共识流程。",
        "Canton 智能合约（Daml）侧共识与验证流程。",
    ),
    "overview-reference-splice-wallet-reference": (
        "Splice 钱包参考",
        "Splice 参考钱包架构、Amulet/CC 持有与转账相关合约与 API。",
        "Global Synchronizer 上 Splice 参考钱包技术说明。",
    ),
    "overview-reference-super-validator-components": (
        "超级验证者组件",
        "SV 节点组成：Sequencer、Mediator、治理与 DSO 相关服务。",
        "超级验证者（Super Validator）基础设施组件参考。",
    ),
    "overview-reference-sv-governance-reference": (
        "SV 治理参考",
        "超级验证者治理流程、投票、参数变更与 Canton Foundation 政策接口。",
        "Global Synchronizer 超级验证者治理机制参考。",
    ),
    "overview-reference-synchronizer-overview": (
        "同步器概览",
        "Synchronizer 在 Canton 中的角色：排序、调解、与参与方节点的关系。",
        "Canton Synchronizer（同步器）架构与职责概览。",
    ),
    "overview-reference-tokenomics-of-gs": (
        "全局同步器代币经济学",
        "Canton Coin、Traffic 费用、验证者奖励与 GS 经济激励设计。",
        "Global Synchronizer 代币经济学（Canton Coin / Traffic）参考。",
    ),
    "overview-reference-topology": (
        "拓扑",
        "Canton 拓扑状态：参与方、同步器连接、权限与拓扑事务生命周期。",
        "Canton 网络拓扑模型与拓扑管理参考。",
    ),
    "overview-reference-transaction-lifecycle": (
        "交易生命周期",
        "从命令提交到确认、同步器排序、参与方验证与最终性的完整流程。",
        "Canton 交易端到端生命周期参考。",
    ),
    "overview-reference-validator-node-components": (
        "验证者节点组件",
        "Validator 参与方节点内部模块：Ledger API、同步、存储与运维接口。",
        "Canton 验证者（参与方）节点组件架构参考。",
    ),
    "overview-reference-what-are-cips": (
        "什么是 CIP",
        "Canton 改进提案（CIP）流程、编号规范与已发布 CIP 索引说明。",
        "Canton Improvement Proposal（CIP）介绍与索引。",
    ),
    "overview-understand-canton-coin": (
        "Canton Coin",
        "Canton Coin（CC）用途：Traffic 费用、验证者奖励与网络治理参与。",
        "Global Synchronizer 原生代币 Canton Coin 概念说明。",
    ),
    "overview-understand-cantons-solution": (
        "Canton 的解决方案",
        "Canton 如何通过子交易隐私与同步器架构化解完整性与隐私的矛盾。",
        "Canton 对区块链「透明 vs 隐私」根本张力的架构性解答。",
    ),
    "overview-understand-cips-introduction": (
        "CIP 简介",
        "CIP 在生态中的角色：标准互操作、钱包与代币规范等。",
        "面向开发者的 Canton Improvement Proposal（CIP）入门。",
    ),
    "overview-understand-core-concepts": (
        "核心概念",
        "Party、Contract、Synchronizer、Validator 等 Canton 基础术语与关系。",
        "Canton Network 核心概念速览。",
    ),
    "overview-understand-five-minute-overview": (
        "五分钟概览",
        "五分钟了解 Canton：隐私、同步器、Daml 与 Global Synchronizer 要点。",
        "Canton Network 五分钟快速入门。",
    ),
    "overview-understand-getting-app-featured": (
        "应用上架与推广",
        "在 Canton 生态展示应用的要求、申请流程与最佳实践。",
        "如何让应用在 Canton Network 生态中获得展示与推广。",
    ),
    "overview-understand-global-synchronizer": (
        "全局同步器",
        "Global Synchronizer 的定位、SV 运营、Canton Coin 与开放参与方式。",
        "Canton Network 公共协调层 Global Synchronizer 说明。",
    ),
    "overview-understand-glossary": (
        "术语表",
        "Canton Network 权威术语表：ACS、Party、Synchronizer、Traffic 等。",
        "Canton Network 概念与术语权威参考。",
    ),
    "overview-understand-the-problem": (
        "Canton 要解决的问题",
        "公链全局可见性带来的抢跑、合规与商业机密风险，及常见折中方案的局限。",
        "区块链「透明 vs 隐私」矛盾与 Canton 的切入点。",
    ),
    "overview-understand-use-cases": (
        "用例",
        "DvP、代币化证券、跨组织工作流等 Canton 隐私模型擅长的场景。",
        "Canton 隐私架构适用的典型业务用例。",
    ),
    "overview-understand-what-is-canton": (
        "什么是 Canton Network",
        "Canton Network 定位：子交易隐私、同步器架构、Daml 与生态组件。",
        "Canton Network 是什么、与公链有何不同、何时适合使用。",
    ),
    "overview-understand-who-should-read": (
        "谁应阅读本文档",
        "按角色（开发者、运维、架构师）与目标选择 Canton 文档入口。",
        "根据角色与目标选择 Canton 文档阅读路径。",
    ),
}

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")

translator = GoogleTranslator(source="en", target="zh-CN")

TERM_FIXES: list[tuple[str, str]] = [
    ("Global Synchronizer", "全局同步器"),
    ("global synchronizer", "全局同步器"),
    ("Super Validator", "超级验证者"),
    ("super validator", "超级验证者"),
    ("Super Validators", "超级验证者"),
    ("Participant Node", "参与方节点"),
    ("participant node", "参与方节点"),
    ("Participant Nodes", "参与方节点"),
    ("Synchronizer", "同步器"),
    ("synchronizer", "同步器"),
    ("Canton Coin", "Canton Coin"),
    ("Canton Network", "Canton Network"),
    ("Canton Foundation", "Canton Foundation"),
    ("Ledger API", "Ledger API"),
    ("Active Contract Set", "活跃合约集"),
    ("sub-transaction privacy", "子交易隐私"),
    ("Delivery vs. Payment", "货银对付（DvP）"),
    ("Zero-Knowledge", "零知识"),
]


def strip_en(md: str) -> str:
    md = FRONTMATTER_RE.sub("", md)
    md = DOC_INDEX_RE.sub("", md)
    md = FOOTER_RE.sub("", md)
    lines = md.splitlines()
    out: list[str] = []
    skip = False
    for i, line in enumerate(lines):
        if i < 8 and (
            line.startswith("# ")
            or (line.startswith("> ") and "llms.txt" in line)
            or line.startswith("> ## Documentation Index")
        ):
            if line.startswith("> ## Documentation Index"):
                skip = True
            continue
        if skip and line.startswith("> "):
            skip = False
            continue
        if line.startswith("> ") and "llms.txt" in line:
            continue
        out.append(line)
    text = "\n".join(out).strip()
    text = re.sub(r"^# [^\n]+\n\n# [^\n]+\n\n", "", text, count=1)
    text = re.sub(r"^# [^\n]+\n\n", "", text, count=1)
    return text.strip()


def mask_protected(text: str) -> tuple[str, list[str]]:
    tokens: list[str] = []

    def protect(regex: re.Pattern[str], s: str) -> str:
        def repl(m: re.Match[str]) -> str:
            tokens.append(m.group(0))
            return f"⟦P{len(tokens) - 1}⟧"

        return regex.sub(repl, s)

    masked = protect(CODE_FENCE, text)
    masked = protect(INLINE_CODE, masked)
    return masked, tokens


def unmask(text: str, tokens: list[str]) -> str:
    for i, val in enumerate(tokens):
        text = text.replace(f"⟦P{i}⟧", val)
    return text


def chunk_text(text: str, max_len: int = 4500) -> list[str]:
    parts = re.split(r"(\n{2,})", text)
    chunks: list[str] = []
    current = ""
    for part in parts:
        if len(current) + len(part) > max_len and current.strip():
            chunks.append(current)
            current = part
        else:
            current += part
    if current.strip():
        chunks.append(current)
    return chunks if chunks else [text]


def translate_chunk(chunk: str, retries: int = 3) -> str:
    chunk = chunk.strip()
    if not chunk:
        return chunk
    letters = sum(c.isalpha() for c in chunk)
    if letters < 20:
        return chunk
    masked, tokens = mask_protected(chunk)
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            translated = translator.translate(masked)
            return unmask(translated, tokens)
        except Exception as e:
            last_err = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"translate failed: {last_err}")


def translate_body(body: str) -> str:
    chunks = chunk_text(body)
    out: list[str] = []
    for i, ch in enumerate(chunks):
        out.append(translate_chunk(ch))
        if i < len(chunks) - 1:
            time.sleep(0.4)
    result = "".join(out)
    for en, zh in TERM_FIXES:
        result = result.replace(en, zh)
    return result


def write_slug(slug: str, force: bool = False) -> bool:
    out_path = OUT_DIR / f"{slug}.json"
    if out_path.exists() and out_path.stat().st_size > 800 and not force:
        return True
    en_path = EN_DIR / f"{slug}.md"
    if not en_path.exists():
        print(f"missing EN: {slug}", file=sys.stderr)
        return False
    zh_title, summary, intro = META[slug]
    en_body = strip_en(en_path.read_text(encoding="utf-8"))
    print(f"  translating {slug} ({len(en_body)} chars)...", flush=True)
    zh_body = translate_body(en_body)
    payload = {
        "zhTitle": zh_title,
        "summary": summary,
        "body": f"> {intro}\n\n{zh_body}",
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  wrote {out_path.name} ({len(payload['body'])} chars)", flush=True)
    return True


def main() -> None:
    batches = sys.argv[1:] if len(sys.argv) > 1 else ["18", "19", "20"]
    counts: dict[str, int] = {}
    for batch_id in batches:
        slugs = BATCHES.get(batch_id, [])
        n = 0
        print(f"=== batch {batch_id} ({len(slugs)} slugs) ===", flush=True)
        for slug in slugs:
            if write_slug(slug):
                n += 1
            time.sleep(0.3)
        counts[batch_id] = n
        print(f"batch {batch_id} count: {n}", flush=True)
    print("counts:", counts)


if __name__ == "__main__":
    main()
