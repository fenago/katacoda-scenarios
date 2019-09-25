Now, in the src/main/java/kioto/custom directory, open a file in **vscode** explorer called `CustomProcessor.java` with the content of Listing 4.16.

```
package kioto.custom;
import ...

public final class CustomProcessor {

  private Consumer<String, HealthCheck> consumer;
  private Producer<String, String> producer;

  public CustomProcessor(String brokers) {
    Properties consumerProps = new Properties();
    consumerProps.put("bootstrap.servers", brokers);
    consumerProps.put("group.id", "healthcheck-processor");
    consumerProps.put("key.deserializer", StringDeserializer.class);
    consumerProps.put("value.deserializer",                        HealthCheckDeserializer.class);
    consumer = new KafkaConsumer<>(consumerProps);
    Properties producerProps = new Properties();
    producerProps.put("bootstrap.servers", brokers);
    producerProps.put("key.serializer", StringSerializer.class);
    producerProps.put("value.serializer", StringSerializer.class);
    producer = new KafkaProducer<>(producerProps);
  }
```

An analysis of the first part of the custom processor class includes the following:

- In the first part, we declare a consumer
- In the second part, we declare a producer


Now, in the src/main/java/kioto/customdirectory, let's complete the `CustomProcessor.java` file with the content of Listing 4.17.

The following is the content of Listing 4.17, CustomProcessor.java (part 2):

```
public final void process() {
    consumer.subscribe(Collections.singletonList(
             Constants.getHealthChecksTopic()));           //1
    while(true) {
      ConsumerRecords records = consumer.poll(Duration.ofSeconds(1L)); //2
      for(Object record : records) {                 //3
        ConsumerRecord it = (ConsumerRecord) record;
        HealthCheck healthCheck = (HealthCheck) it.value(); //4
        LocalDate startDateLocal =healthCheck.getLastStartedAt().toInstant()
                 .atZone(ZoneId.systemDefault()).toLocalDate();         //5
        int uptime =
             Period.between(startDateLocal, LocalDate.now()).getDays();  //6
        Future future =
             producer.send(new ProducerRecord<>(
                              Constants.getUptimesTopic(),
                              healthCheck.getSerialNumber(),
                             String.valueOf(uptime)));                  //7
        try {
          future.get();
        } catch (InterruptedException | ExecutionException e) {
          // deal with the exception
        }
      }
    }
  }
  public static void main( String[] args) {
    new CustomProcessor("localhost:9092").process();
  }
}
```

An analysis of the CustomProcessor process method includes the following:

- In line `//1`, here the consumer is created and subscribed to the source topic. This is a dynamic assignment of the partitions to our customer and join to the customer group.
- In line `//2`, an infinite loop to consume the records, the pool duration is passed as a parameter to the method pool. The customer waits no longer than one second before return.
- In line `//3`, we iterate over the records.
- In line `//4`, the JSON string is deserialized to extract the HealthCheck object.
- In line `//5`, the start time is transformed in format at the current time zone.
- In line `//6`, the uptime is calculated.
- In line `//7`, the uptime is written to the uptimes topic, using the serial number as the key and the uptime as the value. Both values are written as normal strings.
