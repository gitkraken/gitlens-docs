---
title: GitLens Commit Graph
description: Visualize your repository history, branches, and collaborators with the GitLens Commit Graph in VS Code.
taxonomy:
    category: gitlens

---

<kbd>Last updated: August 2025</kbd>

## Commit Graph <code>PRO</code>

The GitLens Commit Graph provides an interactive view of your repository history. It shows commits, branches, and collaborators in one place, helping you understand contributions and make faster decisions.

<figure>
  <img src="/wp-content/uploads/commit-graph.png" class="help-center-img img-bordered" alt="Commit Graph in GitLens showing branches and commits" />
  <figcaption style="text-align: center; color: #888">Commit Graph overview in GitLens</figcaption>
</figure>

---

### Open the Commit Graph

1. Open the Command Palette:
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
2. Type **Show Commit Graph** and select it.

The Commit Graph opens in a new tab, where you can scroll through history and resize column widths.

<figure>
  <img src="/wp-content/uploads/show-commit-graph.gif" class="help-center-img img-bordered" alt="GIF showing how to open the Commit Graph from the Command Palette" />
  <figcaption style="text-align: center; color: #888">Opening the Commit Graph from the Command Palette</figcaption>
</figure>

---

### Repository Information

At the top of the Commit Graph, you’ll see:

- **Repository name**
- **Checked-out branch** (click to switch branches)
- **Last fetched time** (click **Fetch** to update)

<figure>
  <img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="help-center-img img-bordered" alt="Repository details in the Commit Graph toolbar" />
  <figcaption style="text-align: center; color: #888">Repository details in the Commit Graph toolbar</figcaption>
</figure>

---

### Availability

- The Commit Graph is available to all users for **public** and **local** repositories.
- A **paid GitLens subscription or trial** is required for use with **private repositories**.

---

### Feedback

