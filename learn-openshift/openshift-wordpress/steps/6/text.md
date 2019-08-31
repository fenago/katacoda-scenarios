This indicates that our application should work now. Let's see what URL it was exposed through and try to access it via a web browser:


`oc get route`{{execute}}

```
NAME HOST/PORT PATH SERVICES PORT TERMINATION WILDCARD
wordpress wordpress-wp.127.0.0.1.nip.io wordpress 8080 edge/Allow None
```

Once you open your browser and go to wordpress-wp.[[HOST_SUBDOMAIN]]-80-[[KATACODA_HOST]].environments.katacoda.com, the WordPress application should display a configuration page. Choose you favorite language and press continue On the next page, just fill in the fields, as shown here, and click on Install WordPress.