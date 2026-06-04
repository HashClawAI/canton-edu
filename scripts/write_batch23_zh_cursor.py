#!/usr/bin/env python3
"""Write batch 23 GS deployment zh-cursor JSON (EN → zh-CN, code preserved)."""
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

BATCH_23: list[str] = [
    "global-synchronizer-deployment-deployment-options",
    "global-synchronizer-deployment-docker",
    "global-synchronizer-deployment-identity-management",
    "global-synchronizer-deployment-kubernetes-deployment",
    "global-synchronizer-deployment-oidc-providers",
    "global-synchronizer-deployment-onboarding-process",
    "global-synchronizer-deployment-prerequisites",
    "global-synchronizer-deployment-required-network-parameters",
    "global-synchronizer-deployment-sv-network-resets",
    "global-synchronizer-deployment-sv-operations",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-deployment-deployment-options": (
        "部署选项",
        "Docker Compose 与 Kubernetes 验证者部署方式对比及选型建议。",
        "Canton Network 验证者部署：Docker Compose 与 Kubernetes 选型指南。",
    ),
    "global-synchronizer-deployment-docker": (
        "Canton Docker 运维",
        "获取与运行 Canton Docker 镜像、环境变量、端口与自定义配置。",
        "Canton 官方 Docker 镜像下载、运行与容器配置说明。",
    ),
    "global-synchronizer-deployment-identity-management": (
        "Canton 身份管理",
        "链上拓扑身份、拓扑事务、参与方入驻与用户身份管理 cookbook。",
        "Canton 身份架构、拓扑事务与用户/参与方身份管理参考。",
    ),
    "global-synchronizer-deployment-kubernetes-deployment": (
        "超级验证者 Helm 部署",
        "在 Kubernetes 上使用 Helm 部署超级验证者（SV）完整节点。",
        "Global Synchronizer 超级验证者 Kubernetes/Helm 部署指南。",
    ),
    "global-synchronizer-deployment-oidc-providers": (
        "Okta 与 Keycloak OIDC 配置",
        "验证者节点部署时 Okta 与 Keycloak OIDC 提供方逐步配置说明。",
        "Canton 验证者 OIDC 认证：Okta 与 Keycloak 配置 walkthrough。",
    ),
    "global-synchronizer-deployment-onboarding-process": (
        "验证者入驻流程",
        "通过 SV 赞助在 DevNet、TestNet、MainNet 入驻验证者的步骤与 IP 校验。",
        "Canton Network 验证者入驻流程与网络准入说明。",
    ),
    "global-synchronizer-deployment-prerequisites": (
        "前置条件",
        "运行 Canton Network 验证者的硬件、内存与数据库延迟要求。",
        "验证者部署系统要求与资源参考值。",
    ),
    "global-synchronizer-deployment-required-network-parameters": (
        "必需网络参数",
        "初始化验证者并连接网络所需的 MIGRATION_ID、SPONSOR_SV_URL 等参数。",
        "验证者入网初始化所需网络参数与 onboarding secret 说明。",
    ),
    "global-synchronizer-deployment-sv-network-resets": (
        "SV 网络重置",
        "DevNet/TestNet 定期重置时超级验证者节点的备份、卸载与重新部署步骤。",
        "超级验证者应对 DevNet/TestNet 网络重置的操作指南。",
    ),
    "global-synchronizer-deployment-sv-operations": (
        "SV 运维概览",
        "超级验证者运营：入驻密钥、身份层级、奖励权重、流量参数与 Scan 重摄取。",
        "Global Synchronizer 超级验证者日常运维与治理操作参考。",
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
    ("Docker Compose", "Docker Compose"),
    ("Kubernetes", "Kubernetes"),
    ("Helm", "Helm"),
    ("DevNet", "DevNet"),
    ("TestNet", "TestNet"),
    ("MainNet", "MainNet"),
    ("OIDC", "OIDC"),
    ("onboarding secret", "入驻密钥"),
    ("Onboarding secret", "入驻密钥"),
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


def chunk_text(text: str, max_len: int = 2800) -> list[str]:
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

    # Split any oversized chunk (e.g. long numbered lists without blank lines)
    final: list[str] = []
    for ch in (chunks if chunks else [text]):
        if len(ch) <= max_len:
            final.append(ch)
            continue
        lines = ch.split("\n")
        buf = ""
        for line in lines:
            candidate = f"{buf}\n{line}" if buf else line
            if len(candidate) > max_len and buf.strip():
                final.append(buf)
                buf = line
            else:
                buf = candidate
        if buf.strip():
            if len(buf) > max_len:
                for i in range(0, len(buf), max_len):
                    final.append(buf[i : i + max_len])
            else:
                final.append(buf)
    return final if final else [text]


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
            time.sleep(min(2 ** attempt, 30))
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
    slugs = BATCH_23
    n = 0
    print(f"=== batch 23 ({len(slugs)} slugs) ===", flush=True)
    for slug in slugs:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.3)
    print(f"batch 23 count: {n}", flush=True)


if __name__ == "__main__":
    main()
