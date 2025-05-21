---
title: "Admin User Page"
linkTitle: "Admin User Page"
weight: 340
---

## SW360 "Admin > User" Page Test Cases

### Advance Search on the Left Panel

#### Search Fields
- **Test Case ID:** ADMIN-USER-001
- **Description:** Verify the presence of the advance search on the left panel with the specified fields.
- **Steps:**
    1. Navigate to the "Admin > User" page.
    2. Locate the advance search section on the left panel.
    3. Verify the presence of the following search fields:
        - Given Name
        - Last Name
        - Email
        - Primary Department
        - Primary Department Role (dropdown)
    4. Click on the "Search" button.
- **Expected Result:** The search fields are present, and clicking the "Search" button loads the results in the same page.

### Users Count

#### Display of Users Count
- **Test Case ID:** ADMIN-USER-002
- **Description:** Verify the display of the users count in the top right.
- **Steps:**
    1. Navigate to the "Admin > User" page.
    2. Locate the top right section of the page.
- **Expected Result:** The users count is displayed in the top right.

### Users Table

#### Columns
- **Test Case ID:** ADMIN-USER-003
- **Description:** Verify the presence of the specified columns in the Users table.
- **Steps:**
    1. Navigate to the "Admin > User" page.
    2. Locate the Users table.
    3. Verify the presence of the following columns:
        - Given name
        - Last name
        - Email (click to open user)
        - Active status
        - Primary Department
        - Primary Department Role
        - Secondary Departments and Roles (unordered list of Department (bold) and role)
        - Actions (Edit and Edit secondary department)
    4. Click on the "Edit secondary department" action to verify the popup for Secondary department and role.
- **Expected Result:** All specified columns are present and function as described. Clicking on "Edit secondary department" opens a popup for Secondary department and role.

---

## SW360 "User Details" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** USER-DTL-001
- **Description:** Verify the presence of the "Edit User" button on the top left and the user email on the top right.
- **Steps:**
    1. Navigate to the "User Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Edit User" button and user email are present.

### User Information Section

#### Fields
- **Test Case ID:** USER-DTL-002
- **Description:** Verify the presence of the specified fields in the User Information section.
- **Steps:**
    1. Navigate to the "User Details" page.
    2. Locate the User Information section.
    3. Verify the presence of the following fields:
        - Given name
        - Last name
        - Email Id
        - Global Identifier (external ID)
        - Active status
        - Department
        - Primary roles
        - Secondary Department and Roles (as unordered list)
- **Expected Result:** All specified fields are present and function as described.

---

## SW360 "User Edit" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** USER-EDIT-001
- **Description:** Verify the presence of the "Update User", "Deactivate User", and "Cancel" buttons on top, and the user email on the top right.
- **Steps:**
    1. Navigate to the "User Edit" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Update User", "Deactivate User", and "Cancel" buttons are present, and the user email is displayed on the top right.

### General Information Section

#### Editable Fields
- **Test Case ID:** USER-EDIT-002
- **Description:** Verify the presence of the specified editable fields in the General Information section.
- **Steps:**
    1. Navigate to the "User Edit" page.
    2. Locate the General Information section.
    3. Verify the presence of the following editable fields:
        - Given name
        - Last name
        - Email ID
        - Gobal Identifier
        - Department
        - Primary roles
- **Expected Result:** All specified editable fields are present and function as described.

### Secondary Departments and Roles Section

#### Fields and Buttons
- **Test Case ID:** USER-EDIT-003
- **Description:** Verify the presence of the specified fields and buttons in the Secondary Departments and Roles section.
- **Steps:**
    1. Navigate to the "User Edit" page.
    2. Locate the Secondary Departments and Roles section.
    3. Verify the presence of the following fields and buttons:
        - Secondary department (text box)
        - Secondary department role (dropdown)
        - delete row button
        - "Click to add" button below
- **Expected Result:** All specified fields and buttons are present and function as described.

### Update User Button

#### User Update and Redirection
- **Test Case ID:** USER-EDIT-004
- **Description:** Verify that clicking on the "Update User" button saves the changes and redirects the user to the user's detail page.
- **Steps:**
    1. Navigate to the "User Edit" page.
    2. Make changes to the fields.
    3. Click on the "Update User" button.
- **Expected Result:** The changes are saved, and the user is redirected to the user's detail page.
