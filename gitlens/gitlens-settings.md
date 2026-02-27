---
title: GitLens Settings Overview
description: Learn how to access and customize GitLens settings in Visual Studio Code
taxonomy:
    category: gitlens
---
<kbd>Last updated: February 2026</kbd>

## Overview

<figure>
  <img src="/wp-content/uploads/settings.png" alt="GitLens settings editor UI in Visual Studio Code" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens interactive settings editor in VS Code</figcaption>
</figure>

GitLens offers a powerful and easy-to-use **interactive settings editor** that helps you configure many features directly in Visual Studio Code.

To open the editor, run the _GitLens: Open Settings_ command (`gitlens.showSettingsPage`) from the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

GitLens is highly customizable—nearly every feature can be tailored to fit your workflow using the available settings.

## Current Line Blame Settings

Use these settings to customize how GitLens displays blame annotations for the current line of code. These annotations help identify the last commit that modified a line, along with contextual details like date, author, and related pull requests.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.currentLine.dateFormat</code></td>
<td>Defines how absolute dates appear in current line blame annotations using the <code>${date}</code> token. Refer to the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js format guide</a>.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.enabled</code></td>
<td>Enables or disables current line blame annotations by default. Toggle annotations in any window with the <em>Toggle Line Blame Annotations</em> command (<code>gitlens.toggleLineBlame</code>).</td>
</tr>
<tr>
<td><code>gitlens.currentLine.format</code></td>
<td>Sets the display format for the annotation. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> for supported placeholders. Date format is managed by <code>gitlens.currentLine.dateFormat</code>.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.pullRequests.enabled</code></td>
<td>Shows pull request info (if available) for the commit in the current line annotation. Requires a connected remote provider like GitHub.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.scrollable</code></td>
<td>Determines if annotations can scroll into view when off-screen. <strong>Note:</strong> Setting this to <code>false</code> disables hover tooltips unless <code>gitlens.hovers.currentLine.over</code> is set to <code>line</code>.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.uncommittedChangesFormat</code></td>
<td>Customizes annotation format for uncommitted changes. An empty string disables annotations for these changes.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontFamily</code></td>
<td>Sets the font family for inline blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontSize</code></td>
<td>Sets the font size for inline blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontStyle</code></td>
<td>Sets the font style for inline blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontWeight</code></td>
<td>Sets the font weight for inline blame annotations.</td>
</tr>
</tbody>
</table>

***

## Git CodeLens Settings

These settings control GitLens CodeLens overlays, which provide inline contextual information such as author and commit history directly in your code.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.codeLens.authors.command</code></td>
<td>Sets the command triggered when an <em>authors</em> CodeLens is clicked. Default is <code>gitlens.toggleFileBlame</code>. To disable click actions, set this to <code>false</code>.<br><br>Available commands include:<br>
<code>gitlens.toggleFileBlame</code>, <code>gitlens.toggleFileHeatmap</code>, <code>gitlens.toggleFileChanges</code>, <code>gitlens.toggleFileChangesOnly</code>, <code>gitlens.diffWithPrevious</code>, <code>gitlens.revealCommitInView</code>, <code>gitlens.showCommitsInView</code>, <code>gitlens.showQuickCommitDetails</code>, <code>gitlens.showQuickCommitFileDetails</code>, <code>gitlens.showQuickFileHistory</code>, <code>gitlens.showQuickRepoHistory</code>, <code>gitlens.openCommitOnRemote</code>, <code>gitlens.copyRemoteCommitUrl</code>, <code>gitlens.openFileOnRemote</code>, <code>gitlens.copyRemoteFileUrl</code>.</td>
</tr>
<tr>
<td><code>gitlens.codeLens.authors.enabled</code></td>
<td>Enables or disables the <em>authors</em> CodeLens. Displays the number of contributors and highlights the most active author for a file or block.</td>
</tr>
<tr>
<td><code>gitlens.codeLens.enabled</code></td>
<td>Globally enables or disables all GitLens CodeLens features. Use the <em>Toggle Git CodeLens</em> command (<code>gitlens.toggleCodeLens</code>) to turn this feature on or off for the current window.</td>
</tr>
<tr>
<td><code>gitlens.codeLens.includeSingleLineSymbols</code></td>
<td>Determines whether GitLens shows CodeLens for single-line symbols (e.g., one-line functions).</td>
</tr>
<tr>
<td><code>gitlens.codeLens.recentChange.command</code></td>
<td>Sets the command triggered when a <em>recent change</em> CodeLens is clicked. Default is <code>gitlens.showQuickCommitFileDetails</code>. To disable, set to <code>false</code>.<br><br>Available commands mirror those listed under <code>authors.command</code>.</td>
</tr>
<tr>
<td><code>gitlens.codeLens.recentChange.enabled</code></td>
<td>Enables or disables the <em>recent change</em> CodeLens. Displays the author and timestamp of the most recent commit for the line or block.</td>
</tr>
<tr>
<td><code>gitlens.codeLens.scopes</code></td>
<td>Controls where Git CodeLens is displayed:<br>
<code>document</code> – top of the file<br>
<code>containers</code> – start of container symbols (e.g., classes, interfaces)<br>
<code>blocks</code> – start of block symbols (e.g., functions, methods)</td>
</tr>
<tr>
<td><code>gitlens.codeLens.symbolScopes</code></td>
<td>Defines specific symbol types to include or exclude from CodeLens. Prefix a symbol with <code>!</code> to exclude it. Uses <a href="https://code.visualstudio.com/docs/extensionAPI/vscode-api#_a-namesymbolkindaspan-classcodeitem-id660symbolkindspan" rel="nofollow"><code>SymbolKind</code></a> values.</td>
</tr>
</tbody>
</table>

***

## Status Bar Settings

