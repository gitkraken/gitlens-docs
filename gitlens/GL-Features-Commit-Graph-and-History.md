---
title: Commit Graph and History Features
description: "Technical reference for the GitLens Commit Graph, Visual History, and commit file details in large histories: commands, settings, layout, search, and filters."
product: GitLens
feature: Commit Graph
content_type: reference
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [commit-graph, visual-history, search, minimap, layout, filters, repository-health]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Commit Graph and History"
    nav_order: 10
    nav_parent: "gitlens-features"
    page_type: "content"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

***

## Commit Graph

For workflows and examples, see [Commit Graph](/gitlens/gl-commit-graph/) and [Commit Graph is Home](/gitlens/home-view/).

The Commit Graph is the starting point for working in GitLens. It brings repository history, branches, worktrees, Working Changes, pull requests, and supported agent activity into one connected workbench, so you can understand what's happening and move changes toward merge without rebuilding context across tools.

Built on a high-performance rendering engine, the graph stays responsive on large repositories, showing commits, branches, and contributors in one place.

The Commit Graph is included in **GitLens Community** and available to everyone on public and local repositories &mdash; no account required. A <a href="https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens" target="_blank">GitLens Pro subscription or trial</a> is required only for private repositories.

If you aren't signed in, opening the Commit Graph on a privately hosted repository for the first time starts a 3-day preview. A banner above the graph shows how much of the preview is left, with a **Sign In** link. When the 3 days are up, the graph shows **Commit Graph Preview Ended** for privately hosted repositories until you sign in or start a free Pro trial. The preview is only for signed-out use; a signed-in account without a Pro trial or paid plan sees the upgrade prompt on private repositories.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-01-v4@2x.png" alt="Commit Graph in GitLens showing branches and commits" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Explore your full Git history at a glance</figcaption>
</figure>

---

### How to Open the Commit Graph

The Commit Graph opens automatically when you click the GitLens icon in the Activity Bar. You can also open it from the Command Palette:

1. Open the Command Palette:  
   <kbd>Cmd/Ctrl + Shift + P</kbd>

2. Type:  
   `GitLens: Show Commit Graph`

<figure>
  <img src="/wp-content/uploads/show-commit-graph.gif" alt="Using the Command Palette to open the GitLens Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Launch the graph directly from the Command Palette</figcaption>
</figure>

---

### Commit Graph Header

At the top of the graph, you’ll see:

- **Repository** — the hosting provider's icon (hover it for the repository name; the editor tab is titled *Commit Graph: &lt;repository&gt;*)
- **Checked-out branch**
- **Last fetched time** — beside **Fetch** and in its hover
- **Account button** — your avatar and plan, last in the header

From here, you can:

- Click the branch name to switch branches
- Click **Fetch** to update commit data
- Click **Publish Repository** to open the Git Command Palette's **Publish** step with **Publish Repository…** selected, which creates a repository on a hosting provider and publishes the current branch to it; choose **Add Remote…** there instead to add a remote of your own (see [Git Command Palette](/gitlens/gl-features-git-commands-and-rebase/#git-command-palette)). It appears in place of **Publish Branch** when the repository has no remotes, and **Fetch** is hidden then
- Click the account button to open its popover. The popover holds your account actions (**Synchronize Status**, **Manage Account**, **Send Feedback**, and **Sign Out**), the AI model you use and your GitKraken AI usage, your agents, and your connected integrations. Sections that aren't set up yet offer **Set up AI**, **Set up agents**, or **Set up integrations**, which open GitLens Settings.

<figure>
  <img src="/wp-content/uploads/gl-graph-info-01-v3@2x.png" srcset="/wp-content/uploads/gl-graph-info-01-v3@2x.png" alt="The top of the Commit Graph in the editor area: the tab reads &quot;Commit Graph: Playground2026&quot;, the header shows the current branch (main) with Push and &quot;Fetch (1wk ago)&quot; buttons, and the Fetch button's hover popover lists the upstream (origin/main on GitHub), &quot;Last fetched last week&quot; and the Auto-fetch option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access key branch controls directly from the header</figcaption>
</figure>

> **Note:** The Commit Graph is included in GitLens Community and available to all users on public or local repositories, without needing an account.
>
> Only private repository access requires a [GitLens Pro subscription or trial](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens). Signed out, you get a 3-day preview of the Commit Graph on privately hosted repositories first.
>
> We welcome your input—join the discussion on [GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).

