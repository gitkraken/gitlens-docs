---
title: GitLens Integrations
description: Connect GitLens to remote providers and issue trackers, and open or copy remote URLs from VS Code.
product: GitLens
feature: Integrations
content_type: integration
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server, gitea, gerrit]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server, jira, jira-data-center, linear, trello]
hosted_variant: both
status: GA
last_verified: 2026-09
llms_include: true
tags: [integrations, remote-providers, github, gitlab, jira, self-managed, autolinks]
taxonomy:
    category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gl-start-here"
    nav_label: "Integrations"
    nav_order: 20
    nav_parent: "gl-start-here"
    page_type: "content"
    card_icon: "plug-connected"
    card_color: "purple"
    card_description: "Explore GitLens integrations with remote providers"
    home_group: "features"
    home_order: 80
---

<kbd>Last updated: November 2026</kbd>

Connect GitLens to your remote providers and issue trackers to see their pull requests, issues, and links inside Visual Studio Code. GitLens supports these platforms:

- GitHub (including GitHub Enterprise)
- GitLab
- Gitea
- Gerrit
- Bitbucket (Cloud and Server)
- Azure DevOps (Cloud and Server)
- Jira Cloud and Jira Data Center (issue tracking)
- Linear (issue tracking)
- Trello (issue tracking)
- Asana (issue tracking)

