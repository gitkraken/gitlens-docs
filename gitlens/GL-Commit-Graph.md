---
title: GitLens Commit Graph
description: Visualize your repository history, branches, and collaborators with the GitLens Commit Graph in VS Code.
taxonomy:
    category: gitlens
last_updated: 2026-09

---

<kbd>Last updated: September 2026</kbd>

## Commit Graph

The Commit Graph is the starting point for working in GitLens. It brings repository history, branches, worktrees, Working Changes, pull requests, and supported agent activity into one connected workbench, so you can understand what's happening and move changes toward merge without rebuilding context across tools.

Built on a high-performance rendering engine, the graph stays responsive on large repositories, showing commits, branches, and collaborators in one place.

The Commit Graph is included in **GitLens Community** and available to everyone on public and local repositories &mdash; no account required. A GitLens Pro subscription or trial is required only for private repositories.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-01-v4@2x.png" class="help-center-img img-bordered" alt="Commit Graph in GitLens showing branches and commits" />
  <figcaption style="text-align: center; color: #888">Commit Graph overview in GitLens</figcaption>
</figure>

---

### Open the Commit Graph

The Commit Graph is the leading view in the GitLens sidebar. Click the GitLens icon in the Activity Bar to open it directly.

You can also open it from the Command Palette:
1. Open the Command Palette:
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
2. Type **Show Commit Graph** and select it.

The Commit Graph opens in a new tab, where you can scroll through history and resize column widths.

<figure>
  <img src="/wp-content/uploads/show-commit-graph.gif" class="help-center-img img-bordered" alt="GIF showing how to open the Commit Graph from the Command Palette" />
  <figcaption style="text-align: center; color: #888">Opening the Commit Graph from the Command Palette</figcaption>
</figure>

---

### Repository Information

At the top of the Commit Graph, you’ll see:

- **Repository** — the hosting provider's icon (hover it for the repository name; the editor tab is titled *Commit Graph: &lt;repository&gt;*)
- **Checked-out branch** (click to switch branches)
- **Last fetched time** — shown beside **Fetch** and in its hover (click **Fetch** to update)
- **Account** — the account button opens a popover with your plan and the **Synchronize Status**, **Manage Account**, **Sign Out**, and **Send Feedback** actions, plus rows for your connected integrations, your AI model and GitKraken AI usage, and your agents

You can enable automatic fetching with the `gitlens.graph.autoFetch.enabled` setting. When enabled, GitLens periodically runs `git fetch` for repositories visible in the Commit Graph, keeping your view up to date without manual refreshes.

<figure>
  <img src="/wp-content/uploads/gl-graph-info-01-v3@2x.png" srcset="/wp-content/uploads/gl-graph-info-01-v3@2x.png" class="help-center-img img-bordered" alt="The top of the Commit Graph in the editor area: the tab reads &quot;Commit Graph: Playground2026&quot;, the header shows the current branch (main) with Push and &quot;Fetch (1wk ago)&quot; buttons, and the Fetch button's hover popover lists the upstream (origin/main on GitHub), &quot;Last fetched last week&quot; and the Auto-fetch option" />
  <figcaption style="text-align: center; color: #888">Repository details in the Commit Graph toolbar</figcaption>
</figure>

---

### Availability

- The Commit Graph is included in **GitLens Community** and available to all users on **public** and **local** repositories, with no account required.
- A **GitLens Pro subscription or trial** is required only for use with **private repositories**.

---

### Feedback

You can send feedback to the GitKraken team without leaving the Commit Graph. Select the **Send Feedback...** (feedback) icon in the title bar of the Commit Graph editor tab or view, or select **Send Feedback** in the account popover. In the **Send Feedback** dialog, choose **General**, **Bug**, or **Feature**, enter your message, and select **Send Feedback**.

When you send a bug report, GitLens also opens a GitHub issue prefilled with your message so you can add more details. After you send a feature request, you can select **File on GitHub** to file it as a GitHub issue as well.

<figure>
  <img src="/wp-content/uploads/gl-graph-send-feedback-dialog.png" class="help-center-img img-bordered" alt="The Send Feedback dialog over the Commit Graph with its General, Bug and Feature choices, an empty Message box, links to the Help Center, Discussions and Issues, and the Cancel and Send Feedback buttons." />
  <figcaption style="text-align: center; color: #888">The Send Feedback dialog</figcaption>
</figure>

You can also share ideas in the [GitLens Commit Graph discussion on GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).

---

### Graph Sidebar

The Commit Graph includes an expandable sidebar panel that provides quick access to your repository refs. The sidebar lists branches, remotes, stashes, tags, and worktrees in both list and tree views. Click the sidebar toggle to expand or collapse it, or use the `gitlens.graph.sidebar.pinned` setting to keep it pinned open.

The sidebar contains several panels, including:

