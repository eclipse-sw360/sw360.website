This page is one of the basic user workflow documentation pages. It can give orientation how the sw360 can be used - as guidance or orientation. There is no particular need to follow these workflows, it is just one way. Workflows are shown as flow charts.

### Introduction

When working with FOSSology, it turned out that an overview on a product-/project-basis would be helpful. People actually do not want to have a look at the individual components, analyzed by FOSSology, but they would like to know, which of the components used in a product are analyzed and which require to have a look at. The sw360 provides that view on components: it groups the components - their releases actually by the products.

### Clearing

The term clearing refers to clarifying the condition of an item - in our case the license and copyright condition of a component's release. The steps are as follows:

1. Transfer the source code attachment to FOSSology using the transfer functionality in sw360.
2. In FOSSology, process the upload for license and copyright clearing.
3. In FOSSology generate a clearing report (for example SPDX file)
4. Correct, review, complete the clearing report manually as required - on the local computer.
5. Upload the clearing report as attachment to a release. Set the attachment type of that attachment to clearing report.

After the update is performed (if this was a moderation request, after the moderation request was approved) the clearing status of the release in sw360 changes to "report available". In addition, another user can review the clearing report an approve it. Then, the clearing status changes to "approved".



![workflow-clearing](https://github.com/eclipse/sw360/wiki/images-workflow/workflow-clearing.png)