---
title: "Add Component"
linkTitle: "Add Component"
weight: 70
---

## SW360 "Add Component" Page Test Cases

### General Page Behavior

#### New Page Opening
- **Test Case ID:** COMP-CRT-013
- **Description:** Verify that upon clicking "Add Component," a new page opens with a message on top "Creating new Component."
- **Steps:**
    1. Navigate to the Main Components page.
    2. Click on the "Add Component" button.
- **Expected Result:** A new page opens with the message "Creating new Component" on top.

### Summary Tab

#### General Information Section
- **Test Case ID:** COMP-CRT-014
- **Description:** Verify the "General Information" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Component" page.
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
- **Test Case ID:** COMP-CRT-015
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Component" page.
    2. Locate the "Roles" section.
    3. Verify the presence of the following fields:
        - Component Owner (single value)
        - Owner Accounting Unit
        - Owner Billing Group
        - Owner Country
        - Moderators (multi value)
- **Expected Result:** All specified fields are present and function as described.

#### Additional Roles Section
- **Test Case ID:** COMP-CRT-016
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Component" page.
    2. Locate the "Additional Roles" section.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External Ids Section
- **Test Case ID:** COMP-CRT-017
- **Description:** Verify the "External Ids" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Component" page.
    2. Locate the "External Ids" section.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** COMP-CRT-018
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Component" page.
    2. Locate the "Additional Data" section.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

### Create Component Button

#### Component Creation
- **Test Case ID:** COMP-CRT-019
- **Description:** Verify that upon hitting the "Create Component" button, the component is saved, and the user is redirected to the component edit page for the newly created component.
- **Steps:**
    1. Navigate to the "Add Component" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create Component" button.
- **Expected Result:** The component is saved, and the user is redirected to the component edit page for the newly created component.
