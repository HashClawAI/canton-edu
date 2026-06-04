#!/usr/bin/env python3
"""Post-fix batch 22 zh-cursor JSON: Canton MT errors, MDX tags, placeholder tokens."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"
EN = ROOT / "docs/education/canton-dev/en"

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

REPLACEMENTS: list[tuple[str, str]] = [
    ("广州二进制", "Canton 二进制"),
    ("广州的内部状况", "Canton 内部状态"),
    ("对坎顿感与趣", "对 Canton 感兴趣"),
    ("坎顿感", "Canton"),
    ("广州", "Canton"),
    ("坎顿", "Canton"),
    ("</标签>", "</Tabs>"),
    ("<标签>", "<Tabs>"),
    ("与会者的端口", "participant 的端口"),
    ("直接访问Canton节点流程", "直接访问 Canton 节点进程"),
    ("音序器控制台", "Sequencer 控制台"),
    ("中介控制台", "Mediator 控制台"),
    ("定序器", "Sequencer"),
    ("调解器", "Mediator"),
    ("参与者控制台", "Participant 控制台"),
]

PLACEHOLDER_RE = re.compile(r"⟦P(\d+)⟧")
FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def fix_body(body: str) -> str:
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    return body


def restore_placeholders(slug: str, body: str) -> str:
    if not PLACEHOLDER_RE.search(body):
        return body
    en_path = EN / f"{slug}.md"
    if not en_path.exists():
        return body
    fences = FENCE_RE.findall(en_path.read_text(encoding="utf-8"))
    if not fences:
        return body

    def repl(m: re.Match[str]) -> str:
        idx = int(m.group(1))
        if idx < len(fences):
            return fences[idx]
        return m.group(0)

    return PLACEHOLDER_RE.sub(repl, body)


def main() -> None:
    n = 0
    for slug in BATCH22:
        path = OUT / f"{slug}.json"
        if not path.exists():
            print(f"missing: {slug}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        body = fix_body(data["body"])
        body = restore_placeholders(slug, body)
        data["body"] = body
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print(f"fixed {slug}")
    print(f"total: {n}")


if __name__ == "__main__":
    main()
