---
linkTitle: "Docker Deployment"
title: "Docker Deployment"
weight: 100
description: >
  Deploy SW360 with Docker
---

# A quick how-to for testing SW360

## Requirements

### Platform Requirements

As you need Apache Thrift 0.11.0 (see <https://github.com/eclipse/sw360#required-software> ), using the latest Ubuntu LTS (18.04) won't work, so we start on Ubuntu 19.10 if you want to install from packages. As an alternative, consider the following script from the sw360 repository:

https://github.com/eclipse/sw360/blob/master/scripts/install-thrift.sh

We'll go the Docker way and follow the instructions of the [sw360chores project](https://github.com/sw360/sw360chores). There is a nice diagram there, explaining the rather complex setup.

### sw360chores Requirements

> the perl interpreter to run ./sw360chores.pl

You should already have it in your default, even if minimal, installation

```
$ which perl 
/usr/bin/perl
```

> git which is used in some prepare scripts

`sudo apt install git`

> a current version of docker (min 1.30) \[https://docs.docker.com/\]

```
sudo apt install docker.io
```

> docker-compose (min 1.21) \[https://docs.docker.com/compose/install/\]

```
sudo apt install docker-compose
```

And you actually also need curl,

```
sudo apt install curl
```

### Sw360 Requirements

From the [sw360 Readme](https://github.com/eclipse/sw360#required-software):

> Java 1.8.X

And when they say "1.8.X", they mean it: it won't work with a later version. So it's better to uninstall the potential other versions of Java (/!\\ this is expected to break other things on your environment if you depend on Java for anything), and then install the required version

```
 sudo apt install openjdk-8-jdk openjdk-8-jre
```

> In order to build you will need:
>
> * A git client
> * Apache Maven 3.6.X
> * Apache Thrift 0.11.0

```
sudo apt install maven
```

That will install maven Apache Maven 3.6.1 but you need to have installed the correct version (8) of Java *before hand* otherwise it will install a too recent one.

```
sudo apt install thrift-compiler
```

That will install Thrift version 0.11.0, if you have not installed thrift using the script above.

## Cloning the repos

### Generating an ssh key-pair for your machine

If you don't already have one, generate a key pair with no passphrase, in default location:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Not 100% sure, but not having one may create problems, so...

### Cloning sw360 chores

I created a `code` folder at the root of the user's directory, just to make things simple.

```
~$ cd code
~/code$ git clone https://github.com/sw360/sw360chores.git
```

### Cloning eclipse/sw360

```
~/code$ git clone https://github.com/eclipse/sw360.git
```

## Compiling and deploying SW360 Code

```
~$ cd code/sw360/
~/code/sw360$ mvn package -P deploy -Dbase.deploy.dir=/home/inno3/code/sw360chores/_deploy -DskipTests
```

## Launching the containers

```
$ cd ~/code/sw360chores/
~/code/sw360chores$ ./sw360chores.pl --build -- up
```

And yes, there is a space between `--` and `up`.

If everything goes fine, you should see a line like

```
sw360_1                | 15-Jan-2020 12:33:38.480 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [144,475] milliseconds 
```

You should be able to login at <https://localhost:8443> with the default credentials `setup@sw360.org` and the password `sw360fossy` (found [here](https://github.com/eclipse/sw360/wiki/Deploy-Liferay#liferay-administrator-steps)).

Please go ahead now with the setup of the Liferay - links can be found in the main wiki page.
