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
    page_type: "content"
---
<kbd>Last updated: November 2026</kbd>

Features marked with <span style="color: #888;">`PRO`</span> require a [trial or paid plan](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) for use on privately hosted repositories.

Features marked with <span style="color: #888;">`PREVIEW`</span> require a GitKraken Account, with access based on your [plan level](https://www.gitkraken.com/gitlens/pricing?source=help_center&product=gitlens) (Community, Pro, etc).

***

## Feature Reference Pages

The GitLens feature reference is split by feature type. Each page below holds the technical details for its features: commands, settings, and options. For workflows and examples, see the feature pages under **Popular Features** and **AI in GitLens** in the navigation.

- **[Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/)**: The Commit Graph, its layout, search and filters, Visual History, and large-history performance.
- **[Blame and Annotations](/gitlens/gl-features-blame-and-annotations/)**: Revision navigation, inline and status bar blame, CodeLens, hovers, and file annotations.
- **[Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/)**: Launchpad, Start Review and Start Work, Code Suggest, and Cloud Patches.
- **[AI and Agents](/gitlens/gl-features-ai-and-agents/)**: GitKraken AI features, Auto-Rebase, the Commit Composer, and AI agent integration.
- **[Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/)**: The Git Command Palette, powerful commands, the Interactive Rebase Editor, signature verification, and submodules.
- **[Integrations and Links](/gitlens/gl-features-integrations-and-links/)**: Remote provider, GitHub Enterprise Server, GitLab Self-Managed, and Jira integrations, plus autolinks, terminal links, and deep links.
- **[Interface and Customization](/gitlens/gl-features-interface-and-customization/)**: Menus and toolbars, modes, the Welcome view, and display language.

***

## Where Did This Section Go?

The sections of this page moved to the feature reference pages above. Find a section by its old name:

| Section | Now on |
| --- | --- |
| <span id="revision-navigation"></span>Revision Navigation | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#revision-navigation) |
| <span id="current-line-blame"></span>Current Line Blame | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#current-line-blame) |
| <span id="git-codelens"></span>Git CodeLens | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#git-codelens) |
| <span id="codelens-types"></span>CodeLens Types | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#codelens-types) |
| <span id="codelens-behavior"></span>CodeLens Behavior | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#codelens-behavior) |
| <span id="related-command"></span>Related Command | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#related-command) |
| <span id="status-bar-blame"></span>Status Bar Blame | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#status-bar-blame) |
| <span id="default-behavior"></span>Default Behavior | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#default-behavior) |
| <span id="customizable-click-behavior"></span>Customizable Click Behavior | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#customizable-click-behavior) |
| <span id="hovers"></span>Hovers | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#hovers) |
| <span id="current-line-hovers"></span>Current Line Hovers | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#current-line-hovers) |
| <span id="details-hover"></span>Details Hover | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#details-hover) |
| <span id="changes-diff-hover"></span>Changes (Diff) Hover | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#changes-diff-hover) |
| <span id="annotation-hovers"></span>Annotation Hovers | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#annotation-hovers) |
| <span id="file-blame"></span>File Blame | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#file-blame) |
| <span id="features"></span>Features | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#features) |
| <span id="file-changes"></span>File Changes | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#file-changes) |
| <span id="file-heatmap"></span>File Heatmap | [Blame and Annotations](/gitlens/gl-features-blame-and-annotations/#file-heatmap) |
| <span id="code-suggest-preview"></span>Code Suggest PREVIEW | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#code-suggest) |
| <span id="how-to-create-a-code-suggestion"></span>How to Create a Code Suggestion | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#how-to-create-a-code-suggestion) |
| <span id="accepting-a-suggestion-locally"></span>Accepting a Suggestion Locally | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#accepting-a-suggestion-locally) |
| <span id="accepting-a-suggestion-on-gitkraken-dev"></span>Accepting a Suggestion on gitkraken.dev | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#accepting-a-suggestion-on-gitkraken-dev) |
| <span id="cloud-patches-preview"></span>Cloud Patches PREVIEW | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#cloud-patches-preview) |
| <span id="what-are-cloud-patches-and-why-use-them"></span>What Are Cloud Patches and Why Use Them? | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#what-are-cloud-patches-and-why-use-them) |
| <span id="how-to-set-up-cloud-patches"></span>How to Set Up Cloud Patches | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#how-to-set-up-cloud-patches) |
| <span id="how-to-work-with-cloud-patches"></span>How to Work with Cloud Patches | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#how-to-work-with-cloud-patches) |
| <span id="sharing-options"></span>Sharing Options | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#sharing-options) |
| <span id="self-hosting-cloud-patch-data"></span>Self-Hosting Cloud Patch Data | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#self-hosting-cloud-patch-data) |
| <span id="commit-graph"></span>Commit Graph | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#commit-graph) |
| <span id="how-to-open-the-commit-graph"></span>How to Open the Commit Graph | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#how-to-open-the-commit-graph) |
| <span id="commit-graph-header"></span>Commit Graph Header | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#commit-graph-header) |
| <span id="scope-the-graph-to-a-worktree"></span>Scope the Graph to a Worktree | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#scope-the-graph-to-a-worktree) |
| <span id="follow-the-active-terminal"></span>Follow the Active Terminal | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#follow-the-active-terminal) |
| <span id="configuration-and-layout"></span>Configuration and Layout | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#configuration-and-layout) |
| <span id="column-customization"></span>Column Customization | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#column-customization) |
| <span id="panel-vs-editor-layout"></span>Panel vs. Editor Layout | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#panel-vs-editor-layout) |
| <span id="compact-layout"></span>Compact Layout | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#compact-layout) |
| <span id="scroll-markers"></span>Scroll Markers | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#scroll-markers) |
| <span id="settings"></span>Settings | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#settings) |
| <span id="repository-health"></span>Repository Health | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#repository-health) |
| <span id="rich-commit-search"></span>Rich Commit Search | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#rich-commit-search) |
| <span id="natural-language-search-pro"></span>Natural Language Search PRO | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#natural-language-search-pro) |
| <span id="search-prefixes"></span>Search Prefixes | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#search-prefixes) |
| <span id="full-context-menu-support"></span>Full Context Menu Support | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#full-context-menu-support) |
| <span id="compare-mode-pro"></span>Compare Mode PRO | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#compare-mode-pro) |
| <span id="compose-mode-pro"></span>Compose Mode PRO | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#compose-mode-pro) |
| <span id="multi-file-selection"></span>Multi-File Selection | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#multi-file-selection) |
| <span id="pull-request-indicators"></span>Pull Request Indicators | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#pull-request-indicators) |
| <span id="hiding-remotes-branches-or-tags"></span>Hiding Remotes, Branches, or Tags | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#hiding-remotes-branches-or-tags) |
| <span id="filtering-options"></span>Filtering Options | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#filtering-options) |
| <span id="minimap-experimental"></span>Minimap (Experimental) | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#minimap) |
| <span id="minimap-settings"></span>Minimap Settings | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#minimap-settings) |
| <span id="minimap-legend"></span>Minimap Legend | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#minimap-legend) |
| <span id="launchpad-pro"></span>Launchpad PRO | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#launchpad-pro) |
| <span id="accessing-launchpad"></span>Accessing Launchpad | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#accessing-launchpad) |
| <span id="using-launchpad"></span>Using Launchpad | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#using-launchpad) |
| <span id="start-review-pro"></span>Start Review PRO | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#start-review-pro) |
| <span id="start-work-pro"></span>Start Work PRO | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#start-work-pro) |
| <span id="pin-or-snooze-prs"></span>Pin or Snooze PRs | [Pull Requests and Collaboration](/gitlens/gl-features-pull-requests-and-collaboration/#pin-or-snooze-prs) |
| <span id="visual-history"></span>Visual History | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#visual-history) |
| <span id="how-to-read-the-graph"></span>How to Read the Graph | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#how-to-read-the-graph) |
| <span id="gitkraken-ai"></span>GitKraken AI | [AI and Agents](/gitlens/gl-features-ai-and-agents/#gitkraken-ai) |
| <span id="ai-generated-commit-messages"></span>AI-Generated Commit Messages | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-generated-commit-messages-pro) |
| <span id="ai-stash-messages-pro"></span>AI Stash Messages PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-stash-messages-pro) |
| <span id="ai-explanations-preview"></span>AI Explanations PREVIEW | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-explanations) |
| <span id="ai-commit-explanations-pro"></span>AI Commit Explanations PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-commit-explanations-pro) |
| <span id="ai-changelog-creation-advanced"></span>AI Changelog Creation ADVANCED | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-changelog-creation-pro) |
| <span id="ai-generate-commits-pro"></span>AI Generate Commits PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#commit-composer-view-pro) |
| <span id="ai-rebase-pro"></span>AI Rebase PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#commit-composer-view-pro) |
| <span id="auto-rebase-pro"></span>Auto-Rebase PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#auto-rebase-pro) |
| <span id="commit-composer-view-pro"></span>Commit Composer View Pro | [AI and Agents](/gitlens/gl-features-ai-and-agents/#commit-composer-view-pro) |
| <span id="interactive-draft-commits"></span>Interactive Draft Commits | [AI and Agents](/gitlens/gl-features-ai-and-agents/#interactive-draft-commits) |
| <span id="commit-composer-branch-recomposition"></span>Commit Composer: Branch Recomposition | [AI and Agents](/gitlens/gl-features-ai-and-agents/#commit-composer-branch-recomposition) |
| <span id="recompose-entire-branches"></span>Recompose Entire Branches | [AI and Agents](/gitlens/gl-features-ai-and-agents/#recompose-entire-branches) |
| <span id="enhanced-composer-capabilities"></span>Enhanced Composer Capabilities | [AI and Agents](/gitlens/gl-features-ai-and-agents/#enhanced-composer-capabilities) |
| <span id="commit-composer-selective-recomposition"></span>Commit Composer: Selective Recomposition | [AI and Agents](/gitlens/gl-features-ai-and-agents/#commit-composer-selective-recomposition) |
| <span id="compose-and-recompose-commands"></span>Compose and Recompose Commands | [AI and Agents](/gitlens/gl-features-ai-and-agents/#compose-and-recompose-commands) |
| <span id="git-command-palette"></span>Git Command Palette | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#git-command-palette) |
| <span id="quick-commit-access"></span>Quick Commit Access | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#quick-commit-access) |
| <span id="quick-stash-access"></span>Quick Stash Access | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#quick-stash-access) |
| <span id="quick-status-access"></span>Quick Status Access | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#quick-status-access) |
| <span id="interactive-rebase-editor"></span>Interactive Rebase Editor | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#interactive-rebase-editor) |
| <span id="start-or-continue-with-auto-rebase-pro"></span>Start or Continue with Auto-Rebase PRO | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#start-or-continue-with-auto-rebase-pro) |
| <span id="conflict-detection"></span>Conflict Detection | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#conflict-detection) |
| <span id="rebase-editor-settings"></span>Rebase Editor Settings | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#rebase-editor-settings) |
| <span id="conflict-resolution-actions"></span>Conflict Resolution Actions | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#conflict-resolution-actions) |
| <span id="to-use-this-directly-from-your-terminal-e-g-when-running-git-rebase-i"></span>To use this directly from your terminal (e.g., when running git rebase -i): | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#to-use-this-directly-from-your-terminal-e-g-when-running-git-rebase-i) |
| <span id="commit-signature-verification-pro"></span>Commit Signature Verification PRO | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#commit-signature-verification-pro) |
| <span id="verification-badges"></span>Verification Badges | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#verification-badges) |
| <span id="allowed-signers-management"></span>Allowed Signers Management | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#allowed-signers-management) |
| <span id="autolinks"></span>Autolinks | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#autolinks) |
| <span id="terminal-links"></span>Terminal Links | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#terminal-links) |
| <span id="remote-provider-integrations"></span>Remote Provider Integrations | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#remote-provider-integrations) |
| <span id="connecting-the-github-and-gitlab-integration"></span>Connecting the GitHub and GitLab Integration | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#connecting-the-github-and-gitlab-integration) |
| <span id="github-enterprise-server-and-gitlab-self-managed-integration-pro"></span>GitHub Enterprise Server and GitLab Self-Managed Integration PRO | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#github-enterprise-server-and-gitlab-self-managed-integration-pro) |
| <span id="connecting-github-enterprise-server-or-gitlab-self-managed"></span>Connecting GitHub Enterprise Server or GitLab Self-Managed | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#connecting-github-enterprise-server-or-gitlab-self-managed) |
| <span id="jira-integration-pro"></span>Jira Integration PRO | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#jira-integration-pro) |
| <span id="powerful-commands"></span>Powerful Commands | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#powerful-commands) |
| <span id="deep-links"></span>Deep Links | [Integrations and Links](/gitlens/gl-features-integrations-and-links/#deep-links) |
| <span id="git-submodule-support"></span>Git Submodule Support | [Git Commands and Rebase](/gitlens/gl-features-git-commands-and-rebase/#git-submodule-support) |
| <span id="commit-file-details-in-large-histories"></span>Commit File Details in Large Histories | [Commit Graph and History](/gitlens/gl-features-commit-graph-and-history/#commit-file-details-in-large-histories) |
| <span id="display-language"></span>Display Language | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#display-language) |
| <span id="welcome-view"></span>Welcome View | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#welcome-view) |
| <span id="ai-agent-integration-pro"></span>AI Agent Integration PRO | [AI and Agents](/gitlens/gl-features-ai-and-agents/#ai-agent-integration) |
| <span id="supported-agents"></span>Supported Agents | [AI and Agents](/gitlens/gl-features-ai-and-agents/#supported-agents) |
| <span id="agent-hooks"></span>Agent Hooks | [AI and Agents](/gitlens/gl-features-ai-and-agents/#agent-hooks) |
| <span id="agent-sessions"></span>Agent Sessions | [AI and Agents](/gitlens/gl-features-ai-and-agents/#agent-sessions) |
| <span id="mcp-server-management"></span>MCP Server Management | [AI and Agents](/gitlens/gl-features-ai-and-agents/#mcp-server-management) |
| <span id="menus-toolbars"></span>Menus & Toolbars | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#menus-toolbars) |
| <span id="modes"></span>Modes | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#modes) |
| <span id="experimental-multi-diff-editor"></span>Experimental Multi-diff Editor | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#experimental-multi-diff-editor) |
| <span id="commands-using-multi-diff"></span>Commands using Multi-diff | [Interface and Customization](/gitlens/gl-features-interface-and-customization/#commands-using-multi-diff) |
