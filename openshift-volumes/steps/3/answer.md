<pre class="file" data-filename="volume-claim.yaml" data-target="replace">
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-web
spec:
  accessModes:
  - ReadWriteOnce 
  resources:
     requests:
       storage: 1Gi
  volumeName: "volume-webroot"
</pre>