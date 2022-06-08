---

title: GitLens Features
description: GitLens Features
taxonomy:
    category: gitlens

---

Core features availible to both free and paid GitLens users. 

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

Adds on-demand, [customizable](/gitlens/settings/#gutter-blame-settings), and [themable](/gitlens/settings/#themable-colors), gutter blame annotations to show the commit and author who last modified each line of a file

- Contains the commit message and date, by [default](/gitlens/settings/#gutter-blame-settings)
- Adds a heatmap (age) indicator on right edge (by [default](/gitlens/settings/#gutter-blame-settings),) of the gutter to provide an easy, at-a-glance way to tell how recently lines were changed (optional, on by default)
- See the gutter heatmap section below for more details
- Adds a Toggle File Blame Annotations command (`gitlens.toggleFileBlame`) with a shortcut of <kbd>alt+b</kbd> to toggle the blame annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##Gutter Changes

<img src="/wp-content/uploads/gutter-blame.png" class="img-bordered img-responsive center">

Adds an on-demand, [customizable](/gitlens/settings/#gutter-changes-settings), and [themable](/gitlens/settings/#themable-colors), gutter changes annotation to highlight any local (unpublished) changes or lines changed by the most recent commit.

- Adds Toggle File Changes command (`gitlens.toggleFileChanges`) to toggle the changes annotations on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##Gutter Heatmap

<img src="/wp-content/uploads/gutter-heatmap.png" class="img-bordered img-responsive center">

Adds an on-demand heatmap to the edge of the gutter to show how recently lines were changed

- The indicator's [customizable](/gitlens/settings/#gutter-heatmap-settings) color will either be hot or cold based on the age of the most recent change (cold after 90 days by [default](/gitlens/settings/#gutter-heatmap-settings))
- The indicator's brightness ranges from bright (newer) to dim (older) based on the relative age, which is calculated from the median age of all the changes in the file
- Adds Toggle File Heatmap Annotations command (`gitlens.toggleFileHeatmap`) to toggle the heatmap on and off
- Press <kbd>Escape</kbd> to turn off the annotations

***

##Side Bar Views

GitLens adds many [side bar views](/gitlens/side-bar) to provide additional rich functionality. The default layout (location) of these views can be quickly customized via the GitLens: Set Views Layout (`gitlens.setViewsLayout`) command from the <a href='https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette' target='_blank'>VS Code Command Palette</a>.

- Source Control Layout — shows all the views together on the Source Control side bar
- GitLens Layout — shows all the views together on the GitLens side bar

<img src="/wp-content/uploads/views-layout-scm-gitlens.png" class="img-responsive left"> 

Check out the [Side Bar documentation](/gitlens/side-bar/) for more information.

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
- Copy _Remote File Url From... command (`gitlens.copyRemoteFileUrlFrom`) — copies the url of a file or revision on a specific branch or tag the remote provider
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

***

##Powerful Commands

- Adds an _Add Co-authors_ command (`gitlens.addAuthors`) to add a co-author to the commit message input box

- Adds a _Copy SH_A command (`gitlens.copyShaToClipboard`) to copy the commit SHA of the current line to the clipboard or from the most recent commit to the current branch, if there is no current editor

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
