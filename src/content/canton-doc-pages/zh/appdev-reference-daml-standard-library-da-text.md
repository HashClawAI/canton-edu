---
title: "DA.Text"
slug: "appdev-reference-daml-standard-library-da-text"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-text.md"
source_title: "DA.Text"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-text
---

# DA.Text

> Daml 模块 DA.Text 参考文档

# DA.Text

<span id="module-da-text-83238" />

# DA.Text

操作 Text 的函数。

## 模块快照

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="通知">
    状态：`active`
    引入版本：`3.4.9`
    移除版本：`-`
    警告数：`0`
    弃用数：`0`
    弃用自：`-`
  </Card>
</CardGroup>

## 函数

<span id="function-da-text-explode-24206" />

### `explode`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
explode : Text -> [Text]
```

<span id="function-da-text-implode-82253" />

### `implode`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
implode : [Text] -> Text
```

<span id="function-da-text-isempty-39554" />

### `isEmpty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isEmpty : Text -> Bool
```

测试是否为空。

<span id="function-da-text-isnotempty-43984" />

### `isNotEmpty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isNotEmpty : Text -> Bool
```

测试是否非空。

<span id="function-da-text-length-94326" />

### `length`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
length : Text -> Int
```

计算文本中的符号数。

<span id="function-da-text-trim-11808" />

### `trim`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
trim : Text -> Text
```

去除给定文本两端的空格。

<span id="function-da-text-replace-9445" />

### `replace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replace : Text -> Text -> Text -> Text
```

在全文替换子串；第一个参数
不能为空。

<span id="function-da-text-lines-25154" />

### `lines`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lines : Text -> [Text]
```

在换行符处将 `Text` 拆成 `Text` 列表；
结果不含换行符。

<span id="function-da-text-unlines-66467" />

### `unlines`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unlines : [Text] -> Text
```

连接各行，并在每行末尾追加换行符。

<span id="function-da-text-words-34636" />

### `words`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
words : Text -> [Text]
```

按空白符号将 Text 拆成单词列表。

<span id="function-da-text-unwords-40113" />

### `unwords`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unwords : [Text] -> Text
```

用单个空格连接单词。

<span id="function-da-text-linesby-11211" />

### `linesBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
linesBy : (Text -> Bool) -> Text -> [Text]
```

`lines` 的变体，使用自定义分隔测试；
末尾分隔符会被丢弃。

<span id="function-da-text-wordsby-15461" />

### `wordsBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wordsBy : (Text -> Bool) -> Text -> [Text]
```

`words` 的变体，使用自定义分隔测试；
相邻及首尾分隔符均会被丢弃。

<span id="function-da-text-intercalate-63059" />

### `intercalate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intercalate : Text -> [Text] -> Text
```

`intercalate` 在 `ts` 各项之间插入 `t` 并拼接。

<span id="function-da-text-dropprefix-62361" />

### `dropPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropPrefix : Text -> Text -> Text
```

`dropPrefix` 去掉给定前缀；若无此前缀则返回原文。

<span id="function-da-text-dropsuffix-37682" />

### `dropSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropSuffix : Text -> Text -> Text
```

去掉给定后缀；若无此后缀则返回原文。
示例：

```
  dropSuffix "!" "Hello World!"  == "Hello World"
  dropSuffix "!" "Hello World!!" == "Hello World!"
  dropSuffix "!" "Hello World."  == "Hello World."
```

<span id="function-da-text-stripsuffix-58624" />

### `stripSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripSuffix : Text -> Text -> Optional Text
```

若第二段文本的后缀与第一段完全匹配，则返回其前缀。
示例：

```
  stripSuffix "bar" "foobar" == Some "foo"
  stripSuffix ""    "baz"    == Some "baz"
  stripSuffix "foo" "quux"   == None
```

<span id="function-da-text-stripprefix-74987" />

### `stripPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripPrefix : Text -> Text -> Optional Text
```

`stripPrefix` 去掉给定前缀；
若文本不以该前缀开头则返回 `None`。

<span id="function-da-text-isprefixof-82357" />

### `isPrefixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isPrefixOf : Text -> Text -> Bool
```

`isPrefixOf` 判断第一段是否为第二段的前缀。

<span id="function-da-text-issuffixof-35218" />

### `isSuffixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSuffixOf : Text -> Text -> Bool
```

`isSuffixOf` 判断第一段是否为第二段的后缀。

<span id="function-da-text-isinfixof-98358" />

### `isInfixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isInfixOf : Text -> Text -> Bool
```

`isInfixOf` 判断第一段是否完整出现在第二段中。

<span id="function-da-text-takewhile-40431" />

### `takeWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhile : (Text -> Bool) -> Text -> Text
```

`takeWhile p t` 返回 `t` 中最长前缀（可为空），
其中符号均满足 `p`。

<span id="function-da-text-takewhileend-32455" />

### `takeWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhileEnd : (Text -> Bool) -> Text -> Text
```

`takeWhileEnd p t` 返回 `t` 中最长后缀（可为空），
其中符号均满足 `p`。

<span id="function-da-text-dropwhile-46373" />

### `dropWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhile : (Text -> Bool) -> Text -> Text
```

`dropWhile p t` 为 `takeWhile p t` 之后的后缀。

<span id="function-da-text-dropwhileend-2917" />

### `dropWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhileEnd : (Text -> Bool) -> Text -> Text
```

`dropWhileEnd p t` 为从末尾去掉满足 `p` 的符号后剩余的前缀。

<span id="function-da-text-spliton-44082" />

### `splitOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitOn : Text -> Text -> [Text]
```

用第一个文本（不可为空）作分隔符拆分，并消耗分隔符。

<span id="function-da-text-splitat-25614" />

### `splitAt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitAt : Int -> Text -> (Text, Text)
```

在指定位置拆分，使得对 `0 <= n <= length t`，
`length (fst (splitAt n t)) == n`。

<span id="function-da-text-take-27133" />

### `take`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
take : Int -> Text -> Text
```

