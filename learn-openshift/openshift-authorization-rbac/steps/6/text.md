<pre class="file" data-filename="nginx-pod.yml" data-target="replace">
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    role: web
spec:
  containers:
  - name: nginx
    image: nginx
</pre>