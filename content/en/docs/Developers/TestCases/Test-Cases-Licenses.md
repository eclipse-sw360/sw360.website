**TC01: Create, edit and delete license**

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known _clearing admin_ user | User successfully signed in and _Home_ page is displayed		
2 | Click on _Licenses_ tab | _Licenses_ page is displayed
3 | Click on _Add License_ | _New License_ page is displayed
4 | Fill in _Fullname_ and _Shortname_ fields and press _Add License_ | _License added successfully!_ message is displayed
5 | Write the license or part of newly created license name in _Keyword Search_ field | License is filtered successfully
6 | Click on license name and then on _Edit License Details and Text_ | License page is displayed
7 | Modify some fields and click _Update License_ | _License updated successfully!_ message is displayed
8 | Check all fields on _Details_ and _Text_ pages | Values are filled in correctly
9 | Click on _Edit License Details and Text_ | License page is displayed
10 | Click o _Delete_ license name | _License removed successfully!_ message is displayed

**TC02: Edit license TODOs and Obligations**

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known _clearing admin_ user | User successfully signed in and _Home_ page is displayed		
2 | Click on previously created license name | _License Details_ page is displayed
3 | Click on _Add a Todo_ | Todo page displayed successfully
4 | Enter a Todo text (e.g. "First todo text"), click _Applies to development_, and click _Submit_ | _License updated successfully!_ message is displayed
5 | Click _TODOs and Obligations_ | The previously entered Todo is listed on the page with _No obligations_
6 | Click on _Add a Todo_ | Todo page displayed successfully
7 | Enter a Todo text (e.g. "Second todo text"), click on some Obligations and click Submit | _License updated successfully!_ message is displayed
8 | Click TODOs and Obligations | The previously entered Todo is listed on the page together with chosen obligations
9 | Click on _Edit WhiteList_, deselect first Todo and click _Submit_ | The deselected Todo is not displayed anymore on _TODOs and Obligations_ page

**TC03: Check Export Licenses**

Step | Action | Result
---:|:-----|:----
1 | Sign In with a known user | User successfully signed in and _Home_ page is displayed		
2 | Click on _Licenses_ tab | _Licenses_ page is displayed
3 | Click on _Export Licenses_ | A dialog for opening _Licenses.xlsx_ is displayed
4 | Open the xlsx file and compare the number of rows with total number of entries from _Licenses_ tab | All licenses names are exported successfully.
