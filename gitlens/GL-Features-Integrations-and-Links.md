---
title: Integration and Link Features
description: Technical reference for GitLens remote provider, GitHub Enterprise Server, GitLab Self-Managed, and Jira integrations, plus autolinks, terminal links, and deep links.
product: GitLens
feature: Integrations
content_type: reference
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops, gerrit, gitea]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, azure-devops, jira, jira-data-center, trello]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [integrations, remote-providers, jira, autolinks, terminal-links, deep-links]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Integrations and Links"
    nav_order: 60
    nav_parent: "gitlens-features"
    page_type: "content"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

***

## Remote Provider Integrations

For workflows and examples, see [Integrations](/gitlens/gl-integrations/).

GitLens provides rich integrations with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/gitlens-settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/gitlens-settings/#remote-provider-integration-settings).

Basic integrations offer issue and pull request autolinking. Richer integrations, like GitHub or GitLab, include:

- Launchpad support
- Rich hover information for autolinks
- Pull request association with branches and commits
- Avatars for authors and commenters

These integrations also support various commands to open or copy URLs for files, commits, branches, and repositories:

- **Open File from Remote** (`gitlens.openFileFromRemote`) — Open a local file from a URL on a remote provider
- **Open Revision from Remote** (`gitlens.openRevisionFromRemote`) — Open the specific file revision referenced by a remote URL, rather than the working copy
- **Open File on Remote** (`gitlens.openFileOnRemote`) — Open a file or revision on the remote provider
- **Copy Remote File URL** (`gitlens.copyRemoteFileUrlToClipboard`) — Copy the URL of a file or revision
- **Open File on Remote From...** (`gitlens.openFileOnRemoteFrom`) — Open a file or revision from a specific branch or tag
- **Copy Remote File URL From...** (`gitlens.copyRemoteFileUrlFrom`) — Copy the URL from a specific branch or tag
- **Open Commit on Remote** (`gitlens.openCommitOnRemote`) — Open a commit
- **Copy Remote Commit URL** (`gitlens.copyRemoteCommitUrl`) — Copy the commit URL
- **Open Branch on Remote** (`gitlens.openBranchOnRemote`) — Open a branch
- **Copy Remote Branch URL** (`gitlens.copyRemoteBranchUrl`) — Copy the branch URL
- **Open Branches on Remote** (`gitlens.openBranchesOnRemote`) — Open the branches view
- **Copy Remote Branches URL** (`gitlens.copyRemoteBranchesUrl`) — Copy the branches view URL
- **Open Comparison on Remote** (`gitlens.openComparisonOnRemote`) — Open a comparison view
- **Copy Remote Comparison URL** (`gitlens.copyRemoteComparisonUrl`) — Copy the comparison view URL
- **Open Pull Request on Remote** (`gitlens.openPullRequestOnRemote`) — Open a pull request
- **Copy Pull Request URL** (`gitlens.copyRemotePullRequestUrl`) — Copy the pull request URL
- **Open Repository on Remote** (`gitlens.openRepoOnRemote`) — Open the repository
- **Copy Remote Repository URL** (`gitlens.copyRemoteRepositoryUrl`) — Copy the repository URL

### Connecting the GitHub and GitLab Integration

