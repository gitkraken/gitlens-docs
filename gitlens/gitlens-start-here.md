---

title: Start Here
description: How to start working with GitLens
taxonomy:
    category: gitlens
last_updated: 2026-11
    
---

<kbd>Last updated: November 2026</kbd>

---

GitLens is a Git extension for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens). You can download GitLens from the VS Code Marketplace:

<a class="button button--basic" href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank">Install GitLens</a> 

Besides blame, hovers, and annotations, GitLens supports these workflows:

* [Interactive Code History](#interactive-code-history)
* [Accelerate PR Reviews](#accelerate-pr-reviews)
* [Streamline Collaboration](#streamline-collaboration)

***

### Interactive Code History

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/uSc7aQV8uMs?si=7bGXpqRI0lv7k-A0' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

In a repository with many branches and contributors, it can be hard to see who made each change, when, and why. The Commit Graph, GitLens Inspect, and Inline Blame and Hovers let you navigate your repository's history and act on it.

#### Commit Graph

The Commit Graph is the main view in the GitLens sidebar and your starting point for working with GitLens. With a repository open in VS Code, it shows your commit and branch history, and you can act on any branch or commit from it. Follow what happens on each branch over time, and read the commit messages to see why each change was made. To jump to any point in history, search for a branch or commit.

The Commit Graph opens automatically in the GitLens sidebar. You can also open the Command Palette (**Ctrl/⌘ + Shift + P**) and run **GitLens: Show Commit Graph View**.

<a href="vscode://eamodio.gitlens/link/command/graph">Open the Commit Graph in GitLens</a>.

#### GitLens Inspect

GitLens Inspect shows the details of a single commit. To open it, right-click a commit and select **Inspect Details**. Inspect shows which files and lines the commit modified, and you can step through the history of a file or line to see how it changed over time. Autolinks show related items, such as Jira issues or pull requests.

<a href="vscode://eamodio.gitlens/link/command/inspect">Open the Inspect View in GitLens</a>.

#### Inline Blame and Hovers

Inline Blame and Hovers show who changed a line in a file, when, and why. To see the inline blame, open a file and select a line. Hover over the blame to act on the change, such as viewing the previous revision, opening the pull request it was included in, or opening the commit in the Commit Graph.

***

### Accelerate PR Reviews

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/FJ_IdTcqBi0?si=PFT5wDTiGs87Eu0-' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Launchpad and Worktrees let you review pull requests without leaving Visual Studio Code. Launchpad groups your pull requests by the action you need to take, so you do not search through unrelated pull requests in a browser. Worktrees give you separate working directories, so checking out a pull request's branch does not interrupt your work in progress.

#### Launchpad `PRO`

To use Launchpad, connect the [GitHub integration](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens). Then open the Command Palette (**Ctrl/⌘ + Shift + P**) and run **GitLens: Open Launchpad**.

Launchpad shows pull requests that are open on your current branch, blocked, need your review, require follow-up, are waiting for a review, or are in draft.

To review a pull request, select it, then select **Open in Worktree** or **Switch to Branch**.

<a href="vscode://eamodio.gitlens/link/command/launchpad">Open the Launchpad in GitLens</a>.
<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>
#### Worktrees

Worktrees give you separate working directories, so you can check out and work in several branches at once. You can review a pull request without committing or stashing the changes you are working on.

After you open a worktree, review the pull request's changes in the **Pull Request** view. It lists the commits and changed files, and you can open the diff of each file.

<a href="vscode://eamodio.gitlens/link/command/worktrees">Open the Worktree View in GitLens</a>.

<div class='callout callout--warning'>
    <p>The Community plan supports only public and local repositories.</p>
</div>

***

### Streamline Collaboration 

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

With Cloud Patches, you can share code without committing or pushing it to a remote, so your repository does not fill up with commits and branches that are not ready. With Code Suggest, you can apply edits that reviewers suggest to any file in the repository, including files the pull request did not modify.

#### Cloud Patches `PRO`

Cloud Patches are Git patches that you share with anyone in your GitKraken organization. Recipients apply a patch to their working directory to keep collaborating on the changes or commit them to the repository.

To create a Cloud Patch, make and save changes to any file in a repository. Then open the Command Palette (**Ctrl/⌘ + Shift + P**) and run **GitLens: Share as Cloud Patch...**.

The members you share it with see the patch in the **Cloud Patches** view, where they can apply it to their working directory.

<a href="vscode://eamodio.gitlens/link/command/cloud-patches">Open the Cloud Patches View in GitLens</a>.
<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

#### Code Suggest `PRO`

A Code Suggestion proposes edits to any file in a repository and is attached to an open pull request. Reviewers create Code Suggestions in GitKraken Desktop.

To review one in GitLens, expand the pull request in a GitLens view, expand **Code Suggestions**, and select the suggestion. In **Patch Details**, select **Apply Patch** to apply the changes to your working tree, then **Accept** or **Reject** the suggestion. See [GitLens Code Suggest](/gitlens/gl-code-suggest/).

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

***

### Improve Workflows With Integrations

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/0LaCdNTRhMw?si=elYPqhs10LRf4W1b' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Integrations and Autolinks connect GitLens to the services where you track your work, so you switch to them less often.

#### Integrations

Connect GitLens to GitHub, GitLab, Azure DevOps, or Bitbucket to track your pull requests in Launchpad without leaving GitLens.

#### Autolinks

GitLens integrations link to external services such as Jira and Trello, so you can reference issues and tickets in your workflow.

You can also create custom autolinks with pattern-matching rules. They link external references, such as Jira issues or Zendesk tickets, in your commit messages.

***

## Other places to check out

To submit a feature request or bug report, use the public GitHub repository.
[GitHub Repository](https://github.com/gitkraken/vscode-gitlens)

Join the public GitKraken Slack community to talk with other GitLens users.
[GitKraken Slack](https://slack.gitkraken.com/)

If you cannot find what you need in the documentation, paid users can contact the support team.
[Contact Support](https://help.gitkraken.com/gitlens/gl-contact-support)
