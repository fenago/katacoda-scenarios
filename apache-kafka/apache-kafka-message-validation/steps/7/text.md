Running the processing engine
The ProcessingEngine class coordinates the Reader and Writer classes. It contains the main method to coordinate them. Create a new file called ProcessingEngine.java in the src/main/java/monedero/directory and copy therein the code in Listing 2.8.

The following is the content of Listing 2.8, ProcessingEngine.java:

```
package monedero;
public class ProcessingEngine {
  public static void main(String[] args) {
    String servers = args[0];
    String groupId = args[1];
    String sourceTopic = args[2];
    String targetTopic = args[3];
    Reader reader = new Reader(servers, groupId, sourceTopic);
    Writer writer = new Writer(servers, targetTopic);
    reader.run(writer);
  }
}
```

Listing 2.8: ProcessingEngine.java

ProcessingEngine receives four arguments from the command line:

- args[0]servers, the host and port of the Kafka broker
- args[1]groupId, the consumer group of the consumer
- args[2]sourceTopic, inputTopic where Reader reads from
- args[3]targetTopic, outputTopic where Writer writes to



In this step, we will shutdown. We will also verify that the kafka is not running anymore. `./stop.sh`{{copy}}




In this step, we will publish a message using kafka. We will also verify that the message is consumed by the client.

#### Publish a message
We can publish a message to kafka topic and consumers can get these messages from the beginning.
`echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TestTopic > /dev/null`{{copy}}

#### Subscribe to a message
We can subscribe to a kafka topic and get messages from the beginning.
`~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic TestTopic --from-beginning`{{copy}}

You should get following message as output. This is the message which we published.
```
Hello, World
```

**Note** Press `Ctrl + C` after receiving the message to quit above script.

#### Verify
We can try publish a message to kafka topic.
`echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TestTopic > /dev/null`{{copy}}

You should get following message as output. Connection could not be established, broker may not be available.

```
[2019-08-21 16:14:58,029] WARN [Producer clientId=console-producer] Connection to node -1 (localhost/127.0.0.1:9092) could not be established. Broker may not be available. (org.apache.kafka.clients.NetworkClient)
```
