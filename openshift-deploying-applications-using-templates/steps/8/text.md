Exporting existing resources as templates
Existing OpenShift resources may be exported as templates by using the oc export command. Let's create a running application using oc new-app command first.

Copy
$ oc new-app httpd
--> Found image 9fd201d (10 days old) in image stream "openshift/httpd" under tag "2.4" for "httpd"
...
<output omitted>
...
--> Success
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose svc/httpd'
    Run 'oc status' to view your app.

$ oc get all
NAME             READY     STATUS    RESTARTS   AGE
httpd-1-dcm2d    1/1       Running   0          2s
httpd-1-deploy   1/1       Running   0          3s
[root@openshift ~]# oc get all
NAME                      REVISION   DESIRED   CURRENT   TRIGGERED BY
deploymentconfigs/httpd   1          1         1         config,image(httpd:2.4)

NAME                 DOCKER REPO                       TAGS      UPDATED
imagestreams/httpd   172.30.1.1:5000/myproject/httpd   2.4

NAME               READY     STATUS    RESTARTS   AGE
po/httpd-1-dcm2d   1/1       Running   0          15s

NAME         DESIRED   CURRENT   READY     AGE
rc/httpd-1   1         1         1         17s

NAME        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
svc/httpd   ClusterIP   172.30.18.224   <none>        8080/TCP,8443/TCP   17s

$ oc export dc,svc,route --as-template=myhttpd > myhttpd_template.yaml
Once the template is created, you can see its contents:

Copy
$ cat myhttpd_template.yaml | head -n 20