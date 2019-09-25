Now, in the src/main/java/kioto/plaindirectory, open a file in **vscode** explorer called `PlainStreamsProcessor.java` with the content shown as follows:

```
import ...
public final class PlainStreamsProcessor {
  private final String brokers;
  public PlainStreamsProcessor(String brokers) {
    super();
    this.brokers = brokers;
  }
  public final void process() {
    // below we will see the contents of this method 
  }
  public static void main(String[] args) {
    (new PlainStreamsProcessor("localhost:9092")).process();
  }
}
```

All the magic happens inside the process() method. The first step in a Kafka Streams application is to get a StreamsBuilder instance, as shown in the following code:

```
StreamsBuilder streamsBuilder = new StreamsBuilder();
```

The StreamsBuilder is an object that allows building a topology. A topology in Kafka Streams is a structural description of a data pipeline. The topology is a succession of steps that involve transformations between streams. A topology is a very important concept in streams; it is also used in other technologies such as Apache Storm.

The StreamsBuilder is used to consume data from a topic. There are other two important concepts in the context of Kafka Streams: a KStream, a representation of a stream of records, and a KTable, a log of the changes in a stream. To obtain a KStream from a topic, we use the stream() method of the StreamsBuilder, shown as follows:

```
KStream healthCheckJsonStream = 
  streamsBuilder.stream( Constants.getHealthChecksTopic(), 
    Consumed.with(Serdes.String(), Serdes.String()));
```

There is an implementation of the stream() method that just receives the topic name as a parameter. But, it is good practice to use the implementation where we can also specify the serializers, as in this example we have to specify the Serializer for the key and the Serializer for the value for the Consumed class; in this case, both are strings.

Don't let the serializers be specified through application-wide properties, because the same Kafka Streams application might read from several data sources with different data formats.

We have obtained a JSON stream. The next step in the topology is to obtain the HealthCheck object stream, and we do so by building the following Stream:

```
KStream healthCheckStream = healthCheckJsonStream.mapValues((v -> {
  try {
    return Constants.getJsonMapper().readValue(
      (String) v, HealthCheck.class);
  } catch (IOException e) {
    // deal with the Exception
  }
 }));
```

First, note that we are using the `mapValues()` method, so as in Java 8, the method receives a lambda expression. There are other implementations for the mapValues() method, but here we are using the lambda with just one argument (v->).

The `mapValues()` here could be read as follows: for each element in the input Stream, we are applying a transformation from the JSON object to the HealthCheck object, and this transformation could raise an IOException, so we are catching it.

Recapitulating until the moment, in the first transformation, we read from the topic a stream with (String, String) pairs. In the second transformation, we go from the value in JSON to the value in `HealthCheck` objects.