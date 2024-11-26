---
title: "Projects"
linkTitle: "Projects"
weight: 10
---

## TC01: Add a simple project with no relations and no releases

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Projects_ tab | _Projects_ page is displayed
3 | Click _Add Project_ button| _New Project_ page is displayed with mandatory fields marked with red star: <br> - Summary tab: Name, Visibility, Project Type, Group <br> - Administration tab: Project State
4 | Fill mandatory _Name_ with a project name, change other fields if needed <br> Eg: <br> - Name: PROJECT_REQUIRED_FIELDS| Values are entered in the fields
5 | Click _Create Project_ button| - Navigate to the new project's viewing screen with the message _"Success: Your project is created"_ is displayed <br> - New project _Summary_ page is displayed
6 | Click _Projects_ tab | - The new project _"PROJECT_REQUIRED_FIELDS"_ should be added to the projects list <br> - Data of the project correctly, matches with input data

## TC02: Add a full project with relations, releases and send to clearing process

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Projects_ tab <br> Click _Add Project_ button <br> Input Name as "A_FULL_PROJECTS" <br> Fill in all editable fields in _Summary_ and _Administration_ links | Values are entered in the fields
2 | Click _Linked Releases And Projects_ link | _Linked Releases And Projects_ page is displayed
3 | Click _Add Projects_ button | _Search Project_ dialog is displayed
4 | Click _Search_ button then select a project to be linked (Eg: created in TC01 "PROJECT_REQUIRED_FIELDS") <br> Click _Link Projects_ button| Dialog is closed and selected project is displayed under _Linked Projects_ section
5 | Click _Add Releases_ button | _Search Release_ dialog is displayed
6 | Click _Search_ button <br> Select releases to be linked <br> Click _Link Releases_ button| Dialog is closed and selected release is displayed under _Linked Releases_ section
7 | Click _Linked Packages_ link | _Linked Packages_ page is displayed
8 | Click _Add Packages_ button | _Search Package_ dialog is displayed
9 | Click _Search_ button in the dialog <br> Select an orphan package to be added then click _Link Packages_ button | Dialog is closed and selected release is displayed under _Linked Packages_ section
10 | Click _Create Project_ button | - Navigate to the new project's viewing screen with the message _"Success: Your project is created"_ is displayed <br> - New project _Summary_ page is displayed
11 | Click _Projects_ tab <br> At _Advanced Search_ area, input _"A_FULL_PROJECTS"_ in the _"Project Name"_ textbox <br> Click _Search_ button| The new project should be added to the projects list with data correctly, matches with input data
12 | In new project, check _Clearing Status_ by hovering mouse over the numbers | The message should be _{number} Releases out of {total number} have approved clearing reports (including sub-projects)._
13 | Click _Create Clearing Request_ icon under _Actions_ column | The dialog _Create Clearing Request_ is displayed
14 | Choose clearing team email id, _Clearing Type_ and _Preferred Clearing Date_  | The data in the fields is displayed as the selected data
15 | Click _Create Request_ button | The message: <br> _Clearing Request {clearing request id} created successfully! <br> Clearing team will confirm on the agreed clearing date._ <br> is displayed in the dialog
16 | Click _Close_ button in the dialog | The dialog is closed
17 | Re-click the _Create Clearing Request_ icon under _Actions_ column | The _View Clearing Request_ dialog is displayed with: <br> - Requesting User: {requested user} <br> - Created on: {created request date} <br> - Preferred Clearing Date: {displayed as input data} <br> - Clearing Team: {email of chosen clearing team} <br> - Priority: LOW <br> - Request Status: NEW
18 | Click _Close_ button in the dialog | The dialog is closed