These settings control how GitLens displays blame information in the status bar, including format, alignment, and click behavior.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.statusBar.alignment</code></td>
<td>Controls where the blame annotation appears in the status bar.<br><br><code>left</code> – aligns to the left<br><code>right</code> – aligns to the right</td>
</tr>
<tr>
<td><code>gitlens.statusBar.command</code></td>
<td>Specifies the command executed when clicking the blame status bar item. Default is <code>gitlens.toggleFileBlame</code>. You can choose from a list of commands, such as:<br><br>
<code>gitlens.toggleFileBlame</code>, <code>gitlens.toggleFileHeatmap</code>, <code>gitlens.toggleFileChanges</code>, <code>gitlens.toggleFileChangesOnly</code>, <code>gitlens.diffWithPrevious</code>, <code>gitlens.revealCommitInView</code>, <code>gitlens.showCommitsInView</code>, <code>gitlens.showQuickCommitDetails</code>, <code>gitlens.showQuickCommitFileDetails</code>, <code>gitlens.showQuickFileHistory</code>, <code>gitlens.showQuickRepoHistory</code>, <code>gitlens.openCommitOnRemote</code>, <code>gitlens.copyRemoteCommitUrl</code>, <code>gitlens.openFileOnRemote</code>, <code>gitlens.copyRemoteFileUrl</code></td>
</tr>
<tr>
<td><code>gitlens.statusBar.dateFormat</code></td>
<td>Sets the date format using the <code>${date}</code> token. For valid formats, see the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js documentation</a>.</td>
</tr>
<tr>
<td><code>gitlens.statusBar.enabled</code></td>
<td>Enables or disables blame information in the status bar.</td>
</tr>
<tr>
<td><code>gitlens.statusBar.format</code></td>
<td>Defines the display format of blame data in the status bar. Refer to <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>. Controlled alongside <code>gitlens.statusBar.dateFormat</code>.</td>
</tr>
<tr>
<td><code>gitlens.statusBar.pullRequests.enabled</code></td>
<td>Shows pull request details for the commit in the status bar, if available. Requires a connected remote (e.g., GitHub).</td>
</tr>
<tr>
<td><code>gitlens.statusBar.reduceFlicker</code></td>
<td>Reduces visual flicker by preventing blame info from clearing when switching lines.</td>
</tr>
<tr>
<td><code>gitlens.statusBar.tooltipFormat</code></td>
<td>Specifies the markdown format used in the hover tooltip over blame info. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>.</td>
</tr>
</tbody>
</table>

***

## Hover Settings

Use these settings to control when and how GitLens displays hover popups that show commit details, line changes, avatars, and pull request information.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.hovers.annotations.changes</code></td>
<td>Enables a <em>changes (diff)</em> hover for all lines when blame annotations are shown.</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.details</code></td>
<td>Enables a <em>commit details</em> hover for all lines when blame annotations are shown.</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.enabled</code></td>
<td>Enables all hovers related to blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.over</code></td>
<td>Controls when annotation hovers trigger:<br><br><code>annotation</code> – hover only on the annotation<br><code>line</code> – hover anywhere on the line</td>
</tr>
<tr>
<td><code>gitlens.hovers.avatars</code></td>
<td>Displays avatar images in hovers when enabled.</td>
</tr>
<tr>
<td><code>gitlens.hovers.avatarSize</code></td>
<td>Sets the avatar image size in hover popups.</td>
</tr>
<tr>
<td><code>gitlens.hovers.changesDiff</code></td>
<td>Controls the diff content shown in hovers:<br><br><code>line</code> – shows only changes to the line<br><code>hunk</code> – shows related changes (code hunk)</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.changes</code></td>
<td>Enables a <em>changes (diff)</em> hover for the current line.</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.details</code></td>
<td>Enables a <em>commit details</em> hover for the current line.</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.enabled</code></td>
<td>Enables all hover popups for the current line.</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.over</code></td>
<td>Controls when hovers appear on the current line:<br><br><code>annotation</code> – hover only on the annotation<br><code>line</code> – hover anywhere on the line</td>
</tr>
<tr>
<td><code>gitlens.hovers.detailsMarkdownFormat</code></td>
<td>Defines the markdown format used for <em>commit details</em> hovers. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>.</td>
</tr>
<tr>
<td><code>gitlens.hovers.enabled</code></td>
<td>Enables or disables all GitLens hovers.</td>
</tr>
<tr>
<td><code>gitlens.hovers.autolinks.enabled</code></td>
<td>Automatically links external resources mentioned in commit messages.</td>
</tr>
<tr>
<td><code>gitlens.hovers.autolinks.enhanced</code></td>
<td>Fetches enhanced details for autolinks using supported remote services (e.g., GitHub).</td>
</tr>
<tr>
<td><code>gitlens.hovers.pullRequests.enabled</code></td>
<td>Displays pull request information (if available) in hovers. Requires connection to a supported remote service.</td>
</tr>
</tbody>
</table>

</table>
***

## View Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.defaultItemLimit</code></td>
<td>Specifies the default number of items to show in a view list. Use 0 for no limit.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.commits.label</code></td>
<td>Specifies the format of commits in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.commits.description</code></td>
<td>Specifies the description format of commits in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.label</code></td>
<td>Specifies the format of a file in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.description</code></td>
<td>Specifies the description format of a file in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.label</code></td>
<td>Specifies the format of stashes in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.description</code></td>
<td>Specifies the description format of stashes in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.tooltip</code></td>
<td>Specifies the tooltip format of stashes in GitLens views.</td>
</tr>
<tr>
<td><code>gitlens.views.pageItemLimit</code></td>
<td>Specifies the number of items to show per page when paginating a view list. Use 0 for no limit.</td>
</tr>
<tr>
<td><code>gitlens.views.showRelativeDateMarkers</code></td>
<td>Specifies whether to show relative date markers (<em>Less than a week ago</em>, <em>Over a week ago</em>, <em>Over a month ago</em>, etc.) on revision histories in the views.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.icon</code></td>
<td>Specifies how the Commits view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.icon</code></td>
<td>Specifies how the Repositories view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.icon</code></td>
<td>Specifies how the Branches view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.label</code></td>
<td>Specifies how the Remotes view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.icon</code></td>
<td>Specifies how the Stashes view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.icon</code></td>
<td>Specifies how the Tags view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.icon</code></td>
<td>Specifies how the Worktrees view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.icon</code></td>
<td>Specifies how the Contributors view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.files.icon</code></td>
<td>Specifies how the Search & Compare view displays file icons.</td>
</tr>
<tr>
<td><code>gitlens.views.collapseWorktreesWhenPossible</code></td>
<td>Specifies whether to collapse opened worktrees into a single repository in views when possible.</td>
</tr>
<tr>
<td><code>Gitlens.views.showCurrentBranchOnTo</code></td>
<td>Specifies whether the current branch is shown at the top of views.</td>
</tr>
<tr>
<td><code>gitlens.views.scm.grouped.default</code></td>
<td>Specifies the default view shown in the grouped GitLens view for new workspaces/folders (otherwise last selected view is remembered).</td>
</tr>
<tr>
<td><code>gitlens.views.scm.grouped.views</code></td>
<td>Specifies which views to show in the grouped GitLens view.</td>
</tr>
</tbody>
</table>


