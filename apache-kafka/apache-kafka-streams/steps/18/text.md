Now, let's solve the problem of counting how many events are in each window. For this, we will use Kafka Streams. When we do this type of analysis, it is said that we are doing streaming aggregation.

In the src/main/java/kioto/events directory, open a file in **vscode** explorer called `EventProcessor.java` with the contents as shown follows:

```
package kioto.events;
import ...
public final class EventProcessor {
  private final String brokers;
  private EventProcessor(String brokers) {
    this.brokers = brokers;
  }
  private void process() {
    // ...
  }
  public static void main(String[] args) {
    (new EventProcessor("localhost:9092")).process();
  }
}
```

All the processing logic is contained in the process() method. The first step is to create a StreamsBuilder to create the KStream, shown as follows:

```
StreamsBuilder streamsBuilder = new StreamsBuilder();
KStream stream = streamsBuilder.stream(
  "events", Consumed.with(Serdes.String(), Serdes.String()));
```

As we know, we specify from topic we are reading the events in this case is called events, and then we always specify the Serdes, both keys and values of type String.

If you remember, we have each step as a transformation from one stream to another.

The next step is to build a KTable. To do so, we first use the groupBy() function, which receives a key-value pair, and we assign a key called "foo", because it is not relevant but we need to specify one. Then, we apply the windowedBy() function, specifying that the window will be 10 seconds long. Finally, we use the count() function, so we are producing key-value pairs with String as keys and long as values. This number is the count of the events for each window (the key is the window start time):

```
KTable aggregates = stream
  .groupBy( (k, v) -> "foo", Serialized.with(Serdes.String(), Serdes.String()))
  .windowedBy( TimeWindows.of(10000L) )
  .count( Materialized.with( Serdes.String(), Serdes.Long() ) );
```

If you have problems with the conceptual visualization of the KTable, which keys are of type KTable<Windowed<String>> and values are of type long, and printing it (in the KSQL chapter we will see how to do it), would be something like the one, as follows:

```
key | value
 ----------------- |-------
 1532529050000:foo | 10
 1532529060000:foo | 10
 1532529070000:foo | 9
 1532529080000:foo | 3
 ...
```

The key has the window ID and the utility aggregation key with value "foo". The value is the number of elements counted in the window at a specific point of time.

Next, as we need to output the KTable to a topic, we need to convert it to a KStream as follows:

```
aggregates
  .toStream()
  .map( (ws, i) -> new KeyValue( ""+((Windowed)ws).window().start(), ""+i))
  .to("aggregates", Produced.with(Serdes.String(), Serdes.String()));
```

The toStream() method of the KTable returns a KStream. We use a map() function that receives two values, the window and the count, then we extract the window start time as the key and the count as the value. The to() method specifies to which topic we want to output (always specifying the serdes as a good practice).

Finally, as in previous sections, we need to start the topology and the application, shown as follows:

```
Topology topology = streamsBuilder.build();
Properties props = new Properties();
props.put("bootstrap.servers", this.brokers);
props.put("application.id", "kioto");
props.put("auto.offset.reset", "latest");
props.put("commit.interval.ms", 30000);
KafkaStreams streams = new KafkaStreams(topology, props);
streams.start();
```

Remember that the commit.interval.ms property indicates how many milliseconds we will wait to write the results to the aggregates topic.