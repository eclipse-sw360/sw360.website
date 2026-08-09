---
title: "Licenses"
linkTitle: "Licenses"
weight: 10
---

## TC01: Create a license with mandatory fields then edit External link

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Licenses_ tab | _Licenses_ page is displayed
3 | Click _Add License_ button | _New License_ page is displayed
4 | Fill in _Fullname_ and _Shortname_ fields<br>_Eg:_<br> - Fullname: Open Logistics Foundation License v1.3 <br> - Shortname: OLFL-1.3 | Values are entered in the fields
5 | Click _Create License_ button | - Navigate to the license list page and the message "Success:License added successfully!" is displayed <br> - The new license should be added to the licenses list
6 | At _Details_ tab, update _External link for more information_ field <br> _Eg:_ https://eclipse.dev/sw360/docs/development/testcases/test-cases-licenses/ <br> Click _Save_ button| - The page remains the same and the message _"Success:SUCCESS"_ is displayed <br> - Data of the _"External link for more information"_ field is updated correctly

## TC02: Create a license with all fields

Step | Action | Result
---:|:-----|:----
1 | Sign in with a known _clearing admin_ user <br> Click _Licenses_ tab <br> Click _Add License_ button | _New License_ page is displayed
2 | Fill in all editable fields <br> _Eg:_ <br> - Fullname: JAM License <br> - Shortname: Jam <br> - License Type: select a license type <br> - OSI Approved?: Yes <br> - Note: take a note! <br> - License Text:  Copyright (C) YEAR by AUTHOR EMAIL Permission to use, copy and modify. | Values are entered in the fields
3 | Click _Linked Obligation_ tab | _Linked Obligation_ page is displayed
4 | Click _Add Obligation_ button | Screen display a dialog: _"Select License Obligations to be added."_
5 | Select some obligations and click _Add_ button | The selected obligations have been added to the obligation table
6 | Click _Create License_ button | - Navigate to the license portlet and the message _"Success:License added successfully!"_ is displayed <br> - The new license should be added to the licenses list
7 | Click the newly created license name hyperlink | The details page of license is displayed
8 | Check data of License in _Details_ tab <br> Click _Text_ tab and check data of License in _Text_ tab <br> Click _Obligations_ tab and check data of License in _Obligations_ tab | The displayed data matches the input data

## TC03: Create a license with linked obligations then edit whitelist

Step | Action | Result
---:|:-----|:----
1 | Sign in with a known _clearing admin_ user <br> Click _Licenses_ tab <br> Click _Add License_ button | _New License_ page is displayed
2 | Fill in _Fullname_ and _Shortname_ <br>_Eg:_<br> - Fullname: Apache License 2.0 <br> - Shortname: Apache-2.0 | Values are entered in the fields
3 | Click _Linked Obligation_ tab | _Linked Obligation_ page is displayed
4 | Click _Add Obligation_ button | Screen display a dialog: _"Select License Obligations to be added"_
5 | Select some obligations and click _Add_ button | The selected obligations have been added to the obligation table
6 | Click _Create License_ button | - Navigate to the license list screen <br> - The new license should be added to the licenses list
7 | Search for new created license, then click _hyper link of new created license_ | The details page of license is displayed
8 | Click _Obligations_ tab | _Obligation_ page is displayed
9 | Click _Edit Whitelist_ button | _Update whitelist_ page is displayed
10 | Unselect  the first obligation then click _Update Whitelist_ button | - Redirect to view license page with the message _"Success:License updated successfully!"_ is displayed <br> - The unselected obligation is not displayed anymore on obligations table

## TC04: Edit License and remove/ add Obligations

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Licenses_ tab <br> At _Quick Filter_ area, input existed license with obligations. E.g: _JAM License_ in the textbox <br> Click _JAM License_ license name <br> Click _Edit License_ button | The update license page is displayed
3 | Edit some editable fields <br> _Eg:_ <br> - Fullname: JAM License 2.0 <br> - OSI Approved?: (n/a) <br> - FSF Free/Libre?: Yes <br> - License Text: <blank> | Values are entered in the fields
4 | Click _Linked Obligation_ tab <br> Click _Delete_ icon of the first obligation in _Action_ column | The _"Delete Obligation?"_ dialog is displayed with message: _"Do you really want to delete the obligation {deleted obligation name}?"_
5 | Click _"Delete Obligation"_ button in the dialog | The chosen obligation is removed from the obligations table
6 | Click _Add Obligation_ button | Screen display a dialog: _"Select License Obligations to be added."_
7 | Select some obligations and click _Add_ button | The selected obligations have been added to the obligation table
8 | Click _Update License_ button | - Navigate to the license details page <br> - Data of the obligation is updated successfully
9 | Click the edited license name (_JAM License 2.0_) | The details page of license is displayed
10 | Check data of License in _Details_ tab, _Text_ tab and _Obligation_ tab | The displayed data matches the input data

## TC05: Delete an existing license

Step | Action | Result
---:|:-----|:----
1 | Sign in with a known _clearing admin_ user <br> Click _Licenses_ tab <br> At _Quick Filter_ area, input existing license in the textbox <br> &ensp; _Eg:_ "License_delete" <br> Click _"License_delete"_ license name in the result table <br> Click _Edit License_ button | The update license page is displayed
2 | Click _Delete License_ button | Screen display dialog with message: _"Do you really want to delete the license {licenseFullName ({licenseShortName})}?"_
3 | Click _Delete License_ button in the dialog | - Navigate to the license portlet and the message _"Success:License removed successfully!"_ is displayed <br> - The removed license has been removed to the license table

## TC06: Check Export Licenses
Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Licenses_ tab | _Licenses_ page is displayed
3 | Click _Export Spreadsheet_ button | A dialog for opening _Licenses.xlsx_ is displayed
4 | Open the newly downloaded _Licenses.xlsx_ file in the local <br> Compare the number of rows with total number of entries from _Licenses_ tab | All licenses names are exported successfully