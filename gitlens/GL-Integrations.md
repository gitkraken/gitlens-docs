---
title: GitLens Integrations
description: Explore GitLens integrations with remote providers
taxonomy:
    category: gitlens
---

<kbd>Last updated: July 2025</kbd>

GitLens supports a wide range of remote providers to enhance your Git workflow inside Visual Studio Code. Supported platforms include:

- GitHub (including GitHub Enterprise)
- GitLab
- Gitea
- Gerrit
- Bitbucket (Cloud and Server)
- Azure DevOps

You can also define [custom remote providers or providers with custom domains](/gitlens/settings/#remote-provider-integration-settings).

## Integration Capabilities

Basic integrations include:

- **Auto-linking** for issues and pull requests

Enhanced integrations (e.g., GitHub, GitLab) offer:

- **Launchpad support** to manage pull requests and workflows
- **Rich hovers** showing issue and PR details
- **Pull request associations** with branches and commits
- **Avatars** for contributors and reviewers

These integrations also add contextual commands to open or copy URLs to files, commits, branches, and comparisons directly from your remote provider.

---

## Remote Command Reference

You can use the following GitLens commands to interact with files, commits, and repositories on your remote platform.

### Files

- **Open File from Remote** (`gitlens.openFileFromRemote`) — Open a local file by specifying a remote file URL
- **Open File on Remote** (`gitlens.openFileOnRemote`) — Open the current file or revision on the remote
- **Copy Remote File URL** (`gitlens.copyRemoteFileUrlToClipboard`) — Copy the URL of the current file or revision
- **Open File on Remote From...** (`gitlens.openFileOnRemoteFrom`) — Open a file/revision from a specific branch or tag
- **Copy Remote File URL From...** (`gitlens.copyRemoteFileUrlFrom`) — Copy the file/revision URL from a specific branch or tag

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


### Connect GitHub or GitLab Integration

To connect GitHub or GitLab to GitLens, you'll use your GitKraken account via the [GitLens integrations dashboard](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens).

#### Steps to Connect:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and run `GitLens: Manage Integrations`, **or**
2. Go to the **GitKraken Account** section in the GitLens Activity Bar and choose **Integrations**.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration.png" srcset="/wp-content/uploads/gl-connect-remote-integration@2x.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Navigate to Integrations in the GitKraken Account menu</figcaption>
</figure>

3. If you’re not already signed in, log into your GitKraken account.
4. Click **Connect with GitHub** or **Connect with GitLab** and complete the sign-in process.
5. Select **Complete Setup** to return to Visual Studio Code and activate the integration.

You can connect multiple integrations if needed.

<figure>
  <img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Select the service you want to integrate and finish setup</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>Community users are limited to basic functionality only.</p>
</div>

## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro supports advanced integration with GitHub Enterprise Server and GitLab Self-Managed.

Once authenticated, GitLens enhances autolinks for these services in hover cards. You'll see:

- User avatars
- Links to related pull requests and issues
- Pull request and issue details directly in the Sidebar views

<figure>
  <img src="/wp-content/uploads/gitlab-github-integration.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Enhanced hover cards with issue and PR metadata</figcaption>
</figure>

### Connect GitHub Enterprise Server or GitLab Self-Managed

To connect a self-hosted GitHub or GitLab instance:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select **Preferences: Open User Settings (JSON)**
2. In `settings.json`, add a `gitlens.remotes` entry with your domain and provider type:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or for GitLab:

```json
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

3. Open the self-hosted repository in Visual Studio Code
4. Open the [Remotes View](/gitlens/side-bar/#remotes-view)
5. Click <i class="fa-solid fa-plug"></i> **Connect to Remote**

<figure>
  <img src="/wp-content/uploads/gl-connect-to-remote-ghe.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Use the plug icon to connect a self-managed remote</figcaption>
</figure>

> If the **Connect to Remote** option doesn't appear, double-check that your JSON entry matches the example format.

6. When prompted, provide a Personal Access Token (PAT) with the required scopes and press **Enter** to complete setup


***

## Jira Integration `PRO`

GitLens Pro supports integration with Jira Cloud via your GitKraken Account. This allows GitLens to automatically link Jira issue keys (e.g., `ABC-123`) in commit messages and views wherever autolinks are supported.

<figure>
  <img src="/wp-content/uploads/gl-jira-integration.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Jira issues auto-linked in GitLens hovers and views</figcaption>
</figure>

<div class='callout callout--warning'>
  <p>This feature is only available for Pro subscription tiers or higher.</p>
</div>

### Connect the Jira Integration

1. Open the GitLens Sidebar and navigate to the **GitKraken Account** view.
2. Select **Cloud Integrations**.
3. Choose **Jira Cloud** and follow the prompts to connect.
4. Allow GitKraken access to your Atlassian Account.

You can also configure this via the [Integration Settings](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

<figure>
  <img src="/wp-content/uploads/gl-cloud-integrations.png" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">Jira integration via GitLens Cloud Integrations panel</figcaption>
</figure>
