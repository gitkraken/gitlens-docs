---

title: Settings
description: GitLens Settings
taxonomy:
    category: gitlens

---

<img src="/wp-content/uploads/settings.png" class="img-bordered img-responsive center">

GitLens provides a rich **interactive settings editor**, an easy-to-use interface, to configure many of GitLens' powerful features. It can be accessed via the _GitLens: Open Settings_ (`gitlens.showSettingsPage`) command from the [_Command Palette_](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

GitLens is highly customizable and provides many configuration settings to allow the personalization of almost all features.

##Current Line Blame Settings

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
<td>Specifies how to format absolute dates (e.g. using the <code>${date}</code> token) for the current line blame annotations. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
<tr>
<td><code>gitlens.currentLine.enabled</code></td>
<td>Specifies whether to provide a blame annotation for the current line, by default. Use the <em>Toggle Line Blame Annotations</em> command (<code>gitlens.toggleLineBlame</code>) to toggle the annotations on and off for the current window</td>
</tr>
<tr>
<td><code>gitlens.currentLine.format</code></td>
<td>Specifies the format of the current line blame annotation. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs. Date formatting is controlled by the <code>gitlens.currentLine.dateFormat</code> setting</td>
</tr>
<tr>
<td><code>gitlens.currentLine.pullRequests.enabled</code></td>
<td>Specifies whether to provide information about the Pull Request (if any) that introduced the commit in the current line blame annotation. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.currentLine.scrollable</code></td>
<td>Specifies whether the current line blame annotation can be scrolled into view when it is outside the viewport. <strong>NOTE</strong>: Setting this to <code>false</code> will inhibit the hovers from showing over the annotation; Set <code>gitlens.hovers.currentLine.over</code> to <code>line</code> to enable the hovers to show anywhere over the line.</td>
</tr>
<tr>
<td><code>gitlens.currentLine.uncommittedChangesFormat</code></td>
<td>Specifies the uncommitted changes format of the current line blame annotation. <strong>NOTE</strong>: Setting this to an empty string will disable current line blame annotations for uncommitted changes</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontFamily</code></td>
<td>Specifies the font family of the Inline Blame annotation</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontSize</code></td>
<td>Specifies the font size of the Inline Blame annotation</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontStyle</code></td>
<td>Specifies the font style of the Inline Blame annotation</td>
</tr>
<tr>
<td><code>gitlens.currentLine.fontWeight</code></td>
<td>Specifies the font weight of the Inline Blame annotation</td>
</tr>
</tbody>
</table>

***

##Git CodeLens Settings

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
<td>Specifies the command to be executed when an <em>authors</em> CodeLens is clicked, set to (<code>gitlens.toggleFileBlame</code>) by default. Can be set to <code>false</code> to disable click actions on the CodeLens.<br><br><code>gitlens.toggleFileBlame</code> - toggles file blame annotations<br><code>gitlens.toggleFileHeatmap</code> - toggles file heatmap<br><code>gitlens.toggleFileChanges</code> - toggles file changes since before the commit<br><code>gitlens.toggleFileChangesOnly</code> - toggles file changes from the commit<br><code>gitlens.diffWithPrevious</code> - opens changes with the previous revision<br><code>gitlens.revealCommitInView</code> - reveals the commit in the Side Bar<br><code>gitlens.showCommitsInView</code> - searches for commits within the range<br><code>gitlens.showQuickCommitDetails</code> - shows details of the commit<br><code>gitlens.showQuickCommitFileDetails</code> - show file details of the commit<br><code>gitlens.showQuickFileHistory</code> - shows the current file history<br><code>gitlens.showQuickRepoHistory</code> - shows the current branch history<br><code>gitlens.openCommitOnRemote</code> - opens the commit on the remote service (when available)<br><code>gitlens.copyRemoteCommitUrl</code> - copies the remote commit url to the clipboard (when available)<br><code>gitlens.openFileOnRemote</code> - opens the file revision on the remote service (when available)<br><code>gitlens.copyRemoteFileUrl</code> - copies the remote file url to the clipboard (when available)</td>
</tr>
<tr>
<td><code>gitlens.codeLens.authors.enabled</code></td>
<td>Specifies whether to provide an <em>authors</em> CodeLens, showing number of authors of the file or code block and the most prominent author (if there is more than one)</td>
</tr>
<tr>
<td><code>gitlens.codeLens.enabled</code></td>
<td>Specifies whether to provide any Git CodeLens, by default. Use the <em>Toggle Git CodeLens</em> command (<code>gitlens.toggleCodeLens</code>) to toggle the Git CodeLens on and off for the current window</td>
</tr>
<tr>
<td><code>gitlens.codeLens.includeSingleLineSymbols</code></td>
<td>Specifies whether to provide any Git CodeLens on symbols that span only a single line</td>
</tr>
<tr>
<td><code>gitlens.codeLens.recentChange.command</code></td>
<td>Specifies the command to be executed when a <em>recent change</em> CodeLens is clicked, set to (<code>gitlens.showQuickCommitFileDetails</code>) by default. Can be set to <code>false</code> to disable click actions on the CodeLens.<br><br><code>gitlens.toggleFileBlame</code> - toggles file blame annotations<br><code>gitlens.toggleFileHeatmap</code> - toggles file heatmap<br><code>gitlens.toggleFileChanges</code> - toggles file changes since before the commit<br><code>gitlens.toggleFileChangesOnly</code> - toggles file changes from the commit<br><code>gitlens.diffWithPrevious</code> - opens changes with the previous revision<br><code>gitlens.revealCommitInView</code> - reveals the commit in the Side Bar<br><code>gitlens.showCommitsInView</code> - searches for commits within the range<br><code>gitlens.showQuickCommitDetails</code> - shows details of the commit<br><code>gitlens.showQuickCommitFileDetails</code> - show file details of the commit<br><code>gitlens.showQuickFileHistory</code> - shows the current file history<br><code>gitlens.showQuickRepoHistory</code> - shows the current branch history<br><code>gitlens.openCommitOnRemote</code> - opens the commit on the remote service (when available)<br><code>gitlens.copyRemoteCommitUrl</code> - copies the remote commit url to the clipboard (when available)<br><code>gitlens.openFileOnRemote</code> - opens the file revision on the remote service (when available)<br><code>gitlens.copyRemoteFileUrl</code> - copies the remote file url to the clipboard (when available)</td>
</tr>
<tr>
<td><code>gitlens.codeLens.recentChange.enabled</code></td>
<td>Specifies whether to provide a <em>recent change</em> CodeLens, showing the author and date of the most recent commit for the file or code block</td>
</tr>
<tr>
<td><code>gitlens.codeLens.scopes</code></td>
<td>Specifies where Git CodeLens will be shown in the document<br><br><code>document</code> - adds CodeLens at the top of the document<br><code>containers</code> - adds CodeLens at the start of container-like symbols (modules, classes, interfaces, etc)<br><code>blocks</code> - adds CodeLens at the start of block-like symbols (functions, methods, etc) lines</td>
</tr>
<tr>
<td><code>gitlens.codeLens.symbolScopes</code></td>
<td>Specifies a set of document symbols where Git CodeLens will or will not be shown in the document. Prefix with <code>!</code> to avoid providing a Git CodeLens for the symbol. Must be a member of <a href="https://code.visualstudio.com/docs/extensionAPI/vscode-api#_a-namesymbolkindaspan-classcodeitem-id660symbolkindspan" rel="nofollow"><code>SymbolKind</code></a></td>
</tr>
</tbody>
</table>

