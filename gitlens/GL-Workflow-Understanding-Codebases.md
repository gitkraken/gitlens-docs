---
title: understanding an Unfamiliar Codebase
description: Use GitLens Git intelligence to gain context, reduce risk, and make confident changes

taxonomy:
  category: gitlens
---

**Level**: New Developers
**Primary Goal:** Use GitLens Git intelligence to gain context, reduce risk, and make confident changes

## When to use this workflow

Use this workflow when you are:

- New to a repository or team

- Modifying code you did not write

- Unsure why certain logic exists

- Looking to understand history, ownership, and intent before making changes

## Real-world scenario

You have been asked to update a function that occasionally breaks production. You did not write it, and you are still learning how the system works.

## How GitLens helps (in practice)

You open the file and immediately start leveraging **GitLens Git intelligence**, which surfaces repository context directly inside your editor. At the top of the function, **CodeLens** appears automatically, showing who last modified the code, when it changed, and how many commits touched it. Clicking the CodeLens opens commit details so you can see the diff and the reasoning behind the change.

<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-codelens.png" class="help-center-img img-bordered" alt="A screenshot of the CodeLens above a function" />
  <figcaption style="text-align: center; color: #888">CodeLens Above a Function</figcaption>
</figure>

As you move through the file, **Inline Blame** appears when you move your cursor to individual lines, revealing the author, commit message, and timestamp for each line of code, and letting you jump straight into the commit that introduced it.

<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-inline-blame.png" class="help-center-img img-bordered" alt="A screenshot of the Inline Blame in VS Code with GitLens also showing the popup when you hover the annotation." />
  <figcaption style="text-align: center; color: #888">Inline Blame Details</figcaption>
</figure>

To understand how this function fits into the broader evolution of the project, you open the **Commit Graph** from the GitLens sidebar, where you can visually trace commits, branches, and merges related to the file.

<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-commit-graph.png" class="help-center-img img-bordered" alt="A screenshot of the GitLens Commit Graph" />
  <figcaption style="text-align: center; color: #888">Commit Graph</figcaption>
</figure>

Before making your change, you open **Launchpad**, which centralizes pull requests, reviews, and branch status, so you can confirm there is no overlapping work that might conflict.

<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-launchpad.png" class="help-center-img img-bordered" alt="A screenshot of the GitLens Launchpad in the sidebar and via the Command Palette" />
  <figcaption style="text-align: center; color: #888">Launchpad</figcaption>
</figure>

Finally, you use **GitKraken AI** from the editor or command palette to explain what the function does and summarize your uncommitted changes, giving you an additional layer of validation before committing.

<!-- Not so sure about this screenshot. Is this actually what we wanted? -->
<figure>
  <img src="/wp-content/uploads/workflows-1-understanding-ai-explain.png" class="help-center-img img-bordered" alt="A screenshot GitKraken AI Explain functionality" />
  <figcaption style="text-align: center; color: #888">GitKraken AI Explain</figcaption>
</figure>

GitLens turns Git history into actionable intelligence, helping you understand not just what the code does, but why it exists.

### Key GitLens features used

- [CodeLens (inline commit and author context)](https://help.gitkraken.com/gitlens/gitlens-features/#git-codelens)

- [Inline Blame (line-level history and intent)](https://help.gitkraken.com/gitlens/gitlens-features/#current-line-blame)

- [Commit Graph (visual repository history)](https://help.gitkraken.com/gitlens/gitlens-features/#commit-graph-pro)

- [Launchpad (PR and branch awareness)](https://help.gitkraken.com/gitlens/gitlens-features/#launchpad-pro)

- [GitKraken AI (explanations and summaries)](https://help.gitkraken.com/gitlens/gitlens-features/#gitkraken-ai)

## Outcome

You make a well-informed change backed by Git intelligence, reducing risk and building confidence in an unfamiliar codebase.
