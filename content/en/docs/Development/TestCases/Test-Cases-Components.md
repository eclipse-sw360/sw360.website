---
title: "Component / Release"
linkTitle: "Component / Release"
weight: 10
---

## TC01: Add a component and release with vendor present

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Components_ tab | _Components_ page is displayed
3 | Click _Add Component_ button | - _New Component_ page is displayed with mandatory fields marked with red star: Name, Categories, Component Type. <br>- A message _Success:New Component_ is displayed
4 | Fill in a component _Name_, _Categories_ and _Component Type_ fields. <br>_Eg:_<br>- Name: Component 1@1<br>- Categories: Categories_1@1<br>- Component Type: OSS | Values are entered in the fields
5 | Click _Create Component_ button | - Create component successfully. <br>- Redirect to the edit component page.<br>-Show message: _Success:You are editing the original document._
6 | Click _Releases_ tab<br>Click _Add Release_ button | Redirect to Add Release page
7 | Fill in a release _Version_ and _CPE ID_<br>_Eg:_<br>- Version: version1.0.0.x<br>- CPE ID: UUID_1002 | Values are entered in the fields:<br>- Version: version1.0.0.x<br>- CPE ID: UUID_1002
8 | Click _Create Release_ button | - Create a release successfully.<br>- Redirect to the edit new release page.<br>- The message _Success:You are editing the original document._ is displayed
9 | Click _Vendor_ field | _Search Vendor_ dialog is displayed
10 | Click _Add Vendor_ button | _Create new Vendor_ dialog display
11 | Input data in fields<br>- Full Name: add vendor 01<br>-Short Name: add vendor01<br>-URL: <https://github.com/eclipse-sw360/sw360> | Values are entered in the fields.
12 | Click _Add Vendor_ button | The vendor is added in Vendor field of the release with full name is _add vendor 01_
13 | Click _Attachments_ tab | _Attachments_ page is displayed
14 | Click _Add Attachment_ button | _Upload Attachment_ dialog is displayed
15 | Click _Browse_ and select the attachment.<br>Eg: attachment1.xlsx | File name is displayed in the dialog
16 | Click _Upload_ button | The file is uploaded and dialog is closed. Also the attached file is listed in the _Attachment_ page
17 | Change the attachment _Type_ to real type.<br>Eg: Component license information (Combined) | Type changed successfully
18 | Click _Update Release_ button | Message: _Success:Release {name} ({version}) updated successfully!_ is displayed

## TC02: Verify data after add a component and release with vendor present

Step | Action | Result
---:|:-----|:----
1 | Search for the component is created in TC01:<br>- Click _Components_ portlet<br>- At Advanced Search area, input _Component 1@1_ in the _Component Name_ textbox.<br>- Click _Search_ button | The new component display in the table with:<br>- Vendor: add vendor01<br>- Component Name: _Component 1@1_ is displayed with hyper link.<br>- Main licenses: blank<br>- Component Type: OSS
2 | Click hyper link of name _Component 1@1_ | Redirect to view component _Component 1@1_ page
3 | Click _Release Overview_ tab | The release display with:<br>- Name: Component 1@1<br>- Version displays with hyper link: version1.0.0.x<br>- Clearing State: New<br>- Clearing Report: no report<br>- Release Mainline State: Open
4 | Click hyper link _version1.0.0.x_ | Redirect to view screen of release _Component 1@1 version1.0.0.x_<br>Data of the release:<br>- Summary tab:<br>+ display text with: COMPONENT 1@1 VERSION1.0.0.X<br>+ CPE ID: UUID_1002<br>+ Created on: date of created.<br>+ Created by: user created.<br>+ Modified On: date of modified.<br>+ Modified By: user modified.<br>+ Clearing State: New<br>+ Release Mainline State: Open<br>+ Release Vendor with:<br> &emsp; Full Name: add vendor 01<br> &emsp; Short Name: add vendor01<br> &emsp; URL: <https://github.com/eclipse-sw360/sw360>
5 | Click _Attachments_ tab | Display file name _attachment1.xlsx_ in the table.

## TC03: Modify a component and release with vendor present

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component (e.g. created in TC01: _Component 1@1_) and click _Edit_ icon | _Success:You are editing the original document_ message is displayed
2 | Click _Releases_ tab | Release list is displayed
3 | Click _Add Release_ button | Redirect to Add Release page
4 | Fill in a release _Version_ and _CPE ID_<br>_Eg:_<br>- Version: v1.0.0.1<br>- CPE ID: cpe:id:123456 | Values are entered in the fields:<br>- Version: v1.0.0.1<br>- CPE ID: cpe:id:123456
5 | Click _Create Release_ button | - Redirect to the edit new release page.<br>- The message _Success:You are editing the original document._ is displayed
6 | Click _Vendor_ field | _Search Vendor_ dialog is displayed
7 | Click _Search_ button.<br>Select a vendor (eg: select  vendor with full name _VendorUp_) <br>Click _Select Vendor_ button. | Dialog is closed and selected Vendor is  added under _Vendor_ field: VendorUp
8 | Click _Attachments_ tab<br>Click _Add Attachment_ button<br>Click _Browse_ and select the attachment. Eg:  attachment2.img<br>Click _Upload_ button | The file is uploaded and dialog is closed.  Also the attached file is listed in the Attachment page
9 | Click _Update Release_ button | Message _Success:Release Component 1@1  (v1.0.0.1) updated successfully!_ is displayed

