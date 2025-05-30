---

title: Gitlens Visual File History
description: Learn about Visual File History in Gitlens
taxonomy:
    category: gitlens

---


The Visual File History allows you to quickly see the evolution of a file, including when changes were made, how large they were, and who made them.

To access the Visual File History view, open the GitLens Inspect sidebar. Once the sidebar is open, the view will be available. Alternatively, you can open Visual File History from the Command Palette by using (`cmd/ctrl + shift + P`) > GitLens: Show Visual File History View.

<img src="/wp-content/uploads/visual-file-history.png" class="help-center-img img-bordered">

Authors who have contributed changes to the file are on the left y-axis to create a swim-lane of their commits over time (the x-axis). Commit are plotted as color-coded (per-author) bubbles, whose size represents the relative magnitude of the changes.

Additionally, each commit's additions and deletions are visualized as color-coded, stacked, vertical bars, whose height represents the number of affected lines (right y-axis). Added lines are shown in green, while deleted lines are red.


Gain additional insights on hover.

<img src="/wp-content/uploads/visual-file-history-hover.png" class="help-center-img img-bordered">

<div class='callout callout--warning'>
    <p>Community plan is restricted to Public and Local Repositories only.</p>
</div>

***