---
title: "Requests - Clearing Request Details"
linkTitle: "Requests - Clearing Request Details"
weight: 330
---

## SW360 "Clearing Request Details" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** CR-DTL-001
- **Description:** Verify the presence of the "Edit Request" button and CR ID on top. If the CR is closed, the "Reopen Request" button should be shown instead, clicking which opens a Reopen dialog box.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page of an Open state request.
    2. Locate the top section of the page.
    3. Click on the "Edit Request" button.
    4. Navigate to the "Clearing Request Details" page of a closed request.
    5. Click on the "Reopen Request" button.
- **Expected Result:** The "Edit Request" button and CR ID are present for Open state requests. The "Reopen Request" button is present for closed requests and opens a Reopen dialog box.

### Clearing Request Information for Project Section

#### Project Link
- **Test Case ID:** CR-DTL-002
- **Description:** Verify the presence of the project link to open the project.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Information for Project section.
- **Expected Result:** The project link is present and functional.

#### Clearing Request Fields
- **Test Case ID:** CR-DTL-003
- **Description:** Verify the presence of the specified fields in the Clearing Request section.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Information for Project section.
    3. Verify the presence of the following fields:
        - Requesting User
        - Created on
        - Preferred Clearing Date
        - Business Area/Line
        - Clearing Type
        - Requester comment
- **Expected Result:** All specified fields are present and function as described.

#### Clearing Decision Fields
- **Test Case ID:** CR-DTL-004
- **Description:** Verify the presence of the specified fields in the Clearing Decision section.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Information for Project section.
    3. Verify the presence of the following fields:
        - Request Status
        - Priority
        - Clearing Team
        - Agreed Clearing Date
        - Last Updated on
- **Expected Result:** All specified fields are present and function as described.

### Clearing Request Comments Section

#### Comment Count
- **Test Case ID:** CR-DTL-005
- **Description:** Verify the display of the comment count.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Comments section.
- **Expected Result:** The comment count is displayed.

#### Comment Box
- **Test Case ID:** CR-DTL-006
- **Description:** Verify the presence of the comment box with an "Add comment" button and a search bar on the right.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Comments section.
- **Expected Result:** The comment box with an "Add comment" button and a search bar on the right is present.

#### Comment Rows
- **Test Case ID:** CR-DTL-007
- **Description:** Verify the presence of comment rows below the comment box.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Locate the Clearing Request Comments section.
- **Expected Result:** Comment rows are present below the comment box.

### Edit Clearing Request

#### Editable Fields
- **Test Case ID:** CR-DTL-008
- **Description:** Verify that the "Edit Clearing Request" allows changes to the specified fields.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Click on the "Edit Request" button.
    3. Verify the presence of the following fields:
        - Requesting User
        - Clearing Type
        - Request Status
        - Priority
        - Clearing Team
        - Agreed Clearing Date
- **Expected Result:** The specified fields are present and editable.

#### Update and Cancel Buttons
- **Test Case ID:** CR-DTL-009
- **Description:** Verify the presence of the "Update Request" and "Cancel" buttons on top.
- **Steps:**
    1. Navigate to the "Clearing Request Details" page.
    2. Click on the "Edit Request" button.
    3. Locate the top section of the edit page.
- **Expected Result:** The "Update Request" and "Cancel" buttons are present.
