We will follow the instructions contained in https://operatorhub.io/operator/wildfly

So at first install the Operator Lifecycle Manager (OLM), which is a tool to help manage the Operators running on your cluster.

`curl -sL https://github.com/operator-framework/operator-lifecycle-manager/releases/download/0.10.0/install.sh | bash -s 0.10.0`{{execute}}

Then, we can install WildFly Operator itself by running kubectl against WildFly's Operator YAML file:
`kubectl create -f https://operatorhub.io/install/wildfly.yaml`{{execute}}

After installing, verify that the Operator is listed in your resources with:

`kubectl get csv -n operators`{{execute}}

``` 
NAME                      DISPLAY   VERSION   REPLACES                  PHASE
wildfly-operator.v0.2.0   WildFly   0.2.0     wildfly-operator.v0.1.0   Succeeded
```

So from now, you have a Custom Resource Definition named WildFlyServer which can be used to deliver new instances of WildFly Application Server. At minimum, you can provide an application image to it and it will be built on the top of WildFly:

```
apiVersion: wildfly.org/v1alpha1
kind: WildFlyServer
metadata:
  name: quickstart
spec:
  applicationImage: 'quay.io/jmesnil/wildfly-operator-quickstart:16.0'
  size: 1
```

Notice the parameter `applicationImage` which refererences a Docker Image and size which is the number of Pods that will be started with that Image.

Let's see now a more complex example which involves a custom WildFly configuration to be loaded by the Operator.