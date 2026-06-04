#!/usr/bin/env python3
"""Post-process batch 27 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-production-operations-scalability",
    "global-synchronizer-production-operations-splice-metrics-overview",
    "global-synchronizer-production-operations-sv-backup",
    "global-synchronizer-production-operations-sv-pruning",
    "global-synchronizer-production-operations-sv-security",
    "global-synchronizer-production-operations-sv-upgrades",
    "global-synchronizer-production-operations-upgrade-canton-nodes",
    "global-synchronizer-production-operations-validator-backups",
    "global-synchronizer-production-operations-validator-disaster-recovery",
    "global-synchronizer-production-operations-validator-security",
]

REPLACEMENTS = [
    ("/global-同步器/", "/global-synchronizer/"),
    ("global-同步器", "global-synchronizer"),
    ("生产-操作", "production-operations"),
    ("product-operations", "production-operations"),
    ("生产操作", "production-operations"),
    ("逻辑-同步器-upgrade", "logical-synchronizer-upgrade"),
    ("密钥管理", "key-management"),
    ("</卡>", "</Card>"),
    ("<卡 ", "<Card "),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<笔记>", "<Note>"),
    ("</笔记>", "</Note>"),
    ("<标签>", "<Tabs>"),
    ("</标签>", "</Tabs>"),
    ("<Tab ", "<Tab "),
    ("验证器Right", "ValidatorRight"),
    ("验证者Right", "ValidatorRight"),
    ("钱包AppInstall", "WalletAppInstall"),
    ("验证者RewardCoupon", "ValidatorRewardCoupon"),
    ("#splice-钱包:", "#splice-wallet:"),
    ("Splice.钱包.", "Splice.Wallet."),
    (".拓扑.", ".topology."),
    ("participant.拓扑.", "participant.topology."),
    ("external-party/拓扑/", "external-party/topology/"),
    ("排序器修剪", "Sequencer 修剪"),
    ("由于排序器修剪", "由于 Sequencer 修剪"),
    ("超级验证节点", "超级验证者节点"),
    ("验证节点", "验证者节点"),
    ("验证器应用程序", "验证者应用"),
    ("验证器 API", "验证者 API"),
    ("验证器就绪", "验证者就绪"),
    ("验证器限制", "验证者限制"),
    ("验证器运营商", "验证者运营方"),
    ("验证器端点", "验证者端点"),
    ("验证器应用", "验证者应用"),
    ("验证器 party", "验证者 party"),
    ("验证器钱包", "验证者钱包"),
    ("验证器初始化", "验证者初始化"),
    ("验证器日志", "验证者日志"),
    ("验证器数据库", "验证者数据库"),
    ("验证器 participant", "验证者 participant"),
    ("验证器 hint", "验证者 hint"),
    ("验证器运营方", "验证者运营方"),
    ("验证人运营方", "验证者运营方"),
    ("验证人", "验证者"),
    ("铸币委托", "铸币委派"),
    ("硬币余额", "Canton Coin 余额"),
    ("coin balance", "Canton Coin 余额"),
    ("100 万方", "100 万个 Party"),
    ("200 个方", "200 个 Party"),
    ("200 方的限制", "200 个 Party 的限制"),
    ("设置外部方", "设置外部 Party"),
    ("`验证者`方", "`validator` party"),
    ("key-management系统", "密钥管理系统"),
    ("验证器API", "验证者 API"),
    ("配置验证器", "配置验证者"),
    ("新的验证器", "新的验证者"),
    ("非 KMS 验证器", "非 KMS 验证者"),
    ("验证器部署", "验证者部署"),
    ("支持 KMS 的验证器", "支持 KMS 的验证者"),
    ("停用非 KMS 验证器", "停用非 KMS 验证者"),
    ("验证器。", "验证者。"),
    ("验证器 ", "验证者 "),
    ("`验证者` 方", "`validator` party"),
    ("identites", "identities"),
    ("&lt;pod-name&gt;", "<pod-name>"),
    ("&lt;container-name&gt;", "<container-name>"),
    ("&lt;token&gt;", "<token>"),
    ("&lt;namespace&gt;", "<namespace>"),
    ("api/验证者/", "api/validator/"),
    ("splice_store", "splice_store"),
    ("广东", "Canton"),
    ("定序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("中介者", "Mediator"),
    ("KmsParticipantsContext", "KmsParticipantsContext"),
    ("publicKey", "publicKey"),
    ('"public":', '"publicKey":'),
    ("cometbft-governance-keys.json", "cometbft-governance-keys.json"),
    ("--boostrap", "--bootstrap"),
    ("oldsynchronizer", "oldsynchronizer"),
    ("newsynchronizer", "newsynchronizer"),
    ("testsynchronizer", "testsynchronizer"),
    ("validator-metrics-reference", "validator-metrics-reference"),
    ("validator_recover_external_party", "validator_recover_external_party"),
    ("helm-validator-install", "helm-validator-install"),
]


def fix_body(body: str) -> str:
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
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        n += 1
        print(f"fixed: {slug}")
    print(f"batch 27 fix count: {n}")


if __name__ == "__main__":
    main()
