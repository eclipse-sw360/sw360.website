---
title: "Project - Attachment Usages"
linkTitle: "Project - Attachment Usages"
weight: 51
---

## SW360 "Attachment Usages" Page Test Cases

### General Page Behavior

#### Availability as a Tab
- **Test Case ID:** PROJ-AU-001
- **Description:** Verify that the "Attachment Usages" tab is available under the Projects Details page.
- **Steps:**
    1. Navigate to the "Projects Details" page.
    2. Locate the "Attachment Usages" tab.
- **Expected Result:** The "Attachment Usages" tab is present.

#### Top Buttons and Filters
- **Test Case ID:** PROJ-AU-002
- **Description:** Verify the presence of the "Save Usages" button, Linked Releases and Projects, Expand all, Collapse all, Release Filter (dropdown), and Search box on top.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Locate the top section of the page.
    3. Verify the presence of the following elements:
        - "Save Usages" button
        - Linked Releases and Projects
        - Expand all button
        - Collapse all button
        - Release Filter (dropdown) with options: With CLI Attachments, With Attachments, Without Source Attachments, Without Attachments
        - Search box
- **Expected Result:** All specified elements are present and function as described.

### Attachment Usages Table

#### Columns
- **Test Case ID:** PROJ-AU-003
- **Description:** Verify the presence of the specified columns in the Attachment Usages Table.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Locate the Attachment Usages Table.
    3. Verify the presence of the following columns:
        - Name
        - Relation
        - Uploaded by
        - Type
        - License Info (for CLX/SRR)
        - Conclusions (ends with .rdf)
        - Source Code Bundle
        - Other
- **Expected Result:** All specified columns are present and function as described.

#### No Linked Releases or Projects Message
- **Test Case ID:** PROJ-AU-004
- **Description:** Verify the display of the message "No Linked releases or projects" if no sub projects or linked releases are present.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Locate the Attachment Usages Table.
- **Expected Result:** The message "No Linked releases or projects" is displayed if no sub projects or linked releases are present.

#### Linked Release Details
- **Test Case ID:** PROJ-AU-005
- **Description:** Verify the display of each Linked Release in the Project with an expand button, release name and version (max 60 char), CLI count (if 0: red, 1: green, else yellow), and relation.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Locate the Attachment Usages Table.
    3. Click on the expand button of a Linked Release.
- **Expected Result:** The Linked Release details are displayed as specified.

#### Expanded Release Details
- **Test Case ID:** PROJ-AU-006
- **Description:** Verify the details displayed when a release is expanded.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Locate the Attachment Usages Table.
    3. Click on the expand button of a Linked Release.
    4. Verify the presence of the following details:
        - Title: "Created on: date\nStatus: checked\nIf checked Checked By: email\nChecked On: date"
        - Attachment name (max 60 char)
        - Uploader name
        - Attachment type shortname
        - Checkbox for License Info enabled if CLX or CLI (combined)
        - Checkbox for Conclusions enabled if CLX or CLI and ends with ".rdf"
        - Checkbox for Source Code bundle enabled if SRC or SRS
        - Checkbox for Other is always enabled
        - All the checkboxes are disabled if the user does not have write permission (admin or contributor or clearing admin or clearing expert)
        - Subproject's releases are indented
- **Expected Result:** All specified details are present and function as described.

### Save Usages Button

#### Save Usages Message
- **Test Case ID:** PROJ-AU-007
- **Description:** Verify that clicking on the "Save Usages" button shows a saved message.
- **Steps:**
    1. Navigate to the "Attachment Usages" page.
    2. Click on the "Save Usages" button.
- **Expected Result:** A saved message is shown.
