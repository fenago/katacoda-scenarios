Updating the compatibility requirements under the healthchecks–value subject
To update the compatibility requirements under the healthchecks-value subject, you can use the following command:

Copy
curl -X PUT -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{"compatibility": "BACKWARD"}' \
http://localhost:8081/config/healthchecks-value
The output should be something like this:

Copy
{"compatibility":"BACKWARD"}