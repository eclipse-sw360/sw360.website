---
title: "Merge Components"
linkTitle: "Merge Components"
weight: 130
---

## SW360 "Merge Components" Page Test Cases

### General Page Behavior

#### Accessing the Merge Components Page
- **Test Case ID:** COMP-MRG-001
- **Description:** Verify that the merge components page can be reached by clicking the "Merge" button on a component. The component from which the button was clicked is called the Target component.
- **Steps:**
    1. Navigate to the "Component Details" page of a component.
    2. Click on the "Merge" button.
- **Expected Result:** The merge components page is opened with the Target component specified.

### Choose Source Section

#### Source Components Table
- **Test Case ID:** COMP-MRG-002
- **Description:** Verify the display of the table with all components except the Target component, with a search bar on top.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Choose source" section.
    3. Verify the presence of a table with the following columns:
        - Component Name
        - Created by
        - Releases (count)
- **Expected Result:** The table with the specified columns is present, and the search bar is functional.

#### Selecting a Source Component
- **Test Case ID:** COMP-MRG-003
- **Description:** Verify the process of choosing one source component and clicking "Next."
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Choose source" section.
    3. Select a source component from the table.
    4. Click on the "Next" button.
- **Expected Result:** The selected source component is chosen, and the page navigates to the "Merge data" section.

### Merge Data Section

#### Display of Data
- **Test Case ID:** COMP-MRG-004
- **Description:** Verify the display of all data from the Target component on the left and the Source component on the right with a `<=` button in between.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
- **Expected Result:** The data from the Target component is displayed on the left, and the Source component data is displayed on the right with a `<=` button in between.

#### Data Carry Forward
- **Test Case ID:** COMP-MRG-005
- **Description:** Verify that the data on the left will be carried forward to the Target component.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
- **Expected Result:** The data on the left is carried forward to the Target component.

#### Created by Info Hover
- **Test Case ID:** COMP-MRG-006
- **Description:** Verify the presence of an info hover for the "Created by" field.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
    3. Hover over the "Created by" field.
- **Expected Result:** The info hover is present.

#### `<=` Button Action
- **Test Case ID:** COMP-MRG-007
- **Description:** Verify the action of pressing the `<=` button.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
    3. Press the `<=` button.
- **Expected Result:** The action can be undone with the undo button.

#### Conflict Releases
- **Test Case ID:** COMP-MRG-008
- **Description:** Verify the behavior of releases with the same version.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
    3. Press the `<=` button on releases with the same version.
- **Expected Result:** The undo button is disabled, and a conflict is indicated.

#### Finalizing Data
- **Test Case ID:** COMP-MRG-009
- **Description:** Verify the process of finalizing data and clicking "Next."
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
    3. Finalize the data.
    4. Click on the "Next" button.
- **Expected Result:** The page navigates to the "Confirm" section.

#### Going Back
- **Test Case ID:** COMP-MRG-010
- **Description:** Verify the ability to click "Back" to go to the "Merge data" section.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Merge data" section.
    3. Click on the "Next" button to go to the "Confirm" section.
    4. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Merge data" section.

### Confirm Section

#### Display of Data
- **Test Case ID:** COMP-MRG-011
- **Description:** Verify that only the data on the left is displayed in the "Confirm" section.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Confirm" section.
- **Expected Result:** Only the data on the left is displayed.

#### Merge Selection Payload
- **Test Case ID:** COMP-MRG-012
- **Description:** Verify that only the displayed data is sent as the merge selection payload.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Confirm" section.
    3. Click on the "Finish" button.
- **Expected Result:** Only the displayed data is sent as the merge selection payload.

#### Submitting the Merge
- **Test Case ID:** COMP-MRG-013
- **Description:** Verify the process of clicking "Finish" to submit the merge.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Confirm" section.
    3. Click on the "Finish" button.
- **Expected Result:** The merge is submitted, and the user lands on the Component Details page of the Target component.

#### Going Back from Confirm Section
- **Test Case ID:** COMP-MRG-014
- **Description:** Verify the ability to click "Back" to go to the "Merge data" section from the "Confirm" section.
- **Steps:**
    1. Navigate to the "Merge Components" page.
    2. Locate the "Confirm" section.
    3. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Merge data" section.
