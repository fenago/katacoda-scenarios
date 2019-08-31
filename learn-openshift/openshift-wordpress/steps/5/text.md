Building a multi-tier application
We explained to you previously how to use templates to deploy simple and multi-tier applications. This allows for deploying complex applications by creating deployment configs and deploying a number of pods, services, and routes. This approach is limited since most of the multi-tier applications need to be built from source code. OpenShift templates allow building applications from source code. The combination of building an application from source code and using templates to deploy and build a multi-tier application is described in this chapter. This is a hands-on chapter that gives you real examples of leveraging OpenShift templates to deploy applications in a production environment. Now it is time to see how to build a WordPress application from source code using MariaDB as a database.

WordPress template
WordPress is a free and open-source Content Management System (CMS) based on PHP and MySQL. We want to demonstrate the Source-to-Image (S2I) build process for WordPress using templates prepared at https://github.com/openshift-evangelists/wordpress-quickstart. This repository contains ready-to-use templates for deploying WordPress on an OpenShift cluster. There are two example templates available in the repository. Let's clone the repository first:


`git clone https://github.com/openshift-evangelists/wordpress-quickstart.git
Cloning into 'wordpress-quickstart'...
remote: Counting objects: 331, done.
remote: Total 331 (delta 0), reused 0 (delta 0), pack-reused 331
Receiving objects: 100% (331/331), 1.07 MiB | 1.96 MiB/s, done.
Resolving deltas: 100% (119/119), done.
We are going to apply the wordpress-quickstart/templates/classic-standalone.json WordPress template. For simplicity, we converted the template from JSON to YAML and removed persistent storage-related entities. We also removed a default value for the APPLICATION_NAME parameter.

Building a WordPress application
First, we want to place the application into a separate namespace:


`oc new-project wp
Now using project "wp" on server "https://openshift.example.com:8443".
First, since it is a new template for us, we want to gather some information regarding available parameters. As was previously described, oc process --parameters can be helpful:


`oc process --parameters -f  wordpress-quickstart/templates/classic-standalone.json

NAME DESCRIPTION GENERATOR VALUE
APPLICATION_NAME The name of the WordPress instance.
QUICKSTART_REPOSITORY_URL The URL of the quickstart Git repository. https://github.com/openshift-evangelists/wordpress-quickstart
WORDPRESS_DEPLOYMENT_STRATEGY Type of the deployment strategy for Wordpress. Recreate
WORDPRESS_MEMORY_LIMIT Amount of memory available to WordPress. 512Mi
DATABASE_MEMORY_LIMIT Amount of memory available to the database. 512Mi
DATABASE_USERNAME The name of the database user. expression user[a-f0-9]{8}
DATABASE_PASSWORD The password for the database user. expression [a-zA-Z0-9]{12}
MYSQL_VERSION The version of the MySQL database. 5.7
PHP_VERSION The version of the PHP builder. 7.0
Notice that only APPLICATION_NAME doesn't have a default value.

Let's build the application from source code by instantiating that template with its APPLICATION_NAME=wordpress:


`oc new-app -f wordpress-quickstart/templates/classic-standalone.json -p APPLICATION_NAME=wordpress`{{execute}}


You may want to check the build logs for WordPress application:


`oc logs bc/wordpress -f`{{execute}}

```
Cloning "https://github.com/openshift-evangelists/wordpress-quickstart" ...
  Commit: 0f5076fbb3c898b77b820571fa30d1293c3ac33b (Update README with details on how to enable WebDav access.)
...
<output omitted>
...
Pushed 9/10 layers, 96% complete
Pushed 10/10 layers, 100% complete
Push successful
After some time, all WordPress pods will be up and running, as shown as follows:
```


`oc get pods`{{execute}}