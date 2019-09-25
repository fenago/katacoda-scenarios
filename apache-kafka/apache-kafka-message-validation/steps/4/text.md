
**Note:** Final code was already cloned from github for this scenario. You can just understand the application design and run it using the instructions.

Let's proceed with the first step. Build a Kafka worker that reads individual raw messages from the input-messages topic. We say in the Kafka jargon that a consumer is needed. If you recall, in the first chapter we built a command-line producer to write events to a topic and a command-line consumer to read the events from that topic. Now, we will code the same consumer in Java.

For our project, a consumer is a Java interface that contains all of the necessary behavior for all classes that implement consumers.

Open a file called `Consumer.java` in the src/main/java/monedero/directory:

```
package monedero;
import java.util.Properties;
public interface Consumer {
  static Properties createConfig(String servers, String groupId) {
    Properties config = new Properties();
    config.put("bootstrap.servers", servers);
    config.put("group.id", groupId);
    config.put("enable.auto.commit", "true");
    config.put("auto.commit.interval.ms", "1000");
    config.put("auto.offset.reset", "earliest");
    config.put("session.timeout.ms", "30000");
    config.put("key.deserializer",
        "org.apache.kafka.common.serialization.StringDeserializer");
    config.put("value.deserializer",
        "org.apache.kafka.common.serialization.StringDeserializer");
    return config;
  }
}
```

The consumer interface encapsulates the common behavior of the Kafka consumers. The consumer interface has the createConfig method that sets all of the properties needed by all of the Kafka consumers. Note that the deserializers are of the StringDeserializertype because the Kafka consumer reads Kafka key-value records where the value are of the type string.

Now, open a file in **vscode** explorer called `Reader.java` in the src/main/java/monedero/directory:

```
package monedero;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import java.time.Duration;
import java.util.Collections;
class Reader implements Consumer {
  private final KafkaConsumer<String, String> consumer;//1
  private final String topic;
  Reader(String servers, String groupId, String topic) {
    this.consumer =
        new KafkaConsumer<>(Consumer.createConfig(servers, groupId));
    this.topic = topic;
  }
  void run(Producer producer) {
    this.consumer.subscribe(Collections.singletonList(this.topic));//2
 while (true) {//3
      ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));  //4
      for (ConsumerRecord<String, String> record : records) {
producer.process(record.value());//5
      }
    }
  }
}
```

The Reader class implements the consumer interface. So, Reader is a Kafka consumer:

- In line `//1`, <String, String> says that KafkaConsumer reads Kafka records where the key and value are both of the type string
- In line `//2`, the consumer subscribes to the Kafka topic specified in its constructor
- In line `//3`, there is a while(true) infinite loop for demonstrative purposes; in practice, we need to deal with more robust code maybe, implementing Runnable
- In line `//4`, this consumer will be pooling data from the specified topics every 100 milliseconds
- In line `//5`, the consumer sends the message to be processed by the producer

This consumer reads all of the messages from the specified Kafka topic and sends them to the process method of the specified producer. All of the configuration properties are specified in the consumer interface, but specifically the groupId property is important because it associates the consumer with a specific consumer group.

The consumer group is useful when we need to share the topic's events across all of the group's members. Consumer groups are also used to group or isolate different instances.