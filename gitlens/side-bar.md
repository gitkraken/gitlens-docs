---

title: GitLens Sidebar
description: GitLens sidebar views
taxonomy:
    category: gitlens

---


#GitLens Sidebar Views

GitLens adds many [side bar views](/gitlens/side-bar) to provide additional rich functionality. The default layout (location) of these views can be quickly customized via the GitLens: Set Views Layout (`gitlens.setViewsLayout`) command from the <a href='https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette' target='_blank'>VS Code Command Palette</a>.

- Source Control Layout — shows all the views together on the Source Control side bar
- GitLens Layout — shows all the views together on the GitLens side bar

<img src="/img/documentation/gitlens/views-layout-scm-gitlens.png" class="img-responsive left"> 

***
 
##Commits view


<img src="/img/documentation/gitlens/commits-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#commits-view-settings) view to visualize, explore, and manage Git commits

The Commits view lists all of the commits on the current branch, and additionally provides:

- a toggle to switch between showing all commits or just your own commits
- a toggle to change the file layout: list, tree, auto
- a branch comparison tool (Compare <current branch> with <branch, tag, or ref>) — optionally shows a comparison of the current branch (or working tree) to a user-selected reference
    -  Behind — lists the commits that are missing from the current branch (i.e. behind) but exist in the selected reference
        - number of files changed — lists all of the files changed in the behind commits
    - Ahead — lists the commits that the current branch has (i.e. ahead) but are missing in the selected reference
        - number of files changed — lists all of the files changed in the ahead commits
        - number of files changed — lists all of the files changed between the compared references
- the current branch status — shows the upstream status of the current branch
    - Publish <current branch> to <remote> — shown when the current branch has not been published to a remote
    - Up to date with <remote> — shown when the current branch is up to date with the upstream remote
    - Changes to pull from <remote> — lists all of the commits waiting to be pulled when the current branch has commits that are waiting to be pulled from the upstream remote
    - Changes to push to <remote> — lists of all the files changed in the unpublished commits when the current branch has (unpublished) commits that waiting to be pushed to the upstream remote
    - Merging into <branch> or Resolve conflicts before merging into <branch> — lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated Merging
<img src="/img/documentation/gitlens/commits-view-merge.png" class="img-bordered img-responsive center">

    - Rebasing <branch> or Resolve conflicts to continue rebasing <branch> — shows the number of rebase steps left, the commit the rebase is paused at, and lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated Rebasing
<img src="/img/documentation/gitlens/commits-view-rebase.png" class="img-bordered img-responsive center">

- any associated pull request — shows any opened or merged pull request associated with the current branch

***
##Repositories view

<img src="/img/documentation/gitlens/repositories-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#repositories-view-settings) view to visualize, explore, and manage Git repositories

The **Repositories view** lists opened Git repositories, and additionally provides:

- a toggle to automatically refresh the repository on changes
- a toggle to change the file layout: list, tree, auto
-  an icon overlay indicator to show the current branch's upstream status (if available)
    - No dot — no changes or the branch is unpushlished
    - Green dot — has changes unpushed (ahead)
    - Red dot — has changes unpulled (behind)
    - Yellow dot — both unpushed and unpulled changes
- a branch comparison tool (Compare <current branch> with <branch, tag, or ref>) — optionally shows a comparison of the current branch (or working tree) to a user-selected reference
    - Behind — lists the commits that are missing from the current branch (i.e. behind) but exist in the selected reference
        - Number of files changed — lists all of the files changed between the compared references
    - Ahead — lists the commits that the current branch has (i.e. ahead) but are missing in the selected reference
        - files changed — lists all of the files changed between the compared references
