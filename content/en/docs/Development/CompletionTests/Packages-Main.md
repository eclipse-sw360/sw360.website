---
title: "Packages Page"
linkTitle: "Packages Page"
weight: 160
---

## SW360 "Main Packages" Page Test Cases

### Advance Search on the Left Hand

#### Search Fields
- **Test Case ID:** PKGS-001
- **Description:** Verify that the advance search on the left hand contains the specified search fields.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the advance search section on the left hand.
    3. Verify the presence of the following search fields:
        - Package Name
        - Package Version
        - Package Manager (one of PackageManager thrift enum)
        - License
        - Created by
        - Created on (with filter type adding or removing date field)
        - "Orphan Package" checkbox
        - A checkbox "Exact Match" with a Search button
- **Expected Result:** All specified search fields are present.

#### Search Behavior
- **Test Case ID:** PKGS-002
- **Description:** Verify the search behavior based on the "Exact Match" checkbox.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the advance search section on the left hand.
    3. Enter search criteria in the search fields.
    4. Perform a search without checking the "Exact Match" checkbox.
    5. Verify that the endpoint has "luceneSearch=true" and uses full-text search.
    6. Check the "Exact Match" checkbox and perform a search.
    7. Verify that the endpoint has "luceneSearch=false" and uses exact match.
- **Expected Result:** The search behavior changes based on the "Exact Match" checkbox.

### Buttons in Middle

#### "Add Package" Button
- **Test Case ID:** PKGS-003
- **Description:** Verify that the "Add Package" button opens a form to create a new package.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Click on the "Add Package" button.
- **Expected Result:** A form to create a new package is opened.

### Table in Middle

#### Page Size
- **Test Case ID:** PKGS-004
- **Description:** Verify that the table can change page size, with a default of 10.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the table in the middle.
    3. Change the page size and verify the default is 10.
- **Expected Result:** The table page size can be changed, and the default is 10.

#### "Print" Button
- **Test Case ID:** PKGS-005
- **Description:** Verify that the "Print" button on the right prints the Table HTML component to the browser.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Print" button on the right of the table.
    3. Click on the "Print" button.
- **Expected Result:** The Table HTML component is printed to the browser.

#### Column "Package Name (Version)"
- **Test Case ID:** PKGS-006
- **Description:** Verify that the "Package Name (Version)" column displays the package name and version, with a clickable link to open the package.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Package Name (Version)" column in the table.
    3. Click on a package name to open the package.
- **Expected Result:** The package name and version are displayed, and clicking on it opens the package.

#### Column "Release Name (Version)"
- **Test Case ID:** PKGS-007
- **Description:** Verify that the "Release Name (Version)" column displays the linked release name, or "No Linked Release" with a clickable link to open the release.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Release Name (Version)" column in the table.
- **Expected Result:** The linked release name is displayed, or "No Linked Release" with a clickable link to open the release.

#### Column "Release Clearing State"
- **Test Case ID:** PKGS-008
- **Description:** Verify that the "Release Clearing State" column displays the clearing state of the release, or "Not Applicable".
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Release Clearing State" column in the table.
- **Expected Result:** The clearing state of the release is displayed, or "Not Applicable".

#### Column "Licenses"
- **Test Case ID:** PKGS-009
- **Description:** Verify that the "Licenses" column displays the licenses.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Licenses" column in the table.
- **Expected Result:** The licenses are displayed.

#### Column "Package Manager"
- **Test Case ID:** PKGS-010
- **Description:** Verify that the "Package Manager" column displays the package manager.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Package Manager" column in the table.
- **Expected Result:** The package manager is displayed.

#### Column "Actions"
- **Test Case ID:** PKGS-011
- **Description:** Verify that the "Actions" column shows an Edit Icon or Delete icon.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the "Actions" column in the table.
- **Expected Result:** The Edit Icon or Delete icon is displayed.

#### Pagination Components
- **Test Case ID:** PKGS-012
- **Description:** Verify that the table bottom has pagination components.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Locate the table in the middle.
    3. Scroll to the bottom of the table and verify the presence of pagination components.
- **Expected Result:** Pagination components are present at the bottom of the table.
