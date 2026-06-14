# Cursor Automation — canton-edu 每日内容更新（08:00 GMT+8）

在 [cursor.com/automations](https://cursor.com/automations)（或 Cursor IDE → Agents → Automations）创建本任务。GitHub Actions **不能**代替 Cursor 改 `translations.ts`；本 Automation 是**主路径**。

## 创建步骤（一次性）

| 字段 | 值 |
|------|-----|
| **Name** | `canton-edu daily content → PR` |
| **Trigger** | Schedule |
| **Cron** | `0 8 * * *` |
| **Timezone** | `Asia/Shanghai`（GMT+8，每天 **08:00**） |
| **Repository** | `HashClawAI/canton-edu`（单仓库，必须勾选以便 push 分支、开 PR） |
| **Model** | 默认或 `composer-2.5`（需能完成多步 git + 网页检索） |

保存后可用 **Run now** 试跑一轮，确认能开 PR 再依赖定时触发。

## Automation 指令（复制到 Prompt 框）

```text
You maintain the bilingual Canton education site in this repository (HashClawAI/canton-edu).

## Goal
Scan for verifiable new Canton Network / Canton Coin / Digital Asset / Canton Foundation updates since the newest dates already in `src/i18n/translations.ts`. Apply incremental, accurate edits. Open a **Pull Request for human review** — do **not** merge.

## Scope (edit only when you have primary or credible secondary sources)
Single source of truth: `src/i18n/translations.ts`
- Mirror every EN change in `zh` with the same array lengths and order.
- Sections: `home`, `learn`, `ecosystem`, `cips`, `news`, `videos`, `research`, `community`, `resources`.
- Prefer official sources: canton.network, canton.foundation, PRNewswire/BusinessWire, SEC EDGAR, GitHub canton-foundation/cips, issuer press releases.
- Skip duplicates (check existing `url` / titles). News items: reverse-chronological `{ date, tag, title, body, url }`.
- Do not remove existing entries unless clearly wrong.

## Workflow
1. `git fetch origin && git checkout main && git pull origin main`
2. Branch: `content/scheduled-YYYY-MM-DD` (use today's UTC or Asia/Shanghai date)
3. Web search for news since latest `news.items[0].date`; sweep other modules per credible findings only.
4. Edit `src/i18n/translations.ts` (EN then ZH).
5. `npm run build` — fix until green (expect ~28 site pages + doc pages).
6. Commit: `chore(content): scheduled scan YYYY-MM-DD — <short summary>`
7. `git push -u origin HEAD`
8. `gh pr create` with title `content: scheduled scan YYYY-MM-DD` and body using `.github/PULL_REQUEST_TEMPLATE/content_update.md` structure:
   - Summary (EN bullets; note ZH parity)
   - Modules touched (check boxes)
   - Sources (canonical URLs)
   - Risks / review focus
   - Build result
9. **Never** merge, **never** push to `main`, **never** force-push.

## PR rules
- Repository requires human approval before merge.
- If a branch name is rejected by branch rules, use `content/scheduled-YYYY-MM-DD` or `chore/news-refresh-YYYY-MM-DD`.
- If no verifiable updates: still open a short PR comment in the run output explaining "no changes" OR skip commit but report in automation summary — prefer **no empty PR**; exit cleanly with summary only.

## Output when finished
Reply with: branch name, PR URL, list of added/changed items, and `npm run build` status.
```

## 人工审阅与上线

1. 收到 PR 通知 → 看摘要与 diff，核对中英对齐与链接。
2. **Approve** → **Squash merge** 到 `main`。
3. `deploy.yml` 自动部署 GitHub Pages：https://hashclawai.github.io/canton-edu/

## 与 GitHub Actions 的分工

| 机制 | 时间（GMT+8） | 作用 |
|------|----------------|------|
| **本 Cursor Automation** | **每天 08:00** | 扫描 → 改 `translations.ts` → **开 PR** |
| `deploy.yml` | 约 08:00 / 20:00 | 合并后重建站点 |
| `daily-canton-news-scan.yml` | 约 20:15 | RSS 候选 Issue（辅助） |
| `scheduled-content-agent-reminder.yml` | 约 20:45 | 备用提醒 Issue（Automation 失败时） |

## 故障排查

- **PR 未创建**：检查 Automation 是否绑定 `HashClawAI/canton-edu` 且 GitHub 集成有 write 权限。
- **Self-approval 无法合并**：需账号持有人 Approve（仓库规则）。
- **无更新**：正常；不必强行凑新闻。
