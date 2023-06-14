---

title: GitLens Features
description: GitLens Features
taxonomy:
    category: gitlens

---

All features are **completely free** for use on all repos, except for ones marked with:

- ✨ require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos
- ☁️ require an account and access is based on your plan, e.g. Free, Pro, etc

***

##Revision Navigation

<img src="/wp-content/uploads/revision-navigation.gif" class="img-bordered img-responsive center">

- Adds an _Open Changes with Previous Revision_ command (`gitlens.diffWithPrevious`) to compare the current file or revision with the previous commit revision
- Adds an _Open Changes with Next Revision_ command (`gitlens.diffWithNext`) to compare the current file or revision with the next commit revision
- Adds an _Open Line Changes with Previous Revision_ command (`gitlens.diffLineWithPrevious`) to compare the current file or revision with the previous line commit revision
- Adds an _Open Changes with Working File_ command (`gitlens.diffWithWorking`) to compare the current revision or most recent commit revision of the current file with the working tree
- Adds an _Open Line Changes with Working File_ command (`gitlens.diffLineWithWorking`) to compare the commit revision of the current line with the working tree
- Adds an _Open Changes with Branch or Tag..._ command (`gitlens.diffWithRevisionFrom`) to compare the current file or revision with another revision of the same file on the selected reference
- Adds an _Open Changes with Revision..._ command (`gitlens.diffWithRevision`) to compare the current file or revision with another revision of the same file

***

##Current Line Blame

<img src="/wp-content/uploads/current-line-blame.png" class="img-bordered img-responsive center">

