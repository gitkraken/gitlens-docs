---
title: GitLens Commit Graph
description: Visualize your repository history, branches, and collaborators with the GitLens Commit Graph in VS Code.
taxonomy:
    category: gitlens

---

<kbd>Last updated: August 2025</kbd>

## Commit Graph <code>PRO</code>

The GitLens Commit Graph is the main view in the GitLens sidebar, providing an interactive visualization of your repository history. Built on a high-performance rendering engine, it shows commits, branches, and collaborators in one place, helping you understand contributions and make faster decisions.

<figure>
  <img src="/wp-content/uploads/commit-graph.png" class="help-center-img img-bordered" alt="Commit Graph in GitLens showing branches and commits" />
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

- **Repository name**
- **Checked-out branch** (click to switch branches)
- **Last fetched time** (click **Fetch** to update)

You can enable automatic fetching with the `gitlens.graph.autoFetch` setting. When enabled, GitLens periodically runs `git fetch` for repositories visible in the Commit Graph, keeping your view up to date without manual refreshes.

<figure>
  <img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="help-center-img img-bordered" alt="Repository details in the Commit Graph toolbar" />
  <figcaption style="text-align: center; color: #888">Repository details in the Commit Graph toolbar</figcaption>
</figure>

---

### Availability

- The Commit Graph is available to all users for **public** and **local** repositories.
- A **paid GitLens subscription or trial** is required for use with **private repositories**.

---

### Feedback

We’d love your input! Share ideas and feedback in the [GitLens Commit Graph discussion on GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).

---

### Graph Sidebar

The Commit Graph includes an expandable sidebar panel that provides quick access to your repository refs. The sidebar lists branches, remotes, stashes, tags, and worktrees in both list and tree views. Click the sidebar toggle to expand or collapse it, or use the `gitlens.graph.sidebar.pinned` setting to keep it pinned open.

The sidebar contains several panels:

- **Overview**: Displays branch cards with WIP stats and upstream tracking information at a glance.
- **Focus Branch**: Scopes the graph to a single branch, filtering out unrelated history.
- **Agent Branches**: Filters branches to show only those associated with AI agent sessions.
- **Agent Sessions**: A Kanban-style panel for monitoring and managing active agent sessions. Branches with running agent sessions display status pills directly in the graph, so you can track agent activity at a glance.

<figure>
  <img src="/wp-content/uploads/gl-graph-sidebar-01.png" class="help-center-img img-bordered" alt="The Commit Graph with the sidebar panel expanded, showing branches, remotes, stashes, tags, and worktrees in a tree view" />
  <figcaption style="text-align: center; color: #888">The Commit Graph sidebar with branches, remotes, and worktrees</figcaption>
</figure>

#### Detail Sheets

Clicking on a branch, pull request, or comparison in the sidebar opens a slide-out detail sheet with rich information:

- **Branch sheet**: Shows branch details, tracking status, and recent commits.
- **Pull request sheet**: Displays PR description, reviewers, status checks, and stacked PR information when applicable.
- **Compare sheet**: Shows file-level comparison between branches or commits, with a pinned mode to keep the comparison visible while navigating.
- **Rebase summary sheet**: Appears after a rebase operation, summarizing what changed.
- **WIP conflict sheet**: Surfaces during conflict resolution to help resolve working changes.

---

### Overview Bar

The overview bar is a horizontal strip displayed above the graph showing one pill per worktree. Each pill indicates the branch's WIP status, and hovering reveals additional details. The `gitlens.graph.overviewBar.visibility` setting controls when the overview bar is shown.

#### Ref Find

The ref-finder widget provides a typeahead search for quickly jumping to any branch, tag, or WIP row in the graph. The `gitlens.graph.refFindAutoHide` setting controls whether the widget auto-hides after selecting a result.

---

### WIP Bar

The Commit Graph displays a WIP bar at the top of the graph with one pill per worktree. Each pill shows the branch name, a dirty indicator when there are uncommitted changes, an unpushed arrow with ahead count when commits have not been pushed, and changed file counts on hover. Clicking a pill scrolls the graph to that worktree's WIP row.

<figure>
  <img src="/wp-content/uploads/gl-graph-wip-bar-01.png" class="help-center-img img-bordered" alt="The Commit Graph WIP bar showing worktree pills with branch name and dirty indicator for uncommitted changes" />
  <figcaption style="text-align: center; color: #888">WIP bar with worktree pills above the graph</figcaption>
</figure>

---

### Details Panel

The Commit Graph includes an embedded details panel that shows information about the selected commit or your current working changes. The details panel replaces the former standalone Graph Details view and is integrated directly within the graph.

When you select a commit, the details panel displays the commit message, author, changed files, and diff. When viewing working changes, it shows your uncommitted modifications. The panel can be positioned to the right or bottom of the graph using the `gitlens.graph.details.location` setting. An `auto` option is also available, which switches between right and bottom placement based on the graph width. The `gitlens.graph.details.maximizeOnMode` setting automatically maximizes the details panel when entering compose, review, or resolve modes.

The details panel supports multiple modes:

