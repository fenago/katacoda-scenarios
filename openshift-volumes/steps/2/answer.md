<pre class="file" data-filename="volume.yaml" data-target="replace">

apiVersion: v1
kind: PersistentVolume
metadata:
    name: volume-webroot
spec:
    accessModes:
        - ReadWriteOnce
        - ReadWriteMany
        - ReadOnlyMany
    capacity:
        storage: 1Gi
    hostPath:
        path: /data/volume1
    persistentVolumeReclaimPolicy: Recycle
	
</pre>