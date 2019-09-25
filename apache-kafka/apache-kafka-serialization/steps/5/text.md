As we already know, to build a Kafka Message producer that we use the Java client library, in particular the producer API (in the following chapters, we will see how to use Kafka Streams and KSQL).

The first thing we need is a data source; to make it simple we need to produce our mock data. Each message will be a health message with all of its attributes. The first step is to build a producer to send these messages in JSON format to a topic, as in the example:

```
{"event":"HEALTH_CHECK","factory":"Port Roelborough","serialNumber":"QT89-TZ50","type":"GEOTHERMAL","status":"SHUTTING_DOWN","lastStartedAt":"2018-09-13T00:36:39.079+0000","temperature":28.0,"ipAddress":"235.180.238.3"}

{"event":"HEALTH_CHECK","factory":"Duckburg","serialNumber":"NB49-XL51","type":"NUCLEAR","status":"RUNNING","lastStartedAt":"2018-08-18T05:42:29.648+0000","temperature":49.0,"ipAddress":"42.181.105.188"}
...
```

Let's start by creating a Kafka producer that we will use to send the input messages.

As we already know, there are two requisites that all of the Kafka producers should have: they must be KafkaProducer and have specific properties set, as shown below.
 
The following content, the constructor method for PlainProducer:

```
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.common.serialization.StringSerializer;
public final class PlainProducer {
  private final Producer<String, String> producer;
  public PlainProducer(String brokers) {
    Properties props = new Properties();
    props.put("bootstrap.servers", brokers);                //1
    props.put("key.serializer", StringSerializer.class);    //2
    props.put("value.serializer", StringSerializer.class);  //3
    producer = new KafkaProducer<>(props);                  //4
  }
  ...
}
```

An analysis of the PlainProducer constructor includes the following:

- In line `//1`, the list of the brokers where our producer will be running
- In line `//2`, the serializer type for the messages' keys (we will see serializers later)
- In line `//3`, the serializer type for the messages' values (in this case, the values are strings)
- In line `//4`, with these properties we build a KafkaProducer with string keys and string values, for example,  <String, String>

**Note** that properties behave like a HashMap; in languages such as Kotlin, the properties assignment could be made using the =operator, rather than by calling a method


We are using a string serializer for both keys and values: in this first approach, we will serialize the values to JSON manually using Jackson. We will see later how to write a custom serializer.

Now, in the src/main/java/kioto/plain directory, open a file in **vscode** explorer called PlainProducer.java with the content of Listing 4.7.

The following is the content of Listing 4.7, PlainProducer.java: 

```
package kioto.plain;
import ...
public final class PlainProducer {
  /* here the Constructor code in Listing 4.6 */
  public void produce(int ratePerSecond) {
    long waitTimeBetweenIterationsMs = 1000L / (long)ratePerSecond; //1
    Faker faker = new Faker();
    while(true) { //2
      HealthCheck fakeHealthCheck /* here the code in Listing 4.5 */;
      String fakeHealthCheckJson = null;
      try {
        fakeHealthCheckJson = Constants.getJsonMapper().writeValueAsString(fakeHealthCheck); //3
      } catch (JsonProcessingException e) {
         // deal with the exception
      }
      Future futureResult = producer.send(new ProducerRecord<>
         (Constants.getHealthChecksTopic(), fakeHealthCheckJson)); //4
      try {
        Thread.sleep(waitTimeBetweenIterationsMs); //5
        futureResult.get(); //6
      } catch (InterruptedException | ExecutionException e) {
         // deal with the exception
      }
    }
  }
  public static void main(String[] args) {
    new PlainProducer("localhost:9092").produce(2); //7
  }
}
```

An analysis of the PlainProducer class includes the following:

- In line `//1`, ratePerSecond is the number of messages to send in a one second period
- In line `//2`, to simulate repetition, we use an infinite loop (try to avoid this in production)
- In line `//3`, the code to serialize as JSON a Java POJO
- In line `//4`, we use a Java Future to send the message to HealthChecksTopic
- In line `//5`, we wait this time to send messages again
- In line `//6`, we read the result of the future created previously
- In line `//7`, everything runs on the broker in localhost in port 9092, sending two messages at intervals of one second

It is important to note that here we are sending records without a key; we only specified the value (a JSON string), so the key is null. We are also calling the get() method on the result in order to wait for the write acknowledgment: without that, messages could be sent to Kafka but are lost without our program noticing the failure.