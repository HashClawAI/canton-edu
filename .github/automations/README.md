# Cursor Automations — canton-edu

本目录存放 **Cursor Cloud Automation** 的任务说明（Prompt + 调度），供在 [cursor.com/automations](https://cursor.com/automations) 创建定时 Agent。

## 推荐：一条 Automation 搞定

| 文件 | 调度 | 说明 |
|------|------|------|
| **[canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md)** | `0 8 * * *` · `Asia/Shanghai` | **08:00** Phase 0 合并积压 PR → Phase 1 内容扫描开 PR → Phase 2 同轮 merge（当日上线） |

在 cursor.com 只建 **一个** Automation，Name 如 `canton-edu daily update → merge + PR`，Prompt 复制上表文件中的 **Automation 指令**。

## 可选：拆成两条

| 文件 | 调度 | 说明 |
|------|------|------|
| [canton-edu-daily-8am-pr-merge-gmt8.md](./canton-edu-daily-8am-pr-merge-gmt8.md) | `0 8 * * *` | 仅审查 merge |
| [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md) Phase 1 部分 | `15 8 * * *` | 仅扫描开 PR（需单独剪 Prompt） |

操作说明亦见 [.github/SCHEDULED_AGENT_RUN.md](../SCHEDULED_AGENT_RUN.md)。
