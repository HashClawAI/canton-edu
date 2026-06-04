#!/usr/bin/env python3
"""Write batch 14 zh-cursor JSON (error codes, PQS SQL, tooling, troubleshooting)."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

BATCH14 = [
    "appdev-reference-error-codes",
    "appdev-reference-pqs-sql-reference",
    "appdev-tooling-debugging-tools",
    "appdev-tooling-development-tools-overview",
    "appdev-tooling-ide-setup",
    "appdev-troubleshooting",
    "appdev-troubleshooting-guide-common-questions",
    "appdev-troubleshooting-guide-development-issues",
    "appdev-troubleshooting-guide-error-code-reference",
    "appdev-troubleshooting-guide-installation-issues",
]

META: dict[str, tuple[str, str, str]] = {
    "appdev-reference-error-codes": (
        "错误码",
        "Canton 错误码、类别、gRPC 状态映射与重试策略参考。",
        "Canton 错误码、类别、gRPC 状态映射与重试策略参考。",
    ),
    "appdev-reference-pqs-sql-reference": (
        "PQS SQL",
        "Participant Query Store (PQS) 完整 SQL API：表函数、offset 管理、维护操作与 JSONB 索引。",
        "Participant Query Store (PQS) 完整 SQL API 参考，含表函数、offset 管理、维护操作与 JSONB 索引。",
    ),
    "appdev-tooling-debugging-tools": (
        "调试工具",
        "调试 Canton 应用的工具与工作流：测试输出、Canton Console、PQS 查询与日志分析。",
        "调试 Canton 应用的工具与工作流：测试输出、Canton Console、PQS 查询与日志分析。",
    ),
    "appdev-tooling-development-tools-overview": (
        "开发工具概览",
        "Canton 开发工具链概览：DPM、Daml Studio、Canton Console、Sandbox、LocalNet 与 PQS。",
        "Canton 开发工具链概览：DPM、Daml Studio、Canton Console、Sandbox、LocalNet 与 PQS。",
    ),
    "appdev-tooling-ide-setup": (
        "IDE 配置",
        "为 Canton 应用开发配置 VS Code 与其他 IDE（Daml、Java、全栈工具）。",
        "为 Canton 应用开发配置 VS Code 与其他 IDE（Daml、Java、全栈工具）。",
    ),
    "appdev-troubleshooting": (
        "故障排查速查表",
        "Canton Network 应用开发详细故障排查指南索引。",
        "Canton Network 应用开发详细故障排查指南索引。",
    ),
    "appdev-troubleshooting-guide-common-questions": (
        "常见问题",
        "Canton Network 应用开发常见问题与解答。",
        "Canton Network 应用开发常见问题与解答。",
    ),
    "appdev-troubleshooting-guide-development-issues": (
        "开发问题",
        "排查 Daml 编译错误、API 连接问题与开发期交易失败。",
        "排查 Daml 编译错误、API 连接问题与开发期交易失败。",
    ),
    "appdev-troubleshooting-guide-error-code-reference": (
        "Daml 错误码",
        "Daml 编译、Canton 运行时与 Ledger API 常见错误码参考。",
        "Daml 编译、Canton 运行时与 Ledger API 常见错误码参考。",
    ),
    "appdev-troubleshooting-guide-installation-issues": (
        "安装问题",
        "排查 Canton Network 开发环境安装中的 Nix、Docker 与内存问题。",
        "排查 Canton Network 开发环境安装中的 Nix、Docker 与内存问题。",
    ),
}

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")
MDX_BLOCK = re.compile(r"<(?:Warning|Note|CardGroup|Card)[\s\S]*?</(?:Warning|Note|CardGroup|Card)>|<div[\s\S]*?</div>")

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


TABLE_ROW = re.compile(r"^\|.+\|$", re.M)


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
    # keep first columns (identifiers/types); translate description-like trailing cells
    head = " | ".join(cells[:-1])
    desc = cells[-1]
    if sum(c.isalpha() for c in desc) < 8:
        return row
    masked, tokens = mask_protected(desc)
    try:
        zh_desc = translator.translate(masked)
        zh_desc = unmask(zh_desc, tokens)
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
            translated = translator.translate(masked)
            return unmask(translated, tokens)
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


HEADING_FIXES = {
    "警告": "Warning",
    "注意": "Note",
    "CardGroup": "CardGroup",
}


def postprocess(body: str) -> str:
    fixes = {
        "Participant Node": "Participant 节点",
        "participant node": "participant 节点",
        "Participant Nodes": "Participant 节点",
        "Synchronizer": "Synchronizer",
        "synchronizer": "synchronizer",
        "Ledger API": "Ledger API",
        "Daml Script": "Daml Script",
        "Canton Console": "Canton Console",
        "LocalNet": "LocalNet",
        "cn-quickstart": "cn-quickstart",
        "DevNet": "DevNet",
        "TestNet": "TestNet",
        "MainNet": "MainNet",
        "Smart Contract Upgrade": "智能合约升级",
        "SCU": "SCU",
        "PQS": "PQS",
        "DPM": "DPM",
        "DAR": "DAR",
        "gRPC": "gRPC",
        "JSONB": "JSONB",
        "HOCON": "HOCON",
        "JWT": "JWT",
        "ACS": "ACS",
        "UTXO": "UTXO",
        "CIP": "CIP",
    }
    for en, zh in fixes.items():
        pass  # keep English technical terms as in prior batches
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in BATCH14:
        out_path = OUT_DIR / f"{slug}.json"
        if out_path.exists() and out_path.stat().st_size > 500:
            print(f"skip existing: {slug}")
            count += 1
            continue
        en_path = EN_DIR / f"{slug}.md"
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
    print(f"batch14 count: {count}")


if __name__ == "__main__":
    main()
