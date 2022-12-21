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

At the top of the commit graph the repository name, the branch name that is currently checked out, and the last fetched time is shown. This section offers the ability to switch branches by selecting the branch name and the ability to fetch by selecting "Fetch".

<img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="img-bordered img-responsive center">

The Author, Commit Date / Time, and SHA columns can be rearranged by dragging + dropping the column headers and can be toggled on/off from the settings.

<img src="/wp-content/uploads/graph-columns.png" srcset="/wp-content/uploads/graph-columns@2x.png" class="img-bordered img-responsive center">

The commit graph settings can be adjusted by opening the Command Palette (`command/ctrl + shift + P`) and searching "GitLens: Open Settings".

<img src="/wp-content/uploads/commit-graph-settings.png" srcset="/wp-content/uploads/commit-graph-settings@2x.png" class="img-bordered img-responsive center">


<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens+ subscription can use the Commit Graph with private repos. </br></br>
    
    We’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

###Rich Commit Search

The Commit Graph will highlight all matching results across your entire repository when searching for a commit, message, author, a changed file or files, or even a specific code change. Use shortcut keys or the up/down arrows on the search bar  to navigate the search results; `F3` (also `Cmd+G` on macOS) goes to the next result from your selection while  `Shift+F3`  ( also `Shift+Cmd+G` on macOS) goes to the previous. 

<img src="/wp-content/uploads/Rich-Commit-Search.png" class="img-responsive center img-bordered">

Once you type search filtering criteria, use the arrow icons to move through each result. Additionally, you can quickly jump to the first or last result, by holding `Shift` while clicking on the up/down arrows respectively.

<img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="img-responsive center img-bordered">

The following options can be used to search:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me`

Additionally, the options on the right side of the search bar can be used to match all, match case, or use regular expression.

<img src="/wp-content/uploads/search-options.png" class="img-bordered img-responsive center">

###Full Context Menu Support

You can right-click a branch, commit, tag, author, or column headers (author, commit date / time, or SHA) to interact with them. 

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

### Pull Request Information

For GitHub and GitLab, the commit Graph will display a Pull Request icon for any branch that currently has a pull request. You will need to connect the [rich integration](/gitlens/settings/#remote-provider-integration-settings) in order to see this.

<img src="/wp-content/uploads/pull-request-icon.png" class="img-bordered img-responsive center">

### Hiding Remotes, Branches or Tags

The Commit Graph shows refs to your remotes, branches and tags. Hover over any of these refs to access the “Hide” option to help focus your Commit Graph. To show them again, hover over the "Hide" option at the top of the commit graph and select the desired refs. 

<img src="/wp-content/uploads/gl-hide-refs.gif" class="img-bordered img-responsive center">

Filter options can be accessed from the filter dropdown. This provides the ability to switch between _Show Current Branch Only_ - to show the current branch and its upstream remote remote - or _Show All Local Branches_ - this is selected by default. Additionally, remote branches, stashes and tags can be hidden or shown. 

<img src="/wp-content/uploads/filter-options.png" srcset="/wp-content/uploads/filter-options@2x.png" class="img-bordered img-responsive center">

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

Initially, in GitLens 12 we introduced new GitLens+ features that include Worktrees and Visual File History. Later we added the Commit Graph, see above all the additions we have made, with more to come!

###What is GitLens+?

GitLens+ is a set of exciting new visualization and code collaboration capabilities designed to help devs code faster and more efficiently solo or as a team. These additional features can be used indefinitely with public repositories for any user without or with a GitLens account. You’ll also be able to test drive GitLens+ features with private repos as part of your automatic 7-day free trial of GitLens+ Pro.

###Is GitLens still free?

Yes, GitLens is free. All core features will continue to be free without an account. In fact, we’re still adding many core features to GitLens. GitLens+ features are purely additive and provide a richer, more powerful experience.


###Is GitLens+ free?

GitLens+ requires a paid license when working with private repoistories. For local and public repositories it is free. To summarize: 

+ GitLens is **free**, no account required, and can be used on any local repository.
+ GitLens+ features on local & public repositories are also **free**.
+ GitLens+ features on private repositories require a Pro plan (or greater), view pricing [here](https://www.gitkraken.com/gitlens/pricing).