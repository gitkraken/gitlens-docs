---
title: GitLens Release Notes
description: GitLens Release Notes
taxonomy:
  category: gitlens
---

Find out what’s new, what’s fixed, or just take a trip down memory lane remembering those bugs of yesterday.

Check out our [Changelog](https://github.com/gitkraken/vscode-gitlens/blob/main/CHANGELOG.md) to see linked issues and past changes.

<a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank" class="button button--basic ">Install Current Version Now</a>

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos \
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Free, Pro, etc

---
<a id="v16-0"></a>

## Version 16.0

#### Tuesday, November 12, 2024

<a id="v15-6"></a>

## Version 15.6

#### Monday, October 7, 2024

GitLens 15.6 arrives with easier branch workflows from within the Commit Graph, Account View integrated into the Home View, improved Cursor support, and a host of other improvements and bug fixes.

<img src="/wp-content/uploads/gl-15-6-hero.png" class="img-responsive center img-bordered">

### Commit Graph Improvements

GitLens 15.6 includes several new features and improvements for the Commit Graph:

The graph toolbar now includes a new _Create New Branch_ button in the upper-right corner that allows you to conveniently create a new branch (and worktree, if you prefer) from the current branch or commit. Furthermore, when your current branch is both ahead and behind its upstream, we've added a new _Force Push_ button to the toolbar next to the _Pull_ button that allows you to force push your current branch to its upstream (always force push with caution, as you may lose commits). These new buttons allow for easier entry into common branch workflows directly from the Commit Graph.

The Commit Graph sidebar is now enabled by default. You can disable it by setting `gitlens.graph.sidebar.enabled` to `false` in your settings.

Finally, we've improved the integration indicator and connection button on the upper left corner of the graph toolbar. The icon now more accurately reflects the hosting service for the current repository, and hovering over the connect button now provides some more context on the benefits of connecting the integration.

### Account View moved into Home View

The Account View has been moved into the bottom of the Home View as a new collapsible section. You can quickly jump into the Home View with the _GitLens: Show Home View_ command and expand the Account section to manage your account, cloud integrations and active organization, or leave it collapsed to view account status at a glance.

### Cursor Support

GitLens 15.6 improves support for GitLens in the Cursor editor. Cursor users can now take full advantage of GitLens commands, views and functionality, including account login and sign-up, within Cursor.

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- Jean Pierre ([@jeanp413](https://github.com/jeanp413))

### Added

- Adds [Cursor](https://cursor.so) support &mdash; closes [#3222](https://github.com/gitkraken/vscode-gitlens/issues/3222)
- Adds monospace formatting in commit messages &mdash; closes [#2350](https://github.com/gitkraken/vscode-gitlens/issues/2350)
- Adds a new `${authorFirst}` and `${authorLast}` commit formatting tokens that can be used in inline blame, commit hovers, etc &mdash; closes [#2980](https://github.com/gitkraken/vscode-gitlens/issues/2980)
- Adds a new _Create New Branch_ button to the _Commit Graph_ toolbar &mdash; closes [#3553](https://github.com/gitkraken/vscode-gitlens/issues/3553)
- Adds new ability to force push from the _Commit Graph_ toolbar&mdash; closes [#3493](https://github.com/gitkraken/vscode-gitlens/issues/3493)
- Adds a new `gitlens.launchpad.includedOrganizations` setting to specify which organizations to include in _Launchpad_ &mdash; closes [#3550](https://github.com/gitkraken/vscode-gitlens/issues/3550)
- Adds repository owner/name and code suggest to hovers on the experimental Launchpad view

### Changed

- Integrates the _GitKraken Account_ view into the bottom of the _Home_ view as a collapsible section &mdash; closes [#3536](https://github.com/gitkraken/vscode-gitlens/issues/3536)
- Changes the new _Commit Graph_ sidebar to be enabled by default; use the `gitlens.graph.sidebar.enabled` settings to disable it
- Changes how GitLens handles creating and renaming branches to avoid using the terminal &mdash; refs [#3528](https://github.com/gitkraken/vscode-gitlens/issues/3528)
- Changes patch generation (e.g. cloud patches, code suggest, _Copy as Patch_, _Copy WorkingChanges to Worktree..._, etc) to automatically include untracked files
- Improves _Switch_, _Open in Worktree_, and deeplink and Launchpad workflows
  - Reduces prompts for locating repositories which the user has previously opened &mdash; closes [#3555](https://github.com/gitkraken/vscode-gitlens/issues/3555)
  - Improves automatic detection of matching repositories for pull requests &mdash; closes [#3627](https://github.com/gitkraken/vscode-gitlens/issues/3627)
  - Automatically fetches the repository when needed rather than prompting the user
- Improves the integration connection indicator and connection button on the _Commit Graph_ &mdash; closes [#3538](https://github.com/gitkraken/vscode-gitlens/issues/3538)

### Fixed

- Fixes [#3548](https://github.com/gitkraken/vscode-gitlens/issues/3548) - Change the current branch icon on the Commit Graph to a worktree icon if its on a worktree
- Fixes [#3592](https://github.com/gitkraken/vscode-gitlens/issues/3592) - Connecting to an integration via Remotes view (but likely others) doesn't work
- Fixes [#3571](https://github.com/gitkraken/vscode-gitlens/issues/3571) - Gitlens fails to register buttons on top-right corner &mdash; thanks to [PR #3605](https://github.com/gitkraken/vscode-gitlens/pull/3605) by Jean Pierre ([@jeanp413](https://github.com/jeanp413))
- Fixes [#3617](https://github.com/gitkraken/vscode-gitlens/issues/3617) - Auto-links not working for alphanumberic issue numbers
- Fixes [#3573](https://github.com/gitkraken/vscode-gitlens/issues/3573) - 'Create Branch in Worktree' option in 'Create Branch' shows a repo picker if you have multiple repos open
- Fixes [#3612](https://github.com/gitkraken/vscode-gitlens/issues/3612) - Prevents cloud integration sync process from opening gkdev connect page/flow
- Fixes [#3519](https://github.com/gitkraken/vscode-gitlens/issues/3519) - Add fallback/cutoff to our backend calls similar to how we handle GitHub queries
- Fixes [#3608](https://github.com/gitkraken/vscode-gitlens/issues/3608) - Integration connection page opening on every launch of VS Code and on profile change
- Fixes [#3618](https://github.com/gitkraken/vscode-gitlens/issues/3618) -Reauthentication not working for cloud integrations
- Fixes an issue where virtual repositories for GitHub PRs from forks wouldn't load properly
- Fixes an issue where deleting a worktree would not always remove the worktree from the view
- Fixes actions not working on Launchpad items with special characters in their branch name
- Fixes _Open in Worktree_ command sometimes showing an unnecessary worktree confirmation step
- Fixes some instances where the progress notification lingers after canceling when connecting an integration

### Engineering

- Adds end-to-end testing infrastructure using [Playwright](https://playwright.dev)
- Adds vscode-test to run unit-tests &mdash; closes [#3570](https://github.com/gitkraken/vscode-gitlens/issues/3570)

<a id="v15-5"></a>

## Version 15.5

#### Thursday, September 12, 2024

GitLens 15.5 brings a few notable changes for the Commit Graph, current branches and worktree creation.

<img src="/wp-content/uploads/gl-15-5-hero.png" class="img-responsive center img-bordered">

### Launchpad Preview Ending

Preview access to Launchpad ends on September 27th. After this date, GitLens users will need a Pro account to continue accessing Launchpad and Launchpad View. The Launchpad status bar summary will continue to be free for everyone.

### Commit Graph Sidebar

We've equipped the Commit Graph with a sidebar which gives you quick and convenient access to branches, remotes, stashes, tags, and worktrees from within the graph. Clicking an icon from the sidebar will take you to its respective view. You can enable the new sidebar by setting `gitlens.graph.sidebar.enabled` to `true` in your settings.

### Current Branch Visibility

You now have the option to see your current branch at the top of the list anywhere local branches are shown in views. To enable this feature, turn on `gitlens.views.showCurrentBranchOnTop` in settings.

### Simplified Worktree Creation

We've streamlined the Create Worktree command flow, now prompting for a new branch name only when necessary. This simplifies the creation of worktrees from different sources.

### Added

- Adds a `gitlens.views.showCurrentBranchOnTop` setting to specify whether the current branch is shown at the top of the views &mdash; closes [#3520](https://github.com/gitkraken/vscode-gitlens/issues/3520)
- Adds a sidebar to the _Commit Graph_
  - Shows counts of branches, remotes, stashes, tags, and worktrees
  - Clicking an item reveals it's corresponding view
  - Try out this new feature by enable the setting `gitlens.graph.sidebar.enabled` to `true`

### Changed

- Preview access of Launchpad is ending on September 27th
- Improves the branch comparisons in views to automatically select the base or target branch

### Fixed

- Fixes [#3514](https://github.com/gitkraken/vscode-gitlens/issues/3514) - Attempting to delete the main worktree's branch causes a invalid prompt to delete the main worktree
- Fixes [#3518](https://github.com/gitkraken/vscode-gitlens/issues/3518) - Branches in worktrees are no longer collapsed into folder groupings

### Removed

- Removes (disables) legacy "focus" editor

<a id="v15-4"></a>

## Version 15.4

#### Wednesday, September 4, 2024

GitLens 15.4 focuses on branches and worktrees, with icon, action, and tooltip upgrades that make the association between branches and worktrees clearer, improved cleanup when deleting a branch with a worktree or a worktree with a branch, improvements to comparisons, and more.

<img src="/wp-content/uploads/gl-15-4-hero.png" class="img-responsive center img-bordered">

### Worktee Enhancements

Branches in views and quick pick menus have received a few visual improvements to reduce clutter and make it easier to understand branch state. Branches with worktrees now display a repository icon instead of the typical branch icon, and the tooltip now also indicates that the branch is in a worktree. Branch tooltips now also split out information in a way that is easier to read.

### Branch & Worktree Cleanup Improvements

When a branch has an associated worktree, it is now easier to clean up the associated branch when deleting the worktree, and vice versa. Using the _Git Delete Worktree_ command on a worktree now also includes options to delete or force-delete both the worktree and its associated branch. Similarly, when deleting a branch that has a worktree, the user is first presented with options for deleting the branch's worktree before deleting the branch itself.

### Branch Comparison Improvements

On the _Commits_ view and nested within branches on the _Branches_ view, there is a comparison item to quickly compare the branch with another reference (branch, commit, tag, etc). In GitLens 15.4, we now automatically pick the "best" target branch as the default reference to compare with. Expand the _Ahead_ item to review your changes as they would be applied to the target branch.

### Commit Graph Search Additions

On the _Commit Graph_ (and commit search from the _Search & Compare_ view) you can now limit a search to only search within stashes. Use `type:stash` (or `is:stash`) to highlight all your stashes, or add it to a search query to limit the results to stashes.

### Added

- Adds better support for branches in worktrees
  - Changes the branch icon to a "repo" icon when the branch is in a worktree in views, quick pick menus, and the _Commit Graph_
  - Adds an _Open in Worktree_ inline and context menu command and an _Open in Worktree in New Window_ context menu command to branches and pull requests in views and on the _Commit Graph_
  - Removes the _Switch to Branch..._ inline and context menu command from branches in views and on the _Commit Graph_ when the branch is in a worktree
- Adds ability to only search stashes when using `type:stash` (or `is:stash`) in commit search via the _Commit Graph_, _Search & Compare_ view, or the _Search Commits_ command
- Adds `...` inline command for stashes on the _GitLens Inspect_ view
- Adds an "up-to-date" indicator dot to the branch icon of branches in views
- Adds an "alt" _Pull_ command for the inline _Fetch_ command on branches in views
- Adds an "alt" _Fetch_ command for the inline _Pull_ command on branches in views
- Adds _Open Comparison on Remote_ command to branch comparisons in views
- Adds new options to the _Git Delete Worktree_ command to also delete the associated branch along with the worktree

### Changed

- Improves the branch comparisons in views to automatically select the base or target branch
- Improves tooltips on branches, remotes, and worktrees in views
- _Upgrade to Pro_ flows now support redirects back to GitLens

### Fixed

- Fixes [#3479](https://github.com/gitkraken/vscode-gitlens/issues/3479) - Tooltip flickering
- Fixes [#3472](https://github.com/gitkraken/vscode-gitlens/issues/3472) - "Compare working tree with.." often flashes open then closes the menu
- Fixes [#3448](https://github.com/gitkraken/vscode-gitlens/issues/3448) - "Select for Compare" on a Commit/Stash/etc causes the Search and Compare view to be forcibly shown
- Fixes the _Git Delete Branch_ command when deleting a branch that is open on a worktree by adding a step to delete the branch's worktree first
- Fixes an issue where pull requests in views could show the wrong comparison with the working tree when using worktrees
- Fixes _Copy Remote Comparison URL_ command to not open the URL, just copy it
- Fixes cloud integrations remaining disconnected after disconnecting and reconnecting to a GitKraken account
- Fixes "switch" deep links sometimes failing to complete in cases where the switch occurs in the current window

### Removed

- Removes status (ahead, behind, etc) decoration icons from branches in views

<a id="v15-3"></a>

## Version 15.3

#### Tuesday, August 13, 2024

GitLens 15.3 arrives with a host of improvements to popular GitLens features and commands. New branch filtering in the commit graph makes it easier to review history for branches with upstreams to improve pull request reviews. Launchpad has been expanded with GitLab support and is experimentally available as a view. GitHub virtual repositories now support comparisons, and some comparison commands now take a smarter approach to determining directionality of comparison, providing more relevant and useful results.

<img src="/wp-content/uploads/gl-15-3-hero.png" class="img-responsive center img-bordered">

### Commit Graph Branch Visibility

The Commit Graph now adds a third branch visibility option: Smart Branches. Existing options allowed you to show all branches or only the current branch (and its upstream). The new Smart Branches option shows the current branch, its upstream, and its base or target branch. This provides enough history to compare local branch changes with upstream changes on your current branch, and against changes with the merge base to determine, for example, whether a rebase is needed or if conflicts might occur. This option is particularly useful for workflows like pull request reviews.

Branch visibility options have now moved out of the graph filter dropdown and into a new branch visibility dropdown to the left of it in the graph header bar.

### Launchpad Improvements

#### GitLab in Launchpad

Launchpad now includes GitLab support! You can connect your GitLab integration and see GitLab merge requests alongside GitHub pull requests. We've also added a new _Connect Additional Integrations_ button to the titlebar of Launchpad that lets you easily connect additional integrations.

#### Launchpad View (Experimental)

We're experimenting with bringing Launchpad into a view so that you can keep it open and view pull request details at a glance, in a tree format. You can enable this experimental feature either by running the _Show Launchpad View_ command or setting `gitlens.views.launchpad.enabled` to `true` in your settings file.

### Comparison Improvements

When comparing commits, stashes, and tags with the HEAD commit via context menu commands, the comparison now uses a combination of commit topology and the timestamp of the reference and HEAD commit in order to determine the directionality of the comparison.

When comparing a commit with the HEAD commit, for example, we order the comparison from the HEAD commit to the chosen commit if it is ahead in time from the HEAD commit, and from the chosen commit to the HEAD commit if it is behind. This ensures that this command, now called _Compare to/from HEAD_, is more useful in general since the revision history within the comparison is always forward-looking.

Virtual repositories, such as GitHub repositories opened locally with the GitHub Repositories extension or on vscode.dev or github.dev, now also support comparison commands within views and the Commit Graph.

### Added

- Adds improvements and enhancements to _Launchpad_ to make it easier to manage and review pull requests
  - Adds GitLab (cloud-only for now) support to show and manage merge requests in _Launchpad_
  - Adds a new _Connect Additional Integrations_ button to the _Launchpad_ titlebar to allow connecting additional integrations (GitHub and GitLab currently)
  - Adds an new experimental _Launchpad_ view to provide a persistent view of the _Launchpad_ in the sidebar
    - To try it out, run the _Show Launchpad View_ command or set the `gitlens.views.launchpad.enabled` setting to `true` &mdash; let us know what you think!
    - While its functionality is currently limited, pull requests can be expanded to show changes, commits, and code suggestions, as well as actions to open changes in the multi-diff editor, open a comparision, and more
- Adds new features and improvements to the _Commit Graph_
  - Branch visibility options, formerly in the _Graph Filtering_ dropdown, are now moved to the new _Branches Visibility_ dropdown in the _Commit Graph_ header bar
  - Adds a new _Smart Branches_ visibility option to shows only relevant branches &mdash; the current branch, its upstream, and its base or target branch, to help you better focus
  - Improves interactions with hovers on rows &mdash; they should do a better job of staying out of your way
  - Adds pull request information to branches with missing upstreams
- Adds support for GitHub and GitLab cloud integrations &mdash; automatically synced with your GitKraken account
  - Adds an improved, streamlined experience for connecting cloud integrations to GitLens
  - Manage your connected integration via the the _Manage Integrations_ command or the _Integrations_ button on the _GitKraken Account_ view
- Adds comparison support to virtual (GitHub) repositories

### Changed

- Improves the _Compare to/from HEAD_ command (previously _Compare with HEAD_) to compare commits, stashes, and tags with the HEAD commit where directionality is determined by topology and time
- Improves the messaging of the merge and rebase commands
- Renames _Compare with Working Tree_ command to _Compare Working Tree to Here_
- Renames _Compare Common Base with Working Tree_ command to _Compare Working Tree to Common Base_
- Renames _Open Worktree in New Window_ Launchpad command to _Open in Worktree_
- Renames _Open Directory Compare_ command to _Open Directory Comparison_
- Renames _Open Directory Compare with Working Tree_ command to _Directory Compare Working Tree to Here_
- Improves some messaging on _Switch_ and _Checkout_ commands

### Fixed

- Fixes [#3445](https://github.com/gitkraken/vscode-gitlens/issues/3445) - Cannot merge branch into detached HEAD
- Fixes [#3443](https://github.com/gitkraken/vscode-gitlens/issues/3443) - Don't show gitlens context menu items in Copilot Chat codeblock editors
- Fixes [#3457](https://github.com/gitkraken/vscode-gitlens/issues/3457) - Enriched autolink duplication in graph hover (and possibly other places)
- Fixes [#3473](https://github.com/gitkraken/vscode-gitlens/issues/3473) - Plus features can't be restored after they are hidden
- Fixes column resizing being stuck when the mouse leaves the _Commit Graph_
- Fixes issues with incorrect commit count when using the merge and rebase commands
- Fixes issues where a merge or rebase operation says there or no changes when there are changes
- Fixes an error with queries that can cause Jira Cloud and other cloud integrations to stop working
- Fixes issues with some directory comparison commands

<a id="v15-2"></a>

## Version 15.2

#### Wednesday, July 10th, 2024

GitLens 15.2 introduces several new features and improvements. This release focuses on enhancing the Commit Graph and Launchpad, expanding AI-generated messaging, and additional AI support for the latest Anthropic models.

<img src="/wp-content/uploads/gl-15-2-hero.png" class="img-responsive center img-bordered">

### Commit Graph Improvements

The Commit Graph now provides rich hovers on commit rows. These hovers include detailed commit information and links to related pull requests, issues, and linking to Inspect. We've also added pull request markers to the graph scroll and minimap, offering visual queues of PR activity in your repo history.

### Launchpad Improvements

We've added a new "Open Worktree in New Window" action to the Launchpad. This feature allows you to quickly open specific branches of pull requests in a separate VS Code window, minimizing context switching when working on multiple tasks.

### AI-Generated Descriptions

You can now generate titles and descriptions for Cloud Patches and Code Suggest. This is available using the "Generate Title & Description" button within the title input of the _Create Cloud Patch_ view and in the _Changes to Suggest_ section of the Inspect Overview tab. It uses the AI provider of your choice, helping to save time in creating meaningful titles and descriptions.

### Claude 3.5 Sonnet Support

GitLens now supports Anthropic's latest Claude 3.5 Sonnet model for our experimental AI features. You can switch to this version by selecting `GitLens: Switch AI Model` from the command palette.

### Added

- Adds a _Generate Title & Description_ button to the title input in _Create Cloud Patch_ and in _Changes to Suggest_ of the _Inspect Overview_ tab
- Adds support for Anthropic's Claude 3.5 Sonnet model for GitLens' experimental AI features
- Adds a new `counts` option to the `gitlens.launchpad.indicator.label` setting to show the status counts of items which need your attention in the _Launchpad_ status bar indicator
- Adds _Search for Commits within Selection_ command to the editor context menu when there is a selection
- Adds a `gitlens.launchpad.ignoredOrganizations` setting to specify an array of organizations (or users) to ignore in the _Launchpad_
- Improves the tooltips of stashes in GitLens views
  - Adds a `gitlens.views.formats.stashes.tooltip` setting to specify the tooltip format of the stashes in GitLens views
- Improves the display of branch and tag tips in the _File History_ and _Line History_ and in commit tooltips in GitLens views
  - Adds provider-specific icons to tips of remote branches
- Adds Commit Graph improvements:
  - Adds pull request markers to the graph scroll and minimap
  - Adds rich hovers on commit rows which include detailed commit information and links to pull requests, issues, and inspect
- Adds Launchpad improvements:
  - Truncates long titles for Pull Requests so that the repository label is always visible
  - Adds _Open on GitHub_ button to other relevant rows in the action step
  - Adds a new _Open Worktree in New Window_ action and button to Launchpad items to more easily view the item in a worktree

### Changed

- Renames `Reset Stored AI Key` command to `Reset Stored AI Keys...` and adds confirmation prompt with options to reset only the current or all AI keys
- Renames _Open Inspect_ to _Inspect Commit Details_
- Renames _Open Line Inspect_ to _Inspect Line Commit Details_
- Renames _Open Details_ to _Inspect Commit Details_
- Replaces _Open in Editor_ link in the Launchpad with a link to _gitkraken.dev_
- The _Manage Account_ button in the GitKraken Account view and the _GitLens: Manage Your Account_ command now use the account management page at _gitkraken.dev_
- Fixes some cases where worktree state can be out-of-date after creation/deletion of a worktree

### Fixed

- Fixes [#3344](https://github.com/gitkraken/vscode-gitlens/issues/3344) - Make changing the AI key easier
- Fixes [#3377](https://github.com/gitkraken/vscode-gitlens/issues/3377) - Cannot read properties of undefined (reading 'start')
- Fixes [#3377](https://github.com/gitkraken/vscode-gitlens/issues/3378) - Deleting a worktree (without force) with working changes causes double prompts
- Fixes fixes issue with Jira integration not refreshing
- Fixes the _Learn More_ link not working in the account verification dialog
- Upgrading to Pro and account management now no longer require the user to log in again in their respective pages on _gitkraken.dev_
- Fixes deep links failing to cancel in the remote add stage

<a id="v15-1"></a>

## Version 15.1

#### Wednesday, June 5th, 2024

We're excited to announce the latest release of GitLens, bringing you expanded AI capabilities, a better Launchpad experience, and bug fixes reported by our community.

<img src="/wp-content/uploads/gl-15-1-hero.png" class="img-responsive center img-bordered">

### GitHub Copilot and AI Model Integration

<img src="/wp-content/uploads/gl-15-1-ai-models.png" class="img-responsive center img-bordered">

GitLens now supports integration with GitHub Copilot and other VS Code extension-provided AI models for its experimental AI features. Simply select a model from the quickpick after choosing a GitLens AI action.

> You can also specify the AI model you want to use through the new `gitlens.ai.experimental.model` setting. When the model is set to `vscode`, specifying the `gitlens.ai.experimental.vscode.model` setting will target the VS Code extension-provided AI model you want to use.

To simplify the overall configuration of AI models, we have unified all settings under: `gitlens.ai.experimental.model`. This replaces the previous provider-specific settings, making it more straightforward to specify the AI model you want to use.

### Launchpad Enhancements

We've made several improvements to the Launchpad to provide a more intuitive and user-friendly experience. The collapsed state of Launchpad groups is now saved between uses, ensuring a consistent view across sessions. The Draft and Pinned categories in the Launchpad always sort their items by date, making it easier to find recent entries. The Launchpad status bar indicator now provides clear indications when there is an error loading data, keeping you informed of any issues. Additionally, we've improved loading performance and are continuing to look for ways to improve that in the future.

To leave us feedback such as what do you think, is this useful, what does it have that you like, what is it missing, etc. reach out to us on the GitLens [GitHub Discussion board](https://github.com/gitkraken/vscode-gitlens/discussions/3286). We really want to hear your feedback!

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- bm-w ([@bm-w](https://github.com/bm-w))

### Added

- Adds support for GitHub Copilot and other VS Code extension-provided AI models for GitLens' experimental AI features
  - Adds a `gitlens.ai.experimental.model` setting to specify the AI model to use
  - Adds a `gitlens.ai.experimental.vscode.model` setting to specify the VS Code extension-provided AI model to use when `gitlens.ai.experimental.model` is set to `vscode`
- Adds new Launchpad improvements:
  - Collapsed state of Launchpad groups are now saved between uses
  - The _Draft_ and _Pinned_ categories in the Launchpad now always sort their items by date
  - The Launchpad and Launchpad status bar indicator now indicate when there is an error loading data
  - The Launchpad indicator now shows the Launchpad icon next to the loading spinner when the Launchpad is loading

### Changed

- Changes the settings used to configure the AI models for GitLens' experimental AI features
  - Adds a `gitlens.ai.experimental.model` setting to specify the AI model to use
  - Removes the `gitlens.ai.experimental.provider`, `gitlens.ai.experimental.openai.model`, `gitlens.ai.experimental.anthropic.model`, and `gitlens.ai.experimental.gemini.model` settings in favor of the above

### Fixed

- Fixes [#3295](https://github.com/gitkraken/vscode-gitlens/issues/3295) - Incorrect pluralization in Authors lens &mdash; thanks to [PR #3296](https://github.com/gitkraken/vscode-gitlens/pull/3296) by bm-w ([@bm-w](https://github.com/bm-w))
- Fixes [#3277](https://github.com/gitkraken/vscode-gitlens/issues/3277) - Unable to pull branch when the local branch whose name differs from its tracking branch

<a id="v15-0"></a>

## Version 15.0

#### Tuesday, May 14th, 2024

With the release of GitLens 15 comes some of GitLens' most exciting features yet, Launchpad, Code Suggest, Jira integration and so much more. This release is packed with tools and enhancements to improve code review workflows and makes it easier than ever to keep your team unblocked.

<img src="/wp-content/uploads/gl-15-hero.png" class="img-responsive center img-bordered">

### Launchpad

GitLens 15 introduces a preview of the Launchpad, a new Pro feature that brings your GitHub pull requests into a unified, categorized list. The Launchpad categorizes pull requests by status, making it easy to see which pull requests are ready to merge, blocked, need your review, and more. Use the Launchpad to quickly action on the highest priority pull requests and keep your team unblocked.

Once you've selected a pull request in the Launchpad, you can choose from a list of actions to take on that pull request, including merging the pull request, opening the pull request on GitHub, switching to or creating a branch or worktree for the pull request, viewing the pull request's changes, and more.

Also included is a Launchpad status bar icon which provides a pulse on the most critical pull request needing your attention, and a summary of your most critical pull requests on hover.

You can open the new Launchpad directly from its status bar icon by clicking the icon or by using the new _GitLens: Open Launchpad_ command. Clicking a category in the Launchpad status bar icon tooltip will open the Launchpad directly to that category.

### Code Suggest

Code Suggest is a new cloud feature that frees your code reviews from the unnecessary restrictions of GitHub's comment-style code suggestions. Code suggestions can be created from any code and right from inside the convenience of your IDE.

You can create a Code Suggestion from the _Inspect: Overview_ tab when on a PR's branch. You can also start Code Suggestions on a pull request directly from the Launchpad. Simply choose which file changes to include, add a title and optional description, and you're ready to go.

Upon creation of a Code Suggestion, a comment will appear on the pull request. Code Suggestions can be viewed and applied directly from [gitkraken.dev](https://gitkraken.dev), or opened in GitKraken Desktop or GitLens.

You can see a PR's Code Suggestions from anywhere we currently display PR information in our views, including Commits, Branches, Remotes, and the new Pull Request view. From there you can view the changes, apply them, accept or reject the code suggestion, or copy a link to share with team members.

### Jira Integration

GitLens 15 introduces rich Jira Cloud integration, enabling automatic, rich Jira autolinks in commit messages wherever autolinks are supported in GitLens. You can connect to Jira by clicking the _Cloud Integrations_ button in the GitKraken Account view or by using the new _GitLens: Manage Cloud Integrations_ command. Once connected, rich autolinks will automatically populate for Jira issues in your commit messages.

Support for more cloud integrations and other Jira integration features are coming soon.

### Gemini and Latest OpenAI & Anthropic Model Support

This release also adds support for Google Gemini for GitLens' experimental AI features. You can specify the Gemini model to use with the new `gitlens.ai.experimental.gemini.model` setting.

We've also expanded our OpenAI and Anthropic model support to include the latest models.

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- may ([@m4rch3n1ng](https://github.com/m4rch3n1ng))

### Added

- Adds [Launchpad](https://gitkraken.com/solutions/launchpad?utm_source=gitlens-extension&utm_medium=in-app-links) `preview`, a new Pro feature bringing your GitHub pull requests into a unified, categorized list to keep you focused and your team unblocked
  - Open using the new _GitLens: Open Launchpad_ command
  - Categorizes pull requests by status
    - _Current Branch_: Pull requests associated with your current branch
    - _Ready to Merge_: Pull requests without conflicts, ci failures, change suggestions or other issues preventing merge
    - _Blocked_: Pull requests with conflicts, CI failures, or that have no reviewers assigned
    - _Needs Your Review_: Pull requests waiting for your review
    - _Requires Follow-Up_: Pull requests that have been reviewed and need follow-up
    - _Draft_: Draft pull requests
    - _Pinned_: Pull requests you have pinned
    - _Snoozed_: Pull requests you have snoozed
    - _Other_: Other pull requests
  - Action on a pull request directly from the Launchpad:
    - Merge a pull request
    - Open a pull request on GitHub
    - Switch to or create a branch or worktree for a pull request to review changes
    - Display a pull request's details in the _Overview_
    - Open a pull request's changes in the multi-diff editor
    - View a pull request's branch in the _Commit Graph_
    - View or create code suggestions for a pull request
    - Pin or snooze a pull request in the Launchpad
  - Adds a status bar indicator of the _Launchpad_
    - Opens the Launchpad when clicked
    - Shows the top pull request and its status in the status bar
      - Also highlights your top pull request in the launchpad when opened from the indicator
    - Provides a summary of your most critical pull requests on hover
      - Each summary line includes a link to open the Launchpad to that category
  - Adds new settings for the Launchpad and indicator
    - `gitlens.launchpad.ignoredRepositories`: Array of repositories with `owner/name` format to ignore in the Launchpad
    - `gitlens.launchpad.staleThreshold`: Value in days after which a pull request is considered stale and moved to the _Other_ category
    - `gitlens.launchpad.indicator.enabled`: Specifies whether to show the Launchpad indicator in the status bar
    - `gitlens.launchpad.indicator.icon`: Specifies the style of the Launchpad indicator icon
    - `gitlens.launchpad.indicator.label`: Specifies the style of the Launchpad indicator label
    - `gitlens.launchpad.indicator.groups`: Specifies which critical categories of pull requests to summarize in the indicator tooltip
    - `gitlens.launchpad.indicator.useColors`: Specifies whether to use colors in the indicator
    - `gitlens.launchpad.indicator.openInEditor`: Specifies whether to open the Launchpad in the editor when clicked
    - `gitlens.launchpad.indicator.polling.enabled`: Specifies whether to regularly check for changes to pull requests
    - `gitlens.launchpad.indicator.polling.interval`: Specifies the interval in minutes to check for changes to pull requests
- Adds new features that make code reviews easier
  - Adds [Code Suggest](https://gitkraken.com/solutions/code-suggest?utm_source=gitlens-extension&utm_medium=in-app-links) `preview`, a cloud feature, that frees your code reviews from unnecessary restrictions
    - Create a Code Suggestion from the _Inspect: Overview_ tab when on a PR's branch
    - Upon creation of a Code Suggestion, a comment will appear on the pull request
      - Code Suggestions can be viewed and apply directly from [gitkraken.dev](https://gitkraken.dev), or open in GitKraken Desktop or GitLens.
    - See a PR's Code Suggestions from anywhere we currently display PR information in our views (Commits, Branches, Remotes)
    - You can additionally start Code Suggestions from the Launchpad
  - Adds a _Pull Request_ view to view PR commits and review file changes
  - Adds a _Pull Request_ badge to the Graph and the Inspect Overview
- Adds rich Jira Cloud integration
  - Enables rich automatic Jira autolinks in commit messages everywhere autolinks are supported in GitLens
  - Adds a _Cloud Integrations_ button to the GitKraken Account view and a new `GitLens: Manage Cloud Integrations` command to manage connected cloud integrations
  - Adds a _Manage Jira_ button to _Inspect_ and a link in Autolink settings to connect to Jira
- Adds support for Google Gemini for GitLens' experimental AI features
  - Adds a `gitlens.ai.experimental.gemini.model` setting to specify the Gemini model
- Adds support for the latest OpenAI and Anthropic models for GitLens' experimental AI features
- Adds a new `gitlens.views.collapseWorktreesWhenPossible` setting to specify whether to try to collapse the opened worktrees into a single (common) repository in the views when possible

### Changed

- Reworks _Commit Details_, now called the _Inspect_ view
  - Revamps the _Working Changes_ tab into the _Overview_ tab
  - Provides richer branch status information and branch switching
  - Adds Push, Pull, and Fetch actions
  - Richer Pull Request Information
    - Open details in the Pull Request view
    - Links to open and compare changes
    - List of the PR's Code Suggestions
  - Create a Code Suggestion by clicking the _Suggest Changes for PR_ button
- Improves contributor and team member picking for the adding co-authors, _Code Suggest_, and _Cloud Patches_
- Improves performance when creating colors derived from the VS Code theme
- Changes the command to open the Launchpad in the editor (formerly _Focus View_) from _GitLens: Show Focus_ to _GitLens: Open Launchpad in Editor_
- Renames the setting `gitlens.focus.allowMultiple` to `gitlens.launchpad.allowMultiple`
- Updates most deep link prompts to quick picks or quick inputs, moves most prompts to before a repository is opened.
- Updates Pro upgrade links to use the newer gitkraken.dev site

### Fixed

- Fixes [#3221](https://github.com/gitkraken/vscode-gitlens/issues/3221) - Cannot use word "detached" in branch names
- Fixes [#3197](https://github.com/gitkraken/vscode-gitlens/issues/3197) - Only emojify standalone emojis &mdash; thanks to [PR #3208](https://github.com/gitkraken/vscode-gitlens/pull/3208) by may ([@m4rch3n1ng](https://github.com/m4rch3n1ng))
- Fixes [#3180](https://github.com/gitkraken/vscode-gitlens/issues/3180) - Focus View feedback button is not working
- Fixes [#3179](https://github.com/gitkraken/vscode-gitlens/issues/3179) - The checkmarks in cherry pick are not displayed
- Fixes [#3249](https://github.com/gitkraken/vscode-gitlens/issues/3249) - Error "Cannot read properties of null (reading 'map')
- Fixes [#3198](https://github.com/gitkraken/vscode-gitlens/issues/3198) - Repository location in cloud workspace doesn't work when the repo descriptor does not contain a url
- Fixes [#3143](https://github.com/gitkraken/vscode-gitlens/issues/3143) - File Annotation icon isn't themed according to the icons...

<a id="v14-9"></a>

## Version 14.9

#### Wednesday, March 6, 2024

The 14.9 release of GitLens brings improved reviewing of branch changes and new Anthropic Claude models along with general fixes and improvements.

<img src="/wp-content/uploads/gl-14-9-hero.png" class="img-responsive center img-bordered">

### Improved reviewing of Branch Changes

Two new commands were added to branches in the _Commit Graph_ and views. The `Compare with Common Base` enables reviewing changes as if the selected branch were to be merged by comparing the common ancestor (merge base) with the current branch to the selected branch. Use the new `Open All Changes with Common Base` command to review the changes as if the selected branch were to be merged in the multi-diff editor.

### Anthropic Claude Models

We've added support for Anthropic's Claude 3 Opus & Sonnet models for GitLens' experimental AI features. You can select these models from the `GitLens: Switch AI Model` command in the Command Palette. You can then use these models with the `GitLens: Generate Commit Message (Experimental)...` command in the Command Palette or in the `Explain (AI)` panel of _Commit Details_ and _Cloud Patch Details_ views.

### Added

- Adds support for Anthropic's Claude 3 Opus & Sonnet models for GitLens' experimental AI features
- Adds a _Compare with Common Base_ command to branches in the _Commit Graph_ and views to review the changes if the selected branch were to be merged by comparing the common ancestor (merge base) with the current branch to the selected branch
- Adds an _Open All Changes with Common Base_ command to branches in the _Commit Graph_ and views to review the changes if the selected branch were to be merged in the multi-diff editor
- Adds a _Stash All Changes_ command to Source Control repository toolbar (off by default)
- Adds the repository name as a prefix to worktree name when adding to the current workspace
- Adds a better message when stashing only untracked files without including untracked files

### Changed

- Re-adds _Add to Workspace_ option when creating a worktree &mdash; closes [#3160](https://github.com/gitkraken/vscode-gitlens/issues/3160)
- Changes _Commit Graph_ date style to default to the default date style &mdash; refs [#3153](https://github.com/gitkraken/vscode-gitlens/issues/3153)
- Renames the _Compare Ancestry with Working Tree_ command on branches to _Compare Common Base with Working Tree_ for better clarity
- Improves _File Blame_ annotations performance and layout accuracy with certain character sets
- Improves string formatting performance

### Fixed

- Fixes [#3146](https://github.com/gitkraken/vscode-gitlens/issues/3146) - Search & Compare fails to remember items after restart
- Fixes [#3152](https://github.com/gitkraken/vscode-gitlens/issues/3152) - Fixes double encoding of redirect URLs during account sign-in which affects certain environments
- Fixes [#3153](https://github.com/gitkraken/vscode-gitlens/issues/3153) - `gitlens.defaultDateStyle` not working in Commit Details view
- Fixes the _Open Pull Request Changes_ & _Compare Pull Request_ commands to scope the changes only to the pull request
- Fixes broken _Compare Common Base with Working Tree_ (previously _Compare Ancestry with Working Tree_)
- Fixes issue when switching to a worktree via branch switch when there are multiple repos in the workspace

<a id="v14-8"></a>

## Version 14.8

#### Thursday, February 8, 2024

The 14.8 release of GitLens features several enhancements to make it easier to use worktrees, view diffs and pull-requests, and includes enterprise improvements for Cloud Patches.

<img src="/wp-content/uploads/gl-14-8-hero.png" class="img-responsive center img-bordered">

### Worktree Workflow Improvements `PRO`

We've improved and streamlined the process of creating and opening worktrees. This includes new options for creating a worktree when switching branches as well as skipping prompts for remote creating and just auto-adding them. We've also added a command for copying your current working changes to an existing worktree.

### VS Code Multi-diff Support

VS Code's new multi-diff editor is out of experimental, so we've enabled it in our commands by default for VS Code 1.86 and above. The multi-diff editor allows you to view changes across multiple files in a single tab, instead of switching between tabs. This makes comparing a set of changes across files much easier.

### Cloud Patch Enterprise Storage ☁️

For Enterprise customers, there is now the option to host Cloud Patches on your own dedicated storage for maximum security. Your organization's admin can configure the self-managed storage at https://gitkraken.dev/settings/security. When creating a Cloud Patch, GitLens will confirm they are being stored on your secure organization storage.

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- yutotnh ([@yutotnh](https://github.com/yutotnh))

### Added

- Adds support for Cloud Patches hosted on your own dedicated storage for the highest level of security (requires an Enterprise plan)
- Improves worktree usage, discoverability, and accessibility
  - Simplifies the create worktree and open worktree flows &mdash; reduces number of steps and options presented
  - Adds _Create Branch in New Worktree_ confirmation option when creating branches, e.g. via the _GitLens: Git Create Branch..._ command
  - Adds _Create Worktree for Branch_, _Create Worktree for Local Branch_, and _Create Worktree for New Local Branch_ confirmation options when switching branches, e.g. via the _GitLens: Git Switch to..._ command
  - Adds a _Copy Working Changes to Worktree..._ command to the _Commit Graph_ and command palette to copy the current working changes to an existing worktree
  - Avoids prompt to add a (required) remote and instead auto-adds the remote during worktree creation from a pull request
- Adds ability to open multiple changes in VS Code's new multi-diff editor, previously experimental and now enabled by default
  - Adds an inline _Open All Changes_ command to commits, stashes, and comparisons in the views
  - Changes _Open All Changes_ & _Open All Changes with Working Tree_ commands to use the new multi-diff editor when enabled
  - Adds _Open All Changes, Individually_ & _Open All Changes with Working Tree, Individually_ commands to provide access to the previous behavior
  - Renames the `gitlens.experimental.openChangesInMultiDiffEditor` setting to `gitlens.views.openChangesInMultiDiffEditor`, which is enabled by default, to specify whether to open changes in the multi-diff editor (single tab) or in individual diff editors (multiple tabs)
  - Requires VS Code `1.86` or later, or VS Code `1.85` with `multiDiffEditor.experimental.enabled` enabled
- Adds new comparison features to pull requests in GitLens views
  - Adds an _Open Pull Request Changes_ context menu command on pull requests in the _Commit Graph_ and other GitLens views to view pull request changes in a multi-diff editor (single tab)
    - Requires VS Code `1.86` or later, or VS Code `1.85` with `multiDiffEditor.experimental.enabled` enabled
  - Adds a _Compare Pull Request_ context menu command on pull requests in the _Commit Graph_ and other GitLens views to open a comparison between the head and base of the pull request for easy reviewing
- Adds an _Open in Commit Graph_ context menu command on pull requests in GitLens view to open the tip commit in the _Commit Graph_
- Adds ability to copy changes, commits, stashes, and comparison as a patch to the clipboard
  - Adds a _Copy as Patch_ context menu command on files, commits, stashes, and comparisons in GitLens views
  - Adds a _Copy as Patch_ context menu command on files in the _Changes_ and _Staged Changes_ groups as well as the groups themselves in the _Source Control_ view
  - Adds a _Apply Copied Patch_ command in the command palette to apply a patch from the clipboard
- Adds an _Open All Changes_ inline button to branch status (upstream) and branch status files in GitLens views
- Adds an _Open Changes_ submenu to branch status (upstream) and branch status files in GitLens views
- Adds ability to preserve inline and file annotations while editing, previously experimental and now enabled by default
  - Renames the `gitlens.experimental.allowAnnotationsWhenDirty` setting to `gitlens.fileAnnotations.preserveWhileEditing`, which is enabled by default, to specify whether file annotations will be preserved while editing &mdash; closes [#1988](https://github.com/gitkraken/vscode-gitlens/issues/1988), [#3016](https://github.com/gitkraken/vscode-gitlens/issues/3016)
  - Use the existing `gitlens.advanced.blame.delayAfterEdit` setting to control how long to wait (defaults to 5s) before the annotation will update while the file is still dirty, which only applies if the file is under the `gitlens.advanced.sizeThresholdAfterEdit` setting threshold (defaults to 5000 lines)
- Adds an _Open File Annotation Settings_ command to the _File Annotations_ submenu in the editor toolbar to open the GitLens Settings editor to the file annotations sections
- Adds `gitlens.blame.fontFamily`, `gitlens.blame.fontSize`, `gitlens.blame.fontWeight` settings to specify the font (family, size, and weight respectively) of the _File Blame_ annotations &mdash; closes [#3134](https://github.com/gitkraken/vscode-gitlens/issues/3134)
- Adds _Copy Link to Code_, _Copy Link to File_, and _Copy Link to File at Revision..._ commands to the _Share_ submenu in the editor line number (gutter) context menu
- Adds an alternate flow (pick another file) when using the _Open File at Revision..._ and _Open Changes with Revision..._ commands to open a file that has been renamed and the rename is currently unstaged &mdash; closes [#3109](https://github.com/gitkraken/vscode-gitlens/issues/3109)
- Adds access to most _Git Command Palette_ commands directly to the command palette
- Adds _Rename Stash..._ options to stash quick pick menus
- Adds support for the latest GPT-4 Turbo models

### Changed

- Changes adds avatars to commits in quick pick menus
- Changes the pull request to be first item in the _Commits_ view, when applicable
- Changes the branch comparison to be below the branch status in the _Commits_ view to keep top focus on the status over the comparison
- Renames "Open Worktree for Pull Request via GitLens..." to "Checkout Pull Request in Worktree (GitLens)..."
- Renames the `gitlens.experimental.openChangesInMultiDiffEditor` setting to `gitlens.views.openChangesInMultiDiffEditor` as it is no longer experimental and enabled by default

### Fixed

- Fixes [#3115](https://github.com/gitkraken/vscode-gitlens/issues/3115) - Always-on file annotations
- Fixes ahead/behind diffs on files (root) in the _Commits_ view to correctly show the diff of the range rather than the base to the working tree
- Fixes missing repository icons in the _Repositories_ view
- Fixes [#3116](https://github.com/gitkraken/vscode-gitlens/issues/3116) - Fix typos in README.md and package.json &mdash; thanks to [PR #3117](https://github.com/gitkraken/vscode-gitlens/pull/3117) by yutotnh ([@yutotnh](https://github.com/yutotnh))

<a id="v14-7"></a>

## Version 14.7

#### Wednesday, January 16, 2024

With GitLens 14.7, we're kicking off 2024 with some bugfixes and some new features for Cloud Patches and Deep Links, and more.

<img src="/wp-content/uploads/gl-14-7-hero.png" class="img-responsive center img-bordered">

### Cloud Patch Collaboration ☁️

You can now add members of your GitKraken organization as collaborators on cloud patches you created or maintain as an admin. To invite a collaborator, click on one of your cloud patches in the _Cloud Patches_ view to open its patch details, and then click on the _Invite_ button. You can then select one or more members of your organization to add as collaborators on the patch. Once selected, you can choose a role for each collaborator, and click _Update Patch_ when done to finish adding collaborators.

Cloud patches you've been invited to as a collaborator appear under the _Shared with Me_ category in the _Cloud Patches_ view.

### Deep Links to Files and Code

You can now create (and use) deep links to files and code in GitLens. Create links to files using the new _Copy Link to File_ and _Copy Link to File at Revision..._ commands in the _Copy As_ submenu of the editor context menu and in the _Share_ submenu of files in GitLens views.

If you have code selected in an editor tab, you'll also have the option to link to the selected lines using the new _Copy Link to Code_ command in the _Copy As_ submenu of that tab's context menu.
Use or share these links to quickly and easily open the referenced file or code in an editor tab.

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- Ian Chamberlain ([@ian-h-chamberlain](https://github.com/ian-h-chamberlain))
- Brandon Cheng ([@gluxon](https://github.com/gluxon))

### Added

- Adds the ability to share Cloud Patches with specific members of your GitKraken organization
  - You can now share Cloud Patches exclusively with specific members of your organization by selecting _Collaborators Only_ when viewing or creating a Cloud Patch
  - Click the _Invite_ button at the bottom of the _Patch Details_ view to add members of your organization to collaborate and click _Update Patch_ to save your changes
  - Cloud Patch collaborators will see these Patches under the _Shared with Me_ section of the _Cloud Patches_ view
- Adds support for deep links to files and code
  - Deep link format: `https://gitkraken.dev/link/r/{repoId}/f/{filePath}?[url={remoteUrl}|path={repoPath}]&lines={lines}&ref={ref}`
  - Adds _Copy Link to File_, _Copy Link to File at Revision..._, and _Copy Link to Code_ commands to the _Copy As_ submenu in the editor context menu and to the _Share_ submenu of files in GitLens views
- Adds the ability to choose multiple stashes to drop in the _Git Command Palette_'s _stash drop_ command &mdash; closes [#3102](https://github.com/gitkraken/vscode-gitlens/issues/3102)
- Adds a new _prune_ subcommand to the _Git Command Palette_'s _branch_ command to easily delete local branches with missing upstreams
- Adds a new _Push Stash Snapshot_ confirmation option to the _Git Command Palette_'s _stash push_ command to save a stash without changing the working tree
- Adds _Copy_ to search results in the _Search & Compare_ view to copy the search query to more easily share or paste queries into the _Commit Graph_
- Adds a status bar indicator when blame annotations (inline, statusbar, file annotations, etc) are paused because the file has unsaved changes (dirty), with a tooltip explaining why and how to configure/change the behavior
- Adds an experimental `gitlens.experimental.allowAnnotationsWhenDirty` setting to specify whether file annotations are allowed on files with unsaved changes (dirty) &mdash; closes [#1988](https://github.com/gitkraken/vscode-gitlens/issues/1988), [#3016](https://github.com/gitkraken/vscode-gitlens/issues/3016)
  - Use the existing `gitlens.advanced.blame.delayAfterEdit` setting to control how long to wait (defaults to 5s) before the annotation will update while the file is still dirty, which only applies if the file is under the `gitlens.advanced.sizeThresholdAfterEdit` setting threshold (defaults to 5000 lines)
- Adds a `gitlens.fileAnnotations.dismissOnEscape` setting to specify whether pressing the `ESC` key dismisses the active file annotations &mdash; closes [#3016](https://github.com/gitkraken/vscode-gitlens/issues/3016)

### Changed

- Changes the commit search by file to allow some fuzziness by default &mdash; closes [#3086](https://github.com/gitkraken/vscode-gitlens/issues/3086)
  - For example, if you enter `file:readme.txt`, we will treat it as `file:**/readme.txt`, or if you enter `file:readme` it will be treated as `file:*readme*`
- Improves the _Switch_ command to no longer fail when trying to switch to a branch that is linked to another worktree and instead offers to open the worktree
- Changes branch/tag "tips" that are show on commits in many GitLens views to be truncated to 11 characters by default to avoid stealing to much real estate

### Fixed

- Fixes [#3087](https://github.com/gitkraken/vscode-gitlens/issues/3087) - Terminal executed commands fail if the GitLens terminal is closed
- Fixes [#2784](https://github.com/gitkraken/vscode-gitlens/issues/2784) - Git stash push error
- Fixes [#2926](https://github.com/gitkraken/vscode-gitlens/issues/2926) in more cases - "Open File at Revision" has incorrect editor label if revision contains path separator &mdash; thanks to [PR #3060](https://github.com/gitkraken/vscode-gitlens/issues/3060) by Ian Chamberlain ([@ian-h-chamberlain](https://github.com/ian-h-chamberlain))
- Fixes [#3066](https://github.com/gitkraken/vscode-gitlens/issues/3066) - Editing a large file and switching away to another file without saving causes current line blame to disappear; thanks to [PR #3067](https://github.com/gitkraken/vscode-gitlens/pulls/3067) by Brandon Cheng ([@gluxon](https://github.com/gluxon))
- Fixes [#3063](https://github.com/gitkraken/vscode-gitlens/issues/3063) - Missing icons in GitLens Settings UI
- Fixes issue with _Switch_ command not honoring the confirmation setting
- Fixes worktree delete from offering to delete main worktree (which isn't possible)
- Fixes worktree delete on windows when the worktree's folder is missing

### Removed

- Removes the `gitlens.experimental.nativeGit` setting as it is now the default experience &mdash; closes [#3055](https://github.com/gitkraken/vscode-gitlens/issues/3055)

<a id="v14-6"></a>

## Version 14.6

#### Wednesday, December 13, 2023

GitLens 14.6 marks our last release of 2023 and with it some great enhancements to Cloud Patches, Focus View and much more!

<img src="/wp-content/uploads/gl-14-6-hero.png" class="img-responsive center img-bordered">

### Cloud Patch Sharing Options ☁️

Users can now specify who can access shared Cloud Patches, choosing between anyone with a link or only members of your GitKraken organization with the link.

Coming soon is the ability to explicitly select individuals from your organization as collaborators. Cloud Patches explicitly shared to you, i.e. you are a collaborator, will appear in the Cloud Patches view under "Shared with Me".

> Note: If you have multiple organizations, you can easily switch between them from the GitKraken Account view.

### Focus View Timed Snoozing

The focus view now supports timed snoozing of items. Select a duration like 1 hour or 4 hours when snoozing a focus item and then that item will automatically move back when the time expires.

### Experimental Multi-diff Editor

You can now open changes in VS Code's new multi-diff editor. This requires VS Code 1.85 or later with the `multiDiffEditor.experimental.enabled` and `gitlens.experimental.openChangesInMultiDiffEditor` settings enabled.

#### Commands using Multi-diff

- `Open Folder Changes with Revision...` and `Open Folder Changes with Branch or Tag...` commands using the Command Palette as well as the Explorer and Source Control views
- An inline `Open All Changes` command for commits, stashes, and comparisons in the views
- `Open All Changes` and `Open All Changes with Working Tree` will use the new multi-diff editor when enabled

> Note: `Open All Changes, Individually` and `Open All Changes with Working Tree, Individually` commands were added to provide access to the previous behavior.

### Thank you to our contributors

Shout-out to our awesome contributor for this release!

- Victor Hallberg ([@mogelbrod](https://github.com/mogelbrod))

### Added

- Adds the ability to specify who can access a Cloud Patch when creating it
  - _Anyone with the link_ &mdash; allows anyone with the link and a GitKraken account to access the Cloud Patch
  - _Members of my Org with the link_ &mdash; allows only members of your selected GitKraken organization with the link to access the Cloud Patch
  - (Coming soon to GitLens) Ability to explicitly share to specific members from your organization and add them as collaborators on a Cloud Patch
  - Cloud Patches that have been explicitly shared with you, i.e. you are a collaborator, now will appear in the _Cloud Patches_ view under _Shared with Me_
- Adds timed snoozing for items in the _Focus View_ &mdash; choose from a selection of times when snoozing and the item will automatically move out of the snoozed tab when that time expires
- Adds the ability to open folder changes &mdash; closes [#3020](https://github.com/gitkraken/vscode-gitlens/issues/3020)
  - Adds _Open Folder Changes with Revision..._ & _Open Folder Changes with Branch or Tag..._ commands to the Command Palette and to the _Explorer_ and _Source Control_ views
  - Requires VS Code `1.85` or later and `multiDiffEditor.experimental.enabled` to be enabled
- Adds last modified time of the file when showing blame annotations for uncommitted changes
- Adds search results to the minimap tooltips on the _Commit Graph_
- Adds support for Anthropic's Claude 2.1 model for GitLens' experimental AI features
- Adds a status indicator when the upstream branch is missing in _Commits_ view
- Adds support for opening renamed/deleted files using the _Open File at Revision..._ & _Open File at Revision from..._ commands by showing a quick pick menu if the requested file doesn't exist in the selected revision &mdash; closes [#708](https://github.com/gitkraken/vscode-gitlens/issues/708) thanks to [PR #2825](https://github.com/gitkraken/vscode-gitlens/pull/2825) by Victor Hallberg ([@mogelbrod](https://github.com/mogelbrod))
- Adds an _Open Changes_ submenu to comparisons in the _Search & Compare_ view
- Adds experimental `gitlens.experimental.openChangesInMultiDiffEditor` setting to specify whether to open multiple changes in VS Code's experimental multi-diff editor (single tab) or in individual diff editors (multiple tabs)
  - Adds an inline _Open All Changes_ command to commits, stashes, and comparisons in the views
  - Changes _Open All Changes_ & _Open All Changes with Working Tree_ commands to use the new multi-diff editor when enabled
  - Adds _Open All Changes, Individually_ & _Open All Changes with Working Tree, Individually_ commands to provide access to the previous behavior
  - Requires VS Code `1.85` or later and `multiDiffEditor.experimental.enabled` to be enabled
- Adds a confirmation prompt when attempting to undo a commit with uncommitted changes
- Adds a _[Show|Hide] Merge Commits_ toggle to the _Contributors_ view
- Adds _Open in Integrated Terminal_ command to repositories in the views &mdash; closes [#3053](https://github.com/gitkraken/vscode-gitlens/issues/3053)
- Adds _Open in Terminal_ & _Open in Integrated Terminal_ commands to the upstream status in the _Commits_ view
- Adds the ability to choose an active GitKraken organization in the _Account View_ for users with multiple GitKraken organizations.

### Changed

- Improves AI model choice selection for GitLens' experimental AI features
- Improves performance when logging is enabled
- Changes the contextual view title from GL to GitLens

### Fixed

- Fixes [#2663](https://github.com/gitkraken/vscode-gitlens/issues/2663) - Debounce bug: file blame isn't cleared when editing document while text in output window changes
- Fixes [#3050](https://github.com/gitkraken/vscode-gitlens/issues/3050) - Opening revision of a renamed file is broken
- Fixes [#3019](https://github.com/gitkraken/vscode-gitlens/issues/3019) - Commits Views not working
- Fixes [#3026](https://github.com/gitkraken/vscode-gitlens/issues/3026) - Gitlens stopped working in sub-repositories
- Fixes [#2746](https://github.com/gitkraken/vscode-gitlens/issues/2746) - Remove 'undo commit' command from gitlens inspect
- Fixes [#2482](https://github.com/gitkraken/vscode-gitlens/issues/2482) - Unresponsive "commits" view and "branches" view update due to git log
- Fixes duplicate entries in the _Search & Compare_ view when adding a new comparison from outside the view and before the view has loaded
- Fixes _Load more_ in the _File History_ view when the file has been renamed
- Fixes broken _Open Changed & Close Unchanged Files_ (`gitlens.views.openOnlyChangedFiles`) command in the views
- Fixes issues with _Contributors_ view updating when changing toggles
- Fixes issues with _Open [Previous] Changes with Working File_ command in comparisons
- Fixes banner styling on the _Commit Graph_

<a id="v14-5"></a>

## Version 14.5

#### Monday, November 13, 2023

GitLens 14.5 features the all new Cloud Patches preview ☁️, which allows you to easily share changes with other developers by creating a Cloud Patch from your WIP, commit or stash and sharing the generated link with your teammates. Other notable enhancements include opening multiple tabs of Commit Graph & Focus.

<img src="/wp-content/uploads/gl-14-5-hero.png" class="img-responsive center img-bordered">

### Cloud Patches preview ☁️

[Cloud Patches](https://www.gitkraken.com/solutions/cloud-patches) aim to shift developer collaboration earlier in the process for faster feedback, cleaner pull requests, and overcoming tricky code challenges as a team. Create Cloud Patches from working changes, commits, stashes, or comparisons &mdash; then share the patch URL with others to get feedback and iterate on the changes together. It is currently available across GitLens, GitKraken Desktop, and GitKraken CLI, with plans to add commenting and more capabilities soon.

### Open Multiple Commit Graph & Focus Tabs

Open multiple instances of the Commit Graph, Focus, and Visual File History views, side-by-side, to look at multiple repositories at once or just different visualizations of the same repository.

### Thank you to our contributors

Shout-out to all of our awesome contributors for this release!

- Aidos Kanapyanov ([@aidoskanapyanov](https://github.com/aidoskanapyanov))
- Shashank Shastri ([@Shashank-Shastri](https://github.com/Shashank-Shastri))

### Added

- Adds a preview of [Cloud Patches](https://www.gitkraken.com/solutions/cloud-patches), an all-new ☁️ feature &mdash; engage in early collaboration before the pull request:
  - Share your work with others by creating a Cloud Patch from Working Changes, Commits, Stashes or Comparisons
  - View Cloud Patches from URLs shared to you and apply them to your working tree or to a new or existing branch
  - Manage your Cloud Patches from the new _Cloud Patches_ view in the GitLens side bar
  - Adds a _Share as Cloud Patch..._ command to the command palette and to the _Share_ submenu in applicable GitLens views
  - Adds a `gitlens.cloudPatches.enabled` setting to specificy whether to enable Cloud Patches (defaults to `true`)
- Adds support to open multiple instances of the _Commit Graph_, _Focus_, and _Visual File History_ in the editor area
  - Adds a _Split Commit Graph_ command to the _Commit Graph_ tab context menu
  - Adds a `gitlens.graph.allowMultiple` setting to specify whether to allow opening multiple instances of the _Commit Graph_ in the editor area
  - Adds a _Split Focus_ command to the _Focus_ tab context menu
  - Adds a `gitlens.focus.allowMultiple` setting to specify whether to allow opening multiple instances of the _Focus_ in the editor area
  - Adds a _Split Visual File History_ command to the _Visual File History_ tab context menu
  - Adds a `gitlens.visualHistory.allowMultiple` setting to specify whether to allow opening multiple instances of the _Visual File History_ in the editor area
- Adds a _Generate Commit Message (Experimental)_ button to the SCM input when supported (currently `1.84.0-insider` only)
  - Adds a `gitlens.ai.experimental.generateCommitMessage.enabled` setting to specify whether to enable GitLens' experimental, AI-powered, on-demand commit message generation &mdash; closes [#2652](https://github.com/gitkraken/vscode-gitlens/issues/2652)
- Improves the experience of the _Search Commits_ quick pick menu
  - Adds a stateful authors picker to make it much easier to search for commits by specific authors
  - Adds a file and folder picker to make it much easier to search for commits containing specific files or in specific folders
- Adds ability to sort repositories in the views and quick pick menus &mdash; closes [#2836](https://github.com/gitkraken/vscode-gitlens/issues/2836) thanks to [PR #2991](https://github.com/gitkraken/vscode-gitlens/pull/2991)
  - Adds a `gitlens.sortRepositoriesBy` setting to specify how repositories are sorted in quick pick menus and views by Aidos Kanapyanov ([@aidoskanapyanov](https://github.com/aidoskanapyanov))
- Adds a _[Show|Hide] Merge Commits_ toggle to the Commits\_ view &mdash; closes [#1399](https://github.com/gitkraken/vscode-gitlens/issues/1399) thanks to [PR #1540](https://github.com/gitkraken/vscode-gitlens/pull/1540) by Shashank Shastri ([@Shashank-Shastri](https://github.com/Shashank-Shastri))
- Adds a _Filter Commits by Author..._ commands to the _Commits_ view and comparisons context menus to filter commits in the _Commits_ view by specific authors
- Adds ability to publish to a remote branch to a specific commit using the _Push to Commit_ command
- Adds an _Open Comparison on Remote_ command to comparisons in views
- Adds a _Share > Copy Link to Repository_ command on branches in the views
- Adds _Share > Copy Link to Branch_ and _Share > Copy Link to Repository_ commands on the current branch status in the _Commits_ view
- Adds a _Clear Reviewed Files_ command to comparisons to clear all reviewed files &mdash; closes [#2987](https://github.com/gitkraken/vscode-gitlens/issues/2987)
- Adds a _Collapse_ command to many view nodes
- Adds a `gitlens.liveshare.enabled` setting to specify whether to enable integration with Visual Studio Live Share

### Changed

- Improves accuracy, performance, and memory usage related to parsing diffs, used in _Changes_ hovers, _Changes_ file annotations, etc
- Improves confirmation messaging in the _Git Command Palette_
- Refines merge/rebase messaging when there is nothing to do &mdash; refs [#1660](https://github.com/gitkraken/vscode-gitlens/issues/1660)
- Improves view messaging while loading/discovering repositories
- Honors VS Code's `git.useForcePushWithLease` and `git.useForcePushIfIncludes` settings when force pushing
- Changes _File Heatmap_ annotations to not color the entire line by default. Want it back, add `line` to the `gitlens.heatmap.locations` setting

### Fixed

- Fixes [#2997](https://github.com/gitkraken/vscode-gitlens/issues/2997) - "push to commit" pushes everything instead of up to the selected commit
- Fixes [#2615](https://github.com/gitkraken/vscode-gitlens/issues/2615) - Source Control views disappear after opening a file beyond a symbolic link
- Fixes [#2443](https://github.com/gitkraken/vscode-gitlens/issues/2443) - UNC-PATH: File History changes not displaying any changes when open
- Fixes [#2625](https://github.com/gitkraken/vscode-gitlens/issues/2625) - full issue ref has escape characters that break hover links
- Fixes [#2987](https://github.com/gitkraken/vscode-gitlens/issues/2987) - Unable to remove all marks on reviewed files with a single operation
- Fixes [#2923](https://github.com/gitkraken/vscode-gitlens/issues/2923) - TypeError: Only absolute URLs are supported
- Fixes [#2926](https://github.com/gitkraken/vscode-gitlens/issues/2926) - "Open File at Revision" has incorrect editor label if revision contains path separator
- Fixes [#2971](https://github.com/gitkraken/vscode-gitlens/issues/2971) - \[Regression\] The branch column header text disappears when you have a hidden ref
- Fixes [#2814](https://github.com/gitkraken/vscode-gitlens/issues/2814) - GitLens Inspect: "Files Changed" not following when switching between commits in File History
- Fixes [#2952](https://github.com/gitkraken/vscode-gitlens/issues/2952) - Inline blame not working because of missing ignoreRevsFile
- Fixes issue where _Changes_ hovers and _Changes_ file annotations sometimes weren't accurate
- Fixes intermittent issue where inline blame and other revision-based editor features are unavailable when repository discovery takes a bit
- Fixes intermittent issues where details sometimes get cleared/overwritten when opening the _Commit Details_ view
- Fixes issue when clicking on commits in the Visual File History to open the _Commit Details_ view
- Fixes issue opening stashes in the _Commit Details_ view from the _Stashes_ view
- Fixes issue where GitHub/GitLab enriched autolinks could incorrectly point to the wrong repository
- Fixes issue showing folder history in the _File History_ view when there are uncommitted changes (staged or unstaged)
- Fixes issue when pushing to a remote branch with different name than the local
- Fixes tooltip styling/theming on the _Commit Graph_
- Fixes issues staged files in repositories not "opened" (discovered) by the built-in Git extension

<a id="v14-4"></a>

## Version 14.4

#### Friday, October 13, 2023

GitLens 14.4 is here, featuring new enhancements to _Focus View_, the addition of _Working Changes_ to _Commit Details_ and _Graph Details_, and some performance improvements to _Inline_ and _Status Bar Blame_.

<img src="/wp-content/uploads/gl-14-4-hero.png" class="img-responsive center img-bordered">

### Focus View Enhancements

_Focus View_ now includes the ability to pin and snooze items. These options appear as clickable icons in the new snooze/pin column in the view. Pinned issues and pull requests will always show at the top of the list, while snoozed items will be hidden and moved to the new Snoozed section. To unsnooze an item, simply click on the Snoozed section header and select the unsnooze icon for that item in the pin/snooze column.

<img src="/wp-content/uploads/gl-14-4-focus-view-update.png" class="img-responsive center img-bordered">

### Working Changes Tab

_Commit Details_ and _Graph Details_ now include a separate _Working Changes_ tab. This allows you to view your work-in-progress changes any time without losing context on your current selected change. The tab includes the ability to stage and unstage changes, open files to view changes, and open the changes in the _Commit Graph_ and SCM view.

<img src="/wp-content/uploads/gl-14-4-commit-details-wip.png" class="img-responsive center img-bordered">

### Inline and Status Bar Blame Performance Improvements

Inline blame and status bar blame now appear faster on hover. This performance improvement is especially notable when using connected remote integrations.

### Added

- Adds a _Working Changes_ tab to the _Commit Details_ and _Graph Details_ views to show your working tree changes
  - Adds _Stage Changes_ and _Unstage Changes_ commands to files on the _Working Changes_ tab
- Adds a _[Show|Hide] Merge Commits_ toggle to the _File History_ view &mdash; closes [#2104](https://github.com/gitkraken/vscode-gitlens/issues/2104) & [#2944](https://github.com/gitkraken/vscode-gitlens/issues/2944)
  - Adds a `gitlens.advanced.fileHistoryShowMergeCommits` setting to specify whether merge commits will be show in file histories
- Adds deep link support for workspaces in the _GitKraken Workspaces_ view
  - Deep link format: `https://gitkraken.dev/link/workspaces/{workspaceId}`
  - Adds a _Share_ submenu with a _Copy Link to Workspace_ command to workspaces in the _GitKraken Workspaces_ view

### Changed

- Improves performance of inline blame, status bar blame, and hovers especially when working with remotes with connected integrations
- Changes the _File History_ view to follow renames and filters out merge commits by default &mdash; closes [#2104](https://github.com/gitkraken/vscode-gitlens/issues/2104) & [#2944](https://github.com/gitkraken/vscode-gitlens/issues/2944)
- Changes the _File History_ view to allow following renames while showing history across all branches (which was a previous limitation of Git) &mdash; closes [#2828](https://github.com/gitkraken/vscode-gitlens/issues/2828)
- Changes to use our own implementation of `fetch`, `push`, and `pull` Git operations, rather than delegating to VS Code to avoid limitations especially with GitKraken Workspaces. Please report any issues and you can revert this (for now) by setting `"gitlens.experimental.nativeGit"` to `"false"` in your settings
- Relaxes PR autolink detection for Azure DevOps to use `PR <number>` instead of `Merged PR <number>` &mdash; closes [#2908](https://github.com/gitkraken/vscode-gitlens/issues/2908)
- Changes wording on `Reset Stored OpenAI Key` command to `Reset Stored AI Key` to reflect support for other providers

### Fixed

- Fixes [#2941](https://github.com/gitkraken/vscode-gitlens/issues/2941) - Invalid Request when trying to generate a commit message using Anthropic API
- Fixes [#2940](https://github.com/gitkraken/vscode-gitlens/issues/2940) - Can't use Azure OpenAI model because i can't save the openai key because of the verification
- Fixes [#2928](https://github.com/gitkraken/vscode-gitlens/issues/2928) - Apply Changes should create new files when needed
- Fixes [#2896](https://github.com/gitkraken/vscode-gitlens/issues/2896) - Repositories view stuck in loading state
- Fixes [#2460](https://github.com/gitkraken/vscode-gitlens/issues/2460) - Gitlens Remote provider doesn't work properly in "Commit graph" view
- Fixes issue with "View as [List|Tree]" toggle not working in the _Commit Details_ view
- Fixes an issue with deep links sometimes failing to properly resolve when a matching repository without the remote is found
- Fixes an issue in the _Commit Graph_ where commits not in the history of a merge commit were showing in the same column
- Fixes `Reset Stored AI Key` command to work for the current provider
- Fixes an issue with parsing some renames in log output

<a id="v14-3"></a>

## Version 14.3

#### Thursday, September 7, 2023

This release focuses on quality of life improvements to the _Commit Graph_, _Search & Compare_, and File History as well bug fixes around the deep links and viewing diffs.

<img src="/wp-content/uploads/gl-14-3-hero.png" class="img-responsive center img-bordered">

### Commit Graph Improvements

<img src="/wp-content/uploads/gl-14-3-multiple-open-graphs.png" class="img-responsive center img-bordered">

You can now have a Commit Graph in the bottom Panel and one in the Editor Area open at the same time. This enables viewing more than repo at a time or different areas of the same repo at the same time.

<img src="/wp-content/uploads/gl-14-3-commit-graph-prefers.png" class="img-responsive center img-bordered">

Additionally, you can also set a preference for which mode to use by default, which you can set from the gear icon on the Commit Graph or by adding `gitlens.graph.layout` in settings. _GitLens: Show Commit Graph_ from the command palette will honor that preference.

### Search & Compare Review Checkboxes

<img src="/wp-content/uploads/gl-14-3-search-compare-checkboxes.png" class="img-responsive center img-bordered">

From the _Search & Compare_, you now have checkboxes next to each files to help keep track of files you've reviewed. This was an long sought after request by the community, you asked and we delivered!

### Thank you to our contributors

Shout-out to our awesome contributor for this release!

- Omar Ghazi ([@omarfesal](https://github.com/omarfesal))

### Added

- Adds checkboxes to files in the _Search & Compare_ view to allow for tracking review progress &mdash; closes [#836](https://github.com/gitkraken/vscode-gitlens/issues/836)
- Allows the _Commit Graph_ to be open in the panel and in the editor area simultaneously
- Adds an _Open Changes_ button to commits in the file history quick pick menu &mdash; closes [#2641](https://github.com/gitkraken/vscode-gitlens/issues/2641) thanks to [PR #2800](https://github.com/gitkraken/vscode-gitlens/pull/2800) by Omar Ghazi ([@omarfesal](https://github.com/omarfesal))

### Changed

- Changes the `gitlens.graph.layout` setting to be a default preference rather than a mode change

### Fixed

- Fixes [#2885](https://github.com/gitkraken/vscode-gitlens/issues/2885) - Folder History not show changed files of commit
- Fixes issues with opening changes (diffs) of renamed files
- Fixes issues with deep links including when opening VS Code from the deep link

<a id="v14-2"></a>

## Version 14.2

#### Friday, August 4, 2023

GitLens 14.2 arrives with a few hotly-requested improvements to the Focus View for even greater productivity in your daily workflow.

<img src="/wp-content/uploads/gl-14-2-hero.png" class="img-responsive center img-bordered">

## Focus View

The Focus View has been improved with a new unified experience and includes a few new features to help you navigate pull requests and issues.

<img src="/wp-content/uploads/gl-focus-changes-14-2.png" class="img-responsive center img-bordered">

Pull Requests and Issues have now been combined into a single view with tabs to quickly toggle between showing all items, pull requests, or issues only.

You can also click on a branch name to show the branch on the Commit Graph, and if you don't already have a remote configured for that branch you'll be guided to add it.

<img src="/wp-content/uploads/gl-focus-search-14-2.png" class="img-responsive center img-bordered">

Furthermore, we've added a search bar to the Focus View to help you quickly find pull requests or issues by their title.

### Thank you to our contributors

Shout-out to all of our awesome contributors for this release!

- Victor Hallberg ([@mogelbrod](https://github.com/mogelbrod))

### Added

- Improves the _Focus_ view experience
  - Unifies pull requests and issues into a single view
  - Adds tabs to switch between showing Pull Requests, Issues, or All
  - Adds a filter/search box to quickly find pull request or issues by title
  - Adds ability to click on a branch name to show the branch on the _Commit Graph_
- Adds a new command _Open Changed & Close Unchanged Files..._ to the command palette, the context menu of the _Commit Graph_ work-in-progress (WIP) row, and the SCM group context menu to open all changed files and close all unchanged files.
- Adds a new command _Reset Current Branch to Tip..._ to branch context menus in the _Commit Graph_ and in GitLens views to reset the current branch to the commit at the chosen branch's tip.

### Changed

- Changes _Compact Graph Column Layout_ context menu command to _Use Compact Graph Column_ for better clarity
- Changes _Default Graph Column Layout_ context menu command to _Use Expanded Graph Column_ for better clarity
- Improves remote parsing for better integration support for some edge cases

### Fixed

- Fixes [#2823](https://github.com/gitkraken/vscode-gitlens/issues/2823) - Handle stdout/stderr Buffers in shell run() &mdash; thanks to [PR #2824](https://github.com/gitkraken/vscode-gitlens/pull/2824) by Victor Hallberg ([@mogelbrod](https://github.com/mogelbrod))
- Fixes issues with missing worktrees breaking the Worktrees view and Worktree quick pick menus

<a id="v14-1"></a>

## Version 14.1

### Thursday, July 13, 2023

We're delighted to introduce GitLens 14.1. We've enhanced integration between GitKraken Cloud and VS Code workspaces. You can now link a GitKraken Cloud workspace and VS Code workspace and GitLens can automatically update your VS Code workspace when new repositories are added to its linked counterpart.
Additionally, we've added deep link support for comparisons in the _Search & Compare_ view, coupled with a new _Copy Link to Comparison_ command in a new _Share_ submenu, streamlining review and collaboration.

We've also added support for Anthropic's new Claude 2 model for use with our experimental AI features. You can switch to it using the _Switch AI Model_ command from the Command Palette.

<img src="/wp-content/uploads/gl-14-1-hero.png" class="img-responsive center img-bordered">

## Workspace Linking

When you create a VS Code workspace from a GitKraken Cloud workspace, the two are now linked. You can open a linked VS Code workspace from its cloud workspace using the new _Open VS Code Workspace in New Window_ option (hold <kbd>alt</kbd> to open in the current window).

<img src="/wp-content/uploads/gl-linked-workspaces-14-1.png" class="img-responsive center img-bordered">

When repositories are added to a GitKraken Cloud workspace, you can automatically add those repositories to its linked VS Code workspace when that workspace is opened. You can choose to automatically add new repositories, be prompted to add them, or disable auto-adding repositories altogether for that workspace. You'll be prompted to choose your desired behavior when creating the VS Code workspace, but it can also be changed at any time via the _Change Linked Workspace Auto-Add Behavior..._ context menu command on the _Current Window_ item or its linked workspace in the _GitKraken Workspaces_ view.

<img src="/wp-content/uploads/gl-linked-auto-add-settings-14-1.png" class="img-responsive center img-bordered">

You can also manually add repositories to the VS Code workspace at any time using the new _Add Repositories from Linked Workspace..._ context menu command.

<img src="/wp-content/uploads/gl-linked-add-repositories-14-1.png" class="img-responsive center img-bordered">

## Comparison Deep Links

You can now deep link directly into comparisons in the _Search & Compare_ view. This includes comparisons between branches, tags, and commits. You can also copy a deep link to a comparison to your clipboard using the new _Copy Link to Comparison_ context menu command on the _Share_ submenu.

<img src="/wp-content/uploads/gl-deep-link-comparison-14-1.png" class="img-responsive center img-bordered">

### Thank you to our contributors

Shout-out to all of our awesome contributors for this release!

- Neil Ghosh ([@neilghosh](https://github.com/neilghosh))
- Leo Dan Peña ([@leo9-py](https://github.com/leo9-py))

### Added

- Adds the ability to link a GitKraken Cloud workspace with an associated VS Code workspace
  - Adds ability to automatically add repositories to the current VS Code workspace that were added to its associated GitKraken Cloud workspace, if desired
    - Adds a _Change Linked Workspace Auto-Add Behavior..._ context menu command on the _Current Window_ and linked workspace to control the desired behavior
    - Adds an _Add Repositories from Linked Workspace..._ context menu command on the _Current Window_ item to trigger this manually
  - Adds a new _Open VS Code Workspace_ command to open an existing VS Code workspace associated with a GitKraken Cloud workspace
  - Adds a highlight (green) to the linked GitKraken Cloud workspace when the current VS Code workspace is associated with it in the _GitKraken Workspaces_ view
- Adds deep link support for comparisons in the _Search & Compare_ view
  - Deep link format: `vscode://eamodio.gitlens/r/{repoId}/compare/{ref1}[..|...]{ref2}?[url={remoteUrl}|path={repoPath}]`
  - Adds a _Share_ submenu with a _Copy Link to Comparison_ command to comparisions in the _Search & Compare_ view
- Adds support for Anthropic's Claude 2 AI model
- Adds a progress notification while repositories are being added to a GitKraken Cloud workspace

### Changed

- Improves scrolling performance on the _Commit Graph_
- Renames _Convert to VS Code Workspace_ to _Create VS Code Workspace_ for workspaces in the _GitKraken Workspaces_ view to better reflect the behavior of the action
- Hides _Create VS Code Workspace_ and _Locate All Repositories_ commands on empty workspaces in the _GitKraken Workspaces_ view

### Fixed

- Fixes [#2798](https://github.com/gitkraken/vscode-gitlens/issues/2798) - Improve response from OpenAI if key used is tied to a free account
- Fixes [#2785](https://github.com/gitkraken/vscode-gitlens/issues/2785) - Remote Provider Integration URL is broken &mdash; thanks to [PR #2786](https://github.com/gitkraken/vscode-gitlens/pull/2786) by Neil Ghosh ([@neilghosh](https://github.com/neilghosh))
- Fixes [#2791](https://github.com/gitkraken/vscode-gitlens/issues/2791) - Unable to use contributors link in README.md &mdash; thanks to [PR #2792](https://github.com/gitkraken/vscode-gitlens/pull/2792) by Leo Dan Peña ([@leo9-py](https://github.com/leo9-py))
- Fixes [#2793](https://github.com/gitkraken/vscode-gitlens/issues/2793) - Requesting username change in contributors README page &mdash; thanks to [PR #2794](https://github.com/gitkraken/vscode-gitlens/pull/2794) by Leo Dan Peña ([@leo9-py](https://github.com/leo9-py))
- Fixes some rendering issues when scrolling in the _Commit Graph_
- Fixes an issue with some shared workspaces not showing up in the _GitKraken Workspaces_ view when they should
- Fixes an issue when adding repositories to a workspace in the _GitKraken Workspaces_ view where the added repository would show as missing until refreshing the view

<a id="v14-0"></a>

## Version 14.0 &mdash; GitLens Reimagined

### Wednesday, June 14, 2023

We're thrilled to announce the release of GitLens 14 with a reimagined GitLens experience! We restructured our views layout to better enhance productivity and focus by grouping views contextually, giving you easy access to the right information when you need it. The commit graph has been moved to the (bottom) panel, providing convenient and persistent access to the graph and its details. We've also rethought and rebuilt our Welcome and Walkthrough as well as the Home view to provide a friendlier onboarding experience.

The power of GitKraken Workspaces now in GitLens. Workspaces are an easy way to work with and manage multiple repositories and include the ability to convert to and from a VS Code workspace, with further improvements coming soon. Create workspaces just for yourself or share (coming soon to GitLens) them with your team for faster onboarding and better collaboration.

<img src="/wp-content/uploads/gl-14-0-hero.png" class="img-responsive center img-bordered">

## New Views layout

We've grouped views contextually and introduced GitLens Inspect, giving you easy access to the right information when you need it. We've moved some of our views from their previous home, in Source Control, into either the GitLens or the new GitLens Inspect side bar.

<img src="/wp-content/uploads/gl-views-and-features.png" class="img-responsive center img-bordered">

### GitLens Inspect side bar

The all-new GitLens Inspect is like an x-ray or developer tools inspector into your code, which focuses on providing contextual information and insights to what you're actively working on.

<img src="/wp-content/uploads/gl-inspect-side-bar.png" class="img-responsive center img-bordered">

Views include:

- Commit Details
- Line History
- File History
- Visual File History
- Search & Compare

_Pro tip: you can drag the entire GitLens Inspect Side Bar onto your secondary Side Bar, without needing to arrange views on-by-one._

### GitLens side bar

We've re-focused this to be the home of GitKraken services (e.g. GitKraken Workspaces) as well as discovery, help, and support.

<img src="/wp-content/uploads/gl-side-bar-v14.png" class="img-responsive center img-bordered">

Views include:

- Home view
- GitKraken Workspaces
- GitKraken Account

### Source Control side bar

We've slimmed down this side bar to only contain views that are focused on your repositories.

<img src="/wp-content/uploads/gl-side-bar.png" class="img-responsive center img-bordered">

Views include:

- Commits
- Branches
- Remotes
- Stashes
- Tags
- Worktrees
- Contributors
- Repositories (hidden by default)

### (Bottom) Panel

The new home for the Commit Graph, providing convenient and easy access to the graph and the new Commit Graph Details view.

<img src="/wp-content/uploads/gl-bottom-panel.png" class="img-responsive center img-bordered">

Views include:

- Commit Graph
- Commit Graph Details

_Pro tip: You can toggle the Commit Graph between Panel and Editor layouts by clicking the "cog" icon on the upper right corner of the Graph view._
_Pro tip 2: When the Commit Graph is in the Panel Layout, you can quickly toggle it via the new **Toggle Commit Graph** and **Toggle Maximized Commit Graph** commands._

### Adopting the new views layout

Unless you opt into the new layout, which we recommend, your existing views will stay where they are. You can opt in at any time from _Reset Views Layout_ in the Command Palette.

## New Onboarding Experience

The rebuilt welcome goes beyond quick settings and now includes overviews of important features as well as bringing better visibility to the views and functionality GitLens offers. Along the same lines, we consolidated and streamlined our walkthroughs.

Also, we've made significant changes to the home view, with the help of your feedback, to refocus on quick access and discovery of many GitLens features.

## ☁️ GitKraken Workspaces

GitKraken Workspaces are a convenient way to group and manage multiple repositories. Cloud workspaces store the metadata of the grouped repositories and can be accessed across machines and GitKraken products. They can easily be imported into or created from VS Code workspaces.

<img src="/wp-content/uploads/gl-workspaces-sidebar.png" class="img-responsive center img-bordered">

Please note that while using cloud workspaces requires a free account, shared cloud workspaces, which are shared between GitKraken organizations and teams, require a trial or plan. Shared Workspaces functionality is coming soon to GitLens.

Workspaces can be accessed in the new GitKraken Workspaces view in the GitLens side bar.

## Commit Graph Enhancements `PRO`

We’ve greatly improved the ease of access to the Commit Graph as well as additional change information and easy-to-use customization options.

### New Home in (Bottom) Panel

The Commit Graph has moved into the (bottom) panel, providing convenient and persistent access to the graph and its details. If you prefer the Graph in the editor area, you can toggle between Panel and Editor layouts by clicking the "cog" icon on the upper right corner of the Graph view.

### Minimap and Markers

The Minimap which shows an overview of commit activity, previously an experimental feature, is now on by default. You can now toggle between 'lines changed' and 'commits' in the minimap display.

With both the Minimap and the Commit Graph scrollbar, you can toggle specific markers on and off, including local branch, remote branch, stash, and tag markers. For the minimap, use the split minimap button, and for the scrollbar use the `Scroll Markers` submenu from the "cog" icon at the top of the scrollbar.

### New Column and Column Layout

The _Changes_ column, which shows the size of commit changes, is now visible by default. The column now also includes a count of the changed files, helping you quickly grasp the scale of each change.

Reset your columns between the _Default_ and the new _Compact_ set via the context menu on the graph column headers, making it easy to toggle into a more minimal experience.

### Added

- Adds an all-new Welcome experience to quickly get started with GitLens and discover features &mdash; even if you are familiar with GitLens, definitely check it out!
- Adds a new streamlined _Get Started with GitLens_ walkthrough
- Adds an all-new _Home_ view for quick access to GitLens features and _GitKraken Account_ for managing your account
- Adds a new reimagined views layout &mdash; see discussion [#2721](https://github.com/gitkraken/vscode-gitlens/discussions/2721) for more details
  - Rearranges the GitLens views for greater focus and productivity, including the new _GitLens Inspect_ and moved some of our views from Source Control into either _GitLens_ or _GitLens Inspect_.
  - Adds a new GitLens Inspect activity bar icon focuses on providing contextual information and insights to what you're actively working on
  - Adds a _Reset Views Layout_ command to reset all the GitLens views to the new default layout
- Adds an all-new _GitKraken Workspaces_ ☁️ feature as a side bar view, supporting interaction with local and cloud GitKraken workspaces, lists of repositories tied to your account.
  - Create, view, and manage repositories on GitKraken cloud workspaces, which are available with a GitKraken account across the range of GitKraken products
  - Automatically or manually link repositories in GitKraken cloud workspaces to matching repositories on your machine
  - Quickly create a GitKraken cloud workspace from the repositories in your current window
  - Open a GitKraken cloud workspace as a local, persisted, VS Code workspace file (further improvements coming soon)
  - Open a cloud workspace or repository in a new window (or your current window)
  - See your currently open repositories in the _Current Window_ section
  - Explore and interact with any repository in a GitKraken cloud workspace, some actions are currently limited to repositories which are open in your current window &mdash; ones highlighted in green
  - (Coming soon) Share your GitKraken cloud workspaces with your team or organization
- Adds new _Commit Graph_ `PRO` features and improvements
  - Makes the _Panel_ layout the default for easy access to the Commit Graph with a dedicated details view
  - Adds two new options to the graph header context menu
    - `Reset Columns to Default Layout` - resets column widths, ordering, visibility, and graph column mode to default settings
    - `Reset Columns to Compact Layout` - resets column widths, ordering, visibility, and graph column mode to compact settings
  - Adds a _Toggle Commit Graph_ command to quickly toggle the graph on and off (requires the _Panel_ layout)
  - Adds a _Toggle Maximized Commit Graph_ command to maximize and restore the graph for a quick full screen experience (requires the _Panel_ layout)
  - Enables the _Minimap_ by default, as its no longer experimental, to provide a quick overview of of commit activity above the graph
    - Adds ability to toggle between showing commits vs lines changed in the minimap (note: choosing lines changed requires more computation)
    - Adds a legend and quick toggles for the markers shown on the minimap
    - Defers the loading of the minimap to avoid impacting graph performance and adds a loading progress indicator
    - Adds a `gitlens.graph.minimap.enabled` setting to specify whether to show the minimap
    - Adds a `gitlens.graph.minimap.dataType` setting to specify whether to show commits or lines changed in the minimap
    - Adds a `gitlens.graph.minimap.additionalTypes` setting to specify additional markers to show on the minimap
  - Makes the _Changes_ column visible by default (previously hidden)
    - Defers the loading of the _Changes_ column to avoid impacting graph performance and adds a loading progress indicator to the column header
    - Adds a changed file count in addition to the changed lines visualization
    - Improves the rendering of the changed line visualization and adds extra width to the bar for outlier changes so that they stand out a bit more
  - Adds an _Open Repo on Remote_ button to left of the repo name in the graph header
  - Improves contextual help on the search input as you type
  - Improves tooltips on _Branch/Tag_ icons to be more uniform and descriptive
  - Adds new context menu options to the _Commit Graph Settings_ (cog, above the scrollbar) to toggle which scroll marker to show
  - Improves alignment of scroll markers on the scrollbar, and adds a gap between the last column and the scrollbar
- Adds the ability to choose which AI provider, OpenAI or Anthropic, and AI model are used for GitLens' experimental AI features
  - Adds a _Switch AI Model_ command to the command palette and from the _Explain (AI)_ panel on the _Commit Details_ view
  - Adds a `gitlens.ai.experimental.provider` setting to specify the AI provider to use (defaults to `openai`)
  - Adds a `gitlens.ai.experimental.openai.model` setting to specify the OpenAI model (defaults to `gpt-3.5-turbo`) &mdash; closes [#2636](https://github.com/gitkraken/vscode-gitlens/issues/2636) thanks to [PR #2637](https://github.com/gitkraken/vscode-gitlens/pull/2637) by Daniel Rodríguez ([@sadasant](https://github.com/sadasant))
  - Adds a `gitlens.ai.experimental.anthropic.model` setting to specify the Anthropic model (defaults to `claude-v1`)
- Adds expanded deep link support
  - Adds cloning, adding a remote, and fetching from the target remote when resolving a deep link
  - Adds deep linking to a repository with direct file path support
- Adds the automatic restoration of all GitLens webviews when you restart VS Code
- Adds ability to control encoding for custom remote configuration &mdash; closes [#2336](https://github.com/gitkraken/vscode-gitlens/issues/2336)
- Improves performance and rendering of the _Visual File History_ and optimizes it for usage in the side bars
  - Adds a _Full history_ option to the _Visual File History_ &mdash; closes [#2690](https://github.com/gitkraken/vscode-gitlens/issues/2690)
  - Adds a loading progress indicator
- Adds _Reveal in File Explorer_ command to repositories
- Adds _Copy SHA_ command to stashes
- Adds new icons for virtual repositories

### Changed

- Changes header on _GitLens Settings_ to be consistent with the new Welcome experience
- Reduces the visual noise of currently inaccessible `PRO` features in the side bars
- Performance: Improves rendering of large commits on the _Commit Details_ view
- Performance: Defers possibly duplicate repo scans at startup and waits until repo discovery is complete before attempting to find other repos
- Security: Disables Git access in Restricted Mode (untrusted)
- Security: Avoids dynamic execution in string interpolation

### Fixed

- Fixes [#2728](https://github.com/gitkraken/vscode-gitlens/issues/2728) - Submodule commit graph will not open in the panel layout
- Fixes [#2734](https://github.com/gitkraken/vscode-gitlens/issues/2734) - 🐛 File History: Browse ... not working
- Fixes [#2671](https://github.com/gitkraken/vscode-gitlens/issues/2671) - Incorrect locale information provided GitLens
- Fixes [#2689](https://github.com/gitkraken/vscode-gitlens/issues/2689) - GitLens hangs on github.dev on Safari
- Fixes [#2680](https://github.com/gitkraken/vscode-gitlens/issues/2680) - Git path with spaces is not properly quoted in the command
- Fixes [#2677](https://github.com/gitkraken/vscode-gitlens/issues/2677) - Merging branch produces path error
- Fixes an issue with comparison commands on File/Line History views
- Fixes an issue with stale state on many webviews when shown after being hidden
- Fixes an issue with fetch/push/pull on the _Commit Graph_ header
- Fixes an issue where _Branch / Tag_ items on the _Commit Graph_ sometimes wouldn't expand on hover
- Fixes an issue where some command were showing up on unsupported schemes
- Fixes an issue where the file/line history views could break because of malformed URIs

<a id="v13-6"></a>

## Version 13.6

### Thursday, May 11, 2023

GitLens 13.6 brings a range of enhancements and additions to the Commit Graph and refinements to our context menus. We've made improvements to the layout, condensing author names and column titles into avatars and icons when sized to minimums, and added flexibility of rearranging and moving columns as desired. This allows for a more streamlined and personalized GitLens experience. We have also updated the Commit Graph's toolbar to dynamically show a Push or Pull action, depending on a branch's state in relation to its upstream remote.

<img src="/wp-content/uploads/gl-13-6-hero.png" class="img-responsive center img-bordered">

## Context Menu Updates

<img src="/wp-content/uploads/gl-13-6-context-menu-update.gif" class="img-responsive center img-bordered">

To improve structure and findability of our menu options, we’ve made several changes to our context menus. Many Copy Remote URL commands, which were previously in a Copy As submenu, have been moved to a Share submenu within GitLens views, which aligns with VS Code menus. And once [microsoft/vscode#176316](https://github.com/microsoft/vscode/issues/176316) lands we will move the rest of the Copy Remote URL commands into the appropriate Share submenu. This reorganization consolidates related commands and makes it easier to locate and utilize them.

Similarly, the Copy SHA and Copy Message commands, previously nested in submenus, have been promoted to the root of the context menu. This elevates their visibility and enables quick access for performing actions on commits. Additionally, the Copy Relative Path command has been relocated to the root of the context menu. These adjustments enhance convenience when working with file paths.

### Commit Graph Enhancements `PRO`

We’ve made it easier to customize your Commit Graph experience as well as improvements for better readability when in compact layouts.

#### Compact Graph Improvements

<img src="/wp-content/uploads/gl-13-6-graph-customize-columns.gif" class="img-responsive center img-bordered">

Previously unmovable columns within the Commit Graph can now be rearranged and customized according to your preferences. This flexibility enables you to arrange the columns in a way that best suits their workflow and priorities.

In addition, we have implemented a more compact layout by removing the commit icon when avatars are hidden. This optimization maximizes the utilization of screen space and results in a cleaner and more streamlined visual representation.

Moreover, the Author column now displays avatars instead of text when sized to its minimum width. That combined with the compact layout for the Graph column provide a nice compact experience with no loss of fidelity.

#### Column Headers

<img src="/wp-content/uploads/gl-13-6-graph-show-hide-columns.gif" class="img-responsive center img-bordered">

Commit Graph column headers have received dynamic behavior for enhanced readability. When the Commit Graph columns are compacted, the column headers seamlessly switch from displaying text to icons. This adaptation ensures that crucial information remains visible, even in constrained display settings.

### Stash Improvements

We've added the ability to rename stashes. If you are like me and often stash changes in a rush with very poor names, e.g. "wip" and then kick yourself later for not providing a more descriptive name, the this feature is for you. You can now rename any stash at any time.

You can now search within stashes using the Commit Graph, the Search & Compare view, or the Search Commits command. This improvement facilitates efficient navigation and retrieval of specific stash entries.

### Added

- Adds the ability to rename stashes &mdash; closes [#2538](https://github.com/gitkraken/vscode-gitlens/issues/2538)
  - Adds a new _Rename Stash..._ command to the _Stashes_ view
- Adds new _Commit Graph_ features and improvements
  - Adds a _Push_ or _Pull_ toolbar button depending the current branch being ahead or behind it's upstream
  - Adds support for the _Commit Graph_ over [Visual Studio Live Share](https://visualstudio.microsoft.com/services/live-share/) sessions
  - Adds the ability to move all of the columns, including the ones that were previously unmovable
  - Automatically switches column headers from text to icons when the column's width is too small for the text to be useful
  - Automatically switches the Author column to shows avatars rather than text when the column is sized to its minimum width
- Adds the ability to search stashes when using the commit search via the _Commit Graph_, _Search & Compare_ view, or the _Search Commits_ command
- Adds an _Open Visual File History_ command to the new _File History_ submenu on existing context menus
- Allows the _Repositories_ view for virtual repositories
- Honors the `git.repositoryScanIgnoredFolders` VS Code setting
- Adds _Share_, _Open Changes_, and _Open on Remote (Web)_ submenus to the new editor line numbers (gutter) context menu
- Adds an _Open Line Commit Details_ command to the _Open Changes_ submenus on editor context menus
- Adds an _Open Changes_ submenu to the row context menu on the _Commit Graph_

### Changed

- Refines and reorders many of the GitLens context menus and additions to VS Code context menus
  - Moves _Copy Remote \* URL_ commands from the _Copy As_ submenu into the _Share_ submenu in GitLens views
  - Adds a _Share_ submenu to Source Control items
  - Moves _Copy SHA_ and _Copy Message_ commands on commits from the _Copy As_ submenu into the root of the context menu
  - Moves _Copy Relative Path_ command on files from the _Copy As_ submenu into the root of the context menu
  - Moves file history commands into a _File History_ submenu
  - Moves _Open \* on Remote_ commands into _Open on Remote (Web)_ submenu
  - Renames the _Commit Changes_ submenu to _Open Changes_
  - Renames _Show Commit_ command to _Quick Show Commit_ and _Show Line Commit_ command to _Quick Show Line Commit_ for better clarity as it opens a quick pick menu
- Changes the file icons shown in many GitLens views to use the file type's theme icon (by default) rather than the status icon
  - Adds a `gitlens.views.commits.files.icon` setting to specify how the _Commits_ view will display file icons
  - Adds a `gitlens.views.repositories.files.icon` setting to specify how the _Repositories_ view will display file icons
  - Adds a `gitlens.views.branches.files.icon` setting to specify how the _Branches_ view will display file icons
  - Adds a `gitlens.views.remotes.files.icon` setting to specify how the _Remotes_ view will display file icons
  - Adds a `gitlens.views.stashes.files.icon` setting to specify how the _Stashes_ view will display file icons
  - Adds a `gitlens.views.tags.files.icon` setting to specify how the _Tags_ view will display file icons
  - Adds a `gitlens.views.worktrees.files.icon` setting to specify how the _Worktrees_ view will display file icons
  - Adds a `gitlens.views.contributors.files.icon` setting to specify how the _Contributors_ view will display file icons
  - Adds a `gitlens.views.searchAndCompare.files.icon` setting to specify how the _Search & Compare_ view will display file icons
- Renames _Delete Stash..._ command to _Drop Stash..._ in the _Stashes_ view
- Removes the commit icon when hiding avatars in the _Commits_ view to allow for a more compact layout
- Limits Git CodeLens on docker files &mdash; closes [#2153](https://github.com/gitkraken/vscode-gitlens/issues/2153)
- Shows progress notification for deep links earlier in the process &mdash; closes [#2662](https://github.com/gitkraken/vscode-gitlens/issues/2662)

### Fixed

- Fixes [#2664](https://github.com/gitkraken/vscode-gitlens/issues/2664) - Terminal run Git command can be "corrupted" if there is previous text waiting in the terminal
- Fixes [#2660](https://github.com/gitkraken/vscode-gitlens/issues/2660) - Commands executed in the terminal fail to honor found Git path
- Fixes [#2654](https://github.com/gitkraken/vscode-gitlens/issues/2654) - Toggle zen mode not working until you restart vscode
- Fixes [#2629](https://github.com/gitkraken/vscode-gitlens/issues/2629) - When on VSCode web, add handling for failing repo discovery
- Fixes many issues with using GitLens over [Visual Studio Live Share](https://visualstudio.microsoft.com/services/live-share/) sessions
- Fixes mouse scrubbing issues with the minimap on the _Commit Graph_
- Fixes _Refresh Repository Access_ and _Reset Repository Access Cache_ commands to always be available
- Fixes state not being restored on the Home webview
- Fixes getting the oldest unpushed commit when there is more than 1 remote
- Fixes an issue with the quick input on the _Git Command Palette_ unexpectedly going back to the previous step
- Fixes GitLens access tooltip not being visible when hovering in the _Commit Graph_

### Removed

- Removes "Open Commit on Remote" command from the VS Code Timeline view as it can no longer be supported &mdash; see [microsoft/vscode#177319](https://github.com/microsoft/vscode/issues/177319)

<a id="v13-5"></a>

## Version 13.5

### Thursday, Apr 6, 2023

With 13.5, we've added the ability to switch to an alternate panel layout for the Commit Graph, which moves the Commit Graph into the bottom panel and adds a new Commit Graph Details view alongside on the right, for more convenient and persistent access. You can now also switch to a compact layout for the Graph column and shrink the Branch / Tag column to a single icon to reduce the space and allow you to focus on what you deem most important. You can now take action on your pull requests in the Focus View, with the new ability to create or switch branches or worktrees. We've also heard your feedback that the Commit Details view pinning was confusing and hard to work with, so 13.5 includes many improvements to make that experience better. We've also continued our quest to reduce the size and improve performance of GitLens and have shaved another ~7% off the GitLens bundle.

<img src="/wp-content/uploads/gl-13-5-hero.png" class="img-responsive center img-bordered">

### Commit Graph Layouts `PRO`

<img src="/wp-content/uploads/gl-commit-graph-panel-layout-view.png" class="img-responsive center img-bordered">

The new panel layout brings even more flexibility and customization options to GitLens. While using the panel layout, GitLens moves the Commit Graph into the bottom panel and adds a new Commit Graph Details view alongside on the right. If the layout in the bottom panel doesn't suit your needs you can move the Commit Graph around to other locations (side bar, secondary side bar, etc) to suit your preferences. Whether you prefer to have the Commit Graph in the editor or in a separate panel, GitLens makes it easy to switch and find the layout that works best for you.

<img src="/wp-content/uploads/gl-commit-graph-panel-layout-change.gif" class="img-responsive center img-bordered">

To switch to the panel layout, simply click on the Commit Graph settings cog located at the top right of the Commit Graph. From there, select the "Switch Commit Graph to Panel Layout" option, and if you want to switch back follow the same steps and choose "Switch Commit Graph to Editor Layout".

#### Compact Graph Column Layout

<img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="img-responsive center img-bordered">

With the new compact Graph column layout, GitLens provides a more streamlined and compact layout to reduce the space required to visualize the commit history and branch relationships.

To enable the new compact Graph Column layout, right click on the Graph column header, and select the "Compact Graph Column Layout" option. If you want to switch back follow the same steps and choose "Default Graph Column Layout".

#### Pull Requests on Local Branches

You can now see pull requests (PRs) for your local branch upstreams directly on the local branches themselves. You no longer have to hunt for the local branch's upstream on the Commit Graph to see the associated PR.

#### Publish Local Branches from Commit Graph

Publishing local branches directly from the Commit Graph is a nice productivity boost. You can quickly and easily publish your local changes without having to switch to the Branches view or use the command line.

### Focus View Pull Request Actions `PRO`

<img src="/wp-content/uploads/gl-focus-view-create-worktree-create-branch.png" class="img-responsive center img-bordered">

The Focus View is no longer read-only! We've introduced new actions within Focus View, aimed at enhancing your workflow and productivity. You can now easily create a branch or worktree, or switch/open an existing one, for a PR directly from the Focus View page, streamlining the process of reviewing or contributing to pull requests. As a quick worktree refresher, creating a worktree from the PR will let you review or contribute to multiple PRs simultaneously without affecting your current branch and working tree.

### Commit Details Interaction Improvements

<img src="/wp-content/uploads/gl-commit-details-pinned-commit-deets.png" class="img-responsive center img-bordered">

We've heard your feedback on the Commit Details view and the confusion and difficulty with using the pinning feature. We updated the visual appearance of the pinned state, so its easier to know when Commit Details is pinned. Additionally, we've introduced navigation controls that enable you to move back and forth through the commits you've recently viewed, helping to avoid losing context as you navigate through your code.

### Thank you to our contributors

Shout-out to all of our awesome contributors for this release!

- WofWca ([@WofWca](https://github.com/WofWca))

### Added

- Adds the ability to switch to an alternate panel layout for the _Commit Graph_ &mdash; closes [#2602](https://github.com/gitkraken/vscode-gitlens/issues/2602) and [#2537](https://github.com/gitkraken/vscode-gitlens/issues/2537)
  - Adds a new context menu from the _Commit Graph Settings_ (cog) to switch between the "Editor" and "Panel" layouts
  - Adds a `gitlens.graph.layout` setting to specify the layout of the _Commit Graph_
    - `editor` - Shows the _Commit Graph_ in an editor tab
    - `panel` - Shows the _Commit Graph_ in the bottom panel with an additional _Commit Graph Details_ view alongside on the right
- Adds new _Commit Graph_ features and improvements
  - Adds a compact layout to the Graph column of the _Commit Graph_
    - Adds a context menu option to the header to toggle between the "Compact" and "Default" layouts &mdash; closes [#2611](https://github.com/gitkraken/vscode-gitlens/pull/2611)
  - Shows pull request icons on local branches when their upstream branch is associated with a pull request
  - Adds tooltips to work-in-progress (WIP) and stash nodes
  - Adds a "Publish Branch" context menu action to local branches without an upstream branch &mdash; closes [#2619](https://github.com/gitkraken/vscode-gitlens/pull/2619)
  - Lowers the minimum width of the "Branch / Tag" column
- Adds actions to _Focus View_ Pull Requests
  - Switch to or create a local branch
  - Create or open a worktree from the branch
- Adds a _Generate Commit Message (Experimental)..._ command to the SCM context menus

### Changed

- Reduces the size of the GitLens (desktop) bundle which reduces memory usage and improves startup time &mdash; ~7% smaller (1.21MB -> 1.13MB)
  - Consolidates the "extension" side of all the GitLens webviews/webview-views into a unified controller and code-splits each webview/webview-view into its own bundle
    - Allows for very minimal code to be loaded for each webview/webview-view until its used, so if you never use a webview you never "pay" the cost of loading it
- Changes _Open Associated Pull Request_ command to support opening associated pull requests with the current branch or the HEAD commit if no branch association was found &mdash; closes [#2559](https://github.com/gitkraken/vscode-gitlens/issues/2559)
- Improves the "pinning" of the _Commit Details_ view
  - Avoids automatically pinning
  - Changes the pinned state to be much more apparent
- Changes _Commit Details_ to always open diffs in the same editor group as the currently active editor &mdash; closes [#2537](https://github.com/gitkraken/vscode-gitlens/issues/2537)

### Fixed

- Fixes [#2597](https://github.com/gitkraken/vscode-gitlens/issues/2597) - Allow disabling "Open worktree for pull request via GitLens..." from repository context menu
- Fixes [#2612](https://github.com/gitkraken/vscode-gitlens/issues/2612) - Clarify GitLens telemetry settings
- Fixes [#2583](https://github.com/gitkraken/vscode-gitlens/issues/2583) - Regression with _Open Worktree for Pull Request via GitLens..._ command
- Fixes [#2252](https://github.com/gitkraken/vscode-gitlens/issues/2252) - "Copy As"/"Copy Remote File Url" copies %23 instead of # in case of Gitea &mdash; thanks to [PR #2603](https://github.com/gitkraken/vscode-gitlens/pull/2603) by WofWca ([@WofWca](https://github.com/WofWca))
- Fixes [#2582](https://github.com/gitkraken/vscode-gitlens/issues/2582) - _Visual File History_ background color when in a panel
- Fixes [#2609](https://github.com/gitkraken/vscode-gitlens/issues/2609) - If you check out a branch that is hidden, GitLens should show the branch still
- Fixes tooltips sometimes failing to show in _Commit Graph_ rows when the Date column is hidden
- Fixes [#2595](https://github.com/gitkraken/vscode-gitlens/issues/2595) - Error when stashing changes

<a id="v13-4"></a>

## Version 13.4

### Thursday, Mar 16, 2023

With 13.4, we've introduced an experimental new AI feature to assist with writing commit messages, improved GitLens performance by reducing its size, made improvements to the `PRO` Commit Graph, and accepted community contributions as well as many bug fixes from community feedback.

<img src="/wp-content/uploads/gl-13.4-banner.png" class="img-responsive center img-bordered">

### AI-Generated Commit Messages (Experimental)

<img src="/wp-content/uploads/gl-ai-generated-commit-message.gif" class="img-responsive center img-bordered">

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

### Commit Graph Enhancements `PRO`

##### Upstream Tracking

<img src="/wp-content/uploads/gl-upstream-tracking.png" class="img-responsive center img-bordered">

It's now possible to effortlessly keep track of upstreams of your local branches in the commit graph. The upstreams of visible local branches, along with their corresponding commit history, will be displayed in the graph even if other remote branches are filtered out from your settings.

We've also revised the wording of the remote filter setting to "Hide Remote-only Branches.

#### Graph Alignment

<img src="/wp-content/uploads/gl-graph-alignment.png" class="img-responsive center img-bordered">

The graph column is now more left-aligned, making it easier to read and follow the history of a branch at a glance.

#### Branches and Tags on Remote Repositories

<img src="/wp-content/uploads/gl-remote-ref-tracking.png" class="img-responsive center img-bordered">

You can now see the tips of your branches and tags in the Commit Graph on remote repositories! Previously, opening a remote repository in the graph would show only the current branch. Currently, we are still limited to only showing commits for the current branch, so the included branches and tags are ones pointing to commits in the current branch’s commit history.

### Sunsetting GitLens Insiders (Replaced with Pre-release)

<img src="/wp-content/uploads/gl-sunsetting-insiders.gif" class="img-responsive center img-bordered">

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
- Fixes [#2495](https://github.com/gitkraken/vscode-gitlens/issues/2495) - Cannot use GitLens Pro feature on public repo in some folders
- Fixes [#2530](https://github.com/gitkraken/vscode-gitlens/issues/2530) - Error when creating worktrees in certain conditions
- Fixed [#2566](https://github.com/gitkraken/vscode-gitlens/issues/2566) - hide context menu in output panel &mdash; thanks to [PR #2568](https://github.com/gitkraken/vscode-gitlens/pull/2568) by hahaaha ([@hahaaha](https://github.com/hahaaha))
- Fixes [#2533](https://github.com/gitkraken/vscode-gitlens/issues/2533) - Current Branch Only graph filter sometimes fails
- Fixes [#2504](https://github.com/gitkraken/vscode-gitlens/issues/2504) - Graph header theme colors were referencing the titlebar color properties
- Fixes [#2527](https://github.com/gitkraken/vscode-gitlens/issues/2527) - shows added files for Open All Changes
- Fixes an issue where trial status can be shown rather than a purchased license
- Fixes graph issue where scroll markers do not update until mouseover when changing the `gitlens.graph.scrollMarkers.additionalTypes` setting.

---

<a id="v13-3"></a>

## Version 13.3

### Thursday, Feb 23, 2023

Supercharge your Git game with GitLens 13.3: the latest update to help you master Git like a pro. With 13.3 we’re introducing Workspace Focus View, Deep Linking Support, and Commit Graph Improvements featuring the new (experimental) minimap and changes column.

<img src="/wp-content/uploads/glrn-13.3.png" class="img-responsive center img-bordered">

GitLens also just got a whole lot faster with the release of version 13.3! Thanks to some serious bundle slimming, the startup times have significantly improved.

- GitLens' extension bundle for desktop (node) is now ~18% smaller
- GitLens' extension bundle for web (vscode.dev/github.dev) is now ~37% smaller
- GitLens' Commit Graph webview bundle is now ~31% smaller

### Focus View (Preview) `PRO`

<img src="/wp-content/uploads/glrn-focus-view.png" class="img-responsive center img-bordered">

With the preview of GitLens Focus View, you can streamline your workflow and prioritize your tasks with ease. The Focus View feature gives you a comprehensive list of all your most important work across all your GitHub repos. No more jumping back and forth between multiple pages or repos - GitLens Focus View makes it simple and efficient to keep track of and manage your work progress.

The new Focus View will provide you with a summary of Pull Requests and Issues relevant to you for the repositories grouped in your Workspace.

- My Pull Requests: shows all GitHub PRs opened by you, assigned to you, or awaiting your review
- My Issues: shows all issues created by you, assigned to you, or that mention you.

Instead of hunting for these pieces of information separately, you can get a holistic view of what you’re working on.

\*_Note Focus View is currently in a Preview Only state, it is subject to change in the future._

### Commit Graph improvements `PRO`

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

---

<a id="v13-2"></a>

## Version 13.2

### Tuesday, Dec 20th, 2022

Since the release of [GitLens 13](https://www.gitkraken.com/blog/gitlens-13), we know how the power of GitLens Pro features like the Commit Graph, have been helping supercharge your dev workflow. That’s why we’re excited to present GitLens 13.2, with all new (and highly requested) Graph improvements like filtering, to quickly focus on what is most important to you. We've also streamlined the Commit Graph interface with a new header bar, providing context and quick access to switch between repositories or branches, and even fetch to keep up to date. Get ready to level up your Git game with GitLens 13.2!

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
    - Also moves GitLens Pro feature status and feedback links to the top right
  - Adds new ability to reorder columns by dragging and dropping column headers (not all columns are reorderable)
  - Adds new keyboard shortcuts
    - Use `shift+down arrow` and `shift+up arrow` to move to the parent/child of the selected commit row
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

---

<a id="v13-1"></a>

## Version 13.1

### Thursday, November 17th, 2022

With GitLens 13, we released the power of GitLens Pro features like the Commit Graph, Visual File History, and Worktrees to ALL users on local and public repos. No account required. Learn more about the changes happening with GitLens in this [article](https://www.gitkraken.com/blog/gitlens-13).

<img src="/wp-content/uploads/GitLens-13-1-Hero.png" class="img-responsive center img-bordered">

## Commit Graph Enhancements

### Search History

Find what you seek with ease! Quickly navigate through your search history by using the UP⇧ or DOWN⇩ arrow keys.

<img src="/wp-content/uploads/New-Search-History.gif" class="img-responsive center img-bordered">

### New Search Filter @me

Want to see only your commits? Search For @me to highlight only your commits.

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

You can now customize the Commit Details view from the GitLens Settings editor to personalize how it looks and behaves so you can focus on the most important details.

<img src="/wp-content/uploads/commit-details-view-1.png" class="img-responsive center img-bordered">

## Terminal Links Can Use the Commit Details View

Terminal Links for commits in VS Code’s integrated terminal now use the Commit Details view to provide rich details about the selected commit.

## GitLens Home View Updates

Keeping a home tidy is important! We’ve streamlined the Home view to make it even easier to get started with GitLens, learn about its features, and how to personalize your experience.

<img src="/wp-content/uploads/New-Home-Side-Panel.png" class="img-responsive center img-bordered">

## Added

- Adds Commit Graph enhancements
  - Adds the ability to set keyboard shortcuts to commits and stashes on the Commit Graph — closes [#2345](https://github.com/gitkraken/vscode-gitlens/issues/2345) - Keyboard shortcuts can be applied to many of the gitlens.graph.\* commands and should use gitlens:webview:graph:focus && !gitlens:webview:graph:inputFocus for their "When Expression" to only apply when the Commit Graph is focused - For example, add the following to your keybindings.json to allow Ctrl+C to copy the selected commit's SHA to the clipboard
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

---

<a id="v13-0"></a>

## Version 13.0

### Monday, October 17th, 2022

Find what you seek.

<img src="/wp-content/uploads/gitlens-13-social-3x.png" class="img-responsive center img-bordered">

## GitLens Pro Features for All on Local & Public Repos `PRO`

With GitLens 13.0, we are excited to bring the power of GitLens Pro features like the Commit Graph, Visual File History, and Worktrees to ALL users on local and public repos. No account required. Learn more about the changes happening with GitLens in this [article](https://www.gitkraken.com/blog/gitlens-13).

Here’s how to get started with each of the GitLens Pro features with your local or public repos:

- [Commit Graph](https://help.gitkraken.com/gitlens/gitlens-plus/#commit-graph)
- [Worktrees](https://help.gitkraken.com/gitlens/gitlens-plus/#worktrees)
- [Visual File History](https://help.gitkraken.com/gitlens/gitlens-plus/#visual-file-history)

## Commit Graph - Now out of Preview! `PRO`

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

Whether searching for a specific commit, message, author, a changed file or files, or even a specific code change, the Commit Graph will highlight matching results across your entire repository. Use shortcut keys or the up/down arrows on the search bar to navigate the search results; `F3` (also `Cmd+G` on macOS) goes to the next result from your selection while `Shift+F3` ( also `Shift+Cmd+G` on macOS) goes to the previous. Additionally you can quickly jump to the first or last result, by holding `Shift` while clicking on the up/down arrows respectively – to make it easy to see when a file or change was introduced into the codebase.

<img src="/wp-content/uploads/Rich-Commit-Search.png" class="img-responsive center img-bordered">

Once you type search filtering criteria, use the arrow icons to move through each result.

<img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="img-responsive center img-bordered">

### PR information in form of icon

Wait, which branch has that PR?

If connected to one of the rich integrations with GitHub or GitLab, the Commit Graph will display a PR icon for any branch currently in PR. Right-click on the PR icon to open the PR on the GitHub or GitLab, or copy the URL.

<img src="/wp-content/uploads/PR-Icon.png" class="img-responsive center img-bordered">

### Hiding remotes, branches or tags

Need to focus and have too many remotes or just want to curate how much is shown in your Commit Graph? Now you can hide entire remotes, or specific branches and tags. Hover over any branch or tag to access the “Hide” button or right-click to hide the whole remote, or just the local or remote branch, to help focus your Commit Graph.

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

- `PRO` All GitLens Pro features on public and local repos are now available to everyone -- no account required!
  - We want to bring the power of GitLens Pro features to more people without any gates.
- `PRO` Commit Graph is out of preview!
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

---

<a id="v12-2"></a>

## Version 12.2

### Tuesday, August 30th, 2022

The new Commit Graph 🎨 in GitLens 12.2 will fix all your commitment problems...in your code 🥁 👩‍💻

<div class='embed-container embed-container--16-9'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/EsnA4zIUvWY?controls=1&modestbranding=1" frameborder="0" allowfullscreen></iframe>
</div>

## Commit Graph - Preview `PRO`

Users may now view the Commit Graph of their repository through GitLens.

This beloved feature from GitKraken Desktop helps visualize your repo commit history and give you information about branches, commits, and collaborators all in one view — making it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/1-commit-graph.png" class="img-responsive center img-bordered">

To open the Commit Graph, open the command palette using the keyboard shortcut <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd> and type `Show Commit Graph`.

<img src="/wp-content/uploads/2-commit-graph.gif" class="img-responsive center img-bordered">

This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths.

You may also access the Commit Graph by clicking this graph icon from the Source Control view in the Sidebar or Status Bar.

<img src="/wp-content/uploads/How-to-open-commit-graph-B.png" class="img-responsive center img-bordered">

The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens Pro subscription can use the Commit Graph with private repos.

For those on [vscode.dev](vscode.dev) or [github.dev](github.dev), this also means you can open the Commit Graph on a web browser.

The Commit Graph is in `Preview` mode, and we’d love to hear your feedback in the [Commit Graph discussion on GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).

## Commit Details View

GitLens 12.2 also ships with a `Commit Details View`, which gives you contextual change info about your code.

<img src="/wp-content/uploads/3-commit-details-view.png" class="img-responsive center img-bordered">

To open the `Commit Details View`, open the command palette using <kbd>Cmd</kbd> <kbd>Shift</kbd> <kbd>P</kbd> and this time type: `Show Commit Details View` or navigate to the Commit Details View in the Sidebar.

<img src="/wp-content/uploads/4-commit-details-view.gif" class="img-responsive center img-bordered">

The `Commit Details View` updates as you move your cursor throughout the file with information about the commit that modified that line of code. Get quick information about the commit author, commit ID, links to Pull Requests, files modified in the commit, and more.

Click on a file to open the diff, and see what changed. You may also hover over the file name to access options like Open File, Open Changes with Working File, and Open Remote.

## GitHub Enterprise Integration `PRO`

Next, GitLens Pro now offers a richer integration with GitHub Enterprise.

Once authenticated, GitLens will enrich GitHub autolinks in the hovers. You’ll see your GitHub Enterprise avatar, links to related pull requests, along with a footnote of the pull request or issue details.

<img src="/wp-content/uploads/6-GitHub-Enterprise.png" class="img-responsive center img-bordered">

You’ll see similar details from the Sidebar views for any commit or branch associated with a pull request or issue.

## Single Sign On `PRO`

Single Sign On is here, providing GitLens Pro users with a more secure sign in method!

### Requirements and configuration

Your GitKraken account may now initiate an Oauth authentication flow with the following supported Identity Providers (IdPs):

- Azure Active Directory
- Okta
- Google Identity Platform
- Ping Identity

<img src="/wp-content/uploads/SSO-setup.png" class="img-responsive center img-bordered">

Please note that your IdP will first need to be configured before setting up the connection in your GitKraken account. For assistance, please contact your IdP administrator or consult the IdP documentation for help.

Additional requirements: - Configurable only by GitKraken Owner or Admin of an organization - Subscribed to either the Teams or Enterprise plan

→ [Documentation: How to set up SSO in GitKraken](https://help.gitkraken.com/gitkraken-client/single-sign-on/)

### Signing in with SSO

GitLens Pro users should see a new option to Sign in with SSO from the login screen.

<img src="/wp-content/uploads/9-GitLens-SSO.png" class="img-responsive center img-bordered">

After clicking `Sign in with SSO`, the SSO form will open and ask for an email address to use for SSO login. The app will then check the email and determine whether the email address belongs to a single IdP for SSO. When the email address is successfully identified, the user will be taken to that IdP to login.

Once authenticated, the user may use GitLens Pro

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
