
We can reuse the Serdes built on the previous chapters. The following code creates a KStream that deserializes the values of the messages as HealthCheckobjects.

The StreamsBuilder is used to consume data from a topic. The same as in previous sections, to obtain a KStream from a topic, we use the stream() method of the StreamsBuilder, shown as follows:

```
KStream healthCheckStream =
  streamsBuilder.stream( Constants.getHealthChecksTopic(),
    Consumed.with(Serdes.String(), customSerde));
```

We use the implementation where we can also specify the serializers, as in this example, we have to specify the serializer for the key, and the serializer for the value for the Consumed class, in this case the key is a String (always null), and the serializer for the value is our new customSerde.

The magic here is that the rest of the code of the process() method remains the same as in the previous section; it is also shown as follows:

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
