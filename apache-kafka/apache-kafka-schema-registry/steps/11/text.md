Getting the top-level compatibility configuration
To get the top level compatibility configuration, you can use the following command:
`curl -X GET http://localhost:8081/config`{{execute}}

The output should be something like this:
```
{"compatibilityLevel":"BACKWARD"}
```