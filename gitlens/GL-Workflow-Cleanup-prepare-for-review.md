---
title: Cleaning Up and Preparing Work for Review
description: Use Git intelligence to transform iterative work into clean, reviewable history
taxonomy:
  category: gitlens
---

<kbd>Last updated: February 2026</kbd>

**Level:** Intermediate Developers
**Primary Goal:** Use Git intelligence to transform iterative work into clean, reviewable history

## When to use this workflow

Use this workflow when you are:

- Preparing a pull request for review

- Cleaning up “wip” or noisy commit history

- Juggling multiple streams of work

- Optimizing for reviewer clarity and speed

## Real-world scenario

You have finished implementing a feature, but your branch contains several exploratory commits that would be difficult for reviewers to follow.

## How GitLens helps (in practice)

You begin by opening the **Commit Graph** from the GitLens sidebar, which gives you a visual view of your branch history and how your work diverges from main. From there, you select the commits related to the feature and open **Commit Composer** directly from the graph.

<figure>
  <img src="/wp-content/uploads/workflows-2-cleaning-and-prep-recompose-commits-01.png" class="help-center-img img-bordered" alt="A context menu within the Commit Graph showing the Recompose Selected Commits option" />
  <figcaption style="text-align: center; color: #888">Recompose Selected Commits</figcaption>
</figure>

<!-- Full tab instead of just the bottom panel
<figure>
  <img src="/wp-content/uploads/workflows-2-cleaning-and-prep-recompose-commits-02.png" class="help-center-img img-bordered" alt="A context menu within the Commit Graph showing the Recompose Selected Commits option" />
  <figcaption style="text-align: center; color: #888">Recompose Selected Commits</figcaption>
</figure>
-->

Commit Composer uses Git intelligence to understand the structure of your changes and allows you to recompose them into clearer, more intentional commits. With **Selective Recomposition**, you can choose only the relevant commits, rewrite their messages, split changes, or combine related work, all before anything is rewritten on disk.

<figure>
  <img src="/wp-content/uploads/workflows-2-cleaning-and-prep-recompose-result.png" class="help-center-img img-bordered" alt="A screenshot of the Commit Composer with Selective Recomposition" />
  <figcaption style="text-align: center; color: #888">Commit Composer with Selective Recomposition</figcaption>
</figure>

As you review your branch, you open **Launchpad** to check for open pull requests, review feedback, or dependencies that might affect your changes, keeping everything in one place instead of jumping between tools.

<figure>
  <img src="/wp-content/uploads/workflows-2-cleaning-and-prep-launchpad.png" class="help-center-img img-bordered" alt="A screenshot of GitKraken Launchpad which shows issues assigned to the user" />
  <figcaption style="text-align: center; color: #888">Launchpad</figcaption>
</figure>

When an urgent fix on another branch comes up, you create a **Worktree** from GitLens, which lets you check out another branch in a separate folder without stashing or disturbing your current work. Throughout the process, you rely on advanced **Commit Graph context menu actions**, accessed by right-clicking commits, to compare branches, inspect diffs, and validate that your history tells a clear story.

<figure>
  <img src="/wp-content/uploads/workflows-2-cleaning-and-prep-context-menu.png" class="help-center-img img-bordered" alt="A screenshot of the Commit Graph context menu showing all of the options available" />
  <figcaption style="text-align: center; color: #888">Commit Graph Context Menu</figcaption>
</figure>

GitLens uses Git intelligence to help you ship work that is easier to review, reason about, and maintain.

## Key GitLens features used

- [Commit Graph (visual branch and commit context)](https://help.gitkraken.com/gitlens/gitlens-features/#commit-graph-pro)

- [Commit Composer with Selective Recomposition](https://help.gitkraken.com/gitlens/gitlens-features/###Commit-composer:-Selective-Recomposition)

- [Launchpad (PR and review awareness)](https://help.gitkraken.com/gitlens/gitlens-features/#launchpad-pro)

- Worktrees (parallel branch workflows)

- Commit Graph context menu actions

## Outcome

You submit a pull request with a clean, intentional commit history that reviewers can understand quickly and confidently.
