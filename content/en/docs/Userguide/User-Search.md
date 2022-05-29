
This page shows the user which option he has to search in sw360. It can give orientation how the search in sw360 - as guidance or orientation. 

## General Search
 
![general-search](https://github.com/eclipse/sw360/wiki/images/general-search.png)

The user can use the general Search. He can find that under Search at the navigation bar. There he can choose, for what elements (Projects, Components, Releases, Licences, Users, Vendors) he wants to search. Therefore he toogle the elements which should be included in the search.  

### Wildcards 

The user can search with wildcards. A wildcard is a character which substitue for zero or more characters in a string. For a single character users can use '?' and for multiple character wildcard he can use '*'. The Wildcard can stand in the middle of characters or at the end, but not at the beginning.

## Search in Projects, Components and Licenses 
![specific-search](https://github.com/eclipse/sw360/wiki/images/navigationbar-search.png)

The user can use besides of the general search the specific search at the specific view of projects, components and licenses. There he has a Quickfilter and the Advanced Search where he has the option to search more refined.    

##
<img src="https://github.com/eclipse/sw360/wiki/images/sw360_specific_search.png"/><img src="https://github.com/eclipse/sw360/wiki/images/specific-search.png"/>

### Quickfilter

The Quickfilter let the user see the search result immediately when he starts typing. Therefore the Data has to be loaded. At the specific search for components, the user can choose under 'loading' how much components sw360 should load. He can choose between the '200 newest' up to 'all'.  If the user did not use the quickfilter, it makes sense to set the loading option on 200 newest, so he does not unnecessarily slow down the site. <br> 
At the specific search for projects, the user has the option to choose the group for the projects which should get loaded for the quick filter. If the user is just interested in the projects of his group, he should set the group to his group. So he does not load unnecessary projects every time he goes on the project site. Note that you cannot use wildcards for the quick search. 


### Advanced Search 

The user has for components and projects the option to use the advanced search if he wants a more refined search. At the advanced search, the user can search for the different attributes projects or components have. For example, the user wants to search for all components which are for Linux; therefore he writes Linux in the field 'Operating System' and click search. For the advanced search, the search result does not depend on the setting the user has chosen at the loading selection.

### Export Spreadsheet

With the Export Spreadsheet button at the bottom of the site, users can export the search result as a xlsx file (Excel). He can choose between a file with 'only components' or 'components with releases'. If he chooses 'only components' he gets a file with just the Components and its attributes. If the user chooses the option 'with release', he will get all the release of the components with their attributes, for example the clearing state of releases, in the xlsx file.

![Export-Spreadsheet](https://github.com/eclipse/sw360/wiki/images/Export-Spreadsheet.png)
 

