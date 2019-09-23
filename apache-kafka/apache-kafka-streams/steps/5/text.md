
In the third step, we are going to calculate the uptime and send it to the uptimeStream, as shown in the following block:

```
KStream uptimeStream = healthCheckStream.map(((KeyValueMapper)(k, v)-> {
  HealthCheck healthCheck = (HealthCheck) v;
  LocalDate startDateLocal = healthCheck.getLastStartedAt().toInstant()
              .atZone(ZoneId.systemDefault()).toLocalDate();
  int uptime = Period.between(startDateLocal, LocalDate.now()).getDays();
  return new KeyValue<>(
    healthCheck.getSerialNumber(), String.valueOf(uptime));
 }));
```
 

Note that we are using the map() method, also as in Java 8, the method receives a lambda expression. There are other implementations for the map() method; here, we are using a lambda with two arguments ((k, v)->)

The map() here could be read as follows: for each element in the input stream, we extract the tuples (key, value). We are using just the value (anyway, the key is null), cast it to HealthCheck, extract two attributes (the start time and the SerialNumber), calculate the uptime, and return a new KeyValue pair with (SerialNumber, uptime).

The last step is to write these values into the uptimes topic, shown as follows:

```
uptimeStream.to( Constants.getUptimesTopic(), 
  Produced.with(Serdes.String(), Serdes.String()));
Again, I will emphasize it until I get tired: it is widely recommended to declare the data types of our Streams. Always stating, in this case for example, that key value pairs are of type (String, String).
```

Here is a summary of the steps:

- Read from the input topic key value pairs of type (String, String)
- Deserialize each JSON object to `HealthCheck`
- Calculate the uptimes
- Write the `uptimes` to the output topic in key value pairs of type (String, String)

Finally, it is time to start the Kafka Streams engine.

Before starting it, we need to specify the topology and two properties, the broker and the application ID, shown as follows:

```
Topology topology = streamsBuilder.build();
Properties props = new Properties();
props.put("bootstrap.servers", this.brokers);
props.put("application.id", "kioto");
KafkaStreams streams = new KafkaStreams(topology, props);
streams.start();
```

Note that the serializers and deserializers are just explicitly defined when reading from and writing to topics. So, we are not tied application-wide to a single data type, and we can read from and write to topics with different data types, as happens continuously in practice.

Also with this good practice, between different topics, there is no ambiguity about which Serde to use.