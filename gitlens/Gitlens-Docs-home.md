---

title: GitLens Documentation Home
description: What GitLens is, what it does, and where to go in the GitLens Help Center for the Commit Graph, coding agents, worktrees, AI review, Launchpad, blame, integrations, settings, and support.
taxonomy:
    category: gitlens
last_updated: 2026-09

---

<kbd>Last updated: September 2026</kbd>

Welcome to the GitLens Help Center. This page explains what GitLens is, what it does, and where to find the guide you need. It assumes you already use Git and Visual Studio Code or a VS Code-based IDE. It does not cover installation steps or individual settings, which the pages linked below describe in full.

<a class="button button--basic" href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank">Install GitLens from the VS Code Marketplace</a>

## What GitLens is

GitLens is an [open-source](https://github.com/gitkraken/vscode-gitlens) Git extension built and maintained by GitKraken. It is the most installed Git extension for Visual Studio Code, and it also runs in VS Code-based IDEs such as Cursor, Windsurf, Trae, and Kiro. GitLens brings your repository history, working changes, branches, worktrees, pull requests, and coding agent activity into one interactive workbench inside the editor, so you can understand what changed, shape it into clean commits, and move it to merge without leaving your IDE.

GitLens Community is free and open source. GitLens Pro unlocks the Commit Graph, Worktrees, Visual History, Launchpad, agent sessions, and GitKraken AI on private repositories. The [GitLens Community vs. GitLens Pro comparison](/gitlens/gitlens-community-vs-gitlens-pro/) lists exactly what each plan includes.

<figure>
  <img src="/wp-content/uploads/GL-Commit-Graph-Full.png" alt="The GitLens Commit Graph in the side bar, showing a branch with working changes, an Agents panel, a Files Changed list, and a Launchpad panel grouping pull requests by status." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">The Commit Graph is the GitLens development workbench.</figcaption>
</figure>

## What GitLens does

GitLens covers the full arc of a change, from understanding a line of code to landing a pull request. The sections below summarize each capability and link to the page that documents it.

### See everything in one place with the Commit Graph

The Commit Graph shows commits, branches, working changes, worktrees, upstream state, and supported coding agent activity in one connected view. Every row carries live state, such as ahead and behind counts and unpushed or unpulled changes, and you can act on a row directly to branch, merge, rebase, cherry-pick, stash, push, pull, or open a pull request. Commit search understands Git filters such as `message:`, `author:`, `file:`, and `change:`, and also accepts natural language.

The [GitLens Commit Graph](/gitlens/gl-commit-graph/) page describes the graph in full, and the [Commit Graph is Home](/gitlens/home-view/) page explains how the graph replaced the earlier Home view as the starting point in GitLens.

### Keep human and agent work visible

Coding agents open branches and worktrees faster than you can track by hand. GitLens shows supported agent sessions in the Commit Graph with their live status, so you can see which agents are working, idle, or waiting on you, and resume a session from the row it belongs to. Multi-worktree working-changes rows keep every parallel stream of work in view without switching branches.

<figure>
  <img src="/wp-content/uploads/GL-Agent-working.png" alt="The Agents panel under a branch's working changes, listing one session marked Working and one marked Idle, with counts of working, idle, and completed sessions." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Agent sessions stay attached to the branch they are working on.</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/GL-Worktrees-multi-wip.png" alt="The Commit Graph with separate Working Changes rows for the main worktree and three other worktrees, each grouped with its branch." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Each worktree gets its own working-changes row in the graph.</figcaption>
</figure>

Read [AI Agents in GitLens](/gitlens/gl-agents/) for agent sessions, Start Work with Agent, and the Agent Kanban view, and [GitLens Worktrees](/gitlens/gl-worktrees/) for creating and managing worktrees.

### Review, compose, and compare before you merge

From the Commit Graph, you can review a change as a whole with AI-powered Review, send findings back to your coding agent for another pass, sort a pile of working changes into separate commits with Commit Composer, and compare any two revisions. GitKraken AI also generates commit messages, stash messages, pull request descriptions, and changelogs, explains what a commit or branch did, and automates rebases and conflict resolution.

<figure>
  <img src="/wp-content/uploads/GL-Graph-Review.png" alt="The Reviewing Changes panel in the Commit Graph, listing unstaged changes and four changed files, with an instructions field and a Start Review button at the bottom." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Review your changes in the Commit Graph before you open a pull request.</figcaption>
</figure>

The [GitKraken AI Features in GitLens](/gitlens/gl-gk-ai/) page covers every AI capability, and the [Commit Composer](/gitlens/gitlens-features/#commit-composer-view-pro) section of the features page explains how to compose commits.

### Keep pull requests moving with Launchpad

Launchpad lists every pull request you are involved in and groups them by what needs to happen next: needs your review, blocked, requires follow-up, waiting for review, and draft. You can check a pull request out, open it in a worktree, or start its review with a coding agent without opening a browser tab. See the [Launchpad](/gitlens/gl-launchpad/) page for setup and daily use.

### Understand any line of code

The features GitLens is best known for remain free and on by default. Inline blame shows who last changed the current line and why, rich hovers add commit details, linked issues and pull requests, and quick actions, and Git CodeLens summarizes recent changes at the top of each file and code block. File History and Line History follow a file or a single line across renames, and Visual History draws a timeline of how a file or the whole repository evolved.

<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-inline-blame.png" alt="A TypeScript file in VS Code with inline blame at the end of a line and a hover card showing the author, commit date, commit message, and actions such as Explain and Connect to GitHub." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Inline blame and hovers answer who changed a line, when, and why.</figcaption>
</figure>

Start with [GitLens Interactive Code History](/gitlens/gl-interactive-code-history/) for blame, hovers, and Inspect, then [GitLens Visual File History](/gitlens/gl-visual-file-history/) for the timeline view.

### Connect your Git host and issue tracker

GitLens integrates with GitHub, GitLab, Bitbucket, Azure DevOps, and Jira to show pull requests and issues beside your history, correlate branches with their pull requests, and turn issue keys into links. Custom autolinks and custom remotes extend the same behavior to Gerrit, Gitea, and internal tooling. The [GitLens Integrations](/gitlens/gl-integrations/) page walks through connecting each provider.

## Where to go next

Pick the guide that matches what you want to do:

| Goal | Page |
|---|---|
| Install GitLens and take a first tour | [Get Started with GitLens](/gitlens/gitlens-home/) |
| Learn the side bar views and how to arrange them | [Using the GitLens Sidebar](/gitlens/side-bar/) |
| Browse every feature in one reference | [GitLens Features](/gitlens/gitlens-features/) |
| Look up a setting | [GitLens Settings Overview](/gitlens/gitlens-settings/) |
| Sign in or manage your plan | [GitKraken Account](/gitlens/gl-gk-account/) |
| Share work without pushing a branch | [GitLens Cloud Patches](/gitlens/gl-cloud-patches/) and [GitLens Code Suggest](/gitlens/gl-code-suggest/) |
| Group repositories across machines | [GitLens Workspaces](/gitlens/gl-workspaces/) |
| Review how GitLens handles your data | [GitLens Security Information](/gitlens/gl-security/) |
| See what changed in the latest release | [GitLens Release Notes](/gitlens/gitlens-release-notes-current/) |

## Follow a complete workflow

These guides string several features together into one end-to-end task:

- [Manage Parallel Development from the Commit Graph](/gitlens/gl-parallel-dev-workflow/)
- [Take Agent-Generated Work from Change to Merge](/gitlens/gl-agent-generated-work-end-to-end/)
- [Prepare Your Branch to Ship](/gitlens/gl-branch-prep-to-ship/)
- [Accelerate PR Reviews](/gitlens/gl-accelerate-pr-reviews/)
- [Understanding an Unfamiliar Codebase](/gitlens/gl-workflow-understanding-codebases/)
- [Cleaning Up and Preparing Work for Review](/gitlens/gl-workflow-cleanup-prepare-for-review/)
- [Orchestrating Complex Git Operations](/gitlens/gl-workflow-orchestrate-complex-git-operations/)

## Get help

If something is not working, start with these resources:

- [GitLens Troubleshooting](/gitlens/gitlens-troubleshooting/) for common problems and how to collect logs
- [GitLens FAQ](/gitlens/gitlens-faq/) for frequently asked questions
- [GitLens issues on GitHub](https://github.com/gitkraken/vscode-gitlens/issues) to report a bug or request a feature
- [GitHub Discussions for GitLens](https://github.com/gitkraken/vscode-gitlens/discussions) to talk with other users and the engineering team
- [GitKraken Support](https://help.gitkraken.com/gitlens/gl-contact-support) for direct help on paid plans
