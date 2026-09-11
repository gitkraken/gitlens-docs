---
title: GitLens Features
description: Learn how to use GitLens autolinks, terminal links, powerful Git commands, remote provider integrations, and UI customizations to enhance your Git workflow in VS Code.
taxonomy:
  category: gitlens
---
<kbd>Last updated: September 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

Features marked with <span style="color: #888;">`PREVIEW`</span> require a GitKraken Account, with access based on your [plan level](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) (Community, Pro, etc).

***

## Revision Navigation

<figure>
  <img src="/wp-content/uploads/revision-navigation.gif" alt="GitLens revision navigation animated demo" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Step through revisions using built-in navigation commands</figcaption>
</figure>

Revision Navigation allows you to quickly compare different versions of a file or specific lines.

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

Current Line Blame adds a subtle, [customizable](/gitlens/settings/#current-line-blame-settings), and [themable](/gitlens/settings/#themable-colors) annotation at the end of the active line.

By default, the annotation displays:

- The author of the most recent commit
- The commit date
- The commit message

You can control visibility with the command:

- **Toggle Line Blame Annotations** (`gitlens.toggleLineBlame`)


***

## Git CodeLens

<figure>
  <img src="/wp-content/uploads/gl-code-lens-01-v3@2x.png" alt="GitLens CodeLens annotations above file and code blocks" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Inline Git insights for authorship and history</figcaption>
</figure>

Git CodeLens displays inline Git insights at the top of each file and above code blocks (enabled by [default](/gitlens/settings/#git-codelens-settings), and [customizable](/gitlens/settings/#git-codelens-settings)).

### CodeLens Types

- **Recent Change**  
  Shows the author and date of the most recent commit for the file or block.  
  - Click to open a **quick pick menu** with commit details and actions (e.g., compare, explore history).

- **Authors**  
  Displays the number of contributors and the most prominent author.  
  - Click to toggle Git blame annotations across the file.  
  - Automatically hides if there's only one author (to reduce visual noise).

### CodeLens Behavior

Click behavior for each CodeLens is fully [customizable](/gitlens/settings/#git-codelens-settings). You can choose from:

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

The **Status Bar Blame** displays Git blame details for the current line directly in the VS Code status bar. This feature is enabled by default and fully customizable.

### Default Behavior

- Displays the **author** and **date** of the last commit affecting the current line.
- Clicking the status bar opens a **quick pick menu** with commit actions (compare, explore history, etc.).

### Customizable Click Behavior

You can configure what happens when the status bar item is clicked:

- Toggle file blame annotations
- Toggle Git CodeLens on and off
- Compare the line’s commit to the previous one
- Compare the line’s commit to the working tree
- Show a quick pick menu with:
  - Commit details and actions *(default)*
  - File-level commit details
  - Commit history of the current file
  - Commit history of the current branch


***

## Hovers

GitLens provides rich, [customizable](/gitlens/settings/#hover-settings) hover annotations to surface Git information directly in your editor. These hovers are enabled by default and support both blame and diff insights.

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

Accessible when blame annotations are active, these hovers provide the same detail and diff options.

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

File Blame adds [customizable](/gitlens/settings/#gutter-blame-settings), [themable](/gitlens/settings/#themable-colors) inline annotations that show the commit and author responsible for each line in a file.

### Features

- Displays **commit message** and **commit date** per line (enabled by [default](/gitlens/settings/#file-blame-settings)).
- Adds a **heatmap (age) indicator** along the right edge to show how recently each line was changed.  
  _(See [File Heatmap](/gitlens/gitlens-features/#file-heatmap) for more info.)_
- Easily toggle annotations with:

  - **Command**: `gitlens.toggleFileBlame`
  - **Shortcut**: <kbd>Alt+B</kbd>
  - **Dismiss**: <kbd>Escape</kbd>


***

## File Changes

<figure>
  <img src="/wp-content/uploads/gl-gutter-changes-01@2x.png" alt="File Changes annotations in README.md with the gutter and line locations enabled: the uncommitted edits at the bottom of the file — one modified line and a new &quot;Release checklist&quot; section — are highlighted, with the matching marker in the gutter, while the unchanged lines above are plain" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Highlight unpublished or most recent changes</figcaption>
</figure>

The File Changes annotation highlights lines that have been changed either locally (unpublished) or by the most recent commit.

This feature is [customizable](/gitlens/settings/#file-changes-settings) and [themable](/gitlens/settings/#themable-colors), and is designed for quick visual inspection of file updates.

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

The File Heatmap adds a color-coded bar to the edge of your file, helping you quickly spot older versus more recent changes.

### Features

- Heatmap colors are [customizable](/gitlens/settings/#file-heatmap-settings) and reflect line age:
  - **Hot (bright)** for recent changes
  - **Cold (dim)** for older changes  
    _(Lines default to “cold” after 90 days.)_
- Brightness adjusts dynamically based on the **median age** of all changes in the file.
- Toggle with the command: `gitlens.toggleFileHeatmap`
- Press <kbd>Escape</kbd> to hide the heatmap annotations

***

## Code Suggest <span style="color: #888;">`PREVIEW`</span>

GitKraken Code Suggest simplifies code review by enabling you to propose edits across an entire project—not just the lines changed—in GitLens, GitKraken Desktop, or [gitkraken.dev](https://gitkraken.dev).

When a pull request is open, you can make suggestions that collaborators can review and apply directly to the PR.

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

Once submitted, the pull request will receive a comment with two options:

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
3. Click **Commit Suggestions** to commit the patch directly to the PR’s branch.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion.gif" alt="Committing suggestions from gitkraken.dev" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Accept changes and push them to the remote branch</figcaption>
</figure>


***

## Cloud Patches <span style="color: #888;">`PREVIEW`</span>

### What Are Cloud Patches and Why Use Them?

Cloud Patches are Git patches that GitKraken securely stores for easy sharing across GitLens, GitKraken Desktop, and the GitKraken CLI. The patch is uploaded directly from your machine into secure cloud storage.

This feature enables early collaboration—before a pull request is created—by letting you share in-progress work with your team. It helps streamline feedback cycles and reduce delays in PR reviews.

---

### How to Set Up Cloud Patches

Cloud Patches are enabled by default, but you can manage this per client.

1. Open the Command Palette:  
   `Ctrl`/`Command` + `Shift` + `P` → **Preferences: Open User Settings (JSON)**

2. Add the following line to your settings:

       "gitlens.cloudPatches.enabled": true

To disable Cloud Patches, change the value to `false`.


### How to Work with Cloud Patches

Cloud Patches are accessible from the **Cloud Patches** view in the GitLens sidebar.

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

- **Anyone with the link** – Public access without login.
- **Anyone in my org** – Restricted to users in your GitKraken organization (GitKraken login required).
- **Only collaborators** – Restricted to selected organization members. Use **Invite** to choose recipients.

Cloud Patches shared with you appear under the **Shared with Me** section.

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> If you're a member of multiple organizations, you can switch organizations from the GitKraken Account view.</p>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" alt="Cloud patch share dialog with access levels" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Control access to shared patches by role</figcaption>
</figure>

You can also apply Cloud Patches directly from a shared URL. Simply click or paste the link, then follow GitLens prompts to apply it to your working directory or to a new/existing branch.

<figure>
  <img src="/wp-content/uploads/gl-apply-patch-example.gif" alt="Apply a cloud patch animation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Apply patches seamlessly to your current repo</figcaption>
</figure>

To delete a Cloud Patch, right-click it and choose **Delete Cloud Patch...**.

<figure>
  <img src="/wp-content/uploads/gl-delete-cloud-patch-01-v3@2x.png" alt="Cloud Patches view in the GitLens sidebar showing a right-click context menu with Delete Cloud Patch option on a patch entry" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Remove unused patches with one click</figcaption>
</figure>


### Self-Hosting Cloud Patch Data

If you prefer not to store Cloud Patch data on GitKraken servers, you can configure GitLens to use your own AWS S3 storage.

Learn how to configure this in our [Self-Hosting Guide](/gk-dev/gk-dev-home/#self-hosted).

***

## Commit Graph

The Commit Graph is the starting point for working in GitLens. It brings repository history, branches, worktrees, Working Changes, pull requests, and supported agent activity into one connected workbench, so you can understand what's happening and move changes toward merge without rebuilding context across tools.

Built on a high-performance rendering engine, the graph stays responsive on large repositories, showing commits, branches, and contributors in one place.

The Commit Graph is included in **GitLens Community** and available to everyone on public and local repositories &mdash; no account required. A <a href="https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens" target="_blank">GitLens Pro subscription or trial</a> is required only for private repositories.

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

From here, you can:

- Click the branch name to switch branches
- Click **Fetch** to update commit data

<figure>
  <img src="/wp-content/uploads/gl-graph-info-01-v3@2x.png" srcset="/wp-content/uploads/gl-graph-info-01-v3@2x.png" alt="The top of the Commit Graph in the editor area: the tab reads &quot;Commit Graph: Playground2026&quot;, the header shows the current branch (main) with Push and &quot;Fetch (1wk ago)&quot; buttons, and the Fetch button's hover popover lists the upstream (origin/main on GitHub), &quot;Last fetched last week&quot; and the Auto-fetch option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access key branch controls directly from the header</figcaption>
</figure>

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> The Commit Graph is included in GitLens Community and available to all users on public or local repositories, without needing an account.</br></br>
  Only private repository access requires a <a href="https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens" target="_blank">GitLens Pro subscription or trial</a>.</p>
  <p>We welcome your input—join the discussion on <a href="https://github.com/gitkraken/vscode-gitlens/discussions/2158" target="_blank">GitHub</a>.</p>
</figure>

### Configuration and Layout

The Commit Graph offers extensive layout and configuration options so you can tailor the view to fit your workflow.

---

#### Column Customization

All columns in the Commit Graph are fully customizable:

- Drag and drop column headers to rearrange the layout.
- Right-click a column header to toggle columns on or off.
- The **Changes** column visualizes added and deleted lines per commit. The `gitlens.graph.changesColumn.mode` setting controls the display style: `numbers` (numeric counts), `squares` (colored blocks), `bar` (horizontal bar), or `bipolar` (split additions/deletions bar).

<figure>
  <img src="/wp-content/uploads/gl-column-settings-v2@2x.png" alt="Commit Graph settings menu showing options to hide the Author, Date, SHA, Changes, and other columns, switch the graph layout, and use a compact layout" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Customize visible columns with right-click options</figcaption>
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
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location-01-v3@2x.png" alt="The Commit Graph open in the editor area with the tab's More Actions (…) menu expanded, listing Prefer Commit Graph in Editor and Prefer Commit Graph as a View among the editor actions" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Choose where the graph displays: Panel or Editor</figcaption>
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

You can toggle scroll markers in [Commit Graph settings](/gitlens/gitlens-features/#settings).

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

### Rich Commit Search

The Commit Graph includes a powerful search bar to locate commits by message, author, file, or even specific code changes.

#### Natural Language Search `PRO`

You can type plain-language queries (e.g., "changes to the login page last week") and GitKraken AI converts them into structured Git search operators automatically. Natural language search works in the Commit Graph search bar, the Search & Compare view, and the Search Commits command.

#### Search Prefixes

Use the following search prefixes:

- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
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

### Pull Request Indicators

For GitHub and GitLab, GitLens displays a **Pull Request icon** on branches with active pull requests. To enable this:

1. Connect your account using [rich integration settings](/gitlens/settings/#remote-provider-integration-settings).
2. The icon will appear next to branches in the graph once linked.

<figure>
  <img src="/wp-content/uploads/gl-pull-request-icon-01-v3@2x.png" alt="The Commit Graph with the fixture/code-suggest-demo branch pill ringed: after the branch name and its origin remote the pill carries the pull-request icon, which marks the branch as having an associated open pull request" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Active pull requests are shown with branch-level icons</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

You can hide individual remotes, branches, or tags from the Commit Graph to reduce clutter and focus your view.

- **To hide**: Right-click a branch or tag pill and select **Hide Local Branch**, **Hide Remote Branch**, or **Hide Tag**. To hide whole classes of refs, use the scope/filter popover next to the search box.
- **To show again**: Use the **Hide** panel at the top of the graph and reselect the ref.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs-01-v3@2x.gif" alt="Hiding a branch in the Commit Graph: right-clicking the conflict-branch ref opens its context menu, and choosing Hide Local Branch removes the ref from the graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Use the “Hide” option to declutter the graph</figcaption>
</figure>

#### Filtering Options

You can further control what is shown using the filter dropdown:

- **All Branches** — Display all branches
- **Current Branch** — Display the current branch and its upstream (minimal view)
- **Smart Branches** — Display only the relevant branches: the current branch, its upstream, and its base or target branch
- Toggle visibility of:
  - Remote-only branches
  - Tags
  - Stashes
- Option to **dim merge commits**

<figure>
  <img src="/wp-content/uploads/gl-filter-options-2-01-v3@2x.png" alt="Commit Graph filter options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Customize your view with filter presets</figcaption>
</figure>

---

### Minimap <span style="color: #888;">(Experimental)</span>

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

<div class='callout callout--basic'>
  <p>Note: We welcome your feedback on the Minimap. Share your thoughts on the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>GitLens GitHub Discussions</a>.</p>
</div>


***

## Launchpad `PRO`

Launchpad organizes pull requests (PRs) by status to help you identify bottlenecks and take prioritized actions. This streamlined view allows you to manage PRs quickly, directly within VS Code.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" alt="Launchpad PR overview" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View and act on PRs based on current status</figcaption>
</figure>

<div class='callout callout--basic'>
  <p>Launchpad currently supports GitHub.com and GitLab.com repositories. To use it, connect your Git provider using the <a href="https://help.gitkraken.com/gitlens/gitlens-features/#connecting-the-github-and-gitlab-integration">GitHub or GitLab Integration</a>.</p>
</div>

---

### Accessing Launchpad

- From the **Command Palette**: `Command/Ctrl + Shift + P` → `GitLens: Open Launchpad`
- Or select the **Pull Request status bar item** in VS Code

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" alt="Opening Launchpad from status bar" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Launchpad from the status bar or Command Palette</figcaption>
</figure>

---

### Using Launchpad

View PRs by grouped statuses:
- Ready to merge
- Blocked
- Requires follow-up
- Needs your review
- Waiting for review
- Draft
- Snoozed

Click a PR to:
- View full details
- Open in your browser
- Merge (if eligible)
- Switch to the branch or open in a worktree

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" alt="PR detail view in Launchpad" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Interact with pull requests directly in VS Code</figcaption>
</figure>

You can also start or review [Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) directly from the PR action menu.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" alt="Launchpad with Code Suggest options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Suggest code edits from within the Launchpad</figcaption>
</figure>

*This feature is available through the [Gitkraken MCP](https://help.gitkraken.com/mcp/mcp-tools-reference/)*

---

### Start Review `PRO`

The **Start Review** command (`gitlens.startReview`) provides a guided wizard for beginning a pull request review. It walks you through selecting a PR from your connected integration, choosing whether to check out the branch or create a worktree, and optionally launching an AI chat pre-filled with a review prompt.

Access it from the Command Palette: `GitLens: Start Review`

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
  <p>Note: Launchpad prioritizes items requiring action by elevating them to the top of the list. This behavior may change in future updates.</p>
</div>

<div class='callout callout--warning'>
  <p>This feature is only available on GitLens Pro subscription tiers or higher.</p>
</div>


***

## Visual History

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

<div class='callout callout--warning'>
  <p>The Community plan supports Visual History only on public and local repositories.</p>
</div>


***

## GitKraken AI

GitKraken AI enhances your development workflow with automated commit messages, intelligent stash descriptions, and code change explanations.

---

### AI-Generated Commit Messages

Automatically generate descriptive commit messages based on staged changes.

<figure>
  <img src="/wp-content/uploads/gl-ai-generated-commit-message-01-v2.gif" alt="The Source Control view with a staged file: the empty commit message box, then an AI-generated commit message appearing in it" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit messages from staged changes</figcaption>
</figure>

To use:
- Stage your changes.
- In the Source Control view, open the GitLens sparkle menu in the Changes header and choose **Generate Commit Message**, or
- Use the Command Palette: `GitLens: Generate Commit Message`

GitKraken AI will analyze the diff of staged changes to generate a message. You may provide additional context in the commit box to improve results.

You can customize behavior using [`gitlens.ai` settings](/gitlens/gitlens-settings/#misc-settings) for provider, model, and prompt preferences.

<div class='callout callout--warning'>
  <p>Pro users and above can optionally use a custom API key to connect to a different AI provider. GitKraken AI currently uses the Google Gemini model.</p>
</div>

---

### AI Stash Messages `PRO`

Available in **Pro**, **Advanced**, and **Business** plans.

Automatically generate meaningful stash descriptions to make your stashes easier to identify later.

**How to access:**
- From the Command Palette: `GitLens: Generate Stash Message with AI`
- During stash creation: Use the AI option in the stash interface
- In the Stash view: Generate AI-powered descriptions for existing stashes

---

### AI Explanations `PREVIEW`

Let GitKraken AI help explain complex changes across your repo with natural language summaries.

<figure>
  <img src="/wp-content/uploads/ai-branch-summary.png" alt="AI branch summary explanation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI summaries in rendered markdown for improved clarity</figcaption>
</figure>

Standalone **Explain** commands provide markdown summaries for:
- Commits — **Explain Commit**
- Branches — **Explain Branch**
- Working changes — **Explain Working Changes**
- Stashes — **Explain Stash**

**Where to find it:**
- Commit Graph
- Command Palette
- GitLens views: Commits, Branches, Stashes, Search & Compare
- Editor blame hovers (sparkle Explain button)

With GitKraken AI explanations, you can quickly understand:
- The purpose and impact of individual commits
- What changed across all commits in a branch
- What you've modified in your working directory
- What your previous stashes contain
#### AI Commit Explanations `PRO`

*Available in:* **Pro**, **Advanced**, and **Business** plans

Understand the purpose and context of commits with AI-generated summaries. These explanations help you grasp the intent behind complex commits without manually reviewing all changes.

**How to access:**
- **Commit Details** view: See the AI explanation panel
- **Cloud Patch Details** view: View AI insights alongside commit data
- **Commit Review**: Generate explanations for any selected commit

---

### AI Changelog Creation `ADVANCED`

*Available in:* **Advanced** and **Business** plans only

Automatically generate detailed and structured changelogs from a set of selected commits—ideal for maintaining release documentation.

**How to access:**
- **Search/Compare** view: Click the inline button on the commits line
- **Commit Graph**: Select multiple commits, right-click, then choose **Generate Changelog**
- **Command Palette**: `GitLens: Generate Changelog from Commits`

<div class='callout callout--basic'>
  <p>More questions about GitKraken AI? See the <a href="https://help.gitkraken.com/general/gitkraken-ai-faq/">GitKraken AI FAQ</a> for additional details.</p>
</div>

### AI Generate Commits `PRO`

Generate well-structured commits from your working tree changes using AI analysis. The **Generate Commits** command analyzes your staged and unstaged changes, groups them logically, and creates commits with descriptive messages. A first-time confirmation dialog explains what the command will do, and an **Undo** button is available after generation to revert if needed.

### AI Rebase `PRO`

The **AI Rebase** command restructures commits on an existing branch onto a target commit using AI-generated commit grouping and messages. Like Generate Commits, it includes an undo button and a first-time confirmation dialog. Both commands produce markdown explanation documents summarizing the changes made.

### AI Auto Rebase `PRO`

AI Auto Rebase (`gitlens.ai.autoRebase`) carries a rebase forward through the conflicts GitKraken AI can resolve confidently, and hands the rest back to you. When a rebase encounters a conflict, AI analyzes it and resolves it only when its confidence meets the threshold you set; anything below that threshold pauses the rebase so you can resolve the conflict yourself and continue. Every run is reviewable and reversible.

Key capabilities:

- **Confidence threshold** — Configure `gitlens.ai.autoRebase.confidenceThreshold` (0 to 1) to control how confident the AI must be before resolving a conflict on its own. Raise it to keep more decisions in your hands.
- **Stops rather than guesses** — Conflicts that fall below the threshold are left for you to resolve manually, with the rebase paused at that point.
- **Custom instructions** — Use `gitlens.ai.resolveConflicts.customInstructions` to provide project-specific guidance for conflict resolution
- **Rebase summary sheet** — After the rebase completes, a summary sheet shows what was resolved and how, so you can review each decision
- **Full undo support** — Undo the entire auto-rebase with `gitlens.ai.autoRebase.undo` to return to the pre-rebase state if the results are not what you wanted

Access it from the Commit Graph context menu or the Command Palette: `GitLens: AI Auto Rebase`

### Commit Composer View `Pro`
The Commit Composer has evolved from a simple one-step process into a comprehensive drafting and review experience. Previously, AI would analyze your changes and immediately create commits. Now, the Commit Composer gives you complete control over the composition process, with options to auto-compose with AI or compose manually. It is integrated directly into the Commit Graph details panel as Compose mode, and is also available as a standalone view.

Join the [Commit Composer discussion](https://github.com/gitkraken/vscode-gitlens/discussions/4530) and provide feedback.

<figure>
  <img src="/wp-content/uploads/gl-commit-composer-17-4-01-v6@2x.png" alt="Commit Graph in Compose mode: the ringed Compose (wand) action on the Working Changes row, and the composer panel beside the graph listing Staged changes and Unstaged changes entries, the changed files, and the Instructions box with the Compose button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">The Commit Composer drafting view</figcaption>
</figure>

#### Interactive Draft Commits

When composing commits, GitLens now creates "draft" commits that you can review, modify, and refine before applying them to your repository. This new workflow lets you:

- **Preview before committing**: See exactly what will be committed before it touches your repository
- **Switch Models**: Try composition with different AI models
- **Guide the AI**: Provide custom instructions to match your team's conventions and preferences  
- **Iterate and refine**: Regenerate individual messages or entire commit compositions
- **Review and edit**: Manually tweak any commit message or approach

<figure>
  <img src="/wp-content/uploads/commit-composer-composed-17-4.png" alt="Commit Composer with AI-composed commit message populated and ready for review" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-composed commit message ready for review</figcaption>
</figure>

You can launch the new Commit Composer view from several places in GitLens:

- **GitLens commit details view**
- **Context menu on the Working Changes row** in the GitLens Commit Graph  
- **Commit Graph details panel**: Switch to **Compose** mode
- **✨ icon in the SCM view header**
- **Command palette**: Search for "Compose Commits"

<figure>
  <img src="/wp-content/uploads/gl-access-composer-1-17-4-01-v3@2x.png" alt="Commit Graph toolbar showing the Compose button entry point" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access Commit Composer from the graph toolbar</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-access-composer-2-17-4-01-v4@2x.png" alt="The Commit Graph's Working Changes details panel with the Compose and Review mode chips ringed in its header, above the branch row, the four changed files and the commit-message box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Or switch to Compose mode in the Working Changes details panel</figcaption>
</figure>

The foundation is now in place for even more powerful composition features in future releases, including intuitive drag-and-drop functionality for moving lines and hunks between commits, creating new draft commits on the fly, and reordering commit sequences.

Whether you prefer to let AI handle the heavy lifting or want granular control over every detail, Commit Composer provides the flexibility to create well-structured commit histories that make code reviews more effective and repository history easier to understand.

### Commit Composer: Branch Recomposition

Commit Composer now lets you clean up and reorganize commits on existing branches, making it perfect for preparing pull requests or refining your commit history before pushing.

<figure>
  <img src="/wp-content/uploads/gl-17-7-recompose-branch-01-v4@2x.png" alt="The Commit Composer opened for the feature/spending-insights branch: its four commits sit in the scope list with drag handles, main's commits are dimmed beneath them above the base, the three changed files are listed, and the Instructions box with the Compose button waits at the bottom" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Recompose an entire branch from the Commit Graph</figcaption>
</figure>

#### Recompose Entire Branches

Open Commit Composer from any branch in the Commit Graph (or anywhere branches appear in GitLens) to inspect and reorganize its commits. The composer creates draft commits you can review before applying changes to your repository.

**Auto-Recompose with AI**: Let AI analyze your branch and restructure commits into logical, well-documented units. Choose your preferred model and provide custom instructions to match your team's conventions. (Pro tip: Set default instructions in the "Generate Commits: Custom Instructions" setting to save time.)

**Manual Control**: Review AI suggestions, regenerate specific commit messages, or manually edit messages and change organization. The composer gives you complete flexibility to craft the commit story that works best.

<video src="/wp-content/uploads/gl-17-7-recompose-example.mp4" autoplay loop controls muted class="help-center-video"></video>

#### Enhanced Composer Capabilities

Commit Composer now handles edge cases that previously blocked composition:

- **Untracked files**: Working changes now include untracked files, so all modifications can be composed together
- **New repositories**: Compose your initial commits even before a base commit exists
- **Performance boost**: Significantly faster rendering when working with changes across many files

### Commit Composer: Selective Recomposition

Commit Composer now lets you recompose specific commits within a branch, giving you precise control over cleaning up your commit history.

<figure>
  <img src="/wp-content/uploads/gl-17-8-recompose-selected-commits-01-v5@2x.png" alt="The Commit Composer scoped to two selected commits of the feature/spending-insights branch — &quot;fix(insights): exclude refunds from spending totals&quot; and &quot;feat(insights): add budget threshold alerts&quot; — shown in the scope list with drag handles while the branch's other commits are dimmed, above the changed files and the Compose instructions box" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Select specific commits to recompose</figcaption>
</figure>

Previously, you could only recompose all working changes or an entire branch. Now you can select specific commits that need refinement—like those quick "wip" or "fix" commits made during rapid iteration—and let AI restructure just those changes with better messages.

Select multiple contiguous commits on the same branch using <kbd>Shift</kbd> or <kbd>Cmd</kbd> click, then right-click and choose "Recompose Selected Commits." Commit Composer opens with only your selected commits as drafts, ready for AI-powered or manual refinement.

Commit Composer is also more discoverable, with a new wand button on the Working Changes row in the Commit Graph that opens the composer for all working directory changes. Additionally, when rebasing, you can now switch directly into Commit Composer from the Rebase Editor, canceling your rebase to let AI handle the composition instead.

<figure>
  <img src="/wp-content/uploads/gl-17-8-compose-in-wip-01-v4@2x.png" alt="The Working Changes row at the top of the Commit Graph with its row actions at the right: the wand button that opens Commit Composer for all working directory changes is ringed" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Commit Composer from the Working Changes row</figcaption>
</figure>

### Compose and Recompose Commands

Commit Composer can also be launched via dedicated commands:

- **Compose Commits** (`gitlens.compose`) — Opens the Commit Composer for working changes in the current repository, or from a Compose mode entry in the Commit Graph details panel.
- **Recompose Branch** (`gitlens.recomposeBranch`) — Opens the Commit Composer scoped to an entire branch. GitKraken AI can propose a clearer, more intentional sequence of commits and messages for you to review and refine before applying the result.
- **Recompose from Commit** (`gitlens.recomposeFromCommit`) — Scopes the same workflow to a specific commit onward.
- **Recompose Selected Commits** (`gitlens.recomposeSelectedCommits`) — Scopes the same workflow to only the selected commits on a branch.

These commands are available from the Commit Graph context menu, branch context menus throughout GitLens, and the Command Palette. Coach marks guide first-time users through the workflow.

***

## Git Command Palette

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-01-v4@2x.png" alt="GitLens Git Command Palette showing guided step-by-step command options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Guided Git commands through the Command Palette</figcaption>
</figure>

Adds a [customizable](/gitlens/settings/#git-command-palette-settings) Git Command Palette (`gitlens.gitCommands`) for guided, step-by-step access to many common Git commands. Quickly navigate Git actions, explore commit history, manage stashes, and more—all through intuitive, confirmable menus.

---

### Quick Commit Access

- **Show Branch History** (`gitlens.showQuickBranchHistory`): Explore the commit history of any selected branch.
  
  <img src="/wp-content/uploads/menu-branch-history.png" class="help-center-img img-bordered">

- **Show Current Branch History** (`gitlens.showQuickRepoHistory`): View the commit history of your current branch.
- **Show File History** (`gitlens.showQuickFileHistory`): Access the full commit history of the current file. The File History view supports a **contributors mode** (`gitlens.views.fileHistory.mode`) that shows all contributors to the file instead of the commit list.

  <img src="/wp-content/uploads/gl-menu-file-history-01-v3@2x.png" alt="File History QuickPick for README.md listing its six commits with message, author, date, SHA and line-change counts; the newest commit is highlighted" class="help-center-img img-bordered">

- **Search Commits** (`gitlens.showCommitSearch`): Use a quick pick menu to search by:

  - Message: `<message>`
  - Author: `@<pattern>`
  - Commit SHA: `#<sha>`
  - File path or glob: `:<path/glob>`
  - Patch changes: `~<pattern>`

  <img src="/wp-content/uploads/gl-menu-commit-search-01-v2@2x.png" alt="Commit Search QuickPick showing the search mode options, including Search by Message, Author, Commit ID, File, and Changes, with their usage patterns" class="help-center-img img-bordered">

  Refer to the [Git log documentation](https://git-scm.com/docs/git-log) for advanced usage.

- **Show Commit Details** (`gitlens.showQuickCommitDetails`): Review commit information and actions.

  <img src="/wp-content/uploads/gl-menu-commit-details-01-v2@2x.png" alt="Commit Details QuickPick showing the commit message, author, SHA, and changed-file count, with actions including Revert, Reset, Create Branch, and Create Tag" class="help-center-img img-bordered">

- **Show Line Commit Details** (`gitlens.showQuickCommitFileDetails`): Explore the file's commit and take action on it.

  <img src="/wp-content/uploads/menu-commit-file-details.png" class="help-center-img img-bordered">


### Quick Stash Access

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-list-01-v3@2x.png" alt="Stash list QuickPick showing all stash entries in the repository with stash messages and selection options" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-details-01-v3@2x.png" alt="Stash details QuickPick for stash #0 showing its files-changed summary and the Apply Stash, Rename Stash, Drop Stash, Copy Message, Open, Compare and Browse Repository actions" class="help-center-img img-bordered">
</figure>

- Adds a _Show Stashes_ command (`gitlens.showQuickStashList`) to show a quick pick menu to explore your stashes.

---

### Quick Status Access

- Adds a _Show Repository Status_ command (`gitlens.showQuickRepoStatus`) to show a quick pick menu for visualizing the current repository status.

<figure>
  <img src="/wp-content/uploads/menu-repo-status.png" class="help-center-img img-bordered">
</figure>

---

## Interactive Rebase Editor

<figure>
  <img src="/wp-content/uploads/gl-rebase-01-v3@2x.gif" alt="GitLens interactive rebase editor: five commits each with an action dropdown, the second entry's dropdown open on pick / reword / edit / squash / fixup / drop, and then squash applied to it; the footer lists the keyboard shortcuts including alt + up/down to move a commit" class="help-center-img img-bordered">
</figure>

Adds a user-friendly interactive rebase editor to easily configure an interactive rebase session:

- Quickly re-order, edit, squash, and drop commits.
- Includes drag & drop support.
- Toolbar commands for **Abort**, **Continue**, **Reopen as Interactive Editor**, and **Reopen as Text Editor**.

### Conflict Detection

The rebase editor includes a **conflict files panel** that displays files with potential conflicts along with per-file conflict counts and status indicators. **Predictive conflict detection** warns about upcoming conflicts against the current base before you start the rebase, helping you prepare for issues in advance.

### Rebase Editor Settings

The rebase editor offers several configuration options:

- `gitlens.rebaseEditor.openOnPausedRebase` — Automatically open the rebase editor when a rebase is paused (e.g., due to conflicts).
- `gitlens.rebaseEditor.openBehavior` — Controls how the rebase editor opens: `auto` (default) or `beside` (opens alongside the current editor).
- `gitlens.rebaseEditor.revealLocation` — Where to reveal commit details: `graph` or `inspect`.
- `gitlens.rebaseEditor.revealBehavior` — When to reveal details: `never`, `onOpen`, or `onSelection`.
- `gitlens.rebaseEditor.density` — Controls row padding in the editor: `compact` (default) or `comfortable` for more spacing.

### Conflict Resolution Actions

When a rebase is paused due to conflicts, the rebase editor provides inline actions to **stage current changes** or **stage incoming changes** directly, streamlining the conflict resolution workflow.

### To use this directly from your terminal (e.g., when running `git rebase -i`):

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

GitLens verifies commit signatures using GPG, SSH, and X.509 certificates, displaying verification badges directly in the Commit Details view, Graph Details panel, and inline blame hovers.

### Verification Badges

Each signed commit shows a badge indicating its verification status:

- **Verified** — The signature is valid and the signer is trusted
- **Unverified** — The signature could not be verified (missing key, untrusted signer, etc.)
- **Unsigned** — The commit has no signature

The `${signature}` token is available in commit tooltip format strings to display signature status in custom tooltip layouts.

### Allowed Signers Management

The **Allowed Signers** webview (`gitlens.allowedSigners`) provides a dedicated panel for managing SSH trusted signers. It scans recent commits for SSH signatures, discovers candidate signers with their avatars, and lets you select which keys to trust. Trusted entries are saved to your SSH `allowed_signers` file.

Access it from the Command Palette: `GitLens: Manage Allowed Signers`


***

## Autolinks

Use autolinks to convert external references—such as Jira issues or Zendesk tickets—into clickable links directly from commit messages.

<figure>
  <img src="/wp-content/uploads/gl-autolinks-01-v4@2x.png" alt="Commit details in the GitLens Inspect view for a commit whose message ends in &quot;Closes #7&quot;: the #7 reference is a link, and the Autolinks section below the message shows the #7 chip with its hover popover naming the open pull request &quot;fix: add types and config to rate limiter&quot;" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of autolinks in commit messages</figcaption>
</figure>

## Terminal Links

<figure>
  <img src="/wp-content/uploads/gl-terminal-links-01-v3@2x.png" alt="The integrated terminal showing git log --oneline output, with the pointer on the first commit's SHA: GitLens underlines it as a link and shows the &quot;Show Commit (ctrl + click)&quot; hover" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Autolinks in the integrated terminal</figcaption>
</figure>

Terminal links optionally provide clickable references in the integrated terminal:

- [Branches, tags, and commit ranges](/gitlens/settings/#terminal-links-settings): Quickly explore their commit history.
- [Individual commits](/gitlens/settings/#terminal-links-settings): Review commit details and take further action.

***

## Remote Provider Integrations

GitLens provides rich integrations with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/settings/#remote-provider-integration-settings).

Basic integrations offer issue and pull request autolinking. Richer integrations, like GitHub or GitLab, include:

- Launchpad support
- Rich hover information for autolinks
- Pull request association with branches and commits
- Avatars for authors and commenters

These integrations also support various commands to open or copy URLs for files, commits, branches, and repositories:

- **Open File from Remote** (`gitlens.openFileFromRemote`) — Open a local file from a URL on a remote provider
- **Open Revision from Remote** (`gitlens.openRevisionFromRemote`) — Open the specific file revision referenced by a remote URL, rather than the working copy
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
2. Run `GitLens: Manage Integrations`.
3. Alternatively, in the GitLens **Home** view, select the integrations chip in the header to open the **Integrations** popover, then its gear (**Manage Integrations**).

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-01-v3@2x.png" srcset="/wp-content/uploads/gl-connect-remote-integration-01-v3@2x.png" alt="The GitLens Home view with the Integrations popover open from the header's integrations chip: a list of providers — GitHub, GitLab, Azure DevOps, Bitbucket, Jira, Linear — each with what it supports and a connected check mark, a Show: All | Connected filter, and the Manage Integrations gear ringed in the popover header" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Open the Integrations popover from the Home view header</figcaption>
</figure>

If you're not already signed in, you'll be prompted to log in to your GitKraken account. Then, select **Connect with GitHub** or **Connect with GitLab**, and follow the sign-in steps. You can connect multiple integrations if needed.

Finish the process by selecting **Complete Setup** to return to VS Code and begin using the integrations.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Manage your connected integrations</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>Community users are limited to basic functionality only.</p>
</div>


## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro offers a richer integration with GitHub Enterprise Server and GitLab Self-Managed.

Once authenticated, GitLens enhances autolinks in hovers with additional context. You’ll see your GitHub Enterprise Server or GitLab Self-Managed avatar, links to related pull requests, and a summary of pull request or issue details. Sidebar views for commits or branches also show this contextual information.

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

The Jira Integration, connected through your GitKraken Account, enables Jira [Autolinks](/gitlens/gitlens-features#autolinks) wherever autolinks are supported in GitLens. Once connected, GitLens automatically converts Jira issue keys (e.g., `ABC-123`) in commit messages into clickable links.

<figure>
  <img src="/wp-content/uploads/gl-jira-integration.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Jira autolinks in commit messages</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>This feature is only available for Pro subscription tiers or higher.</p>
</div>

To connect the integration:

1. Open the GitLens Settings editor (run _GitLens: Open Settings_ from the Command Palette).
2. Select **Cloud Integrations** under **Integrations** in the navigation rail.
3. Choose **Jira Cloud**, and authorize access to your Atlassian Account.
4. Alternatively, visit your [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations-01-v3@2x.png" alt="GitLens Settings Cloud Integrations category showing provider connection cards for GitHub, GitLab, Azure DevOps, Bitbucket, Jira, and Linear" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Cloud Integrations category in the GitLens Settings editor</figcaption>
</figure>


***

## Powerful Commands

GitLens provides powerful commands to improve your workflow:

- **Add Co-authors** (`gitlens.addAuthors`) — Add a co-author to the commit message input box.
- **Copy SHA** (`gitlens.copyShaToClipboard`) — Copy the commit SHA of the current line or the latest commit.
- **Copy Message** (`gitlens.copyMessageToClipboard`) — Copy the commit message from the current line or latest commit.
- **Copy Current Branch** (`gitlens.copyCurrentBranch`) — Copy the current branch name to the clipboard.
- **Switch to Another Branch** (`gitlens.views.switchToAnotherBranch`) — Quickly switch branches.
- **Compare References...** (`gitlens.compareWith`) — Compare two references.
- **Compare HEAD with...** (`gitlens.compareHeadWith`) — Compare HEAD with a selected reference.
- **Compare Working Tree with...** (`gitlens.compareWorkingWith`) — Compare the working tree with a selected reference.
- **Open Changes (difftool)** (`gitlens.externalDiff`) — Open file changes with the configured Git difftool.
- **Open All Changes (difftool)** (`gitlens.externalDiffAll`) — Open all working changes with the configured difftool.
- **Open Directory Compare (difftool)** (`gitlens.diffDirectoryWithHead`) — Compare working tree with HEAD using a difftool.
- **Open Directory Compare (difftool) with...** (`gitlens.diffDirectory`) — Compare with a selected reference.
- **Open File** (`gitlens.openWorkingFile`) — Open the working version of the current file.
- **Open Revision...** (`gitlens.openFileRevision`) — Open a selected file revision.
- **Open Revision from...** (`gitlens.openFileRevisionFrom`) — Open a revision from a specific reference.
- **Open Blame Prior to Change** (`gitlens.openBlamePriorToChange`) — Show blame for the prior revision of a line.
- **Open Changed Files** (`gitlens.openChangedFiles`) — Open all changed files in the working tree.
- **Close Unchanged Files** (`gitlens.closeUnchangedFiles`) — Close all files without changes.
- **Enable Debug Logging** (`gitlens.enableDebugLogging`) — Enable debug logging in the GitLens output.
- **Disable Debug Logging** (`gitlens.disableDebugLogging`) — Disable debug logging.
- **Copy as Patch** (`gitlens.copyPatchToClipboard`) — Copy patch data from views, changes, or stashes.
- **Apply Copied Patch** (`gitlens.applyPatchFromClipboard`) — Apply a patch from clipboard contents.
- **Change Branch Merge Target** (`gitlens.changeBranchMergeTarget`) — A multi-step wizard to set or reset a branch's merge target. Pick a local branch, then select a remote branch as its merge target, or reset an existing target.
- **Copy Changes to Worktree** (`gitlens.worktree.copyChanges`) — Copy working changes from one worktree to another.
- **Unlock Worktree** (`gitlens.worktree.unlock`) — Unlock a locked worktree from the tree view context menu.


***

## Deep Links

Deep Links are URLs that open specific GitLens resources, improving collaboration by sharing direct links to repositories, files, comparisons, and more. Resources that support Deep Linking include:

- **Search & Compare** — Link to comparisons in the [Search & Compare view](/gitlens/side-bar/#search-compare-view). Right-click a comparison, hover over _Share_, and select _Copy Link to Comparison_.
- **GitKraken Workspaces** — Link to a [GitKraken Workspace](/gitlens/side-bar/#workspaces-☁%ef%b8%8f). Right-click a Workspace, hover over _Share_, and select _Copy Link to Workspace_.
- **Commit Graph** — Link to remote repositories, commits, branches, and tags in the [Commit Graph](gitlens/gitlens-features/#commit-graph-%60pro%60). Right-click the resource, hover over _Share_, and select _Copy Link to <resource>_.
- **Files or Lines** — Link to specific files or lines of code. Right-click highlighted lines or a file, hover over _Share_, and select _Copy vscode.dev Link_.
- **Cloud Patches** — Link to a [Cloud Patch](/gitlens/gitlens-features/#cloud-patches-preview-%e2%98%81%ef%b8%8f). After generating a Cloud Patch, click _Copy Link_ from the success prompt.

<figure>
  <img src="/wp-content/uploads/gl-deep-link-example.gif" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of generating and using Deep Links</figcaption>
</figure>

***

## Git Submodule Support

GitLens provides basic support for Git submodules. Submodule repositories are automatically discovered and tracked when you open a project that contains them. In the sidebar views, submodule repositories are distinguished with dedicated icons and tooltips. Submodule changes are handled in diffs so you can see when a submodule reference has been updated.

***

## Welcome View

The **Welcome** sidebar view provides a guided multi-step walkthrough for new and returning users. It covers getting started with GitLens, the Home view, the Commit Graph, AI features, Git Blame, PR reviews, and MCP agent integration. The walkthrough content adapts based on your subscription level.

Access it from the GitLens sidebar — the Welcome view appears at the top of the sidebar panel.

***

## AI Agent Integration `PRO`

GitLens integrates with AI coding agents to monitor their activity and coordinate their work alongside your own development workflow.

### Supported Agents

Agent integration supports multiple AI agents:

- Claude Code
- OpenAI Codex
- GitHub Copilot
- Google Gemini
- OpenCode

### Agent Hooks

GitLens can install hooks for AI agents so their activity is tracked within your repository. Use the following commands:

- **Install Agent Hooks** (`gitlens.installHooks`) — Install hooks for all detected agents
- **Install Hooks for Agent** (`gitlens.installHooksForAgent`) — Install hooks for a specific agent
- **Uninstall Agent Hooks** (`gitlens.uninstallHooks`) — Remove hooks for all agents
- **Uninstall Hooks for Agent** (`gitlens.uninstallHooksForAgent`) — Remove hooks for a specific agent

### Agent Sessions

When hooks are active, GitLens tracks agent sessions and displays status indicators:

- **Agent session cards** appear in the Home view showing active and recent sessions
- **Status pills** on branches in the Commit Graph indicate which branches have active agent sessions
- **Resume Session** (`gitlens.resumeSession`) and **Archive Session** (`gitlens.archiveSession`) commands manage session lifecycle

### MCP Server Management

GitLens manages the GitKraken MCP server installation on a per-agent basis. The **Connect Agents** flow walks you through installing the CLI, registering MCP for your current IDE, and connecting additional agents.

- **Connect Agents** (`gitlens.mcp.connectAgents`) — Interactive flow to install and configure MCP for your agents
- **Install MCP for All Agents** (`gitlens.mcp.installForAllAgents`) — Install the GitKraken MCP server for all detected agents
- **Install MCP for Agent** (`gitlens.mcp.installForAgent`) — Install for a specific agent
- **Uninstall MCP for Agent** (`gitlens.mcp.uninstallForAgent`) — Remove MCP from a specific agent

The agent settings panel provides a centralized view for managing agent configurations.

***

## Menus & Toolbars

<figure>
  <img src="/wp-content/uploads/gl-menus-01-v2@2x.png" alt="GitLens Visual Settings Editor showing the Menus and Toolbars category, with toggle options controlling where GitLens commands appear in editor menus, context menus, and toolbars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">GitLens menu and toolbar options</figcaption>
</figure>

GitLens provides [customizable](/gitlens/gitlens-settings/#elementor-toc__heading-anchor-16) menu and toolbar contributions to let you control where GitLens commands appear. You can easily manage these settings via the [interactive settings editor](/gitlens/gitlens-settings/).

For example, disabling **Add to the editor group toolbar** removes those items from the toolbar:

<figure>
  <img src="/wp-content/uploads/gl-menus-example-01-v2@2x.png" alt="VS Code editor tab bar with the GitLens editor group toolbar items removed, showing a toolbar without GitLens action buttons" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Editor group toolbar items removed</figcaption>
</figure>

You can also expand each section to customize visibility and placement more granularly.

***

## Modes

GitLens supports [user-defined](#modes-settings- 'Jump to the Modes settings') modes for quickly toggling between sets of settings.

- Shows the active mode in the **status bar** ([optional](#modes-settings- 'Jump to the Modes settings'), enabled by default)
  - **Toggle Review Mode** (`gitlens.toggleReviewMode`) — Quickly toggle Review mode.
- **Switch Mode** (`gitlens.switchMode`) — Quickly switch between modes.
- **Zen Mode** — Disables many visual elements for a focused experience.
  - **Toggle Zen Mode** (`gitlens.toggleZenMode`) — Toggle Zen mode.
- **Review Mode** — Enables visual elements for code review.

### Experimental Multi-diff Editor

VS Code 1.86 or later is required for these capabilities.

#### Commands using Multi-diff

- **Open Folder Changes with Revision...** and **Open Folder Changes with Branch or Tag...** via Command Palette, Explorer, and Source Control views.
- Inline **Open All Changes** in commits, stashes, and comparison views.
- **Open All Changes** and **Open All Changes with Working Tree** — Use the new multi-diff editor.
- **Open All Changes, Individually** and **Open All Changes with Working Tree, Individually** — Provide legacy behavior.
