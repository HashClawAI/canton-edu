# Cursor Automation — canton-edu 每日 PR 审查合并（08:00 GMT+8）

> **推荐：** 多数情况用 [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md) **一条 Automation**（Phase 0 合并 + Phase 1 扫描 + Phase 2 同轮 merge）。本文件仅在你想**拆分**「只 merge」与「只扫描」时使用。

在 [cursor.com/automations](https://cursor.com/automations) 创建本任务，与内容扫描 **分开**配置。

## 创建步骤（一次性）

| 字段 | 值 |
|------|-----|
| **Name** | `canton-edu daily PR review → merge` |
| **Trigger** | Schedule |
| **Cron** | `0 8 * * *` |
| **Timezone** | `Asia/Shanghai`（GMT+8，每天 **08:00**） |
| **Repository** | `HashClawAI/canton-edu`（需 write + 可 `gh pr merge`） |
| **Model** | 默认或 `composer-2.5` |

**与内容扫描的时序：** 建议本任务 **08:00** 先合并积压 PR；内容扫描改为 **08:15**（`15 8 * * *`），见 [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md)。

保存后 **Run now** 试跑一轮，确认能列出 open PR 并在无问题时 merge。

**重要：** 更新本文件 Prompt 后，须在 cursor.com/automations **重新粘贴**（仓库内文档不会自动同步）。

## Automation 指令（复制到 Prompt 框）

```text
You are the GitHub maintainer for HashClawAI/canton-edu (deploys to https://ccprivacy.club/).

## Goal
Every run: review all **open** pull requests on `HashClawAI/canton-edu`, merge those that pass review, close duplicates. Do **not** open new content PRs (that is a separate Automation).

## Preconditions
- `gh auth status` must succeed for an account with repo **admin** or merge rights.
- Branch ruleset on `main`: required approvals = **0** (merge without separate Approve). Do **not** use `--admin` unless a merge is blocked and rules explicitly require bypass.

## Step 1 — Inventory
```bash
gh pr list -R HashClawAI/canton-edu --state open --json number,title,headRefName,isDraft,author,url,mergeable,mergeStateStatus
```

If **zero** open PRs → reply `No open PRs — nothing to merge` and stop.

## Step 2 — Triage overlapping content PRs (mandatory when multiple)
If **2+** open PRs match any of:
- title prefix `content: scheduled scan`
- branch `content/scheduled-*` or `cursor/canton-content-scan-*`

Then **do not merge them individually**:
1. Identify the PR with the **newest** scan date / most complete diff (usually highest PR number or latest commit).
2. **Close** the others with comment: `Superseded by #<n> (daily batch merge).`
3. Merge **only** the consolidated winner (or create one batch PR on `main` if none is clearly complete — rare; prefer closing stale and merging the best one).

Same pattern as historical [#41](https://github.com/HashClawAI/canton-edu/pull/41) / #47–#52 cleanup.

## Step 3 — Per-PR review (each PR to merge)
For each remaining open PR (non-draft first; see drafts below):

### A. Mark draft ready (content scans)
If `isDraft: true` and title matches `content: scheduled scan`:
- `gh pr ready <n> -R HashClawAI/canton-edu`
- Re-check `mergeable` / `mergeStateStatus`

Skip draft PRs that are **not** content scans unless the user explicitly marked them ready elsewhere.

### B. Diff review
```bash
gh pr diff <n> -R HashClawAI/canton-edu --name-only
gh pr diff <n> -R HashClawAI/canton-edu | head -500
gh pr view <n> -R HashClawAI/canton-edu --json body,additions,deletions,changedFiles
```

**Reject / do not merge** if:
- Touches `.env`, secrets, credentials, or deploy tokens
- `translations.ts` EN/ZH news (or paired arrays) length mismatch
- Duplicate news `url:` already on `main` (grep `origin/main:src/i18n/translations.ts`)
- Large unrelated refactors mixed with content
- `mergeStateStatus` is CONFLICTING (attempt rebase on branch or leave for human)

**Content PR checklist (`content: scheduled scan`):**
- [ ] New URLs not already on `main`
- [ ] EN + ZH `news.items` (and any touched sections) same count & order
- [ ] Sources cited in PR body

**Feature PR checklist (feat/*, chore/*, fix/*):**
- [ ] Scope matches title; no obvious security issues
- [ ] If code/build changes: verify locally when feasible

### C. Build verification (when PR changes site build)
If diff touches `src/`, `scripts/`, `package.json`, `astro.config.mjs`, or `public/`:
```bash
git fetch origin pull/<n>/head:pr-<n> && git checkout pr-<n>
npm ci && npm run build
git checkout main && git branch -D pr-<n>
```
If build fails → **do not merge**; comment on PR with error summary.

For **translations-only** content PRs, build is strongly recommended; skip only if environment cannot run npm and PR body already states green CI (note in reply).

### D. Merge
When checks pass:
```bash
gh pr merge <n> -R HashClawAI/canton-edu --squash --delete-branch
```
Use a clear squash subject if `--subject` is needed (e.g. content scan date).

Do **not** merge to `main` via direct push. One PR at a time; refresh list after each merge.

## Step 4 — Post-merge
- `gh run list -R HashClawAI/canton-edu --branch main --limit 1` — confirm Deploy workflow started.
- Reply with markdown summary:

| PR | Action | Notes |
|----|--------|-------|
| #n | merged / closed / skipped | one-line reason |

Include deploy run URL if available.

## Hard stops (never do)
- Force-push to `main`
- Merge without reading diff when PR touches >3 files or >200 lines
- Merge multiple overlapping content PRs without closing duplicates
- Merge if `npm run build` failed on your checkout

## Output when finished
- **Nothing to do:** `No open PRs`
- **Merged:** list PR URLs + deploy status
- **Blocked:** list PR numbers + what human must fix
```

## 人工兜底

| 现象 | 处理 |
|------|------|
| Merge 仍被 rules 拦截 | 检查 ruleset Required approvals 是否为 0；或临时 `--admin` |
| 多条重复 content PR 又出现 | 更新内容扫描 Automation Prompt（开 PR 前检查 open PR） |
| Build 在 Agent 环境失败 | 本地 `npm run build` 验证后手动 merge |
| 非 content 的大 feature PR | Agent 可 skip 并在摘要中标注「需人工看一下」 |

## 与内容 Automation 的分工

| 时间 (GMT+8) | Automation | 作用 |
|--------------|------------|------|
| **08:00** | **本任务** | 审查 + merge 已有 open PR |
| **08:15** | [canton-edu-daily-8am-gmt8.md](./canton-edu-daily-8am-gmt8.md) | 扫描内容 → **仅开新 PR**，不 merge |
| merge `main` / 20:00 UTC cron | `deploy.yml` | GitHub Pages 部署 |