`take n t` 返回长度为 `n` 的前缀；若 `n` 大于长度则返回 `t`。

<span id="function-da-text-drop-34163" />

### `drop`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
drop : Int -> Text -> Text
```

`drop n t` 返回去掉前 `n` 个字符后的后缀；
若 `n` 大于长度则返回空 `Text`。

<span id="function-da-text-substring-36270" />

### `substring`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substring : Int -> Int -> Text -> Text
```

从参数文本的位置 `s` 起取长度为 `l` 的符号序列。

<span id="function-da-text-ispred-73747" />

### `isPred`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isPred : (Text -> Bool) -> Text -> Bool
```

`isPred f t` 在 `t` 非空且 `t` 中所有符号满足 `f` 时为 `True`。

<span id="function-da-text-isspace-72803" />

### `isSpace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSpace : Text -> Bool
```

`isNewLine t` 在 `t` 非空且仅含换行符时为 `True`。

<span id="function-da-text-isnewline-85831" />

### `isNewLine`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isNewLine : Text -> Bool
```

`isNewLine t` 在 `t` 非空且仅含换行符时为 `True`。

<span id="function-da-text-isupper-58977" />

### `isUpper`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUpper : Text -> Bool
```

`isUpper t` 在 `t` 非空且仅含大写符号时为 `True`。

<span id="function-da-text-islower-60966" />

### `isLower`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLower : Text -> Bool
```

`isLower t` 在 `t` 非空且仅含小写符号时为 `True`。

<span id="function-da-text-isdigit-15622" />

### `isDigit`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isDigit : Text -> Bool
```

`isDigit t` 在 `t` 非空且仅含数字符号时为 `True`。

<span id="function-da-text-isalpha-72233" />

### `isAlpha`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isAlpha : Text -> Bool
```

`isAlpha t` 在 `t` 非空且仅含字母符号时为 `True`。

<span id="function-da-text-isalphanum-87978" />

### `isAlphaNum`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isAlphaNum : Text -> Bool
```

`isAlphaNum t` 在 `t` 非空且仅含字母数字符号时为 `True`。

<span id="function-da-text-parseint-736" />

### `parseInt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseInt : Text -> Optional Int
```

尝试从 `Text` 解析 `Int`。

<span id="function-da-text-parsenumeric-9858" />

### `parseNumeric`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseNumeric : NumericScale n => Text -> Optional (Numeric n)
```

尝试从 `Text` 解析 `Numeric`。
要得到 `Some`，文本须匹配正则
`(-|\+)?[0-9]+(\.[0-9]+)?`
简写 `".12"`、`"12."` 无效，
但可用 `+` 前缀。
首尾零可以，但不可含空格。
示例：

```
  parseNumeric "3.14" == Some 3.14
  parseNumeric "+12.0" == Some 12
```

<span id="function-da-text-parsedecimal-57278" />

### `parseDecimal`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseDecimal : Text -> Optional Decimal
```

尝试从 `Text` 解析 `Decimal`。
要得到 `Some`，文本须匹配正则
`(-|\+)?[0-9]+(\.[0-9]+)?`
简写 `".12"`、`"12."` 无效，
但可用 `+` 前缀。
首尾零可以，但不可含空格。
示例：

```
  parseDecimal "3.14" == Some 3.14
  parseDecimal "+12.0" == Some 12
```

<span id="function-da-text-sha256-29291" />

### `sha256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sha256 : Text -> Text
```

对 `Text` 的 UTF-8 字节计算 SHA256，并以小写十六进制返回。

若编译目标为 Daml-LF < 1.2，此函数会在运行时崩溃。

<span id="function-da-text-reverse-37387" />

### `reverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverse : Text -> Text
```

反转 `Text`。

```
  reverse "Daml" == "lmaD"
```

<span id="function-da-text-tocodepoints-44801" />

### `toCodePoints`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toCodePoints : Text -> [Int]
```

将 `Text` 转为 Unicode 码点序列。

<span id="function-da-text-fromcodepoints-94464" />

### `fromCodePoints`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromCodePoints : [Int] -> Text
```

将 Unicode 码点序列转为 `Text`；无效码点会抛异常。

<span id="function-da-text-asciitolower-24557" />

### `asciiToLower`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asciiToLower : Text -> Text
```

将 `Text` 中的 ASCII 大写转为小写；
其他字符不变。

<span id="function-da-text-asciitoupper-96826" />

### `asciiToUpper`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asciiToUpper : Text -> Text
```

将 `Text` 中的 ASCII 小写转为大写；
其他字符不变。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
