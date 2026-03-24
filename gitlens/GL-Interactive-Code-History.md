---
title: GitLens Interactive Code History
description: Learn how GitLens helps you explore and understand your repository’s commit history.
product: GitLens
feature: Interactive Code History
content_type: concept
audience: developer
plan_required: all
status: GA
last_verified: 2026-03
taxonomy:
  category: gitlens
---

<kbd>Last updated: March 2026</kbd>

<figure class='embed-container embed-container--16-9'>
  <iframe width='560' height='315' src='https://www.youtube.com/embed/uSc7aQV8uMs?si=7bGXpqRI0lv7k-A0' frameborder='0' allowfullscreen title="GitLens Interactive Code History video overview"></iframe>
</figure>

&nbsp;

GitLens helps users understand code history through Commit Graph, GitLens Inspect, inline blame, and hovers across supported GitLens IDEs. Use this overview when you need to choose the right GitLens history view before investigating authorship, prior changes, or repository context.

Understanding code history in large repositories can be challenging, especially with multiple branches and contributors. GitLens provides tools that surface meaningful context:

- **Commit Graph** – Visualize the structure of your repository.
- **GitLens Inspect** – Drill into file and line-level history.
- **Inline Blame and Hovers** – Quickly see who changed what and when.

These features make it easier to navigate your repository, understand changes, and make informed decisions about your code.

## When to Use Commit Graph

Use Commit Graph when you need repository-wide history, branch relationships, merge context, or a visual view of how work diverged over time.

## When to Use GitLens Inspect

Use GitLens Inspect when you want commit, file, or line details for the code currently in front of you without switching to a repository-wide history view.

## When Inline Blame and Hovers Are Enough

Use Inline Blame and hovers when you only need quick authorship, timing, or commit context for the current line before deciding whether to open a deeper history view.
