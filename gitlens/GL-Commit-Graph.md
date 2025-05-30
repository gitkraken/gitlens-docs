---

title: Gitlens Commit Graph
description: Learn about the Commit Graph in Gitlens
taxonomy:
    category: gitlens

---

## Commit Graph `PRO`

The commit graph helps visualize your repository commit history and give you information about branches, commits, and collaborators all in one view. This makes it easier to see contributions and help you make faster, more informed decisions.

<img src="/wp-content/uploads/commit-graph.png" class="help-center-img img-bordered">

To open the Commit Graph, open the command palette using the keyboard shortcut `Cmd/ctrl + Shift + P` and type “Show Commit Graph”. This will open a new tab and render your current repo’s commit history, where you may scroll through your history and resize any of the columns widths.

<img src="/wp-content/uploads/show-commit-graph.gif" class="help-center-img img-bordered">

At the top of the commit graph the repository name, the branch name that is currently checked out, and the last fetched time is shown. This section offers the ability to switch branches by selecting the branch name and the ability to fetch by selecting "Fetch".

<img src="/wp-content/uploads/graph-info.png" srcset="/wp-content/uploads/graph-info@2x.png" class="help-center-img img-bordered">

<div class='callout callout--basic'>
    <p>Note: The Commit Graph is available to all users working on public or local repositories, and requires no account. Additionally, users with a paid GitLens subscription or trial can use the Commit Graph with private repos. </br></br>

    We’d love to hear your feedback in the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2158' target='_blank'>Commit Graph discussion on GitHub</a>.</p>
</div>

### Configuration and Layout

The commit graph can be configured to be shown as desired offering different settings for what to show and how or where to show it.

All columns can be rearranged by dragging and dropping the column headers. The columns can be toggled on/off from the column's context menu via right-click. This enables you to arrange the columns in a way that best suits your workflow and priorities. The Changes column represents added (green) and deleted (red) lines made to each file within the commit.

<img src="/wp-content/uploads/gl-column-settings.png" class="help-center-img img-bordered">

A Commit Graph Panel Layout is offered to show the Commit Graph in the bottom Panel (near the Terminal) with a dedicated Commit Graph Details view alongside the Commit Graph. To switch between the Editor Layout and Panel Layout, select the Commit Graph settings gear located at the top right of the editor. From there, select the "Prefer Commit Graph in Panel Layout" or "Prefer Commit Graph in Editor Area". The Commit Graph can also be opened in both the Penel Layout and Editor Area simultaneously. 

<img src="/wp-content/uploads/gl-prefer-commit-graph-location.png" class="help-center-img img-bordered">

A compact layout for the Graph column is offered in the Commit Graph to reduce the visual complexity and size of the Graph column. To enable the compact layout, right click on the Graph column header, and select the Compact Graph Column Layout option. Additionally the Author column displays avatars instead of text when sized to its minimum width, which pairs nicely with the compact Graph column as you can retain avatars. Also, when the any of the Commit Graph columns are resized small enough so that their text would be truncated, they switch to displaying icons to ensure that crucial information remains visible, even in constrained display settings.

<img src="/wp-content/uploads/gl-commit-graph-compact-graph.gif" class="help-center-img img-bordered">

