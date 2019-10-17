The first S2I lab will use a very simple WildFly application that displays the WildFly configuration using a standard WildFly function—myapp(). It's composed of a single index.wildfly file, with the following content:

#### Create Application
Once ready, open a terminal and at the command prompt, enter the following command to create a Java web application.

`oc new-app --name=myapp wildfly~https://github.com/openshiftdemos/os-sample-java-web.git`{{execute}}

And the output should look something like this:

```
--> Found image 0fe7da4 (4 weeks old) in image stream "wildfly" in project "openshift" under tag "10.0" for "wildfly"

    WildFly 10.0.0.Final
    --------------------
    Platform for building and running JEE applications on WildFly 10.0.0.Final

    Tags: builder, wildfly, wildfly10

    * A source build using source code from https://github.com/openshiftdemos/os-sample-java-web.git will be created
      * The resulting image will be pushed to image stream "myapp:latest"
    * This image will be deployed in deployment config "myapp"
    * Port 8080/tcp will be load balanced by service "myapp"
      * Other containers can access this service through the hostname "myapp"

--> Creating resources with label app=myapp ...
    imagestream "myapp" created
    buildconfig "myapp" created
    deploymentconfig "myapp" created
    service "myapp" created
--> Success
    Build scheduled, use 'oc logs -f bc/myapp' to track its progress.
    Run 'oc status' to view your app.
The --name=myapp names the application. By default it would be the base name of the URL without extension, in our case os-sample-java-web, but it’s much nicer to have the application named myapp and that’s what we did using this switch.
```
