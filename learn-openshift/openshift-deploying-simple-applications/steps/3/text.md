
Now, let's see what happens if we try to create one more pod. Prepare a new pod definition from the one used to create the first pod by replacing nginx with httpd:


<pre class="file" data-filename="httpd-pod.yml" data-target="replace">

</pre>

Advanced deployment
The oc new-app command takes a number of parameters, allowing you to modify the deployment process according to your needs. For example, you may need to modify names, specify environment variables, and so on.

Advanced options can always be displayed by using the built-in help function, which can be displayed by oc new-app --help:


`oc new-app --help`{{execute}}

Create a new application by specifying source code, templates, and/or images


If you provide source code, a new build will be automatically triggered. You can use 'oc status' to
check the progress.

```
Usage:
  oc new-app (IMAGE | IMAGESTREAM | TEMPLATE | PATH | URL ...) [options]

Examples:
  # List all local templates and image streams that can be used to create an app
  oc new-app --list

  # Create an application based on the source code in the current git repository (with a public
remote)
  # and a Docker image
  oc new-app . --docker-image=repo/langimage
```

**Note:**
We are going to work with oc new-appa lot in the following chapters. You don't have to learn all options right now. 

Deploying MariaDB
In this section, we will deploy a database container with additional configuration options. The container requires a number of parameters to be passed to oc new-app. Let's create a simple mariadb container as shown here.

First delete objects created previously:
`oc delete all --all`{{execute}}

...
<OUTPUT OMITTED>
...
Now we want to create a database container where the database user named openshift is allowed to connect to the database named openshift. For simplicity reasons, we will use openshift as the database password. The following example, shows how to start a MariaDB container:


`oc new-app -e MYSQL_USER=openshift -e MYSQL_PASSWORD=openshift \
-e MYSQL_DATABASE=openshift mariadb`{{execute}}


Run `oc status`{{execute}} to view your app.

Verify mariadb is up and running:
`oc get all`{{execute}}

Now login to the container using oc exec:
`oc exec -it mariadb-1-54h6x /bin/bash`{{execute}}


Connect to mariadb database and verify that database named openshift is created and you have access to it running show dababases command.

`mysql -uopenshift -popenshift -h127.0.0.1 openshift`{{execute}}

`show databases;`{{execute}}

...
MariaDB [openshift]> show databases;`{{execute}}
+--------------------+
| Database |
+--------------------+
| information_schema |
| openshift |
| test |
+--------------------+

```

You can exit database and get ready for the next chapter.


`exit`{{execute}}

`exit`{{execute}}


Clear out your lab environment.


`oc delete all --all`{{execute}}


`oc delete project simpleappication`{{execute}}


`oc project myproject`{{execute}}