The scroll markers indicate points of interest on the commit graph such as checked-out branches, selected rows, and search results. This provides the ability to jump to important points like the HEAD or refs. This can be toggled on or off in the [Commit Graph settings](/gitlens/gitlens-features/#settings).

<img src="/wp-content/uploads/gl-scroll-markers.png" class="help-center-img img-bordered">

### Settings

The Commit Graph settings can be adjusted by opening the Command Palette (`command/ctrl + shift + P`) and searching "GitLens: Open Settings".

<img src="/wp-content/uploads/commit-graph-settings.png" class="help-center-img img-bordered">

### Rich Commit Search

The Commit Graph will highlight all matching results across your entire repository when searching for a commit, message, author, a changed file or files, or even a specific code change. Use shortcut keys or the up/down arrows on the search bar  to navigate the search results; `F3` (also `Cmd+G` on macOS) goes to the next result from your selection while  `Shift+F3`  ( also `Shift+Cmd+G` on macOS) goes to the previous.

<img src="/wp-content/uploads/Rich-Commit-Search.png" class="img-responsive center img-bordered">

Once you type search filtering criteria, use the arrow icons to move through each result. Additionally, you can quickly jump to the first or last result, by holding `Shift` while clicking on the up/down arrows respectively.

<img src="/wp-content/uploads/Commit-Search-Moving-Arrow-Keys.gif" class="img-responsive center img-bordered">

The following options can be used to search:
- `Commit:`
- `Message:`
- `Author:`
- `File:`
- `Change:`
- `@me`

Additionally, the options on the right side of the search bar can be used to match all, match case, or use regular expression.

<img src="/wp-content/uploads/search-options.png" class="help-center-img img-bordered">

### Full Context Menu Support

You can right-click a branch, commit, tag, author, or column headers (author, commit date / time, or SHA) to interact with them.

<img src="/wp-content/uploads/gl-context-menu.gif" class="help-center-img img-bordered">

Helpful context menu actions: 

- _Compare with Common Base_: to review the changes if the selected branch were to be merged by comparing the common ancestor (merge base) with the current branch to the selected branch
- _Open All Changes with Common Base_: to review the changes if the selected branch were to be merged in the multi-diff editor

### Pull Request Information

For GitHub and GitLab, the commit Graph will display a Pull Request icon for any branch that currently has a pull request. You will need to connect the [rich integration](/gitlens/settings/#remote-provider-integration-settings) in order to see this.

<img src="/wp-content/uploads/pull-request-icon.png" class="help-center-img img-bordered">

### Hiding Remotes, Branches or Tags

The Commit Graph shows refs to your remotes, branches and tags. Hover over any of these refs to access the “Hide” option to help focus your Commit Graph. To show them again, hover over the "Hide" option at the top of the commit graph and select the desired refs.

<img src="/wp-content/uploads/gl-hide-refs.gif" class="help-center-img img-bordered">

Filter options can be accessed from the filter dropdown. This provides the ability to switch between _Show Current Branch Only_ - to show the current branch and its upstream remote - or _Show All Local Branches_ - this is selected by default. Additionally, remote-only branches, stashes and tags can be hidden/shown and merge commit rows can be dimmed.

<img src="/wp-content/uploads/filter-options-2.png" class="help-center-img img-bordered">

### Minimap (Experimental)

The Minimap provides an additional dimension to the Commit Graph. You can quickly see the activity of the repository, see the HEAD/upstream, branches (local and remote), and easily jump to them. Select the Toggle Minimap icon in the right corner of the Commit Graph top bar to toggle the Minimap on and off.

<img src="/wp-content/uploads/gl-minimap-2.png" class="help-center-img img-bordered">

The Minimap can be toggled between showing commits or lines changed by selecting the graph icon dropdown in the top right of the Activity Minimap. Additionally, markers can be toggled on or off from here.

<img src="/wp-content/uploads/gl-minimap-settings.png" class="help-center-img img-bordered">

Minimap Overview:

- Reads left to right - left is the most recent and the right is older
- Highlighted region: Commit Graph area that is in view
- Green Lines: HEAD
- Yellow lines: Search results
- Upper row markers:
    - Blue blocks: remote branches
    - Brown blocks: Tags
- Lower row markers:
    - Pink blocks: stashes
    - Blue blocks: local branches

<div class='callout callout--basic'>
    <p>Note: We would love to hear your feedback regarding the Minimap. Please share it on the <a href='https://github.com/gitkraken/vscode-gitlens/discussions/2477#discussion-4807133' target='_blank'>GitHub Discussion board</a>.</p>
</div>

***
