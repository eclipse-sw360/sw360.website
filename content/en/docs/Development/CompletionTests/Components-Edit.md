---
title: "Edit Component"
linkTitle: "Edit Component"
weight: 80
---

## SW360 "Edit Component" Page Test Cases

### General Page Behavior

#### Info Message on Page Load
- **Test Case ID:** COMP-EDIT-001
- **Description:** Verify the info message on top on page load: "Success: You are editing the original document."
- **Steps:**
    1. Navigate to the "Edit Component" page.
- **Expected Result:** The info message "Success: You are editing the original document." is displayed on top.

### Summary Tab

#### General Information Section
- **Test Case ID:** COMP-EDIT-002
- **Description:** Verify the "General Information" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "General Information" section.
    3. Verify the presence of the following fields:
        - Name (required)
        - Created by
        - Categories (required) (type to auto complete)
        - Component Type (required) (one of OSS, COTS, Internal, Inner Source, Service, Freeware, Code Snippet) (info hover beneath)
        - CycloneDX Component Type (one of CDX type) (info hover beneath)
        - Default vendor (click to open vendor popup) (clear button beneath)
        - Homepage URL
        - VCS/Repository URL
        - Block URL
        - Wiki URL
        - Mailing List URL
        - Short Description (text area)
        - Modified By
- **Expected Result:** All specified fields are present and function as described.

#### Roles Section
- **Test Case ID:** COMP-EDIT-003
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "Roles" section.
    3. Verify the presence of the following fields:
        - Component Owner (single value)
        - Owner Accounting Unit
        - Owner Billing Group
        - Owner Country
        - Moderators (multi value)
- **Expected Result:** All specified fields are present and function as described.

#### Additional Roles Section
- **Test Case ID:** COMP-EDIT-004
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "Additional Roles" section.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External Ids Section
- **Test Case ID:** COMP-EDIT-005
- **Description:** Verify the "External Ids" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "External Ids" section.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** COMP-EDIT-006
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "Additional Data" section.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

### Releases Tab

#### Releases Table
- **Test Case ID:** COMP-EDIT-007
- **Description:** Verify the table with releases in the Releases Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the Releases Tab.
    3. Verify the presence of a table with the following column:
        - Name Version (clickable link to release)
- **Expected Result:** The table with the specified column is present.

#### Add Releases Button
- **Test Case ID:** COMP-EDIT-008
- **Description:** Verify the "Add Releases" button in the Releases Tab.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the Releases Tab.
    3. Click on the "Add Releases" button.
- **Expected Result:** A new page opens to create a release.

### Attachments Tab

#### Attachments Table
- **Test Case ID:** {{< relref path="Projects-Edit.md">}}#attachments-table
