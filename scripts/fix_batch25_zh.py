#!/usr/bin/env python3
"""Post-process batch 25 zh-cursor JSON: fix MT errors, preserve MDX/code."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

SLUGS = [
    "global-synchronizer-extension-synchronizers-other-private-synchronizers",
    "global-synchronizer-extension-synchronizers-private-synchronizers",
    "global-synchronizer-extension-synchronizers-private-validators",
    "global-synchronizer-extension-synchronizers-synchronizer-monitoring",
    "global-synchronizer-extension-synchronizers-synchronizer-operations",
    "global-synchronizer-faq",
    "global-synchronizer-production-operations-canton-console",
    "global-synchronizer-production-operations-decommission-nodes",
    "global-synchronizer-production-operations-disaster-recovery",
    "global-synchronizer-production-operations-key-management",
]

REPLACEMENTS = [
    ("验证器", "验证者"),
    ("定序器", "Sequencer"),
    ("排序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("调解人", "Mediator"),
    ("中介人", "Mediator"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<笔记>", "<Note>"),
    ("</笔记>", "</Note>"),
    ("<注意>", "<Note>"),
    ("</注意>", "</Note>"),
    ("bootstrap.同步器", "bootstrap.synchronizer"),
    ("participant.同步器s", "participant.synchronizers"),
    ("participant1.同步器s", "participant1.synchronizers"),
    ("participantReference.同步器s", "participantReference.synchronizers"),
    ("同步器Name", "synchronizerName"),
    ("同步器Owners", "synchronizerOwners"),
    ("同步器Threshold", "synchronizerThreshold"),
    ("同步器Alias", "synchronizerAlias"),
    ("同步器ConnectionConfig", "SynchronizerConnectionConfig"),
    ("static同步器Parameters", "staticSynchronizerParameters"),
    ("Static同步器Parameters", "StaticSynchronizerParameters"),
    ("Physical同步器Id", "PhysicalSynchronizerId"),
    ("ProtocolVersion.for同步器", "ProtocolVersion.forSynchronizer"),
    ("ListConnected同步器sResult", "ListConnectedSynchronizersResult"),
    ("Connect同步器Request", "ConnectSynchronizerRequest"),
    ("Connect同步器", "ConnectSynchronizer"),
    ("同步器ConnectionConfig", "SynchronizerConnectionConfig"),
    ("同步器ConnectivityService", "SynchronizerConnectivityService"),
    ("同步器Operator", "Synchronizer Operator"),
    ("my同步器", "mySynchronizer"),
    ("private-sync", "private-sync"),
    ("my-private-sync", "my-private-sync"),
    ("ledger\\_api", "ledger_api"),
    ("\\#22917", "#22917"),
    ("&lt;", "<"),
    ("&gt;", ">"),
    ("广东", "Canton"),
    ("硬币", "代币"),
    ("登录密码", "入驻密钥"),
    ("入驻Type", "onboardingType"),
    ("发现-dso", "found-dso"),
    ("decentralized同步器Url", "decentralizedSynchronizerUrl"),
    ("广州控制台", "Canton Console"),
    ("参与者节点", "参与方节点"),
    ("参与方节点节点", "参与方节点"),
    ("同步器 fees", "同步器费用"),
    ("`同步器 fees`", "`synchronizer fees`"),
    ("重分配.unassign", "reassignment.unassign"),
    ("重分配.assign", "reassignment.assign"),
    ("commands.重分配", "commands.reassignment"),
    ("sequencer.health.status", "sequencer.health.status"),
    ("mediator.health.status", "mediator.health.status"),
    ("mediator1.inspection.verdicts", "mediator1.inspection.verdicts"),
    ("myNode.keys.secret.rotate_node_keys", "myNode.keys.secret.rotate_node_keys"),
    ("nodes.local.start", "nodes.local.start"),
    ("participants.local.dars.upload", "participants.local.dars.upload"),
    ("health.ping", "health.ping"),
    ("SEQUENCER_TOMBSTONE_ENCOUNTERED", "SEQUENCER_TOMBSTONE_ENCOUNTERED"),
    ("FAILED_PRECONDITION", "FAILED_PRECONDITION"),
    ("InvalidCounter", "InvalidCounter"),
    ("VERDICT_RESULT_ACCEPTED", "VERDICT_RESULT_ACCEPTED"),
    ("OffboardMember", "OffboardMember"),
    ("helm-validator-install", "helm-validator-install"),
    ("helm-sv-install", "helm-sv-install"),
    ("sv_backups", "sv_backups"),
    ("validatorPartyHint", "validatorPartyHint"),
    ("jq '.identities.participant'", "jq '.identities.participant'"),
    ("广州概览", "Canton 概览"),
    ("广州网络", "Canton Network"),
    ("广州同步器", "Canton 同步器"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("global-同步器-foundation", "global-synchronizer-foundation"),
    ("extension-同步器s", "extension-synchronizers"),
    ("linking-验证者-multi-sync", "linking-validator-multi-sync"),
    ("Private 同步器", "Private Synchronizer"),
    ("className=\"词汇表\"", "className=\"glossary\""),
    ("className=\"内容\"", "className=\"contents\""),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("</注意>", "</Note>"),
    ("中介器节点", "Mediator 节点"),
    ("中介节点", "Mediator 节点"),
    ("定序器", "Sequencer"),
    ("#monitoring-choices", "#monitoring-choices"),
]


def fix_slug(slug: str) -> None:
    path = OUT / f"{slug}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    body = data["body"]
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    data["body"] = body
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"fixed {slug}")


def main() -> None:
    for slug in SLUGS:
        fix_slug(slug)
    print(f"batch 25 fix: {len(SLUGS)} files")


if __name__ == "__main__":
    main()
