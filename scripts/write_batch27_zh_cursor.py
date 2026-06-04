#!/usr/bin/env python3
"""Write batch 27 GS production-ops zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_27 = [
    "global-synchronizer-production-operations-scalability",
    "global-synchronizer-production-operations-splice-metrics-overview",
    "global-synchronizer-production-operations-sv-backup",
    "global-synchronizer-production-operations-sv-pruning",
    "global-synchronizer-production-operations-sv-security",
    "global-synchronizer-production-operations-sv-upgrades",
    "global-synchronizer-production-operations-upgrade-canton-nodes",
    "global-synchronizer-production-operations-validator-backups",
    "global-synchronizer-production-operations-validator-disaster-recovery",
    "global-synchronizer-production-operations-validator-security",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-production-operations-scalability": (
        "网络可扩展性",
        "Canton Network 节点的扩展特性、Party 数量限制与调优建议。",
        "Canton Network 节点的扩展特性与调优指南。",
    ),
    "global-synchronizer-production-operations-splice-metrics-overview": (
        "Splice 指标概览",
        "Canton Network 各组件暴露的 Prometheus 指标及抓取方式。",
        "Canton Network 组件的 Prometheus 指标与抓取说明。",
    ),
    "global-synchronizer-production-operations-sv-backup": (
        "超级验证者备份",
        "超级验证者节点身份、数据库与 CometBFT 的备份流程。",
        "超级验证者节点的备份流程。",
    ),
    "global-synchronizer-production-operations-sv-pruning": (
        "超级验证者修剪",
        "超级验证者节点上 Sequencer 与 CometBFT 的修剪配置。",
        "超级验证者节点 Sequencer 与 CometBFT 修剪。",
    ),
    "global-synchronizer-production-operations-sv-security": (
        "超级验证者安全",
        "超级验证者节点安全加固、KMS 配置与第三方 Daml 应用说明。",
        "超级验证者节点安全加固与 KMS 配置。",
    ),
    "global-synchronizer-production-operations-sv-upgrades": (
        "超级验证者升级",
        "超级验证者节点的小版本升级流程与注意事项。",
        "超级验证者节点的小版本升级流程。",
    ),
    "global-synchronizer-production-operations-upgrade-canton-nodes": (
        "升级 Canton 节点",
        "升级 Canton 参与方与同步器二进制、变更协议版本的完整指南。",
        "升级 Canton 参与方与同步器二进制及协议版本。",
    ),
    "global-synchronizer-production-operations-validator-backups": (
        "验证者备份",
        "验证者节点身份、数据库与组件转储的备份流程。",
        "验证者节点的备份流程。",
    ),
    "global-synchronizer-production-operations-validator-disaster-recovery": (
        "验证者灾难恢复",
        "验证者节点灾难恢复与从备份/转储恢复的详细步骤。",
        "验证者节点的灾难恢复与恢复流程。",
    ),
    "global-synchronizer-production-operations-validator-security": (
        "验证者安全",
        "验证者节点安全加固与参与方密钥的外部 KMS 配置。",
        "验证者节点安全加固与 KMS 配置。",
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
    ("party", "party"),
    ("Helm", "Helm"),
    ("Kubernetes", "Kubernetes"),
    ("Docker Compose", "Docker Compose"),
    ("OIDC", "OIDC"),
    ("OAuth", "OAuth"),
    ("gRPC", "gRPC"),
    ("PostgreSQL", "PostgreSQL"),
    ("Canton Console", "Canton Console"),
    ("Daml", "Daml"),
    ("topology", "拓扑"),
    ("Topology", "拓扑"),
    ("reassignment", "重分配"),
    ("Reassignment", "重分配"),
    ("unassignment", "取消分配"),
    ("Unassignment", "取消分配"),
    ("Prometheus", "Prometheus"),
    ("CometBFT", "CometBFT"),
    ("KMS", "KMS"),
    ("GCP", "GCP"),
    ("AWS", "AWS"),
    ("pruning", "修剪"),
    ("Pruning", "修剪"),
    ("backup", "备份"),
    ("Backup", "备份"),
    ("disaster recovery", "灾难恢复"),
    ("Disaster Recovery", "灾难恢复"),
    ("MIGRATION_ID", "MIGRATION_ID"),
    ("Canton", "Canton"),
    ("Scan", "Scan"),
    ("AmuletRules", "AmuletRules"),
    ("MemberTraffic", "MemberTraffic"),
    ("CNS", "CNS"),
    ("ANS", "ANS"),
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
            time.sleep(2**attempt)
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
    print(f"=== batch 27 ({len(BATCH_27)} slugs) ===", flush=True)
    for slug in BATCH_27:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 27 count: {n}", flush=True)


if __name__ == "__main__":
    main()
