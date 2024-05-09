---

title: Sidebar
description: GitLens sidebar views
taxonomy:
    category: gitlens

---

GitLens adds many side bar views to provide additional rich functionality. There are three side bars with GitLens views in them: GitLens Inspect, GitLens, and Source Control.

All views are free to use on all repos, **except** for views:  

- marked with a ✨ require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos
- marked with a ☁️ require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Free, Pro, etc

***

## Side Bars

### GitLens Inspect

GitLens Inspect side bar focuses on providing contextual information and insights to what you're actively working on. This side bar includes:

- Commit Details
- Line History
- File History
- Visual File History
- Search & Compare

<img src="/wp-content/uploads/gl-inspect-side-bar.png" class="img-responsive left"> 

### GitLens

The GitLens side bar is the home of GitKraken teams and collaboration services (e.g. GitKraken Workspaces) as well as discovery, help, and support. This side bar includes:

- Home view
- GitKraken Workspaces
- GitKraken Account

<img src="/wp-content/uploads/gl-side-bar-v14.png" class="img-responsive left"> 

### Source Control

Source Control contains side bar that are only focused on your repositories. This side bar includes:

- Commits
- Branches
- Remotes
- Stashes
- Tags
- Worktrees
- Contributors
- Repositories

<img src="/wp-content/uploads/gl-side-bar.png" class="img-responsive left">

### Moving Views

Any view can be moved between GitLens Inspect, GitLens, and the Source Control Sidebar. To move a view, simply drag and drop the view into the desired sidebar. 

<img src="/wp-content/uploads/move-view.gif" class="img-bordered img-responsive center">

To revert back to the default view locations, open the command palette (<kdb>command/ctrl + shift + P</kdb>) and use the command <kdb>View: Reset View Locations</kdb>

***
 
##Commits view

<img src="/wp-content/uploads/commits-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#commits-view-settings) view to visualize, explore, and manage Git commits

The _Commits_ view lists all of the commits on the current branch, and additionally provides:

- a toggle to switch between showing all commits or just your own commits
- a toggle to change the file layout: list, tree, auto
- a branch comparison tool **(Compare <current branch> with <branch, tag, or ref>)** — [optionally](/gitlens/gitlens-settings/#commits-view-settings) shows a comparison of the current branch (or working tree) to a user-selected reference
    -  **Behind** — lists the commits that are missing from the current branch (i.e. behind) but exist in the selected reference
        - **number of files changed** — lists all of the files changed in the behind commits
    - **Ahead** — lists the commits that the current branch has (i.e. ahead) but are missing in the selected reference
        - **number of files changed** — lists all of the files changed in the ahead commits
        - **number of files changed** — lists all of the files changed between the compared references
- the current branch status — shows the upstream status of the current branch
    - **Publish \<current branch\> to <remote>** — shown when the current branch has not been published to a remote
    - **Up to date with \<remote\>** — shown when the current branch is up to date with the upstream remote
    - **Changes to pull from \<remote\>** — lists all of the commits waiting to be pulled when the current branch has commits that are waiting to be pulled from the upstream remote
    - **Changes to push to <remote>** — lists of all the files changed in the unpublished commits when the current branch has (unpublished) commits that waiting to be pushed to the upstream remote
    - **Merging into \<branch\>** or **Resolve conflicts before merging into \<branch\>** — lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated Merging
<img src="/wp-content/uploads/commits-view-merge.png" class="img-bordered img-responsive center">

    - **Rebasing \<branch\>** or **Resolve conflicts to continue rebasing \<branch\>** — shows the number of rebase steps left, the commit the rebase is paused at, and lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated Rebasing
<img src="/wp-content/uploads/commits-view-rebase.png" class="img-bordered img-responsive center">

- any associated pull request — shows any opened or merged pull request associated with the current branch

***

##Commit Details View ✨

The Commit Details View gives you contextual change info about your code and working changes. It offers two tabs: Commit and Working Changes.  

To open the Commit Details View, open the command palette using `Cmd/ctrl + Shift + P` and type: “Show Commit Details View” or navigate to the Commit Details View in the sidebar.

<img src="/wp-content/uploads/show-commit-details-view.gif" class="img-bordered img-responsive center">

### Commits

The Commit tab updates as you move your cursor throughout the file with information about the commit that modified that line of code. Get quick information about the commit author, commit ID, links to Pull Requests, files modified in the commit, and more.

Click on a file to open the diff, and see what changed. You may also hover over the file name to access options like Open File, Open Changes with Working File, and Open Remote.

<img src="/wp-content/uploads/commit-details-view.png" class="img-bordered img-responsive center">

### Working Changes

The Working Changes tab allows you to view your work-in-progress changes any time without losing context on your current selected change. The tab includes the ability to stage and unstage changes, open files to view changes, and open the changes in the Commit Graph and SCM view.

<img src="/wp-content/uploads/gl-14-4-commit-details-wip.png" class="img-bordered img-responsive center">

***

##Repositories view

<img src="/wp-content/uploads/repositories-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#repositories-view-settings) view to visualize, explore, and manage Git repositories

The _Repositories_ view lists opened Git repositories, and additionally provides:

- a toggle to automatically refresh the repository on changes
- a toggle to change the file layout: list, tree, auto
-  an icon overlay indicator to show the current branch's upstream status (if available)
    - _No dot_ — no changes or the branch is unpushlished
    - _Green dot_ — has changes unpushed (ahead)
    - _Red dot_ — has changes unpulled (behind)
    - _Yellow dot_ — both unpushed and unpulled changes
- a branch comparison tool **(Compare <current branch> with <branch, tag, or ref>)** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows a comparison of the current branch (or working tree) to a user-selected reference
    - **Behind** — lists the commits that are missing from the current branch (i.e. behind) but exist in the selected reference
        - **Number of files changed** — lists all of the files changed between the compared references
    - **Ahead** — lists the commits that the current branch has (i.e. ahead) but are missing in the selected reference
        - **# files changed** — lists all of the files changed between the compared references
- **files changed** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) lists all of the files changed in the working tree
- the current branch status — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the upstream status of the current branch
    - **Publish \<current branch\>** to remote — shown when the current branch has not been published to a remote
    - **Up to date with \<remote\>** — shown when the current branch is up to date with the upstream remote
    - **Changes to pull from \<remote\>** — lists all of the unpulled commits and all of the files changed in them, when the current branch has commits that are waiting to be pulled from the upstream remote
    - **Changes to push to \<remote\>** — lists of all the unpublished commits and all of the files changed in them, when the current branch has commits that waiting to be pushed to the upstream remote
    - **Merging into \<branch\>** or **Resolve conflicts before merging into \<branch\>** — lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated
    - **Rebasing \<branch\>** or **Resolve conflicts to continue rebasing \<branch\>** — shows the number of rebase steps left, the commit the rebase is paused at, and lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated
