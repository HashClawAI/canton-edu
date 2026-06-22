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

**重要：** 更新本文件中的 Prompt 后，须在 cursor.com/automations 里**重新粘贴**到对应 Automation 的 Prompt 框（仓库内文档不会自动同步到 Cloud）。

## Automation 指令（复制到 Prompt 框）

```text
You maintain the bilingual Canton education site in this repository (HashClawAI/canton-edu).

## Goal
Scan for verifiable new Canton Network / Canton Coin / Digital Asset / Canton Foundation updates since content already on `main` in `src/i18n/translations.ts`. Apply incremental, accurate edits. Open **one** Pull Request for human review when—and only when—there is at least one deduplicated change. Do **not** merge.

## Anti-duplication (mandatory — run before any edit)
1. **Open PR gate**
   - `gh pr list -R HashClawAI/canton-edu --state open --json number,title,headRefName,isDraft`
   - If ANY open PR matches `content: scheduled scan`, `content: batch`, branch `content/scheduled-*`, or `cursor/canton-content-scan-*`:
     - **STOP.** Do not push a new branch or open another PR.
     - Reply: `Skipped — open content PR #<n> exists; merge or close it before the next scan.`
2. **URL inventory on current main**
   - After `git pull origin main`, collect every `url: '...'` and ecosystem/CIP link already in `src/i18n/translations.ts` (use ripgrep).
   - **Never** add a news item, ecosystem row, or resource link whose canonical URL already exists.
   - Same story re-reported elsewhere: skip unless it is a genuinely new primary source **and** a distinct URL (e.g. forum completion post vs sv-cal freeze notice).
3. **CIP / ecosystem IDs**
   - Do not re-add CIP highlights or SV list entries that already exist (check `id: 'CIP-…'` and svList strings).
4. **One PR per scan day**
   - If multiple days of backlog since `news.items[0].date`, add **all new unique items in a single PR**, reverse-chronological—never assume an older unmerged automation PR will land first.

## Scope (edit only with primary or credible secondary sources)
Single source of truth: `src/i18n/translations.ts`
- Mirror every EN change in `zh` with the same array lengths and order.
- Sections: `home`, `learn`, `ecosystem`, `cips`, `news`, `videos`, `research`, `community`, `resources`.
- Prefer: canton.network, canton.foundation, forum.canton.network, PRNewswire/BusinessWire, SEC EDGAR, GitHub canton-foundation/cips, issuer press releases.
- News: `{ date, tag, title, body, url }` — reverse-chronological; no duplicate URLs.
- Do not remove existing entries unless clearly wrong.

## When to skip (no commit, no push, no PR)
- After dedup, **zero** new unique URLs and no material module updates.
- Findings are already on `main` (including same URL or same event already covered).
- Reply with summary only: `No changes — findings already on main` + list what you checked.

## Workflow (when there IS new content)
1. `git fetch origin && git checkout main && git pull origin main`
2. Run **Anti-duplication** steps above.
3. Branch: `content/scheduled-YYYY-MM-DD` (Asia/Shanghai date). If that branch already exists on remote with an open PR, **stop** (see gate #1).
4. Web search since latest `news.items[0].date`; sweep other modules only for credible, non-duplicate findings.
5. Edit `src/i18n/translations.ts` (EN then ZH).
6. `npm run build` — fix until green (~1600+ static pages including doc mirror).
7. Commit: `chore(content): scheduled scan YYYY-MM-DD — <short summary>`
8. `git push -u origin HEAD`
9. `gh pr create -R HashClawAI/canton-edu --title "content: scheduled scan YYYY-MM-DD" --body` using `.github/PULL_REQUEST_TEMPLATE/content_update.md`:
   - Summary, modules touched, sources (URLs), risks, build result
   - Add line: `Open PRs checked: none blocked` or note if you skipped due to open PR
10. **Never** merge, **never** push to `main`, **never** force-push.

## PR create failure
If `gh pr create` fails (e.g. integration permissions): still push branch, then reply with branch name + compare URL and ask a human to open the PR manually.

## Output when finished
- **Skipped:** reason + open PR number if any.
- **No changes:** sources checked, none added.
- **PR opened:** branch, PR URL, bullet list of **new** URLs only, `npm run build` status.
```

## 人工审阅与上线

1. 收到 PR 通知 → 看摘要与 diff，核对中英对齐与链接。
2. **Approve** → **Squash merge** 到 `main`。
3. `deploy.yml` 自动部署 GitHub Pages：https://ccprivacy.club/

若积压多条 Automation Draft PR，**不要逐条合并**——应像 [#41](https://github.com/HashClawAI/canton-edu/pull/41) 一样合并为一条去重 PR，并关闭其余。

## 与 GitHub Actions 的分工

| 机制 | Cron (UTC) | 约北京时间 | 作用 |
|------|------------|------------|------|
| **本 Cursor Automation** | `0 8 * * *` Asia/Shanghai | **08:00** | 扫描 → 改 `translations.ts` → **开 PR**（无增量则跳过） |
| `deploy.yml` | `0 12 * * *` + push `main` | ~20:00 + 合并即部署 | 定时全量重建；合并到 `main` 也会触发 |
| `daily-canton-news-scan.yml` | `0 12 * * *` | ~20:00 | RSS 候选 Issue（辅助） |
| `scheduled-content-agent-reminder.yml` | `30 12 * * *` | ~20:30 | Automation 失败时的备用提醒 |

## 故障排查

| 现象 | 处理 |
|------|------|
| **PR 未创建** | 检查 Automation 是否绑定仓库 write 权限；或本次无增量（正常跳过） |
| **连续多条重复 PR** | 在 cursor.com 更新 Prompt 为本文件最新版；合并/关闭未合 open PR |
| **Self-approval 无法合并** | 需 DrJingLee Approve |
| **无更新** | 正常；Automation 应输出 `No changes` 而非空 PR |
