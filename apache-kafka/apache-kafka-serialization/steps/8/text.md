Now, in the src/main/java/kioto/plaindirectory, open a file in **vscode** explorer called PlainProcessor.java with the content of Listing 4.9.

The following is the content of Listing 4.9, PlainProcessor.java (part 1):

```
package kioto.plain;
import ...
public final class PlainProcessor {
  private Consumer<String, String> consumer;
  private Producer<String, String> producer;
  public PlainProcessor(String brokers) {
    Properties consumerProps = new Properties();
    consumerProps.put("bootstrap.servers", brokers);
    consumerProps.put("group.id", "healthcheck-processor");
    consumerProps.put("key.deserializer", StringDeserializer.class);
    consumerProps.put("value.deserializer", StringDeserializer.class);
    consumer = new KafkaConsumer<>(consumerProps);
    Properties producerProps = new Properties();
    producerProps.put("bootstrap.servers", brokers);
    producerProps.put("key.serializer", StringSerializer.class);
    producerProps.put("value.serializer", StringSerializer.class);
    producer = new KafkaProducer<>(producerProps);
  }
```

An analysis of the first part of the PlainProcessor class includes the following:

- In the first part, we declare a consumer, as in Listing 4.8
- In the second part, we declare a producer, as in Listing 4.6

Before continuing to write code, let's remember the project requirements for the Kioto stream processing engine.

Putting it all together, the specification is to create a stream engine that does the following:

- Generates messages to a Kafka topic called healthchecks
- Reads messages from the Kafka topic called healthchecks
- Calculates the uptime based on the start up time
- Writes the messages in a Kafka topic called uptimes

This entire process is detailed below, that is, the Kioto stream processing application:

![](https://github.com/fenago/katacoda-scenarios/raw/master/apache-kafka/apache-kafka-serialization/steps/8/1.png)

The messages are generated into HealthChecksTopic, then read, and finally the calculated uptimes are written it in the uptimes topic.
