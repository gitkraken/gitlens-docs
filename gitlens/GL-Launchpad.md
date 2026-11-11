---
title: Launchpad
description: Use GitLens Launchpad to organize and prioritize pull requests in VS Code.
taxonomy:
    category: gitlens
last_updated: 2026-11

---

<kbd>Last updated: November 2026</kbd>

## Launchpad <code>PRO</code>

Use the GitLens Launchpad to see your pull requests grouped by status, so you can identify bottlenecks, prioritize work, and act on each pull request.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" class="help-center-img img-bordered" alt="The Launchpad quick pick with pull requests grouped by status" />
  <figcaption style="text-align: center; color: #888">GitLens Launchpad pull request overview</figcaption>
</figure>

---

### Open the Launchpad

1. Open the Command Palette:
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
2. Search for **GitLens: Open Launchpad**, or select **Pull Request** from the status bar in VS Code.

To learn more about Launchpad, open the GitLens **Welcome** view, which includes a Launchpad and Worktrees step. Select any of these to open it:

- **Click to learn more about Launchpad**, when Launchpad asks you to connect an integration
- The **What is this?** icon in the Launchpad status bar tooltip
- **Learn about Launchpad...** in the Launchpad view

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" class="help-center-img img-bordered" alt="Opening the Launchpad from the Command Palette in VS Code" />
  <figcaption style="text-align: center; color: #888">Accessing the Launchpad</figcaption>
</figure>

---

### Review Pull Requests

The Launchpad shows pull requests for your repositories, grouped by status:

- **Ready to Merge**
- **Blocked**
- **Requires Follow-up**
- **Needs Your Review**
- **Waiting for Review**
- **In Merge Queue**
- **Draft**
- **Snoozed**

Select a pull request to:

- View detailed information
- Open it in a browser
- Merge it (if ready)
- Rebase its stack with **Rebase Stack...**, for a GitHub stacked pull request
- Switch to the branch or worktree

To find a pull request that is not in your list, select **Search for Pull Request...** and enter a term. Launchpad matches the term against pull request titles and descriptions. You can also paste a pull request URL to act on that pull request.

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" class="help-center-img img-bordered" alt="Pull request details in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Viewing pull request details</figcaption>
</figure>

#### Pull Requests in a GitHub Merge Queue

If a repository on GitHub.com merges through a merge queue, Launchpad shows where each pull request stands in the queue:

- A pull request waiting in the queue appears under **In Merge Queue**, with its queue status, such as *#1 in the merge queue, checks running*.
- A pull request that is failing in the queue, or that the queue just removed after a failed run, appears under **Blocked** as **Failing in Merge Queue**.
- When the base branch requires a merge queue, **Add to Merge Queue...** replaces **Merge...** for a pull request that is ready to merge.
- To take a pull request out of the queue, select it and then select **Remove from Merge Queue...**. The pull request loses its place in the queue.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-merge-queue-01-v2@2x.png" class="help-center-img img-bordered" alt="Launchpad open on a queued pull request, Add a release checklist #13, whose status reads &quot;#1 in the merge queue, checks running&quot;, with Remove from Merge Queue... (Will remove this pull request from the merge queue, losing its place) among its actions." />
  <figcaption style="text-align: center; color: #888">Removing a queued pull request from the merge queue</figcaption>
</figure>

GitLens supports merge queues on GitHub.com only, not on GitHub Enterprise. For details, see [GitHub Merge Queue](/gitlens/gl-integrations/#github-merge-queue).

---

### Code Suggestions

You can start or review [Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) from pull requests in the Launchpad.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" class="help-center-img img-bordered" alt="Launchpad pull request actions with Code Suggest option" />
  <figcaption style="text-align: center; color: #888">Starting or reviewing Code Suggestions</figcaption>
</figure>

---

### Pin or Snooze Pull Requests

Pin or snooze a pull request to move it to its own group:

- **Pin**: Select the pin icon <i class="fa-solid fa-thumbtack"></i> to move a pull request to the **Pinned** group.
- **Snooze**: Select the snooze icon <i class="fa-solid fa-snooze"></i> to move a pull request to the **Snoozed** group.
- **Unpin or unsnooze**: Select the same icon again.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" class="help-center-img img-bordered" alt="Pinning or snoozing pull requests in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Pinning and snoozing pull requests</figcaption>
</figure>

---

### Availability

- Supported for pull requests on **GitHub**, **GitHub Enterprise**, **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server**, **Bitbucket**, and **Bitbucket Data Center**. Connect the [integration for your provider](/gitlens/gl-integrations/) to use Launchpad. **Search for Pull Request...** searches every connected provider.
- Launchpad places items that require immediate action at the top.
- Launchpad requires a **Pro subscription tier or higher**.