## TC04: Verify data after  modify a component and release with vendor present

Step | Action | Result
---:|:-----|:----
1 | Continue TC03 |
2 | Click _Summary_ tab | Data in the tab:<br>- Modified On: date of modified.<br>- Modified By: user modified.<br>Data of other fields in the tab is same data before updated.
3 | Click _Release Overview_ tab | New release with version _v1.0.0.1_  is added in the release  table.
4 | Click _v1.0.0.1_ hyper link | Text display with: _COMPONENT 1@1  V1.0.0.1_ at the right corner.<br>- At Summary tab: <br>  + CPE ID: cpe:id:123456<br>  + Release Vendor: display with Full Name, Short Name and URL correctly with  vendor _VendorUp_  <br>- At Attachments tab: attachment _attachment2.img_ display in  the attachment table with correct information.
5 | Click _Component 1@1_ hyper link | Redirect to view screen of _Component 1@1_  component.
6 | Click _Attachments_ tab | Data in the tab is same data before updated.
7 | Click _Vulnerabilities_ tab | Data in the tab is same data before updated.

## TC05: Add and modify a component and release with all fields filled in

Step | Action | Result
---:|:-----|:----
1 | Click _Components_ tab<br>Click _Add Component_ button<br>Fill in all editable fields<br>Click _Create Component_ button | - Redirect to edit component screen with the  message _Success:You are editing the original document._ is displayed in the  left corner.<br>- Create component successfully. Data match with input  data.
2 | Click _Releases_ tab.<br>Click _Add Releases_ button.<br>At _Summary_ tab, fill in all editable fields under _Release Summary_ and _Release Repository_.<br>Click _Create Release_ button.<br> | Redirect to edit release screen.<br>Created release successfully. Data match with input data.
3 | Click _Linked Releases_ tab<br>Click _Click to add Releases_ button | The dialog _Link Releases_ is displayed.
4 | Input search name into textbox<br>Click _Search_ button<br>Select 3 releases.<br>Click _Link Releases_ button | Dialog is closed and selected release is displayed under _Linked Releases_ section.
5 | Click _Linked Packages_ tab<br>Click _Add Packages_ button | The dialog _Link Packages_ is displayed.
6 | Input an exist orphan package name into textbox.<br>Click _Search_ button.<br>Select a package.<br>Click _Link Packages_ button. | Dialog is closed and selected package is displayed under _Linked Packages_ table
7 | Click _Clearing Details_ tab<br>Fill in all editable fields | Values are entered in the fields
8 | Click _ECC Details_ tab<br>Fill in all editable fields | Values are entered in the fields
9 | Click _Attachments_ tab<br>Click _Add Attachment_ button<br>Click _Browse_ and select the attachment. _Eg_: attachment3.xlsx<br>Click _Upload_ button | The file is uploaded and dialog is closed. Also the attached file is listed in the Attachment page
10 | Click _Update Release_ button | - _Success:Release {componentName} ({version}) updated successfully!_ message is displayed.<br>- Redirect to the view release screen.
11 | Check all fields of the release by click tabs: _Summary, Linked Releases, Linked Packages, Clearing Details and Attachments_. | Values are filled in correctly, match with input data.
12 | Click _Edit Release_ button, modify some fields.<br>Eg: <br>- _Version_ field ( in _Summary_ tab): rename version name_updated<br>      - _ECC Status_ field (in _ECC Details_ tab): Approved.<br>Click _Update Release_ button. | Values are updated successfully

## TC06: Delete a component that is first linked to a project and then not, and a project

