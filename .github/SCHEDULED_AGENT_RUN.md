# Scheduled agent run — canton-edu（定时 Agent → 摘要 → 人工上线）

## 主路径：Cursor Automation（推荐）

**每天 08:00 北京时间（GMT+8）** 由 Cursor Cloud Agent 自动扫描并开 PR。

1. 打开 [cursor.com/automations](https://cursor.com/automations) → **New automation**
2. 按 [.github/automations/canton-edu-daily-8am-gmt8.md](./automations/canton-edu-daily-8am-gmt8.md) 填写：
   - Schedule：`0 8 * * *`，Timezone：`Asia/Shanghai`
   - Repository：`HashClawAI/canton-edu`
   - Prompt：复制该文件中的 **Automation 指令** 整段
3. **Run now** 试跑 → 确认 PR 能创建 → 启用定时

GitHub Actions **不会**代替 Cursor 改文案；下面 CI 仅作 RSS 候选、部署与**备用提醒**。

## 在 Cursor IDE 里手动跑（复制给 Agent）

```text
在仓库 canton-edu 执行 skill「canton-edu-scheduled-publish」：
1. 从 main 拉最新并新建分支 content/scheduled-今天日期
2. 结合 canton-edu-updater 与 canton-edu-news-daily，对各模块做有依据的增量更新（translations.ts 英中成对、数组对齐）
3. npm run build 必须通过
4. 提交并 push，用 gh 创建 PR（非 merge），PR 描述写完整摘要
5. 不要合并 PR；等我审完再合并
```

## 人工上线

1. 打开 GitHub 上的 **PR**，看摘要与 diff。  
2. 确认无误后 **Approve** → **Merge 到 `main`** → 触发 **Deploy to GitHub Pages**。  
3. 合并后可关闭当日 `[content run]` / `[news scan]` Issue（若适用）。

## PR 模板

创建 PR 时可选：`?template=content_update.md`

## 定时节奏

| 机制 | Cron (UTC) | 约北京时间 | 作用 |
|------|------------|------------|------|
| **Cursor Automation** | `0 8 * * *` Asia/Shanghai | **08:00** | **全站扫描 → PR（主路径）** |
| `deploy.yml` | `0 12 * * *` + push `main` | ~20:00 + 合并即部署 | 定时全量重建；合并到 `main` 也会触发 |
| `daily-canton-news-scan.yml` | `0 12 * * *` | ~20:00 | RSS 候选 Issue |
| `scheduled-content-agent-reminder.yml` | `30 12 * * *` | ~20:30 | Automation 失败时的备用提醒 |

可选本机 LaunchAgent：见 `~/.cursor/skills/canton-edu-news-daily/scripts/com.user.canton-edu-news-reminder.plist`（默认 20:00 北京时间）。
