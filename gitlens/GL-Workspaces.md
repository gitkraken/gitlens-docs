---

title: Gitlens Workspaces
description: Explore Workspaces in Gitlens
taxonomy:
    category: gitlens

---


Workspaces are a convenient way to group and manage multiple repositories, making them easily accessible from anywhere. Whether you're working individually or collaborating with a team, Workspaces provide a seamless way to manage your projects. A Workspace can be made up of local repositories, those you currently have open in your VS Code window, or GitKraken Workspaces, which are repositories stored on the cloud or on GitKraken services.

Whether you're working individually or collaborating with a team, these new features are designed to help you work more efficiently and effectively.

To access Workspaces, simply open the GitLens Home menu and you will find them in the panel located at the bottom left. Alternatively, you can access them by performing a search in the command palette.

Please note that while using cloud workspaces requires a GitKraken account, shared cloud workspaces require a trial or subscription.

<img src="/wp-content/uploads/gl-workspaces-sidebar.png" class="help-center-img img-bordered">

### Creating a Workspace

To create a workspace, tap the '+' button next to GitKraken Workspaces, provide a name and a description, and connect a provider if you wish.

<img src="/wp-content/uploads/gl-create-workspace.png" class="help-center-img img-bordered">

### Adding Repositories

You can add repositories to a workspace by tapping the '+' button under the Workspace tab. And if you want to keep your Workspaces and their repositories up-to-date, simply tap the Refresh icon.

<img src="/wp-content/uploads/gl-add-repo-to-workspace.png" class="help-center-img img-bordered">

### Locating Repositories

To locate the disk location of the repositories within the Cloud Workspace, select the 'Locate Repositories' (pin icon) next to the repository name. If you have a folder set up for a Workspace with multiple repositories on your disk, you can select the option and choose the parent folder. GitLens will then find all the repositories within that parent folder.

<img src="/wp-content/uploads/gl-locate-repo-in-workspace.png" class="help-center-img img-bordered">

### Opening Repositories

To open a repository from a Workspace tap the 'Open Repository in New Window' icon.

_Pro Tip: If you prefer to open the Workspace in your current window, hold down the ALT/OPTION key on a Mac and click 'Open Repo'._

<img src="/wp-content/uploads/gl-open-as-vscode-workspace.png" class="help-center-img img-bordered">

### Removing Repositories

To remove a repository from a Workspace, you can do so by right-clicking to open the context menu on the repository you wish to remove and then selecting 'remove repository from Workspace'.

<img src="/wp-content/uploads/gl-remove-repo-from-wrokspace.png" class="help-center-img img-bordered">

### Converting to Cloud Workspaces

To convert your local VSCode workspace into a GitKraken Workspace, press the 'Convert to Cloud Workspace' icon, provide a name and a description, and your workspace will be stored in the cloud for your GitKraken user account. This means that your Cloud Workspace will now appear in any of your GitKraken shared services, such as GitKraken Desktop, GitLens, and the GitKraken CLI.

<img src="/wp-content/uploads/gl-convert-workspace-to-cloud.png" class="help-center-img img-bordered">

### Understanding Workspace indicators and colors

Workspaces also include visual indicators to help you understand their status. For example, a green Workspace with an 'O' symbol indicates that it is open in your current window.

<img src="/wp-content/uploads/gl-workspace-indicators.png" class="help-center-img img-bordered">

### Workspace linking

A VS Code workspace can be created from a GitKraken Workspace to link them.

<img src="/wp-content/uploads/gl-create-vs-workspace-from-gl.png" class="help-center-img img-bordered">

You can open a linked VS Code workspace from its cloud workspace using the new `Open VS Code Workspace in New Window` option (hold alt to open in the current window).

When repositories are added to a GitKraken Cloud workspace, you can automatically add those repositories to its linked VS Code workspace when that workspace is opened. You can choose to automatically add the repositories, be prompted to add them, or disable auto-adding repositories altogether for that workspace. This setting is chosen when creating the VS Code workspace, but can be changed at any time using the new `Change Linked Workspace Auto-Add Behavior` command on the `Current Window` item or its linked workspace in the _Workspaces_ view.

<img src="/wp-content/uploads/gl-link-repositories-in-workspaces.png" class="help-center-img img-bordered">

You can also manually add repositories to the VS Code workspace at any time using the new `Add Repositories from Linked Workspace` command.

***