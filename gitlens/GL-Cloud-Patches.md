---
title: GitLens Cloud Patches
description: Use GitLens Cloud Patches to securely share work-in-progress changes across GitKraken tools for early collaboration.
product: GitLens
feature: Cloud Patches
content_type: how-to
audience: developer
plan_required: Pro
status: GA
last_verified: 2026-03
taxonomy:
    category: gitlens

---

<kbd>Last updated: March 2026</kbd>

## What Are Cloud Patches?

GitLens Cloud Patches let GitLens users securely share uncommitted or in-progress changes across **GitLens**, **GitKraken Desktop**, and the **GitKraken CLI** before opening a pull request. Use this feature when you need early feedback on work in progress and have a GitKraken account with Cloud Patch access.

---

## How to Set Up GitLens Cloud Patches

To enable or disable Cloud Patches per client:

1. Open the Command Palette:  
   - macOS: <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
   - Windows/Linux: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>  
2. Search for **Preferences: Open User Settings (JSON)**.  
3. Set the value of `gitlens.cloudPatches.enabled`:  
   - `true` = enabled (default)  
   - `false` = disabled  

---

## How to Create and Share a Cloud Patch

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

| Sharing option | Requires account | Best for | Limitation |
|---|---|---|---|
| Anyone with the link | No | Fast sharing outside your organization | Anyone with the link can access it |
| Anyone in my org | Yes | Broad sharing within a GitKraken organization | Limited to organization members |
| Only collaborators | Yes | Restricted review with named teammates | Requires selecting collaborators |

- **Anyone with the link**: Public access for anyone with the link.  
- **Anyone in my org**: Accessible to members of your GitKraken Organization (authentication required).  
- **Only collaborators**: Restricted to selected GitKraken Organization members (authentication required). Use **Invite** to select members.  

Cloud Patches shared with you appear under **Shared with Me** in the Cloud Patches section.

<figure>
  <img src="/wp-content/uploads/gl-cloud-patch-sharing-options-2.png" class="help-center-img img-bordered" alt="Sharing options for a Cloud Patch in GitLens" />
  <figcaption style="text-align: center; color: #888">Cloud Patch sharing options</figcaption>
</figure>

---

## How to Apply or Delete a Cloud Patch

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
