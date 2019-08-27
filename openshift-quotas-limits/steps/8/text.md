
In this example, we will supply the Nginx web server with our custom configuration file, which will make its default virtual host listen on port 8888 instead of 80. Here's the simple configuration to achieve that:


`cat nginx_custom_default.conf`{{execute}}
server {
    listen       8888;
    server_name  localhost;
    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
}
Now, let's go ahead and create a ConfigMap from this configuration:


`oc create cm nginx --from-file nginx_custom_default.conf`{{execute}}
configmap "nginx" created
If we take a look at the raw resource definition of this ConfigMap, we will see the following:


`oc export configmap/nginx`{{execute}}
apiVersion: v1
data:
 nginx_custom_default.conf: |
    server {
        listen 8888;
        server_name localhost;
        location / {
            root /usr/share/nginx/html;
            index index.html index.htm;
        }
    }
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: nginx


As you can see, the entire contents of the configuration file was inserted as value into the config map definition with the key nginx_custom_default.conf, which can be used to reference the configuration in a pod.