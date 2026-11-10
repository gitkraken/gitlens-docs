---
title: Blame and Annotation Features
description: Technical reference for GitLens revision navigation, current line blame, Git CodeLens, status bar blame, hovers, and file blame, changes, and heatmap annotations.
product: GitLens
feature: Blame and Annotations
content_type: reference
audience: developer
plan_required: [all]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [blame, codelens, hovers, annotations, heatmap, revision-navigation]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Blame and Annotations"
    nav_order: 20
    nav_parent: "gitlens-features"
    page_type: "content"
    card_icon: "code"
    card_color: "red"
    card_description: "Revision navigation, inline and status bar blame, CodeLens, hovers, and file annotations"
---
<kbd>Last updated: November 2026</kbd>

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

Current Line Blame adds a subtle, [customizable](/gitlens/gitlens-settings/#current-line-blame-settings), and [themable](/gitlens/gitlens-settings/#themable-colors) annotation at the end of the active line.

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

Git CodeLens displays inline Git insights at the top of each file and above code blocks (enabled by [default](/gitlens/gitlens-settings/#git-codelens-settings), and [customizable](/gitlens/gitlens-settings/#git-codelens-settings)).

### CodeLens Types

- **Recent Change**  
  Shows the author and date of the most recent commit for the file or block.  
  - Click to open a **quick pick menu** with commit details and actions (e.g., compare, explore history).

- **Authors**  
  Displays the number of contributors and the most prominent author.  
  - Click to toggle Git blame annotations across the file.  
  - Automatically hides if there's only one author (to reduce visual noise).

### CodeLens Behavior

Click behavior for each CodeLens is fully [customizable](/gitlens/gitlens-settings/#git-codelens-settings). You can choose from:

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

GitLens provides rich, [customizable](/gitlens/gitlens-settings/#hover-settings) hover annotations to surface Git information directly in your editor. These hovers are enabled by default and support both blame and diff insights.

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

File Blame adds [customizable](/gitlens/gitlens-settings/#file-blame-settings), [themable](/gitlens/gitlens-settings/#themable-colors) inline annotations that show the commit and author responsible for each line in a file.

### Features

- Displays **commit message** and **commit date** per line (enabled by [default](/gitlens/gitlens-settings/#file-blame-settings)).
- Adds a **heatmap (age) indicator** along the right edge to show how recently each line was changed.  
  _(See [File Heatmap](#file-heatmap) for more info.)_
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

This feature is [customizable](/gitlens/gitlens-settings/#file-changes-settings) and [themable](/gitlens/gitlens-settings/#themable-colors), and is designed for quick visual inspection of file updates.

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

- Heatmap colors are [customizable](/gitlens/gitlens-settings/#file-heatmap-settings) and reflect line age:
  - **Hot (bright)** for recent changes
  - **Cold (dim)** for older changes  
    _(Lines default to “cold” after 90 days.)_
- Brightness adjusts dynamically based on the **median age** of all changes in the file.
- Toggle with the command: `gitlens.toggleFileHeatmap`
- Press <kbd>Escape</kbd> to hide the heatmap annotations
