#!/usr/bin/env python3
"""Post-process batch 14 zh-cursor JSON: fix MT errors and untranslated blocks."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "appdev-reference-error-codes",
    "appdev-reference-pqs-sql-reference",
    "appdev-tooling-debugging-tools",
    "appdev-tooling-development-tools-overview",
    "appdev-tooling-ide-setup",
    "appdev-troubleshooting",
    "appdev-troubleshooting-guide-common-questions",
    "appdev-troubleshooting-guide-development-issues",
    "appdev-troubleshooting-guide-error-code-reference",
    "appdev-troubleshooting-guide-installation-issues",
]

REPLACEMENTS = [
    ("广州控制台", "Canton Console"),
    ("广州网络", "Canton Network"),
    ("粤网", "Canton Network"),
    ("</卡组>", "</CardGroup>"),
    ("### 取决于国家（类别 9-12）", "### 状态相关（类别 9-12）"),
    ("### 选择范围", "### Choice 覆盖率"),
    ("管理派对", "管理 Party"),
    ("Daml Studio（VS 代码扩展）", "Daml Studio（VS Code 扩展）"),
    ("## 本地网络", "## LocalNet"),
    ("## 沙盒", "## Sandbox"),
    ("沙箱为您提供", "Sandbox 为您提供"),
    ("适合运行 Daml 脚本测试", "适合运行 Daml Script 测试"),
    ("## 发展\n", "## 开发\n"),
    ("获得新的代币", "获取新令牌"),
    ("| 11合同不存在", "| 合同不存在"),
    ("| 11交易不存在", "| 交易不存在"),
    ("| 11未找到", "| 未找到"),
    ("| 10具有此密钥", "| 具有此密钥"),
    (
        "<Warning>\n  Some errors are redacted for security. The API response omits sensitive details, but the full error message appears in server-side logs. Work with your operator if you need the complete error context.\n</Warning>",
        "<Warning>\n  部分错误会因安全原因被脱敏。API 响应会省略敏感细节，但完整错误信息会出现在服务端日志中。如需完整错误上下文，请联系运维人员。\n</Warning>",
    ),
]

TROUBLESHOOTING_CARDS = """<CardGroup cols={2}>
  <Card title="安装问题" icon="wrench" href="/appdev/troubleshooting-guide/installation-issues">
    Nix shell 失败、Docker 配置、内存分配与 JDK 设置。
  </Card>

  <Card title="开发问题" icon="bug" href="/appdev/troubleshooting-guide/development-issues">
    Daml 编译错误、API 连接问题、开发期交易失败。
  </Card>

  <Card title="运维问题" icon="server" href="/appdev/troubleshooting-guide/operational-issues">
    流量耗尽、升级问题、DevNet/TestNet/MainNet 上的 PQS 故障。
  </Card>

  <Card title="常见问题 FAQ" icon="circle-question" href="/appdev/faq">
    应用开发与 validator 运维常见问题，含简短答案与后续步骤。
  </Card>

  <Card title="常见问题" icon="circle-question" href="/appdev/troubleshooting-guide/common-questions">
    Canton Network 应用开发常见问题。
  </Card>

  <Card title="Daml 错误码" icon="circle-exclamation" href="/appdev/troubleshooting-guide/error-code-reference">
    Daml 编译错误与 Canton 运行时错误码，含原因与解决方案。
  </Card>

  <Card title="Ledger API 错误" icon="circle-exclamation" href="/appdev/troubleshooting-guide/ledger-api-errors">
    命令提交时常见的 Ledger API 错误码。
  </Card>
</CardGroup>"""


def dedupe_intro(body: str) -> str:
    # Remove duplicate blockquote immediately after first intro line
    body = re.sub(
        r"(> [^\n]+\n\n)> [^\n]+\n\n",
        r"\1",
        body,
        count=1,
    )
    return body


def fix_file(slug: str) -> None:
    path = OUT / f"{slug}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    body = data["body"]
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    body = dedupe_intro(body)
    if slug == "appdev-troubleshooting":
        body = re.sub(r"<CardGroup cols=\{2\}>[\s\S]*?</CardGroup>", TROUBLESHOOTING_CARDS, body)
        body = body.replace("</卡组>", "</CardGroup>")
    data["body"] = body
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"fixed {slug}")


def main() -> None:
    for slug in SLUGS:
        fix_file(slug)
    print(f"fixed {len(SLUGS)} files")


if __name__ == "__main__":
    main()
