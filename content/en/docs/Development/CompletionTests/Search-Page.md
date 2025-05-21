---
title: "Search Page"
linkTitle: "Search Page"
weight: 290
---

## SW360 "Search" Page Test Cases

### Keyword Search Panel

#### Search Box
- **Test Case ID:** SEARCH-001
- **Description:** Verify the presence of the search box in the Keyword Search panel on the left.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the Keyword Search panel on the left.
- **Expected Result:** The search box is present.

#### Restrict to Type
- **Test Case ID:** SEARCH-002
- **Description:** Verify the presence of the "Restrict to type" option with an info hover and the specified restrictions.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the "Restrict to type" option in the Keyword Search panel on the left.
    3. Hover over the "Restrict to type" option.
- **Expected Result:** The "Restrict to type" option is present with an info hover, and the specified restrictions are available.

#### Toggle and Deselect All Buttons
- **Test Case ID:** SEARCH-003
- **Description:** Verify the presence of the "Toggle" and "Deselect all" buttons which change the checkboxes in the Restrictions.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the "Toggle" and "Deselect all" buttons in the Keyword Search panel on the left.
    3. Click on the "Toggle" button.
    4. Click on the "Deselect all" button.
- **Expected Result:** The "Toggle" and "Deselect all" buttons are present and function as described.

#### Search Button
- **Test Case ID:** SEARCH-004
- **Description:** Verify the presence of the "Search" button to submit the search.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the "Search" button in the Keyword Search panel on the left.
    3. Click on the "Search" button.
- **Expected Result:** The "Search" button is present and functional.

### Search Result

#### Total Count
- **Test Case ID:** SEARCH-005
- **Description:** Verify the display of the search result total count on the top right.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the top right section of the page.
- **Expected Result:** The search result total count is displayed.

#### Result Table
- **Test Case ID:** SEARCH-006
- **Description:** Verify the presence of the result table with the specified columns.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the result table.
    3. Verify the presence of the following columns:
        - Type (icons matching restriction)
        - Text (Name of document, click to open)
- **Expected Result:** The result table with the specified columns is present.

### Page First Load Message

#### Entire Document Message
- **Test Case ID:** SEARCH-007
- **Description:** Verify the display of the message about "Entire Document" at the bottom of the table on the page first load.
- **Steps:**
    1. Navigate to the "Search" page.
    2. Locate the bottom of the result table.
- **Expected Result:** The message about "Entire Document" is displayed at the bottom of the table.
