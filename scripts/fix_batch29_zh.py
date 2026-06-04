#!/usr/bin/env python3
"""Post-process batch 29 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-reference-metrics-reference",
    "global-synchronizer-reference-observability-configuration",
    "global-synchronizer-reference-security-configuration",
    "global-synchronizer-release-notes-canton",
    "global-synchronizer-release-notes-splice",
    "global-synchronizer-splice-fundamentals-glossary",
    "global-synchronizer-splice-fundamentals-rewards-minting",
    "global-synchronizer-splice-fundamentals-sv-live-tokenomics",
    "global-synchronizer-splice-fundamentals-validator-development-fund",
    "global-synchronizer-splice-fundamentals-validator-liveness",
]

REPLACEMENTS = [
    ("验证器", "验证者"),
    ("验证节点", "验证者节点"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("<笔记>", "<Note>"),
    ("</笔记>", "</Note>"),
    ("global-同步器", "global-synchronizer"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("广州", "Canton"),
    ("广东", "Canton"),
    ("定序器", "Sequencer"),
    ("排序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("中介者", "Mediator"),
    ("调解者", "Mediator"),
    ("daml.参与方", "daml.participant"),
    ("验证者s", "validators"),
    ("超级验证人", "超级验证者"),
    ("代币经济委员会", "tokenomics 委员会"),
    ("代币经济学委员会", "tokenomics 委员会"),
    ("活跃合约集", "Active Contract Set"),
    ("护身符", "Amulet"),
    ("Amulet 名称服务", "Amulet Name Service"),
]

DUPLICATE_INTRO = [
    (
        "> 超级验证者节点获得与分配 Canton Coin 奖励的机制。\n\n> 超级验证人节点如何赚取和分配Canton Coin奖励\n\n",
        "> 超级验证者节点获得与分配 Canton Coin 奖励的机制。\n\n",
    ),
    (
        "> 验证者活跃度奖励与相关代币经济学。\n\n> 验证者活跃度奖励及其背后的代币经济学\n\n",
        "> 验证者活跃度奖励与相关代币经济学。\n\n",
    ),
    (
        "> Canton Network 验证者与超级验证者节点监控指标参考。\n\n> Canton Network 验证器和超级验证器节点公开的监控指标参考\n\n",
        "> Canton Network 验证者与超级验证者节点监控指标参考。\n\n",
    ),
    (
        "> 在 Canton 节点上配置日志、追踪、指标与健康监控。\n\n> 在 Canton 节点上配置日志记录、跟踪、指标运行状况监控。\n\n",
        "> 在 Canton 节点上配置日志、追踪、指标与健康监控。\n\n",
    ),
    (
        "> Global Synchronizer 软件发布说明与版本历史。\n\n> Global Synchronizer 软件的发行说明和版本历史\n\n",
        "> Global Synchronizer 软件发布说明与版本历史。\n\n",
    ),
]


def fix_body(body: str) -> str:
    for old, new in DUPLICATE_INTRO:
        body = body.replace(old, new)
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
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
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print(f"fixed: {slug}")
    print(f"fix batch 29 count: {n}")


if __name__ == "__main__":
    main()
