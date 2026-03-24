---
title: GitLens Code Suggest
description: Use GitLens Code Suggest to propose edits and code review suggestions across entire projects in GitHub repositories.
product: GitLens
feature: Code Suggest
content_type: how-to
audience: developer
plan_required: Pro
status: GA
last_verified: 2026-03
taxonomy:
    category: gitlens

---

<kbd>Last updated: March 2026</kbd>

## What Is Code Suggest?

GitLens Code Suggest lets GitLens users propose project-wide edits and review suggestions for GitHub pull requests from **GitLens**, **GitKraken Desktop**, or **gitkraken.dev**. Use it when review feedback spans files beyond changed-line comments and your repository supports Code Suggest workflows.

**Requirements:**
- **Supported host:** GitHub.com repositories
- **Requires:** An open pull request on the branch you are reviewing
- **Review surfaces:** GitLens, GitKraken Desktop, or gitkraken.dev
- **Best for:** Multi-file or project-wide pull request suggestions

<figure>
  <img src="/wp-content/uploads/gl-code-suggest.png" class="help-center-img img-bordered" alt="GitLens Code Suggest view showing suggestion options" />
  <figcaption style="text-align: center; color: #888">GitLens Code Suggest view</figcaption>
</figure>

---

## How to Start a Code Suggestion

1. Open the [GitLens Inspect Overview](/gitlens/side-bar/#overview) for your repository.  
2. Check out a branch with an open pull request.  
3. Select **Start Review for PR #PR**.  
4. Modify and save any files you want to include in the suggestion.  
5. When ready, select **Suggest Changes for PR** → provide a title → **Create Code Suggestion**.  

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-create.gif" class="help-center-img img-bordered" alt="Creating a Code Suggestion in GitLens" />
  <figcaption style="text-align: center; color: #888">Creating a Code Suggestion</figcaption>
</figure>

This action adds a comment on the pull request with two options:  
- **Code Suggestion for #PR** → review in **gitkraken.dev**  
- **Locally on your machine** → review in **GitLens** or **GitKraken Desktop**

<figure>
  <img src="/wp-content/uploads/gl-code-suggest-comment.png" class="help-center-img img-bordered" alt="Pull request comment with Code Suggestion options" />
  <figcaption style="text-align: center; color: #888">Pull request with Code Suggestion comment</figcaption>
</figure>

---

## How to Review and Apply Suggestions Locally

1. Select **Locally on your machine**.  
2. Open the suggestion in GitLens or [GitKraken Desktop](/gitkraken-client/pull-requests/#review-code-and-suggest-changes).  
3. Review changes file by file.  
4. Choose **Apply** to apply to your current branch, or select **Apply to a Branch** to apply to a new or existing branch.  

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" class="help-center-img img-bordered" alt="Applying a Code Suggestion locally in GitLens" />
  <figcaption style="text-align: center; color: #888">Applying a Code Suggestion locally</figcaption>
</figure>

---

## How to Review and Commit Suggestions in gitkraken.dev

1. Select **Code Suggestion for #PR** to open the suggestion in **gitkraken.dev**.  
2. Review each file and its proposed changes.  
3. When ready, select **Commit Suggestions**.  

This creates a new commit on the remote branch (shown under **COMMIT SUGGESTIONS TO**).

<figure>
  <img src="/wp-content/uploads/gl-accept-code-suggestion.gif" class="help-center-img img-bordered" alt="Accepting and committing Code Suggestions in gitkraken.dev" />
  <figcaption style="text-align: center; color: #888">Committing suggestions in gitkraken.dev</figcaption>
</figure>

---

## Availability

<div class='callout callout--basic'>
  <p><strong>Note:</strong> Code Suggest is currently supported only for repositories on <strong>GitHub.com</strong>.</p>
</div>
