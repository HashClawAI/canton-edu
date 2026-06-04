#!/usr/bin/env python3
"""Write batch 2 part 2 zh-cursor JSON translations (6 deep-dive docs)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "src/content/canton-doc-pages/en"
OUT = ROOT / "docs/education/canton-dev/zh-cursor"
BODIES_DIR = Path(__file__).parent / "batch2-zh-part2-bodies"

SLUGS = [
    "appdev-deep-dives-app-architecture-design",
    "appdev-deep-dives-command-deduplication",
    "appdev-deep-dives-explicit-contract-disclosure",
    "appdev-deep-dives-external-signing-hashing-algorithm",
    "appdev-deep-dives-external-signing-onboarding",
    "appdev-deep-dives-external-signing-topology",
]

META: dict[str, dict[str, str]] = {
    "appdev-deep-dives-app-architecture-design": {
        "zhTitle": "Canton Network 应用架构设计",
        "summary": "Canton 应用组件、后端读写路径、技术栈与三种部署架构的权衡与成本视角。",
    },
    "appdev-deep-dives-command-deduplication": {
        "zhTitle": "命令去重",
        "summary": "Daml 命令去重机制及应用在已知/未知处理时间边界下实现恰好一次账本变更。",
    },
    "appdev-deep-dives-explicit-contract-disclosure": {
        "zhTitle": "显式合约披露",
        "summary": "向非利益相关方链下披露合约，使提交方在交易中附带披露合约并绕过可见性限制。",
    },
    "appdev-deep-dives-external-signing-hashing-algorithm": {
        "zhTitle": "外部签名：哈希算法",
        "summary": "PreparedTransaction 确定性哈希规范（V2），供外部 Party 私钥签名授权账本变更。",
    },
    "appdev-deep-dives-external-signing-onboarding": {
        "zhTitle": "外部签名：Party 入网",
        "summary": "通过 Admin API 或 Ledger API 入网外部 Party：拓扑映射、多交易哈希签名与多方托管。",
    },
    "appdev-deep-dives-external-signing-topology": {
        "zhTitle": "外部签名：拓扑交易",
        "summary": "构建、签署并提交拓扑交易；哈希、指纹、命名空间委托与 Admin API 提交流程。",
    },
}


def write_doc(slug: str, data: dict) -> None:
    path = OUT / f"{slug}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path.name)


def main() -> int:
    written: list[str] = []
    failed: list[str] = []

    for slug in SLUGS:
        en_path = EN_DIR / f"{slug}.md"
        body_path = BODIES_DIR / f"{slug}.body.md"
        if not en_path.is_file():
            print("missing en source:", slug, file=sys.stderr)
            failed.append(slug)
            continue
        if slug not in META:
            print("missing meta:", slug, file=sys.stderr)
            failed.append(slug)
            continue
        if not body_path.is_file():
            print("missing body:", body_path, file=sys.stderr)
            failed.append(slug)
            continue
        body = body_path.read_text(encoding="utf-8").strip()
        if not body:
            print("empty body:", slug, file=sys.stderr)
            failed.append(slug)
            continue
        summary = META[slug]["summary"]
        if len(summary) > 120:
            print("summary exceeds 120 chars:", slug, file=sys.stderr)
            failed.append(slug)
            continue
        write_doc(slug, {"zhTitle": META[slug]["zhTitle"], "summary": summary, "body": body})
        written.append(slug)

    print("count", len(written))
    if failed:
        print("failed", ",".join(failed))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
