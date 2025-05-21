---
title: "Admin Vendors Page"
linkTitle: "Admin Vendors Page"
weight: 350
---

## SW360 "Admin > Vendors" Page Test Cases

### General Page Behavior

#### Quick Filter and Buttons
- **Test Case ID:** ADMIN-VENDORS-001
- **Description:** Verify the presence of the Quick Filter on the left, "Add Vendor" and "Export Spreadsheet" buttons on top, and the Vendors count on the right.
- **Steps:**
    1. Navigate to the "Admin > Vendors" page.
    2. Locate the Quick Filter on the left, the buttons on top, and the Vendors count on the right.
- **Expected Result:** The Quick Filter, buttons, and Vendors count are present.

### Vendors Table

#### Columns
- **Test Case ID:** ADMIN-VENDORS-002
- **Description:** Verify the presence of the specified columns in the Vendors table.
- **Steps:**
    1. Navigate to the "Admin > Vendors" page.
    2. Locate the Vendors table.
    3. Verify the presence of the following columns:
        - Full Name (click to open vendor)
        - Short name
        - URL
        - Actions (edit, merge, and delete)
- **Expected Result:** All specified columns are present and function as described.

---

## SW360 "Add Vendor" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** ADD-VENDOR-001
- **Description:** Verify the presence of the "Create Vendor" and "Cancel" buttons on top.
- **Steps:**
    1. Navigate to the "Add Vendor" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Create Vendor" and "Cancel" buttons are present.

#### Fields
- **Test Case ID:** ADD-VENDOR-002
- **Description:** Verify the presence of the specified fields in the table.
- **Steps:**
    1. Navigate to the "Add Vendor" page.
    2. Locate the table.
    3. Verify the presence of the following fields:
        - Full Name
        - Short Name
        - URL
- **Expected Result:** All specified fields are present and function as described.

### Create Vendor Button

#### Vendor Creation and Redirection
- **Test Case ID:** ADD-VENDOR-003
- **Description:** Verify that clicking on the "Create Vendor" button shows the message "Vendor created" and redirects the user to the Vendors main page.
- **Steps:**
    1. Navigate to the "Add Vendor" page.
    2. Fill in the required fields.
    3. Click on the "Create Vendor" button.
- **Expected Result:** The message "Vendor created" is shown, and the user is redirected to the Vendors main page.

---

## SW360 "Vendor Details" Page Test Cases

### General Page Behavior

#### Opening Vendor Edit Page
- **Test Case ID:** VENDOR-DTL-001
- **Description:** Verify that clicking on the Vendor Name opens the Vendor Edit Page.
- **Steps:**
    1. Navigate to the "Vendor Details" page.
    2. Click on the Vendor Name.
- **Expected Result:** The Vendor Edit Page is opened.

---

## SW360 "Vendor Edit" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** VENDOR-EDIT-001
- **Description:** Verify the presence of the "Update Vendor", "Delete Vendor", and "Cancel" buttons on top left, and the Vendor full name on top right.
- **Steps:**
    1. Navigate to the "Vendor Edit" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Update Vendor", "Delete Vendor", and "Cancel" buttons are present, and the Vendor full name is displayed on the top right.

#### Editable Fields
- **Test Case ID:** VENDOR-EDIT-002
- **Description:** Verify the presence of the specified editable fields in the Vendor table.
- **Steps:**
    1. Navigate to the "Vendor Edit" page.
    2. Locate the Vendor table.
    3. Verify the presence of the following editable fields:
        - Full Name
        - Short Name
        - URL
- **Expected Result:** All specified editable fields are present and function as described.

### Update Vendor Button

#### Vendor Update and Redirection
- **Test Case ID:** VENDOR-EDIT-003
- **Description:** Verify that clicking on the "Update Vendor" button saves the changes and redirects the user to the Vendor Details page.
- **Steps:**
    1. Navigate to the "Vendor Edit" page.
    2. Make changes to the fields.
    3. Click on the "Update Vendor" button.
- **Expected Result:** The changes are saved, and the user is redirected to the Vendor Details page.
