---

title: GitLens Features
description: GitLens Features
taxonomy:
    category: gitlens

---

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repos
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens), e.g. Community, Pro, etc

***

##Revision Navigation

<img src="/wp-content/uploads/revision-navigation.gif" class="help-center-img img-bordered">

- Adds an _Open Changes with Previous Revision_ command (`gitlens.diffWithPrevious`) to compare the current file or revision with the previous commit revision
- Adds an _Open Changes with Next Revision_ command (`gitlens.diffWithNext`) to compare the current file or revision with the next commit revision
- Adds an _Open Line Changes with Previous Revision_ command (`gitlens.diffLineWithPrevious`) to compare the current file or revision with the previous line commit revision
- Adds an _Open Changes with Working File_ command (`gitlens.diffWithWorking`) to compare the current revision or most recent commit revision of the current file with the working tree
- Adds an _Open Line Changes with Working File_ command (`gitlens.diffLineWithWorking`) to compare the commit revision of the current line with the working tree
- Adds an _Open Changes with Branch or Tag..._ command (`gitlens.diffWithRevisionFrom`) to compare the current file or revision with another revision of the same file on the selected reference
- Adds an _Open Changes with Revision..._ command (`gitlens.diffWithRevision`) to compare the current file or revision with another revision of the same file

***

##Current Line Blame

<img src="/wp-content/uploads/current-line-blame.png" class="help-center-img img-bordered">

