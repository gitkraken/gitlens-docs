---

title: Manage GitKraken Organization
description: Learn about GitKraken Organizations
taxonomy:
    category: gitlens
    
---

A GitKraken organization is a collection of [GitKraken accounts](/gitkraken-client/gitkraken-account/) which unlocks a shared [subscription](/gitkraken-client/gitkraken-subscriptions/), collaboration features between members, and administration of the members in the organization. If you are creating an account for the first time, an organization will automatically be created for you.


***

## Create

To create an organization, go to [app.gitkraken.com](https://app.gitkraken.com/) and select "New Organization” in the left side menu. Next, select the tier that is best for your organization (Pro, Teams, or Enterprise). The creator of the organization is automatically the [owner](/gitlens/gitlens-organization/#roles) of it.

<img src="/wp-content/uploads/gitkraken-create-organization-2.png" class="img-responsive center img-bordered">

You also have the option to purchase an organization for someone else that would be the [owner](/gitlens/gitlens-organization/#roles) and use the subscription. To do this, check "This purchase is for someone else" in the checkout page and it will ask who the owner is by email and sends them email instructions with next steps. You will be the owner of the organization until they accept, then you will be set as the [Billing Contact](/gitlens/gitlens-organization/#roles).

<img src="/wp-content/uploads/gitkraken-organization-new-owner-1.png" class="img-responsive center img-bordered">

***

## Add Users

To add someone to your organization, go to [app.gitkraken.com](https://app.gitkraken.com/), select your organization in the left sidebar, select "Users," and finally select "Add Users." Here you can enter as many email addresses as you want and the [role](/gitlens/gitlens-organization/#roles) (in the drop down) you would like to assign them all. 

<img src="/wp-content/uploads/gitkraken-organization-add-users.png" class="img-responsive center img-bordered">

Only members that have a [role](/gitlens/gitlens-organization/#roles) with permission can add users to an organization. When you do add someone, it will consume a license of your subscription. If all available licenses are consumed when adding a user, a billing summary will show up during the process, select "Purchase" to complete the transaction and add the users.

<img src="/wp-content/uploads/gitkraken-organization-add-users-2.png" class="img-responsive center img-bordered">

You can also add licenses in bulk to your organization separately from adding users by going to the [Subscription](/gitlens/gitlens-subscriptions/) section in your organization.

***

## Reallocate Licenses

Any Owner, Admin, or Billing Contact may remove users and then add users to reallocate licenses.

The Billing Contact role cannot remove or edit Owner or Admin users.

To reallocate a license, navigate to Users and then select "Remove" for the desired user. Then, you can add the new user. 

***

## Import and Export Users

To import multiple users via CSV select the “Add User” button. From here you can select “Import via CSV”. When importing users, be sure to have columns for `Email`, `Username`, `Role`, `User License`.

<img src="/wp-content/uploads/gitkraken-organization-import-and-export-users.png" class="img-responsive center img-bordered">

To export users to a CSV, select “Export via CSV”. The export will contain columns for Email, Username, Role, User License.

<img src="/wp-content/uploads/gitkraken-organization-import-and-export-users-2.png" class="img-responsive center img-bordered">

***

## Roles

Roles grant members permissions within an organization. There are four roles a user may have:
+ Owner: there is exactly one owner per organization. Owners have full permission and consume a license.
+ Admin: Admins have full permissions and consume a license. Admins cannot remove or edit the owner.
+ User: Users have no administrative permissions but do consume a license.
+ Billing Contact: Billing Contacts have the same permissions as admins, except they do not consume a license.



<table class='table table--bordered table--shortcuts'>
    <thead>
        <tr>
            <th>Permission</th>
            <th>Owner</th>
            <th>Admin</th>
            <th>User</th>
            <th>Billing Contact</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Licensed to use GitKraken</td>
            <th>✅</th>
            <th>✅</th>
            <th>✅</th>
            <th></th>
        </tr>
        <tr>
            <td>Add, edit, and remove users</td>
            <th>✅</th>
            <th>✅</th>
            <th></th>
            <th>✅</th>
        </tr>
        <tr>
            <td>Create and manage teams</td>
            <th>✅</th>
            <th>✅</th>
            <th></th>
            <th>✅</th>
        </tr>
        <tr>
            <td>Manage billing and purchase licenses</td>
            <th>✅</th>
            <th>✅</th>
            <th></th>
            <th>✅</th>
        </tr>
        <tr>
            <td><a href="/gitlens/gitlens-organization/#transfer-ownership">Transfer ownership</a> of the organization</td>
            <th>✅</th>
            <th></th>
            <th></th>
            <th></th>
        </tr>
    </tbody>
</table>

***

## Teams

Teams are the best way to organize members of your GitKraken organization. In addition, teams can create Shared Workspaces to bring focus to their collaborative work and help identify conflicts by showing what files and branches your team is working on.

Any member can create a team by visiting the Teams tab within the organization at [app.gitkraken.com](https://app.gitkraken.com/). For more information on creating and working with teams, see the [Teams](/gitkraken-client/teams/) page.

<img src="/wp-content/uploads/gitkraken-organization-teams.png" class="img-responsive center img-bordered">

***

## SSO

Single sign-on (SSO) is available for organizations that require it. SSO requires:
+ A Teams or Enterprise subscription (If you want to give SSO a try, start an org trial or reach out to us)
+ A GitKraken organization
+ A compatible Identity Provider (IDP) which is limited to:
    + Azure Active Directory
    + Okta
    + Google Identity Platform (G Suite)
    + Ping Identity
+ SSO can only be set up by the Owner or by an Admin of the organization.
+ SSO is set up at the Organization level. Each organization can have multiple IDPs connected simultaneously.

### How to setup SSO

See how to setup SSO by visiting the [Setting up SSO](/gitkraken-client/single-sign-on/#setting-up-sso-on-a-gitkraken-organization) section.

***

## Settings

Visiting the Settings section of your organization will give you a snapshot of your subscription and allow you to edit a few key aspects of your organization like changing the name and [transferring ownership](/gitlens/gitlens-organization/#transfer-ownership) of the organization.

You can hide organizations that you do not wish to see from the sidebar view by checking the “Hide organization in the sidebar” box. You can also rename an organization by typing the desired name into **Organization Name** and then selecting "Save."

<img src="/wp-content/uploads/gitkraken-organization-settings.png" class="img-responsive center img-bordered">

***

## Transfer Ownership

If you’re the [owner](/gitkraken-client/gitkraken-organization/#roles) of an organization and would like to make someone else the owner you can do that. First you need to make sure to first add that account to the organization. Once the account is added to your organization, go to your organization, select "Settings" and then “Transfer ownership.” You will select the user within the organization to become the owner (and type their email to confirm). Once you select “Transfer Ownership,” the transfer is final and cannot be undone unless the new owner transfers ownership back to the original owner.

<img src="/wp-content/uploads/gitkraken-organization-transfer-organization.gif" class="img-responsive center img-bordered">

***

## Leave an Organization

If you no longer need to be a part of an organization, you can leave an organization by navigating to Settings and then `Leave Organization`. If you leave an organization, only an admin can invite you back. You will lose access to collaboration with members of GitKraken and your GitKraken paid license. 

This option will only be available if you are part of another organization and you are not the owner of the organization. If you are the current owner, you can [transfer the ownership](/gitlens/gitlens-organization/#transfer-ownership) and then leave the organization after.

<img src="/wp-content/uploads/gk-leave-organization.png" class="img-responsive center img-bordered">
