Checking whether a schema is already registered under the healthchecks–key subject
To check whether a schema is already registered under the healthchecks-key subject, you can use the following command:

Copy
curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json"\
--data 'our escaped avro data' \
http://localhost:8081/subjects/healthchecks-key
The output should be something like this:

Copy
{"subject":"healthchecks-key","version":3,"id":1}