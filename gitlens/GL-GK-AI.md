---

title: GitKraken AI Features in GitLens
description: Learn more about the use of Gitkraken AI in Gitlens!
taxonomy:
    category: gitlens

---

<kbd>Last updated: February 2026</kbd>

Merge cutting-edge AI capabilities with your Git workflow to save time, increase clarity, and enhance collaboration. GitLens' AI features transform how you create, understand, and document code changes.

---

## Available AI Features

GitLens integrates powerful AI capabilities across different subscription tiers, each designed to address specific pain points in your development workflow.

### AI Generate Commit `Pro`
**Available in:** Pro, Advanced, and Business plans

Generate clear, descriptive commit messages based on your code changes, saving time and ensuring consistency across your repository. The AI analyzes your staged changes and creates meaningful messages that accurately describe what you've modified.

**How to access:**
- From the Command Palette: `GitLens: Generate Commit Message with AI`
- From the SCM panel: Click the "Generate Commit Message" button
- During the commit process: Look for the AI option in the commit interface

<img src="/wp-content/uploads/GL-ai-commit-generate.png" class="help-center-img img-bordered">

### AI Stash Messages`Pro`
**Available in:** Pro, Advanced, and Business plans

Create intelligent descriptions for stashed changes, making it easier to find and understand your work later. This feature generates context-rich stash descriptions that help you quickly identify the purpose of each stash.

**How to access:**
- From the Command Palette: `GitLens: Generate Stash Message with AI`
- When creating a stash: Look for the AI option in the stash creation interface
- From the stash view: Generate descriptions for existing stashes

<img src="/wp-content/uploads/GL-ai-stash.png" class="help-center-img img-bordered">

### AI Commit Explain `Pro`
**Available in:** Pro, Advanced, and Business plans

Understand the reasoning behind changes with AI-generated explanations of commit content and purpose. Quickly grasp the intent and impact of complex commits without having to manually review all changed files.

**How to access:**
- In the "Commit Details" view: Find the AI explanation panel
- In the "Cloud Patch Details" view: Look for explanations alongside commit information
- When reviewing commits: Option to generate explanations for any selected commit


<img src="/wp-content/uploads/GL-ai-commit-explain.png" class="help-center-img img-bordered">

### AI Changes Explain `Preview`
Gitkraken AI can also be used to generate summaries in Branches, Working changes, and Stashes.

What changed across all commits in a branch – ✨Explain Branch
What you’ve modified in your working directory – ✨Explain Working Changes
What you’ve previously stashed – ✨Explain Stash

You’ll find ✨Explain options for commits, branches, stashes, and working changes in several places:

- In the Commit Graph
- Available as commands in the command palette
- In many GitLens views: Commits, Branches, Stashes, Search & Compare, etc.
- In branch cards in the Home view

### AI Changelog Creation `Pro`
**Available in:** Advanced and Business plans only

Automatically generate comprehensive changelogs from selected commits in the Graph, perfect for release documentation. Maintain consistent and detailed changelogs without manual effort.

**How to access:**
- In the Search/Compare view: Click the inline button on the "commits" line
- When selecting multiple commits in the Graph: Right-click and choose "Generate Changelog"
- From the Command Palette: `GitLens: Generate Changelog from Commits`

<img src="/wp-content/uploads/GL-ai-generate-changelog.png" class="help-center-img img-bordered">

### AI Open Pull Request `Advanced`
**Available in:** Advanced and Business plans only

Open Pull Requests: Automatically generate clear PR titles and descriptions directly from your branch changes, speeding up review cycles.

**How to access:**
- From the GitLens Home View panel: Click the ✨button next to “Create a Pull Request”

<img src="/wp-content/uploads/GL-ai-create-pr.png" class="help-center-img img-bordered">

---
## AI Token Allocation by Plan

GitKraken AI features operate on a token-based system, with different allocations based on your subscription. For more information about Gitkraken AI allocations, please see our [Gitkraken AI FAQ](https://help.gitkraken.com/general/gitkraken-ai-faq) page.

Tokens refresh weekly and are shared across all AI features. More complex operations like changelog generation typically use more tokens than simpler ones like commit messages.

---
## Configuring Your AI Provider

### Provider Options

GitLens offers flexibility in choosing your AI provider:

1. **GitKraken AI** (default): Pre-configured and ready to use with your token allocation
2. **GitHub Copilot**: If installed, can be used as your AI provider
3. **Custom Provider** (BYOK): Connect your own key from supported AI services
>
- New OpenAI and Google models
- Self-hosted Azure AI models
- OpenAI-compatible API providers
- Local Ollama models
- OpenRouter support
>

### Setup Instructions

To configure your AI provider:
1. Open GitLens settings
2. Navigate to the "AI" section
3. Select your preferred provider from the dropdown
4. For custom providers, enter your API key in the designated field

---
## Advanced AI Settings
### User-Level Customization

- **Customize AI prompts**: Tailor the prompts used for various AI features to match your team's style
- **Token usage monitoring**: Track your token consumption for better allocation management
- **Default AI mode**: Choose between concise or detailed outputs for each feature

### Organization-Level Controls `Business`

- **Enforceable AI rules**: Set organization-wide policies for AI usage
- **Private AI model providers**: Connect to your organization's approved AI services
- **Token allocation management**: Distribute tokens across teams and projects

---
<div class='callout callout--basic'>
    <p>More questions about Gitkraken AI? Please see our <a href="https://help.gitkraken.com/general/gitkraken-ai-faq/">GitKraken AI FAQ page</a> for more details. For additional questions or support regarding GitKraken AI features, please contact our support team or visit the <a href="https://forum.gitkraken.com/">GitKraken Community forum</a>.</p>
</div>
