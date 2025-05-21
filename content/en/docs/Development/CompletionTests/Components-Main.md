---
title: "Components Page"
linkTitle: "Components Page"
weight: 60
---

## SW360 "Main Components" Page Test Cases

### Advance Search on the Left Hand

#### Search Fields
- **Test Case ID:** COMP-001
- **Description:** Verify that the advance search on the left hand contains the specified search fields.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the advance search section on the left hand.
    3. Verify the presence of the following search fields:
        - Component Name
        - Categories
        - Component Type (one of OSS, COTS, Internal, Inner Source, Service, Freeware, Code Snippet)
        - Languages (type to get defaults)
        - Software Platforms (type to get defaults)
        - Operating Systems (type to get defaults)
        - Vendors (type to get values)
        - Main licenses
        - Created by
        - Created on (with filter type adding or removing date field)
        - A checkbox "Exact Match" with a Search button
- **Expected Result:** All specified search fields are present.

#### Search Behavior
- **Test Case ID:** COMP-002
- **Description:** Verify the search behavior based on the "Exact Match" checkbox.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the advance search section on the left hand.
    3. Enter search criteria in the search fields.
    4. Perform a search without checking the "Exact Match" checkbox.
    5. Verify that the endpoint has "luceneSearch=true" and uses full-text search.
    6. Check the "Exact Match" checkbox and perform a search.
    7. Verify that the endpoint has "luceneSearch=false" and uses exact match.
- **Expected Result:** The search behavior changes based on the "Exact Match" checkbox.

### Buttons in Middle

#### "Add Component" Button
- **Test Case ID:** COMP-003
- **Description:** Verify that the "Add Component" button opens a form to create a new component.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Click on the "Add Component" button.
- **Expected Result:** A form to create a new component is opened.

#### "Export Spreadsheet" Dropdown
- **Test Case ID:** COMP-004
- **Description:** Verify that the "Export Spreadsheet" dropdown generates an Excel of the search result with either "Components only" or "Components with releases".
- **Steps:**
    1. Navigate to the Main Components page.
    2. Perform a search using the advance search fields.
    3. Click on the "Export Spreadsheet" dropdown and select an option.
    4. Verify that the exported sheet has restricted data based on the advance search values from the left panel.
    5. Check if the file is downloaded or if a message is shown indicating that an email will be sent based on server configuration.
- **Expected Result:** The Excel file is generated with the correct data, and the file is either downloaded or an email is sent based on server configuration.

### Table in Middle

#### Page Size
- **Test Case ID:** COMP-005
- **Description:** Verify that the table can change page size, with a default of 10.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the table in the middle.
    3. Change the page size and verify the default is 10.
- **Expected Result:** The table page size can be changed, and the default is 10.

#### "Print" Button
- **Test Case ID:** COMP-006
- **Description:** Verify that the "Print" button on the right prints the Table HTML component to the browser.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Print" button on the right of the table.
    3. Click on the "Print" button.
- **Expected Result:** The Table HTML component is printed to the browser.

#### Column "Vendor"
- **Test Case ID:** COMP-007
- **Description:** Verify that the "Vendor" column displays the vendor name.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Vendor" column in the table.
- **Expected Result:** The vendor name is displayed.

#### Column "Component Name"
- **Test Case ID:** COMP-008
- **Description:** Verify that the "Component Name" column displays the component name with a clickable link to open the component.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Component Name" column in the table.
    3. Click on a component name to open the component.
- **Expected Result:** The component name is displayed, and clicking on it opens the component.

#### Column "Main licenses"
- **Test Case ID:** COMP-009
- **Description:** Verify that the "Main licenses" column displays truncated lists of main licenses, with a clickable link to open the license.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Main licenses" column in the table.
- **Expected Result:** The truncated lists of main licenses are displayed, and clicking on a license opens the license.

#### Column "Component Type"
- **Test Case ID:** COMP-010
- **Description:** Verify that the "Component Type" column displays the component type.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Component Type" column in the table.
- **Expected Result:** The component type is displayed.

#### Column "Actions"
- **Test Case ID:** COMP-011
- **Description:** Verify that the "Actions" column shows an Edit Icon or Delete icon.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the "Actions" column in the table.
- **Expected Result:** The Edit Icon or Delete icon is displayed.

#### Pagination Components
- **Test Case ID:** COMP-012
- **Description:** Verify that the table bottom has pagination components.
- **Steps:**
    1. Navigate to the Main Components page.
    2. Locate the table in the middle.
    3. Scroll to the bottom of the table and verify the presence of pagination components.
- **Expected Result:** Pagination components are present at the bottom of the table.
