---
title: "Split Components"
linkTitle: "Split Components"
weight: 140
---

## SW360 "Split Component" Page Test Cases

### General Page Behavior

#### Accessing the Split Component Page
- **Test Case ID:** COMP-SPLT-001
- **Description:** Verify that the split component page can be reached by clicking the "Split" button on a component. The component from which the button was clicked is called the Source component.
- **Steps:**
    1. Navigate to the "Component Details" page of a component.
    2. Click on the "Split" button.
- **Expected Result:** The split component page is opened with the Source component specified.

### Choose Target Section

#### Target Components Table
- **Test Case ID:** COMP-SPLT-002
- **Description:** Verify the display of the table with all components except the Source component, with a search bar on top.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Choose target" section.
    3. Verify the presence of a table with the following columns:
        - Component Name
        - Created by
        - Releases (count)
- **Expected Result:** The table with the specified columns is present, and the search bar is functional.

#### Selecting a Target Component
- **Test Case ID:** COMP-SPLT-003
- **Description:** Verify the process of choosing one target component and clicking "Next."
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Choose target" section.
    3. Select a target component from the table.
    4. Click on the "Next" button.
- **Expected Result:** The selected target component is chosen, and the page navigates to the "Split data" section.

### Split Data Section

#### Display of Data
- **Test Case ID:** COMP-SPLT-004
- **Description:** Verify the display of all data from the Source component on the left and the Target component on the right with a `=>` button in between for releases and attachments.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
- **Expected Result:** The data from the Source component is displayed on the left, and the Target component data is displayed on the right with a `=>` button in between for releases and attachments.

#### Data Carry Forward
- **Test Case ID:** COMP-SPLT-005
- **Description:** Verify that the releases and attachments on the right will be carried forward to the Target component.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
- **Expected Result:** The releases and attachments on the right are carried forward to the Target component.

#### `=>` Button Action
- **Test Case ID:** COMP-SPLT-006
- **Description:** Verify the action of pressing the `=>` button.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
    3. Press the `=>` button.
- **Expected Result:** The action can be undone with the undo button.

#### Conflict Releases
- **Test Case ID:** COMP-SPLT-007
- **Description:** Verify the behavior of releases with the same version.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
    3. Press the `=>` button on releases with the same version.
- **Expected Result:** The undo button is disabled, and a conflict is indicated.

#### Finalizing Data
- **Test Case ID:** COMP-SPLT-008
- **Description:** Verify the process of finalizing data and clicking "Next."
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
    3. Finalize the data.
    4. Click on the "Next" button.
- **Expected Result:** The page navigates to the "Confirm" section.

#### Going Back
- **Test Case ID:** COMP-SPLT-009
- **Description:** Verify the ability to click "Back" to go to the "Split data" section.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Split data" section.
    3. Click on the "Next" button to go to the "Confirm" section.
    4. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Split data" section.

### Confirm Section

#### Display of Data
- **Test Case ID:** COMP-SPLT-010
- **Description:** Verify that the data in the "Confirm" section is similar to the "Split data" section without the buttons.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Confirm" section.
- **Expected Result:** The data is displayed similarly to the "Split data" section without the buttons.

#### Submitting the Split
- **Test Case ID:** COMP-SPLT-011
- **Description:** Verify the process of clicking "Finalize" to submit the split.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Confirm" section.
    3. Click on the "Finalize" button.
- **Expected Result:** The split is submitted, and the user lands on the Component Details page of the Source component.

#### Going Back from Confirm Section
- **Test Case ID:** COMP-SPLT-012
- **Description:** Verify the ability to click "Back" to go to the "Split data" section from the "Confirm" section.
- **Steps:**
    1. Navigate to the "Split Component" page.
    2. Locate the "Confirm" section.
    3. Click on the "Back" button.
- **Expected Result:** The page navigates back to the "Split data" section.
