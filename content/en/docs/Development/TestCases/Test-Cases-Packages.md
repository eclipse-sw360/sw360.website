---
title: "Packages"
linkTitle: "Packages"
weight: 10
---

## TC01: Create a package with required fields

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click _Packages_ tab <br> Click _Add Package_ button| The _Create Package_ page is displayed
3 | Input valid data into required fields <br> _Eg:_ <br> - Name: package1 <br> - Version: 1.0.0 <br> - Package Type: Framework <br> - PURL (Package URL): pkg:npm/angular-sanitize@1.8.2 | Values are entered in the fields
4 | Click _Create Package_  button | - The message: _"Success: Package created successfully"_ is displayed at the left corner <br> - Redirect to the _Package list_ page <br> - The new package is added to the package list
5 | Search for the new project then click the hyperlink of the newly created package name | Redirect to view page of the created package
6 | Check data of all fields | Data in all fields match with input values

## TC02: Create a package with all fields

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Packages_ tab <br> Click _Add Package_ button | The _Create Package_ page is displayed
2 | Input valid data into all editable fields | Values are entered in the fields
3 | Click _Create Package_  button | - The message: _"Success: Package created successfully"_ is displayed at the left corner <br> - Redirect to the _Package list_ page <br> - The new package is added to the package list
4 | Search for the new package then click the hyperlink of the newly created package name | Redirect to view page of the created package
5 | Check data of all fields | Data in all fields match with input values

## TC03: Update some fields for package

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Component_ tab <br> Create a component with name is _ComponentA_ <br> Create a release with name is _ComponentA (1.0.1)_ | Release _ComponentA (1.0.1)_ is created successfully
2 | Click _Packages_ tab <br> Create a new package with name and version are _Package1 (1.0.1)_ | Package _Package1 (1.0.1)_ is created successfully
3 | At advanced Search, search for newly created package <br> _Eg:_ Package1 (1.0.1) <br> Click _Edit Package_ icon at _Actions_ column | _Update Package_ page is displayed
4 | Update data of some fields <br> _Eg:_ <br> - Version: 1.0.2 <br> - Homepage URL: pkg:npm/@microsoft/applicationinsights-web@2.5.11 <br> - Release: ComponentA (1.0.1) | Data is filled in fields match with input values
5 | Click _Update Package_ button | - The message: _"Success: Package updated successfully"_ is displayed at the left corner <br> - Redirect to the package list page
6 | Search for the updated project then click the hyperlink of the package name | Redirect to view page of the updated package
7 | Check data of all fields | Data in all fields match with data at update page

## TC04: Link package to project with release of the package has not linked to the project yet

Step | Action | Result
---:|:-----|:----
1 | Create Component with name is _ComponentA_ <br> Create a release with name is _ComponentA (1.0.1)_| Release is created successfully  
2 | Click _Packages_ tab <br> Click _Add Package_ button <br>Create a new package with: <br> - Name: _PackageA_ <br> - Version: _(1.0.1)_ <br> - Release: _ComponentA (1.0.1)_| Package is created successfully  
3 | Click _Project_ tab <br> Create project with name is _ProjectA_ | Project is created successfully
4 | In _Edit ProjectA project_ page then click _Linked Packages_ tab <br> Click _Add Packages_ button | Dialog _Link Packages_ is displayed
5 | Input _PackageA_ in textbox then click _Search_ button <br> Choose _PackageA_ package then click _Link Packages_ button | Information of the _PackageA_ package is displayed correctly in the table
6 | Click _Update Project_ button | - Redirect to the _ProjectA_ project view screen <br>  - Information of _Linked Package_ tab is correct with input data
7 | Click _License Clearing_ tab, check information of the table | Display data of _ComponentA (1.0.1)_ release with correctly information

## TC05: Unlink package from the project

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Packages_ tab <br> Create a new package with name and version are _PackageA (1.0.1)_| Package is created successfully
2 | Click _Project_ tab <br> Create a project with name is _ProjectA_ and then add _PackageA_ newly created as linked package of _ProjectA_ project | Project is created successfully
3 | In edit project page, click _Linked Packages_ tab <br> Click _Delete_ icon of PackageA (1.0.1) package <br> Click _Delete Link_ button | Data of _PackageA (1.0.1)_ package is removed from package table
4 | Click _Update Project_ button | - Redirect to view _ProjectA_ page <br> - Project _ProjectA_ is updated successfully <br> - Data in the _Linked Packages_ tab: _PackageA (1.0.1)_ package information is removed

## TC06: Delete a package that is first linked to a project and then not

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user <br> Click _Packages_ tab <br> Create a new package with name and version are _PackageA (1.0.1)_| Package is created successfully
2 | Click _Projects_ tab <br> Create a project with name is _ProjectA_ and then add _PackageA_ newly created as linked package of _ProjectA_ project | Project is created successfully
3 | Click _Packages_ tab <br> At advanced Search, search for newly created package <br> _Eg:_ PackageA(1.0.1) <br> Click _Delete Package_ icon in _Actions_ column of this package | Dialog _"Delete Package?"_ display with message: _"Do you really want to delete the package {packageName} ({package version})?"_
4 | Click _Delete Package_ button | Error message is displayed: _"Package cannot be deleted!"_
5 | Unlink _PackageA_ package from _ProjectA_ project<br> Re-delete _PackageA(1.0.1)_ package follow steps from 3-4| - Delete _PackageA_ package successfully with message "Deleted successfully!" in the dialog <br> - Package _PackageA(1.0.1)_ is not display in the package list table