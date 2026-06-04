---
title: "DA.Tuple"
slug: "appdev-reference-daml-standard-library-da-tuple"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-tuple.md"
source_title: "DA.Tuple"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-tuple
---

# DA.Tuple

> Daml 模块 DA.Tuple 参考文档

# DA.Tuple

<span id="module-da-tuple-81988" />

# DA.Tuple

Tuple——元组的常用函数。

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

<span id="function-da-tuple-first-48871" />

### `first`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
first : (a -> a') -> (a, b) -> (a', b)
```

对二元组第一分量应用函数得到的新二元组。

<span id="function-da-tuple-second-48360" />

### `second`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
second : (b -> b') -> (a, b) -> (a, b')
```

对二元组第一分量应用函数得到的新二元组。
对二元组第二分量应用函数得到的新二元组。

<span id="function-da-tuple-both-63511" />

### `both`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
both : (a -> b) -> (a, a) -> (b, b)
```

对二元组第一分量应用函数得到的新二元组。
对二元组两个分量应用同一函数。

<span id="function-da-tuple-swap-76115" />

### `swap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
swap : (a, b) -> (b, a)
```

交换二元组两个分量的顺序。

<span id="function-da-tuple-dupe-14430" />

### `dupe`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dupe : a -> (a, a)
```

将单个值复制为二元组。

> dupe 12 == (12, 12)

<span id="function-da-tuple-fst3-84676" />

### `fst3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fst3 : (a, b, c) -> a
```

取三元组第一分量。

<span id="function-da-tuple-snd3-63950" />

### `snd3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
snd3 : (a, b, c) -> b
```

取三元组第二分量。

<span id="function-da-tuple-thd3-58697" />

### `thd3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
thd3 : (a, b, c) -> c
```

取三元组第三分量。

<span id="function-da-tuple-curry3-2900" />

### `curry3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
curry3 : ((a, b, c) -> d) -> a -> b -> c -> d
```

将非柯里化函数转为柯里化函数。

<span id="function-da-tuple-uncurry3-51859" />

### `uncurry3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry3 : (a -> b -> c -> d) -> (a, b, c) -> d
```

将柯里化函数转为接受三元组的函数。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
