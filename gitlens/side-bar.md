---
title: Using the GitLens Sidebar
description: Explore GitLens sidebar views for working with repositories, authors, commits, and branches.
taxonomy:
  category: gitlens
last_updated: 2026-09
---

<kbd>Last updated: September 2026</kbd>

GitLens provides multiple sidebars that extend the functionality of Visual Studio Code, making it easier to navigate and understand your Git repositories. These include:

- **GitLens Inspect** — View blame annotations, code lenses, and commit details.
- **GitLens** — Access features like commit history, branches, and remotes.
- **Source Control** — Integrates with GitLens to enhance the built-in source control panel.

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Community, Pro, etc

***

## Use the GitLens Sidebars

GitLens offers three sidebars in Visual Studio Code that enhance Git workflows with rich visualizations, insights, and collaboration tools.

### GitLens Inspect Sidebar

The **GitLens Inspect** sidebar provides contextual information about your current file, line, or repository activity. Use it to dive into commit details, history, and comparisons.

This sidebar includes:

- **Commit Details**
- **Overview**
- **Line History**
- **File History**
- **Visual History**
- **Search & Compare**

<figure>
  <img src="/wp-content/uploads/gl-inspect-side-bar.png" class="help-center-img img-bordered" alt="GitLens Inspect sidebar overview">
</figure>

### GitLens Sidebar

The **GitLens** sidebar is where you start working in GitLens. It holds the Commit Graph, the GitLens onboarding guide, and collaboration views.

This sidebar includes:

- **Graph** — The [Commit Graph](/gitlens/gl-commit-graph/)
- **Welcome** — The GitLens onboarding guide, with walkthroughs of GitLens and the Commit Graph
- **Launchpad** `PRO` — Hidden by default
- **Cloud Patches** `PRO` — Hidden by default
- **Cloud Workspaces** — Hidden by default

GitLens 19.2 removed the Home view. Your GitKraken account and the setup status of AI, agents, and integrations now appear in the account menu in the Commit Graph header. Links that used to open the Home view open the Commit Graph instead.

<figure>
  <img src="/wp-content/uploads/gl-home-view-v16.png" class="help-center-img img-bordered" alt="GitLens sidebar">
</figure>

#### Start in the Commit Graph