- files changed — optionally lists all of the files changed in the working tree
- the current branch status — optionally shows the upstream status of the current branch
    - Publish <current branch> to remote — shown when the current branch has not been published to a remote
    - Up to date with <remote> — shown when the current branch is up to date with the upstream remote
    - Changes to pull from <remote> — lists all of the unpulled commits and all of the files changed in them, when the current branch has commits that are waiting to be pulled from the upstream remote
    - Changes to push to <remote> — lists of all the unpublished commits and all of the files changed in them, when the current branch has commits that waiting to be pushed to the upstream remote
    - Merging into <branch> or Resolve conflicts before merging into <branch> — lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated
    - Rebasing <branch> or Resolve conflicts to continue rebasing <branch> — shows the number of rebase steps left, the commit the rebase is paused at, and lists any conflicted files. Conflicted files show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated
- any associated pull request — optionally shows any opened or merged pull request associated with the current branch
- Commits — optionally shows the current branch commits, similar to the Commits view
- Branches — optionally shows the local branches, similar to the Branches view
- Remotes — optionally shows the remotes and remote branches, similar to the Remotes view
- Stashes — optionally shows the stashes, similar to the Stashes view
- Tags — optionally shows the tags, similar to the Tags view
- Contributors — optionally shows the contributors, similar to the Contributors view
- Incoming Activity (experimental) — optionally shows any incoming activity, which lists the command, branch (if available), and date of recent incoming activity (merges and pulls) to your local repository

***

##File History view

<img src="/img/documentation/gitlens/file-history-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#file-history-view-settings) view to visualize, navigate, and explore the revision history of the current file or just the selected lines of the current file

The file history view lists all of the commits that changed the current file on the current branch, and additionally provides:

- a toggle to pin (pause) the automatic tracking of the current editor
- a toggle to switch between file and line history, i.e. show all commits of the current file, or just the selected lines of the current file
- the ability to change the current base branch or reference when computing the file or line history
- (file history only) a toggle to follow renames across the current file
- (file history only) a toggle to show commits from all branches rather than just from the current base branch or reference
- merge conflict status when applicable
    - Merge Changes — show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated

<img src="/img/documentation/gitlens/file-history-view-merge-conflict.png" class="img-bordered img-responsive center">

***

##Line History view

<img src="/img/documentation/gitlens/line-history-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#line-history-view-settings) view to visualize, navigate, and explore the revision history of the selected lines of the current file

The line history view lists all of the commits that changed the selected lines of the current file on the current branch, and additionally provides:

- a toggle to pin (pause) the automatic tracking of the current editor
- the ability to change the current base branch or reference when computing the line history
- merge conflict status when applicable
    - Merge Changes — show comparisons with the common base of the current and incoming changes to aid in resolving the conflict by making it easier to see where changes originated


***

##Branches view

<img src="/img/documentation/gitlens/branches-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#branches-view-settings)  view to visualize, explore, and manage Git branches

The Branches view lists all of the local branches, and additionally provides:

- a toggle to change the branch layout: list or tree
- a toggle to change the file layout: list, tree, auto
- an icon overlay indicator to show the branch's upstream status (if available)
    - No dot — no changes or the branch is unpushlished
    - Green dot — has changes unpushed (ahead)
    - Red dot — has changes unpulled (behind)
    - Yellow dot — both unpushed and unpulled changes
- status indicators (decorations), on the right, and themeable colorizations
    - ✓ — indicates that the branch is the current branch
    - ▲ + green colorization — indicates that the branch has unpushed changes (ahead)
    - ▼ + red colorization — indicates that the branch has unpulled changes (behind)
    - ▼▲ + yellow colorization — indicates that the branch has diverged from its upstream; meaning it has both unpulled and unpushed changes
    - ▲+ + green colorization — indicates that the branch hasn't yet been published to an upstream remote
    - ! + dark red colorization — indicates that the branch has a missing upstream (e.g. the upstream branch was deleted)
