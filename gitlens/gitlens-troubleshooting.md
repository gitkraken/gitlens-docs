---
title: GitLens Troubleshooting
description: GitLens Troubleshooting
taxonomy:
  category: gitlens
---

## Enable showing Bitbucket pull request for a commit

GitLens can show a Pull Request for a commit for a connected integration. But Bitbucket [requires](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-pullrequests/#api-repositories-workspace-repo-slug-commit-commit-pullrequests-get)
a Pull Request Commit Links app to be installed in the workspace to enable this feature.

It's not a real application that can be seen in workspace settings, it's rather an internal service that Bitbucket activates after some event,
so for a user it is just a part of the Bitbucket service.

To enable this feature, you need to visit any commit in the Bitbucket UI and click on the "Pull requests" link in the "Apps" section at the bottom-right of the page:

<img src="/wp-content/uploads/gl-troubleshooting-bitbucket-pr-commit-links.png" class="help-center-img img-bordered">

The click makes the application is activated and its takes some time for Bitbucket to index data on their side.
After that PullRequests for commits will be shown in GitLens:

<img src="/wp-content/uploads/gitlens-troubleshooting-bitbucket-pr-on-a-commit.png" class="help-center-img img-bordered">
