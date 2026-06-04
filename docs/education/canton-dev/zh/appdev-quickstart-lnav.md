---
title: "使用 lnav 调试"
slug: "appdev-quickstart-lnav"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/lnav.md"
source_title: "Debugging with lnav"
tags:
  - appdev
  - quickstart
  - lnav
---

# 使用 lnav 调试

> 使用 lnav 交互式检查 Canton quickstart 日志。

# 使用 lnav 调试

# 使用 lnav 调试与排障

## 快速入门

`lnav` 是日志查看与导航工具，用于查看、搜索、过滤与分析日志。本节帮助你在 LocalNet 上快速将 `lnav` 用于 CN 应用开发；截图与说明基于 `lnav 0.13.1`。

### lnav 下载与文档

在 [lnav 下载页](https://lnav.org/downloads) 下载对应系统版本。

用 `which lnav` 查看路径，用 `lnav --version` 查看版本。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-version.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=3940cc5358b11329063fd81c44997682" alt="lnav version" width="270" height="61" data-path="images/docs_website/lnav-version.png" />

若不熟悉 lnav，请阅读其[文档](https://docs.lnav.org/)。

### 安装 Canton lnav 格式

Canton Network 提供自定义 `lnav` 配置以分析 Canton 日志；JSON 配置位于 Hyperledger Labs Splice 开源仓库，可阅读 schema 了解字段与日志结构。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-hyperledger-labs.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=01a2a8eeb18e9fefd52a651d622172fb" style={{width: "60.0%"}} alt="Splice lnav format" width="1600" height="1262" data-path="images/docs_website/lnav-hyperledger-labs.png" />

`splice/canton/canton-json.lnav.json`

下载并安装配置供 `lnav` 使用：

curl -L [https://raw.githubusercontent.com/canton-network/splice/main/canton/canton-json.lnav.json](https://raw.githubusercontent.com/canton-network/splice/main/canton/canton-json.lnav.json) -o /tmp/canton-json.lnav.json && lnav -i /tmp/canton-json.lnav.json

现在可用 `lnav` 浏览 CN 日志。

## 采集 Quickstart 日志

在 `quickstart/` 目录运行 `make capture-logs` 采集所有 quickstart 容器日志；让该终端在后台运行，再在另一终端 `make start` 启动容器。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-make-capture-logs.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=7d86cdca5e63763640d259c8e97cbe95" style={{width: "25.0%"}} alt="Capture logs" width="794" height="156" data-path="images/docs_website/lnav-make-capture-logs.png" />

在终端 1 启动 `make capture-logs`

## 查找日志

容器运行时在 `logs/` 目录生成日志；用 `ls logs` 查看。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-ls-logs.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=780d2f46ee8d672ad11e45e47d7334e8" style={{width: "55.0%"}} alt="List logs" width="864" height="184" data-path="images/docs_website/lnav-ls-logs.png" />

## Canton 日志

“c-log”（`clog`）为采用 Canton 自定义格式的日志，多用于 Canton、Splice 等长运行服务；标准日志文件通常来自初始化脚本与工具。

在 `quickstart/` 运行 `lnav logs/*.clog` 实时查看（按 q 或输入 `:quit` 退出）

clogs 显示来自 Canton、Splice 与后端服务的实时日志流。

## 浏览事件

在终端于 `quickstart/` 运行 `make create-app-install-request` 创建可追踪的业务事件。

回到 `lnav`，按 “=” 暂停/继续流。

### 搜索事件

输入 `/AppInstallRequest` 搜索。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-app-install-request-event.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=e857be75050b5f6c71720f40ee084b40" alt="lnav app install request event" width="1517" height="221" data-path="images/docs_website/lnav-app-install-request-event.png" />

Use “n” and “shift + N” to jump through entries containing “AppInstallRequest”. “>” and “\<” scroll horizontally across long entries.

按 Shift+G 跳到最新条目；若未暂停将恢复实时流。

### 过滤事件

用 `:filter-in AppInstallRequest` 仅显示相关事件。

与搜索高亮不同，`:filter-in` 仅显示包含目标信息的条目。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-filter-in-app-install-request.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=35442029d006b7a22bfa3c1c0eeb1abd" alt="lnav filter-in app install request" width="1612" height="111" data-path="images/docs_website/lnav-filter-in-app-install-request.png" />

### 清除 filter-in

用 `:reset-session` 恢复完整流；若空白则 q 退出后重新 `lnav logs/*.clog`。

### 生成可分析事件

在 Quickstart 应用中完成一次完整业务操作以生成可分析事件。

### 快速工作流摘要

1. 在 `localhost:3000` 以 `app-provider` 登录
2. 接受安装请求
3. 创建许可
4. 发出许可续期请求
5. 以 `app-user` 登录并在 Canton 钱包付款
6. 接受并分配续期付款
7. 以 `app-provider` 回到应用完成续期

分步截图说明见 `quickstart-explore-the-demo`。

## 按 Trace ID 搜索

日志含 OpenTelemetry [trace](https://opentelemetry.io/docs/concepts/signals/traces/) 标识（trace-id），便于跨容器关联同一操作。

### 查找 Trace ID

用 `:filter-in listLicenses` 查找；Trace ID 为括号内字符串。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-filter-in-listlicenses.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=2c6c0f4e5cc38bd67594ea0c42962139" alt="trace id filtering" width="1375" height="143" data-path="images/docs_website/lnav-filter-in-listlicenses.png" />

选择并复制任一 Trace ID。

例如 “835a02159672310b58c2b106b482654d”

<Warning>
  你的 trace ID 唯一，复制示例将无结果。
</Warning>

### 按 Trace ID 过滤

过滤仅显示该 Trace ID 相关日志：

:reset-session
:filter-in 835a02159672310b58c2b106b482654d

现在可查看处理该请求的所有容器日志。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-trace-id.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=acf0e5aa3022bbfb7f98f9027ef57065" alt="lnav trace id" width="1439" height="111" data-path="images/docs_website/lnav-trace-id.png" />

也可不过滤而直接搜索 trace ID：

:reset-session
/0f23f6d54af3176a6d4c904ed66e8702

这会高亮所有出现位置而不隐藏其他日志。

过滤（`:filter-in`）— 仅关注单一操作；搜索（`/`）— 保留上下文。

## lnav 进阶

「快速入门」与「采集日志」介绍基础用法；本节介绍开发期监控 CN 应用的进阶功能。

Integrate `lnav` into your workflow:

* **开发**：构建功能时监控行为，验证 Daml 合约与工作流，尽早发现问题。
* **调试**：跨 Canton、Splice、后端追踪操作，用 trace ID 理解失败操作全生命周期，过滤无关噪声。
* **排障**：快速定位错误与警告，搜索操作、合约 ID、party，分析异常事件序列。

有效阅读与分析日志对构建稳健 CN 应用至关重要；复杂度上升时 `lnav` 是理解系统行为与排障的利器。

## 进一步探索 lnav clogs

下文帮助熟悉 `lnav`，请在 `lnav` 中练习下列操作。

Press “g” on the keyboard to go to the top of the logs. “Shift + g” takes you to the end of the logs and reinitiates the stream.

按 = 暂停/继续。

左方向键查看日志来源文件。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-view-log-origination.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=c0480052cad051318c460d50f8694a73" alt="lnav file origin" width="940" height="345" data-path="images/docs_website/lnav-view-log-origination.png" />

右方向键查看日志条目。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-view-log-entry.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=d98c9212305ef2d769da4d9da5ddc834" alt="lnav log entry" width="1386" height="244" data-path="images/docs_website/lnav-view-log-entry.png" />

Shift+左右方向键小幅移动视图。

Use “x” to expand and collapse information within the square brackets after the date.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-collapse-expand-metadata.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=22e9c60fb7e7d402d063470ec71dfffa" alt="expand collapse lnav metadata" width="860" height="306" data-path="images/docs_website/lnav-collapse-expand-metadata.png" />

Ctrl+x 切换光标行模式。

## 标记与复制行

* 用 m 标记行
* 用 c 标记并复制到剪贴板
* m 与 c 便于分享关注条目
* Shift+J 复制后续行
* Shift+K 取消后续标记
* u / Shift+U 在标记行间跳转
* Shift+C 清除所有标记

## 查找错误、警告与 trace ID

* e / Shift+E 在错误间跳转
* w / Shift+W 在警告间跳转
* o / Shift+O 在 traceId（opId）间跳转

## 时间

Shift+T 切换时间标记，以选中项为时间中心；数字越小越接近事件（秒）。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-time-toggle.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=126dab7bc274b32fdf1b15ec445c18dc" alt="lnav time toggle" width="512" height="42" data-path="images/docs_website/lnav-time-toggle.png" />

## 命令模式

命令模式（输入 :）可精确控制导航、过滤与分析，便于隔离 trace ID、按组件过滤或缩小时间窗。

Enter command mode with the colon key, “:” then type your desired command.

To scroll through command history, press “:” followed by the up arrow.

A small selection of available commands are showcased in the Appendix section below. Read the `lnav` documentation for a full list of available [commands](https://docs.lnav.org/en/latest/commands.html).

### 帮助

用 `:help` 或 ? 查看命令详情；q 或 ? 退出帮助。

## 修剪日志

有时需清理日志，可执行：

docker rm -f \$(docker ps -qa); docker system prune -f; docker volume prune -f; rm -r logs; mkdir logs

执行后需 `make start` 恢复运行。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-prune-logs.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=fc55b9e72ca88bfc8eaef0d69edb134b" alt="lnav prune logs" width="267" height="311" data-path="images/docs_website/lnav-prune-logs.png" />

## 排障

若 `lnav` 崩溃可能终止 capture-logs 并清空 `logs/`。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/lnav-troubleshooting.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=2b3e2fec9469cf622627cfec01feffc2" alt="lnav troubleshooting" width="512" height="216" data-path="images/docs_website/lnav-troubleshooting.png" />

重建 `logs/` 与 `*.clogs`：在 `quickstart/` 执行 `make stop && make clean-all` 后 `make start`。

## 附录

### 关联机制

Canton Network 日志含多种关联与过滤字段：

* `level` — 日志级别
* `logger_name` — 组件标识
* `message` — 消息内容
* `trace-id` — OpenTelemetry trace
* `span-id` — span 标识
* `span-parent-id` — span 层级链接
* `span-name` — 操作名
* `@timestamp` — 时间戳

示例说明各关联字段：

2025-10-09T22:03:41.702-0500 \[⋮] DEBUG - ⋮ (---) - ⋮

* 时间戳：`2025-10-09T22:03:41.702-0500`
* Collapsed metadata including the thread\_name: `[⋮]`
* 级别：`DEBUG`
* 分隔符：`-`
* 更多折叠：`⋮`
* 无活跃 trace：`(---)`

2025-10-09T22:22:08.976-0500 \[⋮] DEBUG - ⋮ (846ff12a35f6e8b61171039527934709-SvOffboardingSequencerTrigger--6aaa9f37e9ae78c4) - ⋮

* Trace ID：`846ff12a35f6e8b61171039527934709`
* Span 名：`SvOffboardingSequencerTrigger`
* Span ID：`6aaa9f37e9ae78c4`

2025-10-09T22:22:08.978-0500 \[⋮] DEBUG - ⋮ (2a2f0baca0ce4452d713a30d9a5bcb7d---) - Request com.digitalasset.canton.topology.admin.v30.TopologyManagerReadService/ListSequencerSynchronizerState by /172.18.0.22:43954: received a message

* Trace ID: `2a2f0baca0ce4452d713a30d9a5bcb7d`
* 日志消息：`Request ... received a message`
* 三个连字符 `---` 表示无 span-name 与 span-id。
* 格式见上一示例。

### 高级过滤

#### 常用字段参考

下列结构化字段可用于 `lnav` 过滤表达式。

#### 按严重程度过滤

:filter-in level = 'ERROR'
:filter-out level = 'DEBUG'

#### 按组件过滤

:filter-in logger\_name =\~ '.*sequencer.*'
:filter-in logger\_name =\~ '.*participant1.*'

#### 按 Trace 过滤

:filter-in trace-id = '2a2f0baca0ce4452d713a30d9a5bcb7d'
:filter-in span-name =\~ '.*Transfer.*'

#### 按时间范围过滤

:filter-in @timestamp >= '2024-01-01 10:00:00'
:filter-in @timestamp \< '2024-01-01 11:00:00'

#### 按内容过滤

:filter-out message =\~ 'health.\*check'
:filter-in message =\~ 'license'

### 隐藏行

可用下列命令隐藏匹配行：

* `:hide-lines-before` 隐藏指定日期之前的行
* `:hide-lines-after` 隐藏指定日期之后的行
* `:hide-fields` 隐藏每行特定字段

可隐藏 `logger_name`、`thread_name`、`trace-id`、`level` 等，可同时隐藏多个。

例如隐藏 `thread_name` 与 `level`：

`:hide-fields thread_name level`

#### 隐藏行 before

​​# Hide logs before a specific time
`:hide-lines-before 2025-10-10 14:30:00`

# Hide logs before the last hour

`:hide-lines-before -1h`

# Hide logs before a specific line number

`:hide-lines-before 1000`

#### 隐藏行 after

# Hide logs after a specific time

:hide-lines-after 2025-10-10 16:00:00

# Hide logs after a specific duration from start

:hide-lines-after +2h

# Hide logs after line 5000

:hide-lines-after 5000

#### 显示行

* `:show-lines-before` shows lines that were previously hidden before a specific time, duration, or line number.
* `:show-lines-after` shows lines that were previously hidden after a specific time, duration, or line number.

### 将日志打包到目录

在 `quickstart/` 按系统打包 `logs/`：

`tar -czf my-cn-logs.tar.gz logs/`

`zip -r my-cn-logs.zip logs/`

### 常用 lnav 快捷键

快捷键见 [lnav 热键参考](https://docs.lnav.org/en/latest/hotkeys.html)。

#### 导航

* j/k 或 ↓/↑ — 上下移动
* J/K — 选择/取消后续条目
* 空格/b — 翻页
* g/G — 顶/底
* n/N — 上/下条搜索结果

#### 搜索与过滤

* / — 向前搜索
* ? — 帮助
* f — 设置过滤表达式
* F — 清除过滤
* t — 仅错误/警告
* T — 清除错误过滤

#### 时间 Navigation

* 7/8 — 跳到整点
* Shift+T — 切换时间视图

#### 显示

* v — 切换日志视图
* Tab — 切换文件与文本过滤菜单
* i — 显示/隐藏信息消息
* p — 切换美化打印

#### 书签

* m — 设书签
* u/U — 上/下书签

#### 其他

* q — 退出
* ? - Help (shows all shortcuts)

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
