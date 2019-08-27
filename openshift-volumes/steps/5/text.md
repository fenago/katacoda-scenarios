To complete this step, define a pod called `mywebserverpod` and with that pod define a container called `webserver`, which is based on the official `docker.io/centos/httpd` docker image. We will send request to nginx at this port.

Also, define _volumeMounts_ with name `volume-webroot` and use _mountPath_ as `/var/www/html`. We will also use claim `pvc-web` created in the previous step.

OpenShift finds the claim with the given name and then uses the claim to find the volume to mount.

Create nginx pod by running `oc create -f pod.yaml`{{execute HOST1}}

You can see the name of the pods corresponding to the running containers for this application, by running:
`oc get pods`{{execute HOST1}}

You only have one instance of the application so only one pod will be listed.


Now, we can verify that the server is accessible. First, we will need to get the cluster IP address of our web server:
`oc describe pod mywebserverpod | grep IP:`{{execute}}

And secondly, try to reach it via curl: `curl http://<pod-ip>`{{copy}}