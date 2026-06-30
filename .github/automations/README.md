# Cursor Automations — canton-edu

本目录存放 **Cursor Cloud Automation** 的任务说明（Prompt + 调度配置），供在 [cursor.com/automations](https://cursor.com/automations) 创建定时 Agent。

| 文件 | 调度 | 说明 |
|------|------|------|
| [canton-edu-daily-8am-pr-merge-gmt8.md](./canton-edu-daily-8am-pr-merge-gmt8.md) | `0 8 * * *` · `Asia/Shanghai` | 每日 **08:00** 审查 open PR → **合并**（去重 content PR） |
| [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md) | `15 8 * * *` · `Asia/Shanghai` | 每日 **08:15** 扫描 → **有增量才开 PR**（去重 + 无 open content PR） |

**推荐顺序：** 先 08:00 合并积压 PR，再 08:15 内容扫描开新 PR，避免同一时刻冲突。

操作说明亦见仓库根目录 [.github/SCHEDULED_AGENT_RUN.md](../SCHEDULED_AGENT_RUN.md)。