You can also define [custom remote providers or providers with custom domains](/gitlens/gitlens-settings/#remote-provider-integration-settings).

## Integration Capabilities

Basic integrations provide:

- **Auto-linking** for issues and pull requests

Enhanced integrations, such as GitHub and GitLab, add:

- **Launchpad support** to manage pull requests and workflows
- **Rich hovers** showing issue and pull request details
- **Pull request associations** with branches and commits
- **Avatars** for contributors and reviewers

Integrations also add commands that open or copy the remote provider's URLs for files, commits, branches, and comparisons.

---

## Remote Command Reference

Use these GitLens commands to open or copy links to files, commits, branches, comparisons, pull requests, and repositories on your remote platform.

### Files

- **Open File from Remote** (`gitlens.openFileFromRemote`) — Open a local file by specifying a remote file URL
- **Open Revision from Remote** (`gitlens.openRevisionFromRemote`) — Open a specific file revision from a remote URL, resolving the exact revision rather than the working copy
- **Open File on Remote** (`gitlens.openFileOnRemote`) — Open the current file or revision on the remote
- **Copy Remote File URL** (`gitlens.copyRemoteFileUrlToClipboard`) — Copy the URL of the current file or revision
- **Open File on Remote From...** (`gitlens.openFileOnRemoteFrom`) — Open a file or revision from a specific branch or tag
- **Copy Remote File URL From...** (`gitlens.copyRemoteFileUrlFrom`) — Copy the file or revision URL from a specific branch or tag

### Commits

- **Open Commit on Remote** (`gitlens.openCommitOnRemote`) — Open a commit on the remote
- **Copy Remote Commit URL** (`gitlens.copyRemoteCommitUrl`) — Copy the URL of a commit

### Branches

- **Open Branch on Remote** (`gitlens.openBranchOnRemote`) — Open the current branch on the remote
- **Copy Remote Branch URL** (`gitlens.copyRemoteBranchUrl`) — Copy the URL of the current branch
- **Open Branches on Remote** (`gitlens.openBranchesOnRemote`) — Open the list of branches on the remote
- **Copy Remote Branches URL** (`gitlens.copyRemoteBranchesUrl`) — Copy the URL for all branches

### Comparisons

- **Open Comparison on Remote** (`gitlens.openComparisonOnRemote`) — Open a diff comparison on the remote
- **Copy Remote Comparison URL** (`gitlens.copyRemoteComparisonUrl`) — Copy the URL for the comparison

### Pull Requests

- **Open Pull Request on Remote** (`gitlens.openPullRequestOnRemote`) — Open the associated pull request
- **Copy Pull Request URL** (`gitlens.copyRemotePullRequestUrl`) — Copy the pull request URL

### Repositories

- **Open Repository on Remote** (`gitlens.openRepoOnRemote`) — Open the entire repository in your browser
- **Copy Remote Repository URL** (`gitlens.copyRemoteRepositoryUrl`) — Copy the repository URL for sharing or navigation


***

## Connect GitHub or GitLab Integration

You connect GitHub or GitLab to GitLens through your GitKraken account, on the [GitLens integrations dashboard](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

### Steps to Connect

1. Open your integrations in one of these ways:
   - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and run `GitLens: Manage Integrations`.
   - Open the Commit Graph and select the **Account** button (your avatar and plan badge) in its header. In the popover, select the **Integrations** row, or **Set up integrations** if nothing is connected yet, to open **Cloud Integrations** in GitLens Settings.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" srcset="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" alt="The Commit Graph header's account button with its menu open and the Integrations row ringed, a row of provider icons that opens GitLens Settings > Integrations." class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Open your integrations from the Commit Graph account popover</figcaption>
</figure>

2. If you are not signed in, sign in to your GitKraken account.
3. Select **Connect with GitHub** or **Connect with GitLab** and complete the sign-in.
4. Select **Complete Setup** to return to Visual Studio Code and activate the integration.

You can connect several integrations, including more than one account for the same provider. For example, you can connect a personal and a work GitHub account at the same time. In the integration settings, you can set a primary account, manage connections, and limit searches to a specific account.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" alt="The GitKraken integrations page with Connect buttons for GitLab, Azure DevOps, Bitbucket, Jira Cloud and Trello and a Complete Setup button" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Select the service you want to integrate and finish setup</figcaption>
</figure>

> **Warning:** On the Community plan, integrations offer basic functionality only.

***

## GitHub PR Stacks `PRO`

GitLens supports stacked pull request workflows on GitHub.com. For a pull request in a stack, GitLens shows the stack size, the pull request's position in the stack, and the base ref. When you merge, you choose whether to merge a single layer or the entire stack.

The stack details appear in the Commit Graph pull request sheet when you view a pull request that belongs to a stack.

To bring a whole stack up to date with its base branch, select **Rebase Stack...** in the pull request sheet or in Launchpad. GitLens rebases each branch onto the one below it, from the bottom of the stack up, and then offers to force push the rebased branches. **Auto-Rebase Stack...** does the same and resolves conflicts with AI. For details, see [Pull Request Information](/gitlens/gl-commit-graph/#pull-request-information) in the Commit Graph documentation.

***

## GitHub Merge Queue

If a repository on GitHub.com requires pull requests to merge through a merge queue, GitLens shows where each pull request stands in the queue and lets you add or remove it. GitLens supports merge queues on GitHub.com only, not on GitHub Enterprise. Connect the GitHub integration to see them.

- **Queue status:** Hovers, autolinks, and the GitLens views show a queued pull request's status, such as *#2 in the merge queue, checks running*, *Merging*, or *Failing in the merge queue*, with an estimated merge time when GitHub provides one.
- **Launchpad:** Queued pull requests appear in the **In Merge Queue** group, and pull requests failing in the queue appear under **Blocked** as **Failing in Merge Queue**. When the base branch requires a merge queue, **Add to Merge Queue...** replaces **Merge...**, and **Remove from Merge Queue...** takes a pull request out of the queue. For details, see [Launchpad](/gitlens/gl-launchpad/#review-pull-requests).
- **Commit Graph:** The pull request sheet shows **In merge queue** with **View Merge Queue** and **Remove from Merge Queue...**, or **Add to Merge Queue...** for a pull request that is ready to queue. While a pull request is in the queue, GitLens stops suggesting changes to its branch, such as pushing or rebasing, until it merges or leaves the queue. For details, see [Pull Request Information](/gitlens/gl-commit-graph/#pull-request-information).

A pull request that you remove from the merge queue loses its place. If you add it back, it goes to the end of the queue.

***

## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro connects to GitHub Enterprise Server and GitLab Self-Managed.

After you connect, autolinks for these services gain richer hover cards, and GitLens shows:

- User avatars
- Links to related pull requests and issues
- Pull request and issue details directly in the Sidebar views

<figure>
  <img src="/wp-content/uploads/gl-gitlab-github-integration-01-v4@2x.png" alt="The Commit Graph with the pull-request hover card open over the #7 badge of the fixture/code-suggest-demo branch pill: the pull request's title &quot;fix: add types and config to rate limiter&quot;, its number, who opened it and when it was last updated — metadata supplied by the connected GitHub integration" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Enhanced hover cards with issue and PR metadata</figcaption>
</figure>

### Connect GitHub Enterprise Server or GitLab Self-Managed

To connect a self-hosted GitHub or GitLab instance:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **Preferences: Open User Settings (JSON)**.
2. In `settings.json`, add a `gitlens.remotes` entry with your domain and provider type:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or for GitLab:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

3. Open the self-hosted repository in Visual Studio Code.
4. Open the [Remotes View](/gitlens/side-bar/#remotes-view).
5. Select <i class="fa-solid fa-plug"></i> **Connect to Remote**.

<figure>
  <img src="/wp-content/uploads/gl-connect-to-remote-ghe-01-v3@2x.png" alt="GitLens Remotes sidebar view listing repository remotes with the Connect to Remote action icon for linking a self-hosted provider" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Use the plug icon to connect a self-managed remote</figcaption>
</figure>

> If the **Connect to Remote** option does not appear, check that your JSON entry matches the example format.

6. When prompted, enter a personal access token with the required scopes and press **Enter** to complete setup.


***

## Jira Integration `PRO`

GitLens Pro connects to Jira Cloud through your GitKraken account. GitLens then links Jira issue keys (for example, `ABC-123`) in commit messages and views wherever it supports autolinks.

<figure>
  <img src="/wp-content/uploads/gl-jira-integration.png" alt="A GitLens commit hover in which the Jira issue key HC-132 is autolinked, with the linked issue Add Jira integration and when it was opened" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Jira issues auto-linked in GitLens hovers and views</figcaption>
</figure>

> **Warning:** This feature is only available for Pro subscription tiers or higher.

### Connect the Jira Integration

1. Open the GitLens Settings editor (run _GitLens: Open Settings_ from the Command Palette).
2. Select **Cloud Integrations** under **Integrations** in the navigation rail. Each provider has a card: a provider you have not connected shows **Connect**, and a connected one shows **Connected** and **Manage**.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations-01-v6@2x.png" alt="GitLens Settings open on Cloud Integrations, with GitHub, Azure DevOps, Bitbucket, Jira and Linear connected and Connect buttons for GitHub Enterprise, GitLab, GitLab Self-Hosted, Azure DevOps Server, Bitbucket Data Center, Jira Data Center, Trello and Asana" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Cloud Integrations in GitLens Settings, shown here with Jira already connected</figcaption>
</figure>

3. Select **Connect** on the **Jira** card and follow the prompts to connect.
4. Allow GitKraken access to your Atlassian account.

Linear, Trello, and Asana connect the same way from the **Cloud Integrations** category: select **Connect** on the provider's card and finish connecting on gitkraken.dev in your browser. All three require a Pro plan or higher. After you connect Trello or Asana, a branch associated with a Trello card or an Asana task shows that card or task in the Commit Graph. GitLens does not autolink Trello cards or Asana tasks, and it does not list them in Start Work or Launchpad.

You can also connect integrations from [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) on gitkraken.dev in a browser.

### Connect Jira Data Center

GitLens Pro can also connect a self-hosted Jira (Jira Data Center or Jira Server) through your GitKraken account. Select **Connect** on the **Jira Data Center** card in **Cloud Integrations** and follow the prompts. Each Jira host is its own connection. GitLens supports instances served under a context path, such as `https://jira.example.com/jira`.

A connected Jira Data Center instance shows the issues associated with a branch and autolinks its projects' issue keys (for example, `ABC-123`) in commit messages and branch names to the issue on your instance. Start Work and the Commit Graph's issue tracker picker do not list Jira Data Center issues yet.
