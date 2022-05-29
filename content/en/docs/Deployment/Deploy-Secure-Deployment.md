After the basic installation, there are some following steps that should be considered for securing the deployment. The main issue that can be done upfront is the documentation of the involved components:

* Lifearay
* Tomcat
* Couchdb
* Vagrant

For vagrant it is important to understand how to close the provisioning users and not keep default usernames and passwords open.

Then for the applications, the following very first line measure should be considered:

* Change password of Liferay administrator user or check if that is appropriately secure.

* You should check the permissions of the involved users in the user management in Liferay.

* Assign individual passwords for users, also you could force the users to change their passwords at login if you like.

* Besides the general advice to check the deployment instructions for the involved components, it is of particular interest to limit couchdb access from localhost only.

* Also for Tomcat you limit port access from localhost only.

* Do you need the ssh ports open or can you just go to the machine (physically).

* Fix the admin party on couchdb

* Add https access to couchdb

* check that sw360 eyecuting user does not have sudo rights and config files for sw360 are `600` only for the executing user.

Note that the Linux vagrant scripts applies somesecurity measures already on the OS level.