***

##Status Bar Settings

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
<td>Specifies the blame alignment in the status bar<br><br><code>left</code> - aligns to the left<br><code>right</code> - aligns to the right</td>
</tr>
<tr>
<td><code>gitlens.statusBar.command</code></td>
<td>Specifies the command to be executed when the blame status bar item is clicked<br><br><code>gitlens.toggleFileBlame</code> - toggles file blame annotations<br><code>gitlens.toggleFileHeatmap</code> - toggles file heatmap<br><code>gitlens.toggleFileChanges</code> - toggles file changes since before the commit<br><code>gitlens.toggleFileChangesOnly</code> - toggles file changes from the commit<br><code>gitlens.diffWithPrevious</code> - opens changes with the previous revision<br><code>gitlens.revealCommitInView</code> - reveals the commit in the Side Bar<br><code>gitlens.showCommitsInView</code> - searches for commits within the range<br><code>gitlens.showQuickCommitDetails</code> - shows details of the commit<br><code>gitlens.showQuickCommitFileDetails</code> - show file details of the commit<br><code>gitlens.showQuickFileHistory</code> - shows the current file history<br><code>gitlens.showQuickRepoHistory</code> - shows the current branch history<br><code>gitlens.openCommitOnRemote</code> - opens the commit on the remote service (when available)<br><code>gitlens.copyRemoteCommitUrl</code> - copies the remote commit url to the clipboard (when available)<br><code>gitlens.openFileOnRemote</code> - opens the file revision on the remote service (when available)<br><code>gitlens.copyRemoteFileUrl</code> - copies the remote file url to the clipboard (when available)</td>
</tr>
<tr>
<td><code>gitlens.statusBar.dateFormat</code></td>
<td>Specifies how to format absolute dates (e.g. using the <code>${date}</code> token) in the blame information in the status bar. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
<tr>
<td><code>gitlens.statusBar.enabled</code></td>
<td>Specifies whether to provide blame information in the status bar</td>
</tr>
<tr>
<td><code>gitlens.statusBar.format</code></td>
<td>Specifies the format of the blame information in the status bar. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs. Date formatting is controlled by the <code>gitlens.statusBar.dateFormat</code> setting</td>
</tr>
<tr>
<td><code>gitlens.statusBar.pullRequests.enabled</code></td>
<td>Specifies whether to provide information about the Pull Request (if any) that introduced the commit in the status bar. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.statusBar.reduceFlicker</code></td>
<td>Specifies whether to avoid clearing the previous blame information when changing lines to reduce status bar "flashing"</td>
</tr>
<tr>
<td><code>gitlens.statusBar.tooltipFormat</code></td>
<td>Specifies the format (in markdown) of hover shown over the blame information in the status bar. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
</tbody>
</table>
***

##Hover Settings

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
<td>Specifies whether to provide a <em>changes (diff)</em> hover for all lines when showing blame annotations</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.details</code></td>
<td>Specifies whether to provide a <em>commit details</em> hover for all lines when showing blame annotations</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.enabled</code></td>
<td>Specifies whether to provide any hovers when showing blame annotations</td>
</tr>
<tr>
<td><code>gitlens.hovers.annotations.over</code></td>
<td>Specifies when to trigger hovers when showing blame annotations<br><br><code>annotation</code> - only shown when hovering over the line annotation<br><code>line</code> - shown when hovering anywhere over the line</td>
</tr>
<tr>
<td><code>gitlens.hovers.avatars</code></td>
<td>Specifies whether to show avatar images in hovers</td>
</tr>
<tr>
<td><code>gitlens.hovers.avatarSize</code></td>
<td>Specifies the size of the avatar images in hovers</td>
</tr>
<tr>
<td><code>gitlens.hovers.changesDiff</code></td>
<td>Specifies whether to show just the changes to the line or the set of related changes in the <em>changes (diff)</em> hover<br><br><code>line</code> - Shows only the changes to the line<br><code>hunk</code> - Shows the set of related changes</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.changes</code></td>
<td>Specifies whether to provide a <em>changes (diff)</em> hover for the current line</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.details</code></td>
<td>Specifies whether to provide a <em>commit details</em> hover for the current line</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.enabled</code></td>
<td>Specifies whether to provide any hovers for the current line</td>
</tr>
<tr>
<td><code>gitlens.hovers.currentLine.over</code></td>
<td>Specifies when to trigger hovers for the current line<br><br><code>annotation</code> - only shown when hovering over the line annotation<br><code>line</code> - shown when hovering anywhere over the line</td>
</tr>
<tr>
<td><code>gitlens.hovers.detailsMarkdownFormat</code></td>
<td>Specifies the format (in markdown) of the <em>commit details</em> hover. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.hovers.enabled</code></td>
<td>Specifies whether to provide any hovers</td>
</tr>
<tr>
<td><code>gitlens.hovers.autolinks.enabled</code></td>
<td>Specifies whether to automatically link external resources in commit messages</td>
</tr>
<tr>
<td><code>gitlens.hovers.autolinks.enhanced</code></td>
<td>Specifies whether to lookup additional details about automatically link external resources in commit messages. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.hovers.pullRequests.enabled</code></td>
<td>Specifies whether to provide information about the Pull Request (if any) that introduced the commit in the hovers. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
</tbody>
</table>
***

