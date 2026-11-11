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
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

***

## GitKraken AI

For workflows and examples, see [AI in GitLens](/gitlens/gl-gk-ai/).

GitKraken AI enhances your development workflow with automated commit messages, intelligent stash descriptions, and code change explanations.

---

### AI-Generated Commit Messages `PRO`

Automatically generate descriptive commit messages based on staged changes.

<figure>
  <img src="/wp-content/uploads/gl-ai-generated-commit-message-01-v2.gif" alt="The Source Control view with a staged file: the empty commit message box, then an AI-generated commit message appearing in it" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit messages from staged changes</figcaption>
</figure>

To use:
- Stage your changes.
- In the Source Control view, open the GitLens sparkle menu in the Changes header and choose **Generate Commit Message**, or
- Use the Command Palette: `GitLens: Generate Commit Message`

GitKraken AI will analyze the diff of staged changes to generate a message. You may provide additional context in the commit box to improve results.

You can customize behavior using [`gitlens.ai` settings](/gitlens/gitlens-settings/#misc-settings) for provider, model, and prompt preferences.

> **Warning:** Pro users and above can optionally use a custom API key to connect to a different AI provider.

---

### AI Stash Messages `PRO`

Available in **Pro**, **Advanced**, and **Business** plans.

Automatically generate meaningful stash descriptions to make your stashes easier to identify later.

**How to access:**
- From the Command Palette: `GitLens: Generate Stash Message with AI`
- During stash creation: Use the AI option in the stash interface
- In the Stash view: Generate AI-powered descriptions for existing stashes

---

### AI Explanations

Let GitKraken AI help explain complex changes across your repo with natural language summaries.

<figure>
  <img src="/wp-content/uploads/ai-branch-summary.png" alt="AI branch summary explanation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI summaries in rendered markdown for improved clarity</figcaption>
</figure>

Standalone **Explain** commands provide markdown summaries for:
- Commits — **Explain Commit**
- Branches — **Explain Branch**
- Working changes — **Explain Working Changes**
- Stashes — **Explain Stash**

**Where to find it:**
- Commit Graph
- Command Palette
- GitLens views: Commits, Branches, Stashes, Search & Compare
- Editor blame hovers (sparkle Explain button)

With GitKraken AI explanations, you can quickly understand:
- The purpose and impact of individual commits
- What changed across all commits in a branch
- What you've modified in your working directory
- What your previous stashes contain
#### AI Commit Explanations `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

Understand the purpose and context of commits with AI-generated summaries. These explanations help you grasp the intent behind complex commits without manually reviewing all changes.

**How to access:**
- **Commit Details** view: See the AI explanation panel
- **Cloud Patch Details** view: View AI insights alongside commit data
- **Commit Review**: Generate explanations for any selected commit

---

### AI Changelog Creation `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

Automatically generate detailed and structured changelogs from a set of selected commits—ideal for maintaining release documentation.

**How to access:**
- **Search/Compare** view: Click the inline button on the commits line
- **Commit Graph**: Select multiple commits, right-click, then choose **Generate Changelog**
- **Command Palette**: `GitLens: Generate Changelog from Commits`

> **Note:** More questions about GitKraken AI? See the [GitKraken AI FAQ](https://help.gitkraken.com/general/gitkraken-ai-faq/) for additional details.

### Auto-Rebase `PRO`

Auto-Rebase (`gitlens.ai.autoRebase`) carries a rebase forward through the conflicts GitKraken AI can resolve confidently, and hands the rest back to you. When a rebase encounters a conflict, AI analyzes it and resolves it only when its confidence meets the threshold you set; anything below that threshold pauses the rebase so you can resolve the conflict yourself and continue. Every run is reviewable and reversible.

Key capabilities:

- **Confidence threshold** — Configure `gitlens.ai.autoRebase.confidenceThreshold` (0 to 1) to control how confident the AI must be before resolving a conflict on its own. Raise it to keep more decisions in your hands.
- **Stops rather than guesses** — Conflicts that fall below the threshold are left for you to resolve manually, with the rebase paused at that point.
- **Custom instructions** — Use `gitlens.ai.resolveConflicts.customInstructions` to provide project-specific guidance for conflict resolution
- **Rebase summary sheet** — After the rebase completes, a summary sheet shows what was resolved and how, so you can review each decision
- **Full undo support** — Undo the entire Auto-Rebase with **Undo Auto-Rebase** (`gitlens.ai.autoRebase.undo`) to return to the pre-rebase state if the results are not what you wanted
- **Your messages and edit stops** — When a `reword` or `squash` step needs a new commit message, Auto-Rebase opens the message in VS Code for you to edit. At a commit you marked `edit`, it resolves and stages any conflicts, then pauses so you can make your changes before you continue.

To start Auto-Rebase, run `GitLens: Auto-Rebase...` from the Command Palette, choose the **Auto-Rebase** option in the Git Command Palette's rebase confirmation, or select **Start Auto-Rebase** in the [Interactive Rebase Editor](/gitlens/gl-features-git-commands-and-rebase/#interactive-rebase-editor). If a rebase is already paused, run `GitLens: Continue with Auto-Rebase`.

For a GitHub [stacked pull request](/gitlens/gl-commit-graph/#pull-request-information), **Auto-Rebase Stack** rebases every branch in the stack from the bottom up, each onto the one below it, and resolves conflicts with AI along the way. **Rebase Stack** does the same but stops at each conflict for you to resolve. Start either one from the Commit Graph pull request sheet, from Launchpad, from the Git Command Palette's rebase confirmation when the current branch belongs to a stack, or with `GitLens: Git Rebase Stacked Pull Requests...` or `GitLens: Auto-Rebase Stacked Pull Requests...`. When the rebase finishes, GitLens offers **Force Push Stack** so you can publish the rebased branches.

When Auto-Rebase pauses, its notification offers **Review & Resolve** and **Abort Rebase**, plus **Resume with AI** when AI features are allowed.

### Commit Composer View `Pro`
The Commit Composer has evolved from a simple one-step process into a comprehensive drafting and review experience. Previously, AI would analyze your changes and immediately create commits. Now, the Commit Composer gives you complete control over the composition process, with options to auto-compose with AI or compose manually. It is integrated directly into the Commit Graph details panel as Compose mode, and is also available as a standalone view.

Join the [Commit Composer discussion](https://github.com/gitkraken/vscode-gitlens/discussions/4530) and provide feedback.

<figure>
  <img src="/wp-content/uploads/gl-commit-composer-17-4-01-v6@2x.png" alt="Commit Graph in Compose mode: the ringed Compose (wand) action on the Working Changes row, and the composer panel beside the graph listing Staged changes and Unstaged changes entries, the changed files, and the Instructions box with the Compose button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">The Commit Composer drafting view</figcaption>
</figure>

#### Interactive Draft Commits

When composing commits, GitLens now creates "draft" commits that you can review, modify, and refine before applying them to your repository. This new workflow lets you:

- **Preview before committing**: See exactly what will be committed before it touches your repository
- **Switch Models**: Try composition with different AI models
- **Guide the AI**: Provide custom instructions to match your team's conventions and preferences  
- **Iterate and refine**: Regenerate individual messages or entire commit compositions
- **Review and edit**: Manually tweak any commit message or approach

<figure>
  <img src="/wp-content/uploads/commit-composer-composed-17-4.png" alt="Commit Composer with AI-composed commit message populated and ready for review" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-composed commit message ready for review</figcaption>
</figure>

You can launch the new Commit Composer view from several places in GitLens:

- **GitLens commit details view**
- **Context menu on the Working Changes row** in the GitLens Commit Graph  
- **Commit Graph details panel**: Switch to **Compose** mode
- **✨ icon in the SCM view header**
- **Command palette**: Search for "Compose Commits"

<figure>
  <img src="/wp-content/uploads/gl-access-composer-1-17-4-01-v3@2x.png" alt="Commit Graph toolbar showing the Compose button entry point" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access Commit Composer from the graph toolbar</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-access-composer-2-17-4-01-v4@2x.png" alt="The Commit Graph's Working Changes details panel with the Compose and Review mode chips ringed in its header, above the branch row, the four changed files and the commit-message box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Or switch to Compose mode in the Working Changes details panel</figcaption>
</figure>

The foundation is now in place for even more powerful composition features in future releases, including intuitive drag-and-drop functionality for moving lines and hunks between commits, creating new draft commits on the fly, and reordering commit sequences.

Whether you prefer to let AI handle the heavy lifting or want granular control over every detail, Commit Composer provides the flexibility to create well-structured commit histories that make code reviews more effective and repository history easier to understand.

### Commit Composer: Branch Recomposition

Commit Composer now lets you clean up and reorganize commits on existing branches, making it perfect for preparing pull requests or refining your commit history before pushing.

<figure>
  <img src="/wp-content/uploads/gl-17-7-recompose-branch-01-v4@2x.png" alt="The Commit Composer opened for the feature/spending-insights branch: its four commits sit in the scope list with drag handles, main's commits are dimmed beneath them above the base, the three changed files are listed, and the Instructions box with the Compose button waits at the bottom" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Recompose an entire branch from the Commit Graph</figcaption>
</figure>

#### Recompose Entire Branches

Open Commit Composer from any branch in the Commit Graph (or anywhere branches appear in GitLens) to inspect and reorganize its commits. The composer creates draft commits you can review before applying changes to your repository.

**Auto-Recompose with AI**: Let AI analyze your branch and restructure commits into logical, well-documented units. Choose your preferred model and provide custom instructions to match your team's conventions. (Pro tip: Set default instructions in the "Generate Commits: Custom Instructions" setting to save time.)

**Manual Control**: Review AI suggestions, regenerate specific commit messages, or manually edit messages and change organization. The composer gives you complete flexibility to craft the commit story that works best.

<video src="/wp-content/uploads/gl-17-7-recompose-example.mp4" autoplay loop controls muted class="help-center-video"></video>

#### Enhanced Composer Capabilities

Commit Composer now handles edge cases that previously blocked composition:

- **Untracked files**: Working changes now include untracked files, so all modifications can be composed together
- **New repositories**: Compose your initial commits even before a base commit exists
- **Performance boost**: Significantly faster rendering when working with changes across many files

### Commit Composer: Selective Recomposition

Commit Composer now lets you recompose specific commits within a branch, giving you precise control over cleaning up your commit history.

<figure>
  <img src="/wp-content/uploads/gl-17-8-recompose-selected-commits-01-v5@2x.png" alt="The Commit Composer scoped to two selected commits of the feature/spending-insights branch — &quot;fix(insights): exclude refunds from spending totals&quot; and &quot;feat(insights): add budget threshold alerts&quot; — shown in the scope list with drag handles while the branch's other commits are dimmed, above the changed files and the Compose instructions box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Select specific commits to recompose</figcaption>
</figure>

Previously, you could only recompose all working changes or an entire branch. Now you can select specific commits that need refinement—like those quick "wip" or "fix" commits made during rapid iteration—and let AI restructure just those changes with better messages.

Select multiple contiguous commits on the same branch using <kbd>Shift</kbd> or <kbd>Cmd</kbd> click, then right-click and choose "Recompose Selected Commits." Commit Composer opens with only your selected commits as drafts, ready for AI-powered or manual refinement.

Commit Composer is also more discoverable, with a new wand button on the Working Changes row in the Commit Graph that opens the composer for all working directory changes. Additionally, when rebasing, you can now switch directly into Commit Composer from the Rebase Editor, canceling your rebase to let AI handle the composition instead.

<figure>
  <img src="/wp-content/uploads/gl-17-8-compose-in-wip-01-v5@2x.png" alt="The Commit Graph's Working Changes row with its action buttons, Compose ringed between Run Default Task and Review." class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Commit Composer from the Working Changes row</figcaption>
</figure>

The Working Changes row also has a **Run Default Task** (play) button that runs a VS Code task in that row's worktree. The first time you select it, GitLens asks you to choose the default task, then runs that task on later clicks. <kbd>Alt</kbd>-click the button to choose a different task. While the task runs, the button reads **Running:** and the task name, and clicking it shows the running task instead of starting another. To pick a task from a list, right-click a Working Changes row in the Commit Graph, or a worktree in the side bar views, and select **Run Task on Worktree...**. In that list, select a task's checkmark button (**Set as Default Task**) to make it the default.

### Compose and Recompose Commands

Commit Composer can also be launched via dedicated commands:

- **Compose Commits...** (`gitlens.composeCommits`) — Opens the Commit Composer for working changes in the current repository, or from a Compose mode entry in the Commit Graph details panel.
- **Recompose Commits...** (`gitlens.ai.recomposeBranch`) — Opens the Commit Composer scoped to an entire branch. GitKraken AI can propose a clearer, more intentional sequence of commits and messages for you to review and refine before applying the result.
- **Recompose Commits from Here...** (`gitlens.ai.recomposeFromCommit`) — Scopes the same workflow to a specific commit onward.
- **Recompose Selected Commits...** (`gitlens.ai.recomposeSelectedCommits`) — Scopes the same workflow to only the selected commits on a branch.

These commands are available from the Commit Graph context menu, branch context menus throughout GitLens, and the Command Palette. Coach marks guide first-time users through the workflow.

***

## AI Agent Integration

For workflows and examples, see [AI Agents in GitLens](/gitlens/gl-agents/).

GitLens integrates with AI coding agents to monitor their activity and coordinate their work alongside your own development workflow.

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

Codex doesn't run newly installed hooks until you trust them. After you install hooks for Codex, run `/hooks` in Codex to trust them, and trust them again whenever the hooks are reinstalled. GitLens shows this reminder in the install notification, with a **Start Codex Session** button, and in the Agents table of GitLens Settings.

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

GitLens manages the GitKraken MCP server installation on a per-agent basis. The **Connect AI Agents** flow walks you through installing the CLI, registering MCP for your current IDE, and connecting additional agents.

- **Connect AI Agents (Install MCP and Hooks)** (`gitlens.ai.connectAgents`) — Interactive flow to install and configure MCP for your agents
- **Connect GitKraken MCP to All Detected Agents** (`gitlens.ai.mcp.installForAllAgents`) — Install the GitKraken MCP server for all detected agents
- **Install GitKraken MCP for Agent** (`gitlens.ai.mcp.installForAgent`) — Install for a specific agent
- **Uninstall GitKraken MCP for Agent** (`gitlens.ai.mcp.uninstallForAgent`) — Remove MCP from a specific agent

In VS Code 1.101 and later, GitLens also installs and enables the GitKraken MCP server for VS Code automatically. To turn this off, disable the `gitlens.gitkraken.mcp.autoEnabled` setting. Turning it off, or turning off GitLens AI features (`gitlens.ai.enabled`), removes the GitKraken MCP server from VS Code's **Configure Tools** list right away, without reloading the window; turning it back on adds the server again.

The agent settings panel provides a centralized view for managing agent configurations.
