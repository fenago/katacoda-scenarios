In this step, we will talk about REST APIs. It can be used to manage end-user applications, the cluster, and the users of the cluster.

API calls must be authenticated with an access token.

# Task 
To complete this step, get the session token  with the oc whoami command:

`token=$(oc whoami -t)`{{execute}} 

`curl -X GET -H "Authorization: Bearer $token" https://[[HOST_IP]]:8443/oapi/v1/projects --insecure`{{execute}}

# Note:
Above curl command will return project information you created in the earlier step.
 
 
 



When we use the oc command, it makes an API call to the OpenShift cluster using user credentials.

There are three main user types in OpenShift. Let's quickly talk about each of these three types:

Regular users: A regular OpenShift user. Regular users are usually developers with access to OpenShift projects. Regular OpenShift user examples include user1 and user2. 
System users: System OpenShift users are special and most of these users are created when OpenShift is being installed. System user examples are:
system:admin: OpenShift cluster administrator user
system:node:node1.example.com: node1.example.com node user
system:openshift-registry: OpenShift registry user
Service accounts: Special system users associated with projects. Some of these users are created when a new OpenShift project is being created.  
Note
We are going to work with system users and service accounts in the next chapter. In this chapter, we are going to work with regular users.

We can get information about the OpenShift user we are currently logged in as by using the oc whoami command:


`oc whoami`{{execute}}
system:admin
In order to create a regular user, you can use the oc create user command:


`oc create user user1`{{execute}}
user "user1" created
Note
We do not need to set a user password in this lab because our lab environment is set up to accept any password from any user.

By default, the user is going to be created for a project we are currently working on. To get the list of users, use the oc get users command:


`oc get users`{{execute}}
NAME      UID FULL NAME IDENTITIES
developer 46714e6b-2981-11e8-bae6-025000000001 anypassword:developer
user1 473664ec-299d-11e8-bae6-025000000001
We should be able to see two users: developer and user1. 

Note
Developer users are created as a part of the oc cluster up command, as well as the project myproject.    The IDENTITIES field defines the authentication method. In our lab environment setup, the developer user takes anything as a password. This is what anypassword:developer means. 

The last essential things we need to learn is how to switch between different users. We can use the oc login command to do so:


`oc login -u developer`{{execute}}

Logged into "https://127.0.0.1:8443" as "developer" using existing credentials.
You have one project on this server: "myproject"
Using project "myproject".