#!/usr/bin/env python3
"""Translate batch 10 slugs to zh-cursor JSON (full Chinese body, code preserved)."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "appdev-reference-configuration-reference",
    "appdev-reference-daml-language-reference",
    "appdev-reference-daml-lf-reference",
    "appdev-reference-daml-standard-library-da-action",
    "appdev-reference-daml-standard-library-da-action-state",
    "appdev-reference-daml-standard-library-da-action-state-class",
    "appdev-reference-daml-standard-library-da-assert",
    "appdev-reference-daml-standard-library-da-bifunctor",
    "appdev-reference-daml-standard-library-da-crypto-text",
    "appdev-reference-daml-standard-library-da-date",
]

META = {
    "appdev-reference-configuration-reference": (
        "配置参考",
        "Canton HOCON 配置、DPM 项目设置、存储、命令行参数与环境变量参考。",
        "Canton 配置文件、DPM 项目设置、存储后端、命令行参数与环境变量参考。",
    ),
    "appdev-reference-daml-language-reference": (
        "Daml 语言参考",
        "Daml 模板、choice、数据类型、表达式、包、接口与异常的完整语言参考。",
        "Daml 模板、choice、数据类型、表达式、包、接口与异常等语言参考。",
    ),
    "appdev-reference-daml-lf-reference": (
        "Daml-LF 参考",
        "Daml-LF 类型转换、JSON 编码、Protobuf 映射、包与 DAR 文件结构。",
        "Daml-LF 类型转换、JSON 编码、Protobuf 映射、包与 DAR 结构说明。",
    ),
    "appdev-reference-daml-standard-library-da-action": (
        "DA.Action",
        "Daml 标准库模块 DA.Action：when、unless、foldrA、filterA 等 Action 工具函数。",
        "Daml 标准库模块 DA.Action 参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-action-state": (
        "DA.Action.State",
        "State monad：runState、evalState、execState 与状态变量读写。",
        "Daml 标准库模块 DA.Action.State 参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-action-state-class": (
        "DA.Action.State.Class",
        "ActionState 类型类：get、put、modify 及状态变量法则。",
        "Daml 标准库模块 DA.Action.State.Class 参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-assert": (
        "DA.Assert",
        "断言与相等性检查：assertEq、===、时间截止与账本时间断言。",
        "Daml 标准库模块 DA.Assert 参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-bifunctor": (
        "DA.Bifunctor",
        "Bifunctor 类型类：bimap、first、second 及 Either 等实例。",
        "Daml 标准库模块 DA.Bifunctor 参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-crypto-text": (
        "DA.Crypto.Text",
        "Alpha 加密工具：SHA256、Keccak256、SECP256K1 验签与十六进制类型。",
        "Daml 标准库模块 DA.Crypto.Text（Alpha）参考文档。",
    ),
    "appdev-reference-daml-standard-library-da-date": (
        "DA.Date",
        "Date 与 Gregorian 日历：加减天数、星期、闰年与 datetime 构造。",
        "Daml 标准库模块 DA.Date 参考文档。",
    ),
}

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")

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
    # drop duplicate top H1 block
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


def translate_chunk(chunk: str) -> str:
    chunk = chunk.strip()
    if not chunk:
        return chunk
    # skip if mostly placeholders / markup
    letters = sum(c.isalpha() for c in chunk)
    if letters < 20:
        return chunk
    masked, tokens = mask_protected(chunk)
    try:
        translated = translator.translate(masked)
    except Exception as e:
        print(f"  translate error: {e}, retry...")
        time.sleep(2)
        translated = translator.translate(masked)
    return unmask(translated, tokens)


def translate_body(body: str) -> str:
    chunks = chunk_text(body)
    out: list[str] = []
    for i, ch in enumerate(chunks):
        out.append(translate_chunk(ch))
        if i < len(chunks) - 1:
            time.sleep(0.35)
    return "".join(out)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in SLUGS:
        out_path = OUT_DIR / f"{slug}.json"
        if out_path.exists() and out_path.stat().st_size > 500:
            print(f"skip existing: {slug}")
            count += 1
            continue
        en_path = EN_DIR / f"{slug}.md"
        en_body = strip_en(en_path.read_text(encoding="utf-8"))
        zh_title, summary, intro = META[slug]
        print(f"translating {slug} ({len(en_body)} chars)...")
        zh_body = translate_body(en_body)
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
    print(f"batch10 count: {count}")


if __name__ == "__main__":
    main()
