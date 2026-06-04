#!/usr/bin/env python3
"""Post-fix overview zh-cursor JSON: Canton mistranslations and broken MDX."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "overview-reference-ledger-model-detailed",
    "overview-reference-ordering-consensus",
    "overview-reference-pruning",
    "overview-reference-reassignment-protocol",
    "overview-reference-smart-contract-consensus",
    "overview-reference-splice-wallet-reference",
    "overview-reference-super-validator-components",
    "overview-reference-sv-governance-reference",
    "overview-reference-synchronizer-overview",
    "overview-reference-tokenomics-of-gs",
    "overview-reference-topology",
    "overview-reference-transaction-lifecycle",
    "overview-reference-validator-node-components",
    "overview-reference-what-are-cips",
    "overview-understand-canton-coin",
    "overview-understand-cantons-solution",
    "overview-understand-cips-introduction",
    "overview-understand-core-concepts",
    "overview-understand-five-minute-overview",
    "overview-understand-getting-app-featured",
    "overview-understand-global-synchronizer",
    "overview-understand-glossary",
    "overview-understand-the-problem",
    "overview-understand-use-cases",
    "overview-understand-what-is-canton",
    "overview-understand-who-should-read",
]

REPLACEMENTS: list[tuple[str, str]] = [
    ("global-同步器-foundation", "global-synchronizer-foundation"),
    ("global-同步器", "global-synchronizer"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("五分钟-overview", "five-minute-overview"),
    ("广州改进提案", "Canton 改进提案"),
    ("坎顿改进提案", "Canton 改进提案"),
    ("广州网络标准", "Canton Network 标准"),
    ("广州网络概念的权威术语参考", "Canton Network 概念权威术语参考"),
    ("广州网络", "Canton Network"),
    ("广州网", "Canton Network"),
    ("广州币", "Canton Coin"),
    ("广币", "Canton Coin"),
    ("什么是广币", "什么是 Canton Coin"),
    ("了解广州币", "了解 Canton Coin"),
    ("广东币 (CC)", "Canton Coin (CC)"),
    ("广州控制台", "Canton Console"),
    ("广州政党有身份", "Canton 参与方具有身份"),
    ("广州改进提案 (CIP)", "Canton 改进提案 (CIP)"),
    ("## 坎顿解决的问题", "## Canton 要解决的问题"),
    ("坎顿拓扑管理", "Canton 拓扑管理"),
    ("坎顿改进提案", "Canton 改进提案"),
    ("坎顿颠倒", "Canton 颠覆"),
    ("坎顿的核心创新", "Canton 的核心创新"),
    ("### 广州", "### Canton"),
    ("## 广州有何不同", "## Canton 有何不同"),
    ("## 何时使用广州", "## 何时使用 Canton"),
    ("|为什么广州适合|", "|为何适合 Canton|"),
    ("|为什么广州可能不适合|", "|为何可能不适合 Canton|"),
    ("广州提供：", "Canton 提供："),
    ("都可以进入广州", "都可以接入 Canton Network"),
    ("### 关于广州", "### 在 Canton 上"),
    ("在Canton，", "在 Canton，"),
    ("### 广州\n", "### Canton\n"),
    ("**广州**", "**Canton**"),
    ("广州是底层技术", "Canton 是底层技术"),
    ("运行在Canton协议", "运行在 Canton 协议"),
    ("“流量”是Canton", "「流量」是 Canton"),
    ("将Canton Coin", "将 Canton Coin"),
    ("加入Canton Network", "加入 Canton Network"),
    ("想了解Canton", "想了解 Canton"),
    ("广州概念和模式", "Canton 概念与模式"),
    ("<卡组列={2}>", "<CardGroup cols={2}>"),
    ("</卡>", "</Card>"),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("icon=\"服务器\"", 'icon="server"'),
    ("## 派对", "## 参与方 (Party)"),
    ("**当事人**是 Canton", "**参与方 (Party)** 是 Canton"),
    ("### 派对做什么", "### 参与方能做什么"),
    ("**本地聚会**", "**本地参与方**"),
    ("聚会管理", "参与方管理"),
    ("精心设计你的政党结构", "精心设计参与方结构"),
    ("不要创建不必要的政党", "不要创建不必要的参与方"),
    ("超级验证者s", "超级验证者"),
    ("Delivery vs. Payment (DvP)", "货银对付（DvP）"),
    ("交货与付款 (DvP)", "货银对付（DvP）"),
    ("前期风险", "抢跑风险"),
    ("1.Alice提交", "1. Alice 提交"),
    ("【Canton Network网站】", "[Canton Network 网站]"),
    ("坎顿网络", "Canton Network"),
    ("坎顿采取了", "Canton 采取"),
    ("坎顿的利益相关者", "Canton 的利益相关者"),
    ("在广州架构中的角色", "在 Canton 架构中的角色"),
    ("全局同步器 Foundation", "Global Synchronizer Foundation"),
    ("|派对 |", "|参与方 |"),
    ("Canton网络生态系统", "Canton Network 生态系统"),
    ("Canton Network成为", "Canton Network 成为"),
    ("用Daml编写", "用 Daml 编写"),
    ("2.交易进入", "2. 交易进入"),
    ("5.任何人", "5. 任何人"),
    ("Canton的核心创新", "Canton 的核心创新"),
    ("每个Canton节点", "每个 Canton 节点"),
    ("在Canton，", "在 Canton，"),
    ("转化为Canton", "转化为 Canton"),
    ("Canton与传统", "Canton 与传统"),
]


def fix_body(body: str) -> str:
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    # Residual 广州 when clearly Canton (not city names in examples)
    body = re.sub(r"(?<![\u4e00-\u9fff])广州(?![市省])", "Canton", body)
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
        print(f"fixed {slug}")
    print(f"total: {n}")


if __name__ == "__main__":
    main()
