---
title: GitLens Features
description: Index of the GitLens feature reference pages, by feature type, with a map of where each former All Features section now lives.
product: GitLens
feature: All Features
content_type: overview
audience: developer
plan_required: [Community]
os_support: [Windows, macOS, Linux]
git_hosts: [generic]
integrations: [github, github-enterprise, gitlab, gitlab-self-managed, bitbucket, bitbucket-data-center, azure-devops, azure-devops-server, jira, jira-data-center, linear, trello, claude-code, codex, copilot-cli, opencode]
hosted_variant: both
status: GA
last_verified: 2026-11
llms_include: true
tags: [features, blame, codelens, commit-graph, launchpad, gitkraken-ai, rebase-editor, autolinks]
taxonomy:
  category: gitlens
last_updated: 2026-11
custom_fields:
    nav_category: "gitlens-features"
    nav_label: "All Features"
    nav_order: 90
    nav_parent: ""
    page_type: "index"
    card_icon: "list-details"
    card_color: "red"
    card_description: "Technical reference for every GitLens feature, by feature type"
    anchor_map:
        - "revision-navigation|gl-features-blame-and-annotations#revision-navigation"
        - "current-line-blame|gl-features-blame-and-annotations#current-line-blame"
        - "git-codelens|gl-features-blame-and-annotations#git-codelens"
        - "codelens-types|gl-features-blame-and-annotations#codelens-types"
        - "codelens-behavior|gl-features-blame-and-annotations#codelens-behavior"
        - "related-command|gl-features-blame-and-annotations#related-command"
        - "status-bar-blame|gl-features-blame-and-annotations#status-bar-blame"
        - "default-behavior|gl-features-blame-and-annotations#default-behavior"
        - "customizable-click-behavior|gl-features-blame-and-annotations#customizable-click-behavior"
        - "hovers|gl-features-blame-and-annotations#hovers"
        - "current-line-hovers|gl-features-blame-and-annotations#current-line-hovers"
        - "details-hover|gl-features-blame-and-annotations#details-hover"
        - "changes-diff-hover|gl-features-blame-and-annotations#changes-diff-hover"
        - "annotation-hovers|gl-features-blame-and-annotations#annotation-hovers"
        - "file-blame|gl-features-blame-and-annotations#file-blame"
        - "features|gl-features-blame-and-annotations#features"
        - "file-changes|gl-features-blame-and-annotations#file-changes"
        - "file-heatmap|gl-features-blame-and-annotations#file-heatmap"
        - "code-suggest-preview|gl-features-pull-requests-and-collaboration#code-suggest"
        - "how-to-create-a-code-suggestion|gl-features-pull-requests-and-collaboration#how-to-create-a-code-suggestion"
        - "accepting-a-suggestion-locally|gl-features-pull-requests-and-collaboration#accepting-a-suggestion-locally"
        - "accepting-a-suggestion-on-gitkraken-dev|gl-features-pull-requests-and-collaboration#accepting-a-suggestion-on-gitkraken-dev"
        - "cloud-patches-preview|gl-features-pull-requests-and-collaboration#cloud-patches-preview"
        - "what-are-cloud-patches-and-why-use-them|gl-features-pull-requests-and-collaboration#what-are-cloud-patches-and-why-use-them"
        - "how-to-set-up-cloud-patches|gl-features-pull-requests-and-collaboration#how-to-set-up-cloud-patches"
        - "how-to-work-with-cloud-patches|gl-features-pull-requests-and-collaboration#how-to-work-with-cloud-patches"
        - "sharing-options|gl-features-pull-requests-and-collaboration#sharing-options"
        - "self-hosting-cloud-patch-data|gl-features-pull-requests-and-collaboration#self-hosting-cloud-patch-data"
        - "commit-graph|gl-features-commit-graph-and-history#commit-graph"
        - "how-to-open-the-commit-graph|gl-features-commit-graph-and-history#how-to-open-the-commit-graph"
        - "commit-graph-header|gl-features-commit-graph-and-history#commit-graph-header"
        - "scope-the-graph-to-a-worktree|gl-features-commit-graph-and-history#scope-the-graph-to-a-worktree"
        - "follow-the-active-terminal|gl-features-commit-graph-and-history#follow-the-active-terminal"
        - "configuration-and-layout|gl-features-commit-graph-and-history#configuration-and-layout"
        - "column-customization|gl-features-commit-graph-and-history#column-customization"
        - "panel-vs-editor-layout|gl-features-commit-graph-and-history#panel-vs-editor-layout"
        - "compact-layout|gl-features-commit-graph-and-history#compact-layout"
        - "scroll-markers|gl-features-commit-graph-and-history#scroll-markers"
        - "settings|gl-features-commit-graph-and-history#settings"
        - "repository-health|gl-features-commit-graph-and-history#repository-health"
        - "rich-commit-search|gl-features-commit-graph-and-history#rich-commit-search"
        - "natural-language-search-pro|gl-features-commit-graph-and-history#natural-language-search-pro"
        - "search-prefixes|gl-features-commit-graph-and-history#search-prefixes"
        - "full-context-menu-support|gl-features-commit-graph-and-history#full-context-menu-support"
        - "compare-mode-pro|gl-features-commit-graph-and-history#compare-mode-pro"
        - "compose-mode-pro|gl-features-commit-graph-and-history#compose-mode-pro"
        - "multi-file-selection|gl-features-commit-graph-and-history#multi-file-selection"
        - "pull-request-indicators|gl-features-commit-graph-and-history#pull-request-indicators"
        - "hiding-remotes-branches-or-tags|gl-features-commit-graph-and-history#hiding-remotes-branches-or-tags"
        - "filtering-options|gl-features-commit-graph-and-history#filtering-options"
        - "minimap-experimental|gl-features-commit-graph-and-history#minimap"
        - "minimap-settings|gl-features-commit-graph-and-history#minimap-settings"
        - "minimap-legend|gl-features-commit-graph-and-history#minimap-legend"
        - "launchpad-pro|gl-features-pull-requests-and-collaboration#launchpad-pro"
        - "accessing-launchpad|gl-features-pull-requests-and-collaboration#accessing-launchpad"
        - "using-launchpad|gl-features-pull-requests-and-collaboration#using-launchpad"
        - "start-review-pro|gl-features-pull-requests-and-collaboration#start-review-pro"
        - "start-work-pro|gl-features-pull-requests-and-collaboration#start-work-pro"
        - "pin-or-snooze-prs|gl-features-pull-requests-and-collaboration#pin-or-snooze-prs"
        - "visual-history|gl-features-commit-graph-and-history#visual-history"
        - "how-to-read-the-graph|gl-features-commit-graph-and-history#how-to-read-the-graph"
        - "gitkraken-ai|gl-features-ai-and-agents#gitkraken-ai"
        - "ai-generated-commit-messages|gl-features-ai-and-agents#ai-generated-commit-messages-pro"
        - "ai-stash-messages-pro|gl-features-ai-and-agents#ai-stash-messages-pro"
        - "ai-explanations-preview|gl-features-ai-and-agents#ai-explanations"
        - "ai-commit-explanations-pro|gl-features-ai-and-agents#ai-commit-explanations-pro"
        - "ai-changelog-creation-advanced|gl-features-ai-and-agents#ai-changelog-creation-pro"
        - "ai-changelog-creation-pro|gl-features-ai-and-agents#ai-changelog-creation-pro"
        - "ai-commit-composition-pro|gl-features-ai-and-agents#ai-commit-composition-pro"
        - "ai-generate-commits-pro|gl-features-ai-and-agents#ai-commit-composition-pro"
        - "ai-rebase-pro|gl-features-ai-and-agents#ai-commit-composition-pro"
        - "auto-rebase-pro|gl-features-ai-and-agents#auto-rebase-pro"
        - "commit-composer-view-pro|gl-features-ai-and-agents#commit-composer-view-pro"
        - "interactive-draft-commits|gl-features-ai-and-agents#interactive-draft-commits"
        - "commit-composer-branch-recomposition|gl-features-ai-and-agents#commit-composer-branch-recomposition"
        - "recompose-entire-branches|gl-features-ai-and-agents#recompose-entire-branches"
        - "enhanced-composer-capabilities|gl-features-ai-and-agents#enhanced-composer-capabilities"
        - "commit-composer-selective-recomposition|gl-features-ai-and-agents#commit-composer-selective-recomposition"
        - "compose-and-recompose-commands|gl-features-ai-and-agents#compose-and-recompose-commands"
        - "git-command-palette|gl-features-git-commands-and-rebase#git-command-palette"
        - "quick-commit-access|gl-features-git-commands-and-rebase#quick-commit-access"
        - "quick-stash-access|gl-features-git-commands-and-rebase#quick-stash-access"
        - "quick-status-access|gl-features-git-commands-and-rebase#quick-status-access"
        - "interactive-rebase-editor|gl-features-git-commands-and-rebase#interactive-rebase-editor"
        - "start-or-continue-with-auto-rebase-pro|gl-features-git-commands-and-rebase#start-or-continue-with-auto-rebase-pro"
        - "conflict-detection|gl-features-git-commands-and-rebase#conflict-detection"
        - "rebase-editor-settings|gl-features-git-commands-and-rebase#rebase-editor-settings"
        - "conflict-resolution-actions|gl-features-git-commands-and-rebase#conflict-resolution-actions"
        - "use-the-rebase-editor-from-the-terminal|gl-features-git-commands-and-rebase#use-the-rebase-editor-from-the-terminal"
        - "to-use-this-directly-from-your-terminal-e-g-when-running-git-rebase-i|gl-features-git-commands-and-rebase#use-the-rebase-editor-from-the-terminal"
        - "commit-signature-verification-pro|gl-features-git-commands-and-rebase#commit-signature-verification-pro"
        - "verification-badges|gl-features-git-commands-and-rebase#verification-badges"
        - "allowed-signers-management|gl-features-git-commands-and-rebase#allowed-signers-management"
        - "autolinks|gl-features-integrations-and-links#autolinks"
        - "terminal-links|gl-features-integrations-and-links#terminal-links"
        - "remote-provider-integrations|gl-features-integrations-and-links#remote-provider-integrations"
        - "connecting-the-github-and-gitlab-integration|gl-features-integrations-and-links#connecting-the-github-and-gitlab-integration"
        - "github-enterprise-server-and-gitlab-self-managed-integration-pro|gl-features-integrations-and-links#github-enterprise-server-and-gitlab-self-managed-integration-pro"
        - "connecting-github-enterprise-server-or-gitlab-self-managed|gl-features-integrations-and-links#connecting-github-enterprise-server-or-gitlab-self-managed"
        - "jira-integration-pro|gl-features-integrations-and-links#jira-integration-pro"
        - "powerful-commands|gl-features-git-commands-and-rebase#powerful-commands"
        - "deep-links|gl-features-integrations-and-links#deep-links"
        - "git-submodule-support|gl-features-git-commands-and-rebase#git-submodule-support"
        - "commit-file-details-in-large-histories|gl-features-commit-graph-and-history#commit-file-details-in-large-histories"
        - "display-language|gl-features-interface-and-customization#display-language"
        - "welcome-view|gl-features-interface-and-customization#welcome-view"
        - "ai-agent-integration-pro|gl-features-ai-and-agents#ai-agent-integration"
        - "supported-agents|gl-features-ai-and-agents#supported-agents"
        - "agent-hooks|gl-features-ai-and-agents#agent-hooks"
        - "agent-sessions|gl-features-ai-and-agents#agent-sessions"
        - "mcp-server-management|gl-features-ai-and-agents#mcp-server-management"
        - "menus-toolbars|gl-features-interface-and-customization#menus-toolbars"
        - "modes|gl-features-interface-and-customization#modes"
        - "experimental-multi-diff-editor|gl-features-interface-and-customization#experimental-multi-diff-editor"
        - "commands-using-multi-diff|gl-features-interface-and-customization#commands-using-multi-diff"
---
<kbd>Last updated: November 2026</kbd>

The GitLens feature reference is split by feature type. Each page below holds the technical details for its features: commands, settings, and options. For workflows and examples, see the feature pages under **Popular Features** and **AI in GitLens** in the navigation.

---

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

Features marked with <span style="color: #888;">`PREVIEW`</span> require a GitKraken Account, with access based on your [plan level](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens), such as Community or Pro.
