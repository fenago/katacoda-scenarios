

`oc new-app --template=example-template -p WEB_SERVER=httpd`{{execute}}

```
--> Deploying template "myproject/example-template" to project myproject

     example-template
     ---------
You chose to deploy httpd
...
<output omitted>
...
    Access your application via route 'example-route-advanced.openshift.example.com' 
    Run 'oc status' to view your app.
```


`curl -H 'Host: example-route-advanced.openshift.example.com' 127.0.0.1`{{execute}}

```
<html><body><h1>It works!</h1></body></html>
```

`curl -IH 'Host: example-route-advanced.openshift.example.com' 127.0.0.1`{{execute}}

That's it—one parameter and you have a different web server deployed for you in a matter of seconds.