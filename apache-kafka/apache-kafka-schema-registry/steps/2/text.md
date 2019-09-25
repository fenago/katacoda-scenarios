The first step is to define the Avro schema. As a reminder, our HealthCheck class looks like Listing 5.1:

```
public final class HealthCheck {
 private String event;
 private String factory;
 private String serialNumber;
 private String type;
 private String status;
 private Date lastStartedAt;
 private float temperature;
 private String ipAddress;
}
```

Now, with the representation of this message in Avro format, the schema (that is, the template) of all the messages of this type in Avro would be Listing 5.2:

```
{
 "name": "HealthCheck",
 "namespace": "kioto.avro",
 "type": "record",
 "fields": [
 { "name": "event", "type": "string" },
 { "name": "factory", "type": "string" },
 { "name": "serialNumber", "type": "string" },
 { "name": "type", "type": "string" },
 { "name": "status", "type": "string"},
 { "name": "lastStartedAt", "type": "long", "logicalType": "timestamp-
    millis"},
 { "name": "temperature", "type": "float" },
 { "name": "ipAddress", "type": "string" }
 ]
}
```

This file must be saved in the kioto project in the src/main/resources directory.

It is important to note that there are the types `string`, `float`, and `double`. But, in the case of Date, it can be stored as a long or as a string.

For this example, we will serializeDate as a long. Avro doesn't have a dedicated Date type; we have to choose between a long and a string (an ISO-8601 string is usually better), but the point with this example is to show how to use different data types.
