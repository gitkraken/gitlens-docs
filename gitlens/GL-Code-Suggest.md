---
title: GitLens Code Suggest
description: Find, apply, and accept or reject Code Suggestions on your GitHub pull requests in GitLens.
taxonomy:
    category: gitlens
last_updated: 2026-11

---

<kbd>Last updated: November 2026</kbd>

## What Is Code Suggest?

Code Suggest lets a reviewer propose edits to any file in a repository, including lines a pull request did not change, and attach them to the pull request as a Code Suggestion. Reviewers create Code Suggestions in [GitKraken Desktop](/gitkraken-desktop/pull-requests/#how-to-accept-or-reject-suggestions).

In GitLens, you find the Code Suggestions on a pull request, apply them to your working tree, and accept or reject them.

---

## Find Code Suggestions on a Pull Request

When someone adds a Code Suggestion, the pull request gets a comment with 2 links:

- **Code Suggestion for #PR** opens the suggestion on gitkraken.dev.
- **locally on your machine** opens the suggestion in GitLens or GitKraken Desktop.

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-comment.png" class="help-center-img img-bordered" alt="Pull request comment with Code Suggestion options" />
  <figcaption style="text-align: center; color: #888">Pull request with Code Suggestion comment</figcaption>
</figure>

You can also find them in the GitLens views:

1. Expand a branch, commit, or worktree that has a pull request, then expand the pull request.
2. Expand **Code Suggestions** to list each suggestion with its author.
3. Select a suggestion to open it in **Patch Details**.

---

## Review and Apply Suggestions Locally

1. Open the suggestion in **Patch Details**, from the pull request comment or the **Code Suggestions** list.
2. Review the changes file by file.
3. Select **Apply Patch** to apply the changes to your current branch, or open the **Apply Patch Options...** menu and select **Apply to a Branch**.
4. Select **Accept** to mark the suggestion accepted, or **Reject** to decline it.

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" class="help-center-img img-bordered" alt="Applying a Code Suggestion locally in GitLens" />
  <figcaption style="text-align: center; color: #888">Applying a Code Suggestion locally</figcaption>
</figure>

---

## Review and Commit Suggestions in gitkraken.dev

1. Select **Code Suggestion for #PR** to open the suggestion in **gitkraken.dev**.  
2. Review each file and its proposed changes.  
3. Select **Commit Suggestions**.  

This creates a new commit on the remote branch (shown under **COMMIT SUGGESTIONS TO**).

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion.gif" class="help-center-img img-bordered" alt="Accepting and committing Code Suggestions in gitkraken.dev" />
  <figcaption style="text-align: center; color: #888">Committing suggestions in gitkraken.dev</figcaption>
</figure>

---

## Availability

<div class='callout callout--basic'>
  <p><strong>Note:</strong> Code Suggest is supported only for repositories on <strong>GitHub.com</strong>.</p>
</div>