- any associated pull request — optionally shows any opened or merged pull request associated with the current branch
- **Commits** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the current branch commits, similar to the Commits view
- **Branches** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the local branches, similar to the Branches view
- **Remotes** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the remotes and remote branches, similar to the Remotes view
- **Stashes** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the stashes, similar to the Stashes view
- **Tags** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the tags, similar to the Tags view
- **Contributors** — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows the contributors, similar to the Contributors view
- **Incoming Activity** (experimental) — [optionally](/gitlens/gitlens-settings/#repositories-view-settings) shows any incoming activity, which lists the command, branch (if available), and date of recent incoming activity (merges and pulls) to your local repository

***

##File History view

<img src="/wp-content/uploads/file-history-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#file-history-view-settings) view to visualize, navigate, and explore the revision history of the current file or just the selected lines of the current file

The file history view lists all of the commits that changed the current file on the current branch, and additionally provides:

- a toggle to pin (pause) the automatic tracking of the current editor
- a toggle to switch between file and line history, i.e. show all commits of the current file, or just the selected lines of the current file
- the ability to change the current base branch or reference when computing the file or line history
- (file history only) a toggle to follow renames across the current file
- (file history only) a toggle to show commits from all branches rather than just from the current base branch or reference
- merge conflict status when applicable
    - **Merge Changes** — show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated

<img src="/wp-content/uploads/file-history-view-merge-conflict.png" class="img-bordered img-responsive center">

***

##Line History view

<img src="/wp-content/uploads/line-history-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#line-history-view-settings) view to visualize, navigate, and explore the revision history of the selected lines of the current file

The line history view lists all of the commits that changed the selected lines of the current file on the current branch, and additionally provides:

- a toggle to pin (pause) the automatic tracking of the current editor
- the ability to change the current base branch or reference when computing the line history
- merge conflict status when applicable
    - **Merge Changes** — show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated


***

##Branches view

<img src="/wp-content/uploads/branches-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#branches-view-settings)  view to visualize, explore, and manage Git branches

The _Branches_ view lists all of the local branches, and additionally provides:

- a toggle to change the branch layout: list or tree
- a toggle to change the file layout: list, tree, auto
- an icon overlay indicator to show the branch's upstream status (if available)
    - _No dot_ — no changes or the branch is unpushlished
    - _Green dot_ — has changes unpushed (ahead)
    - _Red dot_ — has changes unpulled (behind)
    - _Yellow dot_ — both unpushed and unpulled changes
- status indicators (decorations), on the right, and themeable colorizations
    - `✓` — indicates that the branch is the current branch
    - `▲` + green colorization — indicates that the branch has unpushed changes (ahead)
    - `▼` + red colorization — indicates that the branch has unpulled changes (behind)
    - `▼▲` + yellow colorization — indicates that the branch has diverged from its upstream; meaning it has both unpulled and unpushed changes
    - `▲+` + green colorization — indicates that the branch hasn't yet been published to an upstream remote
    - `!` + dark red colorization — indicates that the branch has a missing upstream (e.g. the upstream branch was deleted)
- a branch comparison tool **(Compare <branch> with <branch, tag, or ref>)** — [optionally](/gitlens/settings/#branches-view-settings) shows a comparison of the branch to a user-selected reference
    - **Behind** — lists the commits that are missing from the branch (i.e. behind) but exist in the selected reference
        - **Number of files changed** — lists all of the files changed in the behind commits
    - **Ahead** — lists the commits that the branch has (i.e. ahead) but are missing in the selected reference
        - **number of files changed** — lists all of the files changed in the ahead commits
    - **Number of files changed** — lists all of the files changed between the compared references
- the branch status — shows the upstream status of the branch
    - **Publish \<branch\> to \<remote\>** — shown when the current branch has not been published to a remote
    - **Changes to push to \<remote\>** — lists of all the files changed in the unpublished commits when the branch has (unpublished) commits that waiting to be pushed to the upstream remote
    - **Changes to pull from \<remote\>** — lists all of the commits waiting to be pulled when the branch has commits that are waiting to be pulled from the upstream remote
- any associated pull request — shows any pull request associated with the branch

***

##Remotes view

<img src="/wp-content/uploads/remotes-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#remotes-view-settings) view to visualize, explore, and manage Git remotes and remote branches

The _Remotes_ view lists all of the remotes and their remote branches, and additionally provides:

- a toggle to change the branch layout: list or tree
- a toggle to change the file layout: list, tree, auto
- a toggle to connect to a supported remote providers to enable a rich integration with pull requests, issues, avatars, and more

***

##Stashes view

<img src="/wp-content/uploads/stashes-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#stashes-view-settings)  view to visualize, explore, and manage Git stashes

The _Stashes_ view lists all of the stashes, and additionally provides:

- a toggle to change the file layout: list, tree, auto

***

##Tags view

<img src="/wp-content/uploads/tags-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#tags-view-settings) view to visualize, explore, and manage Git tags

The _Tags_ view lists all of the tags, and additionally provides:

- a toggle to change the tag layout: list or tree
- a toggle to change the file layout: list, tree, auto

***

## Workspaces ☁️

Workspaces are a convenient way to group and manage multiple repositories, making them easily accessible from anywhere. Whether you're working individually or collaborating with a team, Workspaces provide a seamless way to manage your projects. A Workspace can be made up of local repositories, those you currently have open in your VS Code window, or GitKraken Workspaces, which are repositories stored on the cloud or on GitKraken services.

Whether you're working individually or collaborating with a team, these new features are designed to help you work more efficiently and effectively.

To access Workspaces, simply open the GitLens Home menu and you will find them in the panel located at the bottom left. Alternatively, you can access them by performing a search in the command palette.

Please note that while using cloud workspaces requires a free account, shared cloud workspaces require a trial or subscription.

<img src="/wp-content/uploads/gl-workspaces-sidebar.png" class="img-bordered img-responsive center">

### Creating a Workspace

To create a workspace, tap the '+' button next to GitKraken Workspaces, provide a name and a description, and connect a provider if you wish.

<img src="/wp-content/uploads/gl-create-workspace.png" class="img-bordered img-responsive center">

### Adding Repositories

You can add repositories to a workspace by tapping the '+' button under the Workspace tab. And if you want to keep your Workspaces and their repositories up-to-date, simply tap the Refresh icon.

<img src="/wp-content/uploads/gl-add-repo-to-workspace.png" class="img-bordered img-responsive center">

### Locating Repositories

To locate the disk location of the repositories within the Cloud Workspace, select the 'Locate Repositories' (pin icon) next to the repository name. If you have a folder set up for a Workspace with multiple repositories on your disk, you can select the option and choose the parent folder. GitLens will then find all the repositories within that parent folder.

<img src="/wp-content/uploads/gl-locate-repo-in-workspace.png" class="img-bordered img-responsive center">

### Opening Repositories

To open a repository from a Workspace tap the 'Open Repository in New Window' icon.

_Pro Tip: If you prefer to open the Workspace in your current window, hold down the ALT/OPTION key on a Mac and click 'Open Repo'._

<img src="/wp-content/uploads/gl-open-as-vscode-workspace.png" class="img-bordered img-responsive center">

### Removing Repositories

To remove a repository from a Workspace, you can do so by right-clicking to open the context menu on the repository you wish to remove and then selecting 'remove repository from Workspace'.

<img src="/wp-content/uploads/gl-remove-repo-from-wrokspace.png" class="img-bordered img-responsive center">

### Converting to Cloud Workspaces

To convert your local VSCode workspace into a GitKraken Workspace, press the 'Convert to Cloud Workspace' icon, provide a name and a description, and your workspace will be stored in the cloud for your GitKraken user account. This means that your Cloud Workspace will now appear in any of your GitKraken shared services, such as GitKraken Desktop, GitLens, and the GitKraken CLI.

<img src="/wp-content/uploads/gl-convert-workspace-to-cloud.png" class="img-bordered img-responsive center">

### Understanding Workspace indicators and colors

Workspaces also include visual indicators to help you understand their status. For example, a green Workspace with an 'O' symbol indicates that it is open in your current window.

<img src="/wp-content/uploads/gl-workspace-indicators.png" class="img-bordered img-responsive center">

### Workspace linking

A VS Code workspace can be created from a GitKraken Workspace to link them.

<img src="/wp-content/uploads/gl-create-vs-workspace-from-gl.png" class="img-bordered img-responsive center">

You can open a linked VS Code workspace from its cloud workspace using the new `Open VS Code Workspace in New Window` option (hold alt to open in the current window).

When repositories are added to a GitKraken Cloud workspace, you can automatically add those repositories to its linked VS Code workspace when that workspace is opened. You can choose to automatically add the repositories, be prompted to add them, or disable auto-adding repositories altogether for that workspace. This setting is chosen when creating the VS Code workspace, but can be changed at any time using the new `Change Linked Workspace Auto-Add Behavior` command on the `Current Window` item or its linked workspace in the _Workspaces_ view.

<img src="/wp-content/uploads/gl-link-repositories-in-workspaces.png" class="img-bordered img-responsive center">

You can also manually add repositories to the VS Code workspace at any time using the new `Add Repositories from Linked Workspace` command.

***

## Worktrees view✨

<img src="/wp-content/uploads/worktrees-view.png" class="img-bordered img-responsive center">

A [customizable](gitlens/gitlens-settings/#worktrees-view-settings) view to create, view, and work with <a href="https://www.gitkraken.com/learn/git/git-worktree" target="_blank">Worktrees</a>. Worktrees allow multiple branches to be checked-out at once on the same repository. This makes it easier to develop on, or test multiple branches, by minimizing the context switching between branches.

***

##Contributors view

<img src="/wp-content/uploads/contributors-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#contributors-view-settings) view to visualize, navigate, and explore contributors

The Contributors view lists all of the contributors, and additionally provides:

- a toggle to change the file layout: list, tree, auto

***

##Search & Compare view

<img src="/wp-content/uploads/search-and-compare-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#search-and-compare-view-settings) view to search and explore commit histories by message, author, files, id, etc, or visualize comparisons between branches, tags, commits, and more

The _Search & Compare_ view lists pinnable (saved) results for searching commit histories or for comparison operations, and additionally provides,

- a toggle to keep previous results when new results are added
- a toggle to change the file layout: list, tree, auto
- pinnable search — lists all of the commits that match the search query
    - Search results can be provided by the following commands
        - _Search Commits_ command (`gitlens.showCommitSearch`) can search
            - by message — use `<message>` to find commits with messages that match `<message>` — See Git docs
            - or, by author — use `@<pattern>` to find commits with authors that match `<pattern>` — See Git docs
            - or, by commit SHA — use `#<sha>` to find a commit with SHA of `<sha>` — See Git docs
            - or, by files — use `:<path/glob>` to find commits with file names that match `<path/glob>` — See Git docs
            - or, by changes — use `~<pattern>` to find commits with differences whose patch text contains added/removed lines that match `<pattern>` — See Git docs
        - _Show File History_ command (`gitlens.showQuickFileHistory`)
        - _Show Commit_ command (`gitlens.showQuickCommitDetails`)
- pinnable comparison — shows a comparison of the two user-selected references
    - **Behind** — lists the commits that are missing from the branch (i.e. behind) but exist in the selected reference
        - **Number of files changed** — lists all of the files changed in the behind commits
    - **Ahead** — lists the commits that the branch has (i.e. ahead) but are missing in the selected reference
        - **Number of files changed** — lists all of the files changed in the ahead commits
    - **Number of files changed** — lists all of the files changed between the compared references
    - Comparision results can be provided by the following commands
        - _Compare with Upstream_ command (`gitlens.views.compareWithUpstream`)
        - _Compare with Working Tree_ command (`gitlens.views.compareWithWorking`)
        - _Compare with HEAD_ command (`gitlens.views.compareWithHead`)
        - _Compare with Selected_ command (`gitlens.views.compareWithSelected`)
        - _Compare Ancestry with Working Tree_ command (`gitlens.views.compareAncestryWithWorking`)
- a checkbox next to files to allow tracking review progress