##View Settings

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
<td>Specifies the default number of items to show in a view list. Use 0 to specify no limit</td>
</tr>
<tr>
<td><code>gitlens.views.formats.commits.label</code></td>
<td>Specifies the format of commits in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.commits.description</code></td>
<td>Specifies the description format of commits in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.label</code></td>
<td>Specifies the format of a file in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.description</code></td>
<td>Specifies the description format of a file in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.label</code></td>
<td>Specifies the format of stashes in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.description</code></td>
<td>Specifies the description format of stashes in the views. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.tooltip</code></td>
<td>Specifies the tooltip format of the stashes in GitLens views</td>
</tr>
<tr>
<td><code>gitlens.views.pageItemLimit</code></td>
<td>Specifies the number of items to show in a each page when paginating a view list. Use 0 to specify no limit</td>
</tr>
<tr>
<td><code>gitlens.views.showRelativeDateMarkers</code></td>
<td>Specifies whether to show relative date markers (<em>Less than a week ago</em>, <em>Over a week ago</em>, <em>Over a month ago</em>, etc) on revision (commit) histories in the views</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.icon</code></td>
<td>Specifies how the Commits view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.icon</code></td>
<td>Specifies how the Repositories view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.icon</code></td>
<td>Specifies how the Branches view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.label</code></td>
<td>Specifies how the Remotes view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.icon</code></td>
<td>Specifies how the Stashes view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.icon</code></td>
<td>Specifies how the Tags view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.icon</code></td>
<td>Specifies how the Worktrees view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.icon</code></td>
<td>Specifies how the Contributors view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.files.icon</code></td>
<td>Specifies how the Search & Compare view will display file icons</td>
</tr>
<tr>
<td><code>gitlens.views.collapseWorktreesWhenPossible</code></td>
<td>Specifies whether to try to collapse the opened worktrees into a single (common) repository in the views when possible</td>
</tr>
<tr>
<td><code>Gitlens.views.showCurrentBranchOnTo</code></td>
<td>Specifies whether the current branch is shown at the top of the views</td>
</tr>
</tbody>
</table>

***

##Commits View Settings

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
<td><code>gitlens.views.commits.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Commits</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Commits</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.layout</code></td>
<td>Specifies how the <em>Commits</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.commits.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Commits</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.enabled</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Commits</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.showForBranches</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Commits</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.commits.pullRequests.showForCommits</code></td>
<td>Specifies whether to show pull requests (if any) associated with the current branch in the <em>Commits</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.commits.reveal</code></td>
<td>Specifies whether to reveal commits in the <em>Commits</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.commits.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of the current branch or the working tree with a user-selected reference (branch, tag. etc) in the <em>Commits</em> view<br><br><code>false</code> - hides the branch comparison<br><code>branch</code> - compares the current branch with a user-selected reference<br><code>working</code> - compares the working tree with a user-selected reference</td>
</tr>
</tbody>
</table>
***

##Repositories View Settings

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
<td><code>gitlens.views.repositories.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.autoRefresh</code></td>
<td>Specifies whether to automatically refresh the <em>Repositories</em> view when the repository or the file system changes</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.autoReveal</code></td>
<td>Specifies whether to automatically reveal repositories in the <em>Repositories</em> view when opening files</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.branches.layout</code></td>
<td>Specifies how the <em>Repositories</em> view will display branches<br><br><code>list</code> - displays branches as a list<br><code>tree</code> - displays branches as a tree when branch names contain slashes <code>/</code></td>
</tr>
<tr>
<td><code>gitlens.views.repositories.branches.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of the branch with a user-selected reference (branch, tag. etc) under each branch in the <em>Repositories</em> view view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.compact</code></td>
<td>Specifies whether to show the <em>Repositories</em> view in a compact display density</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Repositories</em> view. Only applies when <code>gitlens.views.repositories.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.layout</code></td>
<td>Specifies how the <em>Repositories</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.repositories.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Repositories</em> view. Only applies when <code>gitlens.views.repositories.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.repositories.includeWorkingTree</code></td>
<td>Specifies whether to include working tree file status for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of a user-selected reference (branch, tag. etc) to the current branch or the working tree in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showBranches</code></td>
<td>Specifies whether to show the branches for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>itlens.views.repositories.showCommits</code></td>
<td>Specifies whether to show the commits on the current branch for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showContributors</code></td>
<td>Specifies whether to show the contributors for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showIncomingActivity</code></td>
<td>Specifies whether to show the experimental incoming activity for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showRemotes</code></td>
<td>Specifies whether to show the remotes for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showStashes</code></td>
<td>Specifies whether to show the stashes for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showTags</code></td>
<td>Specifies whether to show the tags for each repository in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.repositories.showUpstreamStatus</code></td>
<td>Specifies whether to show the upstream status of the current branch for each repository in the <em>Repositories</em> view</td>
</tr>
</tbody>
</table>
***

##File History View Settings

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
<td><code>gitlens.views.fileHistory.avatars</code></td>
<td>Specifies whether to show avatar images instead of status icons in the <em>File History</em> view</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryShowMergeCommits</code></td>
<td>Specifies whether to <code>show</code> or <code>hide</code> merge commits in file histories</td>
</tr>
</tbody>
</table>

***

##Line History View Settings

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
<td><code>gitlens.views.lineHistory.avatars</code></td>
<td>Specifies whether to show avatar images instead of status icons in the <em>Line History</em> view</td>
</tr>
</tbody>
</table>
***

##Branch View Settings

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
<td><code>gitlens.views.branches.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Branches</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.branches.branches.layout</code></td>
<td>Specifies how the <em>Branches</em> view will display branches<br><br><code>list</code> - displays branches as a list<br><code>tree</code> - displays branches as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Branches</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.layout</code></td>
<td>Specifies how the <em>Branches</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Branches</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.enabled</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Branches</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.showForBranches</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Branches</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.branches.pullRequests.showForCommits</code></td>
<td>Specifies whether to show pull requests (if any) associated with the current branch in the <em>Branches</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.branches.reveal</code></td>
<td>Specifies whether to reveal branches in the <em>Branches</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.branches.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of the branch with a user-selected reference (branch, tag. etc) in the <em>Branches</em> view<br><br><code>false</code> - hides the branch comparison<br><code>branch</code> - compares the current branch with a user-selected reference</td>
</tr>
</tbody>
</table>
***

