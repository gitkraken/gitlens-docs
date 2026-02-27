---
title: Manage Multiple Repositories with GitLens Workspaces
description: Learn how to create and use Workspaces in GitLens to organize your repositories
taxonomy:
    category: gitlens
---

<kbd>Last updated: February 2026</kbd>

Workspaces in GitLens help you organize and manage multiple repositories from one convenient interface. Whether you're working solo or collaborating with a team, Workspaces simplify project access and context switching.

A Workspace can include:
- **Local repositories**: The ones currently open in your VS Code window.
- **Cloud Workspaces**: Hosted by GitKraken and accessible anywhere (GitKraken account required).

> 💡 **Note:** Shared cloud Workspaces require a GitKraken trial or subscription.

### Accessing Workspaces

You can open your Workspaces in two ways:

1. Click the **GitLens Home** icon in the Activity Bar.
2. Use the Command Palette (`Cmd+Shift+P` or `Ctrl+Shift+P`) and search for `GitLens: Open Workspaces`.

<figure>
  <img src="/wp-content/uploads/gl-workspaces-sidebar.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Workspaces section in the GitLens Home panel</figcaption>
</figure>

### Creating a Workspace

To create a new GitLens Workspace:

1. In the GitLens Home panel, click the **+** button next to **GitKraken Workspaces**.
2. Enter a **name** and an optional **description**.
3. (Optional) Connect a Git provider (such as GitHub or GitLab) to link repositories.

<figure>
  <img src="/wp-content/uploads/gl-create-workspace.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create Workspace dialog with name, description, and provider options</figcaption>
</figure>

### Adding Repositories

To add repositories to a Workspace:

1. Click the **+** button under the **Workspace** tab.
2. To sync repository status, click the **Refresh** icon.

<figure>
  <img src="/wp-content/uploads/gl-add-repo-to-workspace.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Add repositories to your Workspace</figcaption>
</figure>

### Locating Repositories

To find the disk location of a repository in a Cloud Workspace:

1. Click the **Locate Repositories** (pin icon) next to the repository name.
2. If you have a folder with multiple repositories, select the parent folder. GitLens will detect and associate all repositories within it.

<figure>
  <img src="/wp-content/uploads/gl-locate-repo-in-workspace.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Locate local disk path of repositories in your Workspace</figcaption>
</figure>

### Opening Repositories

To open a repository from a Workspace:

- Click the **Open Repository in New Window** icon.
- _Pro Tip:_ To open the repository in the **current window**, hold the **Alt/Option** key (Mac) while clicking **Open Repo**.

<figure>
  <img src="/wp-content/uploads/gl-open-as-vscode-workspace.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Open repositories from a Workspace in VS Code</figcaption>
</figure>

### Removing Repositories

To remove a repository from a Workspace:

1. Right-click the repository.
2. Select **Remove repository from Workspace** from the context menu.

<figure>
  <img src="/wp-content/uploads/gl-remove-repo-from-wrokspace.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Remove repositories from a Workspace</figcaption>
</figure>

### Converting to Cloud Workspaces

To convert a local VS Code workspace into a GitKraken Cloud Workspace:

1. Click the **Convert to Cloud Workspace** icon.
2. Enter a **name** and **description**.

Your Cloud Workspace will be synced to your GitKraken account and accessible via GitKraken Desktop, GitLens, and the GitKraken CLI.

<figure>
  <img src="/wp-content/uploads/gl-convert-workspace-to-cloud.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Convert local Workspace to GitKraken Cloud Workspace</figcaption>
</figure>

### Understanding Workspace Indicators and Colors

Visual indicators in Workspaces help you quickly understand their status. For example:
- A **green Workspace** with an **O** symbol indicates it is open in your current window.

<figure>
  <img src="/wp-content/uploads/gl-workspace-indicators.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Workspace status indicators</figcaption>
</figure>

### Workspace Linking

You can link a VS Code workspace to a GitKraken Workspace:

1. Create a VS Code workspace from an existing GitKraken Cloud Workspace.
2. Use the **Open VS Code Workspace in New Window** option (hold **Alt** to open in the current window).

<figure>
  <img src="/wp-content/uploads/gl-create-vs-workspace-from-gl.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Create a VS Code workspace from a GitKraken Workspace</figcaption>
</figure>

When opening a linked workspace, you can choose how to handle repository auto-adding:
- Automatically add repositories
- Prompt before adding
- Disable auto-adding

This behavior is configurable during setup or later via the `Change Linked Workspace Auto-Add Behavior` command.

To manually sync repositories:
- Use the `Add Repositories from Linked Workspace` command at any time.

<figure>
  <img src="/wp-content/uploads/gl-link-repositories-in-workspaces.png" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Manage repository linking for VS Code and GitKraken Workspaces</figcaption>
</figure>

