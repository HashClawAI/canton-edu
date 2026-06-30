# Scheduled agent run — canton-edu（定时 Agent → 摘要 → 人工上线）

## 主路径：一条 Cursor Automation（推荐）

**每天 08:00 北京时间** — 合并积压 PR → 扫描内容 → 有增量则开 PR → **同轮 merge**（当日部署）。

1. [cursor.com/automations](https://cursor.com/automations) → **New automation**
2. 按 [.github/automations/canton-edu-daily-8am-gmt8.md](./automations/canton-edu-daily-8am-gmt8.md) 填写：
   - Name：`canton-edu daily update → merge + PR`
   - Schedule：`0 8 * * *`，Timezone：`Asia/Shanghai`
   - Repository：`HashClawAI/canton-edu`
   - Prompt：复制该文件 **Automation 指令** 整段
3. **Run now** 试跑 → 确认 Phase 0/1/2 行为 → 启用定时
4. **Prompt 更新时**：改仓库内 md 后须在 cursor.com **重新粘贴**

三阶段分工（同一 Prompt 内顺序执行）：

| Phase | 作用 |
|-------|------|
| **0** | 审查并 squash merge 已有 open PR（去重 content PR） |
| **1** | 拉最新 `main`，扫描 `translations.ts`，有增量才开 PR |
| **2** | 若刚开了 content PR 且 build 已过 → 同轮 merge → 触发部署 |

**可选拆分：** 若不想合并+扫描同一条任务，见 [canton-edu-daily-8am-pr-merge-gmt8.md](./automations/canton-edu-daily-8am-pr-merge-gmt8.md)（仅 merge，08:00）+ 内容扫描改 08:15。

GitHub Actions **不会**代替 Cursor 改文案；CI 仅 RSS 候选、部署与备用提醒。

## 在 Cursor IDE 里手动跑

```text
在仓库 canton-edu 执行 skill「canton-edu-scheduled-publish」：
1. 先 gh 合并可 merge 的 open content PR（或人工确认无积压）
2. main 拉最新，分支 content/scheduled-今天日期
3. canton-edu-updater + canton-edu-news-daily 增量更新 translations.ts（英中成对）
4. npm run build 通过 → push → gh pr create
5. 审查通过后 merge（或交给次日 08:00 Automation）
```

## 人工兜底

Automation Phase 0/2 merge 失败 → 人工 Review PR → Merge 到 `main` → `deploy.yml` 部署 https://ccprivacy.club/

## PR 模板

`?template=content_update.md`

## 定时节奏

| 机制 | Cron | 约北京时间 | 作用 |
|------|------|------------|------|
| **Cursor Automation（合并+扫描）** | `0 8 * * *` Asia/Shanghai | **08:00** | merge → scan → PR → merge |
| `deploy.yml` | `0 12 * * *` + push `main` | ~20:00 + 合并即部署 | GitHub Pages |
| `daily-canton-news-scan.yml` | `0 12 * * *` | ~20:00 | RSS 候选 Issue |
| `scheduled-content-agent-reminder.yml` | `30 12 * * *` | ~20:30 | 失败备用提醒 |

可选本机 LaunchAgent：`~/.cursor/skills/canton-edu-news-daily/scripts/com.user.canton-edu-news-reminder.plist`（默认 20:00 北京时间）。
