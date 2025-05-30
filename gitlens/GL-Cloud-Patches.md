---

title: Gitlens Cloud Patches
description: Learn about Cloud Patches in Gitlens
taxonomy:
    category: gitlens

---


### What are Cloud Patches and why would you want to use them

A Cloud Patch is a Git patch that GitKraken securely stores for you so it can be easily shared with others across GitLens, GitKraken Desktop, and the GitKraken CLI. The patch is directly transferred from your machine into secure storage. 

Cloud Patches allow the ability to engage early with your team before a pull request. They can be created as soon as you have a work in progress. This can help with collaborating on changes prior to a pull request and minimize the delay of pull request reviews.

### How to setup Cloud Patches 

To enable Cloud Patches per client, open the user Settings (`command/ctrl + shift + P` > `Preferences: Open User Settings (JSON)`) and set `gitlens.cloudPatches.enabled` to `true` - this is on by default. To disable Cloud Patches per client, set this setting to `false` .

### How to work with Cloud Patches

Cloud Patches can be managed from the Cloud Patches view in the GitLens side bar.

<img src="/wp-content/uploads/gl-cloud-patch-create.webp" class="help-center-img img-bordered">

A Cloud Patch can be created from Working Changes, Commits, Stashes or Comparisons by using the "Share as Cloud Patch" option from the command palette or from the Share submenu in applicable gitlens views. 

<img src="/wp-content/uploads/gl-create-cloud-patch-example.png" class="help-center-img img-bordered">

When creating a Cloud Patch, you have the following sharing options:

- `Anyone with the link`: Anyone that you share the public link with will be able to work with the Cloud Patch.

- `Anyone in my org`: Anyone in the GitKraken Organization will be able to work with the Cloud Patch. They will be required to authenticate with a GitKraken account to access it.

- `Only collaborators`: Only users in the GitKraken Organization who have been selected when sharing will be able to work with the Cloud Patch. They will be required to authenticate with a GitKraken account to access it. Select `Invite` to select desired members.

Cloud Patches shared with you can be viewed in the Cloud Patches section under `Shared with Me`.

<div class='callout callout--basic'>
    <p>Note: If you have multiple organizations, you can easily switch between them from the GitKraken Account view.</p>
</div>

<img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" class="help-center-img img-bordered">

Cloud Patches can be viewed from URLs shared to you and they can be applied to your working tree or to a new or existing branch. Simply select or open the link and then follow the prompts within GitLens to apply the Cloud Patch. 

<img src="/wp-content/uploads/gl-apply-patch-example.gif" class="help-center-img img-bordered">

To delete a cloud patch, right-click it and select `Delete Cloud Patch...`.

<img src="/wp-content/uploads/gl-delete-cloud-patch.png" class="help-center-img img-bordered">

### Self-Hosting Cloud Patch data

If you do not want your Cloud Patch data stored on GitKraken Servers, we offer the ability for you to host Cloud Patches on your own AWS S3 storage instance. For more information on configuring this, see our documentation [here](/gk-dev/gk-dev-home/#self-hosted).
