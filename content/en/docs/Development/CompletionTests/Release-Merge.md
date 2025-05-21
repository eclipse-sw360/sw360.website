---
title: "Merge Releases"
linkTitle: "Merge Releases"
weight: 150
---

## SW360 "Merge Release" Page Test Cases

### General Page Behavior

#### Accessing the Merge Release Page
- **Test Case ID:** MERGE-REL-001
- **Description:** Verify that the merge releases page can be reached by clicking the "Merge" button on a release or the merge icon in the release tab of a component details page. The release from which the button was clicked is called the Target release.
- **Steps:**
    1. Navigate to the "Release Details" page of a release.
    2. Click on the "Merge" button.
- **Expected Result:** The merge releases page is opened with the Target release specified.

### Choose Source Section

#### Source Releases Table
- **Test Case ID:** MERGE-REL-002
- **Description:** Verify the display of the table with all releases of the component except the Target release, with a search bar on top.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Choose source" section.
    3. Verify the presence of a table with the following columns:
        - Release Name
        - Version
        - Created by
- **Expected Result:** The table with the specified columns is present, and the search bar is functional.

#### Selecting a Source Release
- **Test Case ID:** MERGE-REL-003
- **Description:** Verify the process of choosing one source release and clicking "Next."
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Choose source" section.
    3. Select a source release from the table.
    4. Click on the "Next" button.
- **Expected Result:** The selected source release is chosen, and the page navigates to the "Merge data" section.

### Merge Data Section

#### Different Source Attachments
- **Test Case ID:** MERGE-REL-004
- **Description:** Verify the message displayed if releases have different source attachments.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Verify the presence of the message: "Cannot continue to merge of releases: Both releases must have at least one pair of same source attachments or no source attachments at all. Otherwise a merge is not possible."
- **Expected Result:** The specified message is displayed.

#### Abort Button
- **Test Case ID:** MERGE-REL-005
- **Description:** Verify the presence of the "Abort" button on the bottom.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Click on the "Abort" button.
- **Expected Result:** The page navigates back to the release.

#### Same Source Attachment or No Attachment
- **Test Case ID:** MERGE-REL-006
- **Description:** Verify the display of the section "following documents will be effected" if releases have the same source attachment or no attachment.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Verify the presence of the following fields:
        - Count for projects
        - Count for releases
        - Count for vulnerabilities
        - Count for attachment usage
        - Count for project vulnerability ratings
- **Expected Result:** The specified fields are present.

#### Display of Data
- **Test Case ID:** MERGE-REL-007
- **Description:** Verify the display of all data from the Target release on the left and the Source release on the right with a `<=` button in between.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
- **Expected Result:** The data from the Target release is displayed on the left, and the Source release data is displayed on the right with a `<=` button in between.

#### Data Carry Forward
- **Test Case ID:** MERGE-REL-008
- **Description:** Verify that the data on the left will be carried forward to the Target release.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
- **Expected Result:** The data on the left is carried forward to the Target release.

#### Created by Info Hover
- **Test Case ID:** MERGE-REL-009
- **Description:** Verify the presence of an info hover for the "Created by" field.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Hover over the "Created by" field.
- **Expected Result:** The info hover is present.

#### `<=` Button Action
- **Test Case ID:** MERGE-REL-010
- **Description:** Verify the action of pressing the `<=` button.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Press the `<=` button.
- **Expected Result:** The action can be undone with the undo button.

#### Attachments
- **Test Case ID:** MERGE-REL-011
- **Description:** Verify the display of attachments with name and attachment type in brackets. Matching source attachments section has an i icon. Other Attachments can be carried over.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
- **Expected Result:** The attachments are displayed with the specified details.

#### Finalizing Data
- **Test Case ID:** MERGE-REL-012
- **Description:** Verify the process of finalizing data and clicking "Next."
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Finalize the data.
    4. Click on the "Next" button.
- **Expected Result:** The page navigates to the "Confirm" section.

#### Going Back
- **Test Case ID:** MERGE-REL-013
- **Description:** Verify the ability to click "Back" to go to the "Merge data" section.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Merge data" section.
    3. Click on the "Next" button to go to the "Confirm" section.
    4. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Merge data" section.

### Confirm Section

#### Display of Data
- **Test Case ID:** MERGE-REL-014
- **Description:** Verify that only the data on the left is displayed in the "Confirm" section, and the effected notification is visible on top.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Confirm" section.
- **Expected Result:** Only the data on the left is displayed, and the effected notification is visible on top.

#### Merge Selection Payload
- **Test Case ID:** MERGE-REL-015
- **Description:** Verify that only the displayed data is sent as the merge selection payload.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Confirm" section.
    3. Click on the "Finish" button.
- **Expected Result:** Only the displayed data is sent as the merge selection payload.

#### Submitting the Merge
- **Test Case ID:** MERGE-REL-016
- **Description:** Verify the process of clicking "Finish" to submit the merge.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Confirm" section.
    3. Click on the "Finish" button.
- **Expected Result:** The merge is submitted, and the user lands on the Release Details page of the Target release.

#### Going Back from Confirm Section
- **Test Case ID:** MERGE-REL-017
- **Description:** Verify the ability to click "Back" to go to the "Merge data" section from the "Confirm" section.
- **Steps:**
    1. Navigate to the "Merge Release" page.
    2. Locate the "Confirm" section.
    3. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Merge data" section.
