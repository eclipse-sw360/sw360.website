# General: Our Versioning and Release Principles

We have the following main principles for versioning and releases. We consider [semantic versioning](http://semver.org/):

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> - MAJOR version when you make incompatible API changes,
> - MINOR version when you add functionality in a backwards-compatible manner, and
> - PATCH version when you make backwards-compatible bug fixes.
>
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

with the following implementation in our project:

### Major Version

* API breaking changes are considered for the upcoming REST API.
* Breaking change is *also* if a migration script is required for the data base.
* Thrift API is not considered a public API anymore.
* Therefore milestones cannot correspond to our versions like `1.4`, `1.5`, etc. anymore: we do not know which feature or issue will cause a version jump according to semantic versioning guidelines.

### Minor Version

* Changes to the thrift API will cause minor version increment.
* Larger new functionality which is backwards compatible, maybe one pull requests or maybe a group of pull requests.
* Minor versions requires also tagging in the repo.

### Patch Level

* Every push (merged pull request) to master shall generate *at least* (not there yet) a new patch level version, in order to allow for (clean) deployments at this level.
* Could e also minor improvements like adding a button with some functionality
* Patch level is not tagged.

## Naming and Meaning of Milestones

* Milestones cannot correspond to versions (releases) anymore, because in general the version designator is determined by the level of change.
* We use milestones as work packages. We see them as work packages from an organizational point of view. However, it is not a milestone to release a version, because - again in general - the version is determined by the level of change.
* However, If the last merged pull quest of a work package, a completing merge: If it is not causing a major or minor version increment, still, this would lead to a minor version increment.

## Technical Implementation

* Plan: The artifacts will be build by travis and stored on aws S3 (not there yet) with patch level version increments, but patch level versions will not lead to a tag in the repo.
* Currently, the versioning is "manual maven based", we look for a cleaner more automated approach.

# Technical: Maven Universe How to make/tag a release⁽¹⁾:

The following information refers to the existing maven-based versioning scheme, as of now we are looking into a system which is not leading to a temporary change in the repo, commit, and then reverting changes.

Let us assume, that we want to tag the version **1.2.0** and that the current version in the pom's is **1.2.0-SNAPSHOT**.

### 0. Work in a clean environment
Especially should all poms be without uncommitted changes. The safe way is to start with:
``` 
$ cd /tmp/
$ git clone https://github.com/eclipse/sw360.git
$ cd sw360portal
``` 

### 1. Write the version of the release into the poms
<pre>
$ mvn versions:set -DnewVersion=<b>1.2.0</b>
$ git add pom.xml \*\*/pom.xml
$ git commit -m "set version to <b>1.2.0</b>"
</pre>
This will actually edit all pom.xml files and change the versions to **1.2.0**, i.e. remove the SNAPSHOT.

### 2. Test the project
<pre>
$ mvn install
</pre>
or even better: use vagrant.

### 3. Create and push the tag
<pre>
$ mvn scm:tag
</pre>
This creates the tag and **pushes it to github**.

### 4. Write the new incremented SNAPSHOT-version into the poms
<pre>
$ mvn versions:set -DnewVersion=<b>1.3.0-SNAPSHOT</b>
$ git add pom.xml \*\*/pom.xml
$ git commit -m "set version to <b>1.3.0-SNAPSHOT</b>"
$ git push origin master
</pre>


--
⁽¹⁾ based on: https://axelfontaine.com/blog/final-nail.html

# How to deploy/distribute binarys
TODO

# How to communicate the new release
TODO

# How to modify the github release page
TODO