##Remotes View Settings

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
<td><code>gitlens.views.remotes.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Remotes</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.branches.layout</code></td>
<td>Specifies how the <em>Remotes</em> view will display branches<br><br><code>list</code> - displays branches as a list<br><code>tree</code> - displays branches as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Remotes</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.layout</code></td>
<td>Specifies how the <em>Remotes</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Remotes</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.enabled</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Remotes</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.showForBranches</code></td>
<td>Specifies whether to query for pull requests associated with the current branch and commits in the <em>Remotes</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.pullRequests.showForCommits</code></td>
<td>Specifies whether to show pull requests (if any) associated with the current branch in the <em>Remotes</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.reveal</code></td>
<td>Specifies whether to reveal remotes in the <em>Remotes</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of the branch with a user-selected reference (branch, tag. etc) in the <em>Remotes</em> view<br><br><code>false</code> - hides the branch comparison<br><code>branch</code> - compares the current branch with a user-selected reference</td>
</tr>
</tbody>
</table>
***

##Stashes View Settings

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
<td><code>gitlens.views.stashes.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Stashes</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.layout</code></td>
<td>Specifies how the <em>Stashes</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.stashes.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Stashes</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.stashes.reveal</code></td>
<td>Specifies whether to reveal stashes in the <em>Stashes</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
</tbody>
</table>
***

##Tags View Settings

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
<td><code>gitlens.views.tags.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Tags</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.tags.branches.layout</code></td>
<td>Specifies how the <em>Tags</em> view will display tags<br><br><code>list</code> - displays tags as a list<br><code>tree</code> - displays tags as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Tags</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.layout</code></td>
<td>Specifies how the <em>Tags</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Tags</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.tags.reveal</code></td>
<td>Specifies whether to reveal tags in the <em>Tags</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
</tbody>
</table>
***

##Worktrees View Settings

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
<td><code>gitlens.views.worktrees.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Worktrees</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Worktrees</em> view.<br />Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.layout</code></td>
<td>Specifies how the <em>Worktrees</em> view will display files<br /><br />`auto` - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br />`list` - displays files as a list<br />`tree` - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Worktrees</em> view<br />Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.enabled</code></td>
<td>Specifies whether to query for pull requests associated with the worktree branch and commits in the <em>Worktrees</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.showForBranches</code></td>
<td>Specifies whether to query for pull requests associated with the worktree branch in the <em>Worktrees</em> view. Requires a connection to a supported remote service (e.g. GitHub) </td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.pullRequests.showForCommits</code></td>
<td>Specifies whether to show pull requests (if any) associated with commits in the <em>Worktrees</em> view. Requires a connection to a supported remote service (e.g. GitHub)</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.reveal</code></td>
<td>Specifies whether to reveal worktrees in the <em>Worktrees</em> view, otherwise they will be revealed in the <em>Repositories</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.worktrees.showBranchComparison</code></td>
<td>Specifies whether to show a comparison of the worktree branch with a user-selected reference (branch, tag. etc) in the <em>Worktrees</em> view<br /><br /><code>false</code> - hides the branch comparison<br /><code>branch</code> - compares the current branch with a user-selected reference</td>
</tr>
</tbody>
</table>
***

##Contributors View Settings

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
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Contributors</em> view.<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.layout</code></td>
<td>Specifies how the <em>Contributors</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.commits.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Contributors</em> view<br>Only applies when <code>gitlens.views.commits.files.layout</code> is set to <code>auto</code></td>
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

##Search & Compare View Settings

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
<td><code>gitlens.views.compare.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Search Commits</em> view<br>Only applies when <code>gitlens.views.compare.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.compare.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Compare</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.compare.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Compare</em> view. Only applies when <code>gitlens.views.compare.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.compare.files.layout</code></td>
<td>Specifies how the <em>Compare</em> view will display files<br><br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.compare.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.compare.files.threshold</code></td>
<td>Specifies when to switch between displaying files as a <code>tree</code> or <code>list</code> based on the number of files in a nesting level in the <em>Compare</em> view. Only applies when <code>gitlens.views.compare.files.layout</code> is set to <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.search.avatars</code></td>
<td>Specifies whether to show avatar images instead of commit (or status) icons in the <em>Search Commits</em> view</td>
</tr>
<tr>
<td><code>gitlens.views.search.files.compact</code></td>
<td>Specifies whether to compact (flatten) unnecessary file nesting in the <em>Search Commits</em> view<br>Only applies when <code>gitlens.views.compare.files.layout</code> is set to <code>tree</code> or <code>auto</code></td>
</tr>
<tr>
<td><code>gitlens.views.search.files.layout</code></td>
<td>Specifies how the <em>Search Commits</em> view will display files<br><code>auto</code> - automatically switches between displaying files as a <code>tree</code> or <code>list</code> based on the <code>gitlens.views.compare.files.threshold</code> value and the number of files at each nesting level<br><code>list</code> - displays files as a list<br><code>tree</code> - displays files as a tree</td>
</tr>
</tbody>
</table>
***

