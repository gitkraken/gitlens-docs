---

---
title: GitLens FAQ
description: Frequently asked questions about GitLens and GitKraken account integration.
taxonomy:
  category: gitlens
---

<kbd>Last updated: July 2025</kbd>

Get answers to frequently asked questions about GitLens features, sign-in options, and GitKraken account integration.

***

## What is GitLens Community vs GitLens Pro?

Learn about the differences between the two versions on the [GitLens Community vs GitLens Pro](/gitlens/gitlens-community-vs-gitlens-pro) page.

***

## How Do I Sign In or Out of GitLens?

### Sign In to GitLens

To sign in with your GitKraken account:

- Click the GitLens icon in the sidebar.
- Under **GITKRAKEN ACCOUNT**, select `Sign In`.

<figure>
  <img src="/wp-content/uploads/gl-sign-in-ls-update-01-v2@2x.png" alt="GitLens sidebar with sign-in option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Sign in from the GitLens sidebar</figcaption>
</figure>

You can also sign in via the VS Code Command Palette:

- Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
- Type and select `GitLens: Sign In to GitKraken...`.

<figure>
  <img src="/wp-content/uploads/gl-sign-in-4-01-v2@2x.png" alt="VS Code command palette with sign-in command" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Sign in using the command palette</figcaption>
</figure>

### Sign Out of GitLens

To sign out:

- Click the GitLens icon in the sidebar.
- Under **GITKRAKEN ACCOUNT**, select `Sign Out`.

<figure>
  <img src="/wp-content/uploads/gl-sign-out-ls-update-01-v2@2x.png" alt="GitLens sidebar with sign-out option" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Sign out from the GitLens sidebar</figcaption>
</figure>

Or use the VS Code Command Palette:

- Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
- Type and select `GitLens: Sign Out of GitKraken`.

<figure>
  <img src="/wp-content/uploads/gl-sign-out-4-01-v2@2x.png" alt="VS Code command palette with sign-out command" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888">Sign out using the command palette</figcaption>
</figure>

***

## How do I enable debug logging?

You can enable debug logging by opening the Command Palette (`ctrl+shift+p` or `command+shift+p`) and running the command `GitLens: Enable Debug Logging`.

<img src="/wp-content/uploads/gl-enable-debug-log-01-v2@2x.png" class="help-center-img img-bordered">

To view logs, open the Output Window (View > Output). The logs will be listed in the _GitLens_ and _GitLens (Git)_ channels. These channels can be toggled from the dropdown.

<img src="/wp-content/uploads/gl-output-01-v2@2x.png" class="help-center-img img-bordered">

***

## How can I export logs?

You can export logs using the actions in the overflow menu of the Output view.

<img src="/wp-content/uploads/gl-export-logs-01-v2@2x.png" class="help-center-img img-bordered">

***

## Can GitLens or Visual Studio Code Work with a Proxy?

Yes, you can configure proxy settings from the Visual Studio Code settings. To open these settings, use the keyboard shortcut `command/ctrl + ,`. Then, search for "proxy" to see all related settings.

<img src="/wp-content/uploads/gl-proxy-settings-01-v2@2x.png" class="help-center-img img-bordered">


***

## Does GitLens Support Git Submodules?

Yes. GitLens provides basic Git submodule support, including automatic discovery and tracking of submodules in your workspace. Submodules are distinguished with their own icons in sidebar views, and diffs correctly handle submodule pointer changes. GitLens detects superproject paths and tracks submodule status alongside your main repository.

***

## Can I Use My GitLens Paid License on More Than One Computer?

Yes. Your GitLens Pro license is tied to your email address, not a specific device. You can activate and use GitLens on multiple computers using the same account.
