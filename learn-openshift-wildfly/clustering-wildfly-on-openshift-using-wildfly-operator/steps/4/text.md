
The standalone XML file must be put in a ConfigMap that is available to the operator. The standaloneConfigMap must provide the name of this ConfigMap as well as the key corresponding to the name of standalone XML file.

Pick up the standalone-openshift.xml from the config folder and create a ConfigMap with:
`kubectl create configmap clusterbench-config-map --from-file config/standalone-openshift.xml`{{execute}}

Now, we will add the Custom Resource Definition, which is available in the crds folder:
`kubectl apply -f crds/clusterbench.yaml`{{execute}}

Great! The cluster has been created. As you can see from the CRD, the clusterbench.yaml file will start 2 Pods in Cluster:

```
apiVersion: wildfly.org/v1alpha1
kind: WildFlyServer
metadata:
  name: clusterbench
spec:
  applicationImage: "quay.io/jmesnil/clusterbench-ee7:17.0"
  size: 2
  standaloneConfigMap:
    name: clusterbench-config-map
    key: standalone-openshift.xml
```

This is verified by:
`oc get pods`{{execute}}

```
NAME             READY     STATUS    RESTARTS   AGE
clusterbench-0   1/1       Running   0          3m
clusterbench-1   1/1       Running   0          2m
```

**Note:** Please wait for few seconds to see pods status running.