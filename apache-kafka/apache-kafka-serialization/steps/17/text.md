Let's create a Kafka consumer that we will use to receive the custom input messages.

Now, in order to incorporate the deserializer in our consumer, there are two requisites that all of the Kafka consumers should have: to be a KafkaConsumer, and to set the specific properties, such as those in Listing 4.15.

The following is the content of Listing 4.15, the constructor method for CustomConsumer:

```
import kioto.HealthCheck;
import kioto.serde.HealthCheckDeserializer;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.common.serialization.StringSerializer;
public final class CustomConsumer {
  private Consumer<String, HealthCheck> consumer;
  public CustomConsumer(String brokers) {
    Properties props = new Properties();
    props.put("group.id", "healthcheck-processor");//1
    props.put("bootstrap.servers", brokers);//2
    props.put("key.deserializer", StringDeserializer.class);//3
    props.put("value.deserializer", HealthCheckDeserializer.class); //4
    consumer = new KafkaConsumer<>(props);//5
  }
  ...
}
```

An analysis of the CustomConsumer constructor includes the following:

- In line `//1`, the group ID of our consumer, in this case, healthcheck- processor
- In line `//2`, the list of the brokers where our consumer will be running
- In line `//3`, the deserializer type for the messages' keys; in this case, the keys remains as strings
- In line `//4`, the deserializer type for the messages' values; in this case, the values are HealthChecks
- In line `//5`, with these properties, we build a KafkaConsumer with string keys and HealthChecks values, for example, <String, HealthCheck>
 

For a consumer, we provide deserializers rather than serializers. Although we don't use the key deserializer (because if you remember, it is null), the key deserializer is a mandatory parameter for the consumer specification. On the other hand, we need the deserializer for the value, because we are reading our data in a JSON string; here, we deserialize the object with the custom deserializer. 