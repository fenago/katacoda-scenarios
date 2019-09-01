Creating custom roles
If pre-defined roles aren't sufficient for you, you can always create custom roles with just the specific rules you need. Let's create a custom role that can be used instead of the edit role to create and get pods:


`oc login -u system:admin`{{execute}}

`oc create clusterrole alice-project-edit --verb=get,list,watch --resource=namespace,project`{{execute}}


Notice that we had to log in as cluster **administrator** to create a cluster role. A cluster role is required to make its users members of a particular project.

OpenShift's create clusterrole command is limited to creating only one set of resources and verbs, so we couldn't add different verbs for pods. We can work around this limitation by editing the role directly:


`oc edit clusterrole/alice-project-edit`{{execute}}
...
<output omitted>
...
- apiGroups:
  - ""  # DO NOT MISS THIS LINE OR IT IS NOT GOING TO WORK  
  attributeRestrictions: null

  **resources:**
  **- pods**
  verbs:
  - create
  - get
  - list
  - watch

```
clusterrole "alice-project-edit" edited
```


Next, delete the edit role from bob:
`oc adm policy remove-role-from-user edit bob`{{execute}}
Assign the new role to bob:
`oc adm policy add-role-to-user alice-project-edit bob`{{execute}}

Login as bob:
`oc login -u bob`{{execute}}