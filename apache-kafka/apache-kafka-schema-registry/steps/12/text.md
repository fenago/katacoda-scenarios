 Globally updating the compatibility requirements
To globally update the compatibility requirements, you can use the following command:

Copy
curl -X PUT -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{"compatibility": "NONE"}' \
http://localhost:8081/config
The output should be something like this:

Copy
{"compatibility":"NONE"}