Step | Action | Result
---:|:-----|:----
1 | Create a new component<br>_Eg:_ component with name _Component @1234_ | Component is created successfully
2 | Add a new release to this component<br>_Eg:_ release _Rel1_ | Release is added successfully
3 | Create a new project _P1_ | Project is created successfully
4 | Add the linked release _Rel1_ to project _P1_. | Release linked successfully
5 | Click _Components_ portlet.<br>Search component _Component @1234_ by name at advanced search. | Component _Component @1234_ display on the result table.
6 | Click delete icon of component _Component @1234_ | A warning _The component Component @1234 cannot be deleted, since it contains 1 releases. Please delete the releases first._
7 | Click _OK_ button in the warning dialog. | The dialog is closed, component is not deleted
8 | Click _Components_ portlet.<br>Search for the component _Component @1234_ and click hyper link of component _Component @1234_. | View screen of _Component @1234_ component is display
9 | Click _Release_ Overview.<br>Click Delete icon button of release _Rel1_.<br>Click _Delete Release_ button in the dialog. | - Dialog _Delete Releases_ is displayed.<br>- Delete the release is failure.<br>- The message: _I could not delete the release, since it is used by another component (release) or project_ display.
10 | Go to project _P1_, delete project _P1_. | The project is deleted successfully
11 | Go to component _Component @1234_, at  _Release Overview_ tab, click Delete icon button of release _Rel1_. | Show message: _Do you really want to delete the release {componentName} ({version}) ?_
12 | Click _Delete Release_ button | Release is deleted successfully
13 | Click _Edit Component_ button.<br>Click _Delete Component_ button. | The dialog is displayed with message: _Do you really want to delete the component {componentName} ?_
14 | Click _Delete Component_ button | Component is deleted successfully

## TC07: Add new attachments to an existing release and delete attachments

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component (e.g. created in TC01) and click _Release Overview_ tab | The list of releases are displayed
2 | Click edit icon in the Action column of release version that needs a new attachment. _Eg:_ release _Rel1_. | Edit release _Rel1_ page is displayed.
3 | Click _Attachments_ tab<br>Click _Add Attachment_ button<br>Click _Browse_ and select several attachments.<br>_Eg:_ 5 attachment files (att1, att2, att3, att4, att5) | File names are displayed in the dialog
4 | Click _Delete_ button near some files not to be added.<br>_Eg:_ delete 2 attachment files (att1, att3) | File names are removed from the list
5 | Click _Upload_ button for the remaining files. | The attached file are listed in the _Attachment_ page: att2, att4, att5
6 | Change some _Attachment type_ to real type, e.g. _source file, clearing report, CLI,..._ | Type changed successfully
7 | Click _Update Release_ button | Release _Ree1_ is updated correctly.
8 | Click _Edit Release_ button | _Success:You are editing the original document._ message is displayed
9 | Click _Attachments_ tab | _Attachments_ page is displayed
10 | Click delete icon to delete an attachment | Show message: _Do you really want to delete attachment {attachmentName}({attachmentId})?_
11 | Click _Delete Attachment button_ | Attachment is deleted successfully, data of attachment is removed from attachment table.
12 | Click _Update Release_ button | Release Ree1 is updated correctly with message _Success: Release {componentName}({version}) updated successfully!_

## TC08: Duplicate an existing release

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component with release with all fields filled in (Eg: created in TC05) and click _Release Overview_ | The list of releases are displayed
2 | Click _Duplicate_ button under Action column | The page changes to create duplicate release screen
3 | Check all fields from copied release | - _Summary_ tab:<br>  + _CPE ID_ field: blank<br>  + Remain fields are unchanged (exclude disable fields).<br>- _Linked Releases_ tab: there is no linked release.
4 | Change the _Version_ field and fill in a _CPE ID_.<br>_Eg:_  Version: ver_duplicate<br>       CPE ID: CPE ID_duplicate<br>Click _Create Release_ button | - Redirect to edit release screen.<br>- Create duplicate release is success with message: _Success:You are editing the original document._<br>- Data of duplicate release is correct.
5 | Modify some other fields.<br>_Eg:_ Release Date: 2023-06-12. <br>Click _Clearing Details_ tab | _Clearing Details_ page is displayed and does not contain any field from copied release
6 | Click _Update Release_ button | The release is updated successfully with data correctly
7 | Click component name link on top of the page | Summary page for the component is displayed
8 | Click _Release Overview_ tab | The new copied release is listed among previous releases

## TC09: Search for and create a new vendor for a new release

Step | Action | Result
---:|:-----|:----
1 | Click _Components_ portlet<br>At advanced Search, search for an existing component.<br>_Eg:_ input _Comp1_ in the Component Name text box.<br>Click _Search_ button. | Component _Comp1_ display in the result table.
2 | Click edit icon in Actions column of component _Comp1_. | Edit screen of component _Comp1_ is displayed with message:  _Success:You are editing the original document_
3 | Click _Releases_ tab<br>Click _Add Releases_ button | The page changes to _New Release Edit_ page
4 | Fill in a release _Version_ and _CPE ID_<br>_Eg:_<br>     + Version: @1.0.2<br>     + CPE ID: moshiano_002 | Values are entered in the fields
5 | Click _Vendor_ field | _Search Vendor_ dialog is displayed
6 | Click _Add Vendor_ | _Create New Vendor_ dialog is displayed
7 | Fill in _Full name_, _Short name_ and _URL_<br>_Eg:_<br>Full Name: Fullvendor_0909<br>Short Name: Short_ven090<br>URL: <https://github.com/> | Values are entered in the fields
8 | Click _Add Vendor_ | Dialog closes and the new vendor is displayed in release _Vendor_ field with full name _Fullvendor_0909_
9 | Click _Create Release_ | Redirect to edit release page with the message _Success:You are editing the original document._ is displayed
10 | Click component name link on top of the page | Summary page for the component is displayed. The new vendor for the new release, as well as existing vendors from previous releases are listed under _Vendors_ field for the component

