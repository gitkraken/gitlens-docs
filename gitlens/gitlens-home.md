---

title: Get Started with GitLens
description: Install GitLens in VS Code or a VS Code-based IDE, sign in, connect your Git host, and try the Commit Graph, inline blame, Launchpad, worktrees, AI Review, Commit Composer, and collaboration features for the first time.
taxonomy:
    category: gitlens
    
---
<kbd>Last updated: September 2026</kbd>

This guide takes you from installing GitLens to using its core features on your own repository. Each step shows where to find a feature and what to try first, then links to the page that covers it in full.

For an overview of what GitLens is and what each feature does, see the [GitLens Documentation Home](/gitlens/gitlens-docs-home/).

## Before You Begin

You need:

- Git installed on your machine
- Visual Studio Code, or a VS Code-based IDE such as Cursor, Windsurf, Trae, or Kiro
- A Git repository open in the editor

Features marked `PRO` in this guide require a GitLens Pro plan or a free 14-day Pro trial. The Commit Graph and Worktrees are free on public and local repositories, and inline blame, hovers, and Git CodeLens are free everywhere. [GitLens Community vs. GitLens Pro](/gitlens/gitlens-community-vs-gitlens-pro/) compares the plans.

***

## Step 1: Install GitLens

<a class="button button--basic" href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank">Install GitLens</a>

**To install GitLens in VS Code:**

