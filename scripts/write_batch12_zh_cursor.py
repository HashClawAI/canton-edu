#!/usr/bin/env python3
"""Write batch 12 zh-cursor JSON payloads (DA.Logic … DA.Semigroup)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BODY_DIR = Path(__file__).parent / "_batch12_bodies"
OUT_DIR = ROOT / "docs/education/canton-dev/zh-cursor"

META = {
    "appdev-reference-daml-standard-library-da-logic": {
        "zhTitle": "DA.Logic",
        "summary": "命题演算：Formula 类型、合取/析取/否定与 NNF、DNF 化简及求值。",
    },
    "appdev-reference-daml-standard-library-da-map": {
        "zhTitle": "DA.Map",
        "summary": "泛型 Map（Daml-LF 1.11+）：查找、插入、合并、过滤与 Ord 键约束。",
    },
    "appdev-reference-daml-standard-library-da-math": {
        "zhTitle": "DA.Math",
        "summary": "Decimal 数学函数：幂、根、exp/log 与三角函数；高精度但非高性能。",
    },
    "appdev-reference-daml-standard-library-da-monoid": {
        "zhTitle": "DA.Monoid",
        "summary": "Monoid 新类型：All/Any、Endo、Product、Sum 及相应实例。",
    },
    "appdev-reference-daml-standard-library-da-nonempty": {
        "zhTitle": "DA.NonEmpty",
        "summary": "非空列表类型与函数：cons、append、fold、qualified import 约定。",
    },
    "appdev-reference-daml-standard-library-da-nonempty-types": {
        "zhTitle": "DA.NonEmpty.Types",
        "summary": "NonEmpty 类型定义（稳定 package id）；通常由 DA.NonEmpty 再导出。",
    },
    "appdev-reference-daml-standard-library-da-numeric": {
        "zhTitle": "DA.Numeric",
        "summary": "Numeric 运算与 RoundingMode：mul/div、cast、shift、roundNumeric。",
    },
    "appdev-reference-daml-standard-library-da-optional": {
        "zhTitle": "DA.Optional",
        "summary": "Optional 工具：fromSome、catOptionals、whenSome、findOptional 等。",
    },
    "appdev-reference-daml-standard-library-da-record": {
        "zhTitle": "DA.Record",
        "summary": "GetField/SetField/HasField：记录多态 getter/setter 与记录语法说明。",
    },
    "appdev-reference-daml-standard-library-da-semigroup": {
        "zhTitle": "DA.Semigroup",
        "summary": "Semigroup 新类型 Min/Max：在 min/max 下的 <> 运算。",
    },
}

SLUGS = list(META.keys())


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in SLUGS:
        body_path = BODY_DIR / f"{slug}.zh.txt"
        body = body_path.read_text(encoding="utf-8").strip()
        m = META[slug]
        payload = {"zhTitle": m["zhTitle"], "summary": m["summary"], "body": body}
        out = OUT_DIR / f"{slug}.json"
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {out.name}")
        count += 1
    print(f"batch12 count: {count}")


if __name__ == "__main__":
    main()
