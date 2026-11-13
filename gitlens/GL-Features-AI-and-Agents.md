---
title: AI and Agent Features
description: Technical reference for GitKraken AI in GitLens, including commit messages, explanations, Auto-Rebase and the Commit Composer, and AI agent integration.
product: GitLens
feature: GitKraken AI
content_type: reference
audience: developer
plan_required: [Pro]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [claude-code, codex, copilot-cli, opencode]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [gitkraken-ai, commit-composer, auto-rebase, ai-explain, agents, hooks, mcp]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "AI and Agents"
    nav_order: 40
    nav_parent: "gitlens-features"
    page_type: "content"
    card_icon: "sparkles"
    card_color: "red"
    card_description: "GitKraken AI features, Auto-Rebase, the Commit Composer, and AI agent integration"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

***

## GitKraken AI

For workflows and examples, see [AI in GitLens](/gitlens/gl-gk-ai/).

GitKraken AI writes commit messages and stash descriptions, explains code changes, and helps you compose commits and rebase.

---

### AI-Generated Commit Messages `PRO`

Generate a commit message from your staged changes.

<figure>
  <img src="/wp-content/uploads/gl-ai-generated-commit-message-01-v2.gif" alt="The Source Control view with a staged file: the empty commit message box, then an AI-generated commit message appearing in it" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit messages from staged changes</figcaption>
</figure>

To generate a commit message:

1. Stage your changes.
2. In the Source Control view, open the GitLens sparkle menu in the Changes header and choose **Generate Commit Message**. Or run `GitLens: Generate Commit Message` from the Command Palette.

GitKraken AI reads the diff of your staged changes and writes a message. To improve the result, add context in the commit box first.

