#!/usr/bin/env python3
"""Generate batch 11 zh-cursor JSON (Daml stdlib reference da-either … da-list-total)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_DIR = ROOT / "docs/education/canton-dev/en"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"
BODY_DIR = Path(__file__).parent / "_batch11_bodies"

DOC_INDEX_ZH = """> ## 文档索引
> 获取完整文档索引：https://docs.canton.network/llms.txt
> 在进一步浏览前，可用该文件发现所有可用页面。

"""

FOOTER_RE = re.compile(r"\n---\n\n> Mirrored from.*", re.DOTALL)
FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def strip_en(md: str) -> str:
    md = FRONTMATTER_RE.sub("", md)
    md = FOOTER_RE.sub("", md)
    md = re.sub(
        r"> ## Documentation Index\n> Fetch the complete documentation index at: https://docs\.canton\.network/llms\.txt\n> Use this file to discover all available pages before exploring further\.\n\n",
        "",
        md,
    )
    lines = md.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    if lines and lines[0].strip() == "":
        lines = lines[1:]
    return "\n".join(lines).strip()


def load_zh_body(slug: str) -> str:
    path = BODY_DIR / f"{slug}.zh.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8").strip()


META: dict[str, dict[str, str]] = {
    "appdev-reference-daml-standard-library-da-either": {
        "zhTitle": "DA.Either",
        "summary": "Either 双分支类型：lefts/rights、partitionEithers、isLeft/isRight、fromLeft/fromRight 及与 Optional 互转。",
    },
    "appdev-reference-daml-standard-library-da-exception": {
        "zhTitle": "DA.Exception",
        "summary": "已弃用的 Daml 异常模块；推荐 failWithStatus/FailureStatus，避免 catch。",
    },
    "appdev-reference-daml-standard-library-da-fail": {
        "zhTitle": "DA.Fail",
        "summary": "FailureStatus 与 FailureCategory：failWithStatus、invalidArgument、failedPrecondition 及 Canton 错误分类映射。",
    },
    "appdev-reference-daml-standard-library-da-foldable": {
        "zhTitle": "DA.Foldable",
        "summary": "可折叠结构类型类 fold/foldMap/toList 及 mapA_/forA_/sequence_/concat/and/or/any/all。",
    },
    "appdev-reference-daml-standard-library-da-functor": {
        "zhTitle": "DA.Functor",
        "summary": "Functor 辅助：$>、<&>、<$$>、void 等映射与替换算子。",
    },
    "appdev-reference-daml-standard-library-da-internal-interface-anyview": {
        "zhTitle": "DA.Internal.Interface.AnyView",
        "summary": "接口 AnyView：HasFromAnyView 与 fromAnyView 将 AnyView 转回具体视图类型。",
    },
    "appdev-reference-daml-standard-library-da-internal-interface-anyview-types": {
        "zhTitle": "DA.Internal.Interface.AnyView.Types",
        "summary": "AnyView 与 InterfaceTypeRep 数据类型及字段访问实例。",
    },
    "appdev-reference-daml-standard-library-da-list": {
        "zhTitle": "DA.List",
        "summary": "列表排序/分组/去重/前后缀/索引与 mapAccumL、chunksOf、delete、!! 等扩展函数。",
    },
    "appdev-reference-daml-standard-library-da-list-builtinorder": {
        "zhTitle": "DA.List.BuiltinOrder",
        "summary": "基于 Daml-LF 内建序的 dedup/sort/unique（Daml-LF 1.11+），通常比 Ord 版更高效。",
    },
    "appdev-reference-daml-standard-library-da-list-total": {
        "zhTitle": "DA.List.Total",
        "summary": "列表 head/tail/last/init/!!/foldl1 等的 Optional 安全变体，空列表返回 None。",
    },
}

BATCH11_SLUGS = list(META.keys())


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in BATCH11_SLUGS:
        m = META[slug]
        body = DOC_INDEX_ZH + load_zh_body(slug)
        payload = {"zhTitle": m["zhTitle"], "summary": m["summary"], "body": body}
        out = OUT_DIR / f"{slug}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out.name}")
        count += 1
    print(f"batch11 count: {count}")


if __name__ == "__main__":
    main()
