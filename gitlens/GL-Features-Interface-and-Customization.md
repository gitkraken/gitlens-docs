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

GitLens provides [customizable](/gitlens/gitlens-settings/#menu-and-toolbar-settings) menu and toolbar contributions to let you control where GitLens commands appear. You can easily manage these settings via the [interactive settings editor](/gitlens/gitlens-settings/).

For example, disabling **Add to the editor group toolbar** removes those items from the toolbar:

<figure>
  <img src="/wp-content/uploads/gl-menus-example-01-v2@2x.png" alt="VS Code editor tab bar with the GitLens editor group toolbar items removed, showing a toolbar without GitLens action buttons" class="help-center-img img-bordered">
  <figcaption style="text-align: center; color: #888;">Editor group toolbar items removed</figcaption>
</figure>

You can also expand each section to customize visibility and placement more granularly.

***

## Modes

GitLens supports [user-defined](/gitlens/gitlens-settings/#modes-settings 'Jump to the Modes settings') modes for quickly toggling between sets of settings.

- Shows the active mode in the **status bar** ([optional](/gitlens/gitlens-settings/#modes-settings 'Jump to the Modes settings'), enabled by default)
  - **Toggle Review Mode** (`gitlens.toggleReviewMode`) — Quickly toggle Review mode.
- **Switch Mode** (`gitlens.switchMode`) — Quickly switch between modes.
- **Zen Mode** — Disables many visual elements for a focused experience.
  - **Toggle Zen Mode** (`gitlens.toggleZenMode`) — Toggle Zen mode.
- **Review Mode** — Enables visual elements for code review.

### Experimental Multi-diff Editor

VS Code 1.86 or later is required for these capabilities.

#### Commands using Multi-diff

- **Open Folder Changes with Revision...** and **Open Folder Changes with Branch or Tag...** via Command Palette, Explorer, and Source Control views.
- Inline **Open All Changes** in commits, stashes, and comparison views.
- **Open All Changes** and **Open All Changes with Working Tree** — Use the new multi-diff editor.
- **Open All Changes, Individually** and **Open All Changes with Working Tree, Individually** — Provide legacy behavior.

***

## Welcome View

The **Welcome** sidebar view is the place to get started with GitLens. Its guided walkthrough covers getting started with GitLens, the Commit Graph, AI features, Git Blame, Launchpad and worktrees, Kepler for agent workflows, and the GitKraken MCP server. The getting-started content adapts based on your subscription level. Select **Get Started with the Commit Graph →** for a second walkthrough of the graph's agent monitoring, parallel work, Review, Compose, and Compare features.

Open it from the GitLens sidebar. VS Code's **Get Started** walkthrough for GitLens and the Launchpad's learn-more links also open the Welcome view.

***

## Display Language

GitLens follows the VS Code display language. Experimental Spanish, Simplified Chinese, and Traditional Chinese translations are available, and any text that isn't translated yet appears in English. GitLens has no separate language setting.

To switch languages, install Microsoft's language pack for that language, run **Configure Display Language** from the Command Palette, choose the language, and restart VS Code. The `gitlens.defaultDateLocale` setting still controls only how dates are formatted.
