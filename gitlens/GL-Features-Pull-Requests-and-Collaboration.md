---
title: Pull Request and Collaboration Features
description: Technical reference for GitLens Launchpad, Start Review, Start Work, Code Suggest, and Cloud Patches.
product: GitLens
feature: Pull Requests and Collaboration
content_type: reference
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [launchpad, pull-requests, start-review, start-work, code-suggest, cloud-patches]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Pull Requests and Collaboration"
    nav_order: 30
    nav_parent: "gitlens-features"
    page_type: "content"
    card_icon: "git-pull-request"
    card_color: "red"
    card_description: "Launchpad, Start Review and Start Work, Code Suggest, and Cloud Patches"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

Features marked with <span style="color: #888;">`PREVIEW`</span> require a GitKraken Account, with access based on your [plan level](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) (Community, Pro, etc).

***

## Launchpad `PRO`

For workflows and examples, see [Launchpad](/gitlens/gl-launchpad/) and [Accelerate PR Reviews](/gitlens/gl-accelerate-pr-reviews/).

Launchpad groups your pull requests (PRs) by status, so you can see which ones need your action first and act on them without leaving VS Code.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-quickpick.png" alt="The Launchpad quick pick with pull requests grouped by status" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">View and act on PRs based on current status</figcaption>
</figure>

