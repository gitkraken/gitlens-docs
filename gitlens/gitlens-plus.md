---

title: GitLens+ Features
description: GitLens+ Features
taxonomy:
    category: gitlens

---

<img src="/wp-content/uploads/gl-graphic-image.png" class="img-bordered img-responsive center">


Sign up for GitLens+ to unlock powerful additional features like Worktrees and Visual File History – with more coming soon! It’s completely free to create your account, which enables you to utilize GitLens+ features with public repos indefinitely and private repos during your automatic 7-day trial of GitLens+ Pro. After your Pro trial, your account will enable you to upgrade to a <a href='https://www.gitkraken.com/gitlens/plus-features#paid-plans' target='_blank'>paid plan</a>  if you’d like, or you can simply continue using GitLens+ features with public repos for free. 

The introduction of GitLens+ has no impact on existing GitLens features. You’re not losing access to any of the features you know and love. In fact, more core features will continue to be added to GitLens. Signing up for GitLens+ simply gives you access to certain additional features that enable you to get even more out of Git in VS Code!


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

##Commit Graph - Preview

The commit graph helps visualize your repository commit history and give you information about branches, commits, and collaborators all in one view. This makes it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/commit-graph.png" class="img-bordered img-responsive center">

To open the Commit Graph, open the command palette using the keyboard shortcut `Cmd/ctrl + Shift + P` and type “Show Commit Graph”. This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths. 

<img src="/wp-content/uploads/show-commit-graph.gif" class="img-bordered img-responsive center">

<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public repositories, and requires no account. Additionally, users with a paid GitLens+ subscription can use the Commit Graph with private repos. </br></br>
    
    The Commit Graph is in Preview mode, and we’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

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

GitHub Enterprise Integration

GitLens+ offers a richer integration with GitHub Enterprise.

Once authenticated, GitLens will enrich GitHub autolinks in the hovers. You’ll see your GitHub Enterprise avatar, links to related pull requests, along with a footnote of the pull request or issue details. You’ll see similar details from the Sidebar views for any commit or branch associated with a pull  request or issue.

<img src="/wp-content/uploads/github-enterprise-integration.png" class="img-bordered img-responsive center">

See the [remote provider integration settings](/gitlens/settings/#remote-provider-integration-settings) to configure GitHub Enterprise.

***

##FAQ

###What are GitLens+ features?

Initially, in GitLens 12 we introduced new GitLens+ features that include Worktrees and Visual File History. But we have tons of new visualization and collaboration features in the pipeline, like the GitKraken commit graph, which is coming soon!

###What is GitLens+?

GitLens+ is a set of exciting new visualization and code collaboration capabilities designed to help devs code faster and more efficiently solo or as a team. Signing up for GitLens+ unlocks these additional features that can be used indefinitely with public repositories. You’ll also be able to test drive GitLens+ features with private repos as part of your automatic 7-day free trial of GitLens+ Pro.

###Is GitLens still free?

Yes, GitLens is free. All core features will continue to be free without an account. In fact, we’re still adding many core features to GitLens. GitLens+ features are purely additive and provide a richer, more powerful experience.
