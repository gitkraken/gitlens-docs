---
title: GitLens Release Notes
description: GitLens Release Notes
taxonomy:
  category: gitlens
---

Find out what's new, what's fixed, or just take a trip down memory lane remembering those bugs of yesterday.

Check out our [Changelog](https://github.com/gitkraken/vscode-gitlens/blob/main/CHANGELOG.md) to see linked issues and past changes.

<a href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank" class="button button--basic ">Install Current Version Now</a>

Features marked with `PRO` require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing) for use on privately hosted repos \
Features marked with `PREVIEW` require a GitKraken Account, with access level based on your [plan](https://www.gitkraken.com/gitlens/pricing), e.g. Community, Pro, etc

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

<a id="v18-3"></a>

## Version 18.3

#### Thursday, July 9, 2026

GitLens 18.3 brings a more capable _Compose_ mode, follow-up conversations in AI _Review_, smarter AI conflict resolution, and refreshed provider and model support. Plus, the GitLens Settings page has been completely revamped with a modern, two-pane experience and live, interactive previews.

This release also sharpens working changes and worktree control in the _Commit Graph_ &mdash; stash or copy a patch of just the files you select, open a partially-staged file's staged, unstaged, or combined diff, focus the graph on a single branch or worktree, and more. And with working-changes review now consolidated in the _Commit Graph_, the _Inspect_ view stays focused on commits and stashes.

<img src="/wp-content/uploads/gl-18-3-hero.png" class="help-center-img img-bordered">

### Leveled-up AI Workflows

AI-powered workflows in GitLens get meaningfully stronger, with more capability and increased control:

- **A more capable _Compose_ mode** &mdash; a dual commit/recompose posture, drag to reorder draft commits, drag to move one or more files between draft commits, and multi-diff _Open Changes_ actions right in the curation file trees.
- **Conversations in _Review_** &mdash; AI _Review_ mode now supports follow-up conversations, with _Discard_ and _Refine_ actions available in both _Compose_ and _Review_.
- **Smarter model selection** &mdash; the active model appears as a selectable chip across AI inputs, with consumption-rate and recommendation badges for GitKraken AI models.
- **Refreshed provider and model support** &mdash; newer models land across the registries (OpenAI GPT-5.x, Anthropic Claude 5/4.x, DeepSeek V4, Gemini 3.x, and Grok 4.5/4.3), Hugging Face moves to its OpenAI-compatible router, the xAI provider is renamed SpaceXAI following its rebrand, retired models are hidden, and the GitHub Models provider is removed.

### Smarter Conflict Resolution

The AI **Resolve** mode introduced in 18.2 gets a substantial upgrade. Conflicts the AI can't auto-merge &mdash; binary, symlink, submodule, file-mode, add/add, and rename/rename or rename/delete conflicts &mdash; are now labeled by type and offer inline _Take Current_, _Take Incoming_, and _Delete_ actions instead of dead-ending as _needs review_ (resolving a rename/rename conflict also removes the other side's renamed file). UTF-16/BOM-encoded files are decoded so their conflicts can be resolved rather than skipped.

Resolve mode also gains a split-panel _Conflict Details_ sheet (current vs incoming history), resolution scoped to selected files, automatic handling of both-deleted and rename conflicts, per-file confidence indicators, and collapsible resolved/pending sections with progress. You can now jump into it straight from the _Interactive Rebase Editor_ &mdash; a new _Resolve Conflicts in Commit Graph_ action on its conflicted-files panel opens the graph in **Resolve** mode for the rebase's conflicts.

### A Reimagined Settings Experience

The _GitLens Settings_ page has been rebuilt from the ground up. Gone is the single, static, scroll-forever page &mdash; in its place is a modern two-pane layout with a searchable, grouped, resizable category rail alongside a detail pane that shows **live, interactive previews** reacting to your changes as you make them.

- **Search everything** &mdash; matches category names, setting labels, and literal setting names (e.g. `gitlens.currentLine.format`), scrolls the match into view, and offers an _Open in Settings UI_ escape hatch for settings not surfaced on the page. Press <kbd>Ctrl/Cmd+F</kbd> to jump straight to search.
- **Previews that match reality** &mdash; format string examples are rendered by the real formatter, so what you see is exactly what GitLens will display.
- **New _Cloud Integrations_ and _AI_ categories** &mdash; view and connect hosting and issue-service integrations, and manage your AI provider and model, GitKraken MCP, default coding agent, and Claude Code hooks, all in one place.
- **Connection-aware cues** &mdash; the category rail shows a connected/total count for _Cloud Integrations_ and a rule count for _Autolinks_.

### Sharper Working Changes & Worktree Control

Working with changes and worktrees in the _Commit Graph_ (and _Inspect_ view) gets more precise across the board:

- **Act on just the files you select** &mdash; select 2+ files in the working changes (WIP) file list and the _Stash_ and _Copy (Patch)_ toolbar buttons retarget to your selection (hold <kbd>Alt</kbd> for the whole-scope action), with a matching multi-select _Copy Changes (Patch)_ context menu command.
- **Open exactly the diff you mean** &mdash; a partially-staged file shows as a single row, but you can now open its _Staged_, _Unstaged_, or combined changes from the context menu.
- **See more at a glance** &mdash; a working tree change count badge appears on the _Commit Graph_ panel tab (even while collapsed), per-file added/removed line counts show in the WIP file list, and a new `gitlens.sortWorkingChangesBy` setting sorts working changes by their staged/unstaged state.
- **Quick jumps for files and worktrees** &mdash; _Reveal in Explorer View_ for working files, _Open in Integrated Terminal_ for worktrees, and _Copy Changes (Patch)_ for whole commits and stashes.
- **A cleaner WIP bar and headers** &mdash; the working changes bar scrolls horizontally with the mouse wheel, keeps the primary repository anchored, and stays out of the way unless a secondary worktree has changes, while the details and WIP panel headers are regrouped into clearer clusters.

### Focus the Graph on What Matters

New _Focus on Branch_, _Focus on Worktree_, and _Solo Branch_ actions let you zero in on the work you care about. Right-click a branch or worktree in the side bar (or a graph row) to focus the graph and minimap on it, or right-click a working tree (WIP) row to focus or solo the graph on that worktree's branch. A new _auto_ layout also positions the details panel to the right or bottom based on the graph's width, with <kbd>Alt</kbd>+Click to temporarily pin a location.

### Consolidated Working Changes Review

Reviewing working changes now lives in one place: the _Commit Graph_. The _Inspect_ view drops its Overview (working changes) mode to stay focused on commits and stashes, and _Launchpad_ actions (_Switch to Branch_, _Open Details_, and PR switch deep links) now open the _Commit Graph_ at the working changes (WIP) row.

---

### Added

