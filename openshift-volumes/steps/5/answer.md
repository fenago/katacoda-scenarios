<pre class="file" data-filename="pod.yaml" data-target="replace">
apiVersion: v1
kind: Pod
metadata:
  name: mywebserverpod
  labels:
    name: webserver
spec:
  containers:
    - name: webserver
      image: docker.io/centos/httpd
      ports:
        - name: web
          containerPort: 80
      volumeMounts:
        - name: volume-webroot
          mountPath: /var/www/html
  volumes:
    - name: volume-webroot
      persistentVolumeClaim:
        claimName: pvc-web
</pre>