# Canton Development Fund — proposal drafts

**Where the proposal is actually submitted:** the **Canton Development Fund** program only accepts proposals via a **Pull Request to** [canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund). Your fork should be **[HashClawAI/canton-dev-fund](https://github.com/HashClawAI/canton-dev-fund)** (or whichever GitHub account owns the fork). Copy `open-canton-edu.md` from **this `canton-edu` repo** into that fork’s **`proposals/open-canton-edu.md`**, push a branch there, and open the PR **against upstream `canton-foundation/canton-dev-fund`**—not against `canton-edu`.

**What this folder is:** a **working copy** kept alongside the Open Canton Edu site. Pushes to **`HashClawAI/canton-edu`** do **not** submit the grant; they only version the draft here. Before the deadline, **sync the same file** into **`canton-dev-fund`** and open the program PR.

**Submit checklist (dev-fund fork):**

1. Clone **your fork** `canton-dev-fund`, add `upstream` → `canton-foundation/canton-dev-fund`, branch from `upstream/main` (or the repo default branch).
2. Copy **`proposals/open-canton-edu.md`** from this repo into **`proposals/open-canton-edu.md`** in the fork.
3. Commit and **push to `origin`** on that fork; open PR **base:** `canton-foundation/canton-dev-fund` **← compare:** your branch.
4. PR title e.g. `Proposal: Open Canton Edu`; PR body from **`PR_BODY_OPEN_CANTON_EDU.md`**, aligned with [`.github/pull_request_template.md`](https://github.com/canton-foundation/canton-dev-fund/blob/main/.github/pull_request_template.md) on upstream.

Champion in the proposal is **@v9n** (Nguyan Vinh); adjust **dates** and **CC totals** after Committee feedback if needed.

The current draft focuses **Open Canton Edu** on **Agentic Education** for **maintainers**—**`docs/agentic-education/`** playbooks, guardrails, **eval** logs, **Skills** / agent flows that **propose** PRs only—plus **information aggregation**, **daily** scheduled rebuild, **public on-chain / explorer-indexer** explainers, **human-reviewed** generation units (manifest §1.5), **`ja`/`ko` i18n**, **production launch + IA**, and **12-month maintenance** (weekly **daily-build** rollups)—**not** a developer-community event program. Illustrative **120,000 CC**; see **§6.3**, **§1.5**, **`docs/agentic-education/`** in the proposal.

Proposal sections mirror the [program README](https://github.com/canton-foundation/canton-dev-fund): **Objective and scope**, **Technical approach**, **Architectural alignment**, **Milestones and deliverables**, **Acceptance criteria**, **Funding request and milestone breakdown**, plus adoption plan, capability evidence, and open-source outputs.
