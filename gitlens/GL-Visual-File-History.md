---
title: GitLens Visual File History
description: Use GitLens Visual File History to explore file evolution, changes, and authorship over time in VS Code.
taxonomy:
    category: gitlens

---

<kbd>Last updated: August 2025</kbd>

## Visual File History

The GitLens **Visual File History** shows how a file has evolved, including when changes were made, the size of those changes, and who made them.

---

### Open Visual File History

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

### Understand the Graph

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

### Gain Insights on Hover

Hover over any commit bubble or bar to see details about:  
- Author  
- Commit message  
- Number of additions and deletions  

---

### Availability

<div class='callout callout--warning'>
  <p>The Community plan supports <strong>Public</strong> and <strong>Local</strong> repositories only. A paid GitLens subscription is required for private repositories.</p>
</div>