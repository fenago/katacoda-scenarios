The build process takes some time. During the first phase, you can see a container with -build in its name. This container is deployed from the PHP builder image and is responsible for build operations:
`oc get pod`{{execute}}


After some time, the application will be available. That means that the application's pod should be in a Running state:
`oc get pod`{{execute}}


```
NAME              READY  STATUS     RESTARTS  AGE
phpinfo-1-build   0/1    Completed  0         39s
phpinfo-1-h9xt5   1/1    Running    0         4s
```

OpenShift built and deployed the phpinfo application, which is now available by using its service IP. Let's try to access our application using the curl command:
`oc get svc`{{execute}}

```
NAME    CLUSTER-IP    EXTERNAL-IP PORT(S)            AGE
phpinfo **172.30.54.195** <none>      8080/TCP,8443/TCP  1h
```

`curl -s http://<svc-ip>:8080 | head -n 10`{{copy}}


Note
The phpinfo() function displays the PHP configuration as an HTML table.

A summary of the build process can be displayed by running the oc status or oc status -v commands:


`oc status -v`{{execute}}

View details with 'oc describe <resource>/<name>' or list everything with 'oc get all'.
The preceding command shows that deployment #1 has been rolled out. It can also contain some useful information for troubleshooting the build, in case something goes wrong.

There is another way to display build logs with low-level details—using the oc logs command. We need to show the log for the buildconfig (or just bc) entity, which can be displayed, as follows, by using the oc logs bc/phpinfo command:
`oc logs bc/phpinfo`{{execute}}

```
```
Cloning "https://github.com/neoncyrex/phpinfo.git" ...
  Commit: 638030df45052ad1d9300248babe0b141cf5dbed (initial commit)
  Author: vagrant <vagrant@openshift.example.com>
  Date: Sat Jun 2 04:22:59 2018 +0000
---> Installing application source...
=> sourcing 20-copy-config.sh ...
---> 05:00:11 Processing additional arbitrary httpd configuration provided by s2i ...
=> sourcing 00-documentroot.conf ...
=> sourcing 50-mpm-tuning.conf ...
=> sourcing 40-ssl-certs.sh ...
Pushing image 172.30.1.1:5000/phpinfo/phpinfo:latest ...
...
Push successful
```
```

The preceding output gives us some insight into how builds work.