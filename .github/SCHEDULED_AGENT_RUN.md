# Scheduled agent run — canton-edu（定时 Agent → 摘要 → 人工上线）

## 主路径：Cursor Automation（推荐）

两条 Automation 分工（**先合并、后扫描**）：

| 时间 (GMT+8) | 文档 | 作用 |
|--------------|------|------|
| **08:00** | [canton-edu-daily-8am-pr-merge-gmt8.md](./automations/canton-edu-daily-8am-pr-merge-gmt8.md) | 审查 open PR → **squash merge**（去重 content PR） |
| **08:15** | [canton-edu-daily-8am-gmt8.md](./automations/canton-edu-daily-8am-gmt8.md) | 全站扫描 → **有增量才开 PR** |

### 创建 PR 合并 Automation（08:00）

1. [cursor.com/automations](https://cursor.com/automations) → **New automation**
2. Name：`canton-edu daily PR review → merge`
3. Schedule：`0 8 * * *`，Timezone：`Asia/Shanghai`
4. Repository：`HashClawAI/canton-edu`
5. Prompt：复制 [canton-edu-daily-8am-pr-merge-gmt8.md](./automations/canton-edu-daily-8am-pr-merge-gmt8.md) 中 **Automation 指令** 整段
6. **Run now** 试跑 → 确认能列出/合并 PR → 启用定时

### 创建内容扫描 Automation（08:15）

1. **New automation**（与上一条分开）
2. Name：`canton-edu daily content → PR`
3. Schedule：`15 8 * * *`，Timezone：`Asia/Shanghai`
4. Repository：`HashClawAI/canton-edu`
5. Prompt：复制 [canton-edu-daily-8am-gmt8.md](./automations/canton-edu-daily-8am-gmt8.md) 中 **Automation 指令** 整段
6. **Run now** 试跑 → 确认 PR 能创建 → 启用定时

**Prompt 更新时**：修改仓库内对应 `.md` 后，须在 cursor.com **重新粘贴**（不会自动同步）。

内容 Automation 已配置**去重规则**：已有 open content PR 时跳过；`translations.ts` 中 URL 已存在则不重复添加；无增量时不 commit、不开 PR。PR 合并 Automation 负责像 [#41](https://github.com/HashClawAI/canton-edu/pull/41) / #47–#52 一样合并 batch、关闭重复 PR。

GitHub Actions **不会**代替 Cursor 改文案；下面 CI 仅作 RSS 候选、部署与**备用提醒**。

## 在 Cursor IDE 里手动跑（复制给 Agent）

```text
在仓库 canton-edu 执行 skill「canton-edu-scheduled-publish」：
1. 从 main 拉最新并新建分支 content/scheduled-今天日期
2. 结合 canton-edu-updater 与 canton-edu-news-daily，对各模块做有依据的增量更新（translations.ts 英中成对、数组对齐）
3. npm run build 必须通过
4. 提交并 push，用 gh 创建 PR（非 merge），PR 描述写完整摘要
5. 不要合并 PR；等 PR 合并 Automation 或人工 merge
```

## 人工上线（兜底）

1. 若 08:00 合并 Automation 失败 → 打开 GitHub **PR**，看 diff → **Merge 到 `main`**。
2. `deploy.yml` 合并后自动部署 GitHub Pages：https://ccprivacy.club/
3. 合并后可关闭当日 `[content run]` / `[news scan]` Issue（若适用）。

## PR 模板

创建 PR 时可选：`?template=content_update.md`

## 定时节奏

| 机制 | Cron | 约北京时间 | 作用 |
|------|------|------------|------|
| **Cursor Automation — PR merge** | `0 8 * * *` Asia/Shanghai | **08:00** | 审查并 **merge** open PR |
| **Cursor Automation — content** | `15 8 * * *` Asia/Shanghai | **08:15** | 全站扫描 → 有增量才开 PR |
| `deploy.yml` | `0 12 * * *` + push `main` | ~20:00 + 合并即部署 | 定时全量重建；合并到 `main` 也会触发 |
| `daily-canton-news-scan.yml` | `0 12 * * *` | ~20:00 | RSS 候选 Issue |
| `scheduled-content-agent-reminder.yml` | `30 12 * * *` | ~20:30 | Automation 失败时的备用提醒 |

可选本机 LaunchAgent：见 `~/.cursor/skills/canton-edu-news-daily/scripts/com.user.canton-edu-news-reminder.plist`（默认 20:00 北京时间）。
