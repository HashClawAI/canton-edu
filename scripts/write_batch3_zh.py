#!/usr/bin/env python3
"""Write batch 3 zh-cursor JSON from English sources + embedded Chinese intros."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src/content/canton-doc-pages/en"
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

BATCH3 = [
    "appdev-deep-dives-external-signing-transactions",
    "appdev-deep-dives-manage-daml-parties",
    "appdev-deep-dives-multi-hosting",
    "appdev-deep-dives-open-tracing",
    "appdev-deep-dives-performance-optimization",
    "appdev-deep-dives-smart-contract-upgrade",
    "appdev-deep-dives-smart-contract-upgrading-reference",
    "appdev-deep-dives-tokenomics",
    "appdev-deep-dives-upgrading-architecture",
    "appdev-deep-dives-values-in-the-ledger-api",
]


def strip_en(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    text = re.sub(r"^# [^\n]+\n\n", "", text, count=1)
    text = re.sub(r"> ## Documentation Index\n>.*?\n\n", "", text, count=1, flags=re.S)
    text = re.sub(r"> [^\n]+\n\n", "", text, count=1)
    text = re.sub(r"\n---\n\n> Mirrored from.*", "", text, flags=re.S)
    return text.strip()


def split_blocks(text: str) -> list[str]:
    return re.split(r"(```[\s\S]*?```)", text)


def translate_chunk(chunk: str) -> str:
    if chunk.startswith("```") or not chunk.strip():
        return chunk
    # Section title replacements
    reps = [
        (r"^# (.+)$", lambda m: "# " + TITLES.get(m.group(1), m.group(1))),
    ]
    lines = chunk.split("\n")
    out_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped in LINE_ZH:
            out_lines.append(line.replace(stripped, LINE_ZH[stripped]))
        elif stripped.startswith("## ") and stripped[3:] in LINE_ZH:
            out_lines.append("## " + LINE_ZH[stripped[3:]])
        elif stripped.startswith("### ") and stripped[4:] in LINE_ZH:
            out_lines.append("### " + LINE_ZH[stripped[4:]])
        elif stripped.startswith("#### ") and stripped[5:] in LINE_ZH:
            out_lines.append("#### " + LINE_ZH[stripped[5:]])
        else:
            for en, zh in PHRASE_ZH.items():
                if en in line:
                    line = line.replace(en, zh)
            out_lines.append(line)
    return "\n".join(out_lines)


TITLES = {
    "Smart Contract Upgrade": "智能合约升级",
    "Smart Contract Upgrading Reference": "智能合约升级参考",
    "Performance Optimization": "性能优化",
    "External Signing: Submitting Transactions": "外部签名：提交交易",
    "Values in the Ledger API": "Ledger API 中的值",
}

LINE_ZH = {
    "Overview": "概览",
    "Network Scaling": "网络扩展",
    "Node Scaling": "节点扩展",
    "Performance and Sizing": "性能与容量规划",
    "Batching": "批处理",
    "Asynchronous Submissions": "异步提交",
    "Storage Estimation": "存储估算",
    "Set Up Canton to Get the Best Performance": "配置 Canton 以获得最佳性能",
    "Model Tuning": "模型 Tuning",
    "Problem Definition": "问题定义",
    "Relational Databases": "关系型数据库",
    "Contention in Daml": "Daml 中的争用",
    "Prerequisites": "前置条件",
    "Start Canton": "启动 Canton",
    "Setup": "设置",
    "API": "API",
    "Python": "Python",
    "Shell": "Shell",
    "Tooling": "工具",
    "Static Checks": "静态检查",
    "Packages": "包",
    "Modules": "模块",
    "Templates": "模板",
    "Template Parameters": "模板参数",
    "The Programming Model by Example": "编程模型示例",
    "Package Selection in the Ledger API": "Ledger API 中的包选择",
    "Best Practices": "最佳实践",
    "Testing": "测试",
    "SCU Support in Daml Tooling": "Daml 工具链中的 SCU 支持",
    "What is Smart Contract Upgrade (SCU)?": "什么是智能合约升级（SCU）？",
    "1. Prepare the transaction": "1. 准备交易",
    "2. Validate the transaction": "2. 校验交易",
    "3. Compute the transaction hash": "3. 计算交易哈希",
    "4. Sign the transaction hash": "4. 签署交易哈希",
    "5. Execute the transaction": "5. 执行交易",
    "6. Observe the transaction outcome": "6. 观察交易结果",
    "Exercise `Respond` Choice": "行使 `Respond` Choice",
    "Request": "请求",
    "Response": "响应",
    "Transaction": "交易",
    "Metadata": "元数据",
    "Hash": "哈希",
    "Hashing scheme version": "哈希方案版本",
    "Traffic cost estimation": "流量成本估算",
    "Value Validation in Commands": "命令中的值校验",
    "Value normalization in Ledger API responses": "Ledger API 响应中的值规范化",
}

PHRASE_ZH = {
    "Commands and queries have relaxed validation rules for ingested values. Returned values are subject to normalization.": "命令与查询对摄入的值采用宽松校验；返回的值须规范化。",
    "Smart Contract Upgrade (SCU) allows Daml models": "智能合约升级（SCU）允许在遵循指南的前提下更新 Daml 模型",
    "This document describes in detail": "本文详述",
    "The scaling and performance characteristics": "Canton 系统的扩展与性能特征取决于多种因素",
    "This tutorial demonstrates how to submit Daml commands": "本教程演示如何使用外部私钥向 Canton 账本提交 Daml 命令",
    "For simplicity, this tutorial assumes": "为简化起见，本教程假设",
    "It is strongly recommended that the transaction hash": "强烈建议客户端根据交易与元数据重新计算哈希",
}


INTROS = {
    "appdev-deep-dives-external-signing-transactions": (
        "> 向 Canton 账本提交外部签名的交易\n\n"
        "# 提交外部签名交易 — 第 1 部分\n\n"
        "本教程演示如何使用外部私钥授权提交 Daml 命令。建议先阅读外部签名概览。"
        "流程使用外部 Party `Alice`、`Bob` 及内置 Ping 模板。\n\n"
        "* 第 1 部分：`Alice` 创建 Ping 合约。\n"
        "* 第 2 部分：`Bob` exercise `Respond` 并归档。\n\n"
        "<Warning>仅供演示，勿直接用于生产。</Warning>\n\n"
    ),
    "appdev-deep-dives-performance-optimization": (
        "> 扩展 Canton 应用吞吐量与延迟：网络/节点扩展、争用、ACS、批处理与配置调优。\n\n"
        "# 扩展与性能\n\n"
    ),
    "appdev-deep-dives-smart-contract-upgrade": (
        "> 在 Daml 包版本间开发、部署并验证智能合约升级。\n\n"
        "# 智能合约升级\n\n"
    ),
    "appdev-deep-dives-smart-contract-upgrading-reference": (
        "> 上传时包校验与运行时合约/choice 升降级规则。\n\n"
        "# 智能合约升级参考\n\n"
        "本文详述包上传校验及运行时升级/降级行为，可作为 SCU 专题的完整参考。\n\n"
    ),
}

META = {
    "appdev-deep-dives-external-signing-transactions": ("外部签名：提交交易", "InteractiveSubmission 准备、签署、执行外部签名交易（含第 2 部分显式披露）。"),
    "appdev-deep-dives-manage-daml-parties": ("分配与查询 Daml Party", "通过 JSON Ledger API 在 participant 上创建与查询 Party。"),
    "appdev-deep-dives-multi-hosting": ("多托管与韧性", "多验证者托管同一 Party 以实现高可用与故障转移。"),
    "appdev-deep-dives-open-tracing": ("Ledger API 客户端 OpenTracing", "在 Daml 应用中接入 OpenTelemetry 分布式追踪。"),
    "appdev-deep-dives-performance-optimization": ("性能优化", "Canton 应用的网络/节点扩展、批处理、存储、配置与模型调优。"),
    "appdev-deep-dives-smart-contract-upgrade": ("智能合约升级（SCU）", "Daml 包透明升级：兼容规则、示例、包选择与测试。"),
    "appdev-deep-dives-smart-contract-upgrading-reference": ("智能合约升级参考", "DAR 上传静态检查与运行时升降级详细规则。"),
    "appdev-deep-dives-tokenomics": ("代币经济学", "轮次、活动记录、CC 转账、流量与奖励分配。"),
    "appdev-deep-dives-upgrading-architecture": ("升级架构考量", "异步 rollout、同步切换、向后兼容与回滚。"),
    "appdev-deep-dives-values-in-the-ledger-api": ("Ledger API 中的值", "值的宽松校验、规范化与动态包解析。"),
}

# Pre-translated bodies for shorter pages (skip if already on disk with good size)
EMBEDDED = {
    "appdev-deep-dives-multi-hosting": Path(__file__).parent / "_batch3_multi-hosting.body.txt",
    "appdev-deep-dives-open-tracing": Path(__file__).parent / "_batch3_open-tracing.body.txt",
    "appdev-deep-dives-tokenomics": Path(__file__).parent / "_batch3_tokenomics.body.txt",
    "appdev-deep-dives-values-in-the-ledger-api": Path(__file__).parent / "_batch3_values.body.txt",
    "appdev-deep-dives-manage-daml-parties": Path(__file__).parent / "_batch3_manage-parties.body.txt",
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in BATCH3:
        out_path = OUT / f"{slug}.json"
        if slug == "appdev-deep-dives-upgrading-architecture" and out_path.exists():
            count += 1
            continue
        if slug == "appdev-deep-dives-manage-daml-parties" and out_path.exists():
            count += 1
            continue

        title, summary = META[slug]
        if slug in EMBEDDED and EMBEDDED[slug].exists():
            body = EMBEDDED[slug].read_text(encoding="utf-8")
        else:
            en = strip_en((SRC / f"{slug}.md").read_text(encoding="utf-8"))
            intro = INTROS.get(slug, "> " + summary + "\n\n")
            body = intro + "".join(translate_chunk(c) for c in split_blocks(en))

        out_path.write_text(
            json.dumps({"zhTitle": title, "summary": summary, "body": body}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        count += 1
        print(slug)
    print("count", count)


if __name__ == "__main__":
    main()
