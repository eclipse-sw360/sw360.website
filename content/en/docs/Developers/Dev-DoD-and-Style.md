---
title: "Definition of Done"
linkTitle: "Definition of Done"
weight: 10
description: "The definition of done helps to set a common understanding for solving a ticket."
---

### Policy

* Review points should involve one person from another angle (not just the person you were sitting together with anyways)
* Limit items in review to 5, try to coordinate 
* Using Github assignments to issues or pull requests
* Open review items require conversation

# Definition of Done

* File headers in file OK
  * EPL-2.0 license header
  * Or, if the file is too small, configuration file: license note (see code style)
  * Copyright and author

* Create Branches for sw360
  * Please use conventional branch names for sw360 ([Dev-Branches](https://github.com/eclipse/sw360/wiki/Dev-Branches))

* Avoid (serious) compiler warnings
  * Squash your commits into one or more logical units of work. No dozens of hourly/daily commits in your pull request, please
  * Rebase onto current master so that a fast forward merge is possible
  * That means that merge to master is prepared

* use conventional change log for commit messages ([Dev-Semantic-Commits](https://github.com/eclipse/sw360/wiki/Dev-Semantic-Commits)) <br> For more information please go to https://conventionalcommits.org/ 

* No breaking test
  * Unit testing as it is already present
  * You have more - use them!

* New test
  * For new / added functionality

* Documentation
  * in the Githuib Wiki-Section, if you have done something new
  * At least a technical note for newly added functionality

* Commit style
  * try to squash commits. In the ideal case, a feature is contained in one commit.
  * try to use conventional changelog for commit messages. ([Dev-Semantic-Commits](https://github.com/eclipse/sw360/wiki/Dev-Semantic-Commits))

# Review

Review basically checks for the D-o-D items, in particular

* Code style, not really formatting, but issues like style attributes in HTML tags or exception handling useful
* Design / architecture issues
* Community contribution suitability
* Issue coverage (does it actually solve the problem?)
* Add to commit message of merge commit explicitly:
```
review-by:email@domain.com
```
and
```
tested-by:email@domain.com
```

# Licensing and File Header

All files contributed require headers - this will ensure the license and copyright clearing at the end. Also, all contributions must have the same license as the original source.

If a file has relevant functionality, note that we should move to Eclipse 2.0

```Java
/*
 * Copyright COPYRIGHT HOLDER, 2017.
 * Copyright NEXT COPYRIGHT HOLDER, 2017.
 * Part of the SW360 Portal Project.
 *
 * SPDX-License-Identifier: EPL-1.0
 *
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 */
```
(please adapt comment characters usage)

For small files such as property files, configuration files or standard XML files:

```Bash
# Copyright <COPYRIGHT_HOLDER>, <YEAR>. Part of the SW360 Portal Project.
#
# All rights reserved. This configuration file is provided to you under the
# terms and conditions of the Eclipse Distribution License v1.0 which
# accompanies this distribution, and is available at
# http://www.eclipse.org/org/documents/edl-v10.php
```

# Code style

Just use the standard Java formatting rules of your IDE and **do not reformat** code from others, because you like to correct formatting of other's code.