> **Note:** Launchpad supports GitHub, GitHub Enterprise, GitLab, GitLab Self-Managed, Azure DevOps, Azure DevOps Server, Bitbucket, and Bitbucket Data Center repositories. To use it, connect your Git provider, for example with the [GitHub or GitLab Integration](https://help.gitkraken.com/gitlens/gl-features-integrations-and-links/#connecting-the-github-and-gitlab-integration).

---

### Accessing Launchpad

- From the **Command Palette**: `Command/Ctrl + Shift + P` → `GitLens: Open Launchpad`
- From the **Pull Request status bar item** in VS Code

<figure>
  <img src="/wp-content/uploads/gl-access-launchpad.gif" alt="Opening Launchpad from status bar" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open Launchpad from the status bar or Command Palette</figcaption>
</figure>

---

### Using Launchpad

Launchpad groups PRs by these statuses:

- Ready to merge
- Blocked
- Requires follow-up
- Needs your review
- Waiting for review
- In merge queue
- Draft
- Snoozed

Click a PR to:

- View full details
- Open in your browser
- Merge (if eligible), or add it to the merge queue with **Add to Merge Queue...** when its base branch requires one
- Take it out of the merge queue with **Remove from Merge Queue...**
- Rebase the stack (for a GitHub stacked pull request)
- Switch to the branch or open in a worktree

To find a pull request that is not in your groups, select **Search for Pull Request...** and enter a term. Launchpad searches the pull requests of all your connected providers, including Azure DevOps and Bitbucket Data Center, for that term. You can also paste a pull request's URL to open that pull request. Pasting a URL works for every connected provider, including Azure DevOps, Azure DevOps Server, Bitbucket, and Bitbucket Data Center.

For repositories on GitHub.com that merge through a merge queue, queued pull requests appear in the **In Merge Queue** group with their queue status, and pull requests failing in the queue appear under **Blocked** as **Failing in Merge Queue**. Merge queues are not supported for GitHub Enterprise. For details, see [GitHub Merge Queue](/gitlens/gl-integrations/#github-merge-queue).

<figure>
  <img src="/wp-content/uploads/gl-view-pull-request.png" alt="PR detail view in Launchpad" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Interact with pull requests directly in VS Code</figcaption>
</figure>

You can also start or review [Code Suggestions](#code-suggest) directly from the PR action menu.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-code-suggest.png" alt="Launchpad with Code Suggest options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Suggest code edits from within the Launchpad</figcaption>
</figure>

*Launchpad is also available through the [GitKraken MCP](https://help.gitkraken.com/mcp/mcp-tools-reference/).*

---

### Start Review `PRO`

The **Start PR Review** command (`gitlens.startReview`) guides you through starting a pull request review:

1. Select a PR from your connected integration.
2. Choose whether to check out the branch or create a worktree.
3. Optionally, open an AI chat pre-filled with a review prompt.

Access it from the Command Palette: `GitLens: Start PR Review`

When AI features are enabled, Start Review asks whether to open the review in an agent, continue manually, or, when Kepler supports the pull request's provider, open it in [Kepler](/gitlens/gl-agents/#start-tasks-and-reviews-in-kepler). Select **Always use this choice** to skip that step next time; the `gitlens.ai.openInAgent` setting stores your choice. If no local clone of the pull request's repository is found, Start Review offers **Clone Repository...** and **Choose a Local Folder...** instead of stopping.

---

### Start Work `PRO`

The **Start Work** command (`gitlens.startWork`) starts work on an issue from your connected integrations: pick the issue, and GitLens creates a branch for it. If you are not signed in, Start Work first asks you to sign in or start a Pro trial before it offers to connect an integration.

Access it from the Command Palette: `GitLens: Start Work`

GitLens suggests a branch name built from the issue, which you can edit before the branch is created. By default the name is the issue ID followed by its title, such as `ABC-123-update-login-flow`. To change the pattern, set **Branch name format** in the **Start Work** category of [GitLens Settings](/gitlens/gitlens-settings/#integrations) (`gitlens.startWork.branchNameFormat`), using `${id}` for the issue ID and `${title}` for the title, for example `feature/${id}/${title}`.

---

### Pin or Snooze PRs

Use the pin icon <i class="fa-solid fa-thumbtack"></i> to keep important PRs in the **Pinned** group.

Use the snooze icon <i class="fa-solid fa-snooze"></i> to move less urgent PRs into the **Snoozed** group.

Click the icon again to unpin or unsnooze as needed.

<figure>
  <img src="/wp-content/uploads/gl-launchpad-pin-or-snooze.png" alt="Pin or snooze pull requests" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Pin or snooze PRs to manage your workflow</figcaption>
</figure>

> **Note:** Launchpad lists the items that need your action at the top of the list.

> **Warning:** This feature is only available on GitLens Pro subscription tiers or higher.

***

## Code Suggest

For workflows and examples, see [Code Suggest](/gitlens/gl-code-suggest/).

Use GitKraken Code Suggest to propose edits to any file in a project, including lines that a pull request did not change. You can suggest changes from GitLens, GitKraken Desktop, or [gitkraken.dev](https://gitkraken.dev).

When a pull request is open, collaborators can review your suggestions and apply them to the pull request.

> **Note:** Code Suggest is currently supported only for repositories hosted on **github.com**.

<figure>
  <img src="/wp-content/uploads/gl-code-suggest.png" alt="GitLens Code Suggest UI showing a PR suggestion in progress" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Suggest changes beyond just modified lines</figcaption>
</figure>

### How to Create a Code Suggestion

1. Open the [GitLens Inspect Overview](/gitlens/side-bar/#overview) for the repository.
2. Check out a branch that has an open pull request.
3. Click **Start Review for PR #PR**.
4. Modify and save any files to include in the suggestion.
5. When ready, select **Suggest Changes for PR**, add a title, and click **Create Code Suggestion**.

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-create.gif" alt="Creating a code suggestion in GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create a suggestion from your local changes</figcaption>
</figure>

After you submit the suggestion, the pull request receives a comment with 2 options:

- **Code Suggestion for #PR** — opens in gitkraken.dev
- **Locally on your machine** — opens in GitLens or [GitKraken Desktop](/gitkraken-client/pull-requests/#review-code-and-suggest-changes)

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-comment.png" alt="Comment with code suggestion options" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Collaborators can choose where to review and apply suggestions</figcaption>
</figure>

### Accepting a Suggestion Locally

1. Open the suggestion in GitLens or GitKraken Desktop.
2. Review each modified file.
3. Select **Apply** to apply the patch to your current branch.  
   Or use the dropdown to **Apply to a Branch**.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" alt="Accepting suggestions from GitLens" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Apply suggestions directly to a local or new branch</figcaption>
</figure>

### Accepting a Suggestion on gitkraken.dev

1. Select **Code Suggestion for #PR** in the PR comment.
2. Review the changes on gitkraken.dev.
3. Click **Commit Suggestions** to commit the patch directly to the PR's branch.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion.gif" alt="Committing suggestions from gitkraken.dev" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Accept changes and push them to the remote branch</figcaption>
</figure>

***

## Cloud Patches <span style="color: #888;">`PREVIEW`</span>

For workflows and examples, see [Cloud Patches](/gitlens/gl-cloud-patches/).

Use Cloud Patches to share in-progress work with your team before you open a pull request.

### What Are Cloud Patches and Why Use Them?

Cloud Patches are Git patches that GitKraken stores in secure cloud storage, so you can share them across GitLens, GitKraken Desktop, and the GitKraken CLI. GitLens uploads the patch directly from your machine.

Because you can share work before a pull request exists, your team can give feedback earlier.

---

### How to Set Up Cloud Patches

Cloud Patches are on by default. You turn them on or off separately in each GitKraken app. To manage them in GitLens:

1. Open the Command Palette:  
   `Ctrl`/`Command` + `Shift` + `P` → **Preferences: Open User Settings (JSON)**

2. Add the following line to your settings:

       "gitlens.cloudPatches.enabled": true

To disable Cloud Patches, change the value to `false`.


### How to Work with Cloud Patches

Your Cloud Patches are in the **Cloud Patches** view in the GitLens side bar.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-create.webp" alt="GitLens Cloud Patch creation screen" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create a patch directly from your sidebar</figcaption>
</figure>

You can create a Cloud Patch from:

- Working Changes
- Commits
- Stashes
- Comparisons

To create one, use **Share as Cloud Patch** from the command palette or the **Share** submenu in applicable GitLens views.

<figure>
  <img src="/wp-content/uploads/gl-create-cloud-patch-example.png" alt="Share as Cloud Patch in context menu" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Share patches from a variety of Git sources</figcaption>
</figure>

#### Sharing Options

Choose how your patch can be accessed:

- **Anyone with the link** — Public access without signing in.
- **Anyone in my org** — Restricted to users in your GitKraken organization (GitKraken sign-in required).
- **Only collaborators** — Restricted to selected organization members. Use **Invite** to choose recipients.

Cloud Patches shared with you appear under the **Shared with Me** section.

> **Note:** If you're a member of multiple organizations, you can switch organizations from the GitKraken Account view.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" alt="Cloud patch share dialog with access levels" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Control access to shared patches by role</figcaption>
</figure>

You can also apply a Cloud Patch from a shared URL. Click or paste the link, then follow the GitLens prompts to apply it to your working directory or to a new/existing branch.

<figure>
  <img src="/wp-content/uploads/gl-apply-patch-example.gif" alt="Apply a cloud patch animation" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Apply a patch to your current repo</figcaption>
</figure>

To delete a Cloud Patch, right-click it and choose **Delete Cloud Patch...**.

<figure>
  <img src="/wp-content/uploads/gl-delete-cloud-patch-01-v3@2x.png" alt="Cloud Patches view in the GitLens sidebar showing a right-click context menu with Delete Cloud Patch option on a patch entry" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Remove unused patches with one click</figcaption>
</figure>


### Self-Hosting Cloud Patch Data

If you prefer not to store Cloud Patch data on GitKraken servers, you can configure GitLens to use your own AWS S3 storage. To set it up, see the [Self-Hosting Guide](/gk-dev/gk-dev-home/#self-hosted).