***

## Commits View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings control how the GitLens <em>Commits</em> view displays commit data, associated files, and pull request information.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.commits.avatars</code></td>
<td>Shows avatar images in place of commit or status icons in the <em>Commits</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.layout</code></td>
<td>Controls how files are displayed:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> based on the <code>threshold</code><br>
<code>list</code> – displays a flat file list<br>
<code>tree</code> – displays a hierarchical file structure</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.enabled</code></td>
<td>Enables querying for pull requests associated with the current branch or commits. Requires a connected remote (e.g., GitHub).</td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.showForBranches</code></td>
<td>Shows pull requests linked to the current branch in the <em>Commits</em> view. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.showForCommits</code></td>
<td>Displays pull requests tied to individual commits in the <em>Commits</em> view. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.reveal</code></td>
<td>Determines whether commits are revealed in the <em>Commits</em> view or the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.commits.showBranchComparison</code></td>
<td>Controls whether to display branch or working tree comparisons:<br><br>
<code>false</code> – hides comparison section<br>
<code>branch</code> – compares current branch to another reference<br>
<code>working</code> – compares working tree to a selected reference</td>
</tr>
</tbody>
</table>

***

## Repositories View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings customize how repositories are displayed and interacted with in the GitLens <em>Repositories</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.repositories.avatars</code></td>
<td>Displays avatar images instead of icons in the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.autoRefresh</code></td>
<td>Automatically refreshes the view when the repository or filesystem changes.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.autoReveal</code></td>
<td>Auto-reveals repositories when opening files.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.branches.layout</code></td>
<td>Controls branch layout:<br><br>
<code>list</code> – shows all branches in a list<br>
<code>tree</code> – groups branches in a tree structure if names contain <code>/</code></td>
</tr>
<tr>
<td><code>gitlens.views.repositories.branches.showBranchComparison</code></td>
<td>Displays comparison with a user-selected reference (branch, tag, etc.) under each branch.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.compact</code></td>
<td>Enables a compact display mode in the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code> – switches based on file count and nesting<br>
<code>list</code> – flat file list<br>
<code>tree</code> – hierarchical file view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.threshold</code></td>
<td>Sets the threshold for switching between tree and list layouts when layout is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.includeWorkingTree</code></td>
<td>Includes working tree file status for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showBranchComparison</code></td>
<td>Displays comparison between a selected reference and the current branch or working tree.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showBranches</code></td>
<td>Shows branches for each repository.</td>
</tr>
<tr>
<td><code>itlens.views.repositories.showCommits</code></td>
<td>Displays commits from the current branch for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showContributors</code></td>
<td>Shows contributors for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showIncomingActivity</code></td>
<td>Displays experimental incoming activity for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showRemotes</code></td>
<td>Shows configured remotes for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showStashes</code></td>
<td>Displays stashes for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showTags</code></td>
<td>Shows tags for each repository.</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showUpstreamStatus</code></td>
<td>Displays upstream tracking status of the current branch for each repository.</td>
</tr>
</tbody>
</table>

***

## File History View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings configure the behavior and display options for the GitLens <em>File History</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.fileHistory.avatars</code></td>
<td>Displays avatar images instead of status icons in the <em>File History</em> view.</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryShowMergeCommits</code></td>
<td>Controls whether merge commits are shown in file history:<br><br><code>show</code> – includes merge commits<br><code>hide</code> – excludes merge commits</td>
</tr>
</tbody>
</table>


***

## Line History View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings configure the display behavior of the GitLens <em>Line History</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.lineHistory.avatars</code></td>
<td>Displays avatar images instead of status icons in the <em>Line History</em> view.</td>
</tr>
</tbody>
</table>

***

## Branch View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings configure the display and behavior of the GitLens <em>Branches</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.branches.avatars</code></td>
<td>Displays avatar images instead of commit or status icons in the <em>Branches</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.branches.layout</code></td>
<td>Controls how branches are displayed:<br><br>
<code>list</code> – shows branches as a list<br>
<code>tree</code> – groups branches into a tree structure</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> based on the <code>threshold</code><br>
<code>list</code> – displays a flat list<br>
<code>tree</code> – displays files hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.enabled</code></td>
<td>Enables querying for pull requests associated with the current branch and commits. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.showForBranches</code></td>
<td>Displays pull requests linked to the current branch in the <em>Branches</em> view. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.showForCommits</code></td>
<td>Displays pull requests tied to individual commits. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.reveal</code></td>
<td>Specifies whether branches are revealed in the <em>Branches</em> view or in the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.showBranchComparison</code></td>
<td>Controls display of branch comparisons:<br><br>
<code>false</code> – hides comparisons<br>
<code>branch</code> – compares the current branch with a selected reference</td>
</tr>
</tbody>
</table>

***

## Remotes View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings define how branches, files, and pull requests appear in the GitLens <em>Remotes</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.remotes.avatars</code></td>
<td>Displays avatar images instead of commit or status icons in the <em>Remotes</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.branches.layout</code></td>
<td>Controls how branches are displayed:<br><br>
<code>list</code> – shows branches in a flat list<br>
<code>tree</code> – groups branches hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> depending on nesting<br>
<code>list</code> – flat file list<br>
<code>tree</code> – hierarchical file view</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.enabled</code></td>
<td>Enables pull request queries for the current branch and commits. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.showForBranches</code></td>
<td>Displays pull requests associated with branches in the <em>Remotes</em> view. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.showForCommits</code></td>
<td>Displays pull requests tied to commits in the <em>Remotes</em> view. Requires a connected remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.reveal</code></td>
<td>Determines whether remotes appear in the <em>Remotes</em> view or are shown in the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.showBranchComparison</code></td>
<td>Controls display of branch comparisons:<br><br>
<code>false</code> – hides comparisons<br>
<code>branch</code> – compares the current branch with a selected reference</td>
</tr>
</tbody>
</table>
***

