#!/usr/bin/env python3
"""Post-process batch 24 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-deployment-sv-scratchnet",
    "global-synchronizer-deployment-synchronizer-traffic",
    "global-synchronizer-deployment-validator-docker-compose",
    "global-synchronizer-deployment-validator-kubernetes",
    "global-synchronizer-deployment-validator-network-resets",
    "global-synchronizer-deployment-validator-networking",
    "global-synchronizer-deployment-validator-users",
    "global-synchronizer-extension-synchronizers-bft-orderer",
    "global-synchronizer-extension-synchronizers-hybrid-synchronizer-pattern",
    "global-synchronizer-extension-synchronizers-linking-validator-multi-sync",
]

REPLACEMENTS = [
    ("验证器", "验证者"),
    ("舵值", "Helm 值"),
    ("joinWithKey入驻", "joinWithKeyOnboarding"),
    ("入驻Type", "onboardingType"),
    ("入驻FoundingSvRewardWeightBps", "onboardingFoundingSvRewardWeightBps"),
    ("发现-dso", "found-dso"),
    ("初始同步器FeesConfig", "initialSynchronizerFeesConfig"),
    ("基本速率突发金额", "baseRateBurstAmount"),
    ("基本速率突发窗口分钟", "baseRateBurstWindowMins"),
    ("额外流量价格", "extraTrafficPrice"),
    ("最小充值金额", "minTopupAmount"),
    ("读取与写入缩放因子", "readVsWriteScalingFactor"),
    ("decentralized同步器Url", "decentralizedSynchronizerUrl"),
    ("钱包Sweep", "walletSweep"),
    ("广东网络", "Canton Network"),
    ("广东币", "Canton Coin"),
    ("广州控制台", "Canton Console"),
    ("<标签>", "<Tabs>"),
    ("</标签>", "</Tabs>"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<笔记>", "<Note>"),
    ("</笔记>", "</Note>"),
    ("同步器 fees", "同步器费用"),
    ("`同步器 fees`", "`synchronizer fees`"),
    ("定序器", "Sequencer"),
    ("排序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("登录密码", "入驻密钥"),
    ("验证程序", "验证者"),
    ("硬币", "代币"),
    ("自己加入", "入驻本人"),
    ("验证者钱包User", "validatorWalletUser"),
    ("bootstrap.同步器", "bootstrap.synchronizer"),
    ("participant.同步器s", "participant.synchronizers"),
    ("同步器Name", "synchronizerName"),
    ("同步器Owners", "synchronizerOwners"),
    ("同步器Threshold", "synchronizerThreshold"),
    ("static同步器Parameters", "staticSynchronizerParameters"),
    ("Static同步器Parameters", "StaticSynchronizerParameters"),
    ("Physical同步器Id", "PhysicalSynchronizerId"),
    ("ProtocolVersion.for同步器", "ProtocolVersion.forSynchronizer"),
    ("#验证者-operations", "#validator-operations"),
    ("rpc服务器", "rpcServers"),
    ("赞助商ApiUrl", "sponsorApiUrl"),
    ("状态同步：", "stateSync:"),
    ("* 启用：真", "* enable: true"),
    ("- 启用：假", "- enable: false"),
    ("* 启用：假", "* enable: false"),
    ("SV1：", "sv1:"),
    ("* 密钥地址", "* keyAddress"),
    ("* 节点ID", "* nodeId"),
    ("* 公钥", "* publicKey"),
    ("## 扫描 helm 值", "## scan Helm 值"),
    ("## sv 舵值", "## sv Helm 值"),
    ("## cometbft 舵值", "## cometbft Helm 值"),
    ("1.禁用状态同步", "1. 禁用 state sync"),
    ("2. 对于单个 sv 配置", "2. 对于单个 SV 配置"),
    ("3. 从`sv-values.yaml`中删除`decentralizedSynchronizerUrl`配置。它仅用于在初始 SV 之后加入的节点。",
     "3. 从 `sv-values.yaml` 中删除 `decentralizedSynchronizerUrl` 配置。它仅用于在初始 SV 之后加入的节点。"),
    ("## 入口\n\n验证者没有外部入口要求", "## Ingress\n\n验证者没有外部入站要求"),
    ("## 出口\n\n验证者必须能够连接到所有 SV", "## Egress\n\n验证者必须能够连接到所有 SV"),
    ("> 验证者节点的网络入站与出站要求。\n\n> 验证者节点的网络入口和出口要求\n\n",
     "> 验证者节点的网络入站与出站要求。\n\n"),
    ("中介者", "Mediator"),
    ("可用基本费率流量余额", "可用基础速率（base rate）流量余额"),
    ("基本速率流量余额", "基础速率（base rate）流量余额"),
    ("`base rate`", "`base rate`"),
    ("`sequenced`", "`sequenced`"),
    ("`流量`", "`Traffic`"),
    ("`ACS`", "`ACS`"),
    ("Wasted traffic", "浪费的流量"),
    ("浪费的流量", "浪费的流量"),
    ("Rejected Event Traffic", "Rejected Event Traffic"),
    ("Synchronizer Fees (validator view)", "Synchronizer Fees（验证者视图）"),
    ("Synchronizer Fees (SV view)", "Synchronizer Fees（SV 视图）"),
    ("ISS", "ISS"),
    ("Narwhal", "Narwhal"),
    ("PBFT", "PBFT"),
    ("PoA", "PoA"),
    ("BlockOrderer", "BlockOrderer"),
    ("BFT Orderer", "BFT Orderer"),
    ("mempool", "mempool"),
    ("pre-prepare", "pre-prepare"),
    ("prepare", "prepare"),
    ("commit", "commit"),
    ("Private 同步器", "私有同步器"),
    ("全局同步器 上的", "全局同步器上的"),
    ("全球同步器", "全局同步器"),
    ("专用同步器", "私有同步器"),
    ("`alias`", "`alias`"),
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
        print(f"fixed {slug}")
    print(f"count: {n}")


if __name__ == "__main__":
    main()
