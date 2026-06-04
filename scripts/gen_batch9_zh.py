#!/usr/bin/env python3
"""Assemble batch 9 zh-cursor JSON from EN sources + Chinese bodies."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
BODY_DIR = Path(__file__).parent / "_batch9_bodies"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
DOC_INDEX_RE = re.compile(r"> ## Documentation Index\n.*?\n\n", re.DOTALL)


def strip_en(md: str) -> str:
    md = FRONTMATTER_RE.sub("", md)
    md = DOC_INDEX_RE.sub("", md)
    md = FOOTER_RE.sub("", md)
    lines = md.splitlines()
    while lines:
        line = lines[0].strip()
        if not line or line.startswith("# ") or (line.startswith("> ") and "Documentation Index" not in line):
            if line.startswith("# ") or (line.startswith("> ") and "llms.txt" not in line):
                lines.pop(0)
                continue
        break
    # drop duplicate H1 and doc index block
    out = []
    skip_next_quote = False
    for i, line in enumerate(lines):
        if i == 0 and line.startswith("# "):
            continue
        if line.startswith("> ## Documentation Index"):
            skip_next_quote = True
            continue
        if skip_next_quote and line.startswith("> "):
            skip_next_quote = False
            continue
        if line.startswith("> ") and "llms.txt" in line:
            continue
        out.append(line)
    return "\n".join(out).strip()


META = {
    "appdev-quickstart-deploy-to-devnet": {
        "zhTitle": "将 Quickstart 部署到 DevNet",
        "summary": "从 LocalNet 把 Quickstart 部署到 DevNet：验证者申请、VPN、主机名与端到端验证。",
        "intro": "将 Quickstart 应用从 LocalNet 部署到 DevNet，含验证者申请、VPN 配置与端到端工作流验证。",
    },
    "appdev-quickstart-external-parties": {
        "zhTitle": "在 Quickstart 中接入外部 Party",
        "summary": "外部 Party 自管签名密钥：OpenSSL 密钥、拓扑 API 与交互式提交三步流程。",
        "intro": "在 Canton Network Quickstart 中接入并使用外部 Party 的分步指南，含 OpenSSL 密钥、拓扑 API 与签名流程。",
    },
    "appdev-quickstart-json-api": {
        "zhTitle": "使用 JSON Ledger API",
        "summary": "在 LocalNet 用 JSON Ledger API 创建 Party、上传 DAR、建合约并完成许可续期全流程。",
        "intro": "在 Canton Network Quickstart 环境中使用 JSON Ledger API。",
    },
    "appdev-quickstart-lnav": {
        "zhTitle": "使用 lnav 调试",
        "summary": "用 lnav 查看、过滤与分析 Quickstart 的 Canton 结构化日志与 trace ID。",
        "intro": "使用 lnav 交互式检查 Canton quickstart 日志。",
    },
    "appdev-quickstart-observability-and-tracing": {
        "zhTitle": "可观测性与链路追踪",
        "summary": "Quickstart 可观测性栈：Grafana、Tempo、Prometheus、lnav 与关联 ID 排障。",
        "intro": "跨 Quickstart 组件观测与追踪请求。",
    },
    "appdev-quickstart-prerequisites": {
        "zhTitle": "前置条件与安装",
        "summary": "CN Quickstart 环境要求：Docker、Nix、Direnv 与 LocalNet 分步/快速安装。",
        "intro": "配置开发环境并安装 Canton Network Quickstart。",
    },
    "appdev-quickstart-project-structure": {
        "zhTitle": "项目结构",
        "summary": "cn-quickstart 目录、Gradle/Make、Docker Compose 与许可应用四层架构说明。",
        "intro": "理解 Canton Network QuickStart 项目布局与组件架构。",
    },
    "appdev-quickstart-running-the-demo": {
        "zhTitle": "运行演示",
        "summary": "启动 Quickstart 许可演示：安装请求、续期、Canton 钱包付款与 Console/Shell。",
        "intro": "启动 Canton Network QuickStart 演示并走通许可工作流。",
    },
}


def load_body(slug: str) -> str:
    zh_path = BODY_DIR / f"{slug}.zh.txt"
    if zh_path.exists():
        return zh_path.read_text(encoding="utf-8").strip()
    raise FileNotFoundError(f"Missing Chinese body: {zh_path}")


def main() -> None:
    slugs = [
        "appdev-quickstart-deploy-to-devnet",
        "appdev-quickstart-external-parties",
        "appdev-quickstart-json-api",
        "appdev-quickstart-lnav",
        "appdev-quickstart-observability-and-tracing",
        "appdev-quickstart-prerequisites",
        "appdev-quickstart-project-structure",
        "appdev-quickstart-running-the-demo",
    ]
    count = 0
    for slug in slugs:
        m = META[slug]
        body = f"> {m['intro']}\n\n" + load_body(slug)
        payload = {"zhTitle": m["zhTitle"], "summary": m["summary"], "body": body}
        out = OUT_DIR / f"{slug}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out.name} ({len(body)} chars)")
        count += 1
    print(f"batch9 generated: {count}")


if __name__ == "__main__":
    main()