## Stashes View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings control how files and stash entries are displayed in the GitLens <em>Stashes</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.stashes.files.compact</code></td>
<td>Flattens unnecessary file nesting in the <em>Stashes</em> view. Applies when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> layouts based on nesting<br>
<code>list</code> – shows a flat list<br>
<code>tree</code> – shows a hierarchical view</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.reveal</code></td>
<td>Determines whether stashes appear in the <em>Stashes</em> view or the <em>Repositories</em> view.</td>
</tr>
</tbody>
</table>

***

## Tags View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings control how Git tags and related files appear in the GitLens <em>Tags</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.tags.avatars</code></td>
<td>Displays avatar images instead of commit or status icons in the <em>Tags</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.branches.layout</code></td>
<td>Controls tag layout:<br><br>
<code>list</code> – displays tags as a flat list<br>
<code>tree</code> – groups tags hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.compact</code></td>
<td>Flattens unnecessary file nesting when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> layouts based on nesting<br>
<code>list</code> – shows a flat list<br>
<code>tree</code> – shows a hierarchical view</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.reveal</code></td>
<td>Determines whether tags are shown in the <em>Tags</em> view or revealed in the <em>Repositories</em> view.</td>
</tr>
</tbody>
</table>

***

## Worktrees View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings control how worktrees and related information appear in the GitLens <em>Worktrees</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.worktrees.avatars</code></td>
<td>Displays avatar images instead of commit or status icons in the <em>Worktrees</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.compact</code></td>
<td>Flattens unnecessary file nesting. Applies only when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.layout</code></td>
<td>Controls how files are displayed:<br><br>
<code>auto</code> – automatically switches between <code>tree</code> and <code>list</code> views based on the <code>threshold</code><br>
<code>list</code> – shows files in a flat list<br>
<code>tree</code> – shows files hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.threshold</code></td>
<td>Defines when to switch between <code>tree</code> and <code>list</code> layouts based on file count. Applies only when layout is <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.enabled</code></td>
<td>Enables pull request queries for the current worktree branch and its commits. Requires a supported remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.showForBranches</code></td>
<td>Shows pull requests related to the current worktree branch. Requires a supported remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.showForCommits</code></td>
<td>Displays pull requests (if any) associated with commits in the <em>Worktrees</em> view. Requires a supported remote service.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.reveal</code></td>
<td>Controls whether worktrees appear in the <em>Worktrees</em> view or default to the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.showBranchComparison</code></td>
<td>Shows a comparison of the current branch with a user-selected reference:<br><br>
<code>false</code> – hides comparisons<br>
<code>branch</code> – compares with a selected reference (e.g., tag or branch)</td>
</tr>
</tbody>
</table>

***

## Contributors View Settings