- **Compare mode**: Opens comparisons directly within the graph, showing Ahead, Behind, and All views between branches or commits. This replaces navigating to the standalone Search and Compare view for graph comparisons.
- **Compose mode**: Provides an integrated commit composition experience, letting you craft commit messages and select files to commit without leaving the graph. You can also access Compose from the graph context menu.
- **Recompose**: Restructures the commit history on a branch using AI. Available from the graph context menu, Recompose can operate on an entire branch, from a specific commit, or on selected commits. It analyzes your changes and reorganizes them into cleaner, more logical commits.
- **Review mode**: Uses AI to analyze commits or working changes and surfaces severity-tagged insights such as potential bugs, security issues, or style concerns. You can configure separate AI models for compose and review using per-feature model scoping, and customize review behavior with the `gitlens.ai.reviewChanges.customInstructions` setting.

<figure>
  <img src="/wp-content/uploads/gl-graph-details-panel-01.png" class="help-center-img img-bordered" alt="The Commit Graph with the embedded details panel on the right, showing commit message, author, and changed files for the selected commit" />
  <figcaption style="text-align: center; color: #888">Embedded details panel showing commit information</figcaption>
</figure>

#### Multi-file Selection

File lists in the details panel (WIP, commit details, compare, compose, and review panels) support multi-file selection using <kbd>Shift</kbd>-click and <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>-click. With multiple files selected, you can perform batch operations including stage, unstage, discard changes, and stash. Individual files also show inline action buttons for quick single-file operations.

#### Co-authors

When composing a commit in the graph, use the **Add Co-authors** button to append `Co-authored-by` trailers to your commit message.

#### Navigation and Keyboard Shortcuts

The details panel includes back and forward navigation buttons for browsing through previously viewed commits. A keyboard shortcuts reference dialog is available listing all graph shortcuts organized by category.

---

### Configuration and Layout

You can configure the Commit Graph to control what information is shown and how it is displayed.

#### Graph Style

The `gitlens.graph.style` setting controls the overall row layout of the graph. Options include `table` (columnar layout with visible borders), `list` (compact list layout), and `auto` (switches based on available width).

#### Columns
- Drag and drop column headers to rearrange columns.
- Right-click a column header to toggle columns on or off.
- The **Changes** column visualizes added and deleted lines per commit. The `gitlens.graph.changesColumn.mode` setting controls the display style: `numbers` (numeric counts), `squares` (colored blocks), `bar` (horizontal bar), or `bipolar` (split additions/deletions bar).
- **Column grouping** is enabled by default, combining the Graph and Branches/Tags columns into a compact layout. Lanes can be folded to collapse inactive branches and reduce visual clutter.

#### Lane Colors and Row Markers

The graph uses perceptually-uniform lane colors that are tuned for both dark and high-contrast themes. Row markers indicate important commits at a glance:
- **Green marker**: HEAD commit
- **Blue marker**: upstream tracking commit
- **Colored reference pills**: merge target and other branch roles

<figure>
  <img src="/wp-content/uploads/gl-column-settings.png" class="help-center-img img-bordered" alt="Commit Graph column settings menu showing toggle options" />
  <figcaption style="text-align: center; color: #888">Commit Graph column settings</figcaption>
</figure>

#### Layout Options
- **Panel Layout**: Displays the Commit Graph in the bottom panel (near the Terminal) with a details view alongside it.
- **Editor Layout**: Opens the Commit Graph in an editor tab.
- You can open the Commit Graph in both layouts simultaneously.

To switch layouts:
1. Select the settings gear in the top-right corner of the Commit Graph editor.
2. Choose **Prefer Commit Graph in Panel Layout** or **Prefer Commit Graph in Editor Area**.

The `gitlens.graph.editorOpeningBehavior` setting controls how files open from the graph — either in the active editor group or automatically based on context. You can also open the Commit Graph in a separate VS Code window using the **GitLens: Open Commit Graph in New Window** command.

<figure>
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location.png" class="help-center-img img-bordered" alt="Commit Graph layout preference menu" />
  <figcaption style="text-align: center; color: #888">Switching between Editor and Panel Layout</figcaption>
</figure>

#### Compact Graph Layout
- Right-click the **Graph** column header and select **Compact Graph Column Layout** to reduce visual complexity.
- When the **Author** column is resized to minimum width, it shows avatars instead of text.
- Columns that become too narrow automatically switch to icons to preserve information.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="help-center-img img-bordered" alt="Compact Commit Graph layout with icons and avatars" />
  <figcaption style="text-align: center; color: #888">Compact Graph and Author column with avatars</figcaption>
</figure>

#### Scroll Markers
Scroll markers highlight key points in the Commit Graph, including:
- Checked-out branches
- Selected rows
- Search results
- Work-in-progress (WIP) rows

