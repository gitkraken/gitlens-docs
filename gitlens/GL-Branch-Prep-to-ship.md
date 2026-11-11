---

title: Prepare Your Branch to Ship
description: Check where your branch stands, compare it, clean up its commits, rebase, resolve conflicts and review it in the GitLens Commit Graph before you merge.
taxonomy:
    category: gitlens
last_updated: 2026-11

---
<kbd>Last updated: November 2026</kbd>

Use the Commit Graph to get a finished change ready to merge. Upstream changes, messy commit history, overlapping work, and merge conflicts can all stand between your work and a branch that is ready to ship. From the Commit Graph, you can:

- See where your branch stands
- Compare what changed
- Clean up your commits
- Rebase with AI
- Resolve conflicts
- Review the result

## 1. See Where Your Branch Stands
Start in the Commit Graph to see your branch in the context of the repository around it.

The Commit Graph shows HEAD, the upstream, the merge target, incoming work, and the ahead and behind status together, so you can see what has changed and what needs attention before you move forward.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-full-01-v2@2x.png" alt="The Commit Graph in the GitLens side bar: the branch toolbar with Push and Fetch, the natural-language search box, the selected Working Changes row, and commit rows with their branch and tag pills." class="help-center-img img-bordered">
</figure>

When you have no uncommitted changes, the Working Changes details panel shows a **Next steps** list. The list suggests only the actions that apply to your branch right now:

- **Publish**, when the branch has no upstream yet
- **Delete Local Branch**, when the branch's remote branch was deleted, for example after its pull request merged. **Publish** is the alternate action on the same button
- **Publish Repository** or **Add Remote**, when the repository has no remotes yet
- **Pull** or **Push**, when the branch is only behind or only ahead of its upstream
- **Pull** or **Force Push**, when the branch has diverged from its upstream
- **Create PR** when a published branch has no open pull request, or **View** when it has one. If you added commits after the branch's pull request merged, the step reads **Create a Pull Request for N New Commits**
- **Rebase** or **Merge**, when the branch is in sync with its upstream but behind its merge target or likely to conflict with it. Checking for likely conflicts requires a GitLens Pro trial or paid plan; the ahead and behind counts are available to everyone
- **Delete Branch** or **Delete Worktree**, when the branch's work has landed in its merge target, directly or through a merged pull request. The step reads **Branch Merged into** the merge target, and only **Review** can appear beside it
- **Review** and **Recompose**, to review the branch's changes or recompose its commits. **Recompose** is not offered once the branch has landed

A diverged branch shows a step that reads **Diverged from** its remote, followed by how many commits the branch is behind and ahead. **Pull** is the main action for this step. If you want to replace the remote branch with your local commits instead, for example after a rebase, select **Force Push**, the secondary action on the same split button.

## 2. Compare Before You Merge
Before making changes to your branch history, use Compare to understand exactly how your work differs from its target.

<figure>
  <img src="/wp-content/uploads/GL-Graph-Compare.png" alt="The Commit Graph in Compare mode: the Comparing References panel compares origin/main with gitlens-ux-changes, with the Ahead tab of 5 commits selected beside Behind (56) and All Files (165), the Explain box for an AI explanation, and the changed files below." class="help-center-img img-bordered">
</figure>

From the Commit Graph, compare branches, commits, revisions, and working changes to see what you are introducing and find anything that needs another look. The comparison gives you a baseline before you start preparing the branch for merge.

## 3. Clean Up Your Commits
Use Commit Composer to turn working changes into clean, logical commits that are easier to understand and review.

<figure>
  <img src="/wp-content/uploads/gl-graph-compose-01-v3@2x.png" alt="Commit Graph with the Composing Changes panel open beside it: the main branch, an Unstaged changes entry with four files changed (README.md, reports.ts, spending-analysis.ts, user-management.ts) and the Instructions box with the Compose button" class="help-center-img img-bordered">
</figure>

With Compose, you can:

- Group related changes into commits
- Move files between commits
- Reorder and refine work
- Generate commit messages with AI
- Preview the resulting changes before committing

A cleaner commit structure shows reviewers what changed and why.

## 4. Rebase with AI
When upstream work has moved ahead, use Auto-Rebase to bring your branch up to date and prepare its history for merge. Instead of stepping through a traditional interactive rebase by hand, you let GitLens automate the rebase with AI, and you stay in control of the result.

<figure>
  <img src="/wp-content/uploads/GL-Auto-AI-rebase.png" alt="The Resolving Conflicts panel for a rebase paused at 2/173, showing 14 of 14 conflicts resolved: each listed file is labeled Merged, Took Incoming or Kept Current, with a high confidence rating, an explanation and View Changes, above Refine Resolutions and Apply 14 Resolutions." class="help-center-img img-bordered">
</figure>

Auto-Rebase cuts down the repetitive work of updating and cleaning up your branch before it ships.

## 5. Resolve Conflicts

When parallel changes collide, you resolve the conflicts in the same Commit Graph you have used throughout the workflow. AI conflict resolution proposes a resolution for each conflicted file, with an explanation and a confidence rating, so you can understand the competing changes before you accept the result.

<figure>
  <img src="/wp-content/uploads/GL-Conflict-detection-auto-rebase.png" alt="The Commit Graph with a rebase paused at 2/173: the header shows a 14 conflicts badge, and the Working Changes details offer Resolve 14 Conflicts and list the conflicted files, each marked Modified (Both)." class="help-center-img img-bordered">
</figure>

<figure>
  <img src="/wp-content/uploads/GL-Auto-rebase-resolve.png" alt="The Resolving Conflicts panel for a paused rebase, with the 14 conflicted files checked for AI resolution above an optional guidance box and the Resolve button." class="help-center-img img-bordered">
</figure>

You make the final decision, and you can resolve any conflict manually instead.

## 6. Review the Final Changes
After you update your branch and resolve its conflicts, give the resulting changes one final review.
Use [Review Changes](/gitlens/gl-review-changes/) to read each changed file and check it off as viewed. With GitKraken AI, select **Review Diff** to surface findings tagged by severity before you open or update your pull request.

<figure>
  <img src="/wp-content/uploads/gl-graph-review-01-v2@2x.png" alt="Commit Graph in Review mode: the Reviewing Changes panel with Uncommitted and Branch scope presets above the unstaged changes and the unpushed commit, a checklist reading &quot;1 of 3 viewed&quot; with one file checked as viewed and README.md marked excluded, and an instructions box with Review Diff, Orient and Review in Repo." class="help-center-img img-bordered">
</figure>

If something needs another pass, address it yourself or send the findings back to your coding agent with **Address Findings with Agent** before the branch moves forward.

## Workflow Summary

From finished code to a branch that is ready to merge, the Commit Graph covers these steps in order:

**Understand → Compare → Compose → Rebase → Resolve → Review**