See also [View Settings](/gitlens/settings/#view-settings)

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.contributors.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Contributors</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Contributors</em> view. Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.layout</code></td>
<td>Specifies how the <em>Contributors</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Contributors</em> view. Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.contributors.pullRequests.enabled</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Contributors</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.pullRequests.showForCommits</code></td>
<td>Specifies whether to show pull requests (if any) associated with the current branch in the <em>Contributors</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.showAllBranches</code></td>
<td>Specifies whether to show commits from all branches in the <em>Contributors</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.showStatistics</code></td>
<td>Specifies whether to show contributor statistics in the <em>Contributors</em> view. This can take a while to compute depending on the repository size</td>
</tr>
</tbody>
</table>

***

## Search & Compare View Settings

See also [View Settings](/gitlens/settings/#view-settings).

These settings control the display options for files and avatars in the GitLens <em>Search Commits</em> and <em>Compare</em> views.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.compare.files.compact</code></td>
<td>Flattens unnecessary file nesting in the <em>Compare</em> view. Applies when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.compare.files.layout</code></td>
<td>Controls file display in the <em>Compare</em> view:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> based on nesting and threshold<br>
<code>list</code> – shows files in a flat list<br>
<code>tree</code> – shows files hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.compare.files.threshold</code></td>
<td>Determines when to switch between <code>tree</code> and <code>list</code> layouts based on the number of files in a nesting level. Applies only when layout is <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.compare.avatars</code></td>
<td>Shows avatar images instead of commit or status icons in the <em>Compare</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.search.files.compact</code></td>
<td>Flattens unnecessary file nesting in the <em>Search Commits</em> view. Applies when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.search.files.layout</code></td>
<td>Controls file display in the <em>Search Commits</em> view:<br><br>
<code>auto</code> – switches between <code>tree</code> and <code>list</code> based on nesting and threshold<br>
<code>list</code> – shows files in a flat list<br>
<code>tree</code> – shows files hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.search.avatars</code></td>
<td>Shows avatar images instead of commit or status icons in the <em>Search Commits</em> view.</td>
</tr>
</tbody>
</table>

***

## File Blame Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.blame.avatars</code></td>
<td>Shows avatar images in file blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.compact</code></td>
<td>Compacts (deduplicates) adjacent matching blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.dateFormat</code></td>
<td>Formats absolute dates (e.g., using <code>${date}</code>) in blame annotations. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js documentation</a> for valid formats.</td>
</tr>
<tr>
<td><code>gitlens.blame.format</code></td>
<td>Specifies the display format of blame annotations. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>. Date format is controlled by <code>gitlens.blame.dateFormat</code>.</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.enabled</code></td>
<td>Enables a heatmap indicator in blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.location</code></td>
<td>Determines heatmap indicator placement:<br><br><code>left</code> – left edge of annotations<br><code>right</code> – right edge of annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.enabled</code></td>
<td>Highlights lines related to the current line.</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.locations</code></td>
<td>Specifies where highlights appear:<br><br><code>file</code> – file indicator<br><code>line</code> – full-line background highlight<br><code>overview</code> – decoration in the overview ruler</td>
</tr>
<tr>
<td><code>gitlens.blame.ignoreWhitespace</code></td>
<td>Ignores whitespace differences when comparing revisions during blame operations.</td>
</tr>
<tr>
<td><code>gitlens.blame.separateLines</code></td>
<td>Shows line separators in blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.toggleMode</code></td>
<td>Determines toggle scope:<br><br><code>file</code> – toggles blame per file<br><code>window</code> – toggles blame for all files in the window</td>
</tr>
<tr>
<td><code>gitlens.blame.fontFamily</code></td>
<td>Sets font family for file blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.fontSize</code></td>
<td>Sets font size for file blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.fontWeight</code></td>
<td>Sets font weight for file blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.fontStyle</code></td>
<td>Sets font style for file blame annotations.</td>
</tr>
</tbody>
</table>

***

## File Changes Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.changes.locations</code></td>
<td>Controls where file changes indicators appear:<br><br><code>gutter</code> – shows a file indicator in the gutter<br><code>overview</code> – adds a decoration in the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.changes.toggleMode</code></td>
<td>Determines toggle scope for file changes annotations:<br><br><code>file</code> – toggles annotations per file<br><code>window</code> – toggles annotations for all files in the window</td>
</tr>
</tbody>
</table>

***

## File Heatmap Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.heatmap.ageThreshold</code></td>
<td>Defines the age threshold in days for heatmap coloring. Changes older than this use <code>gitlens.heatmap.coldColor</code>, newer changes use <code>gitlens.heatmap.hotColor</code>.</td>
</tr>
<tr>
<td><code>gitlens.heatmap.coldColor</code></td>
<td>Base color for file heatmap annotations when changes are older than the age threshold (cold).</td>
</tr>
<tr>
<td><code>gitlens.heatmap.hotColor</code></td>
<td>Base color for file heatmap annotations when changes are newer than the age threshold (hot).</td>
</tr>
<tr>
<td><code>gitlens.heatmap.locations</code></td>
<td>Specifies where heatmap indicators appear:<br><br><code>gutter</code> – shows indicator in the gutter<br><code>overview</code> – adds a decoration in the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.heatmap.toggleMode</code></td>
<td>Determines toggle scope for file heatmap annotations:<br><br><code>file</code> – toggles annotations per file<br><code>window</code> – toggles annotations for all files in the window</td>
</tr>
</tbody>
</table>

***

## Git Command Palette Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.gitCommands.closeOnFocusOut</code></td>
<td>Determines whether the <em>Git Commands Palette</em> dismisses automatically when focus is lost. If disabled, press <kbd>ESC</kbd> to dismiss manually.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchAll</code></td>
<td>Controls whether commit message searches match all patterns or any pattern.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchCase</code></td>
<td>Enables case-sensitive matching for commit message searches.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchRegex</code></td>
<td>Enables regular expression matching for commit message searches.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.showResultsInSideBar</code></td>
<td>Controls where commit search results display: in the quick pick menu, the Side Bar, or context-dependent.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.skipConfirmations</code></td>
<td>Specifies which Git commands skip confirmation prompts. Format: <code>git-command-name:(menu/command)</code>.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.sortBy</code></td>
<td>Specifies sorting order of commands in the <em>Git Command Palette</em>:<br><br><code>name</code> – alphabetically by command name<br><code>usage</code> – by last used date</td>
</tr>
</tbody>
</table>

***

## Terminal Links Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.terminalLinks.enabled</code></td>
<td>Enables terminal links—autolinks in the integrated terminal that provide quick access to details for commits, branches, tags, and more.</td>
</tr>
</tbody>
</table>

***

## Remote Provider Integration Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.integrations.enabled</code></td>
<td>Enables rich integrations with supported remote services.</td>
</tr>
<tr>
<td><code>gitlens.remotes</code></td>
<td>Defines custom remote services to match Git remotes for detecting custom domains or supporting additional remote services.<br><br>Supported types include:<br>
<ul>
<li>GitHub</li>
<li>GitLab</li>
<li>Gerrit</li>
<li>GoogleSource</li>
<li>Gitea</li>
<li>AzureDevOps</li>
<li>Bitbucket</li>
<li>BitbucketServer</li>
<li>Custom</li>
</ul>
Examples:<br>
<pre><code>\"gitlens.remotes\": [{ \"domain\": \"git.corporate-url.com\", \"type\": \"GitHub\" }]</code></pre>
<pre><code>\"gitlens.remotes\": [{ \"regex\": \"ssh:\\/\\/(my\\.company\\.com):1234\\/git\\/(.+)\", \"type\": \"GitHub\" }]</code></pre>
Custom example:<br>
<pre><code>\"gitlens.remotes\": [{
  \"domain\": \"git.corporate-url.com\",
  \"type\": \"Custom\",
  \"name\": \"My Company\",
  \"protocol\": \"https\",
  \"urls\": {
    \"repository\": \"https://git.corporate-url.com/${repo}\",
    \"branches\": \"https://git.corporate-url.com/${repo}/branches\",
    \"branch\": \"https://git.corporate-url.com/${repo}/commits/${branch}\",
    \"commit\": \"https://git.corporate-url.com/${repo}/commit/${id}\",
    \"file\": \"https://git.corporate-url.com/${repo}?path=${file}${line}\",
    \"fileInBranch\": \"https://git.corporate-url.com/${repo}/blob/${branch}/${file}${line}\",
    \"fileInCommit\": \"https://git.corporate-url.com/${repo}/blob/${id}/${file}${line}\",
    \"fileLine\": \"#L${line}\",
    \"fileRange\": \"#L${start}-L${end}\"
  }
}]</code></pre>
Another custom example:<br>
<pre><code>\"gitlens.remotes\": [{
  \"regex\": \"ssh:\\/\\/(my\\.company\\.com):1234\\/git\\/(.+)\",
  \"type\": \"Custom\",
  \"name\": \"My Company\",
  \"protocol\": \"https\",
  \"urls\": {
    \"repository\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}\",
    \"branches\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}/branches\",
    \"branch\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}/commits/${branch}\",
    \"commit\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}/commit/${id}\",
    \"file\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}?path=${file}${line}\",
    \"fileInBranch\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}/blob/${branch}/${file}${line}\",
    \"fileInCommit\": \"https://my.company.com/projects/${repoBase}/repos/${repoPath}/blob/${id}/${file}${line}\",
    \"fileLine\": \"#L${line}\",
    \"fileRange\": \"#L${start}-L${end}\"
  }
}]</code></pre>
</td>
</tr>
</tbody>
</table>

***

