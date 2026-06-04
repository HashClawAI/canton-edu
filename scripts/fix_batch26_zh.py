#!/usr/bin/env python3
"""Post-process batch 26 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
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

REPLACEMENTS = [
    ("验证器", "验证者"),
    ("排序器", "Sequencer"),
    ("定序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("中介者", "Mediator"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<注意>", "<Note>"),
    ("</注意>", "</Note>"),
    ("</注>", "</Note>"),
    ("<笔记>", "<Note>"),
    ("</笔记>", "</Note>"),
    ("全球同步器", "全局同步器"),
    ("全局同步器 ", "全局同步器"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("熔接指标", "Splice 指标"),
    ("熔接", "Splice"),
    ("在广州提交", "在 Canton 中提交"),
    ("去中心化的聚会", "去中心化 Party"),
    ("聚会托管", "Party 托管"),
    ("聚会复制", "Party 复制"),
    ("政党", "Party"),
    ("聚会", "Party"),
    ("各方", "Party"),
    ("参与方", "Party"),
    ("举办派对", "创建 Party"),
    ("团体", "Party"),
    ("/api/验证者/", "/api/validator/"),
    ("participant.修剪", "participant.pruning"),
    ("participant1.同步器s", "participant1.synchronizers"),
    ("同步器Id", "synchronizerId"),
    ("同步器s", "synchronizers"),
    ("my-同步器", "my-synchronizer"),
    ("产品-操作", "production-operations"),
    ("sv-修剪", "sv-pruning"),
    ("修剪.set_participant_schedule", "pruning.set_participant_schedule"),
    ("#monitoring-choices", "#monitoring-choices"),
    ("广东", "Canton"),
    ("分类账", "账本"),
    ("包装", "包"),
    ("vetAllPackages", "vetAllPackages"),
    ("NetworkForVersion", "networksForVersion"),
    ("返回<前>", "return <pre>"),
    ("</前>", "</pre>"),
    ("退货选项", "return option"),
]


def fix_body(body: str) -> str:
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    # Drop leaked React fragment from LSU if strip missed
    leak = "  const labelForVersion"
    if leak in body:
        idx = body.find(leak)
        warn = body.find("<Warning>", idx)
        if warn != -1:
            body = body[:idx] + body[warn:]
    return body


def main() -> None:
    n = 0
    for slug in SLUGS:
        path = OUT / f"{slug}.json"
        if not path.exists():
            print(f"missing: {slug}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data["body"] = fix_body(data["body"])
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        n += 1
        print(f"fixed {slug}")
    print(f"count: {n}")


if __name__ == "__main__":
    main()