1. Open the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X`).
2. Search for **GitLens**.
3. Select **GitLens** by GitKraken, then select **Install**.

You can also select **Install GitLens** above to open the extension's VS Code Marketplace listing.

**To install GitLens in Cursor, Windsurf, Trae, or Kiro:** open that IDE's Extensions view, search for **GitLens**, and install it.

After installation, the GitLens icon appears in the Activity Bar. The first time GitLens starts, the **Welcome** view appears above the Commit Graph with a short walkthrough of the Commit Graph, AI features, Git blame, PR reviews, and MCP. Its content adapts to your plan, so it is a good place to see what you have access to.

***

## Step 2: Sign In and Connect Your Git Host

You can use the Commit Graph, inline blame, and hovers without an account. Sign in when you want to start a Pro trial or connect integrations.

### Sign In to GitKraken

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
2. Run **GitLens: Sign In to GitKraken...**.
3. Sign in, or create an account with GitHub, GitLab, Bitbucket, Azure DevOps, Google, email, or SSO.

To try Pro features, [start your free 14-day trial](https://gitkraken.dev/register?source=help_center&product=gitlens&redirect_uri=vscode%3A%2F%2Feamodio.gitlens%2Flogin&flow=gitlens_web). The [GitKraken Account](/gitlens/gl-gk-account/) page covers account creation and management.

### Connect an Integration

Connecting your code host lets GitLens show pull requests beside your branches and commits. It is also required for Launchpad and Code Suggest.

1. Open the Command Palette and run **GitLens: Manage Integrations**.
2. Select **Connect** for your provider.
3. Follow the prompts to authorize GitLens, then return to your IDE.

You can also manage integrations from your [GitKraken integration settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

GitLens integrates with GitHub, GitLab, Bitbucket, Azure DevOps, Jira, and Linear. The Jira integration and self-hosted GitHub Enterprise Server and GitLab Self-Managed integrations require Pro. See [GitLens Integrations](/gitlens/gl-integrations/) for provider-specific steps.

***

## Step 3: Open the Commit Graph

The Commit Graph is where most work in GitLens starts. It shows your branches, commits, working changes, and worktrees in one view, and every row has actions you can run directly.

**To open the Commit Graph:**

- Click the GitLens icon in the Activity Bar. The Commit Graph is the first view in the GitLens sidebar, or
- Open the Command Palette and run **GitLens: Show Commit Graph**

[Open the Commit Graph in GitLens](vscode://eamodio.gitlens/link/command/graph)

<figure>
  <img src="/wp-content/uploads/gl-graph-details-panel-01-v2@2x.png" class="help-center-img img-bordered" alt="The Commit Graph with the embedded details panel on the right, showing commit message, author, and changed files for the selected commit">
  <figcaption style="text-align:center; color:#888">Select a commit to see its details beside the graph</figcaption>
</figure>

**Try this:**

1. Select a commit. The details panel opens with the commit message, author, and changed files.
2. Select the **Working Changes** row at the top of the graph to see your uncommitted changes.
3. Right-click a branch or commit to see the actions you can take, such as merge, rebase, and cherry-pick.
4. In the search bar, type `@me` to find your own commits, or use a filter such as `Message:` or `File:`. Press `F3` (`Cmd+G` on macOS) to move to the next result.

To use a larger view, open the **More Actions** (⋯) menu on the Commit Graph and choose **Prefer Commit Graph in Editor**.

See [GitLens Commit Graph](/gitlens/gl-commit-graph/) for layout options, every search filter, and the full list of actions.

***

## Step 4: Explore Code History in the Editor

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/uSc7aQV8uMs?si=7bGXpqRI0lv7k-A0' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Inline blame, hovers, and Git CodeLens are on by default and free for all repositories.

**Try this:**

1. Open any file in your repository and place the cursor on a line. The inline blame annotation at the end of the line shows who last changed it, when, and the commit message.
2. Hover over the annotation to see full commit details, the associated pull request, and actions such as opening the previous revision or showing the commit in the Commit Graph.
3. Look above functions and at the top of the file for **Git CodeLens**, which shows the most recent change and the number of authors. Select it to open more history actions.
4. To see everything about one commit, open the Command Palette and run **GitLens: Show Inspect View**. The **Commit Details** tab updates as you move through the file.

[Open the Inspect View in GitLens](vscode://eamodio.gitlens/link/command/inspect)

To turn these annotations off, run **GitLens: Toggle Line Blame Annotations** or **GitLens: Toggle Git CodeLens** (`Shift+Alt+B`).

See [Current Line Blame](/gitlens/gitlens-features/#current-line-blame), [Hovers](/gitlens/gitlens-features/#hovers), and [GitLens Inspect](/gitlens/side-bar/#gitlens-inspect) for customization options, and [GitLens Visual File History](/gitlens/gl-visual-file-history/) for a timeline of how a file changed.

***

## Step 5: Review Pull Requests

<figure>
<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/FJ_IdTcqBi0?si=PFT5wDTiGs87Eu0-' frameborder='0' allowfullscreen></iframe>
</div>
<figcaption style="text-align:center; color:#888">Video: Review pull requests without leaving your IDE</figcaption>
</figure>

### Open Launchpad `PRO`

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher and requires a connected integration. See <a href="/gitlens/gl-launchpad/#availability">Launchpad availability</a> for supported Git hosts.</p>
</div>

Launchpad lists the pull requests you are involved in, grouped by what needs to happen next.

1. Open the Command Palette and run **GitLens: Open Launchpad**, or select **Pull Request** in the status bar.
2. Find a pull request under **Needs your review**.
3. Select it to view its details, open it in a browser, or switch to its branch or a worktree.

[Open the Launchpad in GitLens](vscode://eamodio.gitlens/link/command/launchpad)

To start a guided review instead, run **GitLens: Start Review**. It walks you through selecting a pull request, choosing whether to check out its branch or create a worktree, and optionally opening an AI chat with a review prompt. See [Start Review](/gitlens/gitlens-features/#start-review-pro).

The [Launchpad](/gitlens/gl-launchpad/) page covers pinning, snoozing, and every status group.

### Open the Worktrees View

<div class='callout callout--warning'>
    <p>The Community plan supports only public and local repositories.</p>
</div>

Worktrees let you check out several branches at once, so you can review a pull request without stashing or committing the work in progress on your current branch. When you open a pull request in a worktree from Launchpad, GitLens creates the worktree for you. Each worktree then gets its own **Working Changes** row in the Commit Graph.

[Open the Worktrees View in GitLens](vscode://eamodio.gitlens/link/command/worktrees)

See [GitLens Worktrees](/gitlens/gl-worktrees/) to create and manage worktrees.

***

## Step 6: Review and Commit Your Changes with AI

Once you have working changes, you can review them and turn them into clean commits from the Commit Graph details panel. Both workflows use GitKraken AI.

### Run an AI Review `PRO`

1. Open the Commit Graph.
2. Select the **Working Changes** row or a commit.
3. Open the details panel, then switch to **Review** mode.

GitLens returns a review summary, suggested focus areas, and findings tagged by severity, so you can fix issues before you commit or open a pull request.

[Open the Commit Graph in Review mode](vscode://eamodio.gitlens/link/command/graph?mode=review)

See [Run AI Code Review in the Commit Graph](/gitlens/gl-agents/#run-ai-code-review-in-the-commit-graph) for details, and [AI Review](/gitlens/gl-gk-ai/#ai-review-pro) for custom review instructions and plan requirements.

### Compose Commits `PRO`

1. Open the Commit Graph and select the **Working Changes** row.
2. Open the details panel, then switch to **Compose** mode.
3. Review the proposed commit groupings and edit any generated commit message.
4. Commit the changes.

[Open the Commit Graph in Compose mode](vscode://eamodio.gitlens/link/command/graph?mode=compose)

See [Commit Composer](/gitlens/gitlens-features/#commit-composer-view-pro) for other ways to open it, and [GitKraken AI Features in GitLens](/gitlens/gl-gk-ai/) for AI commit messages, AI rebase, and other AI features.

### Track Coding Agent Sessions `PRO`

If you use a supported coding agent such as Claude Code, install its hooks so GitLens can show the agent's sessions in the Commit Graph. Select the integration prompt in the Commit Graph header, or run **GitLens: Install Agent Hooks** from the Command Palette. Sessions then appear with their status in the Commit Graph and in the **Agent Sessions** panel.

See [AI Agents in GitLens](/gitlens/gl-agents/) for setup and the [list of supported agents](/gitlens/gitlens-features/#supported-agents).

***

## Step 7: Share Work with Your Team

<figure>
<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen></iframe>
</div>
<figcaption style="text-align:center; color:#888">Video: Share code and suggest changes in GitLens</figcaption>
</figure>

You can share changes without pushing a branch, and suggest edits on a pull request, even on files the pull request did not change.

### Share a Cloud Patch `PRO`

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher.</p>
</div>

1. Make and save changes to any file.
2. Open the Command Palette and run **GitLens: Share as Cloud Patch...**. You can also choose **Share as Cloud Patch** from the **Share** submenu on working changes, commits, stashes, and comparisons in GitLens views.
3. Choose who can open it: **Anyone with the link**, **Anyone in my org**, or **Only collaborators**.

[Open the Cloud Patches View in GitLens](vscode://eamodio.gitlens/link/command/cloud-patches)

See [GitLens Cloud Patches](/gitlens/gl-cloud-patches/) to apply and manage patches.

### Suggest Changes on a Pull Request `PRO`

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher and is supported only for repositories on GitHub.com.</p>
</div>

1. Check out a branch with an open pull request.
2. Open the Command Palette, run **GitLens: Show Inspect View**, and open the **Overview** tab.
3. Select **Start Review for PR #**, then make and save your proposed changes.
4. Select **Suggest Changes for PR**, add a title, and select **Create Code Suggestion**.

The pull request owner can then review, apply, and commit your suggestions. See [GitLens Code Suggest](/gitlens/gl-code-suggest/).

***

## Step 8: Link Commits to Your Issues

<figure>
<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/0LaCdNTRhMw?si=elYPqhs10LRf4W1b' frameborder='0' allowfullscreen></iframe>
</div>
<figcaption style="text-align:center; color:#888">Video: Use integrations and autolinks to connect GitLens to tools like Jira</figcaption>
</figure>

With an integration connected in [Step 2](#step-2-sign-in-and-connect-your-git-host), GitLens turns issue and pull request references in commit messages into links automatically. For example, a connected Jira integration turns issue keys such as `ABC-123` into links.

For trackers without an integration, such as Zendesk or an internal tool, add a custom autolink with the `gitlens.autolinks` setting. Each autolink matches a prefix and builds a URL from the reference:

```json
"gitlens.autolinks": [
    { "prefix": "JIRA-", "url": "https://jira.company.com/issue?query=<num>" }
]
```

See [Autolinks](/gitlens/gitlens-features/#autolinks) for all options.

***

## Next Steps

You have now used the main parts of GitLens. To put them together into complete tasks, follow one of the end-to-end workflow guides listed on the [GitLens Documentation Home](/gitlens/gitlens-docs-home/#follow-a-complete-workflow), such as [Manage Parallel Development from the Commit Graph](/gitlens/gl-parallel-dev-workflow/).

If something doesn't work as expected, see [GitLens Troubleshooting](/gitlens/gitlens-troubleshooting/) or the other help resources on the [GitLens Documentation Home](/gitlens/gitlens-docs-home/#get-help).
