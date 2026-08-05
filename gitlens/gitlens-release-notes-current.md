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

<a id="v19-0"></a>

## Version 19.0

#### Tuesday, August 11, 2026

GitLens 19 rebuilds the _Commit Graph_ from the ground up, moving to the GitLens panel as the primary surface to keep your workflows moving. It's noticeably faster on large repositories, hosts a handful of powerful tools to manage parellel work, is more configurable than ever, and completely keyboard navigable &mdash; rows and row actions included.

The graph also tells you far more at a glance. HEAD, its upstream, and your merge target are marked right on the rows, the reference pills, and the scroll bar, so you always know where you stand &mdash; and hovering _Pull_ shows you what a pull would bring in, and where it would conflict, before you run it. Additionally, Lane folding allows you to expand/collapse series of commits in a lane to simplify history, a new _Changes_ column shows the size and shape of every commit, and focusing a branch or tag opens a full sheet with its tracking status, pull requests, issues, and what to do next. When you already know the name of what you're looking for, press <kbd>/</kbd> and start typing &mdash; the graph moves to it as you go.

More of your day moves into the graph, too. Your open pull requests and remote branches join the side bar, your account, walkthrough progress, and integrations are a click away in the header, and composing commits with AI now exclusively happens right in the Graph's details panel instead of a view of its own.

And keeping your branches up to date gets easier, too - let AI handle any conflicts along the way. Choose **Automatic Rebase** and GitLens runs the rebase start to finish, letting AI handle every conflicting step, then hands you a summary explaining each decision it made &mdash; with one-click undo if you don't like what you see. GitLens can also verify SSH-signed commits now, with a new visual editor that builds the allowed-signers file Git needs for you.

<img src="/wp-content/uploads/gl-19-0-hero.png" class="help-center-img img-bordered">

### An All-New Commit Graph

The _Commit Graph_ is now drawn by a new layout engine paired with a Lit renderer. The vendored React renderer, its stylesheets, and its dependencies have been removed entirely. 

- **Lanes that hold still** &mdash; the engine's incremental and splice paths reuse prior layout results, so paging in history, fetching, or rewriting it no longer shifts the lanes you were reading. Trunk lanes can't be evicted by branch tips or fetched merges, and a re-rooted trunk is detected rather than reshuffled.
- **Grouped lanes by default** &mdash; lane art folds into an anchor zone alongside your other columns, with `gitlens.graph.lanes.grouped.min` and `gitlens.graph.lanes.grouped.max` controlling how many lanes render inline and how much row width they may claim.
- **Compact by default** &mdash; a new `gitlens.graph.lanes.density` setting defaults to `compact`, and the author, date, and SHA columns start narrower.
- **Lane folding** &mdash; collapsible lane segments get expand/collapse chevrons in a fold strip beside the graph, configurable via `gitlens.graph.lanes.folding.enabled` and `gitlens.graph.lanes.folding.default`.
- **A responsive row layout** &mdash; the new `gitlens.graph.style` setting picks between `table` (single-line rows with columns) and `list` (stacked two-line rows), with `auto` switching to `list` when the panel is too narrow for the columns.
- **A sticky timeline** &mdash; a pill groups scrolled rows into the same relative time buckets as the date column, expanding while you scroll to reveal the range and yielding when it overlaps something interactive, with optional separator lines between date groups (`gitlens.graph.timelineSeparators`).
- **Better columns** &mdash; inline filter buttons that reveal on hover, breadcrumbs showing the grouping hierarchy, double-click auto-fit that measures real date formats, a wider resize hit area, and a new _Quick Refresh_ button that re-lays out the lanes on demand without a refetch.

### The Changes Column

A new _Changes_ column shows each commit's diffstat, with four visualizations you can switch between from the column header: **numbers**, **squares**, **bar**, and **bipolar** (a two-sided bar). It degrades gracefully as the column narrows &mdash; through compact and mini stages down to a single "churn ring" glyph at 36px &mdash; and uses positional, grayscale-friendly markers so deletions stay distinguishable without relying on color.

Because computing stats can be expensive on large repositories, the column is off by default and offers a one-time opt-in (`gitlens.graph.changesColumn.enabled`, with the visualization in `gitlens.graph.changesColumn.mode`).

### Always Know Where You Stand

<!-- TODO: upload gl-19-0-row-markers.png -->

HEAD, its upstream, and your merge target are now called out everywhere the graph can call them out:

