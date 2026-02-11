---
title: GitLens Features
description: Learn how to use GitLens autolinks, terminal links, powerful Git commands, remote provider integrations, and UI customizations to enhance your Git workflow in VS Code.
taxonomy:
  category: gitlens
---
<kbd>Last updated: June 2025</kbd>

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
  <img src="/wp-content/uploads/current-line-blame.png" alt="GitLens current line blame showing inline annotation" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/code-lens.png" alt="GitLens CodeLens annotations above file and code blocks" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/status-bar.png" alt="Status bar showing Git blame annotation with author and date" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/hovers-current-line.png" alt="Current line hover in GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Git blame hover shown over the current line</figcaption>
</figure>

#### Details Hover

<figure>
  <img src="/wp-content/uploads/hovers-current-line-details.png" alt="GitLens current line details hover with commit info and actions" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/hovers-current-line-changes.png" alt="GitLens diff hover showing current vs. previous line version" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View the previous version of a changed line</figcaption>
</figure>

Displays the previous version of the current line.

- Click **Changes** to run the _Open Changes_ command.
- Click commit SHAs to open _Show Commit_ views.

### Annotation Hovers

<figure>
  <img src="/wp-content/uploads/hovers-annotations.png" alt="GitLens annotation hover example" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Hover insights while annotating with blame</figcaption>
</figure>

Accessible when blame annotations are active, these hovers provide the same detail and diff options.

#### Details Hover

<figure>
  <img src="/wp-content/uploads/hovers-annotations-details.png" alt="Details hover during annotation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Commit metadata and action menu per line</figcaption>
</figure>

Shows rich commit details per line with:

- Automatic issue linking
- Quick-action command bar
- Clickable commit SHA to open commit details

#### Changes (Diff) Hover

<figure>
  <img src="/wp-content/uploads/hovers-annotations-changes.png" alt="Changes hover during annotation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Inline diff hover showing previous line content</figcaption>
</figure>

Reveals the previous version of each annotated line.

- Click **Changes** to run _Open Changes_.
- Click SHAs to open the _Show Commit_ view.


***

## File Blame

<figure>
  <img src="/wp-content/uploads/gutter-blame.png" alt="GitLens file blame annotations in the editor gutter" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View who last modified each line and when</figcaption>
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
  <img src="/wp-content/uploads/gutter-blame.png" alt="File changes annotations highlighting modified lines" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/gutter-heatmap.png" alt="GitLens file heatmap on the right gutter of the editor" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/gl-delete-cloud-patch.png" alt="Delete option in GitLens Cloud Patch view" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Remove unused patches with one click</figcaption>
</figure>


### Self-Hosting Cloud Patch Data

If you prefer not to store Cloud Patch data on GitKraken servers, you can configure GitLens to use your own AWS S3 storage.

