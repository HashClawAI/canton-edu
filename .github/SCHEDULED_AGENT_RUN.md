# Scheduled agent run — canton-edu（定时 Agent → 摘要 → 人工上线）

GitHub Actions **不会**代替 Cursor 自动改写 `translations.ts`；定时任务负责 **RSS 候选**、**全站重建部署**，以及 **Issue 提醒** 你在本机执行 Agent 并 **提 Draft PR**。

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
3. 合并后可关闭当日对应 **[content run]** / **[news scan]** Issue（若适用）。

## PR 模板

创建 PR 时可选：`?template=content_update.md`

## 定时节奏（GitHub Actions）

| 机制 | Cron (UTC) | 大致北京时间 | 说明 |
|------|----------------|--------------|------|
| **Deploy to GitHub Pages** | `0 */12 * * *`（每 12 小时 `:00`） | ~08:00、~20:00 | 全站 `npm run build` + Pages；刷新走势图、「上次更新时间」、CIP 话题等构建期内容 |
| **Canton news (RSS scan)** | `15 */12 * * *`（每 12 小时 `:15`） | ~08:15、~20:15 | 若有新候选链接则创建 **`[news scan]`** Issue（同一 UTC 半天槽仅一条） |
| **Scheduled content — agent reminder** | `45 */12 * * *`（每 12 小时 `:45`） | ~08:45、~20:45 | 若无同标题未关闭 Issue，则创建 **`[content run]`**，提示在本机跑 Agent 并 **提 PR** |

GitHub 可能对定时任务有约 **1 小时** 的排队误差。

### 本地 LaunchAgent（可选）

见 `~/.cursor/skills/canton-edu-news-daily/scripts/com.user.canton-edu-news-reminder.plist`。可与线上节奏对齐改为每日两次提醒，或改为「执行 canton-edu-scheduled-publish 全站扫描」文案。