The GitHub and GitLab integrations connect through your GitKraken account at [gitkraken.dev](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

To connect an integration:

1. Open the Command Palette (`Cmd`/`Ctrl`+`Shift`+`P`).
2. Run `GitLens: Manage Integrations`.
3. Alternatively, select the account button (your avatar and plan) in the Commit Graph header, then select the **Integrations** row (or **Set up integrations** if none are connected) to open the integrations settings in GitLens Settings.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" srcset="/wp-content/uploads/gl-connect-remote-integration-01-v4@2x.png" alt="The Commit Graph header's account button with its menu open and the Integrations row ringed, a row of provider icons that opens GitLens Settings > Integrations." class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Open your integrations from the Commit Graph account menu</figcaption>
</figure>

If you're not already signed in, you'll be prompted to log in to your GitKraken account. Then, select **Connect with GitHub** or **Connect with GitLab**, and follow the sign-in steps. You can connect multiple integrations if needed.

Finish the process by selecting **Complete Setup** to return to VS Code and begin using the integrations.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" alt="The GitKraken integrations page with Connect buttons for GitLab, Azure DevOps, Bitbucket, Jira Cloud and Trello and a Complete Setup button" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Manage your connected integrations</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>Community users are limited to basic functionality only.</p>
</div>

***

## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

For workflows and examples, see [Integrations](/gitlens/gl-integrations/).

GitLens Pro offers a richer integration with GitHub Enterprise Server and GitLab Self-Managed.

Once authenticated, GitLens enhances autolinks in hovers with additional context. You’ll see your GitHub Enterprise Server or GitLab Self-Managed avatar, links to related pull requests, and a summary of pull request or issue details. Sidebar views for commits or branches also show this contextual information.

<figure>
  <img src="/wp-content/uploads/gl-gitlab-github-integration-01-v4@2x.png" alt="The Commit Graph with the pull-request hover card open over the #7 badge of the fixture/code-suggest-demo branch pill: the pull request's title &quot;fix: add types and config to rate limiter&quot;, its number, who opened it and when it was last updated — metadata supplied by the connected GitHub integration" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Enhanced hover integration with GitHub Enterprise and GitLab Self-Managed</figcaption>
</figure>

### Connecting GitHub Enterprise Server or GitLab Self-Managed

To connect either integration:

1. Open `settings.json`:
   - Use the Command Palette (`Cmd`/`Ctrl` + `Shift` + `P`) > **Preferences: Open User Settings (JSON)**

2. Add a `gitlens.remotes` entry specifying the domain and type:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

3. Open a repository from GitHub Enterprise Server or GitLab Self-Managed in VS Code.
4. Go to the [Remotes View](/gitlens/side-bar/#remotes-view).
5. Select <i class="fa-solid fa-plug"></i> **Connect to Remote**.
   - If this option is missing, verify the format in your `settings.json` matches the example above.

<figure>
  <img src="/wp-content/uploads/gl-connect-to-remote-ghe-01-v3@2x.png" alt="GitLens Remotes sidebar view listing repository remotes with the Connect to Remote action icon for linking a self-hosted provider" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Connect to a GitHub Enterprise or GitLab Self-Managed instance</figcaption>
</figure>

6. Provide a Personal Access Token (PAT) with the required scopes when prompted, and press **Enter** to complete the connection.

***

## Jira Integration `PRO`

For workflows and examples, see [Integrations](/gitlens/gl-integrations/).

The Jira Integration, connected through your GitKraken Account, enables Jira [Autolinks](#autolinks) wherever autolinks are supported in GitLens. Once connected, GitLens automatically converts Jira issue keys (e.g., `ABC-123`) in commit messages into clickable links.

<figure>
  <img src="/wp-content/uploads/gl-jira-integration.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Jira autolinks in commit messages</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>This feature is only available for Pro subscription tiers or higher.</p>
</div>

To connect the integration:

1. Open the GitLens Settings editor (run _GitLens: Open Settings_ from the Command Palette).
2. Select **Cloud Integrations** under **Integrations** in the navigation rail. Each provider has a card: a provider you have not connected shows **Connect**, and a connected one shows **Connected** and **Manage**.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations-01-v5@2x.png" alt="GitLens Settings open on Cloud Integrations, with GitHub, Azure DevOps, Bitbucket, Jira and Linear connected and Connect buttons for GitHub Enterprise, GitLab, GitLab Self-Hosted, Azure DevOps Server, Bitbucket Data Center, Jira Data Center and Trello" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Cloud Integrations in GitLens Settings, shown here with Jira already connected</figcaption>
</figure>

3. Select **Connect** on the **Jira** card, and authorize access to your Atlassian Account.
4. Alternatively, visit your [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

You can also connect **Trello** (a Pro integration) from the same **Cloud Integrations** list. Once Trello is connected, branches associated with Trello cards show a Trello badge on their Commit Graph pills. GitLens doesn't create autolinks for Trello cards.

To connect a self-hosted Jira (Jira Data Center or Jira Server), select **Connect** on the **Jira Data Center** card in the same list. Like the other self-hosted integrations, it is a Pro integration connected through your GitKraken Account, and each Jira host is its own connection; instances served under a context path, such as `https://jira.example.com/jira`, are supported. For now, a connected Jira Data Center instance is used only to show the issues associated with a branch: it doesn't create autolinks, and Start Work and the Commit Graph's issue tracker picker don't list it yet.

***

## Autolinks

Use autolinks to convert external references—such as Jira issues or Zendesk tickets—into clickable links directly from commit messages.

<figure>
  <img src="/wp-content/uploads/gl-autolinks-01-v4@2x.png" alt="Commit details in the GitLens Inspect view for a commit whose message ends in &quot;Closes #7&quot;: the #7 reference is a link, and the Autolinks section below the message shows the #7 chip with its hover popover naming the open pull request &quot;fix: add types and config to rate limiter&quot;" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of autolinks in commit messages</figcaption>
</figure>

***

## Terminal Links

<figure>
  <img src="/wp-content/uploads/gl-terminal-links-01-v3@2x.png" alt="The integrated terminal showing git log --oneline output, with the pointer on the first commit's SHA: GitLens underlines it as a link and shows the &quot;Show Commit (ctrl + click)&quot; hover" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Autolinks in the integrated terminal</figcaption>
</figure>

Terminal links optionally provide clickable references in the integrated terminal:

- [Branches, tags, and commit ranges](/gitlens/gitlens-settings/#terminal-links-settings): Quickly explore their commit history.
- [Individual commits](/gitlens/gitlens-settings/#terminal-links-settings): Review commit details and take further action.

***

## Deep Links

Deep Links are URLs that open specific GitLens resources, improving collaboration by sharing direct links to repositories, files, comparisons, and more. Resources that support Deep Linking include:

- **Search & Compare** — Link to comparisons in the [Search & Compare view](/gitlens/side-bar/#search-compare-view). Right-click a comparison, hover over _Share_, and select _Copy Link to Comparison_.
- **GitKraken Workspaces** — Link to a [GitKraken Workspace](/gitlens/side-bar/#workspaces-☁%ef%b8%8f). Right-click a Workspace, hover over _Share_, and select _Copy Link to Workspace_.
- **Commit Graph** — Link to remote repositories, commits, branches, and tags in the [Commit Graph](/gitlens/gl-features-commit-graph-and-history/#commit-graph). Right-click the resource, hover over _Share_, and select _Copy Link to <resource>_.
- **Files or Lines** — Link to specific files or lines of code. Right-click highlighted lines or a file, hover over _Share_, and select _Copy vscode.dev Link_.
- **Cloud Patches** — Link to a [Cloud Patch](/gitlens/gl-features-pull-requests-and-collaboration/#cloud-patches-preview). After generating a Cloud Patch, click _Copy Link_ from the success prompt.

<figure>
  <img src="/wp-content/uploads/gl-deep-link-example.gif" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Example of generating and using Deep Links</figcaption>
</figure>