Learn how to configure this in our [Self-Hosting Guide](/gk-dev/gk-dev-home/#self-hosted).

***

## Commit Graph <span style="color: #888;">`PRO`</span>

The Commit Graph helps visualize your repository's commit history by displaying branches, commits, and contributors in a unified view. This makes it easier to understand project activity and make informed decisions quickly.

<figure>
  <img src="/wp-content/uploads/commit-graph.png" alt="Commit Graph in GitLens showing branches and commits" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Explore your full Git history at a glance</figcaption>
</figure>

---

### How to Open the Commit Graph

To open the Commit Graph:

1. Open the Command Palette:  
   <kbd>Cmd/Ctrl + Shift + P</kbd>

2. Type:  
   `Show Commit Graph`

A new tab will open, displaying your current repository’s commit history. You can scroll through the graph and resize column widths for easier viewing.

<figure>
  <img src="/wp-content/uploads/show-commit-graph.gif" alt="Using the Command Palette to open the GitLens Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Launch the graph directly from the Command Palette</figcaption>
</figure>

---

### Commit Graph Header

At the top of the graph, you’ll see:

- **Repository name**
- **Checked-out branch**
- **Last fetched timestamp**

From here, you can:

- Click the branch name to switch branches
- Click **Fetch** to update commit data

<figure>
  <img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" alt="Commit Graph header with repo name, branch, and fetch option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access key branch controls directly from the header</figcaption>
</figure>

<figure class='callout callout--basic'>
  <p><strong>Note:</strong> The Commit Graph is available to all users on public or local repositories without needing an account.</br></br>
  Private repository access requires a <a href="https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens" target="_blank">GitLens Pro subscription or trial</a>.</p>
  <p>We welcome your input—join the discussion on <a href="https://github.com/gitkraken/vscode-gitlens/discussions/2158" target="_blank">GitHub</a>.</p>
</figure>

### Configuration and Layout

The Commit Graph offers extensive layout and configuration options so you can tailor the view to fit your workflow.

---

#### Column Customization

All columns in the Commit Graph are fully customizable:

- Drag and drop column headers to rearrange the layout.
- Right-click a column header to toggle columns on or off.
- The **Changes** column displays visual indicators for added (green) and deleted (red) lines in each commit.

<figure>
  <img src="/wp-content/uploads/gl-column-settings.png" alt="Column customization context menu in Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Customize visible columns with right-click options</figcaption>
</figure>

---

#### Panel vs. Editor Layout

You can choose where the Commit Graph appears:

- **Panel Layout** — displays the graph in the bottom panel (next to Terminal) with a dedicated Commit Graph Details view.
- **Editor Area Layout** — shows the graph in a standard VS Code editor tab.

To switch layouts:

1. Click the gear icon in the top-right of the Commit Graph.
2. Select **Prefer Commit Graph in Panel Layout** or **Prefer Commit Graph in Editor Area**.

You can even open both layouts simultaneously.

<figure>
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location.png" alt="Layout settings for Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Choose where the graph displays: Panel or Editor</figcaption>
</figure>

---

#### Compact Layout

For smaller screens or simplified views:

- **Compact Graph Column Layout** reduces the visual size of the graph.
- The **Author** column shows avatars when minimized.
- Columns display icons instead of truncated text when resized to narrow widths.

To enable the compact graph layout, right-click the **Graph** column header and select **Compact Graph Column Layout**.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" alt="Compact layout in Commit Graph" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/commit-graph-settings.png" alt="Commit Graph settings in GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Access GitLens settings from the Command Palette</figcaption>
</figure>

---

### Rich Commit Search

The Commit Graph includes a powerful search bar to locate commits by message, author, file, or even specific code changes.

Use the following search prefixes:

- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me` (to filter commits made by your user)

<figure>
  <img src="/wp-content/uploads/Rich-Commit-Search.png" alt="Search bar filtering commit history in the Commit Graph" class="img-responsive center img-bordered">
  <figcaption style="text-align: center; color: #888">Search commit history with advanced filtering</figcaption>
</figure>

Use keyboard shortcuts to navigate results:

- <kbd>F3</kbd> / <kbd>Cmd+G</kbd> — next result  
- <kbd>Shift+F3</kbd> / <kbd>Shift+Cmd+G</kbd> — previous result  
- Hold <kbd>Shift</kbd> and click arrows to jump to first or last match

<figure>
  <img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" alt="Navigating through commit search results" class="img-responsive center img-bordered">
  <figcaption style="text-align: center; color: #888">Jump through results using keyboard or search controls</figcaption>
</figure>

You can also refine results with:

- **Match all**
- **Match case**
- **Regular expression**

<figure>
  <img src="/wp-content/uploads/search-options.png" alt="Commit Graph search filter toggles" class="help-center-img img-bordered">
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
### Pull Request Indicators

For GitHub and GitLab, GitLens displays a **Pull Request icon** on branches with active pull requests. To enable this:

1. Connect your account using [rich integration settings](/gitlens/settings/#remote-provider-integration-settings).
2. The icon will appear next to branches in the graph once linked.

<figure>
  <img src="/wp-content/uploads/pull-request-icon.png" alt="Pull request icon displayed in Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Active pull requests are shown with branch-level icons</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

You can hide individual remotes, branches, or tags from the Commit Graph to reduce clutter and focus your view.

- **To hide**: Hover over any ref and click **Hide**.
- **To show again**: Use the **Hide** panel at the top of the graph and reselect the ref.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs.gif" alt="Hiding Git refs in the Commit Graph" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Use the “Hide” option to declutter the graph</figcaption>
</figure>

#### Filtering Options

You can further control what is shown using the filter dropdown:

- **Show Current Branch Only** — Display the current branch and its upstream (minimal view)
- **Show All Local Branches** — Default view showing all local refs
- Toggle visibility of:
  - Remote-only branches
  - Tags
  - Stashes
- Option to **dim merge commits**

<figure>
  <img src="/wp-content/uploads/filter-options-2.png" alt="Commit Graph filter options" class="help-center-img img-bordered">
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

Customize the Minimap via the **graph icon dropdown**:

- Toggle between:
  - **Commits view**
  - **Lines changed view**
- Show or hide:
  - Markers for branches, tags, stashes, search results

<figure>
  <img src="/wp-content/uploads/gl-minimap-settings.png" alt="Minimap settings in Commit Graph" class="help-center-img img-bordered">
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

## Visual File History

Visual File History provides a clear timeline of a file's changes—showing when, what, and who modified it—helping you quickly understand how a file evolved.

To open Visual File History:
- Use the GitLens **Inspect Sidebar**, or
- From the **Command Palette**: `Cmd/Ctrl + Shift + P` → `GitLens: Show Visual File History View`

<figure>
  <img src="/wp-content/uploads/visual-file-history.png" alt="Visual File History overview" class="help-center-img img-bordered">
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
  <p>The Community plan supports Visual File History only on public and local repositories.</p>
</div>


***

## GitKraken AI

GitKraken AI enhances your development workflow with automated commit messages, intelligent stash descriptions, and code change explanations.

---

### AI-Generated Commit Messages

Automatically generate descriptive commit messages based on staged changes.

<figure>
  <img src="/wp-content/uploads/gl-ai-generated-commit-message.gif" alt="Generating AI commit messages" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">AI-generated commit messages from staged changes</figcaption>
</figure>

To use:
- Stage your changes.
- Open the **Home View** and click **Generate Commit Message**, or
- Use the Command Palette: `GitLens: Generate Commit Message (Experimental)`

GitKraken AI will analyze the diff of staged changes to generate a message. You may provide additional context in the commit box to improve results.

You can customize behavior using:
- `gitlens.experimental.generateCommitMessagePrompt` for message formatting
- Additional [`gitlens.ai` settings](/gitlens/gitlens-settings/#misc-settings) for provider and model preferences

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

✨**Explain** functionality provides markdown summaries for:
- Branches — ✨**Explain Branch**
- Working changes — ✨**Explain Working Changes**
- Stashes — ✨**Explain Stash**

**Where to find it:**
- Commit Graph
- Command Palette
- GitLens views: Commits, Branches, Stashes, Search & Compare
- Branch cards in the Home view

With GitKraken AI explanations, you can quickly understand:
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

### Commit Composer View `Pro`
The Commit Composer has evolved from a simple one-step process into a comprehensive drafting and review experience. Previously, AI would analyze your changes and immediately create commits. Now, the new Commit Composer view gives you complete control over the composition process, with options to auto-compose with AI or compose manually.

*This feature is available through the [Gitkraken MCP](https://help.gitkraken.com/mcp/mcp-tools-reference/)*

Join the [Commit Composer discussion](https://github.com/gitkraken/vscode-gitlens/discussions/4530) and provide feedback.

<img src="/wp-content/uploads/commit-composer-17-4.png" class="help-center-img img-bordered">

#### Interactive Draft Commits

When composing commits, GitLens now creates "draft" commits that you can review, modify, and refine before applying them to your repository. This new workflow lets you:

- **Preview before committing**: See exactly what will be committed before it touches your repository
- **Switch Models**: Try composition with different AI models
- **Guide the AI**: Provide custom instructions to match your team's conventions and preferences  
- **Iterate and refine**: Regenerate individual messages or entire commit compositions
- **Review and edit**: Manually tweak any commit message or approach

<img src="/wp-content/uploads/commit-composer-composed-17-4.png" class="help-center-img img-bordered">

You can launch the new Commit Composer view from several places in GitLens:

- **GitLens commit details view**
- **Context menu on the WIP row** in the GitLens Commit Graph  
- **Active branch card** in the GitLens Home View
- **✨ icon in the SCM view header**
- **Command palette**: Search for "Compose Commits"

<img src="/wp-content/uploads/access-composer-1-17-4.png" class="help-center-img img-bordered">
<img src="/wp-content/uploads/access-composer-2-17-4.png" class="help-center-img img-bordered">

The foundation is now in place for even more powerful composition features in future releases, including intuitive drag-and-drop functionality for moving lines and hunks between commits, creating new draft commits on the fly, and reordering commit sequences.

Whether you prefer to let AI handle the heavy lifting or want granular control over every detail, Commit Composer provides the flexibility to create well-structured commit histories that make code reviews more effective and repository history easier to understand.

### Commit Composer: Branch Recomposition

Commit Composer now lets you clean up and reorganize commits on existing branches, making it perfect for preparing pull requests or refining your commit history before pushing.

<img src="/wp-content/uploads/gl-17-7-recompose-branch.png" class="help-center-img img-bordered">

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

<img src="/wp-content/uploads/gl-17-8-recompose-selected-commits.png" class="help-center-img img-bordered">

Previously, you could only recompose all working changes or an entire branch. Now you can select specific commits that need refinement—like those quick "wip" or "fix" commits made during rapid iteration—and let AI restructure just those changes with better messages.

Select multiple contiguous commits on the same branch using <kbd>Shift</kbd> or <kbd>Cmd</kbd> click, then right-click and choose "Recompose Selected Commits." Commit Composer opens with only your selected commits as drafts, ready for AI-powered or manual refinement.

Commit Composer is also more discoverable, with a new button on the WIP row in the Commit Graph that opens the composer for all working directory changes. Additionally, when rebasing, you can now switch directly into Commit Composer from the Rebase Editor, canceling your rebase to let AI handle the composition instead.

<img src="/wp-content/uploads/gl-17-8-compose-in-wip.png" class="help-center-img img-bordered">

***

## Git Command Palette

<img src="/wp-content/uploads/git-command-palette.png" class="help-center-img img-bordered">

Adds a [customizable](/gitlens/settings/#git-command-palette-settings) Git Command Palette (`gitlens.gitCommands`) for guided, step-by-step access to many common Git commands. Quickly navigate Git actions, explore commit history, manage stashes, and more—all through intuitive, confirmable menus.

---

### Quick Commit Access

- **Show Branch History** (`gitlens.showQuickBranchHistory`): Explore the commit history of any selected branch.
  
  <img src="/wp-content/uploads/menu-branch-history.png" class="help-center-img img-bordered">

- **Show Current Branch History** (`gitlens.showQuickRepoHistory`): View the commit history of your current branch.
- **Show File History** (`gitlens.showQuickFileHistory`): Access the full commit history of the current file.

  <img src="/wp-content/uploads/menu-file-history.png" class="help-center-img img-bordered">

- **Search Commits** (`gitlens.showCommitSearch`): Use a quick pick menu to search by:

  - Message: `<message>`
  - Author: `@<pattern>`
  - Commit SHA: `#<sha>`
  - File path or glob: `:<path/glob>`
  - Patch changes: `~<pattern>`

  <img src="/wp-content/uploads/menu-commit-search.png" class="help-center-img img-bordered">

  Refer to the [Git log documentation](https://git-scm.com/docs/git-log) for advanced usage.

- **Show Commit Details** (`gitlens.showQuickCommitDetails`): Review commit information and actions.

  <img src="/wp-content/uploads/menu-commit-details.png" class="help-center-img img-bordered">

- **Show Line Commit Details** (`gitlens.showQuickCommitFileDetails`): Explore the file's commit and take action on it.

  <img src="/wp-content/uploads/menu-commit-file-details.png" class="help-center-img img-bordered">


### Quick Stash Access

<figure>
  <img src="/wp-content/uploads/menu-stash-list.png" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/menu-stash-details.png" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/rebase.gif" class="help-center-img img-bordered">
</figure>

Adds a user-friendly interactive rebase editor to easily configure an interactive rebase session:

- Quickly re-order, edit, squash, and drop commits.
- Includes drag & drop support.

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

## Autolinks

Use autolinks to convert external references—such as Jira issues or Zendesk tickets—into clickable links directly from commit messages.

<figure>
  <img src="/wp-content/uploads/gl-autolinks.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of autolinks in commit messages</figcaption>
</figure>

## Terminal Links

<figure>
  <img src="/wp-content/uploads/terminal-links.gif" class="help-center-img img-bordered">
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
3. Alternatively, open **GitKraken Account** from the GitLens Activity Bar and select **Integrations**.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration.png" srcset="/wp-content/uploads/gl-connect-remote-integration@2x.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Connect integrations from the GitKraken dashboard</figcaption>
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
  <img src="/wp-content/uploads/gitlab-github-integration.png" class="help-center-img img-bordered">
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
  <img src="/wp-content/uploads/gl-connect-to-remote-ghe.png" class="help-center-img img-bordered">
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

1. Open the GitLens Sidebar.
2. From the GitKraken Account view, select **Cloud Integrations**.
3. Choose **Jira Cloud**, and authorize access to your Atlassian Account.
4. Alternatively, visit your [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Connect Jira from GitKraken Cloud Integrations</figcaption>
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

## Menus & Toolbars

<figure>
  <img src="/wp-content/uploads/menus.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">GitLens menu and toolbar options</figcaption>
</figure>

GitLens provides [customizable](/gitlens/gitlens-settings/#elementor-toc__heading-anchor-16) menu and toolbar contributions to let you control where GitLens commands appear. You can easily manage these settings via the [interactive settings editor](/gitlens/gitlens-settings/).

For example, disabling **Add to the editor group toolbar** removes those items from the toolbar:

<figure>
  <img src="/wp-content/uploads/menus-example.png" class="help-center-img img-bordered">
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
