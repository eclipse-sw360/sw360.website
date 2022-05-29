The sw360 is a markdown based documentation part which is available on every sw360 instance at the footer with the link named "SW360 Docs". It provides the documentation about the sw360 application.

[[screenshots/Screenshot 2021-06-20 at 21.40.27.png]]

[[screenshots/Screenshot 2021-06-20 at 21.41.14.png]]

## Technical Introduction

The format of the documentation is in mkdocs and placed in frontend in the sw360-portlet sub project folder. It is there on the source side. However, when it is built, then the documentation is generated into the resources side.It should be on the portlet project and some path accordingly, but that is technical debt, and right now it is on the resources side. (see https://github.com/eclipse/sw360/issues/1275)

The mkdocs plugin execution, which is used to convert the mkdocs format into html format, is placed in sw360-portlet pom file and the profile tag which will tell whether to add the flag (-Dhelp-docs=true) in the maven command or not, is also placed in this pom file. If the flag is not added or the flag is set to false then mkdocs plugin will not work. Please consider setting the profile variable whene executing your maven build:

```
mvn ... -Dhelp-docs=true
```

The result of the mkdocs plugin will be copied to the resource-server folder (target -> classes -> static -> mkdocs) using maven-resources-plugin which is placed in resource-server pom file. In order to use the mkdocs documentation of sw360, you need to install mkdocs and mkdocs material theme in your system. Then only the flag in the maven command will work.

## Prerequisite: mkdocs

Steps/commands to install mkdocs and mkdocs material theme:
MkDocs is installed as a Python module.

1. Install Python: `sudo apt-get install python3`
2. Install pip: `sudo apt-get install python3-pip`
3. Install Mkdocs: `sudo pip3 install mkdocs`
4. Install Mkdocs Material Theme: `sudo pip3 install mkdocs-material`

For more information, please visit the link to install at http://learn.openwaterfoundation.org/owf-learn-mkdocs/install/

In order to call the sw360docs it is at:

```
https://<sw360hostname>:<sw360port>/resource/mkdocs/index.html
```