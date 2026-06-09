---
title: GitLens Release Notes
description: GitLens Release Notes
taxonomy:
  category: gitlens
---

Find out what's new, what's fixed, or just take a trip down memory lane remembering those bugs of yesterday.

Check out our [Changelog](https://github.com/gitkraken/vscode-gitlens/blob/main/CHANGELOG.md) to see linked issues and past changes.

<a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank" class="button button--basic ">Install Current Version Now</a>

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos \
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Community, Pro, etc

---

<a id="v18-1"></a>

## Version 18.1

#### Tuesday, June 9, 2026

GitLens 18.1 introduces powerful new ways to manage your workflow directly from the Commit Graph. You can now squash, drop, reword, and reorder commits without leaving the Graph, as well as push or undo a commit in a single click. A new working changes bar at the top of the Graph also makes it easier than ever to jump between worktrees and track changes.

This release also improves the working changes (WIP) experience, allowing you to discard changes, copy as a patch, add co-authors, and jump between changes and commits. Finally, we've added multi-select file actions to the Details and Inspect views, and refined the experimental Agent Activity Treemap with a live, decaying heatmap.

<img src="/wp-content/uploads/gl-18-1-hero.png" class="help-center-img img-bordered">

### Edit History, Directly in the Commit Graph

You no longer need to drop into the _Interactive Rebase Editor_ for everyday history edits &mdash; the _Commit Graph_ now does them inline. Right-click a commit on the current branch to **Reword** its message, or select two or more contiguous commits to **Squash** them into one (reviewing and editing the combined message, or keeping just the oldest). Select any set of commits to **Drop** them outright. And when you do want the full editor, a new **Modify Commits (Interactive Rebase)** action opens the _Interactive Rebase Editor_ scoped from the commits you selected, ready for squashing, rewording, reordering, dropping, and editing.

### A Deeper Working Changes Experience

The working changes (WIP) experience across the _Commit Graph_ and _Inspect_ view gets a major lift in 18.1 with more actions and better visibility of working changes across worktrees.

- **Working changes bar** &mdash; a horizontal bar above the Graph shows a pill for every worktree with uncommitted changes (primary and secondary alike), with its branch, agent status, and a hover breakdown of changed files. Click a pill to reveal and select that worktree's changes and open its details.
- **Discard changes** &mdash; discard working changes per-file or in bulk, with safe partial discard for files that have both staged and unstaged changes (the first discard drops only the unstaged portion, preserving what's staged).
- **Copy Changes (Patch)** &mdash; copy a unified diff of your uncommitted changes to the clipboard; copies staged changes by default and unstaged on Alt-click when both are present.
- **Add Co-authors** &mdash; a button on the working changes commit box opens the contributor picker and appends the selected co-authors directly to the Graph's commit message.
- **Jump between changes and commit** &mdash; a new action in the working changes header selects the branch tip commit your changes are based on, complementing the existing jump from a commit to its working changes.

Working changes file lists now also honor VS Code's `scm.defaultViewSortKey` setting (keeping unresolved conflicts at the top), and partially staged (mixed) files are counted and badged more clearly.

### Multi-Select File Actions

You can now multi-select files in the _Commit Graph_ details and _Inspect_ view to act on several at once &mdash; Ctrl/Cmd+click to toggle, Shift+click for a range, and Ctrl/Cmd+A to select all. Batch actions are available from the context menu and toolbar: open files, open selected changes as a multi-diff, open on remote, and copy paths or relative paths &mdash; plus stage, unstage, stash, and discard for working changes.

### Quick Commit Actions: Push to Commit, Undo, and Publish

- **Push to Commit** &mdash; commits ahead of the branch's upstream now show an unpushed indicator that doubles as a one-click action to push up to (and including) that commit, also available in the commit's context menu.
- **Undo Commit** &mdash; a HEAD commit row surfaces an inline undo button when hovered, focused, or selected, alongside the existing context-menu action. Undo now works for the HEAD commit of any worktree, targeting the correct working tree for secondary worktrees, not just the active one.
- **Publish Branch** &mdash; a _Publish Branch_ action appears in the Graph header when the current branch has no upstream, publishing it in one click just left of _Fetch_.

### Navigate and Discover in the Graph

- **Back/forward navigation** &mdash; Back and Forward buttons in the commit and working changes detail headers step through previously-viewed commits, stashes, and working changes, re-selecting the row in the Graph where possible.
- **Keyboard shortcuts reference** &mdash; a new keyboard icon in the Graph's sidebar rail opens a reference listing all supported navigation, search, open, and commit shortcuts with platform-aware key labels.
- **Open Worktree File** &mdash; a new action in the commit file menu opens a committed file from the worktree whose branch contains the commit &mdash; handy in multi-worktree repos where the file's working copy lives outside the currently-scoped worktree.
- **Responsive sidebar** &mdash; the Graph's sidebar icon rail now compacts in short layouts, hiding count badges and tightening spacing, then folding overflowing icons into a "…" menu, restoring them as space grows.

### Agent Activity Treemap Improvements

The experimental _Agent Activity Treemap_ now reads as a living heatmap. Touched files fade over a configurable window after each tool call instead of switching on and off, reads and edits blend as cyan/amber weighted by recency, and a soft pulse marks the file an agent is reading or editing right now. Sub-agent file activity rolls up to the parent session, and a new `gitlens.graph.experimental.visualizations.activityDecay` setting (30 seconds to 30 minutes, default 5 minutes) &mdash; with a matching picker in the treemap toolbar &mdash; controls the decay window.

---

### Added

- Adds a `gitlens.graph.searchAutocompleteOnFocus` setting to control whether search autocomplete suggestions appear automatically when focusing or clicking the search input in the _Commit Graph_ ([#5287](https://github.com/gitkraken/vscode-gitlens/issues/5287))
- Adds the ability to copy working changes to other opened worktrees from the _Commit Graph_ ([#5288](https://github.com/gitkraken/vscode-gitlens/issues/5288))
- Adds the ability to discard working changes from the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view &mdash; per-file or in bulk, with safe partial discard for files that have both staged and unstaged changes (a first discard drops only the unstaged changes, preserving the staged portion) and a bulk action that switches to discarding staged changes when no unstaged changes remain ([#5296](https://github.com/gitkraken/vscode-gitlens/issues/5296))
- Adds an _Add Co-authors_ button to the _Commit Graph_'s working changes (WIP) commit box that opens the contributor picker and appends the selected co-authors to the commit message ([#5297](https://github.com/gitkraken/vscode-gitlens/issues/5297))
- Adds a _Copy Changes (Patch)_ button to the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view that copies a unified diff of the uncommitted changes to the clipboard &mdash; copies staged changes by default and unstaged changes on Alt-click when both are present, otherwise copies all changes ([#5302](https://github.com/gitkraken/vscode-gitlens/issues/5302))
- Adds the ability to jump from the working changes (WIP) to its commit in the _Commit Graph_ &mdash; a down-arrow in the working changes header selects the branch tip commit the changes are based on, complementing the existing action to jump from a commit to its working changes ([#5303](https://github.com/gitkraken/vscode-gitlens/issues/5303))
- Adds an _Undo Commit_ row adornment to the _Commit Graph_ &mdash; surfaces an inline undo button on a HEAD commit row when hovered, focused, or selected, alongside the existing context-menu action
- Adds support for undoing the HEAD commit of any worktree from the _Commit Graph_ &mdash; the adornment and context-menu action now target the correct working tree for secondary worktrees, not just the active one (a distinct _Undo Commit on Worktree_ label makes the target clear) ([#5311](https://github.com/gitkraken/vscode-gitlens/issues/5311))
- Adds responsive compaction to the _Commit Graph_'s side bar icon rail in short layouts &mdash; hides the count badges and tightens spacing, then folds the overflowing icons into a "…" menu (with their labels and counts) as the rail runs out of room, restoring them as it grows ([#5313](https://github.com/gitkraken/vscode-gitlens/issues/5313))
- Adds a keyboard shortcuts reference to the _Commit Graph_ &mdash; opened from a new keyboard icon in the graph's sidebar rail &mdash; listing all supported navigation, search, open, and commit shortcuts with platform-aware key labels ([#5312](https://github.com/gitkraken/vscode-gitlens/issues/5312))
- Adds back/forward navigation to the _Commit Graph_ details panel and _Inspect_ view &mdash; Back/Forward buttons in the commit and working changes (WIP) detail headers step back through previously-viewed commits, stashes, and working changes, best-effort re-selecting the row in the _Commit Graph_ ([#5316](https://github.com/gitkraken/vscode-gitlens/issues/5316))
- Adds the ability to push up to (and including) a specific commit from the _Commit Graph_ &mdash; commits ahead of the branch's upstream show an unpushed indicator that doubles as a one-click _Push to Commit_ action, also available in the commit's context menu ([#5314](https://github.com/gitkraken/vscode-gitlens/issues/5314))
- Adds an _Open Worktree File_ action to the commit file menu in the _Commit Graph_ details and _Inspect_ view that opens a committed file from the worktree whose branch contains the commit &mdash; useful in multi-worktree repos where the file's working copy lives outside the currently-scoped worktree, with a worktree picker when more than one worktree applies ([#5317](https://github.com/gitkraken/vscode-gitlens/issues/5317))
- Adds a working changes bar to the _Commit Graph_ &mdash; a horizontal bar above the graph with a pill for each worktree that has uncommitted changes or unpushed commits (primary and secondary worktrees alike), showing its branch and agent status, with an up-arrow (↑) marking unpushed work and a hover breakdown of changed files and commits to push; clicking a pill reveals and selects that worktree's working changes in the graph and opens its details ([#5301](https://github.com/gitkraken/vscode-gitlens/issues/5301))
- Adds heat decay, read/edit color blending, and a live pulse to the experimental _Agent Activity Treemap_ &mdash; touched files now fade over a configurable window after each tool call instead of switching on and off, reads and edits blend as cyan/amber weighted by recency, and a soft pulse marks the file an agent is reading or editing right now
  - Adds a `gitlens.graph.experimental.visualizations.activityDecay` setting (30 seconds to 30 minutes, default 5 minutes) with a matching decay-window picker in the treemap toolbar
  - Rolls sub-agent file activity up to the parent session so the heatmap reflects what a session's sub-agents are reading and editing
- Adds the ability to squash multiple commits from the _Commit Graph_ &mdash; select two or more contiguous commits on the current branch, right-click, and choose _Squash Commits_ to combine them into one, then review and edit the combined commit message (or keep only the oldest commit's message) ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds the ability to drop multiple commits from the _Commit Graph_ &mdash; select commits on the current branch, right-click, and choose _Drop Commits_ to remove them ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds the ability to reword a commit's message from the _Commit Graph_ &mdash; right-click a commit on the current branch and choose _Reword Commit_ ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds a _Modify Commits (Interactive Rebase)_ action to the _Commit Graph_ that opens the interactive rebase editor scoped from the selected commit(s) for squashing, rewording, reordering, dropping, and editing ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds a _Publish Branch_ action to the _Commit Graph_ header that appears when the current branch has no upstream &mdash; publishes (pushes and sets the upstream of) the current branch in one click, sitting just left of _Fetch_ and collapsing to its icon when the header is too narrow ([#5327](https://github.com/gitkraken/vscode-gitlens/issues/5327))
- Adds the ability to multi-select files in the _Commit Graph_ details and _Inspect_ view to act on several at once &mdash; Ctrl/Cmd+click to toggle, Shift+click for a range, and Ctrl/Cmd+A to select all &mdash; with batch actions from the context menu and toolbar: open files, open selected changes (multi-diff), open on remote, copy paths and relative paths, and (for working changes) stage, unstage, stash, and discard ([#5328](https://github.com/gitkraken/vscode-gitlens/issues/5328))
- Adds a `gitlens.advanced.repositorySearch.enabled` setting to control whether GitLens scans workspace folders to discover Git repositories &mdash; when disabled, GitLens relies solely on VS Code's built-in Git/SCM integration to report when repositories are opened or closed
- Adds the ability to stash only the staged changes from the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view &mdash; when both staged and unstaged changes are present, the _Stash_ action stashes only the staged changes by default (Alt-click to stash all)

### Changed

- Improves graph selection reliability and performance
- Honors VS Code's `scm.defaultViewSortKey` setting when sorting working changes (WIP) file lists in the _Commit Graph_, while keeping unresolved conflicts at the top ([#5289](https://github.com/gitkraken/vscode-gitlens/issues/5289))
- Changes the _Add as Co-author_ action in the _Commit Graph_ to append the co-author to the graph's working changes (WIP) commit message box instead of writing to the Source Control input and switching to the Source Control view ([#5294](https://github.com/gitkraken/vscode-gitlens/issues/5294))
- Improves _Commit Graph_ update performance by skipping redundant re-renders when content is structurally unchanged
- Improves performance in large workspaces by only watching a repository's working tree while its node is expanded in the views
- Improves resilience of GitHub requests by retrying transient gateway and network failures (502, 503, 504) with exponential backoff, restricted to idempotent reads
- Improves commit feedback and error handling when committing working changes (WIP) in the _Commit Graph_ &mdash; locks inputs with a spinner during commits and surfaces classified, actionable errors for signing, pre-commit hook, and conflict failures ([#5290](https://github.com/gitkraken/vscode-gitlens/issues/5290))
- Improves how partially staged (mixed) files are counted and displayed in the _Commit Graph_ file tree badges ([#5291](https://github.com/gitkraken/vscode-gitlens/issues/5291))
- Improves resilience when VS Code updates GitLens in the background &mdash; surfaces an actionable _Reload Window_ prompt when a lazily-loaded feature can no longer be found, instead of a cryptic error
- Changes the _Apply Stash_ command labels to _Apply / Pop Stash_ across the command palette, view context menus, _Commit Graph_, and tooltips to clarify that both apply and pop are available

### Fixed

- Fixes opening the _Commit Graph_ in multi root workspace to the correct repo ([#5276](https://github.com/gitkraken/vscode-gitlens/issues/5276))
- Fixes commit signing not being detected as enabled when only VS Code's `git.enableCommitSigning` setting is on (without `commit.gpgsign` set in Git config) &mdash; GitLens-driven commits (e.g. the _Commit Composer_) now sign in this case
- Fixes the `gitlens.advanced.similarityThreshold` setting being ignored when computing Git status &mdash; rename detection in status, working changes (WIP), and stash file lists used Git's default threshold (50%) instead of the configured value
- Fixes the `gitlens.advanced.similarityThreshold` setting being ignored when listing changed files for a diff &mdash; rename detection used Git's default threshold (50%) instead of the configured value
- Fixes force push from the _Push_ command always using `--force-with-lease` (and `--force-if-includes`) and ignoring VS Code's `git.useForcePushWithLease` and `git.useForcePushIfIncludes` settings &mdash; the confirmation could offer a plain `--force` while GitLens still pushed with lease; it now honors the configured preference
- Fixes _Stash Unstaged Changes_ also stashing staged changes when an untracked file is involved &mdash; including untracked files no longer drops the `--keep-index` flag, so staged changes are correctly kept intact ([#5281](https://github.com/gitkraken/vscode-gitlens/issues/5281))
- Fixes push from the _Commit Graph_ silently pushing to a wrong remote branch when the local branch tracks a differently-named upstream (e.g., `feature/foo` tracking `origin/main`) &mdash; now correctly pushes to the configured upstream branch instead of creating a new remote branch ([#5304](https://github.com/gitkraken/vscode-gitlens/issues/5304))
- Fixes the working changes (WIP) _Generate Commit Message_ in the _Commit Graph_ losing its result when the selection changes while a message is generating &mdash; the generation now continues and the message lands in the originating worktree's commit input (or its saved draft if you've navigated away) ([#5295](https://github.com/gitkraken/vscode-gitlens/issues/5295))
- Fixes the commit details metadata bar in the _Commit Graph_ and _Inspect_ view not surfacing a reachable tag when a commit is contained only in tags (and not any branch) &mdash; now shows the most relevant tag with a tag icon and color, matching how branches are shown ([#5293](https://github.com/gitkraken/vscode-gitlens/issues/5293))
- Fixes incorrect GitLab avatars being shown when multiple GitLab users share the same name ([#2205](https://github.com/gitkraken/vscode-gitlens/issues/2205))
- Fixes the repository picker being incorrectly skipped when an action targets a repository that isn't surfaced in VS Code &mdash; for example, using the stash action on a secondary worktree's working changes when that worktree isn't open in VS Code ([#5292](https://github.com/gitkraken/vscode-gitlens/issues/5292))
- Fixes potential runtime errors when formatting invalid or unparseable dates ([#4922](https://github.com/gitkraken/vscode-gitlens/issues/4922))
- Fixes an issue where unchecking _Interactive Rebase Editor_ in the GitLens settings UI would not persist &mdash; the checkbox would revert to checked after changing another setting or reopening the settings UI ([#5277](https://github.com/gitkraken/vscode-gitlens/issues/5277))
- Fixes an issue where the GitKraken CLI was not auto-installed on hosts where MCP auto-registration is unsupported (older VS Code, Windsurf, JetBrains, Trae, Kiro, Zed, etc.), preventing Claude hooks installation and agent dispatch in _Start Work_ and _Start PR Review_ flows ([#5280](https://github.com/gitkraken/vscode-gitlens/issues/5280))
- Fixes the _Commit Graph_ intermittently flashing a "No commits" message during concurrent Git operations
- Fixes styling in rendered markdown (commit message hovers, autolinks, and details) being stripped in webviews by the stricter content-security policy introduced in v18.0.0
- Fixes the `gitlens.advanced.skipOnboarding` setting not being honored, so onboarding surfaces could still appear even when it was enabled
- Fixes the _Commit Graph_ details panel showing stale working changes after the view regains visibility ([#5322](https://github.com/gitkraken/vscode-gitlens/issues/5322))


---

<a id="v18-0"></a>

## Version 18.0

#### Wednesday, May 27, 2026

GitLens 18 turns the _Commit Graph_ into a workbench: an embedded details panel lets you inspect, compare, review, stage, and commit without switching views, while a new overview sidebar puts your work and associated agent sessions within easy reach. AI agents become first-class citizens, integrated deeply within your workflows &mdash; see sessions associated with your current branch in the details panel, plus monitor active sessions with contextual actions wherever you work in GitLens. This release also adds branch pinning, multi-worktree WIP rows, a focused graph scope for the branch you care about, and a wide range of performance and quality-of-life improvements throughout the Graph.

<img src="/wp-content/uploads/gl-18-0-hero.png" class="help-center-img img-bordered">

### The Commit Graph, Now a Workbench

The _Commit Graph_ is no longer just a place to read history &mdash; it's where you work. A new embedded details panel allows you to inspect commits, working changes, compare branches, conduct reviews with AI, and compose commits without leaving the context of your Graph. The panel can be anchored to the right (the default) or to the bottom of the Graph &mdash; hold <kbd>Alt</kbd> while clicking the details toggle to switch between the two. 

This revamped commit details panel adds richer file-tree actions, multi-diff support, and quick toggles to jump into **Compose**, **Review**, and **Compare** modes. 

### Review and Compose, Directly in the Graph

Both _Commit Composer_ and a new _AI Code Review_ tool are now available right inside the Graph's details panel. Switch into compose mode to generate organized commits from your working changes, with multi-diff editor support for previewing proposed commits. Switch into review mode to get an AI-powered review of your changes, with summaries that identify focus areas with severity indicators, so you can check your work before you ship.

<img src="/wp-content/uploads/gl-18-0-review-mode.png" class="help-center-img img-bordered">

### AI Agents in GitLens

GitLens 18 introduces support for integrating AI coding agents, starting with Claude Code. Agent status is now surfaced throughout GitLens so you can monitor, focus, and act on parallel agent sessions without leaving the IDE and context from GitLens.


<img src="/wp-content/uploads/gl-18-0-agent-status.png" class="help-center-img img-bordered">

**Your agents' status, deeply integrated** &mdash; A new agent status pill appears on _Home_ view branch cards, the _Commit Graph_ overview cards, the _Commit Graph_ commit details panel, and the new _Agent Sessions_ sidebar panel. Pills are color-coded by state (running, idle, waiting for input, etc.), with subtle animations when sessions are active or when an agent is waiting for your input. Sessions awaiting input also surface on overview cards so you can find what needs attention at a glance.

**Agent Sessions panel** &mdash; A new panel in the _Home_ view and the _Commit Graph_ sidebar lists all your agent sessions in a streamlined view, with the same rich status hovers and quick actions as the inline pills. Switch between list and tree layouts to organize sessions by workspace or worktree.

**Claude Code hooks integration** &mdash; Install Claude Code hooks directly from GitLens via the _Home_ view banner, the _Commit Graph_ header, the agents sidebar banner, or the integrations menu. Hooks give GitLens real-time visibility into Claude Code session state. A dedicated command lets you uninstall hooks at any time.

**Agent Kanban (Experimental)** &mdash; A new experimental _Agent Kanban_ view turns the _Commit Graph_ into an interactive board for tracking your active AI agent sessions. Toggle it from the graph sidebar ('_Show Agent Kanban_') to see sessions partitioned across four columns: _Needs Input_, _Working_, _Idle_, and _Inactive_. From each session card you can approve or deny pending agent permissions, view a proposed plan, and jump straight to the session's working changes.

The _Agent Kanban_ view is enabled by default and can be toggled with the `gitlens.graph.experimental.kanban.enabled` setting.

### Multi-Worktree WIP Rows

The Graph now displays a work-in-progress row for **each** worktree, not just the active one, so you can see, review, and act on changes across all your parallel work without switching. Each WIP row shows live file stats, supports the full set of WIP actions (commit composition, conflict resolution, generating commit messages, and more), and updates in real time as files change. WIP scrollbar markers help you quickly locate uncommitted changes, with a configurable theme color and a setting to toggle them on or off.

<img src="/wp-content/uploads/gl-18-0-multi-wip.png" class="help-center-img img-bordered">

### Commit Graph Sidebar

The expandable sidebar introduced in 17.12 gets new, powerful views and actions in 18.0:

- **Overview panel** &mdash; surfaces active and recent branches as cards with WIP changes, upstream tracking status, pull requests, associated issues, contributor avatars, and quick actions (Switch, Open Worktree, Fetch, Publish Branch, and compare actions). Rich hover popovers expand each card with the full action set, autolink chips, and Launchpad mergeability tinting.
- **Agent Sessions panel** &mdash; see all your active agent sessions with status pills, branch/worktree associations, and quick actions to keep your agents unblocked.
- **Remote actions** &mdash; full context-menu support for remotes alongside branches, tags, stashes, and worktrees.
- **Worktree parity** &mdash; worktrees now have the same context-menu actions as branches, including AI-powered explain and generate changelog actions.
- **Tree-mode layout toggle** has moved into the filter actions area for a cleaner, more contextual placement.
- **Pin or overlay** &mdash; pin the sidebar in place, or float it as an auto-collapsing overlay over the Graph.

### Visualizations in the Graph

GitLens 18.0 brings powerful new ways to visualize your repository directly in the _Commit Graph_. A more capable _Visual History_ view has been integrated into a _Visualizations_ mode that now hosts new experimental Treemap views to visualize changes by file, commit, and agent activity.

Open the visualizations by clicking on the 'Show Visualizations' pulse icon at the bottom of the Graph sidebar, then use the switcher in the header to move between the _Visual History_ timeline and the new Treemap views.

#### Visual History

The _Visual History_ view renders your repo's history as a time-bucketed view of activity, with author avatars, configurable additions/deletions colors, and richer hover, zoom, scroll, brush, slider scrub, and slice filtering interactions. Scope the history down to specific files and folders, and slice the changes by branches rather than authors if needed.

<img src="/wp-content/uploads/gl-18-0-graph-visual-history.png" class="help-center-img img-bordered">

#### Treemap Visualizations (Experimental)

As an alternative to the _Visual History_ timeline, the _Commit Graph_ now offers three Treemap views that lay your repository out spatially. Each supports hover tooltips, click-to-zoom into folders, and breadcrumb navigation to track and retrace your path:

- **Files Treemap** &mdash; lays out your files and folders as nested rectangles, sized by their footprint, for a bird's-eye view of how the repository is structured.
- **Commits Treemap** &mdash; highlights where development is concentrated by sizing files and folders according to commit activity, making your most-changed areas stand out at a glance.
- **Agent Activity Treemap** &mdash; projects live AI agent presence onto your file structure in real time, distinguishing the files an agent is reading from the ones it's editing.

The Treemap visualizations are enabled by default and can be toggled with the `gitlens.graph.experimental.visualizations.enabled` setting. When disabled, only the _Visual History_ is available.

### Focus on the Work You Care About

You can now pin a branch to the leftmost column of the _Commit Graph_ so it always stays visible as a reference, even as other branches come and go. Pin or unpin from the row's context menu, and click the pinned ref in the Graph header to jump straight to it.

A new focused branch mode on the _Commit Graph_ header lets you focus the Graph on a single branch, with a searchable tree or list view to pick the focus. While scoped, the Graph renders along the focused branch's first-parent line (with the "Simplify Merge History" toggle automatically applied), and the minimap zooms to the relevant range. Clear visual indicators show when the Graph is scoped or modified by filters. The minimap settings have moved into the minimap itself, and dedicated header buttons toggle the sidebar, minimap, and details panel.

### Conflict Resolution Workflows

Conflict resolution now reaches into the _Commit Graph_ and _Interactive Rebase_ editor:

- Resolve conflicts directly from the Graph's WIP details panel, with merge-conflict status surfaced inline
- Conflict resolution actions are also available in the _Interactive Rebase_ editor's conflict file list, with dedicated diff-left/diff-right icons
- The _Interactive Rebase_ editor now shows a dismissible banner during the planning phase clarifying that closing the tab automatically starts the rebase

### Open the Graph in a New Window

A new "Open in New Window" command opens the _Commit Graph_ in a detached window for multi-monitor workflows. It's now the primary action in the Graph view's menus, with "Open in Editor" available as a modifier-key alternative.

### Performance and Reliability

GitLens 18 continues to invest in performance and stability improvements:

- **Faster Graph details loading** &mdash; commit metadata is now eagerly rendered from graph rows to instantly populate the details panel and skip IPC delays, with cached base file contents during compose sessions to eliminate redundant git reads.
- **Smarter caching** &mdash; granular TTLs based on ref mutability (5 minutes for full SHAs, 60 seconds for symbolic refs), cached branch merged-status checks, cached left/right commit counts for comparisons, and shared branch metadata across worktrees.
- **Lazy enrichment** &mdash; branch overview enrichment shifts from eager bootstrap to lazy loading, dramatically reducing initial resource contention during graph rendering.
- **Better cancellation** &mdash; abort signals now propagate through the Git command queue, RPC layer, and webview enrichment, so cancelled work stops instead of running to completion.
- **Coalesced refresh** &mdash; working-tree change emissions are coalesced into a single event per tick, eliminating redundant UI refreshes
- **Startup improvements** &mdash; Git and MCP providers now register in parallel, and the CLI version check is deferred to reduce extension activation time.

---

### Added

- Introduces an all-new _Commit Graph_ experience &mdash; a comprehensive redesign that pulls commit inspection, AI workflows, comparisons, branch focus, and working-change management directly into the graph
  - Adds an embedded details panel &mdash; replaces the standalone Graph Details view with an integrated panel that handles commit details, working changes, branch comparisons, AI reviews, and commit composition without leaving the graph
    - Adds a `gitlens.graph.details.location` setting to anchor the details panel at the bottom or right, with Alt+click on the details button to toggle
  - Adds an integrated AI Compose mode &mdash; provides a much improved AI-powered commit composition directly within the graph, with per-commit include/exclude toggles, multi-diff editor support, a virtual filesystem provider for synthesized per-commit diffs, cancellable generation, parallel/background operation, and copy and send-to-agent actions
    -Adds an integrated AI Code Review mode &mdash; surfaces severity-tagged findings with tooltips, copy and send-to-agent actions on outputs, and PR/issue/autolink context input ([#5235](https://github.com/gitkraken/vscode-gitlens/issues/5235))
  - Adds an integrated Compare mode &mdash; opens comparisons directly inside the graph instead of the _Search & Compare_ view, with Ahead/Behind/All Files tabs, working tree comparisons for peer worktrees, AI-powered explaination and changelog generation, and an _Open in Search & Compare_ action to persist ad-hoc comparisons
  - Adds a refined header with WIP (work-in-progress) status and stash action
  - Adds a unified UI/UX for scoping and filtering the graph
    - Adds an _Agent Branches_ option to filter the graph to show only the branches or worktrees with active or recent agent activity
    - Adds a _Focus Branch_ option to scope the graph to just the changes on specific branch via a new branch selector (or the new Overview or Agents side bar), with merge-target anchoring
  - Adds all new experiences to the graph _Side Bar_
    - Adds pinned and overlay modes &mdash; overlay mode floats over the graph instead of pushing it aside, with auto-collapse on focus loss and a pin/unpin toggle in the panel header
    - Adds an _Overview_ side bar panel &mdash; surfaces active and recent branches as rich cards with WIP stats, upstream tracking, associated pull requests, issues, and agents, as well as quick actions and rich hover details
      - Clicking on an _Overview_ card instantly focuses (scopes) the graph to just the changes on the selected branch
    - Adds an _Agents_ side bar panel &mdash; surfaces active and recent agents with their activity, associated branches/worktrees
      - Clicking on an agent row instantly focuses (scopes) the graph to just the changes on the selected wokrtree, and selects the agent in the details panel
    - Adds a _Visualizations_ mode to the side bar &mdash; houses the all-new _Visual History_, and 3 experimental treemap visualizations
      - _Visual History_ &mdash; rebuilt from the ground up to provide a better experience with dynamical loading and dealing with many contributors and/or branches
      - _Files Treemap_ &mdash; an experimental spatial visualization of file layout within the repository color coded by file type, with hover tooltips, deep zoom-to-folder, and tracking breadcrumbs
      - _Commits Treemap_ &mdash; an experimental spatial visualization of commit activity within the repository colorized as a heatmap
      - _Agent Activity Treemap_ &mdash; an experimental spatial visualization of realtime agent activity. See where your agents are currently reading and editing across your repository
    - Adds an experimental _Agent Kanban_ mode to the side bar &mdash; an interactive Kanban board grouping active agent sessions by state (Working, Idle, Inactive, Needs Input), with inline plan view and permission approval directly from session cards
    - Adds comprehensive context menu support for worktrees in the sidebar and Commit Graph &mdash; brings feature parity with branches, including Reveal in File Explorer, AI-powered actions (explain WIP, generate changelog), Open in Terminal, and Copy Path
  - Adds an all new way to manage worktrees and working changes (WIP)
    - Changes working changes (WIP) rows to always be visible regardless of whether or not there are uncommitted changes
      - When there are uncommitted changes, the _Details Panel_ now allows you to review, stage, and commit your changes, or leverage the all-new _Compose_ and _Review_ modes to have AI review and automatically compose your changes into a set of well-structured commits
      - When there are no uncommitted, the _Details Panel_ transforms into a hub to guide you to the next steps &mdash; like pulling, pushing, drafting a PR, reviewing, recomposing, etc. Everything to help you get your changes merged faster ([#5218](https://github.com/gitkraken/vscode-gitlens/issues/5218))
    - Adds support for working changes (WIP) rows from secondary worktrees
      - Selecting a WIP rows provides file actions, conflict resolution, and live-updating stats for non-active worktrees, plus _Open in Integrated Terminal_ and _Open Worktree in New Window_ actions on the header
    - Adds the ability to discard uncommitted changes
    - Adds smart push/pull on the WIP details panel header &mdash; offers Force Push when a branch is both ahead and behind its remote
    - Adds conflict resolution actions to the WIP details panel
    - Adds the ability to share working changes as a Cloud Patch directly from the WIP header
    - Adds persistence of in-progress commit messages and amend state per worktree &mdash; drafts are restored when switching contexts, the original message is restored on Undo Commit, and per-worktree search box and filter preferences persist across sessions
    - Adds Jump to Working Changes &mdash; quickly navigate from the selected commit to the most relevant WIP node in the same lane, with primary-worktree fallback
    - Adds bulk staging operations &mdash; _Stage All_ and _Unstage All_, with Alt-click on mixed-state checkboxes to unstage all currently staged items
  - Adds auto-fetch while the _Commit Graph_ is visible and focused, yielding to VS Code's built-in Git auto-fetch when enabled, with a fetch button popover to manage settings and a minimum interval floor to prevent excessive fetching
  - Adds search and filtering improvements &mdash; adds a `type:wip` operator to filter to working changes, and column header filters with interactive pickers for authors, refs, and files
  - Adds the ability to pin and unpin branches &mdash; pinned branches persist across sessions with a jump-to-pinned-branch actionn ([#5139](https://github.com/gitkraken/vscode-gitlens/issues/5139), [#5181](https://github.com/gitkraken/vscode-gitlens/issues/5181))
  - Adds inline row actions for commit and stash rows including open all changes (Alt to compare against working tree) and apply/drop stashes
  - Adds a floating "HEAD" indicator to the graph to quickly jump to the HEAD commit
  - Adds a completely rebuilt minimap with better performance and zoom controls and clearer markers
  - Adds minimap and scrollbar markers for worktrees &mdash; surfaces uncommitted changes on the minimap and scrollbar with a configurable theme color and a toggle setting
  - Adds an _Open in New Window_ toolbar view action &mdash; opens the graph in a detached window for multi-monitor workflows, with _Open in Editor_ available as the Alt+click alternative
- Adds comprehensive AI agent integration throughout GitLens
  - Adds an agent status framework with Claude Code support using Claude Code Hooks (must be installed) &mdash; surfaces sessions across the _Home_ view, _Commit Graph_ overview cards ([#5170](https://github.com/gitkraken/vscode-gitlens/issues/5170)), WIP rows, _Commit Details_, _Agents_ side bar panel, and the experimental _Agent Kanban_ mode
  - Adds an _Agent Branches_ visibility mode to the _Commit Graph_ that filters branches to only those with active or recently active agents
  - Adds an agent picker to _Start Work_ and _Start Review_ flows, plus a default-agent picker, _Switch Default Agent_ command, and Start Work/Start Review in Agent actions in the _Home_ and _Commit Graph_ views
  - Adds support for opening agent sessions hosted in other VS Code windows
  - Adds a _Resume in Terminal_ fallback when an agent session fails to open or is active in another VS Code window
  - Adds notifications for peer-discovered agent session permissions
  - Adds an experimental _Agent Kanban_ mode &mdash; an interactive Kanban board grouping active agent sessions by state
- Adds conflict resolution actions to the _Interactive Rebase_ editor conflict file list
- Adds a close-tab warning banner to the _Interactive Rebase_ editor &mdash; displays a dismissible informational banner during the planning phase to clarify that closing the tab automatically starts the rebase ([#5123](https://github.com/gitkraken/vscode-gitlens/issues/5123))
- Adds a `gitlens.rebaseEditor.openBehavior` setting to control where the _Interactive Rebase_ editor opens when automatically reopened on a paused rebase &mdash; `auto` (default) opens beside only when a multi-pane layout already exists; `beside` always opens in a side group
- Adds Seti file icon theme support for webviews &mdash; files in webview trees now display the correct Seti glyph
- Adds folder actions in _Details Panel_ and _Inspect_ view
- Adds a unified onboarding reset command that consolidates the previous Banners and Usage Tracking resets into a single restore-first-time-experience action

### Changed

- Switches the _Commit Graph_ sidebar to be visible by default for new installations in overlay mode
- Switches _Open Worktree in New Window_ to be the primary action and _Open Worktree_ to be the alternative across views and the _Commit Graph_
- Improves the default _Interactive Rebase_ editor density to a more spacious layout
- Improves _Commit Graph_ performance and responsiveness &mdash; content-fingerprint deduping of full-state pushes, incremental row-stats sending, avatar omission for unchanged rows, in-memory WIP caches, and debounced repository event coalescing
- Improves branch overview enrichment performance &mdash; tiered caching using stored merge targets as cache keys, lazy loading, and parallelized metadata fetches
- Improves Git diff performance &mdash; switches diff operations to `numstat`+`summary` instead of `name-status` parsing
- Improves Git command result caching &mdash; granular TTLs based on ref mutability (5-minute cache for full SHAs, 60-second failsafe for symbolic refs), plus caching for left-right commit counts, merge bases, and per-branch config lookups
- Improves performance for GitHub virtual repositories &mdash; adds caching for commit details, counts, merge bases, paged branches/tags, and default branches, plus deduping of in-flight GraphQL requests
- Improves the _Commit Graph_ minimap colors and contrast for better theme accessibility, and adds out-of-view proxy handles and improved scope zoom rendering
- Improves the _Connect More Agents_ picker to only show agents that don't already have the GitKraken MCP installed, with a clearer empty state when all detected agents are already connected ([#5142](https://github.com/gitkraken/vscode-gitlens/issues/5142))
- Improves repository visibility detection with promise-based caching to prevent redundant computation
- Improves Git command priority inference &mdash; keeps polymorphic history commands at normal priority, requires expensive full-history walks to opt into background priority
- Improves the default and maximum limits for concurrent background Git processes
- Improves branch comparison default target logic &mdash; automatically suggests the merge target of a branch as the default right-side reference and uses branch names instead of SHAs for stability
- Improves stash reachability filtering &mdash; uses Git's authoritative stash metadata via the `%s` subject parsing instead of expensive parent-timestamp tracking
- Improves AI error handling and network detection &mdash; distinguishes between "No Network" and "Unreachable" states, with automatic retry on network failures and a recursive cause-chain analysis for better diagnostics
- Improves header and breadcrumb responsiveness across webviews &mdash; priority-based collapsing with compact icons and overflow popovers for narrow views
- Migrates from `node-fetch` to native fetch and adopts VS Code's built-in proxy support &mdash; removes the custom `gitlens.proxy` setting in favor of standard VS Code and OS proxy settings
- Migrates the webview component library to WebAwesome, modernizing selects, overlays, sliders, and tooltips with workspace-color-aware highlights

### Fixed

- Fixes an issue where starting an interactive rebase forced a split-pane layout when git paused for a `reword` &mdash; the _Interactive Rebase_ editor now opens as a hidden background tab alongside the commit message editor instead of stealing the active tab ([#5203](https://github.com/gitkraken/vscode-gitlens/issues/5203))
- Fixes an issue where untracked files were missing from the _Compare Working Tree with..._ file list unless manually staged with `git add -N` first ([#5158](https://github.com/gitkraken/vscode-gitlens/issues/5158))
- Fixes an issue where the _Interactive Rebase_ editor would auto-open during the brief teardown window after a rebase completed (or on non-interactive rebases), showing stale or empty state ([#5217](https://github.com/gitkraken/vscode-gitlens/issues/5217))
- Fixes an issue where the _Interactive Rebase_ editor would show a blank state when opened on a repository outside the workspace (e.g., from a terminal) ([#5229](https://github.com/gitkraken/vscode-gitlens/issues/5229))
- Fixes an issue where the terminal integration relaunch warning persisted due to stale environment variable state ([#4977](https://github.com/gitkraken/vscode-gitlens/issues/4977))
- Fixes an issue where MCP reinstallation could fail when the proxy binary was locked on Windows ([#5126](https://github.com/gitkraken/vscode-gitlens/issues/5126))
- Fixes an issue where stashing staged changes was not using the `--staged` flag ([#5138](https://github.com/gitkraken/vscode-gitlens/issues/5138))
- Fixes an issue where the currently selected option is not visually distinguishable in select-style menus on the _Home_ view (agent workspace filter, recent timeframe filter) and elsewhere (_Visual History_ period menu, _Commit Graph_ overview filter) &mdash; most noticeable on light themes ([#5259](https://github.com/gitkraken/vscode-gitlens/issues/5259))
- Fixes an issue where diff hunks could be missing for renamed or copied files in editor gutters and hovers &mdash; rename detection was inadvertently filtering out valid diffs
- Fixes an issue where stash apply and pop actions could fail silently due to missing stash numbers, producing invalid `stash@{undefined}` references, and where the _Commit Graph_ would not refresh when a stash was dropped
- Fixes an issue where GitLens would automatically re-open repositories that the user had explicitly closed via the SCM interface
- Fixes an issue where the _File History_ context menu actions on commits and folders launched a standalone editor instead of integrating with the embedded _Visual History_ in the _Commit Graph_
- Fixes an issue where the SCM grouped views could intermittently "detach" &mdash; alt commands have been removed from SCM grouped views due to flakey/sticky alt detection in VS Code
- Fixes an issue where the _Compare Working Tree_ "Show All Diffs" button used inverted diff direction
- Fixes an issue where authentication errors could surface noisy notifications and break-on-exception breakpoints instead of returning safe defaults
- Fixes various race conditions and stale-state issues across the _Commit Graph_ during repository, branch, and worktree switches &mdash; including phantom anchors after removing the last secondary worktree, cross-repo data contamination during rapid swaps, lost state notifications during in-flight updates, and forced reloads during panel restoration
- Fixes an issue where the working tree comparison could incorrectly include untracked files for revision-range diffs

---

### Previous Release Notes

- [Version 17.x Release Notes](/gitlens/GL-Release-v17-x)
- [Older Release Notes (v16.x and earlier)](/gitlens/GL-Releases-Old)
