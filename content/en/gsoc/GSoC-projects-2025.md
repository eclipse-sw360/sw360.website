---
linkTitle: "GSoC 2025"
title: "GSoC Idea List - 2025"
Weight: 1
---

{{< blocks/cover image_anchor="top" height="sm" color="primary" >}}
{{< page/header >}}
{{< /blocks/cover >}}

<div class="container l-container--padded">


<div class="row">

<div class="col-12 col-lg-8">


Welcome to the idea page for all GSoC 2025 related information.

- Check https://github.com/eclipse-sw360/sw360/discussions/2868

## Intro

SW360 project has been selected as a mentoring Org with GSoC 2025. Thank you,
Google!

Please see two main resources for finding out more SW360 in general:

- Check https://eclipse.dev/sw360/ and development and deployment section.
- Try to install SW360 from source or your can try the [Docker](https://github.com/eclipse-sw360/sw360/blob/main/docker-compose.yml)

Meetings: Checkout the [Meetings table]({{< relref path="_index.md">}}#meetings-table)

## Interested in Application? - Getting Grip

If you are interested in an application - great! We encourage your application.
So the question is how to get started with the topic, just a few points:

- Check https://eclipse.dev/sw360/docs/ for development and operational guides.
- Check the frontend project for UI: https://github.com/eclipse-sw360/sw360-frontend
- Try to install SW360, either from source or Docker
    - https://github.com/eclipse-sw360/sw360/blob/main/docker-compose.yml
- Read the proposed topics
- Use the mailing list sw360-dev@eclipse.org or contact proposed mentors for
  further steps.
- [Matrix group](https://chat.eclipse.org/#/room/#technology.sw360-general:matrix.eclipse.org)
- [GitHub discussion](https://github.com/eclipse-sw360/sw360/discussions/2868)
- If you are interested in trying to make contributions, see
  [contribution guidelines](https://github.com/eclipse-sw360/sw360/blob/main/CONTRIBUTING.md).

## Mentors

Interested in becoming a mentor? Please reach out to us!

#### Volunteers so far:

- [Akshit Joshi](https://github.com/akshitjoshii)
- [Amrit Kumar Verma](https://github.com/amritkv)
- [Arun Azhakesan](https://github.com/arunazhakesan)
- [Gaurav Mishra](https://github.com/GMishx)
- [Helio Chissini de Castro](https://github.com/heliocastro)
- [Katharina Ettinger](https://github.com/EttingerK)
- [Keerthi BL](https://github.com/keerthi-bl)
- [Rudra Chopra](https://github.com/rudra-superrr)

## Topic Proposals

Please reach out to us to add more proposals for GSoC 2025.

Currently, discussion happening on
https://github.com/eclipse-sw360/sw360/discussions/2868

## Topic Proposals from 2025

1. [License Change Detection](#license-change-detection)
2. [Improve integration with FOSSology](#improve-integration-with-fossology)
3. [Thrift layer removal](#thrift-layer-removal)
4. [Improve tests for all REST API endpoints](#improve-tests-for-all-rest-api-endpoints)
5. [SBOM based recommendation](#sbom-based-recommendation)
6. [Creating Project as a Service](#creating-project-as-a-service)

### License Change Detection

**Goal:** Understand the changes in licensing between two versions of a
software package.

This would be combined effort between SW360 and FOSSology.

As the software evolves in time, so does their licensing. A scenario where a
package (say "mylib-v1.2") was scanned by FOSSology and cleaned by a clearing
team. The new version of the package (say "mylib-v1.5") was released and
uploaded again to FOSSology for clearing. Now, another metric can be generated
showing the files from both packages against the change in licensing per file
(addition, removal, change of license or new file).

This either can be shown in FOSSology itself, but also when doing an initial
scan report (ISR), triggered from SW360. Then it would be very visible for the
requester if there are changes in the new version of the release or not. Also,
the diff could be shown in the CLI files.

It can generate a table like:

| File path        | mylib-v1.2 | mylib-v1.5 |
|:-----------------|:-----------|:-----------|
| path/to/file     | MIT        | MIT        |
| path/to/file2    | MIT,BSD    | MIT        |
| path/to/file3    | GPL-2.0    | GPL-3.0    |
| path/to/new-file |            | BSD        |


| Category               | Rating               |
|:-----------------------|:---------------------|
| Low Hanging Fruit      | **                   |
| Risk/Exploratory       | *                    |
| Fun/Peripheral         | ***                  |
| Core Development       | *                    |
| Project Infrastructure | **                   |
| Project size           | Medium               |
| Preferred contributor  | Student/professional |
| Skills needed          | XML, Java            |
| Contact                | @EttingerK @GMishx   |


### Improve integration with FOSSology

**Goal:** Use extended REST API of FOSSology to improve the "Send to FOSSology"
feature

SW360 already have ways to interact with [FOSSology](https://fossology.org),
however the interaction as of now is very limited. The idea is to expand on
this interaction and make use of extended
[REST API of FOSSology](https://github.com/fossology/fossology/blob/master/src/www/ui/api/documentation/openapiv2.yaml)
and have features like:
* Upload source to FOSSology
* Search and link to existing sources with checksum match
* Reuse previous version of release uploaded/existing in FOSSology
* Provide option to select agents for scanning in FOSSology
* Fetch different kind of reports from FOSSology, not just SPDX

Relevant information:
* FOSSology REST API: https://github.com/fossology/fossology/blob/master/src/www/ui/api/documentation/openapiv2.yaml
* SW360 existing endpoints: `releases/{id}/checkFossologyProcessStatus`
* SW360 existing endpoints: `releases/{id}/triggerFossologyProcess`

| Category               | Rating                      |
|:-----------------------|:----------------------------|
| Low Hanging Fruit      | ***                         |
| Risk/Exploratory       | **                          |
| Fun/Peripheral         | ***                         |
| Core Development       | **                          |
| Project Infrastructure | **                          |
| Project size           | Large                       |
| Preferred contributor  | Student/professional        |
| Skills needed          | Java, REST & HTTP libraries |
| Contact                | @GMishx, @rudra-superrr     |


### Thrift layer removal

**Goal:** Remove thrift layer for communication with Database

Remove thrift layer which is used to interact with DB as it is not required and
makes the installation process of SW360 unnecessarily complex. This change will
help project moving forward with modern architectures like microservices.

| Category               | Rating                         |
|:-----------------------|:-------------------------------|
| Low Hanging Fruit      | *                              |
| Risk/Exploratory       | ***                            |
| Fun/Peripheral         | **                             |
| Core Development       | ***                            |
| Project Infrastructure | **                             |
| Project size           | Large                          |
| Preferred contributor  | Student/professional           |
| Skills needed          | Java, CouchDB                  |
| Contact                | @GMishx @smrutis1 @heliocastro |


### Improve tests for all REST API endpoints

**Goal:** Improve existing tests for all REST API endpoints and write new tests

Write unit and integration tests for all REST API endpoints. This will help in
improving the code quality and make the project more robust.

| Category               | Rating                           |
|:-----------------------|:---------------------------------|
| Low Hanging Fruit      | ***                              |
| Risk/Exploratory       | *                                |
| Fun/Peripheral         | **                               |
| Core Development       | ***                              |
| Project Infrastructure | **                               |
| Project size           | Medium                           |
| Preferred contributor  | Student/professional             |
| Skills needed          | Java, JUnit, REST API            |
| Contact                | @GMishx @heliocastro @keerthi-bl |


### SBOM based recommendation

**Goal:** Recommendation of packages based on SBOM of a project

When a user imports a SBOM file, the tool will share the information about the
cleared & uncleared packages used in that project based on existing knowledge
available in SW360. In addition to that if any package is uncleared,
1. The tool will recommend equivalent package, which is already cleared in
   SW360, which in turn will reduce the project clearing time.
2. If the user still wants to use the same uncleared package, the tool will
   give an estimated time to clear the package as well as the project using
   reports like ISR.

| Category               | Rating               |
|:-----------------------|:---------------------|
| Low Hanging Fruit      | **                   |
| Risk/Exploratory       | *                    |
| Fun/Peripheral         | **                   |
| Core Development       | **                   |
| Project Infrastructure | **                   |
| Project size           | Large                |
| Preferred contributor  | Student/professional |
| Skills needed          | Java, Python, AI/ML  |
| Contact                | @amritkv @GMishx     |


### Creating Project as a Service

**Goal:** Separate out the Project and related modules as a separate
microservice

The idea is to separate the Project related modules as a separate microservice
which can then be customized independently for different organizations while
still reusing the common Component repository.

| Category               | Rating                            |
|:-----------------------|:----------------------------------|
| Low Hanging Fruit      | *                                 |
| Risk/Exploratory       | ***                               |
| Fun/Peripheral         | ***                               |
| Core Development       | *                                 |
| Project Infrastructure | ***                               |
| Project size           | Large                             |
| Preferred contributor  | Student/professional              |
| Skills needed          | Java, Spring, Microservices, REST |
| Contact                | @keerthi-bl @GMishx @heliocastro  |

</div></div></div>
