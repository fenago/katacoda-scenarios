Now, to incorporate the serializer in our producer, there are two requisites that all Kafka producers should fulfill: to be a KafkaProducer, and to set the specific properties, such as Listing 4.12.

The following is the content of Listing 4.12, the constructor method for CustomProducer:

```
import kioto.serde.HealthCheckSerializer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.common.serialization.StringSerializer;
public final class CustomProducer {
  private final Producer<String, HealthCheck> producer;
  public CustomProducer(String brokers) {
    Properties props = new Properties();
    props.put("bootstrap.servers", brokers);                    //1
    props.put("key.serializer", StringSerializer.class);        //2
    props.put("value.serializer", HealthCheckSerializer.class); //3
    producer = new KafkaProducer<>(props);                      //4
  }
```

An analysis of the CustomProducer constructor includes the following:

- In line `//1`, this is the list of the brokers where our producer will be running.
- In line `//2`, the serializer type for the messages' keys in this case keys remains as strings.
- In line `//3`, this is the serializer type for the messages' values,- In this case, the values are HealthCheck.
- In line `//4`, with these properties we build a KafkaProducer with string keys and HealthCheck values.
