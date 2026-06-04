#!/usr/bin/env python3
"""Write batch 25 GS zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_25 = [
    "global-synchronizer-extension-synchronizers-other-private-synchronizers",
    "global-synchronizer-extension-synchronizers-private-synchronizers",
    "global-synchronizer-extension-synchronizers-private-validators",
    "global-synchronizer-extension-synchronizers-synchronizer-monitoring",
    "global-synchronizer-extension-synchronizers-synchronizer-operations",
    "global-synchronizer-faq",
    "global-synchronizer-production-operations-canton-console",
    "global-synchronizer-production-operations-decommission-nodes",
    "global-synchronizer-production-operations-disaster-recovery",
    "global-synchronizer-production-operations-key-management",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-extension-synchronizers-other-private-synchronizers": (
        "独立私有同步器",
        "不连接全局同步器、完全独立运行的私有 Canton 同步器部署与取舍。",
        "独立于全局同步器运行的私有 Canton 同步器。",
    ),
    "global-synchronizer-extension-synchronizers-private-synchronizers": (
        "私有同步器",
        "与全局同步器并行的扩展同步器：隐私、性能、治理与连接方式。",
        "与全局同步器并行运行的私有（扩展）同步器。",
    ),
    "global-synchronizer-extension-synchronizers-private-validators": (
        "私有同步器上的验证者",
        "仅连接私有同步器、无需全局同步器连接的验证者部署与选型。",
        "仅在私有同步器上运行、不连接全局同步器的验证者。",
    ),
    "global-synchronizer-extension-synchronizers-synchronizer-monitoring": (
        "同步器监控",
        "Sequencer/Mediator 健康检查、裁决（verdict）检查与故障排查。",
        "Sequencer 与 Mediator 节点健康监控与检查。",
    ),
    "global-synchronizer-extension-synchronizers-synchronizer-operations": (
        "同步器运维",
        "集中式/去中心化同步器引导、拓扑、参数与日常运维操作。",
        "引导、配置与运维 Canton 同步器节点。",
    ),
    "global-synchronizer-faq": (
        "常见问题",
        "验证者、超级验证者与 JSON API 等 Canton Network 运维常见问题。",
        "Canton Network 验证者与超级验证者常见问题解答。",
    ),
    "global-synchronizer-production-operations-canton-console": (
        "高级 Canton Console",
        "Canton 管理控制台：远程管理、节点引用、超时与 gRPC 管理 API。",
        "使用 Canton 管理控制台进行高级节点运维。",
    ),
    "global-synchronizer-production-operations-decommission-nodes": (
        "下线 Canton 节点",
        "参与方节点与同步器实体下线的前置条件与不可逆注意事项。",
        "Canton 节点与同步器实体下线流程。",
    ),
    "global-synchronizer-production-operations-disaster-recovery": (
        "灾难恢复",
        "数据损坏恢复、SV 完整节点还原与通过验证者找回 Amulet。",
        "数据损坏、SV 重新入驻与 CometBFT 层丢失的恢复步骤。",
    ),
    "global-synchronizer-production-operations-key-management": (
        "密钥管理",
        "节点密钥列举、轮换、生成、停用、删除与密码方案配置。",
        "Canton 节点加密密钥的管理与限制。",
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
    ("Synchronizer", "同步器"),
    ("synchronizer", "同步器"),
    ("Canton Coin", "Canton Coin"),
    ("Canton Network", "Canton Network"),
    ("Ledger API", "Ledger API"),
    ("DevNet", "DevNet"),
    ("TestNet", "TestNet"),
    ("MainNet", "MainNet"),
    ("Sequencer", "Sequencer"),
    ("Mediator", "Mediator"),
    ("Validator", "验证者"),
    ("validator", "验证者"),
    ("validators", "验证者"),
    ("wallet", "钱包"),
    ("Wallet", "钱包"),
    ("traffic", "流量"),
    ("Traffic", "流量"),
    ("onboarding", "入驻"),
    ("Onboarding", "入驻"),
    ("Party", "Party"),
    ("Helm", "Helm"),
    ("Kubernetes", "Kubernetes"),
    ("gRPC", "gRPC"),
    ("PostgreSQL", "PostgreSQL"),
    ("Canton Console", "Canton Console"),
    ("Daml", "Daml"),
    ("topology", "拓扑"),
    ("Topology", "拓扑"),
    ("reassignment", "重分配"),
    ("Reassignment", "重分配"),
    ("unassignment", "取消分配"),
    ("Canton", "Canton"),
    ("Amulet", "Amulet"),
    ("amulet", "amulet"),
    ("KMS", "KMS"),
    ("CometBFT", "CometBFT"),
    ("OIDC", "OIDC"),
    ("JSON API", "JSON API"),
    ("PQS", "PQS"),
    ("ACS", "ACS"),
    ("verdict", "裁决"),
    ("Verdict", "裁决"),
    ("BFT", "BFT"),
    ("pruning", "修剪"),
    ("Pruning", "修剪"),
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


def translate_chunk(chunk: str, retries: int = 5) -> str:
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
            time.sleep(2**attempt)
    raise RuntimeError(f"translate failed: {last_err}")


def translate_body(body: str) -> str:
    chunks = chunk_text(body)
    out: list[str] = []
    for i, ch in enumerate(chunks):
        print(f"    chunk {i + 1}/{len(chunks)} ({len(ch)} chars)", flush=True)
        out.append(translate_chunk(ch))
        if i < len(chunks) - 1:
            time.sleep(0.5)
    result = "".join(out)
    for en, zh in TERM_FIXES:
        result = result.replace(en, zh)
    return result


def write_slug(slug: str, force: bool = False) -> bool:
    out_path = OUT_DIR / f"{slug}.json"
    if out_path.exists() and out_path.stat().st_size > 800 and not force:
        print(f"  skip (exists): {slug}", flush=True)
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
    force = "--force" in sys.argv
    n = 0
    print(f"=== batch 25 ({len(BATCH_25)} slugs) ===", flush=True)
    for slug in BATCH_25:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 25 count: {n}", flush=True)


if __name__ == "__main__":
    main()
