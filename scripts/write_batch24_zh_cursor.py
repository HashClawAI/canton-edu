#!/usr/bin/env python3
"""Write batch 24 GS zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_24 = [
    "global-synchronizer-deployment-sv-scratchnet",
    "global-synchronizer-deployment-synchronizer-traffic",
    "global-synchronizer-deployment-validator-docker-compose",
    "global-synchronizer-deployment-validator-kubernetes",
    "global-synchronizer-deployment-validator-network-resets",
    "global-synchronizer-deployment-validator-networking",
    "global-synchronizer-deployment-validator-users",
    "global-synchronizer-extension-synchronizers-bft-orderer",
    "global-synchronizer-extension-synchronizers-hybrid-synchronizer-pattern",
    "global-synchronizer-extension-synchronizers-linking-validator-multi-sync",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-deployment-sv-scratchnet": (
        "如何引导网络",
        "以超级验证者身份从零引导新 Canton Network 的 Helm 配置要点。",
        "以超级验证者身份从零引导新 Canton Network。",
    ),
    "global-synchronizer-deployment-synchronizer-traffic": (
        "同步器流量",
        "全局同步器上的流量计费、参数查询、自动充值与浪费流量监控。",
        "全局同步器上的流量核算、费用与监控。",
    ),
    "global-synchronizer-deployment-validator-docker-compose": (
        "Docker Compose 验证者部署",
        "使用 Docker Compose 部署独立验证者节点、钱包与 CNS UI 的完整指南。",
        "使用 Docker Compose 部署 Canton Network 验证者。",
    ),
    "global-synchronizer-deployment-validator-kubernetes": (
        "Kubernetes 验证者部署",
        "使用 Helm 在 Kubernetes 上部署验证者、认证、流量充值与运维配置。",
        "使用 Kubernetes Helm 部署 Canton Network 验证者。",
    ),
    "global-synchronizer-deployment-validator-network-resets": (
        "验证者网络重置",
        "DevNet/TestNet 定期重置时验证者节点的卸载与重新部署步骤。",
        "DevNet 与 TestNet 重置时验证者节点的处理方式。",
    ),
    "global-synchronizer-deployment-validator-networking": (
        "验证者入站与出站要求",
        "验证者节点的网络入站/出站与 SV 连通性要求。",
        "验证者节点的网络入站与出站要求。",
    ),
    "global-synchronizer-deployment-validator-users": (
        "验证者用户与钱包",
        "在验证者上管理用户、Party 关联、自定义 Party Hint 与禁用钱包。",
        "验证者节点上的用户、Party 与钱包管理。",
    ),
    "global-synchronizer-extension-synchronizers-bft-orderer": (
        "BFT 排序器架构",
        "Canton 同步器 BFT Orderer 的信任模型、API 与交易排序流水线。",
        "Canton 同步器拜占庭容错（BFT）排序器架构说明。",
    ),
    "global-synchronizer-extension-synchronizers-hybrid-synchronizer-pattern": (
        "混合同步器模式",
        "私有同步器与全局同步器并行的混合部署、合约迁移与配置。",
        "私有同步器与全局同步器并行的混合部署模式。",
    ),
    "global-synchronizer-extension-synchronizers-linking-validator-multi-sync": (
        "将验证者连接到多个同步器",
        "验证者连接多个同步器、拓扑注册与跨同步器工作流配置。",
        "将验证者节点连接到多个同步器的操作指南。",
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
    ("BFT Orderer", "BFT Orderer"),
    ("BlockOrderer", "BlockOrderer"),
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
    ("MIGRATION_ID", "MIGRATION_ID"),
    ("SPONSOR_SV_URL", "SPONSOR_SV_URL"),
    ("ONBOARDING_SECRET", "ONBOARDING_SECRET"),
    ("Canton", "Canton"),
    ("Scan", "Scan"),
    ("AmuletRules", "AmuletRules"),
    ("MemberTraffic", "MemberTraffic"),
    ("PBFT", "PBFT"),
    ("Narwhal", "Narwhal"),
    ("ISS", "ISS"),
    ("PoA", "PoA"),
    ("PoAs", "PoA"),
    ("mempool", "mempool"),
    ("availability", "availability"),
    ("consensus", "consensus"),
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
    print(f"=== batch 24 ({len(BATCH_24)} slugs) ===", flush=True)
    for slug in BATCH_24:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 24 count: {n}", flush=True)


if __name__ == "__main__":
    main()
