---
title: "DA.Date"
slug: "appdev-reference-daml-standard-library-da-date"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-date.md"
source_title: "DA.Date"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-date
---

# DA.Date

> Daml 标准库模块 DA.Date 参考文档。

<span id="module-da-date-80009" />

# DA.日期

该模块提供了一组操作日期值的函数。

日期的界限是 0001-01-01T00:00:00.000000Z 和

9999-12-31T23:59:59.999999Z。

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Stable.
  </Card>

  <Card title="Notices">
    状态：`active`
    引入于：`3.4.9`
    删除于：`-`
    警告：`0`
    弃用：`0`
    已弃用自：`-`
  </Card>
</CardGroup>

## 数据类型

<span id="type-da-date-types-dayofweek-18120" />

### `data DayOfWeek`

构造函数：

<span id="constr-da-date-types-monday-43349" />

* `Monday`

<span id="constr-da-date-types-tuesday-5501" />

* `Tuesday`

<span id="constr-da-date-types-wednesday-18786" />

* `Wednesday`

<span id="constr-da-date-types-thursday-55301" />

* `Thursday`

<span id="constr-da-date-types-friday-14884" />

* `Friday`

<span id="constr-da-date-types-saturday-99714" />

* `Saturday`

<span id="constr-da-date-types-sunday-48181" />

* `Sunday`

实例：

* `instance Eq DayOfWeek`
* `instance Ord DayOfWeek`
* `instance Bounded DayOfWeek`
* `instance Enum DayOfWeek`
* `instance Show DayOfWeek`

<span id="type-da-date-types-month-22803" />

### `data Month`

`Month` 类型代表公历中的月份。

请注意，虽然`Month`有一个`Enum`实例，但`toEnum`和`fromEnum`
函数从 0 开始计数，即 `toEnum 1 :: Month` 是 `Feb`。

构造函数：

<span id="constr-da-date-types-jan-1103" />

* `Jan`

<span id="constr-da-date-types-feb-88523" />

* `Feb`

<span id="constr-da-date-types-mar-5472" />

* `Mar`

<span id="constr-da-date-types-apr-12091" />

* `Apr`

<span id="constr-da-date-types-may-50999" />

* `May`

<span id="constr-da-date-types-jun-17739" />

* `Jun`

<span id="constr-da-date-types-jul-21893" />

* `Jul`

<span id="constr-da-date-types-aug-18125" />

* `Aug`

<span id="constr-da-date-types-sep-63548" />

* `Sep`

<span id="constr-da-date-types-oct-96134" />

* `Oct`

<span id="constr-da-date-types-nov-72317" />

* `Nov`

<span id="constr-da-date-types-dec-74760" />

* `Dec`

实例：

* `instance Eq Month`
* `instance Ord Month`
* `instance Bounded Month`
* `instance Enum Month`
* `instance Show Month`

## 函数

<span id="function-da-date-adddays-7836" />

### `addDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
addDays : Date -> Int -> Date
```

将给定的天数添加到日期中。

<span id="function-da-date-subtractdays-16626" />

### `subtractDays`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subtractDays : Date -> Int -> Date
```

从日期中减去给定的天数。

`subtractDays d r`相当于`addDays d (- r)`。

<span id="function-da-date-subdate-25598" />

### `subDate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
subDate : Date -> Date -> Int
```

返回两个给定日期之间的天数。

<span id="function-da-date-dayofweek-99931" />

### `dayOfWeek`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dayOfWeek : Date -> DayOfWeek
```

返回给定日期是星期几。

<span id="function-da-date-fromgregorian-85346" />

### `fromGregorian`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromGregorian : (Int, Month, Int) -> Date
```

从三元组`(year, month, days)`构造一个`Date`。

<span id="function-da-date-togregorian-84541" />

### `toGregorian`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toGregorian : Date -> (Int, Month, Int)
```

将 `Date` 值转换为 `(year, month, day)` 三倍，根据
到公历。

<span id="function-da-date-date-21355" />

### `date`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
date : Int -> Month -> Int -> Date
```

给定三个值（年、月、日），构造一个 `Date` 值。
`date y m d` 将年 `y`、月 `m` 和日 `d` 转换为 `Date` 值。
如果 `d` 超出范围 `1 .. monthDayCount y m`，则会引发错误。

<span id="function-da-date-isleapyear-61920" />

### `isLeapYear`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLeapYear : Int -> Bool
```

如果给定年份是闰年，则返回 `True`。

<span id="function-da-date-frommonth-90328" />

### `fromMonth````haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromMonth : Month -> Int
```

获取给定月份对应的数字。例如`Jan`对应
`1`，`Feb`对应`2`，依此类推。

<span id="function-da-date-monthdaycount-59295" />

### `monthDayCount`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
monthDayCount : Int -> Month -> Int
```

根据公历获取给定年份中给定月份的天数。
这没有考虑历史日历更改（例如，
从儒略历改为公历），但确实计算闰年。

<span id="function-da-date-datetime-90284" />

### `datetime`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
datetime : Int -> Month -> Int -> Int -> Int -> Int -> Time
```

使用 `year`、`month`、`day`、`hours`、`minutes`、`seconds` 构造一个实例。

<span id="function-da-date-todateutc-87953" />

### `toDateUTC`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toDateUTC : Time -> Date
```

从 UTC 时间提取 UTC 日期。

此函数将截断“Time to Date”，但在许多情况下它不会返回您真正想要的日期。
原因是，通常 Time 的来源是 getTime，而 getTime 返回 UTC，并且很可能
您想要的日期是某个地点或交易所的本地日期。因此，以这种方式检索的日期将是
昨天如果在新加坡开市时检索。

## 孤立类型类实例

* `instance Eq DayOfWeek`

* `instance Ord DayOfWeek`

* `instance Show DayOfWeek`

* `instance Enum DayOfWeek`

* `instance Bounded DayOfWeek`

* `instance Eq Month`

* `instance Ord Month`

* `instance Show Month`

* `instance Enum Month`

* `instance Bounded Month`

* `instance Enum Date`

* `instance Bounded Date`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
