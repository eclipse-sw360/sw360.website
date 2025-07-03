---
title: "Release and Versioning"
linkTitle: "Release and Versioning"
weight: 10
description: "Our Versioning and Release Principles"
---

We have the following main principles for versioning and releases. We consider [semantic versioning](http://semver.org/):

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards-compatible manner, and
> - PATCH version when you make backwards-compatible bug fixes or security fixes.
>
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

with the following implementation in our project:

### Major Version

* API breaking changes are considered for the upcoming REST API.
* Breaking change is *also* if a migration script is required for the database.
* Thrift API is not considered a public API anymore.
* Therefore, milestones cannot correspond to our versions like `1.4`, `1.5`, etc. anymore: we do not know which feature
  or issue will cause a version jump according to semantic versioning guidelines.
* While preparing for a new major release, the repository should go into freeze mode:
  * No new features can be merged.
  * No dependency updates.
  * Add decided bug fixes/issues closed.
  * The main branch is stable and tested.
  * **Only exception** for the freeze are security vulnerability fixes.

### Minor Version

* Larger new functionality which is backwards compatible, maybe one pull requests or maybe a group of pull requests.
* New functionality should come with appropriate test cases either in code (unit or functional) or in the
  [TestCases document]({{< relref path="TestCases">}}).
* Minor versions requires also tagging in the repo.

### Patch Level

* Minor improvements which are backwards compatible and does not require a migration (qualifies as a breaking change).
* A group of pull requests updating outdated dependencies (at least a minor version update of dependency).
* Pull request merge which closes a GitHub issue.

### Release code freeze cycle

* **Major release:** A strict code freeze cycle to be followed with an expected release date.
  * During the freeze cycle, no other pull request to be merged unless it fixes/closes decided issue.
  * New test cases can always be merged.
  * Dependencies are frozen at the announcement of expected release date.
  * Exceptions to update a dependency:
    * **Major vulnerability:** Must be updated even if the release date needs to be shifted.
    * **Medium vulnerability:** Test the update, if validated, merge. If it can't be validated in reasonable period, the
      decision on what to do goes to core team.
    * **Minor vulnerability:** Can be merged only if it does not break compatibility, otherwise not be updated.
* **Minor release:** The code freeze can be relaxed and a release date is not expected.
  * No new **major** feature to be added or changed.
  * Minor bug fixes/patches can be merged.
  * Dependencies can be updated.
  * If a dependency update breaks a minor release, a patch release to be created with the fix.
* **Patch release:** No code freeze for patch release.

## Naming and Meaning of Milestones

* We are no longer following milestones in favour of simple semantic versioning.

## Technical Implementation

* Plan: The artifacts will be build by travis and stored on aws S3 (not there yet) with patch level version increments, but patch level versions will not lead to a tag in the repo.
* Currently, the versioning is "manual maven based", we look for a cleaner more automated approach.

# Technical: Maven Universe How to make/tag a release⁽¹⁾:

The following information refers to the existing maven-based versioning scheme, as of now we are looking into a system
which is not leading to a temporary change in the repo, commit, and then reverting changes.

Let us assume, that we want to tag the version **1.2.0** and that the current version in the pom.xml is **1.1.13**.

### 0. Work in a clean environment
Especially all poms should be without uncommitted changes. The safe way is to start with:
```shell
$ cd /tmp/
$ git clone https://github.com/eclipse-sw360/sw360.git
$ cd sw360
``` 

### 1. Write the version of the release into the poms
```shell
$ mvn versions:set -DnewVersion=<b>1.2.0</b>
```
This will actually edit all pom.xml files and change the versions to **1.2.0**.

### 2. Test the project
```shell
$ mvn install
```

### 3. Update the Changelog

After changing the versions in pom files, update the CHANGELOG.md file with the information about the new releases and
add a summary of significant changes since the last release. Following are helper scripts to create the changelog
portions for annotating the authors and commits. Change the `<last_tag>` in scripts to the
[last tag from git](https://github.com/eclipse-sw360/sw360/tags), example: `sw360-9.2.0`.

#### 3.1. Listing authors
```shell
git log --no-merges --format="format:> %an <%ae>" <last_tag>..HEAD | sort --unique --ignore-case > new-authors
```

#### 3.2. Listing feature commits
```shell
git log --no-merges --format="format:* \`%h\` %s" --grep="feat(\\(|:)" --extended-regexp --regexp-ignore-case <last_tag>..HEAD > feature-changelog
```

#### 3.3. Listing correction commits
```shell
git log --no-merges --format="format:* \`%h\` %s" --grep="(hot)?fix(\\(|:)" --extended-regexp --regexp-ignore-case <last_tag>..HEAD > correction-changelog
```

#### 3.4. Listing infra commits
```shell
git log --no-merges --format="format:* \`%h\` %s" --grep="((hot)?fix|feat)(\\(|:)" --extended-regexp --regexp-ignore-case --invert-grep <last_tag>..HEAD > infra-changelog
```

### 4. Create and push the tag
```shell
$ git add pom.xml **/pom.xml
$ git add CHANGELOG.md
$ git commit -sS -m "chore(release): set version to <b>1.2.0</b>"
$ mvn scm:tag
```
This creates the tag and **pushes it to GitHub**.

--
⁽¹⁾ based on: https://axelfontaine.com/blog/final-nail.html
