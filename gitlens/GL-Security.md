---

title: Security Information - Gitlens
description: Data Security Information for GL
taxonomy:
    category: gitlens

---

Below is a chart outlining some basic security information regarding the type of data that we collect and how we store it.

| Service | What information are we collecting | How is this information secured in the transfer| Where is this information stored | How is this information secured in storage |
| --- | --- | --- | --- | --- |
| Workspaces/Insights | Repo meta-data issues/PR’s | Encrypted with TLS | MongoDB Atlas | Encrypted at rest (AES-256) |
| Teams & Users | Repo-relative file paths, number of lines changed | Encrypted with TLS | MongoDB Atlas | Encrypted at rest (AES-256) |
| Subscriptions | Billing info: lastFour, name, type(creditcard,paypal,ach..), zip, country, creditCard type(mastercard, visa, …) | Encrypted with TLS | MongoDB Atlas | Encrypted at rest (AES-256) |
| Focus View | Storing meta-data for issues/pull-requests/URLs | Encrypted with TLS | Postgres (RDS) | Encrypted at rest (AES-256) |
| Cloud Patches | Info related to the patch (repo name/URL/provider/base branch name/etc.) + the patch content itself. | Encrypted with TLS | Patch info is stored in a Postgres database, patch content is stored in AWS S3. | SSE-S3, which uses 256-bit Advanced Encryption Standard (AES-256) |
