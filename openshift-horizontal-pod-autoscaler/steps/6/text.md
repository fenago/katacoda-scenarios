
Login in a separate terminal as system:admin and at some point you should be able to see that you have 4 pods running :
`oc get po`{{execute}}

Once you press Ctrl + C and benchmarking stops, then after a while, the number of pods will go back to normal:
`oc get po`{{execute}}

NAME            READY     STATUS    RESTARTS   AGE
httpd-1-5wsb5   1/1       Running   0          35m
httpd-1-gvqg2   1/1       Running   0          34m
If you are interested, you can see the collected metrics and autoscaling taking place in the web console. Open the webconsolein a browser at https://openshift.example.com:8443/, confirm the security exception for the self-signed certificate, and login with the usernamealiceand any password.

As our OpenShift cluster uses self-signed TLS certificates for encrypting HTTP traffic, Hawkular metrics will not be accessible from the Overview tab of the web console at first—you will see an error above the list of pods instead. To fix this, click on the provided link to open the Hawkular URL in a separate tab/window in your browser and confirm the security exception for the certificate as well. After that, refresh the Overview tab and you will see the calculated metrics for each pod marked with different colors:


You can also use the Monitoring tab to get a more detailed view:


You can clearly see the spikes in CPU load and network traffic that correspond to the ab run. 

We need to delete CPU-based autoscaler before the next exercise:
`oc delete hpa/httpd`{{execute}}