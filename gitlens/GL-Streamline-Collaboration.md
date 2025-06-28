---
title: GitLens Streamline Collaboration
description: How GitLens helps teams collaborate efficiently using Cloud Patches and Code Suggest.
taxonomy:
  category: gitlens
---
<kbd>Last updated: July 2025</kbd>

<figure class='embed-container embed-container--16-9'>
  <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen title="GitLens Streamline Collaboration video overview"></iframe>
</figure>

&nbsp;

Collaborating in a repository can be tricky—especially when you want to share work without flooding the remote with temporary commits or branches. Traditional pull request workflows also limit which files you can review or comment on—typically only those that have changed.

GitLens helps streamline collaboration through:

- **Cloud Patches** – Share uncommitted code changes without pushing to a remote.
- **Code Suggest** – Propose changes on any file, not just modified ones.

## Cloud Patches <span style="color: #888;">`PRO`</span>

Cloud Patches are Git patches that can be shared with anyone in your GitKraken organization. Teammates can apply them directly to their working directory—ideal for reviewing or collaborating on code before it’s committed.

To create a Cloud Patch:

1. Make and save changes to any file.
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
3. Run: `GitLens: Share as Cloud Patch…`
4. Select teammates to share with.

Recipients will see the patch in the **Cloud Patch** sidebar and can apply it directly to their workspace.

[Open the Cloud Patches View in GitLens](vscode://eamodio.gitlens/link/command/cloud-patches)

<figure class='callout callout--warning'>
  <p>This feature is available with a GitLens Pro subscription or higher.</p>
</figure>


## Code Suggest <span style="color: #888;">`PRO`</span>

Code Suggest lets you propose edits to any file in a repository—regardless of whether the file was modified. You can submit these suggestions directly to another team member’s open pull request.

To create a Code Suggestion:

1. Check out a branch that has an open pull request.
2. Make and save changes to any file.
3. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
4. Run: `GitLens: Show Inspect View` > **Suggest Changes for PR**.

The PR creator can:

- Review your suggestions
- Apply them to their working directory
- Commit and push the changes to the open pull request

<figure class='callout callout--warning'>
  <p>This feature is available with a GitLens Pro subscription or higher.</p>
</figure>

