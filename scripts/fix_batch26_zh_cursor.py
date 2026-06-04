#!/usr/bin/env python3
"""Post-process batch 26 zh-cursor JSON: Canton MT errors, MDX, code paths."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

BATCH26 = [
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

REPLACEMENTS: list[tuple[str, str]] = [
    ("&lt;", "<"),
    ("&gt;", ">"),
    ("api/验证者/", "api/validator/"),
    ("在广州提交", "在 Canton 上提交"),
    ("在广州", "在 Canton"),
    ("广州", "Canton"),
    ("坎顿", "Canton"),
    ("广东", "Canton"),
    ("global-同步器", "global-synchronizer"),
    ("/生产-操作/", "/production-operations/"),
    ("/生产运营/", "/production-operations/"),
    ("熔接指标", "splice-metrics"),
    ("熔接", "Splice"),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<标签>", "<Tabs>"),
    ("</标签>", "</Tabs>"),
    ("去中心化的聚会", "去中心化的 Party"),
    ("聚会托管", "Party 托管"),
    ("已在参与者上托管的聚会", "已在参与方上托管的 Party"),
    ("聚会复制", "Party 复制"),
    ("举办派对", "创建 Party"),
    ("管理 Canton 节点上的政党", "在 Canton 节点上管理 Party"),
    ("去中心化政党设置", "去中心化 Party 设置"),
    ("加入（本地）团体", "入驻（本地）Party"),
    ("各方是与", "Party 是"),
    ("他们可以加入参与者节点", "Party 可以入驻参与方节点"),
    ("如何加入新方", "如何入驻新 Party"),
    ("参与方的名称", "Party 的名称"),
    ("应将参与方分配", "应将 Party 分配"),
    ("有关分配方的元数据", "有关该 Party 的元数据"),
    ("`同步器Id`", "`synchronizerId`"),
    ("同步器Id", "synchronizerId"),
    ("participant1.同步器s", "participant1.synchronizers"),
    (" 同步器Id ", " synchronizerId "),
    ("my-同步器", "my-synchronizer"),
    ("Onboard 外部方", "入驻外部 Party"),
    ("去中心化方概述", "去中心化 Party 概述"),
    ("排序器容量", "Sequencer 容量"),
    ("在排序器之前", "在 Sequencer 之前"),
    ("排序器的备份", "Sequencer 的备份"),
    ("从同步器重放", "从同步器重放"),
    ("定序器 (`ForkHappened`)", "Sequencer (`ForkHappened`)"),
    ("来自定序器", "来自 Sequencer"),
    ("排序器上的队列", "Sequencer 上的队列"),
    ("participant.修剪.", "participant.pruning."),
    ("product-operations", "production-operations"),
    ("sv-修剪", "sv-pruning"),
    ("全局同步器 节点", "全局同步器节点"),
    ("1.配置KMS", "1. 配置 KMS"),
    ("2.GCP KMS", "2. GCP KMS"),
    ("参与者节点", "参与方节点"),
    ("参与节点", "参与方节点"),
    ("参与方节点的 Canton 端剪枝", "参与方节点的 Canton 修剪"),
    ("验证器", "验证者"),
]


def fix_body(body: str) -> str:
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    return body


def main() -> None:
    n = 0
    for slug in BATCH26:
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
