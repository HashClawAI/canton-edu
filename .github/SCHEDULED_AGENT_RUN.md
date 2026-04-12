# Scheduled agent run — canton-edu（定时 Agent → 摘要 → 人工上线）

GitHub Actions **不会**代替 Cursor 改文案；定时任务只负责**提醒**你在本机执行 Agent。

## 在 Cursor 里怎么做（复制下面整段给 Agent）

```text
在仓库 canton-edu 执行 skill「canton-edu-scheduled-publish」：
1. 按该 skill 从 main 拉最新并新建分支 content/scheduled-今天UTC日期
2. 结合 canton-edu-updater 与 canton-edu-news-daily，对各模块做有依据的增量更新（translations.ts 英中成对、数组对齐）
3. npm run build 必须通过
4. 提交并 push，用 gh 创建 Draft PR，PR 描述写完整摘要（改了哪些模块、来源链接、风险点、未改动的模块写「无」）
5. 不要合并 PR；等我审完再合并
```

## 人工上线

1. 打开 GitHub 上的 **Draft PR**，看摘要与 diff。  
2. 确认无误后 **Merge 到 `main`** → 触发 **Deploy to GitHub Pages**。  
3. 合并后可关闭当日由定时任务创建的 `[content run]` / `[news scan]` 相关 Issue（若适用）。

## PR 模板

创建 PR 时可选：`?template=content_update.md`

## 定时节奏（可选）

| 机制 | 说明 |
|------|------|
| Workflow **Scheduled content — agent reminder** | 约每天 **12:30 UTC**（**20:30 北京时间**）开 Issue，若已有未关闭的 `[content run]` 则跳过 |
| Workflow **Daily Canton news (RSS scan)** | **12:00 UTC**（**20:00 北京时间**）RSS 候选 + 可能开 `[news scan]` Issue |
| 本机 LaunchAgent | 见 `~/.cursor/skills/canton-edu-news-daily/scripts/com.user.canton-edu-news-reminder.plist`（默认 **20:00 北京时间** 通知） |

可将 LaunchAgent 的提示改为：「执行 **canton-edu-scheduled-publish** 全站扫描」。
