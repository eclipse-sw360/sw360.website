---
title: "Moderation"
linkTitle: "Moderation"
weight: 10
---

## TC01: Accept moderation request, for visible projects by other users

Step | Action | Result
---:|:-----|:----
1 | Open a first browser instance (Eg: "firefox.exe -p "profile1" -no-remote") and sign in with a known _First_ user | User successfully signed in and _Home_ page is displayed
2 | Open a second browser instance (Eg: "firefox.exe -p "profile2" -no-remote") and sign in with a known _Second_ user | User successfully signed in and _Home_ page is displayed
3 | Activate _First_ browser instance | Instance is active
4 | Create a new project visible for _Second_ user <br> Eg: <br> - Name: Project is created by First user <br> - Project visibility: Everyone | Project is created successfully
5 | Activate _Second_ browser instance | Instance is active
6 | Search for the above created project and click _Edit_ button | _"Success: You will create a moderation request if you update"_ message is displayed 
7 | Edit _Description_ field or other fields <br> Eg: <br> Description: "Update description to create a moderation request!!" <br> Click _Update Project_ button| Create moderation request dialog is displayed
8 | Fill in _Please comment your changes_ field <br> Eg: I want to update this project. Please accept for me. Thanks @@. <br> Click _Send moderation request_ button | Show message: _"Success: Moderation request was sent to update the Project {nameProject} {(version)}!"_
9 | Activate _First_ browser instance | Instance is active
10 | Check status of project in the _MY TASK ASSIGNMENTS_ table on _Home_ page | The above project that needs moderation is displayed with status _Pending_
11 | Click _Requests_ page | The moderation request of _Second_ user is displayed with state _Pending_
12 | Click the project name in the _Document Name_ column | - _"Success: You have assigned yourself to this moderation request."_ message is displayed <br> - _Moderation Request Information_ page is displayed, with proposed changes from step 7 listed
13 | Input a comment in the _Comment on Moderation Decision_ box. Eg: _The request is approved_ <br> Click _Accept Request_ button | Request page display and show message: _"Success: You have accepted the moderation request"_
14 | Click _Closed Moderation Requests_ tab <br> Check state of _Project is created by First user_ project | State changed to _Approved_
15 | Check status of project in the _MY TASK ASSIGNMENTS_ table on _Home_ page | The request is removed from the table
16 | Activate _Second_ browser instance | Instance is active
17 | Check status of project in the _MY TASK SUBMISSIONS_ table on _Home_ page | Status is _Approved_
18 | Open the _Projects_ page and click on previously modified project on step 7 | Project _Summary_ page displayed successfully
19 | Check the moderation requested changes | Changes are visible in the corresponding fields: _Description_ field was changed to _"Update description to create a moderation request!!"_

## TC02: Decline moderation request, for visible projects by other users

Step | Action | Result
---:|:-----|:----
1-11 | Same as in TC01
12 | Input a comment in the _Comment on Moderation Decision_ box. Eg: _The request is declined_ <br> Click _Decline Request_ button| Requests page display  and show message: _"Success: You have rejected the moderation request"_
13 | Click _Closed Moderation Requests_ tab <br> Check state of the above rejected project | State changed to _Rejected_
14 | Check status of project in the _MY TASK ASSIGNMENTS_ table on _Home_ page | The request is removed from the table
15 | Activate _Second_ browser instance | Instance is active
16 | Check status of project in the _MY TASK SUBMISSIONS_ table on _Home_ page | Status is _Rejected_
17 | Open the _Projects_ page and click on previously modified project on step 7 | Project _Summary_ page displayed successfully
18 | Check the moderation requested changes | Changes are not visible in the corresponding fields: data of the project is not changed.

## TC03: Remove Me from Moderators for moderation request, for visible projects by other users

Step | Action | Result
---:|:-----|:----
1-11 | Same as in TC01
12 | Click _Remove Me from Moderators_ button | - _"Warning: You are the last moderator for this request, you are not allowed to unsubscribe !"_ message is displayed (assuming only _First_ user was listed under _Moderators_ column in step 10) <br> - Can't remove from Moderators. Nothing to change
13 | Input a comment in the _Comment on Moderation Decision_ box. Eg: _Decline the request._ <br> Click _Decline Request_ button| Requests page display  and show message: _"Success: You have rejected the moderation request"_
14 | Edit the project and add a new moderator (Eg: _Third_ user) under _Moderators_ field | Project updated successfully
15 | Activate _Second_ browser instance | Instance is active
16 | Edit the project and create a new moderation request | Moderation request was sent
17 | Activate _First_ browser instance | Instance is active
18 | Click _Moderation_ page | The moderation request of _Second_ user is displayed with state _Pending_
19 | Click the project name which the moderation was created in step 16 | - _"Success: You have assigned yourself to this moderation request."_ is displayed <br> - _Moderation Request Information_ page is displayed, with proposed changes from step 16 listed
20 | Click _Remove Me from Moderators_ button| _"Success: You have unassigned yourself from the moderation request"_ message is displayed. Also the document is deleted from moderation list.
21 | Login with the _Third_ user and check the _Moderation request_ in _Request_ page | The moderation request of _Second_ user is displayed with state _Pending_