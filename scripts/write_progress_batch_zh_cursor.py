#!/usr/bin/env python3
"""Translate slugs from translate-progress.json batch → zh-cursor JSON (EN → zh-CN)."""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator

ROOT = Path(__file__).resolve().parents[1]
PROGRESS_PATH = ROOT / "docs/education/canton-dev/translate-progress.json"
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)
CODE_FENCE = re.compile(r"```[\s\S]*?```")
INLINE_CODE = re.compile(r"`[^`\n]+`")
TITLE_FM = re.compile(r'^title:\s*"([^"]+)"', re.M)

translator = GoogleTranslator(source="en", target="zh-CN")

TERM_FIXES: list[tuple[str, str]] = [
    ("Global Synchronizer", "全局同步器"),
    ("global synchronizer", "全局同步器"),
    ("Super Validator", "超级验证者"),
    ("super validator", "超级验证者"),
    ("Participant Node", "参与方节点"),
    ("participant node", "参与方节点"),
    ("Synchronizer", "同步器"),
    ("synchronizer", "同步器"),
    ("Canton Network", "Canton Network"),
    ("Canton Coin", "Canton Coin"),
    ("Ledger API", "Ledger API"),
    ("Admin API", "Admin API"),
    ("Protobuf", "Protobuf"),
    ("gRPC", "gRPC"),
    ("PackageService", "PackageService"),
    ("Participant", "参与方"),
    ("participant", "参与方"),
    ("Validator", "验证者"),
    ("validator", "验证者"),
    ("Sequencer", "Sequencer"),
    ("Mediator", "Mediator"),
    ("Canton", "Canton"),
    ("Daml", "Daml"),
    ("DAR", "DAR"),
    ("ACS", "ACS"),
    ("DevNet", "DevNet"),
    ("TestNet", "TestNet"),
    ("MainNet", "MainNet"),
    ("广州", "Canton"),
    ("广州网络", "Canton Network"),
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


def en_title(raw: str) -> str:
    m = TITLE_FM.search(raw)
    if m:
        return m.group(1)
    for line in raw.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Reference"


def summary_for(slug: str, title: str) -> str:
    if "protobuf-operations" in slug:
        return f"Admin API Protobuf 操作参考：{title}。"
    if "protobuf-index" in slug or slug.endswith("-index"):
        return f"Admin API Protobuf 索引与包浏览：{title}。"
    if slug.startswith("reference-"):
        return f"Canton 参考文档：{title}。"
    return f"{title} 中文镜像。"


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
    expanded: list[str] = []
    for part in parts:
        if len(part) <= max_len:
            expanded.append(part)
            continue
        buf = ""
        for line in part.split("\n"):
            candidate = f"{buf}\n{line}" if buf else line
            if len(candidate) > max_len and buf.strip():
                expanded.append(buf)
                buf = line
            else:
                buf = candidate
        if buf.strip():
            expanded.append(buf)
    parts = expanded
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
    if out_path.exists() and out_path.stat().st_size > 500 and not force:
        print(f"  skip (exists): {slug}", flush=True)
        return True
    en_path = EN_DIR / f"{slug}.md"
    if not en_path.exists():
        print(f"missing EN: {slug}", file=sys.stderr)
        return False
    raw = en_path.read_text(encoding="utf-8")
    title = en_title(raw)
    zh_title = title
    summary = summary_for(slug, title)
    en_body = strip_en(raw)
    print(f"  translating {slug} ({len(en_body)} chars, ~{len(chunk_text(en_body))} chunks)...", flush=True)
    zh_body = translate_body(en_body)
    payload = {
        "zhTitle": zh_title,
        "summary": summary,
        "body": zh_body,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  wrote {out_path.name} ({len(payload['body'])} chars)", flush=True)
    return True


def load_batch(batch_id: str) -> list[str]:
    progress = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    batch = progress.get("batches", {}).get(batch_id)
    if not batch:
        raise SystemExit(f"Unknown batch: {batch_id}")
    return batch["slugs"]


def main() -> None:
    force = "--force" in sys.argv
    batch_id = None
    for arg in sys.argv[1:]:
        if arg.startswith("--batch="):
            batch_id = arg.split("=", 1)[1]
    if not batch_id:
        print("Usage: write_progress_batch_zh_cursor.py --batch=N [--force]", file=sys.stderr)
        sys.exit(1)
    slugs = load_batch(batch_id)
    n = 0
    print(f"=== batch {batch_id} ({len(slugs)} slugs) ===", flush=True)
    for slug in slugs:
        if write_slug(slug, force=force):
            n += 1
        time.sleep(0.25)
    print(f"batch {batch_id} count: {n}", flush=True)


if __name__ == "__main__":
    main()
