---

title: Accelerate PR Reviews
description: Explore using Gitlens to accelerate your PR Reviews
taxonomy:
    category: gitlens

---


<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/FJ_IdTcqBi0?si=PFT5wDTiGs87Eu0-' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Reviewing pull requests can be cumbersome due to needing to context switch to a browser to search through pull requests that are irrelevant to you. Email notification updates can interrupt your workflows when checking out branches if you have work in progress. With the use of Launchpad and Worktrees, GitLens offers the ability to see all pull requests that are organized in groups of actions that you need to take and utilize worktrees to simultaneously have separate working directories, all without leaving Visual Studio Code. 

#### Launchpad `PRO`

To begin working with the Launchpad, connect the [GitHub Integration](gitkraken.dev/settings/integrations?source=help_center&product=gitlens). Once connected, you can access the Launchpad from the command palette (command/ctrl + shift + P) > _GitLens: Open Launchpad_.

Here, you can see pull requests that are open on your current branch, blocked, need your review, require follow-up, waiting for a review, and in draft.

To begin reviewing a pull request, simply select a pull request and then Open in Worktree or Switch to Branch or Worktree. 

<a href="vscode://eamodio.gitlens/link/command/launchpad">Open the Launchpad in GitLens</a>.
<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>
#### Worktrees

Worktrees allow you to have separate working directories, meaning you can check out and work in multiple branches at once. This allows you to not need to commit or stash changes you are currently working on in order to review a pull request.

Once you have opened a worktree, you can easily begin reviewing all changes made in the Pull Request sidebar. You can see what commits have been made, what files have been changed, open the file diffs, and more. 

<a href="vscode://eamodio.gitlens/link/command/worktrees">Open the Worktree View in GitLens</a>.

<div class='callout callout--warning'>
    <p>Community plan is restricted to public and local repositories only.</p>
</div>

***