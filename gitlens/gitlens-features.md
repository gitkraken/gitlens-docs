---
title: GitLens Features
description: Learn how to use GitLens in VS Code to see blame and history, work in the Commit Graph and Launchpad, use GitKraken AI, run guided Git commands, and connect integrations.
taxonomy:
  category: gitlens
last_updated: 2026-11
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

Features marked with <span style="color: #888;">`PREVIEW`</span> require a GitKraken Account, with access based on your [plan level](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens), such as Community or Pro.

***

## Revision Navigation

<figure>
  <img src="/wp-content/uploads/revision-navigation.gif" alt="GitLens revision navigation animated demo" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Step through revisions using built-in navigation commands</figcaption>
</figure>

Use Revision Navigation to compare different versions of a file or of specific lines.

Available commands:

- **Open Changes with Previous Revision** (`gitlens.diffWithPrevious`)  
  Compare the current file or revision with the previous commit.

- **Open Changes with Next Revision** (`gitlens.diffWithNext`)  
  Compare the current file or revision with the next commit.

- **Open Line Changes with Previous Revision** (`gitlens.diffLineWithPrevious`)  
  View how a specific line changed compared to the previous commit.

- **Open Changes with Working File** (`gitlens.diffWithWorking`)  
  Compare the committed version of the file with your working directory.

- **Open Line Changes with Working File** (`gitlens.diffLineWithWorking`)  
  See the difference between the last committed line and its current version.

- **Open Changes with Branch or Tag...** (`gitlens.diffWithRevisionFrom`)  
  Compare the file against another revision from a selected reference.

- **Open Changes with Revision...** (`gitlens.diffWithRevision`)  
  Compare the current file with any revision of the same file.


***

## Current Line Blame

<figure>
  <img src="/wp-content/uploads/gl-current-line-blame-01-v4@2x.png" alt="Editor with the current line's blame annotation shown inline at the end of the line: the author, the date and the start of the commit message" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Blame annotation showing author, date, and commit message</figcaption>
</figure>

