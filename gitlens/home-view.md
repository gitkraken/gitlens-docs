---
title: Commit Graph is Home
description: GitLens Commit Graph: Your Development Workbench
taxonomy:
    category: gitlens
---
<kbd>Last updated: August 2026</kbd>

The Commit Graph is your starting point for working in GitLens. More than a visualization of repository history, it brings your repository state, working changes, branches, worktrees, and supported coding agent activity together in one connected workbench.
From here, you can understand what’s happening across your repository, coordinate parallel work, review and shape changes, and move work toward merge without rebuilding context across disconnected views and tools.

**One Graph. Your development workflow, end to end.**
<figure>
  <img src="/wp-content/uploads/GL-Commit-Graph-Full.png" alt="GitLens Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Commit Graph</figcaption>
</figure>

## Start in the Commit Graph
When you open GitLens, the Commit Graph gives you a connected view of your repository and the work happening across it.

At a glance, you can understand:

- Your current branch, HEAD, upstream, and merge target
- Working changes across multiple worktrees
- Incoming and outgoing work
- Branches and commits across your repository
- Supported coding agent sessions and their status
- Work that may need review or attention

The Commit Graph gives you both the big picture and the context to decide what to do next. When you need to narrow your focus, you can focus the Graph on a single branch while keeping the broader repository within reach.

## Manage Parallel Human and Agent Work

As development spreads across multiple branches, worktrees, and coding agents, keeping track of what is happening becomes more challenging. The Commit Graph keeps these parallel streams visible and connected to the Git context behind them.

<figure>
  <img src="/wp-content/uploads/GL-Worktrees-tab-open.png" class="help-center-img img-bordered">
</figure>

Multi-worktree WIP shows working changes across your worktrees, not just the one you currently have open. Agent Sessions connects supported coding agent activity to the branches and worktrees where that work is happening.

<figure>
  <img src="/wp-content/uploads/GL-Worktrees-multi-wip.png" class="help-center-img img-bordered">
</figure>

From the Commit Graph, you can:

- See work in progress across multiple worktrees
- Monitor supported coding agent sessions
- Identify sessions that need your attention
- Understand where agent work is happening
- Jump directly into working changes
- Resume work with the surrounding repository context intact

## Agent Kanban

Agent Kanban provides a visual way to understand parallel agent work at a glance. Agent sessions are organized by status, including **Needs Input, Working, Idle, and Inactive**, so you can quickly identify what is progressing and where your attention is needed.

From the board, you can inspect agent work and jump into the associated session and working changes.

<figure>
  <img src="/wp-content/uploads/GL-Agent-Kanban.png" class="help-center-img img-bordered">
</figure>

## Run Your Development Workflow from the Commit Graph

The Commit Graph is more than a place to see the work. It gives you the context and tools to move that work forward.

1. Monitor
See human and agent work happening across branches, worktrees, and sessions, and quickly identify what needs your attention.
<figure>
  <img src="/wp-content/uploads/GL-Agent-working.png" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/GL-Agent-approval.png" class="help-center-img img-bordered">
</figure>

2. Review
Review human or agent-generated changes with AI-powered Review. Surface meaningful findings, ask follow-up questions, and send feedback back to your coding agent when another pass is needed.

<figure>
  <img src="/wp-content/uploads/GL-Graph-Review.png" class="help-center-img img-bordered">
</figure>

3. Compose
Turn working changes into clean, logical commits with Commit Composer. Organize related changes, refine commits with AI assistance, and preview the result before writing it to your history.

<figure>
  <img src="/wp-content/uploads/GL-Graph-Compose.png" class="help-center-img img-bordered">
</figure>

4. Compare
Compare branches, commits, revisions, and working changes to quickly understand exactly what changed before moving work forward.

<figure>
  <img src="/wp-content/uploads/GL-Graph-Compare.png" class="help-center-img img-bordered">
</figure>

5. Rebase
Use AI-powered Rebase to automate tedious rebasing while staying in control of how your commit history is prepared.

<figure>
  <img src="/wp-content/uploads/GL-Auto-AI-rebase.png" class="help-center-img img-bordered">
</figure>

6. Resolve
When parallel work collides, use AI-assisted conflict resolution to understand and resolve conflicts while keeping the surrounding repository context in view.

<figure>
  <img src="/wp-content/uploads/GL-Conflict-detection-auto-rebase.png" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/GL-Auto-rebase-resolve.png" class="help-center-img img-bordered">
</figure>

**Monitor parallel work. Review what changed. Shape it. Compare it. Rebase and resolve it. Get it ready to merge. All from the Commit Graph.**

## Stay Oriented as Work Moves

The Commit Graph keeps important reference points visible as your repository changes.

HEAD, upstream, merge target, ahead and behind status, and incoming work indicators help you understand where you are, what has changed remotely, and where your work is headed.

For larger or more active repositories, you can focus the Commit Graph on a single branch, pin important branches, or use search to quickly find commits, authors, files, messages, and specific code changes.

## Explore More GitLens Workflows
Continue exploring the workflows available from the Commit Graph:
- Agent Sessions to monitor supported coding agent activity
- Worktrees to manage parallel development
- Review to understand and validate changes
- Commit Composer to shape changes into logical commits
- Compare to understand differences across your work
- AI-powered Rebase to automate and clean up rebases
- AI-assisted Conflict Resolution to resolve overlapping work
- Visual History to understand how your codebase evolved
- Launchpad to prioritize pull requests and move work toward merge
