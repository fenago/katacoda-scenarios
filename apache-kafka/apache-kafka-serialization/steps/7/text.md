As we already know, to build a Kafka message consumer, we use the Java client library—in particular, the consumer API (in the following chapters, we will see how to use Kafka Streams and KSQL).

Let's create a Kafka consumer that we will use to receive the input messages.

As we already know, there are two requisites that all of the Kafka consumers should have: to be a KafkaConsumer and to set the specific properties, such as  those shown in Listing 4.8.

The following is the content of Listing 4.8, the constructor method for plain consumer:

```
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.common.serialization.StringSerializer;
public final class PlainConsumer {
  private Consumer<String, String> consumer;
  public PlainConsumer(String brokers) {
    Properties props = new Properties();
    props.put("group.id", "healthcheck-processor");         //1
    props.put("bootstrap.servers", brokers);                   //2
    props.put("key.deserializer", StringDeserializer.class);   //3
    props.put("value.deserializer", StringDeserializer.class); //4
    consumer = new KafkaConsumer<>(props);                        //5
  }
  ...
}
```
 

An analysis of the plain consumer constructor includes the following:

- In line `//1`, the group ID of our consumer, in this case, healthcheck-processor
- In line `//2`, the list of brokers where our consumer will be running
- In line `//3`, the deserializer type for the messages' keys (we will see deserializers later)
- In line `//4`, the deserializer type for the messages' values, in this case, values are strings
- In line `//5`, with these properties, we build a KafkaConsumer with string keys and string values

For the customers, we need to provide a group ID to specify the consumer group that our consumer will join.

In the case that multiple consumers are started in parallel, through different threads or through different processes, each consumer will be assigned with a subset of the topic partitions. In our example, we created our topic with four partitions, which means that, to consume the data in parallel, we could create up to four consumers.

For a consumer, we provide deserializers rather than serializers. Although we don't use the key deserializer (because if you remember, it is null), the key deserializer is a mandatory parameter for the consumer specification. On the other hand, we need the deserializer for the value, because we are reading our data in a JSON string, whereas here we deserialize the object manually with Jackson.