## TC03: Add a project with releases, no relations, remove a release

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Projects_ tab <br> Click _Add Project_ button <br> Fill mandatory Name with a project name, change other fields if needed <br> Click _Linked Releases And Projects_ link <br> Click _Add Projects_ button | _Search Project_ dialog is displayed
2 | Click _Search_ and select the project to be linked (Eg: created in TC01 "PROJECT_REQUIRED_FIELDS") <br> Click _Link Projects_ button | Dialog is closed and selected project is displayed under _Linked Projects_ section
3 | Click _Delete_ icon to delete the linked project | Message is displayed: _"Do you really want to remove the link to project {linked project name}?"_
4 | Click _Delete Link_ button | The project is removed from the list of _Linked Projects_
5 | Click _Add Releases_ button | _Search Release_ dialog is displayed
6 | Click _Search_ by name and select a release to be added then click _Link Releases_ button| Dialog is closed and selected release is displayed under _Linked Releases_ section 
7 | Click _Delete_ icon to delete the linked release | Message is displayed: _"Do you really want to remove the link to release  {linked release name}?"_
8 | Click _Delete Link_ button | The release is removed from the list of _Linked Releases_
9 | Click _Linked Packages_ link <br> Click _Add Packages_ button | Search Release dialog is displayed
10 | Click _Search_ button in the dialog <br> Select an orphan package to be added then click _Link Packages_ button | Dialog is closed and selected release is displayed under _Linked Packages_ section
11 | Click _Delete_ icon to delete the linked package | Message is displayed: _"Do you really want to remove the link to package  {linked package name}?"_
12 | Click _Delete Link_ button | The release is removed from the list of _Linked Packages_
13 | Click _Create Project_ button | Navigate to the new project's viewing screen with the message _"Success: Your project is created"_ is displayed
14 | Click _Projects_ tab | The new project should be added to the projects list
15 | In newly created project, check _Clearing Status_ by hovering mouse over the numbers of the project | The message should be 0 Releases out of 0 have approved clearing reports (including sub-projects)

## TC04: Delete a project that is first linked to another project and then not linked

Step | Action | Result
---:|:-----|:----
1 | Create a new project with name is _Child Project_ | _Child Project_ project is created successfully 
2 | Create another project with name is _Parent Project_ and add previously created _Child Project_ as linked project of _Parent Project_ | _Parent Project_ project is created successfully with linked project is _Child Project_ project
3 | Click _Projects_ tab <br> At _Advanced Search_ area, input _Child Project_ in the _Project Name_ textbox <br> Click _Search_ button| _Child Project_ project display in the result table  
4 | Click _Delete_ icon to delete _Child Project_ project | Screen display dialog with message: _"Do you really want to delete the project Child Project?"_
5 | Click _Delete Project_ button | Display message in the dialog: _"The project cannot be deleted, since it is used by another project!"_
6 | Click _Cancel_ button | Dialog is closed and _Child Project_ project wasn't deleted in the table
7 | Go to _Parent Project_ project in the project table and delete it <br> Click _Delete_ button | _Parent Project_ project is deleted successfully 
8 | Go to _Child Project_ project in the project table and re-delete it | _Child Project_ project is deleted successfully

## TC05: Modify an existing project with relations, releases and send to clearing process

