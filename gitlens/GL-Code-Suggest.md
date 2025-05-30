---

title: Gitlens Code Suggest
description: Code Suggest in Gitlens
taxonomy:
    category: gitlens

---


GitKraken Code Suggest simplifies code review by allowing you to make suggestions and edits across the entire project, not just on the lines that were changed, within GitLens, GitKraken Desktop, and gitkraken.dev. When a Pull Request is open, you can make suggestions to the pull request that others can then review and accept to include in the pull request. 

<div class='callout callout--basic'>
    <p>Note: Code Suggest is currently only available for repositories on github.com.</p>
</div>

<img src="/wp-content/uploads/gl-code-suggest.png" class="help-center-img img-bordered">

To begin suggesting changes, open the [GitLens Inspect Overview](/gitlens/side-bar/#overview) for the desired repository and checkout a branch that has an open pull request. From here, you will have the option to _Start Review for PR #PR_. You may begin modifying and saving any file you would like to include in the code suggestion. Once you are ready, select _Suggest Changes for PR_, provide a title, and then finish with _Create Code Suggestion_. 

<img src="/wp-content/uploads/gl-code-suggest-create.gif" class="help-center-img img-bordered">

This will include a comment on the pull request with two options: you can select _Code Suggestion for #PR_ to open the suggestion in gitkraken.dev or select _locally on your machine_ to open the suggestion in GitKraken or GitLens.

<img src="/wp-content/uploads/gl-code-suggest-comment.png" class="help-center-img img-bordered">

When selecting _locally on your machine_ you can open them on GitLens or [GitKraken Desktop](/gitkraken-client/pull-requests/#review-code-and-suggest-changes). Here, you can review the changes by selecting each file and once you are ready, you can select _Apply_ to apply to the branch you currently have checked out or select the dropdown and then _Apply to a Branch_ to apply to a new branch or select an existing branch. This will apply the patch locally. 

<img src="/wp-content/uploads/gl-accept-code-suggestion-from-gl.gif" class="help-center-img img-bordered">

When selecting the _Code Suggestion for #PR_ you will be taken to gitkraken.dev to review and accept the changes. Here, you can review the changes by selecting each file and once you are ready, you can select _Commit Suggestions_. This will create a new commit on the remote for the existing branch (shown under _COMMIT SUGGESTIONS TO_). 

<img src="/wp-content/uploads/gl-accept-code-suggestion.gif" class="help-center-img img-bordered">

***
