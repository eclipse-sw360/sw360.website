In case you need to use Win7 machines, sw360 can be also installed in a virtual box there too. The project sw360vagrant helps you with that. Please find it here:

https://github.com/sw360/sw360vagrant

You would need the following prerequisites:

* VirtualBox
* Vagrant including proxy-conf module
* PowerShell, at least version 3, because Vagrant since version 2 requires that
* cygwin with curl installed

## Detailed Preparation Info

### VirtualBox

sw360vagrant uses vagrant software from vagrantup.com which works with different virtualization environments. In fact you can also try with VMware or Amazon EC2 services (the latter one is also tested with sw360vagrant), but for the sake of simplicity we are using VirtualBox. VirtualBox can be easily installed on most Linux systems, so we have made best experiences with this. VirtualBox is available at https://virtualbox.org/

### PowerShell 3 or later

Vagrant since version 2 requires MS powershell 3 or later on win systems. While the exact reason for this is unknown at the moment, the powershell 3 or later software can be directly obtained from MS in the downloads section. Because the downloads section tends to change there, a direct link to the powershell update for Win7 does not make sense. Just use the search function for finding the download.

### Vagrant

Vagrant is a remote control for VirtualBox and it can apply scripting inside the virtual machine to, in our case, set the entire SW360 solution up. You will need to check if the latest version of vagrant is actually compatible with the latest version of VirtualBox - at some times, we have experienced hiccups to this regard. Vagrant can be obtained from https://vagrantup.com/

Because the vagrant files make use of proxy settings, in case someone needs to setup a proxy, the module `proxy-conf` needs to be installed in any case (regardless if proxy configuration is needed or not). It can be done with the following command:

`vagrant plugin install vagrant-proxyconf`

### Cygwin

sw360vagrant makes use of shell scripts, so you need a shell to execute them. Cygwin is one solution to run this under Win7, installing Cygwin is a good alternative. The shell scripts download dependencies from the Internet using wget, so you need to also install wget. During its installation, cygwin asks you for installing packages, then you should search and select wget.

## Now do the installation

After having all installed, the sw360vagrant project needs to be downloaded. There is no git checkout needed, just download a snapshot of the archive is enough. In the file `shared/configuration.rb` adjustments can be done referring to your environment (allocated RAM for example). Please do all adjustments before everything else because the different stages use this information at various points.

### downloading dependencies

In a cygwin shell, please execute:

`./download-packages.sh`

This downloads all larger dependencies. This is useful, because you do not want to load all dependencies over and over again when you build the virtual machine.

### create the master virtual image file, named 'base box'

In order to create a virtual machine, we create a master virtual machine file, which already contains all relevant dependencies. For doing this, please execute

```
cd generate-box
./generate_box.sh
```

This create the master virtual machine and place it into the vagrant directory of available virtual machine masters.

### install sw360 and start up

After these steps were gone through for one time, change to the directory of the actual setup for the sw360 installation:

```
cd ../sw360-single
```

The above step need to be applied only in the beginning. Again, the reason for making these two steps separate is to have the large dependencies not downloaded at every installation of the sw360. Only with the next step, the vagrant will create a virtual machine for your use to run sw360. in the folder `sw360-single`, execute:

```
vagrant up
```

The reason why this has been called `sw360-single` was that in the early days there were experiments with a multi machine setup. However these plans were not followed later on.

At the end of the terminal output there should be the message from the build system `BUILD SUCCESS`. Above that a list of deployed components shall be visible which should have also a `SUCCESS` remark.

You can now go ahead with the confirguration of liferay, in detail with:

* adjusting user associations
* adjusting password policies
* most important: importing the *.lar files for public and private pages
* import users for testing.

More information is found on the description [how to setup liferay](Deploy-Liferay)

## Old Description (Status of 2016)

If you would like to install the sw360 on Windows on solutions is to use the support project

https://www.github.com/sw360/sw360vagrant

As for Linux and macosx, this project prepares a vagrant box and uses this to install sw360 into a VM derived from the box. The reason for these two stages is that with a prepared box already built, the dependencies are not needed to be downloaded and installed at every deployment. Especially at development, this results in an enormous time savings.

### Preparation

First of all, the scripts of the sw360vagrant will not likely execute. A shell environment needs to be installation. For our case, we have tested this with Cygwin (https://cygwin.com/). So the preparation steps are as follows:

1. Download and install cygwin. In case you are in an enterprise network and have much fun with proxies: The cygwin installer can take your IE settings or have your proxy settings handy.
2. When installing cygwin, make sure that you selct **wget** as this tool is used to download the dependencies.
3. Then as second step you will need to install a git client to download the sw360vagrant project. Alternatively, you could also download the *.zip file from the github page of the current master.
4. Install VirtualBox. Versions such as 4.3.30 or 5.0.18 are used frequently and should be problem free.
5. Install vagrant (https://www.vagrantup.com/) for Virtual box and Windows hosts. Although you will run sw360 on an ubuntu system, please do not be confused, because the ubuntu VM will run as guest and the vagrant download selection refers to the host OS.

In case you have a proxy-ied environment, please not that older versions of vagrant do not support the proxy configuration section. 

### Configuration and Setup of Vagrant

The configuration of the sw360 happens using the file ```shared/configuration.rb```. The following are the most popular settings for installation:

```
# This file will be parsed as Ruby __and__ Bash for configuration puroses. This
# means that it has to be syntactically valid for both
...
# Set this to "true" if you want vagrant to install sw360 automatically
SW360_install=true
# Set this to "true" when working with a network behind a proxy
SW360_proxy=true
SW360_proxy_http="http://yourproxy..."
SW360_proxy_https="https://yourproxy..."
SW360_proxy_bypass="localhost,127.0.0.1"
...
SW360_default_password="sw360fossy-pleasechange"
SW360_admin_name="setup"
...
SW360_vm_name="sw360-single-20160408-cleandemo-2222-8443"
SW360_basebox_name="sw360-trusty"
SW360_vagrant_user="siemagrant"
...
SW360_CPUs=2
SW360_RAM=4096
...
SW360_https_port=8443
...
SW360_gitURL="https://github.com/siemens/sw360portal.git"
...
```
Then, you can go ahead with the ```download-packages.sh``` and ```generate-box/generate_box.sh``` scripting

#### Troubleshooting

When executing the generate_box.sh script you may receive the following error:

```
 Unknown configuration section ‘proxy’.
```

In this case, you will need to install the referring vagrant plugin that adds the missing support for proxy configuration. Enter:

```
vagrant plugin install vagrant-proxyconf
```
In case ruby is not happy downloading this gem, because it complains that it cannot fetch the spec from Hashicorp,  please check the following page for help: https://github.com/mitchellh/vagrant/issues/5966

When executing the generate box part, there might be an error message, complaining about that ```vboxsf``` could not be installed due to a problem with guest additions. That is likely a too old version of VirtualBox. Versions 4.3.36 or 5.0.18 will be certainly fine.

### Start Up and Further Steps

Finally start up with ```vagrant up``` executed in ```sw360-single```. Then you will need to go through the standard vagrant installation steps, which can be seen in the [the readme of the sw360vagrant project](https://github.com/sw360/sw360vagrant/blob/master/README.md).