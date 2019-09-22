As with the consumer interface, an implementation of the producer interface is needed. In this first version, we just pass the incoming messages to another topic without modifying the messages. The implementation code is in Listing 2.7 and should be saved in a file called Writer.java in the src/main/java/m directory.

The following is the content of  Writer.java:

```
package monedero;
import org.apache.kafka.clients.producer.KafkaProducer;
public class Writer implements Producer {
  private final KafkaProducer<String, String> producer;
  private final String topic;
  Writer(String servers, String topic) {
    this.producer = new KafkaProducer<>(
        Producer.createConfig(servers));//1
    this.topic = topic;
  }
  @Override
  public void process(String message) {
    Producer.write(this.producer, this.topic, message);//2
  }
}
```

In this implementation of the Producer class, we see the following: 

- The `createConfig` method is invoked to set the necessary properties from the producer interface
- The process method writes each incoming message in the output topic. As the message arrives from the topic, it is sent to the target topic.

This producer implementation is very simple; it doesn't modify, validate, or enrich the messages. It just writes them to the output topic.