- **Overview**: Displays branch cards with Working Changes stats and upstream tracking information at a glance.
- **Agents**: Lists agent sessions so you can monitor and manage them. Branches with running agent sessions display status pills directly in the graph, so you can track agent activity at a glance. Select **Show Agent Kanban** in the sidebar to see sessions as a Kanban board.
- **Worktrees**: Lists your worktrees. Hover a worktree and select **Scope to Worktree** to work in it from the graph (see [Scope to a Worktree](#scope-to-a-worktree)).

Select **Show Past Sessions** in the **Agents** panel to include sessions that have ended. You can resume a past Claude Code, Codex, OpenCode, or GitHub Copilot CLI session with **Resume in Terminal**, or with **Resume in &lt;agent&gt; Extension** when the agent's VS Code extension can open it. Select **Archive Session** to remove a past session from the list. The `gitlens.agents.resumeTarget` setting controls where a session resumes when both are possible: GitLens asks the first time by default, `terminal` always resumes in a new integrated terminal, and `extension` uses the agent's extension when it can.

<figure>
  <img src="/wp-content/uploads/gl-graph-sidebar-01-v3@2x.png" class="help-center-img img-bordered" alt="The Commit Graph with its sidebar panel expanded on the Branches section, listing the repository's branches beside the graph; the rail also offers remotes, stashes, tags and worktrees" />
  <figcaption style="text-align: center; color: #888">The Commit Graph sidebar with branches, remotes, and worktrees</figcaption>
</figure>

#### Detail Sheets

Clicking on a branch, pull request, comparison, or agent session opens a slide-out detail sheet with rich information:

- **Branch sheet**: Shows branch details, tracking status, and recent commits.
- **Pull request sheet**: Displays PR description, reviewers, status checks, and stacked PR information when applicable.
- **Compare sheet**: Shows file-level comparison between branches or commits, with a pinned mode to keep the comparison visible while navigating.
- **Rebase summary sheet**: Appears after a rebase operation, summarizing what changed.
- **WIP conflict sheet**: Surfaces during conflict resolution to help resolve working changes.
- **Agent session sheet**: Opens when you click an agent session card or row. Shows the session's status, the files the agent read or edited, its first and last prompts, and other worktrees it also worked in. Use the previous and next buttons to move between sessions, and select **Resume** or **Archive** for a session that has ended.

#### Visualizations and Repository Health

Select **Show Visualizations & Health** in the sidebar to replace the graph with a visualization of your repository: **Visual History**, **Files Treemap**, **Commits Treemap**, **Agent Activity Treemap**, or **Repository Health**. You can also run **GitLens: Show Repository Health** from the Command Palette to open the Commit Graph on the Repository Health view.

**Repository Health** checks whether Git can run faster in the current repository. It suggests optimizations (**Untracked cache**, **File system monitor**, **Large-repository index**, **Sparse index**, and **Scheduled maintenance**) that you can enable, disable, or undo one at a time, and it offers **Run Maintenance Now**. When GitLens notices slow Git operations or a very large repository, a banner links to **Show Repository Health**. Nothing changes until you apply an optimization.

While VS Code is open, GitLens also runs safe, repository-local Git maintenance in the background: loose-object packing, incremental repack, and the commit-graph cache. It never applies the optimizations listed above automatically. To turn off the background maintenance, disable the `gitlens.gitOptimizations.enabled` setting; Repository Health requires this setting.

---

### Worktree Overview

See branch state, uncommitted changes, and unpushed commits across your worktrees. Each worktree has a pill above the graph; select it to jump to that worktree's Working Changes row.

Each pill shows the branch name, a dirty indicator when there are uncommitted changes, an unpushed arrow with an ahead count when commits have not been pushed, and changed file counts on hover. The `gitlens.graph.overviewBar.visibility` setting controls when the overview bar is shown: `always`, `worktrees` (when the repository has more than one worktree), `dirtyWorktrees` (the default, when another worktree has working changes or unpushed commits), or `never`.

<figure>
  <img src="/wp-content/uploads/gl-graph-wip-bar-01-v3@2x.png" class="help-center-img img-bordered" alt="The worktree overview above the Commit Graph, ringed, with one pill per worktree: main with its upstream legs, and the feature/api-hardening and docs/contributing-refresh worktree pills each showing a dirty indicator and an unpushed arrow" />
  <figcaption style="text-align: center; color: #888">Worktree pills above the graph</figcaption>
</figure>

#### Working Changes Rows

Each worktree's uncommitted work appears on a **Working Changes** row, which shows the worktree's branch as an inline pill. Working Changes rows of other worktrees carry a worktree row marker; hover it to see the worktree's name. When a rebase, merge, cherry-pick, or revert is paused in a worktree, its row shows a status pill such as **Rebase Paused** or **Resolve conflicts to continue rebasing**.

To run a VS Code task in a worktree, select the **Run Default Task** (play) button on its Working Changes row. The first time, GitLens asks you to choose the default task. <kbd>Alt</kbd>-click the button to choose a different task to run. While the task runs, the button reads **Running: &lt;task&gt;**, and clicking it shows the running task.

<figure>
  <img src="/wp-content/uploads/gl-graph-wip-run-default-task.png" class="help-center-img img-bordered" alt="The selected Working Changes row in the Commit Graph with its row actions showing; the ringed play button's tooltip reads Run Default Task, with Alt-click offering Choose Task to Run." />
  <figcaption style="text-align: center; color: #888">Running the default task on a Working Changes row</figcaption>
</figure>

You can also right-click a worktree's Working Changes row and select **Run Task on Worktree...** to pick any task. The picker lists recent and workspace tasks first, with **All Tasks...** for the rest. Select a task's checkmark to set it as the default task, or select it again to unset it.

<figure>
  <img src="/wp-content/uploads/gl-worktree-run-task-picker.png" class="help-center-img img-bordered" alt="The Run Task on Worktree quick pick for the api-hardening worktree listing the workspace tasks Run unit tests, Lint and Start dev server above All Tasks; the focused row's ringed checkmark sets that task as the default." />
  <figcaption style="text-align: center; color: #888">Choosing a task and setting the default</figcaption>
</figure>

#### Scope to a Worktree

Scope the graph to another worktree to work in it without leaving the Commit Graph. While the graph is scoped, it acts as if you had opened that worktree: you see its branch and its changes, and anything you commit, push, or pull happens there. To scope the graph, do one of the following:

- In the sidebar **Worktrees** panel, hover a worktree and select **Scope to Worktree**. <kbd>Alt</kbd>-click the action to focus on the worktree's branch instead.
- Right-click a worktree's Working Changes row and select **Scope to Worktree**.
- Double-click another worktree's Working Changes row or its pill in the overview bar.

<figure>
  <img src="/wp-content/uploads/gl-graph-worktree-scope-action.png" class="help-center-img img-bordered" alt="The Commit Graph side bar on its Worktrees panel, listing main, feature/api-hardening and docs/contributing-refresh; the hovered feature/api-hardening row shows its inline actions with Scope to Worktree ringed." />
  <figcaption style="text-align: center; color: #888">Scope to Worktree in the sidebar Worktrees panel</figcaption>
</figure>

GitLens marks the scope in yellow on the header's branch pill, which names the worktree's branch, and on the worktree's row in the sidebar. To return to your active worktree, select **Unscope Worktree** on the branch pill or on the worktree's sidebar row.

<figure>
  <img src="/wp-content/uploads/gl-graph-worktree-scoped.png" class="help-center-img img-bordered" alt="The Commit Graph scoped to the feature/api-hardening worktree: the titlebar carries the scoped tint, the branch pill names the worktree's branch and the ringed Unscope Worktree control beside it returns the graph to the main worktree." />
  <figcaption style="text-align: center; color: #888">The Commit Graph scoped to a worktree</figcaption>
</figure>

Two settings control scoping. You can open them from **Worktree Scope Settings...** in the filter dropdown (see [Filter Options](#filter-options)):

- `gitlens.graph.scopeBehavior`: `scopeAndFocus` (default) also focuses the worktree's branch, narrowing the visible rows. `scope` keeps every commit visible.
- `gitlens.graph.doubleClickWorktreeAction`: `scope` (default) scopes the graph when you double-click a worktree's Working Changes row, overview bar pill, or sidebar row. `focus` toggles the branch focus instead.

#### Follow the Active Terminal

When the Commit Graph is visible, it follows your active terminal. Switching to a terminal, or to a Claude Code conversation tab, selects the Working Changes row of the repository or worktree that the terminal is in. If an agent session runs in the terminal, the graph follows the session's worktree. The graph doesn't open itself to follow a terminal.

- To turn following off, select **Stop Following Active Terminal** in the **More Actions…** (⋯) menu of the Commit Graph editor tab or view. Select **Follow Active Terminal** to turn it back on. Both commands change the `gitlens.graph.followTerminal.enabled` setting, which is on by default.
- By default, the graph ignores terminals in other repositories. Enable `gitlens.graph.followTerminal.allowRepositorySwitching` to let the graph switch to another repository.

<figure>
  <img src="/wp-content/uploads/gl-graph-follow-terminal.png" class="help-center-img img-bordered" alt="The Commit Graph following the active terminal: with the api-hardening terminal focused in the panel below, the graph has selected that worktree's Working Changes row." />
  <figcaption style="text-align: center; color: #888">The Commit Graph following the active terminal</figcaption>
</figure>

#### Ref Find

The ref-finder widget provides a typeahead search for quickly jumping to any branch, tag, or Working Changes row in the graph. The `gitlens.graph.refFindAutoHide` setting controls whether the widget auto-hides after selecting a result.

---

### Details Panel

The Commit Graph includes an embedded details panel that shows information about the selected commit or your current working changes. The details panel replaces the former standalone Graph Details view and is integrated directly within the graph.

When you select a commit, the details panel displays the commit message, author, changed files, and diff. When viewing working changes, it shows your uncommitted modifications. The panel can be positioned to the right or bottom of the graph using the `gitlens.graph.details.location` setting. An `auto` option is also available, which switches between right and bottom placement based on the graph width. The `gitlens.graph.details.maximizeOnMode` setting automatically maximizes the details panel when entering compose, review, or resolve modes.

The details panel supports multiple modes:

- **Compare mode**: Opens comparisons directly within the graph, showing Ahead, Behind, and All views between branches or commits. This replaces navigating to the standalone Search and Compare view for graph comparisons.
- **Compose mode**: Provides an integrated commit composition experience, letting you craft commit messages and select files to commit without leaving the graph. You can also access Compose from the graph context menu.
- **Recompose**: Helps clean up existing branch history by reorganizing selected commits into a clearer, more intentional sequence. GitKraken AI can propose the new structure and commit messages for you to review and refine before applying the result. Available from the graph context menu, Recompose can operate on an entire branch, from a specific commit, or on selected commits.
- **Review mode**: Helps you inspect commits or Working Changes before they move forward. GitKraken AI can surface potential bugs, security issues, and other areas that deserve attention &mdash; tagged by severity &mdash; while you decide what needs to change. You can configure separate AI models for compose and review using per-feature model scoping, and customize review behavior with the `gitlens.ai.reviewChanges.customInstructions` setting.

<figure>
  <img src="/wp-content/uploads/gl-graph-details-panel-01-v2@2x.png" class="help-center-img img-bordered" alt="The Commit Graph with the embedded details panel on the right, showing commit message, author, and changed files for the selected commit" />
  <figcaption style="text-align: center; color: #888">Embedded details panel showing commit information</figcaption>
</figure>

#### Next Steps

When you select a Working Changes row that has no uncommitted changes, the details panel suggests **Next steps** for the branch. Depending on the branch, the list offers actions such as publishing the branch, pulling or pushing commits, creating or viewing its pull request, and reviewing or recomposing its changes. If the branch has diverged from its upstream, the list starts with a **Diverged from &lt;remote&gt; — N behind, M ahead** step. Select **Pull** to bring in the remote commits, or select **Force Push** beside it to overwrite the remote branch with your local commits.

<figure>
  <img src="/wp-content/uploads/gl-graph-next-steps-diverged.png" class="help-center-img img-bordered" alt="The Commit Graph details panel for a clean Working Changes row on fix/settlement-retry, whose Next steps list opens with the ringed &quot;Diverged from origin — 1 behind, 1 ahead&quot; step offering Pull and, as its alternate, Force Push." />
  <figcaption style="text-align: center; color: #888">The diverged-branch step in Next steps</figcaption>
</figure>

#### Multi-file Selection

File lists in the details panel (Working Changes, commit details, compare, compose, and review panels) support multi-file selection using <kbd>Shift</kbd>-click and <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>-click. With multiple files selected, you can perform batch operations including stage, unstage, discard changes, and stash. Individual files also show inline action buttons for quick single-file operations.

To ignore an untracked file, right-click it in the Working Changes file list and select **Add to .gitignore**. With several files selected, the action applies to the untracked ones. GitLens adds each file as a pattern anchored to the repository root, such as `/local-config.json`, to the `.gitignore` file at the root of the repository. GitLens creates the file if it doesn't exist and opens it so you can see what was added.

<figure>
  <img src="/wp-content/uploads/gl-wip-add-to-gitignore.png" class="help-center-img img-bordered" alt="The Commit Graph details panel listing the Working Changes files, with the context menu open on the untracked local-config.json and its ringed Add to .gitignore action beneath the stage and discard actions." />
  <figcaption style="text-align: center; color: #888">Adding an untracked file to .gitignore</figcaption>
</figure>

#### Co-authors

When composing a commit in the graph, use the **Add Co-authors** button to append `Co-authored-by` trailers to your commit message.

#### Navigation and Keyboard Shortcuts

The details panel includes back and forward navigation buttons for browsing through previously viewed commits.

Press <kbd>?</kbd> in the Commit Graph to open the **Keyboard Shortcuts** sheet, which lists all graph shortcuts organized by category. Frequently used shortcuts include:

- <kbd>/</kbd>: Find a branch, tag, or worktree.
- <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>F</kbd>: Search commits.
- <kbd>1</kbd> through <kbd>0</kbd>: Jump to a recent worktree.
- <kbd>Alt</kbd> + <kbd>1</kbd> through <kbd>Alt</kbd> + <kbd>8</kbd>: Toggle a sidebar panel.
- <kbd>Alt</kbd> + <kbd>K</kbd>, <kbd>V</kbd>, <kbd>M</kbd>, <kbd>S</kbd>, or <kbd>D</kbd>: Toggle the Agent Kanban, visualizations, minimap, sidebar, or details panel.
- <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>Up</kbd>/<kbd>Down</kbd>: Follow the branch to the previous or next commit.
- <kbd>Alt</kbd> + <kbd>Up</kbd>/<kbd>Down</kbd>: Jump to the previous or next fork point.
- <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>Left</kbd>/<kbd>Right</kbd>: Switch branch at a fork.

Hold <kbd>Ctrl</kbd> or <kbd>Alt</kbd> while you hover a commit to highlight its lane and the commits in its chain, dimming the rest of the graph.

To change or turn off shortcuts, select **Customize…** in the Keyboard Shortcuts sheet to open the `gitlens.graph.shortcuts` settings. Hover a shortcut in the sheet to see its id. In `gitlens.graph.shortcuts.overrides`, set an id to a different key combination, or to `false` to turn it off. To turn off all customizable shortcuts, disable `gitlens.graph.shortcuts.enabled`. Navigation keys such as the arrow keys, <kbd>Enter</kbd>, and <kbd>Esc</kbd> always work.

<figure>
  <img src="/wp-content/uploads/gl-graph-keyboard-shortcuts-sheet.png" class="help-center-img img-bordered" alt="The Commit Graph's Keyboard Shortcuts sheet listing the graph's shortcut groups with their key chips; the footer notes that holding Ctrl or Alt highlights the lane and the ringed Customize link opens the shortcut settings." />
  <figcaption style="text-align: center; color: #888">The Commit Graph Keyboard Shortcuts sheet</figcaption>
</figure>

---

### Configuration and Layout

You can configure the Commit Graph to control what information is shown and how it is displayed.

#### Graph Style

The `gitlens.graph.style` setting controls the overall row layout of the graph. Options include `table` (columnar layout with visible borders), `list` (compact list layout), and `auto` (switches based on available width).

#### Columns
- Drag and drop column headers to rearrange columns.
- Right-click a column header to toggle columns on or off.
- The **Changes** column visualizes added and deleted lines per commit. The `gitlens.graph.changesColumn.mode` setting controls the display style: `numbers` (numeric counts), `squares` (colored blocks), `bar` (horizontal bar), or `bipolar` (split additions/deletions bar).
- **Column grouping** is enabled by default, combining the Graph and Branches/Tags columns into a compact layout. To change it, right-click a column header and select **Group Graph Column**, **Ungroup Graph Column**, **Group Branches / Tags Column**, or **Ungroup Branches / Tags Column**. Lanes can be folded to collapse inactive branches and reduce visual clutter.
- To reuse a layout, right-click a column header and select **Save as Default Layout**. GitLens saves your columns and panel layout, and new workspaces open with it. Select **Apply Saved Layout** to apply the saved layout to the current workspace, or **Reset Layout** to restore the original layout.

#### Lane Colors and Row Markers

The graph uses perceptually-uniform lane colors that are tuned for both dark and high-contrast themes. Row markers indicate important commits at a glance:
- **Green marker**: HEAD commit
- **Blue marker**: upstream tracking commit
- **Worktree marker**: Working Changes row of another worktree
- **Colored reference pills**: merge target and other branch roles

By default, each row shows one branch or tag pill and collapses the rest behind a **+N** badge. To show more pills on a row, set `gitlens.graph.refs.maxInline` to a number from 1 to 10, or to `auto` to fit as many pills as the row allows.

<figure>
  <img src="/wp-content/uploads/gl-graph-ref-pills-overflow.png" class="help-center-img img-bordered" alt="The top of the Commit Graph where the commit carrying origin/main and two worktree branches shows a single branch pill with a ringed +2 badge folding the other branches (and a separate +1 tag badge), the default one-pill-per-row layout." />
  <figcaption style="text-align: center; color: #888">The default layout, with extra refs behind a +N badge</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-graph-ref-pills-inline.png" class="help-center-img img-bordered" alt="The same Commit Graph rows with the branch and tag pill cap set to auto: the commit carrying origin/main and the two worktree branches shows each branch as its own inline pill, with only the commit's tag folded behind a +1 tag badge." />
  <figcaption style="text-align: center; color: #888">Several branch pills per row with the pill cap set to auto</figcaption>
</figure>

To show pills on their own line above the commit, set `gitlens.graph.refs.layout` to `stacked`; rows with pills become taller. The `gitlens.graph.refs.maxStacked` setting (default `auto`) limits the pills on that line. The stacked layout applies when the graph style is `table` and the Branches/Tags column is grouped with the Graph column. You can also change these options in the GitLens settings (**GitLens: Open Settings**).

<figure>
  <img src="/wp-content/uploads/gl-column-settings-v2@2x.png" class="help-center-img img-bordered" alt="Commit Graph settings menu showing options to hide the Author, Date, SHA, Changes, and other columns, switch the graph layout, and use a compact layout" />
  <figcaption style="text-align: center; color: #888">Commit Graph column settings</figcaption>
</figure>

#### Layout Options
- **Panel Layout**: Displays the Commit Graph in the bottom panel (near the Terminal) with a details view alongside it.
- **Editor Layout**: Opens the Commit Graph in an editor tab.
- You can open the Commit Graph in both layouts simultaneously.

To switch layouts:
1. Open the **More Actions…** (⋯) menu in the top-right corner of the Commit Graph editor tab (or of the Commit Graph view in the side bar).
2. Choose **Prefer Commit Graph in Editor** or **Prefer Commit Graph as a View**.

The same menu holds **Follow Active Terminal** and **Stop Following Active Terminal**, which control whether the graph follows your active terminal (see [Follow the Active Terminal](#follow-the-active-terminal)).

The `gitlens.graph.editorOpeningBehavior` setting controls how files open from the graph — either in the active editor group or automatically based on context. You can also open the Commit Graph in a separate VS Code window using the **GitLens: Open Commit Graph in New Window** command.

<figure>
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location-01-v3@2x.png" class="help-center-img img-bordered" alt="The Commit Graph open in the editor area with the tab's More Actions (…) menu expanded, listing Prefer Commit Graph in Editor and Prefer Commit Graph as a View among the editor actions" />
  <figcaption style="text-align: center; color: #888">Switching between Editor and Panel Layout</figcaption>
</figure>

You can also open the Commit Graph from a terminal. Right-click a terminal tab in the Terminal panel, or open the **More Actions…** (⋯) menu of a terminal editor tab, and choose one of these actions for the worktree the terminal is in:

- **Open in Commit Graph**: Opens the Commit Graph with the worktree's Working Changes row selected.
- **Focus in Commit Graph**: Also scopes the graph to the worktree and keeps the details panel closed. A terminal editor tab shows this action as a button in its title bar.
- **Open in New Window**: Opens the worktree folder in a new VS Code window.

Claude Code conversation tabs offer the same actions in their title bar and tab context menu, for the worktree of the agent session in that tab.

<figure>
  <img src="/wp-content/uploads/gl-terminal-editor-worktree-actions.png" class="help-center-img img-bordered" alt="A terminal opened as an editor tab, its Focus in Commit Graph title button ringed and the tab's More Actions menu expanded to show Open in Commit Graph and Open in New Window for the worktree the terminal is in." />
  <figcaption style="text-align: center; color: #888">Commit Graph actions on a terminal editor tab</figcaption>
</figure>

#### Compact Graph Layout
- Select the gear in the **Graph** column header and choose **Use Compact Graph Column** to reduce visual complexity.
- When the **Author** column is resized to minimum width, it shows avatars instead of text.
- Columns that become too narrow automatically switch to icons to preserve information.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-compact-graph-01-v3@2x.gif" class="help-center-img img-bordered" alt="Compact Commit Graph layout toggle showing the graph switching from normal to compact view with icons and avatars" />
  <figcaption style="text-align: center; color: #888">Compact Graph and Author column with avatars</figcaption>
</figure>

#### Scroll Markers
Scroll markers highlight key points in the Commit Graph, including:
- Checked-out branches
- Selected rows
- Search results
- Working Changes rows

Use scroll markers to quickly jump to important points such as `HEAD` or refs. You can toggle this feature in the [Commit Graph settings](/gitlens/gitlens-features/#settings).

The `gitlens.graph.showWorktreeWipStats` setting displays file add/change/delete statistics on worktree Working Changes rows. The `gitlens.graph.minimap.reversed` setting reverses the minimap direction.

<figure>
  <img src="/wp-content/uploads/gl-scroll-markers.png" class="help-center-img img-bordered" alt="Commit Graph scroll markers indicating branch and search results" />
  <figcaption style="text-align: center; color: #888">Scroll markers in the Commit Graph</figcaption>
</figure>

---

### Settings

Adjust Commit Graph settings from the Command Palette:
- macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
- Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

Search for **GitLens: Open Settings**.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-settings-01-v4@2x.png" class="help-center-img img-bordered" alt="VS Code Command Palette filtered to &quot;GitLens: Settings&quot; with the GitLens: Open Settings command highlighted, the step that opens the GitLens settings for the Commit Graph" />
  <figcaption style="text-align: center; color: #888">Opening Commit Graph settings</figcaption>
</figure>

<div class='callout callout--basic'>
  <p>Note: The <code>gitlens.graph.showDetailsView</code> setting and the standalone Graph Details view have been removed. The details panel is now always embedded in the Commit Graph. The <code>gitlens.proxy</code> setting has also been removed.</p>
</div>

---

### Rich Commit Search

The Commit Graph supports rich search across your entire repository. You can search by commit, message, author, file, or even specific code changes.

#### How to Search
1. Type search criteria in the search bar.
2. Use the arrow icons or keyboard shortcuts to navigate results:
   - Next result: <kbd>F3</kbd> (Windows/Linux) or <kbd>Cmd</kbd> + <kbd>G</kbd> (macOS)
   - Previous result: <kbd>Shift</kbd> + <kbd>F3</kbd> (Windows/Linux) or <kbd>Shift</kbd> + <kbd>Cmd</kbd> + <kbd>G</kbd> (macOS)

<figure>
  <img src="/wp-content/uploads/gl-rich-commit-search-02-v3@2x.png" class="help-center-img img-bordered" alt="Commit Graph search bar highlighting results" />
  <figcaption style="text-align: center; color: #888">Searching commits in the Commit Graph</figcaption>
</figure>

You can also:
- Jump to the **first or last result** by holding <kbd>Shift</kbd> while clicking the arrow icons.

<figure>
  <img src="/wp-content/uploads/gl-commit-search-moving-arrow-keys-02-v4@2x.gif" class="help-center-img img-bordered" alt="Navigating commit search results with arrow keys in the Commit Graph, showing the selection jumping between matching commits" />
  <figcaption style="text-align: center; color: #888">Navigating commit search results</figcaption>
</figure>

#### Search Filters
Use these filters in the search bar:
- `commit:`
- `message:`
- `-message:` excludes commits whose message contains a term (you can't combine it with `message:`)
- `author:`
- `committer:` filters by the person who committed the change (supports `@me`)
- `file:`
- `change:`
- `type:merge` shows only merge commits (`is:merge` also works)
- `@me`

You can also use **natural language search** to describe what you are looking for in plain English. GitLens uses AI to convert your query into the appropriate structured search operators; hover the search query to see how GitLens interpreted it. A request such as "only my commits" filters the graph to the matches, and a request such as "take me to" jumps to the first match. If a natural-language search finds nothing, GitLens suggests broader searches with their result counts, such as searching without the date filter or across all branches. If AI isn't available, select **Search as text instead**. Time-based operators such as `after:` and `before:` are available for filtering commits by date.

Additional options:
- Match all
- Match case
- Use regular expressions

If a regular expression isn't valid, GitLens matches the pattern literally instead. When that search finds nothing, select **Match literally** to turn off regular expressions, or **Fix with AI** to have AI repair the pattern. When there are more results than the graph has loaded, a bar shows how many results are loaded, with **Load More Results…** to load the rest.

<figure>
  <img src="/wp-content/uploads/gl-search-options-01-v3@2x.png" class="help-center-img img-bordered" alt="Commit Graph search box with the query &quot;fix&quot; and a ring around the search option toggles at its right end: Match Case, Match Whole Word, Use Regular Expression and Match All, next to the 1 of 6 result counter" />
  <figcaption style="text-align: center; color: #888">Commit Graph search options</figcaption>
</figure>

### Full Context Menu Support

You can right-click a branch, commit, tag, author, Working Changes row, or column header (Author, Commit Date/Time, or SHA) to access context menu actions.

<figure>
  <img src="/wp-content/uploads/gl-context-menu.gif" class="help-center-img img-bordered" alt="Context menu in Commit Graph with options for branches, commits, and authors" />
  <figcaption style="text-align: center; color: #888">Commit Graph context menu options</figcaption>
</figure>

Helpful context menu actions include:

- **Compare with Common Base**: Review changes that would occur if the selected branch were merged by comparing its common ancestor (merge base) with the current branch.  
- **Open All Changes with Common Base**: Review all merge changes in the multi-diff editor.
- **Squash Commits**: Squash selected commits into one without opening the rebase editor.
- **Drop Commits**: Remove selected commits from history.
- **Reword Commit**: Change a commit message in place.
- **Modify Commit**: Amend a commit's contents.
- **Undo Commit**: Appears as an inline action on HEAD commit rows, soft-resetting the commit to return changes to the working tree.
- **Push to Commit**: Appears as an inline cloud-upload icon on unpushed commit rows, pushing all commits up to and including the selected one.
- **Fixup Commit...**: Selects the Working Changes row and fills in the commit message as `fixup! <subject>` for the selected commit. The commit button becomes a **Commit Fixup** split button whose menu offers **Commit Fixup & Squash**.
- **Squash Fixups...**: Available on the current branch. After you confirm, squashes each `fixup!` commit on the branch into its target commit.
- **Push Tag...**: Pushes the selected tag to a remote.
- **Copy Worktree Path**: Copies the path of the worktree where the selected branch is checked out.

<figure>
  <img src="/wp-content/uploads/gl-graph-fixup-commit-box.png" class="help-center-img img-bordered" alt="The Commit Graph details panel for the Working Changes row with the message &quot;fixup! feat: add status field&quot; in the commit box; the ringed Commit Fixup split button replaces Commit, its menu offering Commit Fixup &amp; Squash." />
  <figcaption style="text-align: center; color: #888">Committing a fixup from the details panel</figcaption>
</figure>

Right-click a Working Changes row for actions on its worktree:

- **Start Agent Session...**: Starts a session in the worktree with your default agent, or asks you to choose an agent if you haven't set one. A CLI agent starts in a terminal at the worktree.
- **Start Agent Session With...**: Asks you to choose the agent before starting the session.
- **Run Task on Worktree...**: Runs a VS Code task in the worktree (see [Working Changes Rows](#working-changes-rows)).
- **Copy Branch Name**: Copies the name of the branch checked out in the worktree.

---

### Auto-Rebase <code>PRO</code>

Auto-Rebase carries a rebase forward through the conflicts GitKraken AI can resolve confidently. When conflicts arise, GitLens analyzes each one and resolves it only when its confidence meets the threshold you configure; anything below that threshold pauses the rebase so you can resolve it yourself.

- Run **GitLens: Auto-Rebase...** from the Command Palette, or choose **Auto-Rebase** when you rebase from the graph context menu (for example, **Rebase Current Branch onto Branch...**).
- If a rebase is already paused, run **GitLens: Continue with Auto-Rebase** or select **Continue with Auto-Rebase** in the paused-operation bar.
- The `gitlens.ai.autoRebase.confidenceThreshold` setting (0 to 1) controls how confident the AI must be before automatically applying a resolution.
- Use `gitlens.ai.resolveConflicts.customInstructions` to provide custom instructions that guide how the AI resolves conflicts.
- When Auto-Rebase pauses, its notification offers **Review & Resolve**, **Resume with AI**, and **Abort Rebase**. The resolve panel in the graph also offers **Resume with AI** and **Abort Rebase**.
- If the result is unsatisfactory, select **Undo** in the completion notification or **Undo Rebase** in the rebase summary sheet to reset the branch to its pre-rebase state.

During the rebase, a progress animation appears in the graph to indicate the operation is in progress. A rebase summary sheet opens in the sidebar when the operation completes.

---

### Pull Request Information

For GitHub and GitLab, the Commit Graph displays a Pull Request icon for any branch with an open pull request. To enable this, connect a [rich integration](/gitlens/settings/#remote-provider-integration-settings).

For GitHub repositories, the graph also recognizes **stacked pull requests**. When a branch is part of a PR stack, the PR sheet in the sidebar shows the stack ID, the total number of PRs in the stack, and the current PR's position. Merge operations are stack-aware, distinguishing between merging a single layer and merging the entire stack.

<figure>
  <img src="/wp-content/uploads/gl-pull-request-icon-01-v3@2x.png" class="help-center-img img-bordered" alt="The Commit Graph with the fixture/code-suggest-demo branch pill ringed: after the branch name and its origin remote the pill carries the pull-request icon, which marks the branch as having an associated open pull request" />
  <figcaption style="text-align: center; color: #888">Pull request icon in Commit Graph</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

The Commit Graph shows refs to your remotes, branches, and tags.  
- Right-click a branch or tag pill and select **Hide Local Branch**, **Hide Remote Branch**, or **Hide Tag**. To hide whole classes of refs, use the filter dropdown next to the search box (see [Filter Options](#filter-options)).  
- To hide every branch of a remote, including branches added later, right-click one of its remote branches, or the remote in the sidebar **Remotes** panel, and select **Hide Remote**.
- To show them again, hover over the **Hide** option at the top of the Commit Graph and select the desired refs. Hidden refs also stay in the sidebar **Branches**, **Remotes**, and **Tags** panels, dimmed and marked **Hidden**. Right-click one and select **Show Local Branch**, **Show Remote Branch**, **Show Tag**, or **Show Remote**.
- If you jump to a hidden ref, the graph tells you that it's hidden and offers to show it.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs-01-v3@2x.gif" class="help-center-img img-bordered" alt="Hiding a branch in the Commit Graph: right-clicking the conflict-branch ref opens its context menu, and choosing Hide Local Branch removes the ref from the graph" />
  <figcaption style="text-align: center; color: #888">Hiding refs in the Commit Graph</figcaption>
</figure>

#### Filter Options
Access filters from the dropdown menu to choose:  
- **All Branches**: Displays all branches.  
- **Current Branch**: Displays the current branch and its upstream remote.  
- **Smart Branches**: Displays only the relevant branches — the current branch, its upstream, and its base or target branch.  
- **Agent Branches**: Displays only branches with running agents, or with agents idle for less than 24 hours.
- **Favorited Branches**: Displays only branches you starred as favorites.
- **Focus Branch**: Focuses the graph on a single branch you choose, filtering out unrelated history. While a branch is focused, the dropdown reads **Focused**. If you jump to a ref outside the focus, select **Clear Focus** to show it.

When one of these options narrows the graph, a bar shows how many branches are loaded, with **Load More…** to load the rest.

Additional options let you hide or show:  
- Remote-only branches  
- Stashes  
- Tags  

You can also dim merge commit rows for clarity.

<figure>
  <img src="/wp-content/uploads/gl-filter-options-2-01-v3@2x.png" class="help-center-img img-bordered" alt="Commit Graph filter options for branches, tags, and stashes" />
  <figcaption style="text-align: center; color: #888">Commit Graph filter options</figcaption>
</figure>

---

### Minimap

The Minimap provides a high-level overview of repository activity. It shows commits, branches, HEAD/upstream, and more, letting you quickly jump to points of interest.

- Select the **Toggle Minimap** icon in the Commit Graph toolbar to enable or disable it.  
- Use the gear at the right end of the minimap to switch between **Commits** or **Lines Changed** views.  
- Toggle markers on or off from the same menu.
- The `gitlens.graph.minimap.defaultVisibility` setting controls when the minimap appears: `hidden`, `onSearch` (default, shows during search), or `always`.

<figure>
  <img src="/wp-content/uploads/gl-minimap-2.png" class="help-center-img img-bordered" alt="Commit Graph Minimap enabled in the toolbar" />
  <figcaption style="text-align: center; color: #888">Commit Graph Minimap</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-minimap-gl-settings-01-v4@2x.png" class="help-center-img img-bordered" alt="Commit Graph with the minimap strip above the rows and its Minimap Options popover open: a Minimap group with Commits (selected), Lines Changed and Reverse Direction, and a Markers group with checkboxes for Local Branches, Remote Branches, Pull Requests, Stashes, Tags and Worktrees" />
  <figcaption style="text-align: center; color: #888">Minimap settings and options</figcaption>
</figure>

#### Minimap Overview
- **Reads left to right**: Left = most recent, right = older.  
- **Highlighted region**: Area currently in view.  
- **Green lines**: HEAD.  
- **Yellow lines**: Search results.  
- **Upper row markers**:  
  - Blue blocks = remote branches  
  - Brown blocks = tags  
- **Lower row markers**:  
  - Pink blocks = stashes  
  - Blue blocks = local branches  

<div class='callout callout--basic'>
  <p>Note: We’d love your feedback on the Minimap. Please share it on the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>GitHub Discussion board</a>.</p>
</div>