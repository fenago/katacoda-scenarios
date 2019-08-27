CPU-based autoscaling also requires limit ranges to be set on CPU requests for the pods being scaled, so we can use the LimitRange definition from one of the previous sections.


`cat my-limits.yaml 
apiVersion: v1
kind: LimitRange
metadata:
  name: my-limits
spec:
  limits:
    - type: Pod
      min:
        cpu: 50m
        memory: 64Mi
      max:
        cpu: 150m
        memory: 128Mi
    - type: Container
      min:
        cpu: 50m
        memory: 64Mi
      max:
        cpu: 150m
        memory: 128Mi

`oc create -f my-limits.yaml
limitrange "my-limits" created
Note
Depending on your host machine's CPU, you might have to tweak the values in the file above in order for autoscaling to work, that is why in the listing above they are different than in the beginning of the chapter.