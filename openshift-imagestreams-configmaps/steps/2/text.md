Log in as an unprivileged user:
`oc login -u alice -p 1234`{{execute}}

```
Username: alice
Password: 1234
Login successful.
```

Note Remember that since this time we didn't configure identity provider explicitly, OpenShift defaults to AllowAll, so we can use any password.

Next, create a dedicated project for our lab:
`oc new-project advanced`{{execute}}

Log in back as system:admin:
`oc login -u system:admin`{{execute}}

Next, we will need to run the following command:
`oc adm policy add-scc-to-user anyuid -z default`{{execute}}


**Note:** We have not discussed the concept behind the command above yet,  it relaxes permissions imposed by OpenShift on pods. The concept is known as Security Context Constraint (SCC) and is discussed more thoroughly in security context scenario.

Finally, log back in as alice:
`oc login -u alice`{{execute}}