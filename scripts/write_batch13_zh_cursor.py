#!/usr/bin/env python3
"""Write batch 13 zh-cursor JSON (Daml stdlib ref: Set–Prelude)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "docs/education/canton-dev/en"
OUT = ROOT / "docs/education/canton-dev/zh-cursor"

BATCH13 = [
    "appdev-reference-daml-standard-library-da-set",
    "appdev-reference-daml-standard-library-da-stack",
    "appdev-reference-daml-standard-library-da-text",
    "appdev-reference-daml-standard-library-da-textmap",
    "appdev-reference-daml-standard-library-da-time",
    "appdev-reference-daml-standard-library-da-traversable",
    "appdev-reference-daml-standard-library-da-tuple",
    "appdev-reference-daml-standard-library-da-validation",
    "appdev-reference-daml-standard-library-index",
    "appdev-reference-daml-standard-library-prelude",
]

META: dict[str, tuple[str, str, str]] = {
    "appdev-reference-daml-standard-library-da-set": (
        "DA.Set",
        "Daml 集合类型 Set k：empty、insert、union 等；需 Ord k，仅 Daml-LF 1.11+。",
        "> Daml 模块 DA.Set 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-stack": (
        "DA.Stack",
        "调用栈 SrcLoc 与 prettyCallStack、getCallStack、callStack。",
        "> Daml 模块 DA.Stack 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-text": (
        "DA.Text",
        "Text 拆分、拼接、前缀/后缀、解析 Int/Decimal/Numeric 与 sha256 等工具函数。",
        "> Daml 模块 DA.Text 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-textmap": (
        "DA.TextMap",
        "Text 键关联数组 TextMap：fromList、lookup、insert、merge 等。",
        "> Daml 模块 DA.TextMap 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-time": (
        "DA.Time",
        "Time/RelTime 运算、相对时间构造与 isLedgerTime* 账本时间比较。",
        "> Daml 模块 DA.Time 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-traversable": (
        "DA.Traversable",
        "Traversable 类型类：mapA、sequence、forA；可从左到右遍历的数据结构。",
        "> Daml 模块 DA.Traversable 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-tuple": (
        "DA.Tuple",
        "元组工具：first/second/both/swap、三元组 fst3/snd3/thd3 与 curry3。",
        "> Daml 模块 DA.Tuple 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-da-validation": (
        "DA.Validation",
        "Validation 类型：可累积多条错误的校验结果，含 ok/invalid/run 等。",
        "> Daml 模块 DA.Validation 参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-index": (
        "详情与历史",
        "Daml 标准库模块总览：版本 3.4.11、各模块生命周期与版本变更摘要。",
        "> Daml 标准库各模块参考文档\n\n",
    ),
    "appdev-reference-daml-standard-library-prelude": (
        "Prelude",
        "Daml Prelude：内建类型、类型类、模板/接口函数与常用列表/Optional 工具。",
        "> Daml 模块 Prelude 参考文档\n\n",
    ),
}

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.S)
FOOTER = re.compile(r"\n---\n\n> Mirrored from.*", re.S)
DOC_INDEX = re.compile(r"> ## Documentation Index\n(?:> .*\n)*\n?", re.M)
DUP_H1 = re.compile(r"^# [^\n]+\n\n(?=# )", re.M)
REF_LINE = re.compile(r"^> Reference documentation for Daml module [^\n]+\.\n\n", re.M)

HEADING_ZH = {
    "# DA.Set": "# DA.Set",
    "# DA.Stack": "# DA.Stack",
    "# DA.Text": "# DA.Text",
    "# DA.TextMap": "# DA.TextMap",
    "# DA.Time": "# DA.Time",
    "# DA.Traversable": "# DA.Traversable",
    "# DA.Tuple": "# DA.Tuple",
    "# DA.Validation": "# DA.Validation",
    "# Details and history": "# 详情与历史",
    "# Prelude": "# Prelude",
    "## Module Snapshot": "## 模块快照",
    "## Data Types": "## 数据类型",
    "## Functions": "## 函数",
    "## Typeclasses": "## 类型类",
    "## Orphan Typeclass Instances": "## 孤立类型类实例",
    "## Modules": "## 模块",
    "## Version Summary": "## 版本摘要",
    "Constructors:": "构造子：",
    "Instances:": "实例：",
    "Methods:": "方法：",
    "  <Card title=\"Lifecycle\">": "  <Card title=\"生命周期\">",
    "  <Card title=\"Notices\">": "  <Card title=\"通知\">",
    "    Stable.": "    稳定。",
    "    Status: `active`": "    状态：`active`",
    "    Introduced in: `3.4.9`": "    引入版本：`3.4.9`",
    "    Removed in: `-`": "    移除版本：`-`",
    "    Warnings: `0`": "    警告数：`0`",
    "    Deprecations: `0`": "    弃用数：`0`",
    "    Deprecated since: `-`": "    弃用自：`-`",
    "  \\| Field \\| Type \\| Description \\|": "  \\| 字段 \\| 类型 \\| 说明 \\|",
    "  \\| :---- \\| :--- \\| :---------- \\|": "  \\| :---- \\| :--- \\| :---------- \\|",
    "  (no fields)": "  （无字段）",
    "<p class=\"x2mdx-ref-eyebrow\">Daml Reference</p>": "<p class=\"x2mdx-ref-eyebrow\">Daml 参考</p>",
    "<h1 class=\"x2mdx-ref-title\">Daml Standard Library</h1>": "<h1 class=\"x2mdx-ref-title\">Daml 标准库</h1>",
    "<p class=\"x2mdx-ref-summary\">Generated module overview for the Daml Standard Library, built from versioned docs JSON snapshots.</p>":
        "<p class=\"x2mdx-ref-summary\">由版本化文档 JSON 快照生成的 Daml 标准库模块总览。</p>",
    "<dt>Publish version</dt>": "<dt>发布版本</dt>",
    "<dt>Source</dt>": "<dt>来源</dt>",
    "<dd>Published Daml Standard Library docs JSON from local SDK artifacts</dd>":
        "<dd>本地 SDK 制品中的 Daml 标准库文档 JSON</dd>",
    "<dt>Version filter</dt>": "<dt>版本过滤</dt>",
    "<dd>configured Daml SDK artifact versions</dd>": "<dd>已配置的 Daml SDK 制品版本</dd>",
    "Open a module page for declarations, type signatures, warnings, and lifecycle details.":
        "打开模块页面查看声明、类型签名、警告与生命周期详情。",
    "<dt>Kind</dt>": "<dt>种类</dt>",
    "<dd>Module</dd>": "<dd>模块</dd>",
    "<dt>Introduced</dt>": "<dt>引入</dt>",
    "<dt>Changed</dt>": "<dt>变更</dt>",
    "<dt>Deprecated</dt>": "<dt>弃用</dt>",
    "<dt>Removed</dt>": "<dt>移除</dt>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">Since 3.4.9</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">自 3.4.9 起</span>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--removed\">Deprecated 3.4.9</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--removed\">3.4.9 弃用</span>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">Added 38</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">新增 38</span>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--changed\">Changed 0</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--changed\">变更 0</span>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--removed\">Removed 0</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--removed\">移除 0</span>",
    "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">Added 0</span>":
        "<span class=\"x2mdx-ref-badge x2mdx-ref-badge--added\">新增 0</span>",
    "<p class=\"x2mdx-ref-card-summary\">Module changes included in this Daml docs JSON snapshot.</p>":
        "<p class=\"x2mdx-ref-card-summary\">此 Daml 文档 JSON 快照中包含的模块变更。</p>",
}

PHRASE_ZH: dict[str, str] = {
    "Note: This is only supported in Daml-LF 1.11 or later.":
        "注意：仅支持 Daml-LF 1.11 或更高版本。",
    "This module exports the generic set type `Set k` and associated":
        "本模块导出泛型集合类型 `Set k` 及相关",
    "functions. This module should be imported qualified, for example:":
        "函数。应使用限定导入，例如：",
    "This will give access to the `Set` type, and the various operations":
        "这样可访问 `Set` 类型，并以",
    "as `S.lookup`, `S.insert`, `S.fromList`, etc.":
        "`S.lookup`、`S.insert`、`S.fromList` 等形式使用各操作。",
    "`Set k` internally uses the built-in order for the type `k`.":
        "`Set k` 内部使用类型 `k` 的内建序。",
    "This means that keys that contain functions are not comparable":
        "这意味着含函数的键不可比较，",
    "and will result in runtime errors. To prevent this, the `Ord k`":
        "会导致运行时错误。为避免此问题，多数集合操作要求 `Ord k`",
    "instance is required for most set operations. It is recommended to":
        "实例。建议仅对具有自动",
    "only use `Set k` for key types that have an `Ord k` instance":
        "`deriving` 的 `Ord k` 实例的键类型使用 `Set k`：",
    "that is derived automatically using `deriving`:":
        "",
    "This includes all built-in types that aren't function types, such as":
        "包括所有非函数类型的内建类型，例如",
    "`Int`, `Text`, `Bool`, `(a, b)` assuming `a` and `b` have default":
        "`Int`、`Text`、`Bool`、在 `a` 与 `b` 有默认",
    "`Ord` instances, `Optional t` and `[t]` assuming `t` has a":
        "`Ord` 实例时的 `(a, b)`、在 `t` 有默认 `Ord` 时的 `Optional t` 与 `[t]`、",
    "default `Ord` instance, `Map k v` assuming `k` and `v` have":
        "在 `k` 与 `v` 有默认 `Ord` 时的 `Map k v`，",
    "default `Ord` instances, and `Set k` assuming `k` has a":
        "以及 `k` 有默认 `Ord` 时的 `Set k`。",
    "default `Ord` instance.": "",
    "The type of a set. This is a wrapper over the `Map` type.":
        "集合类型，是对 `Map` 类型的封装。",
    "The empty set.": "空集。",
    "The number of elements in the set.": "集合中元素个数。",
    "Convert the set to a list of elements.": "将集合转为元素列表。",
    "Create a set from a list of elements.": "由元素列表创建集合。",
    "Convert a `Set` into a `Map`.": "将 `Set` 转为 `Map`。",
    "Create a `Set` from a `Map`.": "由 `Map` 创建 `Set`。",
    "Is the element in the set?": "元素是否在集合中？",
    "Is the element not in the set?": "元素是否不在集合中？",
    "`notMember k s` is equivalent to `not (member k s)`.": "`notMember k s` 等价于 `not (member k s)`。",
    "Is this the empty set?": "是否为空集？",
    "Insert an element in a set. If the set already contains the":
        "向集合插入元素；若已存在则返回原集合。",
    "element, this returns the set unchanged.": "",
    "Filter all elements that satisfy the predicate.": "保留满足谓词的所有元素。",
    "Delete an element from a set.": "从集合删除元素。",
    "Create a singleton set.": "创建单元素集合。",
    "The union of two sets.": "两集合的并集。",
    "The intersection of two sets.": "两集合的交集。",
    "`difference x y` returns the set consisting of all":
        "`difference x y` 返回 `x` 中不在 `y` 内的所有元素组成的集合。",
    "elements in `x` that are not in `y`.": "",
    "`isSubsetOf a b` returns true if `a` is a subset of `b`,":
        "`isSubsetOf a b` 在 `a` 是 `b` 的子集时返回 true，",
    "that is, if every element of `a` is in `b`.": "即 `a` 的每个元素都在 `b` 中。",
    "`isProperSubsetOf a b` returns true if `a` is a proper subset of `b`.":
        "`isProperSubsetOf a b` 在 `a` 是 `b` 的真子集时返回 true。",
    "That is, if `a` is a subset of `b` but not equal to `b`.":
        "即 `a` 是 `b` 的子集但不等于 `b`。",
    "Location in the source code.": "源代码中的位置。",
    "Line and column are 0-based.": "行号与列号从 0 开始。",
    "Pretty-print a `CallStack`.": "美化打印 `CallStack`。",
    "Extract the list of call sites from the `CallStack`.": "从 `CallStack` 提取调用点列表。",
    "The most recent call comes first.": "最近的调用排在最前。",
    "Access to the current `CallStack`.": "访问当前 `CallStack`。",
    "Functions for working with Text.": "操作 Text 的函数。",
    "Test for emptiness.": "测试是否为空。",
    "Test for non-emptiness.": "测试是否非空。",
    "Compute the number of symbols in the text.": "计算文本中的符号数。",
    "Remove spaces from either side of the given text.": "去除给定文本两端的空格。",
    "Replace a subsequence everywhere it occurs. The first argument":
        "在全文替换子串；第一个参数",
    "must not be empty.": "不能为空。",
    "Breaks a `Text` value up into a list of `Text`'s at newline":
        "在换行符处将 `Text` 拆成 `Text` 列表；",
    "symbols. The resulting texts do not contain newline symbols.": "结果不含换行符。",
    "Joins lines, after appending a terminating newline to each.": "连接各行，并在每行末尾追加换行符。",
    "Breaks a 'Text' up into a list of words, delimited by symbols":
        "按空白符号将 Text 拆成单词列表。",
    "representing white space.": "",
    "Joins words using single space symbols.": "用单个空格连接单词。",
    "A variant of `lines` with a custom test. In particular, if there":
        "`lines` 的变体，使用自定义分隔测试；",
    "is a trailing separator it will be discarded.": "末尾分隔符会被丢弃。",
    "A variant of `words` with a custom test. In particular, adjacent":
        "`words` 的变体，使用自定义分隔测试；",
    "separators are discarded, as are leading or trailing separators.": "相邻及首尾分隔符均会被丢弃。",
    "`intercalate` inserts the text argument `t` in between the items":
        "`intercalate` 在 `ts` 各项之间插入 `t` 并拼接。",
    "in `ts` and concatenates the result.": "",
    "`dropPrefix` drops the given prefix from the argument. It returns":
        "`dropPrefix` 去掉给定前缀；若无此前缀则返回原文。",
    "the original text if the text doesn't start with the given prefix.": "",
    "Drops the given suffix from the argument. It returns the original":
        "去掉给定后缀；若无此后缀则返回原文。",
    "text if the text doesn't end with the given suffix. Examples:":
        "示例：",
    "Return the prefix of the second text if its suffix matches the":
        "若第二段文本的后缀与第一段完全匹配，则返回其前缀。",
    "entire first text. Examples:": "示例：",
    "The `stripPrefix` function drops the given prefix from the":
        "`stripPrefix` 去掉给定前缀；",
    "argument text.  It returns `None` if the text did not start with":
        "若文本不以该前缀开头则返回 `None`。",
    "the prefix.": "",
    "The `isPrefixOf` function takes two text arguments and returns":
        "`isPrefixOf` 判断第一段是否为第二段的前缀。",
    "`True` if and only if the first is a prefix of the second.": "",
    "The `isSuffixOf` function takes two text arguments and returns":
        "`isSuffixOf` 判断第一段是否为第二段的后缀。",
    "`True` if and only if the first is a suffix of the second.": "",
    "The `isInfixOf` function takes two text arguments and returns":
        "`isInfixOf` 判断第一段是否完整出现在第二段中。",
    "`True` if and only if the first is contained, wholly and intact,":
        "",
    "anywhere within the second.": "",
    "The function `takeWhile`, applied to a predicate `p` and a text,":
        "`takeWhile p t` 返回 `t` 中最长前缀（可为空），",
    "returns the longest prefix (possibly empty) of symbols that satisfy":
        "其中符号均满足 `p`。",
    "`p`.": "",
    "The function 'takeWhileEnd', applied to a predicate `p` and a":
        "`takeWhileEnd p t` 返回 `t` 中最长后缀（可为空），",
    "'Text', returns the longest suffix (possibly empty) of elements":
        "其中符号均满足 `p`。",
    "that satisfy `p`.": "",
    "`dropWhile p t` returns the suffix remaining after `takeWhile p":
        "`dropWhile p t` 为 `takeWhile p t` 之后的后缀。",
    "t`.": "",
    "`dropWhileEnd p t` returns the prefix remaining after dropping":
        "`dropWhileEnd p t` 为从末尾去掉满足 `p` 的符号后剩余的前缀。",
    "symbols that satisfy the predicate `p` from the end of `t`.": "",
    "Break a text into pieces separated by the first text argument":
        "用第一个文本（不可为空）作分隔符拆分，并消耗分隔符。",
    "(which cannot be empty), consuming the delimiter.": "",
    "Split a text before a given position so that for `0 <= n <= length t`,":
        "在指定位置拆分，使得对 `0 <= n <= length t`，",
    "`length (fst (splitAt n t)) == n`.": "`length (fst (splitAt n t)) == n`。",
    "`take n`, applied to a text `t`, returns the prefix of `t` of":
        "`take n t` 返回长度为 `n` 的前缀；若 `n` 大于长度则返回 `t`。",
    "length `n`, or `t` itself if `n` is greater than the length of `t`.": "",
    "`drop n`, applied to a text `t`, returns the suffix of `t` after":
        "`drop n t` 返回去掉前 `n` 个字符后的后缀；",
    "the first `n` characters, or the empty `Text` if `n` is greater":
        "若 `n` 大于长度则返回空 `Text`。",
    "than the length of `t`.": "",
    "Compute the sequence of symbols of length `l` in the argument":
        "从参数文本的位置 `s` 起取长度为 `l` 的符号序列。",
    "text starting at `s`.": "",
    "`isPred f t` returns `True` if `t` is not empty and `f` is `True`":
        "`isPred f t` 在 `t` 非空且 `t` 中所有符号满足 `f` 时为 `True`。",
    "for all symbols in `t`.": "",
    "`isSpace t` is `True` if `t` is not empty and consists only of":
        "`isSpace t` 在 `t` 非空且仅含空格时为 `True`。",
    "spaces.": "",
    "`isSpace t` is `True` if `t` is not empty and consists only of":
        "`isNewLine t` 在 `t` 非空且仅含换行符时为 `True`。",
    "newlines.": "",
    "`isUpper t` is `True` if `t` is not empty and consists only of":
        "`isUpper t` 在 `t` 非空且仅含大写符号时为 `True`。",
    "uppercase symbols.": "",
    "`isLower t` is `True` if `t` is not empty and consists only of":
        "`isLower t` 在 `t` 非空且仅含小写符号时为 `True`。",
    "lowercase symbols.": "",
    "`isDigit t` is `True` if `t` is not empty and consists only of":
        "`isDigit t` 在 `t` 非空且仅含数字符号时为 `True`。",
    "digit symbols.": "",
    "`isAlpha t` is `True` if `t` is not empty and consists only of":
        "`isAlpha t` 在 `t` 非空且仅含字母符号时为 `True`。",
    "alphabet symbols.": "",
    "`isAlphaNum t` is `True` if `t` is not empty and consists only of":
        "`isAlphaNum t` 在 `t` 非空且仅含字母数字符号时为 `True`。",
    "alphanumeric symbols.": "",
    "Attempt to parse an `Int` value from a given `Text`.": "尝试从 `Text` 解析 `Int`。",
    "Attempt to parse a `Numeric` value from a given `Text`.": "尝试从 `Text` 解析 `Numeric`。",
    "To get `Some` value, the text must follow the regex": "要得到 `Some`，文本须匹配正则",
    "In particular, the shorthands `\".12\"` and `\"12.\"` do not work,":
        "简写 `\".12\"`、`\"12.\"` 无效，",
    "but the value can be prefixed with `+`.": "但可用 `+` 前缀。",
    "Leading and trailing zeros are fine, however spaces are not.": "首尾零可以，但不可含空格。",
    "Examples:": "示例：",
    "Attempt to parse a `Decimal` value from a given `Text`.": "尝试从 `Text` 解析 `Decimal`。",
    "Computes the SHA256 hash of the UTF8 bytes of the `Text`, and returns it in its hex-encoded":
        "对 `Text` 的 UTF-8 字节计算 SHA256，并以小写十六进制返回。",
    "form. The hex encoding uses lowercase letters.": "",
    "This function will crash at runtime if you compile Daml to Daml-LF \\< 1.2.":
        "若编译目标为 Daml-LF < 1.2，此函数会在运行时崩溃。",
    "Reverse some `Text`.": "反转 `Text`。",
    "Convert a `Text` into a sequence of unicode code points.": "将 `Text` 转为 Unicode 码点序列。",
    "Convert a sequence of unicode code points into a `Text`. Raises an":
        "将 Unicode 码点序列转为 `Text`；无效码点会抛异常。",
    "exception if any of the code points is invalid.": "",
    "Convert the uppercase ASCII characters of a `Text` to lowercase;":
        "将 `Text` 中的 ASCII 大写转为小写；",
    "all other characters remain unchanged.": "其他字符不变。",
    "Convert the lowercase ASCII characters of a `Text` to uppercase;":
        "将 `Text` 中的 ASCII 小写转为大写；",
    "TextMap - A map is an associative array data type composed of a":
        "TextMap——键值对关联数组，每个键最多出现一次。",
    "collection of key/value pairs such that, each possible key appears":
        "",
    "at most once in the collection.": "",
    "Create a map from a list of key/value pairs.": "由键值对列表创建映射。",
    "Create a map from a list of key/value pairs with a combining":
        "由键值对列表创建映射，并用合并函数处理重复键。",
    "function. The combining function is only used when a key appears multiple":
        "合并函数仅在键多次出现时调用，",
    "times in the list and it takes two arguments: the first one is the new value":
        "参数为新插入值与该键已累积值。",
    "being inserted at that key and the second one is the value accumulated so":
        "",
    "far at that key.": "",
    "Create a map from a list of key/value pairs like `fromListWithL`":
        "类似 `fromListWithL`，但合并函数参数顺序相反。",
    "with the combining function flipped. Examples:": "示例：",
    "Convert the map to a list of key/value pairs where the keys are":
        "将映射转为键值对列表，键按升序排列。",
    "in ascending order.": "",
    "The empty map.": "空映射。",
    "Number of elements in the map.": "映射中元素个数。",
    "Is the map empty?": "映射是否为空？",
    "Lookup the value at a key in the map.": "按键查找值。",
    "Is the key a member of the map?": "键是否在映射中？",
    "Filter the `TextMap` using a predicate: keep only the entries where the":
        "用谓词过滤 `TextMap`：仅保留值满足谓词的条目。",
    "value satisfies the predicate.": "",
    "Filter the `TextMap` using a predicate: keep only the entries which":
        "用谓词过滤 `TextMap`：仅保留满足谓词的条目。",
    "satisfy the predicate.": "",
    "Delete a key and its value from the map. When the key is not a":
        "删除键及其值；键不存在时返回原映射。",
    "member of the map, the original map is returned.": "",
    "Create a singleton map.": "创建单键映射。",
    "Insert a new key/value pair in the map. If the key is already":
        "插入键值对；键已存在则替换为给定值。",
    "present in the map, the associated value is replaced with the":
        "",
    "supplied value.": "",
    "Insert a new key/value pair in the map. If the key is already":
        "插入键值对；键已存在时用 `f new_value old_value` 合并。",
    "present in the map, it is combined with the previous value using the given function":
        "",
    "`f new_value old_value`.": "",
    "The union of two maps, preferring the first map when equal":
        "两映射的并集；键冲突时优先取第一个映射的值。",
    "keys are encountered.": "",
    "Merge two maps. `merge f g h x y` applies `f` to all key/value pairs":
        "合并两映射。`merge f g h x y` 对仅出现在 `x` 的键用 `f`，",
    "whose key only appears in `x`, `g` to all pairs whose key only appears":
        "仅出现在 `y` 的键用 `g`，",
    "in `y` and `h` to all pairs whose key appears in both `x` and `y`.":
        "两映射都有的键用 `h`；保留结果为 `Some` 的条目。",
    "In the end, all pairs yielding `Some` are collected as the result.": "",
    "This module provides a set of functions to manipulate Time values.":
        "本模块提供操作 Time 值的函数集。",
    "The `Time` type represents a specific datetime in UTC,":
        "`Time` 表示 UTC 下的具体日期时间，",
    "for example `time (date 2007 Apr 5) 14 30 05`.": "例如 `time (date 2007 Apr 5) 14 30 05`。",
    "The bounds for Time are 0001-01-01T00:00:00.000000Z and":
        "Time 范围为 0001-01-01T00:00:00.000000Z 至",
    "9999-12-31T23:59:59.999999Z.": "9999-12-31T23:59:59.999999Z。",
    "The `RelTime` type describes a time offset, i.e. relative time.":
        "`RelTime` 表示时间偏移（相对时间）。",
    "`time d h m s` turns given UTC date `d` and the UTC time (given in hours, minutes, seconds)":
        "`time d h m s` 将 UTC 日期 `d` 与 UTC 时分秒转为 `Time`；不处理闰秒。",
    "into a UTC timestamp (`Time`). Does not handle leap seconds.": "",
    "Adjusts `Time` with given time offset.": "用给定偏移调整 `Time`。",
    "Returns time offset between two given instants.": "返回两时刻的时间差。",
    "Returns the number of whole days in a time offset. Fraction of time is rounded towards zero.":
        "返回偏移中的整天数；小数部分向零取整。",
    "A number of days in relative time.": "相对时间中的天数。",
    "A number of hours in relative time.": "相对时间中的小时数。",
    "A number of minutes in relative time.": "相对时间中的分钟数。",
    "A number of seconds in relative time.": "相对时间中的秒数。",
    "A number of milliseconds in relative time.": "相对时间中的毫秒数。",
    "A number of microseconds in relative time.": "相对时间中的微秒数。",
    "Convert RelTime to microseconds": "将 RelTime 转为微秒",
    "Use higher level functions instead of the internal microseconds": "优先使用高层函数而非内部微秒 API",
    "Convert microseconds to RelTime": "将微秒转为 RelTime",
    "True iff the ledger time of the transaction is less than the given time.":
        "当且仅当交易的账本时间小于给定时间时为 True。",
    "True iff the ledger time of the transaction is less than or equal to the given time.":
        "当且仅当交易的账本时间小于等于给定时间时为 True。",
    "True iff the ledger time of the transaction is greater than the given time.":
        "当且仅当交易的账本时间大于给定时间时为 True。",
    "True iff the ledger time of the transaction is greater than or equal to the given time.":
        "当且仅当交易的账本时间大于等于给定时间时为 True。",
    "Class of data structures that can be traversed from left to right, performing an action on each element.":
        "可从左到右遍历并对每个元素执行动作的数据结构类型类。",
    "You typically would want to import this module qualified to avoid clashes with":
        "通常应限定导入以避免与",
    "functions defined in `Prelude`. Ie.:": "`Prelude` 中函数冲突，例如：",
    "Functors representing data structures that can be traversed from left to right.":
        "表示可从左到右遍历的数据结构的 Functor。",
    "Map each element of a structure to an action, evaluate these actions":
        "将结构中每个元素映射为动作，从左到右求值并收集结果。",
    "from left to right, and collect the results.": "",
    "Evaluate each action in the structure from left to right, and":
        "从左到右求值结构中的每个动作并收集结果。",
    "collect the results.": "",
    "`forA` is `mapA` with its arguments flipped.": "`forA` 是参数翻转的 `mapA`。",
    "Tuple - Ubiquitous functions of tuples.": "Tuple——元组的常用函数。",
    "The pair obtained from a pair by application of a programmer":
        "对二元组第一分量应用函数得到的新二元组。",
    "supplied function to the argument pair's first field.": "",
    "supplied function to the argument pair's second field.": "对二元组第二分量应用函数得到的新二元组。",
    "supplied function to both the argument pair's first and second":
        "对二元组两个分量应用同一函数。",
    "fields.": "",
    "The pair obtained from a pair by permuting the order of the":
        "交换二元组两个分量的顺序。",
    "argument pair's first and second fields.": "",
    "Duplicate a single value into a pair.": "将单个值复制为二元组。",
    "Extract the 'fst' of a triple.": "取三元组第一分量。",
    "Extract the 'snd' of a triple.": "取三元组第二分量。",
    "Extract the final element of a triple.": "取三元组第三分量。",
    "Converts an uncurried function to a curried function.": "将非柯里化函数转为柯里化函数。",
    "Converts a curried function to a function on a triple.": "将柯里化函数转为接受三元组的函数。",
    "`Validation` type and associated functions.": "`Validation` 类型及相关函数。",
    "A `Validation` represents eithor a non-empty list of errors, or a successful value.":
        "`Validation` 表示非空错误列表或成功值。",
    "This generalizes `Either` to allow more than one error to be collected.":
        "相比 `Either`，可累积多条错误。",
    "Fail for the given reason.": "因给定原因失败。",
    "Succeed with the given value.": "以给定值成功。",
    "Turn an `Either` into a `Validation`.": "将 `Either` 转为 `Validation`。",
    "Convert a `Validation err a` value into an `Either`,":
        "将 `Validation err a` 转为 `Either`，",
    "taking the non-empty list of errors as the left value.": "左值为非空错误列表。",
    "taking just the first error as the left value.": "左值仅取第一个错误。",
    "Run a `Validation err a` with a default value in case of errors.":
        "运行 `Validation err a`，出错时返回默认值。",
    "Convert an `Optional t` into a `Validation err t`, or":
        "将 `Optional t` 转为 `Validation err t`（或更一般地转为任意 `ActionFail` 类型 `m` 的 `m t`）。",
    "more generally into an `m t` for any `ActionFail` type `m`.": "",
    "The pieces that make up the Daml language.": "构成 Daml 语言的核心部分。",
    "Existential choice type that can wrap an arbitrary choice.": "可包装任意 choice 的存在类型。",
    "Existential contract key type that can wrap an arbitrary contract key.":
        "可包装任意合约键的存在类型。",
    "Existential template type that can wrap an arbitrary template.":
        "可包装任意 template 的存在类型。",
    "Unique textual representation of a template Id.": "模板 Id 的唯一文本表示。",
    "The `Down` type can be used for reversing sorting order.":
        "`Down` 可用于反转排序顺序。",
    "For example, `sortOn (\\x -> Down x.field)` would sort by descending `field`.":
        "例如 `sortOn (\\x -> Down x.field)` 按 `field` 降序排序。",
    "(Daml-LF >= 1.15) Constraint that indicates that a template implements an interface.":
        "（Daml-LF >= 1.15）表示 template 实现某 interface 的约束。",
    "A wrapper for all exception types.": "所有异常类型的包装。",
    "Deprecated: Exceptions are deprecated, prefer `failWithStatus`, and avoid using catch.":
        "已弃用：异常已弃用，请用 `failWithStatus`，避免 catch。",
    "Deprecated: Use `-Wno-deprecated-exceptions` to disable this warning.":
        "已弃用：可用 `-Wno-deprecated-exceptions` 关闭此警告。",
    "The `ContractId a` type represents an ID for a contract created from a template `a`.":
        "`ContractId a` 表示由 template `a` 创建的合约 ID。",
    "You can use the ID to fetch the contract, among other things.": "可用于 fetch 等操作。",
    "The `Date` type represents a date, for example `date 2007 Apr 5`.":
        "`Date` 表示日期，例如 `date 2007 Apr 5`。",
    "The bounds for Date are 0001-01-01 and 9999-12-31.": "Date 范围为 0001-01-01 至 9999-12-31。",
    "The `Map a b` type represents an associative array from keys of type `a`":
        "`Map a b` 是从 `a` 到 `b` 的关联数组，使用内建相等性；",
    "to values of type `b`. It uses the built-in equality for keys. Import":
        "请 import `DA.Map` 使用。",
    "`DA.Map` to use it.": "",
    "The `Party` type represents a party to a contract.": "`Party` 表示合约参与方。",
    "The `TextMap a` type represents an associative array from keys of type":
        "`TextMap a` 是从 `Text` 到 `a` 的关联数组。",
    "`Text` to values of type `a`.": "",
    "The `Update a` type represents an `Action` to update or query the ledger,":
        "`Update a` 表示更新或查询账本并返回 `a` 的 `Action`，",
    "before returning a value of type `a`. Examples include `create` and `fetch`.":
        "例如 `create`、`fetch`。",
    "The `Optional` type encapsulates an optional value.  A value of type":
        "`Optional a` 封装可选值：`Some a` 含值，`None` 为空。",
    "`Optional a` either contains a value of type `a` (represented as `Some a`),":
        "",
    "or it is empty (represented as `None`).  Using `Optional` is a good way to":
        "用 `Optional` 处理错误或边界情况，",
    "deal with errors or exceptional cases without resorting to drastic":
        "无需使用 `error` 等激烈手段。",
    "measures such as `error`.": "",
    "The `Optional` type is also an `Action`.  It is a simple kind of error":
        "`Optional` 也是 `Action`，",
    "`Action`, where all errors are represented by `None`.  A richer":
        "错误以 `None` 表示；更丰富的错误可用 `Either`。",
    "error `Action` could be built using the `Data.Either.Either` type.": "",
    "The data type corresponding to the implicit `Archive`": "对应每个 template 隐式 `Archive`",
    "choice in every template.": "choice 的数据类型。",
    "Constraint satisfied by choices.": "choice 需满足的约束。",
    "Constraint satisfied by template keys.": "template key 需满足的约束。",
    "Constraint that determines whether an assertion can be made": "决定当前上下文是否可断言的约束。",
    "in this context.": "",
    "Abort since an assertion has failed. In an Update, Scenario,":
        "断言失败时中止。在 Update/Scenario/Script 中抛 AssertionFailed；",
    "or Script context this will throw an AssertionFailed": "",
    "exception. In an `Either Text` context, this will return the":
        "在 `Either Text` 中返回错误消息。",
    "message as an error.": "",
    "(Daml-LF >= 1.15) Exposes the `interfaceTypeRep` function. Available only for interfaces.":
        "（Daml-LF >= 1.15）暴露 `interfaceTypeRep`，仅用于 interface。",
    "(Daml-LF >= 1.15) Exposes the `toInterface` and `toInterfaceContractId` functions.":
        "（Daml-LF >= 1.15）暴露 `toInterface` 与 `toInterfaceContractId`。",
    "(Daml-LF >= 1.15) Exposes `fromInterface` and `fromInterfaceContractId`":
        "（Daml-LF >= 1.15）暴露 `fromInterface` 与 `fromInterfaceContractId`。",
    "functions.": "",
    "(Daml-LF >= 1.15) Attempt to convert an interface value back into a":
        "（Daml-LF >= 1.15）尝试将 interface 值转回 template 值；",
    "template value. A `None` indicates that the expected template":
        "`None` 表示底层 template 类型不匹配。",
    "type doesn't match the underyling template type for the":
        "",
    "interface value.": "",
    "For example, `fromInterface @MyTemplate value` will try to convert":
        "例如 `fromInterface @MyTemplate value` 尝试将 interface 值转为 `MyTemplate`。",
    "the interface value `value` into the template type `MyTemplate`.": "",
    "The `HasTime` class is for where the time is available: `Update`":
        "`HasTime` 用于可获取时间的上下文（如 `Update`）。",
    "Get the current time.": "获取当前时间。",
    "The `CanAbort` class is for `Action` s that can be aborted.": "`CanAbort` 用于可中止的 `Action`。",
    "Abort the current action with a message.": "带消息中止当前动作。",
    "Lift a value.": "提升值。",
    "<*> : f (a -> b) -> f a -> f b": "<*> : f (a -> b) -> f a -> f b",
    "Sequentially apply the function.": "顺序应用函数。",
    "A few functors support an implementation of `<*>` that is more":
        "部分 functor 的 `<*>` 实现比默认更高效。",
    "efficient than the default one.": "",
    "Lift a binary function to actions.": "将二元函数提升到动作。",
    "Some functors support an implementation of `liftA2` that is more":
        "部分 functor 的 `liftA2` 比默认更高效；",
    "efficient than the default one. In particular, if `fmap` is an":
        "若 `fmap` 开销大，优先用 `liftA2` 而非 `fmap` 后再 `<*>`。",
    "expensive operation, it is likely better to use `liftA2` than to":
        "",
    "`fmap` over the structure and then use `<*>`.": "",
    "Sequence actions, discarding the value of the first argument.": "顺序执行动作，丢弃第一个结果。",
    "Sequence actions, discarding the value of the second argument.": "顺序执行动作，丢弃第二个结果。",
    "Sequentially compose two actions, passing any value produced":
        "顺序组合两个动作，将第一个的结果传给第二个。",
    "by the first as an argument to the second.": "",
    "This class exists to desugar pattern matches in do-notation.":
        "此类用于 do 记法中模式匹配的脱糖。",
    "Polymorphic usage, or calling `fail` directly, is not recommended.":
        "不建议多态使用或直接调用 `fail`；",
    "Instead consider using `CanAbort`.": "请考虑 `CanAbort`。",
    "Fail with an error message.": "以错误消息失败。",
    "The class of semigroups (types with an associative binary operation).":
        "半群类型类（具有结合二元运算的类型）。",
    "An associative operation.": "结合运算。",
    "The class of monoids (types with an associative binary operation that has an identity).":
        "幺半群类型类（具有结合二元运算与单位元的类型）。",
    "Identity of `(<>)`": "`(<>)` 的单位元",
    "Fold a list using the monoid.": "用幺半群折叠列表。",
    "For example using `mconcat` on a list of strings would concatenate all strings to one lone string.":
        "例如对字符串列表 `mconcat` 会拼接成单个字符串。",
    "Exposes `signatory` function. Part of the `Template` constraint.":
        "暴露 `signatory`，属于 `Template` 约束。",
    "The signatories of a contract.": "合约的 signatory。",
    "Exposes `observer` function. Part of the `Template` constraint.":
        "暴露 `observer`，属于 `Template` 约束。",
    "The observers of a contract.": "合约的 observer。",
    "Exposes `ensure` function. Part of the `Template` constraint.":
        "暴露 `ensure`，属于 `Template` 约束。",
    "A predicate that must be true, otherwise contract creation will fail.":
        "必须为 true 的谓词，否则创建合约失败。",
    "Exposes `create` function. Part of the `Template` constraint.":
        "暴露 `create`，属于 `Template` 约束。",
    "Create a contract based on a template `t`.": "基于 template `t` 创建合约。",
    "Exposes `fetch` function. Part of the `Template` constraint.":
        "暴露 `fetch`，属于 `Template` 约束。",
    "Fetch the contract data associated with the given contract ID.":
        "获取给定合约 ID 的合约数据。",
    "If the `ContractId t` supplied is not the contract ID of an active":
        "若 ID 不对应活跃合约，",
    "contract, this fails and aborts the entire transaction.": "则失败并中止整个交易。",
    "Exposes `softFetch` function": "暴露 `softFetch`",
    "Exposes `archive` function. Part of the `Template` constraint.":
        "暴露 `archive`，属于 `Template` 约束。",
    "Archive the contract with the given contract ID.": "归档给定合约 ID 的合约。",
    "Exposes `templateTypeRep` function in Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `templateTypeRep`，属于 `Template` 约束。",
    "Part of the `Template` constraint.": "",
    "Exposes `toAnyTemplate` function in Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `toAnyTemplate`，属于 `Template` 约束。",
    "Exposes `fromAnyTemplate` function in Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `fromAnyTemplate`，属于 `Template` 约束。",
    "Exposes `exercise` function. Part of the `Choice` constraint.":
        "暴露 `exercise`，属于 `Choice` 约束。",
    "Exercise a choice on the contract with the given contract ID.":
        "对给定合约 ID 行使 choice。",
    "Exposes `choiceController` function. Part of the `Choice` constraint.":
        "暴露 `choiceController`，属于 `Choice` 约束。",
    "Exposes `choiceObserver` function. Part of the `Choice` constraint.":
        "暴露 `choiceObserver`，属于 `Choice` 约束。",
    "(1.dev only) Exposes `exerciseGuarded` function.":
        "（仅 1.dev）暴露 `exerciseGuarded`，仅用于 interface choice。",
    "Only available for interface choices.": "",
    "(1.dev only) Exercise a choice on the contract with":
        "（仅 1.dev）仅当谓词为 `True` 时对合约行使 choice。",
    "the given contract ID, only if the predicate returns `True`.": "",
    "Exposes `toAnyChoice` function for Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `toAnyChoice`，属于 `Choice` 约束。",
    "Exposes `fromAnyChoice` function for Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `fromAnyChoice`，属于 `Choice` 约束。",
    "Exposes `key` function. Part of the `TemplateKey` constraint.":
        "暴露 `key`，属于 `TemplateKey` 约束。",
    "The key of a contract.": "合约键。",
    "Exposes `lookupByKey` function. Part of the `TemplateKey` constraint.":
        "暴露 `lookupByKey`，属于 `TemplateKey` 约束。",
    "Look up the contract ID `t` associated with a given contract key `k`.":
        "查找与合约键 `k` 关联的 template `t` 的合约 ID。",
    "You must pass the `t` using an explicit type application. For":
        "须显式类型应用 `t`，",
    "instance, if you want to look up a contract of template `Account` by its":
        "例如 `lookupByKey @Account k`。",
    "key `k`, you must call `lookupByKey @Account k`.": "",
    "Exposes `fetchByKey` function. Part of the `TemplateKey` constraint.":
        "暴露 `fetchByKey`，属于 `TemplateKey` 约束。",
    "Fetch the contract ID and contract data associated with a given":
        "获取与合约键关联的合约 ID 与数据；",
    "contract key.": "",
    "Exposes `maintainer` function. Part of the `TemplateKey` constraint.":
        "暴露 `maintainer`，属于 `TemplateKey` 约束。",
    "Exposes `toAnyContractKey` function in Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `toAnyContractKey`，属于 `TemplateKey` 约束。",
    "Exposes `fromAnyContractKey` function in Daml-LF 1.7 or later.":
        "在 Daml-LF 1.7+ 暴露 `fromAnyContractKey`，属于 `TemplateKey` 约束。",
    "Exposes `exerciseByKey` function.": "暴露 `exerciseByKey`。",
    "Accepted ways to specify a list of parties: either a single party, or a list of parties.":
        "指定 party 列表的方式：单个 party 或 party 列表。",
    "Convert to list of parties.": "转为 party 列表。",
    "Check whether a condition is true. If it's not, abort the transaction.":
        "检查条件是否为真；否则中止交易。",
    "Check whether a condition is true. If it's not, abort the transaction":
        "检查条件是否为真；否则带消息中止交易。",
    "with a message.": "",
    "Check whether the given time is in the future. If it's not, abort the transaction.":
        "检查给定时间是否在未来；否则中止交易。",
    "Check whether the given time is in the past. If it's not, abort the transaction.":
        "检查给定时间是否在过去；否则中止交易。",
    "Convert from number of days since epoch (i.e. the number of days since":
        "将自 epoch（1970-01-01）起的天数转为日期。",
    "January 1, 1970) to a date.": "",
    "Convert from a date to number of days from epoch (i.e. the number of days":
        "将日期转为自 epoch 起的天数。",
    "since January 1, 1970).": "",
    "(Daml-LF >= 1.15) Obtain the `TemplateTypeRep` for the template given in the interface value.":
        "（Daml-LF >= 1.15）从 interface 值获取其 template 的 `TemplateTypeRep`。",
    "(Daml-LF >= 1.15) Convert a template value into an interface value.":
        "（Daml-LF >= 1.15）将 template 值转为 interface 值。",
    "For example `toInterface @MyInterface value` converts a template":
        "例如 `toInterface @MyInterface value` 将 template 值转为 `MyInterface`。",
    "`value` into a `MyInterface` type.": "",
    "(Daml-LF >= 1.15) Convert a template contract id into an interface":
        "（Daml-LF >= 1.15）将 template 合约 ID 转为 interface 合约 ID。",
    "contract id. For example, `toInterfaceContractId @MyInterface cid`.": "",
    "(Daml-LF >= 1.15) Convert an interface contract id into a template":
        "（Daml-LF >= 1.15）将 interface 合约 ID 转为 template 合约 ID。",
    "contract id. For example, `fromInterfaceContractId @MyTemplate cid`.": "",
    "Can also be used to convert an interface contract id into a contract id of":
        "也可转为所需 interface 的合约 ID。",
    "one of its requiring interfaces.": "",
    "This function does not verify that the interface contract id":
        "此函数不验证 ID 是否指向预期 template；",
    "actually points to a template of the given type. This means":
        "后续 fetch/exercise/archive 可能失败。",
    "that a subsequent `fetch`, `exercise`, or `archive` may fail, if,":
        "",
    "for example, the contract id points to a contract that implements":
        "",
    "the interface but is of a different template type than expected.": "",
    "Therefore, you should only use `fromInterfaceContractId` in situations":
        "仅在已知类型正确或会立即 fetch/exercise/archive 时使用；",
    "where you already know that the contract id points to a contract of the":
        "否则请用 `fetchFromInterface`。",
    "right template type. You can also use it in situations where you will":
        "",
    "fetch, exercise, or archive the contract right away, when a transaction":
        "",
    "failure is the appropriate response to the contract having the wrong":
        "",
    "template type.": "",
    "In all other cases, consider using `fetchFromInterface` instead.": "",
    "(Daml-LF >= 1.15) Convert an interface contract id into a contract id of a":
        "（Daml-LF >= 1.15）将 interface 合约 ID 转为另一 interface 的合约 ID。",
    "different interface. For example, given two interfaces `Source` and `Target`,":
        "",
    "and `cid : ContractId Source`,":
        "",
    "`coerceInterfaceContractId @Target @Source cid : ContractId Target`.": "",
    "(Daml-LF >= 1.15) Fetch an interface and convert it to a specific":
        "（Daml-LF >= 1.15）fetch interface 并转为指定 template；",
    "template type. If conversion is succesful, this function returns":
        "成功则返回 `(ContractId t, t)`，否则 `None`。",
    "the converted contract and its converted contract id. Otherwise,":
        "",
    "this function returns `None`.": "",
    "Can also be used to fetch and convert an interface contract id into a":
        "也可 fetch 并转为所需 interface 的合约与 ID。",
    "contract and contract id of one of its requiring interfaces.": "",
    "Example:": "示例：",
    "Convert the `Party` to `Text`, giving back what you passed to `getParty`.":
        "将 `Party` 转为 `Text`（与 `getParty` 传入一致）。",
    "In most cases, you should use `show` instead. `show` wraps":
        "多数情况用 `show`；`show` 会用反引号标明原为 `Party`。",
    "the party in `'ticks'` making it clear it was a `Party` originally.": "",
    "Converts a `Text` to `Party`. It returns `None` if the provided text contains":
        "将 `Text` 转为 `Party`；含非法字符则 `None`。",
    "any forbidden characters. See Daml-LF spec for a specification on which characters":
        "见 Daml-LF 规范；接受无单引号的文本。",
    "are allowed in parties. Note that this function accepts text *without*":
        "",
    "single quotes.": "",
    "This function does not check on whether the provided":
        "不检查 ledger 上是否存在该 party；",
    "text corresponds to a party that \"exists\" on a given ledger: it merely converts":
        "仅做类型转换。",
    "the given `Text` to a `Party`. The only way to guarantee that a given `Party`":
        "要保证 party 存在须让其参与合约。",
    "exists on a given ledger is to involve it in a contract.": "",
    "This function, together with `partyToText`, forms an isomorphism between":
        "`partyFromText` 与 `partyToText` 在合法 party 字符串与 party 间构成同构。",
    "valid party strings and parties. In other words, the following equations hold:":
        "",
    "This function will crash at runtime if you compile Daml to Daml-LF \\< 1.2.":
        "若编译目标为 Daml-LF < 1.2，此函数会在运行时崩溃。",
    "Used to convert the type index of a `ContractId`, since they are just":
        "转换 `ContractId` 的类型索引（仅为指针）；",
    "pointers. Note that subsequent fetches and exercises might fail if the":
        "若 ledger 上 template 不匹配，后续 fetch/exercise 可能失败。",
    "template of the contract on the ledger doesn't match.": "",
    "Turn a function that takes a pair into a function that takes two arguments.":
        "将接受二元组的函数转为接受两个参数的函数。",
    "Turn a function that takes two arguments into a function that takes a pair.":
        "将接受两个参数的函数转为接受二元组的函数。",
    "Sequentially compose two actions, discarding any value produced":
        "顺序组合两个动作，丢弃第一个结果（类似命令式分号）。",
    "by the first. This is like sequencing operators (such as the semicolon)":
        "",
    "in imperative languages.": "",
    "Synonym for `<*>`.": "`<*>` 的同义词。",
    "Inject a value into the monadic type. For example, for `Update` and a":
        "将值注入 monadic 类型；例如 `Update` 中 `return` 得到 `Update a`。",
    "value of type `a`, `return` would give you an `Update a`.": "",
    "Collapses nested actions into a single action.": "将嵌套动作折叠为单一动作。",
    "The identity function.": "恒等函数。",
    "This function is a left fold, which you can use to inspect/analyse/consume lists.":
        "左折叠，用于检查/分析/消费列表。",
    "`foldl f i xs` performs a left fold over the list `xs` using":
        "`foldl f i xs` 用 `f` 与初值 `i` 从左到右折叠 `xs`。",
    "the function `f`, using the starting value `i`.": "",
    "Note that foldl works from left-to-right over the list arguments.": "foldl 从左到右处理列表。",
    "`find p xs` finds the first element of the list `xs` where the":
        "`find p xs` 返回 `xs` 中首个满足 `p` 的元素（`Optional`）。",
    "predicate `p` is true. There might not be such an element, which":
        "",
    "is why this function returns an `Optional a`.": "",
    "Gives the length of the list.": "返回列表长度。",
    "Are there any elements in the list where the predicate is true?":
        "列表中是否存在满足谓词的元素？",
    "`any p xs` is `True` if `p` holds for at least one element of `xs`.":
        "",
    "Is the predicate true for all of the elements in the list?":
        "谓词是否对列表所有元素为真？",
    "`all p xs` is `True` if `p` holds for every element of `xs`.": "",
    "Is at least one of elements in a list of `Bool` true?":
        "Bool 列表中是否至少有一个为 True？",
    "`or bs` is `True` if at least one element of `bs` is `True`.": "",
    "Is every element in a list of Bool true?": "Bool 列表是否全为 True？",
    "`and bs` is `True` if every element of `bs` is `True`.": "",
    "Does this value exist in this list?": "值是否在列表中？",
    "`elem x xs` is `True` if `x` is an element of the list `xs`.": "",
    "Negation of `elem`:": "`elem` 的否定：",
    "`elem x xs` is `True` if `x` is *not* an element of the list `xs`.": "",
    "Synonym for `fmap`.": "`fmap` 的同义词。",
    "The `optional` function takes a default value, a function, and a `Optional`":
        "`optional` 取默认值、函数与 `Optional` 值；",
    "value.  If the `Optional` value is `None`, the function returns the":
        "`None` 时返回默认值，否则对 `Some` 内值应用函数。",
    "default value.  Otherwise, it applies the function to the value inside":
        "",
    "the `Some` and returns the result.": "",
    "Basic usage examples:": "基本示例：",
    "This example applies `show` to a `Optional Int`. If you have `Some n`,":
        "对 `Optional Int` 应用 `show`：`Some n` 显示 `n`，`None` 显示空串。",
    "this shows the underlying `Int`, `n`. But if you have `None`, this":
        "",
    "returns the empty string instead of (for example) `None`:": "",
    "The `either` function provides case analysis for the `Either` type.":
        "`either` 对 `Either` 做分支：`Left` 用第一个函数，`Right` 用第二个。",
    "If the value is `Left a`, it applies the first function to `a`;":
        "",
    "if it is `Right b`, it applies the second function to `b`.": "",
    "This example has two values of type `Either [Int] Int`, one using the":
        "示例：`Left [Int]` 用 `length`，`Right Int` 用翻倍。",
    "`Left` constructor and another using the `Right` constructor. Then":
        "",
    "it applies `either` the `length` function (if it has a `[Int]`)":
        "",
    "or the \"times-two\" function (if it has an `Int`):":
        "",
    "Take a list of lists and concatenate those lists into one list.":
        "将列表的列表拼接为一个列表。",
    "Concatenate two lists.": "连接两个列表。",
    "Flip the order of the arguments of a two argument function.":
        "翻转二元函数的两个参数顺序。",
    "Reverse a list.": "反转列表。",
    "Apply an applicative function to each element of a list.":
        "对列表每个元素应用 applicative 函数。",
    "Perform a list of actions in sequence and collect the results.":
        "顺序执行动作列表并收集结果。",
    "`=<<` is `>>=` with its arguments flipped.": "`=<<` 是参数翻转的 `>>=`。",
    "Map a function over each element of a list, and concatenate all the results.":
        "映射函数到列表各元素并拼接所有结果。",
    "`replicate i x` gives the list `[x, x, x, ..., x]` with `i` copies of `x`.":
        "`replicate i x` 生成 `i` 个 `x` 的列表。",
    "Take the first `n` elements of a list.": "取列表前 `n` 个元素。",
    "Drop the first `n` elements of a list.": "丢弃列表前 `n` 个元素。",
    "Split a list at a given index.": "在指定索引处拆分列表。",
    "Take elements from a list while the predicate holds.": "取列表中谓词为真的前缀元素。",
    "Drop elements from a list while the predicate holds.": "丢弃列表中谓词为真的前缀元素。",
    "`span p xs` is equivalent to `(takeWhile p xs, dropWhile p xs)`.":
        "`span p xs` 等价于 `(takeWhile p xs, dropWhile p xs)`。",
    "The `partition` function takes a predicate, a list and returns":
        "`partition p xs` 返回满足/不满足 `p` 的两部分列表。",
    "the pair of lists of elements which do and do not satisfy the":
        "",
    "predicate, respectively; i.e.,": "即",
    "Break a list into two, just before the first element where the predicate holds.":
        "在首个满足谓词的元素前拆成两部分。",
    "`break p xs` is equivalent to `span (not . p) xs`.": "",
    "Look up the first element with a matching key.": "查找首个键匹配的元素的值。",
    "Generate a list containing all values of a given enumeration.":
        "生成给定枚举的所有值列表。",
    "`zip` takes two lists and returns a list of corresponding pairs.":
        "`zip` 将两列表配对；较短列表决定长度。",
    "If one list is shorter, the excess elements of the longer list are discarded.":
        "",
    "`zip3` takes three lists and returns a list of triples, analogous to `zip`.":
        "`zip3` 类似 `zip`，但生成三元组。",
    "`zipWith` takes a function and two lists.":
        "`zipWith` 用函数组合两列表对应元素。",
    "It generalises `zip` by combining elements using the function, instead of forming pairs.":
        "",
    "If one list is shorter, the excess elements of the longer list are discarded.":
        "",
    "`zipWith3` generalises `zip3` by combining elements using the function, instead of forming triples.":
        "`zipWith3` 类似 `zip3`，但用函数组合元素。",
    "Turn a list of pairs into a pair of lists.": "将键值对列表拆成两个列表。",
    "Turn a list of triples into a triple of lists.": "将三元组列表拆成三个列表。",
    "`traceRaw msg a` prints `msg` and returns `a`, for debugging purposes.":
        "`traceRaw msg a` 打印 `msg` 并返回 `a`（调试用）。",
    "The default configuration on the participant logs these messages at DEBUG level.":
        "participant 默认以 DEBUG 级别记录这些消息。",
    "`trace b a` prints `b` and returns `a`, for debugging purposes.": "",
    "`traceId a` prints `a` and returns `a`, for debugging purposes.": "",
    "`debug x` prints `x` for debugging purposes.": "`debug x` 打印 `x`（调试用）。",
    "`debugRaw msg` prints `msg` for debugging purposes.": "`debugRaw msg` 打印 `msg`（调试用）。",
    "Return the first element of a tuple.": "返回元组第一元素。",
    "Return the second element of a tuple.": "返回元组第二元素。",
    "`truncate x` rounds `x` toward zero.": "`truncate x` 向零取整。",
    "Convert an `Int` to a `Numeric`.": "将 `Int` 转为 `Numeric`。",
    "Convert an `Int` to a `Decimal`.": "将 `Int` 转为 `Decimal`。",
    "Bankers' Rounding: `roundBankers dp x` rounds `x` to `dp` decimal places, where a `.5` is rounded to the nearest even digit.":
        "银行家舍入：`roundBankers dp x` 保留 `dp` 位小数，`.5` 舍入到最近偶数。",
    "Commercial Rounding: `roundCommercial dp x` rounds `x` to `dp` decimal places, where a `.5` is rounded away from zero.":
        "商业舍入：`roundCommercial dp x` 保留 `dp` 位小数，`.5` 远离零舍入。",
    "Round a `Numeric` to the nearest integer, where a `.5` is rounded away from zero.":
        "将 `Numeric` 四舍五入到最近整数，`.5` 远离零。",
    "Round a `Decimal` down to the nearest integer.": "将 `Decimal` 向下取整。",
    "Round a `Decimal` up to the nearest integer.": "将 `Decimal` 向上取整。",
    "Is the list empty? `null xs` is true if `xs` is the empty list.":
        "列表是否为空？",
    "Filters the list using the function: keep only the elements where the predicate holds.":
        "用谓词过滤列表。",
    "Add together all the elements in the list.": "对列表元素求和。",
    "Multiply all the elements in the list together.": "对列表元素求积。",
    "A convenience function that can be used to mark something not implemented.":
        "标记未实现的便捷函数；",
    "Always throws an error with \"Not implemented.\"": "总是抛出 \"Not implemented.\"。",
    "The stakeholders of a contract: its signatories and observers.":
        "合约 stakeholder：signatory 与 observer。",
    "The list of maintainers of a contract key.": "合约键的 maintainer 列表。",
    "Exercise a choice on the contract associated with the given key.":
        "对与给定键关联的合约行使 choice。",
    "Create a contract and exercise the choice on the newly created contract.":
        "创建合约并在新合约上行使 choice。",
    "Generate a unique textual representation of the template id.":
        "生成 template id 的唯一文本表示。",
    "Wrap the template in `AnyTemplate`.": "将 template 包装为 `AnyTemplate`。",
    "Only available for Daml-LF 1.7 or later.": "仅 Daml-LF 1.7 或更高版本可用。",
    "Extract the underlying template from `AnyTemplate` if the type matches":
        "类型匹配时从 `AnyTemplate` 提取 template，否则 `None`。",
    "or return `None`.": "",
    "Wrap a choice in `AnyChoice`.": "将 choice 包装为 `AnyChoice`。",
    "You must pass the template type `t` using an explicit type application.":
        "须显式类型应用 template 类型 `t`。",
    "For example `toAnyChoice @Account Withdraw`.": "例如 `toAnyChoice @Account Withdraw`。",
    "Extract the underlying choice from `AnyChoice` if the template and":
        "template 与 choice 类型匹配时从 `AnyChoice` 提取 choice，否则 `None`。",
    "choice types match, or return `None`.": "",
    "For example `fromAnyChoice @Account choice`.": "例如 `fromAnyChoice @Account choice`。",
    "Wrap a contract key in `AnyContractKey`.": "将合约键包装为 `AnyContractKey`。",
    "For example `toAnyContractKey @Proposal k`.": "例如 `toAnyContractKey @Proposal k`。",
    "Extract the underlying key from `AnyContractKey` if the template and":
        "类型匹配时从 `AnyContractKey` 提取键，否则 `None`。",
    "For example `fromAnyContractKey @Proposal k`.": "例如 `fromAnyContractKey @Proposal k`。",
    "True if contract exists, submitter is a stakeholder, and all maintainers":
        "合约存在且提交者为 stakeholder 且所有 maintainer 授权时为 True；",
    "authorize. False if contract does not exist and all maintainers authorize.":
        "合约不存在且所有 maintainer 授权时为 False；",
    "Fails otherwise.": "否则失败。",
    "Action": "Action",
    "List": "List",
    "Exception handling in Daml.": "Daml 中的异常处理。",
    "Fail, for FailureStatus": "Fail，用于 FailureStatus",
    "Class of data structures that can be folded to a summary value.": "可折叠为摘要值的数据结构类型类。",
    "The Functor class is used for types that can be mapped over.": "Functor 用于可映射的类型。",
    "Functions for working with Crypto builtins.": "操作 Crypto 内建的函数。",
    "This module provides a set of functions to manipulate Date values.": "提供操作 Date 值的函数集。",
    "The Either type represents values with two possibilities.": "Either 表示两种可能性的值。",
    "Logic - Propositional calculus.": "Logic——命题演算。",
    "Math - Utility Math functions for Decimal": "Math——Decimal 实用数学函数",
    "Type and functions for non-empty lists. This module re-exports many functions with":
        "非空列表类型与函数；本模块重导出多种函数。",
    "This module contains the type for non-empty lists so we can give it a stable package id.":
        "含非空列表类型定义，以提供稳定 package id。",
    "The Optional type encapsulates an optional value. A value of type":
        "Optional 封装可选值。",
    "Exports the record machinery necessary to allow one to annotate":
        "导出记录机制，用于为记录类型添加注解。",
    "Validation type and associated functions.": "Validation 类型及相关函数。",
    "The pieces that make up the Daml language.": "构成 Daml 语言的核心部分。",
}

INDEX_CARD_SUMMARY: dict[str, str] = {
    "Action": "Action",
    "DA.Action.State": "DA.Action.State",
    "DA.Action.State.Class": "DA.Action.State.Class",
    "-": "-",
    "Functions for working with Crypto builtins.": "操作 Crypto 内建的函数。",
    "This module provides a set of functions to manipulate Date values.": "提供操作 Date 值的函数集。",
    "The Either type represents values with two possibilities.": "Either 表示两种可能性的值。",
    "Exception handling in Daml.": "Daml 中的异常处理。",
    "Fail, for FailureStatus": "Fail，用于 FailureStatus",
    "Class of data structures that can be folded to a summary value.": "可折叠为摘要值的数据结构类型类。",
    "The Functor class is used for types that can be mapped over.": "Functor 用于可映射的类型。",
    "List": "List",
    "Note: This is only supported in Daml-LF 1.11 or later.": "注意：仅支持 Daml-LF 1.11 或更高版本。",
    "Logic - Propositional calculus.": "Logic——命题演算。",
    "Math - Utility Math functions for Decimal": "Math——Decimal 实用数学函数",
    "Type and functions for non-empty lists. This module re-exports many functions with":
        "非空列表类型与函数；本模块重导出多种函数。",
    "This module contains the type for non-empty lists so we can give it a stable package id.":
        "含非空列表类型定义，以提供稳定 package id。",
    "The Optional type encapsulates an optional value. A value of type":
        "Optional 封装可选值。",
    "Exports the record machinery necessary to allow one to annotate":
        "导出记录机制，用于为记录类型添加注解。",
    "Functions for working with Text.": "操作 Text 的函数。",
    "TextMap - A map is an associative array data type composed of a":
        "TextMap——键值对关联数组，每个键最多出现一次。",
    "This module provides a set of functions to manipulate Time values.": "提供操作 Time 值的函数集。",
    "Class of data structures that can be traversed from left to right, performing an action on each element.":
        "可从左到右遍历并对每个元素执行动作的数据结构类型类。",
    "Tuple - Ubiquitous functions of tuples.": "Tuple——元组的常用函数。",
    "Validation type and associated functions.": "Validation 类型及相关函数。",
    "The pieces that make up the Daml language.": "构成 Daml 语言的核心部分。",
}


def strip_en(md: str) -> str:
    md = FRONTMATTER.sub("", md)
    md = DOC_INDEX.sub("", md)
    md = DUP_H1.sub("", md, count=1)
    md = REF_LINE.sub("", md)
    md = FOOTER.sub("", md)
    return md.strip()


def translate_line(line: str) -> str:
    if line in HEADING_ZH:
        return HEADING_ZH[line]
    out = line
    for en, zh in sorted(PHRASE_ZH.items(), key=lambda x: -len(x[0])):
        if en and en in out:
            out = out.replace(en, zh)
    for en, zh in HEADING_ZH.items():
        if en.startswith("<") or en.startswith("  ") or en.startswith("\\"):
            if en in out:
                out = out.replace(en, zh)
    if '<p class="x2mdx-ref-card-summary">' in out:
        for en, zh in INDEX_CARD_SUMMARY.items():
            out = out.replace(f">{en}</p>", f">{zh}</p>")
    return out


CARD_INLINE = {
    '<Card title="Lifecycle">': '<Card title="生命周期">',
    '<Card title="Notices">': '<Card title="通知">',
    "    Stable.": "    稳定。",
    "    Status: `active`": "    状态：`active`",
    "    Introduced in: `3.4.9`": "    引入版本：`3.4.9`",
    "    Removed in: `-`": "    移除版本：`-`",
    "    Warnings: `0`": "    警告数：`0`",
    "    Deprecations: `0`": "    弃用数：`0`",
    "    Deprecated since: `-`": "    弃用自：`-`",
    r"  \| Field \| Type \| Description \|": r"  | 字段 | 类型 | 说明 |",
}


def translate_body(text: str) -> str:
    parts = re.split(r"(```[\s\S]*?```|<(?:Warning|Note)[\s\S]*?</(?:Warning|Note)>|<div[\s\S]*?</div>)", text)
    out: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("```") or part.startswith("<"):
            out.append(part)
            continue
        lines = [translate_line(ln) for ln in part.split("\n")]
        out.append("\n".join(lines))
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    for en, zh in CARD_INLINE.items():
        body = body.replace(en, zh)
    return body.strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug in BATCH13:
        zh_title, summary, intro = META[slug]
        en = strip_en((EN / f"{slug}.md").read_text(encoding="utf-8"))
        body = intro + translate_body(en)
        path = OUT / f"{slug}.json"
        path.write_text(
            json.dumps({"zhTitle": zh_title, "summary": summary, "body": body}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        count += 1
        print(f"wrote {slug} ({len(body)} chars)")
    print(f"batch13 count: {count}")


if __name__ == "__main__":
    main()
