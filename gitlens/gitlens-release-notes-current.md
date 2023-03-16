---

title: GitLens Release Notes
description: GitLens Release Notes
taxonomy:
    category: gitlens

---

Find out what’s new, what’s fixed, or just take a trip down memory lane remembering those bugs of yesterday.


Check out our [Changelog](https://github.com/gitkraken/vscode-gitlens/blob/main/CHANGELOG.md) to see linked issues and past changes.


<a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank" class="button button--basic ">Install Current Version Now</a>

✨ indicates [GitLens+ features](/gitlens/gitlens-plus/)

***

<a id="v13-4"></a>
## Version 13.4

### Thursday, Mar 16, 2023

With 13.4, we've introduced an experimental new AI feature to assist with writing commit messages, improved GitLens performance by reducing its size, made improvements to the ✨Commit Graph, and accepted community contributions as well as many bug fixes from community feedback.

<img src="/wp-content/uploads/TODO.png" class="img-responsive center img-bordered">

### AI-Generated Commit Messages (Experimental)

<img src="/wp-content/uploads/TODO.gif" class="img-responsive center img-bordered">

We’ve introduced a new experimental feature to assist with writing commit messages by leveraging OpenAI. To start, stage some changes you want to commit and generate a commit message for and then run the “Generate Commit Message (Experimental)” command from the Command Palette. From there you will be guided through the process of accepting to send the diff of your staged changes to OpenAI and the entry of your OpenAI key. Once completed, the generated commit message will be entered into the commit input box on the Source Control sidebar. You can also enter additional context about your changes in the commit box and those will also be sent to help generate a better message.

Additionally, you can customize the `gitlens.experimental.generateCommitMessagePrompt` setting to control the prompt used to structure and format the generated commit message. You could have it structure commit messages in the conventional commit style, or you can have fun with it and make your commit messages in the style of a pirate, Shakespeare, etc.

This is a very early peek into features and ideas that can leverage AI – look forward to much more in the near future!

### GitLens Size Reduction

Over the last couple releases we’ve made significant progress on optimizing the footprint of GitLens. We’ve focused a lot on the bundle sizes to allow for faster start-up times of both the extension itself and all of our webviews. These optimizations also help reduce our memory usage. We are continually looking for opportunities to optimize and reduce our footprint so look for more progress in the future!

Here are some numbers:
  - GitLens desktop bundle has been reduced by ~37% from 1.91MB to 1.21MB
  - GitLens web bundle (for vscode.dev / github.dev) has been reduced by ~39% from 2.05MB to 1.24MB
  - GitLens Commit Graph webview has been reduced by ~27% from 1.03MB to 758KB and that is including the new minimap and rich scroll markers
  - GitLens Home view has been reduced by ~41% from 267KB to 160KB
  - GitLens Visual File History view has been reduced by ~9% from 508KB to 461KB

### ✨ Commit Graph Enhancements

##### Upstream Tracking

<img src="/wp-content/uploads/TODO.png" class="img-responsive center img-bordered">

It's now possible to effortlessly keep track of upstreams of your local branches in the commit graph. The upstreams of visible local branches, along with their corresponding commit history, will be displayed in the graph even if other remote branches are filtered out from your settings.

We've also revised the wording of the remote filter setting to "Hide Remote-only Branches.

#### Graph Alignment

<img src="/wp-content/uploads/TODO.png" class="img-responsive center img-bordered">

The graph column is now more left-aligned, making it easier to read and follow the history of a branch at a glance.

#### Branches and Tags on Remote Repositories

<img src="/wp-content/uploads/TODO.png" class="img-responsive center img-bordered">

You can now see the tips of your branches and tags in the Commit Graph on remote repositories! Previously, opening a remote repository in the graph would show only the current branch. Currently, we are still limited to only showing commits for the current branch, so the included branches and tags are ones pointing to commits in the current branch’s commit history.

### Sunsetting GitLens Insiders (Replaced with Pre-release)

<img src="/wp-content/uploads/TODO.gif" class="img-responsive center img-bordered">

We’ve deprecated the GitLens Insiders edition in favor of a Pre-release version which is directly supported inside VS Code and is much easier to opt-in to and out of. Existing users of GitLens Insiders should have been automatically migrated to the Pre-release version. The Pre-release version of GitLens is a nightly build of GitLens, just as the GitLens Insiders edition was.

To opt-in to the Pre-release edition, select GitLens from the extensions sidebar and press “Switch to Pre-Release Version”.

### Thank you to our contributors

Shout-out to all of our awesome contributors for this release!
  - Nafiur Rahman Khadem ([@ShafinKhadem](https://github.com/ShafinKhadem))
  - Skyler Dawson ([@foxwoods369](https://github.com/foxwoods369))
  - haha ([@hahaaha](https://github.com/hahaaha))

### Added

- Adds an experimental _Generate Commit Message (Experimental)_ command to use OpenAI to generate a commit message for staged changes
  - Adds a `gitlens.experimental.generateCommitMessagePrompt` setting to specify the prompt to use to tell OpenAI how to structure or format the generated commit message &mdash; can have fun with it and make your commit messages in the style of a pirate, etc
- Adds auto-detection for `.git-blame-ignore-revs` files and excludes the commits listed within from the blame annotations
- Adds a _Open Git Worktree..._ command to jump directly to opening a worktree in the _Git Command Palette_
- Adds a _Copy Relative Path_ context menu action for active editors and file nodes in sidebar views
- Adds the ability to see branches and tags on remote repositories (e.g. GitHub) on the _Commit Graph_
  - Currently limited to only showing them for commits on the current branch, as we aren't yet able to show all commits on all branches

### Changed

- Improves the display of items in the _Commit Graph_
  - When showing local branches, we now always display the upstream branches in the minimap, scrollbar markers, and graph rows
  - When laying out lanes in the Graph column, we now bias to be left aligned when possible for an easier to read and compact graph visualization
- Improves _Open Worktree for Pull Request via GitLens..._ command to use the qualified remote branch name, e.g. `owner/branch`, when creating the worktree
- Removes Insiders edition in favor of the pre-release edition
- Reduces the size of the GitLens bundle which improves startup time
  - GitLens' extension bundle for desktop (node) is now ~24% smaller (1.58MB -> 1.21MB)
  - GitLens' extension bundle for web (vscode.dev/github.dev) is now ~6% smaller (1.32MB -> 1.24MB)

### Fixed

- Fixes [#2550](https://github.com/gitkraken/vscode-gitlens/issues/2550) - Related pull request disappears after refresh
- Fixes [#2549](https://github.com/gitkraken/vscode-gitlens/issues/2549) - toggle code lens does not work with gitlens.codeLens.enabled == false
- Fixes [#2553](https://github.com/gitkraken/vscode-gitlens/issues/2553) - Can't add remote url with git@ format
- Fixes [#2083](https://github.com/gitkraken/vscode-gitlens/issues/2083), [#2539](https://github.com/gitkraken/vscode-gitlens/issues/2539) - Fix stashing staged changes &mdash; thanks to [PR #2540](https://github.com/gitkraken/vscode-gitlens/pull/2540) by Nafiur Rahman Khadem ([@ShafinKhadem](https://github.com/ShafinKhadem))
- Fixes [#1968](https://github.com/gitkraken/vscode-gitlens/issues/1968) & [#1027](https://github.com/gitkraken/vscode-gitlens/issues/1027) - Fetch-> fatal: could not read Username &mdash; thanks to [PR #2481](https://github.com/gitkraken/vscode-gitlens/pull/2481) by Skyler Dawson ([@foxwoods369](https://github.com/foxwoods369))
- Fixes [#2495](https://github.com/gitkraken/vscode-gitlens/issues/2495) - Cannot use gitlens+ feature on public repo in some folders
- Fixes [#2530](https://github.com/gitkraken/vscode-gitlens/issues/2530) - Error when creating worktrees in certain conditions
- Fixed [#2566](https://github.com/gitkraken/vscode-gitlens/issues/2566) - hide context menu in output panel &mdash; thanks to [PR #2568](https://github.com/gitkraken/vscode-gitlens/pull/2568) by hahaaha ([@hahaaha](https://github.com/hahaaha))
- Fixes [#2533](https://github.com/gitkraken/vscode-gitlens/issues/2533) - Current Branch Only graph filter sometimes fails
- Fixes [#2504](https://github.com/gitkraken/vscode-gitlens/issues/2504) - Graph header theme colors were referencing the titlebar color properties
- Fixes [#2527](https://github.com/gitkraken/vscode-gitlens/issues/2527) - shows added files for Open All Changes
- Fixes an issue where trial status can be shown rather than a purchased license
- Fixes graph issue where scroll markers do not update until mouseover when changing the `gitlens.graph.scrollMarkers.additionalTypes` setting.

***

<a id="v13-3"></a>
## Version 13.3

### Thursday, Feb 23, 2023

Supercharge your Git game with GitLens 13.3: the latest update to help you master Git like a pro. With 13.3 we’re introducing Workspace Focus View, Deep Linking Support, and Commit Graph Improvements featuring the new (experimental) minimap and changes column.

<img src="/wp-content/uploads/glrn-13.3.png" class="img-responsive center img-bordered">

GitLens also just got a whole lot faster with the release of version 13.3! Thanks to some serious bundle slimming, the startup times have significantly improved.

- GitLens' extension bundle for desktop (node) is now ~18% smaller
- GitLens' extension bundle for web (vscode.dev/github.dev) is now ~37% smaller
- GitLens' Commit Graph webview bundle is now ~31% smaller


### ✨Focus View (Preview)

<img src="/wp-content/uploads/glrn-focus-view.png" class="img-responsive center img-bordered">

With the preview of GitLens Focus View, you can streamline your workflow and prioritize your tasks with ease. The Focus View feature gives you a comprehensive list of all your most important work across all your GitHub repos. No more jumping back and forth between multiple pages or repos - GitLens Focus View makes it simple and efficient to keep track of and manage your work progress.

The new Focus View will provide you with a summary of Pull Requests and Issues relevant to you for the repositories grouped in your Workspace.

- My Pull Requests: shows all GitHub PRs opened by you, assigned to you, or awaiting your review
- My Issues: shows all issues created by you, assigned to you, or that mention you.

Instead of hunting for these pieces of information separately, you can get a holistic view of what you’re working on.

*_Note Focus View is currently in a Preview Only state, it is subject to change in the future._

### ✨ Commit Graph improvements

#### Minimap (Experimental)

<img src="/wp-content/uploads/glrn-minimap.png" class="img-responsive center img-bordered">

Click the Toggle Minimap icon in the right corner of the Commit Graph top bar to toggle the Minimap on and off. As this is an experimental feature, it is off by default – and we would love to hear your feedback and suggestions.

The idea behind the Minimap is to provide a whole new dimension to the Commit Graph. You can quickly see the activity of the repo, see HEAD/upstream, branches (local and remote), and easily jump to them.

The <span style="color:green">green line</span> showcases HEAD while search results are depicted by <span style="color:yellow">yellow lines</span>. The highlighted region shows the Commit Graph area that is in view. Markers are arranged in two rows of stacked blocks:

- In the upper row, the <span style="color:green">blue blocks</span> signify remote branches, while the <span style="color:brown">brown blocks</span> refer to tags.
- Within the lower row, the <span style="color:pink">pink blocks</span> denote stashes, and the <span style="color:blue">blue blocks</span> represent local branches.

We really want to hear your feedback - this is still a very early feature and we're currently still playing with colors, and additional features. To leave us feedback such as what do you think, is this useful, what does it have that you like, what is it missing, etc. reach out to us on the GitLens, [GitHub Discussion board](https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133).

#### Changes column (lines added/deleted)

<img src="/wp-content/uploads/glrn-changes-column.png" class="img-responsive center img-bordered">

Reduce time and effort required to navigate through code changes, with the changes column in GitLens. The changes column provides a visual representation of changes made to files in each commit, with green bars indicating added lines and red bars indicating deleted lines.

This visual display allows you to quickly identify the extent of changes made to files across multiple commits, making it easier to pinpoint specific areas of code that have been modified.

You can toggle the Change Column by right clicking the graph header and clicking "Show Changes".

#### Scroll Markers (Rich scrollbar)

<img src="/wp-content/uploads/glrn-rich-scrollbar.png" class="img-responsive center img-bordered">

Scroll Markers adds a rich layer of information to the Commit Graph scrollbar. Now you can quickly find and jump to checked-out branches, selected rows, search results, as well as important points such as HEAD and refs. Similar to Overview Ruler in VS Code, Scroll Markers provide a visual indicator on the scrollbar.

Our intention with Scroll Markers is to save you time and effort by allowing you to quickly identify and jump to the relevant sections of your Git history. It's a powerful new addition to the Commit Graph to help streamline workflow.

#### Branch upstream status

<img src="/wp-content/uploads/glrn-branch-upstream.png" class="img-responsive center img-bordered">

The Commit Graph now shows the upstream status of local branches with an upstream. You'll be able to quickly identify when your local branch is out of sync with its upstream branch with the new indicator, which shows how many commits are ahead or behind your upstream branch.

You can also double-click on the upstream indicator, to pull or push the pending commits to bring your local branch back in sync with its upstream. This makes it easy to keep track of upstream changes to your local branches and keep them up to date.

#### Work In Progress Row improvements

<img src="/wp-content/uploads/glrn-wip.png" class="img-responsive center img-bordered">

With the latest Work In Progress Row improvements, with a single right click, you can access the WIP contextual menu. Giving you access to a range of useful options, including Stash All Changes, Open Details, and Open Source Control. These features allow you to more effectively manage your WIP.

### Deep linking support

Deep linking provides you with the ability to easily share specific remote repositories, commits, branches, and tags by copying the link to your clipboard and pasting it into a Jira issue or a Slack conversation for example.

The link will then open in the Commit Graph and can be used to quickly access and review relevant artifacts. With deep linking support, you can improve collaboration and communication by seamless sharing of important information related to your Git repos.

### Added

- Adds new _Commit Graph_ features and improvements
  - Adds a new experimental minimap of commit activity to the _Commit Graph_
  - Adds a new experimental _Changes_ column visualizing commit changes
  - Adds markers to the _Commit Graph_ scroll area indicating the location of the selected row, search results, current branch, upstream, and more
  - Adds the ability to show upstream (ahead/behind) status on local branches with an upstream
    - Adds a double-click action on the status to pull (when behind) or push (when ahead) pending changes
    - Adds context menu actions to _Push_, _Pull_, and _Fetch_ the local branch
    - Adds a `gitlens.graph.showUpstreamStatus` setting to toggle upstream (ahead/behind) indicators on branches
  - Adds the ability to show any associated pull requests with branches
    - Adds a double-click action on the PR icon to open the PR in the browser
    - Adds context menu actions to _Open Pull Request on Remote_ and _Copy_ the PR URL
    - Adds a `gitlens.graph.pullRequests.enabled` setting to toggle PR icons &mdash; closes [#2450](https://github.com/gitkraken/vscode-gitlens/issues/2450)
  - Adds a context menu to the WIP row &mdash; closes [#2458](https://github.com/gitkraken/vscode-gitlens/issues/2458)
  - Adds a double-click action on commit rows to open the _Commit Details_ view
  - Improves Author and Avatar tooltips to now also show the contributor's email address, if available
  - Improves Date tooltips to now always show both the absolute and relative date
- Adds the ability to copy and share links directly to repositories, branches, commits, and tags in the _Commit Graph_
  - Adds context menu actions to copy direct links in the _Share_ submenu
- Improves the Worktree creation experience
  - Adds a prompt after the worktree is created to choose how to open the worktree
    - Adds a `worktrees.openAfterCreate` setting to specify how and when to open a worktree after it is created
  - Ensures new worktrees are created from the "main" repo, if already in a worktree
- Adds a new _remote_ command to the _Git Command Palette_ to add, prune, and remove remotes
- Adds a _Open Worktree for Pull Request via GitLens..._ context menu command on pull requests in the _GitHub Pull Requests and Issues_ extension's views
  - Opens an associated worktree, if one exists, otherwise it creates a new worktree for the pull request
- Adds settings to control the format of commits in the GitLens views

### Changed

- Greatly reduces the size of many of GitLens' bundles which improves startup time
  - GitLens' extension bundle for desktop (node) is now ~18% smaller
  - GitLens' extension bundle for web (vscode.dev/github.dev) is now ~37% smaller
  - GitLens' Commit Graph webview bundle is now ~31% smaller
- Changes the _Contributors_ view to be shown by default on the _GitLens_ sidebar

### Removed

- Removes the use of an external color library for the _File Heatmap_ annotations and webview themes &mdash; reduces the bundled extension size

### Fixed

- Fixes [#2355](https://github.com/gitkraken/vscode-gitlens/issues/2355) - Search by changes stops working in version 13.x.x
- Fixes [#2473](https://github.com/gitkraken/vscode-gitlens/issues/2473) - Commit graph status bar show wrong last fetched date
- Fixes [#2409](https://github.com/gitkraken/vscode-gitlens/issues/2409) - Commit Graph Show Current Branch Only shows unrelated commits from other branches
- Fixes an issue where pinning not being respected in Commit Details view
- Fixes graph issue where search results that are merge commits are not highlighted when the `gitlens.graph.dimMergeCommits` setting is enabled
- Fixes graph issue where rows with tags belonging to a hovered branch are not highlighted when the `gitlens.graph.highlightRowsOnRefHover` setting is enabled

***

<a id="v13-2"></a>
## Version 13.2

### Tuesday, Dec 20th, 2022

Since the release of [GitLens 13](https://www.gitkraken.com/blog/gitlens-13), we know how the power of GitLens+ features like the Commit Graph, have been helping supercharge your dev workflow. That’s why we’re excited to present GitLens 13.2, with all new (and highly requested) Graph improvements like filtering, to quickly focus on what is most important to you. We've also streamlined the Commit Graph interface with a new header bar, providing context and quick access to switch between repositories or branches, and even fetch to keep up to date. Get ready to level up your Git game with GitLens 13.2!

<img src="/wp-content/uploads/gitlens-13.2-hero.png" class="img-responsive center img-bordered">

### Filtering

GitLens 13.2 introduces filtering , which allows you to display a subset of your graph’s information and helps you hone in on specific details of your graph that matter the most.

<img src="/wp-content/uploads/gitlens-filter-options.gif" class="img-responsive center img-bordered">

#### Filtering Capabilities

Use graph filtering in GitLens to get laser focused on the branch you're working on and its remote:

- Only Show the Current Branch
  - Display only the branch that you’re currently working on and it’s remote. In order to focus your attention on the things landing in this branch, and then quickly unfilter to "zoom" back out and see everything in flight.

- Hide Remote Branches
  - Hides commits from the graph view that are only on remote branches.

- Hide Tags
  - Hides all tags that point to commit rows.

- Hide Stashes
  - Hides all stash rows.

- Dim Merge Commit Rows
  - Deemphasizes merge commit rows.

### Graph UX Improvements

We've updated the user interface, so you can get to all your favorite features even faster. Now, you can access change repo, account status, and filtering from the top of the Commit Graph page.

<img src="/wp-content/uploads/graph-ux-improvements.png" class="img-responsive center img-bordered">

### Header Updates

By merging the contextual information from the footer into the header, including the new Branch Picker and Fetch Action we’ve made it easier for you to manage your branches and work more effectively.

<img src="/wp-content/uploads/drop-down.png" class="img-responsive center img-bordered">

- Branch Picker
  - Save time, by easily selecting the branch you want from the drop down branch picker.

- Fetch Action
  - Easily keep your local repo up-to-date and in sync with the fetch action.

### Shortcut Keys

Using the new keyboard shortcuts, `SHIFT+UP` and `SHIFT+DOWN` on the Commit Graph helps you locate what you need more efficiently and effectively by staying within the branch and moving between graph rows. This can be particularly useful if you are working on a complex project with many branches.

<img src="/wp-content/uploads/shift-up-down.gif" class="img-responsive center img-bordered">

### Added
- Adds many all-new _Commit Graph_ features and improvements
  - Adds the ability to filter commits, branches, stashes, and tags
    - Adds a new _Filter Graph_ dropdown button at the start of the search bar
    - Adds ability to quickly switch between _Show All Local Branches_ and _Show Current Branch Only branch_ filtering options
      - _Show All Local Branches_ — displays all local branches (default)
      - _Show Current Branch Only_ — displays only the current branch and it's upstream remote (if exists and _Hide Remote Branches_ isn't enabled)
    - Adds ability to hide all remote branches, stashes, and tags
    - Adds the ability to dim (deemphasize) merge commits
  - Adds a new header bar to provide quick access to common actions
    - Shows the currently selected repository with the ability to switch repositories when clicked (if multiple repositories are open)
    - Shows the current branch with the ability to switch branches when clicked
    - Provides a fetch action which also shows the last fetched time
    - Also moves GitLens+ feature status and feedback links to the top right
  - Adds new ability to reorder columns by dragging and dropping column headers (not all columns are reorderable)
  - Adds new keyboard shortcuts
      - Use `shift+down arrow`  and `shift+up arrow` to move to the parent/child of the selected commit row
      - Holding the `ctrl` key with a commit row selected will highlight rows for that commit's branch
  - Adds new settings
    - Adds a `gitlens.graph.dimMergeCommits` setting to specify whether to dim (deemphasize) merge commit rows
    - Adds a `gitlens.graph.scrollRowPadding` setting to specify the number of rows from the edge at which the graph will scroll when using keyboard or search to change the selected row

### Changed
- In the _Commit Graph_, increases the time to highlight associated rows when hovering over a branch to 1s
- Removes the status bar from the _Commit Graph_ as it was replaced by the new header bar

### Fixed
- Fixes [#2394](https://github.com/gitkraken/vscode-gitlens/issues/2394) - Work in progress file diff compares working tree with working tree, instead of working tree with head
- Fixes [#2207](https://github.com/gitkraken/vscode-gitlens/issues/2207) - Error when trying to push individual commit
- Fixes [#2301](https://github.com/gitkraken/vscode-gitlens/issues/2301) - Create Worktree button doesn't work in certain cases
- Fixes [#2382](https://github.com/gitkraken/vscode-gitlens/issues/2382) - commits disappearing from commit details view when they shouldn't
- Fixes [#2318](https://github.com/gitkraken/vscode-gitlens/issues/2318) - GitLens need to login again after VS Code insiders upgrade every day
- Fixes [#2377](https://github.com/gitkraken/vscode-gitlens/issues/2377) - Missing Azure Devops Icon
- Fixes [#2380](https://github.com/gitkraken/vscode-gitlens/issues/2380) - Autolink fails with curly braces
- Fixes [#2362](https://github.com/gitkraken/vscode-gitlens/issues/2362) - Visual File History becomes unavailable when the workspace contains private repo
- Fixes [#2381](https://github.com/gitkraken/vscode-gitlens/issues/2381) - can't use scrollbar in 'Commit Graph' view
- Fixes an issue where focusout hides toolbar actions for the graph
- Fixes an issue where _Switch to Another Branch..._ doesn't work in the Graph editor toolbar
- Fixes graph issue with row highlighting/dimming sticking when the graph loses focus
- Fixes graph issue with branches remaining hovered/extended when the mouse leaves the graph

***

<a id="v13-1"></a>
## Version 13.1

### Thursday, November 17th, 2022

With GitLens 13, we released the power of GitLens+ features like the Commit Graph, Visual File History, and Worktrees to ALL users on local and public repos. No account required. Learn more about the changes happening with GitLens in this [article](https://www.gitkraken.com/blog/gitlens-13).

<img src="/wp-content/uploads/GitLens-13-1-Hero.png" class="img-responsive center img-bordered">

## Commit Graph Enhancements

### Search History

Find what you seek with ease! Quickly navigate through your search history by using the  UP⇧ or DOWN⇩ arrow keys.

<img src="/wp-content/uploads/New-Search-History.gif" class="img-responsive center img-bordered">

### New Search Filter @me

Want to see only your commits? Search For  @me to highlight only your commits.

<img src="/wp-content/uploads/atmegif.gif" class="img-responsive center img-bordered">

## Faster Interactive Rebase Editor

With GitLens 13.1, we overhauled the Interactive Rebase Editor. It is now dramatically faster, especially for large rebases. We also streamlined the user experience with a persistent header and footer to ensure you always have important context visible and can quickly start or abort the rebase. Also, anytime the commit author and committer are different, you will see both of their avatars.

<img src="/wp-content/uploads/Faster-Interactive-Rebase-Editor.png" class="img-responsive center img-bordered">

### Commit Details View Usage

Need additional details to complete your rebase more efficiently? Now, as you navigate commits, we show the selected commit details in the Commit Details view.

## Commit Details View Improvements

### Custom Autolinks

Custom and basic provider-based autolinks are now shown in the Autolinks section.

### Customizable Settings

You can now customize the Commit Details view from the GitLens Settings editor to personalize how it looks and behaves so you can focus on the most  important details.

<img src="/wp-content/uploads/commit-details-view-1.png" class="img-responsive center img-bordered">

## Terminal Links Can Use the Commit Details View

Terminal Links for commits in VS Code’s integrated terminal now use the Commit Details view to provide rich details about the selected commit.

## GitLens Home View Updates

Keeping a home tidy is important! We’ve streamlined the Home view to make it even easier to get started with GitLens, learn about its features, and how to personalize your experience.

<img src="/wp-content/uploads/New-Home-Side-Panel.png" class="img-responsive center img-bordered">

## Added

- Adds Commit Graph enhancements
  - Adds the ability to set keyboard shortcuts to commits and stashes on the Commit Graph — closes [#2345](https://github.com/gitkraken/vscode-gitlens/issues/2345)
    - Keyboard shortcuts can be applied to many of the gitlens.graph.* commands and should use gitlens:webview:graph:focus && !gitlens:webview:graph:inputFocus for their "When Expression" to only apply when the Commit Graph is focused
    - For example, add the following to your keybindings.json to allow Ctrl+C to copy the selected commit's SHA to the clipboard
{
    "key": "ctrl+c",
    "command": "gitlens.graph.copySha",
    "when": "gitlens:webview:graph:focus && !gitlens:webview:graph:inputFocus"
}
- Automatically selects the HEAD commit in the Commit Graph when switching branches
- Improves performance of updating the Commit Graph when the repository changes
- Improves performance by avoiding unnecessary updates to the Commit Details view when selection changes
- Adds a @me search filter to the search box
- Adds history navigation to the search box in the Commit Graph
  - When the search field is focused, use the up arrow and down arrow to navigate through any previous searches that yielded results
  - Adds ability to reset to any commit in the Commit Graph and GitLens views — closes [#2326](https://github.com/gitkraken/vscode-gitlens/issues/2326)
- Adds Interactive Rebase Editor performance and UX improvements
  - Changes the header and footer to always be visible
  - Shows the Commit Details view on commit selection
    - Adds a gitlens.rebaseEditor.showDetailsView setting to specify when to show the Commit Details view for the selected row in the Interactive Rebase Editor
  - Adds full (multiline) commit message
  - Adds the f fixup shortcut key to UI
  - Consolidates the UI for author and committer information into a stack of avatars
  - Adds emoji support for commit messages — closes [#1789](https://github.com/gitkraken/vscode-gitlens/issues/1789)
  - Ensures that large rebases show rich commit details
- Adds Commit Details view improvements
  - Adds custom and non-rich integration-based autolinks and improves autolink display
  - Improves performance by avoiding unnecessary updates
  - Avoids "pinning" commits by default when opened from the Commit Graph, Visual File History, quick picks, etc
  - Adds a Open in Commit Graph button even when showing uncommitted changes
- Adds new sections and settings to the GitLens Interactive Settings
  - Adds a new Commit Details view section
  - Adds a new Terminal Links section
  - Adds autolink configuration to the Hovers section
- Adds a @me search filter to commit search in the Search & Compare view and quick pick
- Adds product usage telemetry
  - Honors the overall VS Code telemetry settings and add a gitlens.telemetry.enabled setting opt-out specifically for GitLens

## Changed

- Changes the Home view to always be available and polishes the experience
- Changes SHA terminal links to use the Commit Details view — closes [#2320](https://github.com/gitkraken/vscode-gitlens/issues/2320)
  - Adds a gitlens.terminalLinks.showDetailsView setting to specify whether to show the Commit Details view when clicking on a commit link
- Changes to uses VS Code as Git's core.editor for terminal run commands — closes [#2134](https://github.com/gitkraken/vscode-gitlens/issues/2134) thanks to PR [#2135](https://github.com/gitkraken/vscode-gitlens/pull/2135) by Nafiur Rahman Khadem [@ShafinKhadem](https://github.com/ShafinKhadem)
  - Adds a gitlens.terminal.overrideGitEditor setting to specify whether to use VS Code as Git's core.editor for GitLens terminal commands
- Polishes webview (Commit Graph, Interactive Rebase Editor, etc) scroll bars to match VS Code's style and behavior

## Fixed

- Fixes [#2339](https://github.com/gitkraken/vscode-gitlens/issues/2339) - Commit details "Autolinks" group shows wrong count
- Fixes [#2346](https://github.com/gitkraken/vscode-gitlens/issues/2346) - Multiple cursors on the same line duplicate inline annotations; thanks to PR [#2347](https://github.com/gitkraken/vscode-gitlens/pull/2347) by Yonatan Greenfeld [@YonatanGreenfeld](https://github.com/YonatanGreenfeld)
- Fixes [#2344](https://github.com/gitkraken/vscode-gitlens/issues/2344) - copying abbreviated commit SHAs is not working
- Fixes [#2342](https://github.com/gitkraken/vscode-gitlens/issues/2342) - Local remotes are incorrectly treated as private
- Fixes [#2052](https://github.com/gitkraken/vscode-gitlens/issues/2052) - Interactive Rebase fails to start when using xonsh shell due to command quoting
- Fixes [#2141](https://github.com/gitkraken/vscode-gitlens/issues/2141) - GitLens' rebase UI randomly fails loading interactive rebase when performed outside of VSC
- Fixes [#1732](https://github.com/gitkraken/vscode-gitlens/issues/1732) - Phantom rebase-merge directory (rm -rf ".git/rebase-merge")
- Fixes [#1652](https://github.com/gitkraken/vscode-gitlens/issues/1652) - Closing interactive rebase editor after "git rebase --edit" aborts rebase-in-progress
- Fixes [#1549](https://github.com/gitkraken/vscode-gitlens/issues/1549) - Fetch does not work when local branch name differs from remote branch name
- Fixes [#2292](https://github.com/gitkraken/vscode-gitlens/issues/2292) - Push button in BranchTrackingStatusNode of non-current branch does not trigger "Push force"
- Fixes [#1488](https://github.com/gitkraken/vscode-gitlens/issues/1488) - Open Folder History not working with non-English language pack
- Fixes [#2303](https://github.com/gitkraken/vscode-gitlens/issues/2303) - "Googlesource" gerrit only supports two levels of domain — thanks to PR [#2304](https://github.com/gitkraken/vscode-gitlens/pull/2304) by Matt Buckley [@Mattadore](https://github.com/Mattadore)
- Fixes [#2315](https://github.com/gitkraken/vscode-gitlens/issues/2315) - Commit details secondary side bar banner doesn't stay dismissed
- Fixes [#2329](https://github.com/gitkraken/vscode-gitlens/issues/2329) - Remember UI settings in Commit Details panel
- Fixes [#1606](https://github.com/gitkraken/vscode-gitlens/issues/1606) - Adjusts capitalization of "URL" — thanks to PR [#2341](https://github.com/gitkraken/vscode-gitlens/pull/2341) by Dave Nicolson [@dnicolson](https://github.com/dnicolson)
- Fixes issue where we weren't honoring the default gravatar style (gitlens.defaultGravatarsStyle) in certain cases
- Fixes graph issue where stashes are sometimes assigned the wrong column
- Fixes graph issue with commit rows being incorrectly hidden in some cases
- Fixes graph issue with merge commits not being hidden correctly in some cases
- Fixes some graph issues with hover on branch/tag labels


***

<a id="v13-0"></a>
## Version 13.0

### Monday, October 17th, 2022

Find what you seek.

<img src="/wp-content/uploads/gitlens-13-social-3x.png" class="img-responsive center img-bordered">

## ✨GitLens+ Features for All on Local & Public Repos

With GitLens 13.0, we are excited to bring the power of GitLens+ features like the Commit Graph, Visual File History, and Worktrees to ALL  users on local and public repos. No account required. Learn more about the changes happening with GitLens in this [article](https://www.gitkraken.com/blog/gitlens-13).

Here’s how to get started with each of the GitLens+ features with your local or public repos:

- [Commit Graph](https://help.gitkraken.com/gitlens/gitlens-plus/#commit-graph)
- [Worktrees](https://help.gitkraken.com/gitlens/gitlens-plus/#worktrees)
- [Visual File History](https://help.gitkraken.com/gitlens/gitlens-plus/#visual-file-history)

## ✨Commit Graph  - Now out of Preview!

We’re delighted to announce that the Commit Graph is out of Preview, and is full featured! This means you may now interact with the Commit Graph directly and take actions like:

- Interact with branches, commits, tags and more with right-click context menus
- Double click a branch to checkout a branch
- Search and filter for commits
- Get information about Pull Requests

### Full context menu support

Interact with your branches, commits, and more! Context menus are now available when you right click on any branch, tag, commit, or author in the Commit Graph. You may even interact with the Commit Graph column headers to the author, date or SHA columns. So much power!

<img src="/wp-content/uploads/Commit-Search-Context-Menus.gif" class="img-responsive center img-bordered">

Context menu actions include but are not limited to:

- Switch to Branch
- Revert Commit
- Switch to Commit
- Create Branch
- Merge
- Rebase
- Create Worktree
- Create Pull Request

### Rich commit search

Find exactly what you are looking for with the rich search on the powerful new Commit Graph.

Whether searching for a specific commit, message, author, a changed file or files, or even a specific code change, the Commit Graph will highlight matching results across your entire repository. Use shortcut keys or the up/down arrows on the search bar  to navigate the search results; `F3` (also `Cmd+G` on macOS) goes to the next result from your selection while  `Shift+F3`  ( also `Shift+Cmd+G` on macOS) goes to the previous. Additionally you can quickly jump to the first or  last result, by holding `Shift` while clicking on the up/down arrows respectively – to make it easy to see when a file or change was introduced into the codebase.

<img src="/wp-content/uploads/Rich-Commit-Search.png" class="img-responsive center img-bordered">

Once you type search filtering criteria, use the arrow icons to move through each result.

<img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="img-responsive center img-bordered">

### PR information in form of icon

Wait, which branch has that PR?

If connected to one of the rich integrations with GitHub or GitLab, the Commit Graph will display a PR icon for any branch currently in PR. Right-click on the PR icon to open the PR on the GitHub or GitLab, or copy the URL.

<img src="/wp-content/uploads/PR-Icon.png" class="img-responsive center img-bordered">

### Hiding remotes, branches or tags

Need to focus and have too many remotes or just want to curate how much is shown in your Commit Graph? Now you can hide entire remotes, or specific branches and tags. Hover over any  branch or tag to access the “Hide” button  or right-click to hide the whole remote, or just the local or remote branch, to help focus your Commit Graph.

<img src="/wp-content/uploads/Branch-Hide.png" class="img-responsive center img-bordered">

### All new home view

It’s a homecoming! Our GitLens home view has a new look, with quick links to our Getting Started guides, Integrations, Trial info, and Feature spotlights.

<img src="/wp-content/uploads/GitLens-Home.png" class="img-responsive center img-bordered">

### List or tree view in Commit Details View

The Commit Details View, which gives you contextual change info about your code, got a new toggle for List and Tree view.

<img src="/wp-content/uploads/view-as-list.png" class="img-responsive center img-bordered">

To open the Commit Details view, open the command palette using <kbd>Cmd+Shift+P</kbd> and type: Show Commit Details view or navigate to the Commit Details view in the Side Bar.

# Change Log

### Added

- ✨ All GitLens+ features on public and local repos are now available to everyone -- no account required!
  - We want to bring the power of GitLens+ features to more people without any gates.
- ✨ Commit Graph is out of preview!
  - Rich search features to find exactly what you're looking for:
    - Powerful filters to search by commit, message, author, a changed file or files, or even a specific code change
    - Searches look at ALL commits in a repository, not just what's shown in the graph
  - PR support for connected rich integrations (GitHub/GitLab)
  - Contextual right-click menus with popular actions for commits, branches, tags, and authors
  - Personalization of your graph experience
    - Show and hide branches and columns
    - Settings UI for easy fine-grain control over advanced settings
- Adds `View as Tree` option for changed files in the _Commit Details_ view
- Adds an `Open in Commit Graph` action to the hovers and commit quick pick menus

### Changed

- Updates the `Home View` with all new design and content
- Changes the `Show Commit` action in the hovers to `Show Details` and opens the _Commit Details_ view

### Fixed

- Fixes [#2203](https://github.com/gitkraken/vscode-gitlens/issues/2203) - Autolinks missing under commit details
- Fixes [#2230](https://github.com/gitkraken/vscode-gitlens/issues/2230) - j and k are inverted in ascending rebase order
- Fixes [#2195](https://github.com/gitkraken/vscode-gitlens/issues/2195) - Cannot open new files from commit details
- Fixes Commit Details view showing incorrect diffs for certain commits
- Fixes Commit Details view showing incorrect actions for uncommitted changes
- Fixes prioritization of multiple PRs associated with the same commit to choose a merged PR over others
- Fixes Graph not showing account banners when access is not allowed and trial banners were previously dismissed


***

<a id="v12-2"></a>
## Version 12.2

### Tuesday, August 30th, 2022

The new Commit Graph 🎨 in GitLens 12.2 will fix all your commitment problems...in your code 🥁 👩‍💻

<div class='embed-container embed-container--16-9'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/EsnA4zIUvWY?controls=1&modestbranding=1" frameborder="0" allowfullscreen></iframe>
</div>

## ✨Commit Graph  - Preview

Users may now view the Commit Graph of their repository through GitLens.

This beloved feature from GitKraken Client helps visualize your repo commit history and give you information about branches, commits, and collaborators all in one view — making it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/1-commit-graph.png" class="img-responsive center img-bordered">

To open the Commit Graph, open the command palette using the keyboard shortcut <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd> and type `Show Commit Graph`.

<img src="/wp-content/uploads/2-commit-graph.gif" class="img-responsive center img-bordered">

This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths.

You may also access the Commit Graph by clicking this graph icon from the Source Control view in the Sidebar or Status Bar.

<img src="/wp-content/uploads/How-to-open-commit-graph-B.png" class="img-responsive center img-bordered">

The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens+ subscription can use the Commit Graph with private repos.

For those on [vscode.dev](vscode.dev) or [github.dev](github.dev), this also means you can open the Commit Graph on a web browser.

The Commit Graph is in `Preview` mode, and we’d love to hear your feedback in the [Commit Graph discussion on GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).



## Commit Details View

GitLens 12.2 also ships with a `Commit Details View`, which gives you contextual change info about your code.

<img src="/wp-content/uploads/3-commit-details-view.png" class="img-responsive center img-bordered">

To open the `Commit Details View`, open the command palette using <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd> and this time type: `Show Commit Details View` or navigate to the Commit Details View in the Sidebar.

<img src="/wp-content/uploads/4-commit-details-view.gif" class="img-responsive center img-bordered">

The `Commit Details View` updates as you move your cursor throughout the file with information about the commit that modified that line of code. Get quick information about the commit author, commit ID, links to Pull Requests, files modified in the commit, and more.

Click on a file to open the diff, and see what changed. You may also hover over the file name to access options like Open File, Open Changes with Working File, and Open Remote.


## ✨ GitHub Enterprise Integration

Next, GitLens+ now offers a richer integration with GitHub Enterprise.

Once authenticated, GitLens will enrich GitHub autolinks in the hovers. You’ll see your GitHub Enterprise avatar, links to related pull requests, along with a footnote of the pull request or issue details.

<img src="/wp-content/uploads/6-GitHub-Enterprise.png" class="img-responsive center img-bordered">

You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

## ✨ Single Sign On


Single Sign On is here, providing GitLens+ users with a more secure sign in method!


### Requirements and configuration

Your GitKraken account may now initiate an Oauth authentication flow with the following supported Identity Providers (IdPs):

- Azure Active Directory
- Okta
- Google Identity Platform
- Ping Identity


<img src="/wp-content/uploads/SSO-setup.png" class="img-responsive center img-bordered">

Please note that your IdP will first need to be configured before setting up the connection in your GitKraken account. For assistance, please contact your IdP administrator or consult the IdP documentation for help.

Additional requirements:
    - Configurable only by GitKraken Owner or Admin of an organization
    - Subscribed to either the Teams or Enterprise plan

→ [Documentation: How to set up SSO in GitKraken](https://help.gitkraken.com/gitkraken-client/single-sign-on/)

### Signing in with SSO

GitLens+ users should see a new option to Sign in with SSO from the login screen.

<img src="/wp-content/uploads/9-GitLens-SSO.png" class="img-responsive center img-bordered">

After clicking `Sign in with SSO`, the SSO form will open and ask for an email address to use for SSO login. The app will then check the email and determine whether the email address belongs to a single IdP for SSO. When the email address is successfully identified, the user will be taken to that IdP to login.

Once authenticated, the user may use GitLens+


## More improvements

### Stash naming defaults

When applying or popping a stash, GitLens will default the commit message input to the stash message.

<img src="/wp-content/uploads/10-stash-commit-message.gif" class="img-responsive center img-bordered">

And when stashing changes, the stash name will now default to any entry in the commit message input.

### Stats in comparisons

There are now stats about additions & deletions in files nodes in comparisons. To get these stats, navigate to the `Search & Compare` view in the Sidebar and create a comparison between commits.

<img src="/wp-content/uploads/11-comparison-stats.png" class="img-responsive center img-bordered">

### Search for text in Interactive Rebase Editor

And users may now search for text on the `Interactive Rebase Editor` using <kbd>Ctrl</kbd> <kbd>F</kbd>.

<img src="/wp-content/uploads/12-interactive-rebase-text-search.png" class="img-responsive center img-bordered">


## Change Log


### Added

- Adds Commit Graph
- Adds Commit Details View
- Adds [**rich integration**](https://github.com/gitkraken/vscode-gitlens#remote-provider-integrations-) with GitHub Enterprise &mdash; closes [#1210](https://github.com/gitkraken/vscode-gitlens/issues/1210)
  - Adds associated pull request to line annotations and hovers
    ![Pull requests on line annotation and hovers](https://raw.githubusercontent.com/gitkraken/vscode-gitlens/main/images/docs/hovers-current-line-details.png)
  - Adds associated pull request to status bar blame
    ![Pull requests on status bar](https://raw.githubusercontent.com/gitkraken/vscode-gitlens/main/images/docs/status-bar.png)
  - Adds GitHub avatars
  - Adds associated pull requests to branches and commits in GitLens views
  - Adds rich autolinks for GitHub issues and merge requests, including titles, status, and authors
  - Adds rich support to _Autolinked Issues and Pull Requests_ within comparisons to list autolinked GitHub issues and merge requests in commit messages
- Adds new stash behaviors to use the Source Control (commit message) input box &mdash; closes [#2081](https://github.com/gitkraken/vscode-gitlens/issues/2081)
  - When a stash is applied or popped and the Source Control input is empty, we will now update the Source Control input to the stash message
  - When stashing changes and the Source Control input is not empty, we will now default the stash message input to the Source Control input value
- Adds the ability to search (<kbd>Ctrl</kbd>+<kbd>F</kbd>) for text on the Interactive Rebase Editor &mdash; closes [#2050](https://github.com/gitkraken/vscode-gitlens/issues/2050)
- Adds stats (additions & deletions) to files nodes in comparisons &mdash; closes [#2078](https://github.com/gitkraken/vscode-gitlens/issues/2078) thanks to help via [PR #2079](https://github.com/gitkraken/vscode-gitlens/pull/2079) by Nafiur Rahman Khadem ([@ShafinKhadem](https://github.com/ShafinKhadem))
- Adds the ability to uniquely format uncommitted changes for the current line blame annotations &mdash; closes [#1987](https://github.com/gitkraken/vscode-gitlens/issues/1987)
  - Adds a `gitlens.currentLine.uncommittedChangesFormat` setting to specify the uncommitted changes format of the current line blame annotation. **NOTE**: Setting this to an empty string will disable current line blame annotations for uncommitted changes
- Adds variable expansion support to the `gitlens.worktrees.defaultLocation` setting
  - `${userHome}` &mdash; the path of the user's home folder
  - `${workspaceFolder}` &mdash; the path of the folder opened in VS Code containing the specified repository
  - `${workspaceFolderBasename}` &mdash; the name of the folder opened in VS Code containing the specified repository without any slashes (/)
- Adds owner avatars to remotes in the _Remotes_ view for GitHub remotes

### Changed

- Greatly improves performance of many view interactions when connected to a rich integration and pull request details are enabled, including:
  - Showing and refreshing the _Commits_ view
  - Expanding commits, branches, and worktrees
- Remembers chosen filter on files nodes in comparisons when refreshing
- Changes display of filtered state of files nodes in comparisons
- Improves diff stat parsing performance and reduced memory usage
- Disallows comparisons with the working tree on the right-side (left-side still works as expected) and disables swapping
- Uses VS Code as `core.editor` in rebase &mdash; closes [#2084](https://github.com/gitkraken/vscode-gitlens/issues/2084) thanks to [PR #2085](https://github.com/gitkraken/vscode-gitlens/pull/2085) by Nafiur Rahman Khadem ([@ShafinKhadem](https://github.com/ShafinKhadem))

### Fixed

- Fixes [#2156](https://github.com/gitkraken/vscode-gitlens/issues/2156) - Reduce extension package size
- Fixes [#2136](https://github.com/gitkraken/vscode-gitlens/issues/2136) - Search & Compare quickpick shouldn't select the mode text when opening
- Fixes [#1896](https://github.com/gitkraken/vscode-gitlens/issues/1896) - Cannot read property 'fsPath' of undefined
- Fixes [#1550](https://github.com/gitkraken/vscode-gitlens/issues/1550) - Push button in commit widget does not trigger "Push force" when ALT is pressed.
- Fixes [#1991](https://github.com/gitkraken/vscode-gitlens/issues/1991) - Git lens status bar entry has an incomprehensible accessibility label
- Fixes [#2125](https://github.com/gitkraken/vscode-gitlens/issues/2125) - "git log" command in version 12.x is very slow
- Fixes [#2121](https://github.com/gitkraken/vscode-gitlens/issues/2121) - Typo in GitLens header &mdash; thanks to [PR #2122](https://github.com/gitkraken/vscode-gitlens/pull/2122) by Chase Knowlden ([@ChaseKnowlden](https://github.com/ChaseKnowlden))
- Fixes [#2082](https://github.com/gitkraken/vscode-gitlens/issues/2082) - GitLens Home view unreadable in certain themes
- Fixes [#2070](https://github.com/gitkraken/vscode-gitlens/issues/2070) - Quoted HTML / JSX syntax is not escaped correctly
- Fixes [#2069](https://github.com/gitkraken/vscode-gitlens/issues/2069) - Heatmap - incorrect behavior of gitlens.heatmap.fadeLines with gitlens.heatmap.ageThreshold
- Fixes an issue where choosing "Hide Current Branch Pull Request" from the _Commits_ view overflow menu wouldn't hide the PR node
- Fixes an issue where stashes without a message aren't displayed properly
- Fixes an issue where the _Stashes_ view empty state isn't displayed properly when there are no stashes
- Fixes typos via [PR #2086](https://github.com/gitkraken/vscode-gitlens/pull/2086) by stampyzfanz ([@stampyzfanz](https://github.com/stampyzfanz)), and [PR #2043](https://github.com/gitkraken/vscode-gitlens/pull/2043), [PR #2040](https://github.com/gitkraken/vscode-gitlens/pull/2040), [PR #2042](https://github.com/gitkraken/vscode-gitlens/pull/2042) by jogo- ([@jogo-](https://github.com/jogo-))
