---
title: "DA.Time"
slug: "appdev-reference-daml-standard-library-da-time"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-time.md"
source_title: "DA.Time"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-time
---

# DA.Time

> Daml 模块 DA.Time 参考文档

# DA.Time

<span id="module-da-time-32716" />

# DA.Time

本模块提供操作 Time 值的函数集。

`Time` 表示 UTC 下的具体日期时间，

例如 `time (date 2007 Apr 5) 14 30 05`。

Time 范围为 0001-01-01T00:00:00.000000Z 至

9999-12-31T23:59:59.999999Z。

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

## 数据类型

<span id="type-da-time-types-reltime-23082" />

### `data RelTime`

`RelTime` 表示时间偏移（相对时间）。

实例：

* `instance Eq RelTime`
* `instance Ord RelTime`
* `instance Bounded RelTime`
* `instance Additive RelTime`
* `instance Signed RelTime`
* `instance Show RelTime`

## 函数

<span id="function-da-internal-time-time-34667" />

### `time`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
time : Date -> Int -> Int -> Int -> Time
```

`time d h m s` 将 UTC 日期 `d` 与 UTC 时分秒转为 `Time`；不处理闰秒。

<span id="function-da-time-addreltime-70617" />

### `addRelTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
addRelTime : Time -> RelTime -> Time
```

用给定偏移调整 `Time`。

<span id="function-da-time-subtime-47226" />

### `subTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subTime : Time -> Time -> RelTime
```

返回两时刻的时间差。

<span id="function-da-time-wholedays-91725" />

### `wholeDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wholeDays : RelTime -> Int
```

返回偏移中的整天数；小数部分向零取整。

<span id="function-da-time-days-58759" />

### `days`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
days : Int -> RelTime
```

相对时间中的天数。

<span id="function-da-time-hours-54068" />

### `hours`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
hours : Int -> RelTime
```

相对时间中的小时数。

<span id="function-da-time-minutes-72520" />

### `minutes`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minutes : Int -> RelTime
```

相对时间中的分钟数。

<span id="function-da-time-seconds-68512" />

### `seconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
seconds : Int -> RelTime
```

相对时间中的秒数。

<span id="function-da-time-milliseconds-28552" />

### `milliseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
milliseconds : Int -> RelTime
```

相对时间中的毫秒数。

<span id="function-da-time-microseconds-56941" />

### `microseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
microseconds : Int -> RelTime
```

相对时间中的微秒数。

<span id="function-da-time-convertreltimetomicroseconds-23127" />

### `convertRelTimeToMicroseconds`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
convertRelTimeToMicroseconds : RelTime -> Int
```

将 RelTime 转为微秒
优先使用高层函数而非内部微秒 API

<span id="function-da-time-convertmicrosecondstoreltime-73643" />

### `convertMicrosecondsToRelTime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
convertMicrosecondsToRelTime : Int -> RelTime
```

将微秒转为 RelTime
优先使用高层函数而非内部微秒 API

<span id="function-da-time-isledgertimelt-78120" />

### `isLedgerTimeLT`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeLT : Time -> Update Bool
```

当且仅当交易的账本时间小于给定时间时为 True。

<span id="function-da-time-isledgertimele-50101" />

### `isLedgerTimeLE`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeLE : Time -> Update Bool
```

当且仅当交易的账本时间小于等于给定时间时为 True。

<span id="function-da-time-isledgertimegt-6233" />

### `isLedgerTimeGT`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeGT : Time -> Update Bool
```

当且仅当交易的账本时间大于给定时间时为 True。

<span id="function-da-time-isledgertimege-95212" />

### `isLedgerTimeGE`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLedgerTimeGE : Time -> Update Bool
```

当且仅当交易的账本时间大于等于给定时间时为 True。

## 孤立类型类实例

* `instance Eq RelTime`

* `instance Ord RelTime`

* `instance Show RelTime`

* `instance Additive RelTime`

* `instance Signed RelTime`

* `instance Bounded RelTime`

* `instance Bounded Time`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
