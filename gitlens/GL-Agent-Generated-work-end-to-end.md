---

title: Take Agent-Generated Work from Change to Merge
description: Review, revise, compose, compare, and rebase a coding agent's changes in the GitLens Commit Graph until the branch is ready to merge.
product: GitLens
feature: Workflows
content_type: how-to
audience: developer
plan_required: [all]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot-cli, opencode]
hosted_variant: both
status: GA
last_verified: 2026-09
llms_include: true
tags: [ai-agents, ai-review, commit-composer, compare, ai-rebase, commit-graph]
taxonomy:
    category: gitlens
last_updated: 2026-11

custom_fields:
    nav_category: "gl-workflows"
    nav_label: "Take Agent-Generated Work from Change to Merge"
    nav_order: 20
    nav_parent: "gl-workflows"
    page_type: "content"
    card_icon: "robot"
    card_color: "green"
    card_description: "Code Change to Merged branches all through GitLens"
    entry_title: "Take Agent-Generated Work from Change to Merge"
    entry_desc: "Code Change to Merged branches all through GitLens"
    entry_order: 20
---
<kbd>Last updated: November 2026</kbd>

Coding agents can produce changes quickly, but generated code still needs to be understood, organized, and prepared before it is ready to merge.

GitLens keeps that workflow inside the Commit Graph. Review what your agent changed, send feedback to the agent for another pass, shape the result into clean commits, and use Auto-Rebase to prepare the branch for merge without switching between views and tools.

## 1. Start with the Agent's Changes
Open the agent's working changes from the Commit Graph to understand what was modified and how that work relates to the branch and repository around it.
<figure>
  <img src="/wp-content/uploads/GL-Agent-needs-approval-full-view.png" alt="The Commit Graph with the Working Changes details panel below it: an agent session card, &quot;Review current file for discrepancies&quot;, waits for permission with Allow, Always Allow and Deny buttons, above the changed files and the commit box" class="help-center-img img-bordered">
</figure>
The agent session, its worktree, and its changes appear together, so you can understand the work before you decide what happens next.

If the agent's session has already ended, it stays listed as a Past session, so you can pick up where the agent left off. Resume a past session from Claude Code, Codex, GitHub Copilot CLI, or OpenCode with **Resume in Terminal**, or, for Claude Code, with **Resume in Claude Code Extension**. To choose from the worktree's sessions, right-click its Working Changes row and select **Resume Agent Session...**. For details, see [Resume a Past Session](/gitlens/gl-agents/#resume-a-past-session).

## 2. Review the Work While It's Fresh
<figure>
  <img src="/wp-content/uploads/gl-review-findings-01-v2@2x.png" alt="Review panel after Review Diff: the Checklist pane lists four changed files, three with finding-count marks, and the Findings pane shows &quot;3 findings open&quot;, an overview, and the expanded focus area &quot;Admin report and account actions&quot; with a CRITICAL and a WARNING finding card, each with Copy Finding, Address with Agent, Leave a Comment, Dismiss Finding and Delete Finding icons. Below are Address Findings with Agent and the instructions box with Review Diff, Orient and Review in Repo." class="help-center-img img-bordered">
  </figure>
Use Review Changes in the Commit Graph to check the agent-generated changes before they become a pull request. Select **Review Changes…** on the agent's Working Changes row to get a checklist of the changed files.

From the review, you can:

- Read each file's diff and mark it viewed as you go
- Select **Review Diff** to have GitKraken AI return findings grouped into focus areas, or **Orient** for a suggested reading order
- Dismiss, comment on, or ask about a finding, in the panel or as a comment thread in the diff
- Select **Review in Repo** to have your coding agent review the changes in the repository

Review becomes part of the development loop instead of something that happens only after the work is finished. See [Review Changes in the Commit Graph](/gitlens/gl-review-changes/) for the full workflow.

## 3. Send Findings Back for Another Pass
When the review finds something that needs to change, send it to your coding agent with **Address Findings with Agent** for the whole review, **Address Focus Area with Agent** for one focus area, or **Address with Agent** for a single finding.

GitLens sends the findings with your comments, so the agent can address them without you reconstructing the issue in another terminal or chat session.
Once the agent updates the code, return to the working changes and review the result again. Files that changed after you viewed them are tagged **changed since viewed**.

## 4. Compose Clean, Reviewable Commits

Agent-generated work may span multiple files and concerns that do not belong in a single commit.

Use Commit Composer from the Commit Graph to organize those changes into clean, logical commits that are easier for you and your teammates to understand.

<figure>
  <img src="/wp-content/uploads/gl-graph-compose-01-v3@2x.png" alt="Commit Graph with the Composing Changes panel open beside it: the main branch, an Unstaged changes entry with four files changed (README.md, reports.ts, spending-analysis.ts, user-management.ts) and the Instructions box with the Compose button" class="help-center-img img-bordered">
  </figure>
With Compose, you can:

- Group related changes into draft commits
- Move files between commits
- Reorder commits
- Generate commit messages with AI
- Preview synthesized diffs before committing
- Refine the proposed commit structure before writing it to your history

Compose helps turn raw agent output into a history that explains the work instead of simply recording it.

## 5. Compare Before Moving Forward
Before preparing the branch for merge, use Compare to understand exactly how the work differs from another commit, branch, revision, or working state.

Comparing from the Commit Graph keeps the changes and their surrounding repository context together, making it easier to validate the final result before moving on.

## 6. Rebase with AI
Once the work is reviewed and organized, the branch may still need a rebase before it is ready to merge.

Use [Auto-Rebase](/gitlens/gl-gk-ai/#auto-rebase-pro) to rebase the branch with GitKraken AI resolving conflicts, instead of stepping through every rebase operation yourself. You stay in control of the resulting history.

If the rebase creates conflicts, you can move straight into conflict resolution in the Commit Graph without rebuilding context elsewhere.

## From Agent Output to Merge-Ready Work
The Commit Graph keeps every step between generated code and merge-ready work in one place:

**Agent changes → Review → Agent feedback → Compose → Compare → Auto-Rebase**

Treat agent output as a draft, not finished code: use GitLens to understand it, improve it, shape it, and prepare it to ship.


