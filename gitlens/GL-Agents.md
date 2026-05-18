---

title: AI Agents in Gitlens
description: Using AI Agents in Gitlens
taxonomy:
    category: gitlens

---

<kbd>Last updated: May 2026</kbd>

## Using AI Agents in GitLens

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

## Understand Agent Sessions

An agent session represents an active AI coding workflow associated with a repository, branch, or worktree.

GitLens tracks these sessions and surfaces their status throughout the interface so you can monitor progress and act on changes without switching between terminals, chat panels, or external applications.

Agent sessions appear in:

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

## Install Claude Code Hooks

GitLens integrates with Claude Code using hooks that provide real-time session visibility.

You can install hooks from several locations in GitLens:

- Home View banner
- Commit Graph header
- Agent Sessions sidebar banner
- Integrations menu

### Install Hooks

1. Open the GitLens Home View or Commit Graph.
2. Select the Claude Code integration prompt.
3. Follow the setup instructions.
4. Reload VS Code or your IDE if prompted.

Once installed, GitLens automatically detects Claude Code sessions and surfaces their state throughout the UI.

### Uninstall Hooks

1. Open the Command Palette.
2. Run:

```text
GitLens: Uninstall Claude Code Hooks
```

---

## Understand Agent Status Pills

GitLens surfaces agent activity through status pills shown throughout the interface. Status pills are color-coded and animated to help you quickly identify what requires attention.

### Running

The agent is actively processing changes or generating code. Running sessions display subtle pulse animations.

### Waiting for Input

The agent requires your input before continuing. Waiting sessions display attention-grabbing animations and appear prominently in overview cards.

### Idle

The session is connected but not currently performing actions.

### Completed

The agent finished its current task. Changes are ready for inspection or review.

---

## Use the Agent Sessions Panel

GitLens 18 adds a dedicated Agent Sessions panel available from the Home View and the Commit Graph sidebar. The panel provides a centralized place to monitor all active sessions.

### Panel Features

The panel includes:

- Session status pills
- Branch and worktree associations
- Quick actions
- List and tree layouts
- Session grouping by workspace or worktree

### Switch Between List and Tree Layouts

Use the layout toggle in the Agent Sessions panel toolbar to switch between list and tree layouts. Tree layout is especially useful when working across multiple repositories or worktrees.

---

## Review Agent-Generated Code

GitLens 18 turns the Commit Graph into a full review surface for AI-assisted workflows.

From the Commit Graph details panel you can:

- Inspect working changes
- Compare revisions
- Review AI-generated code
- Generate commits with Commit Composer
- Resolve conflicts
- Stage and unstage files

### Open the Commit Graph Details Panel

1. Open the Commit Graph.
2. Select a commit, branch, or WIP row.
3. Toggle the details panel if it is hidden.

The panel can be docked on the right side or at the bottom of the Commit Graph. Hold `Alt` while toggling the panel to switch docking locations.

---

## Run AI Code Review in the Commit Graph

GitLens 18 adds AI-powered review workflows directly inside the Commit Graph.

### Start an AI Code Review

1. Open the Commit Graph.
2. Select a WIP row or commit.
3. Open the details panel.
4. Switch to Review mode.

GitLens generates:

- Review summaries
- Suggested focus areas
- Severity indicators
- File-level context

This helps you validate AI-generated changes before committing or opening a pull request.

> AI Code Review requires GitLens Pro.

---

## Compose Commits from Agent Changes

Commit Composer is integrated directly into the Commit Graph details panel. You can generate structured commits from working changes without leaving the Commit Graph.

### Compose a Commit

1. Open the Commit Graph.
2. Select a WIP row.
3. Open the details panel.
4. Switch to Compose mode.
5. Review proposed commit groupings.
6. Edit the generated commit message if needed.
7. Commit the changes.

Compose mode supports:

- Multi-diff previews
- Staged and unstaged files
- Untracked files
- AI-generated commit messages

---

## Manage Multi-Worktree Workflows

GitLens 18 introduces multi-worktree WIP rows in the Commit Graph. Instead of showing changes only for the active worktree, the Commit Graph displays work-in-progress rows for every connected worktree.

This makes it easier to:

- Monitor parallel agent workflows
- Compare work across tasks
- Review uncommitted changes
- Resolve conflicts
- Compose commits from multiple worktrees

Each WIP row updates live as files change.

### Use WIP Scroll Markers

The Commit Graph minimap includes WIP scroll markers that highlight work-in-progress rows. You can customize marker colors or enable and disable markers in settings.

---

## Use Focus Branch Mode

Focus Branch mode reduces Commit Graph noise when working on a specific branch or task. When enabled, the Commit Graph scopes itself to the branch you select.

### Enable Focus Branch Mode

1. Open the Commit Graph.
2. Open the scope menu in the Commit Graph header.
3. Select a branch to focus.

While focused:

- The Commit Graph follows the branch's first-parent history
- The minimap zooms to the relevant commit range
- Simplify Merge History applies automatically
- Visual indicators show that the Commit Graph is scoped

---

## Pin a Branch in the Commit Graph

GitLens 18 allows you to pin an important branch to the leftmost column of the Commit Graph. This keeps long-lived reference branches like `main` or `develop` visible while you navigate complex histories.

### Pin a Branch

1. Right-click a branch row.
2. Select:

```text
Pin Branch
```

Pinned branches remain visible across Commit Graph sessions.

---

## Resolve Conflicts in the Commit Graph

Conflict resolution workflows extend directly into the Commit Graph. You can resolve merge conflicts from Commit Graph WIP rows or the Interactive Rebase editor. Conflict states appear inline inside the details panel.

---

## Open the Commit Graph in a New Window

GitLens 18 adds support for opening the Commit Graph in a detached window. This is especially useful for multi-monitor setups, large repositories, persistent review workflows, and parallel agent workflows.

### Open in a New Window

From the Commit Graph menu, select:

```text
Open in New Window
```

---

## Related Features

GitLens agent workflows work especially well alongside:

- Commit Composer
- AI Code Review
- Worktrees
- Launchpad
- Interactive Rebase
- GitKraken MCP integrations