### Scope the Graph to a Worktree

Scoping re-centers the Commit Graph on another worktree of the same repository, so that worktree's `HEAD` and Working Changes are treated as the current ones. To scope the graph, do any of the following:

- Select **Scope to Worktree** on a worktree row in the side bar's **Worktrees** panel. <kbd>Alt</kbd>-click the same button to use **Focus on Branch** instead.
- Right-click a worktree row, or the Working Changes row of another worktree, and select **Scope to Worktree** or **Focus on Branch**.
- Double-click the Working Changes row of another worktree, or its pill in the overview bar above the graph.

While the graph is scoped, the header is tinted and the branch button's hover shows **Scoped to Worktree** with the worktree's name. Select **Unscope Worktree** beside the branch button to return to your active worktree.

Two settings control scoping, and the gear in the **Graph Options** popover (**Worktree Scope Settings...**) opens both:

- `gitlens.graph.scopeBehavior` — `scopeAndFocus` (default) also focuses the worktree's branch, narrowing the visible rows. `scope` changes only the perspective and leaves every commit visible.
- `gitlens.graph.doubleClickWorktreeAction` — `scope` (default) scopes the graph when you double-click. `focus` toggles branch focus instead.

The overview bar shows a pill for each worktree. The `gitlens.graph.overviewBar.visibility` setting controls when the bar appears: `dirtyWorktrees` (default) includes other worktrees only when they have working changes or unpushed commits, `worktrees` shows the bar when the repository has more than one worktree, `always` always shows it, and `never` hides it.

### Follow the Active Terminal

When the Commit Graph is already visible, it follows the terminal you're working in. Switching to a terminal, or to a Claude Code conversation tab, selects the Working Changes row of the repository or worktree that terminal is in. If an agent session is running in the terminal, the graph follows the agent's worktree. The graph never opens on its own, and the first time it follows a terminal, a tip explains the behavior and offers **Turn Off**.

- To stop following, select **Stop Following Active Terminal** in the Commit Graph's **More Actions** (⋯) menu, or set `gitlens.graph.followTerminal.enabled` to `false`. Select **Follow Active Terminal** to turn it back on.
- By default, terminals in other repositories are ignored. To let the graph switch repositories, set `gitlens.graph.followTerminal.allowRepositorySwitching` to `true`.

### Configuration and Layout

The Commit Graph offers extensive layout and configuration options so you can tailor the view to fit your workflow.

---

#### Column Customization

All columns in the Commit Graph are fully customizable:

- Drag and drop column headers to rearrange the layout.
- Right-click a column header to toggle columns on or off.
- Right-click a column header and select **Group Graph Column** or **Group Branches / Tags Column** to show that content inside the adjacent column. Select **Ungroup Graph Column** or **Ungroup Branches / Tags Column** to give it its own column again.
- Right-click a column header, or use the gear in the **Graph** column header, to manage the layout of columns and panels (minimap, side bar, and details panel):
  - **Save as Default Layout** — Saves the current layout as your default. New workspaces open with it.
  - **Apply Saved Layout** — Applies your saved default layout to the current workspace. This item appears only after you save a default.
  - **Reset Layout** — Restores the original columns and panels.
- The **Changes** column visualizes added and deleted lines per commit. The `gitlens.graph.changesColumn.mode` setting controls the display style: `numbers` (numeric counts), `squares` (colored blocks), `bar` (horizontal bar), or `bipolar` (split additions/deletions bar).

<figure>
  <img src="/wp-content/uploads/gl-column-gl-settings-01-01-v2@2x.png" alt="Commit Graph settings menu showing options to hide the Author, Date, SHA, Changes, and other columns, switch the graph layout, and use a compact layout" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Customize visible columns and the layout from the column settings menu</figcaption>
</figure>

---

#### Panel vs. Editor Layout

You can choose where the Commit Graph appears:

- **Panel Layout** — displays the graph in the bottom panel (next to Terminal) with the embedded details panel.
- **Editor Area Layout** — shows the graph in a standard VS Code editor tab.

To switch layouts:

1. Open the **More Actions…** (⋯) menu in the top-right of the Commit Graph editor tab (or of the Commit Graph view in the side bar).
2. Select **Prefer Commit Graph in Editor** or **Prefer Commit Graph as a View**.

You can even open both layouts simultaneously.

