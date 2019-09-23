Let's create a Kafka AvroConsumer that we will use to receive the input records. As we already know, there are two prerequisites that all the Kafka Consumers should have: to be a KafkaConsumer and to set specific properties, such as in Listing 5.5:

```
import io.confluent.kafka.serializers.KafkaAvroDeserializer;
import org.apache.avro.generic.GenericRecord;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.common.serialization.StringSerializer;

public final class AvroConsumer {
  private Consumer<String, GenericRecord> consumer; //1
  public AvroConsumer(String brokers, String schemaRegistryUrl) { //2
     Properties props = new Properties();
     props.put("group.id", "healthcheck-processor");
     props.put("bootstrap.servers", brokers);
     props.put("key.deserializer", StringDeserializer.class); //3
     props.put("value.deserializer", KafkaAvroDeserializer.class); //4
     props.put("schema.registry.url", schemaRegistryUrl); //5
     consumer = new KafkaConsumer<>(props); //6
  }
 ...
}
```

An analysis of the changes in the AvroConsumer constructor shows the following:

- In line `//1`, the values now are of type org.apache.avro.generic.GenericRecord
- In line `//2`, the constructor now receives the Schema Registry URL
- In line `//3`, the deserializer type for the messages' keys remains as StringDeserializer
- In line `//4`, the deserializer type for the values is now KafkaAvroDeserializer
- In line `//5`, the Schema Registry URL is added to the consumer properties
- In line `//6`, with these Properties, we build a KafkaConsumer with string keys and GenericRecord values: `<String, GenericRecord>`

It is important to note that when defining the Schema Registry URL for the deserializer to fetch schemas, the messages only contain the schema ID and not the schema itself.