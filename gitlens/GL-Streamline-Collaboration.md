---

title: Gitlens Streamline Collaboration
description: How can gitlens help streamline collaboration
taxonomy:
    category: gitlens

---


<div class='embed-container embed-container--16-9'>
    <iframe width='560' height='315' src='https://www.youtube.com/embed/ljKEzaCMEow?si=YFf7oME8PG926kET' frameborder='0' allowfullscreen></iframe>
</div>

<p> &nbsp; </p>

When collaborating with others in a repository, it can be difficult to share code without bloating your repository with multiple commits and branches that may not be ready to contribute to the remote. Additionally, pull request reviews can be limiting for what you have access to review, comment on, and does not give you the ability to review files that have not been modified. With the use of Cloud Patches and Code Suggest, GitLens offers the ability to easily share code without needing to commit/push it to a remote and allows you to suggest code changes to any file in the repository.

#### Cloud Patches `PRO`

Cloud Patches are Git patches that can be shared with anyone in your GitKraken organization to quickly share code changes with others. It can be applied to their working directory to continue to collaborate on or commit to the repository. 

To create a cloud patch, make changes to any file in a repository and then save those changes. Then, use the command palette (command/ctrl + shift + P) > _GitLens: Share as Cloud Patch…_. 

When you select members to share it with, they will see this in the Cloud Patch sidebar to be able to apply to their working directory.

<a href="vscode://eamodio.gitlens/link/command/cloud-patches">Open the Cloud Patches View in GitLens</a>.
<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

#### Code Suggest `PRO`

Code Suggest allows you to make edits across the entire repository that can be submitted to anyone's open pull request. 

To create a Code Suggestion, have a branch checked out with an open pull request, make changes to any files and save those changes. Then, use the command palette (command/ctrl + shift + P) > _GitLens: Show inspect view_ > Suggest Changes for PR. 

The pull request creator can then review these changes, apply them to their working directory to continue updating them, and accept the changes to commit/push them to the pull request.

<div class='callout callout--warning'>
    <p>This feature is only available for Pro subscription tiers or higher</p>
</div>

***