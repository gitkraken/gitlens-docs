---

title: AI Agents in GitLens
description: Monitor, resume, review and compose the work of Claude Code, Codex, GitHub Copilot CLI and OpenCode sessions in GitLens, with GitKraken Hooks, status pills and the Agent Sessions panel.
taxonomy:
    category: gitlens
last_updated: 2026-11

---

<kbd>Last updated: November 2026</kbd>

## Using AI Agents in GitLens

Follow and act on your AI coding agents from the Commit Graph, inside your IDE. GitLens shows each agent's status, its worktree, and the Git actions you can take on its work, so you do not have to manage agents through separate terminal tabs, apps, or extensions.

With GitLens, you can:

- Monitor active AI coding agents without leaving the IDE
- Track agent sessions tied to branches and worktrees
- Review AI-generated changes inside the Commit Graph
- Compose commits directly from agent-produced work
- Identify sessions waiting for input
- Manage parallel worktrees and Working Changes visually

GitLens tracks sessions from Claude Code, Codex, GitHub Copilot CLI, and OpenCode through GitKraken Hooks.

---

## Understand Agent Sessions

An agent session is a run of an AI coding agent in a repository, branch, or worktree. GitLens shows each session's status in several places, so you can monitor progress and act on changes without switching between terminals, chat panels, or external applications.

Agent sessions appear in:

- The Commit Graph overview cards
- The Commit Graph details panel
- The Agent Sessions sidebar panel

Each session shows its Git context, including:

- Associated branch
- Worktree
- Working changes
- Agent state
- Ahead/behind indicators
- Actions requiring attention

---

## Install GitKraken Hooks

GitLens tracks agent sessions using GitKraken Hooks, which give GitLens real-time visibility into each session. Hooks are available for Claude Code, Codex, GitHub Copilot CLI, and OpenCode.

You can install hooks from several locations in GitLens:

- The Commit Graph header
- The Agent Sessions sidebar banner
- The Integrations menu
- The Command Palette
- The **Agents** section of the GitLens settings, which lists each detected agent with its hooks status

### Install Hooks

1. Open the Command Palette.
2. Run `GitLens: Install GitKraken Hooks for All AI Agents`.
3. If prompted, reload VS Code or your IDE.

GitLens installs hooks for every supported agent it detects on your machine. To install hooks for a single agent, select **Manage Agents** in the Agent Sessions panel toolbar, then use the install button in that agent's **Hooks** column.

After you install the hooks, GitLens detects sessions from those agents and shows their state.

Codex does not run the installed hooks until you trust them. Run `/hooks` in Codex to trust the hooks, and trust them again after you reinstall them. GitLens shows this reminder when the install finishes, with a **Start Codex Session** button.

GitLens can answer permission requests directly only for Claude Code sessions. For other agents, GitLens shows the pending request, and you answer it in the agent's session.

### Uninstall Hooks

1. Open the Command Palette.
2. Run `GitLens: Uninstall GitKraken Hooks for All AI Agents`.

To uninstall hooks for a single agent, use the uninstall button in that agent's **Hooks** column in the **Agents** settings.

---

## Understand Agent Status Pills

Status pills show each agent's activity wherever its session appears. Status pills use color and animation to show which sessions need your attention.

### Running

The agent is processing changes or generating code. Running sessions show a pulse animation.

### Waiting for Input

The agent needs your input before it continues. Waiting sessions show an animation that draws attention and appear prominently in overview cards.

### Idle

The session is connected but is not performing actions.

### Past

The session has ended. Past sessions stay listed, dimmed, until you archive them or until they are removed after 30 days. To list past sessions in the Agent Sessions panel, turn on **Show Past Sessions** in the panel toolbar.

<figure>
  <img src="/wp-content/uploads/gl-agents-panel-past-sessions-01-v2@2x.png" class="help-center-img img-bordered" alt="The Commit Graph sidebar on its Agents panel with the Show Past Sessions toggle ringed, listing three sessions under the main worktree: a working Claude Code session running an edit, an idle OpenCode session and a dimmed past Codex session." />
</figure>

### Resume a Past Session

You can resume a past session from any supported agent: Claude Code, Codex, GitHub Copilot CLI, or OpenCode. Resume actions appear on the session's status pill, its card in the details panel, its session sheet, its Kanban card, and its row in the Agent Sessions panel. Each action names where the session resumes:

- **Resume in Terminal** opens a new integrated terminal in the session's directory and runs the agent's resume command.
- **Resume in Claude Code Extension** reopens the session in the Claude Code extension. This action appears only when the extension is installed and the session's directory is open as a workspace folder.

To choose from a list of sessions, right-click a Working Changes row in the Commit Graph, or a worktree in a side bar view, and select **Resume Agent Session...**. The **Resume Agent Session** quick pick lists that worktree's sessions under **Active** and **Past**. Select a session's destination button to resume it there.

