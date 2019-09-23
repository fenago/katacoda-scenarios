Fetching a schema by its global unique ID
To fetch a schema, you can use the following command:

`curl -X GET http://localhost:8081/schemas/ids/1`{{execute}}

The output should be something like this:

```
{"schema":"{\"type\":\"record\",\"name\":\"HealthCheck\",\"namespace\":\"kioto.avro\",\"fields\":[{\"name\":\"event\",\"type\":\"string\"},{\"name\":\"factory\",\"type\":\"string\"},{\"name\":\"serialNumber\",\"type\":\"string\"},{\"name\":\"type\",\"type\":\"string\"},{\"name\":\"status\",\"type\":\"string\"},{\"name\":\"lastStartedAt\",\"type\":\"long\",\"logicalType\":\"timestamp-millis\"},{\"name\":\"temperature\",\"type\":\"float\"},{\"name\":\"ipAddress\",\"type\":\"string\"}]}"}
```