---

title: Security Information - Gitlens
description: Data Security Information for GL
taxonomy:
    category: gitlens

---
## Information Collection/Storage
Below is a chart outlining some basic security information regarding the type of data that we collect and how we store it remotely.

| Service | What information are we collecting | How is this information secured in the transfer| Where is this information stored | How is this information secured in storage |
| --- | --- | --- | --- | --- |
| Subscriptions | Billing info: name, payment type (credit card, paypal, ACH, etc.), last four digits of payment method, zip code, country, credit card type (mastercard, visa, etc.) | Encrypted with TLS | MongoDB Atlas | Encrypted at rest (AES-256) |
| Launchpad | URLs of issues and pull requests ONLY for pin/snooze functionality | Encrypted with TLS | Postgres (RDS) | Encrypted at rest (AES-256) |
| Cloud Patches | Info related to the patch (repo name/URL/provider/base branch name/etc.) + the patch content itself. | Encrypted with TLS | Patch info is stored in a Postgres database, patch content is stored in AWS S3. | SSE-S3, which uses 256-bit Advanced Encryption Standard (AES-256) |
| Cloud Workspaces | Repository info: URL, provider, org name, repo name | Encrypted with TLS | MongoDB Atlas | Encrypted at rest (AES-256) |

## SOC2
Gitkraken and it’s tools are now SOC 2 Certified! If you would like to request a copy of our SOC2 report, please visit our [Trust Center](https://trust.gitkraken.com/) to get the request process started. Please note that in order to provide a copy of the report, we will need you to sign an MNDA.

<div class="bbb-callout bbb--info">
    <div class="irow">
    <div class="ilogobox">
        <span class="logoimg"></span>
    </div>
    <div class="imsgbox">
       SOC 2 reports are only available for Business and Enterprise customers.
    </div>
    </div>
</div>