## TC10: Link a release to the project in view component page and check used by projects

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component with release and click _Release Overview_ tab | The list of releases are displayed
2 | Click _Link Project_ button under Action column | The dialog _Link Release to Project_ is displayed with _Link to Project_ button is disabled
3 | Click _Search_ button then choose a project to link | _Link to Project_ button on the dialog is enabled
4 | Click _Link to Project_ button | _The release {component name} ({version}) has been successfully linked to project {project name}_<br>_Click <ins>here<ins>_ _to edit the release relation as well as the project mainline state in the project._ message is displayed
5 | Click _here_ hyperlink in the dialog | Redirect to the _edit project_ page with the release was linked (displayed on  _License Clearing_ page)
6 | Re-open the release at view page and click _Summary_ tab | Used by project information is updated correspondingly

## TC11: Link a release to a project in the view release page

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component with release and click _Release Overview_ tab | The list of releases are displayed
2 | Click _a release name_ hyperlink. Eg: release R1 | Redirect to the _view release_ page
3 | Click _Link to Project_ button | The dialog _Link Release to Project_ is displayed with _Link to Project_ button is disabled
4 | Click _Search_ button then choose a project to link | _Link to Project_ button on the dialog is enabled
5 | Click _Link to Project_ button | _The release {component name} ({version}) has been successfully linked to project {project name}_<br>_Click <ins>here<ins>_ _to edit the release relation as well as the project mainline state in the project._ message is displayed
6 | Click _here_ hyperlink in the dialog | Redirect to the _edit project_ page with the release was linked (displayed on  _License Clearing_ page)

## TC12: Import a new component by .spdx/.xml/ .rdf file

Step | Action | Result
---:|:-----|:----
1 | Click _Components_ tab | _Components_ page is displayed
2 | Click _Import SBOM_ button | A dialog _Upload SBOM_ is displayed
3 | Choose a **_.spdx_** or **_.xml_** or **_.rdf_** file by clicking on the _Browse_ button or drop/draft a file into the dialog | The message is displayed in the dialog: <br> _The new Component and new Release will be created, do you want to import? <br> New Component: {new component names} <br> New Release: {new release names}_
4 | Click _Import_ button | The dialog is closed. New releases and new components are imported successfully

## TC13: Export components without releases

Step | Action | Result
---:|:-----|:----
1 | Click _Components_ tab | _Components_ page is displayed
2 | Click _Export Spreadsheet_ button and choose _Components only_ option | - A new file with name's format _components-{yyyy}-{mm}-{dd}.xlsx_ is downloaded<br>- The content of the downloaded file includes information of all components in the system

## TC14: Export components with releases

Step | Action | Result
---:|:-----|:----
1 | Click _Components_ tab | _Components_ page is displayed
2 | Click _Export Spreadsheet_ button and choose _Components with releases_ option | - New file with name _components-{yyyy}-{mm}-{dd}.xlsx_ is downloaded.<br>- The content of the downloaded file includes information of all components and releases in the system

## TC15: Create a clearing request for a release

Step | Action | Result
---:|:-----|:----
1 | Search for an existing component with releases and click _Release Overview_ tab | The list of releases are displayed
2 | Click _Edit_ button under _Action_ column. Eg: edit release R1 | Redirect to _view release_ page and the message _Success:You are editing the original document._ is displayed
3 | Click _Attachments_ tab, then add a source file (Eg: .rdf file) with _Type_ is _Source file_ | The data is updated correspondingly
4 | Click _Update Release_ button | The message _Success:Release {release name} updated successfully!_ is displayed
5 | Click _Clearing details_ tab, then click _Fossology Process_ icon beside _Clearing State_ field and wait for the process to finish | The message _The FOSSology process already finished. You should find the resulting report as attachment at this release._ is displayed in the _Fossology Process_ dialog
6 | Click _Close_ button in the dialog | The dialog is closed
7 | Reload this page, then click _Attachments_ tab | A new file is listed in _Attachments_ page with name's format _{component name}-{version}-{yyyymmdd}-{hhmm}-SPDX.rdf_
