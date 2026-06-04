#!/usr/bin/env python3
"""Write batch 22 GS zh-cursor JSON (Canton Console + deployment ops)."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

BATCH22 = [
    "global-synchronizer-canton-console-advanced-operations",
    "global-synchronizer-canton-console-console-overview",
    "global-synchronizer-canton-console-debugging-workflows",
    "global-synchronizer-canton-console-essential-commands",
    "global-synchronizer-canton-console-getting-started-tutorial",
    "global-synchronizer-canton-console-scripting",
    "global-synchronizer-deployment-community-docker-compose-helm",
    "global-synchronizer-deployment-community-helm-templating",
    "global-synchronizer-deployment-community-keycloak-config",
    "global-synchronizer-deployment-configuration",
]

META: dict[str, tuple[str, str, str]] = {
    "global-synchronizer-canton-console-advanced-operations": (
        "高级运维操作",
        "Canton Console 高级操作：拓扑管理、密钥轮换与修复流程。",
        "面向资深运维的 Canton Console 高级操作：拓扑、密钥与修复。",
    ),
    "global-synchronizer-canton-console-console-overview": (
        "Console 概览",
        "访问 Participant、Sequencer、Mediator Console 的配置与 Docker/K8s 步骤。",
        "验证者与 SV 节点 Canton Console 访问方式概览。",
    ),
    "global-synchronizer-canton-console-debugging-workflows": (
        "调试工作流",
        "用 Canton Console 诊断卡住交易、连通性与 ACS 不一致等问题。",
        "常见 Canton 故障的 Console 逐步诊断流程。",
    ),
    "global-synchronizer-canton-console-essential-commands": (
        "常用命令",
        "Canton Console 健康检查、Party、包管理与拓扑查询命令参考。",
        "Canton Console 核心命令速查（健康、Party、包、拓扑）。",
    ),
    "global-synchronizer-canton-console-getting-started-tutorial": (
        "Canton 入门教程",
        "安装 Canton、理解拓扑、连接同步器并执行首笔 Daml 交易。",
        "Canton 安装、拓扑、身份与首笔智能合约交易入门教程。",
    ),
    "global-synchronizer-canton-console-scripting": (
        "脚本编写",
        "用 Scala/Ammonite 编写 .canton 脚本、自动化运维与健康检查。",
        "Canton Console 脚本化与自动化运维模式。",
    ),
    "global-synchronizer-deployment-community-docker-compose-helm": (
        "社区 Docker Compose 部署",
        "社区贡献的 Canton 验证者 Docker Compose 方案与 x-docker 标准。",
        "社区 Docker Compose 验证者部署方案（非官方）。",
    ),
    "global-synchronizer-deployment-community-helm-templating": (
        "社区 Helm 模板工具",
        "社区 Helm/Kubernetes values 模板工具，多环境 DevNet/TestNet/MainNet。",
        "社区 Helm values 自动化模板工具说明。",
    ),
    "global-synchronizer-deployment-community-keycloak-config": (
        "社区 Keycloak 配置",
        "验证者节点 Keycloak OIDC 端到端配置：Realm、Client Scope 与 Mapper。",
        "Canton 验证者 Keycloak 认证配置指南（社区）。",
    ),
    "global-synchronizer-deployment-configuration": (
        "自定义配置",
        "验证者/SV 应用 HOCON 扩展配置、ADDITIONAL_CONFIG 与 bootstrap 脚本。",
        "Global Synchronizer 验证者节点自定义配置参数。",
    ),
}

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")
MDX_BLOCK = re.compile(
    r"<(?:Warning|Note|CardGroup|Card|Tabs|Tab|figure|External\w+)[\s\S]*?"
    r"</(?:Warning|Note|CardGroup|Card|Tabs|Tab|figure)>|<div[\s\S]*?</div>"
    r"|<figure[\s\S]*?</figure>"
    r"|<External\w+[^>]*/>"
)

translator = GoogleTranslator(source="en", target="zh-CN")


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
    masked = protect(MDX_BLOCK, masked)
    masked = protect(INLINE_CODE, masked)
    return masked, tokens


def unmask(text: str, tokens: list[str]) -> str:
    for i, val in enumerate(tokens):
        text = text.replace(f"⟦P{i}⟧", val)
    return text


def split_oversized(text: str, max_len: int = 3500) -> list[str]:
    if len(text) <= max_len:
        return [text]
    lines = text.split("\n")
    chunks: list[str] = []
    current: list[str] = []
    cur_len = 0
    for line in lines:
        line_len = len(line) + 1
        if cur_len + line_len > max_len and current:
            chunks.append("\n".join(current))
            current = [line]
            cur_len = line_len
        else:
            current.append(line)
            cur_len += line_len
    if current:
        chunks.append("\n".join(current))
    return chunks


def chunk_text(text: str, max_len: int = 3500) -> list[str]:
    parts = re.split(r"(\n{2,})", text)
    chunks: list[str] = []
    current = ""
    for part in parts:
        if len(current) + len(part) > max_len and current.strip():
            chunks.extend(split_oversized(current.strip(), max_len))
            current = part
        else:
            current += part
    if current.strip():
        chunks.extend(split_oversized(current.strip(), max_len))
    return chunks if chunks else [text]


def translate_table_row(row: str) -> str:
    if not row.strip().startswith("|"):
        return row
    if re.match(r"^\|\s*:?-+", row):
        return row
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    if len(cells) < 2:
        return row
    desc = cells[-1]
    if sum(c.isalpha() for c in desc) < 8:
        return row
    masked, tokens = mask_protected(desc)
    try:
        zh_desc = unmask(translator.translate(masked), tokens)
    except Exception:
        return row
    return "| " + " | ".join([*cells[:-1], zh_desc]) + " |"


def translate_table_block(chunk: str) -> str:
    out: list[str] = []
    prose: list[str] = []
    for ln in chunk.split("\n"):
        if ln.startswith("|"):
            if prose:
                out.append(_translate_prose("\n".join(prose)))
                prose = []
            out.append(translate_table_row(ln))
        else:
            prose.append(ln)
    if prose:
        out.append(_translate_prose("\n".join(prose)))
    return "\n".join(out)


def _translate_prose(chunk: str) -> str:
    chunk = chunk.strip()
    if not chunk:
        return chunk
    letters = sum(c.isalpha() for c in chunk)
    if letters < 20:
        return chunk
    masked, tokens = mask_protected(chunk)
    if len(masked) > 4800:
        return "\n".join(_translate_prose(p) for p in split_oversized(chunk, 3000))
    for attempt in range(3):
        try:
            return unmask(translator.translate(masked), tokens)
        except Exception as e:
            print(f"  translate error (attempt {attempt + 1}): {e}")
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("translation failed after retries")


def translate_chunk(chunk: str) -> str:
    chunk = chunk.strip()
    if not chunk:
        return chunk
    letters = sum(c.isalpha() for c in chunk)
    if letters < 20:
        return chunk
    if chunk.count("\n|") >= 3 and len(chunk) > 3000:
        return translate_table_block(chunk)
    return _translate_prose(chunk)


def translate_body(body: str) -> str:
    chunks = chunk_text(body)
    out: list[str] = []
    for i, ch in enumerate(chunks):
        out.append(translate_chunk(ch))
        if i < len(chunks) - 1:
            time.sleep(0.35)
    return "".join(out)


def postprocess(body: str) -> str:
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in BATCH22:
        out_path = OUT_DIR / f"{slug}.json"
        en_path = EN_DIR / f"{slug}.md"
        if not en_path.exists():
            print(f"missing EN: {slug}")
            continue
        en_body = strip_en(en_path.read_text(encoding="utf-8"))
        zh_title, summary, intro = META[slug]
        print(f"translating {slug} ({len(en_body)} chars)...")
        zh_body = postprocess(translate_body(en_body))
        payload = {
            "zhTitle": zh_title,
            "summary": summary,
            "body": f"> {intro}\n\n{zh_body}",
        }
        out_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {out_path.name} ({len(payload['body'])} chars)")
        count += 1
        time.sleep(0.5)
    print(f"batch22 count: {count}")


if __name__ == "__main__":
    main()