<figure>
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location-01-v4@2x.png" alt="The Commit Graph open in the editor area with the tab's More Actions (…) menu expanded, listing Prefer Commit Graph in Editor and Prefer Commit Graph as a View among the editor actions" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Choose where the graph displays: in the editor area or as a view</figcaption>
</figure>

---

#### Compact Layout

For smaller screens or simplified views:

- **Use Compact Graph Column** reduces the visual size of the graph.
- The **Author** column shows avatars when minimized.
- Columns display icons instead of truncated text when resized to narrow widths.

To enable the compact graph layout, select the gear in the **Graph** column header and choose **Use Compact Graph Column**.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-compact-graph-01-v3@2x.gif" alt="Compact Commit Graph layout toggle showing the graph switching from normal to compact view with icons and avatars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Enable compact mode for cleaner visuals</figcaption>
</figure>

---

#### Scroll Markers

Scroll markers appear alongside the Commit Graph scrollbar to highlight:

- Checked-out branches
- Selected rows
- Search matches

They provide quick navigation to key locations like `HEAD` or specific refs.

You can toggle scroll markers in [Commit Graph settings](#settings).

<figure>
  <img src="/wp-content/uploads/gl-scroll-markers.png" alt="Scroll markers in the GitLens Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Navigate instantly using visual markers</figcaption>
</figure>


### Settings

You can adjust Commit Graph preferences through the GitLens Settings panel.

1. Open the Command Palette:  
   <kbd>Cmd/Ctrl + Shift + P</kbd>

2. Search for:  
   `GitLens: Open Settings`

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-settings-01-v4@2x.png" alt="VS Code Command Palette filtered to &quot;GitLens: Settings&quot; with the GitLens: Open Settings command highlighted, the step that opens the GitLens settings for the Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access GitLens settings from the Command Palette</figcaption>
</figure>

---

### Repository Health

GitLens keeps Git fast in your repositories. While VS Code is open, it runs safe, repository-local Git maintenance in the background at most once a day: it packs loose objects, repacks incrementally, and writes the commit-graph cache. This is the same routine work that `git gc` and `git maintenance` do, and it doesn't change your history. To turn it off, set `gitlens.gitOptimizations.enabled` to `false`, which also turns off Repository Health.

The **Repository Health** visualization in the Commit Graph shows the state of each optimization and suggests the ones that would help your repository. To open it, run `GitLens: Show Repository Health` from the Command Palette, or select **Show Visualizations & Health** in the Commit Graph side bar and choose **Repository Health**.

<figure>
  <img src="/wp-content/uploads/gl-graph-repository-health-01-v2@2x.png" class="help-center-img img-bordered" alt="The Repository Health visualization in the Commit Graph, with the ringed verdict &quot;This repository is in good shape&quot; above its facts strip and the Optimizations ledger listing the Commit-graph cache, Untracked cache, File system monitor, Scheduled maintenance, Large-repository index and Sparse index rows with their status, and Run Maintenance Now in the header." />
</figure>

The view shows a verdict for the repository and an **Optimizations** list:

- **Commit-graph cache** — Accelerates history walks and file history. GitLens maintains it automatically.
- **Untracked cache**, **File system monitor**, **Large-repository index**, **Sparse index**, and **Scheduled maintenance** — Optional optimizations that change your repository's Git config or register it with your operating system's scheduler. GitLens never applies them automatically. Select **Enable** to apply one, and **Undo** to restore the previous value.

Select **Run Maintenance Now** to run the maintenance tasks immediately. When GitLens notices that Git operations have been slow, or that the repository is very large, a banner above the graph offers **Show Repository Health**. Dismissing the banner hides it for that repository.

---

### Rich Commit Search

The Commit Graph includes a powerful search bar to locate commits by message, author, file, or even specific code changes.

#### Natural Language Search `PRO`

You can type plain-language queries (e.g., "changes to the login page last week") and GitKraken AI converts them into structured Git search operators automatically. Natural language search works in the Commit Graph search bar, the Search & Compare view, and the Search Commits command.

In the Commit Graph, hover the query to see how GitKraken AI interpreted your request. Phrasing such as "only my commits" turns on filtering for that search, and "take me to…" jumps to the first match. If a natural language search finds nothing, the search box suggests ways to widen it, such as dropping the date filter or searching across all branches, each with its result count. If AI isn't available, select **Search as text instead** to run your words as a plain message search.

If a pattern with **Regular expression** turned on isn't valid regex, the Commit Graph matches it literally and dims the regex toggle. When that search finds nothing, you can choose **Match literally**, or **Fix with AI** to have GitKraken AI repair the pattern. A results bar under the graph shows how many matches are loaded (for example, "Showing 25 of 60 results"), with **Load More Results…** to load the rest.

#### Search Prefixes

Use the following search prefixes:

- `commit:`
- `message:`
- `-message:` (excludes commits whose message contains the term; can't be combined with `message:` in the same query)
- `author:`
- `committer:` (also accepts `@me`)
- `file:`
- `change:`
- `type:merge` or `is:merge` (shows only merge commits)
- `@me` (to filter commits made by your user)
- Time-based operators such as `after:` and `before:` to scope results by date

<figure>
  <img src="/wp-content/uploads/gl-rich-commit-search-02-v3@2x.png" alt="Commit Graph search bar highlighting results" class="img-responsive center img-bordered">
  <figcaption style="text-align: center; color: #888">Search commit history with advanced filtering</figcaption>
</figure>

Use keyboard shortcuts to navigate results:

- <kbd>F3</kbd> / <kbd>Cmd+G</kbd> — next result  
- <kbd>Shift+F3</kbd> / <kbd>Shift+Cmd+G</kbd> — previous result  
- Hold <kbd>Shift</kbd> and click arrows to jump to first or last match

The Commit Graph has more keyboard shortcuts. Press <kbd>?</kbd> in the graph to open the keyboard shortcuts reference, which includes the following:

- <kbd>/</kbd> — find a branch, tag, or worktree
- <kbd>Ctrl/Cmd+F</kbd> — search commits
- <kbd>1</kbd> through <kbd>9</kbd>, and <kbd>0</kbd> — jump to a recent worktree
- <kbd>Alt+1</kbd> through <kbd>Alt+8</kbd> — toggle a side bar panel
- <kbd>Alt+M</kbd>, <kbd>Alt+S</kbd>, and <kbd>Alt+D</kbd> — toggle the minimap, side bar, and details panel

To change or turn off a shortcut, hover it in the reference to see its shortcut id, then set that id in `gitlens.graph.shortcuts.overrides` to a new key combination or to `false`. The reference's **Customize…** link opens these settings. To turn off all customizable shortcuts, set `gitlens.graph.shortcuts.enabled` to `false`; navigation keys such as the arrows, <kbd>Enter</kbd>, and <kbd>Esc</kbd> always work.

<figure>
  <img src="/wp-content/uploads/gl-commit-search-moving-arrow-keys-02-v4@2x.gif" alt="Navigating commit search results with arrow keys in the Commit Graph, showing the selection jumping between matching commits" class="img-responsive center img-bordered">
  <figcaption style="text-align: center; color: #888">Jump through results using keyboard or search controls</figcaption>
</figure>

You can also refine results with:

- **Match all**
- **Match case**
- **Regular expression**

<figure>
  <img src="/wp-content/uploads/gl-search-options-01-v3@2x.png" alt="Commit Graph search box with the query &quot;fix&quot; and a ring around the search option toggles at its right end: Match Case, Match Whole Word, Use Regular Expression and Match All, next to the 1 of 6 result counter" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Adjust search filters for more precision</figcaption>
</figure>

---

### Full Context Menu Support

The Commit Graph supports right-click actions on branches, commits, tags, authors, and column headers.

<figure>
  <img src="/wp-content/uploads/gl-context-menu.gif" alt="Right-click menu on commit for extra options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Use context menus for advanced Git actions</figcaption>
</figure>

Popular options include:

- **Compare with Common Base** — View changes between the current and selected branches based on their shared ancestor.
- **Open All Changes with Common Base** — Launch a multi-diff view showing all changes that would be merged.
- **Squash**, **Drop**, **Reword**, and **Modify Commits** — Run interactive rebase operations directly from the graph without opening the Rebase Editor. Select one or more commits, right-click, and choose the desired operation.
- **Fixup Commit...** — Right-click a commit to select the Working Changes row and pre-fill the commit message with `fixup! <subject>` of that commit. The commit button becomes **Commit Fixup**, and its menu adds **Commit Fixup & Squash**.
- **Squash Fixups...** — Right-click the current branch to fold its `fixup!` commits into the commits they target, after a confirmation.
- **Undo Commit** — Appears as an inline action on the HEAD commit row to soft-reset the latest commit.
- **Push to Commit** — Appears as an inline action on unpushed commit rows to push up to that specific commit.

---

### Compare Mode `PRO`

Compare mode lets you view comparisons directly inside the Commit Graph rather than switching to the Search & Compare view. Select two references to see Ahead, Behind, and All views inline within the graph details panel.

---

### Compose Mode `PRO`

Compose mode integrates commit composition directly within the Commit Graph. Select the Working Changes row to see your uncommitted work, then switch to Compose mode in the details panel to create commits from those changes or to reorganize branch history. GitKraken AI can propose the commits and messages for you to review and refine before applying them.

<figure>
  <img src="/wp-content/uploads/gl-commit-composer-17-4-01-v6@2x.png" alt="Commit Graph in Compose mode: the ringed Compose (wand) action on the Working Changes row, and the composer panel beside the graph listing Staged changes and Unstaged changes entries, the changed files, and the Instructions box with the Compose button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Compose mode in the Commit Graph details panel</figcaption>
</figure>

Click the **Compose** button to generate an AI-assisted commit message based on your staged changes, or write your own message manually.

<figure>
  <img src="/wp-content/uploads/commit-composer-composed-17-4.png" alt="Commit Graph composer with AI-generated commit message ready for review" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit message populated in the composer</figcaption>
</figure>

---

### Multi-File Selection

The Commit Graph and Inspect panels support multi-file selection using <kbd>Shift</kbd>-click and <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>-click in Working Changes, commit details, compare, compose, and review file lists. Selected files can be batch-operated on with stage, unstage, discard, and stash actions. Inline per-file action buttons are also available for individual operations.

To ignore untracked files, right-click one or more of them in Working Changes and select **Add to .gitignore**. GitLens appends an entry for each file to the `.gitignore` at the repository root, creates that file if it doesn't exist, and opens it so you can review the change.

### Pull Request Indicators

For GitHub and GitLab, GitLens displays a **Pull Request icon** on branches with active pull requests. To enable this:

1. Connect your account using [rich integration settings](/gitlens/gitlens-settings/#remote-provider-integration-settings).
2. The icon will appear next to branches in the graph once linked.

<figure>
  <img src="/wp-content/uploads/gl-pull-request-icon-01-v3@2x.png" alt="The Commit Graph with the fixture/code-suggest-demo branch pill ringed: after the branch name and its origin remote the pill carries the pull-request icon, which marks the branch as having an associated open pull request" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Active pull requests are shown with branch-level icons</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

You can hide individual remotes, branches, or tags from the Commit Graph to reduce clutter and focus your view.

- **To hide**: Right-click a branch or tag pill and select **Hide Local Branch**, **Hide Remote Branch**, or **Hide Tag**. To hide every branch of a remote, including branches added later, right-click a remote branch pill or a remote in the side bar's **Remotes** panel and select **Hide Remote**. To hide whole classes of refs, use the scope/filter popover next to the search box.
- **To show again**: Use the **Hide** panel at the top of the graph and reselect the ref. Hidden refs also stay listed, dimmed, in the side bar's **Branches**, **Remotes**, and **Tags** panels; right-click one and select **Show Local Branch**, **Show Remote Branch**, **Show Tag**, or **Show Remote**. Showing one branch of a hidden remote keeps the rest of that remote hidden.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs-01-v3@2x.gif" alt="Hiding a branch in the Commit Graph: right-clicking the conflict-branch ref opens its context menu, and choosing Hide Local Branch removes the ref from the graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Use the “Hide” option to declutter the graph</figcaption>
</figure>

#### Filtering Options

You can further control what is shown using the filter dropdown:

- **All Branches** — Display all branches
- **Current Branch** — Display the current branch and its upstream (minimal view)
- **Smart Branches** — Display only the relevant branches: the current branch, its upstream, and its base or target branch
- **Agent Branches** — Display only branches with currently running agents or agents idle for less than 24 hours
- **Favorited Branches** — Display only the branches you starred as favorites

  The Agent Branches and Favorited Branches modes don't add the current branch automatically. When a mode narrows the graph, a bar under the graph shows how many of the matching branches are loaded (for example, "Showing 3 of 8 branches"), with **Load More…** to load the rest.
- Toggle visibility of:
  - Remote-only branches
  - Tags
  - Stashes
- Option to **dim merge commits**

<figure>
  <img src="/wp-content/uploads/gl-filter-options-2-01-v4@2x.png" alt="The Commit Graph branch-visibility menu: All, Current, Smart, Agent and Favorited Branches, Focus Branch and Focus Pull Request, and under Graph Options the ringed toggles for remote-only branches, stashes and tags, then Simplify Merge History and Dim Merge Commit Rows" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Customize your view with filter presets</figcaption>
</figure>

---

### Minimap

The **Minimap** gives you a visual summary of repository activity at a glance:

- Quickly locate `HEAD`, remotes, tags, and stashes
- Jump to any region in the graph using visual cues
- Toggle it via the **Minimap icon** in the top right

<figure>
  <img src="/wp-content/uploads/gl-minimap-2.png" alt="Minimap view in Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Quickly navigate with the Commit Graph Minimap</figcaption>
</figure>

#### Minimap Settings

Customize the Minimap via the **gear at the right end of the minimap**:

- Toggle between:
  - **Commits view**
  - **Lines changed view**
- Show or hide:
  - Markers for branches, tags, stashes, search results

<figure>
  <img src="/wp-content/uploads/gl-minimap-gl-settings-01-v4@2x.png" alt="Commit Graph with the minimap strip above the rows and its Minimap Options popover open: a Minimap group with Commits (selected), Lines Changed and Reverse Direction, and a Markers group with checkboxes for Local Branches, Remote Branches, Pull Requests, Stashes, Tags and Worktrees" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Choose your preferred Minimap display and markers</figcaption>
</figure>

#### Minimap Legend

| Element | Description |
|--------|-------------|
| **Green lines** | `HEAD` |
| **Yellow lines** | Search results |
| **Blue blocks (top)** | Remote branches |
| **Brown blocks (top)** | Tags |
| **Pink blocks (bottom)** | Stashes |
| **Blue blocks (bottom)** | Local branches |
| **Highlighted area** | Current view region |

> **Note:** We welcome your feedback on the Minimap. Share your thoughts on the [GitLens GitHub Discussions](https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133).

To send feedback from inside VS Code, select **Send Feedback...** (the feedback icon) in the Commit Graph toolbar, or **Send Feedback** in the header's account popover. In the dialog, choose **General**, **Bug**, or **Feature**, write your message, and select **Send Feedback**. You don't need to be signed in. When you send a bug report, GitLens also opens a GitHub issue prefilled with your message so you can add details.

***

## Visual History

For workflows and examples, see [Visual History](/gitlens/gl-visual-file-history/).

Visual History (formerly Visual File History) provides a clear timeline of changes—showing when, what, and who modified your code—helping you quickly understand how a file, folder, repository, or branch evolved.

Visual History supports multiple scopes:

- **File** — View the history of a single file
- **Folder** — View the history of a directory
- **Repository** — View the history of the entire repository
- **Branch** — Slice the history by branch to focus on specific lines of work

To open Visual History:
- Use the GitLens **Inspect Sidebar**, or
- From the **Command Palette**: `Cmd/Ctrl + Shift + P` → `GitLens: Show Visual History View`

<figure>
  <img src="/wp-content/uploads/gl-visual-file-history-01-v3@2x.png" alt="Visual History view for CHANGELOG.md showing eight commits by four authors plotted as colour-coded bubbles over the last four weeks, with the additions and deletions of each commit shown as bars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Track authorship, size, and timing of file changes</figcaption>
</figure>

---

### How to Read the Graph

- **Y-axis (left):** Contributors, shown in individual swim lanes
- **X-axis:** Timeline of commits
- **Bubbles:** Color-coded per author; bubble size reflects the magnitude of changes
- **Bars (right y-axis):** Line additions (green) and deletions (red)

Hover over a bubble or bar for detailed insights.

<figure>
  <img src="/wp-content/uploads/visual-file-history-hover.png" alt="Hover over commit for details" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View commit size, author, and message on hover</figcaption>
</figure>

> **Warning:** The Community plan supports Visual History only on public and local repositories.

***

## Commit File Details in Large Histories

In repositories where loading commit file details has been slow, the Commits view and other history views load a commit's or stash's file details only when they're shown. This makes large histories open faster, at the cost of one extra Git call each time you view a commit's files. GitLens applies this automatically only in repositories where it has recorded slow file-detail loading, and only while `gitlens.gitOptimizations.enabled` is on.

To choose the behavior yourself, set `gitlens.advanced.commits.delayLoadingFileDetails`: `true` always delays loading file details, `false` never delays, and `null` (the default) lets GitLens decide per repository.
