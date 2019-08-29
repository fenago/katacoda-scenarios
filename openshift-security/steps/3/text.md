In this step, you will create PersistentVolumeClaim. We will request storage by creating PersistentVolumeClaim.

# Task
To complete this step, define a PersistentVolumeClaim called `claim1` and define `volumeName` as _volume1_ with `requests` as _storage: "5Gi"_.

Create persistent volume claim which will bound to using volume `volume1` by running `oc create -f volume-claim.yaml`{{execute HOST1}}



Service accounts
Service accounts give us flexibility to control access to API without sharing user’s credentials. In order to show you how it works we need to start the MiniShift VM:

Log in as the privileged user system:admin in order to be able to perform privileged operations, such as adding SCCs and roles:

$ oc login -u system:admin


Another type of user that we will be using is service accounts. They are used by pods and other non-human actors to perform various actions and are a central vehicle by which their access to resources is managed. By default, three service accounts are created in each project:

Name

Description

builder

Used by build pods and assigned the system:image-builder role, which grants push capability into the internal registry to any image stream in the project.

deployer

Used by deploy pods and assigned the system:deployer role, which allows modifying replication controllers in the project.

default

Used by all other pods by default.

 

You can see them by running the following command:


$ oc get serviceaccounts

```
NAME               SECRETS   AGE
builder            2         58s
default            2         58s
deployer           2         58s
```

Each service account is represented by the ServiceAccount resource and is associated with two additional secrets—for access to the OpenShift API and the internal registry:

oc describe serviceaccounts/default

```
Name: default
Namespace: myproject
Labels: <none>
Annotations: <none>
Image pull secrets:    default-dockercfg-wggrl
Mountable secrets:     default-token-mg64x
                       default-dockercfg-wggrl
Tokens:                default-token-7cljg
                       default-token-mg64x
Events:                <none>
```