<figure>
  <img src="/wp-content/uploads/gl-agents-resume-session-picker-01-v2@2x.png" class="help-center-img img-bordered" alt="The Resume Agent Session quick pick for the main worktree, with two Claude Code sessions under Active and two under Past; the focused past session shows its Resume in Terminal button, ringed." />
</figure>

If you select a session without choosing a destination, the `gitlens.agents.resumeTarget` setting decides where it resumes:

- **Not set** (default): GitLens asks where to resume the first time a session can open in either place. Select the pin button in that prompt to remember your choice.
- `terminal`: Always resume in a new integrated terminal.
- `extension`: Resume in the agent's VS Code extension when it can open the session, otherwise in a terminal.

A past session's sheet in the Commit Graph details panel shows a **Resume** button and an **Archive** action in its header.

<figure>
  <img src="/wp-content/uploads/gl-agents-session-sheet-past-01-v2@2x.png" class="help-center-img img-bordered" alt="The agent session sheet for a past Codex session, &quot;Update README with API rate limiting docs&quot;, in the Commit Graph details panel: the Past status, the Playground2026 worktree chip and the ringed Resume button with its Archive action, above the session's last prompt." />
</figure>

---

## Use the Agent Sessions Panel

Monitor all your active sessions in one place from the Agent Sessions panel. The panel opens from the Commit Graph sidebar, where it appears as **Agents**.

### Panel Features

The panel includes:

- Session status pills
- Branch and worktree associations
- Quick actions to open, resume, and archive sessions
- Past sessions, shown when **Show Past Sessions** is on
- List and tree layouts
- Session grouping by workspace or worktree

### Switch Between List and Tree Layouts

Use the layout toggle in the Agent Sessions panel toolbar to switch between list and tree layouts. Use the tree layout when you work across multiple repositories or worktrees.

### Act on a Session from Its Context Menu

Right-click a session in the Agent Sessions panel or in the Commit Graph details panel to act on it without opening the agent. The menu shows only the actions that apply to that session:

