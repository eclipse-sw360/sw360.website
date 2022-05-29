**TC01: Add a simple project with no relations and no releases**

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed
2 | Click on _Projects_ tab | _Projects_ page is displayed
3 | Click _Add Project_ | _New Project_ page is displayed with mandatory fields marked with red star
4 | Fill mandatory _Name_ with a project name, change other fields if needed | Values are entered in the fields
5 | Click _Add Project_ | The page remain the same and the message _You are editing the original document._ is displayed
6 | Click _Cancel_ button | New project _Summary_ page is displayed
7 | Click on _Projects_ tab | The new project should be added to the projects list

**TC02: Add a full project with relations, releases and send to clearing process**

Step | Action | Result
---:|:-----|:----
1 | Click on _Projects_ tab | _Projects_ page is displayed
2 | Click _Add Project_ | _New Project_ page is displayed with mandatory fields marked with red star
3 | Fill mandatory _Name_ with a project name, change other fields if needed | Values are entered in the fields
4 | Click _Click to add linked Projects_ | _Search Project_ dialog is displayed
5 | Click _Search_ and _Select_ the project to be linked (e.g. created in TC01) | Dialog is closed and selected project is displayed under _Linked Projects_ section
6 | Click _Click to add Releases_ | _Search Release_ dialog is displayed
7 | Click _Search by name_ and _Select_ a release to be added | Dialog is closed and selected release is displayed under _Linked Releases_ section
8 | Click _Add Project_ | The page remain the same and the message _You are editing the original document._ is displayed
9 | Click _Cancel_ button | New project _Summary_ page is displayed
10 | Click on _Projects_ tab | The new project should be added to the projects list
11 | Check _Clearing Status_ by hovering mouse over the numbers. | The message should be _new release, under clearing..._
12 | Send open release to clearing by clicking the button _Send to fossology_, under _Actions_ column | _Fossology Clearing_ dialog is displayed
13 | Select the release to be sent for clearing and click _Send_ | _Sent_ message is displayed near the _Send to fossology_ button
14 | Click on project name and check _Summary_ page | _Clearing details_ should have 1 for _Under clearing_
15 | Click on _Clearing Status_ | The "Release Clearing State_ should be _Sent to Fossology_

**TC03: Add a project with releases, no relations, remove a release, and send to clearing process**

Step | Action | Result
---:|:-----|:----
1-5 | Same as in TC02   
5a | Click on _Delete_ icon to delete the linked project | _Do you really want to remove the link to this project?_ message is displayed  
5b | Click _OK_ | The project is removed from the list of _Linked Projects_  
6 | Click _Click to add Releases_ | _Search Release_ dialog is displayed
7 | Click _Search by name_ and _Select_ more than one release to be added | Dialog is closed and selected releases are displayed under _Linked Releases_ section
7a | Click on _Delete_ icon to delete one of the linked release| _Do you really want to remove the link to this release?_ message is displayed  
7b | Click _OK_ | The release is removed from the list of _Linked Releases_
8-15 | Same as in TC02   

**TC04: Delete a project that is first linked to another project and then not linked**

Step | Action | Result
---:|:-----|:----
1 | Create a new project | Project is created successfully  
2 | Create another project and add first created one as linked project | Projects are linked successfully  
3 | Go to first created project in the projects table and try to delete it | Message _Do you want to delete project name?_ is displayed  
4 | Click _OK_ | Message _The project is used by another project!_ is displayed  
5 | Click _OK_ | Project is not deleted (e.g. refresh the page by clicking Projects tab)  
6 | Go to second created project in the projects table and delete it | Message _Do you want to delete project name?_ is displayed  
7 | Click _OK_ | Project is deleted successfully  
8 | Go to first created project in the table (not linked anymore to second project) and delete it | Project is deleted successfully  

**TC05: Modify an existing project with relations, releases and send to clearing process**

Step | Action | Result
---:|:-----|:----
1 | Search for a simple project (e.g. created in TC01) and click _Edit_ | _You are editing the original document_ message is displayed  
2 | Execute steps 5-16 from TC02

**TC06: Add and modify a project with all project fields filled in**

Step | Action | Result
---:|:-----|:----
1 | Click on _Projects_ tab | _Projects_ page is displayed
2 | Click _Add Project_ | _New Project_ page is displayed with mandatory fields marked with red star
3 | Fill in all editable fields under _Basic Information_, _User Information_ and _Admin Information_ | Values are entered in the fields
4 | Click _Add Project_ | The page remain the same and the message _You are editing the original document._ is displayed
5 | Click _Cancel_ button | New project _Summary_ page is displayed
6 | Check all fields on _Summary_ page | Values are filled in correctly
7 | Click _Edit_ button, modify some fields and _Update Project_ | Values are updated successfully

**TC07: Duplicate an existing project**

Step | Action | Result
---:|:-----|:----
1 | Search for an existing project with all fields filled in (e.g. created in TC06) and click _Duplicate_ button under _Actions_ column | Project _Information_ page is displayed
2 | Check all fields from copied project | All fields are unchanged, including _Linked Projects_ and _Linked Releases_
3 | Fill mandatory _Name_ with a project name and click _Add Project_ | The page remain the same and the message _You are editing the original document._ is displayed
4 | Click _Cancel_ button | New project _Summary_ page is displayed
5 | Check all fields | All fields were copied successfully, except the new name of the project