We’d love your input! Share ideas and feedback in the [GitLens Commit Graph discussion on GitHub](https://github.com/gitkraken/vscode-gitlens/discussions/2158).


### Configuration and Layout

You can configure the Commit Graph to control what information is shown and how it is displayed.

#### Columns
- Drag and drop column headers to rearrange columns.
- Right-click a column header to toggle columns on or off.
- The **Changes** column shows added lines in green and deleted lines in red.

<figure>
  <img src="/wp-content/uploads/gl-column-settings.png" class="help-center-img img-bordered" alt="Commit Graph column settings menu showing toggle options" />
  <figcaption style="text-align: center; color: #888">Commit Graph column settings</figcaption>
</figure>

#### Layout Options
- **Panel Layout**: Displays the Commit Graph in the bottom panel (near the Terminal) with a details view alongside it.
- **Editor Layout**: Opens the Commit Graph in an editor tab.
- You can open the Commit Graph in both layouts simultaneously.

To switch layouts:
1. Select the settings gear in the top-right corner of the Commit Graph editor.
2. Choose **Prefer Commit Graph in Panel Layout** or **Prefer Commit Graph in Editor Area**.

<figure>
  <img src="/wp-content/uploads/gl-prefer-commit-graph-location.png" class="help-center-img img-bordered" alt="Commit Graph layout preference menu" />
  <figcaption style="text-align: center; color: #888">Switching between Editor and Panel Layout</figcaption>
</figure>

#### Compact Graph Layout
- Right-click the **Graph** column header and select **Compact Graph Column Layout** to reduce visual complexity.
- When the **Author** column is resized to minimum width, it shows avatars instead of text.
- Columns that become too narrow automatically switch to icons to preserve information.

<figure>
  <img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="help-center-img img-bordered" alt="Compact Commit Graph layout with icons and avatars" />
  <figcaption style="text-align: center; color: #888">Compact Graph and Author column with avatars</figcaption>
</figure>

#### Scroll Markers
Scroll markers highlight key points in the Commit Graph, including:
- Checked-out branches
- Selected rows
- Search results

Use scroll markers to quickly jump to important points such as `HEAD` or refs. You can toggle this feature in the [Commit Graph settings](/gitlens/gitlens-features/#settings).

<figure>
  <img src="/wp-content/uploads/gl-scroll-markers.png" class="help-center-img img-bordered" alt="Commit Graph scroll markers indicating branch and search results" />
  <figcaption style="text-align: center; color: #888">Scroll markers in the Commit Graph</figcaption>
</figure>

---

### Settings

Adjust Commit Graph settings from the Command Palette:
- macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>
- Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

Search for **GitLens: Open Settings**.

<figure>
  <img src="/wp-content/uploads/commit-graph-settings.png" class="help-center-img img-bordered" alt="Commit Graph settings in VS Code" />
  <figcaption style="text-align: center; color: #888">Opening Commit Graph settings</figcaption>
</figure>

---

### Rich Commit Search

The Commit Graph supports rich search across your entire repository. You can search by commit, message, author, file, or even specific code changes.

#### How to Search
1. Type search criteria in the search bar.
2. Use the arrow icons or keyboard shortcuts to navigate results:
   - Next result: <kbd>F3</kbd> (Windows/Linux) or <kbd>Cmd</kbd> + <kbd>G</kbd> (macOS)
   - Previous result: <kbd>Shift</kbd> + <kbd>F3</kbd> (Windows/Linux) or <kbd>Shift</kbd> + <kbd>Cmd</kbd> + <kbd>G</kbd> (macOS)

<figure>
  <img src="/wp-content/uploads/Rich-Commit-Search.png" class="help-center-img img-bordered" alt="Commit Graph search bar highlighting results" />
  <figcaption style="text-align: center; color: #888">Searching commits in the Commit Graph</figcaption>
</figure>

You can also:
- Jump to the **first or last result** by holding <kbd>Shift</kbd> while clicking the arrow icons.

<figure>
  <img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="help-center-img img-bordered" alt="Navigating commit search results with arrow keys" />
  <figcaption style="text-align: center; color: #888">Navigating commit search results</figcaption>
</figure>

#### Search Filters
Use these filters in the search bar:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me`

Additional options:
- Match all
- Match case
- Use regular expressions

<figure>
  <img src="/wp-content/uploads/search-options.png" class="help-center-img img-bordered" alt="Commit Graph search options for case sensitivity and regex" />
  <figcaption style="text-align: center; color: #888">Commit Graph search options</figcaption>
</figure>

### Full Context Menu Support

You can right-click a branch, commit, tag, author, or column header (Author, Commit Date/Time, or SHA) to access context menu actions.

<figure>
  <img src="/wp-content/uploads/gl-context-menu.gif" class="help-center-img img-bordered" alt="Context menu in Commit Graph with options for branches, commits, and authors" />
  <figcaption style="text-align: center; color: #888">Commit Graph context menu options</figcaption>
</figure>

Helpful context menu actions include:

- **Compare with Common Base**: Review changes that would occur if the selected branch were merged by comparing its common ancestor (merge base) with the current branch.  
- **Open All Changes with Common Base**: Review all merge changes in the multi-diff editor.

---

### Pull Request Information

For GitHub and GitLab, the Commit Graph displays a Pull Request icon for any branch with an open pull request. To enable this, connect a [rich integration](/gitlens/settings/#remote-provider-integration-settings).

<figure>
  <img src="/wp-content/uploads/pull-request-icon.png" class="help-center-img img-bordered" alt="Commit Graph branch showing pull request icon" />
  <figcaption style="text-align: center; color: #888">Pull request icon in Commit Graph</figcaption>
</figure>

---

### Hiding Remotes, Branches, or Tags

The Commit Graph shows refs to your remotes, branches, and tags.  
- Hover over any ref to use the **Hide** option.  
- To show them again, hover over the **Hide** option at the top of the Commit Graph and select the desired refs.

<figure>
  <img src="/wp-content/uploads/gl-hide-refs.gif" class="help-center-img img-bordered" alt="Hiding refs from the Commit Graph view" />
  <figcaption style="text-align: center; color: #888">Hiding refs in the Commit Graph</figcaption>
</figure>

#### Filter Options
Access filters from the dropdown menu to choose:  
- **Show Current Branch Only**: Displays the current branch and its upstream remote.  
- **Show All Local Branches** *(default)*.  

Additional options let you hide or show:  
- Remote-only branches  
- Stashes  
- Tags  

You can also dim merge commit rows for clarity.

<figure>
  <img src="/wp-content/uploads/filter-options-2.png" class="help-center-img img-bordered" alt="Commit Graph filter options for branches, tags, and stashes" />
  <figcaption style="text-align: center; color: #888">Commit Graph filter options</figcaption>
</figure>

---

### Minimap (Experimental)

The Minimap provides a high-level overview of repository activity. It shows commits, branches, HEAD/upstream, and more, letting you quickly jump to points of interest.

- Select the **Toggle Minimap** icon in the Commit Graph toolbar to enable or disable it.  
- Use the graph icon dropdown to switch between **Commits** or **Lines Changed** views.  
- Toggle markers on or off from the same menu.

<figure>
  <img src="/wp-content/uploads/gl-minimap-2.png" class="help-center-img img-bordered" alt="Commit Graph Minimap enabled in the toolbar" />
  <figcaption style="text-align: center; color: #888">Commit Graph Minimap</figcaption>
</figure>

<figure>
  <img src="/wp-content/uploads/gl-minimap-settings.png" class="help-center-img img-bordered" alt="Commit Graph Minimap settings with commits or lines changed options" />
  <figcaption style="text-align: center; color: #888">Minimap settings and options</figcaption>
</figure>

#### Minimap Overview
- **Reads left to right**: Left = most recent, right = older.  
- **Highlighted region**: Area currently in view.  
- **Green lines**: HEAD.  
- **Yellow lines**: Search results.  
- **Upper row markers**:  
  - Blue blocks = remote branches  
  - Brown blocks = tags  
- **Lower row markers**:  
  - Pink blocks = stashes  
  - Blue blocks = local branches  

<div class='callout callout--basic'>
  <p>Note: We’d love your feedback on the Minimap. Please share it on the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>GitHub Discussion board</a>.</p>
</div>