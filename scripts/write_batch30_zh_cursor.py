#!/usr/bin/env python3
"""Write batch 30 GS troubleshooting-guide zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_30 = [
    "global-synchronizer-troubleshooting-guide-common-questions",
    "global-synchronizer-troubleshooting-guide-configuration-problems",
    "global-synchronizer-troubleshooting-guide-connectivity-issues",
    "global-synchronizer-troubleshooting-guide-error-code-reference",
    "global-synchronizer-troubleshooting-guide-installation-issues",
    "global-synchronizer-troubleshooting-guide-performance-issues",
    "global-synchronizer-troubleshooting-guide-runbooks",
    "global-synchronizer-troubleshooting-guide-security-issues",
    "global-synchronizer-troubleshooting-guide-transaction-failures",
    "global-synchronizer-troubleshooting-guide-troubleshooting-methodology",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-troubleshooting-guide-common-questions": (
        "常见问题",
        "验证者搭建、运维与升级相关的 Global Synchronizer 常见问题。",
        "验证者搭建、运维与升级相关的常见问题解答。",
    ),
    "global-synchronizer-troubleshooting-guide-configuration-problems": (
        "配置问题",
        "HOCON 解析错误、文件权限与环境变量冲突等配置故障排查。",
        "HOCON 解析、权限与环境变量冲突的配置故障排查。",
    ),
    "global-synchronizer-troubleshooting-guide-connectivity-issues": (
        "连接问题",
        "同步器连接失败、TLS 握手错误与 VPN 相关连通性排查。",
        "同步器连接、TLS 与 VPN 连通性故障排查。",
    ),
    "global-synchronizer-troubleshooting-guide-error-code-reference": (
        "常见错误码",
        "验证者运维中最常遇到的 Canton 与 Splice 结构化错误码说明。",
        "验证者运维常见 Canton/Splice 错误码与处理步骤。",
    ),
    "global-synchronizer-troubleshooting-guide-installation-issues": (
        "安装问题",
        "Docker、Kubernetes 与网络层面的验证者安装故障排查。",
        "Docker/Kubernetes 与网络导致的安装故障排查。",
    ),
    "global-synchronizer-troubleshooting-guide-performance-issues": (
        "性能问题",
        "交易变慢、资源耗尽与数据库瓶颈等性能问题处理。",
        "慢交易、资源耗尽与数据库瓶颈的性能排查。",
    ),
    "global-synchronizer-troubleshooting-guide-runbooks": (
        "运维手册",
        "验证者离线、流量耗尽、磁盘满与升级回滚等事件运维手册。",
        "常见验证者事件的检测、处置与验证运维手册。",
    ),
    "global-synchronizer-troubleshooting-guide-security-issues": (
        "安全问题",
        "证书、JWT 校验与 KMS 密钥管理相关的安全故障排查。",
        "证书、JWT 与 KMS 相关的安全故障排查。",
    ),
    "global-synchronizer-troubleshooting-guide-transaction-failures": (
        "交易失败",
        "授权错误、包 vetting 失败、超时与 ACS 承诺不一致排查。",
        "授权、包 vetting、超时与 ACS 承诺相关交易失败排查。",
    ),
    "global-synchronizer-troubleshooting-guide-troubleshooting-methodology": (
        "故障排查方法论",
        "收集日志、配置与常见错误信息的系统化排查方法。",
        "Global Synchronizer 节点问题系统化排查与信息收集。",
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
    ("participant nodes", "参与方节点"),
    ("Synchronizer", "同步器"),
    ("synchronizer", "同步器"),
    ("synchronizers", "同步器"),
    ("Canton Coin", "Canton Coin"),
    ("Canton Network", "Canton Network"),
    ("Ledger API", "Ledger API"),
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
    ("Helm", "Helm"),
    ("Kubernetes", "Kubernetes"),
    ("Docker Compose", "Docker Compose"),
    ("docker-compose", "docker-compose"),
    ("OIDC", "OIDC"),
    ("gRPC", "gRPC"),
    ("PostgreSQL", "PostgreSQL"),
    ("Canton Console", "Canton Console"),
    ("Canton", "Canton"),
    ("Daml", "Daml"),
    ("HOCON", "HOCON"),
    ("KMS", "KMS"),
    ("JWT", "JWT"),
    ("JWKS", "JWKS"),
    ("TLS", "TLS"),
    ("SSL", "SSL"),
    ("ACS", "ACS"),
    ("Active Contract Set", "活跃合约集（ACS）"),
    ("CometBFT", "CometBFT"),
    ("PQS", "PQS"),
    ("Splice", "Splice"),
    ("SV", "SV"),
    ("traffic", "流量"),
    ("Traffic", "流量"),
    ("pruning", "修剪"),
    ("Pruning", "修剪"),
    ("runbook", "运维手册"),
    ("Runbook", "运维手册"),
    ("Runbooks", "运维手册"),
    ("CrashLoopBackOff", "CrashLoopBackOff"),
    ("HikariCP", "HikariCP"),
    ("HikariPool", "HikariPool"),
    ("JFrog", "JFrog"),
    ("cert-manager", "cert-manager"),
    ("IRSA", "IRSA"),
    ("NTP", "NTP"),
    ("VPN", "VPN"),
    ("MTU", "MTU"),
    ("OOM", "OOM"),
    ("PVC", "PVC"),
    ("DAR", "DAR"),
    ("vetting", "vetting"),
    ("Vetting", "Vetting"),
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
    slugs = [s for s in BATCH_30 if only is None or s in only]
    n = 0
    print(f"=== batch 30 ({len(slugs)} slugs) ===", flush=True)
    for slug in slugs:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 30 count: {n}", flush=True)


if __name__ == "__main__":
    main()
