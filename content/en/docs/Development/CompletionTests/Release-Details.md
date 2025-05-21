---
title: "Release Details"
linkTitle: "Release Details"
weight: 120
---

## SW360 "Release Details" Page Test Cases

### General Page Behavior

#### Dropdown Button for Release Version
- **Test Case ID:** REL-DTL-001
- **Description:** Verify the dropdown button showing the release version, which opens to show other versions. The button has a Red or Green indicator on the left indicating the Clearing State (Report approved: Green, otherwise red).
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the dropdown button for the release version.
- **Expected Result:** The dropdown button is present with the specified behavior and indicator.

#### Top Buttons
- **Test Case ID:** REL-DTL-002
- **Description:** Verify the presence of the "Edit Release", "Link to Project", "merge", and "Subscribe" buttons on top.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The specified buttons are present.

### Summary Tab

#### General Section
- **Test Case ID:** REL-DTL-003
- **Description:** Verify the "General" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the "General" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Release ID
        - CPE ID
        - Release Date of this Release
        - Created on
        - Created By
        - Modified On
        - Modified By
        - Contributors
        - Moderators
        - Subscribers
        - Additional Roles
        - Source Code Download URL
        - Binary Download URL
        - Clearing State
        - Release Mainline State
        - Main licenses (i button next to license name, click to show src file for this license, fail if multiple files)
        - Other licenses (i button next to license name)
        - Programming Languages
        - Operating Systems
        - External ids
        - Additional Data
- **Expected Result:** All specified fields are present and function as described.

#### Release Repository Section
- **Test Case ID:** REL-DTL-004
- **Description:** Verify the "Release Repository" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the "Release Repository" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - "Repository:" link of the repository
        - Repository type in brackets
- **Expected Result:** The specified fields are present and function as described.

#### Release Vendor Section
- **Test Case ID:** REL-DTL-005
- **Description:** Verify the "Release Vendor" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the "Release Vendor" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - FullName
        - Short Name
        - URL
- **Expected Result:** The specified fields are present and function as described.

#### Used By Section
- **Test Case ID:** REL-DTL-006
- **Description:** Verify the "Used By" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the "Used By" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Release name
        - Used by total of visible / restricted projects
        - Table of visible projects with columns: Project name (click to open project), Group, Responsible
    4. If the release is a linked release in another release, verify the presence of the table "Release is used by the following components" with columns: Vendor, Name (click to open Component), Main licenses, Component Type
- **Expected Result:** The specified fields and tables are present and function as described.

### Linked Releases Tab

#### Table of Linked Releases
- **Test Case ID:** REL-DTL-007
- **Description:** Verify the table of linked releases in the Linked Releases Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Linked Releases Tab.
    3. Verify the presence of a table with the following columns:
        - Name (click to open release)
        - Release relation
        - License Names
        - Clearing State
- **Expected Result:** The table with the specified columns is present.

### Linked Packages Tab

#### Table of Linked Packages
- **Test Case ID:** REL-DTL-008
- **Description:** Verify the table of linked packages in the Linked Packages Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Linked Packages Tab.
    3. Verify the presence of a table with the following columns:
        - Vendor (filterable)
        - Package Name version (filterable)
        - Licenses (filterable)
        - Package Manager (filterable)
        - Actions (edit package and delete package)
- **Expected Result:** The table with the specified columns is present.

### Clearing Details Tab

#### SPDX Attachments Section
- **Test Case ID:** REL-DTL-009
- **Description:** Verify the "SPDX Attachments" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields for each CLI report:
        - First column displays filename
        - Second column shows "Show License Info" button
        - On click on "Show License Info" button, verify that it changes to "Add data to this release" button and displays "Main / Concluded License Ids:" and "Other License Ids:" as UL in the third column "Result"
- **Expected Result:** The specified fields and behavior are present.

#### Assessment Summary Info Section
- **Test Case ID:** REL-DTL-010
- **Description:** Verify the "Assessment Summary Info" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Clearing Details Tab.
    3. Click on the "Show Assessment Summary Info" button.
    4. Verify the presence of a table with the `AssessmentSummary` section from the CLIXML file of the approved attachment.
    5. If multiple accepted CLI are found, verify that "Multiple approved CLI are found in release!" is displayed.
- **Expected Result:** The specified fields and behavior are present.

#### Clearing Details: Release Section
- **Test Case ID:** REL-DTL-011
- **Description:** Verify the "Clearing Details: Release" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - Clearing State (fossology button next to it)
        - The 13 checkboxes with Red (No) or Green (Yes) state
        - The text boxes values
        - External URL as clickable link
- **Expected Result:** All specified fields are present and function as described.

#### Request Information Section
- **Test Case ID:** REL-DTL-012
- **Description:** Verify the "Request Information" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - Request ID
        - Additional Request Information
        - Evaluation Start
        - Evaluation End
- **Expected Result:** All specified fields are present and function as described.

#### Supplemental Information Section
- **Test Case ID:** REL-DTL-013
- **Description:** Verify the "Supplemental Information" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - External Supplier ID
        - Number of Security Vulnerabilities
- **Expected Result:** All specified fields are present and function as described.

### ECC Details Tab

#### ECC Information Section
- **Test Case ID:** REL-DTL-014
- **Description:** Verify the "ECC Information" section in the ECC Details Tab.
- **Steps:**
    1. Navigate to the "Release Details" page.
    2. Locate the ECC Details Tab.
    3. Verify the presence of the following fields:
        - ECC Status
        - AL
        - ECCN
        - Material Index Number
        - ECC Comment
        - Assessor Contact Person
        - Assessor Department
        - Assessment Date
- **Expected Result:** All specified fields are present and function as described.

### Attachments Tab

#### Attachments Table

- **Test Case ID:** [PROJ-DTL-016]({{< relref path="Projects-Details.md">}}#attachments-table)

### Vulnerabilities Tab

#### Vulnerabilities Table
- **Test Case ID:** [COMP-DTL-010]({{< relref path="Components-Details.md">}}#tab-name-and-count),
  [COMP-DTL-011]({{< relref path="Components-Details.md">}}#total-vulnerabilities),
  [COMP-DTL-012]({{< relref path="Components-Details.md">}}#vulnerabilities-table) and
  [COMP-DTL-013]({{< relref path="Components-Details.md">}}#changing-vulnerability-state)

### Change Log Tab

#### Change Log Table
- **Test Case ID:** [PROJ-DTL-021]({{< relref path="Projects-Details.md">}}#toggle-on-top),
  [PROJ-DTL-022]({{< relref path="Projects-Details.md">}}#changelog-table),
  [PROJ-DTL-023]({{< relref path="Projects-Details.md">}}#opening-changelog),
  [PROJ-DTL-024]({{< relref path="Projects-Details.md">}}#basic-info-section),
  [PROJ-DTL-025]({{< relref path="Projects-Details.md">}}#changed-fields-table) and
  [PROJ-DTL-026]({{< relref path="Projects-Details.md">}}#returning-to-list)
