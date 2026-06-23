# Cursor Automations — canton-edu

本目录存放 **Cursor Cloud Automation** 的任务说明（Prompt + 调度配置），供在 [cursor.com/automations](https://cursor.com/automations) 创建定时 Agent。

| 文件 | 调度 | 说明 |
|------|------|------|
| [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md) | `0 8 * * *` · `Asia/Shanghai` | 每日 08:00 扫描 → **有增量才开 PR**（去重 + 无 open content PR） |

操作说明亦见仓库根目录 [.github/SCHEDULED_AGENT_RUN.md](../SCHEDULED_AGENT_RUN.md)。