## Date & Time Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.defaultDateFormat</code></td>
<td>Specifies the default format for absolute dates. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js documentation</a> for valid format strings.</td>
</tr>
<tr>
<td><code>gitlens.defaultDateLocale</code></td>
<td>Specifies the locale for date formatting, using a <a href="https://en.wikipedia.org/wiki/IETF_language_tag#List_of_major_primary_language_subtags" rel="nofollow">BCP 47 language tag</a>. Defaults to the VS Code locale. Use <code>system</code> to follow the current system locale or specify a locale like <code>en-US</code> (US English), <code>en-GB</code> (British English), <code>de-DE</code> (German), <code>ja-JP</code> (Japanese), etc.</td>
</tr>
<tr>
<td><code>gitlens.defaultDateShortFormat</code></td>
<td>Specifies the default format for short absolute dates. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js documentation</a> for valid format strings.</td>
</tr>
<tr>
<td><code>gitlens.defaultDateSource</code></td>
<td>Determines whether commit dates use the authored date or the committed date.</td>
</tr>
<tr>
<td><code>gitlens.defaultDateStyle</code></td>
<td>Specifies the default display style for dates.</td>
</tr>
<tr>
<td><code>gitlens.defaultTimeFormat</code></td>
<td>Specifies the default format for times. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js documentation</a> for valid format strings.</td>
</tr>
</tbody>
</table>

***

## Menu & Toolbar Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.menus</code></td>
<td>Defines which commands are added to specific menus.</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.command</code></td>
<td>Controls the behavior of the file annotations button in the editor title:<br><br>
<code>null</code> (default) – shows a menu to select which file annotations to toggle<br>
<code>blame</code> – toggles file blame annotations<br>
<code>heatmap</code> – toggles file heatmap annotations<br>
<code>changes</code> – toggles file changes annotations
</td>
</tr>
</tbody>
</table>

***

## Keyboard Shortcut Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.keymap</code></td>
<td>Specifies the keymap used for GitLens shortcuts:<br><br>
<code>alternate</code> – adds alternate shortcuts starting with <kbd>Alt</kbd> (⌥ on macOS)<br>
<code>chorded</code> – adds chorded shortcuts starting with <kbd>Ctrl+Shift+G</kbd> (⌥⌘G on macOS)<br>
<code>none</code> – disables all GitLens shortcut keys
</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.dismissOnEscape</code></td>
<td>Determines whether pressing <kbd>ESC</kbd> dismisses active file annotations.</td>
</tr>
</tbody>
</table>

***

## Modes Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.mode.active</code></td>
<td>Specifies the currently active GitLens mode, if any.</td>
</tr>
<tr>
<td><code>gitlens.mode.statusBar.enabled</code></td>
<td>Enables display of the active GitLens mode in the status bar.</td>
</tr>
<tr>
<td><code>gitlens.mode.statusBar.alignment</code></td>
<td>Controls alignment of the active mode display in the status bar:<br><br>
<code>left</code> – aligns left<br>
<code>right</code> – aligns right</td>
</tr>
<tr>
<td><code>gitlens.modes</code></td>
<td>Defines user-configured GitLens modes.<br><br>Example: Add heatmap annotations to a <em>Reviewing</em> mode:<br>
<code>"gitlens.modes": { "review": { "annotations": "heatmap" } }</code><br><br>Example: Define a new <em>Annotating</em> mode with blame annotations:<br>
<pre><code>"gitlens.modes": {
  "annotate": {
    "name": "Annotating",
    "statusBarItemName": "Annotating",
    "description": "for root cause analysis",
    "annotations": "blame",
    "codeLens": false,
    "currentLine": false,
    "hovers": true
  }
}</code></pre>
</td>
</tr>
</tbody>
</table>

***

## Autolink Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.autolinks</code></td>
<td>Defines autolinks to external resources in commit messages. Use <code>&lt;num&gt;</code> as a placeholder for the reference number.<br><br>Example for Jira issues:<br>
<code>JIRA-123 ⟶ https://jira.company.com/issue?query=123</code><br>
<code>"gitlens.autolinks": [{ "prefix": "JIRA-", "url": "https://jira.company.com/issue?query=&lt;num&gt;" }]</code>
</td>
</tr>
</tbody>
</table>

***

## AI Settings - Preview

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.ai.enabled</code></td>
<td>Specifies whether to enable GitLens' AI-powered features<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.experimental.composer.enabled</code></td>
<td>Specifies whether to enable the experimental version of the commit composer<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.model</code></td>
<td>Specifies the AI provider and model to use for GitLens' AI features. Should be formatted as <code>provider:model</code>(e.g. <code>openai:gpt-4o</code> or <code>anthropic:claude-3-5-sonnet-latest</code>, <code>gitkraken</code> for GitKraken AI provided models, or <code>vscode</code> for models provided by the VS Code extension API (e.g. Copilot)"<br>
<code>vscode</code><br>
<code>openai:gpt-4</code><br>
<code>openai:gpt-4o</code><br>
<code>xai:grok-beta</code><br>
<code>openai:gpt-4-32k</code><br>
<code>anthropic:claude-2</code><br>
<code>openai:gpt-4-turbo</code><br>
<code>openai:gpt-4o-mini</code><br>
<code>anthropic:claude-2.1</code><br>
<code>openai:gpt-3.5-turbo</code><br>
<code>google:gemini-1.0-pro</code><br>
<code>openai:gpt-3.5-turbo-16k</code><br>
<code>anthropic:claude-instant-1</code><br>
<code>openai:gpt-4-turbo-preview</code><br>
<code>google:gemini-1.5-pro-latest</code><br>
<code>anthropic:claude-3-opus-latest</code><br>
<code>google:gemini-1.5-flash-latest</code><br>
<code>anthropic:claude-3-opus-20240229</code><br>
<code>anthropic:claude-3-haiku-20240307</code><br>
<code>anthropic:claude-3-5-sonnet-latest</code><br>
<code>anthropic:claude-3-sonnet-20240229</code><br>
<code>anthropic:claude-3-5-sonnet-20240620</code><br>
<code>anthropic:claude-3-5-sonnet-20241022</code>
</td>
</tr>
<tr>
<td><code>gitlens.ai.gitkraken.model</code></td>
<td>Specifies the AI provider and model to use for GitLens' AI features. Should be formatted as <code>provider:model</code>(e.g. <code>openai:gpt-4o</code> or <code>anthropic:claude-3-5-sonnet-latest</code>, <code>gitkraken</code> for GitKraken AI provided models, or <code>vscode</code> for models provided by the VS Code extension API (e.g. Copilot)"<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.vscode.model</code></td>
<td>Specifies the VS Code provided model to use for GitLens' AI features, formatted as <code>provider:model</code><br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.ollama.url</code></td>
<td>Specifies the Ollama URL to use for access<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.openai.url</code></td>
<td>Specifies a custom URL to use for access to an OpenAI model.<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.azure.url</code></td>
<td>Specifies a custom URL to use for access to an Azure OpenAI model. Azure URLs should be in the following format: https://{your-resource-name}.openai.azure.com/openai/deployments/{deployment-id}/chat/completions?api-version={api-version}<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.openaicompatible.url</code></td>
<td>Specifies a custom URL to use for access to an OpenAI-compatible model.<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.largePromptWarningThreshold</code></td>
<td>Specifies the threshold (in tokens) for when to show a warning about the prompt being too large<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.modelOptions.temperature</code></td>
<td>Specifies the temperature, a measure of output randomness, to use for the AI model. Higher values result in more randomness, e.g. creativity, while lower values are more deterministic<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.explainChanges.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a summary of changes<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateChangelog.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a changelog from a set of changes<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCommits.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating commits<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateStashMessage.customInstruction</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a stash message<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCreateCloudPatch.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a cloud patch title and description<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCreateCodeSuggest.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a code suggest title and description<br>
</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCreatePullRequest.customInstructions</code></td>
<td>Specifies custom instructions to provide to the AI provider when generating a pull request title and description<br>
</td>
</tr>
</tbody>
</table>


