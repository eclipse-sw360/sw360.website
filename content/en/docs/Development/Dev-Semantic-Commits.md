---
title: "Semantic Commits"
linkTitle: "Semantic Commits"
weight: 10
---

## The reason and benefit of semantic commit messages

- automatic generating of the changelog
- simple navigation through git history (e.g. ignoring style changes)

## Semantic commit message structure

```
<type>(<scope>): <commit message>

Signed-off-by: Name <email address>
```

## The following <types> are supported

- feat (new feature for the user, not a new feature for build script)
- fix (bug fix for the user, not a fix to a build script)
- docs (changes to the documentation)
- style (formatting, missing semi colons, etc; no production code change)
- refactor (refactoring production code, eg. renaming a variable)
- test (adding missing tests, refactoring tests; no production code change)
- chore (updating grunt tasks etc; no production code change)

Example <scope> values:

- ui (user interface)
- rest (REST API)
- thrift (apache thrift services)
- project (project portlet)
- component (component portlet)
- user (user portlet)
- etc.

## Example of semantic commit message

```
fix(rest): change maven plugin order to generate the documentation correctly

Signed-off-by: John Doe <john.doe@example.com>
```

## Referencing issues
Please reference in the pull request to the open issue

`closes eclipse/sw360#<issue-number>`

`closes eclipse/sw360#758`

## Breaking changes
If a commit is introducing a breaking change in a functionality or an endpoint,
it must be documented in the commit message by adding an exclamation `!` after
the commit type. Additional documentation for the break can be added to the
commit footer with a `BREAKING CHANGE:` message.

### Example of commit with breaking change

```
fix(rest)!: migrate health endpoint

BREAKING CHANGE: Move the health endpoint from `/resource/health` to
`/resource/api/health`.

Signed-off-by: John Doe <john.doe@example.com>
```
