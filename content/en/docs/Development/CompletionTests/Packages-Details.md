---
title: "Package Details"
linkTitle: "Package Details"
weight: 190
---

## SW360 "Package Details" Page Test Cases

### General Page Behavior

#### Top Button
- **Test Case ID:** PKGS-DTL-001
- **Description:** Verify the presence of the "Edit Package" button on top, which takes the user to the edit package page.
- **Steps:**
    1. Navigate to the "Package Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Edit Package" button is present and functional.

### Summary Tab

#### Summary Section
- **Test Case ID:** PKGS-DTL-002
- **Description:** Verify the presence of the specified fields in the Summary Section.
- **Steps:**
    1. Navigate to the "Package Details" page.
    2. Locate the Summary Section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Id
        - Name
        - Version
        - Package Type
        - PURL
        - Package Manager
        - VCS
        - Homepage URL
        - Licenses
        - Linked Release (clickable link to open release)
        - Description (note: should be on top like components)
        - Created on
        - Created by
        - Modified On
        - Modified By
- **Expected Result:** All specified fields are present and function as described.

#### Used In Section
- **Test Case ID:** PKGS-DTL-003
- **Description:** Verify the display of the "Used In" section if the Package is used in a project.
- **Steps:**
    1. Navigate to the "Package Details" page.
    2. Locate the "Used In" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Package is used in total of visible / restricted projects count
        - Table with columns: Project name (click to open project), Group, Responsible
- **Expected Result:** The specified fields and table are present and function as described if the Package is used in a project.

### Change Log Tab

#### Change Log Table
- **Test Case ID:** [PROJ-DTL-021]({{< relref path="Projects-Details.md">}}#toggle-on-top),
  [PROJ-DTL-022]({{< relref path="Projects-Details.md">}}#changelog-table),
  [PROJ-DTL-023]({{< relref path="Projects-Details.md">}}#opening-changelog),
  [PROJ-DTL-024]({{< relref path="Projects-Details.md">}}#basic-info-section),
  [PROJ-DTL-025]({{< relref path="Projects-Details.md">}}#changed-fields-table) and
  [PROJ-DTL-026]({{< relref path="Projects-Details.md">}}#returning-to-list)
