#!/usr/bin/env python3
"""Write batch 28 GS zh-cursor JSON (validator upgrades + reference docs)."""
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

BATCH_28 = [
    "global-synchronizer-production-operations-validator-upgrades",
    "global-synchronizer-reference-api-configuration",
    "global-synchronizer-reference-canton-configuration-guide",
    "global-synchronizer-reference-canton-console-commands",
    "global-synchronizer-reference-canton-console-reference",
    "global-synchronizer-reference-canton-metrics",
    "global-synchronizer-reference-configuration-reference",
    "global-synchronizer-reference-crypto-schemes",
    "global-synchronizer-reference-error-codes",
    "global-synchronizer-reference-kms-driver-guide",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-production-operations-validator-upgrades": (
        "验证者升级",
        "验证者节点版本升级与协议升级的操作说明与注意事项。",
        "验证者节点版本升级与协议升级的操作说明。",
    ),
    "global-synchronizer-reference-api-configuration": (
        "Canton API 配置",
        "Admin API、gRPC Ledger API、JSON Ledger API 端口与缓存等通用配置。",
        "Canton 节点 Admin API、Ledger API 与 JSON API 配置。",
    ),
    "global-synchronizer-reference-canton-configuration-guide": (
        "Canton 配置指南",
        "使用 HOCON、命令行与声明式配置 Canton 节点（静态与动态配置）。",
        "使用 HOCON 与命令行配置 Canton 节点的完整指南。",
    ),
    "global-synchronizer-reference-canton-console-commands": (
        "Canton Console 命令",
        "Canton 管理控制台命令参考：参与方、排序器、中介者与拓扑命令。",
        "Canton 管理控制台完整命令参考。",
    ),
    "global-synchronizer-reference-canton-console-reference": (
        "Canton Console 参考",
        "验证者与 SV 运维所需的 Canton Console 访问方式与调试流程。",
        "Global Synchronizer 运维使用的 Canton Console 参考。",
    ),
    "global-synchronizer-reference-canton-metrics": (
        "Canton 指标",
        "Canton 节点导出至 Prometheus 的指标类型与说明。",
        "Canton 节点 Prometheus 指标参考。",
    ),
    "global-synchronizer-reference-configuration-reference": (
        "配置参考",
        "验证者与超级验证者的 Splice、Canton、数据库、认证与可观测性配置项。",
        "Canton Network 验证者与 SV 完整配置参考。",
    ),
    "global-synchronizer-reference-crypto-schemes": (
        "支持的密码学方案",
        "Canton 支持的签名、对称/非对称加密方案与密钥格式。",
        "Canton 支持的密码学方案与密钥格式参考。",
    ),
    "global-synchronizer-reference-error-codes": (
        "错误码参考",
        "Canton 结构化错误码、日志级别含义与运维需关注的错误类别。",
        "Canton 运维错误码、类别与常见操作错误说明。",
    ),
    "global-synchronizer-reference-kms-driver-guide": (
        "KMS 驱动开发指南",
        "自定义 Canton KMS Driver 的 API、实现步骤与配置方法。",
        "开发自定义 Canton KMS Driver 的开发者指南。",
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
    slugs = [s for s in BATCH_28 if only is None or s in only]
    n = 0
    print(f"=== batch 28 ({len(slugs)} slugs) ===", flush=True)
    for slug in slugs:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 28 count: {n}", flush=True)


if __name__ == "__main__":
    main()
