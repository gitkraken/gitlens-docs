---
title: Git Command and Rebase Features
description: Technical reference for the GitLens Git Command Palette, powerful commands, Interactive Rebase Editor, commit signature verification, and Git submodule support.
product: GitLens
feature: Git Commands
content_type: reference
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [git-command-palette, commands, interactive-rebase, signatures, submodules]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Git Commands and Rebase"
    nav_order: 50
    nav_parent: "gitlens-features"
    page_type: "content"
    card_icon: "git-compare"
    card_color: "red"
    card_description: "The Git Command Palette, powerful commands, the Interactive Rebase Editor, signature verification, and submodules"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

***

## Git Command Palette

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-01-v4@2x.png" alt="GitLens Git Command Palette showing guided step-by-step command options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Guided Git commands through the Command Palette</figcaption>
</figure>

Adds a [customizable](/gitlens/gitlens-settings/#git-command-palette-settings) Git Command Palette (`gitlens.gitCommands`) for guided, step-by-step access to many common Git commands. Quickly navigate Git actions, explore commit history, manage stashes, and more—all through intuitive, confirmable menus.

On a command's confirmation step, choose the action row, then turn options on or off with the checkbox toggles under the **Options** separator. Examples include **Prune** for Fetch, **Force** for Push Tags and branch deletion, **Keep Staged** for stashes, **Fast-forward** and **Don't Commit** for Merge, **Update Branches** and **Autosquash** for Rebase, and **In a New Worktree** for Switch. Where a matching Git config value exists, such as `fetch.prune`, `merge.ff`, `rebase.updateRefs`, or `rebase.autosquash`, the toggle starts from that value. Some commands also offer a **Don't Ask Again** toggle, which adds the command to [`gitlens.gitCommands.skipConfirmations`](/gitlens/gitlens-settings/#git-command-palette-settings) so the confirmation is skipped from then on. Steps that ask you to choose between different actions, such as Push's **Publish** step, and warning steps whose safe choice is selected for you don't offer **Don't Ask Again**.

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-confirm-options-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Confirm Fetch step with the Fetch and Fetch All Remotes rows above an Options separator and the ringed Prune checkbox toggle, which removes remote-tracking branches that no longer exist on the remote." />
</figure>

To push tags to a remote, run the **Tag** command and choose **Push Tags**. Pick one or more tags, choose a remote (skipped when the repository has only one), and confirm; turn on **Force** to overwrite a tag that already exists on the remote. You can also push tags from the side bar views (**Push Tag...** or **Push Tags...** on tag nodes) and from the Commit Graph (**Push Tag...** on a tag's context menu).

<figure>
  <img src="/wp-content/uploads/gl-git-command-palette-push-tags-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Push Tags step, titled Push Tags, asking to choose tags to push with the repository's v1.0.0, v1.1.0 and v2.0.0 tags listed as selectable rows." />
</figure>

When you run **Push** on a branch that hasn't been published yet, the command shows a publish step (**Confirm Publish**) so you can choose the remote to publish the branch to. If the repository has no remotes, the **Publish** step reads *Cannot publish; No remotes found* and offers two ways forward:

- **Publish Repository…** creates a new remote repository and publishes the current branch to it. It's selected by default when you push the current branch. If you push another branch, it still publishes the current branch, and **Add Remote…** is selected instead.
- **Add Remote…** walks you through adding a remote, then continues to **Confirm Publish** so you can publish the branch to it.

**Publish Repository** in the Commit Graph and the side bar views opens this same step with your choice already selected.

<figure>
  <img src="/wp-content/uploads/gl-push-wizard-no-remotes-01-v3@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Publish step for a repository with no remotes, placeholder &quot;Cannot publish; No remotes found&quot;, with Publish Repository… selected (&quot;Will create a new remote repository and publish branch main to it&quot;) and Add Remote… (&quot;Will add a remote, then publish branch main to it&quot;) and Cancel. Don't Ask Again is not offered on this step." />
</figure>

When you push several repositories at once, any without remotes are skipped, and the confirmation step lists them. If none of them has a remote, the step reads *Cannot push; No remotes found*.

When you add a remote with **Add Remote**, from the **Remote** command or the side bar's **Remotes** view, the name is pre-filled with `origin` if the repository has no remotes yet. Before adding the remote, GitLens checks that the URL can be reached. If it can't, the confirmation step reads *Cannot reach remote* with the reason, such as *The host could not be found*, and offers:

- **Change URL** (selected) to go back and correct the URL.
- **Add Remote Anyway** to add it despite the failed reachability check. A later fetch or push reports if the URL is wrong.
- **Retry**, the button at the end of the input box, to check again.

<figure>
  <img src="/wp-content/uploads/gl-add-remote-unreachable-01-v2@2x.png" class="help-center-img img-bordered" alt="The Git Command Palette's Confirm Add Remote step for a URL that can't be reached: placeholder &quot;Cannot reach remote; The host could not be found&quot;, the message &quot;Check the URL, or add the remote anyway&quot;, the row &quot;Unable to reach https://nonexistent.invalid/acme/release-notes.git&quot;, Add Remote Anyway (&quot;Will add origin without checking it; a later fetch or push will report if it is wrong&quot;) and Change URL selected, with a Retry button at the end of the input box." />
  <figcaption style="text-align: center; color: #888">Adding a remote whose URL can't be reached</figcaption>
</figure>

If the remote is added but the first fetch from it fails, a warning offers **Remove Remote**. Likewise, if a push can't reach a remote you have never fetched from, for example one you just added with a mistyped URL, the error offers **Remove Remote**. That button doesn't appear for an established remote, where a failure usually means a network problem.

---

### Quick Commit Access

- **Show Branch History** (`gitlens.showQuickBranchHistory`): Explore the commit history of any selected branch.
  
  <img src="/wp-content/uploads/menu-branch-history.png" class="help-center-img img-bordered">

- **Show Current Branch History** (`gitlens.showQuickRepoHistory`): View the commit history of your current branch.
- **Show File History** (`gitlens.showQuickFileHistory`): Access the full commit history of the current file. The File History view supports a **contributors mode** (`gitlens.views.fileHistory.mode`) that shows all contributors to the file instead of the commit list.

  <img src="/wp-content/uploads/gl-menu-file-history-01-v3@2x.png" alt="File History QuickPick for README.md listing its six commits with message, author, date, SHA and line-change counts; the newest commit is highlighted" class="help-center-img img-bordered">

- **Search Commits** (`gitlens.showCommitSearch`): Use a quick pick menu to search by:

  - Message: `<message>`
  - Excluded message: `-message:<message>` (removes commits whose message contains the term)
  - Author: `author:<author>` or `@:<author>`
  - Committer: `committer:<committer>`
  - Commit SHA: `commit:<sha>` or `#:<sha>`
  - File path or glob: `file:<glob>` or `?:<glob>`
  - Patch changes: `change:<pattern>` or `~:<pattern>`
  - Merge commits only: `type:merge` or `is:merge`

  <img src="/wp-content/uploads/gl-menu-commit-search-01-v2@2x.png" alt="Commit Search quick pick listing the search modes, including Search by Message, Exclude by Message, Author, Committer, Commit SHA, File and Changes" class="help-center-img img-bordered">

  Refer to the [Git log documentation](https://git-scm.com/docs/git-log) for advanced usage.

- **Show Commit Details** (`gitlens.showQuickCommitDetails`): Review commit information and actions.

  <img src="/wp-content/uploads/gl-menu-commit-details-01-v2@2x.png" alt="Commit Details QuickPick showing the commit message, author, SHA, and changed-file count, with actions including Revert, Reset, Create Branch, and Create Tag" class="help-center-img img-bordered">

- **Show Line Commit Details** (`gitlens.showQuickCommitFileDetails`): Explore the file's commit and take action on it.

  <img src="/wp-content/uploads/menu-commit-file-details.png" class="help-center-img img-bordered">


### Quick Stash Access

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-list-01-v3@2x.png" alt="Stash list QuickPick showing all stash entries in the repository with stash messages and selection options" class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/gl-menu-stash-details-01-v3@2x.png" alt="Stash details QuickPick for stash #0 showing its files-changed summary and the Apply Stash, Rename Stash, Drop Stash, Copy Message, Open, Compare and Browse Repository actions" class="help-center-img img-bordered">
</figure>

- Adds a _Show Stashes_ command (`gitlens.showQuickStashList`) to show a quick pick menu to explore your stashes.

---

### Quick Status Access

- Adds a _Show Repository Status_ command (`gitlens.showQuickRepoStatus`) to show a quick pick menu for visualizing the current repository status.

<figure>
  <img src="/wp-content/uploads/menu-repo-status.png" class="help-center-img img-bordered">
</figure>

***

## Powerful Commands

GitLens provides powerful commands to improve your workflow:

- **Add Co-authors** (`gitlens.addAuthors`) — Add a co-author to the commit message input box.
- **Copy SHA** (`gitlens.copyShaToClipboard`) — Copy the commit SHA of the current line or the latest commit.
- **Copy Message** (`gitlens.copyMessageToClipboard`) — Copy the commit message from the current line or latest commit.
- **Copy Current Branch** (`gitlens.copyCurrentBranch`) — Copy the current branch name to the clipboard.
- **Switch to Another Branch** (`gitlens.views.switchToAnotherBranch`) — Quickly switch branches.
- **Compare References...** (`gitlens.compareWith`) — Compare two references.
- **Compare HEAD with...** (`gitlens.compareHeadWith`) — Compare HEAD with a selected reference.
- **Compare Working Tree with...** (`gitlens.compareWorkingWith`) — Compare the working tree with a selected reference.
- **Open Changes (difftool)** (`gitlens.externalDiff`) — Open file changes with the configured Git difftool.
- **Open All Changes (difftool)** (`gitlens.externalDiffAll`) — Open all working changes with the configured difftool.
- **Open Directory Compare (difftool)** (`gitlens.diffDirectoryWithHead`) — Compare working tree with HEAD using a difftool.
- **Open Directory Compare (difftool) with...** (`gitlens.diffDirectory`) — Compare with a selected reference.
- **Open File** (`gitlens.openWorkingFile`) — Open the working version of the current file.
- **Open Revision...** (`gitlens.openFileRevision`) — Open a selected file revision.
- **Open Revision from...** (`gitlens.openFileRevisionFrom`) — Open a revision from a specific reference.
- **Open Blame Prior to Change** (`gitlens.openBlamePriorToChange`) — Show blame for the prior revision of a line.
- **Open Changed Files** (`gitlens.openChangedFiles`) — Open all changed files in the working tree.
- **Close Unchanged Files** (`gitlens.closeUnchangedFiles`) — Close all files without changes.
- **Enable Debug Logging** (`gitlens.enableDebugLogging`) — Enable debug logging in the GitLens output.
- **Disable Debug Logging** (`gitlens.disableDebugLogging`) — Disable debug logging.
- **Copy as Patch** (`gitlens.copyPatchToClipboard`) — Copy patch data from views, changes, or stashes.
- **Apply Copied Patch** (`gitlens.applyPatchFromClipboard`) — Apply a patch from clipboard contents.
- **Change Branch Merge Target** (`gitlens.changeBranchMergeTarget`) — A multi-step wizard to set or reset a branch's merge target. Pick a local branch, then select a remote branch as its merge target, or reset an existing target.
- **Copy Changes to Worktree** (`gitlens.worktree.copyChanges`) — Copy working changes from one worktree to another.
- **Unlock Worktree** (`gitlens.worktree.unlock`) — Unlock a locked worktree from the tree view context menu.

***

## Interactive Rebase Editor

<figure>
  <img src="/wp-content/uploads/gl-rebase-01-v4@2x.gif" alt="GitLens interactive rebase editor: five commits each with an action dropdown, the second entry's dropdown open on pick / reword / edit / squash / fixup / drop, and then squash applied to it; the footer lists the keyboard shortcuts including alt + up/down to move a commit" class="help-center-img img-bordered">
</figure>

Adds a user-friendly interactive rebase editor to easily configure an interactive rebase session:

- Quickly re-order, edit, squash, and drop commits.
- Includes drag & drop support.
- Toolbar commands for **Abort**, **Continue**, **Reopen as Interactive Editor**, and **Reopen as Text Editor**.

### Start or Continue with Auto-Rebase `PRO`

When AI features are allowed, the editor footer shows a **Start Auto-Rebase** split button next to **Start Rebase**. Start Auto-Rebase runs the rebase with [Auto-Rebase](/gitlens/gl-features-ai-and-agents/#auto-rebase-pro), which resolves conflicts it's confident about and pauses at commits you marked `edit` or when its confidence is low. After a rebase has started, the footer shows **Continue with Auto-Rebase** beside **Continue** and **Skip**. The chevron menu of each split button holds **Recompose Commits...**, which aborts the rebase and opens the Commit Composer.

<figure>
  <img src="/wp-content/uploads/gl-rebase-auto-rebase-start-01-v2@2x.png" class="help-center-img img-bordered" alt="The Interactive Rebase Editor before a rebase starts, with the footer's Start Rebase button beside the ringed Start Auto-Rebase split button, whose chevron menu holds Recompose Commits, and Abort." />
</figure>

### Conflict Detection

The rebase editor includes a **conflict files panel** that displays files with potential conflicts along with per-file conflict counts and status indicators. **Predictive conflict detection** warns about upcoming conflicts against the current base before you start the rebase, helping you prepare for issues in advance.

### Rebase Editor Settings

The rebase editor offers several configuration options:

- `gitlens.rebaseEditor.openOnPausedRebase` — Automatically open the rebase editor when a rebase is paused (e.g., due to conflicts).
- `gitlens.rebaseEditor.openBehavior` — Controls how the rebase editor opens: `auto` (default) or `beside` (opens alongside the current editor).
- `gitlens.rebaseEditor.revealLocation` — Where to reveal commit details: `graph` or `inspect`.
- `gitlens.rebaseEditor.revealBehavior` — When to reveal details: `never`, `onOpen`, or `onSelection`.
- `gitlens.rebaseEditor.density` — Controls row padding in the editor: `compact` (default) or `comfortable` for more spacing.

### Conflict Resolution Actions

When a rebase is paused due to conflicts, the rebase editor provides inline actions to **stage current changes** or **stage incoming changes** directly, streamlining the conflict resolution workflow.

### To use this directly from your terminal (e.g., when running `git rebase -i`):

- Set VS Code as your default Git editor:
  ```bash
  git config --global core.editor "code --wait"
  ```

- Or, to only affect rebase sessions:
  ```bash
  git config --global sequence.editor "code --wait"
  ```

> To use the Insiders edition of VS Code, replace `code` with `code-insiders` in the commands above.

***

## Commit Signature Verification `PRO`

GitLens verifies commit signatures using GPG, SSH, and X.509 certificates, displaying verification badges directly in the Commit Details view, Graph Details panel, and inline blame hovers.

### Verification Badges

Each signed commit shows a badge indicating its verification status:

- **Verified** — The signature is valid and the signer is trusted
- **Unverified** — The signature could not be verified (missing key, untrusted signer, etc.)
- **Unsigned** — The commit has no signature

The `${signature}` token is available in commit tooltip format strings to display signature status in custom tooltip layouts.

### Allowed Signers Management

The **Allowed Signers** webview provides a dedicated panel for managing SSH trusted signers. It scans recent commits for SSH signatures, discovers candidate signers with their avatars, and lets you select which keys to trust. Trusted entries are saved to your SSH `allowed_signers` file.

Access it from the Command Palette: `GitLens: Edit SSH Allowed Signers...` (`gitlens.git.editAllowedSigners`)

***

## Git Submodule Support

GitLens provides basic support for Git submodules. Submodule repositories are automatically discovered and tracked when you open a project that contains them. In the sidebar views, submodule repositories are distinguished with dedicated icons and tooltips. Submodule changes are handled in diffs so you can see when a submodule reference has been updated.
