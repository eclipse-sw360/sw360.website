**TC01: Accept moderation request, for visible projects by other users**

Step | Action | Result
---:|:-----|:----
1 | Open first browser instance ((e.g. "firefox.exe -p "profile1" -no-remote") and sign in with a known _First_ user | User successfully signed in and _Home_ page is displayed
2 | Open a second browser instance ((e.g. "firefox.exe -p "profile2" -no-remote") and sign in with a known _Second_ user | User successfully signed in and _Home_ page is displayed
3 | Activate _First_ browser instance | Instance is active
4 | Create a new project visible for _Second_ user (e.g. _Me and Moderators_, _Group and Moderators_, _Everyone_) | Project is created successfully
5 | Activate _Second_ browser instance | Instance is active
6 | Search for the above created project and click _Edit_ | _You will create a moderation request if you update._ message is displayed 
7 | Edit Description field or other fields and click _Update Project_ | _Moderation request was sent to update the Project name!_ message is displayed.
8 | Activate _First_ browser instance | Instance is active
9 | Check _My Task Assignments_ on _Home_ page | The above project that needs moderation is displayed with status _PENDING_
10 | Click on _Moderation_ page | The moderation request of _Second_ user is displayed with state _Pending_
11 | Click on moderation request | _Moderation Change Project_ page is displayed, with proposed changes from step 7 listed
12 | Click on _Accept Request_ | _You have accepted the previous moderation request._ message is displayed, and State changes to _Approved_
13 | Check _My Task Assignments_ on _Home_ page | Status is _APPROVED_
14 | Activate _Second_ browser instance | Instance is active
15 | Check _My Task Submissions on _Home_ page | Status is _APPROVED_
16 | Open the _Projects_ tab and click on previously modified project on step 7 | Project _Summary_ page displayed successfully
17 | Check the moderation requested changes | Changes are visible in the corresponding fields

**TC02: Decline moderation request, for visible projects by other users**

Step | Action | Result
---:|:-----|:----
1-11 | Same as in TC01
12 | Click on _Decline Request_ | _You have declined the previous moderation request_ message is displayed, and State changes to _Rejected_
13 | Check _My Task Assignments_ on _Home_ page | Status is _REJECTED_
14 | Activate _Second_ browser instance | Instance is active
15 | Check _My Task Submissions on _Home_ page | Status is _REJECTED_
16 | Open the _Projects_ tab and click on previously modified project on step 7 | Project _Summary_ page displayed successfully
17 | Check the moderation requested changes | Changes are not visible in the corresponding fields

**TC03: Remove Me from Moderators for moderation request, for visible projects by other users**

Step | Action | Result
---:|:-----|:----
1-11 | Same as in TC01
12 | Click on _Remove Me from Moderators_ | _You are the last moderator for this request - you are not allowed to unsubscribe._ message is displayed (assuming only _First_ user was listed under _Moderators_ column in step 10) 
13 | Click on _Decline Request_ | _You have declined the previous moderation request_ message is displayed, and State changes to _Rejected_
14 | Edit the project and add a new moderator (e.g. _Third_ user) under _Moderators_ field | Project updated successfully.
15 | Activate _Second_ browser instance | Instance is active
16 | Edit the project and create a new moderation request | Moderation request was sent
17 | Activate _First_ browser instance | Instance is active
18 | Click on _Moderation_ page | The moderation request of _Second_ user is displayed with state _Pending_
19 | Click on moderation request | _Moderation Change Project_ page is displayed, with proposed changes from step 7 listed
20 | Click on _Remove Me from Moderators_ | _You are removed from the list of moderators for the previous moderation request. You have no open Requests._ message is displayed. Also the document is deleted from moderation list.
21 | Login with the _Third_ user and check the _Moderation_ tab | The moderation request of _Second_ user is displayed with state _Pending_