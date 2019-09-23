Our Reader invokes the process() method; this method belonging to the Producer class. As with the consumer interface, the producer interface encapsulates all of the common behavior of the Kafka producers. The two producers in this chapter implement this producer interface.

Open a file called `Producer.java`, located in the src/main/java/monedero directory using vscode explorer:

```
package monedero;
import java.util.Properties;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
public interface Producer {
  void process(String message);                                 //1
  static void write(KafkaProducer<String, String> producer,
                    String topic, String message) {             //2
    ProducerRecord<String, String> pr = new ProducerRecord<>(topic, message);
    producer.send(pr);
  }
  static Properties createConfig(String servers) {              //3
    Properties config = new Properties();
    config.put("bootstrap.servers", servers);
    config.put("acks", "all");
    config.put("retries", 0);
    config.put("batch.size", 1000);
    config.put("linger.ms", 1);
    config.put("key.serializer",
"org.apache.kafka.common.serialization.StringSerializer");
config.put("value.serializer",
        "org.apache.kafka.common.serialization.StringSerializer"); 
         return config;
}
}
```

The producer interface has the following observations:

- An abstract method called process invoked in the Reader class
- A static method called write that sends a message to the producer in the specified topic
- A static method called createConfig, where it sets all of the properties required for a generic producer