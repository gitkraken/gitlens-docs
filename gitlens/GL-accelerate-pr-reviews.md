---
title: Accelerate PR Reviews
description: Explore how GitLens helps streamline pull request reviews using Launchpad and Worktrees.
taxonomy:
  category: gitlens
---

<kbd>Last updated: July 2025</kbd>

<figure class='embed-container embed-container--16-9'>
  <iframe width='560' height='315' src='https://www.youtube.com/embed/FJ_IdTcqBi0?si=PFT5wDTiGs87Eu0-' frameborder='0' allowfullscreen title="Accelerate PR Reviews with GitLens"></iframe>
</figure>

&nbsp;

Reviewing pull requests (PRs) in the browser can interrupt your workflow. Switching tabs, checking email notifications, and managing local branches can be time-consuming—especially when the PRs aren’t even relevant to you.

GitLens helps streamline PR reviews directly inside Visual Studio Code. With **Launchpad** and **Worktrees**, you can:

- View all relevant PRs grouped by actionable categories.
- Avoid context switching with an integrated experience.
- Work across multiple branches using separate working directories.

## Launchpad <span style="color: #888;">`PRO`</span>

To use Launchpad:

1. Connect your [GitHub Integration](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
3. Run: `GitLens: Open Launchpad`.

Launchpad displays grouped pull requests:

- On your current branch
- Assigned to you for review
- Waiting for follow-up
- Blocked or in draft

To start reviewing:

- Select a PR.
- Choose **Open in Worktree** or **Switch to Branch or Worktree**.

[Open the Launchpad in GitLens](vscode://eamodio.gitlens/link/command/launchpad)

<figure class='callout callout--warning'>
  <p>This feature is available with a GitLens Pro subscription or higher.</p>
</figure>


## Worktrees

Worktrees let you check out multiple branches simultaneously in separate working directories. This means you don’t need to commit or stash in-progress changes before switching to another branch—perfect for reviewing pull requests without disrupting your workflow.

After opening a worktree, use the Pull Request sidebar to:

- Review all commits in the PR
- Explore changed files
- View diffs and inspect updates line by line

[Open the Worktree View in GitLens](vscode://eamodio.gitlens/link/command/worktrees)

<figure class='callout callout--warning'>
  <p>The Community plan supports only public and local repositories.</p>
</figure>
