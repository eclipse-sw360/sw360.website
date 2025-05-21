---
title: "Requests Page"
linkTitle: "Requests Page"
weight: 310
---

## SW360 "Requests" Page Test Cases

### General Page Behavior

#### Moderation Requests and Clearing Requests
- **Test Case ID:** REQ-001
- **Description:** Verify that the page shows both Moderation Requests and Clearing Requests.
- **Steps:**
    1. Navigate to the "Requests" page.
- **Expected Result:** Both Moderation Requests and Clearing Requests are displayed.

### Open Moderation Request Tab

#### Advanced Search
- **Test Case ID:** REQ-002
- **Description:** Verify the presence of the Advanced Search on the left with the specified fields.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Moderation Request Tab.
    3. Verify the presence of the following fields in the Advanced Search:
        - Date
        - Type (dropdown)
        - Document Name
        - Requesting User
        - Department (User Department)
        - Moderators
        - State (Dropdown)
        - Exact Match checkbox
    4. Click on the "Search" button at the bottom to submit the search.
- **Expected Result:** The Advanced Search is present with the specified fields, and the "Search" button is functional.

#### Moderation Count
- **Test Case ID:** REQ-003
- **Description:** Verify the display of the moderation open count/closed count in the top right.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Moderation Request Tab.
- **Expected Result:** The moderation open count/closed count is displayed in the top right.

#### MR Table
- **Test Case ID:** REQ-004
- **Description:** Verify the presence of the specified columns in the MR Table.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Moderation Request Tab.
    3. Verify the presence of the following columns in the MR Table:
        - Date
        - Type
        - Document Name (Click to open)
        - Requesting User (mailto link)
        - Department
        - Moderators (truncated, expanded to see all)
        - State
        - Actions (If open by user to delete)
- **Expected Result:** All specified columns are present and function as described.

#### Pagination Components
- **Test Case ID:** REQ-005
- **Description:** Verify the presence of pagination components around the MR Table.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Moderation Request Tab.
- **Expected Result:** Pagination components are present around the MR Table.

### Closed Moderation Request Tab

#### Advanced Search
- **Test Case ID:** REQ-006
- **Description:** Verify the presence of the Advanced Search on the left like the "Open Moderation Request" Tab.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Moderation Request Tab.
- **Expected Result:** The Advanced Search is present with the specified fields.

#### Moderation Count
- **Test Case ID:** REQ-007
- **Description:** Verify the display of the moderation open count/closed count in the top right.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Moderation Request Tab.
- **Expected Result:** The moderation open count/closed count is displayed in the top right.

#### MR Table
- **Test Case ID:** REQ-008
- **Description:** Verify the presence of the specified columns in the MR Table.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Moderation Request Tab.
    3. Verify the presence of the following columns in the MR Table:
        - Date
        - Type
        - Document Name (Click to open)
        - Requesting User (mailto link)
        - Department
        - Moderators (truncated, expanded to see all)
        - State
        - Actions (If open by user to delete)
- **Expected Result:** All specified columns are present and function as described.

### Open Clearing Request Tab

#### Quick Filter
- **Test Case ID:** REQ-009
- **Description:** Verify the presence of the Quick Filter search box on the left.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Clearing Request Tab.
- **Expected Result:** The Quick Filter search box is present.

#### Advanced Filter
- **Test Case ID:** REQ-010
- **Description:** Verify the presence of the Advanced Filter on the left with the specified fields.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Clearing Request Tab.
    3. Verify the presence of the following fields in the Advanced Filter:
        - Select date type and range (dropdown which shows another dropdown)
        - Priority (dropdown)
        - BA-BL/Group (dropdown)
        - Status (dropdown)
        - Clearing Type (dropdown)
- **Expected Result:** The Advanced Filter is present with the specified fields.

#### Clearing Count
- **Test Case ID:** REQ-011
- **Description:** Verify the display of the clearing open count/closed count in the top right.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Clearing Request Tab.
- **Expected Result:** The clearing open count/closed count is displayed in the top right.

#### Clearing Request Table
- **Test Case ID:** REQ-012
- **Description:** Verify the presence of the specified columns in the Clearing Request Table.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Open Clearing Request Tab.
    3. Verify the presence of the following columns in the Clearing Request Table:
        - Request ID (click to open CR)
        - BA-BL/Group
        - Project (open project)
        - Open Releases
        - Status
        - Priority (color coded)
        - Requesting User (mailto link)
        - Clearing Progress (percentage)
        - Created on
        - Preferred Clearing Date
        - Agreed Clearing Date
        - Clearing Type
        - Actions (edit icon)
- **Expected Result:** All specified columns are present and function as described.

### Closed Clearing Request Tab

#### Quick Filter
- **Test Case ID:** REQ-013
- **Description:** Verify the presence of the Quick Filter search box on the left.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Clearing Request Tab.
- **Expected Result:** The Quick Filter search box is present.

#### Advanced Filter
- **Test Case ID:** REQ-014
- **Description:** Verify the presence of the Advanced Filter on the left with the specified fields.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Clearing Request Tab.
    3. Verify the presence of the following fields in the Advanced Filter:
        - Select date type and range (dropdown which shows another dropdown)
        - BA-BL/Group (dropdown)
        - Status (dropdown)
        - Clearing Type (dropdown)
- **Expected Result:** The Advanced Filter is present with the specified fields.

#### Clearing Count
- **Test Case ID:** REQ-015
- **Description:** Verify the display of the clearing open count/closed count in the top right.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Clearing Request Tab.
- **Expected Result:** The clearing open count/closed count is displayed in the top right.

#### Clearing Request Table
- **Test Case ID:** REQ-016
- **Description:** Verify the presence of the specified columns in the Clearing Request Table.
- **Steps:**
    1. Navigate to the "Requests" page.
    2. Locate the Closed Clearing Request Tab.
    3. Verify the presence of the following columns in the Clearing Request Table:
        - Request ID (click to open CR)
        - BA-BL/Group
        - Project (open project)
        - Open Releases
        - Status
        - Priority (color coded)
        - Requesting User (mailto link)
        - Clearing Progress (percentage)
        - Created on
        - Preferred Clearing Date
        - Agreed Clearing Date
        - Clearing Type
        - Actions (edit icon)
- **Expected Result:** All specified columns are present and function as described.
