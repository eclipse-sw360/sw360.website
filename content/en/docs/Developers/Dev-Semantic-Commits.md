## The reason and benefit of semantic commit messages
- automatic generating of the changelog
- simple navigation through git history (e.g. ignoring style changes)

## Semantic commit message structure
`<type>(<scope>): <commit message>`

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
`fix(rest): change maven plugin order to generate the documentation correctly`

`<type>(<scope>): <commit message>`

## Referencing issues
Please reference in the pull request to the open issue

`closes eclipse/sw360#<issue-number>`

`closes eclipse/sw360#758`