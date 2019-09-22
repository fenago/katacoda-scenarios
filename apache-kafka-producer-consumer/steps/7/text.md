In this step, we will shutdown. We will also verify that the kafka is not running anymore. `./stop.sh`{{copy}}

#### Verify
We can try publish a message to kafka topic.
`echo "Hello, World" | ~/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic TestTopic > /dev/null`{{copy}}

You should get following message as output. Connection could not be established, broker may not be available.

```
[2019-08-21 16:14:58,029] WARN [Producer clientId=console-producer] Connection to node -1 (localhost/127.0.0.1:9092) could not be established. Broker may not be available. (org.apache.kafka.clients.NetworkClient)
```