The [**Commit Graph**](/gitlens/gl-commit-graph/) is your starting point in GitLens, providing visibility into current work and recent activity. To get the most out of it, [connect your Git provider and issue integrations](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

From the Commit Graph you can see:

- The active repository and branch, sync status, and merge target, along with actions for fetch/push/pull. Linked PRs or issues appear when available, or you can start a new PR.
- Working changes across your worktrees, including work in progress outside the worktree you currently have open.
- Branches, commits, and recent activity across your repository, so you can find and return to the work you were last on.
- Supported coding agent sessions and their status, including sessions that need your attention.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-full-01-v2@2x.png" class="help-center-img img-bordered" alt="The Commit Graph filling the GitLens side bar: the branch toolbar with Push and Fetch, the natural-language search box, the Working Changes row, and commit rows with branch and tag pills, authors, and short SHAs.">
</figure>

### Source Control Sidebar

The **Source Control** sidebar enhances VS Code’s native Git interface with additional GitLens-powered views.

This sidebar includes:

- Commits
- Branches
- Remotes
- Stashes
- Tags
- Worktrees
- Contributors
- Repositories

<figure>
  <img src="/wp-content/uploads/gl-source-control.gif" class="help-center-img img-bordered" alt="GitLens Source Control sidebar with enhanced Git views">
</figure>

Views can be detached from the sidebar and [moved](/gitlens/side-bar/#moving-views) or reattached using the ellipsis icon menu.

<figure>
  <img src="/wp-content/uploads/gl-source-control-detach.png" class="help-center-img img-bordered" alt="Detaching GitLens views from the Source Control sidebar">
</figure>

### Move Views Between Sidebars

You can move any GitLens view between the GitLens Inspect, GitLens, and Source Control sidebars. To move a view, simply drag and drop it to the desired sidebar.

<figure>
  <img src="/wp-content/uploads/move-view.gif" class="help-center-img img-bordered" alt="Drag and drop GitLens views to reposition them between sidebars">
</figure>

To restore the default layout, open the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and run:

<kbd>View: Reset View Locations</kbd>

***
 
## Commits View

<figure>
  <img src="/wp-content/uploads/gl-commits-view-01-v2@2x.png" class="help-center-img img-bordered" alt="GitLens Commits view">
</figure>

A [customizable](/gitlens/settings/#commits-view-settings) view to visualize, explore, and manage Git commits.

The **Commits** view displays all commits on the current branch. It also provides:

- A toggle to show all commits or only your own
- A toggle to switch file layout: list, tree, or auto
- A branch comparison tool — compare the current branch (or working tree) with a selected branch, tag, or ref
  - **Behind** — shows commits missing from the current branch
  - **Ahead** — shows commits present on the current branch but not on the selected reference
- Branch status with upstream info:
  - **Publish** — option to publish if not yet pushed
  - **Up to date** — when synced with remote
  - **Changes to pull** — if commits are available on the remote
  - **Changes to push** — if there are local unpublished commits
  - **Merging or rebasing** — indicates in-progress merge or rebase actions and lists conflicted files

<figure>
  <img src="/wp-content/uploads/commits-view-merge.png" class="help-center-img img-bordered" alt="GitLens Commits view with merge in progress">
</figure>

<figure>
  <img src="/wp-content/uploads/commits-view-rebase.png" class="help-center-img img-bordered" alt="GitLens Commits view with rebase in progress">
</figure>

- Associated pull request — displays if a pull request is linked to the current branch

In repositories where loading commit file details has been slow, the Commits view and other history views load a commit's file details on demand instead of up front. This automatic behavior requires `gitlens.gitOptimizations.enabled`. To always or never delay loading file details, set `gitlens.advanced.commits.delayLoadingFileDetails` to `true` or `false`.

***

## GitLens Inspect

The **GitLens Inspect** sidebar focuses on providing contextual insights related to the code you're working on. It includes two tabs: **Commit Details** and **Overview**.

To open GitLens Inspect, launch the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and run:

<kbd>GitLens: Show Inspect View</kbd>

### Commit Details

The **Commit Details** tab updates as you move your cursor through the file or select a commit in the Commit Graph. It shows information such as commit author, ID, modified files, and autolinks.

<figure>
  <img src="/wp-content/uploads/gl-inspect-commit-details-01-v3@2x.png" class="help-center-img img-bordered" alt="GitLens Inspect view showing the details of the commit under the caret: the author and date, the commit message ending in &quot;Closes #7&quot;, the Autolinks section listing the resolved #7 pull-request chip, and the changed file">
</figure>

### Overview

The **Overview** tab helps you stage or unstage changes, open files to view modifications, and access associated pull requests. You can also [suggest changes or view Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) when working on a pull request.

<figure>
  <img src="/wp-content/uploads/gl-inspect-overview-01-v3@2x.png" class="help-center-img img-bordered" alt="GitLens Inspect view showing the Overview of the working changes: the Compose and Review mode toggle, the Working row with its change counts, and the three modified TypeScript files">
</figure>


***

## Repositories View

<figure>
  <img src="/wp-content/uploads/gl-repositories-view-01-v3@2x.png" class="help-center-img img-bordered" alt="GitLens Repositories view with the Playground2026 repository expanded: its upstream status on the repository row and the sub-views beneath it — Commits, Branches, Remotes, Tags, Worktrees and Contributors (Stashes is an optional sub-view, off by default)">
</figure>

A hidden by default, [customizable](/gitlens/settings/#repositories-view-settings) view to visualize, explore, and manage Git repositories.

The **Repositories** view lists all open Git repositories. It includes:

- A toggle to auto-refresh repository changes
- A toggle to switch file layout: list, tree, or auto
- Upstream status indicators:
  - No dot — branch unpublished or no changes
  - Green dot — commits ahead of upstream
  - Red dot — commits behind upstream
  - Yellow dot — ahead and behind
- A branch comparison tool — compare the current branch with a selected branch, tag, or ref:
  - **Behind** — commits missing from current branch
  - **Ahead** — commits present in current branch only
- Optionally show:
  - Changed files in the working tree
  - Current branch status with upstream (e.g., publish, up to date, changes to pull or push)
  - Associated pull request
  - Commit history (like the Commits view)
  - Local branches (like the Branches view)
  - Remotes and branches (like the Remotes view)
  - Stashes, tags, and contributors
  - **Incoming Activity** (experimental) — recent merge and pull events

***


## File History View

<figure>
  <img src="/wp-content/uploads/file-history-view.png" class="help-center-img img-bordered" alt="GitLens File History view">
</figure>

A [customizable](/gitlens/settings/#file-history-view-settings) view to visualize, navigate, and explore the revision history of the current file or selected lines.

The **File History** view lists all commits that modified the current file on the active branch. It includes:

- A toggle to pin (pause) automatic tracking of the current editor
- A toggle to switch between file and line history
- A toggle to switch between **Commits** mode (default) and **Contributors** mode, which shows all contributors to the file instead of the commit list
- The ability to change the base branch or reference for history
- (File history only) A toggle to follow renames
- (File history only) A toggle to show commits from all branches
- Merge conflict status (if applicable):
  - **Merge Changes** — compare base and incoming changes to aid in resolving conflicts

<figure>
  <img src="/wp-content/uploads/file-history-view-merge-conflict.png" class="help-center-img img-bordered" alt="File History view showing a merge conflict">
</figure>

***

## Line History View

<figure>
  <img src="/wp-content/uploads/gl-line-history-view-01-v2@2x.png" class="help-center-img img-bordered" alt="GitLens Line History view">
</figure>

A hidden by default, [customizable](/gitlens/settings/#line-history-view-settings) view to visualize, navigate, and explore the revision history of the selected lines of the current file.

The **Line History** view lists all commits that modified the selected lines. It provides:

- A toggle to pin (pause) automatic tracking of the current editor
- The ability to change the base branch or reference
- Merge conflict status (if applicable):
  - **Merge Changes** — compare base and incoming changes to aid in resolving conflicts


***

## Branches View

<figure>
  <img src="/wp-content/uploads/gl-branches-view-01-v3@2x.png" class="help-center-img img-bordered" alt="GitLens Branches view showing local branches with upstream status indicators, commit history, and branch comparison tools">
</figure>

A [customizable](/gitlens/settings/#branches-view-settings) view to visualize, explore, and manage Git branches.

The **Branches** view lists all local branches and includes:

- A repository filter with an **All Repositories excluding worktrees** option that hides linked worktrees whose main repository is also open
- A toggle to switch between list or tree layout
- A toggle to change file layout: list, tree, or auto
- Upstream status icons:
  - No dot — branch unpublished or no changes
  - Green dot — ahead of upstream
  - Red dot — behind upstream
  - Yellow dot — ahead and behind
- Status indicators:
  - `✓` — current branch
  - `▲` (green) — unpushed changes
  - `▼` (red) — unpulled changes
  - `▼▲` (yellow) — diverged from upstream
  - `▲+` (green) — unpublished branch
  - `!` (dark red) — missing upstream branch
- A comparison tool — compare a branch with another branch, tag, or ref:
  - **Behind** — commits missing from the branch
  - **Ahead** — commits present on the branch only
  - **Number of files changed** — across all comparison points
- Branch status:
  - **Publish** — shown for unpublished branches
  - **Changes to push** — unpublished commits
  - **Changes to pull** — incoming commits
- Associated pull request — shown when linked to a branch

***

## Remotes View

<figure>
  <img src="/wp-content/uploads/gl-remotes-view-01-v3@2x.png" class="help-center-img img-bordered" alt="GitLens Remotes view with two remotes: origin, expanded to show its GitHub provider icon, the gitkraken/Playground2026 repository and its remote branches with their last-commit dates, and a self-hosted enterprise remote below it">
</figure>

A [customizable](/gitlens/settings/#remotes-view-settings) view to visualize, explore, and manage Git remotes and remote branches.

The **Remotes** view lists all remotes and their remote branches. It includes:

- A toggle to switch between list or tree layout for branches
- A toggle to change file layout: list, tree, or auto
- A toggle to connect to supported remote providers for enhanced integration with pull requests, issues, avatars, and more

***

## Stashes View

<figure>
  <img src="/wp-content/uploads/stashes-view.png" class="help-center-img img-bordered" alt="GitLens Stashes view">
</figure>

A [customizable](/gitlens/settings/#stashes-view-settings) view to visualize, explore, and manage Git stashes.

The **Stashes** view lists all stashes and includes:

- A toggle to change file layout: list, tree, or auto

***

## Tags View

<figure>
  <img src="/wp-content/uploads/tags-view.png" class="help-center-img img-bordered" alt="GitLens Tags view">
</figure>

A [customizable](/gitlens/settings/#tags-view-settings) view to visualize, explore, and manage Git tags.

The **Tags** view lists all tags and includes:

- A toggle to switch tag layout: list or tree
- A toggle to change file layout: list, tree, or auto
- **Push Tag...** on a tag, or **Push Tags...** when you select several tags, to push tags to a remote. These actions appear when the repository has a remote.

When you push tags, GitLens asks you to choose a remote if the repository has more than one. The confirmation step includes a **Force** option that overwrites a tag that already exists on the remote. You can also push tags from the **GitLens: Git Command Palette** command by selecting **Tag** and then **Push Tags**.

***

## Launchpad View `PRO`

<figure>
  <img src="/wp-content/uploads/gl-launchpad-view-experimental.png" class="help-center-img img-bordered" alt="GitLens Launchpad view (experimental)">
</figure>

The **Launchpad** view provides an always-visible panel for pull request activity. You can view pull request details in a tree format and take action directly from the sidebar.

To enable this experimental feature, either run the _Show Launchpad View_ command or set `gitlens.views.launchpad.enabled` to `true` in your settings file.

***

## Workspaces

Workspaces offer a convenient way to group and manage multiple repositories for easy access. Whether working solo or as part of a team, Workspaces help streamline your development process. You can include local repositories or GitKraken Workspaces—cloud-hosted repositories or those managed through GitKraken services.

To access Workspaces, open the GitLens sidebar and find them in the lower-left panel. Alternatively, search "Workspaces" via the Command Palette.

> Note: Using cloud Workspaces requires a GitKraken account. Sharing cloud Workspaces requires a trial or paid subscription.

<figure>
  <img src="/wp-content/uploads/gl-workspaces-sidebar.png" class="help-center-img img-bordered" alt="GitLens Workspaces in the sidebar">
</figure>

### Creating a Workspace

Click the **+** icon next to GitKraken Workspaces to create a new Workspace. Enter a name and description, and optionally connect a provider.

<figure>
  <img src="/wp-content/uploads/gl-create-workspace.png" class="help-center-img img-bordered" alt="Create a GitLens Workspace">
</figure>

### Adding Repositories

Add repositories to your Workspace using the **+** icon under the Workspace tab. Click the Refresh icon to sync updates.

<figure>
  <img src="/wp-content/uploads/gl-add-repo-to-workspace.png" class="help-center-img img-bordered" alt="Add a repository to a Workspace">
</figure>

### Locating Repositories

To find a repository’s location on disk, click the **Locate Repositories** (pin icon). Select a parent folder, and GitLens will scan it for repositories.

<figure>
  <img src="/wp-content/uploads/gl-locate-repo-in-workspace.png" class="help-center-img img-bordered" alt="Locate a repo in a Workspace">
</figure>

### Opening Repositories

To open a repository, click the **Open Repository in New Window** icon. 

> Pro Tip: Hold <kbd>Alt/Option</kbd> while clicking to open in the current window.

<figure>
  <img src="/wp-content/uploads/gl-open-as-vscode-workspace.png" class="help-center-img img-bordered" alt="Open Workspace repository in VS Code">
</figure>

### Removing Repositories

Right-click a repository and choose **Remove repository from Workspace** to remove it.

<figure>
  <img src="/wp-content/uploads/gl-remove-repo-from-wrokspace.png" class="help-center-img img-bordered" alt="Remove repository from Workspace">
</figure>

### Converting to Cloud Workspaces

To convert a local Workspace, click **Convert to Cloud Workspace**, add a name and description, and save. Your Workspace will be available across GitKraken tools.

<figure>
  <img src="/wp-content/uploads/gl-convert-workspace-to-cloud.png" class="help-center-img img-bordered" alt="Convert local Workspace to GitKraken Cloud">
</figure>

### Workspace Indicators and Colors

Workspace status indicators use symbols and colors, such as a green **O** for the currently open Workspace.

<figure>
  <img src="/wp-content/uploads/gl-workspace-indicators-01-v3@2x.png" class="help-center-img img-bordered" alt="The Cloud Workspaces view filtered to Playground2026: under Current Window the repository is listed, and in the Demo2026 workspace the same repository is drawn in green with a green dot at the end of its row — the indicator for the repository open in the current window">
</figure>

### Workspace Linking

You can link a GitKraken Workspace to a VS Code workspace.

<figure>
  <img src="/wp-content/uploads/gl-create-vs-workspace-from-gl.png" class="help-center-img img-bordered" alt="Create a VS Code Workspace from GitKraken">
</figure>

Linked VS Code workspaces can be opened from their cloud counterpart using **Open VS Code Workspace in New Window** (hold <kbd>Alt</kbd> to open in the current window).

When you add repositories to a GitKraken Workspace, they can be auto-added to its linked VS Code workspace. You choose the auto-add behavior when creating the workspace and can modify it later via the **Change Linked Workspace Auto-Add Behavior** command.

<figure>
  <img src="/wp-content/uploads/gl-link-repositories-in-workspaces.png" class="help-center-img img-bordered" alt="Link repositories to VS Code workspace">
</figure>

To manually add repositories, use the **Add Repositories from Linked Workspace** command.


***

## Worktrees View

<figure>
  <img src="/wp-content/uploads/gl-worktrees-view-01-v2@2x.png" class="help-center-img img-bordered" alt="GitLens Worktrees view">
</figure>

A [customizable](gitlens/gitlens-settings/#worktrees-view-settings) view to create, view, and manage [Git worktrees](https://www.gitkraken.com/learn/git/git-worktree). Worktrees allow you to check out multiple branches at once within the same repository—useful for parallel development or testing workflows without switching branches.

### Create a Worktree

Select **Create Worktree...** to create a worktree. The confirmation step includes two groups of options:

- **Location**: Select **Root Folder…** to choose a different root folder for worktrees, or **Specific Folder…** to create the worktree directly in an exact folder instead of under the root.
- **After Creating**: Choose **Open in New Window**, **Open in Current Window**, **Add to Workspace**, or **Don't Open**.

Your **After Creating** choice updates the `gitlens.worktrees.openAfterCreate` setting, so GitLens uses it as the default the next time you create a worktree.

### Worktree Actions

Right-click a worktree in the Worktrees view to run these actions:

- **Start Agent Session...**: Starts a coding agent session in the worktree. GitLens uses your default agent from `gitlens.ai.defaultAgent`, or asks you to choose an agent if no default is set. Command-line agents open in a terminal in the worktree's folder.
- **Start Agent Session With...**: Asks you to choose the agent to start in the worktree.
- **Resume Agent Session...**: Opens a list of agent sessions you can resume.
- **Run Task on Worktree...**: Runs a VS Code task in the worktree's folder.

The agent session actions appear when GitLens AI features are enabled.

When you select **Run Task on Worktree...**, the list shows your recent tasks and the tasks defined in your workspace first. Select **All Tasks...** to see every available task. To set a default task, select the checkmark next to a task. The **Run Default Task** button on Working Changes rows in the Commit Graph runs the default task.

***

## Contributors View

<figure>
  <img src="/wp-content/uploads/gl-contributors-view-01-v2@2x.png" class="help-center-img img-bordered" alt="GitLens Contributors view">
</figure>

A hidden by default, [customizable](/gitlens/settings/#contributors-view-settings) view to explore repository contributors.

The **Contributors** view lists all contributors and includes:

- A toggle to change file layout: list, tree, or auto

***

## Search & Compare View

<figure>
  <img src="/wp-content/uploads/search-and-compare-view.png" class="help-center-img img-bordered" alt="GitLens Search and Compare view">
</figure>

A hidden by default, [customizable](/gitlens/settings/#search-and-compare-view-settings) view to search commit history or compare branches, tags, commits, and more.

The **Search & Compare** view displays pinnable results from search or comparison operations. It includes:

- A toggle to retain previous results
- A toggle to change file layout: list, tree, or auto

### Pinnable Search

Search commits by message, author, committer, file, ID, patch, or natural language query. AI-powered natural language search converts plain English queries into structured Git search operators, so you can search for commits by describing what you are looking for. Time-based search operators are also available for filtering by date ranges. If GitLens can't build a search from your description, it shows the reason and returns you to the search box with your description intact, so you can reword it. The Commit Graph search box offers more help, such as broader alternatives when a natural language search finds nothing and a **Match literally** option when a pattern isn't a valid regular expression. For details, see [Rich Commit Search](/gitlens/gl-commit-graph/#rich-commit-search).

Search using:

- **Search Commits** (`gitlens.showCommitSearch`):
  - `<message>` — message match
  - `-message:<message>` — excludes commits whose message contains the term. You can't combine `message:` and `-message:` in the same query.
  - `@<pattern>` — author match
  - `committer:<committer>` — committer match. Use `committer:@me` to match commits where you are the committer.
  - `#<sha>` — commit SHA
  - `:<path/glob>` — filename pattern
  - `~<pattern>` — patch content match
  - `type:merge` (or `is:merge`) — merge commits only
- **Show File History** (`gitlens.showQuickFileHistory`)
- **Show Commit** (`gitlens.showQuickCommitDetails`)

### Pinnable Comparison

Compare any two references:

- **Behind** — commits missing from the target branch
- **Ahead** — commits unique to the target branch
- **Number of files changed** — file diffs between the two references

Comparison commands include:

- `gitlens.views.compareWithUpstream`
- `gitlens.views.compareWithWorking`
- `gitlens.views.compareWithHead`
- `gitlens.views.compareWithSelected`
- `gitlens.views.compareAncestryWithWorking`

You can use checkboxes next to files to track review progress.