- a branch comparison tool (Compare <branch> with <branch, tag, or ref>) — [optionally](/gitlens/settings/#branches-view-settings) shows a comparison of the branch to a user-selected reference
    - Behind — lists the commits that are missing from the branch (i.e. behind) but exist in the selected reference
        - Number of files changed — lists all of the files changed in the behind commits
    - Ahead — lists the commits that the branch has (i.e. ahead) but are missing in the selected reference
        - number of files changed — lists all of the files changed in the ahead commits
    - Number of files changed — lists all of the files changed between the compared references
- the branch status — shows the upstream status of the branch
    - Publish <branch> to <remote> — shown when the current branch has not been published to a remote
    - Changes to push to <remote> — lists of all the files changed in the unpublished commits when the branch has (unpublished) commits that waiting to be pushed to the upstream remote
    - Changes to pull from <remote> — lists all of the commits waiting to be pulled when the branch has commits that are waiting to be pulled from the upstream remote
- any associated pull request — shows any pull request associated with the branch

***

##Remotes view

<img src="/img/documentation/gitlens/remotes-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#remotes-view-settings) view to visualize, explore, and manage Git remotes and remote branches

The Remotes view lists all of the remotes and their remote branches, and additionally provides:

- a toggle to change the branch layout: list or tree
- a toggle to change the file layout: list, tree, auto
- a toggle to connect to a supported remote providers to enable a rich integration with pull requests, issues, avatars, and more

***

##Stashes view

<img src="/img/documentation/gitlens/stashes-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#stashes-view-settings)  view to visualize, explore, and manage Git stashes

The Stashes view lists all of the stashes, and additionally provides:

- a toggle to change the file layout: list, tree, auto

***

##Tags view

<img src="/img/documentation/gitlens/tags-view.png" class="img-bordered img-responsive center">

A [customizable](/gitlens/settings/#tags-view-settings) view to visualize, explore, and manage Git tags

The Tags view lists all of the tags, and additionally provides:

- a toggle to change the tag layout: list or tree
- a toggle to change the file layout: list, tree, auto


***

##Contributors view

<img src="/img/documentation/gitlens/contributors-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#contributors-view-settings) view to visualize, navigate, and explore contributors

The Contributors view lists all of the contributors, and additionally provides:

- a toggle to change the file layout: list, tree, auto

***

##Search & Compare view

<img src="/img/documentation/gitlens/search-and-compare-view.png" class="img-bordered img-responsive center">

A hidden by default, [customizable](/gitlens/settings/#search-and-compare-view-settings) view to search and explore commit histories by message, author, files, id, etc, or visualize comparisons between branches, tags, commits, and more

The Search & Compare view lists pinnable (saved) results for searching commit histories or for comparison operations, and additionally provides,

- a toggle to keep previous results when new results are added
- a toggle to change the file layout: list, tree, auto
- pinnable search — lists all of the commits that match the search query
    - Search results can be provided by the following commands
        - Search Commits command (gitlens.showCommitSearch) can search
            - by message — use <message> to find commits with messages that match <message> — See Git docs
            - or, by author — use @<pattern> to find commits with authors that match <pattern> — See Git docs
            - or, by commit SHA — use #<sha> to find a commit with SHA of <sha> — See Git docs
            - or, by files — use :<path/glob> to find commits with file names that match <path/glob> — See Git docs
            - or, by changes — use ~<pattern> to find commits with differences whose patch text contains added/removed lines that match <pattern> — See Git docs
        - Show File History command (gitlens.showQuickFileHistory)
        - Show Commit command (gitlens.showQuickCommitDetails)
- pinnable comparison — shows a comparison of the two user-selected references
    - Behind — lists the commits that are missing from the branch (i.e. behind) but exist in the selected reference
        - Number of files changed — lists all of the files changed in the behind commits
    - Ahead — lists the commits that the branch has (i.e. ahead) but are missing in the selected reference
        - Number of files changed — lists all of the files changed in the ahead commits
    - Number of files changed — lists all of the files changed between the compared references
    - Comparision results can be provided by the following commands
        - Compare with Upstream command (gitlens.views.compareWithUpstream)
        - Compare with Working Tree command (gitlens.views.compareWithWorking)
        - Compare with HEAD command (gitlens.views.compareWithHead)
        - Compare with Selected command (gitlens.views.compareWithSelected)
        - Compare Ancestry with Working Tree command (gitlens.views.compareAncestryWithWorking)