- Redesigns the _GitLens Settings_ page with a modern two-pane layout &mdash; a searchable, grouped, and resizable category rail paired with a detail pane showing live, interactive previews that react to setting changes as you make them, replacing the previous single-page scroll and its static images ([#5372](https://github.com/gitkraken/vscode-gitlens/issues/5372))
  - Search matches category names, setting labels, and literal setting names (e.g. `gitlens.currentLine.format`), scrolls the match into view, and offers an _Open in Settings UI_ escape hatch for settings not surfaced on the page; Ctrl/Cmd+F focuses the search
  - Format string examples are rendered by the real formatter, so the preview always matches what GitLens displays
  - Adds _Cloud Integrations_ and _AI_ categories &mdash; view and connect hosting and issue service integrations, and manage the AI provider and model, GitKraken MCP, default coding agent, and Claude Code hooks
  - Shows connection-aware cues in the category rail &mdash; a connected/total count for _Cloud Integrations_ and a rule count for _Autolinks_
- Adds the ability to stash or copy a patch of only the selected files from the working tree (WIP) file list in the _Inspect_ and _Commit Graph_ views &mdash; selecting 2+ files retargets the _Stash_ and _Copy (Patch)_ toolbar buttons to the selection, with the whole-scope action available by holding Alt, plus a matching multi-select _Copy Changes (Patch)_ context menu command ([#5384](https://github.com/gitkraken/vscode-gitlens/issues/5384))
- Adds _Open Changes_, _Open Staged Changes_, and _Open Unstaged Changes_ options for working tree files that have both staged and unstaged changes in the _Inspect_ and _Commit Graph_ views &mdash; a partially-staged file appears as a single row but you can now open its staged-only, unstaged-only, or combined diff from the context menu ([#5385](https://github.com/gitkraken/vscode-gitlens/issues/5385))
- Adds a working tree change count badge to the _Commit Graph_ view &mdash; mirrors the _Source Control_ view by showing the number of working tree changes on the GitLens panel tab, even while the panel is collapsed; controllable via the new `gitlens.graph.showWorkingTreeBadge` setting ([#5383](https://github.com/gitkraken/vscode-gitlens/issues/5383))
- Adds an _Open in Integrated Terminal_ option for worktrees in the _Commit Graph_ and the _Worktrees_ view &mdash; opens the selected worktree's folder in the integrated terminal, matching the action already available for repositories and folders ([#5386](https://github.com/gitkraken/vscode-gitlens/issues/5386))
- Adds a _Reveal in Explorer View_ option for working tree (WIP) files in the _Inspect_ and _Commit Graph_ views &mdash; right-click a staged, unstaged, or conflicted working file to reveal and select it in VS Code's Explorer view ([#5387](https://github.com/gitkraken/vscode-gitlens/issues/5387))
- Adds _Focus on Branch_, _Focus on Worktree_, and _Solo Branch_ options to the _Commit Graph_ &mdash; right-click a branch or worktree in the side bar (or a graph row) to focus the graph and minimap on it, and right-click a working tree (WIP) row to focus or solo the graph on that worktree's branch ([#5388](https://github.com/gitkraken/vscode-gitlens/issues/5388))
- Adds manual take-side fallbacks and conflict-type labels to the AI **Resolve** mode in the _Commit Graph_ WIP details panel &mdash; conflicts the AI can't auto-merge (binary, symlink, submodule, file-mode, add/add, and rename/rename or rename/delete conflicts) are now labeled by type and offer inline _Take Current_, _Take Incoming_, and _Delete_ actions instead of dead-ending as "needs review"; resolving a rename/rename conflict also removes the other side's renamed file. Also decodes UTF-16/BOM-encoded files so their conflicts can be resolved rather than skipped ([#5393](https://github.com/gitkraken/vscode-gitlens/issues/5393))
- Adds a commit signing indicator to the _Commit Graph_'s working changes (WIP) commit box &mdash; a key icon appears when commits will be signed (via the repo's `commit.gpgsign` Git config or VS Code's `git.enableCommitSigning` setting), with the signing format (GPG, SSH, X.509, or OpenPGP) shown on hover
- Adds a _Start Review with an Agent_ action to _Launchpad_ pull request items &mdash; after selecting a pull request in the _Launchpad_, you can start an AI agent review that checks out the PR in a worktree and routes straight to the agent picker (or your default agent); available when AI features are enabled ([#5395](https://github.com/gitkraken/vscode-gitlens/issues/5395))
- Adds an _auto_ layout for the _Commit Graph_ details panel that positions it to the right or bottom based on the graph's width, with Alt+Click to temporarily pin a location ([#5402](https://github.com/gitkraken/vscode-gitlens/issues/5402), [#5403](https://github.com/gitkraken/vscode-gitlens/issues/5403))
- Adds a _Copy Changes (Patch)_ action to commits and stashes in the _Inspect_ and _Commit Graph_ details &mdash; copies a patch of the entire commit or stash to the clipboard ([#5455](https://github.com/gitkraken/vscode-gitlens/issues/5455))
- Adds per-file added/removed line counts to the working changes (WIP) file list in the _Commit Graph_ details, loaded lazily when the list is visible ([#5456](https://github.com/gitkraken/vscode-gitlens/issues/5456))
- Adds a `gitlens.sortWorkingChangesBy` setting to sort working changes (WIP) by their Git staged/unstaged state in the _Commit Graph_ details ([#5454](https://github.com/gitkraken/vscode-gitlens/issues/5454))
- Adds a _Resolve Conflicts in Commit Graph_ action to the interactive rebase editor's conflicted files panel &mdash; opens the _Commit Graph_ in AI **Resolve** mode for the rebase's conflicts; available when AI features are enabled ([#5413](https://github.com/gitkraken/vscode-gitlens/issues/5413))
- Adds an _Open Changes with Working File (Worktree)_ action to the commit file menu in the _Commit Graph_ details and _Inspect_ view &mdash; compares a committed file against its working copy in the sibling worktree whose branch contains the commit (rather than the currently-scoped worktree), with a worktree picker when more than one applies
- Adds an optional `avatar` URL template to custom remotes in the `gitlens.remotes` setting &mdash; enables corporate and self-hosted setups to resolve commit-author avatars via a templated URL with `${email}`, `${emailName}`, `${domain}`, and `${size}` tokens; identity values are component-encoded before interpolation to keep attacker-controllable commit emails from injecting URL-structural characters, and templates configured via workspace settings require explicit user approval on first use in a trusted workspace (revocable via _GitLens: Reset > Approved Avatar URL Templates..._) ([#302](https://github.com/gitkraken/vscode-gitlens/issues/302), [#5155](https://github.com/gitkraken/vscode-gitlens/issues/5155)) &mdash; thanks to PR [#1636](https://github.com/gitkraken/vscode-gitlens/pull/1636) by [Tmk](https://github.com/Tmk)
- Adds a _Take your agent workflows further_ step to the _Welcome_ view walkthrough &mdash; introduces Kepler, GitKraken's Agentic Development Environment (ADE), with a _Get Kepler_ call-to-action ([#5378](https://github.com/gitkraken/vscode-gitlens/issues/5378))
- Adds a ConfigCat-based feature flag service for A/B testing and experimentation support ([#5092](https://github.com/gitkraken/vscode-gitlens/issues/5092))

### Changed

- Changes GitLens AI features (_Generate Commits_, _Explain_, _Generate Pull Request_/_Changelog_, and AI-powered search) to no longer be labeled _(Preview)_, and consolidates their commands under the `gitlens.ai.*` namespace ([#5463](https://github.com/gitkraken/vscode-gitlens/issues/5463))
- Improves the _Commit Composer_ &mdash; adds a dual commit/recompose posture, drag to reorder draft commits, drag to move one or more files between draft commits, and multi-diff _Open Changes_ actions in the curation file trees ([#5460](https://github.com/gitkraken/vscode-gitlens/issues/5460))
- Improves AI-powered conflict resolution _(Preview)_ in the _Commit Graph_ working changes (WIP) details &mdash; adds a split-panel _Conflict Details_ sheet (current vs incoming history), resolution scoped to selected files, automatic handling of both-deleted and rename conflicts, per-file confidence indicators, collapsible resolved/pending sections with progress, and a dedicated merge icon ([#5306](https://github.com/gitkraken/vscode-gitlens/issues/5306))
- Improves the AI _Review_ mode with follow-up conversations, plus _Discard_ and _Refine_ actions in _Compose_ and _Review_ ([#5461](https://github.com/gitkraken/vscode-gitlens/issues/5461))
- Improves AI model display and selection across AI inputs &mdash; shows the active model as a selectable chip and surfaces consumption-rate and recommendation badges for GitKraken AI models ([#5425](https://github.com/gitkraken/vscode-gitlens/issues/5425))
- Updates AI provider and model support &mdash; migrates Hugging Face to its OpenAI-compatible router, renames the xAI provider to SpaceXAI following its rebrand, and refreshes the model registries, adding newer models (OpenAI GPT-5.x, Anthropic Claude 5/4.x, DeepSeek V4, Gemini 3.x, and Grok 4.5/4.3) and hiding retired ones ([#5462](https://github.com/gitkraken/vscode-gitlens/issues/5462))
- Changes commits created from the _Commit Graph_'s working changes (WIP) commit box to honor VS Code's `git.enableCommitSigning` setting &mdash; matching the built-in Source Control commit behavior; previously only the repo's `commit.gpgsign` Git config was respected
- Changes the _Commit Graph_ side bar icons to switch back to the graph and open the details panel when clicked from the visualization/kanban modes, instead of being disabled ([#5401](https://github.com/gitkraken/vscode-gitlens/issues/5401))
- Improves the working changes (WIP) bar in the _Commit Graph_ &mdash; scrolls horizontally with the mouse wheel, keeps the primary repository anchored, and hides unless a secondary worktree has changes ([#5457](https://github.com/gitkraken/vscode-gitlens/issues/5457))
- Reorganizes the details and working changes (WIP) panel headers in the _Commit Graph_ and _Inspect_ views &mdash; groups navigation and actions into clearer clusters, folds the _Inspect_ view's separate navigation bar into the details action row, and adds branch and create context menus ([#5459](https://github.com/gitkraken/vscode-gitlens/issues/5459))
- Improves keyboard focus and navigation in the webview tree views &mdash; each row is a single tab stop that cycles its inner controls, Space no longer double-toggles checkboxes, multi-select keyboard navigation is fixed, and checkbox focus rings are visible ([#5458](https://github.com/gitkraken/vscode-gitlens/issues/5458))
- Changes copying changes to a worktree to no longer prompt to open that worktree afterward
- Changes stashing to use the _Commit Graph_ working changes (WIP) commit-box draft message when one is present
- Renames the _Open Worktree File_ action to _Open File (Worktree)_ for consistency with the new _Open Changes with Working File (Worktree)_ action

### Removed

- Removes the Overview (working changes) mode from the _Inspect_ view, making it commit/stash-only &mdash; reviewing working changes is now consolidated in the _Commit Graph_. Launchpad _Switch to Branch_ and _Open Details_ actions, and PR switch deep links, now open the _Commit Graph_ at the working changes (WIP) row instead of the _Inspect_ view; the Launchpad code-suggestion entry points are retired (code suggestions remain available in the _Commit Graph_) ([#5399](https://github.com/gitkraken/vscode-gitlens/issues/5399))
- Removes the _Streamline Workflow with the Home View_ step from the _Welcome_ view walkthrough ([#5378](https://github.com/gitkraken/vscode-gitlens/issues/5378))
- Removes the GitHub Models AI provider ([#5462](https://github.com/gitkraken/vscode-gitlens/issues/5462))

### Fixed

- Fixes Anthropic AI requests failing with a _400 Bad Request_ when the request includes a system message (e.g. generating or recomposing commits with the commit composer, or AI conflict resolution) &mdash; system-role messages are now hoisted into the top-level `system` parameter that Anthropic's Messages API requires, and unrecognized Anthropic errors now surface their actual message instead of a bare _Bad Request_ ([#5426](https://github.com/gitkraken/vscode-gitlens/issues/5426))
- Fixes the coding agents integration running the GitKraken CLI during extension startup &mdash; the agent-detection probe is now deferred out of the initial render window so it no longer competes with _Commit Graph_ and _Home_ view loading, and a fresh CLI install on first launch no longer leaves the detected agents list empty for up to 5 minutes
- Fixes creating a branch from a remote ref incorrectly setting upstream tracking when the new branch name differs from the remote branch name &mdash; e.g. creating `feature/foo` from `origin/main` no longer makes it track `origin/main`; affects _Create & Switch to Branch_, _Switch to... → Create & Switch to New Local Branch_, and _Create Branch in New Worktree_ ([#5360](https://github.com/gitkraken/vscode-gitlens/issues/5360))
- Fixes _Keep Staged_ not keeping staged changes when stashing selected files &mdash; choosing _Keep Staged_ while stashing specific tracked files no longer drops the `--keep-index` flag, so staged changes are correctly kept intact ([#5281](https://github.com/gitkraken/vscode-gitlens/issues/5281))
- Fixes pushing a branch that needs a force-push (e.g. after an amend or rebase) silently reporting success without updating the remote &mdash; a non-fast-forward (_tip of your current branch is behind_) rejection is now surfaced as an error instead of being swallowed as non-fatal ([#5364](https://github.com/gitkraken/vscode-gitlens/issues/5364))
- Fixes _Fetch_, _Pull_, _Switch_, _Reset_, and _Restore_ operations silently reporting success when the underlying Git command failed with a message Git treats as a warning (e.g. an unreachable remote, or an invalid ref/revision) &mdash; these failures are now surfaced as errors instead of being swallowed as non-fatal
- Fixes the working changes (WIP) stats tooltip in the details header duplicating the visible stats pill instead of describing the change breakdown &mdash; the tooltip now reads e.g. _1 file added, 2 files changed in the working tree_
- Fixes a stray gap in the _Commit Graph_ header next to the fetch and sync actions when the current branch is already published &mdash; the publish action no longer reserves empty space once the branch has an upstream
- Fixes the design of the paused-operation banner (shown during a merge, rebase, cherry-pick, or revert in the _Commit Graph_/_Inspect_ details and _Home_) &mdash; the _Continue_ action now uses a start icon, and the action buttons' hover and active states blend into the banner instead of showing a clashing grey toolbar highlight ([#5394](https://github.com/gitkraken/vscode-gitlens/issues/5394))
- Fixes selection and folder expand/collapse state not persisting across refreshes in grouped webview tree views when identical paths appear in different groups
- Fixes the AI input in the _Commit Graph_ details stealing keyboard focus when the panel switched modes automatically
- Fixes the _Commit Graph_ showing an incorrect worktree count when a worktree fetch fails or is unsupported
- Fixes the commit-message headline occasionally rendering at the wrong size before autolinks finish loading in the commit details
- Fixes stray menu-popover styling leaking onto nested tooltips

---

<a id="v18-2"></a>

## Version 18.2

#### Monday, June 15, 2026

GitLens 18.2 brings AI-powered conflict resolution into your workflow. When a merge, rebase, or cherry-pick pauses on conflicts, you can now hand the messy parts to AI &mdash; it works through your conflicted files in parallel, proposes a resolution for each, and lets you review every change before anything touches your working tree. Refine the whole run with a prompt, give per-file feedback, or take just the resolutions you trust.

<img src="/wp-content/uploads/gl-18-2-hero.png" class="help-center-img img-bordered">

### Resolve Conflicts with AI

Merge conflicts can be one of the most disruptive moments in a developer's day. GitLens 18.2 introduces a brand-new **Resolve** mode in the _Commit Graph_ details panel that uses AI to work through them for you &mdash; across merges, rebases, and cherry-picks alike.

When an operation pauses on conflicts, the working changes (WIP) details panel leads with a **Resolve** action. Resolve mode opens to a list of your conflicted files &mdash; click any file to open it (conflict markers and all) and inspect it first &mdash; then hit **Resolve** to let AI go to work. It resolves files in parallel, streaming its progress as it goes, and for each file reports what it did: **merged** the changes, **kept current**, **took incoming**, **deleted**, or flagged the file as **needs review** when it wasn't confident enough to resolve it automatically.

Nothing is applied until you say so. Every proposed resolution is reviewable as a diff before it lands, and from the results you can:

- **Refine the whole run** &mdash; add a prompt with extra guidance and re-resolve everything at once.
- **Give per-file feedback** &mdash; not happy with a single file? Add a note and re-resolve just that one.
- **Apply or Discard** &mdash; apply the resolutions you trust to your working tree, or discard them and resolve manually. Files marked _needs review_ are left conflicted for you to handle.

You can start a resolution from wherever you run into a conflict:

- The **Resolve** action on the working changes (WIP) details header and on the paused-operation (merge/rebase/cherry-pick) banner
- Context menus and WIP row buttons in the _Commit Graph_ &mdash; **Resolve All Conflicts with AI**, or scope it to selected conflicted files
- The Command Palette &mdash; **Resolve Conflicts with AI**
- The **Resolve Conflict with AI** action on individual conflicted files in the sidebar views


---

### Added

- Introduces AI-powered conflict resolution (Preview) &mdash; a new **Resolve** mode in the _Commit Graph_ WIP details panel that uses AI to resolve merge, rebase, and cherry-pick conflicts ([#5306](https://github.com/gitkraken/vscode-gitlens/issues/5306))
  - Resolves conflicted files in parallel with streamed progress, proposing a per-file resolution (merged, kept current, took incoming, deleted, or flagged as needs review) that you review as a diff before anything is applied
  - Adds the ability to refine the whole run with a prompt, give per-file feedback to re-resolve a single file, and apply or discard the proposed resolutions
  - Adds entry points across GitLens: a **Resolve** action on the WIP details header and the paused-operation banner, _Commit Graph_ context menus and WIP row buttons (all conflicts or selected files), the **Resolve Conflicts with AI** Command Palette command, and a **Resolve Conflict with AI** action on individual conflicted files in the sidebar views
  - Adds clickable file links in the resolve panel that open a conflicted working-tree file so you can inspect it before resolving

### Changed

- Changes the working changes (WIP) details header to lead with the _Resolve_ action when conflicts are present, ahead of _Compose_, _Review_, and _Compare_
- Updates the design and readbility of the Pro feature gates (e.g. _Commit Graph_, _Visual History_) &mdash; with an optional _Switch Repos_ action to move to a repository where the feature is available ([#5335](https://github.com/gitkraken/vscode-gitlens/issues/5335))
- Improves the AI weekly usage-limit message with a _Get More Credits_ action to purchase additional AI credits for users who can buy credits, or guidance to contact an org admin for those who can't ([#5298](https://github.com/gitkraken/vscode-gitlens/issues/5298))

---

<a id="v18-1"></a>

## Version 18.1

#### Tuesday, June 9, 2026

GitLens 18.1 introduces powerful new ways to manage your workflow directly from the Commit Graph. You can now squash, drop, reword, and reorder commits without leaving the Graph, as well as push or undo a commit in a single click. A new working changes bar at the top of the Graph also makes it easier than ever to jump between worktrees and track changes.

This release also improves the working changes (WIP) experience, allowing you to discard changes, copy as a patch, add co-authors, and jump between changes and commits. Finally, we've added multi-select file actions to the Details and Inspect views, and refined the experimental Agent Activity Treemap with a live, decaying heatmap.

<img src="/wp-content/uploads/gl-18-1-hero.png" class="help-center-img img-bordered">

### Edit History, Directly in the Commit Graph

You no longer need to drop into the _Interactive Rebase Editor_ for everyday history edits &mdash; the _Commit Graph_ now does them inline. Right-click a commit on the current branch to **Reword** its message, or select two or more contiguous commits to **Squash** them into one (reviewing and editing the combined message, or keeping just the oldest). Select any set of commits to **Drop** them outright. And when you do want the full editor, a new **Modify Commits (Interactive Rebase)** action opens the _Interactive Rebase Editor_ scoped from the commits you selected, ready for squashing, rewording, reordering, dropping, and editing.

### A Deeper Working Changes Experience

The working changes (WIP) experience across the _Commit Graph_ and _Inspect_ view gets a major lift in 18.1 with more actions and better visibility of working changes across worktrees.

- **Working changes bar** &mdash; a horizontal bar above the Graph shows a pill for every worktree with uncommitted changes (primary and secondary alike), with its branch, agent status, and a hover breakdown of changed files. Click a pill to reveal and select that worktree's changes and open its details.
- **Discard changes** &mdash; discard working changes per-file or in bulk, with safe partial discard for files that have both staged and unstaged changes (the first discard drops only the unstaged portion, preserving what's staged).
- **Copy Changes (Patch)** &mdash; copy a unified diff of your uncommitted changes to the clipboard; copies staged changes by default and unstaged on Alt-click when both are present.
- **Add Co-authors** &mdash; a button on the working changes commit box opens the contributor picker and appends the selected co-authors directly to the Graph's commit message.
- **Jump between changes and commit** &mdash; a new action in the working changes header selects the branch tip commit your changes are based on, complementing the existing jump from a commit to its working changes.

Working changes file lists now also honor VS Code's `scm.defaultViewSortKey` setting (keeping unresolved conflicts at the top), and partially staged (mixed) files are counted and badged more clearly.

### Multi-Select File Actions

You can now multi-select files in the _Commit Graph_ details and _Inspect_ view to act on several at once &mdash; Ctrl/Cmd+click to toggle, Shift+click for a range, and Ctrl/Cmd+A to select all. Batch actions are available from the context menu and toolbar: open files, open selected changes as a multi-diff, open on remote, and copy paths or relative paths &mdash; plus stage, unstage, stash, and discard for working changes.

### Quick Commit Actions: Push to Commit, Undo, and Publish

- **Push to Commit** &mdash; commits ahead of the branch's upstream now show an unpushed indicator that doubles as a one-click action to push up to (and including) that commit, also available in the commit's context menu.
- **Undo Commit** &mdash; a HEAD commit row surfaces an inline undo button when hovered, focused, or selected, alongside the existing context-menu action. Undo now works for the HEAD commit of any worktree, targeting the correct working tree for secondary worktrees, not just the active one.
- **Publish Branch** &mdash; a _Publish Branch_ action appears in the Graph header when the current branch has no upstream, publishing it in one click just left of _Fetch_.

### Navigate and Discover in the Graph

- **Back/forward navigation** &mdash; Back and Forward buttons in the commit and working changes detail headers step through previously-viewed commits, stashes, and working changes, re-selecting the row in the Graph where possible.
- **Keyboard shortcuts reference** &mdash; a new keyboard icon in the Graph's sidebar rail opens a reference listing all supported navigation, search, open, and commit shortcuts with platform-aware key labels.
- **Open Worktree File** &mdash; a new action in the commit file menu opens a committed file from the worktree whose branch contains the commit &mdash; handy in multi-worktree repos where the file's working copy lives outside the currently-scoped worktree.
- **Responsive sidebar** &mdash; the Graph's sidebar icon rail now compacts in short layouts, hiding count badges and tightening spacing, then folding overflowing icons into a "…" menu, restoring them as space grows.

### Agent Activity Treemap Improvements

The experimental _Agent Activity Treemap_ now reads as a living heatmap. Touched files fade over a configurable window after each tool call instead of switching on and off, reads and edits blend as cyan/amber weighted by recency, and a soft pulse marks the file an agent is reading or editing right now. Sub-agent file activity rolls up to the parent session, and a new `gitlens.graph.experimental.visualizations.activityDecay` setting (30 seconds to 30 minutes, default 5 minutes) &mdash; with a matching picker in the treemap toolbar &mdash; controls the decay window.

---

### Added

- Adds a `gitlens.graph.searchAutocompleteOnFocus` setting to control whether search autocomplete suggestions appear automatically when focusing or clicking the search input in the _Commit Graph_ ([#5287](https://github.com/gitkraken/vscode-gitlens/issues/5287))
- Adds the ability to copy working changes to other opened worktrees from the _Commit Graph_ ([#5288](https://github.com/gitkraken/vscode-gitlens/issues/5288))
- Adds the ability to discard working changes from the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view &mdash; per-file or in bulk, with safe partial discard for files that have both staged and unstaged changes (a first discard drops only the unstaged changes, preserving the staged portion) and a bulk action that switches to discarding staged changes when no unstaged changes remain ([#5296](https://github.com/gitkraken/vscode-gitlens/issues/5296))
- Adds an _Add Co-authors_ button to the _Commit Graph_'s working changes (WIP) commit box that opens the contributor picker and appends the selected co-authors to the commit message ([#5297](https://github.com/gitkraken/vscode-gitlens/issues/5297))
- Adds a _Copy Changes (Patch)_ button to the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view that copies a unified diff of the uncommitted changes to the clipboard &mdash; copies staged changes by default and unstaged changes on Alt-click when both are present, otherwise copies all changes ([#5302](https://github.com/gitkraken/vscode-gitlens/issues/5302))
- Adds the ability to jump from the working changes (WIP) to its commit in the _Commit Graph_ &mdash; a down-arrow in the working changes header selects the branch tip commit the changes are based on, complementing the existing action to jump from a commit to its working changes ([#5303](https://github.com/gitkraken/vscode-gitlens/issues/5303))
- Adds an _Undo Commit_ row adornment to the _Commit Graph_ &mdash; surfaces an inline undo button on a HEAD commit row when hovered, focused, or selected, alongside the existing context-menu action
- Adds support for undoing the HEAD commit of any worktree from the _Commit Graph_ &mdash; the adornment and context-menu action now target the correct working tree for secondary worktrees, not just the active one (a distinct _Undo Commit on Worktree_ label makes the target clear) ([#5311](https://github.com/gitkraken/vscode-gitlens/issues/5311))
- Adds responsive compaction to the _Commit Graph_'s side bar icon rail in short layouts &mdash; hides the count badges and tightens spacing, then folds the overflowing icons into a "…" menu (with their labels and counts) as the rail runs out of room, restoring them as it grows ([#5313](https://github.com/gitkraken/vscode-gitlens/issues/5313))
- Adds a keyboard shortcuts reference to the _Commit Graph_ &mdash; opened from a new keyboard icon in the graph's sidebar rail &mdash; listing all supported navigation, search, open, and commit shortcuts with platform-aware key labels ([#5312](https://github.com/gitkraken/vscode-gitlens/issues/5312))
- Adds back/forward navigation to the _Commit Graph_ details panel and _Inspect_ view &mdash; Back/Forward buttons in the commit and working changes (WIP) detail headers step back through previously-viewed commits, stashes, and working changes, best-effort re-selecting the row in the _Commit Graph_ ([#5316](https://github.com/gitkraken/vscode-gitlens/issues/5316))
- Adds the ability to push up to (and including) a specific commit from the _Commit Graph_ &mdash; commits ahead of the branch's upstream show an unpushed indicator that doubles as a one-click _Push to Commit_ action, also available in the commit's context menu ([#5314](https://github.com/gitkraken/vscode-gitlens/issues/5314))
- Adds an _Open Worktree File_ action to the commit file menu in the _Commit Graph_ details and _Inspect_ view that opens a committed file from the worktree whose branch contains the commit &mdash; useful in multi-worktree repos where the file's working copy lives outside the currently-scoped worktree, with a worktree picker when more than one worktree applies ([#5317](https://github.com/gitkraken/vscode-gitlens/issues/5317))
- Adds a working changes bar to the _Commit Graph_ &mdash; a horizontal bar above the graph with a pill for each worktree that has uncommitted changes or unpushed commits (primary and secondary worktrees alike), showing its branch and agent status, with an up-arrow (↑) marking unpushed work and a hover breakdown of changed files and commits to push; clicking a pill reveals and selects that worktree's working changes in the graph and opens its details ([#5301](https://github.com/gitkraken/vscode-gitlens/issues/5301))
- Adds heat decay, read/edit color blending, and a live pulse to the experimental _Agent Activity Treemap_ &mdash; touched files now fade over a configurable window after each tool call instead of switching on and off, reads and edits blend as cyan/amber weighted by recency, and a soft pulse marks the file an agent is reading or editing right now
  - Adds a `gitlens.graph.experimental.visualizations.activityDecay` setting (30 seconds to 30 minutes, default 5 minutes) with a matching decay-window picker in the treemap toolbar
  - Rolls sub-agent file activity up to the parent session so the heatmap reflects what a session's sub-agents are reading and editing
- Adds the ability to squash multiple commits from the _Commit Graph_ &mdash; select two or more contiguous commits on the current branch, right-click, and choose _Squash Commits_ to combine them into one, then review and edit the combined commit message (or keep only the oldest commit's message) ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds the ability to drop multiple commits from the _Commit Graph_ &mdash; select commits on the current branch, right-click, and choose _Drop Commits_ to remove them ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds the ability to reword a commit's message from the _Commit Graph_ &mdash; right-click a commit on the current branch and choose _Reword Commit_ ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds a _Modify Commits (Interactive Rebase)_ action to the _Commit Graph_ that opens the interactive rebase editor scoped from the selected commit(s) for squashing, rewording, reordering, dropping, and editing ([#5161](https://github.com/gitkraken/vscode-gitlens/issues/5161))
- Adds a _Publish Branch_ action to the _Commit Graph_ header that appears when the current branch has no upstream &mdash; publishes (pushes and sets the upstream of) the current branch in one click, sitting just left of _Fetch_ and collapsing to its icon when the header is too narrow ([#5327](https://github.com/gitkraken/vscode-gitlens/issues/5327))
- Adds the ability to multi-select files in the _Commit Graph_ details and _Inspect_ view to act on several at once &mdash; Ctrl/Cmd+click to toggle, Shift+click for a range, and Ctrl/Cmd+A to select all &mdash; with batch actions from the context menu and toolbar: open files, open selected changes (multi-diff), open on remote, copy paths and relative paths, and (for working changes) stage, unstage, stash, and discard ([#5328](https://github.com/gitkraken/vscode-gitlens/issues/5328))
- Adds a `gitlens.advanced.repositorySearch.enabled` setting to control whether GitLens scans workspace folders to discover Git repositories &mdash; when disabled, GitLens relies solely on VS Code's built-in Git/SCM integration to report when repositories are opened or closed
- Adds the ability to stash only the staged changes from the working changes (WIP) file list in the _Commit Graph_ and _Inspect_ view &mdash; when both staged and unstaged changes are present, the _Stash_ action stashes only the staged changes by default (Alt-click to stash all)

### Changed

- Improves graph selection reliability and performance
- Honors VS Code's `scm.defaultViewSortKey` setting when sorting working changes (WIP) file lists in the _Commit Graph_, while keeping unresolved conflicts at the top ([#5289](https://github.com/gitkraken/vscode-gitlens/issues/5289))
- Changes the _Add as Co-author_ action in the _Commit Graph_ to append the co-author to the graph's working changes (WIP) commit message box instead of writing to the Source Control input and switching to the Source Control view ([#5294](https://github.com/gitkraken/vscode-gitlens/issues/5294))
- Improves _Commit Graph_ update performance by skipping redundant re-renders when content is structurally unchanged
- Improves performance in large workspaces by only watching a repository's working tree while its node is expanded in the views
- Improves resilience of GitHub requests by retrying transient gateway and network failures (502, 503, 504) with exponential backoff, restricted to idempotent reads
- Improves commit feedback and error handling when committing working changes (WIP) in the _Commit Graph_ &mdash; locks inputs with a spinner during commits and surfaces classified, actionable errors for signing, pre-commit hook, and conflict failures ([#5290](https://github.com/gitkraken/vscode-gitlens/issues/5290))
- Improves how partially staged (mixed) files are counted and displayed in the _Commit Graph_ file tree badges ([#5291](https://github.com/gitkraken/vscode-gitlens/issues/5291))
- Improves resilience when VS Code updates GitLens in the background &mdash; surfaces an actionable _Reload Window_ prompt when a lazily-loaded feature can no longer be found, instead of a cryptic error
- Changes the _Apply Stash_ command labels to _Apply / Pop Stash_ across the command palette, view context menus, _Commit Graph_, and tooltips to clarify that both apply and pop are available

### Fixed

- Fixes opening the _Commit Graph_ in multi root workspace to the correct repo ([#5276](https://github.com/gitkraken/vscode-gitlens/issues/5276))
- Fixes commit signing not being detected as enabled when only VS Code's `git.enableCommitSigning` setting is on (without `commit.gpgsign` set in Git config) &mdash; GitLens-driven commits (e.g. the _Commit Composer_) now sign in this case
- Fixes the `gitlens.advanced.similarityThreshold` setting being ignored when computing Git status &mdash; rename detection in status, working changes (WIP), and stash file lists used Git's default threshold (50%) instead of the configured value
- Fixes the `gitlens.advanced.similarityThreshold` setting being ignored when listing changed files for a diff &mdash; rename detection used Git's default threshold (50%) instead of the configured value
- Fixes force push from the _Push_ command always using `--force-with-lease` (and `--force-if-includes`) and ignoring VS Code's `git.useForcePushWithLease` and `git.useForcePushIfIncludes` settings &mdash; the confirmation could offer a plain `--force` while GitLens still pushed with lease; it now honors the configured preference
- Fixes _Stash Unstaged Changes_ also stashing staged changes when an untracked file is involved &mdash; including untracked files no longer drops the `--keep-index` flag, so staged changes are correctly kept intact ([#5281](https://github.com/gitkraken/vscode-gitlens/issues/5281))
- Fixes push from the _Commit Graph_ silently pushing to a wrong remote branch when the local branch tracks a differently-named upstream (e.g., `feature/foo` tracking `origin/main`) &mdash; now correctly pushes to the configured upstream branch instead of creating a new remote branch ([#5304](https://github.com/gitkraken/vscode-gitlens/issues/5304))
- Fixes the working changes (WIP) _Generate Commit Message_ in the _Commit Graph_ losing its result when the selection changes while a message is generating &mdash; the generation now continues and the message lands in the originating worktree's commit input (or its saved draft if you've navigated away) ([#5295](https://github.com/gitkraken/vscode-gitlens/issues/5295))
- Fixes the commit details metadata bar in the _Commit Graph_ and _Inspect_ view not surfacing a reachable tag when a commit is contained only in tags (and not any branch) &mdash; now shows the most relevant tag with a tag icon and color, matching how branches are shown ([#5293](https://github.com/gitkraken/vscode-gitlens/issues/5293))
- Fixes incorrect GitLab avatars being shown when multiple GitLab users share the same name ([#2205](https://github.com/gitkraken/vscode-gitlens/issues/2205))
- Fixes the repository picker being incorrectly skipped when an action targets a repository that isn't surfaced in VS Code &mdash; for example, using the stash action on a secondary worktree's working changes when that worktree isn't open in VS Code ([#5292](https://github.com/gitkraken/vscode-gitlens/issues/5292))
- Fixes potential runtime errors when formatting invalid or unparseable dates ([#4922](https://github.com/gitkraken/vscode-gitlens/issues/4922))
- Fixes an issue where unchecking _Interactive Rebase Editor_ in the GitLens settings UI would not persist &mdash; the checkbox would revert to checked after changing another setting or reopening the settings UI ([#5277](https://github.com/gitkraken/vscode-gitlens/issues/5277))
- Fixes an issue where the GitKraken CLI was not auto-installed on hosts where MCP auto-registration is unsupported (older VS Code, Windsurf, JetBrains, Trae, Kiro, Zed, etc.), preventing Claude hooks installation and agent dispatch in _Start Work_ and _Start PR Review_ flows ([#5280](https://github.com/gitkraken/vscode-gitlens/issues/5280))
- Fixes the _Commit Graph_ intermittently flashing a "No commits" message during concurrent Git operations
- Fixes styling in rendered markdown (commit message hovers, autolinks, and details) being stripped in webviews by the stricter content-security policy introduced in v18.0.0
- Fixes the `gitlens.advanced.skipOnboarding` setting not being honored, so onboarding surfaces could still appear even when it was enabled
- Fixes the _Commit Graph_ details panel showing stale working changes after the view regains visibility ([#5322](https://github.com/gitkraken/vscode-gitlens/issues/5322))


---

<a id="v18-0"></a>

## Version 18.0

#### Wednesday, May 27, 2026

GitLens 18 turns the _Commit Graph_ into a workbench: an embedded details panel lets you inspect, compare, review, stage, and commit without switching views, while a new overview sidebar puts your work and associated agent sessions within easy reach. AI agents become first-class citizens, integrated deeply within your workflows &mdash; see sessions associated with your current branch in the details panel, plus monitor active sessions with contextual actions wherever you work in GitLens. This release also adds branch pinning, multi-worktree WIP rows, a focused graph scope for the branch you care about, and a wide range of performance and quality-of-life improvements throughout the Graph.

<img src="/wp-content/uploads/gl-18-0-hero.png" class="help-center-img img-bordered">

### The Commit Graph, Now a Workbench

The _Commit Graph_ is no longer just a place to read history &mdash; it's where you work. A new embedded details panel allows you to inspect commits, working changes, compare branches, conduct reviews with AI, and compose commits without leaving the context of your Graph. The panel can be anchored to the right (the default) or to the bottom of the Graph &mdash; hold <kbd>Alt</kbd> while clicking the details toggle to switch between the two. 

This revamped commit details panel adds richer file-tree actions, multi-diff support, and quick toggles to jump into **Compose**, **Review**, and **Compare** modes. 

### Review and Compose, Directly in the Graph

Both _Commit Composer_ and a new _AI Code Review_ tool are now available right inside the Graph's details panel. Switch into compose mode to generate organized commits from your working changes, with multi-diff editor support for previewing proposed commits. Switch into review mode to get an AI-powered review of your changes, with summaries that identify focus areas with severity indicators, so you can check your work before you ship.

<img src="/wp-content/uploads/gl-18-0-review-mode.png" class="help-center-img img-bordered">

### AI Agents in GitLens

GitLens 18 introduces support for integrating AI coding agents, starting with Claude Code. Agent status is now surfaced throughout GitLens so you can monitor, focus, and act on parallel agent sessions without leaving the IDE and context from GitLens.


<img src="/wp-content/uploads/gl-18-0-agent-status.png" class="help-center-img img-bordered">

**Your agents' status, deeply integrated** &mdash; A new agent status pill appears on _Home_ view branch cards, the _Commit Graph_ overview cards, the _Commit Graph_ commit details panel, and the new _Agent Sessions_ sidebar panel. Pills are color-coded by state (running, idle, waiting for input, etc.), with subtle animations when sessions are active or when an agent is waiting for your input. Sessions awaiting input also surface on overview cards so you can find what needs attention at a glance.

**Agent Sessions panel** &mdash; A new panel in the _Home_ view and the _Commit Graph_ sidebar lists all your agent sessions in a streamlined view, with the same rich status hovers and quick actions as the inline pills. Switch between list and tree layouts to organize sessions by workspace or worktree.

**Claude Code hooks integration** &mdash; Install Claude Code hooks directly from GitLens via the _Home_ view banner, the _Commit Graph_ header, the agents sidebar banner, or the integrations menu. Hooks give GitLens real-time visibility into Claude Code session state. A dedicated command lets you uninstall hooks at any time.

**Agent Kanban (Experimental)** &mdash; A new experimental _Agent Kanban_ view turns the _Commit Graph_ into an interactive board for tracking your active AI agent sessions. Toggle it from the graph sidebar ('_Show Agent Kanban_') to see sessions partitioned across four columns: _Needs Input_, _Working_, _Idle_, and _Inactive_. From each session card you can approve or deny pending agent permissions, view a proposed plan, and jump straight to the session's working changes.

The _Agent Kanban_ view is enabled by default and can be toggled with the `gitlens.graph.experimental.kanban.enabled` setting.

### Multi-Worktree WIP Rows

The Graph now displays a work-in-progress row for **each** worktree, not just the active one, so you can see, review, and act on changes across all your parallel work without switching. Each WIP row shows live file stats, supports the full set of WIP actions (commit composition, conflict resolution, generating commit messages, and more), and updates in real time as files change. WIP scrollbar markers help you quickly locate uncommitted changes, with a configurable theme color and a setting to toggle them on or off.

<img src="/wp-content/uploads/gl-18-0-multi-wip.png" class="help-center-img img-bordered">

### Commit Graph Sidebar

The expandable sidebar introduced in 17.12 gets new, powerful views and actions in 18.0:

- **Overview panel** &mdash; surfaces active and recent branches as cards with WIP changes, upstream tracking status, pull requests, associated issues, contributor avatars, and quick actions (Switch, Open Worktree, Fetch, Publish Branch, and compare actions). Rich hover popovers expand each card with the full action set, autolink chips, and Launchpad mergeability tinting.
- **Agent Sessions panel** &mdash; see all your active agent sessions with status pills, branch/worktree associations, and quick actions to keep your agents unblocked.
- **Remote actions** &mdash; full context-menu support for remotes alongside branches, tags, stashes, and worktrees.
- **Worktree parity** &mdash; worktrees now have the same context-menu actions as branches, including AI-powered explain and generate changelog actions.
- **Tree-mode layout toggle** has moved into the filter actions area for a cleaner, more contextual placement.
- **Pin or overlay** &mdash; pin the sidebar in place, or float it as an auto-collapsing overlay over the Graph.

### Visualizations in the Graph

GitLens 18.0 brings powerful new ways to visualize your repository directly in the _Commit Graph_. A more capable _Visual History_ view has been integrated into a _Visualizations_ mode that now hosts new experimental Treemap views to visualize changes by file, commit, and agent activity.

Open the visualizations by clicking on the 'Show Visualizations' pulse icon at the bottom of the Graph sidebar, then use the switcher in the header to move between the _Visual History_ timeline and the new Treemap views.

#### Visual History

The _Visual History_ view renders your repo's history as a time-bucketed view of activity, with author avatars, configurable additions/deletions colors, and richer hover, zoom, scroll, brush, slider scrub, and slice filtering interactions. Scope the history down to specific files and folders, and slice the changes by branches rather than authors if needed.

<img src="/wp-content/uploads/gl-18-0-graph-visual-history.png" class="help-center-img img-bordered">

#### Treemap Visualizations (Experimental)

As an alternative to the _Visual History_ timeline, the _Commit Graph_ now offers three Treemap views that lay your repository out spatially. Each supports hover tooltips, click-to-zoom into folders, and breadcrumb navigation to track and retrace your path:

- **Files Treemap** &mdash; lays out your files and folders as nested rectangles, sized by their footprint, for a bird's-eye view of how the repository is structured.
- **Commits Treemap** &mdash; highlights where development is concentrated by sizing files and folders according to commit activity, making your most-changed areas stand out at a glance.
- **Agent Activity Treemap** &mdash; projects live AI agent presence onto your file structure in real time, distinguishing the files an agent is reading from the ones it's editing.

The Treemap visualizations are enabled by default and can be toggled with the `gitlens.graph.experimental.visualizations.enabled` setting. When disabled, only the _Visual History_ is available.

### Focus on the Work You Care About

You can now pin a branch to the leftmost column of the _Commit Graph_ so it always stays visible as a reference, even as other branches come and go. Pin or unpin from the row's context menu, and click the pinned ref in the Graph header to jump straight to it.

A new focused branch mode on the _Commit Graph_ header lets you focus the Graph on a single branch, with a searchable tree or list view to pick the focus. While scoped, the Graph renders along the focused branch's first-parent line (with the "Simplify Merge History" toggle automatically applied), and the minimap zooms to the relevant range. Clear visual indicators show when the Graph is scoped or modified by filters. The minimap settings have moved into the minimap itself, and dedicated header buttons toggle the sidebar, minimap, and details panel.

### Conflict Resolution Workflows

Conflict resolution now reaches into the _Commit Graph_ and _Interactive Rebase_ editor:

- Resolve conflicts directly from the Graph's WIP details panel, with merge-conflict status surfaced inline
- Conflict resolution actions are also available in the _Interactive Rebase_ editor's conflict file list, with dedicated diff-left/diff-right icons
- The _Interactive Rebase_ editor now shows a dismissible banner during the planning phase clarifying that closing the tab automatically starts the rebase

### Open the Graph in a New Window

A new "Open in New Window" command opens the _Commit Graph_ in a detached window for multi-monitor workflows. It's now the primary action in the Graph view's menus, with "Open in Editor" available as a modifier-key alternative.

### Performance and Reliability

GitLens 18 continues to invest in performance and stability improvements:

- **Faster Graph details loading** &mdash; commit metadata is now eagerly rendered from graph rows to instantly populate the details panel and skip IPC delays, with cached base file contents during compose sessions to eliminate redundant git reads.
- **Smarter caching** &mdash; granular TTLs based on ref mutability (5 minutes for full SHAs, 60 seconds for symbolic refs), cached branch merged-status checks, cached left/right commit counts for comparisons, and shared branch metadata across worktrees.
- **Lazy enrichment** &mdash; branch overview enrichment shifts from eager bootstrap to lazy loading, dramatically reducing initial resource contention during graph rendering.
- **Better cancellation** &mdash; abort signals now propagate through the Git command queue, RPC layer, and webview enrichment, so cancelled work stops instead of running to completion.
- **Coalesced refresh** &mdash; working-tree change emissions are coalesced into a single event per tick, eliminating redundant UI refreshes
- **Startup improvements** &mdash; Git and MCP providers now register in parallel, and the CLI version check is deferred to reduce extension activation time.

---

### Added

- Introduces an all-new _Commit Graph_ experience &mdash; a comprehensive redesign that pulls commit inspection, AI workflows, comparisons, branch focus, and working-change management directly into the graph
  - Adds an embedded details panel &mdash; replaces the standalone Graph Details view with an integrated panel that handles commit details, working changes, branch comparisons, AI reviews, and commit composition without leaving the graph
    - Adds a `gitlens.graph.details.location` setting to anchor the details panel at the bottom or right, with Alt+click on the details button to toggle
  - Adds an integrated AI Compose mode &mdash; provides a much improved AI-powered commit composition directly within the graph, with per-commit include/exclude toggles, multi-diff editor support, a virtual filesystem provider for synthesized per-commit diffs, cancellable generation, parallel/background operation, and copy and send-to-agent actions
    -Adds an integrated AI Code Review mode &mdash; surfaces severity-tagged findings with tooltips, copy and send-to-agent actions on outputs, and PR/issue/autolink context input ([#5235](https://github.com/gitkraken/vscode-gitlens/issues/5235))
  - Adds an integrated Compare mode &mdash; opens comparisons directly inside the graph instead of the _Search & Compare_ view, with Ahead/Behind/All Files tabs, working tree comparisons for peer worktrees, AI-powered explaination and changelog generation, and an _Open in Search & Compare_ action to persist ad-hoc comparisons
  - Adds a refined header with WIP (work-in-progress) status and stash action
  - Adds a unified UI/UX for scoping and filtering the graph
    - Adds an _Agent Branches_ option to filter the graph to show only the branches or worktrees with active or recent agent activity
    - Adds a _Focus Branch_ option to scope the graph to just the changes on specific branch via a new branch selector (or the new Overview or Agents side bar), with merge-target anchoring
  - Adds all new experiences to the graph _Side Bar_
    - Adds pinned and overlay modes &mdash; overlay mode floats over the graph instead of pushing it aside, with auto-collapse on focus loss and a pin/unpin toggle in the panel header
    - Adds an _Overview_ side bar panel &mdash; surfaces active and recent branches as rich cards with WIP stats, upstream tracking, associated pull requests, issues, and agents, as well as quick actions and rich hover details
      - Clicking on an _Overview_ card instantly focuses (scopes) the graph to just the changes on the selected branch
    - Adds an _Agents_ side bar panel &mdash; surfaces active and recent agents with their activity, associated branches/worktrees
      - Clicking on an agent row instantly focuses (scopes) the graph to just the changes on the selected wokrtree, and selects the agent in the details panel
    - Adds a _Visualizations_ mode to the side bar &mdash; houses the all-new _Visual History_, and 3 experimental treemap visualizations
      - _Visual History_ &mdash; rebuilt from the ground up to provide a better experience with dynamical loading and dealing with many contributors and/or branches
      - _Files Treemap_ &mdash; an experimental spatial visualization of file layout within the repository color coded by file type, with hover tooltips, deep zoom-to-folder, and tracking breadcrumbs
      - _Commits Treemap_ &mdash; an experimental spatial visualization of commit activity within the repository colorized as a heatmap
      - _Agent Activity Treemap_ &mdash; an experimental spatial visualization of realtime agent activity. See where your agents are currently reading and editing across your repository
    - Adds an experimental _Agent Kanban_ mode to the side bar &mdash; an interactive Kanban board grouping active agent sessions by state (Working, Idle, Inactive, Needs Input), with inline plan view and permission approval directly from session cards
    - Adds comprehensive context menu support for worktrees in the sidebar and Commit Graph &mdash; brings feature parity with branches, including Reveal in File Explorer, AI-powered actions (explain WIP, generate changelog), Open in Terminal, and Copy Path
  - Adds an all new way to manage worktrees and working changes (WIP)
    - Changes working changes (WIP) rows to always be visible regardless of whether or not there are uncommitted changes
      - When there are uncommitted changes, the _Details Panel_ now allows you to review, stage, and commit your changes, or leverage the all-new _Compose_ and _Review_ modes to have AI review and automatically compose your changes into a set of well-structured commits
      - When there are no uncommitted, the _Details Panel_ transforms into a hub to guide you to the next steps &mdash; like pulling, pushing, drafting a PR, reviewing, recomposing, etc. Everything to help you get your changes merged faster ([#5218](https://github.com/gitkraken/vscode-gitlens/issues/5218))
    - Adds support for working changes (WIP) rows from secondary worktrees
      - Selecting a WIP rows provides file actions, conflict resolution, and live-updating stats for non-active worktrees, plus _Open in Integrated Terminal_ and _Open Worktree in New Window_ actions on the header
    - Adds the ability to discard uncommitted changes
    - Adds smart push/pull on the WIP details panel header &mdash; offers Force Push when a branch is both ahead and behind its remote
    - Adds conflict resolution actions to the WIP details panel
    - Adds the ability to share working changes as a Cloud Patch directly from the WIP header
    - Adds persistence of in-progress commit messages and amend state per worktree &mdash; drafts are restored when switching contexts, the original message is restored on Undo Commit, and per-worktree search box and filter preferences persist across sessions
    - Adds Jump to Working Changes &mdash; quickly navigate from the selected commit to the most relevant WIP node in the same lane, with primary-worktree fallback
    - Adds bulk staging operations &mdash; _Stage All_ and _Unstage All_, with Alt-click on mixed-state checkboxes to unstage all currently staged items
  - Adds auto-fetch while the _Commit Graph_ is visible and focused, yielding to VS Code's built-in Git auto-fetch when enabled, with a fetch button popover to manage settings and a minimum interval floor to prevent excessive fetching
  - Adds search and filtering improvements &mdash; adds a `type:wip` operator to filter to working changes, and column header filters with interactive pickers for authors, refs, and files
  - Adds the ability to pin and unpin branches &mdash; pinned branches persist across sessions with a jump-to-pinned-branch actionn ([#5139](https://github.com/gitkraken/vscode-gitlens/issues/5139), [#5181](https://github.com/gitkraken/vscode-gitlens/issues/5181))
  - Adds inline row actions for commit and stash rows including open all changes (Alt to compare against working tree) and apply/drop stashes
  - Adds a floating "HEAD" indicator to the graph to quickly jump to the HEAD commit
  - Adds a completely rebuilt minimap with better performance and zoom controls and clearer markers
  - Adds minimap and scrollbar markers for worktrees &mdash; surfaces uncommitted changes on the minimap and scrollbar with a configurable theme color and a toggle setting
  - Adds an _Open in New Window_ toolbar view action &mdash; opens the graph in a detached window for multi-monitor workflows, with _Open in Editor_ available as the Alt+click alternative
- Adds comprehensive AI agent integration throughout GitLens
  - Adds an agent status framework with Claude Code support using Claude Code Hooks (must be installed) &mdash; surfaces sessions across the _Home_ view, _Commit Graph_ overview cards ([#5170](https://github.com/gitkraken/vscode-gitlens/issues/5170)), WIP rows, _Commit Details_, _Agents_ side bar panel, and the experimental _Agent Kanban_ mode
  - Adds an _Agent Branches_ visibility mode to the _Commit Graph_ that filters branches to only those with active or recently active agents
  - Adds an agent picker to _Start Work_ and _Start Review_ flows, plus a default-agent picker, _Switch Default Agent_ command, and Start Work/Start Review in Agent actions in the _Home_ and _Commit Graph_ views
  - Adds support for opening agent sessions hosted in other VS Code windows
  - Adds a _Resume in Terminal_ fallback when an agent session fails to open or is active in another VS Code window
  - Adds notifications for peer-discovered agent session permissions
  - Adds an experimental _Agent Kanban_ mode &mdash; an interactive Kanban board grouping active agent sessions by state
- Adds conflict resolution actions to the _Interactive Rebase_ editor conflict file list
- Adds a close-tab warning banner to the _Interactive Rebase_ editor &mdash; displays a dismissible informational banner during the planning phase to clarify that closing the tab automatically starts the rebase ([#5123](https://github.com/gitkraken/vscode-gitlens/issues/5123))
- Adds a `gitlens.rebaseEditor.openBehavior` setting to control where the _Interactive Rebase_ editor opens when automatically reopened on a paused rebase &mdash; `auto` (default) opens beside only when a multi-pane layout already exists; `beside` always opens in a side group
- Adds Seti file icon theme support for webviews &mdash; files in webview trees now display the correct Seti glyph
- Adds folder actions in _Details Panel_ and _Inspect_ view
- Adds a unified onboarding reset command that consolidates the previous Banners and Usage Tracking resets into a single restore-first-time-experience action

### Changed

- Switches the _Commit Graph_ sidebar to be visible by default for new installations in overlay mode
- Switches _Open Worktree in New Window_ to be the primary action and _Open Worktree_ to be the alternative across views and the _Commit Graph_
- Improves the default _Interactive Rebase_ editor density to a more spacious layout
- Improves _Commit Graph_ performance and responsiveness &mdash; content-fingerprint deduping of full-state pushes, incremental row-stats sending, avatar omission for unchanged rows, in-memory WIP caches, and debounced repository event coalescing
- Improves branch overview enrichment performance &mdash; tiered caching using stored merge targets as cache keys, lazy loading, and parallelized metadata fetches
- Improves Git diff performance &mdash; switches diff operations to `numstat`+`summary` instead of `name-status` parsing
- Improves Git command result caching &mdash; granular TTLs based on ref mutability (5-minute cache for full SHAs, 60-second failsafe for symbolic refs), plus caching for left-right commit counts, merge bases, and per-branch config lookups
- Improves performance for GitHub virtual repositories &mdash; adds caching for commit details, counts, merge bases, paged branches/tags, and default branches, plus deduping of in-flight GraphQL requests
- Improves the _Commit Graph_ minimap colors and contrast for better theme accessibility, and adds out-of-view proxy handles and improved scope zoom rendering
- Improves the _Connect More Agents_ picker to only show agents that don't already have the GitKraken MCP installed, with a clearer empty state when all detected agents are already connected ([#5142](https://github.com/gitkraken/vscode-gitlens/issues/5142))
- Improves repository visibility detection with promise-based caching to prevent redundant computation
- Improves Git command priority inference &mdash; keeps polymorphic history commands at normal priority, requires expensive full-history walks to opt into background priority
- Improves the default and maximum limits for concurrent background Git processes
- Improves branch comparison default target logic &mdash; automatically suggests the merge target of a branch as the default right-side reference and uses branch names instead of SHAs for stability
- Improves stash reachability filtering &mdash; uses Git's authoritative stash metadata via the `%s` subject parsing instead of expensive parent-timestamp tracking
- Improves AI error handling and network detection &mdash; distinguishes between "No Network" and "Unreachable" states, with automatic retry on network failures and a recursive cause-chain analysis for better diagnostics
- Improves header and breadcrumb responsiveness across webviews &mdash; priority-based collapsing with compact icons and overflow popovers for narrow views
- Migrates from `node-fetch` to native fetch and adopts VS Code's built-in proxy support &mdash; removes the custom `gitlens.proxy` setting in favor of standard VS Code and OS proxy settings
- Migrates the webview component library to WebAwesome, modernizing selects, overlays, sliders, and tooltips with workspace-color-aware highlights

### Fixed

- Fixes an issue where starting an interactive rebase forced a split-pane layout when git paused for a `reword` &mdash; the _Interactive Rebase_ editor now opens as a hidden background tab alongside the commit message editor instead of stealing the active tab ([#5203](https://github.com/gitkraken/vscode-gitlens/issues/5203))
- Fixes an issue where untracked files were missing from the _Compare Working Tree with..._ file list unless manually staged with `git add -N` first ([#5158](https://github.com/gitkraken/vscode-gitlens/issues/5158))
- Fixes an issue where the _Interactive Rebase_ editor would auto-open during the brief teardown window after a rebase completed (or on non-interactive rebases), showing stale or empty state ([#5217](https://github.com/gitkraken/vscode-gitlens/issues/5217))
- Fixes an issue where the _Interactive Rebase_ editor would show a blank state when opened on a repository outside the workspace (e.g., from a terminal) ([#5229](https://github.com/gitkraken/vscode-gitlens/issues/5229))
- Fixes an issue where the terminal integration relaunch warning persisted due to stale environment variable state ([#4977](https://github.com/gitkraken/vscode-gitlens/issues/4977))
- Fixes an issue where MCP reinstallation could fail when the proxy binary was locked on Windows ([#5126](https://github.com/gitkraken/vscode-gitlens/issues/5126))
- Fixes an issue where stashing staged changes was not using the `--staged` flag ([#5138](https://github.com/gitkraken/vscode-gitlens/issues/5138))
- Fixes an issue where the currently selected option is not visually distinguishable in select-style menus on the _Home_ view (agent workspace filter, recent timeframe filter) and elsewhere (_Visual History_ period menu, _Commit Graph_ overview filter) &mdash; most noticeable on light themes ([#5259](https://github.com/gitkraken/vscode-gitlens/issues/5259))
- Fixes an issue where diff hunks could be missing for renamed or copied files in editor gutters and hovers &mdash; rename detection was inadvertently filtering out valid diffs
- Fixes an issue where stash apply and pop actions could fail silently due to missing stash numbers, producing invalid `stash@{undefined}` references, and where the _Commit Graph_ would not refresh when a stash was dropped
- Fixes an issue where GitLens would automatically re-open repositories that the user had explicitly closed via the SCM interface
- Fixes an issue where the _File History_ context menu actions on commits and folders launched a standalone editor instead of integrating with the embedded _Visual History_ in the _Commit Graph_
- Fixes an issue where the SCM grouped views could intermittently "detach" &mdash; alt commands have been removed from SCM grouped views due to flakey/sticky alt detection in VS Code
- Fixes an issue where the _Compare Working Tree_ "Show All Diffs" button used inverted diff direction
- Fixes an issue where authentication errors could surface noisy notifications and break-on-exception breakpoints instead of returning safe defaults
- Fixes various race conditions and stale-state issues across the _Commit Graph_ during repository, branch, and worktree switches &mdash; including phantom anchors after removing the last secondary worktree, cross-repo data contamination during rapid swaps, lost state notifications during in-flight updates, and forced reloads during panel restoration
- Fixes an issue where the working tree comparison could incorrectly include untracked files for revision-range diffs

---

### Previous Release Notes

- [Version 17.x Release Notes](/gitlens/GL-Release-v17-x)
- [Older Release Notes (v16.x and earlier)](/gitlens/GL-Releases-Old)
