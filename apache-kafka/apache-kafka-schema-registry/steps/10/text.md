Checking whether a schema is already registered under the healthchecks–key subject
To check whether a schema is already registered under the healthchecks-key subject, you can use the following command:

```curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json"\
--data 'our escaped avro data' \
http://localhost:8081/subjects/healthchecks-key```{{execute}}


The output should be something like this:
```
{"subject":"healthchecks-key","version":3,"id":1}
```