Step | Action | Result
---:|:-----|:----
1 | Create a new project. Eg: _PROJECT_REQUIRED_FIELDS_  | The project is created successfully
2 | Click _Project_ tab <br> At _Advanced Search_ area, search for a simple project <br> Eg: project created in TC01: input "PROJECT_REQUIRED_FIELDS" in the "Project Name" textbox <br> Click _Search_ button <br> Click _Edit_ icon of "PROJECT_REQUIRED_FIELDS" project | _Summary_ page is displayed <br> Screen display message: _"Success: You are editing the original document."_
3 | Update project name to _PROJECT_REQUIRED_FIELDS_updated_ | Values are entered in the field
4 | Click _Linked Releases And Projects_ link | _Linked Releases And Projects_ page is displayed
5 | Click _Add Projects_ button | _Search Project_ dialog is displayed
6 | Click _Search_ and select the project to be linked (Eg: created in TC02 "A_FULL_PROJECTS") <br> Click _Link Projects_ button | Dialog is closed and selected project is displayed under _Linked Projects_ section
7 | Click _Add Releases_ button | _Search Release_ dialog is displayed
8 | Click _Search_ button <br> Select an release to be added then click "Link Releases" button | Dialog is closed and selected release is displayed under _Linked Releases_ section
9 | Click _Linked Packages_ link | _Linked Packages_ page is displayed
10 | Click _Add Packages_ button | _Search Release_ dialog is displayed
11 | Click _Search_ button in the dialog <br> Select an orphan package to be added then Click _Link Packages_ button | Dialog is closed and selected release is displayed under _Linked Packages_ section
12 | Click _Update Project_ button | - Navigate to the project's viewing screen with the message _"Success: Project {project name} updated successfully!"_ is displayed <br> - The project is updated according to the input data
13 | Click _Projects_ tab <br> At _Advanced Search_ area, input "PROJECT_REQUIRED_FIELDS_updated" in the _Project Name_ textbox <br> Click _Search_ button | The project name _PROJECT_REQUIRED_FIELDS_updated_ is displayed in the project list table
14 | Click _Create Clearing Request_ icon under _Actions_ column | The dialog _Create Clearing Request_ is displayed
15 | Choose clearing team emaild id, _Clearing Type_ and _Preferred Clearing Date_  | The data in the fields is displayed as the selected data
16 | Click _Create Request_ button | The message: <br> _Clearing Request {clearing request id} created successfully! <br> Clearing team will confirm on the agreed clearing date._ <br> is displayed in the dialog
17 | Click _Close_ button in the dialog | The dialog is closed
18 | Re-click the _Create Clearing Request_ icon under _Actions_ column | The _View Clearing Request_ dialog is displayed with: <br> - Requesting User: {requested user} <br> - Created on: {created request date} <br> - Preferred Clearing Date: {displayed as input data} <br> - Clearing Team: {email of chosen clearing team} <br> - Priority: LOW <br> - Request Status: NEW
19 | Click _Close_ button in the dialog | The dialog is closed

## TC06: Add and modify a project with all project fields filled in

Step | Action | Result
---:|:-----|:----
1 | Click _Projects_ tab <br> Click _Add Project_ button <br> Input Name as _A_FULL_BASIC_PROJECT_ <br> Fill in all editable fields in _Summary_ and _Administration_ links | _Projects_ page is displayed | Values are entered in the fields
2 | Click _Create Project_ button | Navigate to the new project's viewing screen with the message _"Success: Your project is created"_ is displayed
3 | Click _Edit Project_ button | Summary page is displayed with message: _"Success: You are editing the original document."_
5 | Modify some fields <br> Eg: <br> - Name: A_FULL_BASIC_PROJECT_changed <br> - Clearing state (in Administration tab): In Progress <br> Click _Update Project_ button | - Screen is display view page and the message _"Success: Project A_FULL_BASIC_PROJECT_changed updated successfully!."_ is displayed <br> - Values are updated successfully

## TC07: Duplicate an existing project

Step | Action | Result
---:|:-----|:----
1 | Search for an existing project with all fields filled in (Eg: created in TC02 A_FULL_PROJECTS project) and click _Duplicate_ button under _Actions_ column | Project _Information_ page is displayed
2 | Check all fields from copied project | - In the Administration tab, the default for the _Clearing State_ field is _Open_<br> - Other fields are duplicated, including _Linked Projects_, _Linked Releases_ and _Linked Packages_
3 | Change version. Eg: 1.0.5-duplicate <br> Click _Create Project_ button| Navigate to the new project's viewing screen with the message _"Success: Your project is created"_ is displayed
4 | Check all fields | All fields were copied successfully, except the new name and _Project Clearing State_ of the project
