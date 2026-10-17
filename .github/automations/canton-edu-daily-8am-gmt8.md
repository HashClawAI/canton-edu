# Cursor Automation — canton-edu 每日更新（合并 + 扫描，08:00 GMT+8）

在 [cursor.com/automations](https://cursor.com/automations) 创建**一条**任务即可：**先合并积压 PR，再扫描开新 PR**（可选同轮合并刚开的 PR）。GitHub Actions **不能**代替 Cursor 改 `translations.ts`。

> **可选拆分：** 若希望合并与扫描分开调度，见 [canton-edu-daily-8am-pr-merge-gmt8.md](./canton-edu-daily-8am-pr-merge-gmt8.md)（08:00 仅 merge）+ 本文件 Phase 1 单独跑（08:15）。

## 创建步骤（一次性）

| 字段 | 值 |
|------|-----|
| **Name** | `canton-edu daily update → merge + PR` |
| **Trigger** | Schedule |
| **Cron** | `0 8 * * *` |
| **Timezone** | `Asia/Shanghai`（GMT+8，每天 **08:00**） |
| **Repository** | `HashClawAI/canton-edu`（write + `gh pr merge`） |
| **Model** | 默认或 `composer-2.5` |

保存后 **Run now** 试跑：应能 merge 或跳过 → 扫描 → 有增量则开 PR（并可同轮 merge）。

**重要：** 更新 Prompt 后须在 cursor.com **重新粘贴**（仓库内文档不会自动同步）。

## Automation 指令（复制到 Prompt 框）

```text
You maintain HashClawAI/canton-edu (deploys to https://ccprivacy.club/). Each run has **three phases in order** — do not skip Phase 0.

---

## Phase 0 — Merge existing open PRs (always first)

`gh auth status` must succeed. Ruleset on `main`: required approvals = **0**. Do not use `--admin` unless merge is blocked.

1. List open PRs:
   `gh pr list -R HashClawAI/canton-edu --state open --json number,title,headRefName,isDraft,mergeable,mergeStateStatus`

2. **Triage overlapping content PRs** (2+ matching `content: scheduled scan`, `content/scheduled-*`, or `cursor/canton-content-scan-*`):
   - Keep the newest / most complete (usually highest #).
   - Close others: `Superseded by #<n> (daily batch merge).`
   - Merge only the winner. Pattern: #41 / #47–#52.

3. **Per PR to merge:**
   - Content scan drafts: `gh pr ready <n> -R HashClawAI/canton-edu`
   - Review diff; reject if secrets, EN/ZH array mismatch, duplicate URLs on main, or CONFLICTING.
   - If touches `src/`, `scripts/`, `package.json`, `astro.config.mjs`, `public/`: checkout PR, `npm ci && npm run build`; fail → comment, do not merge.
   - Pass → `gh pr merge <n> -R HashClawAI/canton-edu --squash --delete-branch`
   - Skip large feat/* PRs unless clearly safe; note in summary.

4. `git fetch origin && git checkout main && git pull origin main`

If zero open PRs at start → note `Phase 0: no open PRs` and continue to Phase 1.

---

## Phase 1 — Content scan → open PR (only if no blocking open content PR)

### Open PR gate (after Phase 0)
- Re-list open PRs. If ANY still open matches `content: scheduled scan`, `content: batch`, `content/scheduled-*`, or `cursor/canton-content-scan-*`:
  - **STOP Phase 1.** Reply why merge failed + PR number.
  - Do not open another content PR.

### Anti-duplication
- Collect every `url: '...'` and ecosystem/CIP link on `main` in `src/i18n/translations.ts` (ripgrep).
- Never add duplicate URLs or re-add existing CIP/SV ids.
- One PR per scan: batch all new items reverse-chronologically.

### Scope
`src/i18n/translations.ts` only — mirror EN↔ZH (same array lengths/order): `home`, `learn`, `ecosystem`, `cips`, `news`, `videos`, `research`, `community`, `resources`.
Sources: canton.network, canton.foundation, forum.canton.network, credible press, SEC EDGAR, canton-foundation/cips.

### When to skip Phase 1 (no commit)
- Zero new unique URLs / no material updates after dedup → `No changes — findings already on main` + sources checked.

### Workflow when there IS new content
1. Branch: `content/scheduled-YYYY-MM-DD` (Asia/Shanghai).
2. Web search since latest `news.items[0].date`; edit EN then ZH.
3. `npm run build` — fix until green.
4. Commit: `chore(content): scheduled scan YYYY-MM-DD — <summary>`
5. Push + `gh pr create` with title `content: scheduled scan YYYY-MM-DD`, body from `.github/PULL_REQUEST_TEMPLATE/content_update.md` (sources, build result).
6. **Never** push to `main` or force-push.

---

## Phase 2 — Merge PR opened this run (same day deploy)

If Phase 1 **just created** a content PR and `npm run build` was green on that branch:
1. `gh pr ready <n>` if draft.
2. Quick checklist: EN/ZH parity, no duplicate URLs vs main, sources in body.
3. `gh pr merge <n> -R HashClawAI/canton-edu --squash --delete-branch`
4. Confirm deploy: `gh run list -R HashClawAI/canton-edu --branch main --limit 1`

If merge fails → leave PR open; human merges later.

Do **not** merge non-content feat PRs in Phase 2 unless they were the only open PR and passed Phase 0 review.

---

## Hard stops
- Force-push to `main`
- Open duplicate content PR while one is still open after Phase 0
- Merge without build when PR touches build-affecting paths
- Merge overlapping content PRs without closing duplicates

## Final reply (markdown)
| Phase | Result |
|-------|--------|
| 0 merge | PR #n merged / closed / skipped — reason |
| 1 scan | PR opened / skipped — reason |
| 2 merge | merged / skipped — reason |
Include deploy URL if merged.
```

## 人工兜底

1. Automation 摘要里 Phase 0 或 2 失败 → 人工 Review → Merge。
2. `deploy.yml` 合并后部署：https://ccprivacy.club/
3. 积压多条重复 content PR → Phase 0 应 batch 合并；若仍失败，参考 [#41](https://github.com/HashClawAI/canton-edu/pull/41)。

## 与 GitHub Actions 的分工

| 机制 | Cron | 约北京时间 | 作用 |
|------|------|------------|------|
| **本 Cursor Automation** | `0 8 * * *` Asia/Shanghai | **08:00** | merge 积压 → 扫描 → 开 PR → 可选同轮 merge |
| `deploy.yml` | `0 12 * * *` + push `main` | ~20:00 + 合并即部署 | GitHub Pages |
| `daily-canton-news-scan.yml` | `0 12 * * *` | ~20:00 | RSS 候选 Issue |
| `scheduled-content-agent-reminder.yml` | `30 12 * * *` | ~20:30 | 失败备用提醒 |

## 故障排查

| 现象 | 处理 |
|------|------|
| Phase 1 跳过「open content PR exists」 | Phase 0 未成功 merge；人工处理该 PR |
| 连续重复 PR | 更新 Prompt 为本文件最新版 |
| Merge 被 rules 拦截 | Required approvals 应为 0；或 `gh pr merge --admin` |
| 无更新 | 正常；应输出 `No changes` |
