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
