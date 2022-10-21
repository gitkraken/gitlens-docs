---

title: Account
description: GitKraken account page where you can manage your GitKraken GitLens Account.
taxonomy:
    category: gitlens

---

Whether a solo user on a personal license, or an owner managing multiple teams across organizations, learn how to manage your GitKraken GitLens account(s), subscription(s), and organization(s).

The first question to answer: do I need an account to use GitLens or GitLens+? 

+ GitLens is COMPLETELY FREE, no account is required, and can be used on any local repository.
+ GitLens+ features on local & public repositories are also COMPLETELY FREE.
+ GitLens+ features on private repositories require a Pro plan (or greater), view pricing [here](https://www.gitkraken.com/gitlens/pricing).

If you are working with GitLens+ features on private repositories, you will need to create an account and purchase a license. See below for more information.

***

## Sign-up and Purchase

You can [register](https://app.gitkraken.com/register) a GitKraken account to give you access to GitLens+. Feel free to use your email address or use another sign-up source like [GitHub](/integrations/github). Using an alternate sign-in source will automatically pull in your related email address to make an account.

Once your account is created, you can purchase a plan by clicking 🚀 **Purchase License**, and then select **See GitLens Pricing** to be presented with options for purchasing. 

Next you will be promted to select how many licenses you want and enter your billing information. Fill out all relevant fields and click <button class='button button--success button--ui button--nolink'>Complete purchase</button>.

<div class='callout callout--warning'>
    <p><strong>Note:</strong> If you are purchasing a license for just your personal use or otherwise not part of an organization, you can enter a value of your choice. Most use "Personal" or "Self."</p>
</div>

If you already have an **Organization** or **Trial Organization**, you can click on the existing organization instead and navigate to `Subscription` to change the license or add users.


***

## Organizations
The <kbd>Organizations</kbd> section shows your organization(s). Click on an organization to manage the [Users](/organizations/#manage-users), Teams, and Subscriptions.

To access your account and manage your organization(s), navigate to [https://app.gitkraken.com](https://app.gitkraken.com) and login.

Once you log into your account, click <em class="context-menu">Organization  <i class="fa fa-caret-right"></i> [Your organization name]</em> to add users.

<img src="/wp-content/uploads/subscriptions.png" srcset="/wp-content/uploads/subscriptions@2x.png 2x" class="img-responsive center img-bordered">

### Subscriptions
Subsriptions can be added to an organization by clicking the <button class='button button--primary button--ui button--nolink'><span style='color:#141422;'>New Organization</span></button> tab.

<img src="/wp-content/uploads/gk-plans1.png"  class="img-responsive center img-bordered">

Once a subscription is added to the organization owner or admin roles may add users to the account using their email address (see [Manage Users](/account/organizations/#manage-users) section below).

### Rename organization

To rename your Organization, log into [https://app.gitkraken.com](https://app.gitkraken.com) as the `Owner` or `Admin` and then navigate to <em class="context-menu">Organizations  <i class="fa fa-caret-right"></i> [Your organization name] <i class="fa fa-caret-right"></i> Settings</em>.

<img src="/wp-content/uploads/rename.png" class="img-responsive center img-bordered">


Type a new name for the Organization and save.

### Hide organizations

If you have any expired GitKraken subscriptions, you may hide these expired organizations from the left panel of [https://app.gitkraken.com](https://app.gitkraken.com).

<img src="/wp-content/uploads/hide-expired-organizations.png" class="img-responsive center img-bordered">

You can also manually choose to hide an organization in the sidebar from the <em class="context-menu">Organizations  <i class="fa fa-caret-right"></i> [Your organization name] <i class="fa fa-caret-right"></i> Settings</em> menu.

<img src="/wp-content/uploads/hide-organization.png" class="img-responsive center img-bordered">

Click the <kbd>Show Hidden Organizations</kbd> button to show hidden organizations.


***
## Roles

There are four roles for a GitKraken user within an organization's account:

* **Owner**: Add or edit users plus access to billing. No one but the owner can transfer ownership
* **Admin**: Add or edit users plus manage billing
* **User**: General user
* **Billing Contact (unlicensed)**: Does not consume a license. Add or edit general users plus manage billing

***
## Manage users

### Allocating licenses
1. Under <em class="context-menu">Organization  <i class="fa fa-caret-right"></i> [Your organization name]</em> , click <button class='button button--success button--ui button--nolink'>Add User</button>
2. Enter the user email address
3. Select the user role
4. Click <button class='button button--success button--ui button--nolink'>Add user</button>
5. Celebrate

Additionally, you can set up a user as a <kbd>Billing Contact (unlicensed)</kbd>. This is perfect for people who don't need to use GitKraken Client, but wish to have access to manage the account subscription and settings.



### Buying more licenses

First log into [https://app.gitkraken.com](https://app.gitkraken.com) and click through to <em class="context-menu">Organization  <i class="fa fa-caret-right"></i> [Your organization name] <i class="fa fa-caret-right"></i> Subscription</em>.

Increase the user count and then complete the purchase. User upgrades are always prorated to your billing cycle.

<img src="/wp-content/uploads/buy-more-licenses.png" class="img-bordered img-responsive center">

<div class='callout callout--success'>
    <p>Do you have questions about upgrading your plan or an order? Contact our <a href="mailto:sales@gitkraken.com">Success</a> or <a href="mailto:accounting@gitkraken.com">Accounting</a> teams as needed!</p>
</div>

### Removing users

To remove a user and free up a license, click <button class='button button--danger button--ui button--nolink'>Remove</button> next to the user on the list followed by <kbd>Remove User</kbd> for confirmation.

<img src="/wp-content/uploads/remove-user.png" srcset="/wp-content/uploads/remove-user.png" class="img-responsive center img-bordered">

### Reallocating licenses

Any `Owner`, `Admin`, or `Billing Contact` may remove users and then add users to reallocate licenses from [https://app.gitkraken.com](https://app.gitkraken.com).

Note, `Billing Contact` roles cannot remove or edit `Owner` or `Admin` users.

From the *Users* pane in the left panel, click to <button class='button button--danger button--ui button--nolink'>Remove</button> a user. Then click <button class='button button--success button--ui button--nolink'>Add User</button>.

<img src="/wp-content/uploads/licenses-page.png" srcset="/wp-content/uploads/licenses-page@2x.png 2x" class="img-responsive center img-bordered">

### Importing/Exporting users

To import users click the `Add User` button. From here you can import users via a `.csv` file.

<img src="/wp-content/uploads/account-site-import-button.png"/>

When importing users, be sure to have columns for `Email`, `Username`, `Role`, `User License`.


If you need to export users, you may access this option from the Users list on [https://app.gitkraken.com](https://app.gitkraken.com).

<img src="/wp-content/uploads/account-site-export-arrow.png"/>

The export will contain columns for `Email`, `Username`, `Role`, `User License`.

***
## Billing information
Review billing information or switch between credit card and Paypal at any time.

### Editing billing

To edit your billing or to switch payment methods, first log in as an `Admin` or the `Owner` and click <em class="context-menu">Organization  <i class="fa fa-caret-right"></i> [Your organization name]</em>.

Click **Subscription** to update the subscription.  From here you may select <button class='button button--primary button--ui button--nolink'><span style='color:#141422;'>Update Payment</span></button> to change your card details or switch payment methods.

<img src="/wp-content/uploads/edit-billing.png" class="img-bordered img-responsive center">

If you are switching from credit card to Paypal, follow the prompts to authenticate with Paypal.

### Looking for receipts or payment history?
Each billing cycle, our accounting system will send the owner listed a subscription a receipt for record keeping. The account site does not currently display billing history but please email [accounting@gitkraken.com](mailto:accounting@gitkraken.com) for additional copies.

***

## Transfer ownership

If you are the `Owner` of a <strong>GitKraken Pro</strong> or <strong>GitKraken Enterprise</strong> account, then you may transfer ownership to a different user from [https://app.gitkraken.com](https://app.gitkraken.com).

To transfer ownership, navigate to <em class="context-menu">Organizations  <i class="fa fa-caret-right"></i> [Your organization name] <i class="fa fa-caret-right"></i> Settings</em>. Then select the existing user who will become the new `Owner`.

<img src="/wp-content/uploads/transfer-ownership.png" class="img-responsive center img-bordered">


***
## Cancellations

To cancel, first log into your GitKraken account as the `Admin` or `Owner` and click <em class="context-menu">Organizations   <i class="fa fa-caret-right"></i> [Your organization name] <i class="fa fa-caret-right"></i>  Subscription</em>.

You may then `Cancel Subscription` from the lower left corner.

Canceling will turn off the auto-renewal but you will retain access to your license(s) for the remainder of your subscription period.

## Reactivate a subscription

Any canceled or expired subscription may be reactivated by logging into [https://app.gitkraken.com](https://app.gitkraken.com) as the `Owner`, `Admin` or `Billing Contact`.

Click on <kbd>Organizations</kbd> and then click on the name of the expired or canceled subscription.

<img src="/wp-content/uploads/org-expired.png" srcset="/wp-content/uploads/org-expired@2x.png 2x" class="img-responsive center img-bordered">

Then click on <kbd>Subscription</kbd> in the left panel, where you may update the license total or billing details before hitting <button class='button button--success button--ui button--nolink'>Reactivate</button>.