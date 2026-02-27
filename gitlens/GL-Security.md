---
title: GitLens Security Information
description: Learn how GitLens secures your data, including collection, transfer, storage, and SOC 2 certification.
taxonomy:
    category: gitlens

---

<kbd>Last updated: February 2026</kbd>

## Data Collection and Storage

The table below outlines the types of data GitLens collects, how it is secured during transfer, where it is stored, and how it is protected at rest.

| Service         | Data Collected                                                                 | Secured in Transfer | Storage Location                        | Secured in Storage                                |
|-----------------|--------------------------------------------------------------------------------|---------------------|------------------------------------------|--------------------------------------------------|
| **Subscriptions** | Billing info: name, payment type (credit card, PayPal, ACH, etc.), last 4 digits of payment method, zip code, country, card type (Visa, Mastercard, etc.) | Encrypted with TLS  | MongoDB Atlas                            | Encrypted at rest (AES-256)                      |
| **Launchpad**     | URLs of issues and pull requests (for pin/snooze functionality only)          | Encrypted with TLS  | Postgres (RDS)                           | Encrypted at rest (AES-256)                      |
| **Cloud Patches** | Patch metadata (repo name/URL/provider/base branch, etc.) and patch content  | Encrypted with TLS  | Metadata in Postgres; patch content in AWS S3 | Metadata encrypted at rest (AES-256); patch content encrypted with SSE-S3 (AES-256) |
| **Cloud Workspaces** | Repository info: URL, provider, organization name, repository name         | Encrypted with TLS  | MongoDB Atlas                            | Encrypted at rest (AES-256)                      |

---

## SOC 2 Compliance

GitKraken and its tools, including GitLens, are **SOC 2 certified**.  
If you would like to request a copy of our SOC 2 report, please visit our [Trust Center](https://trust.gitkraken.com/) to begin the request process.  

Please note: an MNDA must be signed before we can provide a copy of the report.

<div class='callout callout--info'>
  <p><strong>Note:</strong> SOC 2 reports are only available for <strong>Business</strong> and <strong>Enterprise</strong> customers.</p>
</div>