Getting the top-level compatibility configuration
To get the top level compatibility configuration, you can use the following command:

Copy
curl -X GET http://localhost:8081/config
The output should be something like this:

Copy
{"compatibilityLevel":"BACKWARD"}