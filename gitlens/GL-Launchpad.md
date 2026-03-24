---
title: GitLens Launchpad
description: Use GitLens Launchpad to organize and prioritize pull requests across supported GitLens IDEs.
product: GitLens
feature: Launchpad
content_type: how-to
audience: developer
plan_required: Pro
status: GA
last_verified: 2026-03
taxonomy:
    category: gitlens

---

<kbd>Last updated: March 2026</kbd>

## Launchpad <code>PRO</code>

GitLens Launchpad helps GitLens users organize pull requests by status and next action without leaving the editor. Use it when you need a prioritized review queue across repositories and connected Git hosts, especially for pull requests waiting on you or needing follow-up.

| Workflow | Recommended tool | Best for |
|---|---|---|
| Prioritizing pull requests across repositories | Launchpad | A single action queue for reviews and follow-up |
| Inspecting current repository activity | Home View | Quick status and recent work in one repository |
| Reviewing one pull request in the host UI | Browser or host UI | Host-specific merge or admin actions |

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" class="help-center-img img-bordered" alt="Launchpad view showing pull requests organized by status" />
  <figcaption style="text-align: center; color: #888">GitLens Launchpad pull request overview</figcaption>
</figure>

---

### How to Open Launchpad

1. Open the Command Palette:
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
2. Search for **GitLens: Open Launchpad**, or select **Pull Request** from the status bar in VS Code.

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" class="help-center-img img-bordered" alt="Opening the Launchpad from the Command Palette in VS Code" />
  <figcaption style="text-align: center; color: #888">Accessing the Launchpad</figcaption>
</figure>

---

### How to Review Pull Requests from Launchpad

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

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" class="help-center-img img-bordered" alt="Pull request details in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Viewing pull request details</figcaption>
</figure>

---

### How to Start or Review Code Suggestions from Launchpad

You can start or review [Code Suggestions](/gitlens/gitlens-features/#code-suggest-preview) directly from pull requests in the Launchpad.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" class="help-center-img img-bordered" alt="Launchpad pull request actions with Code Suggest option" />
  <figcaption style="text-align: center; color: #888">Starting or reviewing Code Suggestions</figcaption>
</figure>

---

### How to Pin or Snooze Pull Requests

- **Pin**: Use the pin icon <i class="fa-solid fa-thumbtack"></i> to move a pull request to the pinned group.
- **Snooze**: Use the snooze icon <i class="fa-solid fa-snooze"></i> to move it to the snoozed group.
- To unpin or unsnooze, select the same icon again.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" class="help-center-img img-bordered" alt="Pinning or snoozing pull requests in the Launchpad" />
  <figcaption style="text-align: center; color: #888">Pinning and snoozing pull requests</figcaption>
</figure>

---

### Availability

- Supported for **GitHub.com** and **GitLab.com** repositories only. Connect the [GitHub or GitLab integration](/gitlens/gitlens-features/#connecting-the-github-and-gitlab-integration) to use Launchpad.
- Launchpad prioritizes items that require immediate action, placing them at the top. (This may change in future updates.)
- This feature is available on **Pro, Advanced, Business, and Enterprise** plans.
