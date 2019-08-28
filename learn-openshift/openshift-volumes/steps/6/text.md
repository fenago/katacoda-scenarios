To create an interactive shell within the same container running the application, you can use the ``oc rsh`` command, by providing the name of the pod.
`oc rsh mywebserverpod`{{execute HOST1}}

From within the interactive shell, set directory to `cd /var/www/html`{{execute HOST1}}

Run this command to create text file inside volume `echo "This file will be persisted" > index.html`{{execute}}

Run `exit`{{execute}} to exit the pod.

Verify `index.html` exists at host path by running `cat /data/volume1/index.html`{{execute HOST1}}.

# Protip
You can also run `oc describe pod mywebserverpod`{{execute HOST1}} to verify volume was mounted successfully.


Now, we can verify that the persistent data written earlier is accessible. First, we will need to get the cluster IP address of our web server:
`oc describe pod mywebserverpod | grep IP:`{{execute}}

And secondly, try to reach it via curl: `curl http://<pod-ip>`{{copy}}