Adds an unobtrusive, [customizable](/gitlens/settings/#current-line-blame-settings), and [themable](/gitlens/settings/#themable-colors), **blame annotation** at the end of the current line.

- Contains the author, date, and message of the current line's most recent commit (by [default](/gitlens/settings/#current-line-blame-settings))
- Adds a _Toggle Line Blame Annotations_ (`gitlens.toggleLineBlame`) to toggle the blame annotation on and off

***

##Git CodeLens

<img src="/wp-content/uploads/code-lens.png" class="img-bordered img-responsive center">


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

<img src="/wp-content/uploads/status-bar.png" class="img-bordered img-responsive center">

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

<img src="/wp-content/uploads/hovers-current-line.png" class="img-bordered img-responsive center">

Adds [customizable](/gitlens/settings/#hover-settings) Git blame hovers accessible over the current line

####Details Hover

<img src="/wp-content/uploads/hovers-current-line-details.png" class="img-bordered img-responsive center">

Adds a **details hover** annotation to the current line to show more commit details (optional, on by default)

- Provides **automatic issue linking** to Bitbucket, Gerrit, Gitea, GitHub, GitLab, and Azure DevOps in commit messages
- Provides a **quick-access command bar** with _Open Changes_, _Blame Previous Revision_, _Open on Remote_, _Invite to Live Share_ (if available), and _Show More Actions_ command buttons
- Click the commit SHA to execute the _Show Commit_ command

####Changes (diff) Hover

<img src="/wp-content/uploads/hovers-current-line-changes.png" class="img-bordered img-responsive center">


Adds a changes (diff) hover annotation to the current line to show the line's previous version ([optional](/gitlens/settings/#hover-settings), on by default)
- Click the Changes to execute the _Open Changes_ command
- Click the current and previous commit SHAs to execute the _Show Commit_ command

###Annotation Hovers

<img src="/wp-content/uploads/hovers-annotations.png" class="img-bordered img-responsive center">

Adds [customizable](/gitlens/settings/#hover-settings)  Git blame hovers accessible when annotating


####Details Hover

<img src="/wp-content/uploads/hovers-annotations-details.png" class="img-bordered img-responsive center">

Adds a **details hover** annotation to each line while annotating to show more commit details ([optional](/gitlens/settings/#hover-settings), on by default)

- Provides **automatic issue linking** to Bitbucket, Gerrit, Gitea, GitHub, GitLab, and Azure DevOps in commit messages
- Provides a quick-access command bar with _Open Changes_, _Blame Previous Revision_, _Open on Remote_, _Invite to Live Share_ (if available), and _Show More Actions_ command buttons
- Click the commit SHA to execute the _Show Commit_ command

####Changes (diff) Hover

<img src="/wp-content/uploads/hovers-annotations-changes.png" class="img-bordered img-responsive center">

Adds a **changes (diff) hover** annotation to each line while annotating to show the line's previous version ([optional](/gitlens/settings/#hover-settings), on by default)

- Click the **Changes** to execute the _Open Changes_ command
- Click the current and previous commit SHAs to execute the _Show Commit_ command

***

##File Blame

<img src="/wp-content/uploads/gutter-blame.png" class="img-bordered img-responsive center">

Adds on-demand, [customizable](/gitlens/settings/#gutter-blame-settings), and [themable](/gitlens/settings/#themable-colors), file blame annotations to show the commit and author who last modified each line of a file

- Contains the commit message and date, by [default](/gitlens/settings/#gutter-blame-settings)
- Adds a heatmap (age) indicator on right edge (by [default](/gitlens/settings/#gutter-blame-settings),) of the file to provide an easy, at-a-glance way to tell how recently lines were changed (optional, on by default)
- See the [file heatmap](/gitlens/gitlens-features/#file-heatmap) section below for more details
- Adds a Toggle File Blame Annotations command (`gitlens.toggleFileBlame`) with a shortcut of <kbd>alt+b</kbd> to toggle the blame annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##File Changes

<img src="/wp-content/uploads/gutter-blame.png" class="img-bordered img-responsive center">

Adds an on-demand, [customizable](/gitlens/settings/#gutter-changes-settings), and [themable](/gitlens/settings/#themable-colors), file changes annotation to highlight any local (unpublished) changes or lines changed by the most recent commit.

- Adds _Toggle File Changes_ command (`gitlens.toggleFileChanges`) to toggle the changes annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##File Heatmap

<img src="/wp-content/uploads/gutter-heatmap.png" class="img-bordered img-responsive center">

Adds an on-demand heatmap to the edge of the file to show how recently lines were changed

- The indicator's [customizable](/gitlens/settings/#gutter-heatmap-settings) color will either be hot or cold based on the age of the most recent change (cold after 90 days by [default](/gitlens/settings/#gutter-heatmap-settings))
- The indicator's brightness ranges from bright (newer) to dim (older) based on the relative age, which is calculated from the median age of all the changes in the file
- Adds _Toggle File Heatmap Annotations_ command (`gitlens.toggleFileHeatmap`) to toggle the heatmap on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

## Commit Graph ✨

The commit graph helps visualize your repository commit history and give you information about branches, commits, and collaborators all in one view. This makes it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/commit-graph.png" class="img-bordered img-responsive center">

To open the Commit Graph, open the command palette using the keyboard shortcut `Cmd/ctrl + Shift + P` and type “Show Commit Graph”. This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths.

<img src="/wp-content/uploads/show-commit-graph.gif" class="img-bordered img-responsive center">

At the top of the commit graph the repository name, the branch name that is currently checked out, and the last fetched time is shown. This section offers the ability to switch branches by selecting the branch name and the ability to fetch by selecting "Fetch".

<img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="img-bordered img-responsive center">

<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens subscription or trial can use the Commit Graph with private repos. </br></br>

    We’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

### Configuration and Layout

The commit graph can be configured to be shown as desired offering different settings for what to show and how or where to show it.

All columns can be rearranged by dragging and dropping the column headers. The columns can be toggled on/off from the column's context menu via right-click. This enables you to arrange the columns in a way that best suits your workflow and priorities. The Changes column represents added (green) and deleted (red) lines made to each file within the commit.

<img src="/wp-content/uploads/gl-column-settings.png" class="img-bordered img-responsive center">

A Commit Graph Panel Layout is offered to show the Commit Graph in the bottom Panel (near the Terminal) with a dedicated Commit Graph Details view alongside the Commit Graph. To switch between the Editor Layout and Panel Layout, select the Commit Graph settings cog located at the top right of the editor. From there, select the "Switch Commit Graph to Panel Layout" or "Switch Commit Graph to Editor Layout".

<img src="/wp-content/uploads/gl-commit-graph-panel-layout-change.gif" class="img-bordered img-responsive center">

A compact layout for the Graph column is offered in the Commit Graph to reduce the visual complexity and size of the Graph column. To enable the compact layout, right click on the Graph column header, and select the Compact Graph Column Layout option. Additionally the Author column displays avatars instead of text when sized to its minimum width, which pairs nicely with the compact Graph column as you can retain avatars. Also, when the any of the Commit Graph columns are resized small enough so that their text would be truncated, they switch to displaying icons to ensure that crucial information remains visible, even in constrained display settings.

<img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="img-bordered img-responsive center">

The scroll markers indicate points of interest on the commit graph such as checked-out branches, selected rows, and search results. This provides the ability to jump to important points like the HEAD or refs. This can be toggled on or off in the [Commit Graph settings](/gitlens/gitlens-plus/#settings).

<img src="/wp-content/uploads/gl-scroll-markers.png" class="img-bordered img-responsive center">

### Settings

The Commit Graph settings can be adjusted by opening the Command Palette (`command/ctrl + shift + P`) and searching "GitLens: Open Settings".

<img src="/wp-content/uploads/commit-graph-settings.png" class="img-bordered img-responsive center">

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

<img src="/wp-content/uploads/search-options.png" class="img-bordered img-responsive center">

### Full Context Menu Support

You can right-click a branch, commit, tag, author, or column headers (author, commit date / time, or SHA) to interact with them.

<img src="/wp-content/uploads/gl-context-menu.gif" class="img-bordered img-responsive center">

Context menu actions include but are not limited to:

- Switch to Branch
- Revert Commit
- Switch to Commit
- Create Branch
- Merge
- Rebase
- Create Worktree
- Create Pull Request

### Pull Request Information

For GitHub and GitLab, the commit Graph will display a Pull Request icon for any branch that currently has a pull request. You will need to connect the [rich integration](/gitlens/settings/#remote-provider-integration-settings) in order to see this.

<img src="/wp-content/uploads/pull-request-icon.png" class="img-bordered img-responsive center">

### Hiding Remotes, Branches or Tags

The Commit Graph shows refs to your remotes, branches and tags. Hover over any of these refs to access the “Hide” option to help focus your Commit Graph. To show them again, hover over the "Hide" option at the top of the commit graph and select the desired refs.

<img src="/wp-content/uploads/gl-hide-refs.gif" class="img-bordered img-responsive center">

Filter options can be accessed from the filter dropdown. This provides the ability to switch between _Show Current Branch Only_ - to show the current branch and its upstream remote - or _Show All Local Branches_ - this is selected by default. Additionally, remote-only branches, stashes and tags can be hidden/shown and merge commit rows can be dimmed.

<img src="/wp-content/uploads/filter-options-2.png" class="img-bordered img-responsive center">

### Minimap (Experimental)

The Minimap provides an additional dimension to the Commit Graph. You can quickly see the activity of the repository, see the HEAD/upstream, branches (local and remote), and easily jump to them. Select the Toggle Minimap icon in the right corner of the Commit Graph top bar to toggle the Minimap on and off.

<img src="/wp-content/uploads/gl-minimap-2.png" class="img-bordered img-responsive center">

The Minimap can be toggled between showing commits or lines changed by selecting the graph icon dropdown in the top right of the Activity Minimap. Additionally, markers can be toggled on or off from here.

<img src="/wp-content/uploads/gl-minimap-settings.png" class="img-bordered img-responsive center">

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

### Deep Linking

Deep Links are links that can be used to open up a resource within the Commit Graph of GitLens. This provides the ability to easily share specific remote repositories, commits, branches, and tags. To generate a deep link right-click the desired resource, hover over _Share_ and select _Copy Link to \<resource\>_.

<img src="/wp-content/uploads/gl-deep-link.png" class="img-bordered img-responsive center">

***

## Focus View ☁️

The Focus View allows you to stream line your workflow by providing a summarized list of your pull requests and your issues. To open the Focus View, open the command palette (`command/ctrl + shift + P`) and search `GitLens+: Show Focus view`.

Currently, this view is supported for GitHub repositories. In order to see the Focus View, you will need to connect the [GitHub Integration](/gitlens/gitlens-features/#connecting-the-github-integration).

<img src="/wp-content/uploads/gl-focus-view-3.png" class="img-bordered img-responsive center">

The Focus View includes the following sections:
- My Pull Requests: Shows all PRs opened by you, assigned to you, or awaiting your review
- My Issues: Shows all issues created by you, assigned to you, or that mention you.

The Focus View offers the ability to create or open a worktree or branch from Pull Requests using the arrow and folder icon.

<img src="/wp-content/uploads/gl-focus-view-create-worktree-create-branch.png" class="img-bordered img-responsive center">

<div class='callout callout--basic'>
    <p>Note: The Focus View is currently organized by prioritizing items on the list that require more action by elevating them to the top. This is subject to change in the future.</p>
</div>

***

## Visual File History ✨

The Visual File History allows you to quickly see the evolution of a file, including when changes were made, how large they were, and who made them.

Authors who have contributed changes to the file are on the left y-axis to create a swim-lane of their commits over time (the x-axis). Commit are plotted as color-coded (per-author) bubbles, whose size represents the relative magnitude of the changes.

Additionally, each commit's additions and deletions are visualized as color-coded, stacked, vertical bars, whose height represents the number of affected lines (right y-axis). Added lines are shown in green, while deleted lines are red.

<img src="/wp-content/uploads/visual-file-history.png" class="img-bordered img-responsive center">

Gain additional insights on hover.

<img src="/wp-content/uploads/visual-file-history-hover.png" class="img-bordered img-responsive center">

***

## AI-Generated Commit Messages (Experimental) ✨

Commit messages can be automatically generated using [OpenAI](https://openai.com/).

<img src="/wp-content/uploads/gl-ai-generated-commit-message.gif" class="img-bordered img-responsive center">

To connect OpenAI, stage some changes you want to generate a commit message for and then run the `GitLens: Generate Commit Message (Experimental)` command from the Command Palette (`command/ctrl + shift + P`). From there you will be guided through the process of accepting to send the diff of your staged changes to OpenAI and the entry of your OpenAI key. The OpenAI API key can be created [here](https://platform.openai.com/account/api-keys). Once completed, the generated commit message will be entered into the commit input box on the Source Control sidebar. You can also enter additional context about your changes in the commit box and those will also be sent to help generate a better message. Additionally, you can customize the `gitlens.experimental.generateCommitMessagePrompt` setting to control the prompt used to structure and format the generated commit message.

To remove your OpenAI API key in GitLens, run the command `GitLens: Reset Stored OpenAI Key` from the Command Palette.

***

##Git Command Palette

<img src="/wp-content/uploads/git-command-palette.png" class="img-bordered img-responsive center">

Adds a [customizable](/gitlens/settings/#git-command-palette-settings) Git Command Palette command (`gitlens.gitCommands`) to provide guided (step-by-step) access to many common Git commands, as well as quick access to commit history and search, stashes, and more

- Quickly navigate and execute Git commands through easy-to-use menus where each command can require an explicit confirmation step before executing

###Quick Commit Access

- Adds a Show Branch History command (`gitlens.showQuickBranchHistory`) to show a quick pick menu to explore the commit history of the selected branch
- Adds a Show Current Branch History command (`gitlens.showQuickRepoHistory`) to show a quick pick menu to explore the commit history of the current branch

<img src="/wp-content/uploads/menu-branch-history.png" class="img-bordered img-responsive center">

- Adds a Show File History command (`gitlens.showQuickFileHistory`) to show quick pick menu to explore the commit history of the current file

<img src="/wp-content/uploads/menu-file-history.png" class="img-bordered img-responsive center">

Adds a Search Commits command (`gitlens.showCommitSearch`) to show quick pick menu to search for commits

- by message — use `<message>` to find commits with messages that match `<message>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---grepltpatterngt' target='_blank'>Git docs</a>
- or, by author — use `@<pattern>` to find commits with authors that match `<pattern>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---authorltpatterngt' target='_blank'>Git docs</a>
- or, by commit SHA — use `#<sha>` to find a commit with id of `<sha>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt-ltrevisionrangegt' target='_blank'>Git docs</a>
- or, by files — use `:<path/glob>` to find commits with file names that match `<path/glob>` — See  <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt---ltpathgt82308203' target='_blank'>Git docs</a>
- or, by changes — use `~<pattern>` to find commits with differences whose patch text contains added/removed lines that match `<pattern>` — See <a href='https://git-scm.com/docs/git-log#Documentation/git-log.txt--Gltregexgt' target='_blank'>Git docs</a>

<img src="/wp-content/uploads/menu-commit-search.png" class="img-bordered img-responsive center">

- Adds a _Show Commit_ command (`gitlens.showQuickCommitDetails`) to show a quick pick menu to explore a commit and take action upon it

<img src="/wp-content/uploads/menu-commit-details.png" class="img-bordered img-responsive center">

Adds a _Show Line Commit_ command `(gitlens.showQuickCommitFileDetails`) to show a quick pick menu to explore a file of a commit and take action upon it

<img src="/wp-content/uploads/menu-commit-file-details.png" class="img-bordered img-responsive center">

###Quick Stash Access

<img src="/wp-content/uploads/menu-stash-list.png" class="img-bordered img-responsive center">

<img src="/wp-content/uploads/menu-stash-details.png" class="img-bordered img-responsive center">

- Adds a _Show Stashes_ command (`gitlens.showQuickStashList`) to show a quick pick menu to explore your stashes

###Quick Status Access

- Adds a _Show Repository Status_ command (`gitlens.showQuickRepoStatus`) to show a quick pick menu to for visualizing the current repository status

<img src="/wp-content/uploads/menu-repo-status.png" class="img-bordered img-responsive center">

***

##Interactive Rebase Editor

<img src="/wp-content/uploads/rebase.gif" class="img-bordered img-responsive center">

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

<img src="/wp-content/uploads/gl-autolinks.png" class="img-bordered img-responsive center">

##Terminal Links

<img src="/wp-content/uploads/terminal-links.gif" class="img-bordered img-responsive center">

- [Optionally](/gitlens/settings/#terminal-links-settings) adds autolinks for branches, tags, and commit ranges in the integrated terminal to quickly explore their commit history
- [Optionally](/gitlens/settings/#terminal-links-settings) adds autolinks for commits in the integrated terminal to quickly explore the commit and take action upon it

***

##Remote Provider Integrations
GitLens provides rich integrations with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/settings/#remote-provider-integration-settings) as well.

Basic integrations provide issue and pull request auto-linking, while richer integrations (e.g. GitHub) can provide rich hover information provided for auto-linked issues and pull requests, associate pull requests with branches and commits, and provide avatars.

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

###Connecting the GitHub Integration

To connect the GitHub integration, open a GitHub.com repository in Visual Studio Code. Then, select a file and hover over the line blame to get the details hover. From here, select `Connect to GitHub`.

<img src="/wp-content/uploads/gl-connect-to-github.png" class="img-bordered img-responsive center">

If you are prompted to sign in using GitHub, select `Allow`.

<img src="/wp-content/uploads/gh-sign-in.png" class="img-bordered img-responsive center">

Finally, you will be taken to a browser where you will be prompted to sign into GitHub and `Authorize Visual-Studio-Code` to finish connecting. 

<img src="/wp-content/uploads/gh-authorize.png" class="img-bordered img-responsive center">

###Connecting the GitLab Integration

To connect the GitLab integration, open a GitLab.com repository in Visual Studio Code. Then, select a file and hover over the line blame to get the details hover. From here, select the option to `Connect to GitLab`.

<img src="/wp-content/uploads/gl-connect-to-gitlab.png" class="img-bordered img-responsive center">

Next, you will be prompted to provide a Personal Access Token from GitLab.com. If you do not have one already with the required scopes, [follow these instructions](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) to create one. The required scopes for the token are `read_api`, `read_user`, and `read_repository`. Once you have your token, copy and paste it into the prompt and hit `Enter` to finish connecting. 

<img src="/wp-content/uploads/gl-provide-pat.png" class="img-bordered img-responsive center">

## GitHub Enterprise and GitLab Self-Managed Integration ✨

GitLens Pro offers a richer integration with GitHub Enterprise and GitLab Self-Managed.

Once authenticated, GitLens will enrich GitHub Enterprise or GitLab Self-Managed autolinks in the hovers. You’ll see your GitHub Enterprise or GitLab Self-Managed avatar, links to related pull requests, along with a footnote of the pull request or issue details. You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

<img src="/wp-content/uploads/gitlab-github-integration.png" class="img-bordered img-responsive center">

See the [remote provider integration settings](/gitlens/settings/#remote-provider-integration-settings) to configure these integrations.

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

***

##Menus & Toolbars

<img src="/wp-content/uploads/menus.png" class="img-bordered img-responsive center">

GitLens provides [customizable](/gitlens/gitlens-settings/#elementor-toc__heading-anchor-16) menu and toolbar contributions to put you in control over where GitLens' commands are shown. The easiest way to configure these settings is via the GitLens [interactive settings editor](/gitlens/gitlens-settings/).

For example, if you uncheck the _Add to the editor group toolbar_ you will see the following items removed from the toolbar:

<img src="/wp-content/uploads/menus-example.png" class="img-bordered img-responsive center">

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