***

## Misc Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.defaultGravatarsStyle</code></td>
<td>Specifies the style of default (fallback) gravatar images:<br><br>
<code>identicon</code> – geometric pattern<br>
<code>mp</code> – cartoon-style silhouette (same for all emails)<br>
<code>monsterid</code> – colorful monster faces<br>
<code>retro</code> – 8-bit pixelated faces<br>
<code>robohash</code> – robot faces with variations<br>
<code>wavatar</code> – faces with different features and backgrounds
</td>
</tr>
<tr>
<td><code>gitlens.liveshare.allowGuestAccess</code></td>
<td>Allows guest access to GitLens features during Visual Studio Live Share sessions.</td>
</tr>
<tr>
<td><code>gitlens.outputLevel</code></td>
<td>Controls the verbosity of output sent to the GitLens output channel.</td>
</tr>
<tr>
<td><code>gitlens.showWelcomeOnInstall</code></td>
<td>Shows the Welcome (Quick Setup) experience on first install.</td>
</tr>
<tr>
<td><code>gitlens.showWhatsNewAfterUpgrades</code></td>
<td>Shows the What's New notification after upgrading to new feature releases.</td>
</tr>
<tr>
<td><code>gitlens.sortBranchesBy</code></td>
<td>Determines how branches are sorted in quick pick menus and views.</td>
</tr>
<tr>
<td><code>gitlens.sortContributorsBy</code></td>
<td>Determines how contributors are sorted in quick pick menus and views.</td>
</tr>
<tr>
<td><code>gitlens.sortTagsBy</code></td>
<td>Determines how tags are sorted in quick pick menus and views.</td>
</tr>
<tr>
<td><code>gitlens.sortRepositoriesBy</code></td>
<td>Determines how repositories are sorted in quick pick menus and views.</td>
</tr>
<tr>
<td><code>gitlens.advanced.abbreviatedShaLength</code></td>
<td>Length of abbreviated commit SHAs.</td>
</tr>
<tr>
<td><code>gitlens.advanced.abbreviateShaOnCopy</code></td>
<td>Determines whether copied commit SHAs are abbreviated to the length of <code>gitlens.advanced.abbreviatedShaLength</code>.</td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.customArguments</code></td>
<td>Additional arguments to pass to the <code>git blame</code> command.</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.preserveWhileEditing</code></td>
<td>Allows file annotations on unsaved (dirty) files. The <code>gitlens.advanced.blame.delayAfterEdit</code> setting controls the delay before updating annotations, which applies only if the file size is under <code>gitlens.advanced.sizeThresholdAfterEdit</code> (default 5000 lines).</td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.delayAfterEdit</code></td>
<td>Time (milliseconds) to wait before re-blaming an unsaved document after an edit. Use 0 to wait indefinitely.</td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.sizeThresholdAfterEdit</code></td>
<td>Maximum document size (lines) to re-blame after an edit while still unsaved. Use 0 for no maximum.</td>
</tr>
<tr>
<td><code>gitlens.advanced.caching.enabled</code></td>
<td>Enables caching of git output (changing this is not recommended).</td>
</tr>
<tr>
<td><code>gitlens.advanced.commitOrdering</code></td>
<td>Ordering method for commits (default is reverse chronological by commit date):<br><br>
<code>date</code> – reverse chronological by commit timestamp<br>
<code>author-date</code> – reverse chronological by author timestamp<br>
<code>topo</code> – reverse chronological but avoids mixing multiple lines of history
</td>
</tr>
<tr>
<td><code>gitlens.advanced.externalDiffTool</code></td>
<td>Optional external diff tool for file comparisons (must be a configured <a href="https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftool" rel="nofollow">Git difftool</a>).</td>
</tr>
<tr>
<td><code>gitlens.advanced.externalDirectoryDiffTool</code></td>
<td>Optional external diff tool for directory comparisons (must be a configured <a href="https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftool" rel="nofollow">Git difftool</a>).</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryFollowsRenames</code></td>
<td>Enables following file history through renames, affecting how merge commits display.</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryShowAllBranches</code></td>
<td>Shows commits from all branches in file history views.</td>
</tr>
<tr>
<td><code>gitlens.advanced.maxListItems</code></td>
<td>Maximum number of items shown in lists. Use 0 for no limit.</td>
</tr>
<tr>
<td><code>gitlens.advanced.maxSearchItems</code></td>
<td>Maximum number of items shown in search results. Use 0 for no limit.</td>
</tr>
<tr>
<td><code>gitlens.advanced.messages</code></td>
<td>Specifies which messages to suppress.</td>
</tr>
<tr>
<td><code>gitlens.advanced.quickPick.closeOnFocusOut</code></td>
<td>Dismisses quick pick menus when focus is lost. If disabled, press <kbd>ESC</kbd> to dismiss manually.</td>
</tr>
<tr>
<td><code>gitlens.advanced.repositorySearchDepth</code></td>
<td>Depth (number of folders) to search for repositories.</td>
</tr>
<tr>
<td><code>gitlens.advanced.similarityThreshold</code></td>
<td>Percent similarity required for a deleted and added file pair to be considered a rename.</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.recentChangeAndAuthors</code></td>
<td>String shown in place of both <em>recent change</em> and <em>authors</em> CodeLens when there are unsaved changes.</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.recentChangeOnly</code></td>
<td>String shown in place of the <em>recent change</em> CodeLens when there are unsaved changes.</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.authorsOnly</code></td>
<td>String shown in place of the <em>authors</em> CodeLens when there are unsaved changes.</td>
</tr>
<tr>
<td><code>gitlens.worktrees.defaultLocation</code></td>
<td>Path variables:<br><br>
<code>${userHome}</code> – user's home directory<br>
<code>${workspaceFolder}</code> – path of the opened folder in VS Code containing the repository<br>
<code>${workspaceFolderBasename}</code> – name of the opened folder in VS Code without slashes
</td>
</tr>
<tr>
<td><code>gitlens.visualHistory.allowMultiple</code></td>
<td>Allows opening multiple Visual File History instances in the editor area.</td>
</tr>
<tr>
<td><code>gitlens.liveshare.enabled</code></td>
<td>Enables integration with Visual Studio Live Share.</td>
</tr>
<tr>
<td><code>multiDiffEditor.experimental.enabled</code></td>
<td>Enables VS Code's experimental multi-diff editor (requires VS Code 1.85+).</td>
</tr>
<tr>
<td><code>gitlens.views.openChangesInMultiDiffEditor</code></td>
<td>Controls whether to open multiple changes in VS Code's multi-diff editor (single tab) or individual diff editors (multiple tabs). Requires <code>multiDiffEditor.experimental.enabled</code> and VS Code 1.85+.</td>
</tr>
<tr>
<td><code>gitlens.experimental.cloudIntegrations.enabled</code></td>
<td>Enables GitHub integration via GitKraken account cloud integration.</td>
</tr>
</tbody>
</table>

