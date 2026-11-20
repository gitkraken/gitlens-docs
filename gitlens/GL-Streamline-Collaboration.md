---
title: GitLens Streamline Collaboration
description: Share uncommitted changes with Cloud Patches and review Code Suggestions on your pull requests in GitLens.
taxonomy:
  category: gitlens
last_updated: 2026-11
---
<kbd>Last updated: November 2026</kbd>

<figure class='embed-container embed-container--16-9'>
  <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen title="GitLens Streamline Collaboration video overview"></iframe>
</figure>

&nbsp;

GitLens lets you share work without pushing temporary commits or branches to the remote. A pull request review covers only the files that changed, but with GitLens you can also review edits suggested on other files.

- **Cloud Patches**: share uncommitted code changes without pushing to a remote.
- **Code Suggest**: review and apply changes that reviewers suggest on any file, including files the pull request did not modify.

## Cloud Patches <span style="color: #888;">`PRO`</span>

Cloud Patches are Git patches that you share with anyone in your GitKraken organization. Teammates apply them to their working directory to review or collaborate on code before it is committed.

To create a Cloud Patch:

1. Make and save changes to any file.
2. Open the Command Palette (**Ctrl/⌘ + Shift + P**).
3. Run **GitLens: Share as Cloud Patch...**.
4. Select teammates to share with.

Recipients see the patch in the **Cloud Patches** view and can apply it to their working directory.

[Open the Cloud Patches View in GitLens](vscode://eamodio.gitlens/link/command/cloud-patches)

<figure class='callout callout--warning'>
  <p>This feature is available with a GitLens Pro subscription or higher.</p>
</figure>


## Code Suggest <span style="color: #888;">`PRO`</span>

A Code Suggestion proposes edits to any file in a repository, whether or not the pull request changed it. Reviewers create Code Suggestions in GitKraken Desktop and attach them to an open pull request.

To review a Code Suggestion in GitLens:

1. In a GitLens view, expand the branch that has the pull request, then expand the pull request.
2. Expand **Code Suggestions** and select a suggestion to open it in **Patch Details**.
3. Select **Apply Patch** to apply the changes to your working tree.
4. Select **Accept** or **Reject** to close the suggestion.

See [GitLens Code Suggest](/gitlens/gl-code-suggest/).

<figure class='callout callout--warning'>
  <p>This feature is available with a GitLens Pro subscription or higher.</p>
</figure>