You can customize behavior using [`gitlens.ai` settings](/gitlens/gitlens-settings/#misc-settings) for provider, model, and prompt preferences.

> **Warning:** Pro users and above can optionally use a custom API key to connect to a different AI provider.

---

### AI Stash Messages `PRO`

Available in **Pro**, **Advanced**, and **Business** plans.

Generate stash descriptions so you can identify your stashes later.

**How to access:** When you stash changes with GitLens, select the **Generate Stash Message** sparkle button in the stash message input.

---

### AI Explanations

GitKraken AI explains changes across your repo in plain-language summaries.

<figure>
  <img src="/wp-content/uploads/ai-branch-summary.png" alt="AI branch summary explanation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI summaries in rendered markdown for improved clarity</figcaption>
</figure>

The **Explain** commands write markdown summaries for:

- Commits — **Explain Commit Changes...**
- Branches — **Explain Branch Changes...**
- Working changes — **Explain Working Changes...**
- Stashes — **Explain Stash Changes...**

**Where to find it:**
- Commit Graph
- Command Palette
- GitLens views: Commits, Branches, Stashes, Search & Compare
- Editor blame hovers (sparkle Explain button)

Use GitKraken AI explanations to understand:

- The purpose and impact of individual commits
- What changed across all commits in a branch
- What you have modified in your working directory
- What your previous stashes contain

#### AI Commit Explanations `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

AI-generated summaries explain the purpose and context of a commit, so you can understand its intent without reviewing every change yourself.

**How to access:**
- **Commit Details** view: See the AI explanation panel
- **Cloud Patch Details** view: View AI insights alongside commit data
- **Commit Review**: Generate explanations for any selected commit

---

### AI Changelog Creation `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

Generate a structured changelog from a set of selected commits, for example for your release notes.

**How to access:**
- **Search/Compare** view: Click the inline button on the commits line
- **Commit Graph**: Select multiple commits, right-click, then choose **Generate Changelog**
- **Command Palette**: `GitLens: Generate Changelog...`

> **Note:** More questions about GitKraken AI? See the [GitKraken AI FAQ](https://help.gitkraken.com/general/gitkraken-ai-faq/) for additional details.

### AI Commit Composition `PRO`

GitKraken AI can turn your changes into commits, or restructure the commits on a branch, in the [Commit Composer](#commit-composer-view-pro). You review every proposed commit and message before anything is applied.

- To commit your working changes, run `GitLens: Compose Commits...`.
- To rework the commits already on a branch, run `GitLens: Recompose Commits...`, or use **Recompose Commits from Here...** and **Recompose Selected Commits...** from the Commit Graph's context menu.

See [Compose and Recompose Commands](#compose-and-recompose-commands) for where each command is available. To resolve rebase conflicts with AI, use [Auto-Rebase](#auto-rebase-pro).

### Auto-Rebase `PRO`

Auto-Rebase (`gitlens.ai.autoRebase`) continues a rebase through the conflicts GitKraken AI can resolve confidently, and leaves the rest for you. When a rebase hits a conflict, AI analyzes it and resolves it only when its confidence meets the threshold you set; anything below that threshold pauses the rebase so you can resolve the conflict yourself and continue. Every run is reviewable and reversible.

Key capabilities:

- **Confidence threshold** — Configure `gitlens.ai.autoRebase.confidenceThreshold` (0 to 1) to control how confident the AI must be before resolving a conflict on its own. Raise it to keep more decisions in your hands.
- **Stops rather than guesses** — Conflicts that fall below the threshold are left for you to resolve manually, with the rebase paused at that point.
- **Custom instructions** — Use `gitlens.ai.resolveConflicts.customInstructions` to give project-specific guidance for resolving conflicts.
- **Rebase summary sheet** — After the rebase completes, a summary sheet shows what was resolved and how, so you can review each decision.
- **Full undo support** — Undo the entire Auto-Rebase with **Undo Auto-Rebase** (`gitlens.ai.autoRebase.undo`) to return to the pre-rebase state if the results are not what you wanted.
- **Your messages and edit stops** — When a `reword` or `squash` step needs a new commit message, Auto-Rebase opens the message in VS Code for you to edit. At a commit you marked `edit`, it resolves and stages any conflicts, then pauses so you can make your changes before you continue.

To start Auto-Rebase, run `GitLens: Auto-Rebase...` from the Command Palette, choose the **Auto-Rebase** option in the Git Command Palette's rebase confirmation, or select **Start Auto-Rebase** in the [Interactive Rebase Editor](/gitlens/gl-features-git-commands-and-rebase/#interactive-rebase-editor). If a rebase is already paused, run `GitLens: Continue with Auto-Rebase`.

For a GitHub [stacked pull request](/gitlens/gl-commit-graph/#pull-request-information), **Auto-Rebase Stack** rebases every branch in the stack from the bottom up, each onto the one below it, and resolves conflicts with AI along the way. **Rebase Stack** does the same but stops at each conflict for you to resolve. Start either one from the Commit Graph pull request sheet, from Launchpad, from the Git Command Palette's rebase confirmation when the current branch belongs to a stack, or with `GitLens: Git Rebase Stacked Pull Requests...` or `GitLens: Auto-Rebase Stacked Pull Requests...`. When the rebase finishes, GitLens offers **Force Push Stack** so you can publish the rebased branches.

When Auto-Rebase pauses, its notification offers **Review & Resolve** and **Abort Rebase**, plus **Resume with AI** when AI features are allowed. **Review & Resolve** opens the Commit Graph's resolve panel. Once every conflict there has a resolution, select **Apply & Resume with AI** to apply the resolutions and let Auto-Rebase finish the rebase.

### Commit Composer View `PRO`

Use the Commit Composer to draft and review commits before you create them. Let GitKraken AI compose them, or compose them yourself. The Commit Composer opens in the Commit Graph details panel as Compose mode, and as a standalone view.

Join the [Commit Composer discussion](https://github.com/gitkraken/vscode-gitlens/discussions/4530) and provide feedback.

<figure>
  <img src="/wp-content/uploads/gl-commit-composer-17-4-01-v6@2x.png" alt="Commit Graph in Compose mode: the ringed Compose (wand) action on the Working Changes row, and the composer panel beside the graph listing Staged changes and Unstaged changes entries, the changed files, and the Instructions box with the Compose button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">The Commit Composer drafting view</figcaption>
</figure>

#### Interactive Draft Commits

When you compose commits, GitLens creates draft commits that you can review, change, and refine before you apply them to your repository. With draft commits, you can:

- **Preview before committing**: See exactly what will be committed before anything changes in your repository
- **Switch models**: Try composing with different AI models
- **Guide the AI**: Give custom instructions that match your team's conventions
- **Iterate and refine**: Regenerate individual messages or the whole set of commits
- **Review and edit**: Edit any commit message or how the changes are grouped

<figure>
  <img src="/wp-content/uploads/commit-composer-composed-17-4.png" alt="Commit Composer with AI-composed commit message populated and ready for review" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-composed commit message ready for review</figcaption>
</figure>

You can open the Commit Composer view from these places in GitLens:

- **GitLens commit details view**
- **Context menu on the Working Changes row** in the GitLens Commit Graph  
- **Commit Graph details panel**: Switch to **Compose** mode
- **✨ icon in the SCM view header**
- **Command Palette**: Search for **Compose Commits**

<figure>
  <img src="/wp-content/uploads/gl-access-composer-1-17-4-01-v3@2x.png" alt="Commit Graph toolbar showing the Compose button entry point" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access Commit Composer from the graph toolbar</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-access-composer-2-17-4-01-v4@2x.png" alt="The Commit Graph's Working Changes details panel with the Compose and Review mode chips ringed in its header, above the branch row, the four changed files and the commit-message box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Or switch to Compose mode in the Working Changes details panel</figcaption>
</figure>

### Commit Composer: Branch Recomposition

Use Commit Composer to clean up and reorganize the commits on an existing branch, for example before you open a pull request or push.

<figure>
  <img src="/wp-content/uploads/gl-17-7-recompose-branch-01-v4@2x.png" alt="The Commit Composer opened for the feature/spending-insights branch: its four commits sit in the scope list with drag handles, main's commits are dimmed beneath them above the base, the three changed files are listed, and the Instructions box with the Compose button waits at the bottom" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Recompose an entire branch from the Commit Graph</figcaption>
</figure>

#### Recompose Entire Branches

Open Commit Composer from any branch in the Commit Graph (or anywhere branches appear in GitLens) to inspect and reorganize its commits. The composer creates draft commits you can review before applying changes to your repository.

**Auto-Recompose with AI**: GitKraken AI analyzes your branch and restructures its commits into logical units with clear messages. Choose your model and give custom instructions that match your team's conventions. To reuse the same instructions every time, set them in the **Generate Commits: Custom Instructions** setting (`gitlens.ai.generateCommits.customInstructions`).

**Manual Control**: Review the AI's suggestions, regenerate specific commit messages, or edit messages and how the changes are grouped yourself.

<video src="/wp-content/uploads/gl-17-7-recompose-example.mp4" autoplay loop controls muted class="help-center-video"></video>

#### Enhanced Composer Capabilities

Commit Composer also handles these cases:

- **Untracked files**: Working changes include untracked files, so you can compose all your changes together
- **New repositories**: Compose your first commits before a base commit exists

### Commit Composer: Selective Recomposition

Use Commit Composer to recompose only specific commits within a branch.

<figure>
  <img src="/wp-content/uploads/gl-17-8-recompose-selected-commits-01-v5@2x.png" alt="The Commit Composer scoped to two selected commits of the feature/spending-insights branch — &quot;fix(insights): exclude refunds from spending totals&quot; and &quot;feat(insights): add budget threshold alerts&quot; — shown in the scope list with drag handles while the branch's other commits are dimmed, above the changed files and the Compose instructions box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Select specific commits to recompose</figcaption>
</figure>

Select the commits that need work, such as quick "wip" or "fix" commits, and let GitKraken AI restructure only those changes with clearer messages.

1. Select multiple contiguous commits on the same branch with <kbd>Shift</kbd>-click or <kbd>Cmd</kbd>-click.
2. Right-click and choose **Recompose Selected Commits...**.

Commit Composer opens with only your selected commits as drafts, ready for you or GitKraken AI to refine.

To open the composer for all your working changes, select the **Compose** (wand) button on the Working Changes row in the Commit Graph. While you rebase, you can also switch from the Rebase Editor to Commit Composer with **Recompose Commits...**, which cancels the rebase and lets AI compose the commits instead.

<figure>
  <img src="/wp-content/uploads/gl-17-8-compose-in-wip-01-v5@2x.png" alt="The Commit Graph's Working Changes row with its action buttons, Compose ringed between Run Default Task and Review." class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Commit Composer from the Working Changes row</figcaption>
</figure>

The Working Changes row also has a **Run Default Task** (play) button that runs a VS Code task in that row's worktree:

- The first time you select it, GitLens asks you to choose the default task. Later clicks run that task.
- <kbd>Alt</kbd>-click the button to choose a different task.
- While the task runs, the button reads **Running:** and the task name. Clicking it then shows the running task instead of starting another.

To pick a task from a list, right-click a Working Changes row in the Commit Graph, or a worktree in the side bar views, and select **Run Task on Worktree...**. In that list, select a task's checkmark button (**Set as Default Task**) to make it the default.

### Compose and Recompose Commands

You can also open Commit Composer with these commands:

- **Compose Commits...** (`gitlens.composeCommits`) — Opens the Commit Composer for working changes in the current repository, or from a Compose mode entry in the Commit Graph details panel.
- **Recompose Commits...** (`gitlens.ai.recomposeBranch`) — Opens the Commit Composer scoped to an entire branch. GitKraken AI can propose a clearer, more intentional sequence of commits and messages for you to review and refine before applying the result.
- **Recompose Commits from Here...** (`gitlens.ai.recomposeFromCommit`) — Scopes the same workflow to a specific commit onward.
- **Recompose Selected Commits...** (`gitlens.ai.recomposeSelectedCommits`) — Scopes the same workflow to only the selected commits on a branch.

These commands are available from the Commit Graph context menu, branch context menus throughout GitLens, and the Command Palette. Coach marks guide first-time users through the workflow.

***

## AI Agent Integration

For workflows and examples, see [AI Agents in GitLens](/gitlens/gl-agents/).

GitLens shows the activity of your AI coding agents beside your own work, so you can follow and manage what they do.

### Supported Agents

GitLens tracks sessions of the following agents through GitKraken Hooks:

- Claude Code
- Codex
- GitHub Copilot CLI
- OpenCode

What GitLens can do differs by agent. For Claude Code, GitLens can answer permission requests and read session transcripts. For Codex, GitHub Copilot CLI, and OpenCode, you answer permission requests in the agent itself. You can resume past sessions of every supported agent.

### Agent Hooks

GitLens installs GitKraken Hooks for your AI agents so their activity is tracked within your repository. Use the following commands:

- **Install GitKraken Hooks for All AI Agents** (`gitlens.agents.installHooks`) — Install hooks for all detected agents
- **Install GitKraken Hooks for Agent** (`gitlens.agents.installHooksForAgent`) — Install hooks for a specific agent
- **Uninstall GitKraken Hooks for All AI Agents** (`gitlens.agents.uninstallHooks`) — Remove hooks for all agents
- **Uninstall GitKraken Hooks for Agent** (`gitlens.agents.uninstallHooksForAgent`) — Remove hooks for a specific agent

Codex does not run newly installed hooks until you trust them. After you install hooks for Codex, run `/hooks` in Codex to trust them, and trust them again whenever the hooks are reinstalled. GitLens shows this reminder in the install notification, with a **Start Codex Session** button, and in the Agents table of GitLens Settings.

### Agent Sessions

When hooks are active, GitLens tracks agent sessions and displays status indicators:

- **Agent session cards** appear on the branch cards in the Commit Graph side bar, in the Agents section of the Working Changes details panel, and in the Agent Kanban
- **Status pills** on branches in the Commit Graph indicate which branches have active agent sessions
- **Past sessions** are sessions that have ended. Select **Show Past Sessions** in the side bar's **Agent Sessions** panel to list them. The Working Changes details panel lists a worktree's past sessions with **Show More** to page through them. Select **Archive Session** to remove a past session from the lists.

To pick up a past session where it left off, select **Resume in Terminal**, which opens an integrated terminal in the session's folder and runs the agent's resume command. For a Claude Code session in one of your workspace folders, with the Claude Code extension installed, you can also select **Resume in Claude Code Extension**. The `gitlens.agents.resumeTarget` setting controls where a plain **Resume** opens when both are possible:

- `null` (default) — Ask the first time, with an option to remember your choice
- `terminal` — Always resume in a new integrated terminal
- `extension` — Resume in the agent's VS Code extension when it can open the session, otherwise in a terminal

### MCP Server Management

GitLens installs the GitKraken MCP server separately for each agent. The **Connect AI Agents (Install MCP and Hooks)** command walks you through installing the CLI, registering MCP for your current IDE, and connecting additional agents.

- **Connect AI Agents (Install MCP and Hooks)** (`gitlens.ai.connectAgents`) — Install and configure MCP for your agents, step by step
- **Connect GitKraken MCP to All Detected Agents** (`gitlens.ai.mcp.installForAllAgents`) — Install the GitKraken MCP server for all detected agents
- **Install GitKraken MCP for Agent** (`gitlens.ai.mcp.installForAgent`) — Install for a specific agent
- **Uninstall GitKraken MCP for Agent** (`gitlens.ai.mcp.uninstallForAgent`) — Remove MCP from a specific agent

In VS Code 1.101 and later, GitLens also installs and enables the GitKraken MCP server for VS Code automatically. To turn this off, disable the `gitlens.gitkraken.mcp.autoEnabled` setting. Turning it off, or turning off GitLens AI features (`gitlens.ai.enabled`), removes the GitKraken MCP server from VS Code's **Configure Tools** list right away, without reloading the window; turning it back on adds the server again.

To manage your agents' settings in one place, open the **Agents** category under **Integrations** in GitLens Settings.