***

## Themable Colors

GitLens defines a set of themable colors that can be provided by VS Code themes or customized by users via `workbench.colorCustomizations`.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.gutterBackgroundColor</code></td>
<td>Background color of file blame annotations in the gutter.</td>
</tr>
<tr>
<td><code>gitlens.gutterForegroundColor</code></td>
<td>Foreground color of file blame annotations in the gutter.</td>
</tr>
<tr>
<td><code>gitlens.gutterUncommittedForegroundColor</code></td>
<td>Foreground color for uncommitted lines in file blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.trailingLineBackgroundColor</code></td>
<td>Background color of trailing blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.trailingLineForegroundColor</code></td>
<td>Foreground color of trailing blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.lineHighlightBackgroundColor</code></td>
<td>Background color for associated line highlights in blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.lineHighlightOverviewRulerColor</code></td>
<td>Overview ruler color for associated line highlights in blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.focus.allowMultiple</code></td>
<td>Allows opening multiple instances of the Focus feature in the editor area.</td>
</tr>
</tbody>
</table>


***

## Commit Graph Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.graph.showUpstreamStatus</code></td>
<td>Enables or disables upstream (ahead/behind) indicators on branches.</td>
</tr>
<tr>
<td><code>gitlens.graph.pullRequests</code></td>
<td>Enables or disables pull request icons in the Commit Graph.</td>
</tr>
<tr>
<td><code>gitlens.graph.dimMergeCommits</code></td>
<td>Dims (deemphasizes) merge commit rows in the graph.</td>
</tr>
<tr>
<td><code>gitlens.graph.scrollRowPadding</code></td>
<td>Number of rows from the edge at which the graph scrolls when changing the selected row via keyboard or search.</td>
</tr>
<tr>
<td><code>gitlens.graph.experimental.location</code></td>
<td>Location where the Commit Graph is shown:<br><br>
<code>tab</code> – in a tab in the editor area<br>
<code>view</code> – in the side bar, draggable to side bar, secondary side bar, or panel locations
</td>
</tr>
<tr>
<td><code>gitlens.graph.layout</code></td>
<td>Default layout for the Commit Graph. Options:<br><br>
<code>panel</code> (default) – shows in a panel<br>
<code>editor</code> – shows in the editor area.<br>
Honored when opening the Commit Graph from the command palette.
</td>
</tr>
<tr>
<td><code>gitlens.graph.allowMultiple</code></td>
<td>Allows opening multiple Commit Graph instances in the editor area.</td>
</tr>
<tr>
<td><code>gitlens.graph.sidebar.enabled</code></td>
<td>Shows or hides the sidebar in the Commit Graph.</td>
</tr>
</tbody>
</table>

***

## Cloud Patches (Preview) Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.cloudPatches.enabled</code></td>
<td>Enables or disables Cloud Patches. Defaults to <code>true</code>.</td>
</tr>
</tbody>
</table>


***

## Launchpad Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.launchpad.ignoredRepositories</code></td>
<td>List of repositories (in <code>owner/name</code> format) to ignore in Launchpad.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.ignoredOrganizations</code></td>
<td>List of organizations or users to ignore in Launchpad.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.staleThreshold</code></td>
<td>Number of days after which a pull request is considered stale and moved to the "Other" category.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.enabled</code></td>
<td>Enables the Launchpad indicator in the status bar.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.icon</code></td>
<td>Style of the Launchpad indicator icon.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.label</code></td>
<td>Style of the Launchpad indicator label.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.groups</code></td>
<td>Critical pull request categories to summarize in the indicator tooltip.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.useColors</code></td>
<td>Enables color usage in the Launchpad indicator.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.openInEditor</code></td>
<td>Opens the Launchpad in the editor when the indicator is clicked.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.polling.enabled</code></td>
<td>Enables regular polling for pull request changes.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.polling.interval</code></td>
<td>Polling interval in minutes for checking pull request changes.</td>
</tr>
<tr>
<td><code>gitlens.views.launchpad.enabled</code></td>
<td>(Experimental) Enables the experimental Launchpad view.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.includedOrganizations</code></td>
<td>Organizations to include in Launchpad.</td>
</tr>
</tbody>
</table>
