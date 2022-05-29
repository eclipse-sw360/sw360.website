## Introduction to Architecture

The SW360 Portal is a software project to build a software management portal according to a preceding requirements engineering effort. This effort has identified the following needs to a software catalogue system:

1. Management of software components for facilitating a component clearing process.
2. Exchanging (usage and adoption) information about software components.
3. Enable software component management as ac ommunity effort in the sense of identifying useful ones against less useful components.

Another main driver for the technology selection was the ability to run the sw360 project as open source development project. This has rules out solution where developers or users are obliged to buy commercially licensed software.

### Background

The entire effort rooted from the component management for license compliance. A project or product needs to track the the used components for license compliance. However, the user involvement at requirements engineering revealed need for the following extensions:

1. For the components management for component clearing there should be also an opportunity to manage more (clearing unrelated) information.
2. Information reuse is in general very important. Information found out by one department should be shared with other department.
3. Last but not least there should be a portal to improve the handling of the license compliance assets.

From the requirements engineering, the following points represent the initial focus of the system:

* A first main area covers to provide information about a software component. As the next section about most named requirements will outline, the main requested information was about software licenses.
* Another main set targeted the ability to share knowledge or analyses about software, such as sharing integration experience. As the requirements outline, this can have many facets, for example, experience with certification of a software component in a regulatory certification effort.
* A large share of requirements covers the idea of supporting a community for software people inside an organisation. Often mentioned was the use case that if a person has contributed to an open source project already in the company, if could be relevant information to know, because other persons in the same company want to communicate with the same open source project can coordinate.

Overall, the described offering appears similar in terms of main interaction scheme to other intranet services, such as a combination of a Wiki or some portal technology of a larger worldwide software company famous for its operating systems. This was also pointed out by several interviewees. However, in addition to the plain Wiki or a Workspace of a portal solution, several software-special attributes and information are demanded that would require own business objects with own business logic.
