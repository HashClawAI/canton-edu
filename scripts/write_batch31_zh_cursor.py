#!/usr/bin/env python3
"""Write batch 31 GS understand zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_31 = [
    "global-synchronizer-understand-installing-daml-sdk",
    "global-synchronizer-understand-introduction",
    "global-synchronizer-understand-local-testing",
    "global-synchronizer-understand-overview",
    "global-synchronizer-understand-validator-roles",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-understand-installing-daml-sdk": (
        "安装兼容的 Daml SDK",
        "如何安装与当前 Splice 版本兼容的 Daml SDK。",
        "安装与当前 Splice 版本兼容的 Daml SDK 的方法。",
    ),
    "global-synchronizer-understand-introduction": (
        "节点运维入门",
        "Canton Network 全局同步器上验证者节点运维的概念、环境与职责。",
        "全局同步器上验证者节点运维入门指南。",
    ),
    "global-synchronizer-understand-local-testing": (
        "本地测试",
        "基于 Docker Compose 的 LocalNet 本地 Canton Network 部署与使用。",
        "LocalNet 本地开发与测试环境部署指南。",
    ),
    "global-synchronizer-understand-overview": (
        "Canton Network 全局同步器",
        "全局同步器在 Canton Network 中的定位、角色与代币经济学概览。",
        "全局同步器及其在 Canton Network 中的角色概览。",
    ),
    "global-synchronizer-understand-validator-roles": (
        "验证者角色与职责",
        "Canton Network 验证者的运维职责、期望与成本说明。",
        "验证者在 Canton Network 上的角色、职责与运维期望。",
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
    ("global-同步器-foundation", "global-synchronizer-foundation"),
    ("global-同步器", "global-synchronizer"),
    ("Super Validator", "超级验证者"),
    ("super validator", "超级验证者"),
    ("Super Validators", "超级验证者"),
    ("Participant Node", "参与方节点"),
    ("participant node", "参与方节点"),
    ("participant nodes", "参与方节点"),
    ("Synchronizer", "同步器"),
    ("synchronizer", "同步器"),
    ("synchronizers", "同步器"),
    ("Canton Coin", "Canton Coin"),
    ("Canton Network", "Canton Network"),
    ("Ledger API", "Ledger API"),
    ("Admin API", "Admin API"),
    ("JSON Ledger API", "JSON Ledger API"),
    ("gRPC Ledger API", "gRPC Ledger API"),
    ("DevNet", "DevNet"),
    ("TestNet", "TestNet"),
    ("MainNet", "MainNet"),
    ("LocalNet", "LocalNet"),
    ("Sequencer", "Sequencer"),
    ("sequencer", "sequencer"),
    ("Mediator", "Mediator"),
    ("mediator", "mediator"),
    ("Validator", "验证者"),
    ("validator", "验证者"),
    ("validators", "验证者"),
    ("Participant", "参与方"),
    ("participant", "参与方"),
    ("topology", "拓扑"),
    ("Topology", "拓扑"),
    ("onboarding", "入驻"),
    ("Onboarding", "入驻"),
    ("Party", "Party"),
    ("party", "party"),
    ("Helm", "Helm"),
    ("Kubernetes", "Kubernetes"),
    ("Docker Compose", "Docker Compose"),
    ("docker-compose", "docker-compose"),
    ("OIDC", "OIDC"),
    ("OAuth", "OAuth"),
    ("gRPC", "gRPC"),
    ("PostgreSQL", "PostgreSQL"),
    ("Canton Console", "Canton Console"),
    ("Canton", "Canton"),
    ("Daml", "Daml"),
    ("HOCON", "HOCON"),
    ("KMS", "KMS"),
    ("HSM", "HSM"),
    ("Prometheus", "Prometheus"),
    ("JCE", "JCE"),
    ("AWS KMS", "AWS KMS"),
    ("Google Cloud KMS", "Google Cloud KMS"),
    ("PQS", "PQS"),
    ("Splice", "Splice"),
    ("DSO", "DSO"),
    ("SV", "SV"),
    ("Scan", "Scan"),
    ("GSF", "GSF"),
    ("BFT", "BFT"),
    ("NGINX", "NGINX"),
    ("Swagger UI", "Swagger UI"),
    ("JWT", "JWT"),
    ("CORS", "CORS"),
    ("reassignment", "重分配"),
    ("Reassignment", "重分配"),
    ("unassignment", "取消分配"),
    ("Unassignment", "取消分配"),
    ("pruning", "修剪"),
    ("Pruning", "修剪"),
    ("traffic", "流量"),
    ("Traffic", "流量"),
    ("wallet", "钱包"),
    ("Wallet", "钱包"),
    ("protocol upgrade", "协议升级"),
    ("Protocol upgrade", "协议升级"),
    ("version upgrade", "版本升级"),
    ("Version upgrade", "版本升级"),
    ("release_notes", "release_notes"),
    ("IMAGE_TAG", "IMAGE_TAG"),
    ("MIGRATION_ID", "MIGRATION_ID"),
    ("ADDITIONAL_CONFIG", "ADDITIONAL_CONFIG"),
    ("ADDITIONAL_CONFIG_", "ADDITIONAL_CONFIG_"),
    ("LOCALNET_DIR", "LOCALNET_DIR"),
    ("LOCALNET_ENV_DIR", "LOCALNET_ENV_DIR"),
    ("APP_PROVIDER_UI_PORT", "APP_PROVIDER_UI_PORT"),
    ("PARTICIPANT_JSON_API_PORT", "PARTICIPANT_JSON_API_PORT"),
    ("CANTON_PROTOCOL_VERSION", "CANTON_PROTOCOL_VERSION"),
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
            time.sleep(min(2**attempt, 30))
    raise RuntimeError(f"translate failed: {last_err}")


def translate_body(body: str) -> str:
    chunks = chunk_text(body)
    out: list[str] = []
    total = len(chunks)
    for i, ch in enumerate(chunks):
        out.append(translate_chunk(ch))
        if i < total - 1:
            time.sleep(0.35)
        if total > 20 and (i + 1) % 25 == 0:
            print(f"    ... chunk {i + 1}/{total}", flush=True)
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
    print(f"  translating {slug} ({len(en_body)} chars, ~{len(chunk_text(en_body))} chunks)...", flush=True)
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
    only: set[str] | None = None
    for arg in sys.argv[1:]:
        if arg.startswith("--only="):
            only = {s.strip() for s in arg.split("=", 1)[1].split(",") if s.strip()}
    slugs = [s for s in BATCH_31 if only is None or s in only]
    n = 0
    print(f"=== batch 31 ({len(slugs)} slugs) ===", flush=True)
    for slug in slugs:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 31 count: {n}", flush=True)


if __name__ == "__main__":
    main()
