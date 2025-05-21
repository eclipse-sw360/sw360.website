---
title: "Project - Source Bundle Usages"
linkTitle: "Project - Source Bundle Usages"
weight: 53
---

## SW360 "Generate Source Code Bundle" Page Test Cases

### General Page Behavior

#### Page Similarity
- **Test Case ID:** PROJ-SCB-AU-001
- **Description:** Verify that the page shown when the "Generate Source Code" button is clicked in the "License Clearing Tab" is similar to the Generate License Info usage page.
- **Steps:**
    1. Navigate to the "License Clearing Tab" in a project.
    2. Click on the "Generate Source Code" button.
- **Expected Result:** A page similar to the Generate License Info usage page is shown.

#### Top Button
- **Test Case ID:** PROJ-SCB-AU-002
- **Description:** Verify the presence of the "Download" button on top.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Download" button is present.

#### Selection Restore Message
- **Test Case ID:** PROJ-SCB-AU-003
- **Description:** Verify the display of the selection restore message.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the message section.
- **Expected Result:** The selection restore message is displayed.

### Source Code Bundle Table

#### Columns
- **Test Case ID:** PROJ-SCB-AU-004
- **Description:** Verify the presence of the specified columns in the Source Code Bundle Table.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the Source Code Bundle Table.
    3. Verify the presence of the following columns:
        - Checkbox (clicking will uncheck all checkboxes (except self) and restore selection at page load)
        - Lvl (starts at 1, increases at each subproject)
        - Name
        - Conclusions
        - Type
        - State
        - Uploaded by
        - Clearing Team
- **Expected Result:** All specified columns are present and function as described.

#### Attachment Type
- **Test Case ID:** PROJ-SCB-AU-005
- **Description:** Verify that the table displays only attachments of type SRC, and they cannot be expanded.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the Source Code Bundle Table.
- **Expected Result:** Only attachments of type SRC are displayed, and they cannot be expanded.

#### Row Colors
- **Test Case ID:** PROJ-SCB-AU-006
- **Description:** Verify the row colors based on the number of attachments.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the Source Code Bundle Table.
    3. Verify the row colors:
        - Red for no attachments
        - Green for 1 attachment
        - Yellow for more than 1 attachment
- **Expected Result:** The row colors are displayed as specified.

#### Release Clearing State
- **Test Case ID:** PROJ-SCB-AU-007
- **Description:** Verify that the State column displays the Release's clearing state.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the Source Code Bundle Table.
- **Expected Result:** The State column displays the Release's clearing state.

#### Attachment Rows
- **Test Case ID:** PROJ-SCB-AU-008
- **Description:** Verify the details displayed for each attachment row.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Locate the Source Code Bundle Table.
    3. Verify the presence of the following details:
        - Checkbox if License Info is selected for the attachment
        - Level number
        - If used in number of projects else show "Not used in any projects yet" in the Type column
        - Attachment status
        - Uploader name
        - Uploader Department
- **Expected Result:** All specified details are present and function as described.

### Download Button

#### Report Generation
- **Test Case ID:** PROJ-SCB-AU-009
- **Description:** Verify that clicking the "Download" button triggers the bungle generation and saves the attachment usage of the current page.
- **Steps:**
    1. Navigate to the "Generate Source Code Bundle" page.
    2. Click on the "Download" button.
- **Expected Result:** The bundle is generated, and the attachment usage of the current page is saved.
