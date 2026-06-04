#!/usr/bin/env python3
"""Post-process batch 31 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-understand-installing-daml-sdk",
    "global-synchronizer-understand-introduction",
    "global-synchronizer-understand-local-testing",
    "global-synchronizer-understand-overview",
    "global-synchronizer-understand-validator-roles",
]

REPLACEMENTS = [
    ("验证器", "验证者"),
    ("验证人", "验证者"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("<标签>", "<Tabs>"),
    ("</标签>", "</Tabs>"),
    ("<卡组列={2}>", "<CardGroup cols={2}>"),
    ("</卡组>", "</CardGroup>"),
    ("<卡>", "<Card"),
    ("</卡>", "</Card>"),
    ("global-同步器", "global-synchronizer"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("https://www.canton.network/global-同步器", "https://www.canton.network/global-synchronizer"),
    ("广州网", "Canton Network"),
    ("广州网络", "Canton Network"),
    ("广州", "Canton"),
    ("广东币", "Canton Coin"),
    ("粤币", "Canton Coin"),
    ("广币", "Canton Coin"),
    ("全球同步器", "全局同步器"),
    ("**主办方**", "**托管 Party**"),
    ("主办派对", "托管 Party"),
    ("举办聚会", "托管 party"),
    ("政党管理", "Party 管理"),
    ("派对钥匙", "Party 密钥"),
    ("为您的聚会", "为您的 party"),
    ("**松弛**", "**Slack**"),
    ("招摇用户界面", "Swagger UI"),
    ("http://钱包.localhost", "http://wallet.localhost"),
    ("127.0.0.1   钱包.localhost", "127.0.0.1   wallet.localhost"),
    ("app-同步器", "app-synchronizer"),
    ("同步器定序器", "同步器 Sequencer"),
    ("同步器中介", "同步器 Mediator"),
    ("操作同步器基础设施（排序器、中介节点）", "运营同步器基础设施（Sequencer、Mediator 节点）"),
    ("定序器/中介器", "Sequencer/Mediator"),
    ("**排序**", "**排序**"),
    ("**中介**", "**中介**"),
    ("超级验证者s", "Super Validators"),
    ("超级验证人", "超级验证者"),
    ("验证者-roles", "validator-roles"),
    ("验证者 Node", "Validator Node"),
    ("Your 验证者 Node", "Your Validator Node"),
    ("subgraph 验证者[Your Validator Node]", "subgraph Validator[Your Validator Node]"),
    ("广州/拼接开发", "Canton/Splice 开发"),
    ("广东币应用", "Canton Coin 应用"),
    ("销毁薄荷币", "销毁-铸造"),
    ("White论文", "白皮书"),
    (" payment%20application", "%20payment%20application"),
    ("\\(whitepapers", "(whitepapers"),
    ("etc...\\)", "etc...)"),
    ("infrastruction-requirements", "infrastructure-requirements"),
    ("**交通**", "**流量**"),
    ("交通管理", "流量管理"),
    ("交通费", "流量费"),
    ("**交通费**", "**流量费**"),
    ("参与者\\_LEDGER\\_API\\_PORT\\_SUFFIX", "PARTICIPANT_LEDGER_API_PORT_SUFFIX"),
    ("参与者\\_ADMIN\\_API\\_PORT\\_SUFFIX", "PARTICIPANT_ADMIN_API_PORT_SUFFIX"),
    ("参与者\\_JSON\\_API\\_PORT\\_SUFFIX", "PARTICIPANT_JSON_API_PORT_SUFFIX"),
    ("验证者\\_ADMIN\\_API\\_PORT\\_SUFFIX", "VALIDATOR_ADMIN_API_PORT_SUFFIX"),
    ("应用\\_用户\\_UI\\_端口", "APP_USER_UI_PORT"),
    ("**应用\\_用户\\_UI\\_端口**", "**APP_USER_UI_PORT**"),
    ("[da-support@digitalasset.com]（邮件至：da-support@digitalasset.com）", "[da-support@digitalasset.com](mailto:da-support@digitalasset.com)"),
    ("icon=\"服务器\"", "icon=\"server\""),
    ("#验证器操作", "#validator-operations"),
    ("#验证者-操作用于", "#validator-operations 用于"),
    ("验证者设置", "验证者部署"),
    ("不要**操作", "**不** 运营"),
    ("不要**直接", "**不** 直接"),
    ("不要**运行", "**不** 运行"),
    ("进步路径", "进阶路径"),
    ("季刊", "每季度"),
    ("批判的;", "关键；"),
    ("入职秘密", "入驻密钥"),
    ("获取入职秘密", "获取入驻密钥"),
    ("入门配置", "入驻配置"),
    ("入职流程", "入驻流程"),
    ("完全上线", "完整入驻"),
    ("应用程序进程", "申请流程"),
    ("应用程序审批", "申请审批"),
    ("测试网→主网", "TestNet → MainNet"),
    ("暂存环境", "预发布环境"),
    ("商店合同", "存储合约"),
    ("为应用程序公开", "为应用暴露"),
    ("版本货币", "版本时效"),
    ("通讯", "沟通"),
    ("全权决定", "酌情"),
    ("基于 SLA", "SLA"),
    ("随音量变化", "随数据量变化"),
    ("扫描网页用户界面", "Scan Web UI"),
    ("扫描 UI", "Scan UI"),
    ("存储其主办方的合同数据", "存储其所托管 Party 的合约数据"),
    ("确认影响其各方的交易", "确认影响其 Party 的交易"),
    ("赞助您的入职", "赞助您的入驻"),
    ("超级验证者必须赞助您的入职", "超级验证者必须赞助您的入驻"),
    ("托管 Party和存储合约", "托管 Party 并存储合约"),
]

DUPLICATE_INTRO = [
    (
        "> 安装与当前 Splice 版本兼容的 Daml SDK 的方法。\n\n> 如何安装与当前 Splice 版本兼容的 Daml SDK 版本\n\n",
        "> 安装与当前 Splice 版本兼容的 Daml SDK 的方法。\n\n",
    ),
    (
        "> 全局同步器上验证者节点运维入门指南。\n\n> 了解 Canton Network 全局同步器 上的验证者节点操作\n\n",
        "> 全局同步器上验证者节点运维入门指南。\n\n",
    ),
    (
        "> 全局同步器上验证者节点运维入门指南。\n\n> 了解 Canton Network 全局同步器 上的验证人节点操作\n\n",
        "> 全局同步器上验证者节点运维入门指南。\n\n",
    ),
    (
        "> LocalNet 本地开发与测试环境部署指南。\n\n> 基于 Docker-Compose 部署本地 Canton 网络进行开发和测试\n\n",
        "> LocalNet 本地开发与测试环境部署指南。\n\n",
    ),
    (
        "> 全局同步器及其在 Canton Network 中的角色概览。\n\n> 全球同步器是什么以及它如何融入 Canton 网络\n\n",
        "> 全局同步器及其在 Canton Network 中的角色概览。\n\n",
    ),
    (
        "> 验证者在 Canton Network 上的角色、职责与运维期望。\n\n> 了解在 Canton Network 上运行验证人意味着什么\n\n",
        "> 验证者在 Canton Network 上的角色、职责与运维期望。\n\n",
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
    print(f"fix batch 31 count: {n}")


if __name__ == "__main__":
    main()