- **Allow**, **Always Allow**, and **Deny** answer a pending permission request.
- **Approve Plan**, **Reject Plan**, and **View Plan** handle a plan the agent proposed.
- **Open Session** opens a live session. For a past session, **Resume in Terminal** or **Resume in Claude Code Extension** resumes it.
- **Open Session in Kepler** opens the session in [Kepler](#start-tasks-and-reviews-in-kepler). It appears when Kepler is installed, for Claude Code, Codex, GitHub Copilot CLI, and OpenCode sessions.
- **Open in Integrated Terminal**, **Open Worktree**, and **Open Worktree in New Window** open the session's worktree.
- **Copy Last Prompt** and **Copy Session ID** copy session details to the clipboard.
- **Archive Session** removes a past session from the list.

<figure>
  <img src="/wp-content/uploads/gl-agents-session-context-menu-01-v2@2x.png" class="help-center-img img-bordered" alt="The right-click menu of a past Codex session in the Commit Graph's Agents panel, with Resume in Terminal ringed above Open in Integrated Terminal, Open Worktree, Open Worktree in New Window, Copy Last Prompt, Copy Session ID and Archive Session." />
</figure>

### Open a Session Sheet

Select a session card in the Agents section of the Commit Graph details panel to open that session's sheet in the details panel. The sheet gathers what you need to follow or pick up a session:

- The session's status, agent, and the worktree and branch it runs in
- Actions for the session's current state, such as **Open Session**, **Allow** and **Deny** for a pending request, or **Resume** and **Archive** for a past session. When Kepler is installed, the Kepler button (**Open Session in Kepler**) opens the session in Kepler.
- What the agent is doing now, and **File Activity** listing the files it read and edited
- The **Last prompt** and **First prompt**
- **Also worked in**, which lists other worktrees the session visited

Use the previous and next arrows in the sheet to move between agent sessions.

<figure>
  <img src="/wp-content/uploads/gl-agents-session-sheet-working-01-v2@2x.png" class="help-center-img img-bordered" alt="The agent session sheet in the Commit Graph details panel for a working Claude Code session, &quot;Add retry logic to the rate limiter middleware&quot;: its Working status, the main worktree chip and the Open Session button, the running Edit step, File Activity showing reports.ts being edited and user-management.ts read, and the session's last prompt." />
</figure>

---

## Review Agent-Generated Code

Review the work of your agents in the Commit Graph. From the Commit Graph details panel, you can:

- Inspect working changes
- Compare revisions
- Review AI-generated code
- Generate commits with Commit Composer
- Resolve conflicts
- Stage and unstage files

### Open the Commit Graph Details Panel

1. Open the Commit Graph.
2. Select a commit, branch, or Working Changes row.
3. If the details panel is hidden, toggle it.

You can dock the details panel in 2 places: the right side or the bottom of the Commit Graph. To switch between them, hold `Alt` while you toggle the panel.

### Jump from a Terminal to Its Worktree

When an agent runs in a terminal or a Claude Code conversation tab, you can go straight to the worktree it works in. Right-click the terminal tab, or the title of a terminal editor or Claude Code tab, and select one of these actions:

- **Open in Commit Graph** opens the Commit Graph with that worktree's Working Changes row selected.
- **Focus in Commit Graph** also focuses the Commit Graph on the worktree's branch.
- **Open in New Window** opens the worktree folder in a new window.

GitLens uses the worktree of the agent session running in the terminal. If no agent session runs there, GitLens uses the terminal's current folder. For a Claude Code tab, GitLens uses the worktree of the tab's agent session.

---

## Run AI Code Review in the Commit Graph

Review an agent's changes in the Commit Graph before you commit them or open a pull request. Select a Working Changes row, a commit, or a range of commits, and select **Review** in the details panel. Open each file to read its diff, mark it as viewed with its checkbox, or use **Exclude from Review** to set it aside. The checklist shows how many files you have viewed until the review is complete.

With GitKraken AI, select **Review Diff** to get findings grouped into focus areas and tagged by severity. Dismiss the findings you disagree with, comment on the ones you want to discuss, and send work back to your coding agent with **Address Findings with Agent**, **Address Focus Area with Agent**, or **Address with Agent** on a single finding. **Delete Findings** clears the AI findings and keeps your viewed files and your own comments.

Reading and checking off files works without AI. **Review Diff** uses GitKraken AI and requires GitLens Pro. For the full workflow, see [Review Changes in the Commit Graph](/gitlens/gl-review-changes/).

---

## Compose Commits from Agent Changes

Use Commit Composer in the Commit Graph details panel to turn working changes into structured commits without leaving the Commit Graph.

### Compose a Commit

1. Open the Commit Graph.
2. Select a Working Changes row.
3. Open the details panel.
4. Switch to Compose mode.
5. Review proposed commit groupings.
6. If needed, edit the generated commit message.
7. Commit the changes.

Compose mode supports:

- Multi-diff previews
- Staged and unstaged files
- Untracked files
- AI-generated commit messages

---

## Manage Multi-Worktree Workflows

The Commit Graph shows a Working Changes row for every connected worktree, not only for the active one. Use these rows to:

- Monitor parallel agent workflows
- Compare work across tasks
- Review uncommitted changes
- Resolve conflicts
- Compose commits from multiple worktrees

Each Working Changes row updates live as files change. The row shows its branch in an inline branch pill. Rows for other worktrees also carry a worktree row marker, and a row with a paused operation shows that state, such as **Rebasing**.

### Start an Agent Session in a Worktree

Right-click a Working Changes row in the Commit Graph, or a worktree in a side bar view, to launch an agent in that worktree:

- **Start Agent Session...** starts your default agent. If no default agent is set, GitLens asks you to choose one.
- **Start Agent Session With...** always asks which agent to start.
- **Resume Agent Session...** lists the worktree's sessions so you can [resume one](#resume-a-past-session).

A CLI agent starts in a new terminal at the worktree. The `gitlens.openInTerminalLocation` setting controls whether that terminal opens in the terminal panel or as an editor tab. A chat or extension agent receives a prompt to work in the worktree.

<figure>
  <img src="/wp-content/uploads/gl-graph-wip-row-start-agent-session-01-v2@2x.png" class="help-center-img img-bordered" alt="The right-click menu of the Working Changes row in the Commit Graph, with Start Agent Session... ringed above Start Agent Session With... and Resume Agent Session..., beneath Open in Integrated Terminal." />
</figure>

### Follow the Active Terminal

When the Commit Graph is visible, it follows your active terminal or Claude Code conversation tab and selects the Working Changes row of the worktree that terminal is in. If an agent session runs in the terminal, the Commit Graph selects that session's worktree. Following never opens the Commit Graph for you, and a tip appears the first time it moves the selection.

To stop following, select **Stop Following Active Terminal** from the Commit Graph's overflow menu, or set `gitlens.graph.followTerminal.enabled` to `false`. Select **Follow Active Terminal** to turn it back on.

By default, the Commit Graph ignores terminals in other repositories. Set `gitlens.graph.followTerminal.allowRepositorySwitching` to `true` to let it switch repositories.

### Use Working Changes Scroll Markers

The Commit Graph minimap includes scroll markers that highlight Working Changes rows. You can customize marker colors or enable and disable markers in settings.

---

## Use Focus Branch Mode

Use Focus Branch mode to show less of the Commit Graph while you work on a specific branch or task. When Focus Branch mode is on, the Commit Graph focuses on the branch you select.

### Enable Focus Branch Mode

1. Open the Commit Graph.
2. Open the branch visibility menu in the Commit Graph header.
3. Select **Focus Branch**, then select a branch to focus.

You can also right-click a branch and select **Focus on Branch**.

While a branch is focused:

- The Commit Graph follows the branch's first-parent history
- The minimap zooms to the relevant commit range
- Simplify Merge History applies automatically
- The branch visibility menu shows the focused branch, with the tooltip "Showing *branch* Only"

Focusing a branch is separate from scoping the Commit Graph to a worktree with **Scope to Worktree**.

---

## Pin a Branch in the Commit Graph

Pin an important branch to the leftmost column of the Commit Graph. Pinning keeps a long-lived reference branch, such as `main` or `develop`, visible while you move through a complex history.

### Pin a Branch

1. Right-click a branch row.
2. Select **Pin Branch**.

Pinned branches remain visible across Commit Graph sessions.

---

## Resolve Conflicts in the Commit Graph

Resolve merge conflicts from a Working Changes row in the Commit Graph or from the Interactive Rebase editor. Conflict states appear in the details panel.

---

## Open the Commit Graph in a New Window

Open the Commit Graph in a separate window, for example to:

- Use it on a second monitor
- Work in a large repository
- Keep a review open
- Follow parallel agent work

### Open in a New Window

From the Commit Graph menu, select **Open in New Window**.

---

## Start Tasks and Reviews in Kepler

Kepler is GitKraken's agentic development environment, a desktop app that runs AI agents across a task, from an issue or pull request to a merged change. If you use Kepler, GitLens can hand an issue, a pull request, or a repository to Kepler's **New task** composer, so you set up and run the work there instead of in VS Code. Kepler creates its own worktree for the task, so GitLens does not create a branch or worktree.

You can start a Kepler task from these places:

- **Start Task in Kepler**: Right-click a repository in the **Repositories** view.
- **Start Review in Kepler**: Right-click a pull request in a GitLens view, in the Launchpad view, or in the Commit Graph.
- **Open in Kepler**: Choose this option in the first step of **Start Work** or **Start PR Review**, above **Open in an agent** and **Continue manually**. To skip that step and always use Kepler, set `gitlens.ai.openInAgent` to `kepler`.

<figure>
  <img src="/wp-content/uploads/gl-kepler-start-task-menu-01-v3@2x.png" class="help-center-img img-bordered" alt="The Repositories view with the Playground2026 repository's context menu open and Start Task in Kepler ringed among its actions." />
  <figcaption style="text-align: center; color: #888">Starting a Kepler task from a repository</figcaption>
</figure>

GitLens offers Kepler only for providers that Kepler supports:

- **Pull requests**: GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Azure DevOps, and Bitbucket
- **Issues**: GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Azure DevOps, Jira, Linear, and Trello

Kepler options are not available in VS Code for the Web.

If you choose a Kepler option before Kepler is installed, GitLens asks how to continue:

- **Install Kepler** downloads and installs Kepler, shows the version and download size, and then carries on with your task. In a remote window, it opens the Kepler download page in your browser instead.
- **Learn More** opens the Kepler page in your browser.
- For a pull request review, **Start PR Review with Agent** and **Start PR Review** continue without Kepler.

You can also install Kepler at any time by running **GitLens: Install Kepler** from the Command Palette. When the install finishes, select **Open Kepler** in the notification to open it.

When Kepler is installed, you can open an agent session in Kepler too: select **Open Session in Kepler** in the session's [context menu](#act-on-a-session-from-its-context-menu), or the Kepler button on its session card or [session sheet](#open-a-session-sheet).

When GitLens detects Kepler on your computer, the Kepler step in the Welcome view counts as complete.

---

## Related Features

These features work with GitLens agent workflows:

- [Commit Composer](/gitlens/gitlens-features/#commit-composer-view-pro)
- [Review Changes](/gitlens/gl-review-changes/)
- [Worktrees](/gitlens/gl-worktrees/)
- [Launchpad](/gitlens/gl-launchpad/)
- [Interactive Rebase](/gitlens/gitlens-features/#interactive-rebase-editor)
- [GitKraken MCP integrations](https://help.gitkraken.com/mcp/mcp-tools-reference/)

These end-to-end workflows build on the same agent features:

- [Manage Parallel Development from the Commit Graph](/gitlens/gl-parallel-dev-workflow/)
- [Take Agent-Generated Work from Change to Merge](/gitlens/gl-agent-generated-work-end-to-end/)
- [Prepare Your Branch to Ship](/gitlens/gl-branch-prep-to-ship/)
