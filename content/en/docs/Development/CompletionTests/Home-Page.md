---
title: "Home Page"
linkTitle: "Home Page"
weight: 10
---

## SW360 Project Home Page Test Cases

### General Table Requirements

#### Reload Button
- **Test Case ID:** HOME-001
- **Description:** Verify that each of the 4 sub-tables has a reload button on the top right.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate each of the 4 sub-tables.
    3. Check for the presence of a reload button on the top right of each table.
- **Expected Result:** Each table has a reload button.

#### Pagination Buttons
- **Test Case ID:** HOME-002
- **Description:** Verify that each table has pagination buttons on the bottom.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate each of the 4 sub-tables.
    3. Check for the presence of pagination buttons on the bottom of each table.
- **Expected Result:** Each table has pagination buttons.

#### Empty Message
- **Test Case ID:** HOME-003
- **Description:** Verify that if a table does not have data, it displays an empty message according to the table title.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Check each table for the presence of data.
    3. If a table is empty, verify that the appropriate empty message is displayed.
- **Expected Result:** The appropriate empty message is displayed when the table is empty.

### "My Projects" Table

#### Dropdown Filter
- **Test Case ID:** HOME-004
- **Description:** Verify that the "My Projects" table has a dropdown filter with the specified values.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Projects" table.
    3. Check for the presence of a dropdown filter with the following values:
        - **Role in Project:**
            - Creator
            - Moderator
            - Contributor
            - Project Owner
            - Lead Architect
            - Project Responsible
            - Security Responsible
        - **Clearing State:**
            - Open
            - Closed
            - In Progress
- **Expected Result:** The dropdown filter contains the specified values.

#### Project Details
- **Test Case ID:** HOME-005
- **Description:** Verify that each project in the "My Projects" table is clickable to open the project and displays the description and release counts.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Projects" table.
    3. Click on a project to open it.
    4. Verify that the project name, version, description and release counts are displayed.
- **Expected Result:** Clicking on a project opens the project details page, and the description and release counts are displayed correctly.

### "My Components" Table

#### Component Details
- **Test Case ID:** HOME-006
- **Description:** Verify that the "My Components" table displays the component name, which is clickable to open the component, and the description.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Components" table.
    3. Click on a component name to open it.
    4. Verify that the component description is displayed.
- **Expected Result:** Clicking on a component name opens the component details page, and the description is displayed correctly.

### "My Task Assignments" Table

#### Moderation Requests
- **Test Case ID:** HOME-007
- **Description:** Verify that the "My Task Assignments" table displays the Moderation Requests (assigned to me) document name, which is clickable to open the MR, and the status.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Task Assignments" table.
    3. Click on a document name to open the MR.
    4. Verify that the status is displayed.
- **Expected Result:** Clicking on a document name opens the moderation request, and the status is displayed correctly.

### "My Task Submissions" Table

#### Moderation Requests
- **Test Case ID:** HOME-008
- **Description:** Verify that the "My Task Submissions" table displays the Moderation Requests (open by me) document name, which is clickable to open the MR, the status, and a delete icon to delete the MR.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Task Submissions" table.
    3. Click on a document name to open the MR.
    4. Verify that the status is displayed.
    5. Click on the delete icon to delete the MR.
- **Expected Result:** Clicking on a document name opens the moderation request, the status is displayed correctly, and the delete icon allows the user to delete the MR.

### Right Side of the Page

#### "My Subscriptions" List
- **Test Case ID:** HOME-009
- **Description:** Verify that the "My Subscriptions" list contains all of the user's subscriptions divided by different types and each item is clickable to open.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "My Subscriptions" list on the right side of the page.
    3. Click on an item in the list to open it.
- **Expected Result:** Each item in the list is clickable to open the corresponding subscription.

#### "Recent Components" List
- **Test Case ID:** HOME-010
- **Description:** Verify that the "Recent Components" list shows recent components and each component is clickable to open.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "Recent Components" list on the right side of the page.
    3. Click on a component in the list to open it.
- **Expected Result:** Each component in the list is clickable to open the component details.

#### "Recent Releases" List
- **Test Case ID:** HOME-011
- **Description:** Verify that the "Recent Releases" list shows recent releases and their version, and each release is clickable to open.
- **Steps:**
    1. Navigate to the SW360 project home page.
    2. Locate the "Recent Releases" list on the right side of the page.
    3. Click on a release in the list to open it.
- **Expected Result:** Each release in the list is clickable to open the release details.
