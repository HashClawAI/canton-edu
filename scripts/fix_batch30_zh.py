#!/usr/bin/env python3
"""Post-process batch 30 zh-cursor JSON: fix MT errors, restore code fences from EN."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs/education/canton-dev/zh-cursor"
EN = ROOT / "docs/education/canton-dev/en"

SLUGS = [
    "global-synchronizer-troubleshooting-guide-common-questions",
    "global-synchronizer-troubleshooting-guide-configuration-problems",
    "global-synchronizer-troubleshooting-guide-connectivity-issues",
    "global-synchronizer-troubleshooting-guide-error-code-reference",
    "global-synchronizer-troubleshooting-guide-installation-issues",
    "global-synchronizer-troubleshooting-guide-performance-issues",
    "global-synchronizer-troubleshooting-guide-runbooks",
    "global-synchronizer-troubleshooting-guide-security-issues",
    "global-synchronizer-troubleshooting-guide-transaction-failures",
    "global-synchronizer-troubleshooting-guide-troubleshooting-methodology",
]

FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)

REPLACEMENTS: list[tuple[str, str]] = [
    ("验证器", "验证者"),
    ("验证人", "验证者"),
    ("<警告>", "<Warning>"),
    ("</警告>", "</Warning>"),
    ("<注意>", "<Note>"),
    ("</注>", "</Note>"),
    ("</笔记>", "</Note>"),
    ("<笔记>", "<Note>"),
    ("global-同步器", "global-synchronizer"),
    ("/global-同步器/", "/global-synchronizer/"),
    ("入驻-process", "onboarding-process"),
    ("入驻 process", "onboarding 流程"),
    ("#验证者-operations-入驻", "#validator-operations-onboarding"),
    ("广州控制台", "Canton Console"),
    ("广州", "Canton"),
    ("坎顿登录", "Canton 写入"),
    ("坎顿", "Canton"),
    ("定序器", "Sequencer"),
    ("排序器", "Sequencer"),
    ("测序仪", "Sequencer"),
    ("参与方1", "participant1"),
    ("参与方2", "participant2"),
    ("参与方3", "participant3"),
    ("参与方.parties", "participant.parties"),
    ("参与方.dars", "participant.dars"),
    ("参与方.topology", "participant.topology"),
    ("参与方.packages", "participant.packages"),
    ("参与方修剪Schedule", "participantPruningSchedule"),
    ("参与方_4", "participant_4"),
    ("参与方_5", "participant_5"),
    ("参与方同步器s", "ParticipantSynchronizers"),
    ("参与方s", "participants"),
    ("参与方 =", "participant ="),
    ("参与方Permission", "SynchronizerPermission"),
    ("同步器Permission", "SynchronizerPermission"),
    ("同步器Id", "synchronizerId"),
    ("同步器s", "synchronizers"),
    (".流量_control.", ".traffic_control."),
    (".流量_state", ".traffic_state"),
    ("流量State", "TrafficState"),
    ("extra流量Limit", "extraTrafficLimit"),
    ("extra流量Consumed", "extraTrafficConsumed"),
    ("base流量Remainder", "baseTrafficRemainder"),
    ("available流量", "availableTraffic"),
    ("digitalasset/canton-参与方", "digitalasset/canton-participant"),
    ("验证者-values.yaml", "validator-values.yaml"),
    ("验证者-app", "validator-app"),
    ("验证者-tls", "validator-tls"),
    ("your-验证者", "your-validator"),
    ("-n 验证者", "-n validator"),
    ("deployment/验证者", "deployment/validator"),
    ("name=验证者", "name=validator"),
    ("/api/验证者/", "/api/validator/"),
    ("CertPath验证者Exception", "CertPathValidatorException"),
    ("Parties not known on 同步器", "Parties not known on synchronizer"),
    ("`修剪 is not", "`Pruning is not"),
    ("Insufficient 流量 for", "Insufficient traffic for"),
    ("PARTICIPANT_流量", "PARTICIPANT_TRAFFIC"),
    ("参与者流量低于限制", "PARTICIPANT_TRAFFIC_BELOW_LIMIT"),
    ("参与者\\_拓扑\\_未知\\_各方", "PARTICIPANT_TOPOLOGY_UNKNOWN_PARTIES"),
    ("参与者\\_PRUNING", "PARTICIPANT_PRUNING"),
    ("序列器\\_", "SEQUENCER_"),
    ("Via the 验证者 API", "通过验证者 API"),
    ("### What ports need to be open?", "### 需要开放哪些端口？"),
    ("## Upgrades", "## 升级"),
    ("### Can I skip versions?", "### 能否跳过版本？"),
    ("During a reset:", "重置期间："),
    ("运维手册：验证器离线", "运维手册：验证者离线"),
    ("验证器离线", "验证者离线"),
    ("验证器消失", "验证者消失"),
    ("验证器的消息", "验证者的消息"),
    ("验证器的流量", "验证者的流量"),
    ("验证器的钱包", "验证者的钱包"),
    ("验证器安装", "验证者安装"),
    ("验证器操作员", "验证者操作员"),
    ("验证器 API", "验证者 API"),
    ("验证器钱包", "验证者钱包"),
    ("验证器状态", "验证者状态"),
    ("验证器健康", "验证者健康"),
    ("验证器日志", "验证者日志"),
    ("验证器进程", "验证者进程"),
    ("验证器容器", "验证者容器"),
    ("验证器配置", "验证者配置"),
    ("验证器升级", "验证者升级"),
    ("验证器失败", "验证者失败"),
    ("验证器运行", "验证者运行"),
    ("验证器需要", "验证者需要"),
    ("验证器在", "验证者在"),
    ("验证器将", "验证者将"),
    ("验证器可能", "验证者可能"),
    ("验证器可以", "验证者可以"),
    ("验证器必须", "验证者必须"),
    ("验证器已经", "验证者已经"),
    ("验证器尚未", "验证者尚未"),
    ("验证器使用", "验证者使用"),
    ("验证器获得", "验证者获得"),
    ("验证器赚取", "验证者赚取"),
    ("验证器注册", "验证者注册"),
    ("验证器重新", "验证者重新"),
    ("验证器消失", "验证者消失"),
    ("验证器消失", "验证者消失"),
    ("全局同步器 验证器", "全局同步器验证者"),
    ("全局同步器 Foundation", "Global Synchronizer Foundation"),
    ("[全局同步器 Foundation]", "[Global Synchronizer Foundation]"),
    ("聚会 ID", "Party ID"),
    ("参与方 ID", "Party ID"),
    ("包审查", "包 vetting"),
    ("包审核", "包 vetting"),
    ("事务失败", "交易失败"),
    ("事务超时", "交易超时"),
    ("事务缓慢", "交易缓慢"),
    ("测试事务", "测试交易"),
    ("提交测试事务", "提交测试交易"),
    ("处理事务", "处理交易"),
    ("事务处理", "交易处理"),
    ("事务延迟", "交易延迟"),
    ("事务失败", "交易失败"),
    ("操作手册", "运维手册"),
    ("操作手册都", "运维手册都"),
    ("每个操作手册", "每个运维手册"),
    ("专用操作手册", "专用运维手册"),
    ("相关操作手册", "相关运维手册"),
    ("下面的相关操作手册", "下面的相关运维手册"),
    ("常见验证器事件的操作手册", "常见验证者事件的运维手册"),
    ("诊断和解决全局同步器问题", "Global Synchronizer 问题系统化排查方法"),
    ("解决验证器安装过程中的", "解决验证者安装过程中的"),
    ("解决事务缓慢", "解决交易缓慢"),
    ("诊断授权错误、包审核失败和事务超时", "授权错误、包 vetting 失败与交易超时排查"),
    ("> 有关验证器设置、操作和升级的常见问题\n\n", ""),
    ("> 常见 Canton 和 Splice 错误代码及其原因和解决步骤\n\n", ""),
    ("> 解决验证器安装过程中的 Docker、Kubernetes 和网络问题\n\n", ""),
    ("> 解决事务缓慢、资源耗尽和数据库瓶颈\n\n", ""),
    ("> 常见验证器事件的操作手册以及分步程序\n\n", ""),
    ("> 解决证书问题、JWT 验证失败和密钥管理错误\n\n", ""),
    ("> 诊断授权错误、包审核失败和事务超时\n\n", ""),
    ("> 诊断和解决全局同步器问题的系统方法\n\n", ""),
    ("> 诊断 HOCON 解析错误、权限问题和环境变量冲突\n\n", ""),
    ("> 诊断和解决同步器连接失败、TLS 错误和 VPN 问题\n\n", ""),
    (
        "> 验证者搭建、运维与升级相关的常见问题解答。\n\n> 有关验证者设置、操作和升级的常见问题\n\n",
        "> 验证者搭建、运维与升级相关的常见问题解答。\n\n",
    ),
    ("到synchronizerSequencer", "到 synchronizer sequencer"),
    ("全局synchronizer Foundation", "Global Synchronizer Foundation"),
    ("synchronizer迁移", "同步器迁移"),
    ("涉及synchronizer迁移", "涉及同步器迁移"),
    ("无需synchronizer迁移", "无需同步器迁移"),
    ("网络移动到新的synchronizer ID", "网络移动到新的同步器 ID"),
    ("参与者查询存储", "Participant Query Store（PQS）"),
]

DUPLICATE_INTRO = [
    (
        "> 验证者搭建、运维与升级相关的常见问题解答。\n\n> 有关验证者设置、操作和升级的常见问题\n\n",
        "> 验证者搭建、运维与升级相关的常见问题解答。\n\n",
    ),
]


def restore_fences(slug: str, body: str) -> str:
    en_path = EN / f"{slug}.md"
    if not en_path.exists():
        return body
    en_fences = FENCE_RE.findall(en_path.read_text(encoding="utf-8"))
    if not en_fences:
        return body
    it = iter(en_fences)

    def repl(_m: re.Match[str]) -> str:
        try:
            return next(it)
        except StopIteration:
            return _m.group(0)

    return FENCE_RE.sub(repl, body)


def fix_body(body: str, slug: str) -> str:
    for old, new in DUPLICATE_INTRO:
        body = body.replace(old, new)
    for old, new in REPLACEMENTS:
        body = body.replace(old, new)
    body = restore_fences(slug, body)
    return body


def main() -> None:
    n = 0
    for slug in SLUGS:
        path = OUT / f"{slug}.json"
        if not path.exists():
            print(f"missing: {slug}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        data["body"] = fix_body(data["body"], slug)
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n += 1
        print(f"fixed: {slug}")
    print(f"fix batch 30 count: {n}")


if __name__ == "__main__":
    main()