Adds an unobtrusive, [customizable](/gitlens/settings/#current-line-blame-settings), and [themable](/gitlens/settings/#themable-colors), **blame annotation** at the end of the current line.

- Contains the author, date, and message of the current line's most recent commit (by [default](/gitlens/settings/#current-line-blame-settings))
- Adds a _Toggle Line Blame Annotations_ (`gitlens.toggleLineBlame`) to toggle the blame annotation on and off

***

##Git CodeLens

<img src="/wp-content/uploads/code-lens.png" class="help-center-img img-bordered">


Adds Git authorship CodeLens to the top of the file and on code blocks ([optional](/gitlens/settings/#git-codelens-settings), on by default)

- **Recent Change** — author and date of the most recent commit for the file or code block

    - Click the CodeLens to show a **commit file details quick pick menu** with commands for comparing, navigating and exploring commits, and more (by [default](/gitlens/settings/#git-codelens-settings))

- **Authors** — number of authors of the file or code block and the most prominent author (if there is more than one)
    - Click the CodeLens to toggle the file Git blame annotations on and off of the whole file (by [default](/gitlens/settings/#git-codelens-settings))
    - Will be hidden if the author of the most recent commit is also the only author of the file or block, to avoid duplicate information and reduce visual noise

- Provides [customizable](/gitlens/settings/#git-codelens-settings) click behavior for each CodeLens — choose between one of the following
    - Toggle file blame annotations on and off
    - Compare the commit with the previous commit
    - Show a quick pick menu with details and commands for the commit
    - Show a quick pick menu with file details and commands for the commit
    - Show a quick pick menu with the commit history of the file
    - Show a quick pick menu with the commit history of the current branch

- Adds a _Toggle Git CodeLens_ command (`gitlens.toggleCodeLens`) with a shortcut of `shift+alt+b` to toggle the CodeLens on and off

***

##Status Bar Blame

<img src="/wp-content/uploads/status-bar.png" class="help-center-img img-bordered">

Adds a customizable **Git blame annotation** showing the commit and author who last modified the current line to the status bar (optional, on by default)

- Contains the commit author and date (by default)

- Click the status bar item to show a **commit details quick pick menu** with commands for comparing, navigating and exploring commits, and more (by default)

- Provides customizable click behavior — choose between one of the following

    - Toggle file blame annotations on and off
    - Toggle CodeLens on and off
    - Compare the line commit with the previous commit
    - Compare the line commit with the working tree
    - Show a quick pick menu with details and commands for the commit (default)
    - Show a quick pick menu with file details and commands for the commit
    - Show a quick pick menu with the commit history of the file
    - Show a quick pick menu with the commit history of the current branch

***

##Hovers 

###Current Line Hovers

<img src="/wp-content/uploads/hovers-current-line.png" class="help-center-img img-bordered">

Adds [customizable](/gitlens/settings/#hover-settings) Git blame hovers accessible over the current line

####Details Hover

<img src="/wp-content/uploads/hovers-current-line-details.png" class="help-center-img img-bordered">

Adds a **details hover** annotation to the current line to show more commit details (optional, on by default)

- Provides **automatic issue linking** to Bitbucket, Gerrit, Gitea, GitHub, GitLab, and Azure DevOps in commit messages
- Provides a **quick-access command bar** with _Open Changes_, _Blame Previous Revision_, _Open on Remote_, _Invite to Live Share_ (if available), and _Show More Actions_ command buttons
- Click the commit SHA to execute the _Show Commit_ command

####Changes (diff) Hover

<img src="/wp-content/uploads/hovers-current-line-changes.png" class="help-center-img img-bordered">


Adds a changes (diff) hover annotation to the current line to show the line's previous version ([optional](/gitlens/settings/#hover-settings), on by default)
- Click the Changes to execute the _Open Changes_ command
- Click the current and previous commit SHAs to execute the _Show Commit_ command

###Annotation Hovers

<img src="/wp-content/uploads/hovers-annotations.png" class="help-center-img img-bordered">

Adds [customizable](/gitlens/settings/#hover-settings)  Git blame hovers accessible when annotating


####Details Hover

<img src="/wp-content/uploads/hovers-annotations-details.png" class="help-center-img img-bordered">

Adds a **details hover** annotation to each line while annotating to show more commit details ([optional](/gitlens/settings/#hover-settings), on by default)

- Provides **automatic issue linking** to Bitbucket, Gerrit, Gitea, GitHub, GitLab, and Azure DevOps in commit messages
- Provides a quick-access command bar with _Open Changes_, _Blame Previous Revision_, _Open on Remote_, _Invite to Live Share_ (if available), and _Show More Actions_ command buttons
- Click the commit SHA to execute the _Show Commit_ command

####Changes (diff) Hover

<img src="/wp-content/uploads/hovers-annotations-changes.png" class="help-center-img img-bordered">

Adds a **changes (diff) hover** annotation to each line while annotating to show the line's previous version ([optional](/gitlens/settings/#hover-settings), on by default)

- Click the **Changes** to execute the _Open Changes_ command
- Click the current and previous commit SHAs to execute the _Show Commit_ command

***

##File Blame

<img src="/wp-content/uploads/gutter-blame.png" class="help-center-img img-bordered">

Adds on-demand, [customizable](/gitlens/settings/#gutter-blame-settings), and [themable](/gitlens/settings/#themable-colors), file blame annotations to show the commit and author who last modified each line of a file

- Contains the commit message and date, by [default](/gitlens/settings/#file-blame-settings)
- Adds a heatmap (age) indicator on right edge (by [default](/gitlens/settings/#file-blame-settings),) of the file to provide an easy, at-a-glance way to tell how recently lines were changed (optional, on by default)
- See the [file heatmap](/gitlens/gitlens-features/#file-heatmap) section below for more details
- Adds a Toggle File Blame Annotations command (`gitlens.toggleFileBlame`) with a shortcut of <kbd>alt+b</kbd> to toggle the blame annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##File Changes

<img src="/wp-content/uploads/gutter-blame.png" class="help-center-img img-bordered">

Adds an on-demand, [customizable](/gitlens/settings/#file-changes-settings), and [themable](/gitlens/settings/#themable-colors), file changes annotation to highlight any local (unpublished) changes or lines changed by the most recent commit.

- Adds _Toggle File Changes_ command (`gitlens.toggleFileChanges`) to toggle the changes annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##File Heatmap

<img src="/wp-content/uploads/gutter-heatmap.png" class="help-center-img img-bordered">

Adds an on-demand heatmap to the edge of the file to show how recently lines were changed

- The indicator's [customizable](/gitlens/settings/#file-heatmap-settings) color will either be hot or cold based on the age of the most recent change (cold after 90 days by [default](/gitlens/settings/#file-heatmap-settings))
- The indicator's brightness ranges from bright (newer) to dim (older) based on the relative age, which is calculated from the median age of all the changes in the file
- Adds _Toggle File Heatmap Annotations_ command (`gitlens.toggleFileHeatmap`) to toggle the heatmap on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

## Code Suggest `PREVIEW`

GitKraken Code Suggest simplifies code review by allowing you to make suggestions and edits across the entire project, not just on the lines that were changed, within GitLens, GitKraken Desktop, and gitkraken.dev. When a Pull Request is open, you can make suggestions to the pull request that others can then review and accept to include in the pull request. 

<div class='callout callout--basic'>
    <p>Note: Code Suggest is currently only available for repositories on github.com.</p>
</div>

<img src="/wp-content/uploads/gl-code-suggest.png" class="help-center-img img-bordered">

To begin suggesting changes, open the [GitLens Inspect Overview](/gitlens/side-bar/#overview) for the desired repository and checkout a branch that has an open pull request. From here, you will have the option to _Start Review for PR #PR_. You may begin modifying and saving any file you would like to include in the code suggestion. Once you are ready, select _Suggest Changes for PR_, provide a title, and then finish with _Create Code Suggestion_. 

<img src="/wp-content/uploads/gl-code-suggest-create.gif" class="help-center-img img-bordered">

This will include a comment on the pull request with two options: you can select _Code Suggestion for #PR_ to open the suggestion in gitkraken.dev or select _locally on your machine_ to open the suggestion in GitKraken or GitLens.

<img src="/wp-content/uploads/gl-code-suggest-comment.png" class="help-center-img img-bordered">

When selecting _locally on your machine_ you can open them on GitLens or [GitKraken Desktop](/gitkraken-client/pull-requests/#review-code-and-suggest-changes). Here, you can review the changes by selecting each file and once you are ready, you can select _Apply_ to apply to the branch you currently have checked out or select the dropdown and then _Apply to a Branch_ to apply to a new branch or select an existing branch. This will apply the patch locally. 

<img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" class="help-center-img img-bordered">

When selecting the _Code Suggestion for #PR_ you will be taken to gitkraken.dev to review and accept the changes. Here, you can review the changes by selecting each file and once you are ready, you can select _Commit Suggestions_. This will create a new commit on the remote for the existing branch (shown under _COMMIT SUGGESTIONS TO_). 

<img src="/wp-content/uploads/gl-accept-code-suggestion.gif" class="help-center-img img-bordered">

***

## Cloud Patches `PREVIEW`

### What are Cloud Patches and why would you want to use them

A Cloud Patch is a Git patch that GitKraken securely stores for you so it can be easily shared with others across GitLens, GitKraken Desktop, and the GitKraken CLI. The patch is directly transferred from your machine into secure storage. 

Cloud Patches allow the ability to engage early with your team before a pull request. They can be created as soon as you have a work in progress. This can help with collaborating on changes prior to a pull request and minimize the delay of pull request reviews.

### How to setup Cloud Patches 

To enable Cloud Patches per client, open the user Settings (`command/ctrl + shift + P` > `Preferences: Open User Settings (JSON)`) and set `gitlens.cloudPatches.enabled` to `true` - this is on by default. To disable Cloud Patches per client, set this setting to `false` .

### How to work with Cloud Patches

Cloud Patches can be managed from the Cloud Patches view in the GitLens side bar.

<img src="/wp-content/uploads/gl-cloud-patch-create.webp" class="help-center-img img-bordered">

A Cloud Patch can be created from Working Changes, Commits, Stashes or Comparisons by using the "Share as Cloud Patch" option from the command palette or from the Share submenu in applicable gitlens views. 

<img src="/wp-content/uploads/gl-create-cloud-patch-example.png" class="help-center-img img-bordered">

When creating a Cloud Patch, you have the following sharing options:

- `Anyone with the link`: Anyone that you share the public link with will be able to work with the Cloud Patch.

- `Anyone in my org`: Anyone in the GitKraken Organization will be able to work with the Cloud Patch. They will be required to authenticate with a GitKraken account to access it.

- `Only collaborators`: Only users in the GitKraken Organization who have been selected when sharing will be able to work with the Cloud Patch. They will be required to authenticate with a GitKraken account to access it. Select `Invite` to select desired members.

Cloud Patches shared with you can be viewed in the Cloud Patches section under `Shared with Me`.

<div class='callout callout--basic'>
    <p>Note: If you have multiple organizations, you can easily switch between them from the GitKraken Account view.</p>
</div>

<img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" class="help-center-img img-bordered">

Cloud Patches can be viewed from URLs shared to you and they can be applied to your working tree or to a new or existing branch. Simply select or open the link and then follow the prompts within GitLens to apply the Cloud Patch. 

<img src="/wp-content/uploads/gl-apply-patch-example.gif" class="help-center-img img-bordered">

To delete a cloud patch, right-click it and select `Delete Cloud Patch...`.

<img src="/wp-content/uploads/gl-delete-cloud-patch.png" class="help-center-img img-bordered">

### Self-Hosting Cloud Patch data

If you do not want your Cloud Patch data stored on GitKraken Servers, we offer the ability for you to host Cloud Patches on your own AWS S3 storage instance. For more information on configuring this, see our documentation [here](/gk-dev/gk-dev-home/#self-hosted).

## Commit Graph `PRO`

The commit graph helps visualize your repository commit history and give you information about branches, commits, and collaborators all in one view. This makes it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/commit-graph.png" class="help-center-img img-bordered">

To open the Commit Graph, open the command palette using the keyboard shortcut `Cmd/ctrl + Shift + P` and type “Show Commit Graph”. This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths.

<img src="/wp-content/uploads/show-commit-graph.gif" class="help-center-img img-bordered">

At the top of the commit graph the repository name, the branch name that is currently checked out, and the last fetched time is shown. This section offers the ability to switch branches by selecting the branch name and the ability to fetch by selecting "Fetch".

<img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public or local repositories, and requires no account. Additionally, users with a paid GitLens subscription or trial can use the Commit Graph with private repos. </br></br>

    We’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

### Configuration and Layout

The commit graph can be configured to be shown as desired offering different settings for what to show and how or where to show it.

All columns can be rearranged by dragging and dropping the column headers. The columns can be toggled on/off from the column's context menu via right-click. This enables you to arrange the columns in a way that best suits your workflow and priorities. The Changes column represents added (green) and deleted (red) lines made to each file within the commit.

<img src="/wp-content/uploads/gl-column-settings.png" class="help-center-img img-bordered">

A Commit Graph Panel Layout is offered to show the Commit Graph in the bottom Panel (near the Terminal) with a dedicated Commit Graph Details view alongside the Commit Graph. To switch between the Editor Layout and Panel Layout, select the Commit Graph settings gear located at the top right of the editor. From there, select the "Prefer Commit Graph in Panel Layout" or "Prefer Commit Graph in Editor Area". The Commit Graph can also be opened in both the Penel Layout and Editor Area simultaneously. 

<img src="/wp-content/uploads/gl-prefer-commit-graph-location.png" class="help-center-img img-bordered">

A compact layout for the Graph column is offered in the Commit Graph to reduce the visual complexity and size of the Graph column. To enable the compact layout, right click on the Graph column header, and select the Compact Graph Column Layout option. Additionally the Author column displays avatars instead of text when sized to its minimum width, which pairs nicely with the compact Graph column as you can retain avatars. Also, when the any of the Commit Graph columns are resized small enough so that their text would be truncated, they switch to displaying icons to ensure that crucial information remains visible, even in constrained display settings.

<img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="help-center-img img-bordered">

The scroll markers indicate points of interest on the commit graph such as checked-out branches, selected rows, and search results. This provides the ability to jump to important points like the HEAD or refs. This can be toggled on or off in the [Commit Graph settings](/gitlens/gitlens-features/#settings).

<img src="/wp-content/uploads/gl-scroll-markers.png" class="help-center-img img-bordered">

### Settings

The Commit Graph settings can be adjusted by opening the Command Palette (`command/ctrl + shift + P`) and searching "GitLens: Open Settings".

<img src="/wp-content/uploads/commit-graph-settings.png" class="help-center-img img-bordered">

### Rich Commit Search

The Commit Graph will highlight all matching results across your entire repository when searching for a commit, message, author, a changed file or files, or even a specific code change. Use shortcut keys or the up/down arrows on the search bar  to navigate the search results; `F3` (also `Cmd+G` on macOS) goes to the next result from your selection while  `Shift+F3`  ( also `Shift+Cmd+G` on macOS) goes to the previous.

<img src="/wp-content/uploads/Rich-Commit-Search.png" class="img-responsive center img-bordered">

Once you type search filtering criteria, use the arrow icons to move through each result. Additionally, you can quickly jump to the first or last result, by holding `Shift` while clicking on the up/down arrows respectively.

<img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="img-responsive center img-bordered">

The following options can be used to search:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me`

Additionally, the options on the right side of the search bar can be used to match all, match case, or use regular expression.

<img src="/wp-content/uploads/search-options.png" class="help-center-img img-bordered">

### Full Context Menu Support

You can right-click a branch, commit, tag, author, or column headers (author, commit date / time, or SHA) to interact with them.

<img src="/wp-content/uploads/gl-context-menu.gif" class="help-center-img img-bordered">

Helpful context menu actions: 

- _Compare with Common Base_: to review the changes if the selected branch were to be merged by comparing the common ancestor (merge base) with the current branch to the selected branch
- _Open All Changes with Common Base_: to review the changes if the selected branch were to be merged in the multi-diff editor

### Pull Request Information

For GitHub and GitLab, the commit Graph will display a Pull Request icon for any branch that currently has a pull request. You will need to connect the [rich integration](/gitlens/settings/#remote-provider-integration-settings) in order to see this.

<img src="/wp-content/uploads/pull-request-icon.png" class="help-center-img img-bordered">

### Hiding Remotes, Branches or Tags

The Commit Graph shows refs to your remotes, branches and tags. Hover over any of these refs to access the “Hide” option to help focus your Commit Graph. To show them again, hover over the "Hide" option at the top of the commit graph and select the desired refs.

<img src="/wp-content/uploads/gl-hide-refs.gif" class="help-center-img img-bordered">

Filter options can be accessed from the filter dropdown. This provides the ability to switch between _Show Current Branch Only_ - to show the current branch and its upstream remote - or _Show All Local Branches_ - this is selected by default. Additionally, remote-only branches, stashes and tags can be hidden/shown and merge commit rows can be dimmed.

<img src="/wp-content/uploads/filter-options-2.png" class="help-center-img img-bordered">

### Minimap (Experimental)

The Minimap provides an additional dimension to the Commit Graph. You can quickly see the activity of the repository, see the HEAD/upstream, branches (local and remote), and easily jump to them. Select the Toggle Minimap icon in the right corner of the Commit Graph top bar to toggle the Minimap on and off.

<img src="/wp-content/uploads/gl-minimap-2.png" class="help-center-img img-bordered">

The Minimap can be toggled between showing commits or lines changed by selecting the graph icon dropdown in the top right of the Activity Minimap. Additionally, markers can be toggled on or off from here.

<img src="/wp-content/uploads/gl-minimap-settings.png" class="help-center-img img-bordered">

Minimap Overview:

- Reads left to right - left is the most recent and the right is older
- Highlighted region: Commit Graph area that is in view
- Green Lines: HEAD
- Yellow lines: Search results
- Upper row markers:
    - Blue blocks: remote branches
    - Brown blocks: Tags
- Lower row markers:
    - Pink blocks: stashes
    - Blue blocks: local branches

<div class='callout callout--basic'>
    <p>Note: We would love to hear your feedback regarding the Minimap. Please share it on the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>GitHub Discussion board</a>.</p>
</div>

***

## Launchpad `PRO`

The Launchpad organizes pull requests by status allowing you to identify bottlenecks and take actions on them. This offers the ability to organize and quickly take actions on pull requests with priority.

<img src="/wp-content/uploads/gl-launchpad-quickpick.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Currently, this view is supported for GitHub.com and GitLab.com repositories. In order to see the Launchpad, you will need to connect the <a href="https://help.gitkraken.com/gitlens/gitlens-features/#connecting-the-github-and-gitlab-integration">GitHub Integration</a> .</p>
</div>

The Launchpad can be accessed from the command palette (`command/ctrl + shift + P`) by searching `GitLens: Open Launchpad` or select the Pull Request from the status bar in VS Code.

<img src="/wp-content/uploads/gl-access-launchpad.gif" class="help-center-img img-bordered">

Here you can see a list of all pull requests for your repositories that are ready to merge, blocked, require follow-up, need your review, are waiting for a review, are a draft, or are snoozed. You can select the pull request to see more information about it and take action on it such as open it in a browser, merge (if ready to merge) or switch to the branch/worktree. 

<img src="/wp-content/uploads/gl-view-pull-request.png" class="help-center-img img-bordered">

[Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) can be easily started or reviewed from pull requests in the launchpad actions as well. 

<img src="/wp-content/uploads/gl-launchpad-code-suggest.png" class="help-center-img img-bordered">

You can pin pull requests using the pin icon <i class="fa-solid fa-thumbtack"></i> to move them to the pinned group or snooze them by selecting the snooze icon <i class="fa-solid fa-snooze"></i> to move them into the snooze group. To unpin or unsnooze, select the pin or snooze icon again. 

<img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Note: The Launchpad is currently organized by prioritizing items on the list that require more action by elevating them to the top. This is subject to change in the future.</p>
</div>
<div class='callout callout--warning'>
    <p>This Feature is only available for Pro subscription tiers or higher</p>
</div>

***

## Visual File History

The Visual File History allows you to quickly see the evolution of a file, including when changes were made, how large they were, and who made them.

To access the Visual File History view, open the GitLens Inspect sidebar. Once the sidebar is open, the view will be available. Alternatively, you can open Visual File History from the Command Palette by using (`cmd/ctrl + shift + P`) > GitLens: Show Visual File History View.

<img src="/wp-content/uploads/visual-file-history.png" class="help-center-img img-bordered">

Authors who have contributed changes to the file are on the left y-axis to create a swim-lane of their commits over time (the x-axis). Commit are plotted as color-coded (per-author) bubbles, whose size represents the relative magnitude of the changes.

Additionally, each commit's additions and deletions are visualized as color-coded, stacked, vertical bars, whose height represents the number of affected lines (right y-axis). Added lines are shown in green, while deleted lines are red.


Gain additional insights on hover.

<img src="/wp-content/uploads/visual-file-history-hover.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>Community plan is restricted to Public and Local Repositories only.</p>
</div>

***

## Gitkraken AI
### AI-Generated Commit Messages

Commit messages can be automatically generated using Gitkraken AI.

<img src="/wp-content/uploads/gl-ai-generated-commit-message.gif" class="help-center-img img-bordered">

To generate a commit message, stage the changes you want, then navigate to Home View and tap the "Generate Commit Message" button to generate a precise, descriptive commit messages based on your changes, or run the `GitLens: Generate Commit Message (Experimental)` command from the Command Palette (`command/ctrl + shift + P`). From there you will be guided through the process of accepting to send the diff of your staged changes to Gitkraken AI. Once completed, the generated commit message will be entered into the commit input box on the Source Control sidebar. You can also enter additional context about your changes in the commit box and those will also be sent to help generate a better message. Additionally, you can customize the `gitlens.experimental.generateCommitMessagePrompt` setting to control the prompt used to structure and format the generated commit message. There are additional `gitlens.ai` settings that can be [customized](/gitlens/gitlens-settings/#misc-settings) for the provider and model. 

<div class='callout callout--warning'>
    <p>Gitlens Pro users and above can also choose to provide their own API key in order to use a different AI provider. Gitkraken AI utilizes the Gemini 2.0 Flash model.</p>
</div>

### AI Stash Messages `Pro`
*Available in:* Pro, Advanced, and Business plans
Create intelligent descriptions for stashed changes, making it easier to find and understand your work later. This feature generates context-rich stash descriptions that help you quickly identify the purpose of each stash.
*How to access:*
- From the Command Palette: `GitLens: Generate Stash Message with AI`
- When creating a stash: Look for the AI option in the stash creation interface
- From the stash view: Generate descriptions for existing stashes

### AI Commit Explanations`Pro`
*Available in:* Pro, Advanced, and Business plans
Understand the reasoning behind changes with AI-generated explanations of commit content and purpose. Quickly grasp the intent and impact of complex commits without having to manually review all changed files.

*How to access:*
- In the "Commit Details" view: Find the AI explanation panel
- In the "Cloud Patch Details" view: Look for explanations alongside commit information
- When reviewing commits: Option to generate explanations for any selected commit

### AI Changelog Creation `Advanced`
*Available in:* Advanced and Business plans only
Automatically generate comprehensive changelogs from selected commits in the Graph, perfect for release documentation. Maintain consistent and detailed changelogs without manual effort.
*How to access:*
- In the Search/Compare view: Click the inline button on the "commits" line
- When selecting multiple commits in the Graph: Right-click and choose "Generate Changelog"
- From the Command Palette: `GitLens: Generate Changelog from Commits`

<div class='callout callout--basic'>
    <p>More questions about Gitkraken AI? Please see our <a href="https://help.gitkraken.com/general/gitkraken-ai-faq/">GitKraken AI FAQ page</a> for more details</p>
</div>

***

## Git Command Palette

<img src="/wp-content/uploads/git-command-palette.png" class="help-center-img img-bordered">

Adds a [customizable](/gitlens/settings/#git-command-palette-settings) Git Command Palette command (`gitlens.gitCommands`) to provide guided (step-by-step) access to many common Git commands, as well as quick access to commit history and search, stashes, and more

- Quickly navigate and execute Git commands through easy-to-use menus where each command can require an explicit confirmation step before executing

###Quick Commit Access

- Adds a Show Branch History command (`gitlens.showQuickBranchHistory`) to show a quick pick menu to explore the commit history of the selected branch
- Adds a Show Current Branch History command (`gitlens.showQuickRepoHistory`) to show a quick pick menu to explore the commit history of the current branch

<img src="/wp-content/uploads/menu-branch-history.png" class="help-center-img img-bordered">

- Adds a Show File History command (`gitlens.showQuickFileHistory`) to show quick pick menu to explore the commit history of the current file

<img src="/wp-content/uploads/menu-file-history.png" class="help-center-img img-bordered">

Adds a Search Commits command (`gitlens.showCommitSearch`) to show quick pick menu to search for commits

- by message — use `<message>` to find commits with messages that match `<message>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---grepltpatterngt' target='_blank'>Git docs</a>
- or, by author — use `@<pattern>` to find commits with authors that match `<pattern>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---authorltpatterngt' target='_blank'>Git docs</a>
- or, by commit SHA — use `#<sha>` to find a commit with id of `<sha>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt-ltrevisionrangegt' target='_blank'>Git docs</a>
- or, by files — use `:<path/glob>` to find commits with file names that match `<path/glob>` — See  <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---ltpathgt82308203' target='_blank'>Git docs</a>
- or, by changes — use `~<pattern>` to find commits with differences whose patch text contains added/removed lines that match `<pattern>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt--Gltregexgt' target='_blank'>Git docs</a>

<img src="/wp-content/uploads/menu-commit-search.png" class="help-center-img img-bordered">

- Adds a _Show Commit_ command (`gitlens.showQuickCommitDetails`) to show a quick pick menu to explore a commit and take action upon it

<img src="/wp-content/uploads/menu-commit-details.png" class="help-center-img img-bordered">

Adds a _Show Line Commit_ command `(gitlens.showQuickCommitFileDetails`) to show a quick pick menu to explore a file of a commit and take action upon it

<img src="/wp-content/uploads/menu-commit-file-details.png" class="help-center-img img-bordered">

###Quick Stash Access

<img src="/wp-content/uploads/menu-stash-list.png" class="help-center-img img-bordered">

<img src="/wp-content/uploads/menu-stash-details.png" class="help-center-img img-bordered">

- Adds a _Show Stashes_ command (`gitlens.showQuickStashList`) to show a quick pick menu to explore your stashes

###Quick Status Access

- Adds a _Show Repository Status_ command (`gitlens.showQuickRepoStatus`) to show a quick pick menu to for visualizing the current repository status

<img src="/wp-content/uploads/menu-repo-status.png" class="help-center-img img-bordered">

***

##Interactive Rebase Editor

<img src="/wp-content/uploads/rebase.gif" class="help-center-img img-bordered">

Adds a user-friendly interactive rebase editor to more easily configure an interactive rebase session

- Quickly re-order, edit, squash, and drop commits
- Includes drag & drop support!

To use this directly from your terminal, e.g. when running `git rebase -i`:

- set VS Code as your default Git editor
    - `git config --global core.editor "code --wait"`
- or, to only affect rebase, set VS Code as your Git rebase editor
    - `git config --global sequence.editor "code --wait"`

To use the Insiders edition of VS Code, replace `code` in the above with `code-insiders`

***

## Autolinks

Use autolinks to linkify external references, like Jira issues or Zendesk tickets, in commit messages.

<img src="/wp-content/uploads/gl-autolinks.png" class="help-center-img img-bordered">

##Terminal Links

<img src="/wp-content/uploads/terminal-links.gif" class="help-center-img img-bordered">

- [Optionally](/gitlens/settings/#terminal-links-settings) adds autolinks for branches, tags, and commit ranges in the integrated terminal to quickly explore their commit history
- [Optionally](/gitlens/settings/#terminal-links-settings) adds autolinks for commits in the integrated terminal to quickly explore the commit and take action upon it

***

## Remote Provider Integrations

GitLens provides rich integrations with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/settings/#remote-provider-integration-settings) as well.

Basic integrations provide issue and pull request auto-linking, while richer integrations (e.g. GitHub or GitLab) offer the ability to work with the Launchpad, can provide rich hover information provided for auto-linked issues and pull requests, associate pull requests with branches and commits, and provide avatars.

Additionally, these integrations provide commands to copy the url of or open, files, commits, branches, and the repository on the remote provider.

- Open _File from Remote_ command (`gitlens.openFileFromRemote`) — opens the local file from a url of a file on a remote provider
- Open _File on Remote_ command (`gitlens.openFileOnRemote`) — opens a file or revision on the remote provider
- Copy _Remote File Url_ command (`gitlens.copyRemoteFileUrlToClipboard`) — copies the url of a file or revision on the remote provider
- Open _File on Remote From..._ command (`gitlens.openFileOnRemoteFrom`) — opens a file or revision on a specific branch or tag on the remote provider
- Copy _Remote File Url From..._ command (`gitlens.copyRemoteFileUrlFrom`) — copies the url of a file or revision on a specific branch or tag the remote provider
- Open _Commit on Remote_ command (`gitlens.openCommitOnRemote`) — opens a commit on the remote provider
- Copy _Remote Commit Url_ command (`gitlens.copyRemoteCommitUrl`) — copies the url of a commit on the remote provider
- Open _Branch on Remote_ command (`gitlens.openBranchOnRemote`) — opens the branch on the remote provider
- Copy _Remote Branch Url_ command (`gitlens.copyRemoteBranchUrl`) — copies the url of a branch on the remote provider
- Open _Branches on Remote_ command (`gitlens.openBranchesOnRemote`) — opens the branches on the remote provider
- Copy _Remote Branches Url_ command (`gitlens.copyRemoteBranchesUrl`) — copies the url of the branches on the remote provider
- Open _Comparison on Remote_ command (`gitlens.openComparisonOnRemote`) — opens the comparison on the remote provider
- Copy _Remote Comparison Url_ command (`gitlens.copyRemoteComparisonUrl`) — copies the url of the comparison on the remote provider
- Open _Pull Request_ command (`gitlens.openPullRequestOnRemote`) — opens the pull request on the remote provider
- Copy _Pull Request Url_ command (`gitlens.copyRemotePullRequestUrl`) — copies the url of the pull request on the remote provider
- Open _Repository on Remote_ command (`gitlens.openRepoOnRemote`) — opens the repository on the remote provider
- Copy _Remote Repository Url_ command (`gitlens.copyRemoteRepositoryUrl`) — copies the url of the repository on the remote provider

### Connecting the GitHub and GitLab Integration

The GitHub and GitLab integration are connected via your GitKraken account from [gitkraken.dev](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens). To connect an integration, open the Command Palette (`command/ctrl+shift+P`) and type `GitLens: Manage Integrations`. You can also navigate to GitKraken Account in the GitLens Activity Bar and select `Integrations`. 

<img src="/wp-content/uploads/gl-connect-remote-integration.png" srcset="/wp-content/uploads/gl-connect-remote-integration@2x.png" class="help-center-img img-bordered">

You will be prompted to log into your GitKraken account if you are not already. Then, select `Connect with GitHub` or `Connect with GitLab` and sign into the desired service. You will have the option to connect multiple integrations if needed. Finish the process by selecting `Complete Setup` to hop back into VS Code and begin working with the integrations. 

<img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>Community users are limited to basic functionality only.</p>
</div>

## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro offers a richer integration with GitHub Enterprise Server and GitLab Self-Managed.

Once authenticated, GitLens will enrich GitHub Enterprise Server or GitLab Self-Managed autolinks in the hovers. You’ll see your GitHub Enterprise Server or GitLab Self-Managed avatar, links to related pull requests, along with a footnote of the pull request or issue details. You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

<img src="/wp-content/uploads/gitlab-github-integration.png" class="help-center-img img-bordered">

### Connecting GitHub Enterprise Server or GitLab Self-Managed

To connect either the GitHub Enterprise Server or GitLab Self-Managed integration:

- Open the `settings.json` - this can be done from the command palette  (`command/ctrl + shift + P`) > _Preferences: Open User Settings (JSON)_

- Provide a _gitlens.remote_ with a _domain_ and a _type_ with the below format - for more information on the formatting see the [remote provider integration settings](/gitlens/settings/#remote-provider-integration-settings)

Format Example: 

```
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or

```
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

- Open a GitHub Enterprise Server or GitLab Self-Managed repository in VS Code

- Open the [Remotes View](/gitlens/side-bar/#remotes-view)

- Select <i class="fa-solid fa-plug"></i> _Connect to Remote_ - if you do not see this option, check that the format of the settings.json matches the example above

<img src="/wp-content/uploads/gl-connect-to-remote-ghe.png" class="help-center-img img-bordered">

- You will then be prompted to provide a PAT with the required scopes and can hit _Enter_ to complete the integration connection

***

## Jira Integration `PRO`

The Jira Integration connected through your GitKraken Account gives you access to Jira [Autolinks](/gitlens/gitlens-features#autolinks) anywhere autolinks are supported in GitLens. Simply connect the integration and GitLens will automatically convert Jira IDs in commit messages to links i.e. `ABC-123`.

<img src="/wp-content/uploads/gl-jira-integration.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>This Feature is only available for Pro subscription tiers or higher</p>
</div>

To connect the integration, open the GitLens Sidebar, select `Cloud Integrations` from the GitKraken Account view, select Jira Cloud, and proceed with the integration connection by allowing GitKraken access to your Atlassian Account. You can also open [Integration Settings](gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

<img src="/wp-content/uploads/gl-cloud-integrations.png" class="help-center-img img-bordered">

***

##Powerful Commands

- Adds an _Add Co-authors_ command (`gitlens.addAuthors`) to add a co-author to the commit message input box

- Adds a _Copy SHA_ command (`gitlens.copyShaToClipboard`) to copy the commit SHA of the current line to the clipboard or from the most recent commit to the current branch, if there is no current editor

- Adds a _Copy Message_ command (`gitlens.copyMessageToClipboard`) to copy the commit message of the current line to the clipboard or from the most recent commit to the current branch, if there is no current editor

- Adds a _Copy Current Branch_ command (`gitlens.copyCurrentBranch`) to copy the name of the current branch to the clipboard

- Adds a _Switch to Another Branch_ (`gitlens.views.switchToAnotherBranch`) command — to quickly switch the current branch

- Adds a _Compare References..._ command (`gitlens.compareWith`) to compare two selected references

- Adds a _Compare HEAD with..._ command (`gitlens.compareHeadWith`) to compare the index (HEAD) with the selected reference

- Adds a _Compare Working Tree with..._ command (`gitlens.compareWorkingWith`) to compare the working tree with the selected reference

- Adds an _Open Changes (difftool)_ command (`gitlens.externalDiff`) to open the changes of a file or set of files with the configured git difftool

- Adds an _Open All Changes (difftool)_ command (`gitlens.externalDiffAll`) to open all working changes with the configured git difftool

- Adds an _Open Directory Compare (difftool)_ command (`gitlens.diffDirectoryWithHead`) to compare the working tree with HEAD with the configured Git difftool

- Adds an _Open Directory Compare (difftool) with..._ command (`gitlens.diffDirectory`) to compare the working tree with the selected reference with the configured Git difftool

- Adds an _Open File_ command (`gitlens.openWorkingFile`) to open the working file for the current file revision

- Adds an _Open Revision..._ command (`gitlens.openFileRevision`) to open the selected revision for the current file

- Adds an _Open Revision from..._ command (`gitlens.openFileRevisionFrom`) to open the revision of the current file from the selected reference

- Adds an _Open Blame Prior to Change_ command (`gitlens.openBlamePriorToChange`) to open the blame of prior revision of the selected line in the current file

- Adds a _Open Changed Files_ command (`gitlens.openChangedFiles`) to open any files with working tree changes

- Adds a _Close Unchanged Files_ command (`gitlens.closeUnchangedFiles`) to close any files without working tree changes

- Adds an _Enable Debug Logging_ command (`gitlens.enableDebugLogging`) to enable debug logging to the GitLens output channel

- Adds a _Disable Debug Logging_ command (`gitlens.disableDebugLogging`) to disable debug logging to the GitLens output channel

- Adds a _Copy as Patch_ context menu command (`gitlens.copyPatchToClipboard`) on files, commits, stashes, and comparisons in GitLens views. Additionally, this context menu command can be used on files in the _Changes_ and _Staged Changes_ groups as well as the groups themselves in the _Source Control_ view

- Adds a _Apply Copied Patch_ command (`gitlens.applyPatchFromClipboard`) in the command palette to apply a patch from the clipboard

***

##Deep Links

Deep Links are links that can be used to quickly open up a resource within GitLens. With Deep Linking support, you can improve collaboration and communication by seamless sharing important information related to your Git repositories via a link. There are many resources in GitLens that offer the ability to generate Deep Links:

- _Search & Compare_: Link directly into comparisons in the [Search & Compare view](/gitlens/side-bar/#search-compare-view) for viewing comparisons between branches, tags, and commits. To generate a Deep Link, right-click a comparison, hover over _Share_, and select _Copy Link to Comparison_. 
- _GitKraken Workspaces_: Link directly to a [GitKraken Workspace](/gitlens/side-bar/#workspaces-☁%ef%b8%8f). To generate a Deep Link, right-click a Workspace, hover over _Share_, and select _Copy Link to Workspace_. 
- _Commit Graph_: Link to open up a resource within the [Commit Graph](gitlens/gitlens-features/#commit-graph-%60pro%60) of GitLens such as specific remote repositories, commits, branches, and tags. To generate a Deep Link, right-click the desired resource, hover over _Share_ and select _Copy Link to <resource>_.
- _Files or Lines_: Link directly to files or lines of code. To generate a Deep Link, right-click highlighted lines of code or a file, hover over _Share_ and select _Copy vscode.dev Link_.
- _Cloud Patches_: Link directly to open up a [Cloud Patch](/gitlens/gitlens-features/#cloud-patches-preview-%e2%98%81%ef%b8%8f). To generate a Deep Link, generate a Cloud Patch and select _Copy Link_ from the success prompt.

<img src="/wp-content/uploads/gl-deep-link-example.gif" class="help-center-img img-bordered">

***

##Menus & Toolbars

<img src="/wp-content/uploads/menus.png" class="help-center-img img-bordered">

GitLens provides [customizable](/gitlens/gitlens-settings/#elementor-toc__heading-anchor-16) menu and toolbar contributions to put you in control over where GitLens' commands are shown. The easiest way to configure these settings is via the GitLens [interactive settings editor](/gitlens/gitlens-settings/).

For example, if you uncheck the _Add to the editor group toolbar_ you will see the following items removed from the toolbar:

<img src="/wp-content/uploads/menus-example.png" class="help-center-img img-bordered">

You can also expand each group to control each area more granularly.

***

##Modes

GitLens supports [user-defined](#modes-settings- 'Jump to the Modes settings') modes for quickly toggling between sets of settings.

- Adds the active mode to the **status bar** ([optional](#modes-settings- 'Jump to the Modes settings'), on by default)
  - Adds _Toggle Review Mode_ command (`gitlens.toggleReviewMode`) to toggle Review mode
- Adds _Switch Mode_ command (`gitlens.switchMode`) to quickly switch the active mode
- Adds a _Zen_ mode which for a zen-like experience, disables many visual features
  - Adds _Toggle Zen Mode_ command (`gitlens.toggleZenMode`) to toggle Zen mode
- Adds a _Review_ mode which for reviewing code, enables many visual features

### Experimental Multi-diff Editor

You can open changes in VS Code's new multi-diff editor. This requires VS Code 1.86 or later.

#### Commands using Multi-diff

- `Open Folder Changes with Revision...` and `Open Folder Changes with Branch or Tag...` commands using the Command Palette as well as the Explorer and Source Control views
- An inline `Open All Changes` command for commits, stashes, and comparisons in the views
- `Open All Changes` and `Open All Changes with Working Tree` will use the new multi-diff editor when enabled 
- `Open All Changes, Individually` and `Open All Changes with Working Tree, Individually` commands were added to provide access to the previous behavior