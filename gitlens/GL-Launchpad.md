---

title: Launchpad
description: Gitlens Launchpad
taxonomy:
    category: gitlens

---

The Launchpad organizes pull requests by status allowing you to identify bottlenecks and take actions on them. This offers the ability to organize and quickly take actions on pull requests with priority.

<img src="/wp-content/uploads/gl-launchpad-quickpick.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Currently, this view is supported for GitHub.com and GitLab.com repositories. In order to see the Launchpad, you will need to connect the <a href="https://help.gitkraken.com/gitlens/gitlens-features/#connecting-the-github-and-gitlab-integration">GitHub Integration</a> .</p>
</div>

The Launchpad can be accessed from the command palette (`command/ctrl + shift + P`) by searching `GitLens: Open Launchpad` or select the Pull Request from the status bar in VS Code.

<img src="/wp-content/uploads/gl-access-launchpad.gif" class="help-center-img img-bordered">

Here you can see a list of all pull requests for your repositories that are ready to merge, blocked, require follow-up, need your review, are waiting for a review, are a draft, or are snoozed. You can select the pull request to see more information about it and take action on it such as open it in a browser, merge (if ready to merge) or switch to the branch/worktree. 

<img src="/wp-content/uploads/gl-view-pull-request.png" class="help-center-img img-bordered">

[Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) can be easily started or reviewed from pull requests in the launchpad actions as well. 

<img src="/wp-content/uploads/gl-launchpad-code-suggest.png" class="help-center-img img-bordered">

You can pin pull requests using the pin icon <i class="fa-solid fa-thumbtack"></i> to move them to the pinned group or snooze them by selecting the snooze icon <i class="fa-solid fa-snooze"></i> to move them into the snooze group. To unpin or unsnooze, select the pin or snooze icon again. 

<img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Note: The Launchpad is currently organized by prioritizing items on the list that require more action by elevating them to the top. This is subject to change in the future.</p>
</div>
<div class='callout callout--warning'>
    <p>This Feature is only available for Pro subscription tiers or higher</p>
</div>

***