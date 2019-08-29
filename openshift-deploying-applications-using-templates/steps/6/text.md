
Processing a template
The following is a real-life example of deploying an application from a predefined template using oc new-app command:

Copy
# oc new-app jenkins-persistent -p JENKINS_SERVICE_NAME=myjenkins
--> Deploying template "openshift/jenkins-persistent" to project myproject
...
<output omitted>
...
--> Creating resources ...
    route "myjenkins" created
    deploymentconfig "myjenkins" created
    serviceaccount "myjenkins" created
    rolebinding "myjenkins_edit" created
    service "jenkins-jnlp" created
    service "myjenkins" created
--> Success
...
<output omitted>
...
    Access your application via route 'myjenkins-myproject.127.0.0.1.nip.io'
    Run 'oc status' to view your app
In the preceding example, we passed the template's name to the command as a parameter; the oc utility can also build an application from the template you specify. The following is the list of objects created by the oc new-app command:

Copy
# oc get all
NAME                         REVISION  DESIRED  CURRENT  TRIGGERED BY
deploymentconfigs/myjenkins  1         1         1       config,image(jenkins:latest)

NAME             HOST/PORT               PATH      SERVICES PORT   TERMINATION 
WILDCARD
routes/myjenkins myjenkins-templates.example.com myjenkins <all>    edge/Redirect 
None

NAME                      READY     STATUS    RESTARTS  AGE
po/myjenkins-1-h2mxx      1/1       Running   0         1m

NAME                      DESIRED   CURRENT   READY     AGE
rc/myjenkins-1            1         1         1         1m

NAME                      CLUSTER-IP     EXTERNAL-IP  PORT(S)    AGE
svc/jenkins-jnlp          172.30.33.180  <none>       50000/TCP  1m
svc/myjenkins             172.30.107.99  <none>       80/TCP     1m
This easy you can create a fully functional jenkins CI/CD application running within OpenShift.

Clean out your project before we proceed:

Copy
# oc delete all --all
deploymentconfig "myjenkins" deleted
route "myjenkins" deleted
pod "myjenkins-1-zg4km" deleted
service "jenkins-jnlp" deleted
service "myjenkins" deleted