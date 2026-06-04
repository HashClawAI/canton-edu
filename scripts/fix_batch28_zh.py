#!/usr/bin/env python3
"""Post-process batch 28 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-production-operations-validator-upgrades",
    "global-synchronizer-reference-api-configuration",
    "global-synchronizer-reference-canton-configuration-guide",
    "global-synchronizer-reference-canton-console-commands",
    "global-synchronizer-reference-canton-console-reference",
    "global-synchronizer-reference-canton-metrics",
    "global-synchronizer-reference-configuration-reference",
    "global-synchronizer-reference-crypto-schemes",
    "global-synchronizer-reference-error-codes",
    "global-synchronizer-reference-kms-driver-guide",
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
    ("<图>", "<figure>"),
    ("</图>", "</figure>"),
    ("<图片", "<img"),
    ("global-同步器", "global-synchronizer"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("广州", "Canton"),
    ("广东", "Canton"),
    ("知识管理系统", "KMS"),
    ("定序器", "Sequencer"),
    ("排序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("中介者", "Mediator"),
    ("调解者", "Mediator"),
    ("远程-参与方s", "remote-participants"),
    ("参与方 {", "participant {"),
    ("参与方1", "participant1"),
    ("参与方2", "participant2"),
    ("参与方3", "participant3"),
    (" 参与方 {", " participant {"),
    ("standalone-验证者-values.yaml", "standalone-validator-values.yaml"),
    ("生产-操作", "production-operations"),
    ("Splice 指标-概述", "splice-metrics-overview"),
    ("生产运营", "production-operations"),
    (".拓扑.", ".topology."),
    ("拓扑.", "topology."),
    ("拓扑StoreId", "TopologyStoreId"),
    ("拓扑Store", "TopologyStore"),
    ("Signed拓扑Transaction", "SignedTopologyTransaction"),
    ("GenericSigned拓扑Transaction", "GenericSignedTopologyTransaction"),
    ("拓扑.Namespace", "Topology.Namespace"),
    ("拓扑.transaction", "topology.transaction"),
    ("com.digitalasset.canton.拓扑.", "com.digitalasset.canton.topology."),
    ("<div id=\"退出\"/>", "<div id=\"exit\"/>"),
    ("<div id=\"帮助\"/>", "<div id=\"help\"/>"),
    ("* **警告**", "* **WARN**"),
    ("警告和错误", "WARN 和 ERROR"),
    ("警告级别", "WARN 级别"),
    ("daml.参与方", "daml.participant"),
    ("daml.sequencer-client.流量-control", "daml.sequencer-client.traffic-control"),
    ("daml.sequencer.流量-control", "daml.sequencer.traffic-control"),
    ("traffic-control.wasted-流量", "traffic-control.wasted-traffic"),
    ("wasted-流量-counter", "wasted-traffic-counter"),
    ("in-flight-submission-同步器-tracker", "in-flight-submission-synchronizer-tracker"),
    ("connected-同步器s", "connected-synchronizers"),
    ("routing-同步器", "routing-synchronizer"),
    ("highest-ranked-同步器", "highest-ranked-synchronizer"),
    ("admissible-同步器", "admissible-synchronizer"),
    ("submit\\_重分配", "submit_reassignment"),
    ("重分配\\_validation", "reassignment_validation"),
    ("read.incomplete\\_重分配", "read.incomplete_reassignment"),
    ("services.修剪.", "services.pruning."),
    ("get\\_参与方\\_id", "get_participant_id"),
    ("list\\_known\\_partys", "list_known_parties"),
    ("counter-参与方-latency", "counter-participant-latency"),
    ("largest-counter-参与方-latency", "largest-counter-participant-latency"),
    ("largest-distinguished-counter-参与方-latency", "largest-distinguished-counter-participant-latency"),
    ("timeout-非响应参与者", "timeout-non-responding-participants"),
    ("验证者s", "validators"),
    ("grpc-延迟", "grpc-latency"),
    ("## 定序器指标", "## Sequencer 指标"),
    ("## 中介指标", "## Mediator 指标"),
    ("定序器处理", "Sequencer 处理"),
    ("排序器处理", "Sequencer 处理"),
    ("排序器收到", "Sequencer 收到"),
    ("排序器接受", "Sequencer 接受"),
    ("排序器订阅", "Sequencer 订阅"),
    ("排序器连接", "Sequencer 连接"),
    ("排序器客户端", "Sequencer 客户端"),
    ("排序器日志", "Sequencer 日志"),
    ("排序器见证", "Sequencer 见证"),
    ("排序器对", "Sequencer 对"),
    ("排序器无法", "Sequencer 无法"),
    ("排序器可能", "Sequencer 可能"),
    ("排序器已满", "Sequencer 已满"),
    ("排序器太慢", "Sequencer 太慢"),
    ("排序器并不", "Sequencer 并不"),
    ("排序器总请求", "Sequencer 总请求"),
    ("排序器上", "Sequencer 上"),
    ("排序器读取", "Sequencer 读取"),
    ("排序器数据库", "Sequencer 数据库"),
    ("排序器节点", "Sequencer 节点"),
    ("排序器服务", "Sequencer 服务"),
    ("排序器将", "Sequencer 将"),
    ("排序器等待", "Sequencer 等待"),
    ("排序器进行", "Sequencer 进行"),
    ("排序器转发", "Sequencer 转发"),
    ("排序器公开", "Sequencer 公开"),
    ("排序器指标", "Sequencer 指标"),
    ("排序器处理", "Sequencer 处理"),
    ("排序器定序", "Sequencer 定序"),
    ("排序器排序", "Sequencer 排序"),
    ("P1", "P¹"),
    ("|主要规格|", "| Key Spec |"),
    ("|算法|", "| Algorithm |"),
    ("|目的|", "| Purpose |"),
    ("| JCE|", "| JCE |"),
    ("|知识管理系统 |", "| KMS |"),
    ("|支持的关键规格 |", "| Supported Key Specs |"),
    ("|支持的关键规", "| Supported Key Spec"),
    ("canton_ node_initialization", "canton_node_initialization"),
    ("canton_ node", "canton_node"),
]

DUPLICATE_INTRO = [
    (
        "> Canton 运维错误码、类别与常见操作错误说明。\n\n> Canton 错误代码、日志级别含义和错误类别的操作员参考\n\n",
        "> Canton 运维错误码、类别与常见操作错误说明。\n\n",
    ),
    (
        "> Canton 节点 Admin API、Ledger API 与 JSON API 配置。\n\n> 配置 Admin API、Ledger API、JSON Ledger API 和 Canton 节点的缓存。\n\n\n",
        "> Canton 节点 Admin API、Ledger API 与 JSON API 配置。\n\n",
    ),
    (
        "> 使用 HOCON 与命令行配置 Canton 节点的完整指南。\n\n> 使用 HOCON 文件、命令行选项和声明性配置配置 Canton 节点\n\n",
        "> 使用 HOCON 与命令行配置 Canton 节点的完整指南。\n\n",
    ),
    (
        "> Canton 管理控制台完整命令参考。\n\n> Canton 管理控制台命令参考：参与者、调解者、排序者和拓扑命令。\n\n",
        "> Canton 管理控制台完整命令参考。\n\n",
    ),
    (
        "> Global Synchronizer 运维使用的 Canton Console 参考。\n\n> 全局同步器上验证器和 SV 操作员使用的 Canton 控制台命令参考\n\n",
        "> Global Synchronizer 运维使用的 Canton Console 参考。\n\n",
    ),
    (
        "> Canton 节点 Prometheus 指标参考。\n\n> 为 Prometheus 抓取导出 Canton 节点指标。\n\n\n",
        "> Canton 节点 Prometheus 指标参考。\n\n",
    ),
    (
        "> Canton Network 验证者与 SV 完整配置参考。\n\n> Canton Network 验证器和 SV 算子的完整配置参考\n\n",
        "> Canton Network 验证者与 SV 完整配置参考。\n\n",
    ),
    (
        "> Canton 支持的密码学方案与密钥格式参考。\n\n> Canton 支持的加密方案和密钥格式参考\n\n",
        "> Canton 支持的密码学方案与密钥格式参考。\n\n",
    ),
    (
        "> 开发自定义 Canton KMS Driver 的开发者指南。\n\n> 开发自定义 Canton KMS 驱动程序。\n\n",
        "> 开发自定义 Canton KMS Driver 的开发者指南。\n\n",
    ),
    (
        "> 验证者节点版本升级与协议升级的操作说明。\n\n> 验证者节点的小升级过程\n\n",
        "> 验证者节点版本升级与协议升级的操作说明。\n\n",
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
    print(f"fix batch 28 count: {n}")


if __name__ == "__main__":
    main()
