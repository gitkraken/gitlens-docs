---
title: GitLens Release Notes
description: GitLens Release Notes
taxonomy:
  category: gitlens
last_updated: 2026-11
---

<kbd>Last updated: November 2026</kbd>

Find out what's new, what's fixed, or just take a trip down memory lane remembering those bugs of yesterday.

Check out our [Changelog](https://github.com/gitkraken/vscode-gitlens/blob/main/CHANGELOG.md) to see linked issues and past changes.

<a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank" class="button button--basic ">Install Current Version Now</a>

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos \
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Community, Pro, etc

---

<a id="v19-7"></a>

## Version 19.7

#### Tuesday, November 24, 2026

GitLens 19.7 makes it easier to clean up merged branches in the _Commit Graph_, improves contrast in light and high contrast themes, and uses less memory when reading Git history. It also fixes interrupted history reads, Git operations that stalled after a timeout on Windows, and several long-standing _Commit Graph_ issues.

<img src="/wp-content/uploads/gl-19-7-hero.png" class="help-center-img img-bordered" alt="GitLens 19.7 highlights: smarter branch cleanup, sharper in light themes, and lighter, steadier Git, beside the Commit Graph in a high contrast light theme.">

### More Consistent Branch Cleanup

Version 19.6 added cleanup actions for branches whose work has landed. In 19.7, the _Commit Graph_ makes those actions easier to find and more consistent.

- The header and _Working Changes_ use the same check for whether the current branch landed, and its _Overview_ card shows cleanup without a hover. The header's _Publish Branch_ updates when you change the merge target.
- Once GitLens confirms a branch has landed, the Commit Graph offers to delete it and no longer suggests _Force Push_, _Switch to Branch_, _Create a Pull Request_, or _Recompose Branch_.
- While a pull request is in the merge queue, the graph no longer offers _Push_ or _Force Push_.
- If you've added commits since a branch's pull request merged and its remote branch was deleted, GitLens leads with _Publish N New Commits_ instead of offering to delete the branch.
- When a pull request merged into a branch other than the merge target, such as a stacked parent, the merge target popover and branch details say which one. Deleting a branch that landed by squash, rebase, or fast-forward merge says where its work went, and each cleanup action says whether it deletes the branch or its worktree.

### Clearer in Light and High Contrast Themes

GitLens adds dedicated high contrast light defaults. Blame text, branch status decorations, pull request and issue icons, and _Commit Graph_ lanes stand out more clearly against white, and _Launchpad_'s attention and mergeable indicators have stronger contrast.

In light themes, _Commit Graph_ branch and tag names are darkened just enough to stay legible while keeping their lane's color, and the current branch no longer puts white text on light green. Inline blame annotations are also easier to read in high contrast dark themes.

### Steadier Git, Lighter History

- Reading history uses less memory, especially for searches that match only a few commits, and commits with very large patches or file lists are read faster.
- With Git 2.46 or later, background diff checks no longer lock the index when a tool such as a formatter touches a file without changing it, which could make your own `git add` or commit fail.
- Git operations on Windows now finish when they time out or are cancelled, such as a fetch from a remote that never responds.
- Commit lists, _File History_, contributors, and the _Commit Graph_ no longer show cut-short results with nothing more to load after a read is cancelled partway through.
- GitLens tries again after a failed pull request lookup, instead of treating the commit as having no pull request until reload. It also looks up a remote's default branch without prompting for credentials.
- Patches, cloud patches, and AI commit messages now work with Git configurations that use external diff tools or custom diff prefixes.
- GitLens detects changes in repositories and worktrees inside a `node_modules` folder or a folder whose name ends in `.git`, such as worktrees kept inside a bare repository.

### Everyday Improvements

- AI custom instructions and the commit and stash tooltip formats can now be edited in a multi-line text box in the Settings editor.
- Pull requests waiting in a merge queue get their own icon, a pull request with a clock, across the _Commit Graph_, views, hovers, autolinks, and _Launchpad_.
- _Launchpad_ clears "needs reviewers" when GitHub confirms a repository does not require a review, and the _Commit Graph_'s _Pull Requests_ panel accounts for pending code owner or team reviews when GitHub reports them.
- The _Inspect_ view now autolinks issues and pull requests in the first commit it shows.
- When the _Branches / Tags_ column is last, branch and tag pills expand to the left if that keeps them inside the _Commit Graph_, and the hidden branches and tags menu scrolls and keeps _Show All_ in reach.
- _Compare Working Tree to Here_ works on commits, stashes, and tags in the _Commit Graph_. The _Commit Graph_ button in _Source Control_ opens the right graph for nested repositories and appears for GitHub repositories opened with _Remote Repositories_.
- Repositories cloned through the port 443 SSH hosts of Bitbucket, GitHub, and GitLab (such as `ssh.github.com`) now get working remote links and deep links.
- _Copy Remote File URL_ and _Open File on Remote_ link to the current line when the cursor is at its start, and _Copy Link to Code_ leaves out the next line when a selection ends at its start.
- Links in commit messages and pull request and issue text can only open web or mail addresses.
- Claude Sonnet 4.5 is removed from the Anthropic provider ahead of its November 30, 2026 retirement. If a GitLens AI feature was set to use it, GitLens asks you to choose a replacement when you next run that feature's AI action, and each feature's model choice is now saved independently.

---

### Changed

- Changes the icon for a pull request waiting in a merge queue to a pull request with a clock badge, so it reads as queued at a glance in the _Commit Graph_, views, hovers, autolinks, and _Launchpad_ ([#6126](https://github.com/gitkraken/vscode-gitlens/issues/6126))
- Improves editing of multi-line settings in the Settings editor &mdash; the AI custom instructions and the commit and stash tooltip formats now use a multi-line text box ([#1586](https://github.com/gitkraken/vscode-gitlens/issues/1586))
- Adds high contrast light defaults for GitLens' theme colors &mdash; blame text, branch status decorations, pull request and issue icons, _Commit Graph_ lanes and pale markers, and _Launchpad_'s attention and mergeable indicators now stand out more clearly against white ([#2119](https://github.com/gitkraken/vscode-gitlens/issues/2119))
- Removes an unused inline script from the _Interactive Rebase Editor_ and _Cloud Patch_ details webviews ([#6201](https://github.com/gitkraken/vscode-gitlens/issues/6201))
- Hardens how commit messages and pull request and issue text are rendered in hovers, view tooltips, the _Commit Graph_ and _Inspect_ &mdash; links in that text can only open web or mail addresses, and only GitLens' own actions can run commands ([#6200](https://github.com/gitkraken/vscode-gitlens/issues/6200))
- Changes _Commit Graph_ shortcut overrides (`gitlens.graph.shortcuts.overrides`) to accept modifier and key names in any case, as VS Code keybindings do &mdash; `Alt+KeyM`, `alt+arrowup` and `f3` now work; single characters still match exactly, so `h` and `H` stay distinct
- Improves memory use and large-commit performance when reading commit history &mdash; GitLens retains less of Git's raw output, especially when a search keeps only a small share of the commits it reads, and commits with very large patches or file lists are parsed more efficiently ([#5659](https://github.com/gitkraken/vscode-gitlens/issues/5659))

### Removed

- Removes Claude Sonnet 4.5 from the Anthropic provider ahead of Anthropic's November 30, 2026 retirement &mdash; if a GitLens AI feature was set to use it, GitLens asks you to choose a replacement when you next run that feature's AI action ([#6164](https://github.com/gitkraken/vscode-gitlens/issues/6164))

### Fixed

- Fixes choosing an AI model for composing commits, reviewing changes, resolving conflicts, or as the default not being saved when it matched a model just chosen elsewhere &mdash; each choice is now saved independently ([#6332](https://github.com/gitkraken/vscode-gitlens/issues/6332))
- Fixes the _Create Cloud Patch_ button staying disabled after dismissing the account prompt or submitting without a title ([#6242](https://github.com/gitkraken/vscode-gitlens/issues/6242))
- Fixes the confirmation toggle in _Launchpad_ adding an invalid `launchpad:command` value to `gitlens.gitCommands.skipConfirmations` that made selecting a pull request do nothing &mdash; _Launchpad_, _Start Work_ and _Start PR Review_ no longer offer the toggle, _Stash Apply_ and _Stash Pop_ now honor their documented values, and the setting now accepts the add remote, rename stash and open worktree values ([#5645](https://github.com/gitkraken/vscode-gitlens/issues/5645))
- Fixes the _Commit Graph_ showing a blank view and editor with a Git version older than 2.17, which lacks worktree support ([#4363](https://github.com/gitkraken/vscode-gitlens/issues/4363))
- Fixes the _Show Commit Graph_ button in _Source Control_ opening the parent repository's graph for a submodule or nested repository that GitLens hasn't detected yet ([#4566](https://github.com/gitkraken/vscode-gitlens/issues/4566))
- Fixes the _Commit Graph_ details panel continuing to show the previous repository's commit after switching repositories ([#5362](https://github.com/gitkraken/vscode-gitlens/issues/5362))
- Fixes _Commit Graph_ branch and tag pills expanding past the graph's right edge on hover when the _Branches / Tags_ column is last &mdash; the expanded pill now grows leftward when that keeps it inside the graph ([#2667](https://github.com/gitkraken/vscode-gitlens/issues/2667))
- Fixes _Launchpad_ showing "needs reviewers" for GitHub pull requests on repositories that don't require a review ([#5863](https://github.com/gitkraken/vscode-gitlens/issues/5863))
- Fixes the _Commit Graph_ side bar's _Pull Requests_ panel showing GitHub pull requests that are waiting on code owner or team reviews as needing reviewers or ready to merge ([#6206](https://github.com/gitkraken/vscode-gitlens/issues/6206))
- Fixes hard-to-read branch and tag names in the _Commit Graph_ with light themes &mdash; lane-colored names are darkened just enough to stay legible while keeping their lane's hue, and the current branch's pill and marker no longer put white text on a light green ([#4548](https://github.com/gitkraken/vscode-gitlens/issues/4548))
- Fixes faint inline blame annotations in high contrast dark themes ([#2058](https://github.com/gitkraken/vscode-gitlens/issues/2058))
- Fixes _Commit Graph_ ref pills keeping highlights that no longer describe them ([#5764](https://github.com/gitkraken/vscode-gitlens/issues/5764))
  - Stops painting another branch or tag in the current branch's color when the current branch is hidden behind the _+N_ badge
  - Clears a branch, tag, or worktree's find highlight as soon as the query no longer matches it, instead of when the finder closes
- Fixes a remote URL with an `@` in its path being recognized as a repository on a different host &mdash; e.g. `https://example.com/x@github.com/owner/repo.git` as GitHub's `owner/repo` ([#6185](https://github.com/gitkraken/vscode-gitlens/issues/6185))
- Fixes the _Commit Graph_'s branch details offering _Create a Pull Request_ and _Recompose Branch_ for a branch whose work already landed in its merge target ([#6190](https://github.com/gitkraken/vscode-gitlens/issues/6190))
- Fixes the _Commit Graph_ header hiding _Publish Branch_ for a branch whose pull request merged into a branch other than its merge target, such as a stacked parent ([#6191](https://github.com/gitkraken/vscode-gitlens/issues/6191))
- Fixes the _Commit Graph_ header's _Publish Branch_ going stale after the branch's merge target changes, and depending on whether _Working Changes_ was selected ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
  - Shows or hides _Publish Branch_ as soon as _Change Merge Target_ changes whether the branch's work landed, without reopening the _Commit Graph_
  - Hides _Publish Branch_ for a branch that landed by squash or fast-forward merge whichever row is selected, not only while _Working Changes_ is
  - Stops _Publish Branch_ from briefly appearing when a fetch prunes the remote branch of a branch that already landed, or when _Working Changes_ refreshes
- Fixes the _Commit Graph_'s _Overview_ cards not showing that a branch landed, or offering its cleanup, until hovered &mdash; the current branch's card now offers _Delete Branch_ (or _Delete Worktree_) in place of _Publish_, _Push_ and _Pull_ as soon as its work lands, and a branch's merged state on its card or hover updates when its merge target changes or it gets new commits
- Fixes the _Commit Graph_'s branch details, merge target popover and _Working Changes_ disagreeing on whether cleaning up a landed branch deletes the branch or its worktree &mdash; each now names what the action actually deletes
- Fixes the _Commit Graph_'s branch details and _Working Changes_ offering to delete a branch that has new commits since its pull request merged and its remote branch was deleted &mdash; they now lead with _Publish N New Commits_, and _Create a Pull Request_ follows once published ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
- Fixes the merge target popover and the _Commit Graph_'s branch details not saying when a branch's pull request merged into a branch other than its merge target ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
- Fixes deleting a branch that landed by squash, rebase or fast-forward merge giving no reason why it counts as merged &mdash; the delete confirmation, and git's _not fully merged_ prompt, now say where its work landed, including when the branch's worktree is deleted from another window ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
- Fixes the merge target popover offering _Rebase_ and _Merge_ onto the branch's own upstream, which _Pull_ handles, and its compact tooltip saying _Merged_ for a branch that is only likely merged or merged locally ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
- Fixes the merge target status chip having no accessible name or role for screen readers ([#6205](https://github.com/gitkraken/vscode-gitlens/issues/6205))
- Fixes the _Commit Graph_ header, _Overview_ cards and _Working Changes_ offering _Push_ and _Force Push_ for a branch whose pull request is in the merge queue
- Fixes the _Commit Graph_ offering _Force Push_ for a branch whose work already landed in its merge target, where all it could do is overwrite what the remote branch gained since
- Fixes the _Commit Graph_'s _Working Changes_ and branch details briefly offering _Publish_, _Delete Local Branch_, _Push_ or _Create a Pull Request_ while still checking whether the branch landed
- Fixes the _Commit Graph_'s branch details, _Overview_ cards and branch hovers suggesting _Switch to Branch_ for a branch whose work already landed &mdash; its _Overview_ card offers _Delete Branch_ instead
- Fixes the _Inspect_ view not autolinking issues and pull requests in the first commit it shows, and changes to the `gitlens.views.commitDetails.autolinks.enabled` setting not applying to the commit already shown ([#6204](https://github.com/gitkraken/vscode-gitlens/issues/6204))
- Fixes merge, cherry-pick, and revert conflicts &mdash; and _Show conflicts_ in the _Interactive Rebase Editor_ &mdash; opening a _Commit Graph_ that can't show them when it isn't available for the account or repository; the conflict now opens in the _Source Control_ view instead ([#5675](https://github.com/gitkraken/vscode-gitlens/issues/5675))
- Fixes the _Delay Loading File Details_ setting (`gitlens.advanced.commits.delayLoadingFileDetails`) not being editable from the Settings editor &mdash; it now shows a dropdown again ([#5816](https://github.com/gitkraken/vscode-gitlens/issues/5816))
- Fixes errors in blame, views, and remote links when a custom remote's (`gitlens.remotes`) `regex` matches the full remote URL without capturing both the domain and the path &mdash; the entry is now skipped for that remote, and the _Settings_ editor explains that full URL matches need two capture groups ([#4852](https://github.com/gitkraken/vscode-gitlens/issues/4852))
- Fixes _Compare Working Tree to Here_ doing nothing on a commit, stash, or tag in the _Commit Graph_ &mdash; it only worked on branches ([#5352](https://github.com/gitkraken/vscode-gitlens/issues/5352))
- Fixes the _Commit Graph_'s _Changes_ column opt-in prompt squashing its _Show_ button and cutting off its _Hide_ link when the rows area is short &mdash; the prompt now drops its explanation, then the _Hide_ link, rather than clipping them ([#5607](https://github.com/gitkraken/vscode-gitlens/issues/5607))
- Fixes the _Commit Graph_'s hidden branches and tags menu running off the screen when many refs are hidden &mdash; the list now scrolls and _Show All_ stays in reach ([#2925](https://github.com/gitkraken/vscode-gitlens/issues/2925))
- Fixes the _Commit Graph_ button missing from the _Source Control_ view for GitHub repositories opened with _Remote Repositories_ ([#3144](https://github.com/gitkraken/vscode-gitlens/issues/3144))
- Fixes opening and copying remote links for repositories cloned through the SSH hosts for port 443 of Bitbucket (`altssh.bitbucket.org`), GitHub (`ssh.github.com`), and GitLab (`altssh.gitlab.com`) &mdash; Bitbucket and GitHub repositories weren't recognized at all, and GitLab links pointed at the SSH host ([#6174](https://github.com/gitkraken/vscode-gitlens/issues/6174))
- Fixes links to a repository cloned through the SSH hosts for port 443 of Bitbucket (`altssh.bitbucket.org`), GitHub (`ssh.github.com`), and GitLab (`altssh.gitlab.com`) asking to add a new remote when opened in a clone of the same repository that uses the regular address ([#6234](https://github.com/gitkraken/vscode-gitlens/issues/6234))
- Fixes a _Commit Graph_ shortcut override (`gitlens.graph.shortcuts.overrides`) with a misspelled or unknown key name (e.g. `alt+Bogus`) silently replacing a working shortcut with one that can never fire &mdash; the override is now ignored and the default shortcut kept, as with an unknown modifier, and the reason is logged to the _GitLens_ output channel ([#5831](https://github.com/gitkraken/vscode-gitlens/issues/5831))
- Fixes _File History_ and the _Commit Graph_ erroring or skipping a commit whose message or author name contains an ASCII record (0x1E) or group (0x1D) separator character &mdash; also fixes tags and stashes with these characters in their messages, _Line History_ treating a commit as changing nothing when its history read was cut short, and a commit's changed files going missing when its diff contains these characters ([#5659](https://github.com/gitkraken/vscode-gitlens/issues/5659))
- Fixes _Copy Remote File URL_ and _Open File on Remote_ linking to a backwards line range (e.g. `#L3-L2` instead of `#L3`) when the cursor is at the start of a line with nothing selected ([#6186](https://github.com/gitkraken/vscode-gitlens/issues/6186))
- Fixes _Copy Link to Code_ including an extra line when the selection ends at the start of a line (e.g. `lines=2-5` instead of `lines=2-4`) ([#6278](https://github.com/gitkraken/vscode-gitlens/issues/6278))
- Fixes Jira and Linear autolinks not picking up projects or teams added or removed on the tracker for as long as you keep viewing commits, and up to an hour after ([#6183](https://github.com/gitkraken/vscode-gitlens/issues/6183))
- Fixes _Commit Graph_ branch pills sometimes never getting their pull request badge or upstream status after the graph opens ([#6281](https://github.com/gitkraken/vscode-gitlens/issues/6281))
- Fixes the _Search Commits_ results location (`gitlens.gitCommands.search.showResultsInSideBar`) and _GitKraken CLI Insiders_ (`gitlens.gitkraken.cli.insiders.enabled`) settings not being editable from the Settings editor &mdash; they now show dropdowns again ([#6235](https://github.com/gitkraken/vscode-gitlens/issues/6235))
- Fixes GitLens briefly locking the Git index (`index.lock`) in the background when files are touched without changing, such as by a formatter, which could make your own `git add` or commit fail at the same moment (Git 2.46 or later)
- Fixes file changes going undetected, leaving views, the _Commit Graph_ and _Inspect_ stale, for a repository or worktree inside a folder whose name ends in `.git` (such as worktrees kept inside a bare repository) or inside a `node_modules` folder
- Fixes the _Branches_ and _Worktrees_ views showing a branch as still checked out in a worktree after that worktree switched branches outside of GitLens
- Fixes commit lists, _File History_, contributors, and the _Commit Graph_ sometimes showing cut-short results with nothing more to load after a Git read was cancelled partway through
- Fixes _Create Patch_, _Copy as Patch_, cloud patches, stashing selected files, copying changes to a worktree, and AI commit messages and explanations getting wrong or empty changes when Git is configured with an external diff tool (`diff.external`), `diff.noprefix` or custom diff prefixes, `diff.suppressBlankEmpty`, or `diff.submodule=log`
- Fixes commit details never loading, and commit lists stalling for minutes, for a commit that moves and edits thousands of files &mdash; GitLens now falls back to Git's default rename limit for that read
- Fixes a page of commits coming back empty when one of its commits changes an unusually large number of files
- Fixes Git commands on Windows not stopping when they time out or are cancelled, such as a fetch from a remote that never responds
- Fixes unexpected credential prompts, and waits of up to a minute, when looking up a remote's default branch for a repository missing `refs/remotes/<remote>/HEAD` &mdash; the lookup no longer prompts, each network request times out after 10 seconds, and GitLens waits up to a minute after a failure before trying again
- Fixes incorrect or missing file names in commit and stash file lists, diffs, blame, and _File History_, including names with quotes or tabs
- Fixes a commit's pull request going missing from hovers, _Inspect_ and other views after a single failed lookup &mdash; a server error, network failure, or rate limit was remembered as the commit having no pull request until reload; failed lookups are now retried with a back-off, and _Open Pull Request on Remote_ reports a failed lookup instead of saying the commit has no pull request
  - Fixes GitHub pull requests not being found for a commit when the remote's owner is spelled in a different letter case than on GitHub
  - Fixes Bitbucket Cloud never showing its notice about the missing commit links app
  - Fixes a failed GitLab project lookup hiding that repository's merge requests, metadata, and issues

---

<a id="v19-6"></a>

## Version 19.6

#### Tuesday, November 10, 2026

GitLens 19.6 turns _Review Changes_ in the _Commit Graph_ into a review you work through: a checklist of files that remembers what you've seen, comment threads in the diff, and AI that can help when you want it. Pull requests in a GitHub merge queue now show as queued, with the actions to add or remove them. Branches whose work has already landed now offer to clean up instead of nudging you to publish or rebase. You can also install Kepler without leaving GitLens, and the rest of the release fixes a long list of theme, accessibility, AI and integration issues.

<img src="/wp-content/uploads/gl-19-6-hero.png" class="help-center-img img-bordered">

### Review Sessions in Review Changes

Until now, _Review Changes_ in the _Commit Graph_ meant asking AI for a report. In 19.6 a review is something you work through yourself, with or without AI.

**A checklist of what's changed** &mdash; the review lists the changed files and tracks which ones you've viewed. If a file changes after you've viewed it, it comes back onto the list. The scope picker also has one-click presets to review your _Uncommitted_ changes, everything _Unpushed_, or the whole _Branch_.

**Read through the diff** &mdash; reading controls in the diff editor step through the files you haven't viewed yet. <kbd>Alt</kbd>+click steps through them in list order.

**Comment threads** &mdash; AI findings and your own comments show as threads in the diff. Reply to them, dismiss them, or hand them to your agent.

**AI when you want it** &mdash; _Orient_ has AI plan the order to read the files in, and _Review Diff_ looks for issues in the diff. _Review in Repo_ hands the changes to your CLI agent, which can build, test, and trace call paths in your repository, and streams what it finds back into the review.

A review also survives your history edits. When you amend or rebase commits in its scope, your viewed marks, findings, and comments move to the rewritten commits, and an open diff switches to the new changes in place.

### GitHub Merge Queue Support

For repositories that use a GitHub merge queue, a pull request waiting in the queue now shows as queued instead of open, and _Merge_ adds it to the queue when its base branch merges only through one.

- Hovers, views, autolinks, _Launchpad_, and the _Commit Graph_ show a queued pull request's place in the queue, its status, and its estimated merge time. If the queue removes it, GitLens tells you and why.
- _Add to Merge Queue_ and _Remove from Merge Queue_ are available in _Launchpad_ and the _Commit Graph_.
- _Launchpad_ has a new _In Merge Queue_ group. Pull requests failing in the queue, or just removed from it by a failed run, show under _Blocked_.
- While a pull request is queued, the _Commit Graph_ and _Launchpad_ hold back _Merge_, _Rebase Stack_, and next steps that would change its branch, since the queue owns it until it merges or leaves.

### Clean Up Branches That Have Landed

When a branch's pull request has been merged, or Git shows its work is already in the merge target, the merge target status, the _Commit Graph_'s branch details, and the working changes next steps now lead with deleting the branch instead of offering _Publish_, _Rebase_, _Merge_, or _Create Pull Request_.

GitLens recognizes a merged pull request even after its branch was deleted on the remote, and only pre-selects _Force Delete_ when a merged pull request proves the work landed. If you've added commits since the pull request merged, the branch shows them as new, with an option to open a pull request for them. Along the way, we fixed _Delete Branch_ doing nothing when clicked from these places, and a fast-forward merged branch showing as behind its merge target.

### Install Kepler from GitLens

_Install Kepler_ downloads, verifies, and installs the latest Kepler for you, with no admin rights needed. You'll find it in the _Try Kepler_ banners in _GitLens Settings_ and the _Commit Graph_'s _Agents_ sidebar, in the _Welcome_ walkthrough, and as the _GitLens: Install Kepler_ command. If you start a task or review in Kepler before it's installed, GitLens now offers to install it and then carries on with what you started. Once it's installed, _Open Session in Kepler_ jumps from an agent session in the _Commit Graph_ straight to it.

### Also New

- **Notifications** &mdash; a bell in the _Commit Graph_ header shows GitKraken notifications about your account and organization, and _GitLens Settings_ has a new _Notifications_ section to manage them. Only new security and system notices pop up.
- **Asana** &mdash; connect your Asana account from _GitLens Home_ to see the tasks associated with your branches on the _Commit Graph_.
- **Jira Data Center autolinks** &mdash; issue keys in commit messages and branch names now link to your connected Jira Data Center instance.
- **Azure DevOps pull requests** now show in the _Commit Graph_'s _Pull Requests_ panel.
- **New AI models** &mdash; including Claude Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5, GPT-6.1, Gemini 4 Argon, and Grok 4.7. Claude Haiku 5.5 and DeepSeek Flash are now the recommended models.

### Everyday Improvements

- The _Commit Graph_ no longer takes keyboard focus from an editor or the terminal when an editor beside it opens or is focused.
- GitLens webviews and the _Commit Graph_ follow your theme more closely, with many fixes for high contrast and light themes.
- Screen readers now announce popover panels as dialogs you can Tab into, and announce what a copy button did.
- AI conflict resolution stops and explains why when Copilot hits a usage limit or AI becomes unavailable, instead of trying every remaining file.
- Prompts sent to the Claude Code extension right after a window opens no longer fail, and orphaned Claude Code processes no longer pile up on Windows.
- Azure DevOps Server works with a personal access token limited to one collection, and several GitLab subgroup issues are fixed across checkout, _Launchpad_ search, autolinks, and _Cloud Workspaces_.
- Deep links, cloud patches, and _Code Suggestions_ now work in github.dev and vscode.dev.

---

### Added

- Adds review sessions to the _Commit Graph_'s _Review Changes_ mode &mdash; a review is now something you work through, with or without AI, rather than a one-off AI report
  - Adds a checklist of the changed files that tracks what you've viewed and brings back any file that changes afterward
  - Adds reading controls to the diff editor that step through the review's files not yet viewed (<kbd>Alt</kbd>+click steps in list order)
  - Adds comment threads in the diff for AI findings and your own comments &mdash; reply to them, dismiss them, or hand them to your agent
  - Adds _Orient_ beside _Review Diff_ &mdash; _Orient_ has AI plan the order to read the files in, while _Review Diff_ finds issues in the diff
  - Adds _Review in Repo_ &mdash; hands the changes to your CLI agent, which can build, test and trace call paths in the repository and streams its findings back into the review
  - Adds _Uncommitted_, _Unpushed_ and _Branch_ presets to the review's scope picker &mdash; one click to review your uncommitted changes, those plus the commits not pushed yet, or the whole branch
  - Keeps a review going when you amend or rebase &mdash; its viewed marks, findings and comments move to the rewritten commits, and an open diff switches to the new changes in place
- Adds GitHub merge queue support &mdash; a pull request waiting in a merge queue shows as queued instead of open, and _Merge_ adds it to the queue when its base branch merges only through one ([#5991](https://github.com/gitkraken/vscode-gitlens/issues/5991))
  - Shows a queued pull request's place in the queue, its status, and its estimated merge time in hovers, views, autolinks, _Launchpad_, and the _Commit Graph_ &mdash; and when the queue removes one, says so and why
  - Adds _Add to Merge Queue_ and _Remove from Merge Queue_ to _Launchpad_ and the _Commit Graph_ &mdash; a queued pull request can also be removed from the "already in the merge queue" notification
  - Adds an _In Merge Queue_ group to _Launchpad_ &mdash; pull requests failing in the queue, or just removed from it by a failed run, show under _Blocked_
  - Rechecks a queued pull request while the _Commit Graph_ shows it, so the Graph catches up when the queue merges or removes it
  - Holds back _Merge_, _Rebase Stack_, and branch-changing next steps (push, rebase or merge with the merge target, recompose) in the _Commit Graph_ and _Launchpad_ while a pull request is queued &mdash; the queue owns its branch until it merges or leaves
  - Adds a `gitlens.queuedPullRequestIconColor` theme color for queued pull requests
- Adds cleanup actions for branches whose work has already landed ([#3896](https://github.com/gitkraken/vscode-gitlens/issues/3896)) &mdash; when a branch's pull request was merged, or Git shows its work is in the merge target, the merge target status, the _Commit Graph_'s branch details, overview and working changes next steps lead with deleting the branch instead of offering _Publish_, _Rebase_, _Merge_ or _Create Pull Request_
  - Recognizes a merged pull request even after its branch was deleted on the remote, and pre-selects _Force Delete_ only when a merged pull request proves the work landed
  - Shows a branch with commits after its merged pull request as having new commits since, with an option to create a pull request for them
  - Leads with _Delete Local Branch_, with _Publish_ as the fallback, for a branch that is missing from the remote and hasn't landed
- Adds installing Kepler right from GitLens, with no admin rights needed &mdash; _Install Kepler_ downloads and verifies the latest Kepler and installs it for you, showing its progress
  - Adds _Install Kepler_ and _Learn More_ to the _Try Kepler_ banners in _GitLens Settings_ and the _Commit Graph_'s _Agents_ sidebar, and to the Kepler step of the _Welcome_ view walkthrough; adds a _GitLens: Install Kepler_ command
  - Replaces the "Kepler isn't installed" warning with a picker that offers to install Kepler and then carries on with what you started &mdash; or, for a pull request review, to continue without Kepler; in _Start Work_ and _Start PR Review_ it's the next step, so you can go back
  - Opens the Kepler download page instead in remote windows (Remote - SSH, WSL, Dev Containers), since Kepler runs on your own machine
- Adds _Open Session in Kepler_ to agent sessions in the _Commit Graph_ &mdash; from the _Agents_ sidebar, session cards, the agent status pill, or a session's context menu (when Kepler is installed)
- Adds GitKraken notifications about your account and organization
  - Adds a notifications bell with an unread badge to the _Commit Graph_ header &mdash; shows your newest notifications with quick actions to follow their links and mark them read
  - Adds a _Notifications_ section to _GitLens Settings_ &mdash; filter by all, unread, or read, mark notifications read or unread, delete them, and follow their links
  - Pops up only new security and system notices, and never while notifications are open
- Adds Asana as an issue integration &mdash; connect your Asana account from _GitLens Home_ to see the Asana tasks associated with your branches on the _Commit Graph_
- Adds autolinks for _Jira Data Center_ projects &mdash; issue keys in commit messages and branch names now link to issues on your connected Jira Data Center instance ([#6015](https://github.com/gitkraken/vscode-gitlens/issues/6015))
- Adds Azure DevOps and Azure DevOps Server pull requests to the _Commit Graph_'s _Pull Requests_ panel, which previously said it couldn't list them
- Adds support for the latest AI models &mdash; Claude Fable 5.2 and 5.1, Opus 5.5, Sonnet 5.5, and Haiku 5.5, GPT-6.1 (Sol and Terra) and GPT-6 (Astra, Sol, and Luna), Gemini 4 Argon and Gemini 3.8 Flash, Grok 4.7, DeepSeek Flash, Mistral Large 4, and GLM 5.3 Flash

### Changed

- Changes GitLens webviews and the _Commit Graph_ to follow your theme more closely &mdash; banner text, the Graph's search box and amend button, autocomplete dropdowns, and info, success and warning marks now use your theme's colors instead of fixed ones ([#5400](https://github.com/gitkraken/vscode-gitlens/issues/5400))
- Improves starting a task or review in Kepler when using Remote - SSH or WSL &mdash; Kepler now opens on the machine you're working on, so the task lands in the Kepler window connected to it ([#5760](https://github.com/gitkraken/vscode-gitlens/issues/5760))
- Changes the Pro feature gates, badges, and upgrade prompts to offer _Upgrade to Pro_ alongside _Reactivate Pro Trial_, so an account the server won't reactivate still has a path to Pro ([#6010](https://github.com/gitkraken/vscode-gitlens/issues/6010))
- Changes the recommended AI models to Claude Haiku 5.5 and DeepSeek Flash, hides older model generations from the model picker, and removes models their providers have retired

### Fixed

- Fixes the _Commit Graph_ taking keyboard focus from an editor or the terminal whenever an editor beside it opens or is focused &mdash; what was typed went into the graph instead
- Fixes the _Commit Graph_'s _Review Changes_ and _Compose_ modes holding on to the old commits after commits in their scope are amended or rebased &mdash; the scope now moves to the rewritten commits as one unbroken range, and keeps up with new commits on top when it reaches the branch tip or working changes
- Fixes review findings in the _Commit Graph_'s _Review Changes_ mode pointing at the wrong lines &mdash; when a review spans staged changes or several commits, or after a hunk line starting with `-- ` or `++ ` (such as a SQL or Lua comment); a finding now opens on the line it quotes, or on the file alone when that line is gone
- Fixes focus-area reviews in _Review Changes_ ignoring the review's instructions, not stopping when the review is cancelled or its findings deleted, and opening a finding's file without its line range
- Fixes the commit stats tooltip in the _Commit Graph_'s scope picker counting changed lines as files
- Fixes _Delete Branch_ in the merge target status, the _Commit Graph_'s branch details and its working changes next steps doing nothing when clicked &mdash; it now opens the delete confirmation, and deleting the current branch switches to its merge target first, or explains why it can't when there is no other branch to switch to
- Fixes the merge target status reporting a branch whose work was fast-forward merged as behind its merge target, with _Rebase_ and _Merge_ actions &mdash; it is shown as merged again, with an option to delete it, while a newly created branch with no commits of its own still shows as up to date or behind
- Fixes _Change Merge Target_ suggesting a different branch than the views and _Commit Graph_ measure against &mdash; it now pre-selects the same merge target, including one taken from the branch's pull request
- Fixes a branch's commits disappearing from its details and ahead counts after its base branch was reset off them (e.g. a fast-forwarded pull request undone on `main`)
- Fixes _Fetch_ on a remote branch in the _Commit Graph_ running `git fetch <remote> <remote>` and failing &mdash; it now fetches the branch itself ([#4950](https://github.com/gitkraken/vscode-gitlens/issues/4950))
- Fixes the interactive rebase editor reporting _No Conflicts Detected_ for a rebase that conflicts on Git versions before 2.45 &mdash; when it can't check, it now says so (conflict detection requires Git 2.45 or later)
- Fixes the interactive rebase editor cutting off the last commits when the conflict panel is open in a short pane
- Fixes _Review with Agent_ and other prompts sent to the Claude Code extension failing with "Agent 'Claude Code Extension' is no longer available" when sent right after a window opens, before the extension has started &mdash; GitLens now starts it and sends the prompt ([#6140](https://github.com/gitkraken/vscode-gitlens/issues/6140))
- Fixes orphaned `claude.exe agents --json` processes piling up on Windows when Claude Code is installed via npm &mdash; a timed-out check now ends the whole process tree ([#6146](https://github.com/gitkraken/vscode-gitlens/issues/6146))
- Fixes the agent picker showing "$(warning)" as text in its _No agents available_ header
- Fixes AI conflict resolution with Copilot starting every remaining file after hitting Copilot's usage or rate limit, or when the selected model is no longer available &mdash; it now stops and says why, naming Copilot's own limit or offering to switch models ([#6118](https://github.com/gitkraken/vscode-gitlens/issues/6118), [#6145](https://github.com/gitkraken/vscode-gitlens/issues/6145))
- Fixes AI conflict resolution sending a request for every remaining file after AI becomes unavailable (e.g. the weekly AI allowance runs out or the provider rejects its API key) &mdash; it now stops and shows one message explaining why, and the _Commit Graph_'s _Resolve_ mode chooses the AI model once per run
- Fixes _Retry_ and _Refine_ in the _Commit Graph_'s _Resolve_ mode dropping _Apply & Resume with AI_ while an automatic rebase is still paused
- Fixes AI errors saying "You have exceeded your user token limit" when the weekly AI allowance runs out &mdash; they now say you've reached the weekly AI usage included in your plan
- Fixes the Mistral provider offering GLM 5.2, which Mistral has retired &mdash; replaces it with GLM 5.3 and removes other retired Mistral models ([#6117](https://github.com/gitkraken/vscode-gitlens/issues/6117))
- Fixes _Explain_ inputs still showing in the _Commit Graph_ and _Inspect_ view when `gitlens.ai.enabled` is `false` ([#6121](https://github.com/gitkraken/vscode-gitlens/issues/6121))
- Fixes natural language commit search sending a second AI request when the first one fails
- Fixes _Generate Commit Message_ and _Compose Commits_ appearing twice in the _Source Control_ title bar &mdash; they now appear only in the GitLens AI (sparkle) menu ([#4396](https://github.com/gitkraken/vscode-gitlens/issues/4396))
- Fixes every Git command failing until the window is reloaded after Git once couldn't be found or started
- Fixes a repository being skipped, or watched through the wrong `.git` folder, when a Git command timed out while GitLens was discovering it
- Fixes a repository's `.git` folder showing up as a second repository named `.git` (e.g. during a rebase) when `core.bare` is unset
- Fixes a tag you create or delete not showing up, or still showing, in a commit's branches and tags in _Inspect_ and the _Commit Graph_
- Fixes _Copy Link to Repository_ and other deep link commands failing with "Buffer is not defined" in github.dev and vscode.dev &mdash; the same error also broke opening or archiving a cloud patch and left a pull request's _Code Suggestions_ empty ([#4772](https://github.com/gitkraken/vscode-gitlens/issues/4772))
- Fixes creating a cloud patch from changes that cancel each other out publishing an empty patch, and crashing a code suggestion &mdash; both now stop with "No changes found"
- Fixes Jira issues losing their project and silently failing to associate with a branch through _Associate Issue with Branch_ or _Start Work_ &mdash; failed associations now show a warning ([#5964](https://github.com/gitkraken/vscode-gitlens/issues/5964))
- Fixes an integration that stopped working after repeated failed requests still showing as connected in _Launchpad_, the _Commit Graph_, and autolinks &mdash; it now shows as disconnected until VS Code restarts
- Fixes reconnecting one self-managed integration (e.g. GitHub Enterprise or GitLab Self-Managed) also disconnecting your other connections of the same kind
- Fixes an _Azure DevOps Server_ connection at the server root rejecting a personal access token limited to one collection, leaving _Launchpad_ and the work item lists empty &mdash; GitLens now finds a collection the token works in, and when none accepts it, the warning says why and what to do ([#6071](https://github.com/gitkraken/vscode-gitlens/issues/6071))
- Fixes checking out a pull request from a fork in a GitLab subgroup naming the new remote after the subgroup's path (e.g. `contrib/team`), which GitLens then misread &mdash; the remote is now named `contrib-team`
- Fixes searching _Launchpad_ by a pasted GitLab merge request URL finding nothing when the repository is in a subgroup
- Fixes _Cloud Workspaces_ matching or adding the wrong GitLab repository when two subgroups hold a repository with the same name
- Fixes GitLab autolinks, file links, and merge requests from a fork pointing at the wrong project for repositories in nested groups (e.g. `acme/platform/kepler`)
- Fixes branch names with a one-digit issue number (e.g. `ABC-1-fix`) not linking their issue through an autolink with an explicit prefix
- Fixes screen readers announcing popover panels with controls, such as the _Commit Graph_'s account and _Launchpad_ panels, as tooltips &mdash; they're now announced as named dialogs you can Tab into
- Fixes screen readers not announcing copy buttons by a stable name or what a copy did &mdash; they now announce "Copied!" or why a copy failed
- Fixes the _Commit Graph_'s scope popover and other tall popovers running past the edge of a narrow or short view
- Fixes theme colors across GitLens webviews and the _Commit Graph_ ([#5400](https://github.com/gitkraken/vscode-gitlens/issues/5400))
  - Fixes buttons, action icons, chips, breadcrumbs and search result navigation showing no hover feedback in high contrast themes, including across the _Commit Graph_ and the icon buttons in _GitLens Settings_
  - Fixes the selected suggestion in autocomplete dropdowns (e.g. the _Commit Graph_ search) being invisible in high contrast themes
  - Fixes error banners having no visible edge in high contrast themes (_Visual File History_, _GitLens Settings_, _Inspect_) or showing red text on a red background in the _Commit Graph_ (e.g. _Git Health_, compare, and the rebase summary)
  - Fixes the _Commit Graph_'s pull banner showing hard-to-read white text in high contrast dark themes and with a light conflict color
  - Fixes hard-to-read warning and danger button text (e.g. _Abort_ in the interactive rebase editor) and green success text in _SSH Allowed Signers_ in light themes
  - Fixes secondary buttons showing a blue outline in the 2026 themes
  - Fixes the interactive rebase editor's commit list borders taking on the scrollbar color when the editor is hovered or focused
  - Fixes the _Commit Graph_'s details pane showing bands of the graph's background color when the Graph is open in an editor, and agent markers showing the side bar color behind them in the side bar or panel
  - Fixes the low confidence marker on AI-resolved conflicts in the _Commit Graph_ not using the theme's warning color
  - Fixes links in the Pro feature badge's popup showing as plain text
  - Fixes radio buttons and the checkboxes in the _Commit Graph_'s popovers ignoring the theme's radio and checkbox border colors
  - Fixes the branch status icon using fixed gray colors instead of following the theme's text color

---

<a id="v19-5"></a>

## Version 19.5

#### Tuesday, October 27, 2026

GitLens 19.5 finishes what 19.4 started for brand-new repositories: getting one online now takes you through a single chooser, checks that a remote is reachable before adding it, and helps you back out when a URL was wrong. Merge targets get smarter about which branch they compare against, a long list of Azure DevOps problems are fixed, from legacy `visualstudio.com` remotes to Team Foundation Server 2018, and the rest of the release makes push, pull, and multi-worktree work faster and more reliable.

<img src="/wp-content/uploads/gl-19-5-hero.png" class="help-center-img img-bordered">

### Getting a New Repository Online

In 19.4, the _Commit Graph_ started offering _Publish Repository_ when a repository has no remotes. In 19.5, _Publish Repository_ in the graph and the views opens the push wizard's chooser with your choice pre-selected, so you can publish to a host VS Code supports or pick _Add Remote…_ for one it doesn't, and continue straight to publishing. Branch and worktree rows in the views and the graph's _Pull Requests_ panel now offer it too, and every menu decides based on that row's own repository rather than the whole workspace.

**_Add Remote_ checks before it adds** &mdash; the confirm step now tests the URL. When it can't be reached, it tells you why and offers _Add Remote Anyway_, _Change URL_, or a retry. On a repository with no remotes, the name defaults to `origin`.

**Recover from a mistyped URL** &mdash; if a push can't reach a remote you've never fetched from, the error now offers _Remove Remote_, and an unreachable HTTPS host is reported as unreachable instead of a generic error. _Add Remote and Fetch_ no longer hangs when the fetch fails; it warns you and offers _Remove Remote_.

### Smarter Merge Targets

The _Commit Graph_'s branch cards show how far a branch is from its merge target. When no target is saved or detected, GitLens now picks one more carefully. It finds the default branch from your local branches first (an `upstream` remote's, then `origin`'s) and only asks the remote when they don't name one. The default branch is measured against its own upstream, and a branch created from another branch is measured against that branch until it's merged.

Merge targets are also more accurate:

- A target whose branch was deleted, such as a stacked pull request's base after it merges, is skipped in favor of the next available one instead of sticking.
- An out-of-date local target no longer counts commits that are already on the remote.
- A branch card's overview and merge target status now agree on the target for a branch that tracks a remote other than `origin`, and the graph's commit scope picker respects saved and pull request targets.
- _Explain Branch_ reports when no base branch was found instead of comparing against the current branch, and _Create Pull Request_ keeps the full name of a target like `release/2.0`.

### Azure DevOps, Old and New

- Repositories cloned with a legacy `https://{org}.visualstudio.com/DefaultCollection/…` remote, or with a remote that names no project, now show pull requests, work items, and commit authors.
- Team Foundation Server 2018 works with the Azure DevOps Server integration. Work item details, pull requests for commits, and team review requests no longer fail on unsupported API versions.
- Work items whose content lives outside _Description_, such as a Bug's _Repro Steps_, now show it.
- Removed work items, and completed ones with no closed date, no longer show as open in _Start Work_, autolinks, or a branch's issues.
- _Launchpad_ now shows your authored and review-requested pull requests, including team review requests, for accounts whose identity differs between organizations.

### Everyday Improvements

- Views and the _Commit Graph_ keep updating during long-running activity, like a long rebase or a build writing into your working tree, instead of waiting until it stops.
- Working across several worktrees of one repository is faster. Staging, or pausing a merge, rebase, or cherry-pick, in one worktree no longer refreshes the others, and switching branches or locking a worktree costs the others far less work.
- Staging, unstaging, discarding, and committing now wait and retry when another Git process briefly holds the index lock, instead of failing with an `index.lock` error.
- File watching follows Git's ignore rules exactly, including nested `.gitignore` files, so build output in ignored folders no longer triggers refreshes.
- Push, pull, and fetch go to the right place when a remote's name contains a slash, when a custom fetch refspec is in use, or when a branch tracks another local branch. _Push to Here…_ now pushes onto the branch's upstream.
- The _Commit Graph_ no longer confuses local and remote branches with similar names, and worktrees using `extensions.worktreeConfig` each use their own identity, signing, and pull settings.
- Terminal links work in multi-repository workspaces.
- Files that were deleted or renamed away and then re-added open correctly, and _Open Blame Prior to this Change_ explains when a file didn't exist yet.
- _Start Work_ continues after you sign in from its account prompt, and Jira issues in a done status show as closed.

### Thank you to our contributors

Shout-out to our awesome contributors for this release!

- yuezichong ([@qianxunslimg](https://github.com/qianxunslimg)) &mdash; terminal links in multi-repository workspaces
- Andrés Martínez ([@amartinez1224](https://github.com/amartinez1224)) &mdash; opening files that were deleted or renamed away and re-added

---

### Added

- Adds a reachability check to _Add Remote_ &mdash; the confirm step probes the URL and, when it can't be reached, says why and offers _Add Remote Anyway_, _Change URL_, or a retry; the name defaults to `origin` on a repository with no remotes
- Adds _Publish Repository_ to branch and worktree rows in the views when their repository has no remotes
- Adds _Remove Remote_ to the error shown when a push can't reach a remote that has never been fetched from (e.g. one just added with a mistyped URL)
- Adds a _Publish Repository…_ call to action to the _Commit Graph_'s _Pull Requests_ panel when the repository has no remotes

### Changed

- Changes _Publish Repository_ in the _Commit Graph_ and views to open the push wizard's chooser (_Publish Repository…_ or _Add Remote…_) with the clicked action pre-selected, rather than handing straight to VS Code's publish flow &mdash; _Add Remote…_ continues into the publish confirm without a fetch step, and a multi-repository push now skips (and names) repositories without remotes instead of failing
- Changes views and the _Commit Graph_ to keep updating during long-running activity, such as a long rebase or a build writing into the working tree, where they used to wait until it stopped
- Changes how a branch's merge target is chosen when none is saved or detected &mdash; the default branch is found from local branches first (an `upstream` remote's, then `origin`'s) and the remote is asked only when they name none, the default branch itself is measured against its own upstream, and a branch created from another branch is measured against it until that branch is merged; the guess for a branch created with `git checkout -b` is no longer saved
- Improves performance when working across several worktrees of one repository &mdash; staging changes, or a merge, rebase or cherry-pick pausing, in one worktree no longer refreshes the views and _Commit Graph_ state of every other worktree, switching branches in one worktree refreshes the others once instead of twice, and locking or unlocking a worktree no longer discards the others' cached Git data
- Changes _Push to Here…_ to push onto the branch's upstream rather than a remote branch named like the local one &mdash; they differ when, e.g., local `foo` tracks `origin/bar`
- Improves staging, unstaging, discarding, and committing when another Git process (VS Code's Git extension, a terminal, an AI agent) briefly holds the index lock &mdash; GitLens now waits and retries instead of failing with an `index.lock` error
- Improves how views and the _Commit Graph_ follow Git's ignore rules when watching for file changes &mdash; changes in folders ignored by a nested `.gitignore` (such as a package's `dist/`) no longer trigger refreshes, and `info/exclude` in linked worktrees, a `~/` path in `core.excludesFile`, the global `~/.config/git/ignore` file, and `core.ignorecase` are now respected

### Fixed

- Fixes a push to an unreachable HTTPS remote (e.g. a mistyped host) reporting a generic error rather than that the remote could not be reached
- Fixes the views and the _Commit Graph_'s context menus choosing between _Publish Branch_ and _Publish Repository_ by whether any repository in the workspace has remotes &mdash; each row now follows its own repository, and a remote without a recognized host no longer counts as no remote
- Fixes _Add Remote and Fetch_ hanging (or closing silently) when the fetch failed, leaving the remote behind &mdash; it now warns and offers _Remove Remote_
- Fixes pressing Enter on an invalid value in a wizard input (a remote URL, a branch name) navigating away &mdash; the field now stays open with the message until the value is valid
- Fixes _Don't Ask Again_ appearing on push confirmations it cannot skip &mdash; the no-remotes chooser, the publish step, and the behind-upstream guard
- Fixes GitLens terminal links (commits, branches, tags, ranges, and git commands) not working in multi-repository workspaces &mdash; links now use the repository containing the terminal's working directory, when shell integration reports it ([#5986](https://github.com/gitkraken/vscode-gitlens/issues/5986)) &mdash; thanks to [PR #5196](https://github.com/gitkraken/vscode-gitlens/pull/5196) by yuezichong ([@qianxunslimg](https://github.com/qianxunslimg))
- Fixes opening the changes of a file that was deleted (or renamed away) and re-added failing with "file not found" &mdash; the comparison now shows an empty previous version ([#5914](https://github.com/gitkraken/vscode-gitlens/issues/5914)) &mdash; thanks to [PR #5930](https://github.com/gitkraken/vscode-gitlens/pull/5930) by Andrés Martínez ([@amartinez1224](https://github.com/amartinez1224))
- Fixes _Open Blame Prior to this Change_ on a line whose change added the file (including a file that was deleted or renamed away and re-added) opening an empty file picker or a blank document &mdash; it now says the file didn't exist before that change ([#5914](https://github.com/gitkraken/vscode-gitlens/issues/5914))
- Fixes Azure DevOps work items whose type keeps its content outside Description, such as a Bug's Repro Steps or a custom field on an inherited process, showing no description ([#6047](https://github.com/gitkraken/vscode-gitlens/issues/6047))
- Fixes Removed Azure DevOps work items, and completed ones with no closed date, showing as open in _Start Work_'s issue list, autolinks, and a branch's associated issues ([#6013](https://github.com/gitkraken/vscode-gitlens/issues/6013), [#6041](https://github.com/gitkraken/vscode-gitlens/issues/6041))
- Fixes the Azure DevOps Server integration on Team Foundation Server 2018 &mdash; work item details on autolinks, pull requests for commits, pull request details, and team review requests no longer fail on unsupported REST API versions ([#6048](https://github.com/gitkraken/vscode-gitlens/issues/6048))
- Fixes Azure DevOps repositories cloned with a legacy `https://{org}.visualstudio.com/DefaultCollection/…` remote never showing pull requests, work items or commit authors, and filling the log with `Invalid Azure repository descriptor` errors ([#5999](https://github.com/gitkraken/vscode-gitlens/issues/5999)) &mdash; also fixes remotes that name no project (`…/DefaultCollection/_git/{repo}`, `{org}.visualstudio.com/_git/{repo}` and `dev.azure.com/{org}/_git/{repo}`), whose project is named after the repository
- Fixes Azure DevOps repositories named after their project and cloned without the project segment (`…/{collection}/_git/{repo}`, as TFS 2018 offers them) never showing pull requests or commit authors ([#6000](https://github.com/gitkraken/vscode-gitlens/issues/6000))
- Fixes Azure DevOps showing no authored or review-requested pull requests in _Launchpad_, including those requested of the user's teams, for accounts whose profile id differs from their identity in an organization; _Launchpad_ also categorizes those pull requests as the user's ([#6032](https://github.com/gitkraken/vscode-gitlens/issues/6032))
- Fixes Jira issues in a done status with no resolution set showing as open in autolinks, hovers, and a branch's associated issues
- Fixes a branch's merge target staying stuck on a deleted branch, such as a stacked pull request's base after it merges and is pruned &mdash; a saved, detected, or pull request merge target whose branch no longer exists locally is now skipped in favor of the next available one
- Fixes a branch's merge target counting commits that are already on the remote when the target is an out-of-date local branch &mdash; a merge target is now measured against the local branch or its upstream, whichever the branch split off from more recently
- Fixes the merge target status being hidden when a branch's target is a local branch whose name ends with the branch's own name, such as `release/main` for `main`, and both are at the same commit
- Fixes _Commit Graph_ branch cards measuring the overview and the merge target status against different targets for a branch that tracks a remote other than `origin`
- Fixes the _Commit Graph_'s commit scope picker ignoring a branch's saved or pull request merge target
- Fixes _Explain Branch_ comparing against the current branch, instead of reporting that no base branch was found, for a branch with no merge target
- Fixes _Create Pull Request_ cutting a local merge target's name at its first slash when choosing the pull request's base &mdash; `release/2.0` became `2.0`
- Fixes a branch's base never being found from where it was created when Git's `grep.patternType` is set to `fixed`
- Fixes push, pull, and fetch going to the wrong remote or branch when a remote's name contains a slash (e.g. `team/fork`), when a custom fetch refspec stores a remote's branches under another name, or when a remote is named `remotes`
- Fixes a branch that tracks another local branch being treated as tracking a remote of that name &mdash; fetch and pull no longer target a nonexistent remote, _Publish Branch_ no longer publishes it under the local branch's name, and pushing a branch whose remote was removed now says it has no upstream instead of pushing somewhere unexpected
- Fixes the _Commit Graph_ mixing up local and remote branches with similar names &mdash; a local `team/fork/work` beside a remote `team/fork` no longer shows as a remote branch, a local and a remote branch with the same short name no longer merge into one (losing the current-branch and worktree markers), and refs such as `refs/pull/*` no longer show as local branches
- Fixes worktrees that use `extensions.worktreeConfig` sharing one worktree's Git config &mdash; each worktree now uses its own user identity, commit signing, and pull/rebase settings
- Fixes _Start Work_ not carrying on after signing in from its account gate &mdash; the flow now continues, and _Start Work_, _Start Review_, and _Launchpad_ no longer offer to connect an integration your account already has ([#5988](https://github.com/gitkraken/vscode-gitlens/issues/5988))
- Fixes _Reactivate Pro Trial_ occasionally being offered again after the server refused it ([#6008](https://github.com/gitkraken/vscode-gitlens/issues/6008))

---

<a id="v19-4"></a>

## Version 19.4

#### Thursday, October 15, 2026

As of GitLens 19.4, the _Commit Graph_ no longer requires an account on public and local repositories. Install GitLens, open the graph, and it's all there, with no sign-in prompts.

In 19.0, we made the _Commit Graph_ the home of GitLens and built in new capabilities to help you stay in control of your development workflows. Along with that change, we started requiring a GitKraken account to use it, even on public and local repositories. That got in the way of the very thing we were trying to put front and center, so we've taken it out. Thank you to everyone who told us in issues, discussions, and reviews.

On privately hosted repositories, the _Commit Graph_ is still part of GitLens Pro, but you can try it first. The first time you open it on a private repository, a 3-day preview starts on its own, with no account needed.

If you haven't explored the new _Commit Graph_, now's a good time to come back and explore how GitLens and the _Commit Graph_ can supercharge your Git workflow.

Beyond the graph, _Start Work_ can now name branches the way your team does, with a format built from the issue's ID and title and a live preview in _GitLens Settings_. A brand new repository can also go from your machine to a host without leaving the graph: when there are no remotes, the graph offers _Publish Repository_, with _Add Remote_ beside it. The rest of the release tightens safety and correctness. A pull you started can no longer be undercut by the graph's auto-fetch, worktree deletes warn you when GitLens can't check for changes, and _Start Work_ and _Launchpad_ now read from every self-managed host you've connected instead of just one.

<img src="/wp-content/uploads/gl-19-4-hero.png" class="help-center-img img-bordered">

### The Commit Graph, No Account Required

**Previewing on private repositories** &mdash; while the preview runs, a notice above the graph shows how much time is left, offers _Sign In_, and reminds you that public and local repositories stay free. The sign-in screen only appears once the preview ends, and if your workspace also has public or local repositories, it offers to switch to one of them. The preview used to be three separate one-day sessions, each started by hand with _Continue Preview_. It's now one continuous 3-day window, so you can use the graph over a few working days without having to restart it.

**Signed-out states that make sense** &mdash; the account panel in _GitLens Settings_ now shows a sign-in card and a _Sign in to use GitKraken AI_ line instead of blank cards, and its footer offers _Sign in_ instead of a _Manage subscription_ link. _Start Work_ and _Start Review_ now ask you to sign in up front, instead of signing you in silently when you connect an integration.

### Name Your Start Work Branches

_Start Work_ creates a branch for the issue you pick, and until now you got whatever name it chose. The new `gitlens.startWork.branchNameFormat` setting lets you decide. Use `${id}` for the issue ID and `${title}` for a lowercase, slugged version of its title, so `feature/${id}-${title}` or `${id}` alone both work. The default is `${id}-${title}`.

You'll find it under _Integrations > Start Work_ in _GitLens Settings_, with an editor that shows a live preview of the branch name as you type. Characters Git doesn't allow in branch names are normalized for you, `/` keeps your branch hierarchy, and you can still edit the suggested name before the branch is created.

<img src="/wp-content/uploads/gl-19-4-branch-name-format.png" class="help-center-img img-bordered">

### Publish a Repository from the Commit Graph

Run `git init`, commit some work, and the graph used to offer _Publish Branch_, which could only fail because there was nowhere to publish to. Now, when a repository has no remotes, the graph header, _Working Changes_ panel, overview, and branch details offer **_Publish Repository_**. It uses VS Code's publish flow to create the hosted repository and push your work in one step.

The _Git Command Palette_'s _Push_ offers the same option when there are no remotes. If your host isn't one VS Code can publish to, **_Add Remote_** appears beside _Publish Repository_ in the push wizard and in the _Working Changes_ next steps. _Fetch_ is hidden until the repository has a remote to fetch from.

<img src="/wp-content/uploads/gl-19-4-publish-repository.png" class="help-center-img img-bordered">

### Everyday Improvements

- If you've connected more than one host for the same self-managed provider, _Start Work_ and _Launchpad_ now read from all of them instead of only one. _Launchpad_ also keeps pins, snoozes, and selections separate between hosts, even when their pull requests share an ID.
- Self-managed integrations, including Azure DevOps Server behind a virtual directory, now keep the installation path in their API requests. Azure DevOps names and branches with spaces or reserved characters are encoded correctly.
- A new `gitlens.views.searchAndCompare.files.openDiffOnClick` setting chooses whether clicking a file in the _Search & Compare_ view opens its changes or the working file. Thanks to Steven Vaught ([@Svaught598](https://github.com/Svaught598)) and Ehab Younes ([@EhabY](https://github.com/EhabY)) for their contributions.
- The _Commit Graph_'s auto-fetch no longer replaces `FETCH_HEAD` while a `git pull` you started is between its fetch and its merge, which could have made the pull merge the wrong changes.
- Force-deleting a worktree now asks first when GitLens couldn't check it for uncommitted changes. GitLens also no longer treats a failed check for changes as "no changes" in _Auto-Rebase_, patch apply, and _Copy Changes_.
- Opening a renamed or added file from a comparison or a commit's file list now uses the file's path at that revision, and the _Ahead_ files node no longer shows a rename as an added file.
- Cloning a large repository from a GitLens link no longer fails when it runs past the Git timeout. The clone runs as long as it needs, and you can cancel it from its progress notification.
- Choosing _Open in an agent_ from _Start Work_, _Start Review_, or _Launchpad_ no longer freezes when agent detection stalls. The picker opens right away while agents load.
- _Start Work_ and _Launchpad_ now say when GitHub's API rate limit is reached and when to try again, instead of showing a raw `GraphqlResponseError`.
- Repositories with no commits yet now show their staged and modified files, and diffs against the first commit work in SHA-256 repositories.

---

### Added

- Adds _Publish Repository_ to the _Commit Graph_ for a repository with no remotes &mdash; the header, _Working Changes_ panel, overview, and branch details now offer to create a hosted repository (through VS Code's publish flow) instead of a _Publish Branch_ that could only report "No remotes found"; the _Git Command Palette_'s _Push_ offers the same escape when there are no remotes
  - Offers _Add Remote…_ beside _Publish Repository…_ in the push wizard and the _Working Changes_ next steps, for hosts VS Code can't publish to, and hides _Fetch_ while the repository has no remotes
- Adds configurable branch names for _Start Work_ with `gitlens.startWork.branchNameFormat`, using `${id}` and `${title}` tokens, plus a format editor and live preview in GitLens Settings ([#5925](https://github.com/gitkraken/vscode-gitlens/issues/5925))
- Adds connecting a self-hosted _Jira Data Center_ (or Jira Server) instance from the integrations in _GitLens Settings_ ([#5864](https://github.com/gitkraken/vscode-gitlens/issues/5864)) &mdash; it connects through your GitKraken account like the other self-hosted integrations, with each configured host as its own connection. For now, a connected instance is used only to show the issues associated with a branch; _Start Work_, autolinks, and the _Commit Graph_'s issue tracker picker don't support it yet
  - The _Commit Graph_'s check for whether any issue integration is connected now looks at every configured host of a self-hosted tracker, so disconnecting one host no longer turns off issue enrichment while another is still connected
  - Reads a branch's associated _Jira Data Center_ issues from the instance the association names, never from another configured host that happens to be primary ([#5872](https://github.com/gitkraken/vscode-gitlens/issues/5872))
- Adds a `gitlens.views.searchAndCompare.files.openDiffOnClick` setting to specify whether to open the changes or the working file when clicking a file in the _Search & Compare_ view ([#1651](https://github.com/gitkraken/vscode-gitlens/issues/1651)) &mdash; thanks to [PR #2845](https://github.com/gitkraken/vscode-gitlens/pull/2845) by Steven Vaught ([@Svaught598](https://github.com/Svaught598)) and [PR #3583](https://github.com/gitkraken/vscode-gitlens/pull/3583) by Ehab Younes ([@EhabY](https://github.com/EhabY))

### Changed

- Changes the _Commit Graph_ to no longer require an account on public and local repos &mdash; signed-out users get the full graph with no prompts
  - On privately hosted repos, a preview starts automatically on first open, with a persistent notice above the graph showing the time left, a _Sign In_ action, and a reminder that public and local repos stay free; the sign-in screen now appears only after the preview ends (or for unverified accounts)
  - _Start Work_ and _Start Review_ now ask you to sign in up front instead of implicitly signing you in when connecting an integration
  - Account surfaces get real signed-out states &mdash; the _GitLens Settings_ account panel shows a sign-in card and a _Sign in to use GitKraken AI_ line instead of blank cards, and its footer offers _Sign in_ instead of a _Manage subscription_ link that opened gk.dev signed out
  - The merge-target status chip's potential-conflicts check now requires a trial or Pro subscription, like every other conflict check; ahead/behind counts and merged status stay available to everyone
- Changes the _Commit Graph_ preview for privately hosted repos to one continuous 3-day window &mdash; previously three separate one-day sessions, each started manually with _Continue Preview_
- Renames the `gitlens.views.publishRepository` command to `gitlens.publishRepository:views`; the old id still works but is deprecated

### Fixed

- Fixes Pro feature gates and account surfaces still offering _Reactivate Pro Trial_ after the server refused the reactivation &mdash; once refused, they show the _Upgrade to Pro_ messaging instead ([#5987](https://github.com/gitkraken/vscode-gitlens/issues/5987))
- Fixes _Push_ from the _Git Command Palette_ on a branch with no upstream showing a plain push confirmation (which then failed) instead of the publish step
- Fixes pressing <kbd>Space</kbd> on a _Git Command Palette_ confirmation step breaking the command &mdash; e.g. _Delete Worktree_ would stop responding and never delete the worktree
- Fixes force-deleting a worktree skipping the uncommitted-changes warning when GitLens couldn't check the worktree for changes &mdash; it now asks before deleting a worktree it couldn't check
- Fixes a repository or worktree with no commits yet showing no changes when it has staged or modified files
- Fixes features treating a failed check for changes as "no changes": _Auto-Rebase_ could report a commit as skipped for being empty, applying a patch could skip offering to stash your changes, and _Copy Changes_ could leave out untracked files without saying so
- Fixes diffs against a repository's first commit failing in a SHA-256 repository, including a stash's untracked files and, for a range starting at the first commit, the _Commit Graph_'s scope file list and _Compose_
- Fixes cloning a large repository from a GitLens link failing once it runs past the Git timeout (`gitlens.advanced.git.timeout`) &mdash; the clone now runs as long as it needs, and its progress notification can cancel it
- Fixes branch-associated issues from self-managed Git hosts resolving through the wrong server when an older association has no host. These associations remain usable with a single configured host, and new Bitbucket Server issue associations retain their host ([#5883](https://github.com/gitkraken/vscode-gitlens/issues/5883))
- Fixes Azure DevOps requests escaping the configured installation path with specially encoded remote names, and preserves names and branches containing spaces or reserved characters ([#5878](https://github.com/gitkraken/vscode-gitlens/issues/5878))
- Fixes self-managed integrations dropping the installation path from API requests, including Azure DevOps Server virtual directories, while keeping existing connections usable ([#5871](https://github.com/gitkraken/vscode-gitlens/issues/5871))
- Fixes _Start Work_ and _Launchpad_ reads covering only one host per supported self-managed provider ([#5873](https://github.com/gitkraken/vscode-gitlens/issues/5873)) &mdash; connected hosts are read independently, with open repository scopes kept on their matching host
- Fixes _Launchpad_ mixing pins, snoozes, selections, and tree items between self-managed hosts whose pull requests share an identifier ([#5873](https://github.com/gitkraken/vscode-gitlens/issues/5873))
- Fixes _Start Work_ and _Launchpad_ showing a raw `GraphqlResponseError` when GitHub's API rate limit is exhausted &mdash; they now report that the rate limit was reached and when to try again
- Fixes the GitKraken MCP server staying in VS Code's _Configure Tools_ after turning off `gitlens.gitkraken.mcp.autoEnabled` or AI features ([#5961](https://github.com/gitkraken/vscode-gitlens/issues/5961))
- Fixes _Start Work_, _Start Review_, and _Launchpad_ freezing after choosing _Open in an agent_ when agent detection stalls &mdash; the agent picker now opens right away while agents load, and agent detection gives up after 10 seconds instead of hanging, still offering the editor's chat and the _Claude Code_ extension
- Fixes opening a renamed or added file from a comparison or a commit's file list &mdash; _Open File at Revision_, _Open File_, and file history now use the file's path at that revision, and the _Ahead_ files node no longer shows a rename as an added file ([#5975](https://github.com/gitkraken/vscode-gitlens/issues/5975))
- Fixes the _Commit Graph_'s auto-fetch replacing `FETCH_HEAD` while a `git pull` you started is between its fetch and merge, which could make the pull merge the wrong changes

---

<a id="v19-3"></a>

## Version 19.3

#### Thursday, October 1, 2026

GitLens 19.3 connects to Kepler, GitKraken's Agentic Development Environment (ADE). You can start a task on a repository, or a review of a pull request, in Kepler from the GitLens views, _Launchpad_, and the _Commit Graph_. Kepler opens with the repository or pull request ready to go. _Start Work_ and _Start PR Review_ can also send an issue or pull request to Kepler, and if Kepler isn't installed yet, GitLens offers to get it for you.

You can now rebase all of your stacked pull requests in one action. _Rebase Stack..._ replays each layer onto the one below it, from the bottom up, so none get skipped. _Auto-Rebase Stack..._ does the same with AI resolving conflicts the whole way, and pauses for your help instead of unwinding. When the cascade is done, _Force Push Stack_ publishes every rewritten branch, and you can hold back any of them.

Getting started takes fewer detours. With no repository open, the _Commit Graph_ now offers ways to begin: open a folder, clone a repository, or start a new project. _Start Work_ and _Start PR Review_ also work without a repository. They list your issues and pull requests across your connected integrations, then find the repository locally or clone it for you. When a sign-in or upgrade screen interrupts you, it now names the commit, branch, or comparison you were opening, and opens it for you once you have access.

The rest of the release is polish and fixes. GitLens section headers match VS Code's Modern UI. _Hide Remote-only Branches_ in the graph now hides only what it says it does. A set of Azure DevOps link problems are fixed, and autolinked pull requests and issues no longer disappear after a single failed lookup.

<img src="/wp-content/uploads/gl-19-3-hero.png" class="help-center-img img-bordered">

### Start Tasks and Reviews in Kepler

Kepler is GitKraken's Agentic Development Environment (ADE), and GitLens can now hand work to it from wherever you are.

**_Start Task in Kepler_** is available on repositories, and **_Start Review in Kepler_** is available on pull requests. Both appear in GitLens views, _Launchpad_, and the _Commit Graph_. Each one opens Kepler with the repository or pull request already loaded, so you can start working without setting anything up first.

**Kepler in _Start Work_ and _Start PR Review_** &mdash; for items Kepler supports, both flows now offer _Open in Kepler_ alongside opening in an agent or continuing manually. If Kepler is always where you want to go, set `gitlens.ai.openInAgent` to `kepler` and both flows will go straight there.

If Kepler isn't installed, GitLens offers to get it for you. Once it's installed, the _Try Kepler_ banner stops appearing.

### Rebase Stacked Pull Requests

Keeping stacked pull requests current used to mean rebasing them one branch at a time, in the right order, without missing one. **_Rebase Stack..._** now does the whole chain in one go. It replays each layer onto the one below it and the bottom layer onto the stack's trunk. If you haven't checked out a layer, it creates a local branch for it so the cascade stays unbroken. Every message tells you where you are (_Branch 2 of 4_), and when it finishes you're back on the branch you started from.

**_Auto-Rebase Stack..._** hands conflicts to AI the whole way up. When it needs your help it pauses instead of unwinding. Once you've resolved the conflict, _Continue with Auto-Rebase_ carries on through the rest of the stack, not just the branch you fixed.

**Publishing the result** &mdash; when the rebase completes, GitLens offers _Force Push Stack_ with every rewritten branch pre-checked, so you can uncheck any you want to hold back. The offer also appears on the _Auto-Rebase Summary_ and as the _Git Force Push Stacked Pull Requests..._ command, so dismissing the notification doesn't lose it. It goes away on its own once every branch is published.

Stack rebasing is only offered when the stack has drifted from its trunk, either by falling behind or by conflicting with it, so a stack that's already current won't prompt you. You'll find it on the _Commit Graph_'s pull request sheet and side bar stack rows, in _Launchpad_, in the rebase quick pick, and as the _Git Rebase Stacked Pull Requests..._ and _Auto-Rebase Stacked Pull Requests..._ commands.

### Start From Anywhere

**A no-repository state that helps you begin** &mdash; when no repository is open, the _Commit Graph_'s empty state now offers grouped ways to start: open a folder, clone a repository, or start a new project by opening a remote repository on the web. _Start Work on an Issue_ and _Start Review on a PR_ sit alongside them.

**_Start Work_ and _Start PR Review_ without a repository** &mdash; both now list your issues and pull requests across all your connected integrations, even with nothing open. Once you pick one, GitLens offers to locate the repository in a local folder, or to clone it when the integration provides a repository URL (every pull request, and GitHub issues). When an integration can't search issues across your whole account, _Start Work_ now says so. Bitbucket, for example, has no account-wide issue search, so instead of quietly contributing nothing to the list, it tells you and points you to open a repository.

**Hand it to an agent, or don't** &mdash; _Start Work_ and _Start PR Review_ now follow the `gitlens.ai.openInAgent` setting. After you pick an issue or pull request, they ask whether to open it in an agent (or in Kepler, as described above) or continue yourself, unless you've already set a default. The agent pickers also remember your choice with a single _Always use this choice_ / _Always use this agent_ option, instead of a checkbox on every row.

### Sign-in Screens That Remember What You Were Doing

Opening something in the _Commit Graph_ while signed out, or before upgrading, used to land you on a generic screen and forget what you'd asked for. Now the sign-in and upgrade screens name the task that was interrupted, whether that's a commit, branch, tag, or stash, a file or folder's history, a comparison, your working changes, a branch focus, or an automatic rebase summary. Once you have access, it opens in the graph.

That includes Ctrl-clicking a commit hash in the terminal: instead of an unexplained sign-in screen, you see which commit you clicked, and GitLens holds it until you're signed in. Comparisons and file or folder histories opened this way are no longer discarded, and if a second task arrives while the screen is open, the screen updates to describe it.

### Everyday Improvements

- Section headers in GitLens views, such as _Files Changed_ in _Inspect_ and the _Commit Graph_'s side bar panels, now match VS Code's Modern UI headers when Modern UI is on.
- _Hide Remote-only Branches_ in the _Commit Graph_ now hides only remote branches with no local counterpart. Remote branches that your local branches track keep their pills and commits.
- _Create Branch..._ with _Create Branch in New Worktree_ now always keeps the branch name you entered. Deleting a branch that has a worktree now deletes both in a single confirmation.
- Azure DevOps pull request links are fixed: they're no longer malformed, they keep the collection when the server sits behind a virtual directory, and they always point at your configured organization.
- Autolinked pull requests and issues no longer disappear from _Inspect_, hovers, and views after a failed lookup. GitLens retries the next time they're needed.
- The _GitKraken AI_ usage meter now reads _Allowance used_ when your weekly allowance is fully spent, and shows enough precision to tell a nearly-spent allowance from a spent one.

---

### Added

- Adds starting a task or a pull request review in Kepler, right from where you are in GitLens ([#5760](https://github.com/gitkraken/vscode-gitlens/issues/5760))
  - Adds _Start Task in Kepler_ to repositories, and _Start Review in Kepler_ to pull requests in GitLens views, _Launchpad_, and the _Commit Graph_ &mdash; each opens Kepler with the repository or pull request ready to go
  - Adds _Open in Kepler_ to _Start Work_ and _Start PR Review_ for items Kepler supports, alongside opening in an agent or continuing manually &mdash; or choose `kepler` for `gitlens.ai.openInAgent` to go straight there
  - Offers to get the Kepler application when it isn't installed, and stops showing the _Try Kepler_ banner once it is
- Adds rebasing an entire stacked pull request chain in one action ([#5838](https://github.com/gitkraken/vscode-gitlens/issues/5838))
  - _Rebase Stack..._ cascades bottom to top, replaying each layer onto the one below it and the bottom layer onto the stack's trunk &mdash; and creates a local branch for any layer you haven't checked out, so no link in the chain is skipped
  - _Auto-Rebase Stack..._ resolves conflicts with AI the whole way up, pausing instead of unwinding when it needs your help &mdash; _Continue with Auto-Rebase_ then picks up the rest of the stack, not just the branch you fixed
  - Every message names where you are in the stack (_Branch 2 of 4_), and the cascade puts you back on the branch you started from
  - Offers _Force Push Stack_ on completion, listing each rewritten branch pre-checked so you can hold any of them back &mdash; the offer also lives on the _Auto-Rebase Summary_ and as a _Git Force Push Stacked Pull Requests..._ command, so it survives the notification being dismissed, and retires itself once every branch is published
  - Offered only when the stack has drifted from its trunk &mdash; behind it, or conflicting with it &mdash; so an already-current stack isn't invited into a rebase that would do nothing
  - Reachable from the _Commit Graph_'s pull request sheet and side bar stack rows, _Launchpad_, the rebase quick pick, and the _Git Rebase Stacked Pull Requests..._ and _Auto-Rebase Stacked Pull Requests..._ commands
- Adds start actions to the _Commit Graph_'s no-repository empty state &mdash; grouped ways to get going: open a folder, clone a repository, or start a new project (open a remote repository on the web), alongside _Start Work on an Issue_ and _Start Review on a PR_
  - Adds _Start Work_ and _Start PR Review_ support when no repository is open &mdash; both now list your issues and pull requests across your connected integrations, and offer to locate the repository in a local folder before continuing, or to clone it when the integration supplies a repository URL (every pull request, and GitHub issues)
  - _Start Work_ now tells you when a connected integration can't search issues account-wide, instead of letting it contribute nothing to a seemingly empty list &mdash; Bitbucket has no account-wide issue search, so it now says so and points you to open a repository
- Adds task-specific context to the _Commit Graph_'s sign-in and upgrade screens when navigating to it from other areas of GitLens ([#5820](https://github.com/gitkraken/vscode-gitlens/issues/5820), [#5784](https://github.com/gitkraken/vscode-gitlens/issues/5784))
  - Names the task that was interrupted &mdash; opening a commit, branch, tag, or stash, a file or folder's history, a comparison, your working changes, a branch focus, or an automatic rebase summary &mdash; and confirms it will open in the _Commit Graph_ once you have access
  - Ctrl-clicking a commit hash in the terminal now names the commit and holds it until you're signed in, instead of landing on an unexplained sign-in screen

### Changed

- Changes _Start Work_ and _Start PR Review_ to follow the `gitlens.ai.openInAgent` setting &mdash; after you pick an issue or pull request they now ask whether to open it in an agent or continue manually, unless you've set a default
- Changes the agent pickers to remember your choice with a single _Always use this choice_ / _Always use this agent_ option, instead of a checkbox on every row
- Changes section headers in GitLens views, such as _Files Changed_ in _Inspect_ and the _Commit Graph_'s sidebar panels, to match VS Code's Modern UI headers &mdash; with Modern UI on they use its 12px semibold header text in title case (or all caps when `workbench.experimental.modernUIUppercaseViewHeaders` is enabled), and they're unchanged when it's off

### Fixed

- Fixes GitKraken AI telling someone on a Pro trial to _Upgrade to GitLens Pro_ when a request is refused for lack of entitlement &mdash; it now names the trial and offers to upgrade to the trialed plan ([#5789](https://github.com/gitkraken/vscode-gitlens/issues/5789))
- Fixes a comparison, or a file or folder history, opened in the _Commit Graph_ while signed out or before upgrading being discarded instead of opening once access is granted ([#5820](https://github.com/gitkraken/vscode-gitlens/issues/5820))
- Fixes the _Commit Graph_'s sign-in and upgrade screens still describing the previous task when a second one arrives while they're open ([#5820](https://github.com/gitkraken/vscode-gitlens/issues/5820))
- Fixes _Create Branch..._ discarding the branch name you entered when you choose _Create Branch in New Worktree_ ([#4501](https://github.com/gitkraken/vscode-gitlens/issues/4501)) &mdash; from a remote base the worktree step replaced your name with the remote branch's own and re-prompted with _A branch named 'main' already exists_, and from a local base that isn't checked out anywhere it quietly created the worktree on that branch instead of a new one; a requested branch name is now always honored, including the `pr/` branch _Open Worktree for Pull Request_ asks for
- Fixes _Delete Branch..._ on a branch that has a worktree deleting the worktree but leaving the branch behind &mdash; Git refuses to delete a branch that's checked out in a worktree, so both now happen together in a single confirm with _Delete Branch_ pre-checked; uncheck it to keep the branch. _Prune Branches..._ works the same way
- Fixes the _Delete Worktree_ confirm offering to delete a branch's upstream when that upstream is already missing from the remote
- Fixes the _GitKraken AI_ usage meter saying _Nearly out_ when the weekly allowance is spent in full &mdash; it now reads _Allowance used_ in the error color, in both _GitLens Settings_ and the _Commit Graph_'s account rollup
  - Fixes the credits figure rounding a nearly-spent allowance to look identical to a fully-spent one (`3.2M of 3.2M credits` for either) &mdash; it now shows enough precision to tell the two counts apart, and the account rollup's percentage no longer rounds up to `100%` while credits remain
- Fixes _Hide Remote-only Branches_ in the _Commit Graph_ hiding every remote branch ([#5852](https://github.com/gitkraken/vscode-gitlens/issues/5852)) &mdash; a remote branch that a local branch tracks isn't remote-only, so it now keeps its pill and its commits stay in the graph; only remote branches with no local counterpart are hidden
  - Fixes a tracked remote branch still counting as remote-only when its local branch's tip sat outside the loaded commits &mdash; tracking is now resolved from all of your branches instead of only the ones the graph had walked, which also restores the upstream half of the ref pills it affected
- Fixes the _Commit Graph_'s commit hover ignoring its minimum width &mdash; the width rule was invalid CSS and silently dropped, so a short commit message rendered as a narrow sliver instead of keeping the card's intended size
- Fixes hard-to-read text on customized _Commit Graph_ lane colors &mdash; labels on a mid-lightness `gitlens.graphLaneNColor` color used white text where black was far more legible; they now pick whichever gives more contrast
- Fixes Azure DevOps pull requests returning `undefined` for their base and head repository links &mdash; the repository reference Azure embeds in a pull request does not include a web URL, so the link is now built from the organization and server the pull request was read from ([#5839](https://github.com/gitkraken/vscode-gitlens/issues/5839))
- Fixes Azure DevOps Server links dropping the collection when the server sits behind a virtual directory &mdash; `https://server/tfs/DefaultCollection/…` read `tfs` as the organization and lost everything after it ([#5840](https://github.com/gitkraken/vscode-gitlens/issues/5840))
- Fixes an Azure DevOps pull request's repository links being able to point at another organization, or another server entirely, when the pull request payload said so &mdash; the links are built from the configured organization now, and a fork's link must belong to it ([#5842](https://github.com/gitkraken/vscode-gitlens/issues/5842))
- Fixes malformed Azure DevOps pull request web URLs &mdash; the URL had a double slash after the host (both `dev.azure.com` and `*.visualstudio.com`) and left project and repository names unencoded, so a project or repository named with a space put a literal space in the link ([#5836](https://github.com/gitkraken/vscode-gitlens/issues/5836))
- Fixes autolinked pull requests and issues disappearing from _Inspect_, hovers, and views until the window is reloaded &mdash; a failed lookup (a rate limit, server error, or timeout) was remembered as "not found" for the rest of the session, and enrichment done before an integration finished connecting was kept for 30 minutes; failed lookups are now retried the next time they're needed
- Fixes files you uncheck in the _Commit Graph_'s _Review_ and _Compose_ modes getting checked again &mdash; the details panel refreshing reset your exclusions (and, in _Compose_, your excluded commits), so an unchecked file could quietly end up back in the review or commit plan
- Fixes the commit range appearing twice at the top of the _Commit Graph_'s _Review_ results for a commit selection
- Fixes the _Commit Graph_'s _Next steps_ permanently listing a branch's merged or closed pull request as something to act on ([#5846](https://github.com/gitkraken/vscode-gitlens/issues/5846)) &mdash; only an open pull request is offered now, and a branch whose pull request is merged or closed gets _Create a Pull Request_ instead; the header still shows the merged or closed pull request
- Fixes entering a reference in the _Git Command Palette_'s _show_ command discarding it and going back to the command menu ([#5855](https://github.com/gitkraken/vscode-gitlens/issues/5855)) &mdash; pressing Enter before the reference finished resolving chose _Back_, and a branch or tag name never resolved at all; Enter now waits for the reference, branch and tag names resolve to their commit in every commit step, and a reference that doesn't resolve keeps what you typed

---

<a id="v19-2"></a>

## Version 19.2

#### Tuesday, September 15, 2026

GitLens 19.2 now speaks your language. GitLens follows your VS Code display language, with experimental Spanish and Chinese (Simplified and Traditional) translations available today &mdash; install the matching VS Code language pack and GitLens switches over with it, falling back to English for anything not yet translated.

The _Commit Graph_ can now be scoped to a worktree. _Scope to Worktree_ re-points the whole graph at that worktree &mdash; its working changes become the primary WIP row, its status drives the markers and ahead/behind counts, and every action runs with it as the working directory. History is never re-walked, so scoping and unscoping are immediate and keep your scroll position, selection, search, and filters intact.

The Graph can also save your column arrangement, sizing, grouping, and panels as the default for new workspaces, rebind or disable its keyboard shortcuts, and run your default VS Code task in any worktree with a single click. Past Codex, OpenCode, and GitHub Copilot CLI agent sessions can now be resumed too &mdash; in a terminal, or in the agent's own extension.

Rounding things out, the _Home_ view has been retired now that the _Commit Graph_ covers and expands on everything it did, onboarding is consolidated into the _Welcome_ view, and a new _Send Feedback_ dialog puts feature requests and bug reports one click away.

<img src="/wp-content/uploads/gl-19-2-hero.png" class="help-center-img img-bordered">

### GitLens in Your Language

GitLens is now localized. It follows your VS Code display language, so installing the matching VS Code language pack switches GitLens over too &mdash; no separate setting to find.

**Spanish and Chinese (Simplified and Traditional) are experimental** translations in this release. Anything not yet translated defaults to English, and Git syntax, references, paths, commands, and product names are deliberately left untranslated, so what you type and what you search stays the same everywhere.

### Scope the Graph to a Worktree

_Scope to Worktree_ points the entire _Commit Graph_ at a worktree. Its working changes become the primary WIP row, the current-branch markers, ahead/behind, and upstream status all follow it, and every action you run &mdash; commit, pull, push, switch &mdash; uses it as the working directory. Because history is never re-walked, scoping and unscoping are immediate and preserve your scroll position, selection, search, and filters.

You can scope from worktree rows in the side bar, by double-clicking a WIP row or overview bar pill, from WIP row context menus, or with the _Focus in Commit Graph_ commands. A scoped graph tints its title bar and names the worktree's branch in a pill &mdash; hover it for an explanation of the scope, or use its _Unscope Worktree_ button to return to your active worktree. The scope survives reloads, and the first time you scope, a coach mark explains what changed.

**Scope and focus are now independent.** _Focus_ names the branch projection &mdash; narrowing the visible rows to a branch's history &mdash; while _Scope_ names the worktree perspective, so a scoped graph still shows every commit unless the branch is focused too. Two settings control how they combine: `gitlens.graph.scopeBehavior` (whether scoping also focuses the worktree's branch, the default) and `gitlens.graph.doubleClickWorktreeAction` (whether a double-click scopes or just focuses).

### A Graph That Fits the Way You Work

**Save your layout as the default** &mdash; arrange columns, sizing, grouping, and panels how you like, then use _Save as Default Layout_ in the column header or settings gear menus to make it the starting point for new workspaces. _Apply Saved Layout_ re-applies it anytime, and _Reset Layout_ restores the shipped arrangement.

**Rebind the keyboard shortcuts** &mdash; the new `gitlens.graph.shortcuts.overrides` setting lets you rebind or disable the graph's modifier-key shortcuts (`Alt+M`, `Ctrl+↑`, and the rest) by id &mdash; hover a shortcut in the <kbd>?</kbd> reference to find its id &mdash; or turn them all off with `gitlens.graph.shortcuts.enabled`.

### Worktree Tasks and Resumable Agent Sessions

Worktree WIP rows in the _Commit Graph_ gain a **_Run Default Task_ button** that runs your chosen default VS Code task in that row's worktree in one click. The first click asks which task to make the default; any task can be marked or unmarked as the default from the _Run Task on Worktree_ picker, and <kbd>Alt</kbd>+click always opens the picker. While a task is running the button shows a spinner, and clicking reveals that task's terminal instead of starting another.

**Resuming past agent sessions** now works for Codex, OpenCode, and GitHub Copilot CLI as well. Every _Resume_ action names where it goes &mdash; _Resume in Terminal_ or _Resume in &lt;Agent&gt; Extension_ &mdash; and shows both when a session can open either way. The new `gitlens.agents.resumeTarget` setting picks which one <kbd>Enter</kbd> uses in the _Resume Agent Session_ picker, or asks the first time with an option to remember.

Connecting agents is easier, too: the graph's _Agents_ side bar panel now explains why it's empty instead of showing a generic "No items", with a connect action named for your default agent that opens _GitLens Settings_ and installs that agent's hooks immediately.

### Everyday Improvements

- A _Generate Changelog_ action now works on multi-selected commits in the _Commit Graph_, even when the selection isn't contiguous.
- Working changes _Next steps_ offer _Force Push_ alongside _Pull_ when a branch has diverged from its upstream &mdash; the state you land in after a rebase or recompose.
- In repositories where loading commit file details has been slow, the _Commits_ and other history views now load them on demand automatically, rather than making you find the setting yourself.

---

### Added

- Adds localization infrastructure for GitLens using VS Code’s display language, with English fallback when a translation is unavailable
  - Adds experimental Spanish and Chinese (Simplified and Traditional) translations &mdash; GitLens follows your VS Code display language, so installing the matching language pack switches GitLens over too; the translations are AI-generated and reviewed, and anything not yet translated stays in English
- Adds worktree scoping to the _Commit Graph_ &mdash; _Scope to Worktree_ (on side bar worktree rows, working-changes (WIP) row and overview bar pill double-clicks, WIP row context menus, and the _Focus in Commit Graph_ commands) now re-points the whole graph at that worktree: its working changes become the primary WIP row, the current-branch markers, ahead/behind and upstream status follow it, and every action runs with it as the working directory. History is never re-walked, so scoping and unscoping are immediate and keep your scroll position, selection, search, and filters; a scoped graph tints its title bar and names the worktree's branch in a pill whose hover explains the scope and whose _Unscope Worktree_ button returns to your active worktree; the first time you scope, a coach mark explains what changed. Scope and focus are now independent &mdash; a scoped graph still shows every commit unless the branch is focused too; a scoped graph stays scoped across reloads
  - Adds a `gitlens.graph.scopeBehavior` setting &mdash; whether _Scope to Worktree_ also focuses the worktree's branch, narrowing the visible rows to its history (`scopeAndFocus`, the default), or scopes without narrowing anything (`scope`)
  - Adds a `gitlens.graph.doubleClickWorktreeAction` setting &mdash; whether double-clicking another worktree's WIP row, overview bar pill, or side bar row scopes the graph to it (`scope`, the default) or just focuses its branch (`focus`)
- Adds saving your _Commit Graph_ layout as the default for new workspaces ([#4292](https://github.com/gitkraken/vscode-gitlens/issues/4292)) &mdash; arrange columns, sizing, grouping, and panels how you like, then use the new _Save as Default Layout_ action in the column header or settings gear menus; the new _Apply Saved Layout_ action re-applies it anytime, and _Reset Layout_ restores the shipped arrangement (replacing the previous _Reset Columns to Default/Compact Layout_ actions)
- Adds a _Send Feedback_ dialog ([#5812](https://github.com/gitkraken/vscode-gitlens/issues/5812)) &mdash; reachable from the _Commit Graph_'s title toolbar and its account menu; choose general feedback, a feature request, or a bug report about GitLens and send it straight to the team, bug reports also open a prefilled GitHub issue so you can add logs and details, and feature requests offer to file one
- Adds customizing the _Commit Graph_ keyboard shortcuts ([#5813](https://github.com/gitkraken/vscode-gitlens/issues/5813)) &mdash; use the new `gitlens.graph.shortcuts.overrides` setting to rebind or disable its modifier-key shortcuts (`Alt+M`, `Ctrl+↑`, …) by id (hover a shortcut in the `?` reference to see its id), or `gitlens.graph.shortcuts.enabled` to turn them all off
- Adds a _Run Default Task_ button to worktree working-changes (WIP) rows in the _Commit Graph_ &mdash; runs your chosen default task in the row's worktree in one click; the first click asks which task to make the default, any task can be marked (or unmarked) as the default from the _Run Task on Worktree_ picker, and Alt+click always opens the picker; while a task is running the button shows a spinner and a _Running: &lt;task&gt;_ tooltip, and clicking reveals that task's terminal instead of starting another
- Adds a _Generate Changelog_ action to multi-selected commits in the _Commit Graph_ ([#4088](https://github.com/gitkraken/vscode-gitlens/issues/4088)) &mdash; generates an AI changelog from exactly the selected commits, even when the selection isn't contiguous
- Adds resuming past Codex, OpenCode, and GitHub Copilot CLI agent sessions &mdash; every _Resume_ action now names where it goes, _Resume in Terminal_ or _Resume in <Agent> Extension_, and shows both when a session can open either way; the new `gitlens.agents.resumeTarget` setting picks which one Enter uses in the _Resume Agent Session_ picker, or asks the first time with an option to remember
- Adds a _Force Push_ action to the _Commit Graph_'s working-changes _Next steps_ when a branch has diverged from its upstream ([#5832](https://github.com/gitkraken/vscode-gitlens/issues/5832)) &mdash; after a rebase or recompose the branch is both ahead and behind, and the diverged step now offers _Pull_ and _Force Push_ side by side, instead of only pointing at _Pull_

### Changed

- Changes the _Commits_ view and other history views to load commit file details on demand in repositories where loading them has been slow ([#5498](https://github.com/gitkraken/vscode-gitlens/issues/5498)) &mdash; the `gitlens.advanced.commits.delayLoadingFileDetails` setting now defaults to `null` (automatic); set it to `true` or `false` to force either behavior
- Consolidates the _Get Started_ walkthrough into a single step that opens the _Welcome_ view ([#5809](https://github.com/gitkraken/vscode-gitlens/issues/5809)) &mdash; the _Welcome_ view is now the unified onboarding experience; the extension's _Get Started_ action, Launchpad's learn-more links, and walkthrough deep links all open it directly
- Improves the flow of connecting agents from the _Commit Graph_'s _Agents_ side bar panel ([#5777](https://github.com/gitkraken/vscode-gitlens/issues/5777)) &mdash; the panel now explains why it is empty instead of showing a generic "No items", with a connect action, named for your default agent (e.g. _Connect Claude Code..._), that opens the _Agents_ page in _GitLens Settings_ and immediately installs that agent's hooks (_Manage Agents..._ when there is no connectable default); adds a _Start Agent Session..._ header action (hold `Alt` to always pick the agent)
- Changes the _Commit Graph_'s worktree actions from _Focus on Worktree_ to _Scope to Worktree_ &mdash; _Focus_ now names only the branch projection (narrowing the rows to a branch's history) and _Scope_ names the worktree perspective, so the two read as the independent modes they now are; worktree rows offer both verbs on one button (_Scope to Worktree_ on click, _Focus on Branch_ on Alt+click), and both are hidden for a detached-HEAD worktree, which has no branch to act on
- Changes the _Commit Graph_ minimap's _Zoom to Scope_ action to _Zoom to Focus_ &mdash; matching the graph's vocabulary now that _Scope_ names the worktree perspective
- Changes double-clicking a working-changes (WIP) row or overview bar pill whose branch is already focused through a pull request or a stack to re-focus it as a plain branch instead of unfocusing &mdash; reaching the same branch a different way changes what the graph shows, so it counts as a new focus rather than a repeat of the last one; the side bar already behaved this way
- Improves the _Commit Graph_'s account rollup &mdash; the _AI_ and _Agents_ sections now name what they contain instead of showing unlabeled glyphs: _Agents_ lists each detected agent with its MCP and hooks state, and _AI_ names the active model and gives your _GitKraken AI_ credits their own row; the walkthrough and refer-a-friend rows move into a footer
- Improves the _Commit Graph_'s pull request sheet &mdash; it opens immediately as a skeleton and fills in when the pull request resolves, its description scrolls with a _Show More_ toggle instead of being clipped, images pasted into a description render as chips that open in the browser, and a missing description says so; the title and number open the pull request on the remote, with Alt copying its URL

### Removed

- Removes the `gitlens.graph.experimental.kanban.enabled` and `gitlens.graph.experimental.visualizations.enabled` settings &mdash; Agent Kanban and supported visualizations are always available from the _Commit Graph_
- Removes the _Home_ view &mdash; superseded by the _Commit Graph_, which covers and expands on its workflows ([#5778](https://github.com/gitkraken/vscode-gitlens/issues/5778)); existing _Home_ deep links now open the _Commit Graph_
  - Moves the unsafe-repository explanation into the _Commit Graph_ &mdash; when Git blocks repositories as potentially unsafe, its empty state now says so and points at Source Control, instead of a generic "no repository" message

### Fixed

- Fixes the _Commit Graph_ commit details _Generate Commit Message_ silently doing nothing when the AI provider fails with an untyped error (e.g. Copilot credit limit) &mdash; the failure is now surfaced as an error notification, matching the _Source Control_ panel
- Fixes the _Commit Graph_ retaining outdated parent connections and file statistics after deepening a shallow clone or changing Git replacement refs
- Fixes closing _Compose_ or _Review_ after restarting discarding the saved work, and restores _Resume_ when returning after navigating away
- Fixes contextual tips already seen in one _Commit Graph_ view showing again after another view saves its seen tips
- Fixes [#5827](https://github.com/gitkraken/vscode-gitlens/issues/5827) - It's impossible to use the "Search for commits" dialog
- Fixes the Git Command Palette and other quick picks failing to open on editors older than VS Code 1.108, such as Google Antigravity &mdash; the quick pick `prompt` API is proposal-gated there and throws when set ([#5807](https://github.com/gitkraken/vscode-gitlens/issues/5807))
- Fixes all GitLens webviews staying blank when the Google Antigravity extension is installed &mdash; its `postMessage` patch mangled the binary messages GitLens sends to its webviews, which are now recovered ([#5818](https://github.com/gitkraken/vscode-gitlens/issues/5818), [#5797](https://github.com/gitkraken/vscode-gitlens/issues/5797))
- Fixes AI operations staying in their in-progress state after a request fails on rate limits, exhausted funds, or a missing entitlement ([#5781](https://github.com/gitkraken/vscode-gitlens/issues/5781)) &mdash; _Review_, _Compose_, generated explanations, and the rest now end and report the failure as soon as the request fails, instead of appearing to keep working until the error notification is dismissed; the notification's _Switch Model_ and _Upgrade_ offers stay available afterward
  - Fixes a _Review_ that failed this way reporting no failure at all &mdash; it now surfaces the actual reason instead of reporting the run as cancelled
- Fixes GitLens AI staying without a model after verifying your account's email &mdash; the resolved model and _GitKraken AI_ usage allowance now refresh on verification, and when a trial starts or ends, instead of staying empty until a window reload or opening the model picker ([#5621](https://github.com/gitkraken/vscode-gitlens/issues/5621))
- Fixes clicking an issue or autolink in a branch's hover on the _Commit Graph_ clearing the graph ([#5224](https://github.com/gitkraken/vscode-gitlens/issues/5224)) &mdash; the link now opens in your browser and the graph stays put
- Fixes _Commit Graph_ ref pills permanently missing their pull request and issue badges when the graph loads before your GitHub connection is ready &mdash; the badges now appear once the connection is recognized, instead of needing a window reload
- Fixes _Commit Graph_ ref pills losing their pull request badges after a transient lookup failure (rate limit, server error, expired session) &mdash; a failed lookup is no longer cached as "no pull request", and the graph retries instead of leaving the pill blank
- Fixes opening a stacked pull request from the _Commit Graph_ giving up after 5 seconds and dropping you out to the browser &mdash; the sheet now resolves the pull request and its stack directly, instead of waiting for the repository's entire open pull request list to load
- Fixes _Commit Graph_ reveals landing short of the target commit in the list layout &mdash; a reveal now waits for the row height to settle, and a row-height change keeps the viewport anchored instead of leaving it scrolled to the old position
- Fixes reordering _Commit Graph_ columns moving the grouped columns into whichever column is dropped at the group's position
- Fixes the _Commit Graph_ header and push flow offering nothing when a branch's upstream was deleted on the remote &mdash; a gone upstream is now treated as unpublished, so _Publish_ is offered
- Fixes author avatars failing to load in the _Commit Graph_ as new authors scroll into view &mdash; each lookup sent an empty ref instead of the commit's sha and was rejected
- Fixes opening an agent session hosted in a terminal only raising the VS Code window &mdash; it now shows the terminal or tab actually running the session, including when that session is in another window
- Fixes the _Repository Health_ banner continuing to show after applying one of its suggested optimizations &mdash; acting on a suggestion now quiets it for 30 days, the same as dismissing it
- Fixes the merge conflict check failing on Git 2.33&ndash;2.37, and the cherry-pick and rebase conflict checks failing before Git 2.40 &mdash; each was gated on an older Git version than the flags it uses
- Fixes typos and inconsistencies in user-facing text ([#5849](https://github.com/gitkraken/vscode-gitlens/issues/5849)) &mdash; corrects misspellings, broken grammar, and stray punctuation across notifications, quick picks, and settings descriptions, including a misspelled "acccount" in the _Launchpad_ snooze prompt, a stray brace in the deep-link clone progress title, a missing space before the em dash in the Cloud Patch created notification, the _Open Current Branch on Remote_ picker titling itself "Open Current Branch Name", and seven _Reveal_ settings reading "otherwise they revealed"
  - Fixes four settings descriptions rendering a dead `#…#` link because they named a setting that does not exist &mdash; `gitlens.advanced.blame.delayAfterEdit`, the deprecated `gitlens.views.commitFormat` and `gitlens.views.stashFormat`, and `gitlens.ai.openInAgent`
  - Fixes the _Git CodeLens_ and status bar click-command settings describing _Search for Commits within Selection_ as "Shows the Inspect", and the deprecated `gitlens.outputLevel` naming the debug logging commands without their "(Trace)" part
  - Fixes stale `eamodio/vscode-gitlens` wiki links in three view format settings

---

<a id="v19-1"></a>

## Version 19.1

#### Tuesday, September 1, 2026

GitLens 19.1 now supports live agent status for more coding agents - Codex, GitHub Copilot CLI, and OpenCode sessions now appear everywhere Claude Code's already do &mdash; the _Agents_ side bar panel, details panel, Graph WIP rows, and more. Each session displays the agent's state with full right-click controls so you can jump in when your Agent needs you without distrupting your focus. You can start an agent session or run a VS Code task on any worktree without opening it, and the graph will follow your active terminal to the worktree it's in. Install GitKraken Hooks for each agent to integrate its status directly into your GitLens workflows from _GitLens Settings_. 

Everyday Git operations are expanded and given a sharper flow - Fixup commits arrive in the graph, autosquash lands in rebases, and tags can finally be pushed &mdash; while the _Git Command Palette_ has been rebuilt around one consistent confirmation design. The graph itself says more per row, with multiple branch and tag pills, WIP rows that name the branch they sit on, and hidden refs you can actually find again. Search gets more intent-aware, and finding nothing now offers counted broader alternatives instead of a dead end.

GitLens also starts looking after the repository itself, keeping up the routine work `git gc` performs quietly in the background so history loads fast, with a new experimental _Repository Health_ visualization to show what it noticed and what each suggested optimization costs before anything is applied.

Rounding things out, a pending rebase can be handed straight to automatic (AI) conflict resolution from the _Interactive Rebase Editor_, and a new GitKraken AI usage meter in the _Account_ section of _GitLens Settings_ gives you more visibility into what you've used and when it resets.

<img src="/wp-content/uploads/gl-19-1-hero.png" class="help-center-img img-bordered">

### More Coding Agents Integrated in the Graph

Live agent status is no longer Claude Code's alone. **Codex, GitHub Copilot CLI, and OpenCode** sessions now appear everywhere agent status is shown to ensure full visibility into your coding agent sessions throughout your workflows. Each agent carries its own icon so sessions from different agents stay distinguishable, and GitKraken Hooks can be installed for them from _GitLens Settings_. Agent sessions also gain full right-click context menus, with permission actions, _View Plan_, open and resume actions, worktree and terminal actions, and _Archive Session_.

**Put a worktree to work without opening it**  &mdash; A _Start Agent Session..._ action on WIP rows and worktrees opens a terminal at that worktree running your default coding agent CLI, and a _Run Task on Worktree..._ action runs a VS Code task &mdash; from `tasks.json`, or an auto-detected one like an npm script &mdash; with the worktree as its working directory, so build, test, and launch tasks can target a worktree you never had to open.

**The graph follows your terminal**  &mdash; While a graph is visible, switching to a terminal (or a Claude Code conversation tab) selects the working changes row of the repository or worktree it's in &mdash; without raising the graph, opening the details panel, or switching repositories. It's on by default, with toggles in the graph's "..." menus and a one-time tip the first time it moves your selection.

### Fixup Commits, Autosquash, and Push Tags

**Fixup commits in the _Commit Graph_** &mdash; a new _Fixup Commit..._ action on any commit seeds the working-changes commit box with a `fixup! <subject>` message. Once a message resolves to a target, the commit button becomes a split button: _Commit Fixup_ creates the fixup to squash later, while _Commit Fixup & Squash_ folds it into its target immediately. A _Squash Fixups..._ action on the current branch and working-changes rows squashes all pending fixups into their targets, warning first when pushed commits would be rewritten.

**Autosquash in rebases** &mdash; a new toggle in the _Git Command Palette_ folds `fixup!` and `squash!` commits into the commits they target, defaulting from your `rebase.autosquash` Git config. Interactive rebases open the _Interactive Rebase Editor_ with the fixups already folded; plain and automatic rebases fold them directly. (Requires Git 2.44.)

**Pushing tags** &mdash; a new _Push Tag..._ action on tags in the views and the _Commit Graph_, and a _Git Push Tag..._ command in the Command Palette. Choose the remote (skipped when there's only one) and confirm, with an optional force push for moved tags.

### A Rebuilt Git Command Palette

The _Git Command Palette_'s confirmations have been redesigned around one consistent shape: action rows with the safest choice pre-selected, plus checkbox toggles for options &mdash; replacing a separate row for every flag combination. Toggles default from your Git config (`fetch.prune`, `merge.ff`), and _Force_ toggles visibly rewrite the action and never default on.

Pushing now has three consistent confirmation shapes (ahead, behind, and unpublished) with the blocking reason shown above the choices, switching offers just the targets plus an _In a New Worktree_ toggle, and stashing asks for the message first so the final <kbd>Enter</kbd> stashes &mdash; with a new _Stash Changes & Untracked_ mode and a _Keep Staged_ toggle making previously unreachable combinations possible. Worktree creation and deletion each collapse into a single step with in-place toggles, and skippable confirmations gain a _Don't Ask Again_ checkbox.

### More at a Glance in the Graph

**Multiple refs per row**  &mdash; A row can now show more than one branch or tag pill. The new `gitlens.graph.refs.maxInline` setting caps how many show before the rest collapse behind the +N counter &mdash; a fixed count (default 1, the previous behavior) or `"auto"` to fit the available space. A new `gitlens.graph.refs.layout` setting adds a `"stacked"` option, where rows with pills grow a second line to show them above the commit instead of beside it.

**WIP rows with an identity** &mdash; Every working-changes row &mdash; the current branch's and each worktree's &mdash; now carries a branch pill right after _Working Changes_ naming the branch it sits on. Click the pill to jump to the branch's tip, or to its upstream or merge target when those are known.

**Manage hidden refs easily**  &mdash; _Hide Remote_ and _Show Remote_ actions join remote rows in the side bar, and hidden branches, remotes, and tags now show dimmed with an _eye-closed_ marker and an un-hide action instead of being indistinguishable from visible ones. You can even un-hide a single branch of a hidden remote &mdash; the remote stays hidden while just that branch returns.

**Jumps that land, or tell you why not**  &mdash; Jumping to a commit hidden by your filters, branch visibility, scope, or first-parent-only following now shows a message naming the blocker with a one-click remedy (_Show Branch_, _Clear Scope_) that completes the jump, and a commit that isn't in the repository is reported immediately instead of silently timing out. Keyboard navigation reaches across not-yet-loaded history too, rather than stopping at the edge of what's loaded.

Maximizing the details panel now overlays the graph instead of resizing it, so the graph behind keeps its exact layout and restoring is instant &mdash; and the details toggle becomes a split button whose chevron opens a placement menu with _Auto_, _Right_, and _Bottom_ thumbnails. The side bar's _Overview_ panel is also now the panel the side bar opens to, with branch cards that act as a scope toggle, native branch context menus, and a _Load More_ control.


### Repository Health and Automatic Git Maintenance

A slow repository is usually a repository Git hasn't been allowed to tidy up. GitLens 19.1 takes care of that for you, and shows its work.

After a _Commit Graph_ load, GitLens now writes the repository's commit-graph file in the background when it's missing or stale &mdash; the same standard cache `git gc` and `git maintenance` write &mdash; so the graph's next open starts emitting rows right away. Beyond that, GitLens checks each repository's shape and, at most once a day, runs the same routine work `git gc` performs: packing loose objects and incrementally repacking. These reorganize objects the repository already contains; they never alter history. More invasive levers &mdash; Git's untracked cache, FSMonitor, system-scheduled `git maintenance`, and `feature.manyFiles` &mdash; are never applied for you, and anything you've configured yourself is left alone. All of it is controlled by the new `gitlens.gitOptimizations.enabled` setting.

The new experimental **_Repository Health_** visualization &mdash; a heart tab in the graph's visualizations switcher &mdash; is where you see the reasoning: suggested optimizations appear as cards with a meter showing the measured value against the threshold that triggered it, every optimization carries expandable details explaining what it does and what it costs, and a ledger lists each lever with its state and ownership &mdash; one GitLens applied offers _Undo_, while one you enabled yourself is left alone. A _Run Maintenance Now_ action and a per-repository toggle sit alongside.

You'll also be told when it matters. When a repository has suggested optimizations *and* Git has been measurably slow there (or the repository is clearly large), a dismissible strip above the graph explains what was noticed and opens _Repository Health_ in one click.

### Search That Understands What You Mean

Natural language search in the _Commit Graph_ now reads your intent. "Only show &hellip;" phrasings filter the graph to matches, "take me to &hellip;" phrasings jump to the commit, and a search that finds nothing offers counted broader alternatives &mdash; _1000+ without the date filter_, say &mdash; instead of a dead end. It also understands your repository: branch, tag, worktree, and contributor names resolve to the real thing rather than being guessed, misspelled author names come back as counted corrections, and a tooltip on the generated query explains how your phrasing was interpreted.

Classic search gets more precise, too, with new `committer:`, `type:merge`, and `-message:` (exclude) operators in both the _Commit Graph_ and _Search & Compare_. Failures now say what actually went wrong, and a pattern that isn't valid regular expression syntax quietly matches literally instead of erroring while you're still typing.

### Automatic Rebase, from the Rebase Editor

The _Interactive Rebase Editor_ gains a **_Start Auto-Rebase_** split button that hands the pending rebase off to automatic (AI) conflict resolution before it starts, executing the todo exactly as you arranged it. The editor closes, the run waits for the rebase's first stop and takes over from there, and a rebase that finishes without ever pausing is reported as completed &mdash; not cancelled. Deliberate stops keep working the way you asked for them: `edit` and `break` steps hand back to you with a _Resume with AI_ path, and a commit message that a `reword` or `squash` needs opens for you to write, where it was previously kept or auto-accepted without asking.

When a run does stop for you, the actions stay put &mdash; the _Commit Graph_'s **Resolve** panel keeps _Resume with AI_ and _Abort Rebase_ available rather than offering them only in a transient toast, and the rebase editor's paused view gains a _Continue with AI_ button.

### Monitor Your GitKraken AI Usage

A new **_GitKraken AI Usage_** card in the _Account_ section of _GitLens Settings_ shows your weekly credit allowance, how much of it you've used, and when it resets &mdash; along with your organization's shared pool when one applies, broken down into your own draw against the rest of the organization's. A compact usage meter also sits in the account rollup in the _Commit Graph_ header and on _Home_, opening the full card when clicked.

---

### Added

- Adds live status for more coding agents &mdash; Codex, GitHub Copilot CLI, and OpenCode sessions now appear alongside Claude Code's everywhere agent status is shown, each with its own icon ([#5742](https://github.com/gitkraken/vscode-gitlens/issues/5742), [#5798](https://github.com/gitkraken/vscode-gitlens/issues/5798))
  - Improves the _Commit Graph_'s working-changes Agents section with one consistent, collapsible view for live and past sessions, inline history paging, and _Resume_ and _Archive_ actions
  - Changes agent status indicators to one consistent phase mark everywhere sessions appear &mdash; and each session now shows its own agent's logo instead of a generic robot
  - Adds right-click context menus to agent sessions &mdash; on the _Agents_ panel's rows and the details panel's session cards &mdash; with permission, plan, open/resume, worktree, terminal, copy, and _Archive Session_ actions
  - Adds an agent session details sheet to the _Commit Graph_ &mdash; clicking a live or past session card opens its full details: status and elapsed time, the current permission ask with its resolve actions right there, the running tool, prompt history, and a file-activity tree whose files open with a click. Branch and worktree chips jump the graph to the session's work, and past sessions offer _Resume_ and _Archive_ (_Resume_ explains itself when the session's transcript is gone)
  - Adds installing GitKraken Hooks for these agents from the _Agents_ section in _GitLens Settings_ and the install-all commands; when an agent needs an extra step (Codex requires trusting the hooks via `/hooks`), GitLens says so and offers to start a session to do it
  - Shows these agents' permission requests as read-only &mdash; only Claude Code's can be answered from GitLens today
- Adds deeper integration with your terminals and terminal-based coding agents &mdash; GitLens now connects the _Commit Graph_ to the terminals and agent tabs where the work is actually happening
  - Adds following of the active terminal or Claude Code tab &mdash; switching to one selects its repository's or worktree's working-changes row in the _Commit Graph_, so the graph keeps up with where you and your agents are working, without raising the graph or switching repositories; a one-time tip explains the first move and offers _Turn Off_ (controlled by the new `gitlens.graph.followTerminal.*` settings)
  - Adds _Focus in Commit Graph_, _Open in Commit Graph_, and _Open in New Window_ actions to terminal tabs, terminal editor tabs, and Claude Code conversation tabs &mdash; opening the graph at the tab's worktree with its working changes selected
  - Adds a `gitlens.openInTerminalLocation` setting &mdash; controls where GitLens opens the terminals it creates (the _Open in Integrated Terminal_ actions plus agent session terminals), either in the terminal panel (default) or as an editor tab
- Improves the _Commit Graph_ &mdash; richer branch and tag pills, worktree actions to start agents and run tasks, and refinements across navigation and the side bar
  - Adds richer branch and tag pills
    - Adds support for multiple pills on a row ([#5729](https://github.com/gitkraken/vscode-gitlens/issues/5729)) &mdash; a new `gitlens.graph.refs.maxInline` setting caps how many show before the rest collapse behind the +N counter (default 1, the previous behavior, or `"auto"` to fit the space)
    - Adds a stacked pill layout &mdash; with the new `gitlens.graph.refs.layout` setting on `"stacked"`, rows with pills grow a second line showing them above the commit, capped by `gitlens.graph.refs.maxStacked` (default `"auto"`)
    - Adds a bright lane highlight when pinning a branch's pill, and to the `Ctrl`/`Alt`-held chain highlight &mdash; the branch's lane stays lit and traces down to its fork point while other lanes mute
    - Improves remote branch pills &mdash; the branch's remote now follows the name as a subtle qualifier (yielding first when space is tight); `gitlens.graph.showRemoteNames` still switches to the full `remote/branch` form
    - Adds a marker to a branch pill whose upstream is gone (deleted) &mdash; so a branch whose remote counterpart was removed is called out instead of looking healthy
  - Adds _Start Agent Session..._ and _Start Agent Session With..._ actions to working-changes (WIP) rows in the _Commit Graph_ and to worktrees in the views &mdash; opens a terminal at the worktree running your default coding agent CLI, or _With..._ to pick which agent; _Resume Agent Session..._ now also appears on worktrees in the views
  - Adds a _Run Task on Worktree..._ action to worktree working-changes (WIP) rows and to worktrees in the views &mdash; runs a VS Code task with the worktree as its working directory (and `GITLENS_WORKTREE_PATH` in its environment), so build, test, and launch tasks can target a worktree without opening it
  - Adds feedback when a _Commit Graph_ jump can't land ([#5699](https://github.com/gitkraken/vscode-gitlens/issues/5699)) &mdash; jumping to a commit hidden by your filters, visibility, scope, or first-parent following now names the blocker and offers a one-click remedy (e.g. _Show Branch_, _Clear Scope_) that completes the jump. A commit that isn't in the repository is reported immediately, and longer searches show a cancellable _Looking for…_ indicator
  - Adds _Hide Remote_ and _Show Remote_ actions to remote rows in the _Commit Graph_ side bar &mdash; and hidden branches, remotes, and tags now show dimmed with an _eye-closed_ marker and a one-click un-hide, instead of being indistinguishable from visible ones. Hidden remotes show their provider's icon, and un-hiding a single branch of a hidden remote brings just that branch back
  - Adds _Group_ and _Ungroup_ commands for the _Commit Graph_'s columns to its header context menus &mdash; grouping previously required dragging one column onto another
  - Adds _Copy Worktree Path_ to worktree branch pills and _Copy Branch Name_ to working-changes (WIP) rows in the _Commit Graph_
- Adds Git health and maintenance &mdash; GitLens now keeps Git's performance caches fresh and tells you when a repository needs attention (controlled by the new `gitlens.gitOptimizations.enabled` setting)
  - Adds automatic safe Git maintenance &mdash; once a day per repository, GitLens runs the same routine upkeep `git gc` performs: packing loose objects, incremental repacking, and writing the commit-graph cache, which makes history-heavy features like the _Commit Graph_ open noticeably faster. These only reorganize objects the repository already has &mdash; history is never altered, more invasive optimizations are never applied automatically, and anything you configured yourself is left alone (requires Git 2.24+)
  - Adds an experimental _Repository Health_ visualization &mdash; a heart tab in the _Commit Graph_ that answers whether the repository needs attention: suggested optimizations appear as cards with meters and expandable trade-off explanations, and a ledger tracks each one's state &mdash; an optimization GitLens applied offers _Undo_. Includes _Run Maintenance Now_ and a _Show Repository Health_ command (part of `gitlens.graph.experimental.visualizations.enabled`)
  - Adds a _Repository Health_ banner &mdash; when Git has been measurably slow in a repository (or it is clearly large) and optimizations are suggested, a dismissible strip says what was noticed and opens _Repository Health_ in one click
- Adds smarter commit search to the _Commit Graph_
  - Adds intent-aware natural language search &mdash; "only show &hellip;" phrasings filter the graph to matches, "take me to &hellip;" phrasings jump to the commit, and empty results offer counted broader alternatives (e.g. _1000+ without the date filter_) instead of a dead end
  - Improves natural language search to understand the repository &mdash; branch, tag, worktree, and contributor names resolve to the real thing, misspelled author names get counted corrections (e.g. _7 as 'Keith Daulton'_), and a tooltip on the generated query explains how it was interpreted
  - Improves natural language failure handling &mdash; failed AI queries are repaired automatically, AI-unavailable searches offer _Search as text instead_, and invalid patterns offer _Fix with AI_
  - Adds `committer:`, `type:merge`, and `-message:` (exclude) operators to commit search in the _Commit Graph_ and _Search & Compare_
  - Changes search failures to say what actually went wrong &mdash; unknown references are reported by name, and a pattern that isn't valid regex now quietly matches literally while mid-typed, with a _Match Literally_ action when nothing matches
- Adds handing a pending rebase off to automatic (AI) conflict resolution from the _Interactive Rebase Editor_ ([#5714](https://github.com/gitkraken/vscode-gitlens/issues/5714))
  - Adds a _Start Auto-Rebase_ split button (with _Recompose_ tucked into its menu) &mdash; executes the todo exactly as you arranged it: the editor closes, the run takes over at the rebase's first stop, and a rebase that finishes without pausing is reported as completed
  - Changes deliberate stops to keep working the way you asked &mdash; `edit`/`break` hand back to you with a _Resume with AI_ path, and a commit message a `reword` or `squash` needs opens for you to write instead of being kept or auto-accepted without asking (also applies to _Continue Automatic Rebase_)
  - Adds persistent actions where escalations land &mdash; when a run stops for you, the _Commit Graph_'s **Resolve** panel keeps _Resume with AI_ and _Abort Rebase_ available (previously a transient toast), and the _Interactive Rebase Editor_'s paused view gains a _Continue with AI_ button
- Adds fixup commit support ([#1031](https://github.com/gitkraken/vscode-gitlens/issues/1031), [#2959](https://github.com/gitkraken/vscode-gitlens/issues/2959))
  - Adds a _Fixup Commit..._ action to commits in the _Commit Graph_ &mdash; seeds the commit box with a `fixup! <subject>` message, and any resolvable `fixup!` message turns the commit button into a split button: _Commit Fixup_, or _Commit Fixup & Squash_ to immediately fold it into its target
  - Adds a _Squash Fixups..._ action to the current branch and working-changes rows &mdash; squashes all pending fixup commits into their targets via `git rebase --autosquash`, warning first when pushed commits would be rewritten
  - Adds an _Autosquash_ toggle to rebasing in the _Git Command Palette_ &mdash; folds `fixup!` and `squash!` commits into the commits they target, defaulting from the `rebase.autosquash` Git config; interactive rebases open the _Interactive Rebase Editor_ with the fixups already folded (requires Git 2.44)
- Adds support for pushing tags ([#832](https://github.com/gitkraken/vscode-gitlens/issues/832)) &mdash; a new _Push Tag..._ action on tags in the views and the _Commit Graph_, and a _Git Push Tag..._ command in the Command Palette; choose the remote and confirm, with an optional force push for moved tags
- Adds a _GitKraken AI Usage_ card to the _Account_ section of _GitLens Settings_ ([#5743](https://github.com/gitkraken/vscode-gitlens/issues/5743)) &mdash; your weekly credit allowance, usage, and reset date, with an organization's shared pool split into your own draw against the rest, and a _Get more AI credits_ action on paid plans. A compact meter in the _Commit Graph_'s and _Home_'s account rollups opens the full card
- Adds an _Add to .gitignore_ action to untracked files in the _Commit Graph_ details and _Inspect_ views ([#5780](https://github.com/gitkraken/vscode-gitlens/issues/5780)) &mdash; appends the file's repo-relative path to the repository's `.gitignore`, creating it when missing
- Adds a _Show Resource Usage_ command &mdash; shows resource counts for long-lived GitLens caches and trackers plus extension-host memory usage in an output channel; an aggregate is sampled hourly as telemetry while the window is focused ([#5504](https://github.com/gitkraken/vscode-gitlens/issues/5504))
- Adds support for the Gemini 3.7 Flash AI model

### Changed

- Changes the _Git Command Palette_'s flows to one consistent, faster design &mdash; confirmations become action rows (safest pre-selected) plus checkbox toggles for options, replacing a row for every flag combination; toggles default from your Git config (`fetch.prune`, `merge.ff`), and _Force_ toggles visibly rewrite the action and never default on
  - Adds a _Don't Ask Again_ checkbox to skippable confirmations, with a gear that jumps to the `gitlens.gitCommands.skipConfirmations` setting
  - Changes pushing to three consistent confirmation shapes &mdash; ahead, behind, and unpublished &mdash; with the blocking reason shown above the choices and _Fetch_ beside the input
  - Changes switching to just the targets, with an _In a New Worktree_ toggle (remembered per repository); _Switch to Local Branch & Fast-Forward_ now works in a worktree
  - Changes stashing to ask for the message first so the final Enter stashes, and adds a _Stash Changes & Untracked_ mode plus a _Keep Staged_ toggle
  - Changes worktree creation to pick the location in place (_Root Folder..._ / _Specific Folder..._ rows) with an _After Creating_ choice, replacing the post-create prompt
  - Changes worktree deletion to a single step &mdash; remembered _Delete Branch_ / _Delete Upstream_ toggles, with uncommitted-changes warnings shown before Enter instead of as modals after
  - Changes subcommand menus to Title Case labels (e.g. _Merge Target_ instead of `mergeTarget`); typing the raw key still filters
- Improves working-changes (WIP) rows in the _Commit Graph_ &mdash; each row now carries a pill naming the branch it sits on; clicking it jumps to the branch's tip, its upstream, or its merge target when known. The stats pill leads with a worktree icon, other worktrees' rows carry a worktree marker, and when space is tight the label compacts to _WIP_ before the branch name truncates. Scoping the graph to a branch checked out in another worktree now pins that worktree's WIP row on top
- Improves the _Commit Graph_ side bar's _Overview_ panel &mdash; it now opens by default with proper loading, error, and empty states; branch cards toggle scope (click the scoped card again to clear it, announced to screen readers) and gain right-click context menus, a _Start Work..._ button sits between the groups, and a _Load More_ control pages in branches older than the _Recent_ timeframe
- Improves _Commit Graph_ keyboard navigation across not-yet-loaded history &mdash; `Ctrl`+`↓` jumps straight to the first parent even when it isn't loaded yet, `Alt`+`↓` and `]` keep loading until the next fork point or ref is found (with a cancellable _Looking for…_ indicator), and `Ctrl`+`←`/`→` can reach fork lanes that are hidden or not yet loaded
- Changes the _Commit Graph_'s details toggle into a split button ([#5747](https://github.com/gitkraken/vscode-gitlens/issues/5747)) &mdash; one click still shows and hides the panel, while a new chevron opens a placement menu with _Auto_, _Right_, and _Bottom_ thumbnails; choosing a placement while hidden also shows the panel, and closing it no longer resets `gitlens.graph.details.location` to `auto`
- Changes maximizing the _Commit Graph_'s details panel (or a maximized sheet) to overlay the graph instead of resizing it &mdash; the graph keeps its exact layout and restoring is instant
- Improves the _Account_ section of _GitLens Settings_ &mdash; a purpose-built card stack replaces the compact panel borrowed from the _Commit Graph_ header: identity, your plan (tier and status badges, trial progress, and its feature list), a next-tier upsell, your active organization, and refer-a-friend
- Improves the live preview in _GitLens Settings_ &mdash; it now sticks in view as you scroll a section instead of scrolling away, and the _Commit Graph_ preview reflects the Graph's current design
- Improves ref identity in the _Commit Graph_'s branch and tag sheet headers &mdash; remote and tag headers are more readable, and remote branch sheets lead with the hosting provider's icon
- Improves memory usage for blame results and Git command loading
- Improves switching into the experimental _Agent Kanban_ mode to feel instant &mdash; columns render immediately and session cards fill in right after, instead of building every card before anything appears
- Changes the default remote's `default` text badge in the _Commit Graph_ side bar to a check mark, matching the current branch marker

### Fixed

- Fixes the _Commit Graph_ wedging on "Loading commits…" when its initial load fails &mdash; it now shows what went wrong with a _Retry_ action
- Fixes the _Commit Graph_ getting stuck on "No repository open" when its webview reconnects before repository discovery finishes
- Fixes a blank _Commit Graph_ after a GitLens update &mdash; VS Code could restore the panel pointing at the old version's resources, requiring the tab to be closed and reopened ([#2990](https://github.com/gitkraken/vscode-gitlens/issues/2990))
- Fixes resumed agent sessions being reported as ended instead of live
- Fixes _Hide Remote_ in the _Commit Graph_ only hiding the selected branch instead of all of the remote's branches ([#5728](https://github.com/gitkraken/vscode-gitlens/issues/5728))
- Fixes opening changes and commit message actions targeting the wrong repository for a worktree that lives inside another repository's folder &mdash; opening a modified file's changes failed with "file not found", and generating, restoring, or committing a message via SCM wrote to the wrong _Source Control_ input ([#5773](https://github.com/gitkraken/vscode-gitlens/issues/5773))
- Fixes clicking an untracked nested repository's row in the _Commit Graph_'s _Compare_ panel opening a tab that fails to render ([#5657](https://github.com/gitkraken/vscode-gitlens/issues/5657))
- Fixes the _Commit Graph_'s _Review_ mode choosing focus areas from wrong file details on large change sets &mdash; newly added files counted as modified, and changed-line counts included unchanged context ([#5658](https://github.com/gitkraken/vscode-gitlens/issues/5658))
- Fixes a deep link that fails to open leaving its progress notification spinning indefinitely ([#5651](https://github.com/gitkraken/vscode-gitlens/issues/5651))
- Fixes _Load More Results_ in the _Commit Graph_'s search results bar doing nothing, and the results count including rows that weren't rendered
- Fixes deleting an unmerged branch from the _Commit Graph_ or views showing a generic error instead of offering the force-delete confirmation; a failed remote-ref delete where the ref no longer exists is also reported as such instead of a generic rejection
- Fixes refining a proposed commit plan after leaving the compose panel and returning, or after a refinement failed &mdash; the plan on screen was silently discarded and regenerated from scratch instead of being refined
- Fixes the _Commit Graph_ sometimes failing to scroll to a revealed row &mdash; on long jumps (deep links, _Show in Commit Graph_, and similar reveals) the selection landed but the viewport could strand partway
- Fixes the _Commit Graph_'s reference finder missing branches, tags, and worktrees created outside the extension, and Enter on a still-loading match not focusing the row once it lands
- Fixes focusing (clicking) a branch or tag pill in the _Commit Graph_ reordering the row's pills &mdash; a ref already showing no longer jumps to the front, and one collapsed behind the +N counter swaps into just the last slot; screen readers hear the refs in drawn order with the focused one called out
- Fixes keyboard focus dropping off the row a _Commit Graph_ jump lands on &mdash; arrow-key navigation kept working from where you left, not where you landed
- Fixes focusing a branch that is up to date with its merge target dimming the whole _Commit Graph_
- Fixes searching by author or committer in GitHub virtual repositories &mdash; `@username` dropped the first character of the username, and `@me` skipped the filter entirely for accounts without a display name
- Fixes the _Commit Graph_'s search history reading and saving under the first-opened repository after switching repositories in a multi-repo workspace
- Fixes quick picks opened from the _Commit Graph_ (repository switcher, search filter pickers, compare-ref choosers, _Add Co-authors_) sometimes closing immediately; pickers also no longer hang when dismissed while their items are still loading
- Fixes the _Commit Graph_'s _Working Changes_ details collapsing its file list to zero rows and clipping the commit box when the details panel is short &mdash; the panel now refuses to size below its content and keeps at least one file row visible
- Fixes the _Commit Graph_'s minimap resizing with the graph when the details panel changes size &mdash; it now holds its pixel height until there isn't room, and can no longer shrink below its minimum or get stuck in a sliver
- Fixes the _Commit Graph_'s minimap keeping its zoomed window when switching repositories instead of showing the new repository's full timeline
- Fixes the _Commit Graph_ side bar not refreshing when a worktree is created or removed
- Fixes errors in the _Commit Graph_'s _Pull Requests_ panel hiding the whole panel &mdash; failures now show inline with the tree and prior results still visible
- Fixes clean worktrees being hidden from the _Commit Graph_ overview bar's worktrees mode
- Fixes the _Commit Graph_ side bar's _Overview_ panel rendering empty ("No recent branch activity") when opened while the graph is still loading &mdash; it now shows its loading state and fills in once the branches arrive
- Fixes the _Recent_ header in the _Commit Graph_ side bar's _Overview_ panel wrapping onto a second line when the branch count runs wide
- Fixes branch cards in the _Commit Graph_ side bar's _Overview_ panel counting ended agent sessions in their agent indicator
- Fixes file tree tooltips positioning incorrectly and re-triggering while hovering in GitLens webviews ([#5769](https://github.com/gitkraken/vscode-gitlens/issues/5769))
- Fixes tooltips never appearing on disabled buttons in GitLens webviews
- Fixes the split conflict status icons rendering clipped in file trees &mdash; e.g. the _Commit Graph_'s _Working Changes_ details and _Resolve_ mode, and the _Inspect_ and _Patch Details_ views
- Fixes enriched autolinks being cached without bound for the life of the session &mdash; entries now expire after 30 minutes with a capped count ([#5504](https://github.com/gitkraken/vscode-gitlens/issues/5504))
- Fixes the account popover advertising out-of-date GitKraken AI allowances &mdash; both plans now read the correct per-plan figure in credits (Pro 1M and Advanced 2M per week)
- Fixes `:command`-scoped entries in `gitlens.gitCommands.skipConfirmations` never applying to subcommands &mdash; e.g. `stash-push:command` still confirmed when stashing from a view
- Fixes clicking a checkbox below the fold in _GitLens Settings_ scrolling the page out of view with no way to scroll back
- Fixes the _Get Started_ section's progress bars in _GitLens Settings_ rendering without their fill
- Fixes Student plan accounts being upsold Advanced instead of Pro in _GitLens Settings_ and the account rollup &mdash; both now target the next paid tier, matching the plan _Upgrade_ resolves to on its own
- Fixes the plan card in _GitLens Settings_ reading "Renews" for a subscription that has been cancelled or will not renew
- Fixes the trial line in _GitLens Settings_ reporting more days left than the trial is long (e.g. "15 of 14 days")
- Fixes _Switch Branch..._ separating _Open Worktree_ from _Open Worktree in New Window_ in the _Commit Graph_'s branch context menus

---

<a id="v19-0"></a>

## Version 19.0

#### Tuesday, August 12, 2026

GitLens 19 rebuilds the _Commit Graph_ from the ground up and gives it a new home &mdash; it now leads the GitLens side bar as its main view. It's noticeably faster on large repositories, hosts powerful tools for managing parallel work, is more configurable than ever, and completely keyboard navigable &mdash; rows and row actions included.

The graph also tells you far more at a glance. HEAD, its upstream, and your merge target are marked right on the rows, the reference pills, and the scroll bar &mdash; and hovering _Pull_ or _Push_ shows what's about to move, and where a pull would conflict, before you run it. Lane folding collapses stretches of history you don't need, a new _Changes_ column shows the size and shape of every commit, and selecting a branch or tag opens a full sheet with its tracking status, pull requests, issues, and what to do next. When you know the name of what you're after, press <kbd>/</kbd> and start typing &mdash; the graph moves to it as you go.

More of your day moves into the graph, too. Your open pull requests and remote branches join the side bar &mdash; including full support for GitHub's stacked pull requests, from layer badges to stack-aware merges &mdash; your account, walkthrough progress, and setup status sit in the header, and composing commits with AI now happens in the graph's details panel instead of a view of its own.

Keeping your branches up to date gets easier, too &mdash; with AI handling any conflicts along the way. Choose **Automatic Rebase** and GitLens runs the rebase start to finish, resolving every conflicting step, then hands you a summary explaining each decision it made &mdash; with one-click undo if you don't like what you see. GitLens can also verify SSH-signed commits now, with a new visual editor that builds the allowed-signers file Git needs for you.

<img src="/wp-content/uploads/gl-19-0-hero.png" class="help-center-img img-bordered">

### Graph is the New Home

#### A Graph That Shows You Around

The graph now has your back at every step. Signed out, you get a _Get Started with GitLens_ screen with a rotating spotlight of what GitLens unlocks &mdash; or a _Verify your email_ prompt when the connected account isn't verified. Completing sign-in lands on a welcome that introduces the graph and its walkthrough. Arrive via a specific task &mdash; composing, an AI review, comparing, or resolving conflicts &mdash; and the screen speaks to that task, then returns you to it once access is restored.

With no repository open, an empty state offers _Open a Folder_, _Clone a Repository_, and _Start a New Project_ (or _Open Remote Repository_ in web and virtual environments); Restricted Mode offers _Manage Workspace Trust_, refreshing to your history the moment trust is granted. A one-time prompt on first entry asks whether you'd rather run the graph vertically in the side bar or horizontally in the bottom panel, and moves it there for you.

Contextual how-tos fill in the rest: the first time you reach a feature &mdash; commit details, _Compose_, _Review_, conflicts, _Resolve_, _Compare_, the agents list, and more &mdash; a short tip opens right where you are. Dismiss it for good, or park it on a lightbulb to reopen any time, with "new" dots marking the features you haven't tried yet.

#### Your Account

An account pill sits in the graph header, ringed in a color that tracks your entitlement. Opening it rolls up your account, your walkthrough progress, and your _AI_, _Agents_, and _Integrations_ setup status &mdash; each deep-linking into the matching part of _GitLens Settings_, where the renamed _Show Account in Settings_ command also lands. The _Launchpad_ pill beside it becomes a compact severity dot &mdash; red when anything is blocked, yellow for other actionable work &mdash; with the full breakdown on hover.

### All-New Commit Graph

The _Commit Graph_ is now drawn by an all-new rendering engine, rewritten from the ground up. Loading, rendering, updating, and scrolling are all significantly faster, it uses substantially less memory, and it's far more accessible to keyboards and screen readers.

- **Grouped columns by default** &mdash; the _Graph_ and _Branches / Tags_ columns fold together into a compact anchor zone, with `gitlens.graph.lanes.grouped.min` and `gitlens.graph.lanes.grouped.max` controlling how many lanes render inline and how much of the row width they may claim.
- **Compact lanes by default** &mdash; a new `gitlens.graph.lanes.density` setting defaults to `compact`, and the author, date, and SHA columns start narrower.
- **Lane folding** &mdash; collapsible lane segments get expand/collapse chevrons in a fold strip beside the graph, configurable via `gitlens.graph.lanes.folding.enabled` and `gitlens.graph.lanes.folding.default`.
- **A responsive row layout** &mdash; the new `gitlens.graph.style` setting picks between `table` (single-line rows with columns) and `list` (stacked two-line rows), with `auto` switching to `list` when the view is too narrow for the columns &mdash; which is what you'll get in the side bar until you widen or move it.
- **A sticky timeline** &mdash; a pill groups scrolled rows into the same relative time buckets as the date column, expanding while you scroll to reveal the range and yielding when it overlaps something interactive, with optional separator lines between date groups (`gitlens.graph.timelineSeparators`).
- **Better columns** &mdash; inline filter buttons that reveal on hover, breadcrumbs showing the grouping hierarchy, double-click auto-fit that measures real date formats, a wider resize hit area, and a new _Quick Refresh_ button that re-lays out the lanes on demand without a refetch.
- **Full keyboard navigation** &mdash; the graph is now a standard WAI-ARIA tree with a comprehensive set of shortcuts for jumping around, folding lanes, toggling panels, and acting on rows &mdash; press <kbd>?</kbd> anywhere in the graph for the full reference.

#### Always Know Where You Stand

<!-- TODO: upload gl-19-0-row-markers.png -->

HEAD, its upstream, and your merge target are now called out everywhere the graph can call them out:

- **Role-colored reference pills and row markers** &mdash; HEAD in green, its upstream in a deeper green of the same hue (they're one branch shown in two places), and the merge target in its own role color. Each of those commits also gets a left-edge indicator that expands on hover, and references sitting on the same commit collapse into one.
- **A merge target scroll marker** &mdash; a full-width line on the scroll bar alongside the existing HEAD and upstream markers, themeable via `gitlens.graphScrollMarkerMergeTargetColor`. Right-clicking the rail toggles marker types in place, clicking a marker now selects and focuses its row instead of just scrolling near it, and the optional extra marker types are off by default to cut clutter.
- **Unpulled and unpushed row decorations** &mdash; commits waiting to be pulled are decorated in red and commits waiting to be pushed in green, so what's incoming and what's outgoing reads at a glance.
- **A quick-access overview bar** &mdash; the working changes (WIP) bar becomes a jumping-off point for your recent worktrees, with an indicator dot on any row carrying uncommitted changes. When the main row isn't sitting on HEAD it grows a jump pill for hopping to HEAD, the upstream (with ahead/behind), and the merge target. The new `gitlens.graph.overviewBar.visibility` setting controls when the bar appears &mdash; `worktrees` by default, or `always`, `dirtyWorktrees`, or `never`.
- **New default colors** &mdash; a perceptually-uniform lane palette for dark and high-contrast themes where no lane dominates, plus retuned HEAD and upstream greens that separate on brightness rather than saturation so they stay distinguishable with color blindness. Existing `gitlens.graphLane1Color`&ndash;`gitlens.graphLane10Color` customizations are honored, and branch highlighting now follows a branch's own lane and stops at its merge base.

#### Find and Jump Faster

- **Type-ahead reference finder** &mdash; press <kbd>/</kbd> anywhere in the graph (or the search icon in the references column header) and type to jump to a branch, tag, or worktree by name. The graph moves as you type, the match's pill fills and its row flashes, and <kbd>↑</kbd>/<kbd>↓</kbd> step through the rest. Abbreviated path segments work too &mdash; `d/f/foo` finds `debt/feature/foo`. References whose commits aren't loaded yet are offered dimmed, and <kbd>Enter</kbd> fetches and jumps to them.
- **Jump to the commits a pull or push will move** &mdash; hovering the _Pull_ or _Push_ button offers a jump to the commits involved, and <kbd>Alt</kbd>+click does the same without acting.
- **See where a pull would conflict** `PRO` &mdash; the pull preview warns in one line when pulling would hurt: either that uncommitted changes to the same files will block it, or how many files it would conflict in, simulated the way your `pull.rebase` setting says the pull will actually integrate. Requires Git 2.33 or later.
- **A minimap that shows up when it's useful** &mdash; the minimap is now hidden by default and appears while searching, so matches are visible as they stream in. When to show it lives in the new `gitlens.graph.minimap.defaultVisibility` setting (`onSearch`, `always`, or `hidden`).
- **Smoother reveals** &mdash; jumping to a reference, a search result, or a deep link now slides into the target row instead of cutting to it, and reliably lands on it even when the commit has to be paged in first.
- **Terminal links open in the Graph** &mdash; a new `gitlens.terminalLinks.showIn` setting (default: the _Commit Graph_) replaces the old boolean, and ranges like `main..feature` or `HEAD~3..HEAD` are now detected and opened as comparisons rather than linking only the trailing SHA.

#### Branch and Tag Sheets

Selecting a branch or tag reference now opens a sheet for it in the details panel. Each sheet carries an issue and pull request strip, upstream and merge-target relationship cards with tracking status and the relevant sync, rebase, or merge actions (click the counterpart's name to change it), AI _Explain_ and _Generate Changelog_ actions, and next-step rows tailored to the kind of ref. Tags default their comparison to the newest previous tag; remote branches compare against their merge target.

Sheets also carry _Focus_ and _Hide_ toggles, an _Open on Remote_ chip, and the agent sessions that ref's worktree can resume. They refresh in place as the graph changes and close when their ref disappears, and actions run against the branch's worktree when it's checked out somewhere else.

#### The Changes Column

A new _Changes_ column shows each commit's diffstat, with four visualizations you can switch between from the column header: **numbers**, **squares**, **bar**, and **bipolar** (a two-sided bar). It degrades gracefully as the column narrows &mdash; down to a single "churn ring" glyph at its narrowest &mdash; and uses positional, grayscale-friendly markers so deletions stay distinguishable without relying on color.

Because computing stats can be expensive on large repositories, the column is off by default and offers a one-time opt-in (`gitlens.graph.changesColumn.enabled`, with the visualization in `gitlens.graph.changesColumn.mode`).

#### Remote Branches in the Branches Side Bar

The _Branches_ panel gains a _Show Remote Branches_ toggle (sharing `gitlens.views.branches.showRemoteBranches` with the _Branches_ view), with remote branches keeping their prefix, grouping under their remote in tree layout, and showing their remote's provider icon. Every branch, worktree, and remote-branch row also picks up an inline _Focus_ action, plus pinned and current-branch indicators.

### Stacked Pull Requests

GitLens now understands GitHub's stacked pull requests, so a stack reads as one piece of work instead of a pile of unrelated branches.

Selecting any layer opens its pull request sheet with a **stack map** &mdash; the whole stack laid out in order, so you can see how many layers there are, where you sit among them, and step to any other. In the side bar, a stack's layers group together in the new _Pull Requests_ panel, and each layer is badged with its position on reference pills and in hovers. _Focus Pull Request_ on any layer scopes the graph to the whole stack rather than the single branch you clicked.

Merging routes through GitHub's stack-aware merge, with a confirmation naming how many pull requests will land. _Launchpad_ picks up the same context &mdash; stacked pull requests show their layer position, and merging one becomes _Merge Stack..._, running under cancellable progress and reporting any failures.

### Pull Requests in the Graph

A new _Pull Requests_ panel lists the repository's open pull requests, most-recently-updated first, each with a _Launchpad_-style status indicator when it needs attention, a fork glyph when it came from a fork, and a hover adding CI, review, and change-size signals. Rows lead with a state-aware action &mdash; _Switch to Branch..._, _Open in Worktree..._, or _Open Worktree in New Window..._ &mdash; then _Open Pull Request on Remote_ and _Focus_, which scopes the graph to the pull request's branch, offering to fetch it first when it isn't local yet. When the remote has no integration connected, the panel offers to connect one instead of showing an empty list.

Selecting a pull request anywhere in the graph opens its details sheet &mdash; details, description, and stack map, with switch and worktree actions, _Compare Changes_, _Review Changes_ (an in-place AI review), _Review with Agent..._, and a split merge button offering merge, squash, or rebase that confirms in place.

### AI and Agentic Feature Improvements

#### Automatic Rebase, Start to Finish

The AI **Resolve** mode introduced in 18.2 can now drive an entire rebase. Choose _Automatic Rebase_ in the rebase quick menu, or _Continue Automatic Rebase_ on an already-paused rebase, and each conflicted step is resolved, staged, and continued automatically &mdash; pausing for review only when confidence falls below the new `gitlens.ai.autoRebase.confidenceThreshold` setting, or when something genuinely needs you.

The run narrates itself in the _Commit Graph_'s **Resolve** panel rather than a progress notification: which step it's on, a progress bar, what it's doing right now, and every conflict already resolved with its strategy, confidence, and reasoning. When automation stops, the same panel fills in with the resolutions it already computed. A _Cancel Rebase_ action restores the branch's pre-rebase state mid-run, and on completion a per-step summary shows every file's strategy and reasoning with before/after diffs, plus a validated _Undo_ that refuses if the branch has moved since.

AI Resolve can now consult your repository &mdash; when a conflict hunk is too ambiguous on its own, it can read the file, blame or log the lines in question, search for other uses of the symbols involved, and diff the two sides before choosing. Consultation is read-only and bounded, reported as it happens in the **Resolve** panel, and each resolution's reasoning cites what it consulted. Your AI file-exclusion rules (`gitlens.ai.exclude.files` and `.aiignore`/`.cursorignore`/`.aiexclude`) now apply to everything AI reads, not just what it's asked to change.

A new `gitlens.ai.resolveConflicts.customInstructions` setting gives AI standing guidance for every conflict it resolves &mdash; "prefer the incoming side for lock files", say &mdash; with instructions you type for a single run still applying on top.

The rebase quick menu's confirm step is now three options &mdash; _Rebase_, _Automatic Rebase_, and _Interactive Rebase_ &mdash; with an _Update Branches_ toggle applying `--update-refs` to whichever you pick.

#### Composing Commits

The standalone _Commit Composer_ webview is gone &mdash; composition now lives in the _Commit Graph_'s details panel. Recompose on a branch, a commit selection, or a single commit resolves a covering range and seeds the inline scope picker, merge topologies and interior ranges included. A new top drag handle scopes a compose to staged changes only, commits only, or an arbitrary range, and recompose anchors on the branch's worktree, offering to create one when the branch isn't checked out anywhere.

AI composition itself gets sharper too: commit message convention detection is more accurate, noise hunks are filtered out of proposals, and very large change sets are handled far better.

#### Code Review

Review mode can now be scoped to unstaged changes only, and reviews of working changes include untracked files &mdash; staged into a scratch index rather than your repository's, so a review can never disturb what you have staged.

#### New Model and Agent Harness Support

GitLens adds support for Gemini 3.6 Flash and 3.5 Flash-Lite, and expands the set of models available through GitKraken AI &mdash; the current OpenAI, Gemini, and Anthropic models straight from your GitKraken account, no API key of your own required.

Per-feature AI model selection is now available for _Composing Commits_, _Reviewing Changes_, and _Resolving Conflicts_, each using a different model from your default.

A new Agents configuration in the _GitLens Settings_ view that lists every detected coding agent grouped by kind, each with a _Default_ agent picker and, for CLI agents, easy controls to install GitKraken MCP and Claude Hooks.

### Verify SSH-Signed Commits

A new _Edit SSH Allowed Signers_ editor builds the `allowed_signers` file Git needs to verify SSH-signed commits. Open it from the Command Palette, or from _Add to allowed signers…_ on an unverified SSH signature in a commit's signature details. It finds candidate signers in the public keys embedded in your repository's SSH-signed commits &mdash; entirely offline, on any host &mdash; and cross-checks them against each signer's registered SSH signing keys when a GitHub or GitLab integration is connected, marking keys as signed-here, provider-verified, or both. Review each signer's avatar, email, fingerprint, provenance, and signed-commit count, choose who to include, pick the target file, and optionally point `gpg.ssh.allowedSignersFile` at it globally or per repository &mdash; merging into an existing file without clobbering your manual entries.

### A Deeper Settings Page

The _GitLens Settings_ page rebuilt in 18.3 gains new sections and a reorganized category rail, grouped into _Setup_, _Integrations_, _Views_, _Editor_, and _General_.

- **_Account_** leads the rail &mdash; your account, plan, and subscription actions, with your avatar on the rail item once you're signed in.
- **_Get Started_** is where a first open now lands &mdash; a four-step setup launchpad (sign in, connect integrations, choose an AI model, set up agents) with a completion ring tracking what's left.
- **_Agents_** lists every detected coding agent grouped by kind, each with a _Default_ picker and, for CLI agents, install controls for GitKraken MCP and Claude Hooks.
- **_Custom Remotes_** configures the `gitlens.remotes` setting in the UI instead of hand-editing JSON.
- **Per-feature AI models** &mdash; _Composing Commits_, _Reviewing Changes_, and _Resolving Conflicts_ can each use a different model from your default, with every row naming the model it will actually use and a _Use Default_ action to drop an override.

### Performance and Reliability

- **Faster, smaller webview payloads** &mdash; improved compression and payload sizes, batching, and less extension-to-webview chatter over IPC.
- **Less Git work** &mdash; work avoided or delayed, better caching and sharing, leaner Git calls, and improved Git priority queueing to cut latency.

---

### Added

- Adds a new home for GitLens &mdash; the _Commit Graph_ now leads the GitLens side bar as its main view (only the default location changes, so a graph you moved yourself stays put, and a one-time prompt offers the bottom panel), adapting to the side bar's width with compact list-style rows and the details panel below the graph; widen or move the view for the columnar table layout ([#5545](https://github.com/gitkraken/vscode-gitlens/issues/5545))
  - Adds empty states &mdash; with no repository open, offers _Open a Folder_, _Clone a Repository_, and _Start a New Project_ actions (an _Open Remote Repository_ action in web/virtual environments), and in a workspace running in Restricted Mode offers _Manage Workspace Trust_, refreshing to your history as soon as trust is granted ([#5408](https://github.com/gitkraken/vscode-gitlens/issues/5408))
  - Adds a sign-in experience &mdash; signed-out users see a _Get Started with GitLens_ screen with a rotating spotlight of what GitLens unlocks, completing sign-in lands on a welcome that introduces the graph and its walkthrough, and arriving via a specific task (composing, an AI review, comparing, or resolving conflicts) shows messaging for that task and returns you to it once access is restored ([#5534](https://github.com/gitkraken/vscode-gitlens/issues/5534))
  - Adds an account pill to the header &mdash; ringed in a color tracking your entitlement, opening a rollup with your account, walkthrough progress, and _AI_, _Agents_, and _Integrations_ setup status, each deep-linking into _GitLens Settings_; the _Show Account_ command (renamed _Show Account in Settings_) now opens there too ([#5522](https://github.com/gitkraken/vscode-gitlens/issues/5522))
  - Adds contextual how-tos (coach marks) &mdash; the first time you reach a feature (commit details, _Compose_, _Review_, conflicts, _Resolve_, _Compare_, the agents list, the overview bar, and more) a short tip opens right where you are; dismiss it for good, or park it on a lightbulb to reopen any time, with "new" dots on the features you haven't tried yet ([#5516](https://github.com/gitkraken/vscode-gitlens/issues/5516))
  - Adds _What's New_, _Help Center_, _Report Issue (GitHub)_, and _Share Feedback (GitHub)_ to the graph's "..." menu and the _Welcome_ view toolbar
- Adds an all-new high-performance rendering engine on the _Commit Graph_, rewritten from the ground up &mdash; loading, rendering, updating, and scrolling are significantly faster, it uses substantially less memory, and it is far more keyboard and screen reader accessible
  - Adds column grouping for the _Graph_ and _Branches / Tags_ columns (enabled by default) for a more compact layout, and lane folding to collapse commit histories that aren't relevant right now
  - Adds new perceptually-uniform lane colors for dark and high-contrast themes (existing `gitlens.graphLane1Color`&ndash;`gitlens.graphLane10Color` customizations are honored), and branch highlighting that follows a branch's own lane and stops at its merge base
  - Adds row markers for HEAD, its upstream, and its merge target &mdash; role-colored reference pills (HEAD in a clearer green, its upstream the deeper green of the same hue) with matching markers on the scroll bar &mdash; plus row decorations for commits waiting to be pulled (red) or pushed (green)
  - Adds a context menu to the scroll marker rail to toggle marker types in place, and clicking a marker now selects and focuses its row instead of just scrolling near it; the optional additional marker types are now off by default to reduce clutter
  - Adds previews of what a pull or push would do to the _Pull_ and _Push_ buttons &mdash; hovering offers a jump to the commits involved (Alt+click jumps without acting), and the pull preview warns when uncommitted changes would block the pull or how many files would conflict, simulated the way your `pull.rebase` setting will actually integrate (conflict detection requires GitLens Pro and Git 2.33+)
  - Adds a "quick-access" overview bar for showing and quickly jumping to recent worktrees &mdash; use the new `gitlens.graph.overviewBar.visibility` setting to control when it appears
  - Adds an indicator dot to working changes (WIP) rows with uncommitted changes, and a "jump pill" on the main WIP row when it isn't directly attached to HEAD, for easy jumps to HEAD, the upstream, and the merge target
  - Adds _Apply / Pop Stash..._ and _Apply Copied Changes (Patch)_ options to working tree (WIP) rows &mdash; invoked from another worktree's WIP row, the changes are applied into that worktree
  - Adds a type-ahead reference finder &mdash; press `/` (or use the search icon in the references column header) and type to jump to a branch, tag, or worktree; &uarr;/&darr; step through matches, and references that aren't loaded yet are offered too, fetched only when you press Enter
  - Adds a _Show Remote Branches_ toggle to the side bar's _Branches_ panel &mdash; lists the default remote's branches alongside local ones (falling back to `origin` when no default remote is set), shared with the _Branches_ view via `gitlens.views.branches.showRemoteBranches`; remote branches also become pickable in the _Focus Branch_ scope picker
  - Adds visualization modes for the _Changes_ column &mdash; numbers, squares, bar, or a two-sided bar, with compact versions as the column narrows &mdash; behind a one-time opt-in overlay to avoid impacting performance by default
  - Adds a sticky timeline that names the time period you're scrolled to, with a new `gitlens.graph.timelineSeparators` setting to draw dividers between date groups
  - Adds comprehensive keyboard shortcuts &mdash; jump to HEAD, upstream, merge target, or working changes with `h`/`u`/`t`/`w`, fold lanes with &larr;/&rarr;, toggle the minimap, side bar, and details with `Alt`+`M`/`S`/`D`, hold `Ctrl` to highlight the focused branch's lane, peek the focused commit's rich hover with `i`, and press `?` for the full reference; `Esc` now closes one thing per press
- Adds an automatic rebase that resolves conflicts end-to-end with AI &mdash; choose _Automatic Rebase_ in the rebase quick menu to resolve, stage, and continue each conflicted step, narrated live in the _Commit Graph_'s **Resolve** panel with each file's strategy, confidence, and reasoning, and a _Cancel Rebase_ action that restores the branch's pre-rebase state. It pauses for review when confidence falls below `gitlens.ai.autoRebase.confidenceThreshold`, and finishes with a per-step summary and a validated _Undo_ ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Adds repository consultation to AI-powered conflict resolution _(Preview)_ &mdash; when a conflict hunk is ambiguous on its own, AI can now read the file, blame or log the lines in question, search for other uses of the symbols involved, and diff the two sides before choosing a resolution. Consultation is read-only and bounded, reported as it happens in the _Commit Graph_'s **Resolve** panel and the automatic rebase, and each resolution's reasoning cites what was consulted; your AI file-exclusion rules (`gitlens.ai.exclude.files` and `.aiignore`/`.cursorignore`/`.aiexclude`) now apply to everything AI reads ([#5581](https://github.com/gitkraken/vscode-gitlens/issues/5581))
- Adds a `gitlens.ai.resolveConflicts.customInstructions` setting &mdash; standing guidance for AI conflict resolution (e.g. "prefer the incoming side for lock files"), applied to every conflict AI resolves; guidance typed for a single run still applies on top
- Adds rich pull request support to the _Commit Graph_ &mdash; browse, focus, review, and merge pull requests without leaving the graph
  - Adds a _Pull Requests_ panel to the side bar &mdash; the repository's open pull requests, most-recently-updated first, with _Launchpad_-style status indicators and rich hovers; rows offer switch and worktree actions, _Open Pull Request on Remote_, and _Focus_, which scopes the graph to the pull request's branch &mdash; offering to fetch it first (even from a fork) when it isn't local yet
  - Adds a pull request details sheet &mdash; selecting a pull request anywhere in the graph opens its details, description, and stack map, with switch and worktree actions, _Compare Changes_, _Review Changes_ (an in-place AI review), _Review with Agent..._, and a split merge button (merge, squash, or rebase) that confirms in place
  - When the repository's remote has no integration connected, the panel offers to connect one and fills in without a reload
- Adds support for GitHub's stacked pull requests
  - Badges each layer with its position on ref pills and hovers, and groups a stack's layers in the new _Pull Requests_ panel
  - _Focus Pull Request_ on any layer scopes the graph to the whole stack, and the pull request sheet's stack map lets you step between layers
  - Merging routes through GitHub's stack-aware merge, with a confirmation naming how many pull requests will land
  - Adds stack context to _Launchpad_ &mdash; stacked pull requests show their layer position, and merging one becomes _Merge Stack..._, running under cancellable progress with failures reported
- Improves the _Commit Graph_'s details panel &mdash; smarter placement and new full-height sheets
  - Docks to whichever side of the graph has the room, gains a maximize control (automatic when entering compose, review, resolve, or compare, via `gitlens.graph.details.maximizeOnMode`), and double-clicking a splitter resets it
  - Adds a branch and tag details sheet &mdash; selecting a branch or tag reference opens its issue and pull request, upstream and merge-target relationship cards with sync, rebase, and merge actions (rooted at the ref's own worktree), _Focus_ and _Hide_ toggles, _Open on Remote_, and AI-powered _Explain_ and _Generate Changelog_ actions &mdash; for tags, the changelog covers what shipped since the previous tag
  - Adds keyboard support to file trees &mdash; `Space` toggles a row's checkbox (e.g. staging), `Alt`+`Space` unchecks a mixed one (matching `Alt`+click), and `Ctrl`/`Cmd`+`F` opens and focuses the tree's search/filter box
- Adds AI agent session enhancements to the _Commit Graph_ and _Home_ &mdash; a _Resume Agent Session..._ option on working tree (WIP) rows to open live sessions or resume past ones, sessions listed in the working-changes and branch details, and completed sessions from the last 30 days available behind a filter toggle in the _Agents_ panel, each with _Resume Session_ and _Archive Session_ actions
- Adds support for locked worktrees &mdash; new _Unlock Worktree_ commands, and deleting a locked worktree now surfaces the lock's reason with an offer to force-delete instead of failing with a raw Git error
- Improves the _GitLens Settings_ page with new sections and a reorganized category rail ([#5392](https://github.com/gitkraken/vscode-gitlens/issues/5392))
  - Adds an _Account_ section leading the rail &mdash; your account, plan, and subscription actions, with your avatar on its rail item when signed in
  - Adds a _Get Started_ section, where a first open now lands &mdash; a four-step setup launchpad (sign in, connect integrations, choose an AI model, set up agents) with a completion ring tracking what's left
  - Adds an _Agents_ section &mdash; every detected coding agent grouped by kind, each with a _Default_ picker and, for CLI agents, install controls for GitKraken MCP and Claude Hooks
  - Adds a _Custom Remotes_ section &mdash; configures the `gitlens.remotes` setting in the UI instead of hand-editing JSON
  - Adds per-feature AI model controls to the _AI_ section &mdash; the model for _Composing Commits_, _Reviewing Changes_, and _Resolving Conflicts_ can each be set independently of the default, with each row naming the model it will actually use and a _Use Default_ action to drop an override
  - Reorganizes the category rail into _Setup_, _Integrations_, _Views_, _Editor_, and _General_ groups
- Adds an optional `mode` parameter to the `graph` command deep link (e.g. `vscode://eamodio.gitlens/link/command/graph?mode=compose`) &mdash; opens the _Commit Graph_ directly into _Compose_ or _Review_ ([#5226](https://github.com/gitkraken/vscode-gitlens/issues/5226))
- Adds an _Edit SSH Allowed Signers_ editor &mdash; discovers signers from this repository's SSH-signed commits and from connected GitHub and GitLab signing keys, then writes an `allowed_signers` file (optionally pointing `gpg.ssh.allowedSignersFile` at it) so Git can verify SSH-signed commits. Open it from the Command Palette, or from _Add to allowed signers…_ on an unverified signature ([#5469](https://github.com/gitkraken/vscode-gitlens/issues/5469))
- Adds support for Gemini 3.6 Flash and Gemini 3.5 Flash-Lite AI models

### Changed

- Changes the _Home_, _Cloud Patches_, and _Cloud Workspaces_ views to be hidden by default &mdash; applied once on upgrade too (landing you on the Graph in its new home); each remains available from the Command Palette and stays visible once shown ([#5545](https://github.com/gitkraken/vscode-gitlens/issues/5545))
- Changes commit composition to happen in the _Commit Graph_'s details panel, now the single place to compose &mdash; the standalone _Commit Composer_ editor is gone, and every entry point (the _Compose Commits..._ command, the _Source Control_ view, the GitLens views, _Home_, the GitKraken MCP tools, and the _Interactive Rebase Editor_) opens compose in the graph instead. _Recompose_ on a branch, a commit selection, or a single commit works there too, and a new drag handle narrows a compose to staged changes only, commits only, or a range of the two. AI composition also improves &mdash; more accurate commit message convention detection, noise hunks filtered out of proposals, and better handling of very large change sets ([#5506](https://github.com/gitkraken/vscode-gitlens/issues/5506))
- Changes the rebase quick menu's confirm step &mdash; an _Update Branches_ toggle now applies `--update-refs` to whichever rebase you choose (_Rebase_, _Automatic Rebase_, or _Interactive Rebase_), replacing the separate _& Update Branches_ variants ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Changes paused-rebase auto-open (`gitlens.rebaseEditor.openOnPausedRebase`) to only open for rebases you're driving from GitLens &mdash; a new `auto` value, now the default, ignores paused rebases started outside GitLens (terminals, agents, other tools), which previously popped open the _Interactive Rebase Editor_ or _Commit Graph_ uninvited; set it to `true` to restore the previous behavior ([#5686](https://github.com/gitkraken/vscode-gitlens/issues/5686), [#4954](https://github.com/gitkraken/vscode-gitlens/issues/4954))
- Changes paused merge, rebase, cherry-pick, and revert conflicts to surface in one place &mdash; the _Commit Graph_'s working changes (WIP) details, or the _Interactive Rebase Editor_ for rebases when the graph isn't usable
- Changes the _Commit Graph_'s paused-operation bar into a state-driven strip &mdash; a labeled primary action (e.g. _Resolve 3 Conflicts_), an all-resolved ready state, a "paused at step m/t" link that jumps to the commit being applied, _Continue with Empty Commit_ where Git offers it, and paused reverts can now be continued end-to-end
- Changes the _Commit Graph_ sidebar to be unpinned by default &mdash; it floats over the graph and auto-collapses when it loses focus or on Esc; pin it (or set `gitlens.graph.sidebar.pinned`) to restore the shared-space layout ([#5447](https://github.com/gitkraken/vscode-gitlens/issues/5447))
- Changes the _Commit Graph_ header's jump-to-reference button into a _Focus Branch_ control &mdash; clicking focuses (scopes) the graph to the current branch (clicking again clears it), and Alt-clicking opens the _Focus Branch_ picker; branch and worktree rows in the side bar gain an inline _Focus_ action too ([#5556](https://github.com/gitkraken/vscode-gitlens/issues/5556))
- Improves branch pinning in the _Commit Graph_ &mdash; the off-screen HEAD and pinned-branch indicators merge into a single waypoints capsule, the pinned branch gets its own scroll bar marker, unpinning now lives on the reference pill itself, and side bar rows show pin and current-branch indicators ([#5409](https://github.com/gitkraken/vscode-gitlens/issues/5409), [#5626](https://github.com/gitkraken/vscode-gitlens/issues/5626), [#5624](https://github.com/gitkraken/vscode-gitlens/issues/5624))
- Changes the _Commit Graph_ header's _Launchpad_ pill into a compact indicator &mdash; a severity dot on the rocket (red when anything is blocked, yellow for other actionable work) with the full breakdown on hover ([#5522](https://github.com/gitkraken/vscode-gitlens/issues/5522))
- Changes the _Commit Graph_ minimap to be hidden by default and shown while searching &mdash; controlled by a new `gitlens.graph.minimap.defaultVisibility` setting (`"onSearch"`, the new default, `"always"`, or `"hidden"`); `gitlens.graph.minimap.enabled` goes back to a plain boolean for whether the minimap is available at all &mdash; set `defaultVisibility` to `"always"` to keep the previous always-shown behavior ([#5598](https://github.com/gitkraken/vscode-gitlens/issues/5598))
- Changes where terminal links open &mdash; a commit, branch, or tag clicked in the terminal now opens in the _Commit Graph_ by default, configurable via the new `gitlens.terminalLinks.showIn` setting (replacing `gitlens.terminalLinks.showDetailsView`; existing values migrate), and ranges like `main..feature` now open as a comparison
- Changes when the _Commit Graph_ side bar's _Worktrees_ panel loads each worktree's working change counts &mdash; a fast check settles clean vs. dirty and the `+N ~M -K` breakdown loads only when you hover a row, instead of a `git status` per worktree up front
- Changes the Pro feature gate to adapt to constrained spaces &mdash; the feature list, messaging, and spacing compact in narrow or short placements without hiding content ([#5519](https://github.com/gitkraken/vscode-gitlens/issues/5519))
- Improves switching AI models &mdash; with a provider already selected, the picker opens directly to its model list, with a _Change AI Provider_ entry keeping provider switching one pick away ([#5584](https://github.com/gitkraken/vscode-gitlens/issues/5584))
- Changes _GitLens: Reset Stored Data..._ &mdash; adds AI model, GitKraken CLI install, and _Commit Graph_ cache resets, and a full reset now prompts to reload the window
- Improves _Commit Graph_ and commit details performance &mdash; reference metadata loads through a bounded pool and streams in as it lands, background worktree probes no longer compete with the graph's own Git work, holding a navigation key no longer spawns a Git process per row crossed, and commit details open faster and stay interactive during refreshes
- Renames the _Home_ view's _GitHub Issues_ and _GitHub Discussions_ actions to _Report Issue (GitHub)_ (now opening the new-issue template chooser) and _Share Feedback (GitHub)_

### Fixed

- Fixes blame going stale for open files after you commit, pull, or switch branches outside of VS Code &mdash; blame annotations, hovers, and CodeLens kept showing an older commit for lines a newer commit had changed, until the file was reopened or the window reloaded; this affected repositories at any path containing an uppercase character &mdash; nearly all of them on Windows and macOS ([#5523](https://github.com/gitkraken/vscode-gitlens/issues/5523))
- Fixes diffs opened from GitLens views and details landing at the top of the file instead of scrolling to the first change
- Fixes per-file actions (stage, unstage, conflict options) missing from working-changes file rows in the _Commit Graph_ and _Inspect_ views ([#5548](https://github.com/gitkraken/vscode-gitlens/issues/5548))
- Fixes GitLens silently pinning your AI provider to Copilot without you ever choosing it &mdash; GitKraken AI is now the only provider selected automatically, nothing is written to `gitlens.ai.model` unless you pick a model yourself, and settings written by the old behavior are cleared on upgrade, leaving choices you made yourself untouched ([#5612](https://github.com/gitkraken/vscode-gitlens/issues/5612))
- Fixes a scoped AI model selection leaking into the global default &mdash; resolving a model for _Review_ or _Compose_ could write that operation's preferred model into `gitlens.ai.model` for every other AI feature
- Fixes AI conflict resolution failing outright on models that don't accept a temperature (seen as "upstream AI provider error (OpenAI HTTP 400)" on GPT-5 models via GitKraken AI)
- Fixes AI conflict resolution failing with _No active merge, rebase, or cherry-pick conflicts to resolve_ when conflicts exist without a paused Git operation, such as after a `git stash pop` ([#5487](https://github.com/gitkraken/vscode-gitlens/issues/5487))
- Fixes focusing (scoping) the _Commit Graph_ on a branch sometimes dimming the whole graph instead of re-rooting it, dropping the focused branch's own commits, doing nothing for remote branches, and the focused branch or its working changes row being filtered out from under its own scope
- Fixes the _Commit Graph_'s hidden branches/tags list not identifying which refs are hidden &mdash; entries now name their remote, group by type, and refs that no longer exist are no longer listed or counted
- Fixes branches with parentheses in their names (e.g. `feat/(wip)`) being treated as a detached HEAD &mdash; the working changes row vanished and the toolbar showed a SHA instead of the branch name
- Fixes a transient Git or network failure being cached and served as a real answer for the rest of the session &mdash; blanked branch/tag lists, an authoritative "no issues" for a branch, or stale commit counts that never recovered
- Fixes a branch deleted or renamed through GitLens leaving its stored base and merge target behind &mdash; a new branch reusing the name no longer inherits the dead branch's merge target
- Fixes AI agent sessions being attributed to the wrong worktree, and sessions needing input sometimes showing _Allow_/_Deny_ actions that could not work &mdash; a live permission ask can also no longer be denied by an unrelated event from the same session
- Fixes AI agent sessions from other AI CLIs (Codex, GitHub Copilot CLI, Cursor, OpenCode, Antigravity) appearing as _Claude Code_ sessions on _Home_ and the _Commit Graph_ ([#5715](https://github.com/gitkraken/vscode-gitlens/issues/5715))
- Fixes a transient _Launchpad_ failure (e.g. an expired token at startup) sticking the _Commit Graph_ header on an error state for up to 30 minutes with refresh doing nothing
- Fixes the _Commit Graph_ side bar's _Worktrees_ panel running per-worktree Git commands while collapsed and without bound &mdash; on repositories with many worktrees this could saturate GitLens's Git queue and hold up other Git work
- Fixes the _Commit Graph_ working changes (WIP) details continuing to show files after they were committed or discarded outside of VS Code
- Fixes working-changes actions invoked from another worktree's row (copy patch, compose, explain, review) acting on the current worktree instead of the row's worktree
- Fixes _Copy Changes (Patch)_ producing an empty or incomplete patch &mdash; fully-staged selections reported "No changes found to copy", mixed selections silently dropped their staged changes, and renamed files copied as a bare add of the new path
- Fixes the _Commit Graph_ view's progress indicator repeatedly flashing while nothing appears to change (most noticeable after the window regains focus)
- Fixes the _Commit Graph_ sidebar list hovers repeatedly opening and closing in narrow viewports, and the sidebar restoring at its minimum width after a reload
- Fixes rows in the _Commit Graph_ side bar panels nudging their trailing decorations to the left on hover
- Fixes search results being invisible on the _Commit Graph_'s minimap exactly where you were looking &mdash; result markers were drawn underneath the visible-range band
- Fixes working tree (WIP) search results (`type:wip`) all being marked at today on the _Commit Graph_'s minimap &mdash; each worktree's WIP row is now marked at the commit it's anchored to
- Fixes clearing a natural language search in the _Commit Graph_ silently re-populating the search box a moment later
- Fixes the paused-operation bar offering an enabled _Continue_ while Git was still waiting for you to save and close the commit message tab &mdash; the bar now holds an in-progress state until the operation actually settles ([#5656](https://github.com/gitkraken/vscode-gitlens/issues/5656), [#5668](https://github.com/gitkraken/vscode-gitlens/issues/5668))
- Fixes _Recompose_ failing outright when branches or tags point at commits inside the range being recomposed &mdash; it now warns that those references won't follow the new history and recomposes if you continue ([#5515](https://github.com/gitkraken/vscode-gitlens/issues/5515))
- Fixes the _Commit Graph_'s compose preview misaligning changes for the second and later proposed commits, and dropping earlier hunks of a file renamed with edits &mdash; preview only; applying the compose was unaffected ([#5596](https://github.com/gitkraken/vscode-gitlens/issues/5596), [#5606](https://github.com/gitkraken/vscode-gitlens/issues/5606))
- Fixes excluding an untracked nested repository from a compose having no effect &mdash; it was still sent to AI and still committed; its row in _Files Changed_ also now names the directory instead of being blank ([#5611](https://github.com/gitkraken/vscode-gitlens/issues/5611), [#5629](https://github.com/gitkraken/vscode-gitlens/issues/5629))
- Fixes leaving the _Commit Graph_'s compose or resolve panel discarding your typed AI instructions and _Refine_ state &mdash; both are restored when you return
- Fixes a review of your working changes never including untracked files, and failing with _No changes found_ when untracked files were the only unstaged changes ([#5586](https://github.com/gitkraken/vscode-gitlens/issues/5586))
- Fixes files you excluded from a review being able to reach AI anyway via a cached pre-exclusion diff ([#5630](https://github.com/gitkraken/vscode-gitlens/issues/5630))
- Fixes changing `gitlens.ai.ollama.url` keeping the previously resolved model and model list &mdash; the model is re-resolved against the new server ([#5633](https://github.com/gitkraken/vscode-gitlens/issues/5633))
- Fixes the compare panel's "commits in between" count reading 0 when the newer commit was picked first ([#5547](https://github.com/gitkraken/vscode-gitlens/issues/5547))
- Fixes signing back in after a sign-out interrupted a _Commit Graph_ comparison reopening the comparison on different references ([#5671](https://github.com/gitkraken/vscode-gitlens/issues/5671))
- Fixes the _Commit Graph_ header's account/subscription state never updating after the view loads &mdash; sign-in/sign-out, organization switches, and plan changes now update live instead of requiring a reload ([#5513](https://github.com/gitkraken/vscode-gitlens/issues/5513))
- Fixes the account panel not showing your account when you aren't in an organization &mdash; solo accounts now show their avatar, name, and email in _Home_ and the _Commit Graph_
- Fixes GitLens needing a window reload to notice when you trust a workspace &mdash; repositories are now discovered as soon as you grant trust
- Fixes issue and pull request loading failing wholesale when an author's GitHub account has been deleted &mdash; one failing item or connection no longer discards the rest
- Fixes self-managed cloud integrations (e.g. GitHub Enterprise, GitLab Self-Hosted) repeatedly issuing a token request the server rejects on every session refresh, and legacy connections stuck reported as connected with no usable token ([#5497](https://github.com/gitkraken/vscode-gitlens/issues/5497))
- Fixes a healthy cloud integration being fully disconnected when a backend error lands during an automatic session refresh &mdash; only a definitive "no token" response disconnects it now, so transient failures self-heal ([#5569](https://github.com/gitkraken/vscode-gitlens/issues/5569))
- Fixes a webview quietly going stale after it reconnects (e.g. moving the _Commit Graph_ between panels) &mdash; change notifications stopped flowing and an active search could be silently dropped
- Fixes Alt/Ctrl/Shift-dependent UI staying engaged when focus moves from a GitLens view to an editor or quick pick with the key held
- Fixes commit details showing the autolinks strip when `gitlens.views.commitDetails.autolinks.enabled` is off
- Fixes file tree search boxes only matching file names &mdash; paths with folder separators (e.g. `src/git/`) now match
- Fixes the _Choose Commit..._ and _Search for Commit_ buttons in the _Inspect_ view's empty state doing nothing when clicked

### Removed

- Removes the _Pro_ feature badge from the _Commit Graph_ header &mdash; the _Start New_ menu now occupies that area ([#5447](https://github.com/gitkraken/vscode-gitlens/issues/5447))
- Removes the AI terms confirmation prompt &mdash; AI features no longer interrupt your first use to ask you to accept; the large prompt warning (`gitlens.ai.largePromptWarningThreshold`) is unaffected
- Removes code suggestions from _Launchpad_ &mdash; affected pull requests now group under their provider-assigned category
- Removes the _Reset Current Branch to Previous Commit_ command from the _Commit Graph_ and the views
- Removes the `gitlens.graph.highlightRowsOnRefHover` setting &mdash; click a reference to pin it and highlight its lineage instead
- Removes the _GitLens: Toggle Commit Graph_ command from the Command Palette &mdash; use _Show Commit Graph_ instead; _Toggle Maximized Commit Graph_ now just reveals the Graph and stays available for existing keybindings ([#5545](https://github.com/gitkraken/vscode-gitlens/issues/5545))

---

### Previous Release Notes

- [Version 18.x Release Notes](/gitlens/GL-Release-v18-x)
- [Version 17.x Release Notes](/gitlens/GL-Release-v17-x)
- [Older Release Notes (v16.x and earlier)](/gitlens/GL-Releases-Old)
