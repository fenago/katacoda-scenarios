Now, in the src/main/java/kioto/avro directory, open a file in **vscode** explorer called AvroProcessor.java with the contents of Listing 5.6:

```
package kioto.plain;
import ...
public final class AvroProcessor {
  private Consumer<String, GenericRecord> consumer;
  private Producer<String, String> producer;

  public AvroProcessor(String brokers , String schemaRegistryUrl) {
    Properties consumerProps = new Properties();
    consumerProps.put("bootstrap.servers", brokers);
    consumerProps.put("group.id", "healthcheck-processor");
    consumerProps.put("key.deserializer", StringDeserializer.class);
    consumerProps.put("value.deserializer", KafkaAvroDeserializer.class);
    consumerProps.put("schema.registry.url", schemaRegistryUrl);
    consumer = new KafkaConsumer<>(consumerProps);

    Properties producerProps = new Properties();
    producerProps.put("bootstrap.servers", brokers);
    producerProps.put("key.serializer", StringSerializer.class);
    producerProps.put("value.serializer", StringSerializer.class);
    producer = new KafkaProducer<>(producerProps);
 }
```

An analysis of the first part of the AvroProcessor class shows the following:

In the first section, we declare an AvroConsumer, as in Listing 5.5
In the second section, we declare an AvroProducer, as in Listing 5.4
Now, in the src/main/java/kioto/avro directory, let's complete the AvroProcessor.java file with the contents of Listing 5.7:

```
public final void process() {
  consumer.subscribe(Collections.singletonList(
    Constants.getHealthChecksAvroTopic())); //1
    while(true) {
      ConsumerRecords records = consumer.poll(Duration.ofSeconds(1L));
      for(Object record : records) {
        ConsumerRecord it = (ConsumerRecord) record;
        GenericRecord healthCheckAvro = (GenericRecord) it.value(); //2
        HealthCheck healthCheck = new HealthCheck ( //3
          healthCheckAvro.get("event").toString(),
          healthCheckAvro.get("factory").toString(),
          healthCheckAvro.get("serialNumber").toString(),
          healthCheckAvro.get("type").toString(),
          healthCheckAvro.get("status").toString(),
          new Date((Long)healthCheckAvro.get("lastStartedAt")),
          Float.parseFloat(healthCheckAvro.get("temperature").toString()),
          healthCheckAvro.get("ipAddress").toString());
          LocalDate startDateLocal= 
          healthCheck.getLastStartedAt().toInstant()
                      .atZone(ZoneId.systemDefault()).toLocalDate(); //4
          int uptime = Period.between(startDateLocal,     
          LocalDate.now()).getDays(); //5
          Future future =
               producer.send(new ProducerRecord<>(
                             Constants.getUptimesTopic(),
                             healthCheck.getSerialNumber(),
                             String.valueOf(uptime))); //6
          try {
            future.get();
          } catch (InterruptedException | ExecutionException e) {
            // deal with the exception
          }
        }
      }
    }

    public static void main(String[] args) {
       new      
  AvroProcessor("localhost:9092","http://localhost:8081").process();//7
    }
}
```

An analysis of the AvroProcessor shows the following:

- In line `//1`, the consumer is subscribed to the new Avro topic.
- In line `//2`, we are consuming messages of type GenericRecord.
- In line `//3`, the Avro record is deserialized to extract the HealthCheck object.
- In line `//4`, the start time is transformed into the format in the current time zone.
- In line `//5`, the uptime is calculated.
- In line `//6`, the uptime is written to the uptimes topic, using the serial number as the key and the uptime as the value. Both values are written as normal strings.
- In line `//7`, everything runs on the broker on the localhost in port 9092 and with the Schema Registry running on the localhost in port 8081.
 

As mentioned previously, the code is not type-safe; all the types are checked at runtime. So, be extremely careful with that. For example, the strings are not java.lang.String; they are of type org.apache.avro.util.Utf8. Note that we avoid the cast by calling the toString() method directly on the objects. The rest of the code remains equal.