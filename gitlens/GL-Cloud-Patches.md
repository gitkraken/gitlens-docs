---
title: GitLens Cloud Patches
description: Use GitLens Cloud Patches to securely share work-in-progress changes across GitKraken tools for early collaboration.
taxonomy:
    category: gitlens

---

<kbd>Last updated: February 2026</kbd>

## What Are Cloud Patches?

A **Cloud Patch** is a Git patch securely stored by GitKraken so it can be easily shared across **GitLens**, **GitKraken Desktop**, and the **GitKraken CLI**.  
The patch is transferred directly from your machine into secure storage.

Cloud Patches let you collaborate with your team **before creating a pull request**. You can share work in progress, gather feedback early, and minimize delays in pull request reviews.

---

## Set Up Cloud Patches

To enable or disable Cloud Patches per client:

1. Open the Command Palette:  
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
2. Search for **Preferences: Open User Settings (JSON)**.  
3. Set the value of `gitlens.cloudPatches.enabled`:  
   - `true` = enabled (default)  
   - `false` = disabled  

---

## Create and Share Cloud Patches

You can manage Cloud Patches from the **Cloud Patches view** in the GitLens sidebar.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-create.webp" class="help-center-img img-bordered" alt="Creating a Cloud Patch from the GitLens sidebar" />
  <figcaption style="text-align: center; color: #888">Creating a Cloud Patch</figcaption>
</figure>

A Cloud Patch can be created from **Working Changes, Commits, Stashes, or Comparisons** by selecting **Share as Cloud Patch** from either:  
- The Command Palette  
- The **Share** submenu in applicable GitLens views  

<figure>
  <img src="/wp-content/uploads/gl-create-cloud-patch-example.png" class="help-center-img img-bordered" alt="Creating a Cloud Patch from working changes in GitLens" />
  <figcaption style="text-align: center; color: #888">Example of creating a Cloud Patch</figcaption>
</figure>

### Sharing Options
When creating a Cloud Patch, choose one of the following:

- **Anyone with the link**: Public access for anyone with the link.  
- **Anyone in my org**: Accessible to members of your GitKraken Organization (authentication required).  
- **Only collaborators**: Restricted to selected GitKraken Organization members (authentication required). Use **Invite** to select members.  

Cloud Patches shared with you appear under **Shared with Me** in the Cloud Patches section.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" class="help-center-img img-bordered" alt="Sharing options for a Cloud Patch in GitLens" />
  <figcaption style="text-align: center; color: #888">Cloud Patch sharing options</figcaption>
</figure>

---

## Apply and Manage Cloud Patches

- Open a Cloud Patch from a shared URL to view it in GitLens.  
- Apply it to your **working tree** or to a **new/existing branch** by following the prompts in GitLens.  

<figure>
  <img src="/wp-content/uploads/gl-apply-patch-example.gif" class="help-center-img img-bordered" alt="Applying a Cloud Patch in GitLens" />
  <figcaption style="text-align: center; color: #888">Applying a Cloud Patch</figcaption>
</figure>

### Delete a Cloud Patch
1. Right-click the patch in the Cloud Patches view.  
2. Select **Delete Cloud Patch…**  

<figure>
  <img src="/wp-content/uploads/gl-delete-cloud-patch.png" class="help-center-img img-bordered" alt="Deleting a Cloud Patch in GitLens" />
  <figcaption style="text-align: center; color: #888">Deleting a Cloud Patch</figcaption>
</figure>

---

## Self-Host Cloud Patch Data

If you do not want Cloud Patch data stored on GitKraken servers, you can host Cloud Patches on your own **AWS S3 storage instance**.  

For configuration instructions, see [Self-Hosted Documentation](/gk-dev/gk-dev-home/#self-hosted).

<div class='callout callout--basic'>
  <p>Note: If you belong to multiple organizations, you can switch between them from the GitKraken Account view.</p>
</div>