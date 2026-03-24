---
title: GitLens Visual File History
description: Use GitLens Visual File History to explore file evolution, changes, and authorship across supported GitLens IDEs.
product: GitLens
feature: Visual File History
content_type: reference
audience: developer
plan_required: all
status: GA
last_verified: 2026-03
taxonomy:
    category: gitlens

---

<kbd>Last updated: March 2026</kbd>

## Visual File History

GitLens Visual File History helps GitLens users inspect how one file changed over time, including authorship, change size, and sequence. Use it when you need file-scoped history; use Commit Graph when you need repository-wide branch and commit relationships.

---

### How to Open Visual File History

You can open the Visual File History view in two ways:

1. From the **GitLens Inspect** sidebar.  
   - Open the sidebar, then select the **Visual File History** view.  
2. From the **Command Palette**:  
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Search for **GitLens: Show Visual File History View**.

<figure>
  <img src="/wp-content/uploads/visual-file-history.png" class="help-center-img img-bordered" alt="Visual File History view in GitLens showing commits plotted by author and time" />
  <figcaption style="text-align: center; color: #888">Visual File History view</figcaption>
</figure>

---

### How to Read the Visual File History Graph

- **Authors (y-axis, left):** Each author is shown in a swimlane, mapping their commits over time.  
- **Commits:** Plotted as color-coded bubbles by author. Bubble size represents the relative magnitude of changes.  
- **Changes (y-axis, right):** Each commit’s additions and deletions are shown as stacked vertical bars.  
  - Green = added lines  
  - Red = deleted lines  

<figure>
  <img src="/wp-content/uploads/visual-file-history-hover.png" class="help-center-img img-bordered" alt="Hover details in Visual File History showing commit metadata and changes" />
  <figcaption style="text-align: center; color: #888">Commit details on hover</figcaption>
</figure>

---

### How to Inspect Commit Details on Hover

Hover over any commit bubble or bar to see details about:  
- Author  
- Commit message  
- Number of additions and deletions  

---

### Availability

<div class='callout callout--warning'>
  <p>The Community plan supports <strong>Public</strong> and <strong>Local</strong> repositories only. A paid GitLens subscription is required for private repositories.</p>
</div>
