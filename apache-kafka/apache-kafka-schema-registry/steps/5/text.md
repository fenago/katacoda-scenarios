Registering a new version of a schema under a – value subject
To register the Avro schema healthcheck.avsc, located in the src/main/resources/path listed in Listing 5.2, using the curl command, we use the following:

```curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
--data '{ "schema": "{ \"name\": \"HealthCheck\", \"namespace\": \"kioto.avro\", \"type\": \"record\", \"fields\": [ { \"name\": \"event\", \"type\": \"string\" }, { \"name\": \"factory\", \"type\": \"string\" }, { \"name\": \"serialNumber\", \"type\": \"string\" }, { \"name\": \"type\", \"type\": \"string\" }, { \"name\": \"status\", \"type\": \"string\"}, { \"name\": \"lastStartedAt\", \"type\": \"long\", \"logicalType\": \"timestamp-millis\"}, { \"name\": \"temperature\", \"type\": \"float\" }, { \"name\": \"ipAddress\", \"type\": \"string\" } ]} " }' \
http://localhost:8081/subjects/healthchecks-avro-value/versions```{{execute}} 

The output should be something like this:

```
{"id":1}
```

This means that we have registered the HealthChecks schema with the version "id":1 (congratulations, your first version).

Note that the command registers the schema on a subject called healthchecks-avro-value. The Schema Registry doesn't have information about topics (we still haven't created the healthchecks-avro topic). It is a convention, followed by the serializers/deserializers, to register schemas under a name following the <topic>-value format. In this case, since the schema is used for the message values, we use the suffix-value. If we wanted to use Avro to identify our messages keys, we would use the <topic>-key format.

For example, to obtain the ID of our schema, we use the following command:

`curl http://localhost:8081/subjects/healthchecks-avro-value/versions/`{{execute}} 

The following output is the schema ID:

```
[1]
```

With the schema ID, to check the value of our schema, we use the following command:

`curl http://localhost:8081/subjects/healthchecks-avro-value/versions/1`{{execute}} 
 

The output is the schema value shown here:

```
{"subject":"healthchecks-avro-value","version":1,"id":1,"schema":"{\"type\":\"record\",\"name\":\"HealthCheck\",\"namespace\":\"kioto.avro\",\"fields\":[{\"name\":\"event\",\"type\":\"string\"},{\"name\":\"factory\",\"type\":\"string\"},{\"name\":\"serialNumber\",\"type\":\"string\"},{\"name\":\"type\",\"type\":\"string\"},{\"name\":\"status\",\"type\":\"string\"},{\"name\":\"lastStartedAt\",\"type\":\"long\",\"logicalType\":\"timestamp-millis\"},{\"name\":\"temperature\",\"type\":\"float\"},{\"name\":\"ipAddress\",\"type\":\"string\"}]}"}
```