##File Blame Settings

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
<td>Specifies whether to show avatar images in the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.compact</code></td>
<td>Specifies whether to compact (deduplicate) matching adjacent file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.dateFormat</code></td>
<td>Specifies how to format absolute dates (e.g. using the <code>${date}</code> token) in file blame annotations. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
<tr>
<td><code>gitlens.blame.format</code></td>
<td>Specifies the format of the file blame annotations. See <a href="https://github.com/eamodio/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs. Date formatting is controlled by the <code>gitlens.blame.dateFormat</code> setting</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.enabled</code></td>
<td>Specifies whether to provide a heatmap indicator in the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.location</code></td>
<td>Specifies where the heatmap indicators will be shown in the file blame annotations<br><br><code>left</code> - adds a heatmap indicator on the left edge of the file blame annotations<br><code>right</code> - adds a heatmap indicator on the right edge of the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.enabled</code></td>
<td>Specifies whether to highlight lines associated with the current line</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.locations</code></td>
<td>Specifies where the associated line highlights will be shown<br><br><code>file</code> - adds a file indicator<br><code>line</code> - adds a full-line highlight background color<br><code>overview</code> - adds a decoration to the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.blame.ignoreWhitespace</code></td>
<td>Specifies whether to ignore whitespace when comparing revisions during blame operations</td>
</tr>
<tr>
<td><code>gitlens.blame.separateLines</code></td>
<td>Specifies whether file blame annotations will have line separators</td>
</tr>
<tr>
<td><code>gitlens.blame.toggleMode</code></td>
<td>Specifies how the file blame annotations will be toggled<br><br><code>file</code> - toggles each file individually<br><code>window</code> - toggles the window, i.e. all files at once</td>
</tr>
<tr>
<td><code>gitlens.blame.fontFamily</code></td>
<td>Specifies the font family of the File Blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.fontSize</code></td>
<td>Specifies the font size of the File Blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.fontWeight</code></td>
<td>Specifies the font weight of the File Blame annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.fontStyle</code></td>
<td>Specifies the font style of the File Blame annotations</td>
</tr>
</tbody>
</table>
***

##File Changes Settings

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
<td>Specifies where the indicators of the file changes annotations will be shown<br><br><code>gutter</code> - adds a file indicator<br><code>overview</code> - adds a decoration to the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.changes.toggleMode</code></td>
<td>Specifies how the file changes annotations will be toggled<br><br><code>file</code> - toggles each file individually<br><code>window</code> - toggles the window, i.e. all files at once</td>
</tr>
</tbody>
</table>
***

##File Heatmap Settings

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
<td>Specifies the age of the most recent change (in days) after which the file heatmap annotations will be cold rather than hot (i.e. will use <code>gitlens.heatmap.coldColor</code> instead of <code>gitlens.heatmap.hotColor</code>)</td>
</tr>
<tr>
<td><code>gitlens.heatmap.coldColor</code></td>
<td>Specifies the base color of the file heatmap annotations when the most recent change is older (cold) than the <code>gitlens.heatmap.ageThreshold</code> value</td>
</tr>
<tr>
<td><code>gitlens.heatmap.hotColor</code></td>
<td>Specifies the base color of the file heatmap annotations when the most recent change is newer (hot) than the <code>gitlens.heatmap.ageThreshold</code> value</td>
</tr>
<tr>
<td><code>gitlens.heatmap.locations</code></td>
<td>Specifies where the indicators of the file heatmap annotations will be shown<br><br><code>gutter</code> - adds a file indicator<br><code>overview</code> - adds a decoration to the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.heatmap.toggleMode</code></td>
<td>Specifies how the file heatmap annotations will be toggled<br><br><code>file</code> - toggles each file individually<br><code>window</code> - toggles the window, i.e. all files at once</td>
</tr>
</tbody>
</table>
***

##Git Command Palette Settings

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
<td>Specifies whether to dismiss the <em>Git Commands Palette</em> when focus is lost (if not, press <code>ESC</code> to dismiss)</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchAll</code></td>
<td>Specifies whether to match all or any commit message search patterns</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchCase</code></td>
<td>Specifies whether to match commit search patterns with or without regard to casing</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.matchRegex</code></td>
<td>Specifies whether to match commit search patterns using regular expressions</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.search.showResultsInSideBar</code></td>
<td>Specifies whether to show the commit search results directly in the quick pick menu, in the Side Bar, or will be based on the context</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.skipConfirmations</code></td>
<td>Specifies which (and when) Git commands will skip the confirmation step, using the format: <code>git-command-name:(menu/command)</code></td>
</tr>
<tr>
<td><code>gitlens.gitCommands.sortBy</code></td>
<td>Specifies how Git commands are sorted in the <em>Git Command Palette</em><br><br><code>name</code> - sorts commands by name<br><code>usage</code> - sorts commands by last used date</td>
</tr>
</tbody>
</table>
***

##Terminal Links Settings

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
<td>Specifies whether to enable terminal links — autolinks in the integrated terminal to quickly jump to more details for commits, branches, tags, and more</td>
</tr>
</tbody>
</table>
***

##Remote Provider Integration Settings

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
<td>Specifies whether to enable rich integrations with any supported remote services</td>
</tr>
<tr>
<td><code>gitlens.remotes</code></td>
<td>Specifies custom remote services to be matched with Git remotes to detect custom domains for built-in remote services or provide support for custom remote services<br><br>Supported Types (e.g. <code>"type": "GitHub"</code>):<ul dir="auto"><li>"GitHub"</li><li>"GitLab"</li><li>"Gerrit"</li><li>"GoogleSource"</li><li>"Gitea"</li><li>"AzureDevOps"</li><li>"Bitbucket"</li><li>"BitbucketServer"</li><li>"Custom"</li></ul>Example:<br><code>"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]</code><br><br>Example:<br><code>"gitlens.remotes": [{ "regex": "ssh:\/\/(my\.company\.com):1234\/git\/(.+)", "type": "GitHub" }]</code><br><br>Example:<br><code>"gitlens.remotes": [{</code><br>    <code>"domain": "git.corporate-url.com",</code><br>    <code>"type": "Custom",</code><br>    <code>"name": "My Company",</code><br>    <code>"protocol": "https",</code><br>    <code>"urls": {</code><br>        <code>"repository": "https://git.corporate-url.com/${repo}",</code><br>        <code>"branches": "https://git.corporate-url.com/${repo}/branches",</code><br>        <code>"branch": "https://git.corporate-url.com/${repo}/commits/${branch}",</code><br>        <code>"commit": "https://git.corporate-url.com/${repo}/commit/${id}",</code><br>        <code>"file": "https://git.corporate-url.com/${repo}?path=${file}${line}",</code><br>        <code>"fileInBranch": "https://git.corporate-url.com/${repo}/blob/${branch}/${file}${line}",</code><br>        <code>"fileInCommit": "https://git.corporate-url.com/${repo}/blob/${id}/${file}${line}",</code><br>        <code>"fileLine": "#L${line}",</code><br>        <code>"fileRange": "#L${start}-L${end}"</code><br>        <code>}</code><br>    <code>}]</code><br><br>Example:<br><code>"gitlens.remotes": [{</code><br>    <code>"regex": "ssh:\\/\\/(my\\.company\\.com):1234\\/git\\/(.+)",</code><br>    <code>"type": "Custom",</code><br>    <code>"name": "My Company",</code><br>    <code>"protocol": "https",</code><br>    <code>"urls": {</code><br>        <code>"repository": "https://my.company.com/projects/${repoBase}/repos/${repoPath}",</code><br>        <code>"branches": "https://my.company.com/projects/${repoBase}/repos/${repoPath}/branches",</code><br>        <code>"branch": "https://my.company.com/projects/${repoBase}/repos/${repoPath}/commits/${branch}",</code><br>        <code>"commit": "https://my.company.com/projects/${repoBase}/repos/${repoPath}/commit/${id}",</code><br>        <code>"file": "https://my.company.com/projects/${repoBase}/repos/${repoPath}?path=${file}${line}",</code><br>        <code>"fileInBranch": "https://my.company.com/projects/${repoBase}/repos/${repoPath}/blob/${branch}/${file}${line}",</code><br>        <code>"fileInCommit": "https://my.company.com/projects/${repoBase}/repos/${repoPath}/blob/${id}/${file}${line}",</code><br>        <code>"fileLine": "#L${line}",</code><br>        <code>"fileRange": "#L${start}-L${end}"</code><br>        <code>}</code><br>    <code>}]</code></td>
</tr>
</tbody>
</table>
***

