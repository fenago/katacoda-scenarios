

Unlike autoscaling based on CPU utilization, memory-based autoscaling can only be enabled by creating a HorizontalPodAutoscaler from a raw YAML/JSON definition:


`cat hpa-memory.yml`{{execute}}

kind: HorizontalPodAutoscaler
apiVersion: autoscaling/v1
metadata:
  name: hpa-httpd-memory
spec:
  scaleTargetRef:
    apiVersion: v1
    kind: DeploymentConfig
    name: httpd
  minReplicas: 2
  maxReplicas: 4
  metrics:
  - type: Resource
    resource:
      name: memory
      targetAverageUtilization: 10


Let's enable autoscaling now:
`oc create -f hpa-memory.yml`{{execute}}

Give it a minute or two to pick up the metrics from Heapster and you will be able to see how the current memory utilization is different from the target:
`oc get hpa`{{execute}}

NAME      REFERENCE  TARGETS   MINPODS MAXPODS          ... 
hpa-httpd-memory DeploymentConfig/httpd 7% / 10%  2  4  ...
Note
If you run this command right after creation, you will most likely see unknown instead of 7% in the preceding output. This is expected because HorizontalPodAutoscaler usually needs a few minutes to collect sufficient metrics.