#!/usr/bin/env python3
"""Post-fix batch 10 machine translations for Canton/Daml terminology."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs/education/canton-dev/zh-cursor"

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

FIXES = [
    ("广州节点", "Canton 节点"),
    ("广州配置", "Canton 配置"),
    ("每个广州", "每个 Canton"),
    ("政党注册", "party 注册"),
    ("政党", "Party"),
    ("协定参数", "合约参数"),
    ("协定", "合约"),
    ("合同", "合约"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<注意>", "<Note>"),
    ("</注意>", "</Note>"),
    ("</注>", "</Note>"),
    ("<卡组列={2}>", '<CardGroup cols={2}>'),
    ("<卡组", "<CardGroup"),
    ("</卡组>", "</CardGroup>"),
    ('<卡标题="生命周期">', '<Card title="Lifecycle">'),
    ('<卡标题="通知">', '<Card title="Notices">'),
    ('<卡标题=“生命周期”>', '<Card title="Lifecycle">'),
    ('<卡标题=“通知”>', '<Card title="Notices">'),
    ("<卡标题", "<Card title"),
    ("</卡>", "</Card>"),
    ("  稳定。", "    Stable."),
    ("  阿尔法（实验）。", "    Alpha (experimental)."),
    ("<手风琴组>", "<AccordionGroup>"),
    ("</手风琴组>", "</AccordionGroup>"),
    ("<手风琴 ", "<Accordion "),
    ("</手风琴>", "</Accordion>"),
    ("# DA.Action\n\n行动\n", "# DA.Action\n\nAction\n"),
    ("根本不评价", "根本不会求值"),
    ("如果布尔值`final`为，则将归档合同", "若布尔值 `final` 为 `True`，则归档合约"),
    ("`True`，否则什么都不做", "；否则无操作"),
    (" 选择、", " choice、"),
    ("选择、数据", "choice、数据"),
    ("# 选择", "# Choice"),
    ("选择结构", "Choice 结构"),
    ("选择参数", "choice 参数"),
    ("选择名称", "choice 名称"),
    ("选择体", "choice 体"),
    ("选择观察者", "choice 观察者"),
    ("预消费选择", "预消费 choice"),
    ("后消费选择", "后消费 choice"),
    ("非消费选择", "非消费 choice"),
    ("> Daml 模板、选择、", "> Daml 模板、choice、"),
    ("> Daml 模块", "> Daml 模块"),  # noop anchor
]

# Remove duplicate intro block when two consecutive > lines are similar
import re

DUP_INTRO = re.compile(r"(> [^\n]+\n\n)> [^\n]+\n\n")


def fix_body(body: str) -> str:
    for a, b in FIXES:
        body = body.replace(a, b)
    body = DUP_INTRO.sub(r"\1", body, count=1)
    return body


def main() -> None:
    for slug in SLUGS:
        path = OUT / f"{slug}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["body"] = fix_body(data["body"])
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"fixed {slug}")
    print("done", len(SLUGS))


if __name__ == "__main__":
    main()