##Date & Time Settings

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
<td>Specifies how absolute dates will be formatted by default. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
<tr>
<td><code>gitlens.defaultDateLocale</code></td>
<td>Specifies the locale, a [BCP 47 language tag](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_major_primary_language_subtags), to use for date formatting, defaults to the VS Code locale. Use <code>system</code> to follow the current system locale, or choose a specific locale, e.g <code>en-US</code> — US English, <code>en-GB</code> — British English, <code>de-DE</code> — German, <code>ja-JP</code> - Japanese, etc.</td>
</tr>
<tr>
<td><code>gitlens.defaultDateShortFormat</code></td>
<td>Specifies how short absolute dates will be formatted by default. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
<tr>
<td><code>gitlens.defaultDateSource</code></td>
<td>Specifies whether commit dates should use the authored or committed date</td>
</tr>
<tr>
<td><code>gitlens.defaultDateStyle</code></td>
<td>Specifies how dates will be displayed by default</td>
</tr>
<tr>
<td><code>gitlens.defaultTimeFormat</code></td>
<td>Specifies how times will be formatted by default. See the <a href="https://momentjs.com/docs/#/displaying/format/" rel="nofollow">Moment.js docs</a> for valid formats</td>
</tr>
</tbody>
</table>
***

##Menu & Toolbar Settings

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
<td>Specifies which commands will be added to which menus</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.command</code></td>
<td>Specifies whether the file annotations button in the editor title shows a menu or immediately toggles the specified file annotations<br><code>null</code> (default) - shows a menu to choose which file annotations to toggle<br><code>blame</code> - toggles file blame annotations<br><code>heatmap</code> - toggles file heatmap annotations<br><code>changes</code> - toggles file changes annotations</td>
</tr>
</tbody>
</table>
***

##Keyboard Shortcut Settings

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
<td>Specifies the keymap to use for GitLens shortcut keys<br><br><code>alternate</code> - adds an alternate set of shortcut keys that start with <code>Alt</code> (⌥ on macOS)<br><code>chorded</code> - adds a chorded set of shortcut keys that start with <code>Ctrl+Shift+G</code> (<code>⌥⌘G</code> on macOS)<br><code>none</code> - no shortcut keys will be added</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.dismissOnEscape</code></td>
<td>Specifies whether pressing the <code>ESC</code> key dismisses the active file annotations</td>
</tr>
</tbody>
</table>
***

##Modes Settings

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
<td>Specifies the active GitLens mode, if any</td>
</tr>
<tr>
<td><code>gitlens.mode.statusBar.enabled</code></td>
<td>Specifies whether to provide the active GitLens mode in the status bar</td>
</tr>
<tr>
<td><code>gitlens.mode.statusBar.alignment</code></td>
<td>Specifies the active GitLens mode alignment in the status bar<br><br><code>left</code> - aligns to the left<br><code>right</code> - aligns to the right</td>
</tr>
<tr>
<td><code>gitlens.modes</code></td>
<td>Specifies the user-defined GitLens modes<br><br>Example — adds heatmap annotations to the <em>Reviewing</em> mode<br><code>"gitlens.modes": { "review": { "annotations": "heatmap" } }</code><br><br>Example — adds a new <em>Annotating</em> mode with blame annotations<br><code>"gitlens.modes": {</code><br>    <code>"annotate": {</code><br>        <code>"name": "Annotating",</code><br>        <code>"statusBarItemName": "Annotating",</code><br>        <code>"description": "for root cause analysis",</code><br>        <code>"annotations": "blame",</code><br>        <code>"codeLens": false,</code><br>        <code>"currentLine": false,</code><br>        <code>"hovers": true</code><br>    <code>}</code><br><code>}</code></td>
</tr>
</tbody>
</table>
***

