Summing up what has happened so far, in previous chapters we saw how to make a producer, a consumer, and a simple processor in Kafka. We also saw how to do the same with a custom SerDe, how to use Avro, and the Schema Registry. So far in this chapter, we have seen how to make a simple processor with Kafka Streams.

In this section, we will use all our knowledge so far to build a CustomStreamsProcessor with Kafka Streams to use our own SerDe.

Now, in the src/main/java/kioto/custom directory, open a file in **vscode** explorer called CustomStreamsProcessor.java with the contents of Listing 6.3, shown as follows:

```
import ...
public final class CustomStreamsProcessor {
  private final String brokers;
  public CustomStreamsProcessor(String brokers) {
    super();
    this.brokers = brokers;
  }
  public final void process() {
    // below we will see the contents of this method
  }
  public static void main(String[] args) {
    (new CustomStreamsProcessor("localhost:9092")).process();
  }
}
```

All the magic happens inside the process() method.

The first step in a Kafka Streams application is to get a StreamsBuilder instance, shown as follows:

```
StreamsBuilder streamsBuilder = new StreamsBuilder();
```

We can reuse the Serdes built in the previous chapters. The following code creates a KStream that deserializes the values of the messages as HealthCheckobjects.

```
Serde customSerde = Serdes.serdeFrom(
  new HealthCheckSerializer(), new HealthCheckDeserializer());
```
 
The `serdeFrom()` method of the Serde class dynamically wraps our `HealthCheckSerializer` and `HealthCheckDeserializer` into a single HealthCheck Serde.