---
title: GitLens Home View Overview
description: Learn how the GitLens Home View helps you track current work, plan next steps, and review recent activity
taxonomy:
    category: gitlens
---
<kbd>Last updated: July 2025</kbd>

## Overview

<a href="vscode://eamodio.gitlens/link/command/home">Open the Home View in GitLens</a>

The GitLens Home View helps you stay focused by organizing your work around three key questions:

1. [What am I actively working on now?](/gitlens/home-view/#View-Your-Active-Repository-and-Branch)
2. [What should I work on next?](/gitlens/home-view/#launchpad-section)
3. [What have I worked on recently?](/gitlens/home-view/#recent-section)

Each section in the Home View offers direct insights and actionable links to help you manage tasks efficiently across your repositories.

<figure>
  <div class='embed-container embed-container--16-9'>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/jVzhyVBgNGg?si=T5hmEEe0jO09RNbl" title="Introducing the GitLens Home View" frameborder="0" allowfullscreen></iframe>
  </div>
  <figcaption style="text-align:center; color:#888">Video overview: Introducing the GitLens Home View</figcaption>
</figure>

## Connect to GitHub, GitLab, and Jira

GitLens integrates with popular code hosting and issue tracking services—including GitHub, GitLab, and Jira—to help you monitor branches, track issues, and manage pull requests.

You can connect integrations directly from the top of the Home View.

Some advanced integration features are available with <a href="https://help.gitkraken.com/gitlens/gitlens-community-vs-gitlens-pro/">GitLens Pro features</a>.

<figure>
  <img src="/wp-content/uploads/home-view-integrations.png" alt="GitLens Home View showing integration panel" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Home View integration panel</figcaption>
</figure>

## View Your Active Repository and Branch

At the top of the GitLens Home View, you can see the current state of your active repository and branch.

This section gives you quick access to:
- Sync actions (push, pull, fetch)
- Switch active repositories
- View working directory changes
- Launch the <a href="https://help.gitkraken.com/gitlens/gitlens-home/#commit-graph">GitLens Commit Graph</a>

<figure>
  <img src="/wp-content/uploads/home-view-active-work.png" alt="GitLens Home View showing active repository section" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Home View active repository section</figcaption>
</figure>

When you connect integrations and associate issues or pull requests with your current branch, GitLens Pro groups them for streamlined access. You can check pull request statuses, resume reviews, or revisit linked issue details—all from within this view.

If a pull request isn’t open or your branch isn't yet linked to an issue, GitLens guides you through connecting it.


## Plan Next Steps with Launchpad <span class="badge badge--pro">Pro</span>

<div class='callout callout--warning'>
    <p>This feature is available with GitLens Pro or higher subscription tiers.</p>
</div>

The Launchpad section highlights upcoming priorities to help you decide what to work on next. It surfaces pull requests needing your review and lets you start new work by creating branches and worktrees for issues assigned to you.

<figure>
  <img src="/wp-content/uploads/home-view-next.png" alt="GitLens Home View showing Launchpad section" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Home View Launchpad section</figcaption>
</figure>

### Review Pull Request Statuses

The Launchpad Summary shows how many pull requests are blocking your team and provides reasons for each. With GitLens Pro, you can click a status to open the related pull request in <a href="https://help.gitkraken.com/gitlens/gitlens-features/#launchpad-pro">Launchpad</a>. You can then take actions like checking out the PR in a worktree, enabling fast reviews without changing your main branch.

### Start Work on an Issue

To begin working on an assigned issue, click **Start Work on an Issue**. GitLens displays a list of assigned issues from connected integrations and helps you create a branch named after the issue. The issue becomes linked to the new branch, keeping context visible throughout your work.

## Return to Recent Work

The Recent section minimizes context switching by showing your recent branches, worktrees, and pull requests. This makes it easy to return to recent tasks or review merged and closed pull requests.

By default, the section collapses details like associated issues and branches to reduce clutter. Click any item to expand it for more context.

<figure>
  <img src="/wp-content/uploads/home-view-recent.png" alt="GitLens Home View showing recent activity section" class="help-center-img img-bordered">
  <figcaption style="text-align:center; color:#888">GitLens Home View recent activity section</figcaption>
</figure>