##Autolink Settings

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
<td>Specifies autolinks to external resources in commit messages. Use <code>&lt;num&gt;</code> as the variable for the reference number<br><br>Example to autolink Jira issues: (e.g. <code>JIRA-123 ⟶ https://jira.company.com/issue?query=123</code>)<br><code>"gitlens.autolinks": [{ "prefix": "JIRA-", "url": "https://jira.company.com/issue?query=&lt;num&gt;" }]</code></td>
</tr>
</tbody>
</table>
***

## Experimental AI Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.ai.experimental.model</code></td>
<td>Specifies the AI model to use</td>
</tr>
<tr>
<td><code>gitlens.ai.experimental.vscode.model</code></td>
<td>Specifies the VS Code extension-provided AI model to use when <code>gitlens.ai.experimental.model</code> is set to <code>vscode</code></td>
</tr>
<tr>
<td><code>gitlens.ai.experimental.generateCommitMessage.enabled</code></td>
<td>Specifies whether to enable GitLens’ experimental, AI-powered, on-demand commit message generation</code></td>
</tr>
<tr>
<td><code>gitlens.ai.experimental.openai.url</code></td>
<td>Specifies a custom URL to use for access to an OpenAI model via Azure. Azure URLs should be in the following format: https://{your-resource-name}.openai.azure.com/openai/deployments/{deployment-id}/chat/completions?api-version={api-version}</td>
</tr>
<tr>
<td><code>gitlens.experimental.generateCommitMessagePrompt</code></td>
<td>Specifies the prompt to use to tell the AI provider how to structure or format the generated commit message — can have fun with it and make your commit messages in the style of a pirate, etc</td>
</tr>
</tbody>
</table>

***

##Misc Settings

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
<td>Specifies the style of the gravatar default (fallback) images<br><br><code>identicon</code> - a geometric pattern<br><code>mp</code> - a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)<br><code>monsterid</code> - a monster with different colors, faces, etc<br><code>retro</code> - 8-bit arcade-style pixelated faces<br><code>robohash</code> - a robot with different colors, faces, etc<br><code>wavatar</code> - a face with differing features and backgrounds</td>
</tr>
<tr>
<td><code>gitlens.liveshare.allowGuestAccess</code></td>
<td>Specifies whether to allow guest access to GitLens features when using Visual Studio Live Share</td>
</tr>
<tr>
<td><code>gitlens.outputLevel</code></td>
<td>Specifies how much (if any) output will be sent to the GitLens output channel</td>
</tr>
<tr>
<td><code>gitlens.showWelcomeOnInstall</code></td>
<td>Specifies whether to show the Welcome (Quick Setup) experience on first install</td>
</tr>
<tr>
<td><code>gitlens.showWhatsNewAfterUpgrades</code></td>
<td>Specifies whether to show the What's New notification after upgrading to new feature releases</td>
</tr>
<tr>
<td><code>gitlens.sortBranchesBy</code></td>
<td>Specifies how branches are sorted in quick pick menus and views</td>
</tr>
<tr>
<td><code>gitlens.sortContributorsBy</code></td>
<td>Specifies how contributors are sorted in quick pick menus and views</td>
</tr>
<tr>
<td><code>gitlens.sortTagsBy</code></td>
<td>Specifies how tags are sorted in quick pick menus and views</td>
</tr>
<tr>
<td><code>gitlens.sortRepositoriesBy</code></td>
<td>Specifies how repositories are sorted in quick pick menus and views</td>
</tr>
<tr>
<td><code>gitlens.advanced.abbreviatedShaLength</code></td>
<td>Specifies the length of abbreviated commit SHAs (shas)</td>
</tr>
<tr>
<td><code>gitlens.advanced.abbreviateShaOnCopy</code></td>
<td>Specifies whether to copy full or abbreviated commit SHAs to the clipboard. Abbreviates to the length of <code>gitlens.advanced.abbreviatedShaLength</code></td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.customArguments</code></td>
<td>Specifies additional arguments to pass to the <code>git blame</code> command</td>
</tr>
<tr>
<td><code>gitlens.fileAnnotations.preserveWhileEditing</code></td>
<td>Specifies whether file annotations are allowed on files with unsaved changes (dirty). Use the <code>gitlens.advanced.blame.delayAfterEdit</code> setting to control how long to wait (defaults to 5s) before the annotation will update while the file is still dirty, which only applies if the file is under the <code>gitlens.advanced.sizeThresholdAfterEdit</code> setting threshold (defaults to 5000 lines)</td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.delayAfterEdit</code></td>
<td>Specifies the time (in milliseconds) to wait before re-blaming an unsaved document after an edit. Use 0 to specify an infinite wait</td>
</tr>
<tr>
<td><code>gitlens.advanced.blame.sizeThresholdAfterEdit</code></td>
<td>Specifies the maximum document size (in lines) allowed to be re-blamed after an edit while still unsaved. Use 0 to specify no maximum</td>
</tr>
<tr>
<td><code>gitlens.advanced.caching.enabled</code></td>
<td>Specifies whether git output will be cached — changing the default is not recommended</td>
</tr>
<tr>
<td><code>gitlens.advanced.commitOrdering</code></td>
<td>Specifies the order by which commits will be shown. If unspecified, commits will be shown in reverse chronological order<br><br><code>date</code> - shows commits in reverse chronological order of the commit timestamp<br><code>author-date</code> - shows commits in reverse chronological order of the author timestamp<br><code>topo</code> - shows commits in reverse chronological order of the commit timestamp, but avoids intermixing multiple lines of history</td>
</tr>
<tr>
<td><code>gitlens.advanced.externalDiffTool</code></td>
<td>Specifies an optional external diff tool to use when comparing files. Must be a configured <a href="https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftool" rel="nofollow">Git difftool</a>.</td>
</tr>
<tr>
<td><code>gitlens.advanced.externalDirectoryDiffTool</code></td>
<td>Specifies an optional external diff tool to use when comparing directories. Must be a configured <a href="https://git-scm.com/docs/git-config#Documentation/git-config.txt-difftool" rel="nofollow">Git difftool</a>.</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryFollowsRenames</code></td>
<td>Specifies whether file histories will follow renames -- will affect how merge commits are shown in histories</td>
</tr>
<tr>
<td><code>gitlens.advanced.fileHistoryShowAllBranches</code></td>
<td>Specifies whether file histories will show commits from all branches</td>
</tr>
<tr>
<td><code>gitlens.advanced.maxListItems</code></td>
<td>Specifies the maximum number of items to show in a list. Use 0 to specify no maximum</td>
</tr>
<tr>
<td><code>gitlens.advanced.maxSearchItems</code></td>
<td>Specifies the maximum number of items to show in a search. Use 0 to specify no maximum</td>
</tr>
<tr>
<td><code>gitlens.advanced.messages</code></td>
<td>Specifies which messages should be suppressed</td>
</tr>
<tr>
<td><code>gitlens.advanced.quickPick.closeOnFocusOut</code></td>
<td>Specifies whether to dismiss quick pick menus when focus is lost (if not, press <code>ESC</code> to dismiss)</td>
</tr>
<tr>
<td><code>gitlens.advanced.repositorySearchDepth</code></td>
<td>Specifies how many folders deep to search for repositories</td>
</tr>
<tr>
<td><code>gitlens.advanced.similarityThreshold</code></td>
<td>Specifies the amount (percent) of similarity a deleted and added file pair must have to be considered a rename</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.recentChangeAndAuthors</code></td>
<td>Specifies the string to be shown in place of both the <em>recent change</em> and <em>authors</em> CodeLens when there are unsaved changes</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.recentChangeOnly</code></td>
<td>Specifies the string to be shown in place of the <em>recent change</em> CodeLens when there are unsaved changes</td>
</tr>
<tr>
<td><code>gitlens.strings.codeLens.unsavedChanges.authorsOnly</code></td>
<td>Specifies the string to be shown in place of the <em>authors</em> CodeLens when there are unsaved changes</td>
</tr>
<tr>
<td><code>gitlens.worktrees.defaultLocation</code></td>
<td><code>${userHome}</code> — the path of the user’s home folder<br><code>${workspaceFolder}</code> — the path of the folder opened in VS Code containing the specified repository<br><code>${workspaceFolderBasename}</code> — the name of the folder opened in VS Code containing the specified repository without any slashes (/)</td>
</tr>
<tr>
<td><code>gitlens.visualHistory.allowMultiple</code></td>
<td>Specifies whether to allow opening multiple instances of the Visual File History in the editor area</td>
</tr>
<tr>
<td><code>gitlens.liveshare.enabled</code></td>
<td>Specifies whether to enable integration with Visual Studio Live Share</td>
</tr>
<tr>
<td><code>multiDiffEditor.experimental.enabled</code></td>
<td>Specifies whether to enable VS Code's new multi-diff editor. Requires VS Code 1.85+</td>
</tr>
<tr>
<td><code>gitlens.views.openChangesInMultiDiffEditor</code></td>
<td>Specifies whether to open multiple changes in VS Code's experimental multi-diff editor (single tab) or in individual diff editors (multiple tabs). <code>multiDiffEditor.experimental.enabled</code> must also be enabled in order to use the multi-diff editor. Requires VS Code 1.85+</td>
</tr>
<tr>
<td><code>gitlens.experimental.cloudIntegrations.enabled</code></td>
<td>Specifies to connect GitHub integration using cloud integration of GitKraken account</td>
</tr>
</tbody>
</table>
***

