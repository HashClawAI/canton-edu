#!/usr/bin/env python3
"""Write batch 26 GS production-ops zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_26 = [
    "global-synchronizer-production-operations-key-metrics",
    "global-synchronizer-production-operations-kms-operations",
    "global-synchronizer-production-operations-logical-synchronizer-upgrade",
    "global-synchronizer-production-operations-manage-packages",
    "global-synchronizer-production-operations-monitoring-setup",
    "global-synchronizer-production-operations-multi-sig",
    "global-synchronizer-production-operations-node-backup-restore",
    "global-synchronizer-production-operations-party-management",
    "global-synchronizer-production-operations-performance-optimization",
    "global-synchronizer-production-operations-pruning",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-production-operations-key-metrics": (
        "关键指标",
        "验证者与 SV 节点的就绪/存活探针及核心运维监控指标。",
        "Canton Network 验证者与 SV 节点应监控的关键指标。",
    ),
    "global-synchronizer-production-operations-kms-operations": (
        "Canton KMS 运维",
        "为 Canton 配置与运维 KMS：AWS/GCP/驱动模式、信封加密、外部密钥与轮换。",
        "配置并运维 Canton 密钥管理服务（KMS）。",
    ),
    "global-synchronizer-production-operations-logical-synchronizer-upgrade": (
        "逻辑同步器升级",
        "通过逻辑同步器升级（LSU）以极低停机升级全局同步器协议版本。",
        "以极低停机通过 LSU 升级全局同步器协议版本。",
    ),
    "global-synchronizer-production-operations-manage-packages": (
        "管理 Daml 包与归档",
        "在参与方节点上上传、审查（vet）与取消审查 Daml 包。",
        "在参与方节点上管理 Daml 包的上传、审查与取消审查。",
    ),
    "global-synchronizer-production-operations-monitoring-setup": (
        "监控搭建",
        "Canton 监控示例：Prometheus、Grafana、ELK、健康端点与 ACS 承诺监控。",
        "Canton 侧监控搭建、健康检查与 ACS 承诺监控。",
    ),
    "global-synchronizer-production-operations-multi-sig": (
        "Canton 多重签名",
        "去中心化命名空间、去中心化 Party 托管与去中心化提交签名。",
        "Canton 中的去中心化命名空间、Party 托管与多重签名提交。",
    ),
    "global-synchronizer-production-operations-node-backup-restore": (
        "Canton 节点备份与恢复",
        "备份与恢复 Canton 参与方与同步器节点，含数据库复制与灾备。",
        "Canton 参与方与同步器节点的备份、恢复与灾备。",
    ),
    "global-synchronizer-production-operations-party-management": (
        "Party 管理",
        "在 Canton 节点上管理 Party：分配、复制与去中心化 Party 配置。",
        "在 Canton 节点上管理 Party 的分配、复制与去中心化设置。",
    ),
    "global-synchronizer-production-operations-performance-optimization": (
        "性能优化",
        "为验证者与 SV 调优数据库、JVM、定序器容量与修剪策略。",
        "验证者与 SV 节点的数据库、JVM 与 Canton 性能调优。",
    ),
    "global-synchronizer-production-operations-pruning": (
        "修剪",
        "全局同步器节点的定序器与 CometBFT 修剪及参与方自动修剪配置。",
        "参与方、定序器与 CometBFT 的修剪配置说明。",
    ),
}

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")
translator = GoogleTranslator(source="en", target="zh-CN")


def strip_mdx_exports(text: str) -> str:
    """Remove MDX `export const` blocks (networkData, React components, etc.)."""
    pattern = re.compile(r"^export const ", re.MULTILINE)
    while True:
        m = pattern.search(text)
        if not m:
            break
        start = m.start()
        nl = text.find("\n", start)
        first_line = text[start:] if nl == -1 else text[start:nl]
        semi = first_line.find(";")
        if semi != -1 and (nl == -1 or start + semi < nl):
            end = start + semi + 1
            if end < len(text) and text[end] == "\n":
                end += 1
            text = text[:start] + text[end:]
            continue
        arrow = text.find("=>", start)
        eq_brace = text.find("= {", start)
        brace_start = -1
        if arrow != -1:
            bs = text.find("{", arrow)
            if bs != -1:
                brace_start = bs
        if brace_start == -1 and eq_brace != -1:
            brace_start = eq_brace + 2
        if brace_start == -1:
            brace_start = text.find("{", start)
        if brace_start == -1:
            break
        depth = 0
        i = brace_start
        closed = False
        while i < len(text):
            ch = text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    j = i + 1
                    while j < len(text) and text[j] in " \t":
                        j += 1
                    if j < len(text) and text[j] == ";":
                        j += 1
                    if j < len(text) and text[j] == "\n":
                        j += 1
                    text = text[:start] + text[j:]
                    closed = True
                    break
            i += 1
        if not closed:
            break
    return text

TERM_FIXES: list[tuple[str, str]] = [
    ("Global Synchronizer", "全局同步器"),
    ("global synchronizer", "全局同步器"),
    ("Logical Synchronizer Upgrade", "逻辑同步器升级"),
    ("Logical Synchronizer Upgrades", "逻辑同步器升级"),
    ("logical synchronizer upgrade", "逻辑同步器升级"),
    ("Super Validator", "超级验证者"),
    ("super validator", "超级验证者"),
    ("Super Validators", "超级验证者"),
    ("Participant Node", "参与方节点"),
    ("participant node", "参与方节点"),
    ("participant nodes", "参与方节点"),
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
    ("onboarding", "入驻"),
    ("Onboarding", "入驻"),
    ("Party", "Party"),
    ("party", "party"),
    ("parties", "parties"),
    ("Helm", "Helm"),
    ("Kubernetes", "Kubernetes"),
    ("Docker Compose", "Docker Compose"),
    ("Canton Console", "Canton Console"),
    ("Daml", "Daml"),
    ("topology", "拓扑"),
    ("Topology", "拓扑"),
    ("reassignment", "重分配"),
    ("Reassignment", "重分配"),
    ("unassignment", "取消分配"),
    ("Unassignment", "取消分配"),
    ("envelope encryption", "信封加密"),
    ("Envelope encryption", "信封加密"),
    ("external keys", "外部密钥"),
    ("External keys", "外部密钥"),
    ("Key Management Service", "密钥管理服务"),
    ("key management service", "密钥管理服务"),
    ("KMS", "KMS"),
    ("Prometheus", "Prometheus"),
    ("Grafana", "Grafana"),
    ("pruning", "修剪"),
    ("Pruning", "修剪"),
    ("CometBFT", "CometBFT"),
    ("ACS", "ACS"),
    ("multi-sig", "多重签名"),
    ("Multi-Sig", "多重签名"),
    ("multi-signature", "多重签名"),
    ("Canton", "Canton"),
    ("PostgreSQL", "PostgreSQL"),
    ("JVM", "JVM"),
    ("HOCON", "HOCON"),
    ("gRPC", "gRPC"),
    ("OAuth", "OAuth"),
    ("OIDC", "OIDC"),
]


def strip_en(md: str) -> str:
    md = FRONTMATTER_RE.sub("", md)
    md = DOC_INDEX_RE.sub("", md)
    md = FOOTER_RE.sub("", md)
    md = strip_mdx_exports(md)
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
    text = re.sub(r"^\s*</>;\s*\n", "", text, flags=re.MULTILINE)
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


def chunk_text(text: str, max_len: int = 3200) -> list[str]:
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
    if len(masked) > 4900:
        mid = len(masked) // 2
        split_at = masked.rfind("\n\n", 0, mid)
        if split_at < 100:
            split_at = mid
        return translate_chunk(masked[:split_at], retries) + translate_chunk(
            masked[split_at:], retries
        )
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
    print(f"=== batch 26 ({len(BATCH_26)} slugs) ===", flush=True)
    for slug in BATCH_26:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 26 count: {n}", flush=True)


if __name__ == "__main__":
    main()