- **Role-colored reference pills and row markers** &mdash; HEAD in green and its upstream in a deeper green of the same hue (they're one branch shown in two places), with the merge target as a jump segment on the pill. Each of those commits also gets a left-edge indicator that expands on hover, and references sitting on the same commit collapse into one.
- **A merge target scroll marker** &mdash; a full-width line on the scroll bar alongside the existing HEAD and upstream markers, themeable via `gitlens.graphScrollMarkerMergeTargetColor`. Right-clicking the scroll marker rail now toggles marker types directly.
- **An unpulled commit indicator** &mdash; commits on your upstream that a pull would bring in show an always-visible download glyph, colored to match the _Pull_ button, mirroring the existing indicator on unpushed commits.
- **An always-visible overview bar** &mdash; the working changes (WIP) bar used to hide itself entirely on a single clean worktree; it now always shows the current worktree with jumps to its HEAD tip, upstream (with ahead/behind), and merge target, alongside any other worktrees' working changes.
- **New default colors** &mdash; a vibrant, perceptually-uniform lane palette for dark and high-contrast themes where no lane visually dominates, plus retuned HEAD and upstream greens that separate on brightness rather than saturation so they stay distinguishable with color blindness.

### Branch and Tag Sheets

Focusing a reference pill now opens a sheet in the details panel for that branch or tag &mdash; the WIP details panel, re-scoped to the ref. Each sheet carries an issue and pull request strip, upstream and merge-target relationship cards (where the counterpart's name is the edit affordance) with tracking status and the relevant sync, rebase, or merge actions, an AI band for _Explain_ and _Generate Changelog_ with a scope chip, and next-step rows tailored to the kind of ref. Tags default their comparison to the newest previous tag; remote branches compare against their merge target.

Sheets also carry _Focus_ and _Hide_ toggles, an _Open on Remote_ chip, and the agent sessions that ref's worktree can resume. They refresh in place as the graph changes and close when their ref disappears. Actions root themselves at the branch's worktree when it's checked out somewhere else.

### Pull Requests and Remote Branches in the Side Bar

<!-- TODO: upload gl-19-0-pr-panel.png -->

A new _Pull Requests_ panel lists the repository's open pull requests, most-recently-updated first, each with a _Launchpad_-style status indicator on rows that need attention, a fork glyph on pull requests opened from a fork, and a hover adding CI, review, and change-size signals. Rows lead with a state-aware action &mdash; _Switch to Branch..._, _Open in Worktree..._, or _Open Worktree in New Window..._ &mdash; then _Open Pull Request on Remote_ and _Focus_, which scopes the graph to the pull request's branch and offers to fetch it first when it isn't in your repository yet. When the remote has no integration connected, the panel offers to connect one instead of showing an empty list.

The _Branches_ panel gains a _Show Remote Branches_ toggle (sharing `gitlens.views.branches.showRemoteBranches` with the _Branches_ view), with remote branches keeping their prefix, grouping under their remote in tree layout, and showing their remote's provider icon. Every branch, worktree, and remote-branch row also picks up an inline _Focus_ action, plus pinned and current-branch indicators.

### Find and Jump Faster

- **Type-ahead reference finder** &mdash; press <kbd>/</kbd> anywhere in the graph and start typing to jump to a branch or tag by name. The graph moves as you type, the match's pill fills and its row flashes, and <kbd>↑</kbd>/<kbd>↓</kbd> step through the rest. Abbreviated path segments work too &mdash; `d/f/foo` finds `debt/feature/foo`. References whose commits aren't loaded yet are offered dimmed, and <kbd>Enter</kbd> fetches and jumps to them.
- **See what a pull would do** `PRO` &mdash; hovering the _Pull_ button offers _Jump to Upstream_ to scroll to the incoming commits (<kbd>Alt</kbd>+click does the same without pulling), and warns in one line when pulling would hurt: either that uncommitted changes to the same files will block it, or how many files it would conflict in, simulated the way your `pull.rebase` setting says the pull will actually integrate. Conflict detection requires a GitLens Pro trial or subscription and Git 2.33 or later; the jump doesn't.
- **A minimap that shows up when it's useful** &mdash; the minimap is now hidden by default and appears while searching, so matches are visible as they stream in. When to show it lives in the new `gitlens.graph.minimap.defaultVisibility` setting (`onSearch`, `always`, or `hidden`).
- **Smoother reveals** &mdash; jumping to a reference, a search result, or a deep link now slides into the target row instead of cutting to it, and reliably lands on it even when the commit has to be paged in first.
- **Terminal links open in the Graph** &mdash; a new `gitlens.terminalLinks.showIn` setting (default: the _Commit Graph_) replaces the old boolean, and ranges like `main..feature` or `HEAD~3..HEAD` are now detected and opened as comparisons rather than linking only the trailing SHA.

### Automatic Rebase, Start to Finish

The AI **Resolve** mode introduced in 18.2 now drives an entire rebase. Choose _Automatic Rebase_ in the rebase quick menu, or _Continue Automatic Rebase_ on an already-paused rebase, and each conflicted step is resolved, staged, and continued automatically &mdash; pausing for review only when confidence falls below the new `gitlens.ai.autoRebase.confidenceThreshold` setting, or when something genuinely needs you.

The run narrates itself in the _Commit Graph_'s **Resolve** panel rather than a progress notification: which step it's on, a progress bar, every conflict already resolved with its strategy, confidence, and reasoning, and what it's doing right now. When automation stops, the same panel fills in with the resolutions it already computed instead of switching surfaces. On completion, a per-step summary shows every file's strategy and reasoning with before/after diffs, plus a validated _Undo_ that restores the branch's pre-rebase state and refuses if the branch has moved since.

The rebase quick menu's confirm step is now three options &mdash; _Rebase_, _Automatic Rebase_, and _Interactive Rebase_ &mdash; with an _Update Branches_ toggle applying `--update-refs` to whichever you pick.

### One Place to Compose

The standalone _Commit Composer_ webview is gone. Composition now lives in the _Commit Graph_'s details panel as the single compose surface, and every entry point &mdash; Command Palette, _Source Control_, the views, _Home_, MCP, and the rebase editor &mdash; routes there. Recompose actions on a branch, a commit selection, or a single commit resolve a covering range and seed the inline scope picker, including merge topologies and interior ranges. A new top drag handle scopes a compose to staged changes only, commits only, or an arbitrary range, and recompose anchors on the branch's worktree, offering to create one when the branch isn't checked out anywhere.

Review mode can now be scoped to unstaged changes only, and reviews of working changes include untracked files &mdash; staged into a scratch index rather than your repository's, so a review can never disturb what you have staged.

### Verify SSH-Signed Commits

A new _Edit SSH Allowed Signers_ editor builds the `allowed_signers` file Git needs to verify SSH-signed commits. Open it from the Command Palette, or from an _Add to allowed signers…_ action on an unverified SSH signature in a commit's signature details. It discovers candidate signers by extracting the public keys embedded in your repository's SSH-signed commits &mdash; entirely offline, and works with any host &mdash; and cross-checks them against each signer's registered SSH signing keys when a GitHub or GitLab integration is connected, marking keys as signed-here, provider-verified, or both. Review signers with their avatar, email, fingerprint, provenance, and signed-commit count, choose which to include, pick the target file, and optionally point `gpg.ssh.allowedSignersFile` at it globally or per repository &mdash; merging into an existing file without clobbering your manual entries.

### Keyboard Navigation and Accessibility

The graph is now a standard WAI-ARIA tree with programmatic focus transitions into row controls, and a reusable roving tabindex controller drives keyboard navigation across toolbars, side bar panels, and list cards. An active-descendant virtual cursor makes nested popover menus fully traversable, column resizing and reordering move to <kbd>Shift</kbd>+arrow keys to stay out of the way of row navigation, navigation skips disabled indicators, and nested or duplicated focus indicators are gone. Keyboard navigation is also substantially faster, and the graph pages in more history at the edges when you reach them with <kbd>End</kbd>, <kbd>Page Down</kbd>, or <kbd>Alt</kbd>-navigation.

### Your Account, in the Graph

Two new pills sit after the _Launchpad_ indicator in the graph header: an avatar pill whose hover summarizes your account, walkthrough progress, and connected integrations, and a walkthrough pill with a completion ring and a per-step checklist. Clicking either opens an account modal over the graph with your account details, both walkthroughs, integration and AI controls, and announcements &mdash; and the _Show Account_ command (renamed _Show Account in Graph_) now opens it. The _Launchpad_ pill itself becomes a compact severity dot, with the full breakdown still on hover.

The graph also picks up proper first-run states: a _Get Started with GitLens_ sign-in screen for signed-out users (or a _Verify your email_ prompt when the connected account is unverified), and an empty state offering _Open a Folder_, _Clone a Repository_, and _Start a New Project_ when no repository is open. A one-time prompt on first entry asks whether you'd rather run the graph vertically in the side bar or horizontally in the bottom panel, and moves it there for you.

### Performance and Reliability

- **Faster, smaller webview payloads** &mdash; the desktop host now compresses payloads with Node's `zlib` instead of a bundled JS implementation: ~9x faster on the path that blocks the message it's preparing (46ms to 5ms on a ~7MB payload), and ~31KB smaller in the bundle. The CSS and markup webviews ship inside tagged templates is now minified too.
- **Less Git work** &mdash; the side bar's _Worktrees_ panel no longer runs a `git status` per dirty worktree on every load; it settles clean vs. dirty with a fast check and loads the `+N ~M -K` breakdown only when you hover a row, does that work only while it's on screen, and runs at most four probes at once. Rapid keyboard navigation no longer asks Git about every row it passes, _Launchpad_ no longer fetches everything twice at startup, and the graph skips data loading entirely while signed out.
- **No more cached failures** &mdash; transient Git read, autolink, and issue-lookup failures are no longer cached and served as real answers ("no issues" for an autolink that simply failed, for instance).
- **Blame that stays current** &mdash; blame annotations, hovers, and CodeLens no longer go stale after you commit, pull, or switch branches outside of VS Code. A repo-path casing mismatch meant in-memory blame was never invalidated, affecting repositories at any path containing an uppercase character &mdash; nearly all of them on Windows and macOS.

---

### Added

- Introduces an all-new _Commit Graph_ rendering engine &mdash; a framework-agnostic layout engine (`@gitkraken/commit-graph`) paired with a new Lit renderer, replacing the vendored React renderer that has drawn the graph since it shipped
  - Adds virtualized rows, a rasterized SVG gutter, lane collapse, ref and WIP adornment providers, scroll markers, and keyboard navigation with tree semantics
  - Adds incremental and splice layout paths that reuse prior results, so paging, fetching, and history rewrites no longer shift the lanes you were reading &mdash; trunk lanes can't be evicted by branch tips or fetched merges, and a re-rooted trunk is detected rather than reshuffled
  - Adds a `gitlens.graph.style` setting to pick the row layout &mdash; `table` (single-line rows with columns) or `list` (stacked two-line rows), with `auto` switching to `list` when the panel is too narrow for the columns
  - Adds `gitlens.graph.lanes.density` (default `compact`), `gitlens.graph.lanes.folding.enabled`, `gitlens.graph.lanes.folding.default`, `gitlens.graph.lanes.grouped.min`, and `gitlens.graph.lanes.grouped.max` settings to control lane spacing, folding, and how many lanes render inline when the graph is grouped into another column
  - Adds a sticky timeline pill that groups scrolled rows into the same relative time buckets as the date column, expanding while scrolling to reveal the range and yielding when it overlaps interactive row actions, plus optional separator lines between date groups (`gitlens.graph.timelineSeparators`)
  - Adds a _Quick Refresh_ button to the graph column header that re-lays out the lanes on demand &mdash; entirely webview-side, with no refetch, leaving folds, scope, columns, and selection untouched
  - Adds inline column filter buttons that reveal on hover, responsive header breadcrumbs showing the grouping hierarchy, and double-click column auto-fit that measures real (non-compact) date formats
- Adds a _Changes_ column to the _Commit Graph_ &mdash; visualizes each commit's diffstat as **numbers**, **squares**, **bar**, or **bipolar** (a two-sided bar), switchable from an interactive header popover and persisted in the new `gitlens.graph.changesColumn.mode` setting. Because computing stats can be expensive on large repositories, the column is off by default (`gitlens.graph.changesColumn.enabled`) with a one-time opt-in, degrades through compact, mini, and single-glyph stages as it narrows, and uses positional, grayscale-friendly markers so deletions read without relying on color
- Adds HEAD, upstream, and merge target row markers to the _Commit Graph_ &mdash; the current branch's tip, its upstream, and its merge target now stand out with role-colored reference pills (HEAD in green and its upstream in a deeper green, since they're the same branch in two places, with the merge target as a jump segment on the pill), and each of those commits also gets a left-edge indicator that expands on hover; when the graph is focused (scoped) on a branch, that focus tip and its merge base share the same indicator rather than adding a second one; when a reference is pushed down the list the working changes (WIP) row surfaces the current branch's pill so its tip stays one click away; references on the same commit collapse into a single indicator; the merge target also gets its own full-width marker on the graph's scroll bar, themeable via `gitlens.graphScrollMarkerMergeTargetColor`
- Adds an indicator for not-yet-pulled commits to the _Commit Graph_ &mdash; commits that are on the current branch's upstream but not yet in your branch (i.e. what a pull would bring in) now show an always-visible download glyph, colored to match the _Pull_ button, mirroring the existing indicator on unpushed commits ahead of the upstream; it's an indicator only, with nothing to click
- Adds a branch and tag sheet to the _Commit Graph_ details panel &mdash; focusing a reference pill opens the WIP details panel re-scoped to that ref, with an issues/pull request strip, upstream and merge-target relationship cards (the counterpart's name is the edit affordance) carrying tracking status and the relevant sync, rebase, or merge actions rooted at the branch's worktree, an AI input scoped to unpushed or merge-target changes, and next-step rows tailored to the kind of ref. The sheet refreshes in place as the graph changes and closes if its ref disappears
  - Adds _Focus_ and _Hide_ toggles to the sheet &mdash; _Hide_ is stateful, so it can restore a ref it just hid, and both keep the sheet open
  - Adds an _Open on Remote_ chip, and _Explain_ / _Generate Changelog_ actions to tag and remote branch sheets &mdash; tags default their comparison base to the newest previous reachable tag, remote branches to their merge target
- Adds a _Pull Requests_ panel to the _Commit Graph_ side bar &mdash; lists the repository's open pull requests most-recently-updated first, each with a trailing status indicator mirroring _Launchpad_'s grouping (mergeable, blocked, follow-up, needs review) on rows that need attention, a leading fork glyph on pull requests opened from a fork, and a hover adding that same grouping plus CI, review, and change-size signals. Rows offer a state-aware first action &mdash; _Switch to Branch..._ (Alt: _Open in Worktree..._), or _Open Worktree in New Window..._ when one already exists &mdash; then _Open Pull Request on Remote_ (Alt: _Copy Pull Request URL_), and _Focus_, which scopes the graph to the pull request's branch and offers to fetch it first when that branch isn't in your repository yet, adding a remote for a fork when needed. Right-click adds _Switch to Branch..._, _Open in Worktree_, _Open Pull Request Changes_, _Compare Pull Request_, _Open Pull Request_, and _Copy_. When the repository's remote has no integration connected, the panel offers a _Connect to &lt;provider&gt;..._ action in place of the empty list, and connecting fills it in without a reload
- Adds a _Show Remote Branches_ toggle to the _Commit Graph_ side bar's _Branches_ panel &mdash; remote branches for the default remote can now be listed alongside local ones. Unlike the _Branches_ view, they keep their remote prefix (e.g. `origin/feature/x`), so they stay distinguishable in list layout and group under their remote in tree layout, and a remote branch is still listed when a local branch already tracks it; local branches always sort above remote ones. The toggle shares the `gitlens.views.branches.showRemoteBranches` setting with the _Branches_ view, so changing it in either place updates both. Remote branches also become pickable in the graph's _Focus Branch_ scope picker, and show their remote's provider icon (a cloud when unrecognized) rather than the local-branch glyph
- Adds a _Focus_ inline action to branch, worktree, and remote branch rows in the _Commit Graph_ side bar &mdash; toggles the scope off when the graph is already focused on that ref, and resolves a remote branch to its local tracking branch when one exists. Also adds pinned and current-branch indicators to side bar rows
- Adds a type-ahead reference finder to the _Commit Graph_ &mdash; press `/` anywhere in the graph (outside of a text box), or use the search button in the references column header, and start typing to jump to a branch or tag by name. The graph moves as you type, the matched reference's pill fills and its row flashes briefly, and &uarr;/&darr; step through the other matches. Matching is by substring and requires every whitespace-separated term, and abbreviated path segments work too &mdash; `d/f/foo` finds `debt/feature/foo`. References whose commits aren't loaded yet are offered as well: they're named but dimmed, and pressing Enter fetches the commit and jumps to it, so typing and stepping never start a fetch on their own
- Adds a preview of what a pull would do to the _Commit Graph_'s _Pull_ button &mdash; hovering it now offers a _Jump to Upstream_ action that scrolls the graph to the commits a pull would bring in; Alt+clicking the _Pull_ button does the same jump without pulling, while a plain click still pulls. The hover also warns, in one line, when pulling would hurt &mdash; either that uncommitted changes to files the incoming commits also touch will block the pull (which applies even to a fast-forward), or the number of files the pull would conflict in, simulated the way your `pull.rebase` (or `branch.<name>.rebase`) setting says the pull will actually integrate. Conflict detection requires a GitLens Pro trial or subscription and Git 2.33 or later; the jump does not
- Adds account access to the _Commit Graph_ header &mdash; two new pills after the _Launchpad_ indicator: an avatar pill whose hover shows an account summary, the active walkthrough's progress, and your connected integrations, and a walkthrough pill showing a completion ring with a count (e.g. 6/7) and the per-step checklist on hover &mdash; the walkthrough pill follows the GitLens walkthrough until it's complete, then the _Commit Graph_ walkthrough, and disappears once both are done. Clicking either pill opens a new account modal overlaying the graph with your account details, both walkthroughs, integration and AI controls, and announcements; the _Show Account_ command (renamed _Show Account in Graph_) now opens this modal instead of the _Home_ view ([#5522](https://github.com/gitkraken/vscode-gitlens/issues/5522))
  - Adds separate badges for subscription tier and status to the account panel, with the upgrade action inline on the account row
- Adds a sign-in screen to the _Commit Graph_ for signed-out users &mdash; when no account is connected, the graph is replaced by a _Get Started with GitLens_ screen offering _Create Free Account_ and _Sign In_ actions; when the connected account's email is unverified, it shows a _Verify your email_ prompt with _Resend Email_ and _Synchronize Status_ actions instead
- Adds an empty state to the _Commit Graph_ when no repository is open &mdash; offers _Open a Folder_, _Clone a Repository_, and _Start a New Project_ actions to get started; in web/virtual environments (e.g. vscode.dev) clone and new-project are replaced by an _Open Remote Repository_ action ([#5408](https://github.com/gitkraken/vscode-gitlens/issues/5408))
- Adds a one-time layout prompt on first entry to the _Commit Graph_ when it's your main GitLens view &mdash; asks whether you'd rather run it vertically in the side bar or horizontally in the bottom panel, illustrates both, moves the view to your choice, and never asks again ([#5412](https://github.com/gitkraken/vscode-gitlens/issues/5412), [#5505](https://github.com/gitkraken/vscode-gitlens/issues/5505))
- Adds an automatic rebase that resolves conflicts end-to-end with AI, then presents a reviewable summary with one-click undo &mdash; choose _Automatic Rebase_ in the rebase quick menu, or _Continue Automatic Rebase_ on an already-paused rebase, to run the rebase to completion: each conflicted step is resolved, staged, and continued automatically, pausing for review only when AI confidence falls below the new `gitlens.ai.autoRebase.confidenceThreshold` setting (or when something needs your attention); when automation stops, the _Commit Graph_'s **Resolve** panel opens pre-populated with the already-computed resolutions, and on completion a per-step summary shows every file's strategy, confidence, and reasoning with before/after diffs, plus a validated _Undo_ that restores the branch's pre-rebase state and refuses if the branch has moved since ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Adds an _Edit SSH Allowed Signers_ editor &mdash; opened from the Command Palette, or via an _Add to allowed signers…_ action shown on an unverified SSH signature in a commit's signature details (_Inspect_ view / commit hover) &mdash; that builds an SSH `allowed_signers` file so Git can verify SSH-signed commits &mdash; discovers candidate signers by extracting the full public key embedded in this repository's SSH-signed commits (offline, works with any host) and, when a GitHub or GitLab integration is connected, cross-checks them against each signer's registered SSH signing keys (marking keys as signed-here, provider-verified, or both); lets you review signers (avatar, email, fingerprint, provenance, signed-commit count), choose which to include, pick the target file path, and optionally point `gpg.ssh.allowedSignersFile` at it (globally or for the current repository) &mdash; merging into any existing file without clobbering manual entries ([#5469](https://github.com/gitkraken/vscode-gitlens/issues/5469))
- Adds resumable agent sessions per worktree &mdash; the _Commit Graph_'s working changes details and branch sheets now surface the Claude Code sessions a worktree can resume, live ones alongside the most recent past ones, with a _Resume Session_ action per row and a picker for the rest. Resuming prefers the Claude Code extension when the worktree is the open folder, otherwise a terminal anchored at the worktree
- Adds a _Resume Agent Session..._ option to working tree (WIP) rows in the _Commit Graph_ &mdash; right-click a WIP row to pick from that worktree's AI agent sessions, opening live sessions or resuming past ones, even when no session is currently active on the row
- Adds an _Apply / Pop Stash..._ option to working tree (WIP) rows in the _Commit Graph_ &mdash; right-click a WIP row to pick a stash and choose whether to apply or pop it; invoked from another worktree's WIP row, the stash is applied into that worktree
- Adds an _Apply Copied Changes (Patch)_ option to working tree (WIP) rows in the _Commit Graph_ &mdash; right-click a WIP row to apply changes previously copied with _Copy Changes (Patch)_, without leaving the graph; invoked from another worktree's WIP row, the changes are applied into that worktree, and existing working changes there are kept
- Adds maximize controls to the _Commit Graph_ details panel when docked to the bottom &mdash; a maximize/restore chip expands it to fill the graph area, with automatic maximization when entering _Compose_, _Review_, _Resolve_, or _Compare_ (and restore on exit), controlled by the new `gitlens.graph.details.maximizeOnMode` setting
- Adds a scope chip to the _Commit Graph_'s AI input &mdash; re-scopes the explain and changelog actions (e.g. unpushed commits vs. merge target), with the model chip's credit multiplier moved to sit directly after the model name
- Adds a right-click context menu to the _Commit Graph_'s scroll marker rail to toggle marker types (local/remote branches, stashes, tags, pull requests, WIP) &mdash; the rail stays rendered when empty so the menu remains reachable to re-enable them
- Adds a `gitlens.terminalLinks.showIn` setting to choose where a terminal link opens a commit, branch, tag, or ref &mdash; the _Commit Graph_ (default), the _Inspect_ view, or a quick pick &mdash; replacing the boolean `showDetailsView` setting (existing values are migrated). Commit and ref ranges (`abc1234..def5678`, `main..feature`, `HEAD~3..HEAD`) are now detected and opened as a comparison, where previously only a range's trailing SHA was linked
- Adds a `mode` parameter to the `link/command/graph` deep link that opens the _Commit Graph_ directly into compose or review ([#5226](https://github.com/gitkraken/vscode-gitlens/issues/5226))
- Adds support for unlocking and removing locked worktrees from the _Commit Graph_ and the _Worktrees_ view &mdash; deletion now detects a locked worktree, shows its lock reason when one is set, and escalates to a forced delete on confirmation
- Adds support for Gemini 3.6 Flash and Gemini 3.5 Flash-Lite AI models
- Adds a _Clear Commit Graph Cache_ option and a GitKraken CLI installation reset to _GitLens: Reset Stored Data..._, with a reload prompt after a full reset so in-memory state can't overwrite what was just cleared

### Changed

- Changes the _Commit Graph_ to a grouped lane placement by default &mdash; lane art folds into an anchor zone alongside your other columns rather than occupying a column of its own
- Changes the default _Commit Graph_ lane colors for dark and high-contrast themes to a new vibrant, perceptually-uniform palette &mdash; every lane shares the same perceived brightness so no lane visually dominates; light themes keep the previous colors, and any `gitlens.graphLane1Color`&ndash;`gitlens.graphLane10Color` customizations in `workbench.colorCustomizations` are still honored
- Changes the default colors marking HEAD and its upstream on the _Commit Graph_'s scroll bar, minimap, row markers, and reference pills &mdash; HEAD is now a clearer green and its upstream the deeper green of that same hue, so the two still read as one branch shown in two places while staying easy to tell apart at a glance; they separate on brightness rather than saturation, so upstream reads as deeper rather than faded and the pair stays distinguishable with color blindness, and both are tuned separately for light and dark themes; any `gitlens.graphScrollMarkerHeadColor`, `gitlens.graphScrollMarkerUpstreamColor`, `gitlens.graphMinimapMarkerHeadColor`, or `gitlens.graphMinimapMarkerUpstreamColor` customizations in `workbench.colorCustomizations` are still honored
- Changes the _Commit Graph_ minimap to be hidden by default and shown while searching &mdash; when to show it now lives in a new `gitlens.graph.minimap.defaultVisibility` setting: `"onSearch"` (the new default), `"always"`, or `"hidden"`. On `"onSearch"` the minimap appears as soon as a search starts, so matches are visible as they stream in, and hides again once the search is cleared. `gitlens.graph.minimap.enabled` goes back to a plain boolean controlling whether the minimap is available at all; an existing `false` is honored unchanged, and an existing `true` now means available and shown while searching, so set `gitlens.graph.minimap.defaultVisibility` to `"always"` to keep it always shown ([#5598](https://github.com/gitkraken/vscode-gitlens/issues/5598))
- Changes the _Commit Graph_ sidebar to be unpinned by default &mdash; the sidebar now floats over the graph and auto-collapses when it loses focus or when you press <kbd>Esc</kbd>; pin it (or set `gitlens.graph.sidebar.pinned` to `true`) to restore the previous shared-space layout ([#5447](https://github.com/gitkraken/vscode-gitlens/issues/5447))
- Changes the _Commit Graph_ working changes (WIP) bar into an always-visible overview bar &mdash; it previously hid itself entirely unless another worktree had working changes or unpushed commits, so on a single clean worktree there was nothing to orient from; it now always shows the current worktree with jumps to its HEAD tip, upstream (with ahead/behind), and merge target, alongside any other worktrees' working changes
- Changes the _Commit Graph_ header's _Launchpad_ pill into a compact indicator &mdash; the per-group counts are replaced by a severity dot on the rocket (red when anything is blocked, yellow when there's other actionable work, and nothing when you're all caught up), with the full breakdown still available on hover ([#5522](https://github.com/gitkraken/vscode-gitlens/issues/5522))
- Changes the _Commit Graph_ header's jump-to-reference button into a _Focus Branch_ control &mdash; clicking now focuses (scopes) the graph to the current branch, and Alt-clicking opens the scope menu's _Focus Branch_ picker with the branch filter focused; the _Focus Branch_ and _Current Branch_ scope options also get consistent icons ([#5556](https://github.com/gitkraken/vscode-gitlens/issues/5556))
- Changes the _Commit Graph_ header's _Create_ menu to merge into the _Start New_ menu, which now occupies the area the _Pro_ badge used to
- Moves commit composition into the _Commit Graph_'s details panel as the single compose surface &mdash; all entry points (Command Palette, _Source Control_, the views, _Home_, MCP, and the rebase editor) route to inline compose on the best open graph surface. Recompose actions on branches, commit selections, and single commits resolve a covering commit range and seed the inline scope picker, with support for merge topologies and interior ranges that end below the branch head; a new top drag handle scopes a compose to staged changes only, commits only, or an arbitrary range, and recompose anchors on the branch's worktree, offering to create one when the branch isn't checked out anywhere
- Changes the automatic rebase to narrate itself in the _Commit Graph_'s **Resolve** panel instead of a progress notification &mdash; the panel now opens as the rebase starts and shows which step it's on, a progress bar, every conflict it has already resolved (each file's strategy, confidence, and reasoning), and what it's doing right now. When automation stops for a conflict it can't finish, the same panel fills in with the already-computed resolutions rather than switching surfaces. The notification's _Cancel_ becomes a _Cancel Rebase_ action in the panel, which aborts the rebase and restores the branch's pre-rebase state ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Changes the rebase quick menu's confirm step to offer three options &mdash; _Rebase_, _Automatic Rebase_, and _Interactive Rebase_ &mdash; with an _Update Branches_ toggle applying `--update-refs` to whichever you choose, replacing the separate _& Update Branches_ variant of each option; _Rebase with AI Conflict Resolution_ is renamed _Automatic Rebase_ and now sits between the plain and interactive rebases, and is no longer offered when there's nothing to rebase onto. _Rebase with AI Conflict Resolution..._ and _Continue Rebase with AI_ in the Command Palette are likewise renamed _Automatic Rebase..._ and _Continue Automatic Rebase_ ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Changes each AI conflict resolution's reasoning to always be visible &mdash; in the _Commit Graph_'s **Resolve** panel and the automatic rebase summary, the _Why this resolution_ disclosure is replaced by the reasoning itself, clamped to three lines with a _see more_ expander when there's more to read ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Changes how paused merge, rebase, cherry-pick, and revert operations with conflicts are surfaced &mdash; a single surface now opens: the _Commit Graph_'s working changes (WIP) details with the conflict banner, or the _Interactive Rebase Editor_ for rebases when the _Commit Graph_ is unavailable
- Allows AI _Review_ mode to be scoped to unstaged changes only &mdash; the restriction stays in compose mode, where composing only unstaged changes alongside staged ones isn't supported ([#5577](https://github.com/gitkraken/vscode-gitlens/issues/5577))
- Changes reviews of working changes to include untracked files, staged with intent-to-add into a scratch index rather than your repository's index &mdash; so a review can neither revert a `git add` you made while it was running nor register as a working-tree change that marks its own result stale
- Overhauls keyboard navigation and accessibility in the _Commit Graph_ &mdash; restructures it as a standard WAI-ARIA tree with programmatic focus transitions into row controls, adds a roving tabindex controller across toolbars, side bar panels, and list cards, adds an active-descendant virtual cursor for traversing nested popover menus, moves column resizing and reordering to <kbd>Shift</kbd>+arrow keys, skips disabled indicators when navigating, and eliminates nested or duplicated focus indicators and focus stranded on recycled rows
- Changes what the _Commit Graph_'s Alt-hold branch lane highlight follows &mdash; it seeded only off the pointer, so it did nothing unless a row or reference was hovered, and while navigating by keyboard it kept highlighting whatever row the cursor happened to be parked on. It now follows whichever of the two moved last: hovering a row or reference still claims it, keyboard navigation (including Alt+&uarr;/&darr; between branching points and Alt+PgUp/PgDn between references) retargets it as you move, and with neither pointing anywhere it falls back to the lane of the current branch
- Changes the _Commit Graph_ to slide into a jumped-to row rather than cutting to it, and reworks jumps around a single reveal rule so a reference, search result, or deep link lands on its row even when the commit has to be paged in first
- Changes which remote `gitlens.views.branches.showRemoteBranches` uses when no default remote is set &mdash; repositories with multiple remotes and none designated as the default now fall back to `origin`, rather than the setting appearing to do nothing when turned on
- Changes when the _Commit Graph_ side bar's _Worktrees_ panel loads each worktree's working change counts &mdash; it previously ran a `git status` for every dirty worktree each time the panel loaded, so opening it cost time proportional to the slowest worktree, which on repositories where `git status` is slow could hold up other Git work; it now settles clean vs. dirty with a fast check and loads the `+N ~M -K` breakdown for a worktree only when you hover its row
- Changes the Pro feature gate to adapt to constrained spaces &mdash; in narrow placements (e.g. the side bar) the feature list collapses to a single column, and in short placements (e.g. the bottom panel) the header, messaging, and spacing compact so the pitch and _Upgrade_ action stay legible without hiding any content; full-size placements are unchanged. The gate can also offer to switch organizations, alongside switching repositories ([#5519](https://github.com/gitkraken/vscode-gitlens/issues/5519))
- Improves switching AI models &mdash; when a provider is already selected, the _Switch AI Provider/Model_ picker now opens directly to the model list, showing the selected provider in the title and leading with a _Change AI Provider_ entry so switching providers stays one pick away; also fixes the provider picker highlighting GitKraken instead of the current provider ([#5584](https://github.com/gitkraken/vscode-gitlens/issues/5584))
- Improves the desktop host's webview payload compression by routing it through Node's `zlib` &mdash; ~9x faster on a path that blocks the message it's preparing (46ms to 5ms on a ~7MB payload), with marginally smaller output and ~31KB less in the bundle; the CSS and markup webviews ship inside tagged templates is now minified as well
- Improves file tree search to match full repository-relative paths &mdash; queries containing folder separators (e.g. `src/git/`) now match, with path-aware highlighting mapped onto the visible label and description
- Standardizes commit action labels across the views and the _Commit Graph_ (e.g. _Checkout Commit..._, _Push to Here..._, _Reset Current Branch to Here..._) and tidies context menu grouping and order
- Unifies agent status indicators across GitLens &mdash; the views' agent decoration is now a badge overlaid on the robot icon, matching the _Commit Graph_'s treatment
- Adds a `username` handle to pull request and issue members wherever a provider supplies one (GitHub's login, Azure's `uniqueName`, Bitbucket's nickname), and uses it to categorize your own pull requests in _Launchpad_ rather than matching on display name

### Removed

- Removes the legacy (vendored React) _Commit Graph_ renderer along with its stylesheets, React, `react-dom`, `@lit/react`, `dragula`, the vendored components package, and the JSX build plumbing &mdash; the Lit engine, the default since it reached parity, is now the only renderer
  - Removes the `gitlens.graph.highlightRowsOnRefHover` setting &mdash; hovering a branch or tag no longer highlights its associated rows; click a reference to pin it and highlight its lineage instead
- Removes the standalone _Commit Composer_ webview &mdash; composition now lives inline in the _Commit Graph_'s details panel, and every entry point routes there
- Removes code suggestions from _Launchpad_ &mdash; the `code-suggestions` actionable category, its count badges, confirm-step rows, and tooltip line are gone, along with the per-load network round trip that fetched their counts and the `gitlens.ai.generateCreateCodeSuggest.customInstructions` setting. Items previously forced into that category keep the category their provider assigns, so some move out of _Requires Follow-up_. Viewing and applying code suggestions is unaffected &mdash; the Code Suggestions node under each pull request, the Patch Details accept/decline flow, and the `code_suggestion` deep link all remain
- Removes the AI terms confirmation prompt &mdash; AI features no longer interrupt your first use to ask you to accept, and the now-purposeless _AI Confirmations..._ option is gone from _GitLens: Reset Stored Data..._; the large prompt warning (`gitlens.ai.largePromptWarningThreshold`) is unaffected
- Removes the _Pro_ feature badge from the _Commit Graph_ header &mdash; the _Start New_ menu now occupies that area ([#5447](https://github.com/gitkraken/vscode-gitlens/issues/5447))
- Removes the _Reset Current Branch to Previous Commit_ command from the _Commit Graph_ and the views
- Removes the experimental `gitlens.graph.experimental.homeHeader.enabled` setting, superseded by the graph's new account bar

### Fixed

- Fixes blame going stale for open files after you commit, pull, or switch branches outside of VS Code &mdash; blame annotations, hovers, and CodeLens kept showing an older commit and author for lines a newer commit had changed, while `git blame` in a terminal was correct. Blame for an open file is cached in memory, and a repo-path casing mismatch meant repository changes never invalidated it, so it stayed stale until the file was closed and reopened or the window was reloaded. This affected repositories at any path containing an uppercase character, which is nearly all of them on Windows and macOS. Changing `gitlens.advanced.blame.customArguments` now also refreshes open files, instead of leaving them on blame computed with the old arguments ([#5523](https://github.com/gitkraken/vscode-gitlens/issues/5523))
- Fixes GitLens silently pinning your AI provider to Copilot without you ever choosing it &mdash; with no model configured, simply rendering an AI chip (e.g. in _Home_ or the _Commit Graph_) would resolve a provider and write it into your settings, so signing in later never re-evaluated. GitKraken AI is now the only provider selected automatically, and nothing is written to `gitlens.ai.model` unless you pick a model yourself. Since every AI feature already requires a signed-in account, selecting a provider now prompts for sign-in up front instead of letting you pick a model you can't use yet, and no model is offered while signed out. Affected settings written by the old behavior are cleared on upgrade, leaving any provider or model you chose yourself untouched ([#5612](https://github.com/gitkraken/vscode-gitlens/issues/5612))
- Fixes a scoped AI model selection leaking into the global default &mdash; resolving a model for _Review_ or _Compose_ with nothing configured would write that operation's preferred model into `gitlens.ai.model` for every other AI feature
- Fixes AI conflict resolution (**Resolve** mode in the _Commit Graph_ WIP details panel) failing with _No active merge, rebase, or cherry-pick conflicts to resolve_ when conflicts exist without an in-progress Git operation &mdash; conflicts from a `git stash pop`/`apply`, a `git pull` with autostash, or after `git merge --quit` can now be resolved, re-resolved with feedback, and applied ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Fixes AI conflict resolutions discarding changes that had already merged cleanly
- Fixes the paused-rebase banner (in the _Commit Graph_, _Inspect_, and _Home_) showing two identical play icons once AI has resolved the conflicts &mdash; the AI action now uses a sparkle-badged continue icon and is renamed _Continue Automatic Rebase_ to match the command of the same name, and the plain action now names its operation (e.g. _Continue Rebase_) ([#5450](https://github.com/gitkraken/vscode-gitlens/issues/5450))
- Fixes AI reviews reading files you excluded &mdash; exclusions are now applied while collecting the diff rather than afterwards on the assembled text, so an excluded file's contents are never read, `git add -N` no longer runs on an excluded untracked nested repository (which logged git's _adding embedded git repository_ warning on every review), and an unfiltered cached diff can no longer put excluded content into a prompt ([#5630](https://github.com/gitkraken/vscode-gitlens/issues/5630))
- Fixes a review's temporary staging of untracked files reverting a `git add` you made while it ran, and its index write marking the review's own result stale ([#5604](https://github.com/gitkraken/vscode-gitlens/issues/5604), [#5605](https://github.com/gitkraken/vscode-gitlens/issues/5605))
- Fixes compose previews dropping the earlier hunks of a renamed file, misaligned hunks in the compose preview diff, the scope picker showing an unstaged-only selection it couldn't compose, and a locked commit failing to reorder within an interior range
- Fixes the _Commit Graph_ sometimes not loading more commits when navigating with <kbd>End</kbd> or <kbd>Page Down</kbd> &mdash; navigation would stop at the last loaded commit with nothing further arriving, and only scrolling up and back down with the mouse would start it again; <kbd>Alt</kbd>-navigation to the next branching point or reference row now loads more history at that edge too, instead of doing nothing
- Fixes the _Commit Graph_ not loading more history after expanding the collapsed older-history fold while focused (scoped) on a branch &mdash; the fold showed the commits it already had and then stopped, even though more existed
- Fixes the _Commit Graph_ scrolling short of a commit it was asked to reveal &mdash; when the target had to be paged in first (jumping to a reference, a search result, or a deep link far back in history), the scroll was measured against the row list's pre-growth height and then corrected away, leaving the commit off-screen and appearing unselected. Also fixes a click made while such a reveal was still settling being able to be scrolled away from a moment later
- Fixes the _Commit Graph_ side bar's _Worktrees_ panel running per-worktree Git commands even while the side bar was collapsed, and running them without bound &mdash; on repositories with many worktrees this could saturate GitLens's Git queue on every repository event and hold up other Git work; the panel now does that work only while it's on screen and runs at most four probes at once. A worktree whose check fails also leaves its row's previous state alone instead of reporting it as having no changes
- Fixes rapid keyboard navigation in the _Commit Graph_ asking Git about every row it passes, and two forced layouts on its render and reveal paths
- Fixes _Launchpad_ fetching everything twice at startup, and a _Launchpad_ failure sticking in the _Commit Graph_ rather than clearing on the next successful load
- Fixes transient Git read, autolink, and issue-search failures being cached and served as real answers &mdash; a failed autolink lookup could be cached as "no issues", and a failed read pinned as the answer for as long as the cache held it
- Fixes focusing (scoping) the _Commit Graph_ on a branch dimming the graph instead of re-rooting it, doing nothing at all on a remote branch, and dropping the branch's own commits; also fixes stale scope anchors after a rebase and a working changes row vanishing under branch scope
- Fixes the _Commit Graph_ reference pill leading with the wrong branch, an untracked branch and its remote showing as two separate pills, a pinned upstream wrapping the combined pill onto two lines, tag pills ordering `v1.10.0` before `v1.9.0`, and every tracked remote being marked as HEAD's upstream
- Fixes search results being invisible on the _Commit Graph_'s minimap exactly where you were looking &mdash; result markers were drawn underneath the visible-range band, so matches within the rows currently in view were painted over and lost; on a freshly-loaded graph that band covers most of the minimap, so a search reporting thousands of matches could show only one or two markers
- Fixes working tree (WIP) search results (`type:wip`) all being marked at today on the _Commit Graph_'s minimap &mdash; each worktree's WIP row is now marked at the commit it's anchored to, rather than stacking every worktree onto today
- Fixes clearing a natural language search in the _Commit Graph_ silently re-populating the search box a moment later &mdash; a query still being converted when the search was cleared went on to run and restore itself
- Fixes the _Commit Graph_ not jumping to the first search match
- Fixes the _Commit Graph_'s hidden branches/tags list not identifying which refs are hidden &mdash; entries now show their remote (a whole-remote hide reads as _origin &middot; all branches_ instead of `*`) and are grouped by type; refs that no longer exist are no longer listed or counted
- Fixes remote branches never showing in the _Branches_ view or the graph side bar when no default remote was designated
- Fixes _Copy Changes (Patch)_ producing an empty or incomplete patch &mdash; copying a multi-file working tree (WIP) selection in the _Inspect_ and _Commit Graph_ views diffed against the index rather than HEAD, so a fully-staged selection reported "No changes found to copy" and a selection mixing staged and unstaged files silently dropped its staged changes; renamed files also copied as a bare add of the new path, leaving the old file behind when the patch was applied &mdash; this affected every per-file _Copy Changes (Patch)_ entry point, including commits, comparisons, the views, and the _Source Control_ view
- Fixes the _Commit Graph_ working changes (WIP) details continuing to show files after they were committed or discarded outside of VS Code (e.g. from a terminal)
- Fixes the _Commit Graph_ header's account/subscription state never updating after the view loads &mdash; sign-in/sign-out, organization switches, and plan changes (including the subscription simulator) now update the header live instead of requiring a reload; the same underlying fix also keeps account and organization state live in _Commit Details_ and organization AI/drafts settings live in the _Home_ view ([#5513](https://github.com/gitkraken/vscode-gitlens/issues/5513))
- Fixes the account panel not showing your account when you aren't in an organization &mdash; the avatar, name, and email were gated on having an active organization, so they were hidden entirely for solo accounts in both the _Home_ view and the _Commit Graph_'s account popover and modal
- Fixes the _Commit Graph_ view's progress indicator repeatedly flashing while nothing appears to change (most noticeable after the VS Code window regains focus) &mdash; last-fetched updates now coalesce into a single pending update instead of queuing one per `FETCH_HEAD` change
- Fixes the _Commit Graph_ sidebar list hovers repeatedly opening and closing in narrow viewports &mdash; when there's no room beside the list the hover now falls back below/above the row instead of flipping over the pointer, and moving the pointer into the hover keeps it open (like VS Code's own tree hovers) instead of dismissing it
- Fixes the unpinned _Commit Graph_ side bar restoring open, and hidden side bar content still fetching
- Fixes webviews wedging permanently after a webview-only reload, RPC subscriptions dying after the first reconnect, and a successful notification wiping unrelated queued notifications
- Fixes agent sessions pushing to every webview every few seconds, and agent-session notifications being delivered while the _Commit Graph_ was hidden
- Fixes resuming a Claude Code session that had changed directories, and transcript lookups for worktree and Windows paths
- Fixes self-managed cloud integrations (e.g. GitHub Enterprise, GitLab Self-Hosted) repeatedly issuing a token request that the server rejects on every session refresh, and legacy connections getting stuck reported as connected with no usable token &mdash; the per-connection token fetch no longer uses the host domain as the token id, and a connection whose token can no longer be fetched is now cleanly disconnected instead of left token-less ([#5497](https://github.com/gitkraken/vscode-gitlens/issues/5497))
- Fixes a healthy cloud integration (e.g. GitLab.com, Jira, Azure DevOps, Bitbucket Cloud) being fully disconnected when a backend error happens to land during an automatic session-expiry refresh &mdash; only a definitive "this connection no longer has a token" response now disconnects it; any other failure (a server error, a rate limit, or a rejected account token) preserves the connection so it self-heals on the next successful sync ([#5569](https://github.com/gitkraken/vscode-gitlens/issues/5569))
- Fixes issue searches failing when a GitHub account referenced by an issue has since been deleted
- Fixes the _Choose Commit..._ and _Search for Commit_ buttons in the _Inspect_ view's empty state doing nothing when clicked
- Fixes branches whose names contain parentheses being treated as a detached HEAD
- Fixes worktree actions targeting the wrong worktree, and lost branch reachability when switching worktrees in the _Commit Graph_ details
- Fixes the autolinks chip strip ignoring its enabled setting, and stale pin actions in the _Commit Graph_'s branch menus
- Fixes the AI model not being re-resolved when the Ollama server URL changes
- Fixes GitLens keeping persisted metadata for branches it deleted or renamed
- Fixes a clipped _Show_ button on the dormant _Changes_ column ([#5582](https://github.com/gitkraken/vscode-gitlens/issues/5582))
- Fixes several accessibility defects &mdash; `gl-button` reflecting an inverted `aria-disabled` when toggled, integration rollup chips that weren't focusable buttons, the layout prompt's info icon being unreachable by keyboard, missing focus outlines on side bar buttons, and codicon sizing and spacing in markdown tooltips

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
