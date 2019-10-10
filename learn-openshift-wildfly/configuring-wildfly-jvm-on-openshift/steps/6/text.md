As an alternative, you can define Resource Limits for your whole namespace. For example, the following JSON file defines a set of resource limits:

<pre class="file" data-filename="limits.json" data-target="replace">

apiVersion: "v1"
kind: "LimitRange"
metadata:
  name: "core-resource-limits"
spec:
  limits:
    - type: "Pod"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "200m"
        memory: "6Mi"
    - type: "Container"
      max:
        cpu: "2"
        memory: "1Gi"
      min:
        cpu: "100m"
        memory: "4Mi"
      default:
        cpu: "300m"
        memory: "200Mi"
      defaultRequest:
        cpu: "200m"
        memory: "100Mi"
      maxLimitRequestRatio:
        cpu: "10"
</pre>

Then, you can apply the Resource Limits to a particular project, say "demowildfly":
`oc create -f limits.json -n demowildfly`{{execute}}

Then, you can apply the Resource Limits to a particular project, say "demowildfly":
`oc get LimitRange -n demowildfly`{{execute}}