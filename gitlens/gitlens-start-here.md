---

title: Start Here
description: How to start working with GitLens
taxonomy:
    category: gitlens
    
---
---

<kbd>Last updated: February 2026</kbd>

Welcome to the GitLens Support Documentation site! 

GitLens is the #1 most downloaded [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) Git extension that supercharges your developer workflows. You can download GitLens from the VS Code marketplace: 

<a class="button button--basic" href="https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens" target="_blank">Install GitLens</a> 

GitLens is known for its blame, hover, and annotations, but there’s much more to the extension. Users are leveraging its rich features to increase their developer productivity, which you can learn more about in the popular workflows below. 

* [Interactive Code History](/gitlens/gitlens-home/#interactive-code-history)
* [Accelerate PR Reviews](/gitlens/gitlens-home/#accelerate-pr-reviews)
* [Streamline Collaboration](/gitlens/gitlens-home/#streamline-collaboration)

***

### Interactive Code History

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/uSc7aQV8uMs?si=7bGXpqRI0lv7k-A0' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Understanding code history can be difficult when looking at complex repositories with multiple branches and contributors. Developers can struggle to easily see who made changes, why, and when. With the use of The Commit Graph, GitLens Inspect, and Inline Blame and Hovers, GitLens offers the ability to easily navigate through your repository to provide insights about the history and interact with it to better manage your code. 

#### Commit Graph

Once you have a repository open in VS Code, the Commit Graph gives you an interactive, action oriented visual of your commit and branch history. This allows you to follow your repository over time to see what is happening with branches and see why it was done with commit messages. You can quickly jump to any point in history by searching for either branches or commits. To view the commit graph, use the command palette (command/ctrl + shift + P) > _GitLens: Show Commit Graph View_ or select the _Show Commit Graph_ icon.

<a href="vscode://eamodio.gitlens/link/command/graph">Open the Commit Graph in GitLens</a>.

#### GitLens Inspect

When you are ready to dive deeper into a specific area, you can use GitLens Inspect. To open GitLens Inspect, right-click a commit and select Inspect Details. This will give you contextual information about what files and lines were modified in this specific commit. You can jump through the history of the file or line to see how it has changed over time. Additionally, autolinks help you see things like Jira issues or Pull Requests related to the changes.

<a href="vscode://eamodio.gitlens/link/command/inspect">Open the Inspect View in GitLens</a>.

#### Inline Blame and Hovers

From inside a file, Inline Blame and Hovers provide the answers to who exactly changed a specific line in a file, when, and why. To see the Inline Blame, select a file and then a line in the file. You can hover over the blame to take action on it such as viewing the previous revision, opening the pull request it was included in, opening the commit in the Commit Graph, and much more.  

***

### Accelerate PR Reviews

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

### Streamline Collaboration 

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

When collaborating with others in a repository, it can be difficult to share code without bloating your repository with multiple commits and branches that may not be ready to contribute to the remote. Additionally, pull request reviews can be limiting for what you have access to review, comment on, and does not give you the ability to review files that have not been modified. With the use of Cloud Patches and Code Suggest, GitLens offers the ability to easily share code without needing to commit/push it to a remote and allows you to suggest code changes to any file in the repository.

#### Cloud Patches `PRO`

Cloud Patches are Git patches that can be shared with anyone in your GitKraken organization to quickly share code changes with others. It can be applied to their working directory to continue to collaborate on or commit to the repository. 

To create a cloud patch, make changes to any file in a repository and then save those changes. Then, use the command palette (command/ctrl + shift + P) > _GitLens: Share as Cloud Patch…_. 

When you select members to share it with, they will see this in the Cloud Patch sidebar to be able to apply to their working directory.

<a href="vscode://eamodio.gitlens/link/command/cloud-patches">Open the Cloud Patches View in GitLens</a>.
<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

#### Code Suggest `PRO`

Code Suggest allows you to make edits across the entire repository that can be submitted to anyone's open pull request. 

To create a Code Suggestion, have a branch checked out with an open pull request, make changes to any files and save those changes. Then, use the command palette (command/ctrl + shift + P) > _GitLens: Show inspect view_ > Suggest Changes for PR. 

The pull request creator can then review these changes, apply them to their working directory to continue updating them, and accept the changes to commit/push them to the pull request.

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

***

### Improve Workflows With Integrations

<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/0LaCdNTRhMw?si=elYPqhs10LRf4W1b' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

Enhance your productivity in GitLens by reducing context switching and automating your workflow with Integrations and Autolinks. By connecting to platforms like GitHub, GitLab, Azure DevOps, and Bitbucket, you can seamlessly sync repositories and track issues within Launchpad—your PR hub. Additionally, Autolinks enables automatic linking to external services, making it easy to reference issues from platforms like Jira and Trello directly in your workflow. 

#### Integrations

Connect GitLens to your providers—GitHub, GitLab, Azure DevOps, and Bitbucket—to keep repositories in sync and track issues effortlessly in Launchpad. These integrations reduce the need for context switching, allowing you to focus on coding without leaving GitLens. 

#### Autolinks

GitLens integrations come with automatic linking capabilities, allowing you to link to external services like Jira and Trello. This feature lets you easily reference issues and tickets within your workflow.

Create custom autolinks with pattern-matching rules for a more tailored experience. This enables you to link external references, such as Jira issues or Zendesk tickets, directly in your commit messages, helping you maintain clear and accessible documentation for each change.

***

## Other places to check out

Looking to submit a feature request or bug report? Check out the GitHub.com public repository.
[GitHub Repository](https://github.com/gitkraken/vscode-gitlens)

Join our public slack community and interact with other GitKraken GitLens users from around the world 🌐.
[GitKraken Slack](https://slack.gitkraken.com/)

Didn't find what you're looking for in all of our documentation and help articles? Paid users can reach out to our support team.
[Contact Support](https://help.gitkraken.com/gitlens/gl-contact-support)
