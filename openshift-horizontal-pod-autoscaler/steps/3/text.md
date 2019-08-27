CPU-based autoscaling also requires limit ranges to be set on CPU requests for the pods being scaled, so we can use the LimitRange definition from one of the previous sections.


<pre class="file" data-filename="my-limits.yaml" data-target="replace">
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
        memory: 64Mi
    - type: Container
      min:
        cpu: 50m
        memory: 16Mi
      max:
        cpu: 150m
        memory: 32Mi

</pre>

`oc create -f my-limits.yaml`{{execute}}

Note: Depending on your host machine's CPU, you might have to tweak the values in the file above in order for autoscaling to work, that is why in the listing above they are different than in the beginning of the chapter.