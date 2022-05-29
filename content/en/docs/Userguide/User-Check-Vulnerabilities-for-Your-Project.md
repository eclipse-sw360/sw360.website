# How to Check for Vulnerabilities Affecting Your Project  

The CVE-Search service of SW360 checks for vulnerabilities that affect releases present in SW360. 
The CVE-search service runs automatically at the time that has been scheduled by one of the `SW360-admins`.
Typically, this will happen at night. So, in the beginning, SW360 does not know any vulnerabilities for your project.

## Vulnerabilites in the Project Portlet

After a CVE-search run has been finished, you can see the number of vulnerabilities associated with your project in the `Projects Portlet`.
To that end, open the `Projects Portlet` and click on your project:

![](./images/UCVulnerabilitiesProject/01_SelectProject.png)

In the `Vulnerabilities tab` on the left hand side, you see the number of vulnerabilites that have been found for the releases that are directly linked 
to your project. Actually, you see two numbers. The left number indicates how many vulnerabilities have not been evaluated or `rated` for this project yet.
Whenever this number is positive, the bullet surrounding the numbers will be red. Otherwise the bullet is grey.
 
![](./images/UCVulnerabilitiesProject/02_NumberOfVulnerabilities.png)

## The Vulnerabilities Tab
To view (and to rate the vulnerabilities for the project), click on the `Vulnerabilities Tab`. A list of vulnerabilities occurs. Each vulnerability has been found
 for one of the releases that are directly linked to your project. In the first column, you see the name of that release.

![](./images/UCVulnerabilitiesProject/03_VulnerabilityListProject.png)

By clicking on the `external id` of a vulnerability, you can view the details of the vulnerability in the `Vulnerability Portlet`. 
More details about the `Vulnerability Portlet` can be found [here](https://github.com/eclipse/sw360/wiki/Doc-Vulnerability-Management#the-vulnerability-portlet).
The column `Priority` contains no special information when using `CVE-Search`, it is used when importing vulnerability information from different sources.
In the column `Matched By`, you see the `distance` with which the vulnerability was found, and in the mouse-over the corresponding `needle` is displayed. 
Below the table, you see a report about how many vulnerabilities in your project were found with which `distance` by `heuristics` and how many of them have been found by a `matching CPE` respectively.
For more details on `distances`, `matches` and `needles`, click [here](https://github.com/eclipse/sw360/wiki/Doc-Vulnerability-Management#heuristics). 
In the column `Title`, the `External id` is repeated, and in the mouse-over, you can read the `description` of the vulnerability.

## Evaluating Vulnerabilities for your Project
If you are allowed to edit the project, you can also `rate` the relevance of the vulnerability for your project. In this case, the column `Relevance for project` contains
drop-down menus, where you can select a `rating` for each vulnerability (compare [here](https://github.com/eclipse/sw360/wiki/Doc-Vulnerability-Management#vulnerability-rating-for-projects)). 
To change the rating for a project, simply select a different value from the drop-down menu, enter a comment and click `OK`. 

![](./images/UCVulnerabilitiesProject/04_ChangeRating.png)

In order to update the number of checked and unchecked vulnerabilities in the bullet of the `Vulnerability tab`, you have to reload. 
After that, you can also view the `history of rating changes` in the mouse-over of the corresponding vulnerability, 
see also [here](https://github.com/eclipse/sw360/wiki/Doc-Vulnerability-Management#change-history-for-vulnerability-ratings-and-verifications). 
 
You can also view the vulnerabilities associated with a `component` and those associated with a `release` in the `Components Portlet`. 
CVE Search associates vulnerabilities with a release in SW360 based on the data that SW360 knows for that release. 
For a `release`, a `security admin` or an `admin` can judge whether a vulnerability does indeed refer to the `release`. 
Vulnerabilities that have been classified as `INCORRECT` by an `admin` or `security admin` are not displayed to `USERs` any more and therefore do not distort the picture for your project.




 

