

Now, in the src/main/java/kioto/avro directory, open a file in **vscode** explorer called AvroProducer.java with the contents of Listing 5.4:

```
package kioto.avro;
import ...
public final class AvroProducer {
 /* here the Constructor code in Listing 5.3 */

 public final class AvroProducer {

  private final Producer<String, GenericRecord> producer;
  private Schema schema;

  public AvroProducer(String brokers, String schemaRegistryUrl) {
    Properties props = new Properties();
    props.put("bootstrap.servers", brokers);
    props.put("key.serializer", StringSerializer.class);
    props.put("value.serializer", KafkaAvroSerializer.class);
    props.put("schema.registry.url", schemaRegistryUrl);
    producer = new KafkaProducer<>(props);
    try {
      schema = (new Parser()).parse(new                   
      File("src/main/resources/healthcheck.avsc"));
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  public final void produce(int ratePerSecond) {
    long waitTimeBetweenIterationsMs = 1000L / (long)ratePerSecond;
    Faker faker = new Faker();

    while(true) {
      HealthCheck fakeHealthCheck =
          new HealthCheck(
              "HEALTH_CHECK",
              faker.address().city(),
              faker.bothify("??##-??##", true),
              Constants.machineType.values()                                                                                                                 
              [faker.number().numberBetween(0,4)].toString(),
              Constants.machineStatus.values()                                        
              [faker.number().numberBetween(0,3)].toString(),
              faker.date().past(100, TimeUnit.DAYS),
              faker.number().numberBetween(100L, 0L),
              faker.internet().ipV4Address());
              GenericRecordBuilder recordBuilder = new                                       
              GenericRecordBuilder(schema);
              recordBuilder.set("event", fakeHealthCheck.getEvent());
              recordBuilder.set("factory", 
              fakeHealthCheck.getFactory());
              recordBuilder.set("serialNumber",                                          
              fakeHealthCheck.getSerialNumber());
              recordBuilder.set("type", fakeHealthCheck.getType());
              recordBuilder.set("status", fakeHealthCheck.getStatus());
              recordBuilder.set("lastStartedAt",                                      
              fakeHealthCheck.getLastStartedAt().getTime());
              recordBuilder.set("temperature",                                          
              fakeHealthCheck.getTemperature());
              recordBuilder.set("ipAddress",   
              fakeHealthCheck.getIpAddress());
              Record avroHealthCheck = recordBuilder.build();
              Future futureResult = producer.send(new ProducerRecord<>               
              (Constants.getHealthChecksAvroTopic(), avroHealthCheck));
      try {
        Thread.sleep(waitTimeBetweenIterationsMs);
        futureResult.get();
      } catch (InterruptedException | ExecutionException e) {
        e.printStackTrace();
      }
    }
  }

  public static void main( String[] args) {
    new AvroProducer("localhost:9092",                                       
    "http://localhost:8081").produce(2);
  }
}
```

An analysis of the AvroProducer class shows the following:

- In line `//1`, ratePerSecond is the number of messages to send in a 1-second period
- In line `//2`, to simulate repetition, we use an infinite loop (try to avoid this in production)
- In line `//3`, now we can create GenericRecord objects using GenericRecordBuilder
- In line `//4`, we use a Java Future to send the record to the healthchecks-avro topic
- In line `//5`, we wait this time to send messages again
- In line `//6`, we read the result of the Future
- In line `//7`, everything runs on the broker on the localhost in port 9092, and with the Schema Registry running on the localhost in port 8081, sending two messages in an interval of 1 second