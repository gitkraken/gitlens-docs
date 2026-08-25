---
title: GitLens Visual File History
description: Use GitLens Visual File History to explore file evolution, changes, and authorship over time in VS Code.
taxonomy:
    category: gitlens

---

<kbd>Last updated: August 2025</kbd>

## Visual History

The GitLens **Visual History** (formerly Visual File History) shows how your code has evolved, including when changes were made, the size of those changes, and who made them. Visual History supports multiple scopes: view the history of a single file, a folder, an entire repository, or a specific branch.

---

### Open Visual History

You can open the Visual History view in two ways:

1. From the **GitLens Inspect** sidebar.  
   - Open the sidebar, then select the **Visual History** view.  
2. From the **Command Palette**:  
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Search for **GitLens: Show Visual History View**.

### Scope Options

- **File or Folder**: Visualize the history of a specific file or folder
- **Repository**: See the full history of your entire repository
- **Branch**: Slice history by branch to focus on a specific line of work

<figure>
  <img src="/wp-content/uploads/visual-file-history.png" class="help-center-img img-bordered" alt="Visual History view in GitLens showing commits plotted by author and time" />
  <figcaption style="text-align: center; color: #888">Visual History view</figcaption>
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