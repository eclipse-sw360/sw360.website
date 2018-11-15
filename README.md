# sw360.website

The website is based on the Hugo static page generator. 
All relevant source files can be found at github/sw360.website (https://github.com/eclipse/sw360.website). 
The page is published at eclipse.org/sw360 and build with a jenkins job, which is configured in a jenkins file in the repository of the website.

If you want to add content to the page, please checkout the git repository (https://github.com/eclipse/sw360.website.git) and add your content.
The page will be build as soon as you push to upstream master. There is also a staging area at the Eclipse Foundation page at staging.eclipse.org/sw360, which is protected by your Eclipse Foundation user credentials and filled with the content that is fund at the staging branch in https://github.com/eclipse/sw360.website. If you want to check out your changes first, just push to the staging branch. The content is published the same way as with the master branch.

The jenkins instance is operated by the Eclipse Foundation and can be found here: https://jenkins.eclipse.org/sw360/job/sw360.website/.
The result of the jenkins build is pushed to: http://git.eclipse.org/c/www.eclipse.org/sw360.git.

The jenkins jobs looks every 15 minutes after changes on the repository. If it detects changes it will start the hugo build and copy the generated static html files to git.eclipse.org. From there another job fetches the files and copies them to the actual static webspace of the Eclipse Foundation.