Current Line Blame adds a [customizable](/gitlens/gitlens-settings/#current-line-blame-settings), and [themable](/gitlens/gitlens-settings/#themable-colors) annotation at the end of the active line.

By default, the annotation displays:

- The author of the most recent commit
- The commit date
- The commit message

You can control visibility with the command:

- **Toggle Line Blame** (`gitlens.toggleLineBlame`)


***

## Git CodeLens

<figure>
  <img src="/wp-content/uploads/gl-code-lens-01-v3@2x.png" alt="GitLens CodeLens annotations above file and code blocks" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Inline Git insights for authorship and history</figcaption>
</figure>

Git CodeLens shows Git information at the top of each file and above code blocks. It is on by [default](/gitlens/gitlens-settings/#git-codelens-settings), and you can [customize](/gitlens/gitlens-settings/#git-codelens-settings) it.

### CodeLens Types

- **Recent Change**  
  Shows the author and date of the most recent commit for the file or block.  
  - Click to open a **quick pick menu** with commit details and actions (e.g., compare, explore history).

- **Authors**  
  Displays the number of contributors and the most prominent author.  
  - Click to toggle Git blame annotations across the file.  
  - Hidden when the file or block has only one author.

### CodeLens Behavior

You can [customize](/gitlens/gitlens-settings/#git-codelens-settings) what each CodeLens does when you click it. Choose from:

- Toggle file blame annotations
- Compare the current commit to the previous one
- Show file or commit detail menus
- View commit history for the file or branch

### Related Command

- **Toggle Git CodeLens** (`gitlens.toggleCodeLens`)  
  Shortcut: `Shift+Alt+B`

***

## Status Bar Blame

<figure>
  <img src="/wp-content/uploads/gl-status-bar-01-v3@2x.png" alt="The right end of the VS Code status bar with the GitLens blame item ringed: the author and date of the commit for the current line, beside the line/column, indentation, encoding, line-ending and language items" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Quick access to blame details in the VS Code status bar</figcaption>
</figure>

The **Status Bar Blame** shows Git blame details for the current line in the VS Code status bar. It is on by default, and you can customize it.

### Default Behavior

- Displays the **author** and **date** of the last commit affecting the current line.
- Clicking the status bar opens a **quick pick menu** with commit actions (compare, explore history, etc.).

### Customizable Click Behavior

You can configure what happens when the status bar item is clicked:

- Toggle file blame annotations
- Toggle Git CodeLens on and off
- Compare the line's commit to the previous one
- Compare the line's commit to the working tree
- Show a quick pick menu with:
  - Commit details and actions *(default)*
  - File-level commit details
  - Commit history of the current file
  - Commit history of the current branch


***

## Hovers

GitLens shows [customizable](/gitlens/gitlens-settings/#hover-settings) hovers with Git information in your editor. Hovers are on by default and show both blame details and changes.

### Current Line Hovers

<figure>
  <img src="/wp-content/uploads/gl-hovers-current-line-01-v3@2x.png" alt="Hover tooltip over the current line blame annotation showing commit summary and author for the active line" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Git blame hover shown over the current line</figcaption>
</figure>

#### Details Hover

<figure>
  <img src="/wp-content/uploads/gl-hovers-current-line-details-01-v3@2x.png" alt="Details hover for the current line showing commit metadata, author, date, the commit message, and the quick-action command bar (SHA, copy, search, graph, Explain)" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Expanded commit info and quick actions</figcaption>
</figure>

Displays detailed commit information for the current line.

Features:

- **Automatic issue linking** for Bitbucket, Gerrit, Gitea, GitHub, GitLab, and Azure DevOps.
- **Quick-action bar** with commands:  
  _Open Changes_, _Blame Previous Revision_, _Open on Remote_, _Invite to Live Share_, _Show More Actions_.
- Click the **commit SHA** to trigger the _Show Commit_ command.

#### Changes (Diff) Hover

<figure>
  <img src="/wp-content/uploads/gl-hovers-current-line-changes-01-v3@2x.png" alt="Changes hover for the current line showing the inline diff of the commit that introduced the line, with a link to compare the two revisions" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View the diff of the commit that changed the current line</figcaption>
</figure>

Displays the previous version of the current line.

- Click **Changes** to run the _Open Changes_ command.
- Click commit SHAs to open _Show Commit_ views.

### Annotation Hovers

<figure>
  <img src="/wp-content/uploads/gl-hovers-annotations-01-v3@2x.png" alt="Hover tooltip over a blame annotation in the gutter showing commit summary and author information" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Hover insights while annotating with blame</figcaption>
</figure>

When blame annotations are on, hovering an annotation shows the same details and changes hovers.

#### Details Hover

<figure>
  <img src="/wp-content/uploads/gl-hovers-annotations-details-01-v3@2x.png" alt="Details hover over a blame annotation showing commit metadata, author, date, the commit message, and the quick-action command bar (SHA, copy, search, graph, Explain, PR)" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Commit metadata and action menu per line</figcaption>
</figure>

Shows rich commit details per line with:

- Automatic issue linking
- Quick-action command bar
- Clickable commit SHA to open commit details

#### Changes (Diff) Hover

<figure>
  <img src="/wp-content/uploads/gl-hovers-annotations-changes-01-v3@2x.png" alt="Changes hover over a blame annotation showing an inline diff with the previous version of the line" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Inline diff hover showing previous line content</figcaption>
</figure>

Reveals the previous version of each annotated line.

- Click **Changes** to run _Open Changes_.
- Click SHAs to open the _Show Commit_ view.


***

## File Blame

<figure>
  <img src="/wp-content/uploads/gl-gutter-blame-01-v3@2x.png" alt="File blame annotations in the editor gutter of README.md: every line carries the message and date of the commit that last changed it, so the blocks of lines from different commits stand out" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">See which commit last modified each line, and when — hover for the author</figcaption>
</figure>

File Blame adds [customizable](/gitlens/gitlens-settings/#file-blame-settings), [themable](/gitlens/gitlens-settings/#themable-colors) inline annotations that show the commit and author responsible for each line in a file.

### Features

- Displays **commit message** and **commit date** per line (enabled by [default](/gitlens/gitlens-settings/#file-blame-settings)).
- Adds a **heatmap (age) indicator** along the right edge to show how recently each line was changed.  
  _(See [File Heatmap](/gitlens/gitlens-features/#file-heatmap) for more info.)_
- Toggle annotations with:

  - **Command**: `gitlens.toggleFileBlame`
  - **Shortcut**: <kbd>Alt+B</kbd>
  - **Dismiss**: <kbd>Escape</kbd>


***

## File Changes

<figure>
  <img src="/wp-content/uploads/gl-gutter-changes-01@2x.png" alt="File Changes annotations in README.md with the gutter and line locations enabled: the uncommitted edits at the bottom of the file — one modified line and a new &quot;Release checklist&quot; section — are highlighted, with the matching marker in the gutter, while the unchanged lines above are plain" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Highlight unpublished or most recent changes</figcaption>
</figure>

The File Changes annotation highlights the lines you changed locally (unpublished) or that the most recent commit changed, so you can see which lines in a file changed. File Changes is [customizable](/gitlens/gitlens-settings/#file-changes-settings) and [themable](/gitlens/gitlens-settings/#themable-colors).

### Features

- **Highlights local changes** and recent commit modifications.
- Toggle with the command: `gitlens.toggleFileChanges`
- Press <kbd>Escape</kbd> to disable the annotations


***

## File Heatmap

<figure>
  <img src="/wp-content/uploads/gl-gutter-heatmap-01-v3@2x.png" alt="File heatmap annotations at the bottom of README.md with the gutter and line locations enabled: the gutter stripe and a faint line tint are colored by the age of each line's last change — the two recently edited lines at the bottom in hot red, the older lines above them in cool purple — and the older lines' text is faded" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Visualize how recently each line was modified</figcaption>
</figure>

The File Heatmap adds a color-coded bar to the edge of your file that shows which lines changed recently and which are older.

### Features

- Heatmap colors are [customizable](/gitlens/gitlens-settings/#file-heatmap-settings) and reflect line age:
  - **Hot (bright)** for recent changes
  - **Cold (dim)** for older changes  
    _(Lines default to "cold" after 90 days.)_
- Brightness adjusts dynamically based on the **median age** of all changes in the file.
- Toggle with the command: `gitlens.toggleFileHeatmap`
- Press <kbd>Escape</kbd> to hide the heatmap annotations

***

## Code Suggest <span style="color: #888;">`PREVIEW`</span>

Use GitKraken Code Suggest to propose edits to any file in a project, including lines that a pull request did not change. You can suggest changes from GitLens, GitKraken Desktop, or [gitkraken.dev](https://gitkraken.dev).

When a pull request is open, collaborators can review your suggestions and apply them to the pull request.

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> Code Suggest is currently supported only for repositories hosted on <strong>github.com</strong>.</p>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-code-suggest.png" alt="GitLens Code Suggest UI showing a PR suggestion in progress" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Suggest changes beyond just modified lines</figcaption>
</figure>

### How to Create a Code Suggestion

1. Open the [GitLens Inspect Overview](/gitlens/side-bar/#overview) for the repository.
2. Check out a branch that has an open pull request.
3. Click **Start Review for PR #PR**.
4. Modify and save any files to include in the suggestion.
5. When ready, select **Suggest Changes for PR**, add a title, and click **Create Code Suggestion**.

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-create.gif" alt="Creating a code suggestion in GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create a suggestion from your local changes</figcaption>
</figure>

After you submit the suggestion, the pull request receives a comment with 2 options:

- **Code Suggestion for #PR** — opens in gitkraken.dev
- **Locally on your machine** — opens in GitLens or [GitKraken Desktop](/gitkraken-client/pull-requests/#review-code-and-suggest-changes)

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-comment.png" alt="Comment with code suggestion options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Collaborators can choose where to review and apply suggestions</figcaption>
</figure>

### Accepting a Suggestion Locally

1. Open the suggestion in GitLens or GitKraken Desktop.
2. Review each modified file.
3. Select **Apply** to apply the patch to your current branch.  
   Or use the dropdown to **Apply to a Branch**.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" alt="Accepting suggestions from GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Apply suggestions directly to a local or new branch</figcaption>
</figure>

### Accepting a Suggestion on gitkraken.dev

1. Select **Code Suggestion for #PR** in the PR comment.
2. Review the changes on gitkraken.dev.
3. Click **Commit Suggestions** to commit the patch directly to the PR's branch.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion.gif" alt="Committing suggestions from gitkraken.dev" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Accept changes and push them to the remote branch</figcaption>
</figure>


***

## Cloud Patches <span style="color: #888;">`PREVIEW`</span>

Use Cloud Patches to share in-progress work with your team before you open a pull request.

### What Are Cloud Patches and Why Use Them?

Cloud Patches are Git patches that GitKraken stores in secure cloud storage, so you can share them across GitLens, GitKraken Desktop, and the GitKraken CLI. GitLens uploads the patch directly from your machine.

Because you can share work before a pull request exists, your team can give feedback earlier.

---

### How to Set Up Cloud Patches

Cloud Patches are on by default. You turn them on or off separately in each GitKraken app. To manage them in GitLens:

1. Open the Command Palette:  
   `Ctrl`/`Command` + `Shift` + `P` → **Preferences: Open User Settings (JSON)**

2. Add the following line to your settings:

       "gitlens.cloudPatches.enabled": true

To disable Cloud Patches, change the value to `false`.


### How to Work with Cloud Patches

Your Cloud Patches are in the **Cloud Patches** view in the GitLens side bar.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-create.webp" alt="GitLens Cloud Patch creation screen" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create a patch directly from your sidebar</figcaption>
</figure>

You can create a Cloud Patch from:

- Working Changes
- Commits
- Stashes
- Comparisons

To create one, use **Share as Cloud Patch** from the command palette or the **Share** submenu in applicable GitLens views.

<figure>
  <img src="/wp-content/uploads/gl-create-cloud-patch-example.png" alt="Share as Cloud Patch in context menu" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Share patches from a variety of Git sources</figcaption>
</figure>

#### Sharing Options

Choose how your patch can be accessed:

- **Anyone with the link** — Public access without signing in.
- **Anyone in my org** — Restricted to users in your GitKraken organization (GitKraken sign-in required).
- **Only collaborators** — Restricted to selected organization members. Use **Invite** to choose recipients.

Cloud Patches shared with you appear under the **Shared with Me** section.

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> If you're a member of multiple organizations, you can switch organizations from the GitKraken Account view.</p>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" alt="Cloud patch share dialog with access levels" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Control access to shared patches by role</figcaption>
</figure>

You can also apply a Cloud Patch from a shared URL. Click or paste the link, then follow the GitLens prompts to apply it to your working directory or to a new/existing branch.

<figure>
  <img src="/wp-content/uploads/gl-apply-patch-example.gif" alt="Apply a cloud patch animation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Apply a patch to your current repo</figcaption>
</figure>

To delete a Cloud Patch, right-click it and choose **Delete Cloud Patch...**.

<figure>
  <img src="/wp-content/uploads/gl-delete-cloud-patch-01-v3@2x.png" alt="Cloud Patches view in the GitLens sidebar showing a right-click context menu with Delete Cloud Patch option on a patch entry" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Remove unused patches with one click</figcaption>
</figure>


### Self-Hosting Cloud Patch Data

If you prefer not to store Cloud Patch data on GitKraken servers, you can configure GitLens to use your own AWS S3 storage. To set it up, see the [Self-Hosting Guide](/gk-dev/gk-dev-home/#self-hosted).

***

## Commit Graph

The Commit Graph is the starting point for working in GitLens. It shows your repository's history, branches, worktrees, Working Changes, pull requests, and supported agent activity in one view, so you can follow what is happening and move changes toward merge without switching tools. The graph stays responsive on large repositories.

The Commit Graph is included in **GitLens Community** and available to everyone on public and local repositories, with no account required. You need a <a href="https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens" target="_blank">GitLens Pro subscription or trial</a> only for private repositories.

If you are not signed in, opening the Commit Graph on a privately hosted repository for the first time starts a 3-day preview. A banner above the graph shows how much of the preview is left, with a **Sign In** link. When the 3 days are up, the graph shows **Commit Graph Preview Ended** for privately hosted repositories until you sign in or start a free Pro trial. The preview is only for signed-out use; a signed-in account without a Pro trial or paid plan sees the upgrade prompt on private repositories.

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

The Commit Graph header shows:

- **Repository** — the hosting provider's icon (hover it for the repository name; the editor tab is titled *Commit Graph: &lt;repository&gt;*)
- **Checked-out branch**
- **Last fetched time** — beside **Fetch** and in its hover
- **Account button** — your avatar and plan, last in the header

From here, you can:

- Click the branch name to switch branches
- Click **Fetch** to update commit data
- Click **Publish Repository** to open the Git Command Palette's **Publish** step with **Publish Repository…** selected. That choice creates a repository on a hosting provider and publishes the current branch to it. To add a remote of your own instead, choose **Add Remote…** (see [Git Command Palette](#git-command-palette)). **Publish Repository** replaces **Publish Branch** when the repository has no remotes, and **Fetch** is hidden then.
- Click the account button to open its popover. The popover holds your account actions (**Synchronize Status**, **Manage Account**, **Send Feedback**, and **Sign Out**), the AI model you use and your GitKraken AI usage, your agents, and your connected integrations. Sections that are not set up yet offer **Set up AI**, **Set up agents**, or **Set up integrations**, which open GitLens Settings.

<figure>
  <img src="/wp-content/uploads/gl-graph-info-01-v3@2x.png" srcset="/wp-content/uploads/gl-graph-info-01-v3@2x.png" alt="The top of the Commit Graph in the editor area: the tab reads &quot;Commit Graph: Playground2026&quot;, the header shows the current branch (main) with Push and &quot;Fetch (1wk ago)&quot; buttons, and the Fetch button's hover popover lists the upstream (origin/main on GitHub), &quot;Last fetched last week&quot; and the Auto-fetch option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access key branch controls directly from the header</figcaption>
</figure>

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> To share feedback on the Commit Graph, join the <a href="https://github.com/gitkraken/vscode-gitlens/discussions/2158" target="_blank">Commit Graph discussion on GitHub</a>.</p>
</figure>

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

You can change the Commit Graph's columns, where it opens, and how compact it is.

---

#### Column Customization

You can customize every column in the Commit Graph:

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

You can also open both layouts at the same time.

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

Use them to jump to locations such as `HEAD` or specific refs.

You can toggle scroll markers in [Commit Graph settings](/gitlens/gitlens-features/#settings).

<figure>
  <img src="/wp-content/uploads/gl-scroll-markers.png" alt="Scroll markers in the GitLens Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Navigate instantly using visual markers</figcaption>
</figure>


### Settings

You can adjust Commit Graph preferences in GitLens Settings:

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

GitLens keeps Git fast in your repositories. While VS Code is open, GitLens runs routine Git maintenance on each repository in the background. This is the same kind of work that `git gc` and `git maintenance` do, and it does not change your history. To turn it off, set `gitlens.gitOptimizations.enabled` to `false`, which also turns off Repository Health.

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

Use the Commit Graph search bar to find commits by message, author, file, or specific code changes.

#### Natural Language Search `PRO`

You can type plain-language queries (e.g., "changes to the login page last week") and GitKraken AI converts them into structured Git search operators automatically. Natural language search works in the Commit Graph search bar, the Search & Compare view, and the Search Commits command.

In the Commit Graph, hover the query to see how GitKraken AI interpreted your request. Phrasing such as "only my commits" turns on filtering for that search, and "take me to…" jumps to the first match. If a natural language search finds nothing, the search box suggests ways to widen it, such as dropping the date filter or searching across all branches, each with its result count. If AI is not available, select **Search as text instead** to run your words as a plain message search.

If a pattern with **Regular expression** turned on is not valid regex, the Commit Graph matches it literally and dims the regex toggle. When that search finds nothing, you can choose **Match literally**, or **Fix with AI** to have GitKraken AI repair the pattern. A results bar under the graph shows how many matches are loaded (for example, "Showing 25 of 60 results"), with **Load More Results…** to load the rest.

#### Search Prefixes

Use the following search prefixes:

- `commit:`
- `message:`
- `-message:` (excludes commits whose message contains the term; cannot be combined with `message:` in the same query)
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

The context menus include these actions:

- **Compare with Common Base** — View changes between the current and selected branches based on their shared ancestor.
- **Open All Changes with Common Base** — Launch a multi-diff view showing all changes that would be merged.
- **Squash**, **Drop**, **Reword**, and **Modify Commits** — Run interactive rebase operations directly from the graph without opening the Rebase Editor. Select one or more commits, right-click, and choose the desired operation.
- **Fixup Commit...** — Right-click a commit and select this action to select the Working Changes row and pre-fill the commit message with `fixup! <subject>` of that commit. The commit button becomes **Commit Fixup**, and its menu adds **Commit Fixup & Squash**.
- **Squash Fixups...** — Right-click the current branch to fold its `fixup!` commits into the commits they target, after a confirmation.
- **Undo Commit** — Appears as an inline action on the HEAD commit row to soft-reset the latest commit.
- **Push to Commit** — Appears as an inline action on unpushed commit rows to push up to that specific commit.

---

### Compare Mode `PRO`

Use Compare mode to view comparisons inside the Commit Graph instead of switching to the Search & Compare view. Select two references to see Ahead, Behind, and All views inline within the graph details panel.

---

### Compose Mode `PRO`

Use Compose mode to compose commits inside the Commit Graph. Select the Working Changes row to see your uncommitted work, then switch to Compose mode in the details panel to create commits from those changes or to reorganize branch history. GitKraken AI can propose the commits and messages for you to review and refine before applying them.

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

The Commit Graph and Inspect panels support multi-file selection using <kbd>Shift</kbd>-click and <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>-click in Working Changes, commit details, compare, compose, and review file lists. You can stage, unstage, discard, or stash all the selected files at once. Each file also has its own inline action buttons.

To ignore untracked files, right-click one or more of them in Working Changes and select **Add to .gitignore**. GitLens appends an entry for each file to the `.gitignore` at the repository root, creates that file if it does not exist, and opens it so you can review the change.

### Pull Request Indicators

For GitHub and GitLab, GitLens shows a **Pull Request icon** on branches with active pull requests. To show the icon, connect your account using [rich integration settings](/gitlens/gitlens-settings/#remote-provider-integration-settings). The icon then appears next to linked branches in the graph.

<figure>
  <img src="/wp-content/uploads/gl-pull-request-icon-01-v3@2x.png" alt="The Commit Graph with the fixture/code-suggest-demo branch pill ringed: after the branch name and its origin remote the pill carries the pull-request icon, which marks the branch as having an associated open pull request" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Active pull requests are shown with branch-level icons</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

You can hide individual remotes, branches, or tags from the Commit Graph to show only the refs you are working with.

- **To hide**: Right-click a branch or tag pill and select **Hide Local Branch**, **Hide Remote Branch**, or **Hide Tag**. To hide every branch of a remote, including branches added later, right-click a remote branch pill or a remote in the side bar's **Remotes** panel and select **Hide Remote**. To hide whole classes of refs, use the scope/filter popover next to the search box.
- **To show again**: In the Commit Graph header, select the hidden refs button (its tooltip reads, for example, *2 hidden branches and tags*) to open the **Hidden Branches / Tags** menu, then select the ref, or select **Show All**. Hidden refs also stay listed, dimmed, in the side bar's **Branches**, **Remotes**, and **Tags** panels; right-click one and select **Show Local Branch**, **Show Remote Branch**, **Show Tag**, or **Show Remote**. Showing one branch of a hidden remote keeps the rest of that remote hidden.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs-01-v3@2x.gif" alt="Hiding a branch in the Commit Graph: right-clicking the conflict-branch ref opens its context menu, and choosing Hide Local Branch removes the ref from the graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Hide a branch from the graph</figcaption>
</figure>

#### Filtering Options

You can further control what is shown using the filter dropdown:

- **All Branches** — Display all branches
- **Current Branch** — Display the current branch and its upstream (minimal view)
- **Smart Branches** — Display only the relevant branches: the current branch, its upstream, and its base or target branch
- **Agent Branches** — Display only branches with currently running agents or agents idle for less than 24 hours
- **Favorited Branches** — Display only the branches you starred as favorites

  The Agent Branches and Favorited Branches modes do not add the current branch automatically. When a mode narrows the graph, a bar under the graph shows how many of the matching branches are loaded (for example, "Showing 3 of 8 branches"), with **Load More…** to load the rest.
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

### Minimap <span style="color: #888;">(Experimental)</span>

The **Minimap** shows a summary of repository activity over time:

- Locate `HEAD`, remotes, tags, and stashes
- Jump to any region in the graph
- Toggle it with the **Minimap icon** in the top right

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

<div class='callout callout--basic'>
  <p>Note: To share feedback on the Minimap, join the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>Minimap discussion in GitLens GitHub Discussions</a>.</p>
</div>

To send feedback from inside VS Code, select **Send Feedback...** (the feedback icon) in the Commit Graph toolbar, or **Send Feedback** in the header's account popover. In the dialog, choose **General**, **Bug**, or **Feature**, write your message, and select **Send Feedback**. You do not need to be signed in. When you send a bug report, GitLens also opens a GitHub issue prefilled with your message so you can add details.


***

## Launchpad `PRO`

Launchpad groups your pull requests (PRs) by status, so you can see which ones need your action first and act on them without leaving VS Code.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" alt="The Launchpad quick pick with pull requests grouped by status" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View and act on PRs based on current status</figcaption>
</figure>

<div class='callout callout--basic'>
  <p>Launchpad supports GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Azure DevOps, Azure DevOps Server, Bitbucket, and Bitbucket Data Center repositories. To use it, connect your Git provider, for example with the <a href="https://help.gitkraken.com/gitlens/gitlens-features/#connecting-the-github-and-gitlab-integration">GitHub or GitLab Integration</a>.</p>
</div>

---

### Accessing Launchpad

- From the **Command Palette**: `Command/Ctrl + Shift + P` → `GitLens: Open Launchpad`
- From the **Pull Request status bar item** in VS Code

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" alt="Opening Launchpad from status bar" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Launchpad from the status bar or Command Palette</figcaption>
</figure>

---

### Using Launchpad

Launchpad groups PRs by these statuses:

- Ready to merge
- Blocked
- Requires follow-up
- Needs your review
- Waiting for review
- In merge queue
- Draft
- Snoozed

Click a PR to:

- View full details
- Open in your browser
- Merge (if eligible), or add it to the merge queue with **Add to Merge Queue...** when its base branch requires one
- Take it out of the merge queue with **Remove from Merge Queue...**
- Rebase the stack (for a GitHub stacked pull request)
- Switch to the branch or open in a worktree

To find a pull request that is not in your groups, select **Search for Pull Request...** and enter a term. Launchpad searches the pull requests of all your connected providers, including Azure DevOps and Bitbucket Data Center, for that term. You can also paste a pull request's URL to open that pull request. Pasting a URL works for every connected provider, including Azure DevOps, Azure DevOps Server, Bitbucket, and Bitbucket Data Center.

For repositories on GitHub.com that merge through a merge queue, queued pull requests appear in the **In Merge Queue** group with their queue status, and pull requests failing in the queue appear under **Blocked** as **Failing in Merge Queue**. Merge queues are not supported for GitHub Enterprise. For details, see [GitHub Merge Queue](/gitlens/gl-integrations/#github-merge-queue).

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" alt="PR detail view in Launchpad" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Interact with pull requests directly in VS Code</figcaption>
</figure>

You can also start or review [Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) directly from the PR action menu.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" alt="Launchpad with Code Suggest options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Suggest code edits from within the Launchpad</figcaption>
</figure>

*Launchpad is also available through the [GitKraken MCP](https://help.gitkraken.com/mcp/mcp-tools-reference/).*

---

### Start Review `PRO`

The **Start PR Review** command (`gitlens.startReview`) guides you through starting a pull request review:

1. Select a PR from your connected integration.
2. Choose whether to check out the branch or create a worktree.
3. Optionally, open an AI chat pre-filled with a review prompt.

Access it from the Command Palette: `GitLens: Start PR Review`

When AI features are enabled, Start Review asks whether to open the review in an agent, continue manually, or, when Kepler supports the pull request's provider, open it in [Kepler](/gitlens/gl-agents/#start-tasks-and-reviews-in-kepler). Select **Always use this choice** to skip that step next time; the `gitlens.ai.openInAgent` setting stores your choice. If no local clone of the pull request's repository is found, Start Review offers **Clone Repository...** and **Choose a Local Folder...** instead of stopping.

---

### Start Work `PRO`

The **Start Work** command (`gitlens.startWork`) starts work on an issue from your connected integrations: pick the issue, and GitLens creates a branch for it. If you are not signed in, Start Work first asks you to sign in or start a Pro trial before it offers to connect an integration.

Access it from the Command Palette: `GitLens: Start Work`

GitLens suggests a branch name built from the issue, which you can edit before the branch is created. By default the name is the issue ID followed by its title, such as `ABC-123-update-login-flow`. To change the pattern, set **Branch name format** in the **Start Work** category of [GitLens Settings](/gitlens/gitlens-settings/#integrations) (`gitlens.startWork.branchNameFormat`), using `${id}` for the issue ID and `${title}` for the title, for example `feature/${id}/${title}`.

---

### Pin or Snooze PRs

Use the pin icon <i class="fa-solid fa-thumbtack"></i> to keep important PRs in the **Pinned** group.

Use the snooze icon <i class="fa-solid fa-snooze"></i> to move less urgent PRs into the **Snoozed** group.

Click the icon again to unpin or unsnooze as needed.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" alt="Pin or snooze pull requests" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Pin or snooze PRs to manage your workflow</figcaption>
</figure>

<div class='callout callout--basic'>
  <p>Note: Launchpad lists the items that need your action at the top of the list.</p>
</div>

<div class='callout callout--warning'>
  <p>This feature is only available on GitLens Pro subscription tiers or higher.</p>
</div>


***

## Visual History

Visual History (formerly Visual File History) shows a timeline of changes to a file, folder, repository, or branch: when the code changed, what changed, and who changed it.

Visual History supports multiple scopes:

- **File** — View the history of a single file
- **Folder** — View the history of a directory
- **Repository** — View the history of the entire repository
- **Branch** — Slice the history by branch to focus on specific lines of work

To open Visual History, use one of the following:

- The **GitLens Inspect** side bar
- The **Command Palette**: `Cmd/Ctrl + Shift + P` → `GitLens: Show Visual History View`

<figure>
  <img src="/wp-content/uploads/gl-visual-file-history-01-v3@2x.png" alt="Visual History view for CHANGELOG.md showing eight commits by four authors plotted as color-coded bubbles over the last four weeks, with the additions and deletions of each commit shown as bars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Track authorship, size, and timing of file changes</figcaption>
</figure>

---

### How to Read the Graph

- **Y-axis (left):** Contributors, shown in individual swim lanes
- **X-axis:** Timeline of commits
- **Bubbles:** Color-coded per author; bubble size reflects the magnitude of changes
- **Bars (right y-axis):** Line additions (green) and deletions (red)

Hover over a bubble or bar to see the commit's details.

<figure>
  <img src="/wp-content/uploads/visual-file-history-hover.png" alt="Hover over commit for details" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View commit size, author, and message on hover</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>The Community plan supports Visual History only on public and local repositories.</p>
</div>


***

## GitKraken AI

GitKraken AI writes commit messages and stash descriptions, explains code changes, and helps you compose commits and rebase.

---

### AI-Generated Commit Messages

Generate a commit message from your staged changes.

<figure>
  <img src="/wp-content/uploads/gl-ai-generated-commit-message-01-v2.gif" alt="The Source Control view with a staged file: the empty commit message box, then an AI-generated commit message appearing in it" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit messages from staged changes</figcaption>
</figure>

To generate a commit message:

1. Stage your changes.
2. In the Source Control view, open the GitLens sparkle menu in the Changes header and choose **Generate Commit Message**. Or run `GitLens: Generate Commit Message` from the Command Palette.

GitKraken AI reads the diff of your staged changes and writes a message. To improve the result, add context in the commit box first.

You can customize behavior using [`gitlens.ai` settings](/gitlens/gitlens-settings/#misc-settings) for provider, model, and prompt preferences.

<div class='callout callout--warning'>
  <p>Pro users and above can optionally use a custom API key to connect to a different AI provider. GitKraken AI currently uses the Google Gemini model.</p>
</div>

---

### AI Stash Messages `PRO`

Available in **Pro**, **Advanced**, and **Business** plans.

Generate stash descriptions so you can identify your stashes later.

**How to access:**
- From the Command Palette: `GitLens: Generate Stash Message with AI`
- During stash creation: Use the AI option in the stash interface
- In the Stash view: Generate AI-powered descriptions for existing stashes

---

### AI Explanations `PREVIEW`

GitKraken AI explains changes across your repo in plain-language summaries.

<figure>
  <img src="/wp-content/uploads/ai-branch-summary.png" alt="AI branch summary explanation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI summaries in rendered markdown for improved clarity</figcaption>
</figure>

The **Explain** commands write markdown summaries for:

- Commits — **Explain Commit Changes...**
- Branches — **Explain Branch Changes...**
- Working changes — **Explain Working Changes...**
- Stashes — **Explain Stash Changes...**

**Where to find it:**
- Commit Graph
- Command Palette
- GitLens views: Commits, Branches, Stashes, Search & Compare
- Editor blame hovers (sparkle Explain button)

Use GitKraken AI explanations to understand:

- The purpose and impact of individual commits
- What changed across all commits in a branch
- What you have modified in your working directory
- What your previous stashes contain

#### AI Commit Explanations `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

AI-generated summaries explain the purpose and context of a commit, so you can understand its intent without reviewing every change yourself.

**How to access:**
- **Commit Details** view: See the AI explanation panel
- **Cloud Patch Details** view: View AI insights alongside commit data
- **Commit Review**: Generate explanations for any selected commit

---

### AI Changelog Creation `ADVANCED`

*Available in:* **Advanced** and **Business** plans only

Generate a structured changelog from a set of selected commits, for example for your release notes.

**How to access:**
- **Search/Compare** view: Click the inline button on the commits line
- **Commit Graph**: Select multiple commits, right-click, then choose **Generate Changelog**
- **Command Palette**: `GitLens: Generate Changelog...`

<div class='callout callout--basic'>
  <p>More questions about GitKraken AI? See the <a href="https://help.gitkraken.com/general/gitkraken-ai-faq/">GitKraken AI FAQ</a> for additional details.</p>
</div>

### AI Generate Commits `PRO`

The **Generate Commits** command turns your staged and unstaged changes into commits. GitKraken AI groups related changes and writes a message for each commit. The first time you run the command, a confirmation dialog explains what it does. After the commits are created, select **Undo** to revert them.

### AI Rebase `PRO`

The **AI Rebase** command restructures the commits on an existing branch onto a target commit, with GitKraken AI grouping the changes and writing the messages. Like Generate Commits, it shows a confirmation dialog the first time and offers **Undo** afterward. Both commands produce a markdown document that summarizes the changes they made.

### Auto-Rebase `PRO`

Auto-Rebase (`gitlens.ai.autoRebase`) continues a rebase through the conflicts GitKraken AI can resolve confidently, and leaves the rest for you. When a rebase hits a conflict, AI analyzes it and resolves it only when its confidence meets the threshold you set; anything below that threshold pauses the rebase so you can resolve the conflict yourself and continue. Every run is reviewable and reversible.

Key capabilities:

- **Confidence threshold** — Configure `gitlens.ai.autoRebase.confidenceThreshold` (0 to 1) to control how confident the AI must be before resolving a conflict on its own. Raise it to keep more decisions in your hands.
- **Stops rather than guesses** — Conflicts that fall below the threshold are left for you to resolve manually, with the rebase paused at that point.
- **Custom instructions** — Use `gitlens.ai.resolveConflicts.customInstructions` to give project-specific guidance for resolving conflicts.
- **Rebase summary sheet** — After the rebase completes, a summary sheet shows what was resolved and how, so you can review each decision.
- **Full undo support** — Undo the entire Auto-Rebase with **Undo Auto-Rebase** (`gitlens.ai.autoRebase.undo`) to return to the pre-rebase state if the results are not what you wanted.
- **Your messages and edit stops** — When a `reword` or `squash` step needs a new commit message, Auto-Rebase opens the message in VS Code for you to edit. At a commit you marked `edit`, it resolves and stages any conflicts, then pauses so you can make your changes before you continue.

To start Auto-Rebase, run `GitLens: Auto-Rebase...` from the Command Palette, choose the **Auto-Rebase** option in the Git Command Palette's rebase confirmation, or select **Start Auto-Rebase** in the [Interactive Rebase Editor](#interactive-rebase-editor). If a rebase is already paused, run `GitLens: Continue with Auto-Rebase`.

For a GitHub [stacked pull request](/gitlens/gl-commit-graph/#pull-request-information), **Auto-Rebase Stack** rebases every branch in the stack from the bottom up, each onto the one below it, and resolves conflicts with AI along the way. **Rebase Stack** does the same but stops at each conflict for you to resolve. Start either one from the Commit Graph pull request sheet, from Launchpad, from the Git Command Palette's rebase confirmation when the current branch belongs to a stack, or with `GitLens: Git Rebase Stacked Pull Requests...` or `GitLens: Auto-Rebase Stacked Pull Requests...`. When the rebase finishes, GitLens offers **Force Push Stack** so you can publish the rebased branches.

When Auto-Rebase pauses, its notification offers **Review & Resolve** and **Abort Rebase**, plus **Resume with AI** when AI features are allowed.

### Commit Composer View `PRO`

Use the Commit Composer to draft and review commits before you create them. Let GitKraken AI compose them, or compose them yourself. The Commit Composer opens in the Commit Graph details panel as Compose mode, and as a standalone view.

Join the [Commit Composer discussion](https://github.com/gitkraken/vscode-gitlens/discussions/4530) and provide feedback.

<figure>
  <img src="/wp-content/uploads/gl-commit-composer-17-4-01-v6@2x.png" alt="Commit Graph in Compose mode: the ringed Compose (wand) action on the Working Changes row, and the composer panel beside the graph listing Staged changes and Unstaged changes entries, the changed files, and the Instructions box with the Compose button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">The Commit Composer drafting view</figcaption>
</figure>

#### Interactive Draft Commits

When you compose commits, GitLens creates draft commits that you can review, change, and refine before you apply them to your repository. With draft commits, you can:

- **Preview before committing**: See exactly what will be committed before anything changes in your repository
- **Switch models**: Try composing with different AI models
- **Guide the AI**: Give custom instructions that match your team's conventions
- **Iterate and refine**: Regenerate individual messages or the whole set of commits
- **Review and edit**: Edit any commit message or how the changes are grouped

<figure>
  <img src="/wp-content/uploads/commit-composer-composed-17-4.png" alt="Commit Composer with AI-composed commit message populated and ready for review" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-composed commit message ready for review</figcaption>
</figure>

You can open the Commit Composer view from these places in GitLens:

- **GitLens commit details view**
- **Context menu on the Working Changes row** in the GitLens Commit Graph  
- **Commit Graph details panel**: Switch to **Compose** mode
- **✨ icon in the SCM view header**
- **Command Palette**: Search for **Compose Commits**

<figure>
  <img src="/wp-content/uploads/gl-access-composer-1-17-4-01-v3@2x.png" alt="Commit Graph toolbar showing the Compose button entry point" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access Commit Composer from the graph toolbar</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-access-composer-2-17-4-01-v4@2x.png" alt="The Commit Graph's Working Changes details panel with the Compose and Review mode chips ringed in its header, above the branch row, the four changed files and the commit-message box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Or switch to Compose mode in the Working Changes details panel</figcaption>
</figure>

### Commit Composer: Branch Recomposition

Use Commit Composer to clean up and reorganize the commits on an existing branch, for example before you open a pull request or push.

<figure>
  <img src="/wp-content/uploads/gl-17-7-recompose-branch-01-v4@2x.png" alt="The Commit Composer opened for the feature/spending-insights branch: its four commits sit in the scope list with drag handles, main's commits are dimmed beneath them above the base, the three changed files are listed, and the Instructions box with the Compose button waits at the bottom" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Recompose an entire branch from the Commit Graph</figcaption>
</figure>

#### Recompose Entire Branches

Open Commit Composer from any branch in the Commit Graph (or anywhere branches appear in GitLens) to inspect and reorganize its commits. The composer creates draft commits you can review before applying changes to your repository.

**Auto-Recompose with AI**: GitKraken AI analyzes your branch and restructures its commits into logical units with clear messages. Choose your model and give custom instructions that match your team's conventions. To reuse the same instructions every time, set them in the **Generate Commits: Custom Instructions** setting (`gitlens.ai.generateCommits.customInstructions`).

**Manual Control**: Review the AI's suggestions, regenerate specific commit messages, or edit messages and how the changes are grouped yourself.

<video src="/wp-content/uploads/gl-17-7-recompose-example.mp4" autoplay loop controls muted class="help-center-video"></video>

#### Enhanced Composer Capabilities

Commit Composer also handles these cases:

- **Untracked files**: Working changes include untracked files, so you can compose all your changes together
- **New repositories**: Compose your first commits before a base commit exists

### Commit Composer: Selective Recomposition

Use Commit Composer to recompose only specific commits within a branch.

<figure>
  <img src="/wp-content/uploads/gl-17-8-recompose-selected-commits-01-v5@2x.png" alt="The Commit Composer scoped to two selected commits of the feature/spending-insights branch — &quot;fix(insights): exclude refunds from spending totals&quot; and &quot;feat(insights): add budget threshold alerts&quot; — shown in the scope list with drag handles while the branch's other commits are dimmed, above the changed files and the Compose instructions box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Select specific commits to recompose</figcaption>
</figure>

Select the commits that need work, such as quick "wip" or "fix" commits, and let GitKraken AI restructure only those changes with clearer messages.

1. Select multiple contiguous commits on the same branch with <kbd>Shift</kbd>-click or <kbd>Cmd</kbd>-click.
2. Right-click and choose **Recompose Selected Commits...**.

Commit Composer opens with only your selected commits as drafts, ready for you or GitKraken AI to refine.

To open the composer for all your working changes, select the **Compose** (wand) button on the Working Changes row in the Commit Graph. While you rebase, you can also switch from the Rebase Editor to Commit Composer with **Recompose Commits...**, which cancels the rebase and lets AI compose the commits instead.

<figure>
  <img src="/wp-content/uploads/gl-17-8-compose-in-wip-01-v5@2x.png" alt="The Commit Graph's Working Changes row with its action buttons, Compose ringed between Run Default Task and Review." class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Commit Composer from the Working Changes row</figcaption>
</figure>

The Working Changes row also has a **Run Default Task** (play) button that runs a VS Code task in that row's worktree:

- The first time you select it, GitLens asks you to choose the default task. Later clicks run that task.
- <kbd>Alt</kbd>-click the button to choose a different task.
- While the task runs, the button reads **Running:** and the task name. Clicking it then shows the running task instead of starting another.

To pick a task from a list, right-click a Working Changes row in the Commit Graph, or a worktree in the side bar views, and select **Run Task on Worktree...**. In that list, select a task's checkmark button (**Set as Default Task**) to make it the default.

### Compose and Recompose Commands

You can also open Commit Composer with these commands:

- **Compose Commits...** (`gitlens.composeCommits`) — Opens the Commit Composer for working changes in the current repository, or from a Compose mode entry in the Commit Graph details panel.
- **Recompose Commits...** (`gitlens.ai.recomposeBranch`) — Opens the Commit Composer scoped to an entire branch. GitKraken AI can propose a clearer, more intentional sequence of commits and messages for you to review and refine before applying the result.
- **Recompose Commits from Here...** (`gitlens.ai.recomposeFromCommit`) — Scopes the same workflow to a specific commit onward.
- **Recompose Selected Commits...** (`gitlens.ai.recomposeSelectedCommits`) — Scopes the same workflow to only the selected commits on a branch.

These commands are available from the Commit Graph context menu, branch context menus throughout GitLens, and the Command Palette. Coach marks guide first-time users through the workflow.

***

## Git Command Palette

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-01-v4@2x.png" alt="GitLens Git Command Palette showing guided step-by-step command options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Guided Git commands through the Command Palette</figcaption>
</figure>

The [customizable](/gitlens/gitlens-settings/#git-command-palette-settings) Git Command Palette (`gitlens.gitCommands`) guides you step by step through common Git commands. Use it to run Git actions, explore commit history, manage stashes, and more, with a confirmation before each command runs.

On a command's confirmation step, choose the action row, then turn options on or off with the checkbox toggles under the **Options** separator. For example:

- **Prune** for Fetch
- **Force** for Push Tags and branch deletion
- **Keep Staged** for stashes
- **Fast-forward** and **Don't Commit** for Merge
- **Update Branches** and **Autosquash** for Rebase
- **In a New Worktree** for Switch

Where a matching Git config value exists, such as `fetch.prune`, `merge.ff`, `rebase.updateRefs`, or `rebase.autosquash`, the toggle starts from that value.

Some commands also offer a **Don't Ask Again** toggle, which adds the command to [`gitlens.gitCommands.skipConfirmations`](/gitlens/gitlens-settings/#git-command-palette-settings) so the confirmation is skipped from then on. **Don't Ask Again** is not offered on steps that ask you to choose between different actions, such as Push's **Publish** step, or on warning steps whose safe choice is selected for you.

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-confirm-options-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Confirm Fetch step with the Fetch and Fetch All Remotes rows above an Options separator and the ringed Prune checkbox toggle, which removes remote-tracking branches that no longer exist on the remote." />
</figure>

To push tags to a remote, run the **Tag** command and choose **Push Tags**. Pick one or more tags, choose a remote (skipped when the repository has only one), and confirm; turn on **Force** to overwrite a tag that already exists on the remote. You can also push tags from the side bar views (**Push Tag...** or **Push Tags...** on tag nodes) and from the Commit Graph (**Push Tag...** on a tag's context menu).

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-push-tags-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Push Tags step, titled Push Tags, asking to choose tags to push with the repository's v1.0.0, v1.1.0 and v2.0.0 tags listed as selectable rows." />
</figure>

When you run **Push** on a branch that has not been published yet, the command shows a publish step (**Confirm Publish**) so you can choose the remote to publish the branch to. If the repository has no remotes, the **Publish** step reads *Cannot publish; No remotes found* and offers two ways forward:

- **Publish Repository…** creates a new remote repository and publishes the current branch to it. It's selected by default when you push the current branch. If you push another branch, it still publishes the current branch, and **Add Remote…** is selected instead.
- **Add Remote…** walks you through adding a remote, then continues to **Confirm Publish** so you can publish the branch to it.

**Publish Repository** in the Commit Graph and the side bar views opens this same step with your choice already selected.

<figure>
  <img src="/wp-content/uploads/gl-push-wizard-no-remotes-01-v3@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Publish step for a repository with no remotes, placeholder &quot;Cannot publish; No remotes found&quot;, with Publish Repository… selected (&quot;Will create a new remote repository and publish branch main to it&quot;) and Add Remote… (&quot;Will add a remote, then publish branch main to it&quot;) and Cancel. Don't Ask Again is not offered on this step." />
</figure>

When you push several repositories at once, any without remotes are skipped, and the confirmation step lists them. If none of them has a remote, the step reads *Cannot push; No remotes found*.

When you add a remote with **Add Remote**, from the **Remote** command or the side bar's **Remotes** view, the name is pre-filled with `origin` if the repository has no remotes yet. Before adding the remote, GitLens checks that the URL can be reached. If it cannot, the confirmation step reads *Cannot reach remote* with the reason, such as *The host could not be found*, and offers:

- **Change URL** (selected) to go back and correct the URL.
- **Add Remote Anyway** to add it despite the failed reachability check. A later fetch or push reports if the URL is wrong.
- **Retry**, the button at the end of the input box, to check again.

<figure>
  <img src="/wp-content/uploads/gl-add-remote-unreachable-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Confirm Add Remote step for a URL that can't be reached: placeholder &quot;Cannot reach remote; The host could not be found&quot;, the message &quot;Check the URL, or add the remote anyway&quot;, the row &quot;Unable to reach https://nonexistent.invalid/acme/release-notes.git&quot;, Add Remote Anyway (&quot;Will add origin without checking it; a later fetch or push will report if it is wrong&quot;) and Change URL selected, with a Retry button at the end of the input box." />
  <figcaption style="text-align: center; color: #888">Adding a remote whose URL cannot be reached</figcaption>
</figure>

If the remote is added but the first fetch from it fails, a warning offers **Remove Remote**. Likewise, if a push cannot reach a remote you have never fetched from, for example one you just added with a mistyped URL, the error offers **Remove Remote**. That button does not appear for a remote you have fetched from before.

---

### Quick Commit Access

- **Show Branch History** (`gitlens.showQuickBranchHistory`): Explore the commit history of any selected branch.
  
  <img src="/wp-content/uploads/menu-branch-history.png" alt="The Commits quick pick for branch main, listing commits with their author, date and SHA under Choose a commit" class="help-center-img img-bordered">

- **Show Current Branch History** (`gitlens.showQuickRepoHistory`): View the commit history of your current branch.
- **Show File History** (`gitlens.showQuickFileHistory`): Access the full commit history of the current file. The File History view supports a **contributors mode** (`gitlens.views.fileHistory.mode`) that shows all contributors to the file instead of the commit list.

  <img src="/wp-content/uploads/gl-menu-file-history-01-v3@2x.png" alt="File History QuickPick for README.md listing its six commits with message, author, date, SHA and line-change counts; the newest commit is highlighted" class="help-center-img img-bordered">

- **Search Commits** (`gitlens.showCommitSearch`): Use a quick pick menu to search by:

  - Message: `<message>`
  - Excluded message: `-message:<message>` (removes commits whose message contains the term)
  - Author: `author:<author>` or `@:<author>`
  - Committer: `committer:<committer>`
  - Commit SHA: `commit:<sha>` or `#:<sha>`
  - File path or glob: `file:<glob>` or `?:<glob>`
  - Patch changes: `change:<pattern>` or `~:<pattern>`
  - Merge commits only: `type:merge` or `is:merge`

  <img src="/wp-content/uploads/gl-menu-commit-search-01-v2@2x.png" alt="Commit Search quick pick listing the search modes, including Search by Message, Exclude by Message, Author, Committer, Commit SHA, File and Changes" class="help-center-img img-bordered">

  Refer to the [Git log documentation](https://git-scm.com/docs/git-log) for advanced usage.

- **Quick Show Commit** (`gitlens.showQuickCommitDetails`): Review commit information and actions.

  <img src="/wp-content/uploads/gl-menu-commit-details-01-v2@2x.png" alt="Commit Details QuickPick showing the commit message, author, SHA, and changed-file count, with actions including Revert, Reset, Create Branch, and Create Tag" class="help-center-img img-bordered">

- **Quick Show Line Commit** (`gitlens.showQuickCommitFileDetails`): Explore the file's commit and take action on it.

  <img src="/wp-content/uploads/menu-commit-file-details.png" alt="The quick pick for code.ts in a commit, with actions such as Reveal Commit in Side Bar, Apply Changes, Open Changes and Open File on GitHub" class="help-center-img img-bordered">


### Quick Stash Access

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-list-01-v3@2x.png" alt="Stash list QuickPick showing all stash entries in the repository with stash messages and selection options" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-details-01-v3@2x.png" alt="Stash details QuickPick for stash #0 showing its files-changed summary and the Apply Stash, Rename Stash, Drop Stash, Copy Message, Open, Compare and Browse Repository actions" class="help-center-img img-bordered">
</figure>

- **Show Stashes** (`gitlens.showQuickStashList`): Explore your stashes in a quick pick menu.

---

### Quick Status Access

- **Show Repository Status** (`gitlens.showQuickRepoStatus`): See the current repository status in a quick pick menu.

<figure>
  <img src="/wp-content/uploads/menu-repo-status.png" alt="The Status quick pick for branch main, showing that main is ahead of origin/main by 2 commits with 1 unstaged file, and actions to open or close changed files" class="help-center-img img-bordered">
</figure>

---

## Interactive Rebase Editor

<figure>
  <img src="/wp-content/uploads/gl-rebase-01-v4@2x.gif" alt="GitLens interactive rebase editor: five commits each with an action dropdown, the second entry's dropdown open on pick / reword / edit / squash / fixup / drop, and then squash applied to it; the footer lists the keyboard shortcuts including alt + up/down to move a commit" class="help-center-img img-bordered">
</figure>

Use the GitLens interactive rebase editor to set up an interactive rebase:

- Reorder, edit, squash, and drop commits.
- Drag and drop commits to reorder them.
- Use the toolbar commands **Abort**, **Continue**, **Reopen as Interactive Editor**, and **Reopen as Text Editor**.

### Start or Continue with Auto-Rebase `PRO`

When AI features are allowed, the editor footer shows a **Start Auto-Rebase** split button next to **Start Rebase**. Start Auto-Rebase runs the rebase with [Auto-Rebase](#auto-rebase-pro), which resolves the conflicts it is confident about and pauses at commits you marked `edit` or when its confidence is low. After a rebase has started, the footer shows **Continue with Auto-Rebase** beside **Continue** and **Skip**. The chevron menu of each split button holds **Recompose Commits...**, which aborts the rebase and opens the Commit Composer.

<figure>
  <img src="/wp-content/uploads/gl-rebase-auto-rebase-start-01-v3@2x.png" class="help-center-img img-bordered" alt="The Interactive Rebase Editor before a rebase starts, with the footer's Start Rebase button beside the ringed Start Auto-Rebase split button, whose chevron menu holds Recompose Commits, and Abort." />
</figure>

### Conflict Detection

The rebase editor includes a **conflict files panel** that lists files with potential conflicts, with per-file conflict counts and status indicators. Before you start the rebase, **predictive conflict detection** warns you about conflicts against the current base, so you can prepare for them.

### Rebase Editor Settings

These settings control the rebase editor:

- `gitlens.rebaseEditor.openOnPausedRebase` — Automatically open the rebase editor when a rebase is paused (e.g., due to conflicts).
- `gitlens.rebaseEditor.openBehavior` — Controls how the rebase editor opens: `auto` (default) or `beside` (opens alongside the current editor).
- `gitlens.rebaseEditor.revealLocation` — Where to reveal commit details: `graph` or `inspect`.
- `gitlens.rebaseEditor.revealBehavior` — When to reveal details: `never`, `onOpen`, or `onSelection`.
- `gitlens.rebaseEditor.density` — Controls row padding in the editor: `compact` (default) or `comfortable` for more spacing.

### Conflict Resolution Actions

When a rebase is paused because of conflicts, the rebase editor offers inline actions to **stage current changes** or **stage incoming changes**.

### Use the Rebase Editor from the Terminal

To open the rebase editor when you run an interactive rebase from your terminal (for example, `git rebase -i`):

- Set VS Code as your default Git editor:
  ```bash
  git config --global core.editor "code --wait"
  ```

- Or, to only affect rebase sessions:
  ```bash
  git config --global sequence.editor "code --wait"
  ```

> To use the Insiders edition of VS Code, replace `code` with `code-insiders` in the commands above.


***

## Commit Signature Verification `PRO`

GitLens verifies GPG, SSH, and X.509 commit signatures and shows a verification badge in the Commit Details view, the Graph Details panel, and inline blame hovers.

### Verification Badges

Each signed commit shows a badge indicating its verification status:

- **Verified** — The signature is valid and the signer is trusted
- **Unverified** — The signature could not be verified (missing key, untrusted signer, etc.)
- **Unsigned** — The commit has no signature

To show the signature status in a custom commit tooltip, use the `${signature}` token in the tooltip format string.

### Allowed Signers Management

Use the **SSH Allowed Signers** editor to manage your trusted SSH signers. The editor lists the signers of SSH-signed commits from your recent history, with their avatars, and you select which keys to trust. GitLens saves the trusted entries to your SSH `allowed_signers` file.

Open it from the Command Palette with `GitLens: Edit SSH Allowed Signers...` (`gitlens.git.editAllowedSigners`).


***

## Autolinks

Use autolinks to turn external references in commit messages, such as Jira issues or Zendesk tickets, into clickable links.

<figure>
  <img src="/wp-content/uploads/gl-autolinks-01-v4@2x.png" alt="Commit details in the GitLens Inspect view for a commit whose message ends in &quot;Closes #7&quot;: the #7 reference is a link, and the Autolinks section below the message shows the #7 chip with its hover popover naming the open pull request &quot;fix: add types and config to rate limiter&quot;" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of autolinks in commit messages</figcaption>
</figure>

## Terminal Links

<figure>
  <img src="/wp-content/uploads/gl-terminal-links-01-v3@2x.png" alt="The integrated terminal showing git log --oneline output, with the pointer on the first commit's SHA: GitLens underlines it as a link and shows the &quot;Show Commit (ctrl + click)&quot; hover" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Autolinks in the integrated terminal</figcaption>
</figure>

Terminal links make Git references in the integrated terminal clickable. You can turn them on or off for:

- [Branches, tags, and commit ranges](/gitlens/gitlens-settings/#terminal-links-settings): Explore their commit history.
- [Individual commits](/gitlens/gitlens-settings/#terminal-links-settings): Review commit details and take further action.

***

## Remote Provider Integrations

GitLens integrates with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/gitlens-settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/gitlens-settings/#remote-provider-integration-settings).

Basic integrations offer issue and pull request autolinking. Richer integrations, like GitHub or GitLab, include:

- Launchpad support
- Rich hover information for autolinks
- Pull request association with branches and commits
- Avatars for authors and commenters

These integrations also add commands to open or copy URLs for files, commits, branches, and repositories:

- **Open File from Remote** (`gitlens.openFileFromRemote`) — Open a local file from a URL on a remote provider
- **Open File at Revision from Remote** (`gitlens.openRevisionFromRemote`) — Open the specific file revision referenced by a remote URL, rather than the working copy
- **Open File on Remote** (`gitlens.openFileOnRemote`) — Open a file or revision on the remote provider
- **Copy Remote File URL** (`gitlens.copyRemoteFileUrlToClipboard`) — Copy the URL of a file or revision
- **Open File on Remote From...** (`gitlens.openFileOnRemoteFrom`) — Open a file or revision from a specific branch or tag
- **Copy Remote File URL From...** (`gitlens.copyRemoteFileUrlFrom`) — Copy the URL from a specific branch or tag
- **Open Commit on Remote** (`gitlens.openCommitOnRemote`) — Open a commit
- **Copy Remote Commit URL** (`gitlens.copyRemoteCommitUrl`) — Copy the commit URL
- **Open Branch on Remote** (`gitlens.openBranchOnRemote`) — Open a branch
- **Copy Remote Branch URL** (`gitlens.copyRemoteBranchUrl`) — Copy the branch URL
- **Open Branches on Remote** (`gitlens.openBranchesOnRemote`) — Open the branches view
- **Copy Remote Branches URL** (`gitlens.copyRemoteBranchesUrl`) — Copy the branches view URL
- **Open Comparison on Remote** (`gitlens.openComparisonOnRemote`) — Open a comparison view
- **Copy Remote Comparison URL** (`gitlens.copyRemoteComparisonUrl`) — Copy the comparison view URL
- **Open Pull Request on Remote** (`gitlens.openPullRequestOnRemote`) — Open a pull request
- **Copy Pull Request URL** (`gitlens.copyRemotePullRequestUrl`) — Copy the pull request URL
- **Open Repository on Remote** (`gitlens.openRepoOnRemote`) — Open the repository
- **Copy Remote Repository URL** (`gitlens.copyRemoteRepositoryUrl`) — Copy the repository URL

### Connecting the GitHub and GitLab Integration

The GitHub and GitLab integrations connect through your GitKraken account at [gitkraken.dev](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

To connect an integration:

1. Open the Command Palette (`Cmd`/`Ctrl`+`Shift`+`P`).
2. Run `GitLens: Manage Integrations...`.

Or select the account button (your avatar and plan) in the Commit Graph header, then select the **Integrations** row (or **Set up integrations** if none are connected) to open the integrations settings in GitLens Settings.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" srcset="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" alt="The Commit Graph header's account button with its menu open and the Integrations row ringed, a row of provider icons that opens GitLens Settings > Integrations." class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Open your integrations from the Commit Graph account menu</figcaption>
</figure>

If you are not signed in yet, GitLens asks you to sign in to your GitKraken account. Then select **Connect with GitHub** or **Connect with GitLab**, and follow the sign-in steps. You can connect more than one integration.

To finish, select **Complete Setup** to return to VS Code and start using the integrations.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" alt="The GitKraken integrations page with Connect buttons for GitLab, Azure DevOps, Bitbucket, Jira Cloud and Trello and a Complete Setup button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Manage your connected integrations</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>On the Community plan, integrations offer basic functionality only.</p>
</div>


## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro offers a richer integration with GitHub Enterprise Server and GitLab Self-Managed.

After you connect, autolink hovers show more context: your GitHub Enterprise Server or GitLab Self-Managed avatar, links to related pull requests, and a summary of pull request or issue details. The side bar views for commits and branches show the same information.

<figure>
  <img src="/wp-content/uploads/gl-gitlab-github-integration-01-v4@2x.png" alt="The Commit Graph with the pull-request hover card open over the #7 badge of the fixture/code-suggest-demo branch pill: the pull request's title &quot;fix: add types and config to rate limiter&quot;, its number, who opened it and when it was last updated — metadata supplied by the connected GitHub integration" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Enhanced hover integration with GitHub Enterprise and GitLab Self-Managed</figcaption>
</figure>

### Connecting GitHub Enterprise Server or GitLab Self-Managed

To connect either integration:

1. Open `settings.json`:
   - Use the Command Palette (`Cmd`/`Ctrl` + `Shift` + `P`) > **Preferences: Open User Settings (JSON)**

2. Add a `gitlens.remotes` entry specifying the domain and type:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

3. Open a repository from GitHub Enterprise Server or GitLab Self-Managed in VS Code.
4. Go to the [Remotes View](/gitlens/side-bar/#remotes-view).
5. Select <i class="fa-solid fa-plug"></i> **Connect to Remote**.
   - If this option is missing, verify the format in your `settings.json` matches the example above.

<figure>
  <img src="/wp-content/uploads/gl-connect-to-remote-ghe-01-v3@2x.png" alt="GitLens Remotes sidebar view listing repository remotes with the Connect to Remote action icon for linking a self-hosted provider" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Connect to a GitHub Enterprise or GitLab Self-Managed instance</figcaption>
</figure>

6. Provide a Personal Access Token (PAT) with the required scopes when prompted, and press **Enter** to complete the connection.



***

## Jira Integration `PRO`

Connect the Jira Integration through your GitKraken Account to get Jira [autolinks](/gitlens/gitlens-features#autolinks) wherever GitLens shows autolinks. After you connect, GitLens turns Jira issue keys (for example, `ABC-123`) in commit messages into clickable links.

<figure>
  <img src="/wp-content/uploads/gl-jira-integration.png" alt="A GitLens commit hover in which the Jira issue key HC-132 is autolinked, with the linked issue Add Jira integration and when it was opened" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Jira autolinks in commit messages</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>This feature is only available for Pro subscription tiers or higher.</p>
</div>

To connect the integration:

1. Open the GitLens Settings editor (run _GitLens: Open Settings_ from the Command Palette).
2. Select **Cloud Integrations** under **Integrations** in the GitLens Settings navigation. Each provider has a card. A provider you have not connected shows **Connect**, and a connected one shows **Connected** and **Manage**.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations-01-v5@2x.png" alt="GitLens Settings open on Cloud Integrations, with GitHub, Azure DevOps, Bitbucket, Jira and Linear connected and Connect buttons for GitHub Enterprise, GitLab, GitLab Self-Hosted, Azure DevOps Server, Bitbucket Data Center, Jira Data Center, Trello and Asana" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Cloud Integrations in GitLens Settings, shown here with Jira already connected</figcaption>
</figure>

3. Select **Connect** on the **Jira** card, and authorize access to your Atlassian Account.

Or connect Jira from your [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) on gitkraken.dev in a browser.

You can also connect **Trello** and **Asana** (both Pro integrations) from the same **Cloud Integrations** list. Select **Connect** on the card and finish connecting on gitkraken.dev in your browser. After Trello or Asana is connected, branches associated with a Trello card or an Asana task show it on their Commit Graph pills. GitLens does not create autolinks for Trello cards or Asana tasks, and it does not list them in Start Work or Launchpad.

To connect a self-hosted Jira (Jira Data Center or Jira Server), select **Connect** on the **Jira Data Center** card in the same list. Like the other self-hosted integrations, Jira Data Center is a Pro integration connected through your GitKraken Account. Each Jira host is its own connection. Instances served under a context path, such as `https://jira.example.com/jira`, are supported.

A connected Jira Data Center instance:

- Shows the issues associated with a branch.
- Autolinks its projects' issue keys (for example, `ABC-123`) in commit messages and branch names to the issue on your instance.

Start Work and the Commit Graph's issue tracker picker do not list Jira Data Center issues yet.


***

## Powerful Commands

GitLens adds these commands to VS Code:

- **Add Co-authors...** (`gitlens.addAuthors`) — Add a co-author to the commit message input box.
- **Copy SHA** (`gitlens.copyShaToClipboard`) — Copy the commit SHA of the current line or the latest commit.
- **Copy Message** (`gitlens.copyMessageToClipboard`) — Copy the commit message from the current line or latest commit.
- **Copy Current Branch Name** (`gitlens.copyCurrentBranch`) — Copy the current branch name to the clipboard.
- **Switch Branch...** (`gitlens.switchToAnotherBranch:views`) — Switch to another branch.
- **Compare References...** (`gitlens.compareWith`) — Compare two references.
- **Compare HEAD with...** (`gitlens.compareHeadWith`) — Compare HEAD with a selected reference.
- **Compare Working Tree with...** (`gitlens.compareWorkingWith`) — Compare the working tree with a selected reference.
- **Open Changes (difftool)** (`gitlens.externalDiff`) — Open file changes with the configured Git difftool.
- **Open All Changes (difftool)** (`gitlens.externalDiffAll`) — Open all working changes with the configured difftool.
- **Open Directory Compare (difftool)** (`gitlens.diffDirectoryWithHead`) — Compare working tree with HEAD using a difftool.
- **Open Directory Compare (difftool) with...** (`gitlens.diffDirectory`) — Compare with a selected reference.
- **Open File** (`gitlens.openWorkingFile`) — Open the working version of the current file.
- **Open File at Revision...** (`gitlens.openFileRevision`) — Open a selected file revision.
- **Open File at Revision from...** (`gitlens.openFileRevisionFrom`) — Open a revision from a specific reference.
- **Open Blame Prior to Change** (`gitlens.openBlamePriorToChange`) — Show blame for the prior revision of a line.
- **Open Changed Files** (`gitlens.openChangedFiles`) — Open all changed files in the working tree.
- **Close Unchanged Files** (`gitlens.closeUnchangedFiles`) — Close all files without changes.
- **Enable Debug (Trace) Logging** (`gitlens.enableDebugLogging`) — Enable debug logging in the GitLens output.
- **Disable Debug (Trace) Logging** (`gitlens.disableDebugLogging`) — Disable debug logging.
- **Copy Changes (Patch)** (`gitlens.copyPatchToClipboard`) — Copy patch data from views, changes, or stashes.
- **Apply Copied Changes (Patch)** (`gitlens.applyPatchFromClipboard`) — Apply a patch from clipboard contents.
- **Git Change Branch Merge Target...** (`gitlens.git.branch.setMergeTarget`) — Set or reset a branch's merge target in a few steps. Pick a local branch, then select a remote branch as its merge target, or reset an existing target.
- **Copy Working Changes to Worktree...** (`gitlens.copyWorkingChangesToWorktree`) — Copy working changes from one worktree to another.
- **Unlock Worktree** (`gitlens.views.unlockWorktree`) — Unlock a locked worktree from its context menu in the side bar views.


***

## Deep Links

Deep Links are URLs that open specific GitLens resources. Share them to point teammates directly to repositories, files, comparisons, and more. You can copy Deep Links to these resources:

- **Search & Compare** — Link to comparisons in the [Search & Compare view](/gitlens/side-bar/#search-compare-view). Right-click a comparison, hover over _Share_, and select _Copy Link to Comparison_.
- **GitKraken Workspaces** — Link to a [GitKraken Workspace](/gitlens/side-bar/#workspaces-☁%ef%b8%8f). Right-click a Workspace, hover over _Share_, and select _Copy Link to Workspace_.
- **Commit Graph** — Link to remote repositories, commits, branches, and tags in the [Commit Graph](/gitlens/gitlens-features/#commit-graph). Right-click the resource, hover over _Share_, and select _Copy Link to <resource>_.
- **Files or Lines** — Link to specific files or lines of code. Right-click highlighted lines or a file, hover over _Share_, and select _Copy vscode.dev Link_.
- **Cloud Patches** — Link to a [Cloud Patch](/gitlens/gitlens-features/#cloud-patches-preview-%e2%98%81%ef%b8%8f). After generating a Cloud Patch, click _Copy Link_ from the success prompt.

<figure>
  <img src="/wp-content/uploads/gl-deep-link-example.gif" alt="Animation that starts in the Commit Graph in VS Code and shows a GitLens deep link being generated and used" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of generating and using Deep Links</figcaption>
</figure>

***

## Git Submodule Support

GitLens has basic support for Git submodules. When you open a project that contains submodules, GitLens finds and tracks their repositories. In the side bar views, submodule repositories have their own icons and tooltips. Diffs show when a submodule reference has been updated.

***

## Commit File Details in Large Histories

In repositories where loading commit file details has been slow, the Commits view and other history views load a commit's or stash's file details only when they are shown. Large histories then open faster. GitLens does this automatically only in those repositories, and only while `gitlens.gitOptimizations.enabled` is on.

To choose the behavior yourself, set `gitlens.advanced.commits.delayLoadingFileDetails`: `true` always delays loading file details, `false` never delays, and `null` (the default) lets GitLens decide per repository.

***

## Display Language

GitLens follows the VS Code display language. Experimental Spanish, Simplified Chinese, and Traditional Chinese translations are available, and any text that is not translated yet appears in English. GitLens has no separate language setting.

To switch languages, install Microsoft's language pack for that language, run **Configure Display Language** from the Command Palette, choose the language, and restart VS Code. The `gitlens.defaultDateLocale` setting still controls only how dates are formatted.

***

## Welcome View

Use the **Welcome** side bar view to get started with GitLens. Its guided walkthrough covers getting started with GitLens, the Commit Graph, AI features, Git Blame, Launchpad and worktrees, Kepler for agent workflows, and the GitKraken MCP server. The getting-started content depends on your plan. Select **Get Started with the Commit Graph →** for a second walkthrough of the graph's agent monitoring, parallel work, Review, Compose, and Compare features.

Open it from the GitLens side bar. VS Code's **Get Started** walkthrough for GitLens and the Launchpad's learn-more links also open the Welcome view.

***

## AI Agent Integration `PRO`

GitLens shows the activity of your AI coding agents beside your own work, so you can follow and manage what they do.

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

Codex does not run newly installed hooks until you trust them. After you install hooks for Codex, run `/hooks` in Codex to trust them, and trust them again whenever the hooks are reinstalled. GitLens shows this reminder in the install notification, with a **Start Codex Session** button, and in the Agents table of GitLens Settings.

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

GitLens installs the GitKraken MCP server separately for each agent. The **Connect AI Agents (Install MCP and Hooks)** command walks you through installing the CLI, registering MCP for your current IDE, and connecting additional agents.

- **Connect AI Agents (Install MCP and Hooks)** (`gitlens.ai.connectAgents`) — Install and configure MCP for your agents, step by step
- **Connect GitKraken MCP to All Detected Agents** (`gitlens.ai.mcp.installForAllAgents`) — Install the GitKraken MCP server for all detected agents
- **Install GitKraken MCP for Agent** (`gitlens.ai.mcp.installForAgent`) — Install for a specific agent
- **Uninstall GitKraken MCP for Agent** (`gitlens.ai.mcp.uninstallForAgent`) — Remove MCP from a specific agent

In VS Code 1.101 and later, GitLens also installs and enables the GitKraken MCP server for VS Code automatically. To turn this off, disable the `gitlens.gitkraken.mcp.autoEnabled` setting. Turning it off, or turning off GitLens AI features (`gitlens.ai.enabled`), removes the GitKraken MCP server from VS Code's **Configure Tools** list right away, without reloading the window; turning it back on adds the server again.

To manage your agents' settings in one place, open the **Agents** category under **Integrations** in GitLens Settings.

***

## Menus & Toolbars

<figure>
  <img src="/wp-content/uploads/gl-menus-01-v2@2x.png" alt="GitLens Visual Settings Editor showing the Menus and Toolbars category, with toggle options controlling where GitLens commands appear in editor menus, context menus, and toolbars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">GitLens menu and toolbar options</figcaption>
</figure>

You can [customize](/gitlens/gitlens-settings/#menu-and-toolbar-settings) where GitLens commands appear in VS Code menus and toolbars. Manage these settings in the [interactive settings editor](/gitlens/gitlens-settings/).

For example, disabling **Add to the editor group toolbar** removes those items from the toolbar:

<figure>
  <img src="/wp-content/uploads/gl-menus-example-01-v2@2x.png" alt="VS Code editor tab bar with the GitLens editor group toolbar items removed, showing a toolbar without GitLens action buttons" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Editor group toolbar items removed</figcaption>
</figure>

Expand each section to choose individual menus and toolbars.

***

## Modes

GitLens supports [user-defined](#modes-settings- 'Jump to the Modes settings') modes, so you can switch between sets of settings.

- Shows the active mode in the **status bar** ([optional](#modes-settings- 'Jump to the Modes settings'), on by default)
- **Switch Mode** (`gitlens.switchMode`) — Switch between modes.
- **Zen Mode** — Turns off many visual elements so you can focus on your code.
  - **Toggle Zen Mode** (`gitlens.toggleZenMode`) — Toggle Zen mode.
- **Review Mode** — Turns on visual elements for code review.
  - **Toggle Review Mode** (`gitlens.toggleReviewMode`) — Toggle Review mode.

### Experimental Multi-diff Editor

VS Code 1.86 or later is required for these capabilities.

#### Commands using Multi-diff

- **Open Folder Changes with Revision...** and **Open Folder Changes with Branch or Tag...** via Command Palette, Explorer, and Source Control views.
- Inline **Open All Changes** in commits, stashes, and comparison views.
- **Open All Changes** and **Open All Changes with Working Tree** — Open the changes in the multi-diff editor.
- **Open All Changes, Individually** and **Open All Changes with Working Tree, Individually** — Open each file's changes in its own diff editor.
