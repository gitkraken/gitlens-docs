---
title: Interface and Customization Features
description: Technical reference for GitLens menus and toolbars, modes and the multi-diff editor, the Welcome view, and display language.
product: GitLens
feature: Interface and Customization
content_type: reference
audience: developer
plan_required: [all]
os_support: [Windows, macOS, Linux]
git_hosts: [n/a]
integrations: []
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [menus, toolbars, modes, multi-diff, welcome-view, display-language]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "Interface and Customization"
    nav_order: 70
    nav_parent: "gitlens-features"
    page_type: "content"
    card_icon: "adjustments-horizontal"
    card_color: "red"
    card_description: "Menus and toolbars, modes, the Welcome view, and display language"
---
<kbd>Last updated: November 2026</kbd>

## Menus & Toolbars

<figure>
  <img src="/wp-content/uploads/gl-menus-01-v2@2x.png" alt="GitLens Visual Settings Editor showing the Menus and Toolbars category, with toggle options controlling where GitLens commands appear in editor menus, context menus, and toolbars" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">GitLens menu and toolbar options</figcaption>
</figure>

You can [customize](/gitlens/gitlens-settings/#menu-and-toolbar-settings) where GitLens commands appear in VS Code menus and toolbars. Manage these settings in the [interactive settings editor](/gitlens/gitlens-settings/).

For example, disabling **Add to the editor group toolbar** removes those items from the toolbar:

<figure>
  <img src="/wp-content/uploads/gl-menus-example-01-v2@2x.png" alt="VS Code editor tab bar with the GitLens editor group toolbar items removed, showing a toolbar without GitLens action buttons" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Editor group toolbar items removed</figcaption>
</figure>

Expand each section to choose individual menus and toolbars.

***

## Modes

GitLens supports [user-defined](/gitlens/gitlens-settings/#modes-settings 'Jump to the Modes settings') modes, so you can switch between sets of settings.

- Shows the active mode in the **status bar** ([optional](/gitlens/gitlens-settings/#modes-settings 'Jump to the Modes settings'), on by default)
- **Switch Mode** (`gitlens.switchMode`) — Switch between modes.
- **Zen Mode** — Turns off many visual elements so you can focus on your code.
  - **Toggle Zen Mode** (`gitlens.toggleZenMode`) — Toggle Zen mode.
- **Review Mode** — Turns on visual elements for code review.
  - **Toggle Review Mode** (`gitlens.toggleReviewMode`) — Toggle Review mode.

### Experimental Multi-diff Editor

VS Code 1.86 or later is required for these capabilities.

#### Commands using Multi-diff

- **Open Folder Changes with Revision...** and **Open Folder Changes with Branch or Tag...** via Command Palette, Explorer, and Source Control views.
- Inline **Open All Changes** in commits, stashes, and comparison views.
- **Open All Changes** and **Open All Changes with Working Tree** — Open the changes in the multi-diff editor.
- **Open All Changes, Individually** and **Open All Changes with Working Tree, Individually** — Open each file's changes in its own diff editor.

***

## Welcome View

Use the **Welcome** side bar view to get started with GitLens. Its guided walkthrough covers getting started with GitLens, the Commit Graph, AI features, Git Blame, Launchpad and worktrees, Kepler for agent workflows, and the GitKraken MCP server. The getting-started content depends on your plan. Select **Get Started with the Commit Graph →** for a second walkthrough of the graph's agent monitoring, parallel work, Review, Compose, and Compare features.

Open it from the GitLens side bar. VS Code's **Get Started** walkthrough for GitLens and the Launchpad's learn-more links also open the Welcome view.

***

## Display Language

GitLens follows the VS Code display language. Experimental Spanish, Simplified Chinese, and Traditional Chinese translations are available, and any text that is not translated yet appears in English. GitLens has no separate language setting.

To switch languages, install Microsoft's language pack for that language, run **Configure Display Language** from the Command Palette, choose the language, and restart VS Code. The `gitlens.defaultDateLocale` setting still controls only how dates are formatted.
