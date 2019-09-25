
In this section we will see how to use all this power gathered together: Apache Avro, Schema Registry, and Kafka Streams.

Now, we are going to use Avro format in our messages, as we did in previous chapters. We consumed this data by configuring the Schema Registry URL and using the Kafka Avro deserializer. For Kafka Streams, we need to use a Serde, so we added the dependency in the Gradle build file, given as follows:

```
compile 'io.confluent:kafka-streams-avro-serde:5.0.0'
```

This dependency has the GenericAvroSerde and specific avroSerde explained in previous chapters. Both Serde implementations allow us to work with Avro records.


Now, in the src/main/java/kioto/avro directory, open a file in **vscode** explorer called AvroStreamsProcessor.java with the contents of Listing 6.4, shown as follows:

```
import ...
public final class AvroStreamsProcessor {
  private final String brokers;
  private final String schemaRegistryUrl;
  public AvroStreamsProcessor(String brokers, String schemaRegistryUrl) {
    super();
    this.brokers = brokers;
    this.schemaRegistryUrl = schemaRegistryUrl;
  }
  public final void process() {
    // below we will see the contents of this method
  }
  public static void main(String[] args) {
    (new AvroStreamsProcessor("localhost:9092", 
        "http://localhost:8081")).process();
  }
}
```

One main difference with the previous code listings is the specification of the Schema Registry URL. The same as before, the magic happens inside the process() method.

The first step in a Kafka Streams Application is to get a StreamsBuilder instance, given as follows:

```
StreamsBuilder streamsBuilder = new StreamsBuilder();
```

The seconds step is to get an instance of the GenericAvroSerdeobject, shown as follows:

```
GenericAvroSerde avroSerde = new GenericAvroSerde();
```

As we are using the GenericAvroSerde, we need to configure it with the Schema Registry URL (as in previous chapters); it is shown in the following code:

```
avroSerde.configure(
  Collections.singletonMap("schema.registry.url", schemaRegistryUrl), false);
```
The configure() method of GenericAvroSerde receives a map as a parameter; as we just need a map with a single entry, we used the singleton map method.

Now, we can create a KStream using this Serde. The following code generates an Avro Stream that contains GenericRecordobjects:

```
KStream avroStream =
  streamsBuilder.stream( Constants.getHealthChecksAvroTopic(),
    Consumed.with(Serdes.String(), avroSerde));
```

Note how we request the name of the AvroTopic, and that we have to specify the serializer for the key and the serializer for the value for the Consumed class; in this case, the key is a String (always null), and the serializer for the value is our new avroSerde.

To deserealize the values for the HealthCheck Stream, we apply the same methods used in previous chapters inside the lambda of the mapValues() method with one argument (v->), shown as follows:

```
KStream healthCheckStream = avroStream.mapValues((v -> {
  GenericRecord healthCheckAvro = (GenericRecord) v;
  HealthCheck healthCheck = new HealthCheck(
    healthCheckAvro.get("event").toString(),
    healthCheckAvro.get("factory").toString(),
    healthCheckAvro.get("serialNumber").toString(),
    healthCheckAvro.get("type").toString(),
    healthCheckAvro.get("status").toString(),
    new Date((Long) healthCheckAvro.get("lastStartedAt")),
    Float.parseFloat(healthCheckAvro.get("temperature").toString()),
    healthCheckAvro.get("ipAddress").toString());
  return healthCheck;
}));
```

And again, the rest of the code of the process() method remains the same as in previous sections, shown as follows:

```
KStream uptimeStream = healthCheckStream.map(((KeyValueMapper)(k, v)-> {
  HealthCheck healthCheck = (HealthCheck) v;
  LocalDate startDateLocal = healthCheck.getLastStartedAt().toInstant()
               .atZone(ZoneId.systemDefault()).toLocalDate();
  int uptime =
     Period.between(startDateLocal, LocalDate.now()).getDays();
  return new KeyValue<>(
     healthCheck.getSerialNumber(), String.valueOf(uptime));
}));

uptimeStream.to( Constants.getUptimesTopic(),
      Produced.with(Serdes.String(), Serdes.String()));

Topology topology = streamsBuilder.build();
Properties props = new Properties();
props.put("bootstrap.servers", this.brokers);
props.put("application.id", "kioto");
KafkaStreams streams = new KafkaStreams(topology, props);
streams.start();
```