Use scroll markers to quickly jump to important points such as `HEAD` or refs. You can toggle this feature in the [Commit Graph settings](/gitlens/gitlens-features/#settings).

The `gitlens.graph.showWorktreeWipStats` setting displays file add/change/delete statistics on worktree WIP rows. The `gitlens.graph.minimap.reversed` setting reverses the minimap direction.

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
  <img src="/wp-content/uploads/commit-graph-settings.png" class="help-center-img img-bordered" alt="Commit Graph settings in VS Code" />
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
  <img src="/wp-content/uploads/Rich-Commit-Search.png" class="help-center-img img-bordered" alt="Commit Graph search bar highlighting results" />
  <figcaption style="text-align: center; color: #888">Searching commits in the Commit Graph</figcaption>
</figure>

You can also:
- Jump to the **first or last result** by holding <kbd>Shift</kbd> while clicking the arrow icons.

<figure>
  <img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="help-center-img img-bordered" alt="Navigating commit search results with arrow keys" />
  <figcaption style="text-align: center; color: #888">Navigating commit search results</figcaption>
</figure>

#### Search Filters
Use these filters in the search bar:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me`

You can also use **natural language search** to describe what you are looking for in plain English. GitLens uses AI to convert your query into the appropriate structured search operators. Time-based operators such as `after:` and `before:` are available for filtering commits by date.

Additional options:
- Match all
- Match case
- Use regular expressions

<figure>
  <img src="/wp-content/uploads/search-options.png" class="help-center-img img-bordered" alt="Commit Graph search options for case sensitivity and regex" />
  <figcaption style="text-align: center; color: #888">Commit Graph search options</figcaption>
</figure>

### Full Context Menu Support

You can right-click a branch, commit, tag, author, or column header (Author, Commit Date/Time, or SHA) to access context menu actions.

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

---

### AI Auto Rebase <code>PRO</code>

AI Auto Rebase automatically resolves conflicts during a rebase operation. When conflicts arise, GitLens uses AI to analyze and resolve them end-to-end based on a configurable confidence threshold.

- Run **GitLens: AI Auto Rebase** from the Command Palette or the graph context menu.
- The `gitlens.ai.autoRebase.confidenceThreshold` setting (0 to 1) controls how confident the AI must be before automatically applying a resolution.
- Use `gitlens.ai.resolveConflicts.customInstructions` to provide custom instructions that guide how the AI resolves conflicts.
- If the result is unsatisfactory, use **GitLens: Undo AI Auto Rebase** to revert to the pre-rebase state.

During the rebase, a progress animation appears in the graph to indicate the operation is in progress. A rebase summary sheet opens in the sidebar when the operation completes.

---

### Pull Request Information

For GitHub and GitLab, the Commit Graph displays a Pull Request icon for any branch with an open pull request. To enable this, connect a [rich integration](/gitlens/settings/#remote-provider-integration-settings).

For GitHub repositories, the graph also recognizes **stacked pull requests**. When a branch is part of a PR stack, the PR sheet in the sidebar shows the stack ID, the total number of PRs in the stack, and the current PR's position. Merge operations are stack-aware, distinguishing between merging a single layer and merging the entire stack.

<figure>
  <img src="/wp-content/uploads/pull-request-icon.png" class="help-center-img img-bordered" alt="Commit Graph branch showing pull request icon" />
  <figcaption style="text-align: center; color: #888">Pull request icon in Commit Graph</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

The Commit Graph shows refs to your remotes, branches, and tags.  
- Hover over any ref to use the **Hide** option.  
- To show them again, hover over the **Hide** option at the top of the Commit Graph and select the desired refs.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs.gif" class="help-center-img img-bordered" alt="Hiding refs from the Commit Graph view" />
  <figcaption style="text-align: center; color: #888">Hiding refs in the Commit Graph</figcaption>
</figure>

#### Filter Options
Access filters from the dropdown menu to choose:  
- **Show Current Branch Only**: Displays the current branch and its upstream remote.  
- **Show All Local Branches** *(default)*.  

Additional options let you hide or show:  
- Remote-only branches  
- Stashes  
- Tags  

You can also dim merge commit rows for clarity.

<figure>
  <img src="/wp-content/uploads/filter-options-2.png" class="help-center-img img-bordered" alt="Commit Graph filter options for branches, tags, and stashes" />
  <figcaption style="text-align: center; color: #888">Commit Graph filter options</figcaption>
</figure>

---

### Minimap

The Minimap provides a high-level overview of repository activity. It shows commits, branches, HEAD/upstream, and more, letting you quickly jump to points of interest.

- Select the **Toggle Minimap** icon in the Commit Graph toolbar to enable or disable it.  
- Use the graph icon dropdown to switch between **Commits** or **Lines Changed** views.  
- Toggle markers on or off from the same menu.
- The `gitlens.graph.minimap.defaultVisibility` setting controls when the minimap appears: `hidden`, `onSearch` (default, shows during search), or `always`.

<figure>
  <img src="/wp-content/uploads/gl-minimap-2.png" class="help-center-img img-bordered" alt="Commit Graph Minimap enabled in the toolbar" />
  <figcaption style="text-align: center; color: #888">Commit Graph Minimap</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-minimap-settings.png" class="help-center-img img-bordered" alt="Commit Graph Minimap settings with commits or lines changed options" />
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