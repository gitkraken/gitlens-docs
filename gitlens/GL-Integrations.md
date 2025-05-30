---

title: Gitlens Integrations
description: Explore Gitlens Integrations
taxonomy:
    category: gitlens

---

GitLens provides rich integrations with many remote providers, including GitHub, GitHub Enterprise, GitLab, Gitea, Gerrit, Bitbucket, Bitbucket Server, and Azure DevOps. You can also define [custom remote providers](/gitlens/settings/#remote-provider-integration-settings) or [remote providers with custom domains](/gitlens/settings/#remote-provider-integration-settings) as well.

Basic integrations provide issue and pull request auto-linking, while richer integrations (e.g. GitHub or GitLab) offer the ability to work with the Launchpad, can provide rich hover information provided for auto-linked issues and pull requests, associate pull requests with branches and commits, and provide avatars.

Additionally, these integrations provide commands to copy the url of or open, files, commits, branches, and the repository on the remote provider.

- Open _File from Remote_ command (`gitlens.openFileFromRemote`) — opens the local file from a url of a file on a remote provider
- Open _File on Remote_ command (`gitlens.openFileOnRemote`) — opens a file or revision on the remote provider
- Copy _Remote File Url_ command (`gitlens.copyRemoteFileUrlToClipboard`) — copies the url of a file or revision on the remote provider
- Open _File on Remote From..._ command (`gitlens.openFileOnRemoteFrom`) — opens a file or revision on a specific branch or tag on the remote provider
- Copy _Remote File Url From..._ command (`gitlens.copyRemoteFileUrlFrom`) — copies the url of a file or revision on a specific branch or tag the remote provider
- Open _Commit on Remote_ command (`gitlens.openCommitOnRemote`) — opens a commit on the remote provider
- Copy _Remote Commit Url_ command (`gitlens.copyRemoteCommitUrl`) — copies the url of a commit on the remote provider
- Open _Branch on Remote_ command (`gitlens.openBranchOnRemote`) — opens the branch on the remote provider
- Copy _Remote Branch Url_ command (`gitlens.copyRemoteBranchUrl`) — copies the url of a branch on the remote provider
- Open _Branches on Remote_ command (`gitlens.openBranchesOnRemote`) — opens the branches on the remote provider
- Copy _Remote Branches Url_ command (`gitlens.copyRemoteBranchesUrl`) — copies the url of the branches on the remote provider
- Open _Comparison on Remote_ command (`gitlens.openComparisonOnRemote`) — opens the comparison on the remote provider
- Copy _Remote Comparison Url_ command (`gitlens.copyRemoteComparisonUrl`) — copies the url of the comparison on the remote provider
- Open _Pull Request_ command (`gitlens.openPullRequestOnRemote`) — opens the pull request on the remote provider
- Copy _Pull Request Url_ command (`gitlens.copyRemotePullRequestUrl`) — copies the url of the pull request on the remote provider
- Open _Repository on Remote_ command (`gitlens.openRepoOnRemote`) — opens the repository on the remote provider
- Copy _Remote Repository Url_ command (`gitlens.copyRemoteRepositoryUrl`) — copies the url of the repository on the remote provider

### Connecting the GitHub and GitLab Integration

The GitHub and GitLab integration are connected via your GitKraken account from [gitkraken.dev](https://gitkraken.dev/settings/integrations?source=help_center&product=gitlens). To connect an integration, open the Command Palette (`command/ctrl+shift+P`) and type `GitLens: Manage Integrations`. You can also navigate to GitKraken Account in the GitLens Activity Bar and select `Integrations`. 

<img src="/wp-content/uploads/gl-connect-remote-integration.png" srcset="/wp-content/uploads/gl-connect-remote-integration@2x.png" class="help-center-img img-bordered">

You will be prompted to log into your GitKraken account if you are not already. Then, select `Connect with GitHub` or `Connect with GitLab` and sign into the desired service. You will have the option to connect multiple integrations if needed. Finish the process by selecting `Complete Setup` to hop back into VS Code and begin working with the integrations. 

<img src="/wp-content/uploads/gl-connect-remote-integration-manager.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>Community users are limited to basic functionality only.</p>
</div>

## GitHub Enterprise Server and GitLab Self-Managed Integration `PRO`

GitLens Pro offers a richer integration with GitHub Enterprise Server and GitLab Self-Managed.

Once authenticated, GitLens will enrich GitHub Enterprise Server or GitLab Self-Managed autolinks in the hovers. You’ll see your GitHub Enterprise Server or GitLab Self-Managed avatar, links to related pull requests, along with a footnote of the pull request or issue details. You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

<img src="/wp-content/uploads/gitlab-github-integration.png" class="help-center-img img-bordered">

### Connecting GitHub Enterprise Server or GitLab Self-Managed

To connect either the GitHub Enterprise Server or GitLab Self-Managed integration:

- Open the `settings.json` - this can be done from the command palette  (`command/ctrl + shift + P`) > _Preferences: Open User Settings (JSON)_

- Provide a _gitlens.remote_ with a _domain_ and a _type_ with the below format - for more information on the formatting see the [remote provider integration settings](/gitlens/settings/#remote-provider-integration-settings)

Format Example: 

```
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitHub" }]
```

Or

```
"gitlens.remotes": [{ "domain": "git.corporate-url.com", "type": "GitLab" }]
```

- Open a GitHub Enterprise Server or GitLab Self-Managed repository in VS Code

- Open the [Remotes View](/gitlens/side-bar/#remotes-view)

- Select <i class="fa-solid fa-plug"></i> _Connect to Remote_ - if you do not see this option, check that the format of the settings.json matches the example above

<img src="/wp-content/uploads/gl-connect-to-remote-ghe.png" class="help-center-img img-bordered">

- You will then be prompted to provide a PAT with the required scopes and can hit _Enter_ to complete the integration connection

***

## Jira Integration `PRO`

The Jira Integration connected through your GitKraken Account gives you access to Jira [Autolinks](/gitlens/gitlens-features#autolinks) anywhere autolinks are supported in GitLens. Simply connect the integration and GitLens will automatically convert Jira IDs in commit messages to links i.e. `ABC-123`.

<img src="/wp-content/uploads/gl-jira-integration.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>This Feature is only available for Pro subscription tiers or higher</p>
</div>

To connect the integration, open the GitLens Sidebar, select `Cloud Integrations` from the GitKraken Account view, select Jira Cloud, and proceed with the integration connection by allowing GitKraken access to your Atlassian Account. You can also open [Integration Settings](gitkraken.dev/settings/integrations?source=help_center&product=gitlens) in a browser.

<img src="/wp-content/uploads/gl-cloud-integrations.png" class="help-center-img img-bordered">