##Themable Colors

GitLens defines a set of themable colors which can be provided by vscode themes or directly by the user using `workbench.colorCustomizations`.

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
<td>Specifies the background color of the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.gutterForegroundColor</code></td>
<td>Specifies the foreground color of the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.gutterUncommittedForegroundColor</code></td>
<td>Specifies the foreground color of an uncommitted line in the file blame annotations</td>
</tr>
<tr>
<td><code>gitlens.trailingLineBackgroundColor</code></td>
<td>Specifies the background color of the trailing blame annotation</td>
</tr>
<tr>
<td><code>gitlens.trailingLineForegroundColor</code></td>
<td>Specifies the foreground color of the trailing blame annotation</td>
</tr>
<tr>
<td><code>gitlens.lineHighlightBackgroundColor</code></td>
<td>Specifies the background color of the associated line highlights in blame annotations</td>
</tr>
<tr>
<td><code>gitlens.lineHighlightOverviewRulerColor</code></td>
<td>Specifies the overview ruler color of the associated line highlights in blame annotations</td>
</tr>
<tr>
<td><code>gitlens.focus.allowMultiple</code></td>
<td>Specifies whether to allow opening multiple instances of the Focus in the editor area</td>
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
<td>Toggle the upstream (ahead/behind) indicators on branches</td>
</tr>
<tr>
<td><code>gitlens.graph.pullRequests</code></td>
<td>Toggle pull request icons</td>
</tr>
<tr>
<td><code>gitlens.graph.dimMergeCommits</code></td>
<td>Specifies whether to dim (deemphasize) merge commit rows</td>
</tr>
<tr>
<td><code>gitlens.graph.scrollRowPadding</code></td>
<td>Specifies the number of rows from the edge at which the graph will scroll when using keyboard or search to change the selected row</td>
</tr>
<tr>
<td><code>gitlens.graph.experimental.location</code></td>
<td>Specifies the location in which the Commit Graph will be shown<br><br> <code>tab</code> - Shows the Commit Graph in a tab in the editor area <br><br> <code>view</code> - Shows the Commit Graph in the side bar and can be dragged and dropped into any side bar, secondary side bar, or panel locations</td>
</tr>
<tr>
<td><code>gitlens.graph.layout</code></td>
<td>Specifies the default layout in which the Commit Graph will be shown. Can be `panel` (default) or `editor`. This is honored when opening the commit graph from the command palette.</td>
</tr>
<tr>
<td><code>gitlens.graph.allowMultiple</code></td>
<td>Specifies whether to allow opening multiple instances of the Commit Graph in the editor area</td>
</tr>
<tr>
<td><code>gitlens.graph.sidebar.enabled</code></td>
<td>Specifies whether to show a sidebar on the Commit Graph</td>
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
<td>Specifies whether to enable Cloud Patches (defaults to true)</td>
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
<td>Specifies an array of repositories with <code>owner/name</code> format to ignore in the Launchpad</td>
</tr>
<tr>
<td><code>gitlens.launchpad.ignoredOrganizations</code></td>
<td>Specifies an array of organizations (or users) to ignore in the Launchpad</td>
</tr>
<tr>
<td><code>gitlens.launchpad.staleThreshold</code></td>
<td>Specifies a value in days after which a pull request is considered stale and moved to the Other category</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.enabled</code></td>
<td>Specifies whether to show the Launchpad indicator in the status bar</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.icon</code></td>
<td>Specifies the style of the Launchpad indicator icon</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.label</code></td>
<td>Specifies the style of the Launchpad indicator label</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.groups</code></td>
<td>Specifies which critical categories of pull requests to summarize in the indicator tooltip</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.useColors</code></td>
<td>Specifies whether to use colors in the indicator</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.openInEditor</code></td>
<td>Specifies whether to open the Launchpad in the editor when clicked</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.polling.enabled</code></td>
<td>Specifies whether to regularly check for changes to pull requests</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.polling.interval</code></td>
<td>Specifies the interval in minutes to check for changes to pull requests</td>
</tr>
<tr>
<td><code>gitlens.views.launchpad.enabled</code></td>
<td>(Experimental) Specifies whether to enable an experimental Launchpad view</td>
</tr>
<tr>
<td><code>gitlens.launchpad.includedOrganizations</code></td>
<td>Specifies which organizations to include in Launchpad</td>
</tr>
</tbody>
</table>