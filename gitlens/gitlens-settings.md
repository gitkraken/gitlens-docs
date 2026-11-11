---
title: GitLens Settings Overview
description: Open GitLens Settings to customize GitLens in Visual Studio Code, and look up each GitLens setting for settings.json.
taxonomy:
    category: gitlens
last_updated: 2026-11
---
<kbd>Last updated: November 2026</kbd>

## Overview

You can customize most GitLens features in the **GitLens Settings** editor or by editing `settings.json` directly.

To open the editor, run _GitLens: Open Settings_ (`gitlens.showSettingsPage`) from the [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

<figure>
  <img src="/wp-content/uploads/gl-settings-01-v3@2x.png" alt="GitLens Settings showing the Inline Blame category with toggle controls and format options" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Settings, Inline Blame category</figcaption>
</figure>

The editor's navigation rail on the left lists **Account**, **Notifications**, and **Get Started** at the top, followed by 4 groups: **Integrations**, **Views**, **Editor**, and **General**. Each category shows its controls with live previews, and changes apply immediately. Use the search bar at the top to filter across all categories, and the **User / Workspace** scope toggle to apply changes globally or to the current workspace only.

### Setup

Use the **Account**, **Notifications**, and **Get Started** entries at the top of the navigation rail to manage your account, read messages from GitKraken, and get started with GitLens.

<figure>
  <img src="/wp-content/uploads/gl-settings-account-01-v4@2x.png" alt="GitLens Settings with the Account category selected, stacked as cards: the signed-in identity with Manage Account and Sign Out, the plan card with its tier badge and included features, the GitKraken AI Usage card with its weekly credits bar and reset date, the active organization and a referral card; the name, e-mail and organization are placeholder values." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Account category</figcaption>
</figure>

**Account**: view your plan and subscription status, manage your GitKraken account, sign in or out, and switch your active organization. The **GitKraken AI Usage** card shows how many of your weekly AI credits you have used and when the allowance resets. On a paid plan, select **Get more AI credits** to buy more. If you belong to an organization, only its owners, admins, and billing contacts can buy credits, and other members see a note to ask an admin or owner.

**Get Started**: onboarding steps for new users and feature discovery.

**Notifications**: read messages from GitKraken for your account and organization, such as tips, offers, security notices, and service updates. Sign in to your GitKraken account to see them. The number of unread notifications appears beside the entry in the navigation rail.

- Filter the list with **All**, **Unread**, or **Read**.
- Select **Mark All as Read**, or **Delete All Read** and then **Confirm** to clear notifications you have read.
- Hover over a notification to **Mark as Read**, **Mark as Unread**, or **Delete** it.
- Under **Preferences**, clear **Receive marketing notifications** to stop marketing messages. This option is available on paid plans only.

When a new security or system notice arrives, GitLens also shows it as a VS Code notification with **View**, which opens the inbox, and **Dismiss**. You can also open the inbox from the notifications button in the [Commit Graph](/gitlens/gl-commit-graph/) header.

<figure>
  <img src="/wp-content/uploads/gl-settings-notifications-01-v2@2x.png" alt="GitLens Settings open on Notifications, with 4 unread beside the entry in the navigation rail. The inbox shows the All / Unread (4) / Read filter, Mark All as Read and Delete All Read, four unread notifications tagged Help, Offer, Security and System (the first showing its Mark as Read and Delete buttons on hover, two with Claim Offer and View Status buttons), and the Receive marketing notifications preference below." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Notifications category</figcaption>
</figure>

### Integrations

Use the **Integrations** group to set up AI, agents, cloud integrations, and other external service connections.

<figure>
  <img src="/wp-content/uploads/gl-settings-ai-01-v2.png" alt="GitLens Settings AI category showing AI provider selection and model configuration" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">AI category</figcaption>
</figure>

**AI**: choose your AI provider, configure models, and control AI-powered features such as commit message generation and code explanations.

**Agents**: lists the chat, extension, CLI, and editor agents GitLens detects. For each agent, you can:

- Choose whether it is the **Default** agent GitLens uses for AI features.
- Install or uninstall the GitKraken MCP server (**MCP**).
- Install or uninstall GitKraken Hooks (**Hooks**), which let GitLens track the agent's sessions and coordinate permissions.

Hooks are available for Claude Code, Codex, GitHub Copilot CLI, and OpenCode. Codex does not run the hooks until you trust them by running `/hooks` in Codex. Until then, a warning icon next to an installed Codex row shows this reminder and a button to start a Codex session.

<figure>
  <img src="/wp-content/uploads/gl-settings-agents-table-01-v2@2x.png" alt="The Agents category of GitLens Settings: a table of agents with Default, MCP and Hooks columns, listing Copilot Chat and the detected Claude Code, Codex, GitHub Copilot CLI and OpenCode CLIs with their GitKraken Hooks state, the Hooks column header ringed." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Agents category</figcaption>
</figure>

**Cloud Integrations**: connect GitHub, GitLab, Bitbucket, Azure DevOps, and other hosting providers for pull request information, avatars, and deep links, as well as the Jira, Jira Data Center, Linear, Trello, and Asana issue trackers.

<figure>
  <img src="/wp-content/uploads/gl-settings-integrations-01-v4@2x.png" alt="The Cloud Integrations category of GitLens Settings listing each provider, from GitHub to Asana and including Jira Data Center and Trello, with Connected and Manage on the connected ones and a Connect button on the rest" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Cloud Integrations category</figcaption>
</figure>

The group also includes:

- **Custom Remotes**: define URL patterns for self-hosted or non-standard remote providers.
- **Autolinks**: create patterns that automatically turn issue references (such as `JIRA-123`) into clickable links.
- **Launchpad**: configure the Launchpad status bar indicator and notification behavior.
- **Terminal Links**: control how Git references in the integrated terminal become clickable links.

**Start Work**: set the **Branch name format** that Start Work uses to suggest a branch name when you start work on an issue (`gitlens.startWork.branchNameFormat`, default `${id}-${title}`).

- Use `${id}` for the issue ID and `${title}` for its lowercase, slugged title. Pick them from the field's token list or type them, with the same prefix, suffix, and width modifiers as other GitLens format tokens.
- GitLens replaces characters that are not valid in a Git branch name and keeps any `/` as branch folders. The **Example** line previews the name for a sample issue.
- Leave the field blank to use the default. Start Work still lets you edit the suggested name before it creates the branch.

<figure>
  <img src="/wp-content/uploads/gl-settings-start-work-01-v2@2x.png" alt="The Start Work category of GitLens Settings, selected under Integrations, with the Branch name format field set to ${id}-${title} and its example branch name ABC-123-update-login-flow." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Start Work category</figcaption>
</figure>

### Editor

Use the **Editor** group to configure the annotations and decorations GitLens adds to the code editor.

<figure>
  <img src="/wp-content/uploads/gl-settings-01-v3@2x.png" alt="GitLens Settings Inline Blame category showing current line blame annotation options" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Inline Blame category — the default view</figcaption>
</figure>

- **Inline Blame**: configure the blame annotation shown at the end of the current line, including format, date style, and pull request information.
- **Git CodeLens**: turn on or off and format the authorship and change indicators above code blocks.
- **Status Bar Blame**: control the blame summary in the VS Code status bar.
- **Hovers**: configure hover tooltips that appear over blame annotations and code, including details, changes, and pull request information.

<figure>
  <img src="/wp-content/uploads/gl-settings-hovers-01-v2@2x.png" alt="GitLens Settings Hovers category showing hover annotation toggles" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Hovers category</figcaption>
</figure>

The group also includes the file annotations:

- **File Blame**: gutter annotations showing per-line authorship across the entire file.
- **File Changes**: gutter indicators highlighting additions, deletions, and modifications relative to the previous commit.
- **File Heatmap**: color-coded gutter annotations showing the relative age of each line of code.

### Views

Use the **Views** group to configure the Commit Graph and the GitLens views in the Side Bar.

<figure>
  <img src="/wp-content/uploads/gl-settings-commit-graph-01-v3@2x.png" alt="GitLens Settings on the Commit Graph category: the live preview of graph rows with branch and tag pills at the top, then the setting for where the Commit Graph opens, the row paging limits and the setting that shows markers" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Commit Graph category</figcaption>
</figure>

- **Commit Graph**: layout, columns, minimap, scroll markers, branch and tag pill layout, details panel position, and graph style (table, list, or auto). The Commit Graph is a Pro feature.
- **GitLens SCM**: configure the Source Control Manager view integration.
- **Commits**: format templates for the Commits view (commit label, description, and tooltip formats, and file and file description formats), with a link to the VS Code Settings UI for the view's remaining `gitlens.views.commits` settings.
- **Stashes**: configure the Stashes view layout and display options.

<figure>
  <img src="/wp-content/uploads/gl-settings-views-01-v3@2x.png" alt="GitLens Settings with the Commits view category selected in the Views group: format templates for the commit label, commit description, commit tooltip, file rows and file description, each with a token picker, and a footer link to the full gitlens.views.commits options in the VS Code Settings UI" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Commits view category</figcaption>
</figure>

> **Note:** GitLens Settings has no category for the Repositories, Branches, Remotes, Tags, Worktrees, Contributors, File History, Line History, and Search & Compare views, or for File Annotations. Configure them in `settings.json`, or in _Preferences: Open Settings (UI)_ by searching for `gitlens.views`, or `gitlens.fileAnnotations` for File Annotations.

### General

Use the **General** group to configure date formatting and the GitLens items in menus and toolbars.

<figure>
  <img src="/wp-content/uploads/gl-settings-dates-01-v2.png" alt="GitLens Settings Dates and Times category showing date format options" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Dates & Times category</figcaption>
</figure>

- **Dates & Times**: control absolute and relative date formatting across GitLens.
- **Menus & Toolbars**: show or hide GitLens items in editor context menus, title bars, and toolbars.

***

## Settings Reference

Look up a GitLens setting by feature area. Edit any of these settings directly in `settings.json`, or change the ones GitLens Settings shows in that editor.

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
<td>Sets the display format for the annotation. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> for supported placeholders. Date format is managed by <code>gitlens.currentLine.dateFormat</code>.</td>
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
<code>document</code>: top of the file<br>
<code>containers</code>: start of container symbols (e.g., classes, interfaces)<br>
<code>blocks</code>: start of block symbols (e.g., functions, methods)</td>
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
<td>Controls where the blame annotation appears in the status bar.<br><br><code>left</code>: aligns to the left<br><code>right</code>: aligns to the right</td>
</tr>
<tr>
<td><code>gitlens.statusBar.command</code></td>
<td>Specifies the command executed when clicking the blame status bar item. Default is <code>gitlens.showQuickCommitDetails</code>. Available commands:<br><br>
<code>gitlens.toggleFileBlame</code>, <code>gitlens.toggleFileHeatmap</code>, <code>gitlens.toggleFileChanges</code>, <code>gitlens.toggleFileChangesOnly</code>, <code>gitlens.toggleCodeLens</code>, <code>gitlens.diffWithPrevious</code>, <code>gitlens.diffWithWorking</code>, <code>gitlens.revealCommitInView</code>, <code>gitlens.showCommitsInView</code>, <code>gitlens.showQuickCommitDetails</code>, <code>gitlens.showQuickCommitFileDetails</code>, <code>gitlens.showQuickFileHistory</code>, <code>gitlens.showQuickRepoHistory</code>, <code>gitlens.openCommitOnRemote</code>, <code>gitlens.copyRemoteCommitUrl</code>, <code>gitlens.openFileOnRemote</code>, <code>gitlens.copyRemoteFileUrl</code></td>
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
<td>Defines the display format of blame data in the status bar. Refer to <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>. Controlled alongside <code>gitlens.statusBar.dateFormat</code>.</td>
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
<td>Specifies the markdown format used in the hover tooltip over blame info. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>.</td>
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
<td>Controls when annotation hovers trigger:<br><br><code>annotation</code>: hover only on the annotation<br><code>line</code>: hover anywhere on the line</td>
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
<td>Controls the diff content shown in hovers:<br><br><code>line</code>: shows only changes to the line<br><code>hunk</code>: shows related changes (code hunk)</td>
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
<td>Controls when hovers appear on the current line:<br><br><code>annotation</code>: hover only on the annotation<br><code>line</code>: hover anywhere on the line</td>
</tr>
<tr>
<td><code>gitlens.hovers.detailsMarkdownFormat</code></td>
<td>Defines the markdown format used for <em>commit details</em> hovers. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>.</td>
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
<td>Specifies the format of commits in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.commits.description</code></td>
<td>Specifies the description format of commits in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.label</code></td>
<td>Specifies the format of a file in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.files.description</code></td>
<td>Specifies the description format of a file in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#file-tokens"><em>File Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.label</code></td>
<td>Specifies the format of stashes in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
</tr>
<tr>
<td><code>gitlens.views.formats.stashes.description</code></td>
<td>Specifies the description format of stashes in the views. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a> in the GitLens docs.</td>
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
<td><code>gitlens.views.remotes.files.icon</code></td>
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
<td><code>gitlens.views.showCurrentBranchOnTop</code></td>
<td>Specifies whether to always show the current branch at the top of views.</td>
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

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>auto</code>: switches between <code>tree</code> and <code>list</code> based on the <code>threshold</code><br>
<code>list</code>: displays a flat file list<br>
<code>tree</code>: displays a hierarchical file structure</td>
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
<code>false</code>: hides comparison section<br>
<code>branch</code>: compares current branch to another reference<br>
<code>working</code>: compares working tree to a selected reference</td>
</tr>
<tr>
<td><code>gitlens.signing.showSignatureBadges</code></td>
<td>Shows signature verification badges on commits in the Commit Graph and other views.</td>
</tr>
</tbody>
</table>

***

## Repositories View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>list</code>: shows all branches in a list<br>
<code>tree</code>: groups branches in a tree structure if names contain <code>/</code></td>
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
<code>auto</code>: switches based on file count and nesting<br>
<code>list</code>: flat file list<br>
<code>tree</code>: hierarchical file view</td>
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
<td><code>gitlens.views.repositories.showCommits</code></td>
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
<tr>
<td><code>gitlens.views.repositories.branches.compact</code></td>
<td>Flattens branch folders when using tree layout, combining single-child folders into a single entry.</td>
</tr>
</tbody>
</table>

***

## File History View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<td>Shows merge commits in file histories. Default: <code>false</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.fileHistory.mode</code></td>
<td>Controls the default display mode:<br><br><code>commits</code>: shows commits for the selected file or folder<br><code>contributors</code>: shows contributors for the selected file or folder</td>
</tr>
</tbody>
</table>


***

## Line History View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>list</code>: shows branches as a list<br>
<code>tree</code>: groups branches into a tree structure</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.branches.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code>: switches between <code>tree</code> and <code>list</code> based on the <code>threshold</code><br>
<code>list</code>: displays a flat list<br>
<code>tree</code>: displays files hierarchically</td>
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
<code>false</code>: hides comparisons<br>
<code>branch</code>: compares the current branch with a selected reference</td>
</tr>
<tr>
<td><code>gitlens.views.branches.branches.compact</code></td>
<td>Flattens branch folders when using tree layout, combining single-child folders into a single entry.</td>
</tr>
</tbody>
</table>

***

## Remotes View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>list</code>: shows branches in a flat list<br>
<code>tree</code>: groups branches hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.compact</code></td>
<td>Flattens unnecessary file nesting when file layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.remotes.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code>: switches between <code>tree</code> and <code>list</code> depending on nesting<br>
<code>list</code>: flat file list<br>
<code>tree</code>: hierarchical file view</td>
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
<td><code>gitlens.views.remotes.branches.compact</code></td>
<td>Flattens branch folders when using tree layout, combining single-child folders into a single entry.</td>
</tr>
</tbody>
</table>

***

## Stashes View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>auto</code>: switches between <code>tree</code> and <code>list</code> layouts based on nesting<br>
<code>list</code>: shows a flat list<br>
<code>tree</code>: shows a hierarchical view</td>
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

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>list</code>: displays tags as a flat list<br>
<code>tree</code>: groups tags hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.compact</code></td>
<td>Flattens unnecessary file nesting when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.layout</code></td>
<td>Controls file display layout:<br><br>
<code>auto</code>: switches between <code>tree</code> and <code>list</code> layouts based on nesting<br>
<code>list</code>: shows a flat list<br>
<code>tree</code>: shows a hierarchical view</td>
</tr>
<tr>
<td><code>gitlens.views.tags.files.threshold</code></td>
<td>Defines the threshold for switching between <code>tree</code> and <code>list</code> layouts when <code>layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.reveal</code></td>
<td>Determines whether tags are shown in the <em>Tags</em> view or revealed in the <em>Repositories</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.tags.branches.compact</code></td>
<td>Flattens tag folders when using tree layout, combining single-child folders into a single entry.</td>
</tr>
</tbody>
</table>

***

## Worktrees View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<code>auto</code>: automatically switches between <code>tree</code> and <code>list</code> views based on the <code>threshold</code><br>
<code>list</code>: shows files in a flat list<br>
<code>tree</code>: shows files hierarchically</td>
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
<code>false</code>: hides comparisons<br>
<code>branch</code>: compares with a selected reference (e.g., tag or branch)</td>
</tr>
</tbody>
</table>

***

## Contributors View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

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
<td>Shows avatar images instead of commit or status icons in the <em>Contributors</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.compact</code></td>
<td>Flattens unnecessary file nesting in the <em>Contributors</em> view. Applies only when <code>gitlens.views.contributors.files.layout</code> is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.layout</code></td>
<td>Controls how the <em>Contributors</em> view displays files:<br><br><code>auto</code>: switches between <code>tree</code> and <code>list</code> based on the <code>gitlens.views.contributors.files.threshold</code> value and the number of files at each nesting level<br><code>list</code>: displays files as a list<br><code>tree</code>: displays files as a tree</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.files.threshold</code></td>
<td>Defines when to switch between <code>tree</code> and <code>list</code> layouts based on the number of files in a nesting level in the <em>Contributors</em> view. Applies only when <code>gitlens.views.contributors.files.layout</code> is set to <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.pullRequests.enabled</code></td>
<td>Enables querying for pull requests associated with branches and commits in the <em>Contributors</em> view. Requires a connection to a supported remote service, such as GitHub.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.pullRequests.showForCommits</code></td>
<td>Shows pull requests associated with commits in the <em>Contributors</em> view. Requires a connection to a supported remote service, such as GitHub.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.showAllBranches</code></td>
<td>Shows commits from all branches in the <em>Contributors</em> view.</td>
</tr>
<tr>
<td><code>gitlens.views.contributors.showStatistics</code></td>
<td>Shows contributor statistics in the <em>Contributors</em> view. Computing the statistics can take a while in large repositories.</td>
</tr>
</tbody>
</table>

***

<a id="search-and-compare-view-settings"></a>
## Search & Compare View Settings

See also [View Settings](/gitlens/gitlens-settings/#view-settings).

These settings control how files and avatars are displayed, and what clicking a file opens, in the GitLens <em>Search &amp; Compare</em> view.

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.views.searchAndCompare.files.openDiffOnClick</code></td>
<td>Specifies whether clicking a file in the <em>Search &amp; Compare</em> view opens its changes (diff). When disabled, clicking a file opens the working file at the first changed line instead. Default: <code>true</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.files.layout</code></td>
<td>Controls file display in the <em>Search &amp; Compare</em> view:<br><br>
<code>auto</code>: switches between <code>tree</code> and <code>list</code> based on nesting and threshold<br>
<code>list</code>: shows files in a flat list<br>
<code>tree</code>: shows files hierarchically</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.files.threshold</code></td>
<td>Determines when to switch between <code>tree</code> and <code>list</code> layouts based on the number of files in a nesting level. Applies only when layout is <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.files.compact</code></td>
<td>Flattens unnecessary file nesting in the <em>Search &amp; Compare</em> view. Applies when layout is set to <code>tree</code> or <code>auto</code>.</td>
</tr>
<tr>
<td><code>gitlens.views.searchAndCompare.avatars</code></td>
<td>Shows avatar images instead of commit or status icons in the <em>Search &amp; Compare</em> view.</td>
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
<td>Specifies the display format of blame annotations. See <a href="https://github.com/gitkraken/vscode-gitlens/wiki/Custom-Formatting#commit-tokens"><em>Commit Tokens</em></a>. Date format is controlled by <code>gitlens.blame.dateFormat</code>.</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.enabled</code></td>
<td>Enables a heatmap indicator in blame annotations.</td>
</tr>
<tr>
<td><code>gitlens.blame.heatmap.location</code></td>
<td>Determines heatmap indicator placement:<br><br><code>left</code>: left edge of annotations<br><code>right</code>: right edge of annotations</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.enabled</code></td>
<td>Highlights lines related to the current line.</td>
</tr>
<tr>
<td><code>gitlens.blame.highlight.locations</code></td>
<td>Specifies where highlights appear:<br><br><code>gutter</code>: adds an indicator to the gutter<br><code>line</code>: full-line background highlight<br><code>overview</code>: decoration in the overview ruler</td>
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
<td>Determines toggle scope:<br><br><code>file</code>: toggles blame per file<br><code>window</code>: toggles blame for all files in the window</td>
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
<td>Controls where file changes indicators appear:<br><br><code>gutter</code>: shows a file indicator in the gutter<br><code>line</code>: adds a full-line background highlight<br><code>overview</code>: adds a decoration in the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.changes.toggleMode</code></td>
<td>Determines toggle scope for file changes annotations:<br><br><code>file</code>: toggles annotations per file<br><code>window</code>: toggles annotations for all files in the window</td>
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
<td>Specifies where heatmap indicators appear:<br><br><code>gutter</code>: shows indicator in the gutter<br><code>line</code>: adds a full-line background highlight<br><code>overview</code>: adds a decoration in the overview ruler (scroll bar)</td>
</tr>
<tr>
<td><code>gitlens.heatmap.toggleMode</code></td>
<td>Determines toggle scope for file heatmap annotations:<br><br><code>file</code>: toggles annotations per file<br><code>window</code>: toggles annotations for all files in the window</td>
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
<td>Specifies which (and when) Git commands skip the confirmation step, using the format <code>git-command-name:(menu|command)</code>. Supported commands are <code>branch-create</code>, <code>co-authors</code>, <code>fetch</code>, <code>pull</code>, <code>push</code>, <code>stash-apply</code>, <code>stash-pop</code>, <code>stash-push</code>, <code>switch</code>, <code>tag-create</code>, and <code>tag-push</code>.<br><br>You can also select the <em>Don't Ask Again</em> toggle under <em>Options</em> in a supported confirmation step to add or remove that command here; its gear button opens this setting.</td>
</tr>
<tr>
<td><code>gitlens.gitCommands.sortBy</code></td>
<td>Specifies sorting order of commands in the <em>Git Command Palette</em>:<br><br><code>name</code>: alphabetically by command name<br><code>usage</code>: by last used date</td>
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
<tr>
<td><code>gitlens.terminalLinks.showIn</code></td>
<td>Controls where terminal link references open.<br><br>
<code>graph</code>: opens in the Commit Graph<br>
<code>inspect</code>: opens in the Inspect view<br>
<code>quickpick</code>: opens in a quick pick menu</td>
</tr>
</tbody>
</table>

***

## Rebase Editor Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.rebaseEditor.openOnPausedRebase</code></td>
<td>Controls whether the Interactive Rebase Editor opens automatically when GitLens detects a paused rebase. For a rebase paused on conflicts, GitLens opens the Commit Graph instead, when it can.<br><br>
<code>true</code>: opens for any paused rebase<br>
<code>false</code>: never opens<br>
<code>auto</code> (default): opens only for rebases started or acted on from GitLens<br>
<code>interactive</code>: opens only for interactive rebases</td>
</tr>
<tr>
<td><code>gitlens.rebaseEditor.revealLocation</code></td>
<td>Controls where the Interactive Rebase Editor reveals commits and references:<br><br>
<code>graph</code> (default): in the Commit Graph<br>
<code>inspect</code>: in the Inspect view</td>
</tr>
<tr>
<td><code>gitlens.rebaseEditor.revealBehavior</code></td>
<td>Controls when the Interactive Rebase Editor reveals commits in the location set by <code>gitlens.rebaseEditor.revealLocation</code>:<br><br>
<code>onDoubleClick</code> (default): when you double-click a row<br>
<code>onSelection</code>: when the selection changes or when you double-click a row</td>
</tr>
<tr>
<td><code>gitlens.rebaseEditor.density</code></td>
<td>Controls the visual density of commits in the rebase editor.<br><br>
<code>compact</code>: compact display<br>
<code>comfortable</code>: comfortable display with more spacing</td>
</tr>
<tr>
<td><code>gitlens.rebaseEditor.openBehavior</code></td>
<td>Controls which editor group the Interactive Rebase Editor opens in when it reopens automatically on a paused rebase:<br><br>
<code>auto</code> (default): opens beside the commit message editor when a multi-pane layout already exists, otherwise in the active editor group<br>
<code>beside</code>: always opens beside the active editor, creating a new editor group if needed</td>
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
<td>Specifies the locale for date formatting, using a <a href="https://en.wikipedia.org/wiki/IETF_language_tag#List_of_major_primary_language_subtags" rel="nofollow">BCP 47 language tag</a>. Defaults to the VS Code locale. Use <code>system</code> to follow the current system locale or specify a locale like <code>en-US</code> (US English), <code>en-GB</code> (British English), <code>de-DE</code> (German), <code>ja-JP</code> (Japanese), etc.<br><br>This setting affects only date formatting. GitLens has no separate interface-language setting: it follows VS Code's display language, with translations for Spanish, Simplified Chinese, and Traditional Chinese and English as the fallback. To change it, run <em>Configure Display Language</em> from the Command Palette.</td>
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

<a id="menu-and-toolbar-settings"></a>
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
<code>null</code> (default): shows a menu to select which file annotations to toggle<br>
<code>blame</code>: toggles file blame annotations<br>
<code>heatmap</code>: toggles file heatmap annotations<br>
<code>changes</code>: toggles file changes annotations
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
<code>alternate</code>: adds alternate shortcuts starting with <kbd>Alt</kbd> (⌥ on macOS)<br>
<code>chorded</code>: adds chorded shortcuts starting with <kbd>Ctrl+Shift+G</kbd> (⌥⌘G on macOS)<br>
<code>none</code>: disables all GitLens shortcut keys
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
<code>left</code>: aligns left<br>
<code>right</code>: aligns right</td>
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
<td>Specifies whether to enable GitLens' AI-powered features.</td>
</tr>
<tr>
<td><code>gitlens.gitkraken.mcp.autoEnabled</code></td>
<td>Specifies whether to automatically install and enable the GitKraken MCP server. Applies to VS Code 1.101 and later. Default: <code>true</code>. Turning this setting off, or turning off <code>gitlens.ai.enabled</code>, removes the GitKraken MCP server from VS Code's <strong>Configure Tools</strong> list without reloading the window.</td>
</tr>
<tr>
<td><code>gitlens.ai.model</code></td>
<td>Specifies the AI provider and model to use for GitLens' AI features, formatted as <code>provider:model</code> (for example, <code>openai:gpt-5.5</code> or <code>anthropic:claude-sonnet-5</code>). Use <code>gitkraken</code> for models provided by GitKraken AI, or <code>vscode</code> for models provided through the VS Code extension API, such as Copilot.</td>
</tr>
<tr>
<td><code>gitlens.ai.gitkraken.model</code></td>
<td>Specifies the GitKraken AI provided model to use for GitLens' AI features, formatted as <code>provider:model</code>.</td>
</tr>
<tr>
<td><code>gitlens.ai.vscode.model</code></td>
<td>Specifies the VS Code provided model to use for GitLens' AI features, formatted as <code>provider:model</code>.</td>
</tr>
<tr>
<td><code>gitlens.ai.ollama.url</code></td>
<td>Specifies the Ollama URL to use for access.</td>
</tr>
<tr>
<td><code>gitlens.ai.openai.url</code></td>
<td>Specifies a custom URL to use for access to an OpenAI model.</td>
</tr>
<tr>
<td><code>gitlens.ai.azure.url</code></td>
<td>Specifies a custom URL to use for access to an Azure OpenAI model, in this format: <code>https://{your-resource-name}.openai.azure.com/openai/deployments/{deployment-id}/chat/completions?api-version={api-version}</code></td>
</tr>
<tr>
<td><code>gitlens.ai.openaicompatible.url</code></td>
<td>Specifies a custom URL to use for access to an OpenAI-compatible model.</td>
</tr>
<tr>
<td><code>gitlens.ai.largePromptWarningThreshold</code></td>
<td>Specifies the prompt size (in tokens) above which GitLens warns that the prompt is too large.</td>
</tr>
<tr>
<td><code>gitlens.ai.modelOptions.temperature</code></td>
<td>Specifies the temperature, a measure of output randomness, to use for the AI model. Higher values give more random (creative) output, and lower values give more deterministic output.</td>
</tr>
<tr>
<td><code>gitlens.ai.explainChanges.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating a summary of changes.</td>
</tr>
<tr>
<td><code>gitlens.ai.generateChangelog.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating a changelog from a set of changes.</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCommits.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating commits.</td>
</tr>
<tr>
<td><code>gitlens.ai.generateStashMessage.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating a stash message.</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCreateCloudPatch.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating a cloud patch title and description.</td>
</tr>
<tr>
<td><code>gitlens.ai.generateCreatePullRequest.customInstructions</code></td>
<td>Specifies custom instructions to give the AI provider when generating a pull request title and description.</td>
</tr>
<tr>
<td><code>gitlens.ai.openInAgent</code></td>
<td>Specifies the default route for Start Work and Start PR Review when opening in an agent is offered:<br><br>
<code>ask</code>: asks each time (default)<br>
<code>manual</code>: always continues manually<br>
<code>agent</code>: always opens in an agent, using <code>gitlens.ai.defaultAgent</code> when it is set<br>
<code>kepler</code>: always starts a task in Kepler, without creating a branch or worktree, when Kepler supports the item; otherwise asks</td>
</tr>
<tr>
<td><code>gitlens.ai.defaultAgent</code></td>
<td>Specifies the default agent for Start Work, Start PR Review, and starting an agent session. When the saved agent is no longer available, GitLens asks you to choose one. Set it by selecting <strong>Always use this agent</strong> in the agent picker.</td>
</tr>
<tr>
<td><code>gitlens.ai.exclude.files</code></td>
<td>Glob patterns for files to exclude from AI context. Also respects <code>.aiignore</code>, <code>.cursorignore</code>, and <code>.aiexclude</code> files.</td>
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
<code>identicon</code>: geometric pattern<br>
<code>mp</code>: cartoon-style silhouette (same for all emails)<br>
<code>monsterid</code>: colorful monster faces<br>
<code>retro</code>: 8-bit pixelated faces<br>
<code>robohash</code>: robot faces with variations<br>
<code>wavatar</code>: faces with different features and backgrounds
</td>
</tr>
<tr>
<td><code>gitlens.liveshare.allowGuestAccess</code></td>
<td>Allows guest access to GitLens features during Visual Studio Live Share sessions.</td>
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
<td>Keeps file annotations while you edit a file. The <code>gitlens.advanced.blame.delayAfterEdit</code> setting controls how long GitLens waits before updating the annotations of an unsaved file, which applies only if the file is under <code>gitlens.advanced.blame.sizeThresholdAfterEdit</code> (default 5000 lines).</td>
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
<td><code>gitlens.advanced.commitOrdering</code></td>
<td>Ordering method for commits (default is reverse chronological by commit date):<br><br>
<code>date</code>: reverse chronological by commit timestamp<br>
<code>author-date</code>: reverse chronological by author timestamp<br>
<code>topo</code>: reverse chronological but avoids mixing multiple lines of history
</td>
</tr>
<tr>
<td><code>gitlens.advanced.commits.delayLoadingFileDetails</code></td>
<td>Specifies whether to delay loading commit file details until they are shown. Delaying makes large histories open faster but adds a Git call each time a commit's files are shown.<br><br>
<code>null</code> (default): delays only in repositories where loading file details has been slow (requires <code>gitlens.gitOptimizations.enabled</code>)<br>
<code>true</code>: always delays<br>
<code>false</code>: never delays</td>
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
<code>${userHome}</code>: user's home directory<br>
<code>${workspaceFolder}</code>: path of the opened folder in VS Code containing the repository<br>
<code>${workspaceFolderBasename}</code>: name of the opened folder in VS Code without slashes
</td>
</tr>
<tr>
<td><code>gitlens.worktrees.openAfterCreate</code></td>
<td>Specifies how and when to open a worktree after it is created. Choosing an <em>After Creating</em> option (<em>Open in New Window</em>, <em>Open in Current Window</em>, <em>Add to Workspace</em>, or <em>Don't Open</em>) in the Create Worktree dialog updates this setting.<br><br>
<code>newWindow</code> (default): always open the new worktree in a new window<br>
<code>currentWindow</code>: always open the new worktree in the current window<br>
<code>addToWorkspace</code>: always add the new worktree to the current workspace<br>
<code>none</code>: never open the new worktree<br>
<code>onlyWhenEmpty</code>: open the new worktree in the current window only when no folder is opened, otherwise in a new window</td>
</tr>
<tr>
<td><code>gitlens.visualHistory.allowMultiple</code></td>
<td>Allows opening multiple Visual History instances in the editor area.</td>
</tr>
<tr>
<td><code>gitlens.liveshare.enabled</code></td>
<td>Enables integration with Visual Studio Live Share.</td>
</tr>
<tr>
<td><code>gitlens.views.openChangesInMultiDiffEditor</code></td>
<td>Controls whether to open multiple changes in VS Code's multi-diff editor (single tab) or individual diff editors (multiple tabs).</td>
</tr>
<tr>
<td><code>gitlens.advanced.git.maxConcurrentProcesses</code></td>
<td>Maximum number of concurrent git processes, with priority-based queuing.</td>
</tr>
<tr>
<td><code>gitlens.defaultCurrentUserNameStyle</code></td>
<td>Controls how the current user's name is displayed across blame, hovers, views, and graph.</td>
</tr>
<tr>
<td><code>gitlens.advanced.git.timeout</code></td>
<td>Specifies the timeout (in seconds) for Git commands. Use 0 to disable the timeout. Some long-running operations like merge, rebase, and revert always have the timeout disabled. Default: 60. With 0, background reads that set a time limit of their own still stop at it.</td>
</tr>
<tr>
<td><code>gitlens.advanced.resolveSymlinks</code></td>
<td>Resolves symbolic links before performing git operations.</td>
</tr>
<tr>
<td><code>gitlens.advanced.skipOnboarding</code></td>
<td>Skips onboarding experiences, such as the Welcome view. Useful for ephemeral environments like containers or sandboxes.</td>
</tr>
<tr>
<td><code>gitlens.sortWorkingChangesBy</code></td>
<td>Controls how working changes are sorted.<br><br>
<code>stage</code>: sorts by staging status<br>
<code>flat</code>: flat sort order</td>
</tr>
<tr>
<td><code>gitlens.visualHistory.editorOpeningBehavior</code></td>
<td>Controls how files open from the Visual History view.</td>
</tr>
<tr>
<td><code>gitlens.gitOptimizations.enabled</code></td>
<td>Specifies whether GitLens automatically applies safe, repo-local Git performance optimizations in the background (loose-object packing, incremental repack, and commit-graph) while VS Code is open. Enabled by default.<br><br>
This is the same routine work Git performs during <code>git gc</code> or <code>git maintenance</code>: packing and repacking reorganize objects the repository already contains without altering history, and the commit-graph is an acceleration cache that can be deleted at any time. More invasive optimizations (untracked cache, FSMonitor, system-scheduled maintenance, <code>feature.manyFiles</code>) are never applied automatically. Turning this off also turns off Repository Health in the Commit Graph and the automatic behavior of <code>gitlens.advanced.commits.delayLoadingFileDetails</code>.</td>
</tr>
<tr>
<td><code>gitlens.openInTerminalLocation</code></td>
<td>Specifies where GitLens opens the terminals it creates, such as agent session terminals and <em>Open in Integrated Terminal</em>. The first time GitLens creates a terminal, it offers <em>Use Editor Tabs</em> to switch this setting to <code>editor</code>.<br><br>
<code>panel</code> (default): open in the terminal panel<br>
<code>editor</code>: open as an editor tab</td>
</tr>
<tr>
<td><code>gitlens.agents.resumeTarget</code></td>
<td><strong>Preview</strong> — Specifies where a past agent session is resumed when both a terminal and the agent's VS Code extension could open it. Actions that name a destination, such as <em>Resume in Terminal</em>, are unaffected.<br><br>
<code>null</code> (default): ask which to use the first time a session can be resumed in either place, with an option to remember<br>
<code>terminal</code>: always resume in a new integrated terminal<br>
<code>extension</code>: resume in the agent's VS Code extension when it can open the session, otherwise in a terminal</td>
</tr>
</tbody>
</table>

***

## Themable Colors

GitLens defines themable colors. VS Code themes can set them, and you can customize them with `workbench.colorCustomizations`.

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
<td><code>gitlens.graph.pullRequests.enabled</code></td>
<td>Shows associated pull requests on remote branches in the Commit Graph. Requires a connection to a supported remote service, such as GitHub.</td>
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
<td><code>gitlens.graph.layout</code></td>
<td>Default layout for the Commit Graph. Options:<br><br>
<code>panel</code> (default): shows in a panel<br>
<code>editor</code>: shows in the editor area.<br>
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
<tr>
<td><code>gitlens.graph.stickyTimeline</code></td>
<td>Shows a sticky timeline header that stays visible at the top while you scroll the Commit Graph.</td>
</tr>
<tr>
<td><code>gitlens.graph.autoFetch.enabled</code></td>
<td>Auto-fetches the repository while the Commit Graph is in view, at the interval set by VS Code's <code>git.autofetchPeriod</code> setting. If <code>git.autofetch</code> is enabled, VS Code handles auto-fetching and this setting has no effect.</td>
</tr>
<tr>
<td><code>gitlens.graph.followTerminal.enabled</code></td>
<td>Specifies whether a visible Commit Graph follows the active terminal or Claude Code conversation tab, selecting the working changes row of the repository or worktree it is in. Enabled by default.</td>
</tr>
<tr>
<td><code>gitlens.graph.followTerminal.allowRepositorySwitching</code></td>
<td>Specifies whether following the active terminal or Claude Code conversation tab can switch the Commit Graph to a different repository. When disabled (the default), terminals in other repositories are ignored.</td>
</tr>
<tr>
<td><code>gitlens.graph.details.location</code></td>
<td>Controls where the details panel appears relative to the graph.<br><br>
<code>right</code>: shows the details panel to the right of the Commit Graph<br>
<code>bottom</code>: shows the details panel below the Commit Graph<br>
<code>auto</code> (default): places the details panel to the right of or below the Commit Graph automatically</td>
</tr>
<tr>
<td><code>gitlens.graph.details.maximizeOnMode</code></td>
<td>Automatically maximizes the details panel when you enter a mode, such as Compose, Review, Resolve, or Compare, and restores it when you leave. Applies only when the details panel is docked to the bottom.</td>
</tr>
<tr>
<td><code>gitlens.graph.editorOpeningBehavior</code></td>
<td>Controls how files open from the graph (e.g., in the current editor group or beside it).</td>
</tr>
<tr>
<td><code>gitlens.graph.sidebar.pinned</code></td>
<td>Pins the graph sidebar to stay visible.</td>
</tr>
<tr>
<td><code>gitlens.graph.showWorktreeWipStats</code></td>
<td>Shows working tree change statistics on WIP rows.</td>
</tr>
<tr>
<td><code>gitlens.graph.minimap.reversed</code></td>
<td>Reverses the minimap direction.</td>
</tr>
<tr>
<td><code>gitlens.graph.minimap.defaultVisibility</code></td>
<td>Controls when the minimap is visible by default.<br><br>
<code>hidden</code>: minimap is hidden<br>
<code>onSearch</code>: minimap appears during search<br>
<code>always</code>: minimap is always visible</td>
</tr>
<tr>
<td><code>gitlens.graph.overviewBar.visibility</code></td>
<td>Specifies when to show the overview bar above the Commit Graph: the per-worktree <em>WIP</em> pills and the HEAD, upstream, and merge target jumps. When shown, the primary worktree is always included.<br><br>
<code>always</code>: always shown, with every secondary worktree<br>
<code>worktrees</code>: shown when the repository has more than one worktree, with every secondary worktree<br>
<code>dirtyWorktrees</code> (default): shown when another worktree has working changes or unpushed commits, and includes only those worktrees<br>
<code>never</code>: never shown</td>
</tr>
<tr>
<td><code>gitlens.graph.scopeBehavior</code></td>
<td>Specifies what <em>Scope to Worktree</em> does in the Commit Graph.<br><br>
<code>scope</code>: only moves HEAD-derived state onto the worktree, leaving every commit visible<br>
<code>scopeAndFocus</code> (default): also focuses the worktree's branch, narrowing the visible rows</td>
</tr>
<tr>
<td><code>gitlens.graph.doubleClickWorktreeAction</code></td>
<td>Specifies what double-clicking a secondary worktree's working changes row, its overview bar pill, or its sidebar row does in the Commit Graph.<br><br>
<code>scope</code> (default): scopes the Commit Graph to the worktree, as set by <code>gitlens.graph.scopeBehavior</code><br>
<code>focus</code>: toggles the classic branch focus without scoping</td>
</tr>
<tr>
<td><code>gitlens.graph.refFindAutoHide</code></td>
<td>Closes the Commit Graph's Branch / Tag finder when it loses focus.</td>
</tr>
<tr>
<td><code>gitlens.graph.style</code></td>
<td>Controls the graph display style (row layout):<br><br>
<code>table</code>: single-line rows with columns (message, author, date, SHA)<br>
<code>list</code>: stacked two-line rows with no columns<br>
<code>auto</code> (default): switches to <code>list</code> when the graph is too narrow for the columns</td>
</tr>
<tr>
<td><code>gitlens.graph.changesColumn.enabled</code></td>
<td>Computes file and line change statistics for the Changes column. Computing changes can be slow in large repositories. When this setting is off, the Changes column offers a one-time opt-in.</td>
</tr>
<tr>
<td><code>gitlens.graph.changesColumn.mode</code></td>
<td>Controls how changes are visualized in the Changes column.<br><br>
<code>numbers</code>: shows numeric counts<br>
<code>squares</code>: shows colored squares<br>
<code>bar</code>: shows a bar indicator<br>
<code>bipolar</code>: shows a bipolar indicator</td>
</tr>
<tr>
<td><code>gitlens.graph.refs.layout</code></td>
<td>Specifies how branch and tag pills are laid out on each row of the Commit Graph.<br><br>
<code>inline</code> (default): shows pills inline with the commit row<br>
<code>stacked</code>: shows pills on their own line above the commit, growing the row</td>
</tr>
<tr>
<td><code>gitlens.graph.refs.maxInline</code></td>
<td>Specifies the maximum number of branch and tag pills to show on each row, as space allows: <code>1</code> (default) to <code>10</code>, or <code>auto</code> to fit as many pills as the row area allows. Additional refs are collapsed behind a <em>+N</em> counter on the last pill.</td>
</tr>
<tr>
<td><code>gitlens.graph.refs.maxStacked</code></td>
<td>Specifies the maximum number of branch and tag pills to show on the stacked pill line when <code>gitlens.graph.refs.layout</code> is <code>stacked</code>: <code>1</code> to <code>10</code>, or <code>auto</code> (default) to fit as many pills as the line allows. Additional refs are collapsed behind a <em>+N</em> counter on the last pill.</td>
</tr>
<tr>
<td><code>gitlens.graph.shortcuts.enabled</code></td>
<td>Specifies whether the customizable keyboard shortcuts of the Commit Graph (those using <kbd>Ctrl</kbd>, <kbd>Alt</kbd>, or <kbd>⌘</kbd>, such as <kbd>Alt+M</kbd> or <kbd>Ctrl+↑</kbd>) are enabled. Navigation keys such as the arrows, <kbd>Enter</kbd>, and <kbd>Esc</kbd> always work.</td>
</tr>
<tr>
<td><code>gitlens.graph.shortcuts.overrides</code></td>
<td>Changes or disables individual Commit Graph keyboard shortcuts, keyed by shortcut id. To see an id, press <kbd>?</kbd> in the Commit Graph and hover a shortcut; only shortcuts that show an id can be changed.<br><br>
Set an id to a key combination, a list of them, or <code>false</code> to disable it. A key ending in <code>.*</code> set to <code>false</code> disables every shortcut with that prefix (for example, <code>"panels.*": false</code>), and <code>"*": false</code> disables them all; wildcards cannot rebind. Key combinations join modifiers (<code>ctrl</code>, <code>alt</code>, <code>shift</code>, <code>meta</code>, or <code>mod</code> for <kbd>Ctrl</kbd>, or <kbd>⌘</kbd> on macOS) with <code>+</code> before a key, for example <code>"mod+shift+ArrowUp"</code>. Letters and digits use physical key names (<code>KeyA</code> to <code>KeyZ</code>, <code>Digit0</code> to <code>Digit9</code>); other keys use their <code>KeyboardEvent.key</code> value (<code>ArrowUp</code>, <code>Enter</code>, <code>/</code>).</td>
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

## Start Work Settings

<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gitlens.startWork.branchNameFormat</code></td>
<td>Specifies the branch name format when starting work on an issue. Use <code>${id}</code> for the issue ID and <code>${title}</code> for its lowercase, slugged title; the GitLens token prefix, suffix, and width modifiers are supported. GitLens replaces characters that are not valid in a Git branch name, and <code>/</code> keeps branch folders. Leave blank to use the default, <code>${id}-${title}</code>. You can edit the suggested name before the branch is created.</td>
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
<td>Number of days after which Launchpad considers a pull request stale and moves it to the <strong>Other</strong> group.</td>
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
<td><code>gitlens.launchpad.indicator.polling.enabled</code></td>
<td>Enables regular polling for pull request changes.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.indicator.polling.interval</code></td>
<td>Polling interval in minutes for checking pull request changes. Use 0 to turn off automatic polling.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.includedOrganizations</code></td>
<td>Organizations to include in Launchpad. If the list is empty, Launchpad includes all organizations.</td>
</tr>
<tr>
<td><code>gitlens.launchpad.allowMultiple</code></td>
<td>Allows opening multiple instances of Launchpad as editor tabs.</td>
</tr>
</tbody>
</table>
