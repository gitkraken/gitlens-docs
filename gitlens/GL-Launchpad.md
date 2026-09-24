---
title: Launchpad
description: Use GitLens Launchpad to organize and prioritize pull requests in VS Code.
taxonomy:
    category: gitlens
last_updated: 2026-09

---

<kbd>Last updated: September 2026</kbd>

## Launchpad <code>PRO</code>

The GitLens Launchpad helps you manage pull requests by status, so you can quickly identify bottlenecks, prioritize work, and take action.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" class="help-center-img img-bordered" alt="Launchpad view showing pull requests organized by status" />
  <figcaption style="text-align: center; color: #888">GitLens Launchpad pull request overview</figcaption>
</figure>

---

### Open the Launchpad

1. Open the Command Palette:
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
2. Search for **GitLens: Open Launchpad**, or select **Pull Request** from the status bar in VS Code.

To learn more about Launchpad, select **Click to learn more about Launchpad** when Launchpad asks you to connect an integration, the **What is this?** icon in the Launchpad status bar tooltip, or **Learn about Launchpad...** in the Launchpad view. Each of these opens the GitLens **Welcome** view, which includes a Launchpad and Worktrees step.

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" class="help-center-img img-bordered" alt="Opening the Launchpad from the Command Palette in VS Code" />
  <figcaption style="text-align: center; color: #888">Accessing the Launchpad</figcaption>
</figure>

---

### Review Pull Requests

The Launchpad displays pull requests for your repositories, grouped by status:
- Ready to merge
- Blocked
- Requires follow-up
- Needs your review
- Waiting for review
- Draft
- Snoozed

Select a pull request to:
- View detailed information
- Open it in a browser
- Merge it (if ready)
- Switch to the branch or worktree

To find a pull request that isn't in your list, select **Search for Pull Request...** and enter a term. Launchpad matches the term against pull request titles and descriptions. You can also paste a pull request URL to act on that pull request.

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" class="help-center-img img-bordered" alt="Pull request details in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Viewing pull request details</figcaption>
</figure>

---

### Code Suggestions

You can start or review [Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) directly from pull requests in the Launchpad.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" class="help-center-img img-bordered" alt="Launchpad pull request actions with Code Suggest option" />
  <figcaption style="text-align: center; color: #888">Starting or reviewing Code Suggestions</figcaption>
</figure>

---

### Pin or Snooze Pull Requests

- **Pin**: Use the pin icon <i class="fa-solid fa-thumbtack"></i> to move a pull request to the pinned group.
- **Snooze**: Use the snooze icon <i class="fa-solid fa-snooze"></i> to move it to the snoozed group.
- To unpin or unsnooze, select the same icon again.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" class="help-center-img img-bordered" alt="Pinning or snoozing pull requests in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Pinning and snoozing pull requests</figcaption>
</figure>

---

### Availability

- Supported for pull requests on **GitHub**, **GitHub Enterprise**, **GitLab**, **GitLab Self-Hosted**, **Azure DevOps**, **Azure DevOps Server**, **Bitbucket**, and **Bitbucket Data Center**. Connect the [integration for your provider](/gitlens/gl-integrations/) to use Launchpad. **Search for Pull Request...** searches every connected provider.
- Launchpad prioritizes items that require immediate action, placing them at the top. (This may change in future updates.)
- This feature is available with a **Pro subscription tier or higher**.