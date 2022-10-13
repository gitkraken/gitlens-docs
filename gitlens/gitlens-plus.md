---

title: GitLens+ Features
description: GitLens+ Features
taxonomy:
    category: gitlens

---

<img src="/wp-content/uploads/gl-graphic-image.png" class="img-bordered img-responsive center">

GitLens+ features are available for all users on GitLens version 13+ working with public or local repositories. To work with these features on a private repository, you will need a  <a href='https://www.gitkraken.com/gitlens/plus-features#paid-plans' target='_blank'>paid plan</a>. 

The introduction of GitLens+ has no impact on existing GitLens features. You’re not losing access to any of the features you know and love. In fact, more core features will continue to be added to GitLens that enable you to get even more out of Git in VS Code!


***

##Commit Graph

The commit graph helps visualize your repository commit history and give you information about branches, commits, and collaborators all in one view. This makes it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/commit-graph.png" class="img-bordered img-responsive center">

To open the Commit Graph, open the command palette using the keyboard shortcut `Cmd/ctrl + Shift + P` and type “Show Commit Graph”. This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths. 

<img src="/wp-content/uploads/show-commit-graph.gif" class="img-bordered img-responsive center">

<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens+ subscription can use the Commit Graph with private repos. </br></br>
    
    We’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

###Searching Commits

You can search for commits using the search bar at the top of the commit graph or by selecting `command/ctrl + F`. This will search all commits within the repository, not just what is shown in the commit graph. The following options can be used to search:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`

<img src="/wp-content/uploads/gl-search.png" srcset="/wp-content/uploads/gl-search@2x.png" class="img-bordered img-responsive center">

Additionally, the options on the right side of the search bar can be used to match all, match case, or use regular expression.

<img src="/wp-content/uploads/search-options.png" class="img-bordered img-responsive center">

###Context Menus

You can right-click branches and commits to interact with them.

<img src="/wp-content/uploads/gl-context-menu.gif" class="img-bordered img-responsive center">

Context menu actions include but are not limited to:

- Switch to Branch
- Revert Commit
- Switch to Commit
- Create Branch
- Merge
- Rebase
- Create Worktree
- Create Pull Request

### Pull Request information

For GitHub and GitLab, the commit Graph will display a Pull Request icon for any branch that currently has a pull request. You will need to connect the [rich integration](/gitlens/settings/#remote-provider-integration-settings) in order to see this.

<img src="/wp-content/uploads/pull-request-icon.png" class="img-bordered img-responsive center">

### Hiding refs

The Commit Graph shows refs to your branches and tags. Hover over any of these refs to access the “Hide” option to help focus your Commit Graph. To show them again, hover over the "Hide" option at the top of the commit graph and select the desired refs.

<img src="/wp-content/uploads/gl-hide-refs.gif" class="img-bordered img-responsive center">

***

##Worktrees
Create <a href="https://www.gitkraken.com/learn/git/git-worktree" target="_blank">Git Worktrees</a> that allow multiple branches to be checked-out at once on the same repository. This makes it easier to develop on, or test multiple branches, by minimizing the context switching between branches.

<img src="/wp-content/uploads/worktrees-view.png" class="img-bordered img-responsive center">

***

##Visual File History

The Visual File History allows you to quickly see the evolution of a file, including when changes were made, how large they were, and who made them.
Authors who have contributed changes to the file are on the left y-axis to create a swim-lane of their commits over time (the x-axis). Commit are plotted as color-coded (per-author) bubbles, whose size represents the relative magnitude of the changes.

Additionally, each commit's additions and deletions are visualized as color-coded, stacked, vertical bars, whose height represents the number of affected lines (right y-axis). Added lines are shown in green, while deleted lines are red.

<img src="/wp-content/uploads/visual-file-history.png" class="img-bordered img-responsive center">

Gain addditional insights on hover.

<img src="/wp-content/uploads/visual-file-history-hover.png" class="img-bordered img-responsive center">

***

##Commit Details View

The Commit Details View gives you contextual change info about your code. This view updates as you move your cursor throughout the file with information about the commit that modified that line of code. Get quick information about the commit author, commit ID, links to Pull Requests, files modified in the commit, and more.

Click on a file to open the diff, and see what changed. You may also hover over the file name to access options like Open File, Open Changes with Working File, and Open Remote.

<img src="/wp-content/uploads/commit-details-view.png" class="img-bordered img-responsive center">

To open the Commit Details View, open the command palette using `Cmd/ctrl + Shift + P` and type: “Show Commit Details View” or navigate to the Commit Details View in the sidebar.

<img src="/wp-content/uploads/show-commit-details-view.gif" class="img-bordered img-responsive center">

***

##Single Sign On

Single Sign on offers a secure and easy way to sign into your account. To configure Single Sign On for your organization, refer to the Single Sign On guide <a href='https://help.gitkraken.com/gitkraken-client/single-sign-on/' target='_blank'>here</a>.

###Requirements and Configuration

Your GitKraken account may initiate an Oauth authentication flow with the following supported Identity Providers (IdPs):

- Azure Active Directory
- Okta
- Google Identity Platform
- Ping Identity

Please note that your IdP will first need to be configured before setting up the connection in your GitKraken account. For assistance, please contact your IdP administrator or consult the IdP documentation for help. 

Additional requirements:
- Configurable only by GitKraken Owner or Admin
- Subscribed to either the <a href='https://www.gitkraken.com/gitlens/pricing' target='_blank'>Teams or Enterprise plan</a>

###Signing in with Single Sign On

GitLens+ users will see the option to Sign in with SSO from the login screen.

<img src="/wp-content/uploads/single-sign-on.png" class="img-bordered img-responsive center">

After clicking “Sign in with SSO”, the SSO form will open and ask for an email address to use for SSO login. The app will then check the email and determine whether the email address belongs to a single IdP for SSO. When the email address is successfully identified, the user will be taken to that IdP to login.

***

##GitHub Enterprise and GitLab Self-Managed Integration

GitLens+ offers a richer integration with GitHub Enterprise and GitLab Self-Managed.

Once authenticated, GitLens will enrich GitHub Enterprise or GitLab Self-Managed autolinks in the hovers. You’ll see your GitHub Enterprise or GitLab Self-Managed avatar, links to related pull requests, along with a footnote of the pull request or issue details. You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

<img src="/wp-content/uploads/gitlab-github-integration.png" class="img-bordered img-responsive center">

See the [remote provider integration settings](/gitlens/settings/#remote-provider-integration-settings) to configure these integrations.

***

##FAQ

###What are GitLens+ features?

Initially, in GitLens 12 we introduced new GitLens+ features that include Worktrees and Visual File History. But we have tons of new visualization and collaboration features in the pipeline.

###What is GitLens+?

GitLens+ is a set of exciting new visualization and code collaboration capabilities designed to help devs code faster and more efficiently solo or as a team. These additional features can be used indefinitely with public repositories for any user without or with a GitLens account. You’ll also be able to test drive GitLens+ features with private repos as part of your automatic 7-day free trial of GitLens+ Pro.

###Is GitLens still free?

Yes, GitLens is free. All core features will continue to be free without an account. In fact, we’re still adding many core features to GitLens. GitLens+ features are purely additive and provide a richer, more powerful experience.
