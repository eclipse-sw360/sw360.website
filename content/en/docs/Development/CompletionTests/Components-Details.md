---
title: "Component Details"
linkTitle: "Component Details"
weight: 90
---

## SW360 "Component Details" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** COMP-DTL-001
- **Description:** Verify the presence of the "Edit Component", "Merge", "Split", and "Subscribe"/"Unsubscribe" buttons on top.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The specified buttons are present.

### Summary Tab

#### Description of Component
- **Test Case ID:** COMP-DTL-002
- **Description:** Verify the presence of the description of the component in the Summary Tab.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Summary Tab.
- **Expected Result:** The description of the component is present.

#### General Section
- **Test Case ID:** COMP-DTL-003
- **Description:** Verify the "General" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the "General" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - ID of the Component
        - Name
        - Created on
        - Created by (mailto link)
        - Modified on
        - Modified by (mailto link)
        - Component Type
        - CycloneDX Component Type
        - Default vendor (can be clickable link)
        - Homepage (click URL)
        - VCS/Repository URL (click URL)
        - Block (click URL)
        - Wiki (click URL)
        - Miling list (click URL)
        - External IDs (as UL, key in bold, value next to it)
        - Additional data (same as External IDs)
- **Expected Result:** All specified fields are present and function as described.

#### Release Aggregate Data Section
- **Test Case ID:** COMP-DTL-004
- **Description:** Verify the "Release Aggregate Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the "Release Aggregate Data" section in the Summary Tab.
    3. Verify the presence of the following details as a comma-separated list:
        - Vendors
        - Languages
        - Platforms
        - Operating Systems
        - Main licenses
- **Expected Result:** The specified details are present as a comma-separated list.

#### Roles Section
- **Test Case ID:** COMP-DTL-005
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the "Roles" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Component Owner (mailto link)
        - Owner Accounting Unit
        - Owner Billing Group
        - Owner Country
        - Moderators (comma-separated mailto list)
        - Subscribers (comma-separated mailto list)
        - Additional Roles
    4. Verify that all users displayed are mailto links.
- **Expected Result:** All specified fields are present and function as described.

#### Component Used By
- **Test Case ID:** COMP-DTL-006
- **Description:** Verify the display of the total count of visible and restricted projects using the component.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Summary Tab.
- **Expected Result:** The total count of visible and restricted projects using the component is displayed.

#### Table to Visible Projects
- **Test Case ID:** COMP-DTL-007
- **Description:** Verify the table of visible projects with the specified columns.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Summary Tab.
    3. Verify the presence of a table with the following columns:
        - Project name (with version, clickable link to open project)
        - Group
        - Responsible
- **Expected Result:** The table with the specified columns is present.

#### Component Used By Other Components
- **Test Case ID:** COMP-DTL-020
- **Description:** Verify the display of the table "Component name is used by the following components" if a release of the current component is linked to another release of another component.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Summary Tab.
    3. Verify the presence of a table with the following columns:
        - Vendor
        - Name (Link to open component)
        - Main licenses
        - Component Type
- **Expected Result:** The table with the specified columns is present if a release of the current component is linked to another release of another component.

### Release Overview Tab

#### Releases Table
- **Test Case ID:** COMP-DTL-008
- **Description:** Verify the table of releases in the Release Overview Tab.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Release Overview Tab.
    3. Verify the presence of a table with the following columns:
        - Name
        - Version (click to open release)
        - Clearing State
        - Clearing Report (download link to approved reports, hover to see filename, status, comment, and created)
        - Release Mainline State
        - Action (FOSSology, edit, duplicate, link project, merge, delete)
    4. Verify the presence of a search bar on top.
- **Expected Result:** The table with the specified columns is present, and the search bar is functional.

### Attachments Tab

#### Attachments Table
- **Test Case ID:** [PROJ-DTL-016]({{< relref path="Projects-Details.md">}}#attachments-table)

### Vulnerabilities Tab

#### Tab Name and Count
- **Test Case ID:** COMP-DTL-010
- **Description:** Verify the display of "number of checked or unchecked vulnerabilities + number of incorrect vulnerabilities" on the tab name.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Vulnerabilities Tab.
- **Expected Result:** The specified count is displayed on the tab name.

#### Total Vulnerabilities
- **Test Case ID:** COMP-DTL-011
- **Description:** Verify the display of the total number of vulnerabilities on top.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Vulnerabilities Tab.
- **Expected Result:** The total number of vulnerabilities is displayed on top.

#### Vulnerabilities Table
- **Test Case ID:** COMP-DTL-012
- **Description:** Verify the vulnerabilities table as per test cases DTL-017 & DTL-020.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Vulnerabilities Tab.
    3. Verify the presence of a table with the specified columns.
- **Expected Result:** The table with the specified columns is present.

#### Changing Vulnerability State
- **Test Case ID:** COMP-DTL-013
- **Description:** Verify the behavior when changing the state of selected vulnerability rows.
- **Steps:**
    1. Navigate to the "Component Details" page.
    2. Locate the Vulnerabilities Tab.
    3. Select vulnerability rows to change the state.
    4. Verify that the updated row's verification column updates the state.
    5. Verify that the hover icon says "You just changed this value. Please reload page."
    6. Verify that the count from point a changes to a reload icon with a warning background.
- **Expected Result:** The specified behavior is observed when changing the state of selected vulnerability rows.

### Change Log Tab

#### Change Log Table
- **Test Case ID:** [PROJ-DTL-021]({{< relref path="Projects-Details.md">}}#toggle-on-top),
  [PROJ-DTL-022]({{< relref path="Projects-Details.md">}}#changelog-table),
  [PROJ-DTL-023]({{< relref path="Projects-Details.md">}}#opening-changelog),
  [PROJ-DTL-024]({{< relref path="Projects-Details.md">}}#basic-info-section),
  [PROJ-DTL-025]({{< relref path="Projects-Details.md">}}#changed-fields-table) and
  [PROJ-DTL-026]({{< relref path="Projects-Details.md">}}#returning-to-list)
