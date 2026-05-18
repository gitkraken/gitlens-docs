---

title: AI Agents in Gitlens
description: Using AI Agents in Gitlens
taxonomy:
    category: gitlens

---

# Using AI Agents in GitLens

GitLens 18 introduces integrated AI agent workflows directly inside your IDE. Instead of managing coding agents through scattered terminal tabs, external apps, or separate extensions, GitLens surfaces agent status, worktree context, and actionable Git workflows directly within the Commit Graph and Home View.

With GitLens, you can:

- Monitor active AI coding agents without leaving the IDE
- Track agent sessions tied to branches and worktrees
- Review AI-generated changes inside the Commit Graph
- Compose commits directly from agent-produced work
- Quickly identify sessions waiting for input
- Manage parallel worktrees and WIP changes visually

GitLens 18 currently supports Claude Code integrations through GitLens-managed hooks.

---

# What Are Agent Sessions?

An agent session represents an active AI coding workflow associated with a repository, branch, or worktree.

GitLens tracks these sessions and surfaces their status throughout the interface so you can monitor progress and act on changes without constantly switching between terminals, chat panels, or external applications.

Agent sessions can appear in:

- The Home View
- The Commit Graph overview cards
- The Commit Graph details panel
- The Agent Sessions sidebar panel

Each session displays contextual Git information including:

- Associated branch
- Worktree
- Working changes
- Agent state
- Ahead/behind indicators
- Actions requiring attention

---

# Installing Claude Code Hooks

GitLens integrates with Claude Code using hooks that provide real-time session visibility.

## Install Claude Code Hooks

You can install hooks from several locations in GitLens:

- Home View banner
- Commit Graph header
- Agent Sessions sidebar banner
- Integrations menu

To install hooks:

1. Open the GitLens Home View or Commit Graph
2. Select the Claude Code integration prompt
3. Follow the setup instructions
4. Reload VS Code or your IDE if prompted

Once installed, GitLens automatically detects Claude Code sessions and surfaces their state throughout the UI.

## Uninstall Hooks

To remove Claude Code hooks:

1. Open the Command Palette
2. Run:

```text
GitLens: Uninstall Claude Code Hooks
```

---

# Understanding Agent Status Pills

GitLens surfaces agent activity through status pills shown throughout the interface.

Status pills are color-coded and animated to help you quickly understand what requires attention.

## Agent States

### Running

The agent is actively processing changes or generating code.

Running sessions display subtle pulse animations.

### Waiting for Input

The agent requires developer input before continuing.

Waiting sessions display attention-grabbing animations and are surfaced prominently in overview cards.

### Idle

The session is connected but not currently performing actions.

### Completed

The agent finished its current task and changes are ready for inspection or review.

---

# Using the Agent Sessions Panel

GitLens 18 adds a dedicated Agent Sessions panel available from:

- The Home View
- The Commit Graph sidebar

The Agent Sessions panel provides a centralized place to monitor all active sessions.

## Features

The panel includes:

- Session status pills
- Branch and worktree associations
- Quick actions
- List and tree layouts
- Session grouping by workspace or worktree

## Switch Between List and Tree Layouts

Use the layout toggle in the Agent Sessions panel toolbar to switch between:

- List layout
- Tree layout

Tree layout is especially useful when working across multiple repositories or worktrees.

---

# Reviewing Agent-Generated Code

GitLens 18 turns the Commit Graph into a full review surface for AI-assisted workflows.

From the Commit Graph details panel you can:

- Inspect working changes
- Compare revisions
- Review AI-generated code
- Generate commits with Commit Composer
- Resolve conflicts
- Stage and unstage files

## Open the Commit Graph Details Panel

To open the details panel:

1. Open the Commit Graph
2. Select a commit, branch, or WIP row
3. Toggle the details panel if it is hidden

The panel can be docked:

- On the right side of the Graph
- At the bottom of the Graph

Hold `Alt` while toggling the panel to switch docking locations.

---

# AI Code Review in the Graph

GitLens 18 adds AI-powered review workflows directly inside the Commit Graph.

## Start an AI Review

1. Open the Commit Graph
2. Select a WIP row or commit
3. Open the details panel
4. Switch to Review mode

GitLens generates:

- Review summaries
- Suggested focus areas
- Severity indicators
- File-level context

This helps you validate AI-generated changes before committing or opening a pull request.

> AI Code Review requires GitLens Pro.

---

# Compose Commits from Agent Changes

Commit Composer is now integrated directly into the Commit Graph details panel.

You can generate structured commits from working changes without leaving the Graph.

## Compose a Commit

1. Open the Commit Graph
2. Select a WIP row
3. Open the details panel
4. Switch to Compose mode
5. Review proposed commit groupings
6. Edit the generated commit message if needed
7. Commit the changes

Compose mode supports:

- Multi-diff previews
- Staged and unstaged files
- Untracked files
- AI-generated commit messages

---

# Multi-Worktree Workflows

GitLens 18 introduces multi-worktree WIP rows in the Commit Graph.

Instead of only showing changes for the active worktree, the Graph now displays work-in-progress rows for every connected worktree.

This makes it easier to:

- Monitor parallel agent workflows
- Compare work across tasks
- Review uncommitted changes
- Resolve conflicts
- Compose commits from multiple worktrees

Each WIP row updates live as files change.

## WIP Scroll Markers

The Commit Graph minimap now includes WIP scroll markers that highlight work-in-progress rows.

You can:

- Customize marker colors
- Enable or disable markers in settings

---

# Focus Branch Mode

Focus Branch mode helps reduce Graph noise when working on a specific branch or task.

When enabled, the Commit Graph scopes itself to the branch you care about.

## Enable Focus Branch Mode

1. Open the Commit Graph
2. Open the scope menu in the Graph header
3. Select a branch to focus

While focused:

- The Graph follows the branch's first-parent history
- The minimap zooms to the relevant commit range
- Simplify Merge History is automatically applied
- Visual indicators show that the Graph is scoped

---

# Pin a Branch to the Left Side of the Graph

GitLens 18 allows you to pin an important branch to the leftmost column of the Commit Graph.

This helps keep long-lived reference branches like `main` or `develop` visible while navigating complex histories.

## Pin a Branch

1. Right-click a branch row
2. Select:

```text
Pin Branch
```

Pinned branches remain visible across Graph sessions.

---

# Conflict Resolution Workflows

Conflict resolution workflows now extend directly into the Commit Graph.

You can resolve merge conflicts from:

- Commit Graph WIP rows
- The Interactive Rebase editor

Conflict states are surfaced inline inside the details panel.

---

# Open the Commit Graph in a New Window

GitLens 18 adds support for opening the Commit Graph in a detached window.

This is especially useful for:

- Multi-monitor setups
- Large repositories
- Persistent review workflows
- Parallel agent workflows

## Open in a New Window

From the Commit Graph menu, select:

```text
Open in New Window
```

---

# Related Features

GitLens agent workflows work especially well alongside:

- Commit Composer
- AI Code Review
- Worktrees
- Launchpad
- Interactive Rebase
- GitKraken MCP integrations
