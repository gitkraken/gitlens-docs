---

title: Home View
description: Overview of the GitLens Home View interface and features
taxonomy:
    category: gitlens
    
---

<a href="vscode://eamodio.gitlens/link/command/home">Open the Home View in GitLens</a>

The GitLens Home View is designed to streamline your workflows by answering three key questions throughout your day and providing paths to take action on work.
1. [What am I actively working on now?](/gitlens/home-view/#active-work-section)
2. [What should I work on next?](/gitlens/home-view/#launchpad-section)
3. [What have I worked on recently?](/gitlens/home-view/#recent-section)

<div class='embed-container embed-container--16-9'>
<iframe width="560" height="315" src="https://www.youtube.com/embed/jVzhyVBgNGg?si=T5hmEEe0jO09RNbl" title="Introducing the GitLens Home View" frameborder="0" allowfullscreen></iframe>
</div>


## Connecting Integrations

GitLens integrates with hosting and issue services like GitHub, GitLab, and Jira to help you monitor and take action on branches, issues, and pull requests. Integrations can be connected from the top of the Home View. Some features that leverage integrations are enhanced with <a href="https://help.gitkraken.com/gitlens/gitlens-community-vs-gitlens-pro/">GitLens Pro</a>.

<img src="/wp-content/uploads/home-view-integrations.png" class="img-responsive center img-bordered">

## Active Work Section

At the top of the GitLens Home View, you can see the state of your active repository and current branch. This section provides quick access to actions like syncing (push, pull, fetch), switching the active repo, viewing working directory changes, and more. You can also quickly open the <a href="https://help.gitkraken.com/gitlens/gitlens-home/#commit-graph">GitLens Commit Graph</a> from the icon in the header.

<img src="/wp-content/uploads/home-view-active-work.png" class="img-responsive center img-bordered">

When integrations are connected and issues or pull requests are associated with your branch, GitLens Pro will group them with branches. This allows you to check PR statuses, continue reviews, or revisit issue specifications as you work. If you haven't opened a PR yet or need to associate a branch with an existing issue, GitLens will guide you through the process.


## Launchpad Section

The Launchpad Section highlights the most important tasks to work on next. It leverages integrations to list critical pull requests that need your attention and allows you to start work on issues assigned to you by creating branches and worktrees.

<img src="/wp-content/uploads/home-view-next.png" class="img-responsive center img-bordered">

### Launchpad Summary

The Launchpad Summary shows how many pull requests are blocking your team and why. With GitLens Pro, you can click any status in this list to view the details of each pull request in <a href="https://help.gitkraken.com/gitlens/gitlens-features/#launchpad-pro">Launchpad</a>. From there, you can take actions like checking out a PR in a worktree to review it quickly without disrupting your current working directory.

### Starting Work on an issue

Quickly create branches and worktrees for issues assigned to you by clicking "Start Work on an Issue". This will display a list of issues assigned to you from connected integrations and guide you through creating a branch named after the issue. The issue will then be associated with the branch in GitLens, allowing you to refer back to it while working.

## Recent Section

The Recent section helps reduce the pain of context switching by keeping track of recent branches, worktrees, and pull requests you've interacted with within a specific timeframe. This makes it easy to return to work you may have switched away from. It's also helpful for finding recently merged or closed PRs that you worked on.

To save space, associated branches and issues are collapsed by default in this section. You can click to expand them for additional context.

<img src="/wp-content/uploads/home-view-recent.png" class="img-responsive center img-bordered">
